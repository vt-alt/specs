%def_with fcitx
%def_with ibus
%def_with nas
%def_with pulse

Name: SDL2
Version: 2.0.10
Release: alt1

Summary: Simple DirectMedia Layer
License: zlib
Group: System/Libraries

Url: http://www.libsdl.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://www.libsdl.org/release/%name-%version.tar.gz

BuildPreReq: libXext-devel
BuildPreReq: libdbus-devel

%{?_with_fcitx:BuildRequires: fcitx-devel}
BuildRequires: gcc-c++
BuildRequires: libGLES-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libalsa-devel
%{?_with_nas:BuildRequires: libaudio-devel}
BuildRequires: libesd-devel
%{?_with_ibus:BuildRequires: libibus-devel}
BuildRequires: libjack-devel
%{?_with_pulse:BuildRequires: libpulseaudio-devel}
BuildRequires: libsamplerate-devel
BuildRequires: libudev-devel

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package -n lib%name
Summary: Simple DirectMedia Layer
Group: System/Libraries

%description -n lib%name
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package -n lib%name-devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C
Conflicts: rpm-build < 4.0.4-alt100.96

%description -n lib%name-devel
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

This is the libraries, include files and other resources you can use
to develop SDL applications.

%prep
%setup

%build
%configure \
    --enable-video-vulkan \
    --enable-video-wayland \
    --disable-static
    
%make_build

%install
%makeinstall_std
%__rm -f %buildroot%_libdir/*.{a,la}

%files -n lib%name
%doc BUGS.txt COPYING.txt CREDITS.txt INSTALL.txt README*.txt TODO.txt WhatsNew.txt
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%_bindir/sdl2-config
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/lib%name.so
%dir %_libdir/cmake
%dir %_libdir/cmake/%name
%_libdir/cmake/%name/sdl2-config.cmake
%_pkgconfigdir/sdl2.pc
%_aclocaldir/sdl2.m4

%changelog
* Thu Aug 29 2019 Alexey Tourbin <at@altlinux.ru> 2.0.10-alt1
- 2.0.9 -> 2.0.10
- this new version is required to build 0ad on ppc64le: SDL_cpuinfo.h
  used to pull in altivec.h whose "vector" conflicts with std::vector

* Thu Mar 07 2019 Nazarov Denis <nenderus@altlinux.org> 2.0.9-alt2
- Add vulkan support (ALT #36246)

* Fri Nov 02 2018 Nazarov Denis <nenderus@altlinux.org> 2.0.9-alt1%ubt
- Version 2.0.9

* Sat Mar 17 2018 Nazarov Denis <nenderus@altlinux.org> 2.0.8-alt2%ubt
- Add wayland support (ALT #34657)

* Sun Mar 11 2018 Nazarov Denis <nenderus@altlinux.org> 2.0.8-alt1%ubt
- Version 2.0.8

* Sun Nov 19 2017 Nazarov Denis <nenderus@altlinux.org> 2.0.7-alt2%ubt
- Disable static libraries

* Thu Oct 26 2017 Nazarov Denis <nenderus@altlinux.org> 2.0.7-alt1%ubt
- Version 2.0.7

* Sun Oct 08 2017 Nazarov Denis <nenderus@altlinux.org> 2.0.6-alt3.M80P.1
- Build for branch p8

* Wed Sep 27 2017 Michael Shigorin <mike@altlinux.org> 2.0.6-alt3%ubt
- introduce ibus, fcitx, nas, pulse knobs (on by default)

* Tue Sep 26 2017 Nazarov Denis <nenderus@altlinux.org> 2.0.6-alt2%ubt
- Change BuildPreReq to BuildRequires(pre) for rpm-build-ubt (ALT #33921)

* Mon Sep 25 2017 Nazarov Denis <nenderus@altlinux.org> 2.0.6-alt1%ubt
- Version 2.0.6

* Wed Nov 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.5-alt2
- Conflicts: rpm-build < 4.0.4-alt100.96 (which adds support for
  RUNPATH) because `sdl2-config --libs` forces new dtags since 2.0.5.

* Mon Oct 31 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.5-alt1
- Version 2.0.5

* Thu Jan 07 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.4-alt0.M70P.1
- Build for branch p7

* Mon Jan 04 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.4-alt0.M70T.1
- Build for branch t7

* Sun Jan 03 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.4-alt1
- Version 2.0.4

* Thu Sep 25 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.3-alt0.M70P.1
- Build for branch p7

* Fri May 16 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.3-alt0.M70T.1
- Build for branch t7

* Sun Mar 23 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.3-alt1
- Version 2.0.3

* Sun Mar 09 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt0.M70T.1
- Build for branch t7

* Sun Mar 09 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Tue Feb 25 2014 Fr. Br. George <george@altlinux.ru> 2.0.1-alt2.1
- Rebuild with pkgconfig fix by new rpm

* Wed Feb 05 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1.M70T.1
- Build for branch t7

* Fri Nov 01 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt2
- Fix post-install unowned files

* Wed Oct 30 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux

