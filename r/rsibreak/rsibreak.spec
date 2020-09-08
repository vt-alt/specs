Name:           rsibreak
Version:        0.12.13
Release:        alt1
Summary:        A small utility which bothers you at certain intervals
Group:          Graphical desktop/KDE
License:        GPLv2+
URL:            https://projects.kde.org/projects/unmaintained/rsibreak
Source0:        %name-%version.tar
Packager:	Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kidletime-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-kdoctools

%description
RSIBreak is a small utility which bothers you at certain intervals. The
interval and duration of two different timers can be configured. You can
use the breaks to stretch out or do the dishes. The aim of this utility
is to let you know when it is time to have a break from your computer.
This can help people to prevent Repetive Strain Injury.

%prep
%setup -q

%build
%K5init no_altplace
%K5build

%install
%K5install
%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS TODO
%_K5bin/%name
%_K5xdgapp/*.desktop
%_K5start/%{name}_autostart.desktop
%_K5dbus_iface/org.%name.rsiwidget.xml
%_K5notif/%name.notifyrc
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/*/actions/*.png
%_datadir/metainfo/org.kde.rsibreak.appdata.xml

%changelog
* Mon Apr 06 2020 Andrey Cherepanov <cas@altlinux.org> 0.12.13-alt1
- New version.

* Sat Apr 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.12.12-alt1
- New version.

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.11-alt1
- New version.

* Fri Jun 21 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.10-alt1
- New version.

* Tue Oct 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.9-alt1
- New version.

* Mon Feb 12 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.8-alt1
- New version.

* Tue May 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.12.7-alt1
- New version

* Sat Feb 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.12.6-alt1
- new version 0.12.6

* Tue Dec 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.5-alt1
- new version 0.12.5

* Thu Oct 13 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.4-alt1
- New version 0.12.4
- Build from upstream Git repository
- Fix homepage and maintainer
- Clean up KF5 requirements

* Tue Jun 14 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.3-alt1
- New version
- Build with KF5

* Fri Jan 13 2012 Andrey Cherepanov <cas@altlinux.org> 0.11-alt1
- New version 0.11
- Rewrite on KDE4

* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1.1.qa1
- Disable aRts support
- Adapt to new KDE3 placement

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for rsibreak

* Mon Apr 07 2008 Dmitry M. Maslennikov <rlz at altlinux.ru> 0.8.0-alt1
- initial build
