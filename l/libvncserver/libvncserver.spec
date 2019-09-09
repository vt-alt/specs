#set_libtool_version 1.5

%def_disable vaapi

%define tname     LibVNCServer
%define sover 0
%define libvncserver libvncserver%sover
%define libvncclient libvncclient%sover
Name: libvncserver
%define libname %name
Version: 0.9.12
Release: alt2

Group: System/Libraries
Summary: An easy API to write one's own VNC server
Url: https://libvnc.github.io/
License: GPLv2
Packager: Sergey V Turchin <zerg@altlinux.org>

Requires: %libvncserver %libvncclient

Source: http://downloads.sourceforge.net/libvncserver/%tname-%version.tar.gz
# SuSE
Patch20: redef-keysym.patch
Patch21: cmake-libdir.patch

# Automatically added by buildreq on Thu Apr 21 2011 (-bi)
# optimized out: elfutils libX11-devel libgfortran-devel libstdc++-devel xorg-xproto-devel
#BuildRequires: gcc-c++ gcc-fortran glibc-devel-static imake libICE-devel libSDL-devel libjpeg-devel xorg-cf-files zlib-devel
BuildRequires: cmake gcc-c++
BuildRequires:  libICE-devel libSDL2-devel
BuildRequires:  libsystemd-devel
BuildRequires:  libjpeg-devel libpng-devel zlib-devel liblzo2-devel
BuildRequires:  libssl-devel libgcrypt-devel libgnutls-devel
%if_enabled vaapi
BuildRequires: libva-devel
%endif

%description
LibVNCServer makes writing a VNC server (or more correctly, a program
exporting a framebuffer via the Remote Frame Buffer protocol) easy.

It is based on OSXvnc, which in turn is based on the original Xvnc by
ORL, later AT&T research labs in UK.

It hides the programmer from the tedious task of managing clients and
compression schema.

LibVNCServer was put together and is (actively ;-) maintained by
Johannes Schindelin <Johannes.Schindelin@gmx.de>


%package devel
Summary: Headers for developing programs that will use %tname
Group: Development/C
Requires: %libvncserver %libvncclient
%description devel
Headers for developing programs that will use %tname

%package devel-static
Summary: Static libraries for developing programs that will use %tname
Group: Development/C
Requires: %name-devel = %version-%release
%description devel-static
Static libraries for developing programs that will use %tname

%package -n linuxvnc
Summary: VNC server to monitor a text session
Group: Networking/Remote access
Requires: %name = %version-%release
%description -n linuxvnc
With linuxvnc you can export your currently running text sessions to any VNC
client. So it can be useful, if you want to move to another computer without
having to log out and if you've forgotten to attach a 'screen' session to it,
or to help a distant colleague to solve a problem.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%package -n %libvncserver
Summary: %name server library
Group: System/Libraries
%if "%sover" == "0"
Conflicts: libvncserver < %EVR
%endif
%description -n %libvncserver
%name server library

%package -n %libvncclient
Summary: %name client library
Group: System/Libraries
%if "%sover" == "0"
Conflicts: libvncserver < %EVR
%endif
%description -n %libvncclient
%name client library

%prep
%setup -n %tname-%version
%patch20 -p1
%patch21 -p1

# set so version
sed -i 's|^set.*VERSION_SO[[:space:]].*|set(VERSION_SO "%sover")|' CMakeLists.txt
# fix .pc
sed -i 's|@CMAKE_INSTALL_PREFIX@/lib$|@LIB_INSTALL_DIR@|' *.pc.cmakein

%build
%cmake
%cmake_build VERBOSE=1

%install
%make DESTDIR=%buildroot install -C BUILD

%files

%files -n %libvncserver
%doc AUTHORS ChangeLog NEWS README* TODO
%_libdir/libvncserver.so.%sover
%_libdir/libvncserver.so.%sover.*

%files -n %libvncclient
%doc AUTHORS ChangeLog NEWS README* TODO
%_libdir/libvncclient.so.%sover
%_libdir/libvncclient.so.%sover.*

%files devel
%_pkgconfigdir/libvnc*.pc
%_includedir/rfb
%_libdir/lib*.so

#%files -n linuxvnc
#%doc AUTHORS ChangeLog INSTALL NEWS README TODO
#%_bindir/linuxvnc
#%_bindir/LinuxVNC


%changelog
* Fri Aug 30 2019 Sergey V Turchin <zerg@altlinux.org> 0.9.12-alt2
- fix changelog

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 0.9.12-alt1
- new version

* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 0.9.11-alt4
- security (Fixes: CVE-2018-7225)

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt2
- NMU: remove ubt macro from release

* Wed Sep 20 2017 Sergey V Turchin <zerg@altlinux.org> 0.9.11-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.10-alt3
- rebuild with new gnutls

* Wed Jun 24 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.10-alt2
- rebuild with new libgcrypt

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.10-alt1
- new version

* Tue Sep 24 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.9-alt4
- add compatibility symlink to linuxvnc

* Thu Sep 19 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.9-alt3
- fix depends (ALT#29374)

* Wed Sep 18 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.9-alt2
- split libraries

* Wed Sep 18 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.9-alt1
- new version

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.2-alt1.1
- Removed bad RPATH

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.8.2-alt0.M60P.1
- built for M60P

* Tue Dec 13 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.8.2-alt1
- new version

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt3
- fix build requires

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt2.1
- Rebuilt for soname set-versions

* Thu Mar 11 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt1.M51.1
- built for M51

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt2
- add patches from SuSE
- don't build static library

* Wed Apr 29 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt1
- new version
- remove deprecated macroses from specfile

* Tue Mar 18 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9.1-alt1
- initial specfile
- force detect linux
