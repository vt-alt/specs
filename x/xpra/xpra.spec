# TODO: python-uinput

Name: xpra
Version: 3.0
Release: alt1

Summary: X Persistent Remote Applications

Group: Networking/Remote access
License: GPLv2
Url: http://xpra.org/

Source: https://xpra.org/src/xpra-%version.tar

# TODO: improve detection
BuildRequires(pre): rpm-build-ubt
%if %ubt_id == "M80P"
%def_with ffmpeg_static
%else
%def_without ffmpeg_static
%endif

BuildRequires: gcc-c++ libXcomposite-devel libXdamage-devel libXrandr-devel libXtst-devel libxkbfile-devel libpam0-devel libsystemd-devel

# TODO use gtk3
BuildRequires: python-module-pygtk-devel python-module-pycairo-devel

# Video
BuildRequires: libvpx-devel libx264-devel libx265-devel libwebp-devel libjpeg-devel libpng-devel libyuv-devel python-module-yuicompressor

%if_with ffmpeg_static
BuildRequires: libffmpeg-devel-static
%else
BuildRequires: libavformat-devel libavcodec-devel libswscale-devel 
%endif


# Sound
BuildRequires: libogg-devel libopus-devel libflac-devel libspeex-devel libvorbis-devel libwavpack-devel liblame-devel libtwolame-devel libmad-devel

# GL
BuildRequires: python-module-pygtkglext python-module-OpenGL python-module-OpenGL_accelerate
Requires: python-module-pygtkglext python-module-OpenGL python-module-OpenGL_accelerate

BuildRequires: python-module-Pillow python-module-websockify

BuildRequires: xorg-server brotli

# See https://bugzilla.altlinux.org/show_bug.cgi?id=28632
BuildPreReq: python-module-Cython >= 0.20

AutoReq: yes, nomingw

%add_python_req_skip win32security pyopencl

BuildRequires(pre): rpm-build-gir rpm-build-intro rpm-macros-kde-common-devel

# Unity specific?
%add_typelib_req_skiplist typelib(AppIndicator) typelib(AppIndicator3) typelib(GtkosxApplication)

# TODO:
%add_typelib_req_skiplist typelib(GdkGLExt) typelib(GtkGLExt)

# Note: we have no linking requires to libwebp.so.x
Requires: libwebp

Requires: xorg-xvfb setxkbmap

Requires: python-module-pyinotify python-module-rencode python-module-lz4

%description
Xpra is 'screen for X': it allows you to run X programs,
usually on a remote host, direct their display to your local machine,
and then to disconnect from these programs and reconnect
from the same or another machine, without losing any state.
It gives you remote access to individual applications.
Xpra is "rootless" or "seamless": programs you run under
it show up on your desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt
to changing network bandwidth limits. (see also adaptive JPEG mode)
Xpra is open-source (GPLv2+), multi-platform and multi-language,
with current clients written in Python and Java.

On the machine which will export the application (xterm in this example):
> xpra start :100 --start-child=xterm

We can then attach to this session from the same machine, with:
> xpra attach :100

If connecting from a remote machine, you would use something like (or you can also use the GUI):
> xpra attach ssh:serverhostname:100


%prep
%setup
%__subst "s|-Werror|-Wall|g" setup.py

# fatal error: pygtk-2.0/pygtk/pygtk.h: No such file or directory
%__subst "s|pygtk-2.0/||g" xpra/x11/gtk2/gdk_display_source.pyx xpra/gtk_common/gtk2/gdk_bindings.pyx

# move systemd service to correct %_unitdir
%__subst "s|/bin/systemctl|NONONO|g" setup.py
%__subst "s|.*/etc/default/xpra.*||g" service/xpra

%build
%if_with ffmpeg_static
export PKG_CONFIG_PATH=%_libdir/ffmpeg-static/%_lib/pkgconfig/
%endif

%python_build --without-mdns

%install
%python_install --without-mdns
mkdir -p %buildroot/%_tmpfilesdir/
mv -f %buildroot/usr/lib/tmpfiles.d/xpra.conf %buildroot/%_tmpfilesdir/
mkdir -p %buildroot%_udevrulesdir/
mv -f %buildroot/usr/lib/udev/rules.d/71-xpra-virtual-pointer.rules %buildroot%_udevrulesdir/
install -m644 -D service/xpra.service %buildroot%_unitdir/%name.service

# TODO
rm -f %buildroot/usr/lib/sysusers.d/xpra.conf

%pre
%_sbindir/groupadd -r -f xpra &>/dev/null ||:

%files
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/*
%_bindir/*
%_libexecdir/%name/
%python_sitelibdir/*
%_desktopdir/*
%_iconsdir/*
%_man1dir/*
#_datadir/parti/
#_datadir/wimpiggy/
%_datadir/xpra/
%_tmpfilesdir/xpra.conf
%_datadir/appdata/xpra.appdata.xml
%_K4xdg_mime/application-x-xpraconfig.xml
%_cupslibdir/backend/xpraforwarder
%_sysconfigdir/%name
%_sysconfdir/pam.d/%name
%_sysconfdir/init.d/%name
%_unitdir/%name.service
%_unitdir/%name.socket
%_udevrulesdir/71-xpra-virtual-pointer.rules
/etc/dbus-1/system.d/xpra.conf
/etc/X11/xorg.conf.d/90-xpra-virtual.conf

%changelog
* Sat Oct 12 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- new version 3.0 (with rpmrb script)

* Thu Sep 26 2019 Vitaly Lipatov <lav@altlinux.ru> 2.5.3-alt1
- new version 2.5.3 (with rpmrb script)

* Tue Jun 18 2019 Vitaly Lipatov <lav@altlinux.ru> 2.5.2-alt1
- new version 2.5.2 (with rpmrb script)

* Wed May 08 2019 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version 2.5.1 (with rpmrb script)

* Mon Mar 11 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt4
- build with OpenGL support (ALT bug 36154)
- disable mdns

* Mon Mar 11 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt3
- allow build with static ffmpeg

* Sun Mar 10 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt2
- cleanup spec
- add python-module-lz4 require

* Sun Feb 10 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version 2.4.3 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt1
- new version 2.3.4 (with rpmrb script)

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- new version 2.3.2 (with rpmrb script)

* Mon Jul 10 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 0.17.6-alt3
- rebuild with ffmpeg

* Wed May 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.17.6-alt2
- add xpra group creating (ALT bug 33459)

* Sun Dec 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.17.6-alt1
- new version 0.17.6 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 0.16.3-alt1
- new version (0.16.3) with rpmgs script

* Wed Mar 09 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.19-alt2
- rebuilt with recent libx264

* Thu Mar 05 2015 Michael Shigorin <mike@altlinux.org> 0.14.19-alt1
- new version

* Wed Sep 24 2014 Vitaly Lipatov <lav@altlinux.ru> 0.14.7-alt1
- new version 0.14.7 (with rpmrb script)

* Mon Jul 07 2014 Vitaly Lipatov <lav@altlinux.ru> 0.13.6-alt1
- new version 0.13.6 (with rpmrb script)
- fix description (ALT bug #30130)
- build without avcodec2

* Mon May 12 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt2
- rebuilt with recent libx264

* Mon Feb 17 2014 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)
- build with Cython 0.20
- build without avcodec

* Fri Feb 14 2014 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Wed Feb 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.6-alt3
- Rebuilt for libwebp5.

* Thu Sep 12 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.6-alt2
- rebuilt with recent libx264

* Thu Jul 11 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- new version 0.9.6 (with rpmrb script)
- rebuild with new libwebp, apply patch to build with old libav

* Sat Dec 08 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.5-alt1
- initial build for Sisyphus

