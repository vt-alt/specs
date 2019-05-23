%define guile22 1

Name: alterator-x11
Version: 1.98.14
Release: alt3

Url: http://www.altlinux.com
Source:%name-%version.tar

Summary: alterator module for Xorg setup and configuration
License: GPL
Group:   System/Configuration/Other

Conflicts: alterator-fbi < 5.23-alt1
Conflicts: alterator-lookout < 0.9-alt1

Requires: x11presetdrv
Requires: alterator >= 4.14-alt1
Requires: alterator-sh-functions >= 0.3-alt1

#xorg components
Requires: xinit >= 1.0.1-alt1
Requires: xorg-server >= 1.4.2-alt4

Requires: alterator-backend-x11 = %version-%release

BuildPreReq: alterator >= 3.2-alt5
BuildRequires: libXft-devel libxorgconfig-devel libXt-devel xorg-sdk
%if %guile22
BuildRequires: guile22-devel
BuildRequires: alterator-lookout
%endif

%description
alterator module for Xorg setup and configuration

%package -n alterator-backend-x11
Summary:  alterator backend for x11 setup and configuration
Group:    System/Configuration/Other
Requires: make-initrd
Requires: xsetup = %version-%release
%ifarch %ix86 x86_64
Requires: ddcprobe
%endif

%description -n alterator-backend-x11
simple alterator backend for x11 setup and configuration

%package -n xsetup
Summary:  Tools for Xorg configuration
Group:    System/Configuration/Other
BuildArch: noarch

%description -n xsetup
Scripts which creates simple configuration files in
/etc/X11/xorg.conf.d.

%prep
%setup -q

%build
%make_build

%install
%if %guile22
export GUILE_LOAD_PATH=/usr/share/alterator/lookout/
%endif
%makeinstall

%post -n alterator-backend-x11
# Rename old config
[ -e %_sysconfdir/modprobe.d/blacklist-alterator-x11 ] &&
	mv %_sysconfdir/modprobe.d/blacklist-alterator-x11 \
	   %_sysconfdir/modprobe.d/blacklist-alterator-x11.conf ||:

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_bindir/config-x11

%files -n alterator-backend-x11

%_bindir/is_*
%_bindir/*_ddc
%_bindir/*_setup
%_bindir/*_autosetup
%_bindir/*_scan
%_bindir/*conf
%_bindir/video_drv

%_libexecdir/%name
%_datadir/%name
%_alterator_backend3dir/*

%files -n xsetup
%_bindir/xsetup*

%changelog
* Thu May 23 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.98.14-alt3
- Fixed previous change (aarch64 is non-x86 too).

* Mon Apr 08 2019 Michael Shigorin <mike@altlinux.org> 1.98.14-alt2
- Don't require "ddcprobe" on non-x86 arches (manowar@).

* Thu Dec 27 2018 Mikhail Efremov <sem@altlinux.org> 1.98.14-alt1
- video_scan: Initialize local variable.

* Thu Jul 27 2017 Oleg Solovyov <mcpain@altlinux.org> 1.98.13-alt1
- Fallback to /usr/share/alterator-x11/xorg.conf
  if default xorg.conf does not exist (closes: #32510)

* Mon Dec 05 2016 Michael Shigorin <mike@altlinux.org> 1.98.12-alt1
- suppress sed's stderr noise (missing videoaliases aren't a problem)

* Mon Jun 27 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.98.11-alt1
- bug with unexisting (always) xorg.conf fixed

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 1.98.10-alt1
- update display size option name (closes: #30829)

* Fri Dec 11 2015 Mikhail Efremov <sem@altlinux.org> 1.98.9-alt1
- Fix build with recent glibc.

* Wed Mar 11 2015 Mikhail Efremov <sem@altlinux.org> 1.98.8-alt1
- Use driver name if description is not found (closes: #26581).
- Blacklist other drivers in case of vesa (closes: #29435).
- Replace shell-regexp with shell-quote (closes: #30811).

* Mon Jun 17 2013 Sergey V Turchin <zerg at altlinux dot org> 1.98.7-alt1
- polish DisplaySize UI

* Fri Jun 14 2013 Sergey V Turchin <zerg at altlinux dot org> 1.98.6-alt1
- simplify DisplaySize UI

* Fri Jun 14 2013 Sergey V Turchin <zerg at altlinux dot org> 1.98.5-alt1
- disable DisplaySize by default
- clear DisplaySize when unusable or disabled

* Thu Jun 06 2013 Sergey V Turchin <zerg at altlinux dot org> 1.98.4-alt1
- add ability to setup display size (ALT#28179)

* Mon Apr 15 2013 Mikhail Efremov <sem@altlinux.org> 1.98.3-alt1
- Run make-initrd in compat mode too (closes: #21932).

* Fri Sep 07 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.98.2-alt1
- the modesetting driver added to the drivers database

* Wed Oct 19 2011 Mikhail Efremov <sem@altlinux.org> 1.98.1-alt1
- Add .conf extension to blacklist config name.

* Wed Sep 21 2011 Mikhail Efremov <sem@altlinux.org> 1.98.0-alt1
- Set generic HorizSync and VertRefresh if needed (closes: #26248).
- xsetup-monitor: Add --hsync and --vrefr options.
- xsetup: Fix adding values with spaces.
- xsetup and xsetup-monitor: Usage message improved.
- config-x11: Use xsetup-monitor.
- Use cache for config file (closes: #26301).

* Tue Aug 23 2011 Mikhail Efremov <sem@altlinux.org> 1.97.1-alt1
- xsetup-monitor: Add --create-only option.

* Thu Aug 18 2011 Mikhail Efremov <sem@altlinux.org> 1.97.0-alt1
- backend: Use xsetup and xsetup-monitor.
- Add xsetup-monitor script.
- Add xsetup script.

* Thu Aug 11 2011 Mikhail Efremov <sem@altlinux.org> 1.96.0-alt1
- Return x11_autosetup.

* Wed Aug 10 2011 Mikhail Efremov <sem@altlinux.org> 1.95.1-alt1
- Add warning message on commit changes.

* Fri Jul 29 2011 Mikhail Efremov <sem@altlinux.org> 1.95.0-alt1
- Drop xorg-drv-video requires.
- Recreate initrd if needed.
- Blacklist modules.
- Drop monitor selection.
- Drop test feature.
- Use /etc/X11/xorg.conf.d/.
- video_scan: Fix current driver displaying.
- Drop x11_autosetup.

* Tue May 31 2011 Lenar Shakirov <snejok@altlinux.ru> 1.10.0-alt2
- add data for mach64 video driver

* Mon Mar 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.10.0-alt1
- no HAL/Dbus (stanv@)

* Mon Jan 31 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.9.1-alt1
- x11_autosetup don't set video driver if no driver set, it a work for 
  Xorg now

* Tue Nov 23 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.9-alt1
- data/drivers: nouveau added
- html interface disabled

* Sat May 08 2010 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt2
- data/drivers: add geode/ztv/amd (closes: #13543, thanks to snejok@)

* Fri Dec 25 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt1
- monitor_ddc: avoid non-zero return values
- monitor_ddc: get DDCPROBE and DDCDUMP_FILE from the environment
- remove default modes from template xorg.conf

* Fri Dec 25 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.7-alt1
- backend: don't try to run x11setupdrv if it isn't installed (closes: #22417)

* Mon Dec 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.6-alt1
- monitor_ddc: don't return multiline values (closes: #22394)

* Tue Nov 03 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt1
- come back to libxorgconfig

* Mon Nov 02 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt1
- use local libxf86config
- remove xconf script, resurrect old xconf program
- xconf: fix reversed mode order in -R (closes #16069, thanks to led@)
- xconf: fix help message
- monitor_ddc/resbest: fix error handling
- x11_autosetup: fix error handling

* Wed Oct 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt1
- monitor_setup: add help message
- xconf: don't write empty HorizSync or VertRefresh to xorg.conf
- resolution_setup: don't write 'auto' resolution to xorg.conf

* Tue Oct 20 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt1
- xconf: fix color depth and modes handling
- data/xorg.conf: remove DRI section,
  remove AutoAddDevices and AIGLX ServerFlags

* Fri Oct 16 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt2
- pack missing monitor_ddc tool

* Thu Oct 15 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- xconf: don't set empty depth or resolution
- video_scan: don't try to find current driver if it is not needed
- x11_autosetup: set fbresolution for autodetected fbdev drivers too
- use monitor_ddc script instead of /usr/lib/alterator-x11/ddc*

* Thu Oct 15 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- replace xconf program by shell script
- don't use x11setupdrv (closes #18843)
- html ui:
  - move html ui into ui directory
  - use wf=none
  - use card-index module in ajax.scm
  - rearrange interface design.
  - remove xorg test
- backend: use run_localized for xtest_wrapper.
- heplers:
  - video_scan: don't fail when current driver detection failed.
  - resolution_setup: set resolutions in descending order (use new xconf)
  - resolution_setup: add help message.
- spec: cleanup, change Packager

* Mon Sep 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.27-alt1
- /usr/share/alterator-x11/monitors: change vendor
  for Magnavox MB7000 (closes: #21622)
- video_setup: use /etc/X11/xorg.conf as a default
- video_scan: show current driver

* Fri Aug 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.26-alt3
- change default color depth for vesa driver to 24bpp (see #21270)

* Thu Jun 25 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.26-alt2
- change default depth for intel driver to 24bpp

* Mon Jun 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.26-alt1
- montest.c: do XDefineCursor

* Mon Jun 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.25-alt1
- video_setup: setup default color depth
- data/drivers: set default depth 16 for fbdev driver (#20309)

* Thu Apr 02 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.24-alt1
- mouseconf: fix first mouse adding
- x11_autosetup: fix mouse_autosetup execution

* Thu Apr 02 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.23-alt1
- ressurect serial_mouse_scan program and mouse_autosetup script,
  use old-style mouse autosetup
- x11_autosetup: run with -efu options; don't fail on x11{setup,preset}drv
- update translations in x11.desktop

* Mon Mar 02 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.22-alt6
- If test fails show EE lines from Xorg.log

* Fri Feb 20 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.22-alt5
- fix: remove newline in drivers list (by stanv@)

* Wed Feb 18 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.22-alt4
- fix xtest_wrapper.c

* Wed Feb 18 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.22-alt3
- xtest_wrapper.c: don't fail on second x11setupdrv
  Test is OK even if we can't do x11setupdrv for host xdriver
  (fix "test fail" error on installer)

* Mon Feb 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.22-alt2
- fix monitor lists
- add translations to desktop-file

* Wed Feb 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.22-alt1
- don't remove alterator's copy of xorg.conf until exit

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.21-alt4
- use translations and help from alterator-l10n

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.21-alt3
- backend: fix typo in monitor_scan execution

* Wed Jan 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.21-alt2
- fix video_scan for x86_64

* Tue Jan 20 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.21-alt1
- xconf: some tests for NULL pointers (fix #18571)
- backend: fix config workcopy creation logic (fix #18572)
- Completely rewrite videodriver detection.
  Remove vcscan, vcdb, vcdrv, vcdrv_sorted and vcinfo tools
  Change videodriver database format
  (See  `video_scan -h`  and  `video_drv -h`)

* Sun Jan 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt19
- xconf: fix -a option

* Sun Jan 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt18
- fix write_error on non-existing xorg.conf
- fix a bug with cancel button in config-x11 mode

* Mon Dec 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt17
- message about synaptics driver

* Mon Dec 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt16
- config-x11: error when alterator-standalone does not exists

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt15
- use help from l10n

* Wed Nov 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.20-alt14
- alterator_api_version = 1
- update for latest firefox-alterator-extension
- minor module updates

* Tue Oct 14 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt13
- skipping test on nv-nvidia conflict: finding old driver in /proc (works in installer)

* Tue Oct 14 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt12
- rebuild with new alterator-l10n

* Mon Oct 13 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt11
- error message on nv - nvidia conflict
- add Option "AIGLX" "true" to xorg.conf

* Thu Oct 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt10
- remove %%D template from CONFPATH in xconf
- fix strange SEGV on empty file names in xconf
- cleanup template xorg.conf

* Thu Oct 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt9
- fix sort order in vcdrv_sorted

* Thu Oct 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt8
- add vcdrv_sorted helper; add fallback to other drivers returned by vcdrv

* Mon Sep 22 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt7
- fix minor typos in the help (by wrar@)

* Mon Sep 22 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt6
- add missing parameters to config

* Fri Sep 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt5
- remove fbdev fallback in x11_autosetup, change fbdev and vesa fallbacks in config-x11

* Wed Sep 17 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt4
- sort video drivers using priorities (nvidia before nv etc...)

* Wed Sep 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt3
- add options for explicitly set of xdriver and xres values
  in x11_autosetup

* Wed Sep 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt2
- replace debug() function by verbose() from shell-error

* Wed Sep 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.20-alt1
- remove unused serial_mouse_scan

* Tue Sep 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.19-alt9
- use write_enum

* Tue Sep 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.19-alt8
- rebuild with new alterator-l10n

* Thu Jul 31 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.19-alt7
- Requires: hal dbus

* Thu Jul 31 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.19-alt6
- looking for running hal and dbus in config-x11 (fix #7980)

* Thu Jul 31 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.19-alt5
- backup xorg.conf in config-x11 (fix #7980)

* Mon Jul 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.19-alt4
- fix problem with quit-btn in installer

* Thu Jul 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.19-alt3
- fix setup_xorg_serial() in x11_autosetup

* Tue Jul 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.19-alt2
- comments about mice in xorg.conf
- Option  "AllowMouseOpenFail"  "true"
  (this option is set by default, but i add it explicitely to avoid questions)

* Tue Jul 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.19-alt1
- add quit button to config_x11 (fix #16357)

* Tue Jul 15 2008 Michael Shigorin <mike@altlinux.org> 0.18.1-alt1
- merged mike/M40 forward port by Valentyn Solomko

* Fri Jul 11 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt11
- fix broken "next" button in installer (bug appeared in 0.18-alt2)

* Fri Jul 11 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt10
- remove obsolete script mouse_autosetup

* Fri Jul 11 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt9
- add setup_xorg_serial() to x11_autosetup (fix #16335)

* Thu Jul 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt8
- fix get_auto_xres

* Thu Jul 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt7
- /tmp/xtest-answer -> /tmp/alterator/xtest-answer (fix #13164)

* Thu Jul 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt6
- cleanup autodetect procedures in backend

* Thu Jul 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt5
- autodetect xdepth for the current driver in read action

* Thu Jul 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt4
- vcdb -- return "8 16 24" depth list for unknown cards

* Thu Jul 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt3
- change default values for enumref items from bool (#f) to string ("") (#fix 16325)

* Tue Jul 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt2
- add config-x11 tool

* Fri Jul 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.18-alt1
- remove translation from desktop file
- remove po_domain setting from backend
- remove po/*
- use module.mak
- remove titles and h1-headers from html

* Mon Jun 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.17-alt2
- fix monitor setup

* Fri Jun 27 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.17-alt1
- new x11_autosetup tool

* Wed Jun 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.16-alt4
- in fallback case in driver autodetect function try fbdev before vesa

* Wed Jun 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.16-alt3
- add devault values for unknown drivers

* Mon Jun 23 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.16-alt2
- modify Requires:
  - add Requires: xorg-server >= 1.4.2-alt4 - with libXiconfig
  - remove Requires: xorg-x11-mesagl
  - xorg-x11-* -> xorg-*
- modify xorg.conf template
  - add Option "AutoAddDevices" "true"
  - remove Option "AllowMouseOpenFail" "true"

* Thu Jun 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.16-alt1
- use libXiconfig
  - Requires:libXiconfig
  - add -x option in tools/mouse_autosetup
  - modify template xorg.conf
  - start messagebus and haldaemon

* Thu Jun 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.15-alt6
- add tail_res() definition to tools/resolution_autosetup

* Thu Jun 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.15-alt5
- interface crashes when monitor vendor unknown -fixed

* Fri May 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.15-alt4
- remove autoinstall backend usage
- remove po files

* Tue May 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.15-alt3
- use enumref in html interface

* Tue May 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.15-alt2
- use write_enum_item in backend

* Mon May 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.15-alt1
- improve resolution read/write
- use enumref feature

* Fri Apr 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.14-alt3
- little ui improvements

* Wed Apr 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.14-alt2
- join to common translation database
- update help

* Wed Apr 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.14-alt1
- remove html-messages
- improve ui according alterator-HIG
- use alterator-sh-function
- remove template-*
- drop support runlevel tuning (use installer-feature-runlevel5)

* Mon Apr 14 2008 Michael Shigorin <mike@altlinux.org> 0.13.8-alt1
- applied patch by led@ to improve xconf functionality (#15236)

* Wed Apr 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.13.7-alt1
- add default value in list_xdepth() for labeling non-standart xdepth's

* Wed Apr 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.13.6-alt2
- fix some problems with default bpp's

* Mon Mar 31 2008 Michael Shigorin <mike@altlinux.org> 0.13.6-alt1
- merge changes by slazav@ from 0.13.2-alt2
- disable (comment out) Composite support in generated xorg.conf
  (non-reliable feature thus broken default)

* Mon Mar 31 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.13.2-alt2
- default color depth 2 -> 0 (#15098)
- counter++ when pause button pressed (#11538)
- add composite keys to xorg.conf
- remove type1 module from xorg.conf

* Wed Mar 19 2008 Michael Shigorin <mike@altlinux.org> 0.13.5-alt1
- bumped suggested optimal DPI for resolution autosetup
  from 90 to 96 (#14371)

* Fri Mar 14 2008 Michael Shigorin <mike@altlinux.org> 0.13.4-alt1
- added openchrome to videocards (#14914)

* Fri Mar 14 2008 Michael Shigorin <mike@altlinux.org> 0.13.3-alt1
- fixed default depth fallback from -1 to 16 (#14913)

* Wed Feb 06 2008 Michael Shigorin <mike@altlinux.org> 0.13.2-alt1
- fixed broken assumptions (#14351); thanks led@ for diag/patch

* Wed Feb 06 2008 Michael Shigorin <mike@altlinux.org> 0.13.1-alt1
- modified x11_autosetup to look whether XORG_CONF is already
  given before setting it to default value (for diskless clients;
  fixes #14120)

* Mon Jan 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.13-alt1
- use own copy of the MonitorsDB (fix frequency rates, change names of the some models)
- monscan, moninfo: use common mondrv script to obtain monitors list
- protect monscan and moninfo from dups in the monitors database
- remove dups from list of monitor models
- move helpers from libexec to _libexecdir directory
- add help
- add AMD Geode videocard description

* Fri Dec 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.12-alt4
- mouse_autosetup hack: write COM1 mouse if nothing was found

* Thu Dec 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.12-alt3
- mouse_autosetup: add support for serial mices

* Wed Nov 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.12-alt2
- use sysfsutils instead of direct work with /sys filesystem

* Mon Oct 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.12-alt1
- fix package build
- send messages from x11setupdrv/x11presetdrv to stderr
- start test with alterator (not system) locale

* Wed Aug 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt12
- updated Ukrainian translation

* Mon Jul 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt11
- sort driver list

* Fri Jul 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt10
- fix template generation

* Thu Jul 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt9
- separate driver selection dialog
  (TODO: add some driver features configuration like Composite to this dialog)

* Wed Jul 11 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.10-alt8
- different color depth lists for differnt cards 

* Wed Jul 04 2007 Stanislav Ievlev <inger@altlinux.org> 0.10-alt7
- @boyarsh:  DRI enabled

* Fri Jun 22 2007 Stanislav Ievlev <inger@altlinux.org> 0.10-alt6
- fix button name
- fix xconf utility (hsync,vsync parse)

* Thu Jun 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.10-alt5
- resurrect is_touchpad utility

* Wed Jun 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.10-alt4
- add desktop file
- use std woo-list/name+label function

* Fri Jun 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.10-alt3
- fix x11 test in installer environment

* Tue Jun 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.10-alt2
- add wrapper to allow setup gl from user
- use RPM_OPT_FLAGS

* Mon Jun 04 2007 Stanislav Ievlev <inger@altlinux.org> 0.10-alt1
- improve autosetup tools

* Tue May 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt3
- translate monitor test

* Mon May 21 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt2
- fix xorg test start from user

* Fri May 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- significantly improved interface and backend

* Thu May 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.8-alt2
- new tools for recommended resolution and ddc resolutions list

* Wed May 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- preliminary version of the web interface

* Tue May 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt17
- videocards database: add intel driver description
- fix work with unknown drivers
- fix mouseconf (calloc)
- remove mouse stuff from xconf

* Mon May 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt16
- add mouse autodetect utils

* Wed May 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt15
- add Ukrainian translation

* Wed Apr 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt14
- fix work with monitors with double names ('Comtec CT 150')

* Wed Apr 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt13
- fix autodetection (#11356)

* Tue Mar 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt12
- fix work with monitors containing " symbols in their names (#11236)

* Fri Feb 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt11
- improve ui (use gridbox and separator)

* Mon Feb 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt10
- run x11presetdrv during backend initialization
- add information about current resolution
- simplify ui (replace apply recommended with notes)
- simplify ui code (resolution list generation)

* Fri Feb 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt9
- fix description list

* Thu Feb 01 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt8
- finally move old xconf backend to new x11 backend3
- simplify internal ui logic
- ddc reading optimization
- monitor_autosetup utility

* Wed Jan 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt7
- fix recommended depth calculation

* Wed Jan 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt6
- improve color depth support

* Wed Jan 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt5
- add support for autoinstall
- use ->bool from standard library

* Tue Jan 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt4
- fix message in monitor testing

* Tue Jan 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt3
- new monitor_scan and monitor_setup utilities

* Fri Jan 26 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- monitorinfo tool : update to latest ddcprobe utility
- ui: use auto-detected driver by default

* Mon Jan 22 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- new experimental monitor testing tool

* Thu Jan 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.6-alt4
- backend: fix work on xf86_64
- ui: don't fail on empty lists

* Wed Jan 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.6-alt3
- hotfix: in installer

* Wed Jan 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- new vcdb helper (now we show drivers not listed in Cards+)
- fix makefile: install-data, install-tools
- improve x11 backend: list only installed drivers
- x11 ui: start use new /x11 backend

* Tue Jan 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- improve experimental video card detection

* Mon Jan 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt8
- experimental functions for video cards auto detection
- minimal xorg.conf template

* Thu Jan 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt7
- fix requires

* Fri Dec 29 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt6
- fix typo

* Fri Dec 15 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt5
- another tunings for install3

* Thu Nov 30 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- tunings for install3

* Wed Nov 29 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- start xfs before start
- require xorg-x11-xfs

* Wed Nov 15 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- replace old setupgl call with a modern x11setupdrv

* Wed Nov 08 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- move icons to separate package (alterator-icons)
- update build system
- remove code to work with xkb settings
- update inittab backend

* Wed Jun 14 2006 Anton Farygin <rider@altlinux.ru> 0.4.5-alt1
- updated for new alterator

* Wed May 03 2006 Anton Farygin <rider@altlinux.ru> 0.4.4-alt1
- fixed for new alterator

* Tue Mar 21 2006 Anton Farygin <rider@altlinux.ru> 0.4.3-alt1
- fixed build

* Mon Feb 20 2006 Anton Farygin <rider@altlinux.ru> 0.4.2-alt1
- code fix

* Tue Feb 07 2006 Anton Farygin <rider@altlinux.ru> 0.4.1-alt1
- fixed layouts in monitor selection screen

* Tue Feb 07 2006 Anton Farygin <rider@altlinux.ru> 0.4-alt1
- updated to new alterator-2.6
- use QT4 for qyesno tool

* Fri Oct 21 2005 Anton Farygin <rider@altlinux.ru> 0.3.16-alt1
- icon for acc added

* Thu Oct 20 2005 Anton Farygin <rider@altlinux.ru> 0.3.15-alt1
- added icons

* Tue Sep 27 2005 Anton Farygin <rider@altlinux.ru> 0.3.14-alt1
- Sergey Turchin: quesno - improved look
- don't change keyboard layout in standalone and acc versions (#8042)
- multilib support (#7922)
- config-x11 now work from console (#7980)

* Tue Sep 20 2005 Anton Farygin <rider@altlinux.ru> 0.3.13-alt1
- Sergey Turchin: quesno - improved look

* Wed Sep 07 2005 Anton Farygin <rider@altlinux.ru> 0.3.12-alt1
- improve UI (zerg@)

* Tue Sep 06 2005 Anton Farygin <rider@altlinux.ru> 0.3.11-alt1
- set default runlevel to 5 if /var/lock/TMP_1ST exists

* Mon Sep 05 2005 Anton Farygin <rider@altlinux.ru> 0.3.10-alt1
- tatarian keyboards layouts added
- ui fixes
- added standalone version

* Fri Aug 19 2005 Anton Farygin <rider@altlinux.ru> 0.3.9-alt2
- data files moved to backend

* Fri Aug 19 2005 Anton Farygin <rider@altlinux.ru> 0.3.9-alt1
inger:
    - replace own empty? with general empty-string?
    - use zero? predicate

* Tue Aug 02 2005 Anton Farygin <rider@altlinux.ru> 0.3.8-alt1
- belarussian translations added (thanks to ...?)
- test button into standalone version fixed

* Thu Jul 14 2005 Anton Farygin <rider@altlinux.ru> 0.3.7-alt1
- russian help added (kirill@)
- qyesno timeout (10s) implemented (#7325)

* Mon Jul 11 2005 Anton Farygin <rider@altlinux.ru> 0.3.6-alt1
- apply autodetected for resolutions (#7309)

* Thu Jul 07 2005 Stanislav Ievlev <inger@altlinux.org> 0.3.5-alt1.1
- fixed map
- minor fixes in layout

* Tue Jul 05 2005 Anton Farygin <rider@altlinux.ru> 0.3.5-alt1
- fixed setgl parameters on changes testing (#6964)

* Mon Jul 04 2005 Anton Farygin <rider@altlinux.ru> 0.3.4-alt1
- fixed resolutions list

* Mon Jun 27 2005 Anton Farygin <rider@altlinux.ru> 0.3.3-alt1
- usability improved (#7155)
- xtest message rewrited (#7185)

* Mon Jun 20 2005 Anton Farygin <rider@altlinux.ru> 0.3.2-alt1
- added default runlevel configuration checkbox (x11 or console)
- fixed some bugs
- updated to new alterator
- added "auto" for resolutions list

* Wed Jun 08 2005 Anton Farygin <rider@altlinux.ru> 0.3.1-alt1
- updated russian translation

* Wed Jun 08 2005 Anton Farygin <rider@altlinux.ru> 0.3.0-alt1
- added dualhead workaround into xconf
- rewrited get-resolutions (lioka@)

* Tue Jun 07 2005 Anton Farygin <rider@altlinux.ru> 0.2.1-alt1
- fixed apply button for default values
- updated map for new wizard format

* Tue May 31 2005 Anton Farygin <rider@altlinux.ru> 0.2-alt1
- rewrited ui for new look
- separate select for monitors vendor and model
- restore position of selected values for monitor and drivers substeps
- unset XAUTHORITY before starting X (for testing from acc)
- show recomended monitor and video card settings
- restore color-depth from current config (default 24)
- get resolutions from monitor DDC (if available)
- setting up default resolutions for monitor from DDC
- show dialog after failed monitor test
- split package to backend and frontend

* Wed May 04 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt7
- new shapshot

* Thu Apr 28 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- replace Xdialog with qyesno

* Wed Apr 27 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- new snapshot

* Mon Apr 25 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- improved files layout

* Thu Apr 21 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- bugfixes

* Wed Apr 13 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- bugfixes

* Tue Apr 12 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial

