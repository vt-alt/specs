%def_enable libdmmp

%define syslibdir /%_lib
%define libmpathdir %syslibdir/multipath

%add_verify_elf_skiplist /%_lib/libmpathpersist.so.*
%add_verify_elf_skiplist /%_lib/libmultipath.so.*

Name: multipath-tools
Version: 0.8.3
Release: alt1

Summary: Tools to manage multipath devices with device-mapper
License: GPLv2+
Group: System/Configuration/Hardware

Url: http://christophe.varoqui.free.fr
# http://git.opensvc.com/multipath-tools/.git
Source: %name-%version.tar
Source2: multipath.rules
Source3: multipathd.init
Source4: multipath.modules
Source5: multipath.conf
Patch1: %name-%version.patch

Requires: libmultipath = %EVR
Requires: kpartx = %EVR
Requires: dmsetup

BuildRequires: libaio-devel libdevmapper-devel libreadline-devel libudev-devel libsystemd-devel
BuildRequires: libuserspace-rcu-devel
%{?_enable_libdmmp:BuildRequires: libjson-c-devel}

%description
This package provides the tools to manage multipath devices by
instructing the device-mapper multipath module what to do.
The tools are:
- multipath: lists and configures multipath devices.
- multipathd: monitors paths; as paths fail and come back, it may
  initiate path group switches.

%package -n libmultipath
Summary: The %name modules and shared library
License: GPL+
Group: System/Libraries
Conflicts: multipath-tools <= 0.4.9-alt3

%description -n libmultipath
The libmultipath provides the path checker
and prioritizer modules. It also contains the multipath shared library,
libmultipath.

%package -n libmultipath-devel
Summary: Development libraries and headers for %name
Group: Development/C
Requires: libmultipath = %EVR

%description -n libmultipath-devel
This package contains the files need to develop applications that use
multipath-tools's libmpathpersist and libmpathcmd libraries.

%package -n kpartx
Summary: Partition device manager for device-mapper devices
Group: System/Configuration/Hardware
Conflicts: multipath-tools <= 0.4.9-alt3

%description -n kpartx
kpartx manages partition creation and removal for device-mapper devices.

%package -n libdmmp
Summary: multipath-tools C API library
Group: System/Libraries

%description -n libdmmp
This package contains the shared library for the multipath-tools
C API library.

%package -n libdmmp-devel
Summary: device-mapper-multipath C API library headers
Group: Development/C
Requires: libdmmp = %EVR

%description -n libdmmp-devel
This package contains the files needed to develop applications that use
device-mapper-multipath's libdmmp C API library

%prep
%setup -q
%patch1 -p1

%build
unset RPM_OPT_FLAGS
%make_build \
	LIB=%_lib \
	RUN=run \
	%{?_disable_libdmmp: ENABLE_LIBDMMP=0} \
	SYSTEMDPATH=lib

%install
mkdir -p %buildroot{/sbin,%_libdir,%_man8dir,%_initdir,%_unitdir,%_udevrulesdir,%_modulesloaddir,%_sysconfdir/multipath}
%makeinstall_std \
	DESTDIR=%buildroot \
	SYSTEMDPATH=lib \
	%{?_disable_libdmmp: ENABLE_LIBDMMP=0} \
	LIB=%_lib \
	RUN=run \
	bindir=/sbin \
	syslibdir=%syslibdir \
	libdir=%libmpathdir \
	usr_prefix=%_prefix \
	rcdir=%_initrddir \
	udevrulesdir=%_udevrulesdir \
	unitdir=%_unitdir

#install -pm644 %SOURCE2 %buildroot%_udevrulesdir/56-multipath.rules
install -pm755 %SOURCE3 %buildroot%_initdir/multipathd
#install -pm644 %SOURCE4 %buildroot%_modulesloaddir/multipath.conf
install -pm644 %SOURCE5 %buildroot%_sysconfdir/multipath.conf

%post
%post_service multipathd

%preun
%preun_service multipathd

%files
%doc README
/sbin/multipath
/sbin/multipathd
#/sbin/mpathconf
/sbin/mpathpersist
%_udevrulesdir/*
%exclude %_udevrulesdir/*kpartx.rules
#%_modulesloaddir/*
%dir %_sysconfdir/multipath
%config(noreplace) %attr(644,root,root) %_sysconfdir/multipath.conf
%_initdir/*
%_unitdir/*
%_man5dir/*
%_man8dir/*
%exclude %_man8dir/kpartx.8.*

%files -n libmultipath
/%_lib/libmultipath.so.*
/%_lib/libmpathcmd.so.*
/%_lib/libmpathpersist.so.*
%dir %libmpathdir
%libmpathdir/*

%files -n libmultipath-devel
/%_lib/libmultipath.so
/%_lib/libmpathpersist.so
/%_lib/libmpathcmd.so
%_includedir/mpath_cmd.h
%_includedir/mpath_persist.h
%_man3dir/mpath_*

%files -n kpartx
%_udevrulesdir/*kpartx.rules
/sbin/kpartx
/lib/udev/kpartx_id
%_man8dir/kpartx.8.*

%files -n libdmmp
%_libdir/libdmmp.so.*

%files -n libdmmp-devel
%_libdir/libdmmp.so
%dir %_includedir/libdmmp
%_includedir/libdmmp/*
%_man3dir/dmmp_*
%_man3dir/libdmmp.h.3.*
%_pkgconfigdir/libdmmp.pc

%changelog
* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 0.8.3-alt1
- 0.8.3

* Mon Jul 08 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.2-alt1
- 0.8.2
- do not package %%_modulesloaddir/multipath.conf,
  because ExecPre loaded kernel modules

* Tue May 07 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.1-alt1
- 0.8.1
- fixed udev rules

* Mon Apr 01 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- 0.8.0
- removed ALT glibc functions from util, since  ALT build glibc has its own
  implementation of the strlcat, strlcpy and strnlen functions (closes: #36411)

* Mon Sep 03 2018 Michael Shigorin <mike@altlinux.org> 0.7.4-alt2
- applied patches suggested by Alex Moskalenko
  (closes: #35286, #35287)

* Fri Dec 15 2017 Alexey Shabalin <shaba@altlinux.ru> 0.7.4-alt1
- 0.7.4
- add devel packages

* Sun Nov 12 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt1.1
- autorebuild with libuserspace-rcu.git=0.10.0-alt1

* Thu Mar 23 2017 Alexey Shabalin <shaba@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Tue Nov 08 2016 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt2
- fix work inside initrd (shrek@)

* Fri Jun 17 2016 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1
- 0.6.1
- use upstream udev rules

* Wed Apr 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.5.0-alt3
- updated multipath.rules

* Tue Jul 14 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt2
- upstream snapshot (770e6d0da035deaced82885939161c2b69225e10)
- add patches from suse

* Thu Mar 05 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Tue May 27 2014 Michael Shigorin <mike@altlinux.org> 0.4.9-alt5
- added missing Conflicts: to facilitate upgrade (closes: #30092)

* Fri Nov 16 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.9-alt4
- upstream snapshot 2012-10-01
- update udev rules
- add systemd unit file
- split packages libmultipath and kpartx
- Apply fedora patches:
  0025-RH-fix-systemd-start-order.patch
  0024-RH-start-multipathd-service-before-lvm.patch
  0023-RHBZ-866291-update-documentation.patch
  0022-RHBZ-864368-disable-libdm-failback.patch
  0021-RH-fix-oom-adj.patch
  0020-RH-netapp-config.patch
  0019-RH-detect-prio.patch
  0018-RH-remove-config-dups.patch
  0016-RH-retain_hwhandler.patch
  0015-RH-selector_change.patch
  0014-RH-dm_reassign.patch
  0013-RH-kpartx-msg.patch
  0012-RH-change-configs.patch
  0011-RH-use-sync-support.patch
  0009-RH-dont-remove-map-on-enomem.patch
  0007-RH-add-hp_tur-checker.patch
  0006-RH-add-find-multipaths.patch
  0005-RH-add-mpathconf.patch
  0004-RH-multipathd-blacklist-all-by-default.patch
  0002-RH-multipath.rules.patch
  0001-RH-dont_start_with_no_config.patch

* Tue Feb 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.9-alt3
- rebuild with new libdevmapper versioning

* Mon Mar 01 2010 Konstantin Pavlov <thresh@altlinux.org> 0.4.9-alt2
- Rebase to 0.4.9 b68400c7.
- Apply 0012-RH-udev-sync-support.patch from Fedora devel (fixes #23041).
- Apply 0022-RHBZ-557845-RHEL5-style-partitions.patch from Fedora devel.
- Install udev rules to /lib/udev/rules.d instead of /etc/udev/rules.d.

* Wed Oct 14 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.4.9-alt1
- Rebase to 0.4.9 aa0a885e1.
- Remove devmap_name (redundant with dmsetup, following upstream).
- Blacklist all devices by default (closes #21769).

* Thu Sep 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.4.8-alt3
- Fix another wrong scsi_id invocation in libmultipath.

* Wed Aug 26 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.4.8-alt2
- Apply a bunch of Fedora patches, notable changes are:
  + kpartx now works with logical partitions
  + fix for CVE-2009-0115
  + support for newer scsi_id invocation scheme.
- Some cosmetic spec file changes (spelling, descriptions rewrite).
- Added cciss_id utility.
- Added default configuration file.
- Added init script for multipathd.

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 0.4.8-alt1
- 0.4.8: please see the site for changes that may require
  you altering your config file
- built with libaio
- added kpartx to main package
- buildreq
- NB: I don't have multipath-capable hardware, maintainer wanted

* Tue Sep 02 2008 Michael Shigorin <mike@altlinux.org> 0.4.7-alt4
- BR: glibc-kernheaders instead
- exclude devmap_name from main subpackage

* Mon Sep 01 2008 Michael Shigorin <mike@altlinux.org> 0.4.7-alt3
- BR: kernel-headers-std-def (provides broke?)

* Mon Apr 09 2007 Michael Shigorin <mike@altlinux.org> 0.4.7-alt2
- fixed build
- spec cleanup
- added %_sysconfdir/udev/rules.d/multipath.rules

* Thu Mar 30 2006 Eugene Prokopiev <enp@altlinux.ru> 0.4.7-alt1
- build with new version and without external patches

* Wed Aug 31 2005 Nick S. Grechukh <gns@altlinux.ru> 0.4.4-alt0.18
- initial build for ALT Linux Sisyphus

* Thu Jun 16 2005 - lmb@suse.de
- Remove stray newline character from /dev/disk/by-name/ entries
  (#85798, #86763)
- Clear /dev/disk/by-name/ on boot. (#85978)
- scsi_id now handles EMC Symmetrix; remove work-around for #86760.
* Tue Jun 07 2005 - lmb@suse.de
- Import fixes from upstream.
- Hardware table updates for IBM ESS and EMC CX (#81688).
- Reinstate paths correctly after failure/restore cycle (#85781,
  [#86444]).
- Create map names again and fix segfault in devmap_name (#85798).
* Tue May 24 2005 - hare@suse.de
- Fix segmentation fault with EMC Symmetrix (#85614).
- Update EMC Symmetrix entry in hwtable.
* Mon May 23 2005 - hare@suse.de
- Add hwtable entry for IBM DS6000. (#63903)
- Do a rescan for devices if multipath command line option is set.
* Fri May 20 2005 - hare@suse.de
- Fix devmap_name to use mapname and return proper status (#84748).
* Thu May 12 2005 - lmb@suse.de
- Don't complain about default prio callout command (#81695).
- Reflect recent changes in boot.multipath as well as multipathd init
  scripts.
- Actually fail paths when they are detected to be failed by multipathd
  (#81679).
- killproc/startproc/checkproc can't be used with multipathd because of
  the way the daemon switches to its own namespace (#80443).
* Mon May 09 2005 - hare@suse.de
- Use proper path checker for SGI TPC arrays.
- Update hwtable entries for SGI TP9400 and SGI TP9500.
- Write correct PID file (#80443).
* Mon Apr 25 2005 - lmb@suse.de
- Update to 0.4.4: pp_alua now licensed as GPL (#78628).
- multipath-tools-oom-adj.patch: oom_adj to a valid value.
* Thu Apr 21 2005 - lmb@suse.de
- Update to 0.4.4-pre18 which fixes the multipathd to initialize
  correctly in the absence of a configuration file (79239).
* Wed Apr 20 2005 - lmb@suse.de
- Put multipath cache back into /dev because /var might not be mounted.
- Correct hwtable entry SGI TP9400, TP9500 and IBM 3542.
* Wed Apr 20 2005 - lmb@suse.de
- Update to 0.4.4-pre16
- Build against device-mapper.1.01.xx correctly.
* Tue Apr 19 2005 - lmb@suse.de
- Build w/o device-mapper update again.
* Mon Apr 18 2005 - lmb@suse.de
- Update to 0.4.4-pre14
- Build versus device-mapper-1.01.01 to prevent deadlocks in
  kernel-space.
- Fix devmap_name to work with udev.
- Fix startup of multipathd w/o configuration file present.
* Fri Apr 15 2005 - lmb@suse.de
- Add path priority checker for EMC CLARiiON and make necessary
  adjustments so that it gets called by default (#62491).
- Set the default udev dir to '/dev'
* Fri Apr 15 2005 - hare@suse.de
- Fix to allocate default strings (#78056)
- Fix default entry for TPC9500.
* Wed Apr 13 2005 - hare@suse.de
- Added pp_alua path priority checker.
- Update to multipath-tools-0.4.4-pre12.
* Mon Apr 11 2005 - hare@suse.de
- Update to multipath-tools-0.4.4-pre10.
* Fri Apr 08 2005 - hare@suse.de
- Update multipath to handle only true multipath devices (#62491).
- Update kpartx to use the device mapper target name if available.
- Add boot.multipath script for early set up of multipath targets.
* Thu Mar 31 2005 - hare@suse.de
- Update devmap_name to select targets by table type (#62493).
* Tue Jan 25 2005 - lmb@suse.de
- Update to 0.4.2 and fix some bugs + add support for the extended DM
  multipath kernel module. (#47491)
* Thu Nov 11 2004 - hare@suse.de
- Fix bugs to make it work on S/390 (#47491).
* Fri Nov 05 2004 - hare@suse.de
- Update to version 0.3.6 (#47491).
- Fix multipath init script
- Install configuration file example.
- Install multipathd in /sbin instead of /usr/bin.
* Tue Jul 20 2004 - fehr@suse.de
- updated README mp-tools-issues.pdf (see #40640)
* Wed Jun 09 2004 - fehr@suse.de
- added pdf with README to package (see #40640)
* Thu Jun 03 2004 - fehr@suse.de
- updated to version 0.2.1
- removed patches zero-currpath.patch and rm-newline-in-name.patch
  already contained in 0.2.1
* Thu Jun 03 2004 - fehr@suse.de
- added patch zero-currpath.patch (see bugzilla #40640)
* Wed May 26 2004 - uli@suse.de
- fixed to build on s390x
* Wed May 26 2004 - fehr@suse.de
- added patch rm-newline-in-name.patch (see bugzilla #40640)
* Tue May 25 2004 - fehr@suse.de
- created initial version of a SuSE package from version 0.2.0 of
  multipath tools
