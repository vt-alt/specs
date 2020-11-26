Name: userpasswd
Version: 0.3.3
Release: alt4

Group: System/Configuration/Other
Summary: The graphical tool for changing password
License: GPLv2+
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: %name-%version.tar

Requires: pam0_tcb >= 1.1.0.1
Conflicts: usermode
BuildRequires: libgtk+2-devel


%description
Install this package if you would like to provide users with
graphical tool for changing password.

%prep
%setup -q

%build
%make_build

%install
%make_install install menudir=%_desktopdir

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_datadir/pixmaps/*

%changelog
* Wed Nov 25 2020 Fr. Br. George <george@altlinux.ru> 0.3.3-alt4
- Fix message comparison fail that prevents GUI from start (Closes: #37456)

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Wed Dec 19 2018 Michael Shigorin <mike@altlinux.org> 0.3.3-alt2
- drop %%ubt

* Mon Sep 11 2017 Michael Shigorin <mike@altlinux.org> 0.3.3-alt1%ubt
- E2K: avoid a (trivial) nested function

* Mon Apr 24 2017 Evgeny Sinelnikov <sin@altlinux.ru> 0.3.2-alt1%ubt
- Support for New and Reenter new Password for pam_sss

* Wed Mar 29 2017 Evgeny Sinelnikov <sin@altlinux.ru> 0.3.1-alt1%ubt
- Support sssd password with pam_sss

* Thu Feb 23 2017 Evgeny Sinelnikov <sin@altlinux.ru> 0.3.0-alt1%ubt
- Support Kerberos password with pam_krb5

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.10-alt3.qa1
- NMU: rebuilt for debuginfo.

* Wed Sep 09 2009 Sergey V Turchin <zerg@altlinux.org> 0.2.10-alt3
- using desktop-file for applications menu (closes: 21505)

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 0.2.10-alt2
- Removed obsolete %%update_menus/%%clean_menus calls.

* Wed Oct 29 2008 Dmitry V. Levin <ldv@altlinux.org> 0.2.10-alt1
- Fixed build with fresh glibc.

* Tue Mar 07 2006 Dmitry V. Levin <ldv@altlinux.org> 0.2.9-alt1
- Fixed build with --as-needed.

* Mon Nov 21 2005 Dmitry V. Levin <ldv@altlinux.org> 0.2.8.2-alt1
- Relocated %_libdir/%name to %_datadir/%name (fixes #8506).

* Wed Jun 22 2005 Dmitry V. Levin <ldv@altlinux.org> 0.2.8.1-alt1
- Corrected potential bug introduced in previous release.

* Mon Apr 18 2005 Dmitry V. Levin <ldv@altlinux.org> 0.2.8-alt1
- Updated ui code for GTK2.

* Thu Feb 26 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.7-alt3
- Rebuilt.

* Thu May 08 2003 Stanislav Ievlev <inger@altlinux.ru> 0.2.7-alt2
- more beautiful icons

* Wed Feb 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.7-alt1
- Set dialog type to GTK_WINDOW_POPUP.
- Activate passwd entry widget by default.

* Mon Jan 27 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.6-alt1
- Added loop script for menu.

* Sat Oct 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.5-alt1
- 0.2.5 (fixed gtk_widget_grab_default problem).

* Wed Oct 09 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt2
- Rebuilt with gtk 2.1

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.4-alt1
- Moved to gtk2.
- Added buildrequires.

* Fri Jun 21 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.3-alt1
- 0.2.3

* Fri Jun 07 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.2-alt2
- fixed suxx centering

* Tue Mar 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2.2-alt1
- 0.2.2

* Sun Mar 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2.1-alt1
- Dropped all but userpasswd.
- Added grab focus logic.

* Wed Feb 27 2002 Stanislav Ievlev <inger@altlinux.ru> 1.43-alt2
- added true version of userpasswd
- dropped usermount and userinfo

* Wed Sep 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.43-alt1
- 1.43 (updated translations).

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.42-alt3
- Provides: consolehelper (until real consolehelper package appearance).

* Fri Aug 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.42-alt2
- Fixed latest sanitize_env patch.

* Wed Aug 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.42-alt1
- Specfile cleanup.
- Dropped outdated translations from mdk coz original are better.
- Dropped outdated mdk patches.
- Moved SysVinit stuff back to SysVinit package.
- Relocated %_sbindir/userhelper and %_bindir/consolehelper
 to %_libdir/helper/ according to FHS.
- Added progname patch.
- Added sanitize_env patch.
- Added getlogin patch.
 Here we need at most consolehelper and gui wrappers,
 all the rest will go into shadow-utils or like.

* Wed Jul 11 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.42-2mdk
- Use more macros
- Remove source 1, 2 + menu entry (not needed)
- Shutdown tools are back (conflict with msec < 0.15-17mdk)
- Call msec at install time if installed

* Tue May 22 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.42-1mdk
- Bump a nice and tasty 1.42 out for cooker.
- s/Copyright/License/;

* Tue Apr 10 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.37-5mdk
- Update patch 2 for better INITIAL_USER handling

* Mon Apr 09 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.37-4mdk
- included latest translations

* Tue Apr 03 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.37-3mdk
- Update patch 2 to set INITIAL_USER and BROWSER variable

* Wed Nov 29 2000 Geoffrey lee <snailtalk@mandrakesoft.com> 1.37-2mdk
- use optflags.

* Fri Nov 10 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.37-1mdk
- bump up version for security fix. (RH).

* Tue Oct 10 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.36-2mdk
- patch to set some more environment variables

* Tue Oct 10 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.36-1mdk
- bump up version for security fix. (RH)

* Mon Oct 09 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.35-5mdk
- updated French, Spanish, etc. translations

* Mon Oct 09 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.35-4mdk
- included translations into the rpm; and added new ones (new ones still
 very incomplete)

* Mon Oct 09 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.35-3mdk
- set gid also when no session

* Fri Oct 06 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.35-2mdk
- patch in userhelper to set gid when executing a foreign program
 (-w option) (thanks to Fred Lepied)

* Thu Sep 28 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.35-1mdk
- Release 1.35

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.22-4mdk
- automatically added BuildRequires

* Wed Aug 02 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.22-3mdk
- macroszifications
- Makefile patch for new manpage location
- BM

* Tue Jul 18 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.22-2mdk
- remove pam console wrappers (security fix)

* Sat Apr 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.22-1mdk
- updated to new version
- updated group information
- added menu code
- There are no doc files available.

* Thu Mar 09 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix problem parsing userhelper's -w flag with other args

* Wed Mar 08 2000 Nalin Dahyabhai <nalin@redhat.com>
- ignore read() == 0 because the child exits

* Tue Mar 07 2000 Nalin Dahyabhai <nalin@redhat.com>
- queue notice messages until we get prompts in userhelper to fix bug #8745

* Thu Feb 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- free trip through the build system

* Tue Jan 11 2000 Nalin Dahyabhai <nalin@redhat.com>
- grab keyboard input focus for dialogs

* Fri Jan 07 2000 Michael K. Johnson <johnsonm@redhat.com>
- The root exploit fix created a bug that only showed up in certain
 circumstances. Unfortunately, we didn't test in those circumstances...

* Mon Jan 03 2000 Michael K. Johnson <johnsonm@redhat.com>
- fixed local root exploit

* Thu Sep 30 1999 Michael K. Johnson <johnsonm@redhat.com>
- fixed old complex broken gecos parsing, replaced with simple working parsing
- can now blank fields (was broken by previous fix for something else...)

* Tue Sep 21 1999 Michael K. Johnson <johnsonm@redhat.com>
- FALLBACK/RETRY in consolehelper/userhelper
- session management fixed for consolehelper/userhelper SESSION=true
- fix memory leak and failure to close in error condition (#3614)
- fix various bugs where not all elements in userinfo got set

* Mon Sep 20 1999 Michael K. Johnson <johnsonm@redhat.com>
- set $HOME when acting as consolehelper
- rebuild against new pwdb

* Tue Sep 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- honor "owner" flag to mount
- ask for passwords with username

* Tue Jul 06 1999 Bill Nottingham <notting@redhat.com>
- import pam_console wrappers from SysVinit, since they require usermode

* Mon Apr 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- even better check for X availability

* Wed Apr 07 1999 Michael K. Johnson <johnsonm@redhat.com>
- better check for X availability
- center windows to make authentication easier (improve later with
 transients and embedded windows where possible)
- applink -> applnk
- added a little padding, especially important when running without
 a window manager, as happens when running from session manager at
 logout time

* Wed Mar 31 1999 Michael K. Johnson <johnsonm@redhat.com>
- hm, need to be root...

* Fri Mar 19 1999 Michael K. Johnson <johnsonm@redhat.com>
- updated userhelper.8 man page for consolehelper capabilities
- moved from wmconfig to desktop entries

* Thu Mar 18 1999 Michael K. Johnson <johnsonm@redhat.com>
- added consolehelper
- Changed conversation architecture to follow PAM spec

* Wed Mar 17 1999 Bill Nottingham <notting@redhat.com>
- remove gdk_input_remove (causing segfaults)

* Tue Jan 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- fix missing include files

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- use defattr
- fix spec file ( rm -rf $(RPM_BUILD_ROOT) is a stupid thing to do ! )

* Tue Oct 06 1998 Preston Brown <pbrown@redhat.com>
- fixed so that the close button on window managers quits the program properly

* Thu Apr 16 1998 Erik Troan <ewt@redhat.com>
- use gtk-config during build
- added make archive rule to Makefile
- uses a build root

* Fri Nov 07 1997 Otto Hammersmith <otto@redhat.com>
- new version that fixed memory leak bug.

* Mon Nov 03 1997 Otto Hammersmith <otto@redhat.com>
- updated version to fix bugs

* Fri Oct 17 1997 Otto Hammersmith <otto@redhat.com>
- Wrote man pages for userpasswd and userhelper.

* Tue Oct 14 1997 Otto Hammersmith <otto@redhat.com>
- Updated the packages... now includes userpasswd for changing passwords
 and newer versions of usermount and userinfo. No known bugs or
 misfeatures.
- Fixed the file list...

* Mon Oct 06 1997 Otto Hammersmith <otto@redhat.com>
- Created the spec file.
