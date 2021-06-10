Name:     wineexec
Version:  1.2
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
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop

%changelog
* Fri Jun 04 2021 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Use correct case of value in desktop file.

* Mon May 24 2021 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Hide menu item from application menu.
- Fix localization.

* Wed Dec 30 2020 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
