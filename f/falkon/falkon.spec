# spec file for package qupzilla
# Original author: Mariusz Fik (Fisiu)
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself.

%define sover 3
%define libfalkonprivate libfalkonprivate%sover

Name: falkon
Version: 3.1.0
Release: alt3
%K5init no_altplace

Summary: A very fast open source browser based on WebKit core
License: GPLv3+
Group: Networking/WWW
Url: https://www.falkon.org/

Source: %name-%version.tar
Patch1: alt-qt515.patch
# Automatically added by buildreq on Thu Apr 07 2016
# optimized out: fontconfig gcc-c++ libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel pkg-config python-base python-modules qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: libssl-devel libxcbutil-devel
BuildRequires: qt5-multimedia-devel qt5-script-devel qt5-tools-devel qt5-webengine-devel qt5-websockets-devel qt5-x11extras-devel
BuildRequires: kf5-kwallet-devel kf5-ki18n-devel kf5-kio-devel kf5-kcrash-devel kf5-kcoreaddons-devel kf5-purpose-devel
BuildRequires: libgnome-keyring-devel

%description
Falkon is a new and very fast World Wide Web Browser
which uses Qt Framework and its QtWebEngine rendering core.
It is a lightweight browser with some advanced functions
like integrated AdBlock, Search Engines Manager, Theming
support, Speed Dial and SSL Certificate manager.

%package core
Group: Graphical desktop/KDE
Summary: Falkon KDE integration
Requires(post,preun): alternatives >= 0.2
Provides: webclient
Provides: %name = %EVR
Obsoletes: %name < %EVR
Provides:  qupzilla = %version-%release
Obsoletes: qupzilla < %version-%release
%description core
Falkon KDE integration.

%package kde5
Group: Graphical desktop/KDE
Summary: Falkon KDE integration
Requires: %{name}-core
Provides: webclient
Provides: %name = %version-%release
Provides: %name-kde = %version-%release
Provides:  qupzilla-kde5 = %version-%release
Obsoletes: qupzilla-kde5 < %version-%release
Obsoletes: rekonq < 2.5
%description kde5
Falkon KDE integration.

%package gnome3
Group: Graphical desktop/GNOME
Summary: Falkon GNOME integration
Requires: %{name}-core
Provides: webclient
Provides: %name = %version-%release
Provides: %name-gnome = %version-%release
Provides:  qupzilla-gnome3 = %version-%release
Obsoletes: qupzilla-gnome3 < %version-%release
%description gnome3
Falkon GNOME integration.

%package -n %libfalkonprivate
Group: System/Libraries
Summary: %name library
#Requires: %name-common
%description -n %libfalkonprivate
%name library

%prep
%setup
%patch1 -p1

%build
%K5build

%install
%K5install
ln -s falkon %buildroot/%_K5bin/qupzilla

#install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/xbrowser       %_K5bin/falkon      111
%_bindir/x-www-browser       %_K5bin/falkon      111
__EOF__

%find_lang --all-name --with-qt %name

%files core -f %name.lang
%config /%_sysconfdir/alternatives/packages.d/%name
%_K5bin/falkon
%_K5bin/qupzilla
%_K5plug/falkon/
%exclude %_K5plug/falkon/KDEFrameworksIntegration.so
%exclude %_K5plug/falkon/GnomeKeyringPasswords.so
%_K5xdgapp/org.kde.falkon.desktop
%_pixmapsdir/falkon.png
%_K5icon/hicolor/*/*/*.png
%_K5icon/hicolor/*/*/*.svg
#%_datadir/locale/*/*/*.qm
%_datadir/falkon/
%_datadir/bash-completion/completions/falkon

%files kde5
%_K5plug/falkon/KDEFrameworksIntegration.so

%files gnome3
%_K5plug/falkon/GnomeKeyringPasswords.so

%files -n %libfalkonprivate
%_K5lib/libFalkonPrivate.so.%sover
%_K5lib/libFalkonPrivate.so.%sover.*

%changelog
* Fri Aug 28 2020 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt3
- fix to build with qt-5.15

* Thu Sep 19 2019 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt2
- obsolete rekonq

* Thu Mar 28 2019 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1
- new version
- obsolete qupzilla

* Fri Aug 31 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt2
- rebuild with new openssl (ALT# 35313)

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt1
- new version

* Mon Apr 09 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt3
- fix URL

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt2
- NMU: added URL (closes: #34686)

* Tue Mar 20 2018 Oleg Solovyov <mcpain@altlinux.org> 3.0.0-alt1
- initial build for ALT
