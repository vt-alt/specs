%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
%define git 65b787f
%define sovers 0
%def_disable static

Name: libfaudio
Version: 19.09
Release: alt0.1.g%{git}
Summary: Accuracy-focused XAudio reimplementation for open platforms

License: BSD-like
Group: System/Libraries
Url: https://github.com/FNA-XNA/FAudio

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libSDL2-devel libavcodec-devel libavutil-devel libswresample-devel
BuildRequires: gcc-c++ cmake chrpath

Packager: L.A. Kostis <lakostis@altlinux.ru>

%package -n %name%{sovers}
Summary: Accuracy-focused XAudio reimplementation for open platforms
Group: System/Libraries

%package -n %name-devel
Summary: %name development environment
Group: Development/C++
Requires: %name%{sovers} = %EVR

%package -n %name-devel-static
Summary: %name static development environment
Group: Development/C++
Requires: %name-devel = %EVR

%description
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%description -n %name%{sovers}
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%description -n %name-devel
This package contains all files which are needs to compile programs using
the %name library.

%description -n %name-devel-static
This package contains libraries which are needs to compile programs statically
linked against %name library.

%prep
%setup

%build
%_cmake
%cmake_build

%install
%cmakeinstall_std
chrpath -d %buildroot%{_libdir}/*.so.*.*

%files -n %name%{sovers}
%_libdir/*.so.*
%doc README* LICENSE

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/FAudio

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Sep 30 2019 L.A. Kostis <lakostis@altlinux.ru> 19.09-alt0.1.g65b787f
- Initial build for ALTLinux.

