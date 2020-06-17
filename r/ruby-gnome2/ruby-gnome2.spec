Name: 	       ruby-gnome2
Version:       3.4.1
Release:       alt1.3
Summary:       Ruby bindings for GNOME
License:       MIT
Group:         Development/Ruby
Url:           https://ruby-gnome2.osdn.jp/
Vcs:           https://github.com/ruby-gnome2/ruby-gnome2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libgtk+2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libpixman-devel
BuildRequires: libexpat-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libdrm-devel
BuildRequires: libpcre-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXdamage-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libvte3-devel
BuildRequires: libvte-devel
BuildRequires: libvlc-devel
BuildRequires: libuuid-devel
BuildRequires: libgtksourceview-devel
BuildRequires: libfribidi-devel
BuildRequires: libtiff-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libat-spi2-core-devel
BuildRequires: libepoxy-devel
BuildRequires: libXinerama-devel
BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXcomposite-devel
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: wayland-protocols
BuildRequires: libxkbcommon-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gobject-introspection-devel
BuildRequires: at-spi2-atk-devel
BuildRequires: libselinux-devel
BuildRequires: libXtst-devel
BuildRequires: libthai-devel
BuildRequires: libdatrie-devel
BuildRequires: bzlib-devel
BuildRequires: glib2-devel
BuildRequires: libgio-devel
BuildRequires: libpango-devel
BuildRequires: gst-plugins-devel
BuildRequires: gcc-c++
BuildRequires: gem-cairo-devel
BuildRequires: libbrotli-devel

BuildRequires: gem(pkg-config)
BuildRequires: gem(native-package-installer)
#BuildRequires: gem(mechanize)
BuildRequires: gem-cairo
BuildRequires: gem-rake

Requires:      gem(atk)
Requires:      gem(cairo-gobject)
Requires:      gem(clutter)
Requires:      gem(clutter-gdk)
Requires:      gem(clutter-gstreamer)
Requires:      gem(clutter-gtk)
Requires:      gem(gdk3)
Requires:      gem(gdk4)
Requires:      gem(gdk_pixbuf2)
Requires:      gem(gegl)
Requires:      gem(gio2)
Requires:      gem(glib2)
Requires:      gem(gnumeric)
Requires:      gem(gobject-introspection)
Requires:      gem(goffice)
Requires:      gem(gsf)
Requires:      gem(gstreamer)
Requires:      gem(gtk2)
Requires:      gem(gtk3)
Requires:      gem(gtk4)
Requires:      gem(gtksourceview2)
Requires:      gem(gtksourceview3)
Requires:      gem(gtksourceview4)
Requires:      gem(gvlc)
Requires:      gem(pango)
Requires:      gem(poppler)
Requires:      gem(rsvg2)
Requires:      gem(vte)
Requires:      gem(vte3)
Requires:      gem(webkit-gtk)
Requires:      gem(webkit-gtk2)
Requires:      gem(webkit2-gtk)

%description
This is a set of bindings for the GNOME 2.x and 3.x libraries to use
from Ruby 2.1, 2.2, 2.3 and 2.4.


%package       -n gem-atk
Summary:       Ruby/ATK is a Ruby binding of ATK-1.12.x or later based on GObject-Introspection
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-atk
%summary.


%package       -n gem-atk-devel
Summary:       Headers for gem-atk
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-atk-devel
%summary.


%package       -n gem-atk-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-atk-doc
Documentation files for %{name}.


%package       -n gem-cairo-gobject
Summary:       Ruby/CairoGObject is a Ruby binding of cairo-gobject.
Group:         Development/Ruby

%description   -n gem-cairo-gobject
%summary.


%package       -n gem-cairo-gobject-devel
Summary:       Headers for gem-cairo-gobject
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-cairo-gobject-devel
%summary.


%package       -n gem-cairo-gobject-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-cairo-gobject-doc
Documentation files for %{name}.


%package       -n gem-clutter
Summary:       Ruby/Clutter is a Ruby binding of Clutter.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-clutter
%summary.


%package       -n gem-clutter-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-clutter-doc
Documentation files for %{name}.


%package       -n gem-clutter-gdk
Summary:       Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-clutter-gdk
%summary.


%package       -n gem-clutter-gdk-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-clutter-gdk-doc
Documentation files for %{name}.


%package       -n gem-clutter-gstreamer
Summary:       Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-clutter-gstreamer
%summary.


%package       -n gem-clutter-gstreamer-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-clutter-gstreamer-doc
Documentation files for %{name}.


%package       -n gem-clutter-gtk
Summary:       Ruby/ClutterGTK is a Ruby binding of Clutter-GTK.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-clutter-gtk
%summary.


%package       -n gem-clutter-gtk-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-clutter-gtk-doc
Documentation files for %{name}.


%package       -n gem-gdk3
Summary:       Ruby/GDK3 is a Ruby binding of GDK 3
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gdk3
%summary.


%package       -n gem-gdk3-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gdk3-doc
Documentation files for %{name}.


%package       -n gem-gdk4
Summary:       Ruby/GDK4 is a Ruby binding of GDK 4.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gdk4
%summary. https://developer.gnome.org/gdk4/3.90/


%package       -n gem-gdk4-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gdk4-doc
Documentation files for %{name}.


%package       -n gem-gdk-pixbuf2
Summary:       Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gdk-pixbuf2
%summary.


%package       -n gem-gdk-pixbuf2-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gdk-pixbuf2-doc
Documentation files for %{name}.


%package       -n gem-gegl
Summary:       Ruby/GEGL is a Ruby binding of GEGL
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gegl
%summary.


%package       -n gem-gegl-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gegl-doc
Documentation files for %{name}.


%package       -n gem-gio2
Summary:       Ruby/GIO2 is a Ruby binding of gio-2.0.x
Group:         Development/Ruby

%description   -n gem-gio2
%summary.


%package       -n gem-gio2-devel
Summary:       Headers for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gio2-devel
%summary.


%package       -n gem-gio2-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gio2-doc
Documentation files for %{name}.


%package       -n gem-glib2
Summary:       GLib 2 bindings for the Ruby language
Group:         Development/Ruby

Provides:      ruby-glib2
Obsoletes:     ruby-glib2

%description   -n gem-glib2
GLib is a useful general-purpose C library, notably used by GTK+ and
GNOME. This package contains libraries for using GLib 2 with the Ruby
programming language. It is most likely useful in conjunction with Ruby
bindings for other libraries such as GTK+.


%package       -n gem-glib2-devel
Summary:       Development files for GLib 2 bindings for the Ruby language
Group:         Development/Ruby
BuildArch:     noarch

Provides:      ruby-gnome2-devel
Obsoletes:     ruby-gnome2-devel

%description   -n gem-glib2-devel
This packages contains header files for gem-glib2 gem package.


%package       -n gem-glib2-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

Provides:      ruby-glib2-doc
Obsoletes:     ruby-glib2-doc

%description   -n gem-glib2-doc
Documentation files for %{name}.


%package       -n gem-gnumeric
Summary:       Ruby/Gnumeric is a Ruby binding of Gnumeric
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gnumeric
%summary.


%package       -n gem-gnumeric-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gnumeric-doc
Documentation files for %{name}.


%package       -n gem-gobject-introspection
Summary:       Ruby/GObjectIntrospection is a Ruby binding of GObject Introspect
Group:         Development/Ruby

%description   -n gem-gobject-introspection
%summary.


%package       -n gem-gobject-introspection-devel
Summary:       Headers for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gobject-introspection-devel
%summary.


%package       -n gem-gobject-introspection-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gobject-introspection-doc
Documentation files for %{name}.


%package       -n gem-goffice
Summary:       Ruby/GOffice is a Ruby binding of GOffice
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-goffice
%summary.


%package       -n gem-goffice-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-goffice-doc
Documentation files for %{name}.


%package       -n gem-gsf
Summary:       Ruby/GSF is a Ruby binding of GSF which is needed by GOffice
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gsf
%summary.


%package       -n gem-gsf-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gsf-doc
Documentation files for %{name}.


%package       -n gem-gstreamer
Summary:       Ruby/GStreamer is a Ruby binding for GStreamer
Group:         Development/Ruby

%description   -n gem-gstreamer
%summary.


%package       -n gem-gstreamer-devel
Summary:       Headers for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gstreamer-devel
%summary.


%package       -n gem-gstreamer-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gstreamer-doc
Documentation files for %{name}.


%package       -n gem-gtk2
Summary:       Ruby/GTK2 is a Ruby binding of GTK+-2.10.x
Group:         Development/Ruby

%description   -n gem-gtk2
%summary.

%package       -n gem-gtk2-devel
Summary:       Headers for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gtk2-devel
%summary.


%package       -n gem-gtk2-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gtk2-doc
Documentation files for %{name}.


%package       -n gem-gtk3
Summary:       Ruby/GTK3 is a Ruby binding of GTK+ 3
Group:         Development/Ruby

%description   -n gem-gtk3
%summary.


%package       -n gem-gtk3-devel
Summary:       Headers for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gtk3-devel
%summary.


%package       -n gem-gtk3-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gtk3-doc
Documentation files for %{name}.


%package       -n gem-gtk4
Summary:       Ruby/GTK4 is a Ruby binding of GTK+ 4
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gtk4
%summary.


%package       -n gem-gtk4-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gtk4-doc
Documentation files for %{name}.


%package       -n gem-gtksourceview2
Summary:       Ruby/GtkSourceView2 is a Ruby binding of gtksourceview-2.x
Group:         Development/Ruby

%description   -n gem-gtksourceview2
%summary.


%package       -n gem-gtksourceview2-devel
Summary:       Headers for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gtksourceview2-devel
%summary.


%package       -n gem-gtksourceview2-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gtksourceview2-doc
Documentation files for %{name}.


%package       -n gem-gtksourceview3
Summary:       Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gtksourceview3
%summary.


%package       -n gem-gtksourceview3-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gtksourceview3-doc
Documentation files for %{name}.


%package       -n gem-gtksourceview4
Summary:       Ruby/GtkSourceView4 is a Ruby binding of gtksourceview-4.x
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gtksourceview4
%summary.


%package       -n gem-gtksourceview4-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gtksourceview4-doc
Documentation files for %{name}.


%package       -n gem-gvlc
Summary:       Ruby/VLC is a Ruby binding of libVLC for Ruby/GTK
Group:         Development/Ruby

%description   -n gem-gvlc
%summary.


%package       -n gem-gvlc-devel
Summary:       Headers for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-gvlc-devel
%summary.


%package       -n gem-gvlc-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-gvlc-doc
Documentation files for %{name}.


%package       -n gem-pango
Summary:       Ruby/Pango is a Ruby binding of pango based on GObject-Introspection
Group:         Development/Ruby

%description   -n gem-pango
%summary.


%package       -n gem-pango-devel
Summary:       Headers for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-pango-devel
%summary.


%package       -n gem-pango-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-pango-doc
Documentation files for %{name}.


%package       -n gem-poppler
Summary:       Ruby/Poppler is a Ruby binding of poppler-glib
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-poppler
%summary.


%package       -n gem-poppler-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-poppler-doc
Documentation files for %{name}.


%package       -n gem-rsvg2
Summary:       Ruby/RSVG2 is a Ruby binding of librsvg based on GObject-Introspection
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-rsvg2
%summary.


%package       -n gem-rsvg2-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-rsvg2-doc
Documentation files for %{name}.


%package       -n gem-vte
Summary:       Ruby/VTE is a Ruby binding of VTE
Group:         Development/Ruby

%description   -n gem-vte
%summary.


%package       -n gem-vte-devel
Summary:       Headers for %name
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-vte-devel
%summary.


%package       -n gem-vte-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-vte-doc
Documentation files for %{name}.


%package       -n gem-vte3
Summary:       Ruby/VTE3 is a Ruby binding of VTE for use with GTK3
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-vte3
%summary.


%package       -n gem-vte3-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-vte3-doc
Documentation files for %{name}.


%package       -n gem-webkit-gtk
Summary:       Ruby/WebKitGTK is a Ruby binding of WebKitGTK+
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-webkit-gtk
%summary.


%package       -n gem-webkit-gtk-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-webkit-gtk-doc
Documentation files for %{name}.


%package       -n gem-webkit-gtk2
Summary:       Ruby/WebKitGTK2 is a Ruby binding of WebKitGTK+ for GTK+ 2
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-webkit-gtk2
%summary.


%package       -n gem-webkit-gtk2-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-webkit-gtk2-doc
Documentation files for %{name}.


%package       -n gem-webkit2-gtk
Summary:       Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-webkit2-gtk
%summary.


%package       -n gem-webkit2-gtk-doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   -n gem-webkit2-gtk-doc
Documentation files for %{name}.


%package       -n gem-wnck3
Summary:       Executable file for wnck3 gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета wnck3
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-wnck3
Executable file for wnck3 gem.

%description   -n gem-wnck3 -l ru_RU.UTF8
Исполнямка для wnck3 самоцвета.


%package       -n gem-wnck3-doc
Summary:       Documentation files for wnck3 gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета wnck3
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-wnck3-doc
Documentation files for wnck3 gem.

%description   -n gem-wnck3-doc -l ru_RU.UTF8
Файлы сведений для самоцвета wnck3.


%package       -n gem-libsecret
Summary:       Executable file for libsecret gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета libsecret
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-libsecret
Executable file for libsecret gem.

%description   -n gem-libsecret -l ru_RU.UTF8
Исполнямка для libsecret самоцвета.


%package       -n gem-libsecret-doc
Summary:       Documentation files for libsecret gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libsecret
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-libsecret-doc
Documentation files for libsecret gem.

%description   -n gem-libsecret-doc -l ru_RU.UTF8
Файлы сведений для самоцвета libsecret.


%prep
%setup

%build
%ruby_build --ignore=ruby-gnome2

%install
%ruby_install

%check
%ruby_test

%files         -n ruby-gnome2

%files         -n gem-atk
%ruby_gemspecdir/atk-%version.gemspec
%ruby_gemslibdir/atk-%version

%files         -n gem-atk-doc
%ruby_gemsdocdir/atk-%version

%files         -n gem-cairo-gobject
%ruby_gemspecdir/cairo-gobject-%version.gemspec
%ruby_gemslibdir/cairo-gobject-%version
%ruby_gemsextdir/cairo-gobject-%version

%files         -n gem-cairo-gobject-devel
%ruby_includedir/cairo-gobject

%files         -n gem-cairo-gobject-doc
%ruby_gemsdocdir/cairo-gobject-%version

%files         -n gem-clutter
%ruby_gemspecdir/clutter-%version.gemspec
%ruby_gemslibdir/clutter-%version

%files         -n gem-clutter-doc
%ruby_gemsdocdir/clutter-%version

%files         -n gem-clutter-gdk
%ruby_gemspecdir/clutter-gdk-%version.gemspec
%ruby_gemslibdir/clutter-gdk-%version

%files         -n gem-clutter-gdk-doc
%ruby_gemsdocdir/clutter-gdk-%version

%files         -n gem-clutter-gstreamer
%ruby_gemspecdir/clutter-gstreamer-%version.gemspec
%ruby_gemslibdir/clutter-gstreamer-%version

%files         -n gem-clutter-gstreamer-doc
%ruby_gemsdocdir/clutter-gstreamer-%version

%files         -n gem-clutter-gtk
%ruby_gemspecdir/clutter-gtk-%version.gemspec
%ruby_gemslibdir/clutter-gtk-%version

%files         -n gem-clutter-gtk-doc
%ruby_gemsdocdir/clutter-gtk-%version

%files         -n gem-gdk3
%ruby_gemspecdir/gdk3-%version.gemspec
%ruby_gemslibdir/gdk3-%version

%files         -n gem-gdk3-doc
%ruby_gemsdocdir/gdk3-%version

%files         -n gem-gdk4
%ruby_gemspecdir/gdk4-%version.gemspec
%ruby_gemslibdir/gdk4-%version

%files         -n gem-gdk4-doc
%ruby_gemsdocdir/gdk4-%version

%files         -n gem-gdk-pixbuf2
%ruby_gemspecdir/gdk_pixbuf2-%version.gemspec
%ruby_gemslibdir/gdk_pixbuf2-%version

%files         -n gem-gdk-pixbuf2-doc
%ruby_gemsdocdir/gdk_pixbuf2-%version

%files         -n gem-gegl
%ruby_gemspecdir/gegl-%version.gemspec
%ruby_gemslibdir/gegl-%version

%files         -n gem-gegl-doc
%ruby_gemsdocdir/gegl-%version

%files         -n gem-gio2
%ruby_gemspecdir/gio2-%version.gemspec
%ruby_gemslibdir/gio2-%version
%ruby_gemsextdir/gio2-%version

%files         -n gem-gio2-devel
%ruby_includedir/gio2

%files         -n gem-gio2-doc
%ruby_gemsdocdir/gio2-%version

%files         -n gem-glib2
%ruby_gemspecdir/glib2-%version.gemspec
%ruby_gemslibdir/glib2-%version
%ruby_gemsextdir/glib2-%version

%files         -n gem-glib2-devel
%ruby_includedir/glib2

%files         -n gem-glib2-doc
%ruby_gemsdocdir/glib2-%version

%files         -n gem-gnumeric
%ruby_gemspecdir/gnumeric-%version.gemspec
%ruby_gemslibdir/gnumeric-%version

%files         -n gem-gnumeric-doc
%ruby_gemsdocdir/gnumeric-%version

%files         -n gem-gobject-introspection
%ruby_gemspecdir/gobject-introspection-%version.gemspec
%ruby_gemslibdir/gobject-introspection-%version
%ruby_gemsextdir/gobject-introspection-%version

%files         -n gem-gobject-introspection-devel
%ruby_includedir/gobject-introspection

%files         -n gem-gobject-introspection-doc
%ruby_gemsdocdir/gobject-introspection-%version

%files         -n gem-goffice
%ruby_gemspecdir/goffice-%version.gemspec
%ruby_gemslibdir/goffice-%version

%files         -n gem-goffice-doc
%ruby_gemsdocdir/goffice-%version

%files         -n gem-gsf
%ruby_gemspecdir/gsf-%version.gemspec
%ruby_gemslibdir/gsf-%version

%files         -n gem-gsf-doc
%ruby_gemsdocdir/gsf-%version

%files         -n gem-gstreamer
%ruby_gemspecdir/gstreamer-%version.gemspec
%ruby_gemslibdir/gstreamer-%version
%ruby_gemsextdir/gstreamer-%version

%files         -n gem-gstreamer-devel
%ruby_includedir/gstreamer

%files         -n gem-gstreamer-doc
%ruby_gemsdocdir/gstreamer-%version

%files         -n gem-gtk2
%ruby_gemspecdir/gtk2-%version.gemspec
%ruby_gemslibdir/gtk2-%version
%ruby_gemsextdir/gtk2-%version

%files         -n gem-gtk2-devel
%ruby_includedir/gtk2

%files         -n gem-gtk2-doc
%ruby_gemsdocdir/gtk2-%version

%files         -n gem-gtk3
%ruby_gemspecdir/gtk3-%version.gemspec
%ruby_gemslibdir/gtk3-%version
%ruby_gemsextdir/gtk3-%version

%files         -n gem-gtk3-devel
%ruby_includedir/gtk3

%files         -n gem-gtk3-doc
%ruby_gemsdocdir/gtk3-%version

%files         -n gem-gtk4
%ruby_gemspecdir/gtk4-%version.gemspec
%ruby_gemslibdir/gtk4-%version

%files         -n gem-gtk4-doc
%ruby_gemsdocdir/gtk4-%version

%files         -n gem-gtksourceview2
%ruby_gemspecdir/gtksourceview2-%version.gemspec
%ruby_gemslibdir/gtksourceview2-%version
%ruby_gemsextdir/gtksourceview2-%version

%files         -n gem-gtksourceview2-devel
%ruby_includedir/gtksourceview2

%files         -n gem-gtksourceview2-doc
%ruby_gemsdocdir/gtksourceview2-%version

%files         -n gem-gtksourceview3
%ruby_gemspecdir/gtksourceview3-%version.gemspec
%ruby_gemslibdir/gtksourceview3-%version

%files         -n gem-gtksourceview3-doc
%ruby_gemsdocdir/gtksourceview3-%version

%files         -n gem-gtksourceview4
%ruby_gemspecdir/gtksourceview4-%version.gemspec
%ruby_gemslibdir/gtksourceview4-%version

%files         -n gem-gtksourceview4-doc
%ruby_gemsdocdir/gtksourceview4-%version

%files         -n gem-gvlc
%ruby_gemspecdir/gvlc-%version.gemspec
%ruby_gemslibdir/gvlc-%version
%ruby_gemsextdir/gvlc-%version

%files         -n gem-gvlc-devel
%ruby_includedir/gvlc

%files         -n gem-gvlc-doc
%ruby_gemsdocdir/gvlc-%version

%files         -n gem-pango
%ruby_gemspecdir/pango-%version.gemspec
%ruby_gemslibdir/pango-%version
%ruby_gemsextdir/pango-%version

%files         -n gem-pango-devel
%ruby_includedir/pango

%files         -n gem-pango-doc
%ruby_gemsdocdir/pango-%version

%files         -n gem-poppler
%ruby_gemspecdir/poppler-%version.gemspec
%ruby_gemslibdir/poppler-%version

%files         -n gem-poppler-doc
%ruby_gemsdocdir/poppler-%version

%files         -n gem-rsvg2
%ruby_gemspecdir/rsvg2-%version.gemspec
%ruby_gemslibdir/rsvg2-%version

%files         -n gem-rsvg2-doc
%ruby_gemsdocdir/rsvg2-%version

%files         -n gem-vte
%ruby_gemspecdir/vte-%version.gemspec
%ruby_gemslibdir/vte-%version
%ruby_gemsextdir/vte-%version

%files         -n gem-vte-devel
%ruby_includedir/vte

%files         -n gem-vte-doc
%ruby_gemsdocdir/vte-%version

%files         -n gem-vte3
%ruby_gemspecdir/vte3-%version.gemspec
%ruby_gemslibdir/vte3-%version

%files         -n gem-vte3-doc
%ruby_gemsdocdir/vte3-%version

%files         -n gem-webkit-gtk
%ruby_gemspecdir/webkit-gtk-%version.gemspec
%ruby_gemslibdir/webkit-gtk-%version

%files         -n gem-webkit-gtk-doc
%ruby_gemsdocdir/webkit-gtk-%version

%files         -n gem-webkit-gtk2
%ruby_gemspecdir/webkit-gtk2-%version.gemspec
%ruby_gemslibdir/webkit-gtk2-%version

%files         -n gem-webkit-gtk2-doc
%ruby_gemsdocdir/webkit-gtk2-%version

%files         -n gem-webkit2-gtk
%ruby_gemspecdir/webkit2-gtk-%version.gemspec
%ruby_gemslibdir/webkit2-gtk-%version

%files         -n gem-webkit2-gtk-doc
%ruby_gemsdocdir/webkit2-gtk-%version

%files         -n gem-wnck3
%ruby_gemspecdir/wnck3-%version.gemspec
%ruby_gemslibdir/wnck3-%version

%files         -n gem-wnck3-doc
%ruby_gemsdocdir/wnck3-%version

%files         -n gem-libsecret
%ruby_gemspecdir/libsecret-%version.gemspec
%ruby_gemslibdir/libsecret-%version

%files         -n gem-libsecret-doc
%ruby_gemsdocdir/libsecret-%version


%changelog
* Mon May 25 2020 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1.3
- Fix build by adding libbrotli-devel.

* Sat May 09 2020 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1.2
- Do not require deprecated libwlc0-devel for wayland-protocols.pc.

* Thu Apr 02 2020 Pavel Skrylev <majioa@altlinux.org> 3.4.1-alt1.1
- ! build required package names

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.4.1-alt1
- updated (^) 3.3.8 -> 3.4.1

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.8-alt1
- updated (^) 3.3.7 -> 3.3.8
- fixed (!) spec according to changelog rules

* Tue Aug 20 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.7-alt1
- updated (^) 3.3.6 -> 3.3.7
- added (+) libthai-devel, and libdatrie-devel build reqs
- added (+) wnck3, and libsecret gems

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.6-alt2
- ignore ruby-gnome2 gemfile

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.6-alt1
- Bump to 3.3.6

* Tue Mar 19 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.2-alt2
- Fix build for new gnome

* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.2-alt1
- Bump to 3.3.2 gem;
- Use Ruby Policy 2.0;
- All the subpackages now included.

* Sun Jan 20 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.1-alt1
- Bump to 3.3.1 gem.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt2
- Fix build (add libpcre-devel).

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.7-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 07 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.7-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.6-alt1
- New version.

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.5-alt1
- New version.

* Mon Apr 09 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt1
- New version.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt2
- Build with libvte3.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- New version.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- New version.

* Sat Mar 31 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version.
- Build with gstreamer1.0-devel.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- Initial build in Sisyphus
