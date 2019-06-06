Name:     brisk-menu
Version:  0.5.0
Release:  alt2.gitc809be3

Summary:  An efficient menu for the MATE Desktop
License:  GPLv2
Group:    Other
Url:      https://github.com/getsolus/brisk-menu

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch:    %name-upstream-fixes.patch

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: libgtk+3-devel
BuildRequires: mate-panel-devel
BuildRequires: mate-menus-devel
BuildRequires: libnotify-devel

Requires: mate-menu-editor

%description
brisk-menu is a modern and efficient menu designed to improve the MATE
Desktop Environment with modern, first-class options. The purpose of
this project is to provide a usable menu as seen in other desktops
without the bloat and performance issues.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name
echo "%_datadir/locale/es_419/LC_MESSAGES/brisk-menu.mo" >> %name.lang

%files -f %name.lang
%doc AUTHORS README.md
%_libexecdir/%name
%_datadir/dbus-1/services/org.mate.panel.applet.BriskMenuFactory.service
%_datadir/glib-2.0/schemas/com.solus-project.brisk-menu.gschema.xml
%_datadir/mate-panel/applets/com.solus_project.brisk.BriskMenu.mate-panel-applet
%_iconsdir/hicolor/scalable/actions/brisk_system-log-out-symbolic.svg

%changelog
* Wed Jun 05 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt2.gitc809be3
- Add mate-menu-editor to requirements.

* Thu May 30 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1.gitc809be3
- Initial build for Sisyphus.
