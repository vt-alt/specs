%define ver_major 2.6
%define beta %nil

Name: darktable
Version: %ver_major.2
Release: alt2

Summary: Darktable is a virtual lighttable and darkroom for photographer
License: GPLv3
Group: Graphics

Url: http://%name.org/
#VCS: https://github.com/darktable-org/darktable.git
#Source: %name-%version.tar
Source: https://github.com/darktable-org/darktable/releases/download/release-%version/%name-%version.tar.xz
Patch: darktable-2.6.2-up-exiv2-0.27.2.patch

%define cmake_ver 3.4
%define glib_ver 2.40
%define gtk_ver 3.14
%define exiv2_ver 0.24
%define iso_codes_ver 3.66

Requires: iso-codes >= %iso_codes_ver
Requires: icon-theme-adwaita

BuildRequires(pre): cmake >= %cmake_ver
BuildRequires: gcc-c++ libgomp-devel
BuildRequires: /proc
BuildRequires: intltool desktop-file-utils libappstream-glib-devel
BuildRequires: perl-Pod-Parser xsltproc
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver libxml2-devel
BuildRequires: libSDL2-devel libX11-devel libXrandr-devel libcurl-devel
BuildRequires: libexiv2-devel >= %exiv2_ver libflickcurl-devel libsecret-devel
BuildRequires: libgphoto2-devel libjpeg-devel liblcms2-devel liblensfun-devel
BuildRequires: libpng-devel librsvg-devel libsqlite3-devel libtiff-devel
BuildRequires: openexr-devel libxkbcommon-x11-devel lsb-release
BuildRequires: libjson-glib-devel libsoup-devel libpixman-devel libexpat-devel
BuildRequires: libcolord-gtk-devel libudev-devel
BuildRequires: libGraphicsMagick-c++-devel libopenjpeg2.0-devel
BuildRequires: libharfbuzz-devel libwebp-devel libxshmfence-devel
# since 2.0
BuildRequires: libpugixml-devel libcups-devel
BuildRequires: libosm-gps-map1.0-devel
BuildRequires: python-module-jsonschema
BuildRequires: iso-codes-devel >= %iso_codes_ver
# for not recommended build from git tree
#BuildRequires: gnome-doc-utils fop saxon ...

%description
darktable is a virtual light table and darkroom for photographers. It manages
your digital negatives in a database and lets you view them through a zoomable
light table. It also enables you to develop raw images and enhance them.

%prep
%setup -n %name-%version
%patch -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%cmake -DCMAKE_SKIP_RPATH:BOOL=OFF \
-DCMAKE_BUILD_TYPE=Release \
-DBINARY_PACKAGE_BUILD:BOOL=ON \
%ifarch ppc64le
-DUSE_OPENCL=OFF
%endif

%cmake_build VERBOSE=1
%install
%cmakeinstall_std

ln -s %name/lib%name.so %buildroot%_libdir/lib%name.so

install -pD -m644 data/pixmaps/16x16/darktable.png %buildroot%_miconsdir/darktable.png
install -pD -m644 data/pixmaps/32x32/darktable.png %buildroot%_niconsdir/darktable.png
install -pD -m644 data/pixmaps/48x48/darktable.png %buildroot%_liconsdir/darktable.png

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name/
%_libdir/lib%name.so
%_libdir/%name/
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_datadir/appdata/%name.appdata.xml
%exclude /usr/share/doc/%name/

%changelog
* Sun Aug 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt2
- fixed build against libexiv2-0.27.2
- ppc64le: disabled OpenCL

* Wed Mar 20 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Wed Mar 06 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Mon Dec 24 2018 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Wed Jun 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.4-alt1
- 2.4.4

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- 2.4.3

* Thu Mar 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Thu Jan 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Mon Dec 25 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.5-alt1
- 2.2.5

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt2
- rebuilt against libexiv2.so.26

* Thu Apr 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt1
- 2.2.4

* Wed Feb 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1.1
- fixed buildreqs

* Wed Feb 01 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Sat Jan 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Sun Dec 25 2016 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Tue Oct 25 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- 2.0.7

* Tue Sep 06 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.6-alt1
- 2.0.6

* Tue Jul 05 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- 2.0.5

* Fri May 06 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Sat Apr 16 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt2
- rebuilt against libosmgpsmap-1.0.so.1

* Tue Mar 29 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Tue Mar 08 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Wed Feb 03 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt2
- rebuilt against liblensfun.so.1

* Thu Dec 24 2015 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Oct 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.9-alt1
- 1.6.9

* Tue Aug 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.8-alt1
- 1.6.8

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt2
- rebuilt against libexiv2.so.14

* Wed Jun 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.7-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jun 10 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt1
- 1.6.7 using gcc-4.9

* Tue Apr 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt1
- 1.6.6

* Wed Apr 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Wed Mar 11 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Tue Feb 03 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt2
- rebuilt against libgphoto2_port.so.12

* Sun Feb 01 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Sat Dec 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt2
- added -DBINARY_PACKAGE_BUILD:BOOL=ON  directive to cmake
  (suggested by upstream) to allow the program to run on
  various processors with sse3 and above

* Sat Dec 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Dec 09 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sun Jun 08 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt2
- rebuilt against libcolord.so.2

* Thu May 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri Feb 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sat Dec 28 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4 release

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt0.1.rc1
- 1.4-rc1
- built against libexiv2.so.13

* Wed Sep 18 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3, fixed (ALT #29371)

* Sun Aug 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2
- GraphicsMagick, libopenjpeg support

* Thu Jan 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.1
- Rebuilt with libpng15

* Sat Jun 16 2012 Victor Forsiuk <force@altlinux.org> 1.0.4-alt1
- 1.0.4

* Tue May 15 2012 Victor Forsiuk <force@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Mar 15 2012 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- 1.0

* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 0.9.3-alt1
- 0.9.3

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt2
- rebuilt against libexiv2.so.11

* Sun Aug 28 2011 Victor Forsiuk <force@altlinux.org> 0.9.2-alt1
- 0.9.2

* Wed Jul 27 2011 Victor Forsiuk <force@altlinux.org> 0.9.1-alt1
- 0.9.1

* Sun Jul 03 2011 Victor Forsiuk <force@altlinux.org> 0.9-alt1
- 0.9

* Wed Mar 09 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt3
- Refresh BuildRequires.

* Thu Feb 17 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt2
- Fix build mistake, now darktable will work correctly (closes: #25102).

* Wed Feb 16 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt1
- 0.8

* Tue Dec 14 2010 Victor Forsiuk <force@altlinux.org> 0.7.1-alt1
- 0.7.1

* Fri Dec 03 2010 Victor Forsiuk <force@altlinux.org> 0.7-alt1
- 0.7

* Wed Sep 08 2010 Victor Forsiuk <force@altlinux.org> 0.6-alt1
- 0.6

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 0.5-alt2
- Rebuild with libexiv2.so.9.

* Wed Mar 31 2010 Victor Forsiuk <force@altlinux.org> 0.5-alt1
- 0.5

* Wed Feb 10 2010 Victor Forsiuk <force@altlinux.org> 0.4-alt1.git20100210
- Git snapshot from 2010-02-10.

* Tue Aug 18 2009 Victor Forsyuk <force@altlinux.org> 0.2-alt1
- Initial build.
