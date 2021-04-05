%def_disable snapshot

%define ver_major 0.32
%def_disable introspection
%def_enable gtk_doc
%def_enable man
%def_enable bash_completion
%def_enable vala

Name: dconf
Version: %ver_major.0
Release: alt1.1

Summary: A simple configuration system
Group: System/Servers
License: LGPLv2.1+
Url: https://wiki.gnome.org/Projects/dconf

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: https://download.gnome.org/sources/dconf/%ver_major/%name-%version.tar.xz
%endif
Source1: update-dconf-database.filetrigger
Patch0: dconf-0.32.0-meson-0.52.patch

Provides: %_rpmlibdir/update-dconf-database.filetrigger

Requires: lib%name = %version-%release dbus

BuildRequires(pre): meson
BuildRequires: libgio-devel >= 2.44.0 libdbus-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires: vala-tools >= 0.18.0}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_man:BuildRequires: xsltproc}
%{?_enable_bash_completion:BuildRequires: pkgconfig(bash-completion)}

%description
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

%package -n lib%name
Summary: Shared library for dconf
Group: System/Libraries

%description -n lib%name
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

This package provides shared library required for dconf to work

%package -n lib%name-devel
Summary: Development files for dconf library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

This is a dconf development package. Contains files needed for doing
development using dconf.

%package -n lib%name-devel-doc
Summary: Development documentation for dconf library
Group: Development/Documentation
Conflicts: lib%name < %version
BuildArch: noarch

%description -n lib%name-devel-doc
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

This package contains development documentation for dconf library.

%package -n lib%name-gir
Summary: GObject introspection data for the dconf library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the dconf library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the dconf library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the dconf library

%package -n lib%name-vala
Summary: Vala language bindings for the dconf library
Group: Development/Other
BuildArch: noarch
Requires: lib%name = %version-%release

%description -n lib%name-vala
This package provides Vala language bindings  for the dconf library

%define _libexecdir %_prefix/libexec

%prep
%setup
%patch0 -p1

%build
%meson \
	%{?_enable_gtk_doc:-Dgtk_doc=true} \
	-Dman=true \
	%{?_enable_vala:-Dvapi=true} \
	%{?_disable_bash_completion:-Dbash_completion=false}
%meson_build

%install
%meson_install
mkdir -p %buildroot{%_datadir,%_sysconfdir}/%name/{profile,db}

# rpm posttrans filetrigger
install -pD -m755 {%_sourcedir,%buildroot%_rpmlibdir}/update-dconf-database.filetrigger

%find_lang %name

%files -f %name.lang
%_bindir/dconf
%_libdir/gio/modules/libdconfsettings.so
%_libexecdir/dconf-service
%_datadir/dbus-1/services/ca.desrt.dconf.service
%_rpmlibdir/update-dconf-database.filetrigger
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/profile
%dir %_sysconfdir/%name/db
%dir %_datadir/%name
%dir %_datadir/%name/profile
%dir %_datadir/%name/db
%if_enabled man
%_man1dir/%name-service.1.*
%_man1dir/%name.1.*
%_man7dir/%name.7.*
%endif
%{?_enable_bash_completion:%_datadir/bash-completion/completions/dconf}
%doc README NEWS

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*
%endif

%if_enabled vala
%files -n lib%name-vala
%_vapidir/dconf.deps
%_vapidir/dconf.vapi
%endif

%changelog
* Wed Mar 31 2021 Valery Inozemtsev <shrek@altlinux.ru> 0.32.0-alt1.1
- fixed link_whole usage for meson 0.52.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- 0.32.0

* Tue Oct 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.30.1-alt1
- 0.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1
- 0.30.0

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- 0.28.0

* Tue Oct 03 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26.1-alt1
- 0.26.1

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Fri Sep 19 2014 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Tue Jul 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Thu Jul 04 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt2
- updated to 4171008

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Thu Nov 01 2012 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.90-alt1
- 0.13.90

* Mon May 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sat Mar 03 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt3
- %%_sysconfdir/%%_name/{profile,db} owned by dconf subpackage

* Mon Nov 07 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt2
- implemented update-dconf-database.filetrigger

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Tue Aug 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- 0.7.5

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- 0.7.3

* Fri Dec 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Fri Dec 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt2
- fixed linking for dconf library

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Thu Jun 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1
- introspection support
- gtk-doc documentation

* Tue May 25 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Sun May 23 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- first build for Sisyphus

