%define _cups_serverbin %_libexecdir/cups
%global _localstatedir %_var

Name: cups-filters
Version: 1.27.4
Release: alt2

Summary: OpenPrinting CUPS filters and backends
# For a breakdown of the licensing, see COPYING file
# GPLv2:   filters: commandto*, imagetoraster, pdftops, rasterto*,
#                   imagetopdf, pstopdf, texttopdf
#         backends: parallel, serial
# GPLv2+:  filters: textonly, texttops, imagetops
# GPLv3:   filters: bannertopdf
# MIT:     filters: pdftoijs, pdftoopvp, pdftopdf, pdftoraster
License: GPLv2 and GPLv2+ and GPLv3 and MIT
Group: System/Servers

Url: http://www.linuxfoundation.org/collaborate/workgroups/openprinting/pdf_as_standard_print_job_format
Source0: http://www.openprinting.org/download/cups-filters/cups-filters-%version.tar
Source1: %name.watch
Source2: cups-browsed.init
Source3: default-testpage.pdf
Patch0: %name-alt.patch
Patch1: %name-braille-indexv4-path.patch
Patch2: %name-pjl-as-ps.patch

Conflicts: cups < 1.6.1-alt1
Conflicts: ghostscript-cups
Obsoletes: ghostscript-cups
Provides: ghostscript-cups
Obsoletes: foomatic-filters
Provides: foomatic-filters
Conflicts: foomatic-filters

BuildRequires: cups-devel
BuildRequires: libdbus-devel
BuildRequires: libldap-devel
# pdftopdf
BuildRequires: libqpdf-devel >= 8.1.0
# pdftops
BuildRequires: poppler-utils
# pdftoijs, pdftoopvp, pdftoraster
BuildRequires: libpoppler-devel libpoppler-cpp-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libijs-devel
BuildRequires: glib2-devel
BuildRequires: libgs-devel
BuildRequires: libfreetype-devel
BuildRequires: fontconfig-devel
BuildRequires: liblcms2-devel
BuildRequires: libgio-devel
BuildRequires: libavahi-devel libavahi-glib-devel
# for tests
BuildRequires: fonts-ttf-dejavu

# Make sure we get postscriptdriver tags.
BuildRequires: python3-module-cups

Requires: poppler-utils
Requires: /usr/bin/gs

%package libs
Summary: OpenPrinting CUPS filters and backends - cupsfilters and fontembed libraries
Group: System/Libraries
# LGPLv2: libcupsfilters
# MIT:    libfontembed
License: LGPLv2 and MIT

%package devel
Summary: OpenPrinting CUPS filters and backends - development environment
Group: Development/C
License: LGPLv2 and MIT
Requires: cups-filters-libs = %version-%release

%description
Contains backends, filters, and other software that was
once part of the core CUPS distribution but is no longer maintained by
Apple Inc. In addition it contains additional filters developed
independently of Apple, especially filters for the PDF-centric printing
workflow introduced by OpenPrinting.

%description libs
This package provides cupsfilters and fontembed libraries.

%description devel
This is the development package for OpenPrinting CUPS filters and backends.


%package -n cups-backend-serial
Epoch: 1
Summary: serial backend for cups
License: GPLv2
Group: System/Servers

%description -n cups-backend-serial
serial backend for cups

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
./autogen.sh

# --with-pdftops=pdftops - use Poppler instead of Ghostscript (see README)
%configure --disable-static \
           --disable-silent-rules \
	   --disable-mutool \
	   --without-php \
	   --with-rcdir=no \
	   --enable-driverless \
	   --enable-pclm \
	   --enable-auto-setup-driverless-only \
	   --with-gs-path=/usr/bin/gs \
	   --enable-opvp \
	   --enable-dbus \
	   --with-test-font-path=/usr/share/fonts/ttf/dejavu/DejaVuSans.ttf \
	   --with-pdftops=hybrid

%make

%check
make check

%install
%make install DESTDIR=%buildroot
install -D -m 755 %SOURCE2 %buildroot/%_initdir/cups-browsed
mkdir -p %buildroot/%_unitdir/
install -m 644 utils/cups-browsed.service %buildroot/%_unitdir/
ln -sf ../lib/cups/filter/foomatic-rip %buildroot/%_bindir/foomatic-rip
rm -rf %buildroot%_docdir/%name
install -D -m 644 %SOURCE3 %buildroot/%_datadir/cups/data/


%files
%doc README AUTHORS NEWS
%config(noreplace) %_sysconfdir/cups/cups-browsed.conf
%config(noreplace) %_initdir/cups-browsed
%attr(0755,root,root) %_cups_serverbin/filter/*
%attr(0755,root,root) %_cups_serverbin/driver/*
%attr(0755,root,root) %_cups_serverbin/backend/parallel
%attr(0755,root,root) %_cups_serverbin/backend/beh
%attr(0755,root,root) %_cups_serverbin/backend/implicitclass
%attr(0755,root,root) %_cups_serverbin/backend/driverless
%attr(0755,root,root) %_cups_serverbin/backend/cups-brf
%_datadir/cups/banners
%_datadir/cups/charsets
%_datadir/cups/braille
%_datadir/cups/data/*
%_datadir/cups/ppdc/*
%_datadir/cups/drv/cupsfilters.drv
%_datadir/cups/drv/generic-brf.drv
%_datadir/cups/drv/generic-ubrl.drv
%_datadir/cups/drv/indexv3.drv
%_datadir/cups/drv/indexv4.drv
%_datadir/cups/mime/braille.types
%_datadir/cups/mime/braille.convs
%_datadir/cups/mime/cupsfilters.types
%_datadir/cups/mime/cupsfilters.convs
%_datadir/cups/mime/cupsfilters-poppler.convs
%_datadir/cups/mime/cupsfilters-ghostscript.convs
%_datadir/ppd/cupsfilters
%_bindir/ttfread
%_bindir/foomatic-rip
%_bindir/driverless
%_sbindir/cups-browsed
%_datadir/man/man*/*
%_unitdir/*

%files -n cups-backend-serial
%attr(0700,root,root) %_prefix/lib/cups/backend/serial

%files libs
%doc COPYING fontembed/README
%attr(0755,root,root) %_libdir/libcupsfilters.so.*
%attr(0755,root,root) %_libdir/libfontembed.so.*

%files devel
%_includedir/cupsfilters
%_includedir/fontembed
%_libdir/pkgconfig/libcupsfilters.pc
%_libdir/pkgconfig/libfontembed.pc
%_libdir/libcupsfilters.so
%_libdir/libfontembed.so

%changelog
* Thu May 28 2020 Anton Farygin <rider@altlinux.ru> 1.27.4-alt2
- changed the default behavior: autosetup is only for driverless printers

* Mon Apr 13 2020 Anton Farygin <rider@altlinux.ru> 1.27.4-alt1
- new version 1.27.4

* Mon Mar 23 2020 Anton Farygin <rider@altlinux.ru> 1.27.3-alt1
- new version 1.27.3

* Fri Mar 13 2020 Anton Farygin <rider@altlinux.ru> 1.27.2-alt1
- new version 1.27.2

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 1.27.1-alt1
- new version 1.27.1

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 1.27.0-alt1
- new version 1.27.0

* Wed Jan 15 2020 Anton Farygin <rider@altlinux.ru> 1.26.2-alt1
- new version 1.26.2

* Fri Jan 10 2020 Anton Farygin <rider@altlinux.ru> 1.26.1-alt1
- new version 1.26.1

* Tue Dec 17 2019 Anton Farygin <rider@altlinux.ru> 1.26.0-alt1
- new version 1.26.0

* Mon Dec 02 2019 Anton Farygin <rider@altlinux.ru> 1.25.13-alt1
- new version 1.25.13

* Thu Nov 14 2019 Anton Farygin <rider@altlinux.ru> 1.25.12-alt1
- new version 1.25.12

* Mon Oct 28 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.25.11-alt2
- new default testpage

* Fri Oct 11 2019 Anton Farygin <rider@altlinux.ru> 1.25.11-alt1
- new version 1.25.11

* Wed Sep 25 2019 Anton Farygin <rider@altlinux.ru> 1.25.6-alt1
- new version 1.25.6

* Tue Sep 10 2019 Anton Farygin <rider@altlinux.ru> 1.25.5-alt1
- new version 1.25.5
- enabled tests
- built with pclm support

* Tue Sep 03 2019 Anton Farygin <rider@altlinux.ru> 1.25.4-alt2
- fixed build with qpdf-9.0.0
- cleanup patches

* Sun Sep 01 2019 Anton Farygin <rider@altlinux.ru> 1.25.4-alt1
- new version 1.25.4

* Fri Aug 23 2019 Anton Farygin <rider@altlinux.ru> 1.25.3-alt1
- new version 1.25.3

* Sun Aug 18 2019 Anton Farygin <rider@altlinux.ru> 1.25.2-alt1
- new version 1.25.2

* Wed Jul 24 2019 Anton Farygin <rider@altlinux.ru> 1.25.1-alt1
- new version 1.25.1

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 1.25.0-alt1
- new version 1.25.0

* Wed Jun 05 2019 Anton Farygin <rider@altlinux.ru> 1.24.0-alt1
- new version 1.24.0

* Tue Apr 09 2019 Anton Farygin <rider@altlinux.ru> 1.22.5-alt1
- new version 1.22.5

* Sun Apr 07 2019 Anton Farygin <rider@altlinux.ru> 1.22.4-alt1
- new version 1.22.4

* Thu Mar 28 2019 Anton Farygin <rider@altlinux.ru> 1.22.3-alt1
- new version 1.22.3

* Sun Mar 17 2019 Anton Farygin <rider@altlinux.ru> 1.22.2-alt1
- new version 1.22.2

* Fri Mar 08 2019 Anton Farygin <rider@altlinux.ru> 1.22.1-alt2
- clenup spec (removed php5 support)

* Thu Feb 28 2019 Anton Farygin <rider@altlinux.ru> 1.22.1-alt1
- new version 1.22.1

* Wed Feb 13 2019 Anton Farygin <rider@altlinux.ru> 1.22.0-alt2
- fixed build with poppler 0.74

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.22.0-alt1
- 1.22.0
- enabled opvp filter
- disabled mutool (changed to qpdf)
- pdftops renderer changed to hybrid (for better support printers from Brother,
  Minolta, and Konica Minolta)
- added generic UBRL braille ppd
- added backend for Virtual Braille BRF Printer

* Fri Dec 21 2018 Anton Farygin <rider@altlinux.ru> 1.21.6-alt1
- new version 1.21.6

* Fri Dec 07 2018 Anton Farygin <rider@altlinux.ru> 1.21.5-alt1
- new version 1.21.5

* Mon Nov 26 2018 Anton Farygin <rider@altlinux.ru> 1.21.4-alt1
- new version 1.21.4

* Wed Oct 24 2018 Anton Farygin <rider@altlinux.ru> 1.21.3-alt2
- disabled build of the php extension, due to end of life for php-5 at december 2018

* Sat Oct 06 2018 Anton Farygin <rider@altlinux.ru> 1.21.3-alt1
- new version 1.21.3

* Sat Sep 22 2018 Anton Farygin <rider@altlinux.ru> 1.21.2-alt2
- rebuilt with php5-5.6.38

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 1.21.2-alt1
- new version 1.21.2

* Sun Sep 02 2018 Anton Farygin <rider@altlinux.ru> 1.21.1-alt1
- new version 1.21.1

* Mon Aug 20 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.20.4-alt3
- handling Postscript with PJH heading fixed

* Tue Jul 31 2018 Anton Farygin <rider@altlinux.ru> 1.20.4-alt2
- rebuilt for php5-5.6.37

* Tue Jul 17 2018 Anton Farygin <rider@altlinux.ru> 1.20.4-alt1
- new version 1.20.4

* Fri May 11 2018 Anton Farygin <rider@altlinux.ru> 1.20.3-alt2
- rebuilt for php5-5.6.36

* Sat Apr 21 2018 Anton Farygin <rider@altlinux.ru> 1.20.3-alt1
- new version 1.20.3

* Tue Apr 03 2018 Anton Farygin <rider@altlinux.ru> 1.20.2-alt1
- new version 1.20.2

* Fri Mar 02 2018 Anton Farygin <rider@altlinux.ru> 1.20.1-alt1
- new version 1.20.1

* Mon Feb 12 2018 Anton Farygin <rider@altlinux.ru> 1.20.0-alt1
- new version 1.20.0

* Mon Jan 29 2018 Anton Farygin <rider@altlinux.ru> 1.19.0-alt1
- new version 1.19.0

* Fri Nov 03 2017 Anton Farygin <rider@altlinux.ru> 1.17.9-alt3
- rebuilt for php5-5.6.32

* Thu Oct 26 2017 Anton Farygin <rider@altlinux.ru> 1.17.9-alt2
- use /var for localstatedir

* Mon Oct 09 2017 Anton Farygin <rider@altlinux.ru> 1.17.9-alt1
- new version 1.17.9

* Sat Oct 07 2017 Michael Shigorin <mike@altlinux.org> 1.17.8-alt2
- introduced php knob (on by default)

* Mon Oct 02 2017 Anton Farygin <rider@altlinux.ru> 1.17.8-alt1
- new version 1.17.8

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 1.17.7-alt1
- new version 1.17.7
- build with ldap
- enabled auto-setup for driverless printers

* Tue Aug 22 2017 Anton Farygin <rider@altlinux.ru> 1.16.3-alt1
- new version 1.16.3

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 1.16.2-alt1
- new version 1.16.2

* Mon Aug 14 2017 Anton Farygin <rider@altlinux.ru> 1.16.1-alt1
- new version 1.16.1

* Fri Aug 04 2017 Anton Farygin <rider@altlinux.ru> 1.16.0-alt1
- new version 1.16.0

* Fri Jul 07 2017 Anton Farygin <rider@altlinux.ru> 1.14.1-alt2
- rebuild with new php

* Mon Jul 03 2017 Anton Farygin <rider@altlinux.ru> 1.14.1-alt1
- new version 1.14.1

* Wed May 24 2017 Anton Farygin <rider@altlinux.ru> 1.14.0-alt1
- new version 1.14.0

* Tue May 02 2017 Anton Farygin <rider@altlinux.ru> 1.13.5-alt1
- new version

* Tue Mar 07 2017 Anton Farygin <rider@altlinux.ru> 1.13.4-alt1
- new version 1.13.4

* Mon Jan 30 2017 Anton Farygin <rider@altlinux.ru> 1.13.3-alt1
- new version 1.13.3

* Fri Dec 30 2016 Anton Farygin <rider@altlinux.ru> 1.13.2-alt1
- new version 1.13.2

* Mon Dec 19 2016 Anton Farygin <rider@altlinux.ru> 1.13.1-alt1
- new version 1.13.1

* Wed Dec 14 2016 Anton Farygin <rider@altlinux.ru> 1.13.0-alt1
- new version 1.13.0

* Wed Dec 07 2016 Anton Farygin <rider@altlinux.ru> 1.12.0-alt1
- new version 1.12.0

* Wed Nov 16 2016 Anton Farygin <rider@altlinux.ru> 1.11.6-alt1
- new version 1.11.6

* Wed Nov 16 2016 Anton Farygin <rider@altlinux.ru> 1.11.4-alt3
- rebuild with new PHP

* Mon Oct 17 2016 Anton Farygin <rider@altlinux.ru> 1.11.4-alt2
- rebuild with new PHP

* Mon Sep 26 2016 Anton Farygin <rider@altlinux.ru> 1.11.4-alt1
- new version 1.11.4

* Fri Aug 26 2016 Anton Farygin <rider@altlinux.ru> 1.11.1-alt1
- new version 1.11.1

* Mon Jul 25 2016 Anton Farygin <rider@altlinux.ru> 1.10.0-alt2
- rebuild with php5-5.6.24

* Thu Jul 21 2016 Anton Farygin <rider@altlinux.ru> 1.10.0-alt1
- new version 1.10.0

* Mon Jun 27 2016 Anton Farygin <rider@altlinux.ru> 1.9.0-alt2
- rebuild with php5-5.6.23

* Thu Jun 16 2016 Anton Farygin <rider@altlinux.ru> 1.9.0-alt1
- new version 1.9.0
- build with avahi

* Mon May 30 2016 Anton Farygin <rider@altlinux.ru> 1.0.76-alt6
- rebuild with php5-5.6.22

* Tue May 10 2016 Anton Farygin <rider@altlinux.ru> 1.0.76-alt5
- rebuild with php5-5.6.21

* Tue Apr 05 2016 Anton Farygin <rider@altlinux.ru> 1.0.76-alt4
- rebuild with php5-5.6.20

* Mon Mar 28 2016 Anton Farygin <rider@altlinux.ru> 1.0.76-alt3
- rebuild with php5-5.6.19

* Mon Dec 21 2015 Anton Farygin <rider@altlinux.ru> 1.0.76-alt2
- rebuild with php5-5.6.16

* Mon Oct 19 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.76-alt1
- new version 1.0.76

* Tue Jul 14 2015 Anton Farygin <rider@altlinux.ru> 1.0.71-alt1
- new version 1.0.71

* Thu May 28 2015 Anton Farygin <rider@altlinux.ru> 1.0.68-alt4
- rebuild in new environment

* Mon May 18 2015 Anton Farygin <rider@altlinux.ru> 1.0.68-alt3
- rebuild with php5-5.5.25

* Fri Apr 24 2015 Anton Farygin <rider@altlinux.ru> 1.0.68-alt2
- rebuild for new php-5.5.24

* Wed Apr 15 2015 Anton Farygin <rider@altlinux.ru> 1.0.68-alt1
- new version 1.0.68

* Fri Mar 13 2015 Anton Farygin <rider@altlinux.ru> 1.0.67-alt1
- new version 1.0.67

* Mon Mar 02 2015 Anton Farygin <rider@altlinux.ru> 1.0.66-alt1
- new version 1.0.66

* Tue Feb 24 2015 Anton Farygin <rider@altlinux.ru> 1.0.65-alt1
- new version 1.0.65

* Fri Jan 23 2015 Anton Farygin <rider@altlinux.ru> 1.0.62-alt2
- rebuild with php-5.5.21

* Fri Jan 16 2015 Anton Farygin <rider@altlinux.ru> 1.0.62-alt1
- new version 1.0.62

* Thu Jan 15 2015 Anton Farygin <rider@altlinux.ru> 1.0.61-alt3
- rebuild with php-5.5.20

* Thu Nov 20 2014 Anton Farygin <rider@altlinux.ru> 1.0.61-alt2
- rebuild with new php

* Tue Oct 14 2014 Anton Farygin <rider@altlinux.ru> 1.0.61-alt1
- new version 1.0.61

* Mon Oct 06 2014 Anton Farygin <rider@altlinux.ru> 1.0.59-alt1
- new version 1.0.59

* Wed Sep 10 2014 Anton Farygin <rider@altlinux.ru> 1.0.58-alt2
- rebuild with php-5.5.16

* Mon Sep 08 2014 Anton Farygin <rider@altlinux.ru> 1.0.58-alt1
- new version 1.0.58

* Thu Jun 19 2014 Anton Farygin <rider@altlinux.ru> 1.0.54-alt3
- exclude snapshot in watch file

* Wed Jun 18 2014 Anton Farygin <rider@altlinux.ru> 1.0.54-alt2
- rebuld with php-5.5.13

* Mon Jun 16 2014 Anton Farygin <rider@altlinux.ru> 1.0.54-alt1
- new version 1.0.54

* Fri May 16 2014 Anton Farygin <rider@altlinux.ru> 1.0.53-alt1
- new version

* Tue Apr 08 2014 Anton Farygin <rider@altlinux.ru> 1.0.52-alt1
- new version

* Fri Mar 28 2014 Anton Farygin <rider@altlinux.ru> 1.0.50-alt1
- new version
- watch file added
- initscript added (closes: #29524)

* Fri Mar 21 2014 Anton Farygin <rider@altlinux.ru> 1.0.48-alt2
- rebuild with php-5.5.10

* Thu Mar 13 2014 Anton Farygin <rider@altlinux.ru> 1.0.48-alt1
- new version

* Wed Mar 12 2014 Anton Farygin <rider@altlinux.ru> 1.0.47-alt1
- new version with security fixes: CVE-2013-6474, CVE-2013-6475,
  CVE-2013-6476 and CVE-2013-6473
- fixed ghostscript path (closes: #29884)

* Wed Feb 26 2014 Anton Farygin <rider@altlinux.ru> 1.0.46-alt1
- new version

* Tue Nov 05 2013 Andriy Stepanov <stanv@altlinux.ru> 1.0.41-alt2
- ghostsctip filters, add bannertopdf as PDF form

* Thu Oct 31 2013 Anton Farygin <rider@altlinux.ru> 1.0.41-alt1
- new version

* Tue Oct 29 2013 Fr. Br. George <george@altlinux.ru> 1.0.40-alt1.1
- Make serial backend root-only (Closes: #24172)

* Tue Oct 15 2013 Anton Farygin <rider@altlinux.ru> 1.0.40-alt1
- new version

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 1.0.39-alt1
- new version

* Tue Sep 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.38-alt2
- conflict with ghostscript-cups resolved

* Mon Sep 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.38-alt1
- update to 1.0.38
- cups-browsed packaged

* Fri Jul 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt4.2
- Rebuild with php5-5.4.17.20130704

* Sat May 18 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.31-alt4.1
- Rebuild with php5-5.3.24.20130412-alt1

* Mon May 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt4
- rebuild with php5-5.3.25.20130512-alt1

* Tue Apr 23 2013 Anton Farygin <rider@altlinux.ru> 1.0.31-alt3
- rebuild with new poppler35

* Fri Apr 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt2
- rebuild with php5-5.3.24.20130412-alt1

* Wed Apr 03 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt1
- updated from upstream (closes: #28783)
- rebuild with php5-5.3.23.20130314-alt1

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt3
- rebuild with php5-5.3.18.20121017-alt1

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt2
- rebuild with php5-5.3.17.20120913-alt1

* Tue Sep 18 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt1
- first build for Sisyphus, based on RH spec
