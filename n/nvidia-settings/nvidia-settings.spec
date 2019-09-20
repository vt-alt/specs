%def_disable translation

Name: nvidia-settings
Version: 430.50
Release: alt1

Group: System/Configuration/Hardware
Summary: Tool for configuring the NVIDIA driver
Url: ftp://download1.nvidia.com/XFree86/nvidia-settings/
License: GPL

Source: %name-%version.tar.gz
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Source4: nvidia-settings.sh
Source5: nvidia-settings.desktop
Source100: gettext.h
Source101: ru.po

Patch1: xlibs.patch
Patch2: cflags.patch
Patch3: alt-ui-modules-dir.patch
Patch4: add-error-popup.patch
Patch100: nvidia-settings-410.73-alt-integrate-translation.patch

# Automatically added by buildreq on Mon May 13 2013 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel libGL-devel libX11-devel libXext-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libwayland-client libwayland-server pkg-config python-base xorg-randrproto-devel xorg-renderproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
#BuildRequires: libXrandr-devel libXv-devel libXxf86vm-devel libgtk+2-devel libvdpau-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-ubt
BuildRequires: libXrandr-devel libXv-devel libXxf86vm-devel libGL-devel libvdpau-devel
BuildRequires: libdbus-devel
BuildRequires: libgtk+2-devel libgtk+3-devel

%description
The `nvidia-settings` utility is a tool for configuring the NVIDIA
Linux graphics driver.  It operates by communicating with the NVIDIA
X driver, querying and updating state as appropriate.  This
communication is done with the NV-CONTROL X extension.

Values such as brightness and gamma, XVideo attributes, temperature,
and OpenGL settings can be queried and configured via nvidia-settings.

When nvidia-settings starts, it reads the current settings from
its configuration file and sends those settings to the X server.
Then, it displays a graphical user interface (GUI) interface for
configuring the current settings.  When nvidia-settings exits, it
queries the current settings from the X server and saves them to
the configuration file.

%package devel
Group: Development/Other
Summary: Development files for %name
Provides: libXNVCtrl-devel = %version-%release
Obsoletes: libXNVCtrl-devel < %version-%release
%description devel
Development files for %name

%prep
%setup -q
#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
%if_enabled translation
mkdir -p po/msg
%patch100 -p2
install -p -m644 %SOURCE100 src/gtk+-2.x/gettext.h
install -p -m644 %SOURCE101 po/msg/ru.po
%endif

sed -i 's|@GUI_LIB_PREFIX@|%_libdir/nvidia-settings|' src/nvidia-settings.c

sed -i -E 's|LIBDIR[[:space:]]+=[[:space:]].*|LIBDIR = $(DESTDIR)$(PREFIX)/%_lib|' utils.mk

%build
%add_optflags %optflags_shared
%make_build PREFIX=%prefix CFLAGS="%optflags" NV_VERBOSE=1 -C src/libXNVCtrl
%make_build PREFIX=%prefix LOCAL_CFLAGS="%optflags" NV_VERBOSE=1


%install
make install DESTDIR=%buildroot PREFIX=%prefix bindir=%buildroot/%_bindir mandir=%buildroot/%_man1dir

#mkdir -p %buildroot/%_bindir
#install -m 0755 nvidia-settings %buildroot/%_bindir

for p in %buildroot/%_libdir/%name/* ; do
    new_path=`echo "$p" | sed 's|\.so\..*|.so|'`
    [ "$p" == "$new_path" ] \
	|| ln -s `basename $p` $new_path
done

mkdir -p %buildroot/%_sysconfdir/X11/xinit.d/
install -m 0755 %SOURCE4 %buildroot/%_sysconfdir/X11/xinit.d/%name.sh

mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
install -m 0644 %SOURCE1 %buildroot/%_iconsdir/hicolor/16x16/apps/%name.png
install -m 0644 %SOURCE2 %buildroot/%_iconsdir/hicolor/32x32/apps/%name.png
install -m 0644 %SOURCE3 %buildroot/%_iconsdir/hicolor/48x48/apps/%name.png

mkdir -p %buildroot/%_desktopdir
install -m 0644 %SOURCE5 %buildroot/%_desktopdir/

mkdir -p %buildroot/%_libdir
install -m 0644 src/_out/Linux_*/libXNVCtrl.a %buildroot/%_libdir/

mkdir -p %buildroot/%_includedir/NVCtrl/
install -m 0644 src/libXNVCtrl/*.h %buildroot/%_includedir/NVCtrl/

%find_lang %name

%files -f %name.lang
%doc doc/*.txt
%_man1dir/%name.*
%_bindir/%name
%_libdir/%name/*gtk3*.so*
%_sysconfdir/X11/xinit.d/%name.sh
%_desktopdir/%name.desktop
%_iconsdir/*/*/apps/%name.png

%files devel
%doc doc/FRAMELOCK.txt doc/NV-CONTROL-API.txt samples/README samples/*.{c,h}
%_includedir/NVCtrl/
%_libdir/*.a

%changelog
* Fri Sep 20 2019 Sergey V Turchin <zerg@altlinux.org> 430.50-alt1
- new version

* Tue Aug 20 2019 Slava Aseev <ptrnine@altlinux.org> 430.40-alt3
- add popup for "Unable to load info" error

* Mon Aug 19 2019 Sergey V Turchin <zerg@altlinux.org> 430.40-alt2
- compile libXNVCtrl with -DPIC (ALT#37118)

* Thu Aug 15 2019 Sergey V Turchin <zerg@altlinux.org> 430.40-alt1
- new version

* Tue Jun 11 2019 Sergey V Turchin <zerg@altlinux.org> 430.26-alt1
- new version

* Thu Mar 14 2019 Sergey V Turchin <zerg@altlinux.org> 410.104-alt1
- new version

* Tue Dec 11 2018 Ivan Razzhivin <underwit@altlinux.org> 410.73-alt3
- add the ability to translate the GUI

* Tue Oct 30 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt2
- obsolete libXNVCtrl-devel

* Tue Oct 30 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt1
- new version

* Mon Apr 02 2018 Sergey V Turchin <zerg@altlinux.org> 390.48-alt1%ubt
- new version

* Thu Feb 15 2018 Sergey V Turchin <zerg@altlinux.org> 390.25-alt1%ubt
- new version

* Mon Jan 22 2018 Sergey V Turchin <zerg@altlinux.org> 384.111-alt1%ubt
- new version

* Mon Dec 04 2017 Sergey V Turchin <zerg@altlinux.org> 384.98-alt1%ubt
- new version

* Wed Oct 11 2017 Sergey V Turchin <zerg@altlinux.org> 384.90-alt1%ubt
- new version

* Wed May 10 2017 Sergey V Turchin <zerg@altlinux.org> 375.66-alt1%ubt
- new version

* Mon Mar 06 2017 Sergey V Turchin <zerg@altlinux.org> 375.39-alt1%ubt
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 375.26-alt1%ubt
- new version

* Thu Dec 01 2016 Sergey V Turchin <zerg@altlinux.org> 375.20-alt1%ubt
- new version

* Mon Jul 18 2016 Sergey V Turchin <zerg@altlinux.org> 367.35-alt1
- new version

* Fri Jul 01 2016 Sergey V Turchin <zerg@altlinux.org> 367.27-alt1
- new version
- build with GTK3

* Fri Apr 22 2016 Sergey V Turchin <zerg@altlinux.org> 361.42-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 361.28-alt1
- new version

* Mon Oct 19 2015 Sergey V Turchin <zerg@altlinux.org> 352.55-alt0.M70P.1
- build for M70P

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 352.55-alt1
- new version

* Fri Sep 04 2015 Sergey V Turchin <zerg@altlinux.org> 352.41-alt0.M70P.1
- built for M70P

* Tue Sep 01 2015 Sergey V Turchin <zerg@altlinux.org> 352.41-alt1
- new version

* Mon Jun 29 2015 Sergey V Turchin <zerg@altlinux.org> 346.82-alt0.M70P.1
- build for M70P

* Mon Jun 29 2015 Sergey V Turchin <zerg@altlinux.org> 346.82-alt1
- new version

* Wed Apr 08 2015 Sergey V Turchin <zerg@altlinux.org> 346.59-alt0.M70P.1
- build for M70P

* Wed Apr 08 2015 Sergey V Turchin <zerg@altlinux.org> 346.59-alt1
- new version

* Tue Mar 10 2015 Sergey V Turchin <zerg@altlinux.org> 346.47-alt0.M70P.1
- build for M70P

* Tue Mar 10 2015 Sergey V Turchin <zerg@altlinux.org> 346.47-alt1
- new version

* Fri Jan 23 2015 Sergey V Turchin <zerg@altlinux.org> 346.35-alt0.M70P.1
- build for M70

* Fri Jan 23 2015 Sergey V Turchin <zerg@altlinux.org> 346.35-alt1
- new version

* Tue Oct 07 2014 Sergey V Turchin <zerg@altlinux.org> 340.46-alt0.M70P.1
- built for M70P

* Mon Oct 06 2014 Sergey V Turchin <zerg@altlinux.org> 340.46-alt1
- new version

* Tue Aug 19 2014 Sergey V Turchin <zerg@altlinux.org> 340.32-alt0.M70P.1
- built for M70P

* Mon Aug 18 2014 Sergey V Turchin <zerg@altlinux.org> 340.32-alt1
- new version

* Mon Jul 21 2014 Sergey V Turchin <zerg@altlinux.org> 340.24-alt0.M70P.1
- built for M70P

* Thu Jul 17 2014 Sergey V Turchin <zerg@altlinux.org> 340.24-alt1
- new version

* Wed Apr 30 2014 Sergey V Turchin <zerg@altlinux.org> 331.67-alt0.M70P.1
- built for M70P

* Wed Apr 30 2014 Sergey V Turchin <zerg@altlinux.org> 331.67-alt1
- new version

* Wed Feb 19 2014 Sergey V Turchin <zerg@altlinux.org> 331.49-alt0.M70P.1
- built for M70P

* Wed Feb 19 2014 Sergey V Turchin <zerg@altlinux.org> 331.49-alt1
- new version

* Tue Jan 14 2014 Sergey V Turchin <zerg@altlinux.org> 331.38-alt0.M70P.1
- built for M70P

* Tue Jan 14 2014 Sergey V Turchin <zerg@altlinux.org> 331.38-alt1
- new version

* Mon Dec 09 2013 Sergey V Turchin <zerg@altlinux.org> 331.20-alt0.M70P.1
- built for M70P

* Mon Dec 09 2013 Sergey V Turchin <zerg@altlinux.org> 331.20-alt1
- new version

* Mon Nov 11 2013 Sergey V Turchin <zerg@altlinux.org> 319.72-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 319.60-alt1
- new version

* Mon Sep 02 2013 Sergey V Turchin <zerg@altlinux.org> 319.49-alt1
- new version

* Wed Jun 26 2013 Sergey V Turchin <zerg@altlinux.org> 319.32-alt1
- new version

* Fri May 24 2013 Sergey V Turchin <zerg@altlinux.org> 319.21-alt1
- new version

* Mon May 13 2013 Sergey V Turchin <zerg@altlinux.org> 319.17-alt2
- fix build requires

* Mon May 13 2013 Sergey V Turchin <zerg@altlinux.org> 319.17-alt1
- new version

* Mon Jan 28 2013 Sergey V Turchin <zerg@altlinux.org> 310.32-alt0.M60P.1
- built for M60P

* Mon Jan 28 2013 Sergey V Turchin <zerg@altlinux.org> 310.32-alt1
- new version

* Thu Nov 22 2012 Sergey V Turchin <zerg@altlinux.org> 310.19-alt0.M60P.1
- built for M60P

* Mon Nov 19 2012 Sergey V Turchin <zerg@altlinux.org> 310.19-alt1
- new version

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 304.64-alt0.M60P.1
- built for M60P

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 304.64-alt1
- new version

* Mon Oct 29 2012 Sergey V Turchin <zerg@altlinux.org> 304.60-alt0.M60P.1
- built for M60P

* Fri Oct 19 2012 Sergey V Turchin <zerg@altlinux.org> 304.60-alt1
- new version

* Wed Oct 03 2012 Sergey V Turchin <zerg@altlinux.org> 304.51-alt0.M60P.1
- built for M60P

* Wed Oct 03 2012 Sergey V Turchin <zerg@altlinux.org> 304.51-alt1
- new version

* Thu Aug 30 2012 Sergey V Turchin <zerg@altlinux.org> 304.43-alt0.M60P.1
- built for M60P

* Thu Aug 30 2012 Sergey V Turchin <zerg@altlinux.org> 304.43-alt1
- new version

* Tue Aug 14 2012 Sergey V Turchin <zerg@altlinux.org> 304.37-alt0.M60P.1
- built for M60P

* Tue Aug 14 2012 Sergey V Turchin <zerg@altlinux.org> 304.37-alt1
- new version

* Thu Jul 12 2012 Sergey V Turchin <zerg@altlinux.org> 302.17-alt1
- new version

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 295.40-alt0.M60P.1
- built for M60P

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 295.40-alt1
- new version

* Wed Feb 15 2012 Sergey V Turchin <zerg@altlinux.org> 295.20-alt0.M60P.1
- built for M60P

* Wed Feb 15 2012 Sergey V Turchin <zerg@altlinux.org> 295.20-alt1
- new version

* Thu Jan 19 2012 Sergey V Turchin <zerg@altlinux.org> 290.10-alt0.M60P.1
- built for M60P

* Thu Jan 19 2012 Sergey V Turchin <zerg@altlinux.org> 290.10-alt1
- new version

* Wed Aug 17 2011 Sergey V Turchin <zerg@altlinux.org> 280.13-alt1
- new version

* Mon Jun 20 2011 Sergey V Turchin <zerg@altlinux.org> 275.09.07-alt1
- new version

* Wed May 25 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.19-alt1
- new version

* Wed Apr 13 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.03-alt1
- new version

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 260.19.29-alt1
- new version

* Fri Oct 15 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt1.M51.1
- built for M51

* Fri Oct 15 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt2
- fix xinit.d script

* Mon Sep 13 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt0.M51.1
- built for M51

* Mon Sep 13 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt1
- new version

* Thu Jul 15 2010 Sergey V Turchin <zerg@altlinux.org> 256.35-alt0.M51.1
- built for M51

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 256.35-alt1
- new version

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.31-alt0.M51.1
- built for M51

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.31-alt1
- new version

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.15-alt0.M51.1
- build for M51

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.15-alt1
- new version

* Thu Feb 04 2010 Sergey V Turchin <zerg@altlinux.org> 190.53-alt0.M51.1
- built for M51

* Thu Feb 04 2010 Sergey V Turchin <zerg@altlinux.org> 190.53-alt1
- new version

* Mon Aug 17 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.31-alt1
- new version
- add HardwareSettings category to desktop file (ALT#20897)

* Fri Jun 26 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.14-alt1
- new version

* Fri Mar 20 2009 Sergey V Turchin <zerg@altlinux.org> 180.29-alt1
- new version

* Mon Feb 02 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt3
- move includes to NVCtrl subdir

* Fri Jan 30 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt2
- package desktop-file instead of menu-file
- package development files

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt1
- new version
- remove deprecated macroses from specfile

* Mon Sep 01 2008 Sergey V Turchin <zerg at altlinux dot org> 177.70-alt1
- new version

* Fri Dec 21 2007 Sergey V Turchin <zerg at altlinux dot org> 169.07-alt1
- new version

* Tue Oct 23 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt1
- new version

* Fri Jun 22 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt7
- update tarball

* Sat Jun 09 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt6
- update tarball

* Fri Oct 13 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt5
- update tarball

* Tue May 23 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt4
- update tarball
- fix build on x86_64 (#9597)

* Tue Apr 11 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt3
- update tarball to 2006-03-17

* Mon Dec 26 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt2
- update tarball

* Fri Jul 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- initial spec

