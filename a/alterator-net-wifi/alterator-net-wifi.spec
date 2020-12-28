%define _altdata_dir %_datadir/alterator

Name: alterator-net-wifi
Version: 0.18
Release: alt1

Packager: Vladislav Zavjalov <slazav@altlinux.org>

BuildArch: noarch

Source:%name-%version.tar

Summary: alterator module for wi-fi connections administration
License: GPL
Group: System/Configuration/Other
Requires: wpa_supplicant

Conflicts: alterator-fbi < 2.8-alt1
Conflicts: alterator-lookout < 1.2-alt1
Requires: alterator >= 3.1-alt6
Requires: alterator-sh-functions >= 0.6-alt3
Requires: alterator-hw-functions >= 0.2-alt3

BuildPreReq: alterator >= 3.3-alt5

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator

%description
alterator module for wi-fi connections administration

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall

%files
%_altdata_dir/ui/*/
%_altdata_dir/applications/*
%_alterator_backend3dir/*

%changelog
* Sat Dec 26 2020 Ivan Razzhivin <underwit@altlinux.org> 0.18-alt1
- net-wifi-nm fix translation

* Thu Dec 17 2020 Ivan Razzhivin <underwit@altlinux.org> 0.17-alt1
- show message for wrong password
- hide password entry
- save settings when connected

* Mon Dec 14 2020 Ivan Razzhivin <underwit@altlinux.org> 0.16-alt1
- show password
- connect/disconnect
- check password format

* Thu Dec 03 2020 Ivan Razzhivin <underwit@altlinux.org> 0.15-alt1
- Add support NetworkManager

* Sat Jan 19 2019 Fr. Br. George <george@altlinux.ru> 0.14-alt2
- Fix incorrect interface naming

* Mon May 07 2012 Andriy Stepanov <stanv@altlinux.ru> 0.14-alt1
- Fix crash ahttpd part for uninitialized WiFi adapters.

* Tue Mar 08 2011 Vladislav Zavjalov <slazav@altlinux.org> 0.13-alt1
- show signal level, sort networks by level (patches by vx8400, ALT bug #26992)

* Sun Jan 16 2011 Vladislav Zavjalov <slazav@altlinux.org> 0.12-alt2
- desktop-files: add ru and uk translations (thanks to Roman Savochenko)

* Fri Nov 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.12-alt1
- html ui: use wf=none + card-index module;
- qt ui: don't use document:id's, rearrange functions
- backend: remove unused function

* Thu Nov 05 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.11-alt1
- backend: allow working without alterator-mailbox-send;
  remove auto-dependency on alterator-lookout
- ajax.scm: don't include unused module card-index
- qt ui: use /std/frame

* Thu Aug 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.10-alt1
- qt ui: fix interface name handling (closes: #19897)
- qt ui: don't use cell for iface name

* Wed Aug 19 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt1
- cleanup html interface, move template to ui directory
- use ajax.scm, don't use select.js and effectDisable
- backend: don't restart iface, only start supplicant 
  if needed; don't change BOOTPROTO parameter

* Fri Apr 17 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt1
- use netdev_is_wireless instead of obsolete ifcheckwireless (closes: #19137)
- always use wext as supplicant driver
- don't use hal-dbus
- remove obsolete write call from message-handler (by inger@)
- move supplicant functions to separate place (by inger@)
- move write_string_param out from supplicant_read_status (by inger@)
- refactor read_status function: remove get_status function (by inger@)

* Fri Mar 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt1
- use alterator_api_version=1
- cleanup code
- fix inteface setup (fix #12787)
- setup iface only once (fix #19137)

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt8
- move translations to alterator-l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt7
- rebuild with alterator-l10n

* Thu Dec 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt6
- add desktop-file (fix help)

* Fri Oct 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt5
- remove constraints from backend
- remove some unuseful comments

* Wed Sep 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt4
- fix English messages

* Tue Sep 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt3
- rebuild with new alterator-l10n

* Tue Aug 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- rename button 'Quit' to button 'OK'

* Thu Jul 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt1
- use new alterator (remove po-domain settins from ui and backend)
- use auto-disable in qt ui

* Mon Jun 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt6
- add autoDisable in html

* Mon Jun 23 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt5
- add scan_ssid=1 option to all networks

* Fri May 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt4
- fix ifdriver execution

* Wed May 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt3
- remove debug messages from backend

* Wed May 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt2
- use alterator-l10n

* Thu May 22 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt1
- remove template- backend
- remove html-messages
- rewrite qt ui
- rewrite html ui
- modify backend

* Tue Dec 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- remove config autocleanup

* Wed Nov 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- use scripts from alterator-net-common
- up interface before scanning (need for some ugly wifi cards)

* Mon Sep 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt8
- fix typos in Russian translation

* Thu May 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt7
- Add Russian translation

* Thu May 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt6
- fix wpa supplicant driver selection for ipw2200
- add support both for ASCII and HEX  (as a hash) psk

* Mon May 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt5
- support both ASCII and HEX wep keys
- don't use qt-browser constraints engine

* Fri May 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt4
- fix work with latest supplicant 0.5.7 (hidden key values)
- enable constraints in GUI

* Thu May 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- fix network parameters saving

* Mon May 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- fix width/height

* Mon May 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- add support for edit
- add GUI

* Fri May 04 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- rename to alterator-net-wifi (main stream now)

* Wed May 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release

