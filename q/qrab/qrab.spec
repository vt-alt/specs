%def_disable Werror

Name:     qrab
Version:  0.4
Release:  alt2

Summary:  yet another QR code reader
License:  GPLv3
Group:    Games/Puzzles

Url:      https://qrab.sourceforge.io/

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

Requires: qt5-quickcontrols2
BuildRequires: cmake gcc-c++
BuildRequires: qt5-base-devel qt5-declarative-devel qt5-quickcontrols2-devel libzbar-devel

%description
It grabs code from a screen, decodes it and copies content into clipboard.
Decoded text can be formated before being copied,
so it can be easily pasted to i.e. spreadsheet application.

%prep
%setup

%build
%cmake
cd BUILD
%make_build
cd -

%install
cd BUILD
%makeinstall_std
cd -

%files
%_bindir/*
%_desktopdir/qrab.desktop
%_pixmapsdir/qrab.png

%changelog
* Thu Aug 27 2020 Grigory Ustinov <grenka@altlinux.org> 0.4-alt2
- Fixed FTBFS.

* Tue Dec 19 2017 Grigory Ustinov <grenka@altlinux.org> 0.4-alt1
- Initial build for Sisyphus.
