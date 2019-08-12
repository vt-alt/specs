Name: fotoxx
Version: 19.14
Release: alt1

Summary: Software for digital image editing, HDR composites, and panoramas
License: GPLv3+
Group: Graphics
Url: http://www.kornelix.com/%name/%name.html

# VCS: https://gitlab.com/fotoxx/fotoxx.git
Source: http://www.kornelix.com/downloads/downloads/%name-%version.tar.gz
Source1: fotoxx.desktop
Source2: fotoxx16.png
Source3: fotoxx32.png

Requires: %name-data = %version-%release

# fotoxx uses exiv2 executable to read EXIF data:
Requires: exiv2
# fotoxx uses xdg-open executable to launch HTML docs viewer:
Requires: xdg-utils

# needed to write images to CD/DVD
Requires: brasero

Provides: fotox
Obsoletes: fotox

BuildRequires: gcc-c++ libgtk+3-devel libtiff-devel libjpeg-devel liblcms2-devel
BuildRequires: perl-Image-ExifTool xdg-utils
BuildRequires: libchamplain-gtk3-devel libclutter-gtk3-devel libappstream-glib-devel
BuildRequires: libraw-devel

%description
Fotox is a program for improving digital photos. Navigate through large image
directories using a window of thumbnail images. Create HDR (high dynamic range)
images by combining bright and dark images to improve details visible in both
bright and dark areas. Create panorama (extra wide) images by joining overlapped
images. Adjust brightness and color intensity independently for different
underlying brightness levels. Reduce fog or haze by removing "whiteness" and
intensifying colors. Rotate an image (level a tilted image or turn 90 degrees).
Remove the red-eye effect from electronic flash photos. Resize or crop an image.

%package data
Summary: Arch independent files for Fotox
Group: Graphics
BuildArch: noarch

%description data
This package provides noarch data needed for Fotox to work.

%prep
%setup -n %name
chmod -x doc/*

%build
%make_build PREFIX=/usr CXXFLAGS="%optflags -D_FILE_OFFSET_BITS=64"

%install
install -d %buildroot%_man1dir
%make_install install DESTDIR=%buildroot PREFIX=%_prefix

install -pD -m644 %SOURCE1 %buildroot%_desktopdir/fotoxx.desktop
install -pD -m644 doc/fotoxx.man %buildroot%_man1dir/fotoxx.1
install -pD -m644 images/fotoxx.png %buildroot%_liconsdir/fotoxx.png
install -pD %_sourcedir/fotoxx32.png %buildroot%_niconsdir/fotoxx.png
install -pD %_sourcedir/fotoxx16.png %buildroot%_miconsdir/fotoxx.png

%files
%_bindir/%name

%files data
%_desktopdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_datadir/%name/
%_man1dir/*
%_datadir/appdata/%name.appdata.xml
%doc doc/README* doc/changelog doc/copyright

%exclude %_datadir/doc/%name

%changelog
* Sun Aug 11 2019 Yuri N. Sedunov <aris@altlinux.org> 19.14-alt1
- 19.14

* Mon Aug 05 2019 Yuri N. Sedunov <aris@altlinux.org> 19.13-alt1
- 19.13

* Sun Jun 02 2019 Yuri N. Sedunov <aris@altlinux.org> 19.12-alt1
- 19.12

* Sat May 11 2019 Yuri N. Sedunov <aris@altlinux.org> 19.11-alt1
- 19.11

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 19.10-alt1
- 19.10

* Wed Apr 17 2019 Yuri N. Sedunov <aris@altlinux.org> 19.9-alt1
- 19.9

* Sat Apr 13 2019 Yuri N. Sedunov <aris@altlinux.org> 19.8-alt1
- 19.8

* Wed Apr 03 2019 Yuri N. Sedunov <aris@altlinux.org> 19.7-alt1
- 19.7

* Sun Mar 17 2019 Yuri N. Sedunov <aris@altlinux.org> 19.6-alt1
- 19.6

* Mon Feb 25 2019 Yuri N. Sedunov <aris@altlinux.org> 19.5-alt1
- 19.5

* Wed Jan 30 2019 Yuri N. Sedunov <aris@altlinux.org> 19.4-alt1
- 19.4

* Wed Jan 30 2019 Yuri N. Sedunov <aris@altlinux.org> 19.3-alt1
- 19.3

* Wed Jan 16 2019 Yuri N. Sedunov <aris@altlinux.org> 19.1-alt1
- 19.1

* Mon Aug 06 2018 Yuri N. Sedunov <aris@altlinux.org> 18.07.1-alt2
- rebuilt against libraw.so.19

* Mon Jul 30 2018 Yuri N. Sedunov <aris@altlinux.org> 18.07.1-alt1
- 18.07.1

* Sun Jul 01 2018 Yuri N. Sedunov <aris@altlinux.org> 18.07-alt1
- 18.07

* Sat May 12 2018 Yuri N. Sedunov <aris@altlinux.org> 18.01.4-alt1
- 18.01.4

* Mon Feb 26 2018 Yuri N. Sedunov <aris@altlinux.org> 18.01.3-alt1
- 18.01.3

* Thu Jan 25 2018 Yuri N. Sedunov <aris@altlinux.org> 18.01.2-alt1
- 18.01.2

* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 18.01.1-alt1
- 18.01.1

* Thu Sep 07 2017 Yuri N. Sedunov <aris@altlinux.org> 17.08.3-alt1
- 17.08.3

* Wed Aug 02 2017 Yuri N. Sedunov <aris@altlinux.org> 17.08-alt1
- 17.08

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 17.04.3-alt1
- 17.04.3

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 17.04.2-alt1
- 17.04.2

* Mon Apr 17 2017 Yuri N. Sedunov <aris@altlinux.org> 17.04.1-alt1
- 17.04.1

* Thu Apr 06 2017 Yuri N. Sedunov <aris@altlinux.org> 17.04-alt1
- 17.04

* Sat Mar 04 2017 Yuri N. Sedunov <aris@altlinux.org> 17.01.2-alt1
- 17.01.2

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 17.01.1-alt1
- 17.01.1

* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 16.11.1-alt2
- rebuilt against libraw.so.16

* Mon Nov 28 2016 Yuri N. Sedunov <aris@altlinux.org> 16.11.1-alt1
- 16.11.1

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 16.09-alt1
- 16.09

* Wed Aug 24 2016 Yuri N. Sedunov <aris@altlinux.org> 16.08.1-alt1
- 16.08.1

* Mon Jun 06 2016 Yuri N. Sedunov <aris@altlinux.org> 16.06-alt1
- 16.06
- updated buildreqs

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 16.01.1-alt1
- 16.01.1

* Wed Dec 30 2015 Yuri N. Sedunov <aris@altlinux.org> 15.12.1-alt1
- 15.12.1

* Wed Jul 22 2015 Yuri N. Sedunov <aris@altlinux.org> 15.07-alt1
- 15.07

* Wed Jun 24 2015 Yuri N. Sedunov <aris@altlinux.org> 15.06-alt1
- 15.06

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 15.04.1-alt1
- 15.04.1

* Wed Mar 11 2015 Yuri N. Sedunov <aris@altlinux.org> 15.03.1-alt1
- 15.03.1

* Fri Nov 14 2014 Yuri N. Sedunov <aris@altlinux.org> 14.11-alt1
- 14.11

* Thu Oct 09 2014 Yuri N. Sedunov <aris@altlinux.org> 14.10.1-alt1
- 14.10.1

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 14.06-alt1
- 14.06

* Mon Feb 03 2014 Yuri N. Sedunov <aris@altlinux.org> 14.02.1-alt1
- 14.02.1

* Fri Jan 17 2014 Yuri N. Sedunov <aris@altlinux.org> 14.01.1-alt1
- 14.01.1

* Thu Dec 19 2013 Yuri N. Sedunov <aris@altlinux.org> 13.12-alt1
- 13.12

* Sun Apr 21 2013 Yuri N. Sedunov <aris@altlinux.org> 13.04.1-alt1
- 13.04.1
- updated buildreqs
- arch independent data moved to separate subpackage

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.04-alt1.1
- Rebuilt with libtiff5

* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 12.04-alt1
- 12.04

* Sat Mar 17 2012 Victor Forsiuk <force@altlinux.org> 12.03.2-alt1
- 12.03.2

* Mon Jan 02 2012 Victor Forsiuk <force@altlinux.org> 12.01-alt1
- 12.01

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 11.11.1-alt1
- 11.11.1

* Fri Sep 02 2011 Victor Forsiuk <force@altlinux.org> 11.09-alt1
- 11.09

* Sun Jul 31 2011 Victor Forsiuk <force@altlinux.org> 11.08-alt1
- 11.08

* Sun Jun 12 2011 Victor Forsiuk <force@altlinux.org> 11.06.1-alt1
- 11.06.1

* Thu May 05 2011 Victor Forsiuk <force@altlinux.org> 11.05.1-alt1
- 11.05.1

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 11.04-alt1
- 11.04

* Tue Mar 29 2011 Victor Forsiuk <force@altlinux.org> 11.03.1-alt1
- 11.03.1

* Fri Mar 04 2011 Victor Forsiuk <force@altlinux.org> 11.03-alt1
- 11.03

* Wed Feb 02 2011 Victor Forsiuk <force@altlinux.org> 11.02-alt1
- 11.02

* Thu Jan 13 2011 Victor Forsiuk <force@altlinux.org> 11.01.2-alt1
- 11.01.2

* Thu Nov 25 2010 Victor Forsiuk <force@altlinux.org> 10.11.2-alt1
- 10.11.2

* Mon Oct 18 2010 Victor Forsiuk <force@altlinux.org> 10.10.3-alt1
- 10.10.3

* Mon Sep 13 2010 Victor Forsiuk <force@altlinux.org> 10.9.1-alt1
- 10.9.1

* Wed Sep 08 2010 Victor Forsiuk <force@altlinux.org> 10.9-alt1
- 10.9

* Fri Aug 20 2010 Victor Forsiuk <force@altlinux.org> 10.8.4-alt1
- 10.8.4

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 10.8.3-alt1
- 10.8.3

* Mon Jul 12 2010 Victor Forsiuk <force@altlinux.org> 10.7-alt1
- 10.7

* Fri Jun 18 2010 Victor Forsiuk <force@altlinux.org> 10.6.1-alt1
- 10.6.1

* Mon May 31 2010 Victor Forsiuk <force@altlinux.org> 10.4-alt1
- 10.4

* Tue Apr 06 2010 Victor Forsiuk <force@altlinux.org> 10.0-alt1
- 10.0

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 9.9-alt1
- 9.9

* Thu Mar 25 2010 Victor Forsiuk <force@altlinux.org> 9.8.1-alt1
- 9.8.1

* Mon Mar 22 2010 Victor Forsiuk <force@altlinux.org> 9.8-alt1
- 9.8

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 9.7-alt1
- 9.7

* Thu Feb 25 2010 Victor Forsiuk <force@altlinux.org> 9.6-alt1
- 9.6

* Wed Feb 03 2010 Victor Forsyuk <force@altlinux.org> 9.5-alt1
- 9.5

* Fri Jan 22 2010 Victor Forsyuk <force@altlinux.org> 9.4-alt1
- 9.4

* Thu Jan 14 2010 Victor Forsyuk <force@altlinux.org> 9.3-alt1
- 9.3

* Sat Dec 26 2009 Victor Forsyuk <force@altlinux.org> 9.1-alt1
- 9.1

* Mon Dec 14 2009 Victor Forsyuk <force@altlinux.org> 9.0-alt1
- 9.0

* Wed Oct 21 2009 Victor Forsyuk <force@altlinux.org> 8.6-alt1
- 8.6

* Sun Oct 11 2009 Victor Forsyuk <force@altlinux.org> 8.5.2-alt1
- 8.5.2

* Tue Sep 22 2009 Victor Forsyuk <force@altlinux.org> 8.4.3-alt1
- 8.4.3

* Thu Sep 03 2009 Victor Forsyuk <force@altlinux.org> 8.3-alt1
- 8.3
- Added %%f field code to .desktop's Exec key.

* Tue Aug 04 2009 Victor Forsyuk <force@altlinux.org> 8.0-alt1
- 8.0

* Thu Jul 23 2009 Victor Forsyuk <force@altlinux.org> 7.7-alt1
- 7.7

* Wed Jul 01 2009 Victor Forsyuk <force@altlinux.org> 7.4.1-alt1
- 7.4.1

* Wed Mar 11 2009 Victor Forsyuk <force@altlinux.org> 6.1.1-alt1
- 6.1.1

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 5.6.1-alt1
- 5.6.1

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 5.3.1-alt1
- 5.3.1

* Tue Sep 23 2008 Victor Forsyuk <force@altlinux.org> 5.3-alt1
- 5.3

* Mon Sep 15 2008 Victor Forsyuk <force@altlinux.org> 5.2.4-alt1
- 5.2.4

* Wed May 21 2008 Victor Forsyuk <force@altlinux.org> 42-alt1
- Version 42.

* Thu Mar 27 2008 Victor Forsyuk <force@altlinux.org> 37-alt1
- Version 37.

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 36-alt1
- Version 36.

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 33-alt1
- Initial build.
