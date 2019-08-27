#set_libtool_version 1.5

%def_disable vaapi

%define tname     LibVNCServer
%define vncserver_sover 0
%define libvncserver libvncserver%vncserver_sover
%define vncclient_sover 0
%define libvncclient libvncclient%vncclient_sover
Name: libvncserver
%define libname %name
Version: 0.9.11
Release: alt4

Group: System/Libraries
Summary: An easy API to write one's own VNC server
Url: https://libvnc.github.io/
License: GPLv2
Packager: Sergey V Turchin <zerg@altlinux.org>

Requires: %libvncserver %libvncclient

Source: http://downloads.sourceforge.net/libvncserver/%tname-%version.tar.gz
# FC
Patch11: LibVNCServer-0.9.10-no_x11vnc.patch
Patch12: libvncserver-0.9.1-multilib.patch
Patch13: LibVNCServer-0.9.9-pkgconfig.patch
Patch14: LibVNCServer-0.9.10-system_minilzo.patch
Patch15: libvncserver-0.9.11-soname.patch
# SuSE
Patch20: redef-keysym.patch
Patch21: libvncserver-byteswap.patch
Patch22: libvncserver-0.9.10-ossl.patch
# Debian
Patch31: CVE-2018-7225.patch

# Automatically added by buildreq on Thu Apr 21 2011 (-bi)
# optimized out: elfutils libX11-devel libgfortran-devel libstdc++-devel xorg-xproto-devel
#BuildRequires: gcc-c++ gcc-fortran glibc-devel-static imake libICE-devel libSDL-devel libjpeg-devel xorg-cf-files zlib-devel
BuildRequires: gcc-c++ libICE-devel libSDL-devel libjpeg-devel zlib-devel
BuildRequires: libssl-devel liblzo2-devel libgcrypt-devel libgnutls-devel libpng-devel
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
%if "%vncserver_sover" == "0"
Conflicts: libvncserver < %EVR
%endif
%description -n %libvncserver
%name server library

%package -n %libvncclient
Summary: %name client library
Group: System/Libraries
%if "%vncserver_sover" == "0"
Conflicts: libvncserver < %EVR
%endif
%description -n %libvncclient
%name client library

%prep
%setup -q -n %tname-%version
#%patch11 -p1
%patch12 -p1
#%patch13 -p1
#%patch14 -p1
%patch15 -p1
%patch20 -p1
%patch21 -p0
%patch22 -p0
%patch31 -p1

mkdir -p x11vnc
%autoreconf


%build
%configure \
    --disable-static \
    --enable-shared \
    --with-pic \
    --with-gnu-ld \
    --without-tightvnc-filetransfer \
    --with-gcrypt \
    --with-png \
    --without-x11vnc \
    %{?_enable_vaapi:--with-libva}%{!?_enable_vaapi:--without-libva} \
    #
#sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build


%install
%make DESTDIR=%buildroot install

%files

%files -n %libvncserver
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%_libdir/libvncserver.so.%vncserver_sover
%_libdir/libvncserver.so.%vncserver_sover.*

%files -n %libvncclient
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%_libdir/libvncclient.so.%vncclient_sover
%_libdir/libvncclient.so.%vncclient_sover.*

%files devel
%_pkgconfigdir/libvnc*.pc
%_includedir/rfb
%_libdir/*.so
%_bindir/libvncserver-config

#%files -n linuxvnc
#%doc AUTHORS ChangeLog INSTALL NEWS README TODO
#%_bindir/linuxvnc
#%_bindir/LinuxVNC


%changelog
* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 0.9.11-alt4
- security fixes: CVE-2018-7225

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
