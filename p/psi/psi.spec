%define _unpackaged_files_terminate_build 1

%def_disable webkit

Name: psi
Version: 1.5
Release: alt1
Group: Networking/Instant messaging
Summary: Psi Jabber client
Summary(ru_RU.UTF-8): Jabber клиент Psi
License: GPL
Url: https://psi-im.org/

Source: %name-%version-%release.tar
Source1: iris.tar
Source2: libpsi.tar
Source3: http-parser.tar
Source4: qhttp.tar
Source5: plugins.tar
Patch0: %name-%version-%release.patch
Patch1: psi-0.14-alt-glibc-2.16.patch
Patch2: psi-1.3-build-qt511.patch
Patch3: psi-plus-alt-qt-5.11-window-close-bug.patch
Patch4: psi-1.5-build-qt515.patch

#BuildRequires: unzip
Requires: sound_handler ca-certificates
# Automatically added by buildreq on Tue Nov 25 2008
BuildRequires(pre): rpm-macros-qt5
BuildRequires: cmake gcc-c++ libXScrnSaver-devel libaspell-devel libcom_err-devel libqca-qt5-devel
BuildRequires: libotr-devel libhunspell-devel
BuildRequires: libtidy-devel >= 1.2.0
BuildRequires: libidn-devel zlib-devel
BuildRequires: qt5-base-devel qt5-multimedia-devel qt5-svg-devel qt5-tools qt5-x11extras-devel
%if_enabled webkit
BuildRequires: qt5-webkit-devel
%else
BuildRequires: qt5-webengine-devel
%endif
BuildRequires: libminizip-devel

Conflicts: qssl < 2.0 psi0.11
Obsoletes: psi0.11
Requires: qt5-base-common >= %_qt5_version
Requires: sox qca-qt5-ossl qca-qt5-gnupg

%description 
Psi is a Jabber Instant Messaging client based on Qt.  Jabber supports
gateways (transports) to other IM systems, such as ICQ, MSN, Yahoo and
AIM.  Psi supports many Jabber features, such as simulatenous login to
several servers, conferences, cryptographic abilities (via SSL and
GnuPG), connection via HTTP(S) proxy, etc.

%description -l ru_RU.UTF-8
Psi - это удобный графический клиент сети быстрого обмена сообщениями
Jabber.  Jabber имеет шлюзы в другие сети, включая ICQ, MSN, Yahoo и
AIM.  Psi поддерживает такие возможности Jabber, как одновременная
работа с несколькими серверами, конференции, криптозащиту передаваемой
информации (через SSL и GnuPG), работу через HTTP(S) прокси-сервер и
т.д.

%package plugins
Summary: Plugins pack for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugins
This package contains stable plugins for %name.
List of plugins included:

* Attention Plugin
  This plugin is designed to send and receive special messages such as
  Attentions.

* Autoreply Plugin
  This plugin acts as an auto-answering machine.

* Birthday Reminder Plugin
  This plugin is designed to show reminders of upcoming birthdays.

* Chess Plugin
  This plugin allows you to play chess with your friends.
  The plugin is compatible with a similar plugin for Tkabber.

* Cleaner Plugin
  This plugin is designed to clear the avatar cache, saved local copies
  of vCards and history logs.

* Client Switcher Plugin
  This plugin is intended to spoof version of the Jabber client, the
  name and type of operating system. It is possible to manually specify
  the version of the client and the operating system or choose from a
  predefined list.

* Conference Logger Plugin
  This plugin is designed to save conference logs in which the Psi+
  user sits.

* Content Downloader Plugin
  This plugin can currently be used to download and install roster
  iconsets and emoticons.

* Enum Messages Plugin
  The plugin is designed to enumerate messages, adding the messages
  numbers in chat logs and notification of missed messages. Supports
  per contact on / off message enumeration via the buttons on the chats
  toolbar.

* Extended Menu Plugin
  This plugin adds roster submenu 'Extended Actions' to contact's
  context menu. At the moment we have the following items: 'Copy JID',
  'Copy the nickname', 'Copy the status message' and 'Ping'.

* Extended Options Plugin
  This plugin is designed to allow easy configuration of some advanced
  options in Psi+. This plugin gives you access to advanced application
  options, which do not have a graphical user interface.

* GnuPG Plugin
  GnuPG Key Manager can create, remove, export and import GnuPG keys.
  It can do only the base operations but I hope it will be enough for your needs

* Gomoku Game Plugin
  This plugin allows you to play gomoku with your friends.
  For sending commands, normal messages are used, so this plugin will always
  work wherever you are able to log in.To invite a friend for a game, you can
  use contact menu item or the button on the toolbar in a chat window.

* History Keeper Plugin
  This plugin is designed to remove the history of selected contacts
  when the Psi+ is closed.

* HTTP Upload Plugin
  This plugin allows uploading images and other files via XEP-0363.

* ICQ Must Die Plugin
  This plugin is designed to help you transfer as many contacts as
  possible from ICQ to Jabber.

* Image Plugin
  This plugin is designed to send images to roster contacts.

* Image Preview Plugin
  This plugin shows the preview image for an image URL.

* Juick Plugin
  This plugin is designed to work efficiently and comfortably with the
  Juick microblogging service.

* Off-the-Record Messaging Plugin
  a cryptographic protocol that provides strong encryption for instant
  messaging conversations. OTR uses a combination of the AES
  symmetric-key algorithm, the Diffie-Hellman key exchange, and the SHA-1
  hash function. In addition to authentication and encryption, OTR
  provides perfect forward secrecy and malleable encryption.

* PEP Change Notify Plugin
  The plugin is designed to display popup notifications on change of
  moods, activities and tunes at the contacts of the roster. In the
  settings you can choose which ones to include notification of events,
  specify the time within which a notice will appear, as well as play a
  sound specify.

* Qip X-statuses Plugin
  This plugin is designed to display X-statuses of contacts using the
  QIP Infium jabber client.

* Screenshot Plugin
  This plugin allows you to make a snapshot (screenshot) of the screen,
  edit the visible aria to make a screenshot and save the image to a
  local drive or upload to HTTP/FTP server.

* Skins Plugin
  This plugin is designed to create, store and apply skins to Psi+.

* Stop Spam Plugin
  This plugin is designed to block spam messages and other unwanted
  information from Psi+ users.

* Storage Notes Plugin
  This plugin is an implementation of XEP-0049: Private XML Storage.
  The plugin is fully compatible with notes saved using Miranda IM.
  The plugin is designed to keep notes on the jabber server with the
  ability to access them from anywhere using Psi+ or Miranda IM.

* Translate Plugin
  This plugin allows you to convert selected text into another language.

* Video Status Changer Plugin
  This plugin is designed to set the custom status when you see the
  video in selected video player. Communication with players made by
  D-Bus.

* Watcher Plugin
  This plugin is designed to monitor the status of specific roster contacts,
  as well as for substitution of standard sounds of incoming messages.
  On the first tab set up a list of contacts for the status of
  which is monitored. When the status of such contacts changes a popup window
  will be shown and when the status changes to online a custom sound
  can be played.
  On the second tab is configured list of items, the messages
  are being monitored. Each element can contain a regular expression to
  check for matches with JID, from which the message arrives, a list of
  regular expressions to check for matches with the text of an incoming message,
  the path to sound file which will be played in case of coincidence,
  as well as the setting, whether the sound is played always, even if the
  global sounds off.

Plugins without description yet:
* Jabber Disk Plugin
* Message Filter Plugin

%prep
%setup -q -n %name-%version-%release -a1 -a2 -a3 -a4 -a5
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch4 -p1
mv libpsi src/
mv qhttp 3rdparty/
mv http-parser 3rdparty/
rm -rf src/plugins/deprecated/
mv -f plugins/* src/plugins/
mkdir -p lang/
rm -rf src/libpsi/tools/zip/minizip

%patch3 -p2

%build
%cmake \
    -DBUILD_PLUGINS="ALL" \
    -DENABLE_PLUGINS=ON \
    -DBUILD_DEV_PLUGINS=ON
#
%cmake_build

lrelease-qt5 psi_ru.ts

%install
%cmakeinstall_std
mv %buildroot/%_libdir/%name{-plus,}/
install -Dm644 psi_ru.qm %buildroot%_datadir/psi/lang/psi_ru.qm

# remove unstable plugins
rm -f %buildroot%_libdir/%name/plugins/libbattleshipgameplugin.so
rm -f %buildroot%_libdir/%name/plugins/libripperccplugin.so

%files
%defattr(0644,root,root,0755)
%doc README COPYING INSTALL TODO 
%attr(0755,root,root) %_bindir/psi
%dir %_datadir/psi
%_datadir/psi/*
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%files plugins
%_libdir/%name/plugins/libattentionplugin.so
%_libdir/%name/plugins/libautoreplyplugin.so
%_libdir/%name/plugins/libbirthdayreminderplugin.so
%_libdir/%name/plugins/libchessplugin.so
%_libdir/%name/plugins/libcleanerplugin.so
%_libdir/%name/plugins/libclientswitcherplugin.so
%_libdir/%name/plugins/libconferenceloggerplugin.so
%_libdir/%name/plugins/libcontentdownloaderplugin.so
%_libdir/%name/plugins/libenummessagesplugin.so
%_libdir/%name/plugins/libextendedmenuplugin.so
%_libdir/%name/plugins/libextendedoptionsplugin.so
%_libdir/%name/plugins/libgnupgplugin.so
%_libdir/%name/plugins/libgomokugameplugin.so
%_libdir/%name/plugins/libhistorykeeperplugin.so
%_libdir/%name/plugins/libhttpuploadplugin.so
%_libdir/%name/plugins/libicqdieplugin.so
%_libdir/%name/plugins/libimageplugin.so
%_libdir/%name/plugins/libimagepreviewplugin.so
%_libdir/%name/plugins/libjabberdiskplugin.so
%_libdir/%name/plugins/libjuickplugin.so
%_libdir/%name/plugins/libmessagefilterplugin.so
%_libdir/%name/plugins/libotrplugin.so
%_libdir/%name/plugins/libpepchangenotifyplugin.so
%_libdir/%name/plugins/libqipxstatusesplugin.so
%_libdir/%name/plugins/libscreenshotplugin.so
%_libdir/%name/plugins/libskinsplugin.so
%_libdir/%name/plugins/libstopspamplugin.so
%_libdir/%name/plugins/libstoragenotesplugin.so
%_libdir/%name/plugins/libtranslateplugin.so
%_libdir/%name/plugins/libvideostatusplugin.so
%_libdir/%name/plugins/libwatcherplugin.so

%changelog
* Fri Oct 02 2020 Oleg Solovyov <mcpain@altlinux.org> 1.5-alt1
- Updated to version 1.5

* Wed Nov 21 2018 Oleg Solovyov <mcpain@altlinux.org> 1.4-alt1
- Updated to version 1.4
- disabled QtWebKit (Closes: #37380)

* Wed Oct 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt4
- NMU: fixed main window blanking issue which appears on closing main window in a specific way.

* Thu Sep 13 2018 Oleg Solovyov <mcpain@altlinux.org> 1.3-alt3
- fix build with Qt 5.11
- build with new libhunspell

* Wed Apr 25 2018 Oleg Solovyov <mcpain@altlinux.org> 1.3-alt2
- Built plugins
- Used CMake to build

* Thu Apr 19 2018 Oleg Solovyov <mcpain@altlinux.org> 1.3-alt1
- Updated to version 1.3
- Updated Russian translation from upstream
- Built using Qt5

* Fri Dec 18 2015 Mikhail Efremov <sem@altlinux.org> 0.16-alt1.git1.ccc24db
- Drop history dialog patch.
- Updated to current git.

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt3.1
- Fixed for build with glibc 2.16

* Thu Dec 24 2009 Anton Farygin <rider@altlinux.ru> 0.14-alt3
- updated URL in specfile (closes #21487)
- updated Russian translation (closes #21710)

* Thu Dec 24 2009 Anton Farygin <rider@altlinux.ru> 0.14-alt2
- add history dialog patch from dfo@

* Thu Dec 10 2009 Anton Farygin <rider@altlinux.ru> 0.14-alt1
- new version

* Fri Sep 04 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt4
- new version

* Mon Apr 27 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt3.git11.487e3d4
- new snapshot

* Fri Apr 17 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt3.git10.65d8d0c
- new snapshot

* Thu Apr 16 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt3.git9.c25355e
- new snapshot

* Wed Apr 15 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt3.git8.36d25d7
- added workaround for threaded sender() and QT-4.5 in iris (closes #19391)
- added qca2-gnupg and qca2-ossl requires

* Sat Apr 11 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt2.git8.36d25d7
- revert broken patch from mike@ for drop psi-related cpu wakeups

* Sat Apr 11 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt1.git8.36d25d7
- new snapshot

* Sat Apr 04 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt0.git8.f6760d1
- build with external libqca2

* Sat Apr 04 2009 Michael Shigorin <mike@altlinux.org> 0.13-alt0.git7.f6760d1
- NMU: applied crude patch to drop psi-related cpu wakeups
  (http://lists.affinix.com/pipermail/psi-devel-affinix.com/2008-September/008236.html)

* Sat Mar 28 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt0.git6.f6760d1
- new snapshot
- disabled AVCALL
- disabled whiteboarding

* Tue Mar 03 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt0.git4.561bb4f
- new snapshot
- translations fixed (#17788)

* Sat Feb 07 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt0.git3.57c98f2
- new snapshot

* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 0.13-alt0.git1.20e6902
- updated to 0.13 snapshot
- removed post-scripts
- updated patches

* Mon Sep 01 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt2.svn1173
- fixed psi mainwindow options (hide/unhide from tray)

* Wed Jul 30 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1173
- new snapshot (0.12-release)
- updated translations

* Wed Jun 18 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1167
- new snapshot
- workaround for segfault with enabled spellchecker and QT-4.4.0: 
    don't use WaveUnderline in SpellHighlighter format

* Fri May 16 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1157
- new snapshot
- translation updates and fixes

* Tue May 13 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1148
- new snapshot

* Thu May 08 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1138
- new snapshot

* Mon Apr 28 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1131
- new snapshot
- updated translation

* Tue Apr 22 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1109
- new snapshot

* Thu Apr 17 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1104
- new snapshot

* Mon Apr 07 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1100
- new snapshot

* Thu Mar 20 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1086
- new snapshot
- dbus connection patch included to mainstream

* Wed Mar 05 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1069
- new snaphot
- trying to fix dbus connection with numeric profile

* Wed Feb 27 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1064
- new snapshot

* Tue Feb 26 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1061
- new snapshot

* Tue Sep 18 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt3svn20070918
- added requires to sox (#12427)

* Tue Sep 18 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070918
- updated from mainstream:
    Justin's SASL fix (auth with openfire servers)

* Mon Sep 17 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070917
- update from mainstream

* Fri Aug 03 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070803
-  update from mainstream, RC2
- added requires to libQT4 >= %{get_version libqt4-core}

* Mon Jul 09 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070709
- update from mainstream

* Tue Jun 05 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070605
- update from mainstream

* Wed May 23 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070523
- update from mainstream
- updated russian translation from Andrey Cherepanov

* Sun May 13 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070513
- update from mainstream

* Fri May 11 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070511
- update from mainstream

* Thu May 03 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070503
- update from mainstream

* Fri Apr 20 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070420
- update from mainstream repository
- added russian translation
- build with aspell
- use system locale for translation

* Mon Apr 16 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070416
- update from mainstream repository

* Fri Apr 13 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070413
- new version from subversion repository

* Mon Feb 20 2006 Anton Farygin <rider@altlinux.ru> 0.10-alt3cvs20051215
- NMU (rebuild for x86_64, without changes)

* Mon Dec 12 2005 Mikhail Yakshin <greycat@altlinux.org> 0.10-alt2cvs20051215
- 0.10 prerelease (based on current darcs snapshot)
- added muc-bundle patches from
  http://norman.rasmussen.co.za/darcs/psi-muc-bundle/
  http://norman.rasmussen.co.za/darcs/psi-muc/

* Sun Oct 02 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.10-alt1cvs20050312
- updated translation

* Sat Mar 12 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.10-alt0cvs20050312
- 0.9.3 + cvs changes on 20050312
- global accels went into upstream
- adhoc+rc patch applied

* Sat Jan 01 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.9.3-alt0.test2
- 0.9.3-test2, lots of bugfixes
- disabled global accels by default (one can enable by hand-editing config)

* Tue Dec 14 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.9.3-alt0.cvs20041214
- 0.9.3-test1, slightly fixed from cvs20041214 snapshot

* Mon Aug 02 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.9.2-alt2
- added default data proxy
- fixed "play" calls to use sound_handler wrapper scripts

* Fri Jun 11 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Sat May 15 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.9.2-alt0.test1
- 0.9.2-test1
- incomplete translation
- removed iconsets, they are in ancient non-supported format anyway

* Sat Jan  3 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.9.1-alt0.1
- 0.9.1
- all patches got into mainstream (doubting about mainwin patch)
- got translation from CVS

* Thu Sep 18 2003 Mikhail Yakshin <greycat@altlinux.ru> 0.9-alt3
- added psi dudes, aqualight, businessblack icon sets
- added gpg correction patch

* Fri Jul 11 2003 Mikhail Yakshin <greycat@altlinux.ru> 0.9-alt2
- removed all patches
- updated russian translation
- added tray icon patch (transparent background in kwin)
- added main window customized flag patch ("tool window" working)
- spec cleanup

* Wed Jun 25 2003 Mikhail Yakshin <greycat@altlinux.ru> 0.9-alt1
- 0.9 release
- removed all patches except for sysname (got into mainstream)
- updated russian translation
- spec cleanup
- added 4 more iconsets, several renewed

* Thu May 15 2003 Stanislav Ievlev <inger@altlinux.ru> 0.8.7-alt5.1
- fix closing in kde when program in dock

* Sun Dec 15 2002 Rider <rider@altlinux.ru> 0.8.7-alt5
- updated russian translation from Valentina

* Fri Dec 13 2002 Rider <rider@altlinux.ru> 0.8.7-alt4
- WhatsThis patch from Greycat

* Mon Nov 25 2002 Rider <rider@altlinux.ru> 0.8.7-alt3
- BuildRequires fix (unzip)

* Fri Nov 22 2002 Rider <rider@altlinux.ru> 0.8.7-alt2
- added iconset
- fixed bug for proxy port setup
- fixed URL

* Sun Nov 10 2002 Rider <rider@altlinux.ru> 0.8.7-alt1
- requires fix (libqt3)
- Russian language pack from Valentina Vaneeva <fattie at altlinux ru>

* Tue Nov 05 2002 Rider <rider@altlinux.ru> 0.8.7-alt0.1
- 0.8.7

* Wed Sep 25 2002 Rider <rider@altlinux.ru> 0.8.6-alt4
- requires fix

* Fri Sep 20 2002 Rider <rider@altlinux.ru> 0.8.6-alt3
- rebuild

* Thu Aug 08 2002 Rider <rider@altlinux.ru> 0.8.6-alt2
- proxy port fix and options helper (Mikhail Yakshin aka GreyCat)
- libqssl location fix (me)
- Russian langpack

* Tue Jul 09 2002 Rider <rider@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Mon Apr 01 2002 Rider <rider@altlinux.ru> 0.8.5-alt1
- first build for ALT Linux, based on MandrakeSoft package
- openssl patch

* Tue Feb  8 2002 Alexander Skwar <ASkwar@DigitalProjects.com> 0.8.4-1mdk
- 0.8.4

* Mon Jan 14 2002 Alexander Skwar <ASkwar@Linux-Mandrake.com> 0.8.3.1-1mdk
- First Mandrake release, based on the Conectiva pacakge

* Tue Dec 18 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.8.3.1-1cl
- New minor bugfix version

* Tue Nov 13 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.8.2-1cl
- Bug fix adn new features release
- Name changed. Author uses 0.8.x nomenclature, leaving 0.8x lost
- Epoch added

* Mon Nov 12 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.81-4cl
- Minor Spec changes
- Solved install dir problems

* Fri Nov 09 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.81-3cl
- Added description
- Added menu items
- Added icons

* Fri Nov 09 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.81-2cl
- Added patch to enable right datadir

* Fri Nov 09 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.81-1cl
- First CL package
- Really bad way to install
