%def_disable snapshot
%define gimpplugindir %(gimptool-2.0 --gimpplugindir)
%def_enable zart

%define gmic_git_ver v.2.7.0
# https://github.com/c-koi/zart
# no tags
%define zart_ver 9d67c0d
# https://github.com/c-koi/gmic-qt
# v.2.6.2
%define gmic_qt_ver 2.6.7
# https://github.com/dtschump/gmic-community.git
# 1.6.3.2-1245-g44ad9cb
%define gmic_comm_ver 1.6.3.2-1278-g91e4cf7

Name: gmic
Version: 2.7.0
Release: alt1

Summary: GREYC's Magic Image Converter
License: CeCILL v.2.0, GPLv3
Group: Graphics
Url: http://gmic.sourceforge.net/

%if_disabled snapshot
Source: http://gmic.eu/files/source/%{name}_%version.tar.gz
%else
# VCS: https://github.com/dtschump/gmic.git
Source: %name-%version.tar
%endif
Source1: zart-%zart_ver.tar
Source2: gmic-qt-%gmic_qt_ver.tar
Source3: gmic-community-%gmic_comm_ver.tar

Requires: lib%name = %version-%release

BuildRequires: dos2unix
BuildRequires: gcc-c++ imake libGraphicsMagick-c++-devel libImageMagick-devel libXext-devel libXrandr-devel
BuildRequires: libavformat-devel libfftw3-devel libgimp-devel libjpeg-devel libopencv-devel libpng-devel
BuildRequires: libswscale-devel libtiff-devel openexr-devel xorg-cf-files zlib-devel libgomp-devel
BuildRequires: libcurl-devel
BuildRequires: bash-completion
# for -zart and -qt
BuildRequires: qt5-base-devel

%description
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

%package -n lib%name
Summary: GREYC's Magic Image Converter Library
Group: System/Libraries

%description -n lib%name
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

This package provides shared G'MIC library.

%package -n lib%name-devel
Summary: GREYC's Magic Image Converter Library (development package)
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

This package provides development files for GREYC's Magic Image Converter Library.

%package zart
Summary: GREYC's image processing language demo
Group: Graphics
Provides: zart = %version-%release
Requires: lib%name = %version-%release

%description zart
ZArt is a computer program whose purpose is to demonstrate the possibilities of
the G'MIC image processing language by offering the choice of several
manipulations on a video stream acquired from a webcam. In other words, ZArt is
a GUI for G'MIC real-time manipulations on the output of a webcam.

%package qt
Summary: Qt-based frontend for G'MIC
Group: Graphics
Requires: %name = %version-%release

%description qt
G'MIC-Qt is a versatile front-end to the image processing framework
G'MIC. It is in fact a plugin for GIMP and Krita, as well as a standalone
application.

%package -n gimp-plugin-gmic
Summary: Image denoising and interpolation plugin for GIMP
Group: Graphics
Requires: gimp

%description -n gimp-plugin-gmic
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

%prep
%setup -n gmic-%version -a1 -a2 -a3
dos2unix src/Makefile
# fix libdir
subst 's|\$(USR)/\$(LIB)/|$(USR)/%_lib/|' src/Makefile
# fix libcgmic path
subst 's| \.\.\/\(\.\.\/gmic-community/libcgmic\)| \1|' src/Makefile
%ifnarch %ix86 x86_64
subst 's|-mtune=generic||' src/Makefile
%endif

%build
%add_optflags -D_FILE_OFFSET_BITS=64
pushd src
%make NOSTRIP=1 OPT_CFLAGS="%optflags_default" cli lib libc
popd

pushd %name-qt
%qmake_qt5 CONFIG+=release GMIC_PATH=../src HOST=gimp gmic_qt.pro
%make_build
%qmake_qt5 CONFIG+=release GMIC_PATH=../src HOST=none gmic_qt.pro
%make_build
popd

%if_enabled zart
pushd zart
%qmake_qt5 CONFIG+=release GMIC_PATH=../src zart.pro
%make_build
popd
%endif

%install
cp -f gmic-community/libcgmic/COPYING COPYING-libcgmic

pushd src
%makeinstall_std
popd

pushd %name-qt
%makeinstall_std
popd

%if_enabled zart
pushd zart
%makeinstall_std
popd
%endif

%find_lang --with-man %name

%files -f %name.lang
%_bindir/%name
%_man1dir/%name.1.*
%_datadir/bash-completion/completions/%name
%doc README COPYING

%files qt
%_bindir/%{name}_qt
%doc %name-qt/README*

%files -n lib%name
%_libdir/lib%name.so.*
%_libdir/libc%name.so.*
%doc COPYING COPYING-libcgmic

%files -n lib%name-devel
%_includedir/gmic.h
%_includedir/gmic_libc.h
%_libdir/lib%name.so
%_libdir/libc%name.so

%if_enabled zart
%files zart
%_bindir/zart
%doc zart/README* zart/Licence_CeCILL_V2*
%endif

%files -n gimp-plugin-gmic
%gimpplugindir/plug-ins/*

%changelog
* Thu Aug 15 2019 Yuri N. Sedunov <aris@altlinux.org> 2.7.0-alt1
- 2.7.0

* Tue Jul 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.7-alt1
- 2.6.7

* Sat Jun 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.5-alt1
- 2.6.5

* Tue May 14 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Wed Mar 20 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.3-alt1
- 2.5.3

* Wed Jan 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.4.4-alt1
- 2.4.4

* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Sun Aug 19 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.4-alt1
- 2.3.4

* Fri Jun 29 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2

* Wed Jun 27 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Fri Apr 13 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Thu Jan 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt1
- 2.1.9

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.9.1-alt1
- 1.7.9.1

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.7.8-alt1
- 1.7.8

* Wed Jun 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2

* Wed May 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Apr 12 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt2
- fix build for non-x86 arches

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Fri Dec 18 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.8-alt1
- 1.6.8

* Sat Oct 31 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt1
- 1.6.7

* Mon Oct 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.6.1-alt1
- 1.6.6.1

* Tue Jun 23 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.5.0-alt1
- 1.6.5.0

* Fri May 29 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.3.1-alt1
- 1.6.3.1

* Mon Apr 06 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.1.0-alt1
- 1.6.1.0

* Wed Dec 24 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.0.3-alt1
- 1.6.0.3

* Thu Oct 09 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.0.1-alt1
- 1.6.0.1

* Thu Aug 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.0.0-alt1
- 1.6.0.0

* Sat Nov 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.7.2-alt1
- 1.5.7.2

* Mon Jan 28 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.3.0-alt1
- 1.5.3.0 (ALT #28117)

* Thu Sep 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.8-alt1.1
- Rebuilt with libopencv2.4

* Sun Jan 08 2012 Victor Forsiuk <force@altlinux.org> 1.5.0.8-alt1
- 1.5.0.8

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.7-alt1
- 1.5.0.7

* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.6-alt1
- 1.5.0.6

* Wed Aug 31 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.1-alt1
- 1.5.0.1

* Sun Aug 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.0-alt1.1
- Rebuilt with OpenCV 2.3.1

* Sun Jul 10 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.0-alt1
- 1.5.0.0

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 1.4.9.5-alt1
- 1.4.9.5

* Tue May 10 2011 Victor Forsiuk <force@altlinux.org> 1.4.9.2-alt1
- 1.4.9.2

* Mon Apr 04 2011 Victor Forsiuk <force@altlinux.org> 1.4.9.0-alt1
- 1.4.9.0

* Fri Mar 04 2011 Victor Forsiuk <force@altlinux.org> 1.4.8.2-alt1
- 1.4.8.2

* Mon Feb 21 2011 Victor Forsiuk <force@altlinux.org> 1.4.8.1-alt1
- 1.4.8.1
- Package bash completion file.

* Tue Feb 01 2011 Victor Forsiuk <force@altlinux.org> 1.4.7.4-alt1
- 1.4.7.4

* Wed Dec 01 2010 Victor Forsiuk <force@altlinux.org> 1.4.5.2-alt1
- 1.4.5.2
- Patched to build with libopencv2 (patch by real@).

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 1.4.1.0-alt1.1
- NMU: rebuild with new ImageMagick

* Thu Sep 09 2010 Victor Forsiuk <force@altlinux.org> 1.4.1.0-alt1
- 1.4.1.0

* Wed Jul 14 2010 Anton Farygin <rider@altlinux.ru> 1.3.4.0-alt1.1
- NMU: rebuild with new ImageMagick

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 1.3.4.0-alt1
- 1.3.4.0

* Mon Feb 22 2010 Victor Forsiuk <force@altlinux.org> 1.3.3.6-alt1
- 1.3.3.6

* Thu Nov 26 2009 Victor Forsyuk <force@altlinux.org> 1.3.3.0-alt1
- 1.3.3.0

* Wed Aug 26 2009 Victor Forsyuk <force@altlinux.org> 1.3.2.4-alt1
- 1.3.2.4

* Mon Jun 15 2009 Victor Forsyuk <force@altlinux.org> 1.3.2.0-alt1
- 1.3.2.0

* Thu Mar 19 2009 Victor Forsyuk <force@altlinux.org> 1.3.1.1-alt1
- 1.3.1.1

* Wed Mar 11 2009 Victor Forsyuk <force@altlinux.org> 1.3.0.4-alt1
- 1.3.0.4

* Tue Feb 17 2009 Victor Forsyuk <force@altlinux.org> 1.3.0.3-alt1
- Initial build.
