%def_enable static
%def_enable check

%define Name Exempi
%define _name exempi

Name: lib%_name
Version: 2.5.1
Release: alt1

Summary: Library for easy parsing of XMP metadata
Group: System/Libraries
License: %bsd
Url: http://libopenraw.freedesktop.org/wiki/%Name

Source: http://libopenraw.freedesktop.org/download/%_name-%version.tar.bz2

BuildRequires(pre): rpm-build-licenses
BuildRequires: boost-test-devel gcc-c++ libexpat-devel zlib-devel

%description
%Name provides a library for easy parsing of XMP metadata. It is a
port of Adobe XMP SDK to work on UNIX.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name%{?_disable_shared:-devel-static} = %version-%release

%description devel
This package contains the libraries and header files needed for
developing with %name.

%if_enabled static
%package devel-static
Summary: Static library for developing programs that will use %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains the static library needed for developing with
%name.
%endif


%prep
%setup -n %_name-%version
# fix boost.m4 for gcc < 5, lcc < 1.23
sed -i~ 's|\^\(boost-lib-version\)|\1|' m4/boost.m4

%build
%autoreconf
%configure  \
    %{subst_enable static} \
    CPPFLAGS="-DBanAllEntityUsage=1"
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/%_name
%_libdir/*.so.*
%_man1dir/%_name.1.*
%doc AUTHORS ChangeLog NEWS README

%files devel
%_includedir/%_name-2.0/
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Tue Aug 06 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.1-alt1
- 2.5.1

* Tue Jan 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Fri Mar 23 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.5-alt1
- 2.4.5 (fixed CVE-2018-7730, CVE-2018-7728, CVE-2018-7729, CVE-2018-7731)

* Thu Mar 01 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.4-alt1.1
- fixed boost.m4 for e2k

* Tue Feb 27 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.4-alt1
- 2.4.4

* Wed Feb 01 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Thu Jan 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Sat Mar 26 2016 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1
- %%check section

* Fri Sep 14 2012 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Tue Nov 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt2
- rebuild

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Sun Dec 28 2008 Led <led@altlinux.ru> 2.1.0-alt1
- 2.1.0
- cleaned up spec

* Mon Aug 25 2008 Led <led@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Tue May 06 2008 Led <led@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Thu Apr 03 2008 Led <led@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sat Feb 02 2008 Led <led@altlinux.ru> 1.99.9-alt1
- 1.99.9
- cleaned up spec
- initial build for Sisyphus

* Wed Sep 05 2007 Deji Akingunola <dakingun@gmail.com> - 1.99.4-2
- Rebuild for expat 2.0

* Wed Aug 22 2007 Deji Akingunola <dakingun@gmail.com> - 1.99.4-1
- Update tp 1.99.4

* Tue Jul 10 2007 Deji Akingunola <dakingun@gmail.com> - 1.99.3-1
- Initial packaging for Fedora
