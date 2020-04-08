%define ver_major 0.9.14

Name: compiz
Version: %ver_major.1
Release: alt1

Summary: OpenGL window and compositing manager
License: GPLv2 and LGPLv2 and MIT
Group: System/X11
Url: https://git.launchpad.net/compiz
Packager: Valery Inozemtsev <shrek@altlinux.ru>

#ExclusiveArch: i586 x86_64
Provides: libcompizconfig compiz-fusion-plugins-extra compiz-gtk python-module-compizconfig compiz-gnome
Provides: compiz-fusion-plugins-main compizconfig-backend-gconf ccsm emerald
Obsoletes: libcompizconfig compiz-fusion-plugins-extra compiz-gtk python-module-compizconfig compiz-gnome
Obsoletes: compiz-fusion-plugins-main compizconfig-backend-gconf ccsm emerald

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: boost-devel-headers cmake gcc-c++ intltool libGLU-devel libSM-devel libXcomposite-devel
BuildRequires: libXcursor-devel libXdamage-devel libXi-devel libXinerama-devel libXrandr-devel libdbus-devel
BuildRequires: libglibmm-devel libjpeg-devel libmetacity3.0-devel libnotify-devel libprotobuf-devel librsvg-devel
BuildRequires: libstartup-notification-devel libwnck3-devel libxslt-devel protobuf-compiler xsltproc
BuildRequires: pkgconfig(mate-window-settings-2.0) python3-devel python3-module-Cython
BuildRequires: libpcre-devel libXdmcp-devel libdrm-devel libfribidi-devel libpixman-devel libpng-devel

%description
Compiz is an OpenGL compositing manager that use GLX_EXT_texture_from_pixmap
for binding redirected top-level windows to texture objects. It has a flexible
plug-in system and it is designed to run well on most graphics hardware.

%package -n lib%name
Summary: OpenGL compositing manager library
Group: System/Libraries

%description -n lib%name
OpenGL compositing manager library

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
Development files for %name

%prep
%setup -q
%patch -p1

%build
%define lib_suffix %nil
%if "%_lib" == "lib64"
%define lib_suffix 64
%endif
mkdir -p %_target_platform
pushd %_target_platform
cmake .. \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_CXX_FLAGS_RELEASE='%optflags' \
	-DCOMPIZ_PACKAGING_ENABLED=TRUE \
	-DLIB_SUFFIX=%lib_suffix \
	-DCOMPIZ_BUILD_WITH_RPATH=FALSE \
	-DCOMPIZ_DISABLE_GS_SCHEMAS_INSTALL=OFF \
	-DCOMPIZ_BUILD_TESTING=OFF
popd
find -name flags.make | while read l; do sed -i 's|\ -Werror\ | |g' $l; done
%make_build -C %_target_platform

%install
%make -C %_target_platform DESTDIR=%buildroot install

mkdir -p %buildroot%_sysconfdir/compizconfig
cat << __EOF__ > %buildroot%_sysconfdir/compizconfig/config.conf
[general]
backend = gsettings
profile = mate
integration = true
plugin_list_autosort = true
__EOF__
cat << __EOF__ > %buildroot%_sysconfdir/compizconfig/mate.ini
[core]
s0_active_plugins = core;composite;opengl;decor;matecompat;move;resize;imgpng;wall;session;copytex;compiztoolbox;wobbly;switcher;scale;place;
__EOF__

mkdir -p %buildroot%_datadir/cmake/Modules/%name
mv %buildroot%_datadir/cmake*/Find*.cmake %buildroot%_datadir/cmake/Modules/%name/
rm -f %buildroot%_bindir/compiz-decorator
rm -f %buildroot%python3_sitelibdir_noarch/*.egg-info

%find_lang --output=global.lang %name ccsm

%files -f global.lang
%doc AUTHORS COPYING* README
%dir %_sysconfdir/compizconfig
%config(noreplace) %_sysconfdir/compizconfig/*
%_bindir/*
%python3_sitelibdir_noarch/ccm
%python3_sitelibdir/*.so
%_desktopdir/*.desktop
%_datadir/ccsm
%_datadir/%name
%_datadir/glib-2.0/schemas/*.gschema.xml
%_datadir/gnome-control-center/keybindings/50-compiz-*.xml
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*x*/apps/*.svg
%_iconsdir/hicolor/scalable/apps/*.svg

%files -n lib%name
%_libdir/%name
%_libdir/compizconfig
%_libdir/libcompiz_core.so.*
%_libdir/libdecoration.so.*
%_libdir/libcompizconfig.so.*
%_libdir/libcompizconfig_gsettings_backend.so

%files -n lib%name-devel
%_includedir/%name
%_includedir/compizconfig
%_libdir/libcompiz_core.so
%_libdir/libdecoration.so
%_libdir/libcompizconfig.so
%_pkgconfigdir/*.pc
%_datadir/cmake/Modules/%name

%changelog
* Wed Mar 04 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.9.14.1-alt1
- 0.9.14.1

* Mon Feb 03 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.9.14.0-alt2
- updated build dependencies

* Fri Mar 22 2019 Valery Inozemtsev <shrek@altlinux.ru> 0.9.14.0-alt1
- 0.9.14.0

* Wed Nov 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.9.13.1-alt3
- updated build dependencies

* Tue Oct 02 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.9.13.1-alt2
- updated build dependencies

* Sun Nov 13 2016 Yuri N. Sedunov <aris@altlinux.org> 0.9.13.1-alt1
- 0.9.13.1 (closes: #36338)

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.9.13.0-alt2
- updated to rev.4097
- built against libmetacity.so.1 (metacity-3.22)

* Tue Jul 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.9.13.0-alt1
- 0.9.13.0

* Tue Apr 29 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt12
- gtk/window-decorator: fixed DSO linking against libm.

* Wed Oct 09 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt11
- Fixed build with KDE-4.11.

* Thu Feb 21 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt10
- disable mate too: it requires mateconf

* Tue Feb 19 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt9
- disable mateconf

* Thu Dec 06 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt8
- build for mate
- fix build with kde4.10

* Wed Oct 24 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt7.1
- package libkconfig.so in kde subpackage

* Tue Oct 23 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt7
- fix previous change

* Tue Oct 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.8.8-alt6
- kde3: fixed and packaged kde-window-decorator

* Fri Oct 12 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt5
- update to git.51f4f90
- add kde 4.9 support

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt4.1
- Fixed for build with gcc 4.7
- Rebuilt with libpng15

* Sun May 20 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt4
- fix kde4-window-decorator linking
- fix underlinked plugins

* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt3
- restore compiz in Sisyphus
- disable gnome decorator

* Wed Apr 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt2
- updated to compiz-0.8 git.a24c99c

* Fri Apr 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Tue Nov 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt3
- updated build dependencies

* Sat Oct 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt2
- compiz-0.8 branch 2010-10-10

* Sun Mar 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt4
- disabled KDE 3

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt3
- supported KDE 4.4

* Sat Dec 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt2
- fixed some focus issues
- bumb ABI

* Wed Oct 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Sat Aug 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Thu Aug 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt15
- fixed lag by a call of options

* Tue Aug 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt14
- compiz-0.8 branch 2009-08-15 (aa65a16d3a0b3e40ab5bc717e5a804991b44793a)

* Fri Aug 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt13
- port of KDE4 window decorator to KDE 4.3

* Mon Jul 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt12
- merged compiz-0.8 branch

* Wed Jul 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt11
- build kde4 window decorator (closes: #20713)

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt10
- rebuild with libpng12 1.2.37-alt2

* Thu May 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt9
- added replace option for kde/gtk window-decorator
- sets default plugins

* Thu May 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt8
- compiz-gnome: requires simple-ccsm

* Mon May 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt7
- compiz-kde: fixed startcompiz (closes: #20082)

* Fri Apr 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt6
- compiz-kde: autorun kde-window-decorator

* Tue Apr 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt5
- compiz-gnome: fixed double start if session preservation is included

* Mon Apr 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt4
- oops... renamed compiz.desktop to compiz-wm.desktop

* Mon Apr 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt3
- don't renamed %_desktopdir/compiz.desktop

* Sat Apr 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt2
- enabled gnome

* Sun Mar 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Sat Feb 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Oct 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt2
- added altlinux logo for cube plugin

* Wed Sep 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Wed Sep 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.6-alt2
- rebuild for Mesa-7.1

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Fri Feb 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt5.20080116
- git snapshot 2008-01-16 (256728b9de329bcdbed6d665589082ad8f3bc7e2)

* Tue Nov 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt5
- fix for buffer overflow in strncat

* Tue Nov 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt4
- added %_sysconfdir/X11/wmsession.d/30Compiz to %name-kde

* Wed Nov 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt3
- CVE-2007-3920

* Sat Oct 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt2
- drop compiz-0.5.2-aiglx-defaults.patch: use option "--indirect-rendering"
- rewrite tfp-server-extension patch

* Sun Oct 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Mon Oct 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Sep 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt2
- disable GConf
- updated build dependencies

* Fri Aug 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Mon Apr 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Wed Jan 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Wed Dec 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.3.5-alt1.git20061227
- 0.3.5 2006-12-27 GIT snapshot

* Tue Nov 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.3.3-alt3.git20061101
- added compiz-0.3.3-aiglx-defaults.patch,
	compiz-0.3.3-tfp-server-extension.patch

* Tue Nov 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.3.3-alt2.git20061101
- rename subpackage %name-gnome to %name-gtk
- new subpackage %name-kde, %name-devel

* Mon Nov 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.3.3-alt1.git20061101
- 0.3.3 2006-11-01 GIT snapshot

* Sat Sep 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.13-alt1.git20060901
- merged RH patches
- added ALT Linux logo for cube plugin

* Fri Sep 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.13-alt0.git20060901
- 0.0.13 git snapshot 2006-09-01

* Thu May 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.10-alt0.cvs20060503
- 0.0.10

* Sun Apr 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.9-alt0.cvs20060420
- CVS snapshot 2006-04-20

* Wed Mar 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.7-alt1
- initial release

