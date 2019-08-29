Name:     theme-mate-windows
Version:  1.6
Release:  alt1

Summary:  Mate theme for Windows-like layout
License:  GPLv3+
Group:    Other
Url:      http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

Requires: gksu
Requires: dconf
# Required GTK+ themes
Requires: mate-themes
# Main menu
Requires: mate-menu
# Required fonts
Requires: fonts-ttf-google-noto-sans
Requires: fonts-ttf-google-crosextra-caladea
Requires: fonts-ttf-google-crosextra-carlito
# Other requirements
Requires: color-prompt-and-man

%description
Mate theme for Windows-like layout: taskbar at bottom with menu button.

%prep
%setup

%install
#mate-settings
mkdir -p %buildroot%_datadir/glib-2.0/schemas
install -pm644 *.gschema.override \
        %buildroot%_datadir/glib-2.0/schemas/
install -pDm644 windows.layout \
        %buildroot%_datadir/mate-panel/layouts/windows.layout
install -Dm0644 applications.list \
        %buildroot%_datadir/mate-menu/applications.list-themed

%files
%_datadir/glib-2.0/schemas/*.gschema.override
%_datadir/mate-panel/layouts/windows.layout
%_datadir/mate-menu/applications.list-themed

%changelog
* Tue Aug 27 2019 Andrey Cherepanov <cas@altlinux.org> 1.6-alt1
- Set BlueMenta as default GTK theme.

* Mon Aug 26 2019 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- Use mate-menu as successor of mintmenu.

* Thu Jul 11 2019 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- Use standard Mate menu button instead of Brisk menu.
- Drop deprecated property custom-border-color.

* Fri Jul 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- Replace Materia-light for TraditionalOk.

* Wed Jun 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Replace MintMenu for BriskMenu.
- Replace GTK theme Clearlooks-Phenix for Materia-light.
- Remove side-by-side-tiling parameter unsupported in new version of Marco.
- Increase bottom panel size to 30px.

* Tue Mar 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.1-alt2
- Remove conflict with branding-alt-tonk-mate-settings.

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Set window manager theme to Clearlooks-Phenix.

* Sun Jun 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
