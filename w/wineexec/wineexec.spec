Name:     wineexec
Version:  1.0
Release:  alt1

Summary:  Graphical wrapper for confirmed run Windows executables using WINE
License:  GPL-3.0
Group:    Other
Url:      http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%install
%makeinstall_std

%files
%_bindir/%name
%_desktopdir/%name.desktop

%changelog
* Wed Dec 30 2020 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
