%def_disable snapshot

%define ver_major 1.5
%define rdn_name com.github.johnfactotum.Foliate

Name: foliate
Version: %ver_major.3
Release: alt1

Summary: A simple and modern GTK eBook reader
License: GPLv3+
Group: Office
Url: https://github.com/johnfactotum/foliate

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
# VCS: https://github.com/johnfactotum/foliate.git
Source: %name-%version.tar
%endif
Patch: %name-1.5.0-alt-python3_syntax.patch

%define gjs_ver 1.52

Requires: libgjs >= %gjs_ver dconf
#Recommends: espeak, espeak-ng or festival

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(Pango)
Requires: typelib(WebKit2)

%add_python3_path %_datadir/%rdn_name

BuildRequires(pre): meson rpm-build-gir rpm-build-python3
BuildRequires: desktop-file-utils libappstream-glib-devel
BuildRequires: libgjs-devel

%description
Foliate is a simple and modern GTK eBook reader with following features:
- View EPUB and Kindle files
- Two-page view and scrolled view
- Customize font and line-spacing
- Light, sepia, dark, and invert mode
- Reading progress slider with chapter marks
- Bookmarks and annotations
- Find in book
- Quick dictionary lookup

%prep
%setup
%patch -b .py3

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
* Thu Jul 25 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Fri Jul 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Thu Jul 18 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Mon Jul 15 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Mon Jul 08 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sun Jun 30 2019 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Tue Jun 18 2019 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- updated to 1.3.0-3-g3e30e73

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



