%define ver_major 1.0
%define api_ver 1.0

%def_enable introspection
%def_enable vala
%def_enable check

Name: gtk-vnc
Version: %ver_major.0
Release: alt1

Summary: VNC viewer widget
Group: System/Libraries
License: LGPLv2.1+
Url: https://wiki.gnome.org/Projects/gtk-vnc

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: libgtk3vnc = %version-%release

%define gnutls_ver 3.1.18
%define gcrypt_ver 1.5.0
%define glib_ver 2.42

BuildRequires(pre): meson
BuildRequires: libgtk+3-devel
# pod2man
BuildRequires: perl-podlators
BuildRequires: libgnutls-devel >= %gnutls_ver libgcrypt-devel >= %gcrypt_ver
BuildRequires: glib2-devel >= %glib_ver libcairo-gobject-devel libsasl2-devel
BuildRequires: libpulseaudio-devel zlib-devel perl-Text-CSV
%{?_enable_vala:BuildRequires: vala-tools}
%{?_with_python:BuildRequires: python-module-pygobject-devel}
%{?_enable_introspection:BuildRequires: libgtk+3-gir-devel}

%description
gtk-vnc is a project providing client side APIs for the RFB protocol/VNC
remote desktop technology.It provides two core C libraries, libgvnc for
interacting with the core RFB protocol and libgtk-vnc for a GTK display
widget.

This package provides gvnccapture and gvncviewer - utilities that use
gtk-vnc libraries.

%package -n libgvnc
Summary: GVnc library
Group: System/Libraries

%description -n libgvnc
gtk-vnc is a project providing client side APIs for the RFB protocol/VNC
remote desktop technology.

This package contains the GObject-based library to interact with the RFB
protocol.

%package -n libgvnc-devel
Summary: GVnc library
Group: Development/C
Requires: libgvnc = %version-%release
%{?_disable_vapi:Obsoletes: libgvnc-vala}
%{?_disable_vapi:Provides: libgvnc-vala = %version-%release}

%description -n libgvnc-devel
gtk-vnc is a project providing client side APIs for the RFB protocol/VNC
remote desktop technology.

This package provides development files for the GVnc library.

%package -n libgtk3vnc
Summary: VNC viewer widget library
Group: System/Libraries
Requires: libgvnc = %version-%release

%description -n libgtk3vnc
gtk-vnc is a VNC viewer widget for GTK. It is built using
coroutines allowing it to be completely asynchronous while
remaining single threaded.

%package -n libgtk3vnc-devel
Summary: Development package for VNC viewer widget library
Group: Development/C
Requires: libgtk3vnc = %version-%release
Requires: libgvnc-devel = %version-%release
%{?_disable_vapi:Obsoletes: libgtk3vnc-vala}
%{?_disable_vapi:Provides: libgtk3vnc-vala = %version-%release}

%description -n libgtk3vnc-devel
gtk-vnc is a VNC viewer widget for GTK. It is built using
coroutines allowing it to be completely asynchronous while
remaining single threaded.

This package provides development files for the GtkVnc widget library.

%package -n libgvnc-gir
Summary: GObject introspection data for the CVnc library
Group: System/Libraries
Requires: libgvnc = %version-%release

%description -n libgvnc-gir
GObject introspection data for the GVnc library

%package -n libgvnc-gir-devel
Summary: GObject introspection devel data for the GVnc library
Group: System/Libraries
BuildArch: noarch
Requires: libgvnc-gir = %version-%release

%description -n libgvnc-gir-devel
GObject introspection devel data for the GVnc library

%package -n libgvnc-vala
Summary: Vala bindings for GVnc library
Group: Development/C
BuildArch: noarch
Requires: libgvnc = %version-%release

%description -n libgvnc-vala
This package provides Vala language bindings for for the GVnc library.

%package -n libgtk3vnc-gir
Summary: GObject introspection data for the GtkVnc library
Group: System/Libraries
Requires: libgtk3vnc = %version-%release
Requires: libgvnc-gir = %version-%release

%description -n libgtk3vnc-gir
GObject introspection data for the GtkVnc widget library

%package -n libgtk3vnc-gir-devel
Summary: GObject introspection devel data for the GtkVnc library
Group: System/Libraries
BuildArch: noarch
Requires: libgtk3vnc-gir = %version-%release
Requires: libgvnc-gir-devel = %version-%release

%description -n libgtk3vnc-gir-devel
GObject introspection devel data for the GtkVnc widget library

%package -n libgtk3vnc-vala
Summary: Vala bindings for GtkVnc library
Group: Development/C
Requires: libgtk3vnc = %version-%release

%description -n libgtk3vnc-vala
This package provides Vala language bindings for for the GtkVnc widget
library.

%prep
%setup

%build
%meson \
%{?_enable_vala:-Dwith-vala=true}
%meson_build

%install
%meson_install
%find_lang %name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -f %name.lang
%_bindir/*
%_man1dir/*

%files -n libgvnc
%_libdir/libgvnc-%api_ver.so.*
%_libdir/libgvncpulse-%api_ver.so.*

%files -n libgvnc-devel
%_libdir/libgvnc-%api_ver.so
%_libdir/libgvncpulse-%api_ver.so
%_includedir/gvnc-%api_ver/
%_includedir/gvncpulse-%api_ver/
%_pkgconfigdir/gvnc-%api_ver.pc
%_pkgconfigdir/gvncpulse-%api_ver.pc

%if_enabled vala
%{?_enable_vapi:%files -n libgvnc-vala}
%_vapidir/gvnc-%api_ver.vapi
%_vapidir/gvnc-%api_ver.deps
%_vapidir/gvncpulse-%api_ver.vapi
%_vapidir/gvncpulse-%api_ver.deps
%endif

%files -n libgtk3vnc
%_libdir/libgtk-vnc-2.0.so.*

%files -n libgtk3vnc-devel
%_libdir/libgtk-vnc-2.0.so
%_includedir/gtk-vnc-2.0
%_pkgconfigdir/gtk-vnc-2.0.pc

%if_enabled vala
%{?_enable_vapi:%files -n libgtk3vnc-vala}
%_vapidir/gtk-vnc-2.0.deps
%_vapidir/gtk-vnc-2.0.vapi
%endif

%if_enabled introspection
%files -n libgvnc-gir
%_typelibdir/GVnc-%api_ver.typelib
%_typelibdir/GVncPulse-%api_ver.typelib

%files -n libgvnc-gir-devel
%_girdir/GVnc-%api_ver.gir
%_girdir/GVncPulse-%api_ver.gir

%files -n libgtk3vnc-gir
%_typelibdir/GtkVnc-2.0.typelib

%files -n libgtk3vnc-gir-devel
%_girdir/GtkVnc-2.0.gir
%endif


%changelog
* Wed Aug 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0 (removed gtk2 support, ported to Meson build system)

* Fri Aug 17 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0

* Fri Mar 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Fri May 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Thu Feb 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0 (fixed CVE-2017-5884, CVE-2017-5885)

* Thu Aug 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Wed Apr 06 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt2
- rebuilt against libgnutls.so.30

* Tue Feb 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Tue Oct 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt2
- rebuilt with libsasl2.so.3

* Wed Sep 18 2013 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Sat Feb 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Thu Jul 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt3
- updated buildreqs

* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt2
- move .vapi-files to *-devel subpackages

* Sun Jan 08 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Nov 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4
- new *-vala subpackages

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.3-alt3.1
- Rebuild with Python-2.7

* Tue Mar 08 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt3
- updated buildreqs

* Sat Feb 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt2
- build against GTK+3 too

* Fri Feb 18 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Tue Feb 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt2
- updated buildreqs

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.10-alt1.1
- Rebuilt with python 2.6

* Wed Oct 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.10-alt1
- 0.3.10

* Thu Aug 13 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9
- updated buildreqs

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8
- updated buildreqs

* Thu Apr 24 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.5-alt2
- fix #15449

* Sun Apr 13 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.5-alt1
- First build for ALTLinux


