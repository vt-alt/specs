%global import_path github.com/agola-io/agola
%global commit 375d8ed1683cae01812d56b737d1eeea92221b90

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%define _runtimedir /run

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*


Name:		agola
Version:	0.5.0
Release:	alt3
Summary:	CI/CD redefined

Group:		Development/Other
License:	Apache-2.0
URL:		https://agola.io

Source: %name-%version.tar
Source2: %name.config
Source3: %name.sysconfig
Source4: %name.service

Patch: %name-%version.patch

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: go-bindata

%description
Agola is CI/CD tools.

%prep
%setup -q
%patch -p1

%build

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GO111MODULE=off

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux
export GOFLAGS="-mod=vendor"

%make WEBBUNDLE=1 WEBDISTPATH=dist

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"

mkdir -p -- \
        %buildroot%_bindir \
        %buildroot%_unitdir \
        %buildroot%_sysconfdir/%name \
        %buildroot%_sharedstatedir/%name \

pushd .gopath/src/%import_path

install -p -m 755 bin/agola %buildroot%_bindir/agola
install -p -m 755 bin/agola-toolbox-* %buildroot%_bindir/
install -D -p -m 0644 %SOURCE2 %buildroot%_sysconfdir/%name/config.yml
install -D -p -m 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -D -p -m 0644 %SOURCE4 %buildroot%_unitdir/%name.service

%pre
groupadd -r -f _%name
useradd -r -g _%name -d %_sharedstatedir/%name -s /dev/null -n _%name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md
%_bindir/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.yml
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %attr(770,_%name,_%name) %_sharedstatedir/%name
%_unitdir/%name.service

%changelog
* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 0.5.0-alt3
- fixed description

* Mon Apr 27 2020 Alexey Shabalin <shaba@altlinux.org> 0.5.0-alt2
- cross build toolbox for amd64 arm64 386 arm ppc64le mipsle riscv64
- add config and systemd unit
- useradd agola in %%pre

* Fri Apr 24 2020 Alexey Shabalin <shaba@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Nov 26 2019 Alexey Shabalin <shaba@altlinux.org> 0.4.0-alt1
- 0.4.0

* Mon Sep 16 2019 Alexey Shabalin <shaba@altlinux.org> 0.2.0-alt1
- 0.2.0

* Sun Jul 21 2019 Alexey Shabalin <shaba@altlinux.org> 0.1.1-alt1
- First build for ALTLinux.
