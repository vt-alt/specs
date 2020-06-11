%global import_path github.com/etcd-io/etcd
%global commit 54ba9589114fc3fa5cc36c313550b3c0c0938c91
%global abbrev %(c=%{commit}; echo ${c:0:8})

%define etcd_group etcd
%define etcd_user  etcd

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:    etcd
Version: 3.4.9
Release: alt1
Summary: A highly-available key value store for shared configuration
Group:   System/Servers

URL:     https://etcd.io/
License: Apache-2.0

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
Etcd is a distributed key value store that provides a reliable way to store data
across a cluster of machines. Etcd gracefully handles leader elections during network
partitions and will tolerate machine failure, including the leader.

%prep
%setup -q

for d in client clientv3 contrib etcdctl functional hack; do
mv $d/README.md README-$d.md
done
mv etcdctl/READMEv2.md READMEv2-etcdctl.md

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export LDFLAGS="-X %import_path/version.GitSHA=%abbrev"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%golang_build \
	etcdctl \
	tools/etcd-dump-db \
	tools/etcd-dump-logs \
	tools/etcd-dump-metrics \
#

%install
export BUILDDIR="$PWD/.build"

%golang_install

mkdir -p -- \
	%buildroot%_sbindir \
	%buildroot%_unitdir \
	%buildroot%_sysconfdir/%name \
	%buildroot%_sharedstatedir/%name \
#

mv -f -- %buildroot%_bindir/%name %buildroot%_sbindir/%name

sed \
	-e 's,@USER@,%etcd_user,g' \
	-e 's,@STATEDIR@,%_sharedstatedir/%name,g' \
	-e 's,@SYSCONFDIR@,%_sysconfdir/%name,g' \
	-e 's,@BINDIR@,%_sbindir,g' \
	< rpm/etcd.service > %buildroot%_unitdir/%name.service

install -D -p -m 0644 rpm/etcd.conf    %buildroot%_sysconfdir/%name/%name.conf

# remove unused files
rm -rf -- %buildroot/%_libdir

%pre
groupadd -r -f %etcd_group
useradd -r -g %etcd_group -d /dev/null -s /dev/null -n %etcd_user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md etcd.conf.yml.sample
%doc README-*.md READMEv2-etcdctl.md
%dir %attr(770,%etcd_user,%etcd_group) %_sharedstatedir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%_bindir/*
%_sbindir/*
%_unitdir/%name.service

%changelog
* Fri May 29 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.9-alt1
- 3.4.9.

* Tue Apr 28 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.7-alt2
- add post_service and preun_service.

* Sun Apr 26 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.7-alt1
- 3.4.7.

* Tue Aug 08 2017 Alexey Gladkov <legion@altlinux.ru> 3.2.5-alt1
- First build for ALTLinux.
