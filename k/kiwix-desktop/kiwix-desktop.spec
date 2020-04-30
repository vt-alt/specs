Name:     kiwix-desktop
Version:  2.0.1
Release:  alt1

Summary:  Kiwix for Windows and GNU/Linux desktops
License:  GPL-3.0+
Group:    Other
Url:      https://github.com/kiwix/kiwix-desktop

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-webkit-devel
BuildRequires: qt5-webengine-devel
BuildRequires: qt5-tools
BuildRequires: libkiwix-devel
BuildRequires: aria2

Requires: aria2

%description
%summary

%prep
%setup

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 PREFIX=%_prefix
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc README.md
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*x*/apps/%name.png
%_datadir/metainfo/*.appdata.xml
%_datadir/mime/packages/*.xml

%changelog
* Tue Apr 28 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version.

* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 2.0-alt0.rc4.1
- Initial build for Sisyphus.
