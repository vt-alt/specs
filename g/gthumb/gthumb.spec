%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_base 3.8
%define ver_major 3.8
%define gst_api_ver 1.0
%define xdg_name org.gnome.gThumb

%def_enable exiv2
%def_enable libbrasero
%def_enable webservices
%def_disable libchamplain
%def_enable libraw
%def_enable colord
%def_enable gstreamer

Name: gthumb
Version: %ver_major.1
Release: alt1

Summary: An image file viewer and browser for GNOME
Summary(ru_RU.UTF-8): Просмотрщик изображений и фотоальбом для GNOME

License: GPL
Group: Graphics
Url: http://gthumb.sourceforge.net/

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%endif

%define glib_ver 2.38.0
%define gtk_ver 3.10.0
%define clutter_gtk_ver 1.0.0
%define gst_ver 1.0
%define exiv2_ver 0.20
%define libraw_ver 0.16
%define brasero_ver 3.2.0
%define soup_ver 2.42
%define gnome_common_ver 2.8.0
%define webp_ver 0.2.0
%define webkit_ver 2.6.0
%define champlain_ver 0.12.0
%define desktop_file_utils_ver 0.8

Requires: %name-data = %version-%release

BuildRequires(pre): meson
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libclutter-devel libclutter-gtk3-devel >= %clutter_gtk_ver
%{?_enable_gstreamer:BuildRequires: gstreamer%gst_api_ver-devel >= %gst_ver gst-plugins%gst_api_ver-devel >= %gst_ver}
BuildRequires: libjpeg-devel libpng-devel libtiff-devel zlib-devel
BuildRequires: libsoup-devel >= %soup_ver libsecret-devel
BuildRequires: librsvg-devel intltool perl-XML-Parser gnome-common yelp-tools
BuildRequires: gsettings-desktop-schemas-devel libwebp-devel >= %webp_ver libjson-glib-devel
BuildRequires: libwebkitgtk4-devel >= %webkit_ver
%{?_enable_libraw:BuildRequires: libraw-devel >= %libraw_ver libgomp-devel}
%{?_enable_libbrasero:BuildRequires: libbrasero-devel >= %brasero_ver}
%{?_enable_webservices:BuildRequires: bison flex}
%{?_enabled_libchamplain:BuildRequires: libchamplain-gtk3-devel >= %champlain_ver}
%{?_enable_colord:BuildRequires: libcolord-devel}

%if_enabled exiv2
BuildRequires: libexiv2-devel >= %exiv2_ver gcc-c++
%endif

BuildRequires: libjpeg-devel libtiff-devel libXrender-devel libXext-devel libX11-devel
BuildRequires: libXtst-devel libXxf86vm-devel libXi-devel
BuildRequires: libSM-devel libICE-devel

BuildRequires: desktop-file-utils >= %desktop_file_utils_ver
BuildRequires: gnome-common >= %gnome_common_ver
BuildRequires: libappstream-glib-devel

%description
gThumb lets you browse your hard disk, showing thumbnails of image
files. It also lets view single files (including GIF animations),
add comments to images, organize images in catalogs, print images, view
slideshows, set desktop background, and more.

%description -l ru_RU.UTF-8
gThumb позволяет просматривать содержимое жёсткого диска, показывая
уменьшенные копии содержимого графических файлов. Также программа
позволяет просматривать отдельные изображения (включая мультфильмы в
формате GIF), добавлять комментарии к картинкам, раскладывать картинки
по каталогам, печатать, автоматически пролистывать серии картинок,
менять фон рабочего стола и многое другое.

%package data
Summary: Arch independent files for gThumb
Group: Graphics
BuildArch: noarch

%description data
This package provides noarch data needed for gThumb to work.

%package devel
Summary: gThumb development files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains headers needed to build extensions for gThumb.

%prep
%setup

%build
%meson \
    -Dlibtiff=true \
    %{?_disable_exiv2:-Dexiv2=false} \
    %{?_disable_libbrasero:-Dlibbrasero=false} \
    %{?_enable_libchamplain:-Dlibchamplain=true} \
    %{?_disable_libraw:-Dlibraw=false} \
    %{?_disable_colord:-Dcolord=false} \
    %{?_disable_gstreamer:-Dgstreamer=false}
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files
%_bindir/*
%dir %_libdir/gthumb/extensions
%_libdir/gthumb/extensions/*

%files data  -f %name.lang
%_desktopdir/*
%_datadir/%name/
%_iconsdir/hicolor/*/*/*
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.change-date.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.comments.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.contact-sheet.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.convert-format.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.crop.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.enums.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.facebook.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.file-manager.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.flickr.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.gstreamer-tools.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.image-print.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.image-viewer.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.importer.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.photo-importer.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.picasaweb.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.pixbuf-savers.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.rename-series.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.resize.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.resize-images.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.rotate.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.slideshow.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gthumb.webalbums.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%_man1dir/gthumb.1.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%name/
%_datadir/aclocal/gthumb.m4
%_pkgconfigdir/*

%changelog
* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon May 27 2019 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sun May 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- updated to 3.7.2-2-ga3cf5b19

* Tue Feb 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.7.1-alt1
- 3.7.1

* Sun Sep 30 2018 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Mon Aug 06 2018 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt2
- rebuilt against libraw.so.19

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Nov 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Nov 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.5.4-alt1
- 3.5.4

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.5.3-alt1
- 3.5.3

* Sun Aug 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.5.2-alt1
- 3.5.2

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.5.1-alt2
- rebuilt against libexiv2.so.26

* Thu Mar 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.5.1-alt1
- 3.5.1

* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.4.4.1-alt2
- rebuilt against libraw.so.16

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.4.4.1-alt1
- 3.4.4.1

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.4.4-alt1
- 3.4.4

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon Mar 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt2
- rebuilt against libwebp.so.6

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt3
- rebuilt against libraw.so.15

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt2
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.4.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Mar 31 2015 Yuri N. Sedunov <aris@altlinux.org> 3.3.4-alt1
- 3.3.4

* Tue Feb 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.3.3-alt1
- 3.3.3

* Mon Oct 06 2014 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2

* Sun May 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.2.8-alt1
- 3.2.8

* Wed Mar 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.2.7-alt1
- 3.2.7, built for gnome-3.12

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.2.6-alt2
- rebuilt against libwebp.so.5

* Tue Dec 31 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.6-alt1
- 3.2.6

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.5-alt2
- rebuilt against libexiv2.so.13

* Tue Nov 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.5-alt1
- 3.2.5

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.4-alt1
- 3.2.4

* Sun Sep 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt4
- updated to 3.2_f80e3ba (fixed BGO #708800)

* Tue Sep 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt3
- rebuilt for people/gnome/3.10

* Tue Sep 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt2
- updated to 3.2_56dd7c4 (fixed BGO ##706697, 706343, 705877)
- enabled map support via libchamplain

* Wed Jul 10 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Mar 05 2013 Yuri N. Sedunov <aris@altlinux.org> 3.1.4-alt1
- 3.1.4

* Thu Jan 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt3
- rebuilt against libexiv2.so.12

* Wed Sep 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- rebuilt for people/gnome

* Fri Sep 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Wed Apr 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Apr 10 2012 Yuri N. Sedunov <aris@altlinux.org> 2.90.3-alt1
- 2.90.3

* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 2.90.2-alt2
- updated from upstream git

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 2.90.2-alt1
- 2.90.2

* Tue Jan 24 2012 Yuri N. Sedunov <aris@altlinux.org> 2.14.2-alt1
- 2.14.2

* Sun Dec 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.14.1-alt1
- 2.14.1
- split up noarch data in separate -data subpackage

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt2
- rebuilt against libexiv2.so.11

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt1
- 2.14.0

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 2.13.91-alt1
- 2.13.91

* Sun May 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.12.3-alt1
- 2.12.3

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 2.12.2-alt2
- updated buildreqs
- added some fixes from upstream

* Sat Jan 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.12.2-alt1
- 2.12.2

* Tue Nov 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.12.1-alt1
- 2.12.1

* Thu Oct 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.12.0-alt1
- 2.12.0

* Wed Sep 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.11.92-alt1
- 2.11.92

* Thu Jun 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.11.3-alt2
- rebuild against libexiv2-0.20

* Wed May 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.12-alt1
- 2.10.12

* Sun Sep 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.10.11-alt3
- updated russian translation (ALT #21639)

* Tue Jun 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.10.11-alt2
- rebuild

* Sun Mar 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.10.11-alt1
- new version

* Mon Dec 01 2008 Yuri N. Sedunov <aris@altlinux.org> 2.10.10-alt3
- removed obsolete %%post* macros
- updated buildreqs

* Thu Oct 09 2008 Yuri N. Sedunov <aris@altlinux.org> 2.10.10-alt2
- updated russian translation
  http://l10n.gnome.org/POT/gthumb.HEAD/gthumb.HEAD.ru.po

* Tue Sep 23 2008 Yuri N. Sedunov <aris@altlinux.org> 2.10.10-alt1
- 2.10.10

* Wed Aug 06 2008 Yuri N. Sedunov <aris@altlinux.org> 2.10.9-alt1
- new version
- updated buildreqs (versions, raw and IPTC support enabled)

* Mon Mar 24 2008 Vitaly Lipatov <lav@altlinux.ru> 2.10.8-alt1
- new version 2.10.8 (with rpmrb script)

* Thu Oct 18 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.7-alt1
- new version 2.10.7 (with rpmrb script)

* Sun Sep 23 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.6-alt1
- new version 2.10.6 (with rpmrb script)
- enable update/clean menus

* Sat Jun 23 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.4-alt1
- new version 2.10.4 (with rpmrb script)
- spec fixes

* Wed Mar 14 2007 Vitaly Lipatov <lav@altlinux.ru> 2.9.3-alt1
- new version 2.9.3 (with rpmrb script)
- bzip ChangeLog (fix bug #11084), thanks icesik@

* Sun Jan 21 2007 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt0.1
- new version 2.9.1 (formally unstable)
- add gnome-doc-utils to buildreq

* Fri Dec 29 2006 Alexey Rusakov <ktirf@altlinux.org> 2.8.1-alt1
- new version (2.8.1)

* Sun Sep 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.7.8-alt1
- new version (2.7.8), switching to formally-unstable branch.
- renamed 'with libexif' switch to 'enable exif', to fit with configure script.
- likewise, renamed 'with gphoto' to 'enable gphoto2'.

* Tue Apr 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.6.9-alt1
- new version (2.6.9)
- spec cleanup, dependencies updated
- removed Debian menu support.

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.6-alt1
- 2.6.6

* Sat Apr 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1.1
- rebuild against libexif.so.12.

* Fri Mar 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Sun Jan 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Tue Dec 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sun Nov 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.1-alt1
- 2.6.0.1

* Mon Sep 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1.1
- rebuild with libtiff.so.4

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Wed Sep 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Sun Jul 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Sat May 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Thu May 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1.1
- updated translations by slava@.

* Fri Apr 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Mon Feb 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt2
- build with gphoto2 support.
- new translation, i18n fix, summary and description in UTF-8 by slava.

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Fri Dec 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Thu Dec 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.9-alt1
- 2.1.9

* Mon Nov 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.8-alt1
- 2.1.8

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Mon Sep 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Wed Jul 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3
- ru.po by slava.

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Mon Jan 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- go to gnome2.
- Patch for building with libgnomeprint2-2.2 by AVL.

* Thu Jun 13 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.13-alt1
- ALTLinux build.
