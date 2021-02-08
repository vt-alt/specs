Name:     vokoscreenNG
Version:  3.0.8
Release:  alt1

Summary:  VokscreenNG is a user friendly Open Source screencaster for Linux and Windows
License:  GPL-2.0
Group:    Other
Url:      https://github.com/vkohaupt/vokoscreenNG

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libgstreamermm1.0-devel
BuildRequires: libpulseaudio-devel

%description
%summary

%prep
%setup

%build
cd src
%qmake_qt5 CONFIG+=silent
%make_build

%install
%makeinstall_std -C src
install -Dpm0755 src/%name %buildroot%_bindir/%name
install -Dpm0644 src/applications/%name.desktop %buildroot%_desktopdir/%name.desktop
install -Dpm0644 src/applications/%name.png %buildroot%_pixmapsdir/%name.png

%files
%doc *.md
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Mon Feb 01 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.8-alt1
- New version.

* Thu Oct 01 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.7-alt1
- New version.

* Thu Sep 03 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.6-alt1
- New version.

* Mon Aug 24 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.5-alt1
- Initial build for Sisyphus.
