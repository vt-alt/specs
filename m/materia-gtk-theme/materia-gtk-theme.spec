Name:     materia-gtk-theme
Version:  20200916
Release:  alt1

Summary:  A Material Design theme for GNOME/GTK based desktop environments
License:  GPL-2.0
Group:    Other
Url:      https://github.com/nana-4/materia-theme

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   materia-theme-%version.tar

BuildArch: noarch

BuildRequires: sassc
Requires: libgtk-engine-murrine

%description
Materia is a Material Design theme for GNOME/GTK based desktop environments.

%prep
%setup -n materia-theme-%version

%install
install -d %buildroot%_datadir/themes
./install.sh -d "%buildroot%_datadir/themes"

%files
%doc *.md
%_datadir/themes/Materia*

%changelog
* Thu Sep 17 2020 Andrey Cherepanov <cas@altlinux.org> 20200916-alt1
- New version.
- Fix License tag according to SPDX.

* Sat Apr 04 2020 Andrey Cherepanov <cas@altlinux.org> 20200320-alt1
- New version.

* Wed Jun 05 2019 Andrey Cherepanov <cas@altlinux.org> 20190315-alt1
- Initial build for Sisyphus.
