%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 1.22
%define beta %nil
%define gst_api_ver 1.0
%define wayland_ver 1.11.0

%def_enable multisense
%def_enable fb
# fb requires tslib?
%def_disable tslib
%def_enable drm
%def_enable ibus
%def_enable gstreamer1
%def_enable emotion
%def_enable elogind

%def_enable wayland
# wayland requires elput and drm
%def_enable elput
%def_enable wayland_egl
%def_disable egl
# currently with GLES only
%def_disable gl_drm

# aarch64 with luajit-2.1-alt6: PANIC: unprotected error in call to Lua API (bad light userdata pointer)
%ifarch aarch64
%def_disable elua
%else
%def_enable elua
%endif

%ifnarch %e2k
%def_enable lua
%define _unpackaged_files_terminate_build 1
%endif

Name: efl
Version: %ver_major.4
Release: alt1

Summary: Enlightenment Foundation Libraries
License: BSD/LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

%if_disabled snapshot
Source: https://download.enlightenment.org/rel/libs/%name/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: efl-1.15.0-alt-ecore_fb.patch
Patch1: efl-1.19.1-luajitfix.patch

# to skip libreoffice dependency for evas_generic_loaders
%add_findreq_skiplist %_libdir/evas/utils/evas_generic_pdf_loader.libreoffice
#Requires: LibreOffice

%{?_enable_static:BuildPreReq: glibc-devel-static}
BuildRequires: gcc-c++ glibc-kernheaders glib2-devel libcheck-devel lcov doxygen
BuildRequires: libpng-devel libjpeg-devel libopenjpeg2.0-devel libtiff-devel libgif-devel libwebp-devel
BuildRequires: fontconfig-devel libfreetype-devel libfribidi-devel libharfbuzz-devel
BuildRequires: libpulseaudio-devel libsndfile-devel libbullet-devel zlib-devel liblz4-devel
BuildRequires: libssl-devel libcurl-devel libdbus-devel
BuildRequires: libmount-devel libblkid-devel
BuildRequires: libudev-devel systemd-devel libsystemd-journal-devel libsystemd-daemon-devel
BuildRequires: libX11-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXext-devel
BuildRequires: libXfixes-devel libXinerama-devel libXrandr-devel libXrender-devel libXScrnSaver-devel
BuildRequires: libXtst-devel libXcursor-devel libXp-devel libXi-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libGL-devel

%ifarch %e2k
%{?_enable_lua:BuildRequires: liblua5.1-devel}
# FIXME: lua is broken, elua won't be built but we need it to pass configure
BuildRequires: liblua5.1-devel
%else
# 20171106: not ported to e2k yet
%{?_enable_lua:BuildRequires: libluajit-devel}
BuildRequires: libunwind-devel
%endif
%{?_enable_ibus:BuildRequires: libibus-devel}
%{?_enable_tslib:BuildRequires: libts-devel}
%{?_enable_wayland:BuildRequires: libwayland-client-devel >= %wayland_ver libwayland-server-devel libwayland-cursor-devel wayland-protocols libxkbcommon-devel >= 0.6.0 libuuid-devel}
%{?_enable_wayland_egl:BuildRequires: libwayland-egl-devel}
%{?_enable_egl:BuildRequires: libEGL-devel libwayland-egl-devel}
%{?_enable_gstreamer1:BuildRequires: gst-plugins%gst_api_ver-devel}
%{?_enable_drm:BuildRequires: libdrm-devel libgbm-devel libinput-devel}
#%{?_enable_gl_drm:BuildRequires:}
# for elementary
BuildRequires: /proc dbus-tools-gui doxygen /usr/bin/convert
# for emotion_generic_players
%{?_enable_emotion:BuildRequires: libvlc-devel >= 2.0}
# for evas_generic_loaders
BuildRequires: libpoppler-cpp-devel
BuildRequires: libspectre-devel
BuildRequires: librsvg-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: zlib-devel
BuildRequires: libraw-devel libgomp-devel
%{?_enable_elogind:BuildRequires: libelogind-devel}

%description
EFL is a collection of libraries for handling many common tasks a
developer may have such as data structures, communication, rendering,
widgets and more.

There are many components inside EFL. They also build various things
like shared libraries, loadable plug-in modules and also binary
executables.

For more doumentation please see:

http://www.enlightenment.org/p.php?p=docs

%package -n %name-libs
Summary: Enlightenment Foundation Libraries
Group: System/Libraries
Obsoletes: libeina < %version
Provides: libeina = %version-%release
Obsoletes: libeet < %version
Provides: libeet = %version-%release
Obsoletes: libevas < %version
Provides: libevas = %version-%release
Obsoletes: libecore < %version
Provides: libecore = %version-%release
Obsoletes: edje < %version
Provides: edje = %version-%release
Obsoletes: libedje < %version
Provides: libedje = %version-%release
Obsoletes: libeeze < %version
Provides: libeeze = %version-%release
Obsoletes: eeze < %version
Provides: eeze = %version-%release
Obsoletes: libembryo < %version
Provides: libembryo = %version-%release
Obsoletes: libeio < %version
Provides: libeio = %version-%release
Obsoletes: libefreet < %version
Provides: libefreet = %version-%release
Obsoletes: libethumb < %version
Provides: libethumb = %version-%release
Obsoletes: libemotion < %version
Provides: libemotion = %version-%release
Provides: libeo = %version-%release
Provides: libephysics = %version-%release
Provides: libeldbus = %version-%release
# since 1.18
Obsoletes: evas_generic_loaders < 1.18
Obsoletes: emotion_generic_players < 1.18
Provides: evas_generic_loaders = %version-%release
Provides: emotion_generic_players = %version-%release

%description -n %name-libs
This package contains shared EFL libraries.

%package -n %name-libs-devel
Summary: Enlightenment Foundation Libraries development files
Group: Development/C
Requires: %name-libs = %version-%release
Obsoletes: libeina-devel < %version
Provides: libeina-devel = %version-%release
Obsoletes: libeet-devel < %version
Provides: libeet-devel = %version-%release
Obsoletes: libevas-devel < %version
Provides: libevas-devel = %version-%release
Obsoletes: libecore-devel < %version
Provides: libecore-devel = %version-%release
Obsoletes: libedje-devel < %version
Provides: libedje-devel = %version-%release
Obsoletes: libeeze-devel < %version
Provides: libeeze-devel = %version-%release
Obsoletes: libembryo-devel < %version
Provides: libembryo-devel = %version-%release
Obsoletes: libeio-devel < %version
Provides: libeio-devel = %version-%release
Obsoletes: libefreet-devel < %version
Provides: libefreet-devel = %version-%release
Obsoletes: libethumb-devel < %version
Provides: libethumb-devel = %version-%release
Obsoletes: libemotion-devel < %version
Provides: libemotion-devel = %version-%release
Obsoletes: embryo_cc < %version
Provides: embryo_cc = %version-%release
Provides: libeo-devel = %version-%release
Provides: libephysics-devel = %version-%release
Provides: libeldbus-devel = %version-%release

%description -n %name-libs-devel
This package contains headers, development libraries, test programs and
documentation for EFL.

%package -n libelementary
Summary: Libraries for %name
Group: System/Libraries
Requires: efl-libs = %version-%release
Requires: elementary-data = %version-%release
Obsoletes: libelementary1.8
Provides:  libelementary1.8 = %version-%release

%description -n libelementary
Elementary is a widget set based on the Enlightenment Foundation
Libraries, primarily aimed at creating graphical user interfaces for
mobile and embedded devices. This package contains shared libraries.

%package -n elementary-data
Summary: noarch data for %name
Group: Graphical desktop/Enlightenment
BuildArch: noarch
Obsoletes: elementary1.8-data
Provides:  elementary1.8-data = %version-%release

%description -n elementary-data
The elementary-data package contains architecture independent data files for
Elementary.

%package -n libelementary-devel
Summary: Development files for Elementary
Group: Development/C
Requires: libelementary = %version-%release
Requires: efl-libs-devel = %version-%release
Obsoletes: libelementary1.8-devel
Provides:  libelementary1.8-devel = %version-%release

%description -n libelementary-devel
The libelementary-devel package contains libraries and header files for
developing applications that use Elementary libraries.

%prep
%setup -n %name-%version%beta
%patch -p1
%patch1 -p1

# fix path to soffice.bin
subst 's/libreoffice/LibreOffice/' src/generic/evas/pdf/evas_generic_pdf_loader.libreoffice

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure \
	--disable-static \
	--enable-xinput22 \
	--enable-systemd \
	%{subst_enable elogind} \
	--enable-image-loader-webp \
	--enable-harfbuzz \
	--enable-liblz4 \
	--enable-image-loader-webp \
%ifarch %e2k
	--enable-lua-old \
%else
	%{subst_enable elua} \
%endif
	%{subst_enable multisense} \
	%{subst_enable tslib} \
	%{subst_enable wayland} \
	%{subst_enable fb} \
	%{subst_enable egl} \
	%{subst_enable elput} \
	%{subst_enable drm} \
	%{?_enable_gl_drm:--enable-gl-drm} \
	%{subst_enable ibus} \
	%{subst_enable gstreamer1} \
	--with-mount=/bin/mount \
	--with-umount=/bin/umount \
	--with-eject=%_bindir/eject
%make_build
#%make doc

%install
%makeinstall_std
find %buildroot%_libdir -name "*.la" -delete

%find_lang %name

%files -n %name-libs -f %name.lang
%_bindir/diffeet
%_bindir/edje_cc
%_bindir/edje_decc
%_bindir/edje_external_inspector
%_bindir/edje_inspector
%_bindir/edje_pick
%_bindir/edje_player
%_bindir/edje_recc
%_bindir/edje_watch
%_bindir/eet
%_bindir/eetpack
%_bindir/eeze_disk_ls
%_bindir/eeze_mount
%_bindir/eeze_scanner
%_bindir/eeze_scanner_monitor
%_bindir/eeze_umount
%_bindir/efl_wl_test
%_bindir/efl_wl_test_stack

%_bindir/efreetd
%_bindir/eina_modinfo
%{?_enable_elua:%_bindir/elua}
%_bindir/ethumb
%_bindir/ethumbd
%_bindir/ethumbd_client
%_bindir/vieet
%_libdir/*.so.*
%exclude %_libdir/libelementary.so.*
%_libdir/ecore/
%_libdir/ecore_con/
%_libdir/ecore_evas/
%_libdir/ecore_imf/
%_libdir/ecore_wl2/
%_libdir/edje/
%_libdir/eeze/
%_libdir/efreet/
%{?_enable_emotion:%_libdir/emotion/}
%_libdir/ethumb/
%_libdir/ethumb_client/
%_libdir/evas/
%_datadir/dbus-1/services/org.enlightenment.Ethumb.service
%_datadir/ecore/
%_datadir/ecore_imf/
%_datadir/ecore_x/
%_datadir/edje/
%_datadir/eeze/
%_datadir/efreet/
%_datadir/embryo/
%{?_enable_emotion:%_datadir/emotion/}
%_datadir/ethumb/
%_datadir/ethumb_client/
%_datadir/evas/
%{?_enable_elua:%_datadir/elua/}
# /usr/share/elua/checkme
%{?_disable_elua:%exclude %_datadir/elua}
%_datadir/mime/packages/edje.xml
%_prefix/lib/systemd/user/ethumb.service
%doc AUTHORS README NEWS COMPLIANCE

%files -n %name-libs-devel
%_bindir/ecore_evas_convert
%_bindir/eldbus-codegen
%_bindir/edje_codegen
%_bindir/embryo_cc
%_bindir/eolian_cxx
%_bindir/eolian_gen
%_bindir/efl_debug
%_bindir/efl_debugd
%_bindir/eina_btlog
%_bindir/eo_debug
%_includedir/*
%exclude %_includedir/elementary*/
%_libdir/cmake/*
%exclude %_libdir/cmake/Elementary/
%_libdir/*.so
%exclude %_libdir/libelementary.so
%_pkgconfigdir/ecore-audio-cxx.pc
%_pkgconfigdir/ecore-audio.pc
%_pkgconfigdir/ecore-avahi.pc
%_pkgconfigdir/ecore-con.pc
%_pkgconfigdir/ecore-cxx.pc
%{?_enable_drm:%_pkgconfigdir/ecore-drm2.pc}
%_pkgconfigdir/ecore-evas.pc
%{?_enable_fb:%_pkgconfigdir/ecore-fb.pc}
%_pkgconfigdir/ecore-file.pc
%_pkgconfigdir/ecore-imf-evas.pc
%_pkgconfigdir/ecore-imf.pc
%_pkgconfigdir/ecore-input-evas.pc
%_pkgconfigdir/ecore-input.pc
%_pkgconfigdir/ecore-ipc.pc
%{?_enable_wayland:%_pkgconfigdir/ecore-wl2.pc}
%_pkgconfigdir/ecore-x.pc
%_pkgconfigdir/ecore.pc
%_pkgconfigdir/ector.pc
%_pkgconfigdir/edje-cxx.pc
%_pkgconfigdir/edje.pc
%_pkgconfigdir/eet-cxx.pc
%_pkgconfigdir/eet.pc
%_pkgconfigdir/eeze.pc
%_pkgconfigdir/efl.pc
%_pkgconfigdir/efl-core.pc
%_pkgconfigdir/efl-cxx.pc
%_pkgconfigdir/efl-net.pc
%_pkgconfigdir/efl-ui.pc
%_pkgconfigdir/%name-wl.pc
%_pkgconfigdir/efreet-mime.pc
%_pkgconfigdir/efreet-trash.pc
%_pkgconfigdir/efreet.pc
%_pkgconfigdir/eina-cxx.pc
%_pkgconfigdir/eina.pc
%_pkgconfigdir/eio-cxx.pc
%_pkgconfigdir/eio.pc
%_pkgconfigdir/eldbus.pc
%_pkgconfigdir/elocation.pc
%{?_enable_elput:%_pkgconfigdir/elput.pc}
%{?_enable_elua:%_pkgconfigdir/elua.pc}
%_pkgconfigdir/embryo.pc
%_pkgconfigdir/emile.pc
%{?_enable_emotion:%_pkgconfigdir/emotion.pc}
%_pkgconfigdir/eo-cxx.pc
%_pkgconfigdir/eo.pc
%_pkgconfigdir/eolian-cxx.pc
%_pkgconfigdir/eolian.pc
%_pkgconfigdir/ephysics.pc
%_pkgconfigdir/ethumb.pc
%_pkgconfigdir/ethumb_client.pc
%_pkgconfigdir/evas-cxx.pc
%{?_enable_drm:%_pkgconfigdir/evas-drm.pc}
%{?_enable_fb:%_pkgconfigdir/evas-fb.pc}
%_pkgconfigdir/evas-opengl-x11.pc
%_pkgconfigdir/evas-software-buffer.pc
%_pkgconfigdir/evas-software-x11.pc
%{?_enable_wayland:%_pkgconfigdir/evas-wayland-shm.pc}
%_pkgconfigdir/evas.pc

%exclude %_datadir/gdb
%exclude %_datadir/gdb/auto-load/*/*/libeo.so.*-gdb.py
%exclude %_datadir/eo/
%exclude %_datadir/eo/gdb/eo_gdb.py

%files -n libelementary
%_bindir/elementary_config
%_bindir/elementary_quicklaunch
%_bindir/elementary_run
%_libdir/libelementary*.so.*
%_libdir/edje/modules/elm/*/*.so
%exclude %_libdir/edje/modules/elm/*/module.so
%_libdir/elementary/modules/test_entry/*/*.so
%_libdir/elementary/modules/access_output/*/*.so
%_libdir/elementary/modules/test_map/*/*.so
%_libdir/elementary/modules/clock_input_ctxpopup/*/*.so
%_libdir/elementary/modules/prefs/*/*.edj
%_libdir/elementary/modules/prefs/*/*.so
%_libdir/elementary/modules/web/*/*/module.so

%files -n libelementary-devel
%_bindir/elementary_codegen
%_bindir/elementary_test
%_bindir/elm_prefs_cc
%_includedir/elementary*/
%_libdir/libelementary*.so
%_libdir/cmake/Elementary/
%_pkgconfigdir/elementary*.pc

%files -n elementary-data
%_datadir/elementary/
%_desktopdir/elementary_config.desktop
%_desktopdir/elementary_test.desktop
%_iconsdir/hicolor/*/apps/elementary.png
%_iconsdir/Enlightenment-X/

%changelog
* Wed Sep 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.22.4-alt1
- 1.22.4

* Sat Aug 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.22.3-alt1
- 1.22.3

* Thu May 02 2019 Yuri N. Sedunov <aris@altlinux.org> 1.22.2-alt1
- 1.22.2
- enabled elogind support

* Tue Mar 05 2019 Yuri N. Sedunov <aris@altlinux.org> 1.21.1-alt3
- fixed FTBFS on 32-bit architectures (ALT #36233)

* Thu Sep 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.21.1-alt2
- rebuilt against libraw.so.19

* Thu Sep 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.21.1-alt1
- 1.21.1

* Thu Sep 06 2018 Yuri N. Sedunov <aris@altlinux.org> 1.21.0-alt1
- 1.21.0

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1.20.7-alt3
- rebuilt with openssl-1.1

* Tue Jun 12 2018 Yuri N. Sedunov <aris@altlinux.org> 1.20.7-alt2
- mike:
  introduce emotion knob (on by default)
  E2K: avoid not-ported-yet BRs (libunwind, luajit)
- disabled elua for aarch64 (https://github.com/LuaJIT/LuaJIT/pull/230)

* Thu Mar 01 2018 Yuri N. Sedunov <aris@altlinux.org> 1.20.7-alt1
- 1.20.7

* Fri Nov 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.20.6-alt1
- 1.20.6

* Fri Oct 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.20.5-alt1
- 1.20.5

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.20.4-alt1
- 1.20.4

* Sun Sep 03 2017 Yuri N. Sedunov <aris@altlinux.org> 1.20.3-alt1
- 1.20.3

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.20.2-alt1
- 1.20.2

* Sat May 27 2017 Yuri N. Sedunov <aris@altlinux.org> 1.19.1-alt1
- 1.19.1

* Thu Apr 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1.19.0-alt1
- 1.19.0

* Mon Mar 27 2017 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt3
- updated to v1.18.4-16-ga189bd5

* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt2
- rebuilt against libraw.so.16

* Tue Dec 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt1
- 1.18.4

* Sun Nov 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Tue Oct 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Wed Aug 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Wed Jun 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1.17.2-alt1
- 1.17.2

* Sun Jun 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.17.1-alt1
- 1.17.1

* Tue Feb 02 2016 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt2
- rebuilt against libwebp.so.6

* Fri Dec 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0 release

* Mon Oct 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt0.1
- 1.16.0-beta3

* Wed Aug 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.1-alt1
- 1.15.1

* Wed Aug 05 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0 release

* Tue Jul 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt0.2
- 1.15.0 beta2

* Fri Jun 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Wed Jun 03 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Thu May 07 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0 release

* Mon May 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt0.1
- 1.14.0_9b167d9

* Mon May 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.13.2-alt1
- 1.13.2_a1ea4a41

* Thu Dec 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.5-alt1
- 1.11.5

* Tue Oct 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.4-alt1
- 1.11.4

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.3-alt1
- 1.11.3

* Wed Sep 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.2-alt1
- 1.11.2

* Thu Jul 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.6-alt1
- 1.8.6

* Tue Jan 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt1
- 1.8.5

* Fri Jan 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt2
- enabled IBUS, DRM support
- built against libwebp.so.5

* Sat Dec 21 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Tue Dec 17 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt2
- 1.8.2 snapshot (3b57d1f)
- obsoletes/provides edje

* Tue Dec 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2
- obsoletes/provides all EFL libraries < 1.8

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- first build for Sisyphus

