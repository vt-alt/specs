%define _altdata_dir %_datadir/alterator

Name: alterator-xkb
Version: 3.1
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

Source:%name-%version.tar

Summary: alterator module for XKB administration
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 3.9-alt3 alterator-sh-functions >= 0.1-alt4
Requires: setxkbmap, xkeyboard-config >= 1.2-alt1, xinitrc
Conflicts: alterator-lookout < 2.0-alt2
Conflicts: alterator-fbi < 5.15-alt1

BuildPreReq: alterator >= 3.9-alt3

# Automatically added by buildreq on Wed Jun 20 2007
BuildRequires: alterator-fbi libexpat-devel

%description
alterator module for XKB administration

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_bindir/*
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*

%changelog
* Tue May 28 2019 Paul Wolneykien <manowar@altlinux.org> 3.1-alt1
- Backend update: Filter only the "grp:" options.
- New static XKB rules parser: whitelist XML path check.
- Makefile: Fixed error checking.
- Fix/improve: Unconditionally free the XML parser on exit.

* Mon Feb 18 2019 Paul Wolneykien <manowar@altlinux.org> 3.0-alt3
- Workaround ALTBUG #35797: replace ';' with ',' in the enumerated
  data (closes: #35797).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.0-alt2.qa1
- NMU: rebuilt for debuginfo.

* Mon Oct 12 2009 Stanislav Ievlev <inger@altlinux.org> 3.0-alt2
- fix desktop file (closes: #21757)

* Wed May 13 2009 Stanislav Ievlev <inger@altlinux.org> 3.0-alt1
- replace card-index and special workflow xkb with ajax and
  new form library.

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.1-alt2
- move translations to alterator-l10n

* Thu Jan 15 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt1
- update for new workflow

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt8
- fix work with empty model value

* Fri Sep 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 2.0-alt7
- build with new alterator-l10n

* Fri Sep 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 2.0-alt6
- change label in desktop-file (Keyboard settings -> Keyboard)

* Mon Sep 15 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt5
- update workflow for latest alterator-fbi

* Tue Sep 09 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt4
- update workflow for latest alterator-fbi

* Fri Aug 15 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt3
- redesign workflow as a native guile module

* Mon Aug 11 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- use enumref
- backend: alterator_api_version=1
- improve ui file layout
- improve ui according common HIG

* Fri Aug 08 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- update module for new alterator

* Thu Mar 20 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- update for new xkeyboard-config database format
- detect xml parsing errors
- remove template-*

* Tue Oct 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt3
- fix Xkbmap writing (don't use quotes)
- remove unused options from xkbmapconf utility
- write data in modern xkb format (was problems with KDE and Gnome keyboard indicators)

* Thu Jul 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt2
- fix work if config doesn't exist

* Wed Jun 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- finally switch to new backend, now both qt and html interfaces are ready to use

* Tue Jun 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.8-alt11
- preliminary version of html interface

* Thu Jun 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.8-alt10
- update desktop file

* Wed Jun 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.8-alt9
- add desktop file

* Thu May 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.8-alt8
- rebuild for new standalone

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.8-alt7
- add Ukrainian translation

* Tue Mar 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.8-alt6
- remove obsolete expanded and layout-policy attributes

* Wed Jan 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.8-alt5
- don't use woo-extract-name

* Mon Dec 18 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt4.1
- fix build

* Fri Dec 01 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt4
- remove consolehelper from requires

* Mon Nov 20 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt3
- update to new alterator API

* Wed Nov 15 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt2
- remove cond-plistq definition

* Wed Nov 08 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- update to new alterator (lang-selector)
- move syskbd backend and data to separate package

* Tue Oct 31 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.14
- update to the new backend2

* Mon Oct 16 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.13
- replace command-arg-ref with modern woo-get-option

* Mon Oct 02 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.12
- update build system

* Mon Sep 25 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.11
- remove icons into separate package

* Fri Sep 15 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.10
- use autogenerated profile and menu

* Wed Aug 23 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.9
- update build system

* Wed Jun 07 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.8
- bugfix

* Wed May 17 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.7
- build from git
- updated to latest alterator

* Fri Apr 28 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.6
- added missing backend3 to package

* Wed Apr 26 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.5
- added support for guile16

* Wed Apr 05 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.4
- added missing cell-ref

* Mon Mar 27 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.3
- ported to new guile string interface
- use new alterator functions

* Tue Mar 07 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.2
- fixed linkage

* Thu Mar 02 2006 Stanislav Ievlev <inger@altlinux.org> 0.8-alt0.1
- added kbd data
- move icons to new place
- added keyboard setup installer stage

* Thu Feb 16 2006 Stanislav Ievlev <inger@altlinux.org> 0.7-alt0.2
- rebuild with guile18

* Mon Feb 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.7-alt0.1
- move to new backend2 system

* Thu Feb 09 2006 Stanislav Ievlev <inger@altlinux.org> 0.6-alt0.1
- makefile improvements
- now support standard local xkb config files format

* Thu Feb 02 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt0.3.1
- on-{leave,apply} support

* Fri Jan 27 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt0.3
- bugfix

* Mon Jan 23 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt0.2
- move to new frame scheme

* Fri Jan 20 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt0.1
- move to profile based standalone scheme

* Tue Dec 20 2005 Stanislav Ievlev <inger@altlinux.org> 0.4-alt0.3
- locale related fixes

* Tue Nov 29 2005 Stanislav Ievlev <inger@altlinux.org> 0.4-alt0.2
- bugfixes

* Tue Nov 08 2005 Stanislav Ievlev <inger@altlinux.org> 0.4-alt0.1
- updated to new alterator

* Wed Oct 19 2005 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- added icons

* Wed Aug 31 2005 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- use generic make templates

* Wed Aug 24 2005 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- fixed work with empty variants
- removed unused tab

* Fri Aug 19 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- code improvements

* Tue Aug 09 2005 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- added standalone version, now configure local user config

* Mon Aug 01 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- Belarusian translation

* Wed Jul 20 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- bugfixes

* Mon Jul 18 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- initial release
