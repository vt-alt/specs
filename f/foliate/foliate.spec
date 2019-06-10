%define ver_major 1.2
%define rdn_name com.github.johnfactotum.Foliate

Name: foliate
Version: %ver_major.1
Release: alt1

Summary: A simple and modern GTK eBook(EPUB) reader
License: GPLv3+
Group: Office
Url: https://github.com/johnfactotum/foliate

Source: %url/archive/%version/%name-%version.tar.gz

Requires: %_bindir/gjs dconf

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(Pango)
Requires: typelib(Soup)
Requires: typelib(WebKit2)

BuildRequires(pre): meson rpm-build-gir
BuildRequires: desktop-file-utils libappstream-glib-devel
BuildRequires: libgjs-devel

%description
Foliate is a simple and modern GTK eBook reader with following features:
- View EPUB files
- Two-page view and scrolled view
- Customize font and line-spacing
- Light, sepia, dark, and invert mode
- Reading progress slider with chapter marks
- Bookmarks and annotations
- Find in book
- Quick dictionary lookup

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang --with-gnome --output=%name.lang %name %rdn_name

%files -f %name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%rdn_name/
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%rdn_name.svg
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.appdata.xml
%doc README*


%changelog
* Fri Jun 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Thu Jun 06 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Jun 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Mon Jun 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sun Jun 02 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus



