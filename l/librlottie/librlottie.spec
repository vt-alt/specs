# TODO: external rapidjson
# see soname version in CMakeLists.txt
%define soname 0.0.1
Name: librlottie
Version: 0.0.3gitd08a03b
Release: alt1

Summary: A platform independent standalone library that plays Lottie Animation

Group: Networking/Instant messaging
License: Unlicense

Url: https://github.com/john-preston/rlottie
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/john-preston/rlottie.git
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake
 
%description
rlottie is a platform independent standalone c++ library
for rendering vector based animations and art in realtime.

Lottie loads and renders animations and vectors exported
in the bodymovin JSON format.
Bodymovin JSON can be created and exported
from After Effects with bodymovin,
Sketch with Lottie Sketch Export, and from Haiku.

For the first time, designers can create and ship beautiful
animations without an engineer painstakingly recreating it by hand.
Since the animation is backed by JSON they are extremely
small in size but can be large in complexity!

%package devel
Group: Development/Other
Summary: Development files for %name

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_libdir/librlottie-image-loader.so
%_libdir/librlottie.so.0
%_libdir/librlottie.so.%soname

%files devel
%doc COPYING
%_libdir/librlottie.so
%_includedir/rlottie.h
%_includedir/rlottie_capi.h
%_includedir/rlottiecommon.h
%_libdir/cmake/rlottie/
%_pkgconfigdir/rlottie.pc

%changelog
* Fri Aug 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.0.3gitd08a03b-alt1
- build d08a03b6508b390af20491f2dbeee3453594afc8

* Mon Jul 08 2019 Vitaly Lipatov <lav@altlinux.ru> 0.0.2git40ccf08-alt1
- build 40ccf08 (fix Crash when the resource is not a valid lottie resource)

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 0.0.1git8983925-alt1
- initial build for ALT Sisyphus
