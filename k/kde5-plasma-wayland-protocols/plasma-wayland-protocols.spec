%define rname plasma-wayland-protocols

Name: kde5-%rname
Version: 1.1
Release: alt1
%K5init altplace no_appdata

Group: Development/KDE and QT
Summary: XML files of non-standard wayland protocols used in Plasma
License: LGPL-2.0-or-later
Url: https://invent.kde.org/libraries/plasma-wayland-protocols

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel

%description
XML files of non-standard wayland protocols used in Plasma.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

%files
%_libdir/cmake/PlasmaWaylandProtocols/
%_datadir/plasma-wayland-protocols/

%changelog
* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- initial build
