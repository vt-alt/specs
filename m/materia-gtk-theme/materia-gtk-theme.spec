Name:     materia-gtk-theme
Version:  20190315
Release:  alt1

Summary:  A Material Design theme for GNOME/GTK based desktop environments
License:  GPLv2
Group:    Other
Url:      https://github.com/nana-4/materia-theme

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   materia-theme-%version.tar

BuildArch: noarch

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
* Wed Jun 05 2019 Andrey Cherepanov <cas@altlinux.org> 20190315-alt1
- Initial build for Sisyphus.
