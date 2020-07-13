Name: dolphin-emu
Version: 5.0
Release: alt13

Summary: The Gamecube / Wii Emulator
License: GPLv2
Group: Emulators

Url: https://ru.%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

# https://github.com/%name/dolphin/archive/%version/dolphin-%version.tar.gz
Source: dolphin-%version.tar
Patch0: %name-alt-gcc.patch
Patch1: %name-alt-gcc8.patch
Patch2: %name-alt-git.patch
Patch3: %name-alt-soundtouch.patch

BuildPreReq: bzlib-devel
BuildPreReq: libbrotli-devel
BuildPreReq: libexpat-devel
BuildPreReq: libpcre-devel
BuildPreReq: libswresample-devel
BuildPreReq: libuuid-devel

BuildRequires: cmake
BuildRequires: compat-libwxGTK3.1-gtk2-devel
BuildRequires: gcc-c++
BuildRequires: libSFML-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libao-devel
BuildRequires: libavformat-devel
BuildRequires: libbluez-devel
BuildRequires: libcurl-devel
BuildRequires: libenet-devel
BuildRequires: libevdev-devel
BuildRequires: libgtest-devel
BuildRequires: libgtk+2-devel
BuildRequires: liblzo2-devel
BuildRequires: libmbedtls-devel
BuildRequires: libminiupnpc-devel
BuildRequires: libopenal-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsoil-devel
BuildRequires: libsoundtouch-devel
BuildRequires: libswscale-devel
BuildRequires: libudev-devel
BuildRequires: libusb-devel

%description
Dolphin-emu is a emulator for Gamecube, Wii, Triforce that lets
you run Wii/GCN/Tri games on your Windows/Linux/Mac PC system.

%prep
%setup -n dolphin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_SKIP_RPATH:BOOL=TRUE \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DUSE_SHARED_ENET:BOOL=TRUE \
	-DUSE_SHARED_GTEST:BOOL=TRUE \
	-Wno-dev

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man6dir/%{name}*

%changelog
* Fri Jul 03 2020 Nazarov Denis <nenderus@altlinux.org> 5.0-alt13
- Don't gzip sources to sppedup rpmbuild -bp
- Update BuildRequires and BuidPreReq
- Build for aarch64

* Mon Aug 19 2019 Anton Midyukov <antohami@altlinux.org> 5.0-alt12
- add_optflags (pkg-config --cflags pango) (Fix FTBFS)

* Sun Feb 24 2019 Nazarov Denis <nenderus@altlinux.org> 5.0-alt11
- Rebuilt with new SFML

* Tue Jan 15 2019 Nazarov Denis <nenderus@altlinux.org> 5.0-alt10
- Remove %ubt macro

* Sat Jan 12 2019 Nazarov Denis <nenderus@altlinux.org> 5.0-alt9%ubt
- Fix build

* Tue Sep 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0-alt8%ubt
- Rebuilt with compat-libwxGTK3.0-gtk2-devel

* Sun Jul 22 2018 Nazarov Denis <nenderus@altlinux.org> 5.0-alt7%ubt
- Rebuilt with new mbedTLS

* Sun Jun 17 2018 Nazarov Denis <nenderus@altlinux.org> 5.0-alt6%ubt
- Rebuilt with new libva

* Fri Apr 13 2018 Nazarov Denis <nenderus@altlinux.org> 5.0-alt5%ubt
- Rebuilt with new mbedTLS

* Wed Jun 07 2017 Nazarov Denis <nenderus@altlinux.org> 5.0-alt4%ubt
- Rebuilt with ffmpeg instead libav
- Add gcc fix patch

* Tue Nov 01 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt3.1
- Rebuilt with SFML 2.4.0

* Sun Jul 17 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt2.M80P.1
- Build for branch p8

* Sun Jul 17 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt3
- Rebuilt with shared enet and gtest libraries

* Wed Jul 13 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt2
- Version 5.0

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1.rc.1
- rebuilt against libSoundTouch.so.1

* Mon Aug 03 2015 Nazarov Denis <nenderus@altlinux.org> 5.0-alt1.rc
- Version 5.0 RC

* Thu Jul 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt4.git20150715
- New snapshot

* Sat Mar 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt3.git5fafcb6.1
- Rebuilt with wxGTK3.1 (instead of wxGTK3.0) & gtk+3 (gtk+2)

* Wed Sep 17 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt3.git5fafcb6
- Version from git (commit 5fafcb6)
- Rebuild with new polarssl and GLEW

* Tue Apr 22 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt2
- Rebuild with new polarssl

* Sat Feb 01 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Nov 20 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt3
- Rebuild with wxGTK 3.0

* Mon Nov 11 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt2
- Fix build

* Tue Nov 05 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt1
- Initial build for ALT Linux
