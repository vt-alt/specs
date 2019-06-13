%def_enable snapshot

%define ver_major 3.12
%define brasero_api_ver 3
%define nau_api_ver 3.0
%define gst_api_ver 1.0

%def_enable gtk_doc
# Make use of Tracker
%def_enable search
# Embed a playlist functionality based on libtotem
%def_enable playlist
%def_enable cdrkit
%def_disable cdrtools
%def_enable cdrdao
%def_enable libburnia
%def_enable introspection

Name: brasero
Version: %ver_major.2
Release: alt5

Summary: CD/DVD burning tool for GNOME.
Group: Archiving/Cd burning
License: %gpl2plus
Url: https://wiki.gnome.org/Apps/Brasero

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: %name-2.27.90-alt-link.patch
Patch1: %name-2.28.1-alt-button-underline.patch
Patch2: %name-2.32.1-schemas_convert_typo.patch

Requires: lib%name = %version-%release

%define burn_ver 1.4.9
%define isofs_ver 1.4.9

Requires: dconf
%{?_enable_search:Requires: tracker}
Requires: dvd+rw-tools
Requires: cdrkit
Requires: mkisofs
%{?_enable_libburnia:Requires: libburn >= %burn_ver libisofs >= %isofs_ver}
%{?_enable_cdrdao:Requires: cdrdao}

# to make vcd or video dvd
Requires: dvdauthor vcdimager gst-plugins-bad%gst_api_ver

BuildRequires(pre): gnome-common rpm-build-gnome rpm-build-licenses rpm-build-gir

# From configure.ac
BuildRequires: libgio-devel >= 2.30.0
BuildRequires: libgtk+3-devel >= 3.0.0
BuildRequires: gstreamer%gst_api_ver-devel >= 0.11.99
BuildRequires: gst-plugins%gst_api_ver-devel >= 0.11.99
BuildRequires: libxml2-devel >= 2.6.0
%{?_enable_libburnia:BuildRequires: libburn-devel >= %burn_ver libisofs-devel >= %isofs_ver}
BuildRequires: libnotify-devel >= 0.7
%{?_enable_search:BuildPreReq: pkgconfig(tracker-sparql-2.0)}
%{?_enable_playlist:BuildPreReq: libtotem-pl-parser-devel >= 2.30.2}
BuildRequires: intltool >= 0.35.0
BuildRequires: libcanberra-gtk3-devel
BuildRequires: gtk-doc >= 1.11
BuildRequires: yelp-tools
BuildRequires: libSM-devel
# for nautilus extension
BuildRequires: libnautilus-devel
# GObject introspection support
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}

%description
Brasero is an application to burn CD/DVD for the Gnome Desktop. It is designed
to be as simple as possible and has some unique features to enable users to
create their discs easily and quickly.

%package -n lib%name
Summary: Shared library for Brasero CD/DVD burning application
Group: System/Libraries

%description -n lib%name
Brasero is an application to burn CD/DVD for the Gnome Desktop. It is designed
to be as simple as possible and has some unique features to enable users to
create their discs easily and quickly.

This package provides shared library required for Brasero to work.

%package -n lib%name-devel
Summary: Development files and libraries for Brasero CD/DVD burning application
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Brasero is an application to burn CD/DVD for the Gnome Desktop. It is designed
to be as simple as possible and has some unique features to enable users to
create their discs easily and quickly.

This package provides files and library required to develop applications
that use libbrasero.

%package -n lib%name-devel-doc
Summary: Development documentation for Brasero CD/DVD burning application
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name < %version

%description -n lib%name-devel-doc
Brasero is an application to burn CD/DVD for the Gnome Desktop. It is designed
to be as simple as possible and has some unique features to enable users to
create their discs easily and quickly.

This package provides usefull documentation to develop applications
that use libbrasero.

%package nautilus
Summary: Nautilus extension for the Brasero CD/DVD burning application
Group: Archiving/Cd burning
Requires: %name = %version-%release

%description nautilus
This package provides integration with the Brasero for the Nautilus file
manager.

%package -n lib%name-gir
Summary: GObject introspection data for the Brasero
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Brasero

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Brasero
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Brasero

%prep
%setup
%patch -p1 -b .link
%patch1 -p1 -b .button_underline
%patch2 -b .schemas_convert

%build
%autoreconf
%configure \
	%{subst_enable libburnia} \
	%{subst_enable search} \
	%{subst_enable playlist} \
	%{subst_enable cdrkit} \
	%{subst_enable cdrtools} \
	%{subst_enable cdrdao} \
	%{subst_enable introspection} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--enable-preview \
	--enable-inotify \
	--disable-caches \
	--disable-static \
	--disable-schemas-compile
# SMP-incompatible build
%make

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%dir %_libdir/%name%brasero_api_ver/plugins
%_libdir/%name%brasero_api_ver/plugins/lib%name-cdrdao.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-dvdcss.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-dvdrwformat.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-genisoimage.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-growisofs.so
%{?_enable_libburnia:%_libdir/%name%brasero_api_ver/plugins/lib%name-libburn.so}
%{?_enable_libburnia:%_libdir/%name%brasero_api_ver/plugins/lib%name-libisofs.so}
%_libdir/%name%brasero_api_ver/plugins/lib%name-local-track.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-checksum.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-checksum-file.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-normalize.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-readom.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-audio2cue.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-transcode.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-wodim.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-dvdauthor.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-vcdimager.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-vob.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-burn-uri.so

%if_enabled cdrtools
%_libdir/%name%brasero_api_ver/plugins/lib%name-cdrecord.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-readcd.so
%_libdir/%name%brasero_api_ver/plugins/lib%name-mkisofs.so
%endif

%_desktopdir/%name.desktop
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name-symbolic.svg
%_man1dir/%name.1.*
%_datadir/mime/packages/%name.xml
%config %_datadir/glib-2.0/schemas/org.gnome.brasero.gschema.xml
%_datadir/GConf/gsettings/brasero.convert
%_datadir/metainfo/%name.appdata.xml

%exclude %_datadir/applications/brasero-nautilus.desktop
%exclude %_libdir/%name%brasero_api_ver/plugins/lib%name-*.la

%files nautilus
%_libdir/nautilus/extensions-%nau_api_ver/libnautilus-brasero-extension.so
%_datadir/applications/brasero-nautilus.desktop

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir
%endif

%exclude %_libdir/nautilus/extensions-%nau_api_ver/libnautilus-%name-extension.la

%changelog
* Mon Jun 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt5
- updated to 3.12.2-62-gbd1a4d5b
- Requires: +dconf, +tracker if "search" enabled (ALT #36887)

* Thu Sep 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt4.1
- fixed dependencies

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt4
- updated to 3.12.2-49-gedc40465

* Sun Feb 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt3
- updated to 3.12.2-34-g567326a
- enabled libburn support

* Wed Aug 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt2
- rebuilt against tracker-2.0 for GNOME-3.26

* Mon Jul 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Sun Jan 24 2016 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt2
- fixed files list

* Tue Apr 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Thu Sep 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.4-alt1
- 3.11.4

* Mon May 05 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.3-alt1
- after 3.11.3 snapshot (718139441)

* Mon Nov 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Sep 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt2
- rebuild against libtotem-plparser.so.18

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0
- no support for tracker-0.16

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt3
- updated from upstream git
- tracker support enabled again (using tracker-sparql-0.12)

* Sat Oct 29 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- tracker support disabled

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Jun 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- disabled broken libburnia backend (tnx to boyarsh@ for bug report)

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Mar 29 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Thu Jan 20 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1
- 2.91.5

* Mon Dec 20 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- build current snapshot

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Thu Oct 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Sep 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.92-alt1
- 2.31.92

* Fri Sep 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.91-alt1
- 2.31.91

* Fri Sep 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Wed Apr 07 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.0-alt3
- rebuild with libtracker-client-0.8

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- rebuild with new rpm-build-gir (0.2-alt1)

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Fri Mar 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt2
- rebuild using rpm-build-gir

* Wed Feb 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Tue Feb 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt2
- search via beagle disabled

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Wed Jan 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Wed Dec 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4

* Wed Oct 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt2
- 2.28.2

* Sat Oct 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt2
- fixed "Last Unsaved Project" button property (shrek@)

* Thu Oct 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Sun Sep 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt2
- cdrtools support disabled (shrek@)
- requires cdrkit

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Wed Aug 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91
- updated buildreqs

* Wed Jul 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Sun Jun 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt2
- requires dvd+rw-tools, cdrecord, mkisofs, cdrdao (closes #20521)

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Thu Mar 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Mon Feb 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.90-alt1
- 2.25.90
- new libbrasero, brasero-devel{,-doc} packages

* Sun Dec 14 2008 Yuri N. Sedunov <aris@altlinux.org> 0.8.4-alt1
- new version

* Mon Nov 10 2008 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3
- new nautilus subpackage
- playlist support via libtotem-pl-parser

* Mon Sep 15 2008 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- new version

* Tue Aug 12 2008 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- new version
- requires dvdauthor, vcdimager, gst-plugins-bad for video
  projects.

* Sat Jul 19 2008 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- new version

* Thu Jul 03 2008 Yuri N. Sedunov <aris@altlinux.org> 0.7.91-alt1
- new version.
- updted reqs.
- playlist functionality based on libtotem temporarily disabled -
  new totem required.
- don't built help files 

* Fri Mar 07 2008 Alexey Rusakov <ktirf@altlinux.org> 0.7.1-alt3
- Rebuilt with new libburn and libisofs.
- Fixed desktop files categories (thanks to repocop).
- Temporarily disabled libburn/libisofs plugins.

* Sat Mar 01 2008 Alexey Rusakov <ktirf@altlinux.org> 0.7.1-alt2
- Added %%update_menus/%%clean_menus to the package scripts (thanks to
  repocop).

* Mon Jan 28 2008 Alexey Rusakov <ktirf@altlinux.org> 0.7.1-alt1
- New version (0.7.1).
- Updated buildreqs.

* Wed Dec 26 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.0-alt1
- New version (0.7.0).
- Updated buildreqs (including buildreq on libburn-devel >= 0.4.0).
- Turned integration with Beagle back on (new libbeagle is required now).

* Tue Dec 18 2007 Alexey Rusakov <ktirf@altlinux.org> 0.6.90-alt1
- New version (0.6.90).
- Updated the files list.
- Use license macro.
- Disabled Beagle because of incompatibility with new libbeagle.
- Added configure switches to include all (except search) possible plugins.

* Sat Sep 22 2007 Alexey Rusakov <ktirf@altlinux.org> 0.6.1-alt1.1
- rebuilt with new libisofs.

* Fri Sep 14 2007 Alexey Rusakov <ktirf@altlinux.org> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Mon Jun 25 2007 Alexey Rusakov <ktirf@altlinux.org> 0.5.90-alt3
- spec cleanup, updated dependencies

* Thu Jun 21 2007 Andrii Dobrovol`s`kii <dobr@iop.kiev.ua> 0.5.90-alt2
- build with libburn.

* Thu Jun 21 2007 Andrii Dobrovol`s`kii <dobr@iop.kiev.ua> 0.5.90-alt1
- build with totem and beagle.

* Sat Jun 16 2007 Andrii Dobrovol`s`kii <dobr@iop.kiev.ua> 0.5.2-alt0
- initial build for ALT Linux (Sisyphus) with help from Alexey Rusakov.

