%define sover 0
%define cubeb_commit 8942382280721117900072945767cece14eef046
%define sanitizers_cmake_commit aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a

Name: cubeb
Version: 0.2
Release: alt3.git8942382

Summary: A cross platform audio library
License: ISC
Group: System/Libraries

Url: https://github.com/mozilla/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/mozilla/cubeb/archive/%cubeb_commit/%name-%cubeb_commit.tar.gz
Source0: %name-%cubeb_commit.tar
# https://github.com/arsenm/sanitizers-cmake/archive/%sanitizers_cmake_commit/sanitizers-cmake-%sanitizers_cmake_commit.tar.gz
Source1: sanitizers-cmake-%sanitizers_cmake_commit.tar

Patch0: %name-alt-soname.patch

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: libalsa-devel
BuildRequires: libjack-devel
BuildRequires: libpulseaudio-devel

%description
Cubeb is a cross-platform library, written in C/C++, that was created and has
been maintained by the Firefox Media Team.
The role of the library is to communicate with audio devices and to provide
audio input and/or output.

%package -n lib%name%sover
Summary: A cross platform audio library
Group: System/Libraries

%description -n lib%name%sover
Cubeb is a cross-platform library, written in C/C++, that was created and has
been maintained by the Firefox Media Team.
The role of the library is to communicate with audio devices and to provide
audio input and/or output.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
Development files for %name

%prep
%setup -n %name-%cubeb_commit -b 1

%patch0 -p1

%__mv -Tf ../sanitizers-cmake-%sanitizers_cmake_commit cmake/sanitizers-cmake

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DBUILD_TESTS:BOOL=FALSE \
	-Wno-dev

%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS LICENSE
%_bindir/%name-test

%files -n lib%name%sover
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_libdir/cmake/%name
%_libdir/cmake/%name/%{name}*.cmake
%dir %_includedir/%name
%_includedir/%name/%{name}*.h

%changelog
* Fri Feb 26 2021 Nazarov Denis <nenderus@altlinux.org> 0.2-alt3.git8942382
- Build with alsa, jack and pulseaudio

* Fri Feb 26 2021 Nazarov Denis <nenderus@altlinux.org> 0.2-alt2.git8942382
- Update to git 8942382
- Do not build tool

* Wed Feb 10 2021 Nazarov Denis <nenderus@altlinux.org> 0.2-alt1.git8d53747
- Initial build for ALT Linux
