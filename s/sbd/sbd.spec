

Name:     sbd
Version:  1.4.1
Release:  alt3

Summary:  Storage-based death
License:  GPLv2+
Group:    System/Servers
Url:      https://github.com/ClusterLabs/sbd.git

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source:   %name-%version.tar
Patch1:   %name-%version.patch

BuildRequires: libaio-devel libpacemaker-devel
BuildRequires: glib2-devel corosync libcorosync-devel libuuid-devel libqb-devel libxml2-devel
BuildRequires: /usr/bin/pod2man

Requires: corosync dlm pacemaker pacemaker-remote

%define _localstatedir %_var

%description
This package contains the storage-based death functionality.

%package tests
Summary:  Storage-based death environment for regression tests
License:  GPLv2+
Group:    System/Servers
Requires: %name = %EVR

%description tests
This package provides an environment + testscripts for
regression-testing sbd.

%package tests-devel
Summary:  Storage-based death environment for regression tests
License:  GPLv2+
Group:    System/Servers
Requires: %name = %EVR

%description tests-devel
This package provides a shared library symlink for
regression-testing sbd.

%prep
%setup
%patch1 -p1

%build
./autogen.sh
%add_optflags -Wall -Werror
%configure
%make_build

%install
%makeinstall_std

rm -rf %buildroot%_libdir/stonith

install -D -m 0755 src/sbd.sh %buildroot/usr/share/sbd/sbd.sh
install -D -m 0755 tests/regressions.sh %buildroot/usr/share/sbd/regressions.sh

install -D -m 0644 src/sbd.service %buildroot%_unitdir/sbd.service
install -D -m 0644 src/sbd_remote.service %buildroot%_unitdir/sbd_remote.service

mkdir -p %buildroot%_sysconfdir/sysconfig
install -m 644 src/sbd.sysconfig %buildroot%_sysconfdir/sysconfig/sbd

# Don't package static libs
find %buildroot -name '*.a' -type f -print0 | xargs -0 rm -f
find %buildroot -name '*.la' -type f -print0 | xargs -0 rm -f

%post
%preun

%files
%config(noreplace) %_sysconfdir/sysconfig/%name
%_sbindir/%name
%_datadir/%name
%exclude %_datadir/%name/regressions.sh
%doc %_man8dir/*
%_unitdir/sbd.service
%_unitdir/sbd_remote.service
%doc COPYING

%files tests
%dir %_datadir/%name
%_datadir/%name/regressions.sh
%_libdir/libsbdtestbed*
%exclude %_libdir/libsbdtestbed.so

%files tests-devel
%_libdir/libsbdtestbed.so

%changelog
* Thu Dec 26 2019 Andrew A. Vasilyev <andy@altlinux.org> 1.4.1-alt3
- add tests-devel package

* Tue Dec 24 2019 Andrew A. Vasilyev <andy@altlinux.org> 1.4.1-alt2
- add Requires for corosync, pacemaker and dlm packages

* Mon Dec 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 1.4.1-alt1
- initial import for ALT

