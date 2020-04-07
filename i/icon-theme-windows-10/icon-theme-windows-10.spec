Name: icon-theme-windows-10
Version: 1.0
Release: alt1
Summary: Windows 10 Icon theme

License: GPL-3.0
Group: Graphical desktop/GNOME
URL: https://github.com/B00merang-Artwork/Windows-10

Source: %name-%version.tar

BuildArch: noarch

%description
Icon theme based on material from Windows 10.

%prep
%setup

%install
mkdir -p "%buildroot%_iconsdir/Windows 10"
cp -a * "%buildroot%_iconsdir/Windows 10"

%files
%doc "%_iconsdir/Windows 10/README.md"
"%_iconsdir/Windows 10"

%changelog
* Wed Apr 01 2020 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus.
