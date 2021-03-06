%set_verify_elf_method textrel=relaxed

Name: pcsx2
Version: 1.6.0
Release: alt6

Summary: Playstation 2 console emulator
License: GPLv3
Group: Emulators

Url: http://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: %ix86

Source: https://github.com/PCSX2/%name/archive/v%version/%name-%version.tar.gz

BuildRequires(pre): bzlib-devel
BuildRequires(pre): expat-devel
BuildRequires(pre): libbrotli-devel
BuildRequires(pre): libpcre-devel
BuildRequires(pre): libuuid-devel

BuildRequires: cmake
BuildRequires: libwxGTK3.0-devel
BuildRequires: gcc-c++
BuildRequires: libGLU-devel
BuildRequires: libSDL2-devel
BuildRequires: libXmu-devel
BuildRequires: libaio-devel
BuildRequires: libgtk+3-devel
BuildRequires: liblzma-devel
BuildRequires: libpcap-devel
BuildRequires: libportaudio2-devel
BuildRequires: libsoundtouch-devel
BuildRequires: libudev-devel
BuildRequires: libxml2-devel

Requires: %name-i18n = %EVR
Requires: %name-plugin-cdvd
Requires: %name-plugin-dev9
Requires: %name-plugin-firewire
Requires: %name-plugin-graphics
Requires: %name-plugin-pad
Requires: %name-plugin-sound
Requires: %name-plugin-usb

%description
PCSX2 is an emulator for the playstation 2 video game console. It is written mostly in C++, some part are in C and x86 assembly.
There is still lot of on going work to improve compatibility & speed.

%package i18n
Summary: Localization files for PCSX2
Group: Emulators
BuildArch: noarch

%description i18n
Localization files for PCSX2

%package plugin-cdvdnull
Summary: CDVDnull plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-cdvd = %EVR

%description plugin-cdvdnull
CDVDnull plugin for PCSX2

%package plugin-fwnull
Summary: FWnull plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-firewire = %EVR

%description plugin-fwnull
FWnull plugin for PCSX2

%package plugin-gsdx
Summary: GSdx plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-graphics = %EVR

%description plugin-gsdx
GSdx plugin for PCSX2

%package plugin-gsdx-legacy
Summary: GSdx legacy plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-graphics = %EVR

%description plugin-gsdx-legacy
GSdx legacy plugin for PCSX2

%package plugin-usbnull
Summary: USBnull plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-usb = %EVR

%description plugin-usbnull
USBnull plugin for PCSX2

%package plugin-cdvdgigaherz
Summary: cdvdgigaherz plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-cdvd = %EVR

%description plugin-cdvdgigaherz
cdvdgigaherz plugin for PCSX2

%package plugin-dev9ghzdrk
Summary: dev9ghzdrk plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-dev9 = %EVR

%description plugin-dev9ghzdrk
dev9ghzdrk plugin for PCSX2

%package plugin-dev9null
Summary: dev9null plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-dev9 = %EVR

%description plugin-dev9null
dev9null plugin for PCSX2

%package plugin-onepad-legacy
Summary: onepad legacy plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-pad = %EVR

%description plugin-onepad-legacy
onepad legacy plugin for PCSX2

%package plugin-onepad
Summary: onepad plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-pad = %EVR

%description plugin-onepad
onepad plugin for PCSX2

%package plugin-spu2x
Summary: spu2x plugin for PCSX2
Group: Emulators
Requires: %name = %EVR
Provides: %name-plugin-sound = %EVR

%description plugin-spu2x
spu2x plugin for PCSX2

%prep
%setup

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_BUILD_STRIP:BOOL=TRUE \
	-DCMAKE_BUILD_PO:BOOL=TRUE \
	-DPLUGIN_DIR:PATH=%_libdir/%name \
	-DGAMEINDEX_DIR:PATH=%_datadir/%name \
	-DDISABLE_ADVANCE_SIMD:BOOL=TRUE \
	-DPACKAGE_MODE:BOOL=TRUE \
	-DXDG_STD:BOOL=TRUE \
	-DGSDX_LEGACY:BOOL=TRUE \
	-DDISABLE_BUILD_DATE:BOOL=TRUE \
	-DwxWidgets_CONFIG_EXECUTABLE=%_libdir/wx/config/gtk3-unicode-3.0 \
	-DGTK3_API=TRUE \
	-Wno-dev
popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%find_lang --output=%name.lang %{name}_{Iconized,Main}

%files
%_bindir/PCSX2*
%dir %_libdir/%name
%_desktopdir/PCSX2.desktop
%_man1dir/PCSX2.1.*
%dir %_datadir/%name
%_datadir/%name/GameIndex.dbf
%_datadir/%name/cheats_ws.zip
%_pixmapsdir/PCSX2.xpm
%dir %_defaultdocdir/PCSX2
%_defaultdocdir/PCSX2/*.pdf

%files i18n -f %name.lang

%files plugin-cdvdnull
%_libdir/%name/libCDVDnull.so

%files plugin-fwnull
%_libdir/%name/libFWnull-0.7.0.so

%files plugin-gsdx
%_libdir/%name/libGSdx*.so
%exclude %_libdir/%name/libGSdx-legacy*.so

%files plugin-gsdx-legacy
%_libdir/%name/libGSdx-legacy*.so

%files plugin-usbnull
%_libdir/%name/libUSBnull-0.7.0.so

%files plugin-cdvdgigaherz
%_libdir/%name/libcdvdGigaherz.so

%files plugin-dev9ghzdrk
%_libdir/%name/libdev9ghzdrk-0.4.so

%files plugin-dev9null
%_libdir/%name/libdev9null-0.5.0.so

%files plugin-onepad-legacy
%_libdir/%name/libonepad-legacy.so

%files plugin-onepad
%_libdir/%name/libonepad.so

%files plugin-spu2x
%_libdir/%name/libspu2x-2.0.0.so

%changelog
* Sun Oct 11 2020 Anton Midyukov <antohami@altlinux.org> 1.6.0-alt6
- Rebuild with libwxGTK3.0

* Mon Jun 01 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt5
- Use directory /usr/share/doc/PCSX2 for Configuration Guide and Readme / FAQ

* Sun May 24 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt4
- Build GSdx plugin additionaly without AVX2 & SSE4 support
- Build GSdx legacy plugin
- Disable build date

* Sat May 23 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt3
- Move localization files to separate subpackage
- Add requires to all plugin types

* Sat May 23 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt2
- Add build pre requires
- Return XDG_STD option

* Fri May 08 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt1
- Version 1.6.0

* Mon Jul 23 2018 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt2%ubt
- Rebuilt with new GLEW

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1.1
- rebuilt against libSoundTouch.so.1

* Mon Jan 11 2016 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Nov 18 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt2
- Rebuild with libsoundtouch 1.8.0

* Sun Feb 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt0.M70T.1
- Build for branch t7

* Sun Feb 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt1
- Version 1.2.2

* Tue Feb 11 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1.M70P.1
- Build for branch p7

* Mon Feb 10 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1.M70T.1
- Build for branch t7

* Sun Feb 09 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt2
- Fix language files for x64

* Sat Feb 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt0.M70T.1
- Build for branch t7

* Fri Feb 07 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Tue Feb 04 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Thu Oct 17 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1.M70T.1
- Build for branch t7

* Sat Sep 28 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt2
- Fix post-install unowned files
- Rebuild the ps2hw.dat file

* Fri Sep 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux
