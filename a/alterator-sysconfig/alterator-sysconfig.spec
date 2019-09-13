%define _altdata_dir %_datadir/alterator

Name: alterator-sysconfig
Version: 1.3.0
Release: alt1

%add_findreq_skiplist %_datadir/install2/preinstall.d/*

Provides: alterator-syskbd = %version, alterator-proxy = %version
Obsoletes: alterator-syskbd, alterator-proxy

Url: http://www.altlinux.org/Alterator
Source:%name-%version.tar
Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Summary: alterator module for basic system settings
License: GPL
Group: System/Configuration/Other

Requires: alterator-sh-functions, setup >= 2.2.12-alt1
Requires: alterator >= 3.5-alt1 vhttpd-utils >= 0.3-alt6
Requires: alterator-sh-functions >= 0.6-alt2
Requires: alterator-l10n >= 2.2-alt3

Conflicts: alterator-lookout < 0.9-alt5
Conflicts: alterator-wizardface < 0.5-alt7

BuildPreReq: alterator >= 3.2-alt6

%description
alterator module for basic system settings
(console and X11 keyboard, console font, system locale)

%prep
%setup

%build
%make_build libdir=%_libdir

%install
%makeinstall

%files
%config(noreplace) %_sysconfdir/alterator/sysconfig
%_datadir/alterator/ui/*/
%_datadir/alterator/applications/*
%_alterator_backend3dir/*
%_datadir/install2/preinstall.d/*

%changelog
* Thu Sep 12 2019 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- installer: Setup localized slideshow for selected language.

* Wed Sep 11 2019 Lenar Shakirov <snejok@altlinux.ru> 1.2.7-alt1
- Add NO_PROXY edit box (ALT #27753)

* Tue Sep 10 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- Remove unsupported tt_RU locale.

* Thu Aug 29 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- Use install instead of cp -af to prevent loose permission from tmpfs by un-def kernel.

* Thu Jul 11 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- Use hostname-or-ip field type to support IP address (ALT #35613).

* Sat Apr 28 2018 Maxim Voronov <mvoronov@altlinux.org> 1.2.3-alt1
- set locale for localectl

* Tue Sep 24 2013 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- added Kazah XKB setup, thanks Baurzhan Muftakhidinov (see #28991)

* Tue Feb 14 2012 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt3
- Hack for correct fallback language for tt_RU (thanks sem@) (closes: #26931)

* Tue Sep 20 2011 Radik Usupov <radik@altlinux.org> 1.2.1-alt2
- Added langlist.tt_RU

* Wed Mar 16 2011 Michael Shigorin <mike@altlinux.org> 1.2.1-alt1
- changed default console font to UniCyr_8x16 (closes: #25225)

* Thu Feb 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2-alt1
- DISPLAY setting added if none set

* Sun Aug 29 2010 Michael Shigorin <mike@altlinux.org> 1.1-alt1.1
- fixed 20-sysconfig.sh to ensure /etc/sysconfig existence
- fixed thinko in sysconfig-proxy (HTTPS_PROXY=https://)
- minor spec cleanup
- added an Url:

* Tue Nov 10 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt1
- language selection ui: use modern form API

* Wed Jun 03 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt8
- use new form API (closes: #20288)

* Mon May 25 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt7
- update both console and x11 keytable

* Mon Apr 06 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt6
- fix menu file

* Tue Mar 31 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt5
- use translations directly from alterator-l10n

* Tue Mar 31 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt4
- add some Spanish locales

* Fri Feb 20 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt3
- don't encode host name

* Thu Jan 15 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt2
- html: fix backend name

* Thu Jan 15 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- remove obsolete sysconfig/lang and sysconfig/kbd interfaces
- use help directly from alterator-l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.10-alt2
- rebuild with new l10n

* Fri Dec 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.10-alt1
- use help files from alterator-l10n
- add pt_BR to language list

* Thu Nov 20 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- join with alterator-proxy module

* Fri Oct 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt4
- fix old sysfont backend

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt3
- update Russian keyboard layouts

* Fri Sep 19 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt2
- bugfix

* Thu Sep 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt1
- Merge all interfaces and all backeends (keep old versions)

* Mon Aug 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt3
- add support for defaults (/etc/sysconfig/kbd/kbdlist)
- syskbd backend: alterator_api_version = 1

* Mon May 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- join to common translation datebase
- improve ui layout

* Mon May 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- use enumref
- improve UI according common alterator HIG
- minor bugfixes

* Thu May 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- add help for language step
- remove 'POSIX'
- remove autoinstall backend usage
- translate both 'Next' and 'Help' buttons

* Wed Apr 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt5
- go next on double click (#11000)
- fix focus jump (#14682)

* Mon Mar 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt4
- remove layout-policy attribute (bug #14945)

* Wed Mar 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- provides/obsoletes alterator-syskbd

* Wed Jan 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- use alterator-sh-functions
- add help from installer
- don't setup rpm_install_langs
- add uk_UA to langlist.ru
- rename ru_RU to ru_UA in langlist.uk

* Tue Jan 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- remove old /sysconfig/lang
- add support for translation fallback

* Mon Oct 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- translate step list

* Thu Oct 04 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- add /sysconfig/language - separate language step
- fix old /sysconfig/lang - wrong translation package

* Thu Sep 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- join together all basic system setup:
  console font, console and X11 keyboard layout, system locale

* Mon Aug 06 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt8
- control switching fixed 

* Fri Jun 22 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt7
- added 3-language layput for UA 

* Fri Jun 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- to sisyphus

* Mon Jun 04 2007 Anton V. Boyrshonov <boyarsh@altlinux.ru> 0.2-alt5
- added alt-shift toggle 

* Wed May 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- update Ukrainian translation

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- add Ukrainian translation

* Wed Jan 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- add default action

* Wed Jan 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add support for autoinstall backend
- automatically select single keyboard variant

* Wed Dec 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- really change system files

* Mon Dec 11 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- improve interface for low resolution screens

* Mon Dec 04 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- auto skip in both directions
- save translations in utf8 encodings to avoid iconv usage on installer's stage2 

* Wed Nov 29 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- enable wizard callbacks

* Fri Nov 10 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- initial release

