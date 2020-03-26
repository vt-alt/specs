Name:    mate-menu
Version: 20.04.1
Release: alt2

Summary: An Advanced Menu for the MATE Desktop
# MIT is needed for keybinding.py
License: GPL-2.0 and MIT
Group:   Other
URL:     https://github.com/ubuntu-mate/mate-menu

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-distutils-extra
BuildRequires: intltool

Requires: menu-icons-default
Requires: mate-menu-editor
Requires: altlinux-mime-defaults > 0.17

BuildArch: noarch

Source:  %name-%version.tar
Patch1: alt-applet-name-l10n.patch
Patch2: alt-menubutton-label-l10n.patch
Patch3: alt-use-themed-app-list.patch
Patch4: alt-start-button-themed-icon.patch
Patch5: alt-desktop-place-fix.patch

%description
This is MATE Menu, a fork of MintMenu. An advanced menu for MATE.
Supports filtering, favorites, autosession, and many other features.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%python3_build

%install
%python3_install
%find_lang %name --with-gnome

%files -f %name.lang
%doc *.md
%_bindir/%name
%_libexecdir/%name
%_datadir/%name
%python3_sitelibdir/mate_menu/
%python3_sitelibdir/*.egg-info
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/*.xml
%_datadir/mate-panel/applets/org.mate.panel.MateMenuApplet.mate-panel-applet
%_man1dir/%name.1*

%changelog
* Thu Mar 23 2020 Pavel Vasenkov <pav@altlinux.org> 20.04.1-alt2
- Fix open link to Desktop (ALT #37850)
- Fix edit properties (ALT #37851)

* Thu Mar 12 2020 Andrey Cherepanov <cas@altlinux.org> 20.04.1-alt1
- New version.

* Tue Oct 01 2019 Andrey Cherepanov <cas@altlinux.org> 19.10.2-alt1
- New version.

* Thu Aug 15 2019 Andrey Cherepanov <cas@altlinux.org> 19.10.1-alt1
- Initial build for Sisyphus
