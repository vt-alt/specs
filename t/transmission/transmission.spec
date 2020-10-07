%define _unpackaged_files_terminate_build 1

%define _optlevel s
%def_enable qt

%define rname Transmission
%define dname transmission-daemon

Name: transmission
Version: 3.00
Release: alt2

Group: Networking/File transfer
Summary: Llightweight BitTorrent client
License: GPLv2 + MIT
Url: http://www.transmissionbt.com/

Provides: %rname = %EVR

Obsoletes: %name-benc2php
Obsoletes: %name-proxy

Requires: %name-gui = %EVR
Requires: %name-cli = %EVR
Requires: %name-remote = %EVR
Requires: %name-daemon = %EVR

Requires(post,postun): desktop-file-utils

Source: http://download.m0k.org/%name/files/%name-%version.tar
Patch1: %name-alt-desktop.patch
Patch2: %name-alt-extra-doc-disable.patch
Source1: %dname.init
Source2: %dname.logrotate
Source3: %dname.service
Source4: %name-%version-third-party-dht.tar
Source5: %name-%version-third-party-libutp.tar

BuildPreReq: desktop-file-utils

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++ glibc-devel libcurl-devel libevent-devel libnotify-devel libcanberra-devel libdbus-glib-devel libgtk+3-devel
BuildRequires(pre): rpm-utils desktop-file-utils libalternatives-devel rpm-build-ubt openssl-devel
BuildRequires: libb64-devel
BuildRequires: libnatpmp-devel
BuildRequires: libminiupnpc-devel
%if "%(rpmvercmp '%{get_version glibc-core}' '2.9')" >= "0"
BuildRequires: libgio-devel
%endif
%if_enabled qt
BuildRequires: qt5-base-devel qt5-tools-devel
%endif

%description
Transmission has been built from the ground up to be a lightweight,
yet powerful BitTorrent client. Its simple, intuitive interface
strikes a balance between providing useful functionality without
feature bloat. Furthermore, it is free for anyone to use or modify.

%package common
Group: Networking/File transfer
Summary: Common files for %name
Conflicts: %name < 1.00-alt10
%description common
Common files for %name

%package gui-common
Group: Networking/File transfer
Summary: Common files for %name
Requires: %name-common = %EVR
%description gui-common
Common files for %name

%package gtk
Group: Networking/File transfer
Summary: Graphical BitTorrent client
Provides: %name-gui = %EVR
Requires: %name-common = %EVR
Requires: %name-gui-common = %EVR
%description gtk
GTK-based graphical BitTorrent client

%if_enabled qt
%package qt
Group: Networking/File transfer
Summary: Graphical BitTorrent client
Provides: %name-gui = %EVR
Requires: %name-common = %EVR
Requires: %name-gui-common = %EVR
%description qt
Qt-based graphical BitTorrent client
%endif

%package cli
Group: Networking/File transfer
Summary: Command line BitTorrent client
Requires: %name-common = %EVR
%description cli
Command line BitTorrent client

%package remote
Group: Networking/Remote access
Summary: Command line remote interface to %name-daemon
Requires: %name-common = %EVR
%description remote
Command line remote interface to %name-daemon

%package daemon
Group: Networking/File transfer
Summary: Daemonised BitTorrent client
Requires: %name-common = %EVR
%description daemon
Daemonised BitTorrent client

%prep
%setup -a4 -a5
%patch1 -p1
%patch2 -p1

%build
%cmake \
	-DENABLE_GTK:BOOL=YES \
%if_enabled qt
	-DENABLE_QT:BOOL=YES \
%endif
	-DENABLE_CLI:BOOL=YES \
	-DUSE_SYSTEM_EVENT2:BOOL=YES \
	-DUSE_SYSTEM_MINIUPNPC:BOOL=YES \
	-DUSE_SYSTEM_NATPMP:BOOL=YES \
	-DUSE_SYSTEM_B64:BOOL=YES \
	%nil

%cmake_build

%install
%cmakeinstall_std

# made alternatives entries
mkdir -p %buildroot/%_altdir

cat >%buildroot/%_altdir/%name-gtk <<__EOF__
%_bindir/%name %_bindir/%name-gtk 30
__EOF__

%if_enabled qt
cat >%buildroot/%_altdir/%name-qt <<__EOF__
%_bindir/%name %_bindir/%name-qt 20
__EOF__
%endif

%find_lang %name-gtk

# install daemonic stuff

install -pD -m640 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%dname
install -pD -m755 %SOURCE1 %buildroot%_initdir/%dname
install -pD -m644 %SOURCE3 %buildroot%systemd_unitdir/transmission-daemon.service

mkdir -p %buildroot/%_sysconfdir/transmission-daemon/
BUILD/daemon/transmission-daemon -d 2> %buildroot/%_sysconfdir/transmission-daemon/settings.json
sed -i 's,/usr/src/,/var/lib/transmission-daemon/,' %buildroot/%_sysconfdir/transmission-daemon/settings.json

mkdir -p %buildroot/%_sysconfdir/sysconfig/
echo "TRANSMISSION_OPTIONS=\"-e %_logdir/%dname/%dname.log -g %_localstatedir/%dname\"" > %buildroot/%_sysconfdir/sysconfig/%dname

mkdir -p %buildroot/%_logdir/%dname
mkdir -p %buildroot/%_localstatedir/%dname

%check
pushd BUILD
ctest
popd

%pre daemon
/usr/sbin/groupadd -r -f _%dname
/usr/sbin/useradd -r -g _%dname -d %_localstatedir/%dname -s /dev/null -c 'The Transmission Torrent Client' _%dname >/dev/null 2>&1 ||:
if [ $1 -gt 1 ]; then
        /usr/sbin/usermod -d %_localstatedir/%dname _%dname
fi

%files

%files common
%dir %_datadir/%name
%_datadir/%name/web/

%files gui-common
%_iconsdir/hicolor/*/*/*
%_datadir/applications/%name.desktop

%files gtk -f %name-gtk.lang
%doc AUTHORS COPYING NEWS.md README.md ChangeLog
%_bindir/%name-gtk
%_altdir/%name-gtk
%_man1dir/%name-gtk.1*
%_datadir/appdata/transmission-gtk.appdata.xml

%if_enabled qt
%files qt
%doc AUTHORS COPYING NEWS.md README.md ChangeLog
%_bindir/%name-qt
%_altdir/%name-qt
%_datadir/%name/translations/%{name}_*.qm
%_man1dir/%name-qt.1*
%endif

%files cli
%doc AUTHORS COPYING NEWS.md README.md ChangeLog
%_bindir/%name-create
%_man1dir/%name-create.*
%_bindir/%name-edit
%_man1dir/%name-edit.*
%_bindir/%name-show
%_man1dir/%name-show.*
%_bindir/transmission-cli
%_man1dir/transmission-cli.*

%files remote
%doc AUTHORS COPYING NEWS.md README.md ChangeLog
%_bindir/%name-remote
%_man1dir/%name-remote.*

%files daemon
%doc AUTHORS COPYING NEWS.md README.md ChangeLog
%_bindir/%name-daemon
%_man1dir/%name-daemon.*
%systemd_unitdir/transmission-daemon.service
%config(noreplace) %_sysconfdir/logrotate.d/%dname
%config(noreplace) %_sysconfdir/sysconfig/%dname
%config %_initdir/%dname
%attr(710,root,_%dname) %dir %_sysconfdir/%dname
%config(noreplace) %_sysconfdir/%dname/settings.json
%attr(771,root,_%dname) %dir %_localstatedir/%dname
%attr(770,root,_%dname) %dir %_logdir/%dname

%changelog
* Tue Sep 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.00-alt2
- Switched to cmake build system.
- Removed wxGTK from spec.
- Enabled tests.

* Mon Sep 21 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.00-alt1
- Updated to upstream version 3.00.
- Enabled cli client.
- Packaged debuginfo for transmission-qt.

* Sun Mar 10 2019 Michael Shigorin <mike@altlinux.org> 2.94-alt5
- fix build on e2k with lcc

* Sat Mar 02 2019 Anton Farygin <rider@altlinux.ru> 2.94-alt4
- rebuilt with libevent-2.1

* Mon Sep 03 2018 Anton Farygin <rider@altlinux.ru> 2.94-alt3
- rebuilt with libopenssl1.1

* Wed Jul 18 2018 Anton Farygin <rider@altlinux.ru> 2.94-alt2%ubt
- fixed exec section in  desktop file

* Mon Jul 16 2018 Anton Farygin <rider@altlinux.ru> 2.94-alt1%ubt
- 2.94
- build transmission-qt with qt5

* Mon Apr 09 2018 Anton Farygin <rider@altlinux.ru> 2.93-alt1%ubt
- 2.93

* Mon Jan 15 2018 Anton Farygin <rider@altlinux.ru> 2.92-alt5%ubt
- added fix for security flaw in RPC (closes: #34459)

* Mon Jul 04 2016 Yuri N. Sedunov <aris@altlinux.org> 2.92-alt4
- fixed build with glib2 >= 2.48

* Fri Mar 11 2016 Anton Farygin <rider@altlinux.ru> 2.92-alt3
- fixed permission for access to the daemon Download directory  (closes: #26984)

* Fri Mar 11 2016 Anton Farygin <rider@altlinux.ru> 2.92-alt2
- fixed permission for the log directory (closes: #26710)
- added condreload and reload targets to initscript (closes: #31046)

* Thu Mar 10 2016 Anton Farygin <rider@altlinux.ru> 2.92-alt1
- new version

* Thu Aug 28 2014 Anton Farygin <rider@altlinux.ru> 2.84-alt1
- new version

* Mon Jun 02 2014 Anton Farygin <rider@altlinux.ru> 2.83-alt1
- new version

* Mon Sep 02 2013 Anton Farygin <rider@altlinux.ru> 2.82-alt1
- new version

* Mon Jul 15 2013 Anton Farygin <rider@altlinux.ru> 2.80-alt1
- new version
- removed unsupported "Custom icon" feathure from QT frontend

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 2.71-alt1
- new version

* Tue Aug 21 2012 Anton Farygin <rider@altlinux.ru> 2.61-alt1
- new version

* Wed May 30 2012 Anton Farygin <rider@altlinux.ru> 2.52-alt1
- new version

* Sat Oct 22 2011 Anton Farygin <rider@altlinux.ru> 2.42-alt1
- new version

* Wed Oct 12 2011 Anton Farygin <rider@altlinux.ru> 2.41-alt1
- new version

* Mon Aug 29 2011 Anton Farygin <rider@altlinux.ru> 2.33-alt1
- new version

* Tue Jul 05 2011 Anton Farygin <rider@altlinux.ru> 2.32-alt1
- new version

* Tue May 31 2011 Anton Farygin <rider@altlinux.ru> 2.31-alt2
- fixed Exec in desktop (closes: #25691)

* Mon May 30 2011 Anton Farygin <rider@altlinux.ru> 2.31-alt1
- new version
- build with dbus-glib (closes: #25684)

* Fri Apr 22 2011 Anton Farygin <rider@altlinux.ru> 2.22-alt2
- add systemd support (closes: #25438)

* Wed Mar 09 2011 Anton Farygin <rider@altlinux.ru> 2.22-alt1
- new version

* Thu Dec 16 2010 Anton Farygin <rider@altlinux.ru> 2.13-alt1
- new version

* Thu Dec 02 2010 Anton Farygin <rider@altlinux.ru> 2.12-alt1
- new version

* Wed Nov 03 2010 Anton Farygin <rider@altlinux.ru> 2.11-alt1
- new version

* Thu Sep 16 2010 Anton Farygin <rider@altlinux.ru> 2.04-alt2
- Build with libcanberra and libnotify
- remove daemon requires in transmission-remote package

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 2.04-alt1
- new version

* Mon Jul 12 2010 Anton Farygin <rider@altlinux.ru> 1.93-alt2
- added initscript for transmission-daemon by Timur Batyrshin (Closes: 23751, 21190)

* Tue Jun 01 2010 Anton Farygin <rider@altlinux.ru> 1.93-alt1
- new version

* Wed Feb 24 2010 Anton Farygin <rider@altlinux.ru> 1.91-alt1
- new version

* Wed Feb 24 2010 Anton Farygin <rider@altlinux.ru> 1.76-alt3
- add patches from upstream 1.7x branch with fix for CVE-2010-0012 (closes: #23019)

* Mon Oct 26 2009 Sergey V Turchin <zerg@altlinux.org> 1.76-alt2
- qtr: accept close window event when application exiting

* Mon Oct 26 2009 Anton Farygin <rider@altlinux.ru> 1.76-alt1
- new version

* Wed Oct 21 2009 Sergey V Turchin <zerg@altlinux.org> 1.75-alt2
- qtr: allow customize application icon in session dialog

* Wed Sep 16 2009 Anton Farygin <rider@altlinux.ru> 1.75-alt1
- new version

* Tue Sep 01 2009 Anton Farygin <rider@altlinux.ru> 1.74-alt1
- new version

* Thu Aug 13 2009 Sergey V Turchin <zerg@altlinux.org> 1.73-alt2
- build qtr
- qtr: add russian translation
- qtr: close main window to tray
- qtr: fix raise main window

* Wed Aug 05 2009 Anton Farygin <rider@altlinux.ru> 1.73-alt1
- new version

* Tue Jun 30 2009 Anton Farygin <rider@altlinux.ru> 1.72-alt1
- new version

* Thu May 14 2009 Anton Farygin <rider@altlinux.ru> 1.61-alt2
- add patch from mainstream:
    - #2073: can't upload new torrent file in web ui

* Wed May 13 2009 Anton Farygin <rider@altlinux.ru> 1.61-alt1
- new version

* Wed May 06 2009 Anton Farygin <rider@altlinux.ru> 1.60-alt1
- new version

* Tue Apr 14 2009 Anton Farygin <rider@altlinux.ru> 1.52-alt1
- new version

* Thu Mar 05 2009 Anton Farygin <rider@altlinux.ru> 1.51-alt0.M40.1
- new version

* Mon Feb 16 2009 Anton Farygin <rider@altlinux.ru> 1.50-alt1
- new version
- fixed build from svn
- build with system libevent
- buildreq updated

* Thu Jan 15 2009 Yuri N. Sedunov <aris@altlinux.org> 1.42-alt1
- new version

* Sat Nov 08 2008 Yuri N. Sedunov <aris@altlinux.org> 1.34-alt2
- fix altbug #17817 (patch0)

* Mon Sep 22 2008 Yuri N. Sedunov <aris@altlinux.org> 1.34-alt1.1
- packaged builtin web-server

* Fri Sep 19 2008 Yuri N. Sedunov <aris@altlinux.org> 1.34-alt1
- new version for Sisyphus
- updated buildreqs
- removed {update,clean}_menus from post{,un}

* Tue Aug 05 2008 Sergey V Turchin <zerg at altlinux dot org> 1.22-alt0.M40.1
- new version

* Thu May 08 2008 Sergey V Turchin <zerg at altlinux dot org> 1.11-alt0.M40.1
- new version

* Tue Apr 01 2008 Sergey V Turchin <zerg at altlinux dot org> 1.10-alt0.M40.1
- new version

* Wed Mar 05 2008 Sergey V Turchin <zerg at altlinux dot org> 1.06-alt0.M40.1
- new version

* Tue Feb 19 2008 Sergey V Turchin <zerg at altlinux dot org> 1.05-alt0.M40.1
- new version

* Thu Feb 07 2008 Sergey V Turchin <zerg at altlinux dot org> 1.04-alt0.M40.1
- new version 

* Sat Jan 26 2008 Sergey V Turchin <zerg at altlinux dot org> 1.02-alt0.M40.1
- new version

* Tue Jan 15 2008 Sergey V Turchin <zerg at altlinux dot org> 1.01-alt0.M40.1
- new version
- split to subpackages

* Wed Jan 09 2008 Sergey V Turchin <zerg at altlinux dot org> 1.00-alt0.M40.1
- new version

* Wed Dec 12 2007 Sergey V Turchin <zerg at altlinux dot org> 0.96-alt0.M40.1
- new version

* Thu Dec 06 2007 Sergey V Turchin <zerg at altlinux dot org> 0.95-alt0.M40.1
- new version

* Wed Nov 28 2007 Sergey V Turchin <zerg at altlinux dot org> 0.94-alt0.M40.1
- new version

* Sat Sep 08 2007 Sergey V Turchin <zerg at altlinux dot org> 0.81-0.1.M40
- initial specfile

