%define git_version 13817
%define git_commit 72a6fff36c42989c71765012e26285943085b8c5

%add_optflags %optflags_shared

Name: dolphin-emu
Version: 5.0.%git_version
Release: alt0.p9.1

Summary: The Gamecube / Wii Emulator
License: GPLv2
Group: Emulators

Url: https://%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

# https://github.com/%name/dolphin/archive/%git_commit/dolphin-%git_commit.tar.gz
Source: dolphin-%version.tar
Patch0: %name-alt-git.patch

BuildPreReq: pkgconfig(expat)
BuildPreReq: pkgconfig(libbrotlicommon)
BuildPreReq: pkgconfig(libpcre)
BuildPreReq: pkgconfig(uuid)

BuildRequires: cmake
BuildRequires: libcubeb-devel
BuildRequires: libmbedtls-devel
BuildRequires: libminiupnpc-devel
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(fmt) >= 7.1
BuildRequires: pkgconfig(hidapi-libusb)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libenet)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(lzo2)
BuildRequires: pkgconfig(minizip-ng)
BuildRequires: pkgconfig(pugixml)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(sfml-all)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(udev)

%description
Dolphin-emu is a emulator for Gamecube, Wii, Triforce that lets
you run Wii/GCN/Tri games on your Windows/Linux/Mac PC system.

%prep
%setup -n dolphin-%version
%patch0 -p1

%build
%cmake .. \
	-DENABLE_LTO:BOOL=TRUE \
	-DUSE_SHARED_ENET:BOOL=TRUE \
	-DDOLPHIN_WC_DESCRIBE:STRING="%(sed 's|\.|-|2' <<< %version)" \
	-DDOLPHIN_WC_REVISION:STRING="%git_commit" \
	-DDOLPHIN_WC_BRANCH:STRING="master" \
	-DDISTRIBUTOR:STRING="ALT Linux Team" \
	-Wno-dev

%cmake_build

%install
%cmakeinstall_std
%__install -Dp -m0644 Data/51-usb-device.rules %buildroot%_udevrulesdir/51-%name-usb-device.rules
%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/256x256/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man6dir/%{name}*
%config %_udevrulesdir/51-%name-usb-device.rules

%changelog
* Sat Mar 13 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13817-alt0.p9.1
- Build for branch p9 with shared optflags

* Tue Mar 09 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13817-alt1
- Version 5.0-13817

* Wed Feb 17 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13671-alt2
- Enable Link Time Optimization
- Install udev rules for GameCube Controller Adapter, Wiimotes and DolphinBar

* Wed Feb 17 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13671-alt1
- Version 5.0-13671
- Add distributor option

* Sun Feb 14 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13653-alt1
- Version 5.0.13653
- Build with minizip-ng

* Fri Feb 12 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13633-alt1
- Version 5.0-13633
- Use system headers for Vulkan

* Wed Feb 10 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13614-alt2
- Build with cubeb

* Tue Feb 09 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13614-alt1
- Version 5.0-13614

* Sun Jan 24 2021 Nazarov Denis <nenderus@altlinux.org> 5.0-alt16.gitcaff472
- Update to git commit caff472dbf27fbcc5b3d28cbf5b1789592a9f857
- Use minizip from zlib

* Mon Oct 12 2020 Nazarov Denis <nenderus@altlinux.org> 5.0-alt15.git5a939cc
- Rebuit with minizip

* Sun Oct 11 2020 Nazarov Denis <nenderus@altlinux.org> 5.0-alt14.git5a939cc
- Update to git commit 5a939cc (ALT #39062)

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
