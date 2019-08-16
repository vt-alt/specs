%define rdn_name io.elementary.screenshot-tool

Name: screenshot-tool
Version: 1.6.2
Release: alt1

Summary: Screenshot tool designed for elementary OS
Group: Graphical desktop/GNOME
License: LGPL-3.0
Url: https://github.com/elementary/screenshot-tool

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

Provides: %rdn_name = %version-%release

Requires: icon-theme-hicolor

BuildRequires(pre): meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires: vala >= 0.24
BuildRequires: vala-tools
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: vapi(granite)
BuildRequires: vapi(libcanberra)
BuildRequires: desktop-file-utils


%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%files -f %rdn_name.lang
%doc COPYING README.md
%_bindir/%rdn_name
%_datadir/metainfo/%rdn_name.appdata.xml
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/accessories-screenshot.svg

%changelog
* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 1.6.2-alt1
- new version 1.6.2

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Fri Nov 09 2018 Anton Midyukov <antohami@altlinux.org> 1.6.0-alt1
- new version 1.6.0

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1.S1
- 0.1.5

* Sat Feb 17 2018 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt1%ubt
- Initial build for Sisyphus
