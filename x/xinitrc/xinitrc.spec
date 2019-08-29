Name: xinitrc
Version: 2.4.47
Release: alt2

Summary: The default startup scripts for the X Window System
License: GPL
Group: System/X11

Source: %name-%version.tar

Provides: %_sysconfdir/X11/xinit.d, %_sysconfdir/X11/wmsession.d, %_sysconfdir/X11/wms-methods.d
Provides: %_sysconfdir/X11/xsession.user.d
Requires: app-defaults >= 0:0.2, xvt
Conflicts: kde-settings < 3.1.0-alt3, kdebase < 3.0.2-alt5, kde-config < 1.0-alt5
Conflicts: initscripts < 1:5.49.1-alt1
Conflicts: systemd < 1:214-alt8

%description
The %name package contains system scripts used to start
X Window System session.

%prep
%setup

%build
%make_build -C po
make -C src rundm CFLAGS="%optflags"

%install
install -pD -m755 src/rundm %buildroot%_sbindir/rundm
mkdir -p %buildroot%_sysconfdir/X11/wmsession.d
mkdir -p %buildroot%_sysconfdir/X11/wms-methods.d
mkdir -p %buildroot%_sysconfdir/X11/xsession.user.d

cp -av install/* %buildroot/
%make_install install -C po
%find_lang xrootwarn

%post
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add dm
fi
if grep -qs '^x:5:' /etc/inittab; then
	/sbin/chkconfig --add dm
	sed -i 's/^x:5:/#x:5:/' /etc/inittab
fi

%preun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del dm
fi

%triggerpostun -- initscripts < 1:5.49.1-alt1
/sbin/chkconfig --add dm

%triggerun -- xinitrc < 2.4.39
/sbin/chkconfig --del update_wms

%files -f xrootwarn.lang
%_sbindir/*
%_bindir/*
%_sysconfdir/X11/wmsession.d
%_sysconfdir/X11/wms-methods.d
%_sysconfdir/X11/xsession.user.d
%_rpmlibdir/*
%_initdir/*
%_unitdir/*
%config %_sysconfdir/X11/Xsession
%config %_sysconfdir/X11/prefdm
%config(noreplace) %_sysconfdir/sysconfig/*
%config(noreplace) %_sysconfdir/X11/xinit*
%config(noreplace) %_sysconfdir/X11/xdm/*

%changelog
* Thu Aug 15 2019 Paul Wolneykien <manowar@altlinux.org> 2.4.47-alt2
- Allow to run WM by a command name not by an abstract name (closes:
  #36913).

* Tue Feb 14 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.4.47-alt1
- allow to choose selinux level (zerg@)

* Thu Oct 20 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.46-alt1
- fixkeyboard: drop old XKB layout options instead of just appending the new.

* Fri Jul 08 2016 Dmitry V. Levin <ldv@altlinux.org> 2.4.45-alt1
- xserverrc: fix typo introduced in 2.4.44-alt1 (closes: #32258).

* Wed Jul 06 2016 Dmitry V. Levin <ldv@altlinux.org> 2.4.44-alt1
- xserverrc: specify -auth option to Xserver.

* Mon Sep 07 2015 Sergey V Turchin <zerg@altlinux.org> 2.4.43-alt1
- runwm: add common Xsession compatibility (closes: #31259).

* Sat Apr 18 2015 Michael Shigorin <mike@altlinux.org> 2.4.42-alt1
- prefdm: added SDDM support by zerg@ (closes: #30943).

* Fri Feb 06 2015 Anton Farygin <rider@altlinux.ru> 2.4.41-alt3
- conflict with plymouth-quit.service removed (closes: #30288)

* Thu Jul 03 2014 Alexey Shabalin <shaba@altlinux.ru> 2.4.41-alt2
- add alias display-manager.service for prefdm.service

* Tue Jul 01 2014 Alexey Shabalin <shaba@altlinux.ru> 2.4.41-alt1
- add systemd unit prefdm.service

* Mon Mar 24 2014 Michael Shigorin <mike@altlinux.org> 2.4.40-alt1
- xrootwarn.real: fallback from gxmessage to xmessage,
  no need to pull libgtk+2 with all the family in (see #28111).

* Thu Mar 07 2013 Dmitry V. Levin <ldv@altlinux.org> 2.4.39-alt1
- xrootwarn: replaced xmessage with gxmessage (closes: #28111).
- Dropped no longer needed update_wms startup script (closes: #28103).

* Mon Jan 21 2013 Dmitry V. Levin <ldv@altlinux.org> 2.4.38-alt1
- prefdm: added E17/entrance support (closes: #28399).

* Mon Sep 24 2012 Dmitry V. Levin <ldv@altlinux.org> 2.4.37-alt1
- prefdm: added MATE support (closes: #27611).

* Tue Jun 26 2012 Michael Shigorin <mike@altlinux.org> 2.4.36-alt1
- prefdm: Added nodm support by Max Kosmach (closes: #27449).

* Sat Aug 06 2011 Evgeny Sinelnikov <sin@altlinux.ru> 2.4.35-alt1
- Xsession: add xsession.user.d for fixed wm program per user
  (closes #18316).

* Tue May 17 2011 Mykola Grechukh <gns@altlinux.ru> 2.4.34-alt2
- prefdm: Added lightdm support.
- xserver: Do not listen tcp (by Alexey Gladkov).

* Tue May 18 2010 Dmitry V. Levin <ldv@altlinux.org> 2.4.34-alt1
- prefdm: Added lxdm support (by Nick S. Grechukh, closes: #23424).

* Thu Apr 09 2009 Igor Vlasenko <viy@altlinux.ru> 2.4.33-alt1
- added explicit Provides: of %_sysconfdir/X11/wms-methods.d

* Fri Apr 03 2009 Igor Vlasenko <viy@altlinux.ru> 2.4.32-alt1
- NMU: implemented Display Manager Policy
  (http://www.altlinux.org/Display_Manager_Policy)

* Thu Nov 20 2008 Dmitry V. Levin <ldv@altlinux.org> 2.4.31-alt1
- Implemented posttrans filetrigger for WM registration.
- update_wms: Changed to exit when executed during rpm package install.

* Tue Nov 11 2008 Dmitry V. Levin <ldv@altlinux.org> 2.4.30-alt1
- fixkeyboard: Run xmodmap also in case when XKEYBOARD extension
  is enabled (shrek).

* Fri Aug 29 2008 Dmitry V. Levin <ldv@altlinux.org> 2.4.29-alt1
- runwm: Fixed failsafe mode (closes: #16820).

* Thu Jan 17 2008 Alexey Gladkov <legion@altlinux.ru> 2.4.28-alt1
- Add xrandr 1.2 support (#13955).
  See /etc/sysconfig/xrandr for more information.
- %_sysconfdir/X11/xinit/xserverrc: Add two parameters:
  + IGNORE_ABI - disable ABI check;
  + DEPTH - sets the default color depth.

* Tue Dec 25 2007 Alexey Gladkov <legion@altlinux.ru> 2.4.27-alt1
- Add Xorg server startup arguments customization (#12403).
  See /etc/sysconfig/xserver for more information.
- %_sysconfdir/X11/xdm/Xsetup_0: Add two parameters
  into /etc/sysconfig/xinitrc:
  + XSETROOT - define xsetroot command;
  + XCONSOLE - enables xconsole run.
- prefdm uses system i18n settings (#10981).
- Fix xrootwarn message.

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 2.4.26-alt1
- Removed cvsid tags.
- runwm: Replaced "xterm" with "xvt" (#12773).

* Fri Mar 03 2006 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt1
- %_sysconfdir/X11/xinit/fixkeyboard:
  + Enabled system xkb map support (#9177).
  + Removed obsolete stuff.
- Removed obsolete %_sysconfdir/X11/xinit/Xmodmap.

* Sat Jan 07 2006 Dmitry V. Levin <ldv@altlinux.org> 2.4.24-alt1
- Changed all scripts to avoid full paths to programs.
- Moved all utilities to %_bindir/.

* Fri Sep 30 2005 Dmitry V. Levin <ldv@altlinux.org> 2.4.23-alt1
- %_sysconfdir/X11/xdm/Xresources: Added Xcursor.theme (closes #7324).
- %_x11bindir/xscreenlock: Handle new XSS paths (closes #7617).
- %_x11bindir/runwm: When looking for default WM,
  honor /etc/sysconfig/desktop value (closes #8057).

* Sat Jun 12 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4.22-alt1
- update_wms: deal with strange wm names (fixes #3907).
- Xsession, runwm, init.d/dm: do not use absolute pathnames
  where it is not necessary.

* Thu Jun 03 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4.21-alt1
- update_wms: updated new GDM scheme support, by aris@ (#3907).

* Tue Jun 01 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4.20-alt1
- update_wms: added new GDM scheme support, by aris@ (#3907).
- Xsession: updated TryXBrowser list (#4232).

* Mon Nov 03 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.19-alt1
- /etc/X11/xinit/xrootwarn.real: run xmessage with "-font fixed".

* Tue Oct 14 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.18-alt1
- /etc/X11/xinit/xserverrc: new file.
- /etc/X11/xdm/Xservers: use it.

* Fri Aug 22 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.17-alt1
- /etc/X11/xdm/Xservers, /etc/X11/prefdm:
  reverted #0002531 workarounds.
- %_sbindir/rundm: added dev list support.
- %_initdir/dm: pass dev list to rundm.

* Fri Aug 15 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.16-alt1
- /etc/X11/prefdm:
  added vt7 argument to autologin, to workaround #0002531.
  
* Wed Aug 06 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.15-alt1
- /etc/X11/xdm/Xservers:
  added vt7 argument, to workaround #0002531.

* Mon Jun 09 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.14-alt2
- Provides: %_sysconfdir/X11/wmsession.d

* Tue Jun 03 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.14-alt1
- init.d/update_wms: fixed $LOCKFILE handling.

* Wed May 21 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.13-alt1
- Added %_initdir/update_wms.
- Ported %_initdir/dm to new rc scheme.
- Added %_sysconfdir/X11/xinit.d to provides list.

* Tue Apr 22 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.12-alt1
- Relocated dm stuff from initscripts to this package.

* Fri Jan 24 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.11-alt1
- %_x11bindir/xscreenlock: new wrapper for xscreensaver/xlockmore.

* Tue Jan 21 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.10-alt1
- update_wms: updated.
- ru.po: updated xrootwarn translation.

* Fri Nov 15 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.9-alt1
- Xsession: pass args to scripts (#0001560).
- xrootwarn: workaround bash bug.

* Mon Nov 11 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.8-alt1
- Fixed system Xsession problem (#0000772).
- Fixed /etc/X11/xdm/Xresources (#0000965).
- Fixed autostart problem (#0001430).
- [INCOMPATIBLE] Changed user autostart directory to ~/.xsession.d/ (#0001431).
- Added sourcing of user ~/.xprofile file.
- Implemented xrootwarn.

* Wed Apr 10 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.7-alt1
- runwm: added --print option.
- Xsession: exec runwm default (#0000812).
- Set %_sysconfdir/X11/Xsession to %%config.

* Mon Mar 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.6-alt1
- update_wms: fixed GDM session generation (reported by Alexey Morozov).
- Xsession: redirect stderr to "~/.xsession-errors$DISPLAY".
- Xsession: source shell scripts from /etc/X11/profile.d/*.sh.
- Repackaged sources.

* Mon Feb 18 2002 Stanislav Ievlev <inger@altlinux.ru> 2.4.5-alt3
- Xresources moved into new app-defaults package

* Tue Feb 12 2002 Ivan Zakharyaschev <imz@altlinux.ru> 2.4.5-alt2.2
- change the License: Public Domain -> GPL (beacuse Xresources are under GPL)

* Mon Feb 11 2002 Ivan Zakharyaschev <imz@altlinux.ru> 2.4.5-alt2.1
- Xresources: sync with emacs-21.1-alt10 app-defaults

* Mon Jan 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.5-alt2
- Xsession: added support for forthcoming Xresources.* config files.

* Thu Jan 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.5-alt1
- runwm: return native WM names for "--list" option.
- update_wms: added WDM support.

* Wed Jan 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.5-alt0.1
- Rewritten wmsession.d support.

* Tue Apr 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.4-ipl38mdk
- Fixed Xsession to keep user-defined PATH.

* Wed Mar 07 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.4-ipl37mdk
- /etc/X11/Xsession: execute as bash script.
- /etc/X11/Xresources: added wheel mouse translations for netscape.

* Fri Feb 16 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.4-ipl36mdk
- /etc/X11/Xsession: source /etc/profile.d/lang.sh

* Wed Feb 14 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.4-ipl35mdk
- Merged in patch from AEN.

* Sat Dec 30 2000 Dmitry V. Levin <ldv@fandra.org> 2.4.4-ipl34mdk
- Script cleanup.
- RE adaptions.

* Tue Dec 26 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.4-34mdk
- xinitrc-Mod_Meta_L_Disable: Add this ugly script, when a
  REMOVE_MOD_META_L=yes remove the MOD_META_L to make some
  applications happy (ie:xemacs).

* Tue Nov 28 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-33mdk
- added support for ssh2 (bug #871).
- use bash -login only on Xsession for xdm (bug #1505).

* Fri Oct 13 2000 Pablo Saratxaga <pablo@manderakesoft.com> 2.4.4-32mdk
- added auto-launching of XIM servers.

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 2.4.4-31mdk
- Set HELP_BROWSER

* Mon Oct  2 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-30mdk
- removed ^@ in /etc/X11/Xsession.

* Mon Oct  2 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-29mdk
- remove xhost+ in /etc/X11/Xsession (let msec do this job).

* Tue Sep 12 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-28mdk
- fix resources to make xdm starts the X server only once and let init do its job.

* Fri Sep 01 2000 David BAUDENS <baudens@mandrakesoft.com> 2.4.4-27mdk
- Use Linux-Mandrake colors for xsetroot

* Wed Aug 30 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.4.4-26mdk
- Xsetup_0: commented out the kdmdesktop and added line to fix background colors

* Tue Jun  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.4-25mdk
- Xsession: Resinsert /bin/bash -login.

* Mon Jun  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.4-24mdk
- Xsession: use /bin/sh instead of /bin/bash -login.

* Thu May  4 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-23mdk
- fix path of WindowMaker in RunWM.

* Thu Apr 27 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-22mdk
- added a fallback /etc/X11/xdm/Xsession.

* Thu Apr 20 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-21mdk
- Xsession: merge ~/.Xdefaults too.

* Thu Apr 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.4-20mdk
- xinitrc-RunWM: set wmaker to the right path (thanks
  john.cavan@sympatico.ca).

* Tue Apr 11 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-18mdk
- launch scripts in /etc/X11/xinit.d
- removed imwheel stuff.

* Fri Apr  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.4-18mdk
- Cvs import clean up spec file.

* Thu Apr  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.4-17mdk
- Another fix of Xsession.

* Thu Apr  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.4-16mdk
- Try to get chksession feature when launching with startx (aka:
  fix merge of flepied).

* Thu Apr  6 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.4.4-15mdk
- smaller xterm in Xsession for failsafe setting, in order
  to stay in screen when having 800x600

* Thu Mar 30 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-14mdk
- activate imwheel only if WHEEL is yes in /etc/sysconfig/mouse.
- end the merge of xinit and xdm startup.

* Thu Mar 09 2000 Francis Galiegue <francis@mandrakesoft.com> 2.4.4-13mdk
- imwheel -k added to Xsession

* Wed Mar  1 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-12mdk
- make Xsession ssh aware.

* Mon Feb  7 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-11mdk

- unified xdm and startx init sequences.

* Thu Jan  6 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-10mdk

- load xmodmaps the same way in xinit and xdm modes.

* Wed Dec 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Do an exec for chksession. (c) Chmouel.

* Wed Dec 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Do an exec (flepied).

* Wed Dec 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Xsession and Xclients for new chksession.

* Tue Dec 21 1999 Frederic Lepied <flepied@mandrakesoft.com> 2.4.4-5mdk

- fix RunWM for WindowMaker.
- fix Xclients to be able to launch something else than KDE, GNOME or AnotherLevel.

* Thu Dec 16 1999 Frederic Lepied <flepied@mandrakesoft.com>

- fixed a typo in /etc/X11/xinit/xinitrc.

* Wed Nov 24 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- By default if there is no windows manager launch icewm-light no fvwm.
- Put a midnight color by default.

* Wed Nov  3 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add xmodmap files.
- 2.4.4.

* Thu Jul 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add Xsession files.
- Oups typo :-((

* Sun May 09 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- By default we run kde (again 8-)

* Mon May 03 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adpatations.
- By default Mandrake launch KDE.

* Mon Apr 19 1999 Preston Brown <pbrown@redhat.com>
- argh, fixed my changes from yesterday

* Sun Apr 18 1999 Preston Brown <pbrown@redhat.com>
- added /etc/sysconfig/desktop support

* Mon Mar 22 1999 Bill Nottingham <notting@redhat.com>
- make /etc/X11/xinit/* %%config (bug #1051)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Tue Feb 02 1999 Preston Brown <pbrown@redhat.com>
- added ability to have KDE recognized if it is all that is installed

* Wed Jan 27 1999 Preston Brown <pbrown@redhat.com>
- updated so that GNOME is the default, and a few other cleanups

* Fri Sep 18 1998 Cristian Gafton <gafton@redhat.com>
- added the RunWM script and modified Xclients to use this new script

* Sun Sep 13 1998 Cristian Gafton <gafton@redhat.com>
- included WindowMaker hints

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 22 1998 Cristian Gafton <gafton@redhat.com>
- handle AfterStep (and possibly other window managers)

* Tue Nov 11 1997 Michael K. Johnson <johnsonm@redhat.com>
- export the BROWSER variable.

* Fri Nov 08 1997 Cristian Gafton <gafton@redhat.com>
- added handling for the BROWSER variable

* Wed Oct 15 1997 Cristian Gaftin <gafton@redhat.com>
- updated for AnotherLevel

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built for glibc, added dependencies

* Thu Mar 20 1997 Erik Troan <ewt@redhat.com>
- Added /etc/X11/xinitrc/Xclients to this file and removed it from rootfiles
  and etcskel.
