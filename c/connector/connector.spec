Name: connector
Version: 1.9.6
Release: alt1

Summary: Remote desktop chooser
License: GPL-2.0
Group: Networking/Remote access

Url: http://myconnector.ru
Source0: %name-%version.tar.gz
Packager: Korneechev Evgeniy <ekorneechev@altlinux.org>

BuildArch: noarch
Requires: control
Requires: libgtk+3
Requires: libgtk+3-gir
Requires: python3-module-pygobject3
Requires: python3-module-keyring >= 12.0.0
Requires: python3-module-secretstorage
Requires: remmina
Requires: remmina-plugins
Requires: tigervnc
Requires: xdg-utils
Requires: xfreerdp
Requires: zenity

%define basedir %_datadir/%name

%description
This is an aggregator program to connnect to various servers
using all of the popular remote desktop protocols
(RDP, VNC, Citrix, VMware, etc).

%package kiosk
Summary: Mode "KIOSK" for connector
Group: Networking/Remote access

Requires: connector = %EVR
Requires: xinitrc
Requires: xterm

%description kiosk
Files for connector mode "KIOSK"

%prep
%setup

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %name.desktop %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%basedir/data/
install -p *.png *.ui %buildroot%basedir/data/
install -p *.py %buildroot%basedir/
install -pm755 %name-check-* %buildroot%basedir/
install -pDm644 %name.man %buildroot%_man1dir/%name.1
%find_lang --with-man %name
install -pDm644 %name.xml %buildroot%_datadir/mime/packages/%name.xml
mkdir -p %buildroot%_iconsdir
cp -r icons/hicolor %buildroot%_iconsdir/
mkdir -p %buildroot%basedir/kiosk/
install -p kiosk/*.{py,ui} %buildroot%basedir/kiosk/
install -pm755 kiosk/connector* %buildroot%basedir/kiosk/
install -pDm600 kiosk/kiosk.conf %buildroot%_sysconfdir/%name/kiosk.conf
install -pDm644 kiosk/%name-kiosk.man %buildroot%_man1dir/%name-kiosk.1

%files
%_bindir/%name
%_desktopdir/%name.desktop
%dir %basedir
%basedir/data
%basedir/*.py
%basedir/%name-check-*
%_man1dir/%name.*
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/*/apps/%name.png

%files kiosk
%dir %basedir/kiosk
%basedir/kiosk/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/kiosk.conf
%_man1dir/%name-kiosk.*

%changelog
* Mon Jul 06 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.6-alt1
- kiosk:
 + added SDDM support
 + 'root' is not allowed to use the mode

* Tue Jun 23 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.5-alt1
- kiosk fixes

* Wed Jun 17 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.4-alt1
- kiosk:
 + fixed disable from cmdline
 + fixed webkiosk for firefox < 71

* Tue Jun 09 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.3-alt1
- new stable version

* Tue Jun 02 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.0.rc2-alt1
- kiosk:
 + Added disabling the mode before its enabling
 + Dropped chromium from deps
 + Added --disable-kiosk to connector cmdline
- Updated man (added key 'quit')

* Thu May 28 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.0.rc1-alt1
- Removed the button 'Logout'
- Disabled TRAY by default
- kiosk:
 + Updated WEB-kiosk (incognito and endless cycle)
 + Added ability to disable 'Ctrl' in the WEB-kiosk
 + Added ability to set a username, enable its autologin and create it
 + The connection file is copied to homedir.
 + Added manual
- UI fixes for BlueMenta theme

* Fri Feb 14 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.0.rc0-alt1
- kiosk remaking (like a wiki altlinux.org/kiosk):
 + Added subpackage connector-kiosk
 + root available only
 + WEB-kiosk through chromium
 + The connection file is selected from filesystem (not from list connections)

* Tue Feb 4 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.8-alt1
- FreeRDP:
 + Added escaping special characters in a password
 + Updated setting the window size
 + Added checking AUTH_FAILED error
- Added the debug mode
- Added key 'quit' for cmdline

* Wed Jan 22 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.7-alt1
- FreeRDP: added checking errors
- Disabled empty name for connections
- Added default sorting to connections and its change

* Tue Dec 17 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.6-alt1
- Added 'drag-and-drop' for create label of the connection
- Added the possibility to open Remmina and RDP files
- Updated emblem; added icons of different sizes
- FreeRDP:
 + Added input field for additional user parameters
 + Fixed work connections from previous version
- Added keys 'help' and 'version' for cmdline; updated man

* Thu Nov 07 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.5-alt2
- Fixed version

* Wed Nov 06 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.5-alt1
- Remmina: fixed connect/open/import for RDP/VNC (ALT #36757)
- FreeRDP:  disable fullscreen (auto), when toggled workarea or manually resolution
- FS: if protocol is 'file', then default server is 'localhost'
- 'kiosk' changes:
 + Disable TRAY when activate
 + Added online checking access
- Updated .desktop file
- Updated icons for CITRIX & VMWARE

* Fri Jan 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.4-alt1
- Added buttons 'Communication with developer' and 'Report a bug' into menu Help.
- FreeRDP: added checkbox for glyph-cache (ALT #35796)

* Fri Dec 07 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.3-alt1
- keyring: some fixes

* Tue Dec 04 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.2-alt1
- Added on/off for logging
- Fixed tray update after save first connection
- Added ability to save default settings
- FreeRDP changes:
 + Added checkboxes for GDI rendering, auto-reconnect and cert-ignore
 + Added checking USB PATH while redirecting
 + Updated translation for 'span screen'
 + Added ability to save password in the keyring (ALT #35608)
- Added button reset of the program's parameters
- Remmina: fixed SSH/SFTP connection on new version
- FS: added choise of the protocol from drop-down list

* Fri Aug 03 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.7.2-alt1
- Added on/off for version checking
- Minor changes in the GUI

* Wed Jul 25 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.7.1-alt1
- Added tray icon
- Disabled start of multiple copies via GTK
- Added mymetype and association for .ctor files
- Added version checking

* Fri Jul 13 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.6.4-alt2
- Fixed start programm if FS - new function (after update e.g)

* Thu Jul 12 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.6.4-alt1
- Disabled start of multiple copies
- Fixed creating label if exist of the same name
- Fixed open Citrix/WEB tab from main menu

* Fri Jul 06 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.6.3-alt2
- Fixed open preferences window for FS

* Thu Jul 05 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.6.3-alt1
- Added support SPICE
- Added support connect to fileservers (SMB, FTP, etc.)
- Remmina: Disable password storing by default

* Mon Jun 25 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.6-alt4
- Remmina: fixed connect from preferences window

* Fri Jun 22 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.6-alt3
- Fixed connect from preferences window

* Tue Jun 05 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.6-alt2
- Fixed the fast connect from console

* Thu Apr 19 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.6-alt1
- FreeRDP/Remmina: connection name in the window title

* Tue Mar 27 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.5-alt1
- Update AboutDialog and title of the main window

* Wed Mar 07 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.4-alt1
- Added choise of the default tab on main window
- Changed label's default folder to 'Desktop'
- [kiosk] Notifications disabled, when ACCESS=OFF

* Tue Dec 12 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.3-alt2
- Fixed version

* Tue Dec 12 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.3-alt1
- Added key '/gdi:sw' as default for FreeRDP

* Thu Sep 21 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.2-alt3
- Fixed unowned files

* Wed Sep 20 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.2-alt1
- OS check updated (ALT #33906)
- Added notifications for mode 'kiosk'

* Wed Jul 05 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.1-alt2
- Fixed checking config for mode 'kiosk

* Wed Jul 05 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.1-alt1
- Changes in mode 'kiosk'
 + removed notifications about enable/disable
 + added config for access to the settings

* Tue May 23 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.5.0-alt1
- Added mode 'kiosk'

* Tue May 23 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.4.3-alt3
- Added switching to the default tab after save properties

* Tue May 23 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.4.3-alt2
- Changed the command to open the wiki

* Fri May 19 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.4.3-alt1
- The code is optimized: now the program works equally in both AltLinux and Linux Mint
- Startup command of connection added to the log
- Update vncviewer's keys
- Changed command of web-connection

* Wed May 17 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.4.1-alt2
- Fixed save shortcut of connections
- Minor fixes in changelog

* Tue May 16 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.4.1-alt1
- Added more shared folders for FreeRDP

* Tue Apr 18 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.4.0-alt3
- Fixed build - remove vmware-view-userinstall from requires
- Added checking the installation of the VMware Horizon Client (or vmware-view-userinstall)

* Fri Apr 07 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.4.0-alt2
- Fixed creating LOGFOLDER

* Fri Apr 07 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.4.0-alt1
- Added logging
- Added checking 'control udisks2' (for shared /media, FreeRDP)
- Update requires - added vmware-view-userinstall
- Added manual
- Added key /span for FreeRDP
- Default vncviewer -> TigerVNC
- Added checking the installation of the ICAClient
- Changed the fast connect from console: uses the connection unique name
  instead of the file name
- Fixed import CITRIX & WEB

* Mon Oct 17 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.24-alt3
- Update categories in .desktop

* Tue Sep 13 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.24-alt2
- Fixed command open webbrowser

* Tue Sep 13 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.24-alt1
- Added function - copy ctor-file's name to clipboard

* Wed Aug 24 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.23-alt3
- Update requires - added remmina-plugins

* Mon Aug 22 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.23-alt2
- Update requires - added xfreerdp

* Fri Aug 12 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.23-alt1
- Fixed a bug - sometimes doesn't work quick connection

* Thu Jan 14 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.22-alt2
- Fixed vncviewer parameters for TigerVNC

* Tue Jan 12 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.22-alt1
- Fixed redirect smartcards, added redirect usb-storage and key /workarea. NLA is now optional

* Tue Sep 15 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.21-alt1
- Added performance parameters and choise default tab

* Mon Aug 17 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.19-alt1
- Added quick connect -login@server for SSH & SFTP

* Mon Aug 17 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.18-alt1
- Added sound, microphone and printer for FreeRDP

* Tue Aug 11 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.17-alt1
- Added WEB, smartcards

* Thu Jul 02 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.15-alt1
- Added function Copy, update GTK >=3.10

* Thu Jun 25 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.14-alt1
- Update GUI and FreeRDP features

* Tue Jun 23 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.12-alt4
- Update SPEC

* Mon Jun 22 2015 Korneechev Evgeniy <ekorneechev@altlinux.org> 1.3.12-alt3
- Initial build by GEAR

* Tue Jun 16 2015 Michael Shigorin <mike@altlinux.org> 1.3.12-alt2
- spec cleanup

* Tue Jun 16 2015 Evgeniy Korneechev <ekorneechev@gmail.com> 1.3.12-alt1
- Initial build
