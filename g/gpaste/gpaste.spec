%def_disable snapshot

%define ver_major 3.40
%define api_ver 1.0
%define _name GPaste
%define xdg_name org.gnome.GPaste
%define _libexecdir %_prefix/libexec

%def_disable applet

Name: gpaste
Version: %ver_major.2
Release: alt1

Summary: GPaste is a clipboard management system
Group: Text tools
License: BSD-2-Clause
Url: https://github.com/Keruspe/GPaste

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

Requires: lib%name = %version-%release

%define gtk_ver 3.24.0
%define gi_ver 1.58.0
%define vala_ver 0.42
%define mutter_ver 3.38.0
%define gjs_ver 1.54

BuildRequires(pre): meson rpm-build-gir
BuildRequires: libappstream-glib-devel desktop-file-utils
BuildRequires: libdbus-devel libgtk+3-devel >= %gtk_ver
BuildRequires: libgjs-devel >= %gjs_ver libmutter-devel >= %mutter_ver
BuildRequires: gnome-control-center-devel
BuildRequires: gobject-introspection-devel >= %gi_ver libgtk+3-gir-devel
BuildRequires: vala-tools >= %vala_ver libvala-devel
# since 3.20
BuildRequires: pkgconfig(systemd)

%description
This package provides gpaste-daemon is a clipboard management daemon with DBus
interface.

%package -n lib%name
Summary: GPaste library
Group: System/Libraries

%description -n lib%name
GPaste is a clipboard management system.
This package provides shared library required for GPaste components to
work.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains library and header files for developing
applications that use %name.

%package -n lib%name-gir
Summary: GObject introspection data for the GPaste
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GPaste library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GPaste
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GPaste library.

%package -n gnome-shell-extension-%name
Summary: GNOME Shell extension for GPaste
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: gnome-shell >= %ver_major
Requires: %name = %version-%release

%description -n gnome-shell-extension-%name
GNOME Shell extension for GPaste clipboard management system.

%package applet
Summary: Tray applet to manage GPaste
Group: Graphical desktop/Other
Requires: %name = %version-%release

%description applet
This package provides GPaste applet which starts the status icon
in notification area.

%prep
%setup -n %_name-%version

%build
%meson \
  -Dschemas-compile=false \
  -Dvala=true
%meson_build

%install
%meson_install
%find_lang %_name

%files -f %_name.lang
%_bindir/%name-client
%_libexecdir/%name/
%{?_enable_applet:%exclude %_libexecdir/%name/%name-applet}
%_desktopdir/%xdg_name.Ui.desktop
%_datadir/metainfo/%xdg_name.Ui.appdata.xml
%_prefix/lib/systemd/user/%xdg_name.Ui.service
%_datadir/dbus-1/services/*.service
%_prefix/lib/systemd/user/%xdg_name.service
%_datadir/glib-2.0/schemas/*.xml
%_datadir/gnome-control-center/keybindings/*.xml
%_man1dir/%name-client.1.*

%_datadir/bash-completion/completions/gpaste-client
%exclude %_datadir/zsh/site-functions/_gpaste-client
%doc AUTHORS NEWS README.md THANKS TODO COPYING

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*.pc
%_vapidir/*

%files -n lib%name-gir
%_typelibdir/%_name-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/%_name-%api_ver.gir

%if_enabled applet
%files applet
%_libexecdir/%name/%name-applet
%_datadir/metainfo/%xdg_name.Applet.appdata.xml
%_datadir/applications/%xdg_name.Applet.desktop
%_prefix/lib/systemd/user/%xdg_name.Applet.service
%_sysconfdir/xdg/autostart/%xdg_name.Applet.desktop
%endif

%files -n gnome-shell-extension-%name
%_datadir/gnome-shell/extensions/GPaste@gnome-shell-extensions.gnome.org/
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini


%changelog
* Fri Apr 30 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.2-alt1
- 3.40.2

* Sun Apr 11 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.1-alt1
- 3.40.1

* Tue Mar 09 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.6-alt1
- 3.38.6

* Wed Feb 03 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.5-alt1
- 3.38.5

* Wed Dec 23 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.4-alt1
- 3.38.4 (ported to Meson build system)

* Mon Nov 02 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Sun Oct 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Thu Oct 01 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Wed Sep 16 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Mar 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Wed Mar 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Thu Oct 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Nov 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Mon Sep 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Sat Apr 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Wed Mar 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Fri Mar 16 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt2
- fixed %%files section

* Thu Sep 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Sun Apr 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Sun Feb 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Fri Dec 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Fri Sep 23 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.91-alt1
- 3.21.91

* Sat Jul 02 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20-alt1
- 3.20

* Wed Jan 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Mon Oct 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Wed Sep 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1.1-alt1
- 3.18.1.1

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18-alt1
- 3.18

* Wed Aug 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.90-alt1
- 3.17.90

* Thu May 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2.1-alt1
- 3.16.2.1

* Wed May 06 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16-alt1
- 3.16

* Fri Jan 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14-alt2
- APPSTREAM_XML used instead of APPDATA_XML

* Sun Oct 19 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14-alt1
- 3.14

* Thu Apr 03 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt1
- first build for Sisyphus

