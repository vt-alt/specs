Name: gtk-theme-windows-10
Version: 3.2
Release: alt1
Summary: Windows 10 Theme for Linux

License: GPL-3.0
Group: Graphical desktop/GNOME
URL: https://github.com/B00merang-Project/Windows-10

Source: %name-%version.tar

BuildArch: noarch

Requires: libgtk-engine-murrine
Requires: libgtk+2
Requires: icon-theme-windows-10
Requires: x-cursor-themes-dmz

%description
GTK theme based on the appearance of Win32 apps on the Windows 10
platform using the default color scheme.

%prep
%setup

%install
mkdir -p "%buildroot%_datadir/themes/Windows 10"
cp -a * "%buildroot%_datadir/themes/Windows 10"
rm -f "%buildroot%_datadir/themes/Windows 10/LICENSE.md"

%files
%doc "%_datadir/themes/Windows 10/CREDITS
%doc "%_datadir/themes/Windows 10/README.md
"%_datadir/themes/Windows 10"

%changelog
* Wed Apr 01 2020 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- Initial build in Sisyphus.
