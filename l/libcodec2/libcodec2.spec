Summary: libcodec2 is a library for the codec2 low bit rate speech codec
Name: libcodec2
Version: 0.9.2
Release: alt1.1
License: LGPL2.1
Group: System/Libraries
Url: http://rowetel.com/codec2.html
Source: %name-%version.tar
Source1: %name.watch
BuildRequires: cmake

%description
libcodec2 is a library for the codec2 low bit rate speech codec.

%package devel
Summary: codec2 development files
Group: Development/C
Requires: libcodec2 = %version-%release

%description devel
codec2 development files.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

# Create and install pkgconfig file
mkdir -p %buildroot%_libdir/pkgconfig
cat > %buildroot%_libdir/pkgconfig/codec2.pc << EOF
prefix=%prefix
exec_prefix=\${prefix}
includedir=\${prefix}/include/codec2
libdir=\${exec_prefix}/%_lib
Name: codec2
Description: Next-Generation Digital Voice for Two-Way Radio
Version: %version
Cflags: -I\${includedir}
Libs: -L\${libdir} -lcodec2
EOF


%files
%_libdir/libcodec2.so.*

%files devel
%_includedir/codec2
%_libdir/cmake/codec2
%_libdir/libcodec2.so
%_libdir/pkgconfig/codec2.pc

%changelog
* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.9.2-alt1.1
- NMU: spec: adapted to new cmake macros.

* Mon Jun 29 2020 Anton Farygin <rider@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Thu Aug 09 2018 Anton Farygin <rider@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue Oct 03 2017 Anton Farygin <rider@altlinux.ru> 0.7-alt1
- 0.7

* Fri Oct 21 2016 Anton Farygin <rider@altlinux.ru> 0.5.1-alt1
- new version

* Thu Feb 18 2016 Anton Farygin <rider@altlinux.ru> 0.5-alt1
- first build for Sisyphus
