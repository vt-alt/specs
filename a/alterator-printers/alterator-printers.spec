Name: alterator-printers
Version: 6.2
Release: alt2

Source:%name-%version.tar

Summary: simple alterator module for printer administration
License: GPL
Url: http://www.altlinux.com
Packager: Lenar Shakirov <snejok@altlinux.org>
Group: System/Configuration/Other
BuildArch: noarch

#TODO: will be installed only if needed
Requires: cups >= 1.2.0, samba-client-cups, printer-testpages

Requires: alterator >= 2.9, alterator-standalone, alterator-l10n >= 2.9-alt25
Requires: foomatic-db-engine, gzip-utils

BuildPreReq: alterator >= 2.9-alt0.3, alterator-standalone >= 2.4-alt0.8

%description
simple alterator module for printer administration

%prep
%setup

%build
%make_build

%install
%makeinstall DESTDIR=%buildroot

%files
%_alterator_datadir/images/*
%_alterator_datadir/ui/*/
%_alterator_datadir/applications/*
%_alterator_backend3dir/*
%_libexecdir/%name

%changelog
* Fri Mar 06 2020 Lenar Shakirov <snejok@altlinux.org> 6.2-alt2
- Change path to /usr/sbin/accept -> /usr/sbin/cupsaccept

* Tue Dec 30 2014 Lenar Shakirov <snejok@altlinux.ru> 6.2-alt1
- simply find drivers by "lpinfo -m"
  * Instead of awk/find/foomatic wrappers

* Sat Dec 20 2014 Lenar Shakirov <snejok@altlinux.ru> 6.1-alt1
- backend merged to main package
- lcl.scm: "bind to serial" checkbox added
- lcl.scm: code optimizations

* Mon Dec 08 2014 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt12
- Raw printer support added
- mdl.scm: Vendors sorted in backend
- printer_drivers backed merged to cupsd
- cupsd: allow empty printer description
- index.scm: remove Quit button
- CUPS-ipp connection added
- smb: crash fixed and optimizations

* Tue Oct 08 2013 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt11
- Allow comma and dot in printer name

* Wed Dec 12 2012 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt10
- Backend printer_driver: Fix driver searching

* Tue Dec 11 2012 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt9
- New search paths and file extensions for update-printers-db:
  * Search in /usr/share/ppd/ too
  * Follow symlinks
  * Search for *.ppd.gz extension too

* Mon Apr 04 2011 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt8
- l10n removed: merged to alterator-l10n (ALT #25380)

* Thu Feb 24 2011 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt7
- Use cupspage.ps instead testprint.ps
- Hack for HP printers added
- Use /usr/lib instead of $(getconf LIBDIR)

* Wed Sep 29 2010 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt6
- reload smb service when add/remove printer

* Wed Sep 22 2010 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt5
- select form size increased

* Wed Sep 15 2010 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt4
- generate button id removed
- create temporary ppd with "prn_name" template
- test that directory parport* exist
- .gear/rules: alterator-printers -> @name@

* Thu Aug 12 2010 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt3
- code cleanup and optimizations
- don't rebuild driver when printer reconfigured, use old PPD file
- LPT autodetection: search in the right path for none parport0
- error catching improved in lcl and mdl forms

* Tue Jun 01 2010 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt2
- warn, if cupsd is stopped
- spec cleaned: {update,clean}_menus deleted

* Wed May 05 2010 Lenar Shakirov <snejok@altlinux.ru> 6.0-alt1
- PageSize always A4
- fixed for work on modern branchs:
  + Confirmation "on-leave" removed
  + 'surround "/std/base"' removed from mdl.scm
- backends fixed and cleaned
- backend cups: LANG=C for lpstat
- printer-drivers-utils package merged
- printers drivers cache generating added
- error catching/displaing emproved
- woo-write calls reduced

* Thu Aug 20 2009 Lenar Shakirov <snejok@altlinux.ru> 5.0-alt5
- printer-drivers-utils requires deleted
- obsolete code cleaned
  + invisible reblaced by visibility #f
  + inactive replased by activity #f
  + password field: stars -> "stars"
  + cleaning and optimizations of code
- printer name must match required pattern ([0-9a-zA-Z_-])+
- height of sel.scm raised to 330

* Thu Aug 20 2009 Lenar Shakirov <snejok@altlinux.ru> 5.0-alt4
- printer-drivers-base requires deleted

* Thu Jun 25 2009 Lenar Shakirov <snejok@altlinux.ru> 5.0-alt3
- Interface cleaned from obsolete layout-policy
- Backend cupsd rewrited to backend3 scheme
- Description field is added
- Don't output '$drv', if it not found
- Backend printer_detect rewrited to backend3 scheme
- Make and model autoselecting fixed
- Reload parport drivers on every 'list' command
  + rmmod replaced by modprobe -r
  + unload lp module
- 'Detected printer' label added
- l10n updated
  + ru.po converted to utf8

* Thu Jun 18 2009 Lenar Shakirov <snejok@altlinux.ru> 5.0-alt2
- update to new alterator (replace string-starts-with? by string-prefix?)
- desktop file updated and moved to %alterator_datadir/applications/
- packager and url added to spec
- Makefile cleaned
- frame:buttons-view obsolete: use simple button
- dump_ppds.awk using removed: import dump_ppds.awk script
- Using lpstat when reading data: instead of cat'n'grep
- Wrong string-prefix? usage: fixed to 'string-prefix? prefix str'

* Wed Nov 08 2006 Stanislav Ievlev <inger@altlinux.org> 5.0-alt1
- update to new alterator (replace command-arg-ref with modern woo-get-option)
- update build system

* Mon Sep 25 2006 Stanislav Ievlev <inger@altlinux.org> 5.0-alt0.6
- move icons into separate package
- rename caption to title

* Wed Aug 23 2006 Stanislav Ievlev <inger@altlinux.org> 5.0-alt0.5
- update build system
- added common makefile for all standalone modules

* Wed May 31 2006 Stanislav Ievlev <inger@altlinux.org> 5.0-alt0.4
- ported to new alterator

* Wed May 24 2006 Stanislav Ievlev <inger@altlinux.org> 5.0-alt0.3
- ported to new cups

* Fri May 12 2006 Stanislav Ievlev <inger@altlinux.org> 5.0-alt0.2
- build from git

* Fri May 05 2006 Stanislav Ievlev <inger@altlinux.org> 5.0-alt0.1
- major interface improvements

* Fri Apr 28 2006 Stanislav Ievlev <inger@altlinux.org> 4.2-alt0.7
- fixed backend

* Wed Apr 19 2006 Stanislav Ievlev <inger@altlinux.org> 4.2-alt0.6
- use theme icons now

* Thu Apr 06 2006 Stanislav Ievlev <inger@altlinux.org> 4.2-alt0.5
- replace document:link with document:insert

* Thu Mar 16 2006 Stanislav Ievlev <inger@altlinux.org> 4.2-alt0.4
- added splash message during driver generation

* Tue Mar 14 2006 Stanislav Ievlev <inger@altlinux.org> 4.2-alt0.3
- fixed image symlink

* Thu Mar 09 2006 Stanislav Ievlev <inger@altlinux.org> 4.2-alt0.2
- apply patch from Alexey Miltsev
- fixed icon paths

* Mon Feb 13 2006 Stanislav Ievlev <inger@altlinux.org> 4.2-alt0.1
- minor bugfixes, move to new backend2 subsystem

* Thu Feb 09 2006 Stanislav Ievlev <inger@altlinux.org> 4.1-alt0.3.2
- makefile improvements

* Thu Feb 02 2006 Stanislav Ievlev <inger@altlinux.org> 4.1-alt0.3.1
- use document:popup-options, frame:on-{leave,apply}

* Mon Jan 30 2006 Stanislav Ievlev <inger@altlinux.org> 4.1-alt0.3
- usability improvements

* Mon Jan 23 2006 Stanislav Ievlev <inger@altlinux.org> 4.1-alt0.2
- move to new frame scheme

* Fri Jan 20 2006 Stanislav Ievlev <inger@altlinux.org> 4.1-alt0.1
- move to profile based standalone scheme

* Tue Dec 20 2005 Stanislav Ievlev <inger@altlinux.org> 4.0-alt0.4
- locale improvements

* Mon Dec 19 2005 Stanislav Ievlev <inger@altlinux.org> 4.0-alt0.3
- layout improvements

* Thu Dec 15 2005 Stanislav Ievlev <inger@altlinux.org> 4.0-alt0.2
- added support for local connection

* Wed Dec 14 2005 Stanislav Ievlev <inger@altlinux.org> 4.0-alt0.1
- new layout, now we can edit printers

* Wed Oct 19 2005 Stanislav Ievlev <inger@altlinux.org> 3.3-alt2.2
- added icons

* Wed Oct 05 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3-alt2.1
- fix widgets layout

* Wed Aug 31 2005 Stanislav Ievlev <inger@altlinux.org> 3.3-alt2
- use generic make templates

* Tue Aug 30 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3-alt1.1
- fix widgets layout

* Wed Aug 24 2005 Stanislav Ievlev <inger@altlinux.org> 3.3-alt1
- added splash message during driver generation

* Mon Aug 08 2005 Stanislav Ievlev <inger@altlinux.org> 3.2-alt2
- fixed bug

* Fri Aug 05 2005 Stanislav Ievlev <inger@altlinux.org> 3.2-alt1
- update model for new alterator

* Mon Aug 01 2005 Stanislav Ievlev <inger@altlinux.org> 3.1-alt5
- Belarusian translation

* Thu Jul 21 2005 Stanislav Ievlev <inger@altlinux.org> 3.1-alt4
- fixed menu file

* Wed Jul 20 2005 Stanislav Ievlev <inger@altlinux.org> 3.1-alt3
- updates

* Thu Jul 14 2005 Stanislav Ievlev <inger@altlinux.org> 3.1-alt2
- interface improvements
- printers-config renamed to config-printers

* Wed Jul 06 2005 Stanislav Ievlev <inger@altlinux.org> 3.1-alt1
- map adopted to new config style
- use ready-to-use alterator-standalone frame
- printers-config now in /sbin

* Wed Jul 06 2005 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt1
- update map

* Mon Jun 27 2005 Stanislav Ievlev <inger@altlinux.org> 3.0-alt7
- minor fixes

* Thu Jun 23 2005 Stanislav Ievlev <inger@altlinux.org> 3.0-alt6
- updated po by kirill

* Tue Jun 21 2005 Stanislav Ievlev <inger@altlinux.org> 3.0-alt5
- use external error messages

* Mon Jun 20 2005 Stanislav Ievlev <inger@altlinux.org> 3.0-alt4
- added menu file

* Thu Jun 16 2005 Stanislav Ievlev <inger@altlinux.org> 3.0-alt3
- adopted for new look

* Tue Jun 14 2005 Stanislav Ievlev <inger@altlinux.org> 3.0-alt2
- adopted for new look

* Thu Jun 09 2005 Stanislav Ievlev <inger@altlinux.org> 3.0-alt1
- added standalone version

* Tue Jun 07 2005 Stanislav Ievlev <inger@altlinux.org> 2.4-alt1
- improvements

* Mon Jun 06 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt11
- new scheme of uris

* Tue May 31 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt10
- new snapshot

* Fri May 27 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt9
- new snapshot

* Wed May 04 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt8
- new snapshot

* Wed Apr 27 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt7
- new snapshot

* Mon Apr 25 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt6
- improved files layout

* Fri Apr 22 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt5
- little layout improvements
- added support for ALT control center

* Thu Apr 21 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt4
- changed backend format

* Wed Apr 13 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt3
- bugfixes

* Tue Apr 12 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt2
- little improvements

* Mon Apr 04 2005 Stanislav Ievlev <inger@altlinux.org> 2.2-alt1
- move ui and model tarballs here

* Mon Mar 21 2005 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
