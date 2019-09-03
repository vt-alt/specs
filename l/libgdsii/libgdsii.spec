Name:		libgdsii
Summary:	A C++ library for working with GDSII binary data files
Version:	0.21
Release:	alt1
License:	GPLv2
URL:		https://github.com/HomerReid/libGDSII
Source:		%name-%version.tar.gz
Group:		System/Libraries

BuildRequires:	gcc-c++

%description
libGDSII is a C++ library for working with GDSII binary data files,
intended primarily for use with the computational electromagnetism codes
scuff-em and meep but sufficiently general-purpose to allow other uses
as well.

The packages consists of

* a C++ library (libGDSII) with API functions for reading, processing,
and exporting GDSII files

%package devel
Group: Development/C++
Summary: Development files for %name
%description devel
%summary

%package devel-static
Group: Development/C++
Summary: Development static files for %name
%description devel-static
%summary

%package -n GDSIIConvert
Group:	Graphics
Summary: Reporting statistics on GDSII geometries and exporting them to other file formats
%description -n GDSIIConvert
A command-line executable code (GDSIIConvert) for reporting statistics
on GDSII geometries and exporting them to other file formats, notably
including the GMSH geometry format.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
install -D libGDSII-pkgconfig %buildroot%_pkgconfigdir/libGDSII.pc

%files
%doc README*
%_libdir/*.so.*

%files devel
%doc %_datadir/libGDSII
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files devel-static
%_libdir/*.a

%files -n GDSIIConvert
%_bindir/*

%changelog
* Mon Aug 05 2019 Fr. Br. George <george@altlinux.ru> 0.21-alt1
- Initial build for ALT

