%define _name uhttpmock
%define api_ver 0.0

Name: lib%_name
Version: 0.6.0
Release: alt0.3

Summary: HTTP web service mocking library
Group: System/Libraries
License: LGPLv2
Url: https://gitlab.com/%_name/%_name

Source: %_name-%version.tar

%define glib_ver 2.36
%define soup_ver 2.38

BuildRequires: autoconf-archive intltool gtk-doc
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libsoup-devel >= %soup_ver
BuildRequires: gobject-introspection-devel libsoup-gir-devel
BuildRequires: vala-tools

%description
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request and response traces.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries, header files and documentation for
developing applications that use %name.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for %_name.

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name library.

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %_name library.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
    --disable-static \
    --enable-gtk-doc \
    --enable-introspection \
    --enable-vala=yes
%make_build

%check
#%make check

%install
%makeinstall_std

%files
%_libdir/%name-%api_ver.so.*
%doc README NEWS AUTHORS

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%files devel-doc
%_datadir/gtk-doc/html/%name-%api_ver/

%files gir
%_libdir/girepository-1.0/Uhm-%api_ver.typelib

%files gir-devel
%_datadir/gir-1.0/Uhm-%api_ver.gir

%changelog
* Wed Jun 26 2019 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt0.3
- updated to 0.5.1-13-gcda4b63

* Fri May 04 2018 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt0.2
- NMU: Rebuilt for e2k.

* Fri Jul 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt0.1
- 0.6.0_36d462a0

* Mon Jul 06 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt3
- 0.4.0 release (from gitlab, not github)

* Sun Apr 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt2
- updated to 0.4.0_d30225faf

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- first build for Sisyphus

