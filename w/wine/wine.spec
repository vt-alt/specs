%def_enable static
%define gecko_version 2.47.1
%define mono_version 4.9.4
%define major 5.0
%define rel %nil

Name: wine
Version: %major.2
Release: alt1
Epoch: 1

Summary: WINE Is Not An Emulator - environment for running MS Windows 16/32/64 bit applications

License: LGPLv2+
Group: Emulators
Url: https://www.altlinux.org/Wine

Packager: Vitaly Lipatov <lav@altlinux.ru>

# TODO: major in gear

# Source-url: https://dl.winehq.org/wine/source/5.0/wine-%major%rel.tar.xz
Source: %name-%version.tar
# Source1-url: https://github.com/wine-staging/wine-staging/archive/v%major%rel.tar.gz
Source1: %name-staging-%version.tar

Source3: %name-%version-desktop.tar
Source4: %name-%version-icons.tar

# local patches
Source5: %name-patches-%version.tar

AutoReq: yes, noperl

ExclusiveArch: %ix86 x86_64 aarch64

# try build wine64 only on ALT
%if %_vendor == "alt"
%ifarch x86_64 aarch64
	%def_with build64
%else
    %def_without build64
    # skip -fPIC checking (-fnoPIC need in new wine to skip DECLSPEC_HOTPATCH)
    %add_verify_elf_skiplist %_libdir/wine/*.so
    # TODO: use -fPIC for libwine.so.1
    %add_verify_elf_skiplist %_libdir/*.so.*
%endif
%else
   %def_without build64
%endif

# for wine-staging gitapply.sh script
BuildPreReq: /proc

%ifarch aarch64
BuildRequires: clang >= 5.0
%else
BuildRequires: gcc
%endif

# General dependencies
BuildRequires: rpm-build-intro >= 1.0
BuildRequires: util-linux flex bison
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libncurses-devel libncursesw-devel libtinfo-devel
BuildRequires: zlib-devel libldap-devel libgnutls-devel
BuildRequires: libxslt-devel libxml2-devel
BuildRequires: libjpeg-devel liblcms2-devel libpng-devel libtiff-devel
BuildRequires: libgphoto2-devel libsane-devel libcups-devel
BuildRequires: libalsa-devel jackit-devel libgsm-devel libmpg123-devel libpulseaudio-devel
BuildRequires: libopenal-devel libGLU-devel
BuildRequires: libusb-devel libieee1284-devel libpcap-devel libkrb5-devel
BuildRequires: libv4l-devel
BuildRequires: libunixODBC-devel
#BuildRequires: gstreamer-devel gst-plugins-devel
# TODO: opencl-headers (autoimports now), osmesa

# Staging part
# GTK3 theme support: staging only
BuildRequires: libgtk+3-devel
BuildRequires: libva-devel

# udev needed for udev version detect
BuildRequires: libudev-devel udev libdbus-devel

BuildRequires: libICE-devel libSM-devel libxcb-devel
BuildRequires: libX11-devel libXau-devel libXaw-devel libXrandr-devel
BuildRequires: libXext-devel libXfixes-devel libXfont-devel libXft-devel libXi-devel
BuildRequires: libXmu-devel libXpm-devel libXrender-devel
BuildRequires: libXres-devel libXScrnSaver-devel libXinerama-devel libXt-devel
BuildRequires: libXxf86dga-devel libXxf86misc-devel libXcomposite-devel
BuildRequires: libXxf86vm-devel libfontenc-devel libXdamage-devel
BuildRequires: libXvMC-devel libXcursor-devel libXevie-devel libXv-devel

BuildRequires: perl-XML-Simple

# Actually for x86_32
Requires: glibc-pthread glibc-nss

# Enable with can build on x86_64
# GCC v4.4 is needed for build wine64
#ExclusiveArch:  %{ix86}
Requires: webclient

Requires: wine-gecko = %gecko_version
Conflicts: wine-mono < %mono_version

BuildRequires: desktop-file-utils
# Use it instead proprietary MS Core Fonts
# Requires: fonts-ttf-liberation

# For menu/MIME subsystem
Requires: desktop-file-utils

Requires: lib%name = %EVR

Conflicts: wine-vanilla wine-etersoft

Requires: cabextract

# Provides/Obsoletes Fedora packages
%define common_provobs wine-core wine-filesystem wine-common wine-desktop wine-systemd wine-sysvinit
%define base_provobs wine-alsa wine-capi wine-cms wine-ldap wine-openal wine-pulseaudio wine-wow wine-alsa wine-capi wine-cms wine-ldap wine-openal wine-opencl wine-pulseaudio wine-twain
%define fonts_provobs wine-fonts wine-arial-fonts wine-courier-fonts wine-fixedsys-fonts wine-marlett-fonts wine-ms-sans-serif-fonts wine-small-fonts wine-symbol-fonts wine-system-fonts wine-tahoma-fonts wine-times-new-roman-fonts wine-wingdings-fonts
#Provides: %common_provobs %base_provobs %fonts_provobs
Obsoletes: %common_provobs %base_provobs %fonts_provobs


#=========================================================================

%description
Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x and Win32 executables) on Unix. It
consists of a program loader which loads and executes a Microsoft
Windows binary, and a library (called Winelib) that implements Windows
API calls using their Unix or X11 equivalents.  The library may also
be used for porting Win32 code into native Unix executables.

This build based on wine source with wine-staging project patches
and ALT in progress patches.

%package test
Summary: WinAPI test for Wine
Summary(ru_RU.UTF-8): Тест WinAPI для Wine
Group: Emulators
Requires: %name = %EVR
Conflicts: wine-vanilla-test

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

Conflicts: wine-vanilla-full


%description full
Wine meta package. Use it for install all wine subpackages.

%package programs
Summary: Wine programs
Group: Emulators
Requires: %name = %EVR
# due ExclusiveArch
#BuildArch: noarch

Conflicts: wine-vanilla-programs

%description programs
Wine GUI programs:
 * winefile
 * notepad
 * winemine

%package -n lib%name
Summary: Main library for Wine
Group: System/Libraries
Conflicts: libwine-vanilla

# Actually for x86_32
Requires: glibc-pthread glibc-nss

# Runtime linked
Requires: libcups libncurses
Requires: libXrender libXi libXext libX11 libICE
Requires: libssl libgnutls30 libpng16 libjpeg
# Linked:
#Requires: fontconfig libfreetype

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with Wine.

%description -n lib%name -l ru_RU.UTF-8
Этот пакет состоит из библиотек, которые реализуют Windows API.


%package -n lib%name-gl
Summary: DirectX/OpenGL support libraries for Wine
Group: System/Libraries
Requires: lib%name = %EVR
Conflicts: libwine-vanilla-gl

Requires: libGL
# wine-staging only
Requires: libtxc_dxtn

%description -n lib%name-gl
This package contains the libraries for DirectX/OpenGL support in Wine.

%package -n lib%name-twain
Summary: Twain support library for Wine
Group: System/Libraries
Requires: lib%name = %EVR
Conflicts: libwine-vanilla-twain

# Runtime linked (via dl_open)
Requires: libsane

%description -n lib%name-twain
This package contains the library for Twain support.


%package -n lib%name-devel
Summary: Headers for lib%name-devel
Group: Development/C
Requires: lib%name = %EVR
Obsoletes: wine-devel
Provides: wine-devel
Conflicts: libwine-vanilla-devel

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
Conflicts: libwine-vanilla-devel-static

%description -n lib%name-devel-static
lib%name-devel-static contains the static libraries needed to
develop programs which make use of Wine.


%prep
%setup -a 1 -a 5
# Apply wine-staging patches
%name-staging/patches/patchinstall.sh DESTDIR=$(pwd) --all --backend=patch

# disable rpath using for executable
%__subst "s|^\(LDRPATH_INSTALL =\).*|\1|" Makefile.in

# Apply local patches
%name-patches/patchapply.sh

%build
%ifarch aarch64
%remove_optflags -frecord-gcc-switches
export CC=clang
%endif

%configure --with-x \
%if_with build64
	--enable-win64 \
%endif
	--disable-tests \
	--without-gstreamer \
	--without-oss \
	--without-capi \
	--without-hal \
        --without-mingw \
	--with-xattr

%__make depend
%make_build


%install
%makeinstall_std
# unpack desktop files
cd %buildroot%_desktopdir/
tar xvf %SOURCE3
mkdir -p %buildroot%_datadir/desktop-directories/
mv *.directory %buildroot%_datadir/desktop-directories/

# unpack icons files
mkdir -p %buildroot%_iconsdir/
cd %buildroot%_iconsdir/
tar xvf %SOURCE4

# Do not pack non english man pages yet
rm -rf %buildroot%_mandir/*.UTF-8

# Do not pack dangerous association for run windows executables
rm -f %buildroot%_desktopdir/wine.desktop

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

%_bindir/regsvr32
%_bindir/winecfg
%_bindir/regedit
%_bindir/msiexec

%_bindir/wineconsole
%_bindir/wineserver

%_bindir/winedbg
%_bindir/wineboot
%_bindir/winepath
%_libdir/wine/*.exe.so

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
%_libdir/libwine*.so.*
%dir %_libdir/wine/
%_libdir/wine/fakedlls/

%if_without build64
%_libdir/wine/*.dll16.so
%_libdir/wine/*.drv16.so
%_libdir/wine/*.exe16.so
%_libdir/wine/winoldap.mod16.so
%_libdir/wine/*.vxd.so
%endif

%_libdir/wine/*.com.so
%_libdir/wine/*.cpl.so
%_libdir/wine/*.drv.so
%_libdir/wine/*.dll.so
%_libdir/wine/*.acm.so
%_libdir/wine/*.ocx.so
%_libdir/wine/*.tlb.so
%_libdir/wine/*.sys.so

%dir %_datadir/wine/
%_datadir/wine/wine.inf
%_datadir/wine/winebus.inf
%_datadir/wine/winehid.inf
%_datadir/wine/l_intl.nls
%_datadir/wine/fonts/

# move to separate packages
%exclude %_libdir/wine/twain*
%exclude %_libdir/wine/d3d10.dll.so
%exclude %_libdir/wine/d3d8.dll.so
%exclude %_libdir/wine/d3d9.dll.so
%exclude %_libdir/wine/d3dxof.dll.so
%exclude %_libdir/wine/opengl32.dll.so
%exclude %_libdir/wine/glu32.dll.so
%exclude %_libdir/wine/wined3d.dll.so

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
%_libdir/wine/twain*
%_libdir/wine/gphoto2.ds.so
%_libdir/wine/sane.ds.so

%files -n lib%name-gl
%_libdir/wine/d3d10.dll.so
%_libdir/wine/d3d8.dll.so
%_libdir/wine/d3d9.dll.so
%_libdir/wine/d3dxof.dll.so
%_libdir/wine/opengl32.dll.so
%_libdir/wine/glu32.dll.so
%_libdir/wine/wined3d.dll.so

%files -n lib%name-devel
%doc LICENSE LICENSE.OLD
%_bindir/function_grep.pl
%_bindir/winebuild
%_bindir/msidb
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
%_libdir/lib*.so
%_libdir/wine/lib*.def
%_libdir/wine/libwinecrt0.a
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
%_libdir/wine/lib*.a
%exclude %_libdir/wine/libwinecrt0.a
%endif

%changelog
* Wed Jan 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.0.2-alt1
- new version 5.0.2 (with rpmrb script)
- wine 5.0 release

* Sun Jan 19 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.0.1-alt1
- new version (5.0.1) with rpmgs script
- based on wine 5.0-rc6
- update wine-gecko require to 2.47.1

* Mon Nov 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.20.1-alt1
- new version (4.20.1) with rpmgs script
- update patch set
- update wine-mono require to 4.9.4

* Sun Nov 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.19.2-alt1
- improve patchapply.sh, update patches

* Sat Nov 02 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.19.1-alt1
- new version 4.19.1 (with rpmrb script)
- make GetDriveType() always return DRIVE_FIXED for C: (eterbug #14223)

* Sat Oct 19 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.18.1-alt1
- new version 4.18.1 (with rpmrb script)

* Sat Sep 28 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.17.1-alt1
- new version 4.17.1 (with rpmrb script)
- update wine-mono require to 4.9.3

* Sun Sep 15 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.16.1-alt1
- new version 4.16.1 (with rpmrb script)
- wine/debug.h: Make wine_dbgstr_wn use UTF-8 for output (eterbug #14134)
- reapply ntoskrnl.exe: Ignore CProCtrl initialization failure (eterbug #13466)

* Sun Sep 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.15.1-alt1
- new version 4.15.1 (with rpmrb script)

* Sun Aug 04 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.13.1-alt1
- new version 4.13.1 (with rpmrb script)
- use EVR instead of version-release

* Wed Jul 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.12.1.2-alt1
- add patch with cryptext: Implement CryptExtOpenCER

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.12.1.1-alt1
- new version (4.12.1.1) with rpmgs script
- fixe 64 bit build

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.12.1-alt1
- new version 4.12.1 (with rpmrb script)
- enable ExclusiveArch for x86 and aarch64
- remove BR: prelink

* Sat Jun 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.11.1-alt1
- new version 4.11.1 (with rpmrb script)
- strict require wine-mono-4.9.0

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.10.1-alt1
- new version 4.10.1 (with rpmrb script)

* Wed May 29 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.9.1-alt1
- new version 4.9.1 (with rpmrb script)
- strict require wine-mono-4.8.3

* Wed May 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.8.1-alt1
- new version 4.8.1 (with rpmrb script)

* Fri Apr 19 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.6.1-alt1
- new version 4.6.1 (with rpmrb script)
- strict require wine-mono-4.8.1

* Mon Mar 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.4.1-alt1
- new version 4.4.1 (with rpmrb script)
- fix segfault when run wine in a directory with nonlatin letters in their name (ALT bug 36268)

* Tue Mar 05 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.3.1-alt1
- new version (4.3.1) with rpmgs script

* Mon Feb 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.2.1-alt1
- new version 4.2.1 (with rpmrb script)

* Thu Feb 14 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.1.1-alt1
- new version 4.1.1 (with rpmrb script)
- disable file open associations by default (eterbug #13662)

* Wed Jan 23 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.0.1-alt1
- new version 4.0.1 (with rpmrb script)

* Fri Dec 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.21.2-alt1
- ntoskrnl.exe: Ignore CProCtrl initialization failure (eterbug #13466)
- remove "-firstrundlg" parameter from command line for CryptoPro 5.0 installer (eterbug #13466)
- drop version from internal subdirs

* Sun Nov 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.21.1-alt1
- new version 3.21.1 (with rpmrb script)

* Fri Nov 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.19.1-alt1
- new version 3.19.1 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.18.1-alt1
- new version 3.18.1 (with rpmrb script)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.17.1-alt1
- new version 3.17.1 (with rpmrb script)
- use external winetricks

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.13.3-alt1
- ntdll: Don't allow blocking on a critical section during (eterbug #12662)

* Tue Jul 31 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.13.2-alt1
- add patch kernel32: Set environment variable PUBLIC on the process (eterbug #13054)

* Sat Jul 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.13.1-alt1
- new version 3.13.1 (with rpmrb script)

* Fri Jul 13 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.12.1-alt1
- new version 3.12.1 (with rpmrb script)

* Fri Jun 29 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.11.1-alt1
- new version (3.11.1) with rpmgs script
- drop -fno-omit-frame-pointer

* Wed Jun 13 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.10.1-alt1
- new version 3.10.1 (with rpmrb script)
- use clang on aarch64

* Tue May 29 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.9.1-alt1
- new version 3.9.1 (with rpmrb script)

* Fri May 18 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.8.1-alt1
- new version 3.8.1 (with rpmrb script)

* Sat May 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.7.1-alt1
- new version 3.7.1 (with rpmrb script)

* Wed Apr 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.6.1-alt1
- new version 3.6.1 (with rpmrb script)
- fix missed wined3d-csmt.dll (ALT bug 34777)

* Sat Mar 31 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.5.0-alt1
- new version 3.5.0 (with rpmrb script)

* Thu Mar 22 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.4.1-alt1
- new version 3.4.1 (with rpmrb script)

* Mon Mar 05 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.3.1-alt1
- new version (3.3)
- build with winehq 3.3 incorporated Kerberos related code only

* Tue Jan 16 2018 Vitaly Lipatov <lav@altlinux.ru> 1:2.21.3-alt1
- update winetricks up to 20171222
- wine.inf: Add the Kerberos SSP/AP registration

* Thu Jan 11 2018 Vitaly Lipatov <lav@altlinux.ru> 1:2.21.1-alt2
- add the font replacement for Microsoft Sans Serif as Tahoma
- update and rewrite Kerberos related patches

* Thu Nov 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.21.1-alt1
- update winetricks up to 20171018-next
- remove obsoleted patches
- use separated patch list and apply script
- add local_build.sh script

* Fri Nov 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.21.0-alt1
- new version (2.21) with rpmgs script
- update Kerberos patches against wine staging 2.21

* Wed Nov 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.20.2-alt1
- add server APC patches (eterbug #12054, redmine #356)

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.20.1-alt1
- new version (2.20.1) with rpmgs script
- update Kerberos patches against wine staging 2.20

* Wed Oct 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.18.0-alt1
- new version (2.18.0) with rpmgs script
- update Kerberos patches (eterbug #11982)

* Fri Sep 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.17.1-alt1
- add Kerberos SSPI (via GSSIAPI support)

* Fri Sep 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.17.0-alt1
- new version (2.17.0) with rpmgs script

* Mon Sep 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.16.0-alt1
- new version (2.16.0) with rpmgs script
- update winetricks up to 20170823-next
- add dotnet47 support in winetricks

* Sun Aug 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.15.0-alt1
- new version (2.15.0) with rpmgs script

* Tue Aug 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.14.0-alt1
- new version (2.14.0) with rpmgs script
- enable font smoothing by default
- add libpng16, libjpeg requires

* Sun Jul 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.13.0-alt1
- new version (2.13.0) with rpmgs script
- add fix debug output patches

* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.12.0-alt1
- new version 2.12.0 (with rpmrb script)

* Thu Jun 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.11.0-alt1
- new version (2.11.0) with rpmgs script

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.10.1-alt1
- new version (2.10.1) with rpmgs script
- replace RegQueryValueEx HKEY_PERFORMANCE hack with wine-staging one

* Tue May 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.9.1-alt1
- new version (2.9.1) with rpmgs script

* Fri May 26 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.8.1-alt1
- new version 2.8.1 (with rpmrb script)
- update winetricks to 20170517-next

* Fri May 05 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.7.1-alt1
- new version (2.7.1) with rpmgs script

* Sun Apr 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.4.1-alt2
- set Epoche:1 for compatibility
- fix build requires
- add if_enabled static
- add Obsoletes for Fedora packages, fix conflicts with wine-vanilla

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- patches moving:
 + enable linking with freetype and fontconfig
 + add PERF_DATA_BLOCK struct definition
 + add fast hack for RegQueryValueEx-HKEY_PERFORMANCE_DATA_BLOCK
 + make OleLoadPicture load DIBs using WIC decoder

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- initial build wine-staging for ALT Sisyphus
