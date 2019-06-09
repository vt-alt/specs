# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 4

Summary: Convolution engine library
Name: zita-convolver
Version: 4.0.3
Release: alt1
License: GPLv3+
Group: Sound
Url: http://kokkinizita.linuxaudio.org/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%name-%version.tar.bz2

BuildRequires: gcc-c++ libfftw3-devel

%description
%name is a fast, partitioned convolution engine library.

%package -n lib%name%sover
Summary: Convolution engine library
Group: System/Libraries
Provides: %name = %EVR

%description -n lib%name%sover
%name is a fast, partitioned convolution engine library.

%package devel
Summary: Fast, partitioned convolution engine library
Group: Development/Other
Requires: lib%name%sover = %EVR

%description devel
%name is a fast, partitioned convolution engine library. This package
contains libraries and header files for developing applications that use
%name.

%prep
%setup

# No need to call ldconfig during packaging
%__subst '\|ldconfig|d' source/Makefile

# Preserve timestamps
%__subst 's|install |install -p |' source/Makefile

# Fix optflags
%__subst 's|-march=native|%optflags|' source/Makefile

%build
%make_build -C source PREFIX=%prefix

%install
%makeinstall_std -C source PREFIX=%prefix LIBDIR=%_libdir
# create .so.x link
ln -s lib%name.so.%version %buildroot%_libdir/lib%name.so.%sover

%files -n lib%name%sover
%doc AUTHORS COPYING
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files devel
%_includedir/%name.h
%_libdir/lib%name.so

%changelog
* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> 4.0.3-alt1
- new version (4.0.3) with rpmgs script

* Mon May 13 2019 Anton Midyukov <antohami@altlinux.org> 4.0.0-alt2
- fix optflags (Closes: 36660)

* Sun Nov 25 2018 Anton Midyukov <antohami@altlinux.org> 4.0.0-alt1
- new version 4.0.0

* Sat Jun 09 2018 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt1.1
- Rebuilt for aarch64

* Thu May 18 2017 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt1
- Initial build for ALT Linux Sisyphus.
