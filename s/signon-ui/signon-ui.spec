
%define _libexecdir %prefix/libexec

Name: signon-ui
Version: 0.17
Release: alt3

Group: System/Libraries
Summary: Online Accounts Sign-on Ui
Url: https://launchpad.net/signon-ui
License: GPLv3

Requires: dbus

Source: signon-ui-%version.tar
# FC
# ALT
Patch10: alt-fix-compile.patch
Patch11: alt-fix-crash.patch

# Automatically added by buildreq on Thu Jul 09 2015 (-bi)
# optimized out: elfutils glib2-devel kf5-attica-devel kf5-kjs-devel libGL-devel libX11-devel libaccounts-glib libaccounts-qt51 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgst-plugins1.0 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-xml libsignon-qt51 libstdc++-devel pkg-config python-base python3 python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-webkit-devel xorg-xproto-devel
BuildRequires: qt5-base-devel qt5-webengine-devel qt5-declarative-devel
BuildRequires: accounts-qt5-devel signon-devel libproxy-devel libnotify-devel

%description
Sign-on UI is the component responsible for handling the user interactions which
can happen during the login process of an online account.
It can show password dialogs and dialogs with embedded web pages.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n signon-ui-%version
%patch10 -p1
%patch11 -p1
sed -i 's/\/lib/\/%{_lib}/g' common-installs-config.pri
sed -i 's|tests| |' signon-ui.pro

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 \
    QMF_INSTALL_ROOT=%prefix \
    PREFIX=%prefix \
    CONFIG+=release \
    CONFIG+=force-foreign-qwindow \
    LIBDIR=%_libdir \
    LIBEXECDIR=%_libexecdir \
    signon-ui.pro

%make_build

%install
%install_qt5

# create directory for provider-specific configuration
mkdir -p %buildroot/%_sysconfdir/signon-ui/webkit-options.d

%files
%doc README TODO NOTES
%_bindir/signon-ui
%_desktopdir/signon-ui.desktop
%_datadir/dbus-1/services/*.service
%_sysconfdir/signon-ui

%changelog
* Mon Sep 30 2019 Sergey V Turchin <zerg@altlinux.org> 0.17-alt3
- update to 2017.10.22 snapshot

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2.7
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.7
- NMU: remove ubt from release

* Thu Jun 22 2017 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.7
- fix crash; thanks mcpain@alt

* Fri Apr 07 2017 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.6
- update to 0.17+17.04.20170320

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.5
- fix to build

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.4
- rebuild with foreign qwindow support

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.3
- redefine libexecdir

* Thu Dec 24 2015 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.2
- update to 0.17+15.10.20150810

* Thu Jul 09 2015 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.1
- initial build
