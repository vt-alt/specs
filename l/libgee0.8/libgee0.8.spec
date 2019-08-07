%define _name libgee
%define ver_major 0.20
%define api_ver 0.8
%def_disable static

Name: %_name%api_ver
Version: %ver_major.2
Release: alt1

Summary: a collection library providing GObject-based interfaces
License: LGPL
Group: System/Libraries
Url: http://live.gnome.org/Libgee

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildRequires: libgio-devel >= 2.36 gobject-introspection-devel
BuildRequires: libvala-devel >= 0.23.2 vala-tools

%description
libgee is a collection library providing GObject-based interfaces and classes
for commonly used data structures.

The ArrayList, HashSet, and HashMap classes provide a reasonable sample
implementation of the List, Set, and Map interfaces. ReadOnlyCollection,
ReadOnlyList, ReadOnlySet, and ReadOnlyMap are read-only wrapper classes that
prevent modification of the underlying collection.

libgee is written in Vala and can be used like any GObject-based C
library. It's planned to provide bindings for further languages.

%package devel
Group: Development/C
Summary: Development files of %name
Provides: %_name-devel = %version-%release
Requires: %name = %version-%release

%description devel
libgee is a collection library providing GObject-based interfaces and classes
for commonly used data structures.

This package contains the C headers and libs required for building programs
with %name.

%package gir
Summary: GObject introspection data for the libgee library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the libgee library

%package gir-devel
Summary: GObject introspection devel data for the libgee library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the libgee library

%if_enabled static
%package devel-static
Group: Development/C
Summary: Static library of %name
Requires: %name-devel = %version-%release

%description devel-static
libgee is a collection library providing GObject-based interfaces and classes
for commonly used data structures.

This package contains the static library required for statically linking
applications with %name.

%endif #enabled static

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/libgee-%api_ver.so.*
%doc AUTHORS ChangeLog* MAINTAINERS NEWS README

%files devel
%_includedir/gee-%api_ver
%_libdir/libgee-%api_ver.so
%_pkgconfigdir/gee-%api_ver.pc
%_datadir/vala/vapi/gee-%api_ver.vapi

%files gir
%_typelibdir/Gee-%api_ver.typelib

%files gir-devel
%_girdir/Gee-%api_ver.gir

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Aug 05 2019 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1
- 0.20.2

* Mon Feb 12 2018 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Thu Nov 14 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt1
- 0.10.5

* Tue Sep 03 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8.8-alt1
- 0.8.8

* Sat Jul 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8.7-alt1
- 0.8.7

* Thu Apr 11 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8.6-alt1
- 0.8.6

* Tue Mar 05 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8.5-alt1
- 0.8.5

* Sun Feb 17 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8.4-alt1
- 0.8.4

* Tue Dec 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Tue Nov 20 2012 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- first build libgee0.8 for Sisyphus

* Mon Nov 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.6.1-alt1
- 0.6.6.1

* Fri Aug 31 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Mon Jan 30 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Fri Oct 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.2.1-alt1
- 0.6.2.1

* Tue Jun 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt2
- rebuild with rpm-build-vala

* Mon Jan 31 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Oct 18 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0
- add gir subpackages

* Mon May 24 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.5.0_9_g9a3d481-alt1
- minor new version compatible with current vala

* Mon Oct 05 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.5.0-alt1
- new version

* Mon Oct 05 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.4.0-alt1
- new version
- moved *.vapi to devel subpackage

* Mon Jul 20 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.1.6-alt1
- new version

* Sat Feb 21 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.1.5-alt1
- new version

* Sat Oct 04 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.1.4-alt1.20081001
- initial build for ALTLinux
