%define _unpackaged_files_terminate_build 1
%def_disable static
%define gecko_version 2.47.2
%define mono_version 6.2.0

%ifarch %{ix86}
%define winepedir i386-windows
%define winesodir i386-unix
%endif
%ifarch x86_64
%define winepedir x86_64-windows
%define winesodir x86_64-unix
%endif
%ifarch %{arm}
%define winepedir arm-windows
%define winesodir arm-unix
%endif
%ifarch aarch64
%define winepedir aarch64-windows
%define winesodir aarch64-unix
%endif

# rpm-build-info gives _distro_version
%if %_vendor == "alt" && (%_distro_version == "p9" || %_distro_version == "Sisyphus")
%def_with vulkan
# vkd3d depends on vulkan
%def_with vkd3d
%def_with faudio
%endif

%def_with opencl

Name: wine-vanilla
Version: 6.12
Release: alt1

Summary: Wine - environment for running Windows applications

License: LGPLv2+
Group: Emulators
Url: http://winehq.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: http://source.winehq.org/git/wine.git
Source: %name-%version.tar
Source2: %name-%version-desktop.tar
Source3: %name-%version-icons.tar

AutoReq: yes, noperl

ExclusiveArch: %ix86 x86_64 aarch64

# try build wine64 only on ALT
%if %_vendor == "alt"
%ifarch x86_64 aarch64
    %def_with build64
    %define winearch wine64
%else
    %def_without build64
    %define winearch wine32
    # skip -fPIC checking (-fnoPIC need in new wine to skip DECLSPEC_HOTPATCH)
    %add_verify_elf_skiplist %_libdir/wine/*.so
    # TODO: use -fPIC for libwine.so.1
    %add_verify_elf_skiplist %_libdir/*.so.*
    # -fPIC is totally disabled for i586
    %add_verify_elf_skiplist %_bindir/*
%endif
%else
   %def_without build64
   %define winearch wine32
%endif

%define libdir %_libdir
%define libwinedir %libdir/wine

%ifarch aarch64
BuildRequires: clang >= 5.0
%else
BuildRequires: gcc
%endif

# General dependencies
BuildRequires(pre): rpm-build-intro >= 2.1.14
BuildRequires: util-linux flex bison
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: zlib-devel libldap-devel libgnutls-devel
BuildRequires: libxslt-devel libxml2-devel
BuildRequires: libjpeg-devel liblcms2-devel libpng-devel libtiff-devel
BuildRequires: libgphoto2-devel libsane-devel libcups-devel
BuildRequires: libalsa-devel jackit-devel libgsm-devel libmpg123-devel libpulseaudio-devel
BuildRequires: libopenal-devel libGLU-devel
BuildRequires: libusb-devel libieee1284-devel libkrb5-devel
BuildRequires: libv4l-devel
BuildRequires: libunixODBC-devel
BuildRequires: libpcap-devel
#BuildRequires: gstreamer-devel gst-plugins-devel

%if_with vulkan
BuildRequires: libvulkan-devel
%endif
%if_with vkd3d
BuildRequires: vkd3d-devel >= 1.2
%endif
%if_with faudio
BuildRequires: libfaudio-devel
%endif

%if_with opencl
BuildRequires: ocl-icd-devel opencl-headers
%endif


# udev needed for udev version detect
BuildRequires: libudev-devel udev libdbus-devel

BuildRequires: libICE-devel libSM-devel
BuildRequires: libX11-devel libXau-devel libXaw-devel libXrandr-devel
BuildRequires: libXext-devel libXfixes-devel libXfont-devel libXft-devel libXi-devel
BuildRequires: libXmu-devel libXpm-devel libXrender-devel
BuildRequires: libXres-devel libXScrnSaver-devel libXinerama-devel libXt-devel
BuildRequires: libXxf86dga-devel libXxf86misc-devel libXcomposite-devel
BuildRequires: libXxf86vm-devel libfontenc-devel libXdamage-devel
BuildRequires: libXvMC-devel libXcursor-devel libXevie-devel libXv-devel

BuildRequires: perl-XML-Simple

# Actually for x86_32
Requires: glibc-nss

Requires: webclient

Requires: wine-gecko = %gecko_version
Conflicts: wine-mono < %mono_version

BuildRequires: desktop-file-utils
# Use it instead proprietary MS Core Fonts
# Requires: fonts-ttf-liberation

# For menu/MIME subsystem
Requires: desktop-file-utils

Requires: lib%name = %EVR

Conflicts: wine wine-etersoft


Requires: cabextract

#=========================================================================

%description
While Wine is usually thought of as a Windows(TM) emulator, the Wine
developers would prefer that users thought of Wine as a Windows
compatibility layer for UNIX. This package includes a program loader,
which allows unmodified Windows binaries to run on x86 and x86_64
Unixes. Wine does not require MS Windows, but it can use native system
.dll files if they are available.

This build uses only winehq upstream sources without any patches.

%package test
Summary: WinAPI test for Wine
Summary(ru_RU.UTF-8): Тест WinAPI для Wine
Group: Emulators
Requires: %name = %EVR
Conflicts: wine-test

%description test
WinAPI test for Wine (unneeded for usual work).
Warning: it may kill your X server suddenly.

%package full
Summary: Wine meta package
Summary(ru_RU.UTF-8): Мета пакет Wine
Group: Emulators
# due ExclusiveArch
#BuildArch: noarch
Requires: %name = %EVR
Requires: %name-programs = %EVR
Requires: lib%name-gl = %EVR

Requires: wine-mono = %mono_version
Requires: wine-gecko = %gecko_version
Requires: winetricks

Conflicts: wine-full

%description full
Wine meta package. Use it for install all wine subpackages.

%package programs
Summary: Wine programs
Group: Emulators
Requires: %name = %EVR
# due ExclusiveArch
#BuildArch: noarch

Conflicts: wine-programs

%description programs
Wine GUI programs:
 * winefile
 * notepad
 * winemine

%package -n lib%name
Summary: Main library for Wine
Group: System/Libraries
Conflicts: libwine

# Actually for x86_32
Requires: glibc-pthread glibc-nss

# Runtime linked
Requires: libcups
Requires: libXrender libXi libXext libX11 libICE
Requires: libXcomposite libXcursor libXinerama libXrandr
Requires: libssl libgnutls30
Requires: libpng16 libjpeg libtiff5

%if_with vulkan
Requires: libvulkan1
%endif

# Recommended
#Requires: libnetapi libunixODBC2 libpcap0.8

Requires: fontconfig libfreetype

# https://lists.altlinux.org/pipermail/devel/2020-November/212533.html
AutoProv: no


%description -n lib%name
This package contains the library needed to run programs dynamically
linked with Wine.

%description -n lib%name -l ru_RU.UTF-8
Этот пакет состоит из библиотек, которые реализуют Windows API.


%package -n lib%name-gl
Summary: DirectX/OpenGL support libraries for Wine
Group: System/Libraries
Requires: lib%name = %EVR
Conflicts: libwine-gl

Requires: libGL

%description -n lib%name-gl
This package contains the libraries for DirectX/OpenGL support in Wine.

%package -n lib%name-twain
Summary: Twain support library for Wine
Group: System/Libraries
Requires: lib%name = %EVR
Conflicts: libwine-twain

%description -n lib%name-twain
This package contains the library for Twain support.


%package -n lib%name-devel
Summary: Headers for lib%name-devel
Group: Development/C
Requires: lib%name = %EVR
#Provides: wine-devel
Conflicts: libwine-devel
# Is it needed?
Provides: libwine-devel = %version-%release

# due winegcc require
Requires: gcc-c++

%description -n lib%name-devel
lib%name-devel contains the header files and some utilities needed to
develop programs using lib%name.

%description -n lib%name-devel -l ru_RU.UTF-8
lib%name-devel содержит файлы для разработки программ, использующих Wine:
заголовочные файлы и утилиты, предназначенные
для компилирования программ с lib%name.

%package -n lib%name-devel-static
Summary: Static libraries for lib%name
Group: Development/C
Requires: lib%name = %EVR
Conflicts: libwine-devel-static

%description -n lib%name-devel-static
lib%name-devel-static contains the static libraries needed to
develop programs which make use of Wine.


%prep
%setup

%build
%ifarch aarch64
%remove_optflags -frecord-gcc-switches
export CC=clang
%endif

%configure --with-x \
%ifarch %{arm} \
 --with-float-abi=hard \
%endif \
%if_with build64
	--enable-win64 \
%endif
	--disable-tests \
	%{subst_enable static} \
	--without-mingw \
	--without-gstreamer \
	%{subst_with vulkan} \
	%{subst_with vkd3d} \
	%{subst_with faudio} \
	%nil

%__make depend
%make_build


%install
%makeinstall_std

mv -v %buildroot%libwinedir/%winesodir/libwine.so.1* %buildroot%libdir

install tools/wineapploader %buildroot%_bindir/wineapploader

# unpack desktop files
cd %buildroot%_desktopdir/
tar xvf %SOURCE2
mkdir -p %buildroot%_datadir/desktop-directories/
mv *.directory %buildroot%_datadir/desktop-directories/

# unpack icons files
mkdir -p %buildroot%_iconsdir/
cd %buildroot%_iconsdir/
tar xvf %SOURCE3

# Do not pack non english man pages yet
rm -rf %buildroot%_mandir/*.UTF-8

# Do not pack dangerous association for run windows executables
rm -f %buildroot%_desktopdir/wine.desktop

%if_disabled static
for i in %buildroot%libwinedir/%winesodir/*.a ; do
    [ "$i" == "%buildroot%libwinedir/%winesodir/libwinecrt0.a" ] && continue
    rm -fv $i
done
%endif

%files
%doc ANNOUNCE AUTHORS LICENSE README
%lang(de) %doc documentation/README.de
%lang(es) %doc documentation/README.es
%lang(fr) %doc documentation/README.fr
%lang(hu) %doc documentation/README.hu
%lang(it) %doc documentation/README.it
%lang(ko) %doc documentation/README.ko
%lang(nb) %doc documentation/README.no
%lang(pt) %doc documentation/README.pt
%lang(pt_BR) %doc documentation/README.pt_br
%lang(tr) %doc documentation/README.tr

%if_without build64
%_bindir/wine
%_bindir/wine-preloader
%else
%_bindir/wine64
%_bindir/wine64-preloader
%endif
%_bindir/wineapploader

%_bindir/regsvr32
%_bindir/winecfg
%_bindir/regedit
%_bindir/msiexec

%_bindir/wineconsole
%_bindir/wineserver

%_bindir/winedbg
%_bindir/wineboot
%_bindir/winepath
%libwinedir/%winesodir/*.exe.so

#%_initdir/wine
#%_initdir/wine.outformat

%_iconsdir/*

%_desktopdir/wine-mime-msi.desktop
%_desktopdir/wine-regedit.desktop
#_desktopdir/wine-serverkill.desktop
%_desktopdir/wine-uninstaller.desktop
%_desktopdir/wine-winecfg.desktop
%_desktopdir/wine-wineconsole.desktop
#_desktopdir/wine-winehelp.desktop

# danger
#_desktopdir/wine.desktop

%_datadir/desktop-directories/*.directory

%if_without build64
%_man1dir/wine.*
%endif
%_man1dir/msiexec.*
%_man1dir/regedit.*
%_man1dir/regsvr32.*
%_man1dir/wineboot.*
%_man1dir/winecfg.*
%_man1dir/wineconsole.*
%_man1dir/winepath.*
%_man1dir/wineserver.*
%_man1dir/winedbg.*

%files -n lib%name
%doc LICENSE AUTHORS COPYING.LIB
# for compatibility only
%libdir/libwine.so.1
%libdir/libwine.so.1.0
%dir %libwinedir/
%dir %libwinedir/%winesodir/
%dir %libwinedir/%winepedir/

%if_without build64
%libwinedir/%winesodir/*.dll16.so
%libwinedir/%winesodir/*.drv16.so
%libwinedir/%winesodir/*.exe16.so
%libwinedir/%winesodir/winoldap.mod16.so
%libwinedir/%winesodir/*.vxd.so
%endif

%libwinedir/%winesodir/ntdll.so
%libwinedir/%winesodir/dnsapi.so
%libwinedir/%winesodir/dwrite.so
%libwinedir/%winesodir/gdi32.so
%libwinedir/%winesodir/user32.so
%libwinedir/%winesodir/bcrypt.so
%libwinedir/%winesodir/qcap.so
%libwinedir/%winesodir/odbc32.so
%libwinedir/%winesodir/windowscodecs.so
%libwinedir/%winesodir/crypt32.so
%libwinedir/%winesodir/kerberos.so
%libwinedir/%winesodir/light.msstyles.so
%libwinedir/%winesodir/netapi32.so
%libwinedir/%winesodir/wldap32.so
%libwinedir/%winesodir/mscms.so
%libwinedir/%winesodir/wmphoto.so
%libwinedir/%winesodir/msv1_0.so
%if_with opencl
%libwinedir/%winesodir/opencl.so
%endif
%libwinedir/%winesodir/secur32.so
%libwinedir/%winesodir/winepulse.so
%libwinedir/%winesodir/wpcap.so
%libwinedir/%winesodir/*.com.so
%libwinedir/%winesodir/*.cpl.so
%libwinedir/%winesodir/*.drv.so
%libwinedir/%winesodir/*.dll.so
%libwinedir/%winesodir/*.acm.so
%libwinedir/%winesodir/*.ocx.so
%libwinedir/%winesodir/*.tlb.so
%libwinedir/%winesodir/*.sys.so
%libwinedir/%winesodir/*.ax.so
%libwinedir/%winepedir/*.com
%libwinedir/%winepedir/*.cpl
%libwinedir/%winepedir/*.drv
%libwinedir/%winepedir/*.dll
%libwinedir/%winepedir/*.acm
%libwinedir/%winepedir/*.ocx
%libwinedir/%winepedir/*.tlb
%libwinedir/%winepedir/*.sys
%libwinedir/%winepedir/*.exe
%libwinedir/%winepedir/*.ax
%libwinedir/%winepedir/*.ds
%libwinedir/%winepedir/light.msstyles
%if_without build64
%libwinedir/%winepedir/*.dll16
%libwinedir/%winepedir/*.drv16
%libwinedir/%winepedir/*.exe16
%libwinedir/%winepedir/winoldap.mod16
%libwinedir/%winepedir/*.vxd
%endif

%dir %_datadir/wine/
%_datadir/wine/wine.inf
%_datadir/wine/nls/
%_datadir/wine/fonts/

# move to separate packages
%exclude %libwinedir/%winesodir/twain_32.dll.so
%exclude %libwinedir/%winepedir/twain_32.dll
%exclude %libwinedir/%winesodir/d3d10.dll.so
%exclude %libwinedir/%winesodir/d3d8.dll.so
%exclude %libwinedir/%winesodir/d3d9.dll.so
%exclude %libwinedir/%winesodir/d3dxof.dll.so
%exclude %libwinedir/%winesodir/opengl32.dll.so
%exclude %libwinedir/%winesodir/glu32.dll.so
%exclude %libwinedir/%winesodir/wined3d.dll.so
%exclude %libwinedir/%winesodir/winevulkan.so

%files full

%files programs
%_bindir/notepad
%_bindir/winefile
%_bindir/winemine
%_man1dir/notepad.*
%_man1dir/winefile.*
%_man1dir/winemine.*
%_desktopdir/wine-notepad.desktop
%_desktopdir/wine-winefile.desktop
%_desktopdir/wine-winemine.desktop


%files -n lib%name-twain
%libwinedir/%winepedir/twain_32.dll
%libwinedir/%winesodir/twain_32.dll.so
%libwinedir/%winesodir/gphoto2.ds.so
%libwinedir/%winesodir/sane.ds.so

%files -n lib%name-gl
%libwinedir/%winesodir/d3d10.dll.so
%libwinedir/%winesodir/d3d8.dll.so
%libwinedir/%winesodir/d3d9.dll.so
%libwinedir/%winesodir/d3dxof.dll.so
%libwinedir/%winesodir/opengl32.dll.so
%libwinedir/%winesodir/glu32.dll.so
%libwinedir/%winesodir/wined3d.dll.so
%libwinedir/%winesodir/winevulkan.so

%files -n lib%name-devel
%doc LICENSE
%_bindir/function_grep.pl
%_bindir/winebuild
%_bindir/wmc
%_bindir/wrc
%_bindir/widl
%_bindir/wineg++
%_bindir/winegcc
%_bindir/winecpp
%_bindir/winedump
%_bindir/winemaker
%_bindir/msidb

%_includedir/wine/
%libwinedir/%winesodir/lib*.def
%libwinedir/%winesodir/libwinecrt0.a
#%_aclocaldir/wine.m4

%_man1dir/wmc.*
%_man1dir/wrc.*
%_man1dir/widl.*
%_man1dir/winebuild.*
%_man1dir/winedump.*
%_man1dir/wineg++.*
%_man1dir/winegcc.*
%_man1dir/winecpp.*
%_man1dir/winemaker.*

%if_enabled static
%files -n lib%name-devel-static
%libwinedir/%winesodir/lib*.a
%exclude %libwinedir/%winesodir/libwinecrt0.a
%endif

%changelog
* Sat Jul 03 2021 Vitaly Lipatov <lav@altlinux.ru> 6.12-alt1
- new version 6.12

* Fri Jun 25 2021 Vitaly Lipatov <lav@altlinux.ru> 6.11-alt2
- fix packing

* Sat Jun 19 2021 Vitaly Lipatov <lav@altlinux.ru> 6.11-alt1
- new version 6.11
- set strict require wine-mono 6.2.0
- build with opencl and pcap

* Sat May 08 2021 Vitaly Lipatov <lav@altlinux.ru> 6.8-alt1
- new version 6.8

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 6.7-alt1
- new version 6.7

* Fri Apr 16 2021 Vitaly Lipatov <lav@altlinux.ru> 6.6-alt1
- new version 6.6

* Sat Mar 27 2021 Vitaly Lipatov <lav@altlinux.ru> 6.5-alt1
- new version 6.5

* Sat Mar 13 2021 Vitaly Lipatov <lav@altlinux.ru> 6.4-alt1
- new version 6.4

* Thu Feb 18 2021 Vitaly Lipatov <lav@altlinux.ru> 6.2-alt1
- new version 6.2
- set strict require wine-mono 6.0.0

* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0-alt1
- new version 6.0
- set strict require wine-gecko 2.47.2

* Sun Nov 22 2020 Vitaly Lipatov <lav@altlinux.ru> 5.22-alt2
- don't provide libwine.so.1 from libwine-vanilla subpackage

* Sat Nov 21 2020 Vitaly Lipatov <lav@altlinux.ru> 5.22-alt1
- new version 5.22

* Mon Nov 16 2020 Vitaly Lipatov <lav@altlinux.ru> 5.21-alt1
- new version 5.21

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 5.20-alt1
- new version 5.20

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 5.19-alt1
- new version 5.19
- add gcc-c++ require to devel package (due winegcc)

* Sun Oct 04 2020 Vitaly Lipatov <lav@altlinux.ru> 5.18-alt3
- move additional files to .gear subdir (drop etersoft dir)
- add Source git URL

* Thu Oct 01 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.18-alt2
- Re-enabled vkd3d support.

* Mon Sep 28 2020 Vitaly Lipatov <lav@altlinux.ru> 5.18-alt1
- new version 5.18
- console no longer requires the curses library
- build with vkd3d disabled (see ALT bug 39002)

* Sat Sep 12 2020 Vitaly Lipatov <lav@altlinux.ru> 5.17-alt1
- new version 5.17
- drop static libs if disabled

* Wed Sep 09 2020 Vitaly Lipatov <lav@altlinux.ru> 5.16-alt3
- just require libvulkan1 as all other libs
- backport small fixes from future biarch build
- sync Requires/Conflicts with wine staging package

* Wed Sep 09 2020 Vitaly Lipatov <lav@altlinux.ru> 5.16-alt2
- build vulkan only for p9 and Sisyphus
- disable static package

* Sun Aug 30 2020 Vitaly Lipatov <lav@altlinux.ru> 5.16-alt1
- new version 5.16

* Fri Aug 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.13-alt2
- Rebuilt with vulkan, vkd3d and faudio support (ALT bug #38810).

* Thu Jul 30 2020 Vitaly Lipatov <lav@altlinux.ru> 5.13-alt1
- new version 5.13

* Sat Jul 04 2020 Vitaly Lipatov <lav@altlinux.ru> 5.12-alt1
- new version 5.12
- set strict require wine-mono 5.1.0

* Sat Jun 06 2020 Vitaly Lipatov <lav@altlinux.ru> 5.10-alt1
- new version 5.10

* Sun May 24 2020 Vitaly Lipatov <lav@altlinux.ru> 5.9-alt1
- new version 5.9

* Sat May 09 2020 Vitaly Lipatov <lav@altlinux.ru> 5.8-alt1
- new version 5.8

* Tue May 05 2020 Vitaly Lipatov <lav@altlinux.ru> 5.7-alt1
- new version 5.7

* Mon Mar 30 2020 Vitaly Lipatov <lav@altlinux.ru> 5.5-alt1
- new version 5.5

* Sat Mar 14 2020 Vitaly Lipatov <lav@altlinux.ru> 5.4-alt1
- new version 5.4

* Sun Mar 01 2020 Vitaly Lipatov <lav@altlinux.ru> 5.3-alt2
- update requires

* Sun Mar 01 2020 Vitaly Lipatov <lav@altlinux.ru> 5.3-alt1
- new version 5.3

* Mon Feb 17 2020 Vitaly Lipatov <lav@altlinux.ru> 5.2-alt1
- new version 5.2

* Tue Feb 04 2020 Vitaly Lipatov <lav@altlinux.ru> 5.1-alt1
- new version 5.1

* Wed Jan 22 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0-alt1
- wine 5.0 release

* Sun Jan 19 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0-alt0.rc6
- pre release 5.0-RC6
- wine-gecko 2.47.1

* Sun Nov 17 2019 Vitaly Lipatov <lav@altlinux.ru> 4.20-alt1
- new version 4.20
- strict require wine-mono 4.9.4

* Sat Nov 02 2019 Vitaly Lipatov <lav@altlinux.ru> 4.19-alt1
- new version 4.19

* Fri Oct 18 2019 Vitaly Lipatov <lav@altlinux.ru> 4.18-alt1
- new version 4.18

* Sat Sep 28 2019 Vitaly Lipatov <lav@altlinux.ru> 4.17-alt1
- new version 4.17

* Sun Sep 15 2019 Vitaly Lipatov <lav@altlinux.ru> 4.16-alt1
- new version 4.16

* Sat Aug 31 2019 Vitaly Lipatov <lav@altlinux.ru> 4.15-alt1
- new version 4.15

* Sat Aug 17 2019 Vitaly Lipatov <lav@altlinux.ru> 4.14-alt1
- new version 4.14

* Sun Aug 04 2019 Vitaly Lipatov <lav@altlinux.ru> 4.13-alt1
- new version 4.13

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 4.12.1-alt1
- new version 4.12.1

* Sat Jul 06 2019 Vitaly Lipatov <lav@altlinux.ru> 4.12-alt1
- new version 4.12, enable ExclusiveArch for x86 and aarch64
- remove BR: prelink

* Sat Jun 22 2019 Vitaly Lipatov <lav@altlinux.ru> 4.11-alt1
- new version 4.11
- strict require wine-mono-4.9.0

* Mon Jun 10 2019 Vitaly Lipatov <lav@altlinux.ru> 4.10-alt1
- new version 4.10

* Mon May 27 2019 Vitaly Lipatov <lav@altlinux.ru> 4.9-alt1
- new version 4.9
- strict require wine-mono-4.8.3

* Mon May 20 2019 Vitaly Lipatov <lav@altlinux.ru> 4.8-alt1
- new version 4.8

* Fri Apr 19 2019 Vitaly Lipatov <lav@altlinux.ru> 4.6-alt2
- strict require wine-mono-4.8.1

* Fri Apr 19 2019 Vitaly Lipatov <lav@altlinux.ru> 4.6-alt1
- new version 4.6

* Mon Mar 18 2019 Vitaly Lipatov <lav@altlinux.ru> 4.4-alt1
- new version 4.4

* Sat Mar 02 2019 Vitaly Lipatov <lav@altlinux.ru> 4.3-alt1
- new version 4.3

* Mon Feb 18 2019 Vitaly Lipatov <lav@altlinux.ru> 4.2-alt1
- new version 4.2

* Sat Feb 09 2019 Vitaly Lipatov <lav@altlinux.ru> 4.1-alt1
- new version 4.1

* Wed Jan 23 2019 Vitaly Lipatov <lav@altlinux.ru> 4.0-alt1
- new version 4.0

* Sat Nov 24 2018 Vitaly Lipatov <lav@altlinux.ru> 3.21-alt1
- new version 3.21

* Sun Nov 11 2018 Vitaly Lipatov <lav@altlinux.ru> 3.20-alt1
- new version 3.20

* Sat Nov 03 2018 Vitaly Lipatov <lav@altlinux.ru> 3.19-alt1
- new version 3.19

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 3.18-alt1
- new version 3.18
- use external winetricks

* Sun Sep 30 2018 Vitaly Lipatov <lav@altlinux.ru> 3.17-alt1
- new version 3.17

* Fri Sep 14 2018 Vitaly Lipatov <lav@altlinux.ru> 3.16-alt1
- new version 3.16

* Fri Aug 31 2018 Vitaly Lipatov <lav@altlinux.ru> 3.15-alt1
- new version 3.15

* Mon Aug 20 2018 Vitaly Lipatov <lav@altlinux.ru> 3.14-alt1
- new version 3.14

* Sat Jul 21 2018 Vitaly Lipatov <lav@altlinux.ru> 3.13-alt1
- new version 3.13

* Tue Jul 10 2018 Vitaly Lipatov <lav@altlinux.ru> 3.12-alt1
- new version 3.12

* Sat Jun 23 2018 Vitaly Lipatov <lav@altlinux.ru> 3.11-alt1
- new version 3.11

* Wed Jun 13 2018 Vitaly Lipatov <lav@altlinux.ru> 3.10-alt1
- new version 3.10
- add runtime linking requires
- use clang on aarch64

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 3.9-alt1
- new version 3.9

* Sat May 12 2018 Vitaly Lipatov <lav@altlinux.ru> 3.8-alt1
- new version 3.8

* Sat Apr 28 2018 Vitaly Lipatov <lav@altlinux.ru> 3.7-alt1
- new version 3.7

* Sat Apr 21 2018 Vitaly Lipatov <lav@altlinux.ru> 3.6-alt1
- new version 3.6

* Sat Mar 31 2018 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt1
- new version 3.5

* Mon Mar 19 2018 Vitaly Lipatov <lav@altlinux.ru> 3.4-alt1
- new version 3.4

* Sat Mar 03 2018 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt1
- new version 3.3

* Mon Feb 19 2018 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt1
- new version 3.2

* Fri Feb 02 2018 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version 3.1

* Fri Jan 19 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- new version 3.0
- update winetricks up to 20171222

* Sat Nov 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.22-alt1
- new version 2.22

* Sat Nov 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.21-alt1
- new version 2.21

* Thu Nov 02 2017 Vitaly Lipatov <lav@altlinux.ru> 2.20-alt1
- new version 2.20

* Mon Oct 16 2017 Vitaly Lipatov <lav@altlinux.ru> 2.19-alt1
- new version 2.19

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 2.18-alt1
- new version 2.18

* Fri Sep 15 2017 Vitaly Lipatov <lav@altlinux.ru> 2.17-alt1
- new version 2.17
- update winetricks to 20170823

* Sat Sep 02 2017 Vitaly Lipatov <lav@altlinux.ru> 2.16-alt1
- new version 2.16

* Sun Aug 20 2017 Vitaly Lipatov <lav@altlinux.ru> 2.15-alt1
- new version 2.15

* Thu Aug 03 2017 Vitaly Lipatov <lav@altlinux.ru> 2.14-alt1
- new version 2.14

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.13-alt1
- new version 2.13

* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt1
- new version 2.12

* Sun Jun 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.11-alt1
- new version 2.11

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.10-alt1
- new version 2.10

* Sat May 27 2017 Vitaly Lipatov <lav@altlinux.ru> 2.9-alt1
- new version 2.9
- update winetricks to 20170517-next

* Sat May 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.8-alt1
- new version 2.8

* Sat Apr 29 2017 Vitaly Lipatov <lav@altlinux.ru> 2.7-alt1
- new version 2.7

* Sat Apr 15 2017 Vitaly Lipatov <lav@altlinux.ru> 2.6-alt1
- new version 2.6

* Sun Apr 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt2
- update winetricks to 20170327
- add default icons (ALT bug 25237)

* Sat Apr 01 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt1
- new version 2.5

* Fri Mar 17 2017 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version 2.4

* Sat Mar 04 2017 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- new version 2.3

* Sun Feb 19 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- new version 2.2

* Thu Jan 26 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- new version 2.0

* Thu Dec 01 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.24-alt1
- new version 1.9.24

* Tue Nov 15 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.23-alt1
- new version 1.9.23

* Sun Oct 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.22-alt1
- new version 1.9.22

* Fri Oct 21 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.21-alt3
- pack desktop files for programs to wine-vanilla-programs
- do not pack wine.desktop for protect from suddenly running from GUI

* Thu Oct 20 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.21-alt2
- split wine-vanilla-programs subpackage (ALT bug #32587)

* Sat Oct 15 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.21-alt1
- new version 1.9.21

* Thu Oct 06 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.20-alt1
- new version 1.9.20

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.19-alt1
- new version 1.9.19

* Sat Sep 03 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.18-alt1
- new version 1.9.18

* Fri Sep 02 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.17-alt2
- add wine and libwine-devel provides

* Sun Aug 21 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.17-alt1
- new version 1.9.17

* Thu Aug 18 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.16-alt1
- new version 1.9.16 (requires wine-gecko = 2.47 since 1.9.13)
- update winetricks to 20160724

* Thu Jun 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.12-alt1
- new version 1.9.12

* Sat May 28 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.11-alt1
- new version 1.9.11

* Fri May 20 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.10-alt1
- new version 1.9.10

* Tue Apr 05 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.7-alt1
- new version 1.9.7

* Fri Mar 18 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.6-alt1
- new version 1.9.6

* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt2
- fix packing issues
- make wine-vanilla-full noarch
- add libpulseaudio-devel buildreq

* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt1
- new version 1.9.4 (requires wine-gecko = 2.44)

* Tue Jan 12 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version 1.9.1

* Sat Dec 12 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt0rc4
- new version 1.8-rc4

* Tue Dec 01 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt0rc2
- new version 1.8-rc2

* Sun Nov 22 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt0rc1
- new version 1.8-rc1

* Fri Oct 30 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.54-alt1
- new version 1.7.54

* Sat Oct 17 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.53-alt1
- new version 1.7.53, requires wine-gecko = 2.40

* Mon Aug 10 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.49-alt1
- new version 1.7.49

* Wed Jul 22 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.47-alt2
- add requires to wine-mono and wine-gecko to full subpackage (closes: #31149)

* Mon Jul 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.47-alt1
- new version 1.7.47

* Mon Jun 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.45-alt1
- new version 1.7.45

* Thu Jun 04 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.44-alt1
- new version 1.7.44

* Tue May 26 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.43-alt2
- add unixODBC-devel buildreq (closes: #31024)
- add cabextract require (closes: #31024)
- add wine-vanilla-full package (closes: #31024)

* Tue May 19 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.43-alt1
- new version 1.7.43
- build with liblcms2 (closes: #31006)
- build without gstreamer (closes: #31014)

* Sat May 02 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.42-alt1
- new version 1.7.42

* Sun Apr 05 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.40-alt1
- new version 1.7.40

* Wed Apr 01 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.39.gdbf8bde-alt1
- build against commit dbf8bde14616e54abbcf4caca92d4b708170b0ac

* Fri Mar 27 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.39-alt1
- new version 1.7.39

* Mon Mar 09 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.38-alt1
- new version 1.7.38, requires wine-gecko = 2.36

* Fri Feb 20 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.37-alt1
- new version 1.7.37

* Sun Feb 08 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.36-alt1
- new version 1.7.36

* Fri Feb 06 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.35-alt2
- rebuild with new libgphoto2

* Sat Jan 24 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.35-alt1
- new version 1.7.35

* Wed Jan 14 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.34-alt1
- new version 1.7.34

* Sat Dec 13 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.33-alt1
- new version 1.7.33, requires wine-gecko = 2.34

* Mon Nov 10 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.30-alt1
- new version 1.7.30

* Tue Oct 21 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.29-alt1
- new version 1.7.29

* Sat Oct 11 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.28-alt2
- update winetricks to 20140302 (ALT bug #30382)

* Mon Oct 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.28-alt1
- new version 1.7.28

* Fri Sep 19 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.27-alt1
- new version 1.7.27

* Sat Sep 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.26-alt1
- new version 1.7.26

* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.25-alt1
- new version 1.7.25

* Fri Jul 25 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.23-alt1
- new version 1.7.23

* Mon Jul 14 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.22-alt1
- new version 1.7.22

* Tue Jul 08 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.21-alt1
- new version 1.7.21

* Sun May 18 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.19-alt1
- new version 1.7.19

* Mon May 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.18-alt1
- new version 1.7.18 (ALT bug #30054)

* Sat Apr 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.16-alt1
- new version 1.7.16

* Sat Mar 22 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.15-alt1
- new version 1.7.15

* Fri Mar 14 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.14-alt1
- new version 1.7.14

* Sat Oct 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- new version 1.7.5

* Mon Oct 14 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- new version 1.7.4

* Sat Sep 14 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2

* Fri Aug 02 2013 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- release 1.6
- remove libssl-devel requires

* Sun Jun 30 2013 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt0.rc4
- new version 1.6-rc4

* Sat Jun 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt0.rc3
- new version 1.6-rc3, requires wine-gecko 2.21

* Tue Feb 19 2013 Vitaly Lipatov <lav@altlinux.ru> 1.5.24-alt1
- new version 1.5.24

* Wed Feb 06 2013 Vitaly Lipatov <lav@altlinux.ru> 1.5.23-alt1
- new version 1.5.23, requires wine-gecko 1.9

* Sat Dec 22 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.20-alt1
- new version 1.5.20, requires wine-gecko 1.8
- remove libhal-devel buildreq

* Mon Sep 17 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.13-alt2
- restore missed-in-merge changes

* Sat Sep 15 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.13-alt1
- new version 1.5.13, cleanup spec
- disable libesd support and requires

* Fri Sep 07 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.12-alt1
- new version 1.5.12

* Wed Aug 01 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.10-alt1
- new version 1.5.10, requires wine-gecko 1.7

* Sat Jul 14 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.8-alt1
- new version 1.5.8

* Mon May 28 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt2
- fix wine-gecko requires to 1.5

* Sat May 26 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt1
- new version 1.5.5

* Fri Mar 09 2012 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0
- update winetricks to 20120308
- fix requires

* Sat Jan 14 2012 Vitaly Lipatov <lav@altlinux.ru> 1.3.37-alt1
- new version 1.3.37

* Sat Dec 31 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.36-alt1
- new version 1.3.36

* Sat Dec 17 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.35-alt1
- new version 1.3.35
- update winetricks to 20111115

* Tue Dec 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.34-alt1
- new version 1.3.34, use wine-gecko 1.4

* Sat Nov 05 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.32-alt1
- new version 1.3.32

* Tue Nov 01 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.31-alt1
- new version 1.3.31
- update winetricks to 20110629

* Tue Oct 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.30-alt1
- new version 1.3.30

* Fri Aug 26 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.27-alt1
- new version 1.3.26, use wine-gecko 1.3

* Mon Aug 22 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.26-alt1
- new version 1.3.26
- drop out winehelp desktop file

* Thu Jun 02 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.21-alt1
- new version 1.3.21

* Fri Apr 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.19-alt1
- new version 1.3.19

* Sun Apr 17 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.18-alt1
- new version 1.3.18

* Mon Apr 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.17-alt2
- fix build requires (add missed libtiff-devel, gstreamer plugin base, libgnutls-devel)

* Sat Apr 02 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.17-alt1
- new version 1.3.17
- again winetricks: do not use zenity/kdialog via direct run (ALT bug 24838)
- add libncurses requires

* Wed Mar 30 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt3
- drop xorg-x11-proto-devel buildreqs
- pack all man files

* Tue Mar 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt2
- winetricks: update to 20110324
- winetricks: do not use zenity/kdialog via direct run (ALT bug 24838)

* Sat Mar 19 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt1
- new version 1.3.16
- update winetricks to 20110318
- require wine-gecko 1.2.0
- add some desktop files for menu (ALT bug 25237)

* Thu Dec 30 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3.10-alt2
- winetricks: use detected MENU instead direct command (ALT bug 24838)

* Mon Dec 27 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3.10-alt1
- new version 1.3.10 (ALT bug 24273)

* Fri Jul 16 2010 Ilya Shpigor <elly@altlinux.org> 1.2_rc7-alt1
- new version 1.2-rc7

* Mon Jun 14 2010 Ilya Shpigor <elly@altlinux.org> 1.2_rc3-alt1
- new version 1.2-rc3

* Mon May 31 2010 Ilya Shpigor <elly@altlinux.org> 1.2_rc2-alt1
- new version 1.2-rc2

* Tue May 25 2010 Ilya Shpigor <elly@altlinux.org> 1.1.44-alt3
- fix build for x86_64 architecture (try 2)

* Fri May 14 2010 Ilya Shpigor <elly@altlinux.org> 1.1.44-alt2
- fix build for x86_64 architecture

* Tue May 11 2010 Ilya Shpigor <elly@altlinux.org> 1.1.44-alt1
- new version 1.1.44

* Mon Apr 19 2010 Ilya Shpigor <elly@altlinux.org> 1.1.43-alt1
- new version 1.1.43

* Mon Apr 05 2010 Ilya Shpigor <elly@altlinux.org> 1.1.42-alt1
- new version 1.1.42

* Mon Mar 22 2010 Ilya Shpigor <elly@altlinux.org> 1.1.41-alt1
- new version 1.1.41

* Sat Mar 06 2010 Ilya Shpigor <elly@altlinux.org> 1.1.40-alt1
- new version 1.1.40

* Sun Feb 21 2010 Ilya Shpigor <elly@altlinux.org> 1.1.39-alt1
- new version 1.1.39

* Mon Feb 08 2010 Ilya Shpigor <elly@altlinux.org> 1.1.38-alt1
- new version 1.1.38

* Mon Jan 25 2010 Ilya Shpigor <elly@altlinux.org> 1.1.37-alt1
- new version 1.1.37

* Mon Jan 18 2010 Ilya Shpigor <elly@altlinux.org> 1.1.36-alt2
- add winetricks to wine-vanilla package (fix altbug #22650)

* Sat Jan 16 2010 Ilya Shpigor <elly@altlinux.org> 1.1.36-alt1
- new version 1.1.36

* Fri Jan 08 2010 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt4
- fix conflict libwine-vanilla-devel-static with libwine-devel

* Wed Jan 06 2010 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt3
- don't build libwine-vanilla-devel-doc package

* Wed Jan 06 2010 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt2
- build the libwine-vanilla-devel-doc package as the architecture-independent

* Fri Dec 25 2009 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt1
- new version 1.1.35

* Fri Dec 25 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.34-alt2
- enable build for x86_64 (fix altbug #10042)

* Fri Dec 11 2009 Ilya Shpigor <elly@altlinux.org> 1.1.34-alt1
- new version 1.1.34

* Tue Nov 24 2009 Ilya Shpigor <elly@altlinux.org> 1.1.33-alt1
- new version 1.1.33

* Sat Oct 24 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.32-alt1
- new version 1.1.32

* Sat Aug 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt2
- fix services.exe crash (altbug #20927)

* Fri Jul 24 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt1
- new version 1.1.26

* Thu Jul 23 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.25-alt1
- new version 1.1.25

* Tue Jun 30 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.24-alt1
- new version 1.1.24

* Tue May 26 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.22-alt1
- new version 1.1.22

* Sat May 09 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.21-alt1
- new version 1.1.21

* Sat Mar 28 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.18-alt1
- new version 1.1.18

* Fri Mar 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.17-alt1
- new version 1.1.17

* Sat Feb 28 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.16-alt1
- new version 1.1.16

* Sun Feb 15 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.15-alt1
- new version 1.1.15

* Fri Feb 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version 1.1.14

* Sat Jan 17 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt1
- new version 1.1.13

* Tue Jan 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.12-alt1
- merge with upstream (1.1.12)

* Fri Dec 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.11-alt1
- merge with upstream (1.1.11)
- add libhal-devel buildreq

* Fri Nov 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.9-alt1
- merge with upstream (1.1.9)

* Sat Nov 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt1
- merge with upstream (1.1.8)

* Sat Nov 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt2
- rebuild configure
- remove autoconf due too old autoconf in ALT 4.0

* Wed Oct 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt1
- merge with upstream (1.1.7)
- add autoconf -f due strange configure

* Fri Sep 19 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt1
- merge with upstream (1.1.5)
- revert to original sources from git://source.winehq.org/git/wine.git

* Wed Jul 16 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- merge with upstream (1.1.1)
- cleanup spec, return update_menus
- fix altbug #16230 again (run init functions from linked libs)

* Tue Jul 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- merge with upsteam
- link gdi32 with freetype/fontconfig directly (fix altbug #16230)
- disable RPATH for installed libs (LDRPATH_INSTALL=)

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build from vanilla source for ALT Linux Sisyphus
