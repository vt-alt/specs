# since 3.21.90 (libmutter-clutter-1.0.so private library)
%set_verify_elf_method unresolved=relaxed

%def_disable snapshot

%define ver_major 3.32
%define api_ver 4
%define xdg_name org.gnome.mutter
%define _libexecdir %_prefix/libexec
%def_enable privatelib
%def_enable remote_desktop
%def_enable installed_tests
# https://github.com/NVIDIA/egl-wayland required
%def_disable egl_device

Name: mutter
Version: %ver_major.2
Release: alt1
Epoch: 1

Summary: Clutter based compositing GTK3 Window Manager
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://ftp.gnome.org/pub/gnome/sources/%name

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define pkglibdir %_libdir/%name-%api_ver
%define pkgdatadir %_datadir/%name-%api_ver

%add_findprov_lib_path %pkglibdir
%set_typelibdir %pkglibdir
%set_girdir %pkglibdir

# since 3.22 mutter forks Cogl and Clutter libraries into own private libraries
#%%filter_from_provides /[typelib\|gir]([Cally\|Clutter\|Cogl].*/d
#%%filter_from_requires /[typelib\|gir]([Cally\|Clutter\|Cogl].*/d

#https://lists.altlinux.org/pipermail/sisyphus-incominger/2016-October/444041.html

%define gtk_ver 3.20.0
%define gi_ver 0.9.5
%define glib_ver 2.56.0
%define pango_ver 1.2.0
%define cairo_ver 1.10.0
%define Xi_ver 1.6.0
%define wayland_ver 1.13.0
%define wayland_protocols_ver 1.7
%define upower_ver 0.99.0
%define libinput_ver 0.99.0
%define gsds_ver 3.31.0
%define gudev_ver 232
%define pipewire_ver 0.2.2

Requires: lib%name = %EVR
Requires: zenity
%{?_enable_remote_desktop:Requires: pipewire >= %pipewire_ver}

BuildRequires(pre): meson rpm-build-gir
BuildRequires: gobject-introspection-devel >= %gi_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libpango-devel >= %pango_ver
BuildRequires: libcairo-devel >= %cairo_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: libXcomposite-devel libXfixes-devel libXrender-devel
BuildRequires: libXdamage-devel libXtst-devel libXi-devel >= %Xi_ver
BuildRequires: libXcursor-devel libX11-devel libXinerama-devel libXext-devel libXrandr-devel libSM-devel libICE-devel
BuildRequires: libxcb-devel
BuildRequires: libwayland-server-devel >= %wayland_ver wayland-protocols >= %wayland_protocols_ver
BuildRequires: libgdk-pixbuf-devel libgbm-devel
BuildRequires: libstartup-notification-devel zenity libcanberra-gtk3-devel
BuildRequires: libclutter-gir-devel libpango-gir-devel libgtk+3-gir-devel gsettings-desktop-schemas-gir-devel
BuildRequires: libgnome-desktop3-devel libupower-devel >= %upower_ver
BuildRequires: libxkbcommon-x11-devel libinput-devel >= %libinput_ver libxkbfile-devel xkeyboard-config-devel
BuildRequires: libwacom-devel
BuildRequires: gnome-settings-daemon-devel
%{?_enable_remote_desktop:BuildRequires: pipewire-libs-devel >= %pipewire_ver}
# for mutter native backend
BuildRequires: libdrm-devel libsystemd-devel libgudev-devel >= %gudev_ver
BuildRequires: libGL-devel libGLES-devel xorg-xwayland

%description
mutter is a minimal X window manager aimed at nontechnical users and is
designed  to  integrate well with the GNOME desktop.  mutter lacks some
features that may be expected by traditional UNIX  or  other  technical
users;  these users may want to investigate other available window man-
agers for use with GNOME or standalone.

%package -n lib%name
Summary: Shared library for Mutter
Group: System/Libraries

%description -n lib%name
This package contains shared library needed to run Mutter.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains headers and development libraries for lib%name

%package -n lib%name-gir
Summary: GObject introspection data for the Mutter library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the Mutter library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Mutter library
Group: System/Libraries
Requires: lib%name-devel = %EVR
Requires: lib%name-gir = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the Mutter library.

%package gnome
Summary: GNOME-specific parts of Mutter
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: gnome-wm
Requires: %name = %EVR

%description gnome
This package contains everything necessary to use Mutter in GNOME desktop
environment.

%package tests
Summary: Tests for the Mutter WM
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Mutter.


%prep
%setup

%build
%meson \
	-Dintrospection=true \
	%{?_enable_remote_desktop:-Dremote_desktop=true} \
	%{?_enable_egl_device:-Degl_device=true} \
	%{?_disable_installed_tests:-Dinstalled_tests=false}
%meson_build

%install
%meson_install
%find_lang --with-gnome %name creating-%name-themes

%files -f %name.lang
%_bindir/*
%_libexecdir/%name-restart-helper
%dir %pkglibdir/plugins
%pkglibdir/plugins/*.so
%{?_enable_installed_tests:%dir %pkgdatadir}
%_desktopdir/%name.desktop
%_man1dir/*
%doc NEWS README.md

%if_enabled privatelib
%files -n lib%name
%_libdir/lib%name-%api_ver.so.*
%dir %pkglibdir
%pkglibdir/lib%name-clutter-%api_ver.so.*
%pkglibdir/lib%name-cogl-pango-%api_ver.so.*
%pkglibdir/lib%name-cogl-path-%api_ver.so.*
%pkglibdir/lib%name-cogl-%api_ver.so.*
%pkglibdir/lib%name-cogl-gles2-%api_ver.so.*

%files -n lib%name-devel
%_includedir/%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%pkglibdir/*.so
%_pkgconfigdir/*.pc
%endif

%files -n lib%name-gir
%pkglibdir/*.typelib

%files -n lib%name-gir-devel
%pkglibdir/*.gir

%files gnome
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.wayland.gschema.xml
%_datadir/GConf/gsettings/%name-schemas.convert
%_datadir/gnome-control-center/keybindings/*.xml

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%name-%api_ver/
%_datadir/installed-tests/%name-%api_ver/
%pkgdatadir/tests/
%endif


%changelog
* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 1:3.32.2-alt1
- 3.32.2

* Wed Apr 17 2019 Yuri N. Sedunov <aris@altlinux.org> 1:3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1:3.32.0-alt1
- updated to 3.32.0-13-g2ac7f7f1e

* Mon Nov 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.30.2-alt1
- 3.30.2

* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.30.1-alt1
- 3.30.1

* Sun Sep 30 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.30.0-alt2
- updated to 3.30.0-16-g0210b9510

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.30.0-alt1
- 3.30.0

* Thu Jul 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.28.3-alt1
- 3.28.3

* Tue Jul 03 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.28.2-alt2
- updated to 3.28.2-18-gfe16166

* Wed May 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.28.2-alt1
- 3.28.2

* Sat Apr 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.28.1-alt1
- 3.28.1

* Tue Apr 03 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.28.0-alt3
- add explicit BR to libGL-devel

* Sun Apr 01 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.28.0-alt2
- updated to 3.28.0-21-g7ac551c

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.28.0-alt1
- 3.28.0

* Thu Feb 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1:3.27.91-alt1
- 3.27.91

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.26.2-alt1
- 3.26.2
- enabled support for remote desktop

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.26.0-alt1
- 3.26.0

* Thu Jul 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.24.4-alt1
- 3.24.4

* Fri Jun 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.24.3-alt1
- 3.24.3

* Thu May 11 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.24.2-alt1
- 3.24.2

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.24.0-alt1
- 3.24.0

* Fri Feb 17 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.22.3-alt1
- 3.22.3

* Thu Nov 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1:3.22.2-alt1
- 3.22.2

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1:3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1:3.22.0-alt1
- 3.22.0

* Wed Jun 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1:3.20.3-alt1
- 3.20.3

* Wed May 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1:3.20.2-alt1
- 3.20.2

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1:3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1:3.20.0-alt1
- 3.20.0

* Tue Mar 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1:3.18.3-alt1
- 3.18.3

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 1:3.18.2-alt1
- 3.18.2

* Thu Oct 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1:3.18.1-alt2
- 3.18.1_77177252

* Thu Oct 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1:3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1:3.18.0-alt1
- 3.18.0

* Thu Jul 02 2015 Yuri N. Sedunov <aris@altlinux.org> 1:3.16.3-alt1
- 3.16.3

* Thu May 14 2015 Yuri N. Sedunov <aris@altlinux.org> 1:3.16.2-alt1
- 3.16.2

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1:3.16.1.1-alt1
- 3.16.1.1

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1:3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1:3.16.0-alt1
- 3.16.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1:3.14.4-alt1
- 3.14.4

* Sat Dec 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.14.3-alt1
- 3.14.3

* Thu Dec 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.14.2-alt3
- updated to 3.14.2_56e74b1e (fixed BGO #738686)

* Sun Nov 30 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.14.2-alt2
- updated to 3.14.2_d7ff632c (fixed weird tray icon behavior
  in gnome-shell, fixed BGO #740377, 740133)

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.14.2-alt1
- 3.14.2

* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.14.1.5-alt1
- 3.14.1.5

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.14.1-alt2
- rebuilt against libupower-glib.so.3

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.14.0-alt1
- 3.14.0

* Wed May 14 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.12.2-alt1
- 3.12.2

* Wed Apr 16 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.12.0-alt1
- 3.12.0

* Thu Mar 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.11.92-alt1
- 3.11.92

* Thu Feb 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.4-alt1
- 3.10.4

* Sat Feb 08 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.3-alt2
- updated to (fixed BGO ##723606, 710610, 720630 ..)

* Thu Jan 16 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.3-alt1
- 3.10.3

* Wed Dec 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.2-alt2
- updated to 7278f9b (fixed BGO #710296, 711618, 719669, 720545)

* Thu Nov 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.2-alt1
- 3.10.2

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.1.1-alt1
- 3.10.1.1

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.0.1-alt1
- 3.10.0.1

* Wed Jul 31 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.8.4-alt1
- 3.8.4

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.8.2-alt1
- 3.8.2

* Thu May 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.8.1-alt2
- updated to 2c210e0

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 1:3.8.0-alt1
- 3.8.0

* Tue Mar 19 2013 Alexey Shabalin <shaba@altlinux.ru> 1:3.7.92-alt1
- 3.7.92

* Thu Mar 07 2013 Alexey Shabalin <shaba@altlinux.ru> 1:3.7.91-alt1
- 3.7.91

* Fri Feb 22 2013 Alexey Shabalin <shaba@altlinux.ru> 1:3.7.90-alt1
- 3.7.90

* Mon Feb 18 2013 Alexey Shabalin <shaba@altlinux.ru> 1:3.6.3-alt1
- 3.6.3

* Tue Nov 13 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.6.1-alt1
- 3.6.1

* Mon Oct 08 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.6.0-alt2
- mutter-gnome as noarch

* Tue Sep 25 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.6.0-alt1
- 3.6.0

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.5.92-alt1
- 3.5.92

* Thu Sep 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.5.91-alt1
- 3.5.91

* Wed Apr 18 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.4.1-alt1
- 3.4.1

* Wed Mar 28 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.4.0-alt1
- 3.4.0

* Wed Jan 18 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.2.2-alt1
- 3.2.2

* Tue Oct 25 2011 Alexey Shabalin <shaba@altlinux.ru> 1:3.2.1-alt1
- 3.2.1

* Thu May 26 2011 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.2.1-alt1
- 3.0.2.1

* Wed Apr 06 2011 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.0-alt1
- 3.0.0

* Wed Mar 30 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.93-alt1
- 2.91.93

* Wed Mar 23 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.92-alt1
- 2.91.92

* Wed Mar 09 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.91-alt1
- 2.91.91

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.90-alt1.git20110302
- snapshot 20110302

* Fri Feb 25 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.90-alt1
- 2.91.90

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.6-alt1
- 2.91.6

* Thu Jan 20 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.5-alt1
- 2.91.5

* Mon Oct 11 2010 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.0-alt2
- add serial to requires

* Wed Oct 06 2010 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.0-alt1
- 2.91.0

* Tue Mar 23 2010 Alexey Shabalin <shaba@altlinux.ru> 1:2.29.1-alt1
- 2.29.1

* Sat Mar 13 2010 Alexey Shabalin <shaba@altlinux.ru> 1:2.29.0-alt2
- git snaphot ff4f096f1d9ec3d8113286ade9e9aa53da84b198
- install gir files to standart path

* Wed Mar 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.29.0-alt1
- 2.29.0

* Wed Feb 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.28.0-alt3
- fixed build with clutter 1.1.6

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.0-alt2
- enabled gobject-introspection

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Wed Sep 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.5-alt1
- 2.27.5

* Mon Sep 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.4-alt1
- 2.27.4

* Sat Aug 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.3-alt1
- 2.27.3

* Wed Aug 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.2-alt1
- 2.27.2

* Wed Aug 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.1-alt1
- initial release

