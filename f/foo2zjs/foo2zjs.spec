Name: foo2zjs
Version: 20200207
Release: alt1

Summary: ZJS (some HP/Minolta) printer driver
Summary(ru_RU.UTF8): ZJS драйвер для некоторых принтеров HP/Minolta
License: GPL
Group: System/Configuration/Printing

Url: http://foo2zjs.rkkda.com

Requires: wget cups udev foomatic-filters psutils
Requires: foomatic-db-%name = %version-%release
Requires: %name-PPD = %version-%release

Source0: %name.tar.gz
Source1: README-UTF8.ALT
Source2: foo2zjs_download_fw
Source3: hplj1020.desktop
Source4: hplj1020-16.png
Source5: hplj1020-32.png
Source6: hplj1020-48.png
Source7: hplj10xx.rules

Patch1: foo2zjs.make_20140611.patch
Patch2: foo2zjs.hplj1000_20120714.patch
Patch3: hplj10xx_gui.tcl_20100505.patch
Patch4: foo2zjs.getweb_20140104.patch

Packager: Evgeny V Shishkov <shev@altlinux.org>

# Automatically added by buildreq on Mon Jan 26 2009 (-bi)
BuildRequires: foomatic-filters ghostscript-classic ghostscript-utils ghostscript-module-X groff-ps iputils psutils unzip bc
BuildRequires: libcups-devel

%package -n %name-apps
BuildArch: noarch
Summary: foo2zjs utilities
Summary(ru_RU.UTF8): foo2zjs утилиты
Group: System/Configuration/Printing
Requires: %name = %version-%release
Requires: tcl-tix
Requires: tk >= 8.4

%package -n %name-fwdownloader
BuildArch: noarch
Summary: foo2zjs firmware auto downloader from Internet
Summary(ru_RU.UTF8): foo2zjs автозагрузчик прошивок c интернета
Group: System/Configuration/Printing
Requires: %name = %version-%release
Requires: iputils

%package -n foomatic-db-%name
BuildArch: noarch
Summary: Printers database which supports foo2zjs
Summary(ru_RU.UTF8): База данных принтеров, которые поддерживает foo2zjs
Group: System/Configuration/Printing

%package -n %name-PPD
BuildArch: noarch
Summary: PostScript Printer Description (PPD) files foo2zjs
Summary(ru_RU.UTF8): Файлы PostScript Printer Description (PPD) foo2zjs
Group: System/Configuration/Printing

%description -n %name-apps
Application HP LaserJet 10xx Replaced Paper

%description -l ru_RU.UTF-8 -n %name-apps
Программа для замены бумаги в HP LaserJet 10XX
Запускается при отсутствии бумаги в принтере (естественно предварительно бумагу надо положить в лоток).

%description -n %name-fwdownloader
ATTENTION! Think before you install this package.

This package contains a program to automatically download the firmware (if absent)
from the Internet without warning and your participation.

%description -l ru_RU.UTF-8 -n %name-fwdownloader
ВНИМАНИЕ!!! Подумайте, прежде чем устанавливать данный пакет.

Данный пакет содержит программу для автоматической загрузки прошивки (если она отсутствует)
из сети Internet БЕЗ ПРЕДУПРЕЖДЕНИЯ И ВАШЕГО УЧАСТИЯ.

%description -n foomatic-db-%name
Printers database which supports foo2zjs

%description -l ru_RU.UTF-8 -n foomatic-db-%name
База данных принтеров, которые поддерживает foo2zjs

%description -n  %name-PPD
PostScript Printer Description (PPD) files foo2zjs

%description -l ru_RU.UTF-8 -n %name-PPD
Файлы PostScript Printer Description (PPD) foo2zjs

%description
This package contains %name drivers for printers using ZjStream
wire protocol, including:

foo2zjs:
* Minolta/QMS magicolor 2200 DL / 2300 DL
* Konica Minolta magicolor 2430 DL
* Minolta Color PageWorks/Pro L
* HP LaserJet 1000 / 1005 / 1018 / 1020 / 1022 / 1022n / 1022nw / P2035 / M1319 MFP (PRINTER ONLY; Alpha Quality)
* HP LaserJet Pro P1102 / P1102w / P1566 / P1606dn / CP1025nw

foo2xqx:
* HP LaserJet P1005 / P1006 / P1007 / P1008 / P2014 / P2014n / P1505 / P1505n / P2014n / P2035n
* HP LaserJet M1005MFP (PRINTER ONLY) / M1120MFP (PRINTER ONLY)

foo2hp:
* HP Color LaserJet CP1215 / 1600 / 2600n

foo2lava/LAVAFLOW:
* Konica Minolta magicolor 2490 MF / 2530 DL / 1600W / 1680MF / 1690MF / 2480MF / 4690MF
* Xerox Phaser 6115MFP / 6121MFP

foo2qpdl:
* Samsung CLP-300 / CLP-310 / CLP-315 / CLP-325 / CLP-325W / CLP-600 / CLP-610 / CLP-620 / CLX-2160 / CLX-3160 / CLX-3175
* Xerox Phaser 6110 / 6110MFP

foo2slx:
* Lexmark C500n

foo2hiperc:
* Oki C110 / C310dn / C3100n / C3200n / C3300n / C3400n / C3530n MFP (PRINT ONLY) / C5100n / C5150n / C5200n / C5500n / C5600n / C5650 / C5800n
* Olivetti d-Color P160W

foo2oak:
* HP Color LaserJet 1500 (ALPHA QUALITY)
* Kyocera Mita KM-1635 (ALPHA QUALITY) / KM-2035 (ALPHA QUALITY)

%description -l ru_RU.UTF-8
Этот пакет содержит %name драйвера для принтеров использующих ZjStream протокол, в их числе:

foo2zjs:
* Minolta/QMS magicolor 2200 DL / 2300 DL
* Konica Minolta magicolor 2430 DL
* Minolta Color PageWorks/Pro L
* HP LaserJet 1000 / 1005 / 1018 / 1020 / 1022 / 1022n / 1022nw / P2035 / M1319 MFP (PRINTER ONLY; Alpha Quality)
* HP LaserJet Pro P1102 / P1102w / P1566 / P1606dn / CP1025nw

foo2xqx:
* HP LaserJet P1005 / P1006 / P1007 / P1008 / P2014 / P2014n / P1505 / P1505n / P2014n / P2035n
* HP LaserJet M1005MFP (PRINTER ONLY) / M1120MFP (PRINTER ONLY)

foo2hp:
* HP Color LaserJet CP1215 / 1600 / 2600n

foo2lava/LAVAFLOW:
* Konica Minolta magicolor 2490 MF / 2530 DL / 1600W / 1680MF / 1690MF / 2480MF / 4690MF
* Xerox Phaser 6115MFP / 6121MFP

foo2qpdl:
* Samsung CLP-300 / CLP-310 / CLP-315 / CLP-325 / CLP-325W / CLP-600 / CLP-610 / CLP-620 / CLX-2160 / CLX-3160 / CLX-3175
* Xerox Phaser 6110 / 6110MFP

foo2slx:
* Lexmark C500n

foo2hiperc:
* Oki C110 / C310dn / C3100n / C3200n / C3300n / C3400n / C3530n MFP (PRINT ONLY) / C5100n / C5150n / C5200n / C5500n / C5600n / C5650 / C5800n
* Olivetti d-Color P160W

foo2oak:
* HP Color LaserJet 1500 (ALPHA QUALITY)
* Kyocera Mita KM-1635 (ALPHA QUALITY) / KM-2035 (ALPHA QUALITY)

%prep
%setup -q -n %name
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
sed -i 's,/tmp/,$TMPDIR/,' foo2hiperc-wrapper.in
sed -i 's,/tmp/,$TMPDIR/,' foo2hp2600-wrapper.in
sed -i 's,/tmp/,$TMPDIR/,' foo2lava-wrapper.in
sed -i 's,/tmp/,$TMPDIR/,' foo2oak-wrapper.in
sed -i 's,/tmp/,$TMPDIR/,' foo2qpdl-wrapper.in
sed -i 's,/tmp/,$TMPDIR/,' foo2slx-wrapper.in
sed -i 's,/tmp/,$TMPDIR/,' foo2xqx-wrapper.in
sed -i 's,/tmp/,$TMPDIR/,' foo2zjs-wrapper.in

%build
%make CFLAGS="%optflags"

%install
# need to prepare these by hand
mkdir -p %buildroot{/bin,%_bindir,%_sbindir,%_datadir/cups/model,%_datadir/ppd/foo2zjs}
mkdir -p %buildroot%_datadir/foomatic/db/source/{driver,opt,printer}
mkdir -p %buildroot%_udevrulesdir
%make \
	DESTDIR=%buildroot \
	PREFIX=%buildroot%_usr \
	FOODB=%buildroot%_datadir/foomatic/db/source \
	MODEL=%buildroot%_datadir/ppd/foo2zjs \
	install install-hotplug

install -m644 %SOURCE1 README-UTF8.ALT
install -m755 getweb %buildroot%_bindir/
install -m700 %SOURCE2 %buildroot%_sbindir/
install -pD -m644 %SOURCE3 %buildroot%_desktopdir/hplj1020.desktop
install -pD -m644 %SOURCE4 %buildroot%_miconsdir/hplj1020.png
install -pD -m644 %SOURCE5 %buildroot%_niconsdir/hplj1020.png
install -pD -m644 %SOURCE6 %buildroot%_liconsdir/hplj1020.png

install -pD -m644 %SOURCE7 %buildroot%_udevrulesdir/11-hplj10xx.rules

#ln -s %_datadir/ppd/foo2zjs %buildroot%_datadir/cups/model/foo2zjs-ppd

rm -rf %buildroot%_docdir/%name/

# Make relative symlink for %_libexecdir/cups/filter/command2foo2lava-pjl
rm -f %buildroot%_libexecdir/cups/filter/command2foo2lava-pjl
ln -s ../../../bin/command2foo2lava-pjl %buildroot%_libexecdir/cups/filter/command2foo2lava-pjl

%files -n %name-apps
%_miconsdir/hplj1020.png
%_niconsdir/hplj1020.png
%_liconsdir/hplj1020.png
%_desktopdir/*.desktop
%_localstatedir/foo2zjs/*.gif
%_localstatedir/foo2zjs/*.tcl

%files -n %name-fwdownloader
%_sbindir/foo2zjs_download_fw

%files -n foomatic-db-%name
%_datadir/foomatic/db/source/*/*

%files -n %name-PPD
%_datadir/ppd/foo2zjs/*
#%_datadir/cups/model/*

%files
%doc README-UTF8.ALT COPYING ChangeLog INSTALL README manual.pdf
%_man1dir/*
/bin/*
%_bindir/*
%_sbindir/hplj*
%_udevrulesdir/*
%dir %_localstatedir/foo2zjs/
%_localstatedir/foo2zjs/*
%_localstatedir/foo2hiperc/*
%_localstatedir/foo2lava/*
%_localstatedir/foo2oak/*
%_localstatedir/foo2slx/*
%_localstatedir/foo2xqx/*
%_localstatedir/foo2hp/*
%_localstatedir/foo2qpdl/*
%_libexecdir/cups/filter/command2foo2lava-pjl

# discontinued
%exclude %_bindir/printer-profile
%exclude %_localstatedir/foo2zjs/hplj1020_icon.gif
%exclude %_localstatedir/foo2zjs/hplj10xx_gui.tcl

%changelog
* Wed Mar 18 2020 Andrey Cherepanov <cas@altlinux.org> 20200207-alt1
- New snapshot.
- Support for new models:
  + HP LaserJet Pro M1132s MFP
  + Samsung ML-1670
  + Samsung ML-1675

* Fri Jul 13 2018 Oleg Solovyov <mcpain@altlinux.org> 20180519-alt1
- 2018-05-19 tarball

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 20140519-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for foo2zjs
  * postclean-03-private-rpm-macros for the spec file

* Wed Jun 11 2014 Evgeny V Shishkov <shev@altlinux.org> 20140519-alt1
- 2014-05-19 tarball

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 20120601-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for foo2zjs
  * postclean-03-private-rpm-macros for the spec file

* Sat Mar 23 2013 Igor Vlasenko <viy@altlinux.ru> 20120601-alt2
- NMU: removed conflict with foomatic-db (closes: 28741)

* Mon Jul 16 2012 Evgeny V Shishkov <shev@altlinux.org> 20120601-alt1
- 2012-06-01 tarball
- fix #25798 again

* Tue May 01 2012 Evgeny V Shishkov <shev@altlinux.org> 20120404-alt1
- 2012-04-04 tarball
- fix #27255

* Thu Feb 23 2012 Evgeny V Shishkov <shev@altlinux.org> 20120214-alt1
- 2011-12-27 tarball
- fix hplj10xx.rules (25798)

* Thu Dec 29 2011 Evgeny V Shishkov <shev@altlinux.org> 20111227-alt1
- 2011-12-27 tarball
- Update patches: foo2zjs.make_20111229.patch, foo2zjs.hplj1000_20111229.patch, hplj10xx.rules

* Thu Jun 02 2011 Evgeny V. Shishkov <shev@altlinux.org> 20110525-alt2
- fix hplj10xx.rules (cups could not find a printer)

* Thu Jun 02 2011 Evgeny V. Shishkov <shev@altlinux.org> 20110525-alt1
- 2011-05-25 tarball
- fix #25701 bug
- Update patches: foo2zjs.getweb_20110602.patch

* Fri May 13 2011 Evgeny V. Shishkov <shev@altlinux.org> 20110507-alt1
- 2011-05-07 tarball
    * New Printer: Samsung CLP-325, CLP-325W
- Update patches: foo2zjs.getweb_20110513.patch

* Tue Apr 05 2011 Evgeny V. Shishkov <shev@altlinux.org> 20110308-alt2
- fix foo2zjs.hplj1000_20110405.patch

* Tue Apr 05 2011 Evgeny V. Shishkov <shev@altlinux.org> 20110308-alt1
- 2011-03-08 tarball
- Update patches: foo2zjs.make_20110405.patch, foo2zjs.hplj1000_20110405.patch (#25290)

* Mon Feb 07 2011 Evgeny V. Shishkov <shev@altlinux.org> 20110205-alt1
- 2011-02-05 tarball
    * New Printer: Oki C310dn
- Update patches: foo2zjs.getweb_20100207.patch foo2zjs.make_20110207.patch

* Wed Jan 19 2011 Evgeny V. Shishkov <shev@altlinux.org> 20110118-alt1
- 2011-01-18 tarball
- update patches: foo2zjs.make_20110119.patch
- New printers: HP LaserJet 1022n, HP LaserJet 1022nw

* Mon Dec 20 2010 Evgeny V. Shishkov <shev@altlinux.org> 20101213-alt1
- 2010-12-13 tarball
- update patches: foo2zjs.make_20101220.patch foo2zjs.hplj1000_20101220.patch foo2zjs.getweb_20101220.patch

* Tue Nov 16 2010 Evgeny V. Shishkov <shev@altlinux.org> 20101112-alt1
- 2010-11-12 tarball
    Rick Richardson <rick.richardson@comcast.net>
	* New Printer: Olivetti d-Color P160W
- update patches: foo2zjs.getweb_20101116.patch

* Thu Aug 26 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100817-alt1
- 2010-08-17 tarball
    * New foo2lava printer: Xerox Phaser 6121MFP (printer only)
- update patches: foo2zjs.getweb_20100826.patch

* Wed Aug 11 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100809-alt1
- 2010-08-09 tarball
- update patches: foo2zjs.make_20100810.patch
- add requires: foomatic-filters

* Fri Jun 25 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100624-alt1
- 2010-06-24 tarball

* Wed Jun 16 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100615-alt1
- 2010-06-15 tarball
    * foo2qpld foomatic-db and PPD files: fix Duplex for clp-6100, clp-610,
	clp-620. Manual Duplex is no longer supported. Use Gnome-Manual-Duplex
	instead.
	Please delete and recreate the Samsung CLP-6?? printers.
    * New Printer: Oki C110
- update patches: foo2zjs.getweb_20100616.patch

* Tue Jun 08 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100528-alt1
- 2010-05-28 tarball
    * Split out foo2zjs into:
	foo2zjs- Minolta 2200 DL, 2300 DL, HP 1000, HP 1005
	foo2zjs-z1- HP 1018, 1020, 1022, M1319MFP, P2035
	foo2zjs-z2- HP Laserjet Pro P1102, P1102w, P1566, P1606dn

	* Add new paper sizes and media types to foo2zjs-z1 and foo2zjs-z2
	    A6, 16K *, Postcard and Double Postcard, German Legal (8.5 x 13!)

	* PLEASE delete and recreate the foo2zjs-z1 and foo2zjs-z2 printers!!!
	Otherwise, Page Size will be "Letter" even if you set it to A4.
	This is a Cups problem (cups-1.4.2-26.fc11.i586).

* Tue May 11 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100509-alt1
- 2010-05-09 tarball

* Wed May 05 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100504-alt1
- 2010-05-04 tarball
    * Modify: foo2qpdl-wrapper: modolo 256 some papers (i.e. env#10)
- update patches: hplj10xx_gui.tcl_20100505.patch, foo2zjs.getweb_20100505.patch

* Thu Apr 22 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100421-alt1
- 2010-04-21 tarball
    * New Printers: Oki C5650
- added my hplj10xx.rules (for udev 1.50)

* Thu Apr 15 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100412-alt1
- 2010-04-13 tarball
    * New Printers: HP LaserJet Pro P1102, P1102w
    * New Printers: HP LaserJet Pro P1566
    * New Printers: HP LaserJet Pro P1606dn
- update patches: foo2zjs.make_20100415.patch

* Tue Mar 30 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100329-alt1
- 2010-03-29 tarball
    * New Printer: Samsung CLP-620 added to foo2qpdl et al.
- update patches: foo2zjs.make_20100330.patch

* Fri Mar 12 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100311-alt1
- 2010-03-12 tarball
- update makefile patch (foo2zjs.make_20100312.patch)

* Thu Feb 11 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100210-alt1
- 2010-02-10 tarball

* Fri Jan 29 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100127-alt1
- 2010-01-27 tarball

* Fri Jan 22 2010 Evgeny V. Shishkov <shev@altlinux.org> 20100120-alt1
- 2010-01-20 tarball 

* Mon Dec 14 2009 Evgeny V. Shishkov <shev@altlinux.org> 20091211-alt1
- 2009-12-11 tarball
- update makefile patch (foo2zjs.make_20081211.patch)

* Fri Nov 20 2009 Evgeny V. Shishkov <shev@altlinux.org> 20091112-alt1
- 2009-11-12 tarball
- Printers database is taken out in separate package (foomatic-db-foo2zjs)
- PPD is taken out in separate package (foo2zjs-PPD)
- Exceptions of printers database are removed (Were in .spec file)

* Mon Nov 02 2009 Evgeny V. Shishkov <shev@altlinux.org> 20091027-alt1
- 2009-10-27 tarball
- add ghostscript-classic in BuildRequires
- update foo2zjs.hplj1000_20091102.patch
    1) Add usblp module before downloading firmware
    2) Remove usblp module after downloading firmware
- remove 'KERNEL=="lp*",' from  hplj10xx.rules
    Then udev finds printers.

* Mon Oct 26 2009 Evgeny V. Shishkov <shev@altlinux.org> 20091025-alt1
- 2009-10-25 tarball

* Mon Sep 21 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090920-alt1
- 2009-09-20 tarball
- update .spec file
- update foo2zjs.make_20090921.patch
- update and replaced foo2zjs.hotplug patch at foo2zjs.hplj1000_20090921.patch

* Mon Aug 31 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090830-alt1
- 2009-08-30 tarball
- update getweb patch

* Wed Jun 17 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090614-alt1
- 2009-06-14
    Rick Richardson <rick.richardson@comcast.net>
	* New foo2lava printer:
	    Konica-Minolta magicolor 4690MF
	* upgate getweb for the 4690 printer

* Mon Jun 01 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090530-alt1
- 2009-05-30 tarball
    Rick Richardson <rick.richardson@comcast.net>
	* Added: Samsung CLP-310 manual pages.

* Wed May 06 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090504-alt1
- 2009-05-04 tarball
    Rick Richardson <rick.richardson@comcast.net>
	* Added: Samsung CLP-310 like CLP-315.  The case is white!
- update foo2zjs.getweb_20090506.patch

* Thu Apr 23 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090422-alt1
- 2009-04-22 tarball
    Rick Richardson <rick.richardson@comcast.net>
	* Update: zjsdecode, foo2hp.c: Add ZJI_BITMAP_xxx types.

* Tue Apr 21 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090415-alt1
- 2009-04-15 tarball
- add requires: wget, cups

* Tue Apr 14 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090413-alt1
- 2009-04-13 tarball
    Rick Richardson <rick.richardson@comcast.net>
	Fix: hplj1000 to protect against /lp*

* Thu Mar 26 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090325-alt1
- 2009-03-25 tarball
- update foo2zjs.getweb_20090326.patch
- Rick Richardson <rick.richardson@comcast.net>
    * Add: km-1600-rgb-392-bpp1.icm for color correction using
	the X-rite ColorMunki and Argyll.
	For KONICA MINOLTA 1600W, 1680MF, 1690MF
	Delete 1600W, re-download, make, ./getweb 1600w, make install

* Mon Mar 23 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090314-alt2
- move foo2zjs-apps, foo2zjs-fwdownloader to noarch
- exclude printer-profile file
- remove foo2zjs.printer-profile_20090317.patch

* Tue Mar 17 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090314-alt1
- 2009-03-14 tarball
    Rick Richardson <rick.richardson@comcast.net>
	* New foo2lava printers: 
	    Konica-Minolta magicolor 1600W
	    Konica-Minolta magicolor 1680MF
	    Konica-Minolta magicolor 1690MF
	ALPHA QUALITY!  PRINTER ONLY!
- update patches: foo2zjs.getweb_20090316.patch, foo2zjs.make_20080316.patch
- add foo2zjs.printer-profile_20090317.patch

* Tue Mar 10 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090308-alt1
- updated to 20090308 tarball

* Wed Feb 25 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090219-alt1
- updated to 20090219 tarball
    Rick Richardson <rick.richardson@comcast.net>
	* foo2hp: Fix segv when -b2 and -d2 are given.
	* foo2hp: Fix PageNum when -b2 is given.

* Mon Feb 16 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090213-alt1
- updated to 20090213 tarball

* Mon Feb 02 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090130-alt1
- updated to 20090130 tarball

* Mon Jan 26 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090122-alt1
- updated to 20090122 tarball
    Rick Richardson <rick.richardson@comcast.net>
	New printer: HP LaserJet M1319 MFP.  Printer only!!
	New printer: HP LaserJet P2035
- update buildreq

* Wed Jan 14 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090111-alt1
- updated to 20090111 tarball
- remove foo2oak-wrapper.in_20080504.patch
    Rick Richardson <rick.richardson@comcast.net>
    * foo2oak-wrapper bug fix

* Fri Jan 02 2009 Evgeny V. Shishkov <shev@altlinux.org> 20090102-alt1
- updated to 20090102 tarball
    Rick Richardson <rick.richardson@comcast.net>
    * New printer: Samsung CLX-3175
    * New printer: Oki C3100
- update patches: foo2zjs.getweb_20090102.patch

* Mon Dec 29 2008 Evgeny V. Shishkov <shev@altlinux.org> 20081226-alt1
- updated to 20081225 tarball
- update patches: foo2zjs.getweb_20081229.patch

* Fri Dec 26 2008 Evgeny V. Shishkov <shev@altlinux.org> 20081225-alt1
- updated to 20081225 tarball

* Mon Dec 15 2008 Evgeny V. Shishkov <shev@altlinux.org> 20081207-alt1
- updated to 20081120 tarball
- update patches: foo2zjs.getweb_20081215.patch foo2zjs.hotplug_20081215.patch foo2zjs.make_20081215.patch
- Rick Richardson <rick.richardson@comcast.net>
    - Samsung CLP-315:
	Now use Argyll (samclp-315-argyll-0.icm) for color correction
	make; ./getweb 315; make install
	Delete and recreate Samsung CLP-315
    - HP CLJ CP1215:
	Now use Argyll (hp1215-argyll-0.icm) for color correction
	make; ./getweb 1215; make install
	Delete and recreate HP Color LaserJet CP1215
	foo2hp2600-wrapper: implement -z <model>; 0=1600/2600, 1=1215
    - foo2zjs-pstops: Fix bug with -w

* Mon Nov 24 2008 Evgeny V. Shishkov <shev@altlinux.org> 20081120-alt1
- updated to 20081120 tarball
- remove update_menus, clean_menus from spec file
    (update_menus repocop test)

* Thu Nov 13 2008 Evgeny V. Shishkov <shev@altlinux.org> 20081008-alt4
- remove foo2XXXX-tmp.patch patches.
    subst /tmp/ on  $TMPDIR
    repocop test (unsafe-tmp-usage-in-scripts).
- remove hplj1020.desktop_20080929.patch
- update .desktop file
    repocop test (freedesktop-desktop)

* Wed Nov 05 2008 Evgeny V. Shishkov <shev@altlinux.org> 20081008-alt3
- add foo2XXXX-tmp.patch patches.
    Use 'mktep' command for create tmp file.
    repocop test (unsafe-tmp-usage-in-scripts).

* Mon Oct 27 2008 Evgeny V. Shishkov <shev@altlinux.org> 20081008-alt2
- update .desktop file
- update icons for hplj1020

* Tue Oct 14 2008 Evgeny V. Shishkov <shev@altlinux.org> 20081008-alt1
- updated to 20081008 tarball
    Rick Richardson <rick.richardson@comcast.net>
    * foo2qpdl: bug fix: -z2 (clp-315. clp-610): stripe starts with 0, not 1.

* Wed Oct 08 2008 Evgeny V. Shishkov <shev@altlinux.org> 20081007-alt1
- updated to 20081007 tarball
    Rick Richardson <rick.richardson@comcast.net>
    * foo2qpdl: bug fix: -z2 (clp-315. clp-610): stripe starts with 0, not 1.
- update spec file

* Tue Sep 30 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080923-alt3
- update patch foo2zjs.hotplug_20080930.patch
- update script foo2zjs_download_fw

* Mon Sep 29 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080923-alt2
- move all foo2XXX from /usr/share to /var/lib
- add patch: hplj1020.desktop_20080929.patch, hplj10xx_gui.tcl_20080929.patch, foo2zjs.getweb_20080929.patch
- update patch: foo2zjs.make_20080929.patch, foo2zjs.hotplug_20080930.patch, foo2oak-wrapper.in_20080504.patch
- add script foo2zjs_download_fw (Download and installing printer firmware from internet)
- update README-UTF8.ALT

* Thu Sep 25 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080923-alt1
- updated to 20080923 tarball
    * foo2qpdl: bug fix: LONGEDGE does not need to be flipped on CLP-610.
    * zjsdecode, gipddecode, slxdecode: fix bug with argc[1]
- update makefile patch (foo2zjs.make_20080925.patch)
- update hotplug patch (foo2zjs.hotplug-alt-20080919.patch)
    * add automatical downloading firmware (if need)
- update README-UTF8.ALT

* Tue Sep 23 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080922-alt1
- updated to 20080922 tarball
    *foo2qpdl: Do auto duplex on clp-610
	Delete CLP-610 printer then re-install them (PPD changed) 

* Tue Sep 16 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080914-alt2
- add README-UTF8.ALT - small russian doc

* Mon Sep 15 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080914-alt1
- updated to 20080914 tarball
- update makefile patch to foo2zjs.make_20080915.patch

* Fri Sep 12 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080826-alt1
- updated to 20080826 tarball

* Tue Aug 12 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080809-alt1
- updated to 20080809 tarball
- extract graphic tools in a separate package
- clean spec file

* Thu Aug 07 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080806-alt1
- updated to 20080806 tarball
- New printer: Samsung CLP-315

* Wed Jun 18 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080605-alt2
- Add wget requires
- Change tk >= 8.4

* Mon Jun 09 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080605-alt1
- updated to 20080605 tarball
- update foo2zjs.make_20080609.patch

* Mon May 26 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080523-alt1
- updated to 20080523 tarball
- add requires tk>=8.5
- update description

* Mon May 19 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080515-alt1
- updated to 20080515 tarball

* Sun May 04 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080501-alt1
- updated to 20080501 tarball
- add patch foo2oak-wrapper.in_20080504.patch

* Wed Apr 30 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080426-alt1
- updated to 20080426 tarball
- update Makefile patch

* Fri Apr 25 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080418-alt1
- updated to 2008-04-18 tarball

* Fri Apr 04 2008 Evgeny Shishkov <evgen@svi.pp.ru> 20080401-alt0.2
- updated to 2008-04-01 tarball
- fix menu picture

* Wed Apr 02 2008 Evgeny Shishkov <evgen@svi.pp.ru> 20080324-alt0.1
- updated to 2008-03-24 tarball
- updated all patches

* Fri Nov 23 2007 Michael Shigorin <mike@altlinux.org> 20070520-alt0.3
- following Sisyphus package change (20060523-alt0.8):
  + Remove requires to printer-drivers-utils

* Mon May 28 2007 Michael Shigorin <mike@altlinux.org> 20070520-alt0.2
- rebuilt for Daedalus (should be good enough for Sisyphus
  but a bit of careful testing should be better)
- Dmitriy also rediffed patches, cleaned up spec and noted
  that foo2oak driver (HP LJ1500) is discontinued

* Sun May 27 2007 Dmitriy Shadrinov <shadrinovdd@ystu.ru> 20070520-alt0.1
- updated to 2007-05-20 tarball

* Sat May 26 2007 Michael Shigorin <mike@altlinux.org> 20060523-alt0.4
- updated udev rules file to current fashion;
  thanks Dmitriy Shadrinov <shadrinovdd ystu ru>
  for investigation and fix proposal

* Thu Nov 02 2006 Michael Shigorin <mike@altlinux.org> 20060523-alt0.3
- actually *excluded* and not just mentioned in changelog (#10223):
  HP-Color_LaserJet_2600n.xml
  HP-LaserJet_1020.xml
  Minolta-magicolor_2300_DL.xml
  (thanks Artem Zolochevskiy <azol@> for bringing this up)

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 20060523-alt0.2
- excluded these due to file conflict with foomatic-db-3.0.2-alt3:
  HP-Color_LaserJet_2600n.xml
  HP-LaserJet_1020.xml
  Minolta-magicolor_2300_DL.xml
  (if you happen to miss them, check current foomatic-db)

* Sun Jun 25 2006 Michael Shigorin <mike@altlinux.org> 20060523-alt0.1
- built for Sisyphus (NMU or takeover?)
- NB: it's older snapshot, there are new features in the newer one
  but I can't test (and don't need) them; so leaving 2006-06-25 alone
  (if you have HP2600 or udev troubles with HP10xx, try that too;
  please note the ICM file has different copyright terms, see the 
  website and/or use getweb script)

* Wed May 24 2006 Michael Shigorin <mike@altlinux.org> 20060523-alt0.1.M30.1
- 20060523 tarball
  + should support HP LaserJet 1018 and 1022
- updated patch2
- excluded HP1022 PPD (conflicts with foomatic-db-3.0.2-alt1.20050404)

* Wed Apr 19 2006 Michael Shigorin <mike@altlinux.org> 20060416-alt0.1.M30.1
- added hotplug/udev support
- patched hotplug script and makefile to play nice to packaging
- moved usb_printerid back to /bin (as intended)

* Tue Apr 18 2006 Michael Shigorin <mike@altlinux.org> 20060416-alt0.0.M30.1
- updated to 2006-04-16 tarball (judging on ChangeLog)
- spec cleanup
  + moved actual build to %%build section
  + borrowed a couple of things from Conectiva spec
- extended makefile patch (handle athlon, fix add'l binaries installation)
- added groff-ps to buildrequires so that groff works during build
- added foo2zjs, foo2hp ICM profiles
- added PPDs
- exclude a bunch of Foomatic XML by default since it collides
  with foomatic-db-3.0.2-alt1.20050404

* Wed May 11 2005 Denis Smirnov <mithraen@altlinux.ru> 1.59-alt1
- first build for sisyphus
