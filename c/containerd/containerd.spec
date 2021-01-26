%global import_path github.com/containerd/containerd
%global commit ea765aba0d05254012b0b9e595e995c09186427f
%global abbrev %(c=%{commit}; echo ${c:0:8})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:		containerd
Version:	1.3.9
Release:	alt1
Summary:	A daemon to control runC

Group:		Development/Other
License:	Apache-2.0
URL:		https://%import_path

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.service
Source2: %name.init
Source3: %name.limits
Source4: config.toml

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libbtrfs-devel
BuildRequires: libseccomp-devel

Provides: docker-%name = %version-%release
Obsoletes: docker-%name <= 1.0.0

%description
containerd is a daemon to control runC, built for performance and density.
containerd leverages runC's advanced features such as seccomp and user namespace
support as well as checkpoint and restore for cloning and live migration of containers.

%prep
%setup -q

%build
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$PWD"

mkdir -p src/github.com/containerd
ln -rTsf $PWD src/github.com/containerd/containerd
pushd src/github.com/containerd/containerd
make VERSION=v%version REVISION=%commit
popd

%install
mkdir -p -- \
	%buildroot/%_bindir \
	%buildroot/%_initdir \
	%buildroot/%_unitdir \
	%buildroot/%_sysconfdir/sysconfig/limits.d

cp -a -- bin/%name              %buildroot/%_bindir/%name
cp -a -- bin/%name-shim         %buildroot/%_bindir/%name-shim
cp -a -- bin/ctr                %buildroot/%_bindir/%name-ctr
cp -a -- bin/%name-stress       %buildroot/%_bindir/%name-stress
cp -a -- bin/%name-shim-runc-v1 %buildroot/%_bindir/%name-shim-runc-v1
cp -a -- bin/%name-shim-runc-v2 %buildroot/%_bindir/%name-shim-runc-v2

cp -a -- %SOURCE1 %buildroot/%_unitdir/%name.service
cp -a -- %SOURCE2 %buildroot/%_initdir/%name
cp -a -- %SOURCE3 %buildroot/%_sysconfdir/sysconfig/limits.d/%name
install -p -D -m 644 %SOURCE4 %{buildroot}%{_sysconfdir}/%{name}/config.toml

%post
%post_service %name

%preun
%preun_service %name

%files
%config(noreplace) %{_sysconfdir}/%{name}/config.toml
%_sysconfdir/sysconfig/limits.d/%name
%_bindir/*
%_initdir/%name
%_unitdir/%name.service

%changelog
* Fri Jan 22 2021 Alexey Shabalin <shaba@altlinux.org> 1.3.9-alt1
- 1.3.9 (Fixes: CVE-2020-15257)

* Wed Sep 30 2020 Vladimir Didenko <cow@altlinux.org> 1.3.7-alt1
- 1.3.7

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 1.3.6-alt2
- Add previously missed binaries

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 1.3.6-alt1
- 1.3.6

* Fri May 29 2020 Vladimir Didenko <cow@altlinux.org> 1.3.4-alt1
- 1.3.4

* Tue Feb 18 2020 Vladimir Didenko <cow@altlinux.org> 1.3.3-alt1
- 1.3.3
- Fixes CVE-2019-16884
- Fix license name

* Thu Oct 10 2019 Vladimir Didenko <cow@altlinux.org> 1.3.0-alt1
- 1.3.0

* Thu Sep 12 2019 Vladimir Didenko <cow@altlinux.org> 1.2.9-alt1
- 1.2.9

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 1.2.7-alt1
- 1.2.7

* Sat Mar 16 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.5-alt1
- 1.2.5

* Wed Feb 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.3-alt1
- Snapshot of release/1.2 branch
- Fixes CVE-2019-5736.

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- New version (for docker 18.09.1-ce)

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- New version (for docker 18.09.0-ce)

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt1
- New version (for docker 18.06.0-ce)

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- New version (for docker 18.03.1-ce)

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.org> 1.0.2-alt1
- New version (for docker 18.03.0-ce)

* Tue Feb 6 2018 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1.1
- Fix provides/obsoletes

* Tue Feb 6 2018 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- New version (for docker 18.02.0-ce)

* Mon Jan 23 2017 Vladimir Didenko <cow@altlinux.org> 0.2.5-alt1.git2a5e70cb
- New version

* Tue Aug 2 2016 Vladimir Didenko <cow@altlinux.org> 0.2.2-alt1.git0ac3cd1b
- New version

* Mon Apr 25 2016 Alexey Gladkov <legion@altlinux.ru> 0.2.0-alt1.git0e9e24c6
- First build for ALTLinux.
