Name:    mate-menu
Version: 19.10.1
Release: alt1

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
Patch2: alt-fix-cyrillic-desktop-names.patch
Patch3: alt-menubutton-label-l10n.patch
Patch4: alt-use-themed-app-list.patch

%description
This is MATE Menu, a fork of MintMenu. An advanced menu for MATE.
Supports filtering, favorites, autosession, and many other features.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%python3_build

%install
%python3_install
%find_lang %name --with-gnome
for lang in es_419 zh-Hans;do echo "%_datadir/locale/$lang/LC_MESSAGES/%name.mo" >> %name.lang;done

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
* Thu Aug 15 2019 Andrey Cherepanov <cas@altlinux.org> 19.10.1-alt1
- Initial build for Sisyphus
