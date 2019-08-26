Name: libvisio
Version: 0.1.7
Release: alt1
Summary: A library providing ability to interpret and import visio diagrams

Group: System/Libraries
License: MPLv2
Url: https://wiki.documentfoundation.org/DLP/Libraries/libvisio
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(cppunit) pkgconfig(librevenge-generators-0.0)

BuildRequires: doxygen
BuildRequires: gperf perl

%description
Libvisio is library providing ability to interpret and import visio
diagrams into various applications. You can find it being used in
libreoffice.

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
Requires: %name = %version-%release
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Visio diagrams into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform Visio diagrams into other formats.
Currently supported: XHTML, raw, plain text.

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure --disable-static --disable-werror
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING.*
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%dir %_docdir/%name
%_docdir/%name/html

%files tools
%_bindir/*

%changelog
* Mon Aug 26 2019 Alexey Shabalin <shaba@altlinux.org> 0.1.7-alt1
- 0.1.7

* Tue Oct 02 2018 Alexey Shabalin <shaba@altlinux.org> 0.1.6-alt2
- rebuild with new icu

* Thu Feb 15 2018 Grigory Ustinov <grenka@altlinux.org> 0.1.6-alt1.1
- NMU:
  + Update url (Closes: #30667).
  + Update licence.

* Mon Feb 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Thu Aug 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt2
- Fixed build with new boost.

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt1.4
- Revert previous update and disable deprecated symbols instead

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt1.3
- Fixed broken linking

* Sat Feb 13 2016 Sergey V Turchin <zerg@altlinux.org> 0.1.3-alt1.2
- NMU: fix build requires

* Fri Feb 12 2016 Sergey V Turchin <zerg@altlinux.org> 0.1.3-alt1.1
- NMU: rebuild with new libicu

* Tue Aug 18 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Mon Jan 19 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Thu Sep 05 2013 Fr. Br. George <george@altlinux.ru> 0.0.31-alt1
- Autobuild version bump to 0.0.31
- Build scheme changed

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.0.30-alt1
- initial build
