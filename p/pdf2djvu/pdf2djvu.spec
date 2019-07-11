Name: pdf2djvu
Version: 0.9.13
Release: alt1

Summary: PDF to DjVu converter
License: GPLv2
Group: Office
Url: http://jwilk.net/software/pdf2djvu/
# https://github.com/jwilk/pdf2djvu/releases/download/%version/%name-%version.tar.xz
Source: %name-%version.tar
Requires: djvu-utils
# Automatically added by buildreq on Fri Nov 19 2010
BuildRequires: djvu-utils fontconfig-devel gcc-c++ libGraphicsMagick-c++-devel libdjvu-devel libgomp-devel libpoppler-devel libxslt-devel pstreams

%description
pdf2djvu creates DjVu files from PDF files. It's able to extract:
- graphics,
- text layer,
- hyperlinks,
- document outline (bookmarks),
- metadata (including XMP metadata).

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc doc/COPYING doc/changelog
%_bindir/*
%_man1dir/*

%changelog
* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 0.9.13-alt1
- new version

* Sat Feb 23 2019 Ivan A. Melnikov <iv@altlinux.org> 0.9.12-alt1
- 0.9.12

* Thu Nov 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.11-alt1
- 0.9.11

* Thu Aug 09 2018 Vladislav Zavjalov <slazav@altlinux.org> 0.9.10-alt1
- new version

* Thu Oct 26 2017 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt1
- new version

* Mon Apr 04 2016 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt3
- rebuilt with new poppler

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt2
- rebuilt with new poppler

* Tue Sep 08 2015 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.21-alt2
- rebuilt with new poppler

* Thu May 14 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.21-alt1
- new version

* Mon Dec 01 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.17-alt4
- rebuilt with new poppler

* Wed Jul 09 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.17-alt3
- rebuilt with new poppler

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.17-alt2
- rebuilt with new poppler

* Thu Nov 21 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.17-alt0.M70P.1
- built for M70P

* Thu Nov 21 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.17-alt1
- new version (ALT#29600)

* Wed Apr 24 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.16-alt1.1
- NMU: rebuilt with new poppler

* Mon Apr 08 2013 L.A. Kostis <lakostis@altlinux.ru> 0.7.16-alt1
- Updated to 0.7.16.

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.14-alt1
- Version 0.7.14

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.13-alt1
- Version 0.7.13

* Sat Nov 26 2011 L.A. Kostis <lakostis@altlinux.ru> 0.7.11-alt1
- Updated to 0.7.11.

* Tue Apr 26 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.7-alt1
- Updated to 0.7.7.

* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.4-alt1
- Enabled OpenMP support.
- Updated build requirements.
- Rebuilt for libpoppler.so.7.

* Mon Aug 16 2010 L.A. Kostis <lakostis@altlinux.ru> 0.7.4-alt0.1
- 0.7.4.

* Sat Jan 23 2010 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt0.1.1
- Rebuild w/ new GraphicsMagick.

* Thu Nov 05 2009 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt0.1
- 0.6.0.
- Optimize buildrequires, .spec cleanup.
- Change packager.

* Sun Mar 15 2009 L.A. Kostis <lakostis@altlinux.ru> 0.4.12-alt2.1
- NMU: rebuild with new libdjvu.

* Thu Mar 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.4.12-alt2
- Rebuild with new libdjvu

* Sat Sep 20 2008 Vladimir Scherbaev <vladimir@altlinux.org> 0.4.12-alt1
- Initial build
