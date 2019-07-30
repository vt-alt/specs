%def_enable snapshot

%define _name cpprestsdk
%define ver_major 2.10

%if_enabled snapshot
#can't build on %ix86, see bottom of /usr/share/cmake/websocketpp-configVersion.cmake
%def_without system_websocketpp
%else
# tarball doesn't contain websocketpp headers
%def_with system_websocketpp
%endif
%def_disable check

Name: cpprest
Version: %ver_major.14
Release: alt1

Summary: C++ REST library
Group: System/Libraries
License: MIT
Url: https://github.com/Microsoft/%_name

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildRequires: gcc-c++ cmake
BuildRequires: boost-devel >= 1.55 boost-interprocess-devel boost-filesystem-devel
BuildRequires: boost-asio-devel boost-locale-devel
BuildRequires: pkgconfig(openssl) >= 1.0
%{?_with_system_websocketpp:BuildRequires: websocketpp-devel >= 0.4}
BuildRequires: zlib-devel libbrotli-devel

%description
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

Also known as Casablanca.

%package -n lib%name
Summary: %summary
Group: System/Libraries

%description -n lib%name
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

This package provides shared %name library.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Requires: libssl-devel

%description -n lib%name-devel
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

This package provides development files for %name library.

%prep
%setup -n %_name-%version
# Remove bundled sources of websocketpp
%{?_with_system_websocketpp:rm -r Release/libs}
# Remove file ThirdPartyNotices.txt, which is associated to websocketpp
rm -f ThirdPartyNotices.txt
# fix libdir
subst 's|\(DESTINATION \)lib|\1%_lib|' Release/src/CMakeLists.txt

%build
cd Release
%add_optflags %optflags -D_FILE_OFFSET_BITS=64 -Wl,--as-needed
%cmake .. -DCMAKE_BUILD_TYPE=Release \
	  -DCMAKE_INSTALL_DO_STRIP=OFF \
	  -DCPPREST_EXCLUDE_BROTLI=OFF \
	  -DCPPREST_EXPORT_DIR=cmake/%_name
%cmake_build

%install
cd Release
%cmakeinstall_std

%check
cd Release
LD_LIBRARY_PATH=%buildroot/%_libdir %make -C BUILD test

%files -n lib%name
%_libdir/libcpprest.so.*
%doc README.md license.txt

%files -n lib%name-devel
%_includedir/%name
%_includedir/pplx
%_libdir/libcpprest.so
%_libdir/cmake/%_name/
%doc README.md

%changelog
* Wed Jul 17 2019 Yuri N. Sedunov <aris@altlinux.org> 2.10.14-alt1
- 2.10.14

* Thu Apr 25 2019 Yuri N. Sedunov <aris@altlinux.org> 2.10.13-alt1
- 2.10.13

* Sun Mar 31 2019 Yuri N. Sedunov <aris@altlinux.org> 2.10.12-alt1
- updated to v2.10.12-2-g621f47a5

* Sun Feb 03 2019 Yuri N. Sedunov <aris@altlinux.org> 2.10.10-alt1
- 2.10.10

* Wed Jan 23 2019 Yuri N. Sedunov <aris@altlinux.org> 2.10.9-alt1
- 2.10.9 with bundled websocketpp

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.6-alt1
- 2.10.6

* Thu Aug 30 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.5-alt2
- rebuilt with openssl-1.1

* Sun Aug 19 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.5-alt1
- 2.10.5

* Fri Aug 17 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.4-alt1
- 2.10.4

* Fri Aug 03 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.3-alt1
- 2.10.3

* Fri Jun 01 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt3
- rebuilt with boost-1.67

* Wed Apr 18 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt2
- rebuilt with boost-1.66

* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt1
- 2.10.2

* Fri Jan 19 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- first build for Sisyphus

