
Name: libcgroup
Summary: Libraries for allow to control and monitor control groups
Group: System/Libraries
Version: 0.42.2
Release: alt2
License: LGPLv2+
Url: http://libcg.sourceforge.net/
Packager: Alexey Shabalin <shaba@altlinux.ru>
# VCS: https://github.com/libcgroup/libcgroup.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: flex gcc-c++ libpam-devel

%description
Control groups infrastructure.

This library allows applications to manipulate, control, administrate and
monitor control groups and the associated controllers.

%package -n pam_cgroup
Summary: A Pluggable Authentication Module for libcgroup
Group: System/Base
Requires: libcgroup = %version-%release

%description -n pam_cgroup
Linux-PAM module, which allows administrators to classify the user's login
processes to pre-configured control group.

%package -n cgroup
Summary: Tools to control and monitor control groups
Group: System/Configuration/Other
Requires: libcgroup = %version-%release

%description -n cgroup
Control groups infrastructure.

These tools help manipulate, control, administrate and monitor control groups
and the associated controllers.

%package devel
Summary: Development libraries to develop applications that utilize control groups
Group: Development/C
Requires: libcgroup = %version-%release

%description devel
It provides API to create/delete and modify cgroup nodes. It will also in the
future allow creation of persistent configuration for control groups and
provide scripts to manage that configuration.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--enable-initscript-install \
	--enable-pam-module-dir=/%_lib/security \
	--enable-opaque-hierarchy=name=systemd

%make_build

%install
%make DESTDIR=%buildroot install

# install config files
mkdir -p %buildroot%_sysconfdir/sysconfig
cp samples/cgred.conf %buildroot%_sysconfdir/sysconfig/cgred
cp samples/cgconfig.sysconfig %buildroot%_sysconfdir/sysconfig/cgconfig
cp samples/cgconfig.conf %buildroot%_sysconfdir/cgconfig.conf
cp samples/cgrules.conf %buildroot%_sysconfdir/cgrules.conf
cp samples/cgsnapshot_blacklist.conf %buildroot%_sysconfdir/cgsnapshot_blacklist.conf

rm -f %buildroot/%_lib/security/pam_cgroup.la
rm -f %buildroot%_libdir/*.la
rm -f %buildroot%_libdir/libcgroupfortesting.*

mkdir -p %buildroot%_sysconfdir/cgconfig.d
# install unit and sysconfig files
install -d %buildroot%_unitdir
install -m 644 dist/cgconfig.service %buildroot%_unitdir/
install -m 644 cgred.service %buildroot%_unitdir/

%pre -n cgroup
%_sbindir/groupadd -r -f cgred 2> /dev/null ||:

%post -n cgroup
%post_service cgred
%post_service cgconfig

%preun -n cgroup
%preun_service cgred
%preun_service cgconfig

%files
%_libdir/*.so.*

%files -n cgroup
%doc COPYING INSTALL README README_daemon README_systemd
%config(noreplace) %_sysconfdir/sysconfig/cgred
%config(noreplace) %_sysconfdir/sysconfig/cgconfig
%config(noreplace) %_sysconfdir/cgconfig.conf
%config(noreplace) %_sysconfdir/cgrules.conf
%config(noreplace) %_sysconfdir/cgsnapshot_blacklist.conf
%dir %_sysconfdir/cgconfig.d
%attr(2711, root, cgred) %_bindir/cgexec
%attr(2711, root, cgred) %_bindir/cgclassify
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man5dir/*
%_man8dir/*
%config %_initdir/cgconfig
%config %_initdir/cgred
%_unitdir/cgconfig.service
%_unitdir/cgred.service

%files -n pam_cgroup
%_pam_modules_dir/pam_cgroup.so

%files devel
%doc COPYING INSTALL
%_includedir/libcgroup.h
%_includedir/libcgroup
%_libdir/*.so
%_pkgconfigdir/libcgroup.pc

%changelog
* Tue Feb 25 2020 Alexey Shabalin <shaba@altlinux.org> 0.42.2-alt2
- fixed start service (package %%_sysconfdir/cgconfig.d dir)

* Thu Feb 20 2020 Alexey Shabalin <shaba@altlinux.org> 0.42.2-alt1
- 0.42.2

* Wed Aug 28 2019 Alexey Shabalin <shaba@altlinux.org> 0.41-alt3
- backport several upstream fixes (Fixes: CVE-2018-14348)
- set Delegate property for cgconfig service to make sure complete
  cgroup hierarchy is always created by systemd

* Sat Feb 10 2018 Mikhail Efremov <sem@altlinux.org> 0.41-alt2
- Fix parallel build.

* Fri Mar 21 2014 Alexey Shabalin <shaba@altlinux.ru> 0.41-alt1
- 0.41

* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.38.0-alt1
- 0.38 release

* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.38.0-alt0.rc1
- 0.38.rc1
- add systemd unit files

* Thu Aug 18 2011 Alexey Shabalin <shaba@altlinux.ru> 0.37.1-alt3.7f564
- upstream git snapshot 7f5641d9b2e8d073466f0511a17e669438dbaea7

* Thu May 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.37.1-alt2
- fix pid file of cgred service
- ignore systemd hierarchy
- use -avoid-version instead of messing with pam module renaming
- backported from upstream snapshot:
  + Fixed parsing of mount options
  + Fix cgclear to continue unmounting on error

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 0.37.1-alt1
- 0.37.1
- Fix buffer overflow when processing list of controllers from command line (CVE-2011-1006)

* Thu Dec 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.37-alt1
- 0.37
- defined startup_failure in cgconfig init script (ALT #24596)

* Sun Sep 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.36.2-alt3.git20100906
- git snapshot af53a11e8e5f27593f31a34739756d41a08b5416
- fix init scripts
- mount tmpfs to /sys/fs/cgroup from init cgconfig (/sys/fs/cgroup exist in kernel 2.6.35-un-def-alt4.2)

* Thu Aug 26 2010 Alexey Shabalin <shaba@altlinux.ru> 0.36.2-alt2
- change default mount point from /var/run/cgroup/system to /sys/fs/cgroup/system

* Wed Jul 07 2010 Alexey Shabalin <shaba@altlinux.ru> 0.36.2-alt1
- initial build for ALTLinux
