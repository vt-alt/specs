%define oname opennx

Name: rxclient
Version: 1.0.1
Release: alt1

Summary: A client for RX@Etersoft Terminal Server

License: LGPL/GPL
Group: Networking/Remote access
Url: https://wiki.etersoft.ru/RX

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://gitlab.eterfund.ru/rx-etersoft/rxclient/-/archive/%version-%release/rxclient-%version-%release.tar.bz2
Source: %oname-%version.tar
Source1: rxclient.conf

# Automatically added by buildreq on Sat Sep 19 2009
BuildRequires: gcc-c++ imake libSM-devel libXmu-devel
BuildRequires: libopensc-devel libsmbclient-devel
BuildRequires: xorg-cf-files zip libcups-devel
BuildRequires: libXau-devel
BuildRequires: libwxGTK3.0-devel xxd

# due _ln_sr
BuildRequires: rpm-build-intro >= 1.9.18

Requires: nx-libs >= 3.5.2.31-alt1
Requires: nxssh

Provides: opennx = %version
Obsoletes: opennx

# dynamic loading
Requires: libcups libsmbclient

%description
RX Client is a NX 3.5 compatible client based on OpenNX code.

%prep
%setup

%build
%autoreconf
%configure --localedir=%_datadir/locale --with-nxproto=3.3.0
%make_build

%install
%makeinstall_std

# install workaround for eterbug #11493
install -D -m0755 bin/nxssh.sh %buildroot%_bindir/nxssh.sh

# socks support
#rm -f %buildroot%_bindir/pconnect %buildroot%_datadir/pconnect.html

rm -f %buildroot%_desktopdir/*.directory
install -D -m0644 docs/pconnect.1 %buildroot%_man1dir/pconnect.1

# we need this names due wxDynamicLibrary (see eterbug #11676)
mkdir -p %buildroot%_libdir/%name/
for lib in libsmbclient.so libcups.so ; do
    rlib=$(echo %_libdir/$lib.?)
    %_ln_sr %buildroot$rlib %buildroot%_libdir/%name/$lib
done

mkdir -p %buildroot%_sysconfdir/%name/
cp %SOURCE1 %buildroot%_sysconfdir/%name/

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-report
%_bindir/nxssh.sh
%_bindir/pconnect
%_bindir/watchreader
%_libdir/%name/
%_man1dir/pconnect.*
%_datadir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/*/mimetypes/rx-desktop.*
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/*.conf

%changelog
* Mon Nov 18 2019 Konstantin Kondratyuk <kondratyuk@altlinux.org> 1.0.1-alt1
- fix assert during saving password (eterbug #13646)

* Wed Feb 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2
- no return statement in the non-void function fixed (according g++8)

* Sun Nov 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- change versioning scheme
- implement readonly mode for rxclient (eterbug 12856)
- disabled default settings for timeout (ssh)

* Sun Sep 16 2018 Pavel Vainerman <pv@altlinux.ru> 0.19-alt20
- new release

* Thu Sep 13 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt19
- added rxclient-report util

* Sat Sep 01 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt18
- (CI): fix event bot message

* Sat Sep 01 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt17
- update build require: wxGTK3.1 --> wxGTK3.0 eterbug #12307

* Thu Aug 16 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt16
- (CI): new rpmlog --> new bot message

* Wed Aug 15 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt15
- the proxy for the font server is disabled. eterbug #13048

* Thu Aug 09 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt14
- (CI): disabled test build for i586.32 and build for p7
- (CI): added cups-pdf to 'rxclient' test container
- (CI): moved templates daas to a special project 'rx-daas-templates'

* Thu Aug 09 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt13
- (CI): added an event to the telegram channel

* Tue Jul 31 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt12
- (gitlab-ci): Added docker test after build (eterbug #13053)
- (gitlab-ci): Added run test server (eterbug #13053)
- (gitlab-ci): added a separate directory for each build (eterbug #13053)
- (gitlab-ci): rename 'rx-etersoft' to 'rxserver'

* Thu Jun 28 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt11
- (CI): minor fixes in pipeline
- (CI): test build

* Thu Jun 28 2018 Pavel Vainerman <pv@altlinux.ru> 0.19-alt10
- test build

* Wed Jun 20 2018 Vitaly Lipatov <lav@altlinux.ru> 0.19-alt9
- change Url to our page
- drop nx buildreq

* Thu Jun 14 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt8
- fix type (eterbug #12930)

* Thu Jun 07 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt7
- added new CI build for tests
- added NxProxyTimeout config option (eterbug #12907)
- (CI): remove artifacts for test builds (korinf itself stores logs)
- added test build for i586 (32bit)
- fix desktop file for rxclient (admin) (eterbug #12919)
- set rxclient icon for rxclient-admin (eterbug #12919)

* Tue Apr 24 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt6
- fixed helper name for pcsc module (eterbug #12848)
- added support for errror "Connection timed out" added default timeout for connection 1 sec and 2 attempts

* Sat Apr 21 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt5
- added reading of parameters for the nxssh from the configuration file (user and global)
- added source1

* Fri Apr 20 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt4
- increased pause before terminate nxssh output processing. fix eterbug #12814

* Thu Apr 12 2018 Etersoft Builder <builder@etersoft.ru> 0.19-alt3
- update require to nx-libs

* Tue Apr 10 2018 Pavel Vainerman <pv@altlinux.ru> 0.19-alt2
- fixed eterbug #12816

* Thu Apr 05 2018 Pavel Vainerman <pv@altlinux.ru> 0.19-alt1
- release

* Tue Mar 20 2018 Etersoft Builder <builder@etersoft.ru> 0.18-alt17
- (usbip): USE_USBIP_SYSTEM_INTERFACE - added IDS-file parser - added 'usbip list' parser - read USB device info from IDS file (usbip): use tcp connection for usbipd (usbip): added options 'usbip' and 'usbipdev' (usbip): added module 'UsbIpModule' for usb forwarding, cleanup old code (modules): added print information about modules (--check-modules) update nx require DELETED old code to support usbip
- (gitlab-ci): move 'build for p7' to main build task
- fixed compilation for p7

* Fri Mar 16 2018 Etersoft Builder <builder@etersoft.ru> 0.18-alt16
- (pcscd): added check nx version (protocol version)

* Tue Mar 13 2018 Etersoft Builder <builder@etersoft.ru> 0.18-alt15
- (gitlab-ci): apt-get --> epm and other minor fixes
- (pcscd): added support for pcscd forwarding - added first implementation of ModuleManager - added first implementation of PCSCModule
- moduleManager interface refactoring

* Mon Dec 25 2017 Etersoft Builder <builder@etersoft.ru> 0.18-alt14
- rewrite CupsPort config in .opennx before check isCupsRunning

* Mon Dec 25 2017 Etersoft Builder <builder@etersoft.ru> 0.18-alt13
- use cups port from rxclient settings (eterbug #12404)

* Fri Dec 22 2017 Etersoft Builder <builder@etersoft.ru> 0.18-alt12
- (gitlab-ci): fix "tags" for build for p7

* Fri Dec 22 2017 Etersoft Builder <builder@etersoft.ru> 0.18-alt11
- (gitlab-ci): push to master after build
- up version

* Fri Dec 22 2017 Pavel Vainerman <pv@altlinux.ru> 0.18-alt10
- up version (2)

* Fri Dec 22 2017 Pavel Vainerman <pv@altlinux.ru> 0.18-alt9
- up version

* Wed Dec 13 2017 Pavel Vainerman <pv@altlinux.ru> 0.18-alt8
- fix using server key from session config file (eterbug #12195)
- add initial support of smartcard authentication
- turn off smart card auth for Windows
- add 'const' in function initSmartCard
- add parameter "silent" to opennxapp parameters
- hide all dialogs when rxclient runned in silent mode
- djelf - 03_win32exec; nxwin close
- djelf - 04_noencrypt; fix nonencrypted
- djelf - 05_AddStateWait03; add STATE_WAIT
- djelf - 05_Async; fix AsyncProcess
- djelf - 08_Win32Geometry
- djelf - 14_TraceAll; new option --trace=All
- djelf - 19_TestStartNXWin
- djelf - 20_AddHomeVar; cygwin HOME
- djelf - 21_NoKillNXssh; win32 only
- djelf - 22_RussNameComputer
- djelf - 23-WinCompIsWinNT
- fix nxwin nonmultiwindow modes crash (Djelf-08_Win32Geometry)
- win32 only: add nodecoration mode (Djelf)
- send --screeninfo identical of original nxclient
- no browse local resources if sharing is off
- win32: change environment for new cygwin
- win32: add more compatibility with original nxclient
- win32: wx3 build #1
- win32: don't build PA, use 6.0 binarys from  x2goclient-contrib
- win32: don't start pa at session configure
- encode/decode smb passwords comes back
- annoying messages suppression
- win32: startsession params change
- win32: win32: by Djelf: fix unhide of nxwin again
- win32: try to fix unhide desktop under w7-10
- win32: some dimbor's mingw build stuff
- win32: fix strangeness with X11PropertyDialog
- update about screen
- win32: change windows APPID
- add compability with wx2.8
- win32: change path to pulseaudio headers
- fix by merge request discussion
- small translation improving
- fix virtualdesktop sessions (eterbug #12330)
- disable yesno and warn dialogs for --silent mode (eterbug #12338)
- fix variable name (eterbug #12330)
- added .gitlab-ci.yml
- added test build for p7
- enable CI for 'master'
- (gilab ci): reformat file
- (gitlab-ci): made a separate stage for build for p7

* Mon Nov 13 2017 Pavel Vainerman <pv@altlinux.ru> 0.18-alt7
- added require for nx (nxssh)

* Thu Nov 02 2017 Pavel Vainerman <pv@altlinux.ru> 0.18-alt6
- fix bug for commit 21d6a6864a45385a

* Wed Nov 01 2017 Pavel Vainerman <pv@altlinux.ru> 0.18-alt5
- Update translation
- Add serialization for login type
- Update login dialog, add login type combobox

* Mon Sep 11 2017 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt4
- use new macro _ln_sr instead ln -sr

* Mon Sep 11 2017 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt3
- fix c_str() using

* Tue Jun 20 2017 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt2
- add program library dir to LD_LIBRARY_PATH (eterbug #11676)

* Mon Mar 27 2017 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt1
- fix bug with no save last session
- drop CDE support from code
- use xxd instead internal built bin2hdr
- add mingw build script, fix mingw build

* Mon Dec 26 2016 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt3
- fix build with wxGTK2.8
- fix all icons
- add MATE/LXDE support
- add rsa and ed25519 keys

* Fri Dec 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt2
- update license files, localize about dialog
- add 64x64 icons and fix packing
- do not warning about CUPS
- cleanup install dir
- rename desktop files
- replace opennx logo with rxclient logo

* Fri Dec 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt1
- initial build RX Client 0.17 for RX@Etersoft Terminal Server 1.1.4
- update russian translation
- add nxssh module support

* Fri May 20 2016 Vitaly Lipatov <lav@altlinux.ru> 0.16.e-alt32
- fix big using d instead ld at config session window
- append to commit "Now all paths write to config after start." ( 47816fbff3e6f4aee4142ae843fa3edda529ac77 )
- merge branch 'mainline' into sisyphus

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 0.16.e-alt31
- fix using string in login dialogs combobox

* Mon Oct 05 2015 Vitaly Lipatov <lav@altlinux.ru> 0.16.e-alt30
- fixed exit message: exit function now accept exit message
- fixed 'no sessions' bug
- fixed possible mistakes in code, added version dependency

* Sun Oct 04 2015 Anton Midyukov <antohami@altlinux.org> 0.16.e-alt29.svn724
- Rebuilt for new gcc5 C++11 ABI.

* Wed Aug 12 2015 Vitaly Lipatov <lav@altlinux.ru> 0.16.e-alt28.svn724
- fixed wrong cast, fixed 3.1.0 building

* Tue Aug 11 2015 Vitaly Lipatov <lav@altlinux.ru> 0.16.e-alt27.svn724
- fix release for build in ALT Linux

* Tue Aug 11 2015 Vitaly Lipatov <lav@altlinux.ru> 0.16-eter27.svn724
- add .gear in sisyphus branch
- fix compiles in all versions of wxWidgets (2.8, 2.9, 3.0, 3.1)
- do autoreconf

* Sun Jan 26 2014 Vitaly Lipatov <lav@altlinux.ru> 0.16-eter26.svn724
- fix build with libsmbclient from samba 4.0, fix symlink to libsmbclient

* Thu Oct 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.16-eter25.svn724
- remove PidFile option from cups config (eterbug #9490)

* Mon Aug 12 2013 Vitaly Lipatov <lav@altlinux.ru> 0.16-eter24.svn724
- use absolute path for links, fix requires

* Mon Aug 05 2013 Vitaly Lipatov <lav@altlinux.ru> 0.16-eter23.svn724
- add Num Lock state as a parameter to be send

* Mon Jun 10 2013 Denis Baranov <baraka@altlinux.ru> 0.16-eter22.svn724
- Add patch for translate

* Mon Feb 11 2013 Denis Baranov <baraka@altlinux.ru> 0.16-eter21.svn724
- Now all paths write to config after start

* Fri Jan 18 2013 Denis Baranov <baraka@altlinux.ru> 0.16-eter20.svn724
- Translate of Resume button correct
- Update translations
- Add translate for Wizard button

* Thu Jan 17 2013 Denis Baranov <baraka@altlinux.ru> 0.16-eter19.svn724
- Add copy icon in spec

* Fri Jan 04 2013 Denis Baranov <baraka@altlinux.ru> 0.16-eter18.svn724
- Add wizard button to start menu

* Thu Jan 03 2013 Denis Baranov <baraka@altlinux.ru> 0.16-eter17.svn724
- update from trunk opennx-0.16.0.724

* Fri Jun 01 2012 Denis Baranov <baraka@altlinux.ru> 0.16-eter17.svn708
- Initial build
- update from ALTLinux

* Fri Jun 17 2011 Boris Savelev <boris@altlinux.org> 0.16-alt16.svn634
- update from trunk

* Wed Mar 02 2011 Boris Savelev <boris@altlinux.org> 0.16-alt15.svn611
- update from trunk

* Mon Feb 28 2011 Lenar Shakirov <snejok@altlinux.ru> 0.16-alt14.svn595
- build fixed: disable opensc support by default

* Tue Feb 15 2011 Lenar Shakirov <snejok@altlinux.ru> 0.16-alt13.svn595
- lib{smbclient,cups}.so symlinks packaging fixed for x86_64

* Thu Nov 18 2010 Boris Savelev <boris@altlinux.org> 0.16-alt12.svn595
- update from trunk

* Sat Nov 13 2010 Lenar Shakirov <snejok@altlinux.ru> 0.16-alt11.svn567
- package nx-desktop.png (closes: #24467)

* Thu Sep 09 2010 Boris Savelev <boris@altlinux.org> 0.16-alt10.svn567
- update from trunk

* Tue Aug 31 2010 Boris Savelev <boris@altlinux.org> 0.16-alt9.svn555
- update from trunk

* Mon Aug 02 2010 Boris Savelev <boris@altlinux.org> 0.16-alt8.svn547
- update from trunk
- fix build

* Sat Feb 13 2010 Boris Savelev <boris@altlinux.org> 0.16-alt7.svn481
- update from trunk

* Mon Jan 25 2010 Boris Savelev <boris@altlinux.org> 0.16-alt6.svn450
- update from trunk (work with proxy with authorization)

* Sat Jan 16 2010 Boris Savelev <boris@altlinux.org> 0.16-alt5.svn446
- update from trunk
- add russian localization

* Thu Nov 12 2009 Boris Savelev <boris@altlinux.org> 0.16-alt4.svn444
- update from trunk
- add symlink for nxproxy

* Sun Oct 11 2009 Boris Savelev <boris@altlinux.org> 0.16-alt3.svn442
- update from trunk
- add symlinks for cups and samba

* Thu Sep 24 2009 Boris Savelev <boris@altlinux.org> 0.16-alt2.svn427
- update buildreq
- fix repocop warning

* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 0.16-alt1.svn418
- intial build for Sisyphus

* Sun Apr 19 2009 Fritz Elfert <fritz@fritz-elfert.de>
- Set prefix to /opt/lsb/%name for FHS compliance
* Wed Apr 15 2009 Michael Kromer <michael.kromer@millenux.com>
- Fixes for SuSE Plattform (openSuSE/SLES)
* Sun Jan  7 2007 Fritz Elfert <fritz@fritz-elfert.de>
- Initial package
