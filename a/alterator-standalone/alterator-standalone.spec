Name: alterator-standalone
Version: 7.4
Release: alt1

Summary: System Management center
License: GPL
Group: System/Configuration/Other

# The UI modules aren't currently compiled
BuildArch: noarch

Requires: alterator >= 5.0
Requires: alterator-l10n
Requires: alterator-lookout >= 2.5
Requires: alterator-browser-qt >= 2.11.6-alt1
Requires: consolehelper

#backward compatibility
Provides: acc = %version, alterator-profile = %version, %name-usermode = %version
Obsoletes: acc, alterator-profile, %name-usermode

Source: %name-%version.tar

BuildPreReq: alterator >= 5.0
BuildPreReq: guile

%description
ALTLinux Control Center
Contains engine for system management

%brp_strip_none %_alterator_libdir/*
%add_verify_elf_skiplist %_alterator_libdir/*
%add_findreq_skiplist %_alterator_libdir/*

%prep
%setup

%build
%make_build

%install
%makeinstall

#install consolehelper
for obj in acc alterator-standalone;
do
install -d %buildroot/%_bindir
ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/$obj
install -d %buildroot%_sysconfdir/pam.d/

cat>%buildroot%_sysconfdir/pam.d/$obj<<EOF
#%PAM-1.0
auth	sufficient	pam_rootok.so
auth	required	pam_stack.so service=system-auth
account	required	pam_permit.so
password	required	pam_deny.so
session	optional	pam_xauth.so
EOF

install -d %buildroot%_sysconfdir/security/console.apps/
cat>%buildroot%_sysconfdir/security/console.apps/$obj<<EOF
USER=root
PROGRAM=%_sbindir/$obj
SESSION=true
FALLBACK=true
EOF
done

install -Dpm644 acc.desktop %buildroot/%_desktopdir/acc.desktop

%files
%_sbindir/*
# The UI modules aren't currently compiled
#%_alterator_libdir/ui/*
%_alterator_datadir/ui/*
%_desktopdir/*
%_man8dir/*
%config(noreplace) %_sysconfdir/pam.d/*
%config(noreplace) %_sysconfdir/security/console.apps/*
%_bindir/*

%changelog
* Wed Aug 26 2020 Paul Wolneykien <manowar@altlinux.org> 7.4-alt1
- Allow to set mode change handler with 'frame:mode-onchange-set!'
  global variable.
- Store the expert mode flag in the global variable 'expert_mode'.
- Disable auto compilation of .scm files.

* Thu Dec 28 2017 Paul Wolneykien <manowar@altlinux.org> 7.3-alt1
- Fix: Load lookout AJAX module instead of the default (HTTP).

* Wed Dec 20 2017 Paul Wolneykien <manowar@altlinux.org> 7.2-alt3
- E2K fix: Require "guile" instead of "guileXX-devel" that is enough
  for noarch package.

* Thu Dec 07 2017 Paul Wolneykien <manowar@altlinux.org> 7.2-alt2
- Fix: The UI modules aren\'t currently compiled.

* Tue Apr 11 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.2-alt1
- rebuilt with guile22

* Thu Jul 21 2016 Sergey V Turchin <zerg@altlinux.org> 7.1.2-alt1
- change desktp-file icon
- update bugzilla url

* Sun Mar 24 2013 Andrey Cherepanov <cas@altlinux.org> 7.1.1-alt2
- Add Kazakh translation for System management center (ALT #28744)

* Fri Aug 19 2011 Andrey Cherepanov <cas@altlinux.org> 7.1.1-alt1
- Put acc in system configuration menu (closes: #26127)
- Show all available modules in alterator-standalone
- On missed module show module name and exit button

* Wed Feb 02 2011 Lenar Shakirov <snejok@altlinux.ru> 7.1-alt7
- some description added (ALT #20792)
- .gear-rules -> .gear/rules: cleaned too

* Wed Feb 02 2011 Lenar Shakirov <snejok@altlinux.ru> 7.1-alt6
- fix non standart Alterator category by adding X-ALTLinux- before

* Wed Feb 02 2011 Lenar Shakirov <snejok@altlinux.ru> 7.1-alt5
- acc.desktop cleaned: thanks to desktop-file-validate!

* Wed Feb 02 2011 Lenar Shakirov <snejok@altlinux.ru> 7.1-alt4
- package 'menu' removed from requires
- spec cleaned: thanks to rpmcs!

* Fri Aug 28 2009 Stanislav Ievlev <inger@altlinux.org> 7.1-alt3
- update for new alterator-lookout (closes: #21280)

* Thu Apr 16 2009 Stanislav Ievlev <inger@altlinux.org> 7.1-alt2
- update man-pages (mike@)

* Wed Apr 08 2009 Stanislav Ievlev <inger@altlinux.org> 7.1-alt1
- add support for expert_mode for menu
- add man pages

* Fri Feb 27 2009 Stanislav Ievlev <inger@altlinux.org> 7.0-alt1
- use help and translations directly from alterator-l10n
- remove obsolete macros

* Tue Dec 09 2008 Stanislav Ievlev <inger@altlinux.org> 6.1-alt1
- switch to guile-1.8

* Fri Sep 05 2008 Stanislav Ievlev <inger@altlinux.org> 6.0-alt1
- use alteratord

* Mon Aug 25 2008 Stanislav Ievlev <inger@altlinux.org> 5.0-alt5
- add 'ui "qt" to /menu backend call

* Mon Aug 25 2008 Stanislav Ievlev <inger@altlinux.org> 5.0-alt4
- add Tatar translation to desktop-file

* Thu Aug 21 2008 Stanislav Ievlev <inger@altlinux.org> 5.0-alt3
- add help for main window

* Wed Aug 06 2008 Stanislav Ievlev <inger@altlinux.org> 5.0-alt2
- more fast menu generation

* Tue Aug 05 2008 Stanislav Ievlev <inger@altlinux.org> 5.0-alt1
- new control center UI

* Thu Jul 31 2008 Stanislav Ievlev <inger@altlinux.org> 4.5-alt1
- requires alterator-browser-qt
- remove usermode subpackage
- use module.mak

* Sat Jun 07 2008 Stanislav Ievlev <inger@altlinux.org> 4.4-alt2
- improve ui layout

* Thu May 29 2008 Stanislav Ievlev <inger@altlinux.org> 4.4-alt1
- replace layout files with standalone scripts
- join to common translation database
- remove obsoleted standalone.mak

* Mon May 12 2008 Stanislav Ievlev <inger@altlinux.org> 4.3-alt2
- update to new alterator-menu

* Mon Apr 14 2008 Stanislav Ievlev <inger@altlinux.org> 4.3-alt1
- remove map files

* Mon Apr 14 2008 Stanislav Ievlev <inger@altlinux.org> 4.2-alt1
- use common /std/frame

* Fri Apr 11 2008 Stanislav Ievlev <inger@altlinux.org> 4.1-alt1
- update to new alterator-lookout

* Mon Mar 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 4.0-alt5
- remove layout-policy attribute (bug #14945)

* Wed Mar 12 2008 Vladislav Zavjalov <slazav@altlinux.org> 4.0-alt4
- remove alterator-profile sub-package

* Tue Jan 15 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt3
- resurrect old alterator-standalone (single module runner)

* Thu Jan 10 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt2
- improve UI: add label with information about F1 button
- add title to window
- desktop file: improve translation

* Sat Jan 05 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt1
- add support for help
- remove unused utilities, rename and simplify map and layout files

* Fri Jun 15 2007 Stanislav Ievlev <inger@altlinux.org> 3.0-alt3
- fix requires

* Thu Jun 14 2007 Stanislav Ievlev <inger@altlinux.org> 3.0-alt2
- specify ui type 'qt' for menu subsystem

* Wed Jun 13 2007 Stanislav Ievlev <inger@altlinux.org> 3.0-alt1
- switch to new menu system

* Mon Jun 04 2007 Stanislav Ievlev <inger@altlinux.org> 2.6-alt3
- use splitbox

* Thu May 31 2007 Stanislav Ievlev <inger@altlinux.org> 2.6-alt2
- ignore skip messages (will use if for GUI only interfaces)

* Wed May 30 2007 Stanislav Ievlev <inger@altlinux.org> 2.6-alt1
- rewrite:
    synchronize menu structure with html modules
    drop profiles

* Wed May 02 2007 Stanislav Ievlev <inger@altlinux.org> 2.5-alt15
- update Ukrainian translation

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 2.5-alt14
- add Ukrainian translation

* Wed Mar 14 2007 Stanislav Ievlev <inger@altlinux.org> 2.5-alt13
- add support for 'acc-translation profile parameter

* Mon Feb 05 2007 Stanislav Ievlev <inger@altlinux.org> 2.5-alt12
- replace /std/vbox with /std/box

* Wed Jan 10 2007 Stanislav Ievlev <inger@altlinux.org> 2.5-alt11
- select profile: don't use woo-extract-name

* Fri Dec 22 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt10
- explicit requirement for (lookout atlas) in layout

* Fri Dec 15 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt9
- move menu dependency to usemode package

* Fri Dec 08 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt8
- update to latest alterator

* Thu Dec 07 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt7
- add usermode subpackage

* Tue Dec 05 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt6
- fix args passing

* Fri Dec 01 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt5
- add browser to requires

* Thu Nov 23 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt4
- on start loaded event simulation

* Mon Nov 20 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt3
- replace qtbrowser with alterator-browser-x11

* Fri Nov 10 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt2
- /std/frame : add wizard compatible functions
- add examples
- cond-plistq in algo library now
- fix problem with parameters dropping

* Wed Nov 08 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt1
- use native message boxes

* Tue Oct 31 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.5
- update backend2 for the new alterator

* Mon Oct 16 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.4
- replace command-arg-ref with woo-get-option

* Fri Sep 29 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.3
- auto generate simple map
- update build system

* Wed Sep 27 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.2
- rename caption to title

* Wed Sep 06 2006 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.1
- final version of desktop menu support

* Fri Sep 01 2006 Stanislav Ievlev <inger@altlinux.org> 2.4-alt0.10
- fixed layout according new rules
- create profile and desktop files during build process
- added XDG config files for alterator configurator submenu

* Fri Aug 25 2006 Stanislav Ievlev <inger@altlinux.org> 2.4-alt0.9
- fixed buttons-view cleanup
- fixed auto profile creation

* Wed Aug 23 2006 Stanislav Ievlev <inger@altlinux.org> 2.4-alt0.8
- update build system

* Tue Jun 27 2006 Stanislav Ievlev <inger@altlinux.org> 2.4-alt0.7
- updated to new lookout definition syntax

* Fri Jun 09 2006 Stanislav Ievlev <inger@altlinux.org> 2.4-alt0.6
- added support for alterator help subsystem

* Tue May 30 2006 Stanislav Ievlev <inger@altlinux.org> 2.4-alt0.5
- fixed for new alterator

* Wed May 17 2006 Stanislav Ievlev <inger@altlinux.org> 2.4-alt0.4
- fixed backend

* Mon May 15 2006 Stanislav Ievlev <inger@altlinux.org> 2.4-alt0.3
- removed unused admirals

* Wed May 10 2006 Stanislav Ievlev <inger@altlinux.org> 2.4-alt0.2
- fixed bug with dublicates in module list
- removed deprecated features
- build from git

* Tue Apr 18 2006 Stanislav Ievlev <inger@altlinux.org> 2.4-alt0.1
- now provide acc (profile with all modules)

* Tue Apr 18 2006 Stanislav Ievlev <inger@altlinux.org> 0.4-alt0.2
- added expansion of uris

* Thu Apr 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.4-alt0.1
- allow to work with local profile files

* Tue Apr 04 2006 Stanislav Ievlev <inger@altlinux.org> 0.3-alt0.2
- use help-place widget

* Fri Mar 24 2006 Stanislav Ievlev <inger@altlinux.org> 0.3-alt0.1
- move /std/frame here
- replace document:link with document:insert

* Mon Feb 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.2-alt0.1
- updated backend2 system

* Thu Feb 09 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.9
- minor fixes

* Tue Feb 07 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.8
- new subpackage for profile engine

* Thu Feb 02 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.7.1
- update to new alterator

* Wed Feb 01 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.7
- module changing are ready now

* Tue Jan 31 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.6.1
- added save facility

* Tue Jan 31 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.6
- edit mode improvements

* Fri Jan 27 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.5.1
- added tooltip demo

* Wed Jan 25 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.5
- first version of edit dialog

* Tue Jan 24 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.4
- added module loader/selector

* Mon Jan 23 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.3
- move to new frame scheme

* Fri Jan 20 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.2
- interface improvements, added russian translations

* Thu Jan 19 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt0.1
- initial release

