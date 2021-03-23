%global optflags %optflags -I%_includedir/KF5 -L%_libdir/kf5/devel

Name:		ksnip
Version:	1.8.0
Release:	alt1

Summary:	Window Snipping Tool

License:	GPLv2+
Group:		Graphics
Url:		https://github.com/ksnip/ksnip

# Source-git: https://github.com/ksnip/ksnip.git
Source:	%name-%version.tar

Patch1: %name-%version.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: libX11-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: zlib-devel
BuildRequires: bzlib-devel
BuildRequires: kde5-kimageannotator-devel
BuildRequires: kde5-kcolorpicker-devel
BuildRequires: qt5-tools-devel
BuildRequires: libpng-devel
BuildRequires: libpcre-devel
BuildRequires: libuuid-devel
BuildRequires: libexpat-devel

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       icon-theme-hicolor

%description
Screenshot tool inspired by Windows Snipping Tool and made with Qt5 for Linux.

%prep
%setup -q -n %name-%version
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
%find_lang %name --with-qt

%check
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/*.appdata.xml
desktop-file-validate %buildroot%_datadir/applications/*.desktop

%files -f ksnip.lang
%doc README.md CHANGELOG.md
%_bindir/ksnip
%dir %_datadir/ksnip
%dir %_datadir/ksnip/translations
%_datadir/applications/org.ksnip.ksnip.desktop
%_datadir/icons/hicolor/*/apps/ksnip.svg
%_datadir/metainfo/org.ksnip.ksnip.appdata.xml

%changelog
* Fri Mar 12 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.8.0-alt1
- Initial build in Sisyphus
