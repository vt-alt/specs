%define _unpackaged_files_terminate_build 1
%define import_path github.com/evilsocket/opensnitch

Name: opensnitch
Version: 1.0.0
Release: alt3.b.git5c8f710
Summary: OpenSnitch is a GNU/Linux port of the Little Snitch application firewall
License: GPLv3
Group: Networking/Other
Url: https://opensnitch.io/

%define _pseudouser_user     _%name
%define _pseudouser_group    _%name
%define _pseudouser_home     %_localstatedir/opensnitchd

# https://github.com/evilsocket/opensnitch.git
Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): rpm-build-python3
BuildRequires: python3
BuildRequires: python3-module-grpcio
BuildRequires: python3-module-grpcio-tools
BuildRequires: python3(pyinotify)
BuildRequires: python3(unicode_slugify)
BuildRequires: python3(PyQt5)
BuildRequires: python3(configparser)
BuildRequires: libnetfilter_queue-devel

%description
OpenSnitch is a GNU/Linux port of the Little Snitch application firewall.

%package daemon
Summary: OpenSnitch is a GNU/Linux port of the Little Snitch application firewall
Group: Networking/Other

%description daemon
OpenSnitch is a GNU/Linux port of the Little Snitch application firewall.

This package contains opensnitch daemon.

%package ui
Summary: OpenSnitch is a GNU/Linux port of the Little Snitch application firewall
Group: Networking/Other
BuildArch: noarch
Requires: %name-daemon = %EVR

%description ui
OpenSnitch is a GNU/Linux port of the Little Snitch application firewall.

This package contains opensnitch ui.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

pushd .build/src/%import_path/daemon
%make_build
popd

%make_build

pushd ui
%python3_build_debug
popd

%install
pushd .build/src/%import_path/daemon
mkdir -p %buildroot%_sysconfdir/opensnitchd/rules
install -m 0755 -D opensnitchd %buildroot%_sbindir/opensnitchd
install -m 0644 -D opensnitchd.service %buildroot%_unitdir/opensnitchd.service
popd

%makeinstall_std

pushd ui
%python3_install
popd

mkdir -p %buildroot%_pseudouser_home

%pre daemon
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'The %name daemon' \
	-d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%preun daemon
%preun_service opensnitchd

%post daemon
%post_service opensnitchd

%files daemon
%doc LICENSE README.md
%dir %_sysconfdir/opensnitchd
%dir %_sysconfdir/opensnitchd/rules
%_sbindir/*
%_unitdir/*
%dir %attr(0770,root,%_pseudouser_group) %_pseudouser_home

%files ui
%_bindir/opensnitch-ui
%_desktopdir/*
%_datadir/kservices5/*
%python3_sitelibdir_noarch/*

%changelog
* Sun May 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt3.b.git5c8f710
- fixed build

* Fri Mar 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2.b.git5c8f710
- Updated to current upstream version (Closes: #36208)

* Fri May 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1.b.gitf71d8ce
- Initial build for ALT.
