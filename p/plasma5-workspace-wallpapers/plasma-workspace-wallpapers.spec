%define rname plasma-workspace-wallpapers

Name: plasma5-workspace-wallpapers
Version: 5.18.2
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Wallpapers
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

BuildArch: noarch

Provides: kf5-plasma-workspace-wallpapers = %EVR
Obsoletes: kf5-plasma-workspace-wallpapers < %EVR

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Oct 06 2015 (-bi)
# optimized out: cmake cmake-modules libqt5-core libstdc++-devel python-base python3 python3-base
#BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

%files
%doc COPYING*
%_datadir/wallpapers/*

%changelog
* Thu Feb 27 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.2-alt1
- new version

* Tue Dec 03 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt1
- new version

* Thu Mar 28 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.3-alt1
- new version

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version
- rename package

* Thu Feb 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Fri Dec 04 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Wed Sep 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- initial build
