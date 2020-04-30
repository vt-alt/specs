%define rname pugixml

Name: libpugixml
Version: 1.10
Release: alt2
Summary: A light-weight C++ XML processing library

Group: System/Libraries
License: MIT
Url: http://pugixml.org

Source0: %rname-%version.tar.gz

BuildRequires: ctest cmake
BuildRequires: gcc-c++
Provides: %rname = %version-%release

%description
pugixml is a light-weight C++ XML processing library.
It features:
- DOM-like interface with rich traversal/modification capabilities
- Extremely fast non-validating XML parser which constructs the DOM tree
  from an XML file/buffer
- XPath 1.0 implementation for complex data-driven tree queries
- Full Unicode support with Unicode interface variants and automatic
  encoding conversions

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release
Provides: %rname-devel = %version-%release

%description devel
Development files for package %name

%prep
%setup -n %rname-%version

%build
%cmake -DBUILD_SHARED_LIBS=1
%cmake_build

%install
%cmakeinstall_std

%files
%doc readme.txt
%_libdir/*.so.*

%files devel
%doc docs/*
%_libdir/*.so
%_libdir/cmake/pugixml/
%_includedir/*.hpp
%_libdir/pkgconfig/pugixml.pc

%changelog
* Tue Apr 28 2020 Andrey Cherepanov <cas@altlinux.org> 1.10-alt2
- Package pugixml.pc.

* Mon Sep 16 2019 Andrey Cherepanov <cas@altlinux.org> 1.10-alt1
- New version.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.9-alt1
- New version.

* Tue Nov 29 2016 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- new version 1.8.1

* Thu Oct 29 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.7-alt1
- Updated to 1.7.

* Sat Oct 03 2015 Andrey Cherepanov <cas@altlinux.org> 1.6-alt1
- New version

* Tue Jan 14 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt3
- Make devel .so library as symlink to so-named library

* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Build in Sisyphus under name libpugixml

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- initial fc import

