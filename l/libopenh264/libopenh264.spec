%def_enable snapshot
%define _name openh264
%def_enable check

Name: lib%_name
Version: 2.0.0
Release: alt1

Summary: H.264 codec library
Group: System/Libraries
License: BSD
Url: http://www.%_name.org/

%if_disabled snapshot
Source: https://github.com/cisco/%_name/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%ifarch %ix86
%add_optflags -msse2 -mfpmath=sse
%set_verify_elf_method textrel=relaxed
%endif

ExclusiveArch: x86_64

BuildRequires(pre): meson
BuildRequires: gcc-c++ nasm
%{?_enable_check:BuildRequires: libgtest-devel}

%description
OpenH264 is a codec library which supports H.264 encoding and decoding.
It is suitable for use in real time applications such as WebRTC.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Summary: Static H.264 codec library
Group: Development/C++
Requires: %name-devel = %EVR

%description devel-static
This package provides %_name static library.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%_libdir/%name.so.*
%doc LICENSE README.md RELEASES

%files devel
%_includedir/wels/
%_libdir/%name.so
%_pkgconfigdir/%_name.pc

%files devel-static
%_libdir/%name.a

%changelog
* Fri Oct 04 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- updated to v2.0.0-7-g0e377291

* Wed May 01 2019 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- first build for Sisyphus

