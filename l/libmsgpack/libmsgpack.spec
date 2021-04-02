%define oname msgpack
Name: libmsgpack
Version: 3.3.0
Release: alt2

Summary: Binary-based efficient object serialization library

License: Boost Software License, Version 1.0
Group: System/Libraries
Url: http://msgpack.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/msgpack/msgpack-c/releases/download/cpp-%version/%oname-%version.tar.gz
Source: %name-%version.tar
Patch: msgpack-3.2.0-alt-fix-vrefbuffer-use-on-ppc64le.patch
# actually poor implementation:
# https://github.com/msgpack/msgpack-c/issues/881
Patch1: msgpack-3.3.0-alt-drop-broken-test.patch

BuildRequires: cmake zlib-devel
BuildRequires: gcc-c++ >= 4.8

# for %%check
BuildRequires: ctest libgtest-devel

Provides: %oname = %version-%release
Obsoletes: %oname

%description
MessagePack is a binary-based efficient object serialization
library. It enables to exchange structured objects between many
languages like JSON. But unlike JSON, it is very fast and small.

%package devel
Summary: Libraries and header files for %name
Group: Development/C++
Requires: %name = %version-%release

Provides: %oname-devel = %version-%release
Obsoletes: %oname-devel

%description devel
Libraries and header files for %name

%prep
%setup
%patch0 -p2
%patch1 -p1
subst "s|/lib|/%_lib|g" CMakeLists.txt

%build
%cmake_insource -DCMAKE_INSTALL_LIBDIR=%_lib -DBUILD_SHARED_LIBS=ON -DMSGPACK_CXX11=ON
%make_build

%check
export LD_LIBRARY_PATH=$(pwd)
%make test

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog LICENSE_1_0.txt NOTICE README README.md
%_libdir/*.so.*

%files devel
%_includedir/msgpack.*
%_includedir/msgpack/
%_libdir/*.so
%_pkgconfigdir/msgpack.pc
%_libdir/cmake/msgpack/

%changelog
* Wed Sep 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3.0-alt2
- restored build on armh

* Tue Sep 08 2020 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- new version 3.3.0 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt1
- new version 3.2.1 (with rpmrb script)

* Fri Aug 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.2.0-alt2
- Fixed use of vrefbuffer.hpp header on ppc64le.

* Tue Jun 18 2019 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- new version 3.2.0 (with rpmrb script)

* Sun May 12 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt2
- enable tests
- fix cmake static lib issue (use BUILD_SHARED_LIBS)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1 (with rpmrb script)

* Wed Sep 05 2018 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- new version 3.0.1 (with rpmrb script)

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.5-alt1
- new version 2.1.5 (with rpmrb script)

* Wed Aug 10 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)
- note: breaking changes

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1 (with rpmrb script)

* Mon Jan 11 2016 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sun Nov 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Sun Nov 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Sun Nov 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.5.9-alt2
- initial manual build for ALT Linux

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.5.9-alt1_4
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.9-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1_2
- update to new release by fcimport

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1_1
- update to new release by fcimport

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1_5
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1_4
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1_3
- initial fc import

