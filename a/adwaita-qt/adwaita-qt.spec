Name: adwaita-qt
Version: 1.0.90
Release: alt1
Summary: Adwaita theme for Qt-based applications
License: LGPLv2+
Group: Graphical desktop/GNOME
Url: https://github.com/MartinBriza/adwaita-qt
Source0: adwaita-qt-%version.tar

Patch: adwaita-qt-fix-build-with-qt4.patch
Patch1: adwaita-qt-fix-qt4-style-option.patch

BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: qt5-base-devel

Requires: adwaita-qt4
Requires: adwaita-qt5

%description
Theme to let Qt applications fit nicely into Fedora Workstation

%package common
Summary: Adwaita Qt theme shared files
Group: Graphical desktop/GNOME
BuildArch: noarch
#Requires: icon-theme-oxygen
#Requires: gnome-themes-standard-data

%description common
Common files (assets, etc.) for the Adwaita Qt theme

%package -n adwaita-qt4
Summary: Adwaita Qt4 theme
Group: Graphical desktop/GNOME
Requires: qt4
#Requires: adwaita-qt-common

%description -n adwaita-qt4
Adwaita theme variant for applications utilizing Qt4

%package -n adwaita-qt5
Summary: Adwaita Qt5 theme
Group: Graphical desktop/GNOME
Requires: qt5-qtbase
#Requires: adwaita-qt-common

%description -n adwaita-qt5
Adwaita theme variant for applications utilizing Qt5

%prep
%setup
%patch -p1
%patch1 -p1

%build
mkdir -p "%_target_platform-qt4"
pushd "%_target_platform-qt4"
%cmake -DUSE_QT4=true ../..
%make_build -C BUILD
popd

mkdir -p "%_target_platform-qt5"
pushd "%_target_platform-qt5"
%cmake ../..
%make_build -C BUILD
popd

%install
pushd "%_target_platform-qt4"
%makeinstall_std -C BUILD
popd
pushd "%_target_platform-qt5"
%makeinstall_std -C BUILD
popd

#files common

%files -n adwaita-qt4
%doc LICENSE.LGPL2 README.md
%_libdir/qt4/plugins/styles/adwaita.so

%files -n adwaita-qt5
%doc LICENSE.LGPL2 README.md
%_qt5_archdatadir/plugins/styles/adwaita.so

%files

%changelog
* Wed Jul 10 2019 Anton Midyukov <antohami@altlinux.org> 1.0.90-alt1
- new version 1.0.90

* Wed May 31 2017 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- new version 1.0

* Wed Apr 12 2017 Anton Midyukov <antohami@altlinux.org> 0.99-alt1
- new version 0.99

* Wed Mar 01 2017 Anton Midyukov <antohami@altlinux.org> 0.98-alt1
- new version 0.98

* Sun Sep 04 2016 Anton Midyukov <antohami@altlinux.org> 0.5-alt1
- new version 0.5
- remove qt-creator-menubar-fix.patch

* Tue Aug 30 2016 Anton Midyukov <antohami@altlinux.org> 0.4-alt1
- Initial build for Alt Linux Sisyphus (Thanks Fedora Team).
