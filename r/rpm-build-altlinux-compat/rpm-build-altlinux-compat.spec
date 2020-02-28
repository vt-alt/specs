# NOTE: do not use clean_spec or rpmcs for this spec

Name: rpm-build-altlinux-compat
Version: 2.1.13
Release: alt1

Summary: ALT Linux compatibility and extensions in rpm build

License: GPL
Group: Development/Other
Url: http://wiki.sisyphus.ru/devel/RpmBuildAltlinuxCompat

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://updates.etersoft.ru/pub/Etersoft/Sisyphus/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

# Tune additional rpm macros file placement
%if %_vendor == "alt"
%define macrofilename macros
#ifndef _rpmmacrosdir
%if %{expand:%%{?_rpmmacrosdir:0}%%{!?_rpmmacrosdir:1}}
%define _rpmmacrosdir %_sysconfdir/rpm/macros.d
%endif
# see eterbug #10699 https://bugs.etersoft.ru/show_bug.cgi?id=10699
#BuildPreReq: altlinux-release
%else
# Provide includes macros
Provides: rpm-build-python rpm-build-perl rpm-macros-ttf rpm-build-licenses rpm-macros-cmake
# FreeBSD
%if %_vendor == "portbld" || %_vendor == "any"
%define _rpmmacrosdir /usr/local/etc/rpm
%define macrofilename macros
%else
# in Mandriva for example
%if %{expand:%%{?_sys_macros_dir:1}%%{!?_sys_macros_dir:0}}
%define _rpmmacrosdir %_sys_macros_dir
%define macrofilename 99-altlinux-compat.macros
%else
%define _rpmmacrosdir /etc/rpm
%define macrofilename macros
%endif
%endif

Requires: ed
# ALT has it in rpm, but regular rpm requires define it
BuildRoot: %{_tmppath}/%{name}-%{version}
%endif

Requires: rpm-build

%description
This package contains ALT Linux compatibility layer
and some extensions for rpm build
on various rpm running platforms.

%package -n rpm-build-intro
Summary: New macros for ALT Linux rpm build
Group: Development/Other
Requires: %_rpmmacrosdir
# we will use distr_vendor from it
Requires: rpm-build-compat = %version-%release

%description -n rpm-build-intro
This package contains new macros introduced for
include in ALT Linux rpm build.

If you wish to use these macros, add rpm-build-intro
package to build requires.

%package -n rpm-macros-intro-conflicts
Summary: Conflicts macros for ALT Linux rpm build
Group: Development/Other
Requires: %_rpmmacrosdir
Requires: rpm-build-intro = %version-%release

%description -n rpm-macros-intro-conflicts
This package contains conflicts macros for
use with ALT Linux rpm build.

If you wish to use these macros, add rpm-macros-intro-conflicts
package to build requires.

%package -n rpm-build-compat
Summary: ALT Linux compatibility macros for backport purposes
Group: Development/Other
Requires: %_rpmmacrosdir

%description -n rpm-build-compat
This package contains ALT Linux compatibility layer
for ALT Linux rpm build.
It is useful for backporting packages to previous ALT Linux distros.
Add it to buildrequires when backporting packages.
Command rpmbph from etersoft-build-utils will do it automatically.

%prep
%setup

%install
./install.sh %buildroot %_bindir %_rpmmacrosdir %macrofilename

%if %_vendor == "alt"

%files -n rpm-build-intro
%doc AUTHORS TODO
%_rpmmacrosdir/etersoft-intro

%files -n rpm-macros-intro-conflicts
%doc AUTHORS
%_rpmmacrosdir/etersoft-intro-conflicts

%files -n rpm-build-compat
%doc AUTHORS
%_rpmmacrosdir/compat
%_bindir/distr_vendor

%else

%files
%doc AUTHORS TODO ChangeLog
%_rpmmacrosdir/%macrofilename
%_bindir/add_changelog
%_bindir/stamp_spec
%_bindir/subst
%_bindir/distr_vendor

%endif

%changelog
* Thu May 02 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.13-alt1
- NPROCS: divide by 4 only if we have more than 42G

* Tue Apr 30 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.12-alt1
- add support for python package prefix in py_use macros

* Sat Apr 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.11-alt1
- update python and add python3 macros
- add _pkgdocdir
- resort macros order

* Thu Mar 21 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.10-alt1
- base rpm: add _cachedir

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- introduced _metainfodir (like in Fedora)

* Fri Aug 17 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.8-alt1
- distr_info: use awk instead tr (broken in busybox on OpenWrt)
- distr_info: drop obsoleted systems, cleanup code
- distr_info: use hascommand instead which
- distr_info: add OpenWrt detection
- fix _lib32dir for Astra (eterbug #12915)
- macros.intro: add LDFLAGS in configure32

* Mon Aug 06 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.7-alt1
- add /proc buildreq in _tune_parallel_build_by_procsize

* Tue Jul 17 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- add EVR macros
- add rpm-build-compat require to rpm-build-intro (due distr_vendor)

* Sat Jul 14 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.5-alt1
- introduce _tune_parallel_build_by_procsize
  (set __nprocs limited in depend of system memory and suggested size)
- distr_vendor: major update from dist_info from eepm

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- add _userunitdir
- add python3_dirbuild_debug
- add python_test, python3_test, python3_dirtest

* Tue Dec 26 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- add _pypi_url

* Thu Dec 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- add add_verify_elf_skiplist to other platforms

* Sat Oct 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- spread _rundir, _logdir to other platforms

* Sat Oct 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- move _localstatedir macro to rpm-macros-intro-conflicts package (ALT bug 32554)

* Sun Oct 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- add support for python3_dir* args

* Mon Oct 16 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- add python3_dircheck

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- add py3_use, python3_check

* Fri Oct 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.19-alt1
- introduce python3_dirsetup, python3_dirbuild, python3_dirinstall (see python-module-chatdet for example)
- introduce py_use and lib_use (set low version for buildrequires and requires)

* Wed Sep 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.18-alt3
- fix end of line in _ln_sr macro

* Tue Sep 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.18-alt2
- ln_sr: add nonrelative workaround if ln --relative not yet supported

* Mon Sep 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.18-alt1
- introduce _ln_sr

* Fri Aug 04 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.17-alt1
- fix macros, add logrotatedir for deb systems

* Fri Apr 07 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.16-alt1
- distr_vendor: fix for ALT 8.x, drop obsoleted versions

* Fri Jan 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.15-alt1
- fix _target_python_libdir for Ubuntu/Debian

* Fri Dec 23 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.14-alt1
- move check_distr_vendor.sh to korinf/tools
- distr_vendor: sync with eepm/distr_info
- add liconsdir/niconsdir

* Fri Dec 02 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.13-alt1
- fix astra lib32dir and revert broken changes for Ubuntu (eterbug 4754#c109)

* Wed Nov 23 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.12-alt1
- add logrotate dir

* Tue Nov 15 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.11-alt1
- add link to macros for GosLinux

* Mon Nov 14 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.10-alt1
- add GosLinux support

* Tue Aug 23 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.9-alt1
- add _localstatedir = /var to rpm-build-intro

* Mon Aug 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.8-alt1
- add webserver-common
- ALT Linux: hard set _localstatedir to /var

* Sun Aug 14 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.7-alt1
- set _localstatedir to /var (see ALT bug #10382)

* Mon Jul 18 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.6-alt1
- astra: fix lib32dir

* Mon Jul 18 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.5-alt1
- update distr_vendor
- add AstraLinux support

* Sat Apr 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt1
- distr_vendor: use Sisyphus for ALT Linux as default

* Tue Feb 23 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.3-alt1
- really add python_check macro
- distr_vendor: add Cygwin support, improve ALT Linux version detection

* Mon Jan 25 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.2-alt1
- remove empty file for CentOS/6 (makes wrong macros list) (eterbug #10965)

* Mon Nov 23 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- set udev macros for CentOS/5

* Sun Nov 22 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- introduce configure32

* Mon Oct 12 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.10-alt1
- distr_vendor: sync with distr_info from eepm
- add qt5 rule, update qt4 macro

* Sun Sep 06 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.9-alt1
- add udev macros for other systems

* Thu Sep 03 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt1
- add udev macros for CentOS/6
- add mcst support

* Sat Aug 22 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.7-alt1
- fix add_findreq_skiplist/add_findprov_skiplist for deb based distro
- add udevrulesdir for deb based distros

* Sat Aug 22 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.6-alt1
- add add_findreq_skiplist/add_findprov_skiplist empty macros

* Tue Aug 18 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- add _udevrulesdir and _udevhwdbdir for ALT Linux p5
- add skip for add_findreq_lib_path

* Thu Jul 09 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- update macros cmake
- macros.compat: add _runtimedir

* Thu Jul 10 2014 Vitaly Lipatov <lav@altlinux.ru> 1.8.3-alt1
- set_gcc_version ignoring

* Tue Jun 03 2014 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- fix build with rpm4 on FreeBSD

* Sat Mar 15 2014 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- rename mandriva macros file to correct name macros.mdv

* Wed Mar 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- update README
- rewrite install.sh

* Wed Feb 26 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.37-alt1
- improve distro specific macros detection (use prev. if exits)

* Mon Feb 24 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.36-alt3
- add macros for Debian/7

* Wed Dec 18 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.36-alt2
- add symlink for correct build ROSA specific

* Thu Dec 12 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.36-alt1
- fix _initdir for Gentoo (eterbug #9701)

* Tue Oct 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.35-alt1
- fix fonts install macro

* Tue Oct 15 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.34-alt1
- python: add --prefix for setup.py

* Fri Oct 11 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.33-alt1
- add macro for Gentoo

* Wed Oct 02 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.32-alt1
- fixes for _sudoers dir on ALT Linux
- disable python.env (eterbug # 9477)
- change macros order for override version specific macros

* Mon Sep 16 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.31-alt1
- fix _qt4dir for Ubuntu/Debian

* Thu Sep 12 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.30-alt1
- add sudoersdir macro for old ALT Linux distros
- other fixes for _sudoersdir

* Fri Jul 12 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.29-alt1
- add _unitdir for old RHEL, Mandriva, SUSE distros

* Fri Jun 28 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.28-alt1
- add unitdir macro for systemd dir for deb systems, archlinux and slackware

* Wed Mar 20 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.27-alt1
- import macros from rpm-macros-qt*
- add qmake_qt4 macro (Mandriva like)

* Thu Feb 28 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.26-alt1
- python: disable ext. requires
- update python files
- add provides for included rpm-build-*

* Mon Feb 18 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.25-alt1
- intro macro _cupslibdir for /usr/lib/cups
- intro macro _sudoersdir for /etc/sudoers.d
- distr_vendor: fix ArchLinux package extension

* Sat Feb 02 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.24-alt2
- do not use ifndef in spec

* Thu Dec 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.24-alt1
- add _sharedstatedir to all old ALT Linux distro (p6 and early) in -compat

* Thu Dec 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.23-alt1
- add _sharedstatedir = /var/lib to compat
- distr_vendor: sync with distr_info from eepm package

* Mon Jul 23 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.22-alt1
- add _target_libdir

* Thu Jul 19 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.21-alt1
- distr_vendor: add ROSA support

* Tue Jun 05 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.20-alt1
- use x86_64 version instead regular if it exists

* Tue May 22 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.19-alt1
- major improve distr_vendor:
 + add support without ROOTDIR translation names
 + add SunOS support
 + cleanup
 + add -V for printout version

* Sat May 05 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.18-alt1
- fix Ubuntu/12.04 multiarch dir placement
- add _libexecdir for deb systems

* Sat May 05 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.17-alt1
- add support for Ubuntu 12.04 multiarch
- macros.intro: use prefix instead /usr (FreeBSD/Solaris uses /usr/local)

* Tue Apr 17 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.16-alt1
- add intro.backport to compat

* Tue Apr 17 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.15-alt1
- fix compat macros for ALT Linux

* Thu Apr 12 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.14-alt1
- add missed _lib32dir on ALT backports

* Tue Apr 10 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.13-alt1
- distr_vendor: update for new systems
- install.sh: fix subst using

* Tue Apr 10 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.12-alt1
- set _initddir as /etc/rc.d for ArchLinux (eterbug #7863)

* Mon Apr 09 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.11-alt1
- macros.intro: add _lib32dir

* Tue Mar 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.10-alt1
- add .x86_64 support and add hack for deb based systems

* Fri Jan 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.9-alt1
- use _sys_macros_dir for macros dir if defined

* Mon Oct 03 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.8-alt1
- do not use pushd/popd in specs

* Wed Sep 28 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- add macros from control

* Tue Aug 30 2011 Denis Baranov <baraka@altlinux.ru> 1.7.6-alt2
- spec: add openpkg from SunOS support for macros dir

* Mon Jul 25 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.6-alt1
- add rpm-build-tts

* Wed Jul 13 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- distr_vendor: fixes for ALT Linux
- spec: add FreeBSD support for macros dir

* Fri Jul 01 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- distr_vendor: use uname -r for FreeBSD

* Sat Apr 02 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- add _target_libdir, _target_libdir_noarch (needed for python macros)

* Sat Feb 19 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt3
- fix version detection for Fedora

* Tue Feb 08 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt2
- use /etc/init.d for SUSE based distro (eterbug #6629)

* Fri Feb 04 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- distr_vendor: get Mandriva version via lsb-release
- use rc.d/init.d for rpm based distro (eterbug #6629)

* Wed Oct 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt2
- define _initddir for all pkgtype

* Wed Oct 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- remove python env. var. (http://bugs.etersoft.ru/show_bug.cgi?id=4754#c25)
- use _initddir instead _initdir, add _initdir to ALT compat macros (see ALT #24290)
- remove dup macros

* Sat Oct 02 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- split in two package on ALT Linux: rpm-build-compat and rpm-build-intro
- disable start_service on ALT Linux (fix for ALT bug #24152)
- improve detecting ALT Linux 5.1 and 6.0

* Fri Oct 01 2010 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- update SUSE/Mandriva/PCLinux detections
- fix install pkgtype related macros

* Mon Jul 26 2010 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt1
- add python, perl macros

* Mon May 31 2010 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- rearrange source macros file
- update distr_vendor

* Sat Apr 10 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt1
- introduce %%_sysconfigdir (%%_sysconfdir/sysconfig)

* Sun Mar 07 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt2
- fix translation distro name
- fix Url to new place
- add support for -p option to subst

* Sat Mar 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- add macros from rpm-build-perl
- move build to BuildFarm

* Wed Jan 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt1
- small rearrange macros
- move _aclocaldir, _locksubsysdir, _rpmmacrosdir to already realized in ALT

* Thu Nov 19 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- update cmake macros from cmake 2.8.0-alt1, move it to compat

* Sat Sep 26 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- fix cmake for build in build subdir

* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- distr_vendor: add -n option for printout distro name in _vendor macros format
- update distr_vendor to newest distro support

* Mon Mar 02 2009 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- fix cmake, fix_permissions macros
- introduce remove_repo_info macro
- sync python_ macros with rpm-build-python

* Tue Jan 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt2
- add bindir to install script

* Thu Jan 08 2009 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- introduce cmake, fix_permissions, python_check macros

* Wed Dec 10 2008 Yuri Fil <yurifil@altlinux.org> 1.2-alt4
- add compat add_python_req_skip, license macros
- introduce _locksubsysdir macro

* Thu Nov 13 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt3
- fix font path for other system

* Thu Oct 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- add modified macroses from rpm-build-fonts for other systems
- bin/distr_vendor: right use status of the last command in functions

* Mon Jun 09 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- fix copy/paste error in add_optflags/remove_optflags

* Sat Jun 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- add distro specific macroses support
- set correct fonts path for various distro

* Thu May 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt3
- add add_optflags/remove_optflags

* Mon Mar 24 2008 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt2
- disable empty rpmldflags
- ignore return status from groupadd/useradd

* Thu Mar 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt1
- fix useradd/groupadd realization again
- update rpm opt* flags

* Sun Mar 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt1
- fix useradd/groupadd realization for various distros

* Sun Feb 24 2008 Vitaly Lipatov <lav@altlinux.ru> 0.98-alt1
- add autoreconf macros
- add add_findprov_lib_path skipping
- do not override add_findprov_lib_path and set_verify_elf_method on ArchLinux

* Sat Jan 19 2008 Vitaly Lipatov <lav@altlinux.ru> 0.97-alt1
- do not check tty -s in start_service for other platforms
- check DURING_INSTALL in start_service

* Fri Jan 11 2008 Vitaly Lipatov <lav@altlinux.ru> 0.96-alt1
- add make_install_std, makeinstall_std, omfdir
- cleanup spec according to etersoft-build-utils 1.3.6

* Sat Dec 15 2007 Vitaly Lipatov <lav@altlinux.ru> 0.95-alt2
- add set_verify_elf_method stub for non ALT systems

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.95-alt1
- upgrade dist_vendor script to newest systems
- add check for too old mktemp to add_changelog
- add defaultdocdir definition
- add ChangeLog file
- fix start_service macros
- add initial ArchLinux support
- use lxp suffix for LinuxXP and mdv for Mandriva

* Fri Sep 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt1
- update distr_vendor
- add macros start_service for conditional start service during install

* Mon Jul 02 2007 Vitaly Lipatov <lav@altlinux.ru> 0.93-alt1
- upgrade dist_vendor script to newest systems

* Fri Mar 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.92-alt1
- do not add old ALT distro compatibility macroses for all (fix bug #11183)

* Thu Mar 08 2007 Vitaly Lipatov <lav@altlinux.ru> 0.91-alt1
- rewrite distr_vendor (add detect for all supported system)
- enable make_build to multiprocess build

* Mon Feb 26 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- define post_service macroses separately for rpm and deb

* Thu Feb 22 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt5
- fix distr_vendor script, fixes for dash using
- pack distr_vendor for ALT Linux

* Sun Jan 14 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt4
- remove _libexecdir

* Thu Nov 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt3
- fix _libexecdir

* Sat May 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt2
- add _docdir
- use nil for correct macro functions
- fix subst script

* Sat Apr 15 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- add dummy macroses for menu/desktopdb update
- add distr_vendor script for distro version detecting
- use : in stub macroses

* Tue Apr 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt3
- fix chkconfig params
- change initdir to /etc/init.d (for non ALT)
- rewrite preun/post scripts

* Sun Apr 09 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt2
- revert prev. changes, fix some macroses

* Sun Apr 09 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- define ALT macroses only if not defined yet
- add __niconsdir

* Sat Mar 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- fix stupid bug with postun script name
- fix mktemp in old systems

* Sat Feb 18 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- some fixes

* Sun Feb 12 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- merge rpm-build-altlinux-compat and rpm-build-compat projects

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- fix __autoreconf macro name
- add _aclocaldir macro

* Sun Feb 05 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- add rpmcflags macro

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- start ALT backports compatibility project

* Fri Dec 30 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- new release, macros updated by Denis Smirnov

* Sat Oct 29 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1-redhat1
- test pre release
