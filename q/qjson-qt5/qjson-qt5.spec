%def_disable snapshot
%define _name qjson

Name: %_name-qt5
Version: 0.9.0
Release: alt2

Group: System/Libraries
Summary: Lightweight data-interchange format
Url: http://qjson.sourceforge.net
License: GPLv2+

%if_disabled snapshot
Source: http://sourceforge.net/projects/qjson/files/%name/%version/%_name-%version.tar.gz
%else
#VCS: https://github.com/flavio/qjson/
Source: %_name-%version.tar
%endif

BuildRequires: cmake gcc-c++ qt5-base-devel

%description
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It can represents integer, real number, string, an ordered sequence of value,
and a collection of name/value pairs. QJson is a qt-based library that maps
JSON data to QVariant objects: JSON arrays will be mapped to QVariantList instances,
while JSON objects will be mapped to QVariantMap.

%package -n lib%name
Summary: Lightweight data-interchange format library
Group: System/Libraries

%description -n lib%name
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It can represents integer, real number, string, an ordered sequence of value,
and a collection of name/value pairs. QJson is a qt-based library that maps
JSON data to QVariant objects: JSON arrays will be mapped to QVariantList instances,
while JSON objects will be mapped to QVariantMap.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: lib%name = %version-%release

%description devel
Development files for %name


%prep
%setup -n %_name-%version

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif
%cmake \
    -DCMAKE_MODULES_INSTALL_DIR=%_datadir/CMake/Modules
%cmake_build

%install
%cmakeinstall_std

%files -n lib%name
%doc README*
%_libdir/lib%name.so.*

%files devel
%doc README*
%_libdir/lib%name.so
%_includedir/%name/
%_libdir/cmake/%name/
%_pkgconfigdir/QJson-qt5.pc

%changelog
* Tue Sep 03 2019 Michael Shigorin <mike@altlinux.org> 0.9.0-alt2
- E2K: explicit -std=c++11

* Thu Jan 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0

* Thu Jul 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- first build for Sisyphus (0.8.1-118-g5e3b9b8)

