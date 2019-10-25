
%define sover 5
%define libopenh264 libopenh264_%sover
Name: openh264
Version: 2.0.0
Release: alt3

Summary: H.264 codec library
Group: System/Libraries
License: BSD
Url: http://www.openh264.org/

Source: %name-%version.tar

BuildRequires: gcc-c++ nasm

%description
OpenH264 is a codec library which supports H.264 encoding and decoding.
It is suitable for use in real time applications such as WebRTC.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %libopenh264

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Summary: Static H.264 codec library
Group: Development/C++
Requires: %name-devel

%description devel-static
This package provides %name static library.

%package -n %libopenh264
Summary: %name library
Group: System/Libraries
%description -n %libopenh264
%name library.

%prep
%setup -n %name-%version

# setup build options
%add_optflags %optflags_shared
%ifarch %ix86
%add_optflags -msse2 -mfpmath=sse
sed -i 's|^USE_ASM[[:space:]][[:space:]]*=.*|USE_ASM = No|' Makefile
sed -i 's|^HAVE_AVX2[[:space:]][[:space:]]*:=.*|HAVE_AVX2 := No|' build/arch.mk
%endif
sed -i -e 's|^CFLAGS_OPT=.*$|CFLAGS_OPT=%{optflags}|' Makefile
#sed -i -e '/^CFLAGS_OPT=/i LDFLAGS={ldflags}' Makefile
sed -i -e 's|^PREFIX=.*$|PREFIX=%{_prefix}|' Makefile
sed -i -e 's|^LIBDIR_NAME=.*$|LIBDIR_NAME=%{_lib}|' Makefile
sed -i -e 's|^SHAREDLIB_DIR=.*$|SHAREDLIB_DIR=%{_libdir}|' Makefile

%build
%make_build

%install
%makeinstall_std

%files -n %libopenh264
%doc LICENSE README.md RELEASES
%_libdir/libopenh264.so.%sover
%_libdir/libopenh264.so.*

%files devel
%_includedir/wels/
%_libdir/lib*.so
%_pkgconfigdir/%name.pc

%files devel-static
%_libdir/lib*.a

%changelog
* Fri Oct 25 2019 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt3
- rename according Shared Libs Policy

* Fri Oct 11 2019 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt2
- remove ExclusiveArch

* Fri Oct 04 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- updated to v2.0.0-7-g0e377291

* Wed May 01 2019 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- first build for Sisyphus

