Name: libfreehand
Version: 0.1.2
Release: alt1.1
Summary: A library for import of Macromedia/Adobe FreeHand documents

Group: System/Libraries
License: MPLv2.0
Url: http://www.freedesktop.org/wiki/Software/libfreehand/
Source: %name-%version.tar.xz
Patch1: 0001-Add-missing-semicolon-to-fix-build-with-icu-65.1.patch

# Automatically added by buildreq on Mon Jul 31 2017
# optimized out: glibc-kernheaders-x86 libstdc++-devel perl pkg-config python-base xz
BuildRequires: doxygen gcc-c++ glibc-kernheaders-generic gperf libicu-devel liblcms2-devel librevenge-devel zlib-devel

BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0) pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(zlib)

BuildRequires: doxygen
BuildRequires: gperf cppunit-devel

%description
libfreehand is library providing ability to interpret and import
Macromedia/Adobe FreeHand documents into various applications.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Macromedia/Adobe FreeHand documents into other formats
Group: Publishing

%description tools
Tools to transform Macromedia/Adobe FreeHand documents into other formats.
Currently supported: SVG, raw.

%prep
%setup
%patch1 -p1

%build
mkdir -p m4
%autoreconf
%configure --disable-silent-rules --disable-static --disable-werror
%make_build

%install
%makeinstall_std
# we install API docs directly from build
rm -rf %buildroot/%_docdir/%name

%files
%doc AUTHORS COPYING
%_libdir/*.so.*

%files devel
%doc ChangeLog
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc COPYING
%doc docs/doxygen/html

%files tools
%_bindir/*

%changelog
* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.1.2-alt1.1
- FTBFS: use upstream fix for build with icu65.

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 0.1.2-alt1
- Autobuild version bump to 0.1.2

* Mon Jul 31 2017 Fr. Br. George <george@altlinux.ru> 0.1.1-alt1
- Autobuild version bump to 0.1.1
- Fix buildreqs

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.1.0-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.0.0-alt1
- Initial build from FC

* Mon Nov 04 2013 David Tardon <dtardon@redhat.com> - 0.0.0-3
- fix memory leak

* Thu Oct 31 2013 David Tardon <dtardon@redhat.com> 0.0.0-2
- add gperf to BuildRequires

* Thu Oct 31 2013 David Tardon <dtardon@redhat.com> 0.0.0-1
- initial import
