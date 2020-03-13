%def_without test

Name: gscan2pdf
Version: 2.6.5
Release: alt1

Summary: A GUI to ease the process of producing a multipage PDF from a scan
Group: Office
License: GPL

Url: http://gscan2pdf.sourceforge.net/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name/%version/%name-%version.tar

#Patch: %name.patch

BuildArch: noarch

# perl(Gtk2/Ex/PodViewer.pm) at line 3501 (depth 4) inside eval SKIP
#Requires: perl(Gtk2/Ex/PodViewer.pm)

BuildRequires: libdb4-devel perl-Archive-Tar perl-Config-General perl-Filesys-Df perl-List-MoreUtils perl-Locale-gettext perl-Log-Log4perl perl-PDF-API2 perl-Proc-ProcessTable perl-Readonly perl-Set-IntSpan perl-Sub-Name perl-podlators perl-Text-Balanced

BuildRequires: perl-Data-UUID perl-JSON-PP perl-Date-Calc perl-Image-Sane perl-Sub-Override perl-Time-Piece
BuildRequires: perl-Gtk3 perl-Gtk3-SimpleList libgoocanvas2-gir perl-GooCanvas2

Requires: libgoocanvas2-gir perl-Pod-Perldoc

BuildRequires: perl-Magick perl-Sane >= 0.05

BuildRequires: perl-devel

# needs for backports
BuildPreReq: perl-Try-Tiny

# ImageMagick
Requires: %_bindir/convert
Requires: perl-Magick

# %_bindir/cjb2
Requires: djvu-utils

# tiffcp
Requires: libtiff-utils

Requires: xdg-utils unpaper

# /usr/bin/scanimage
Requires: sane

# OCR:
#Requires: cuneiform

%description
At maturity, the GUI will have similar features to that of the Windows Imaging
program, but with the express objective of writing a PDF, including metadata.

Scanning is handled with SANE via scanimage. PDF conversion is done by libtiff.

%prep
%setup
#patch -p2
%__subst "s|use Gtk3 0.028 -init;|use Gtk3 0.028; INIT { Gtk3->init; }|g" bin/%name
%__subst "5iuse Gtk3;" lib/Gscan2pdf/Canvas.pm
# djvu %_bindir/cjb2
%__subst "s|requires djvulibre-bin|djvu-utils|g" bin/%name

%build
%perl_vendor_build
#__subst "s|^test .*||g" Makefile
%make_build

# used Gtk2
#check
#make test

%install
%makeinstall_std INSTALLSITELIB=%perl_vendor_privlib INSTALLSITESCRIPT=%_bindir
find %buildroot -name perllocal.pod | xargs rm -f
find %buildroot -name .packlist | xargs rm -f

%find_lang %name

%files -f %name.lang
%doc History
%_bindir/gscan2pdf
#_bindir/scanadf-perl
#_bindir/scanimage-perl
%_desktopdir/*%name.desktop
%_datadir/%name/
%_datadir/metainfo/*gscan2pdf.appdata.xml
%_datadir/help/C/gscan2pdf/
%_pixmapsdir/*
%_man1dir/*
%perl_vendor_privlib/Gscan2pdf/

%changelog
* Sat Mar 07 2020 Vitaly Lipatov <lav@altlinux.ru> 2.6.5-alt1
- new version 2.6.5 (with rpmrb script)

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 2.5.4-alt1
- new version 2.5.4 (with rpmrb script)

* Sun Feb 10 2019 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)

* Fri Dec 14 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version 2.2.1 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Sun Nov 18 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.7-alt1
- new version 2.1.7 (with rpmrb script)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- new version 2.1.4 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- new version 2.1.2 (with rpmrb script)

* Mon Apr 02 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script)
- add missed require libgoocanvas2-gir (ALT bug 34750)
- add missed require perl-Pod-Perldoc (ALT bug 33707)

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.8.11-alt1
- new version 1.8.11 (with rpmrb script)

* Sun Jun 04 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- new version 1.8.2 (with rpmrb script)

* Sat May 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Tue Apr 18 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- new version 1.7.3 (with rpmrb script)

* Sat Feb 18 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script)

* Mon Jan 16 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- new version 1.7.1 (with rpmrb script)

* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version 1.7.0 (with rpmrb script)

* Sun Dec 04 2016 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)

* Thu Oct 20 2016 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- new version 1.5.4 (with rpmrb script)

* Thu Oct 13 2016 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt1
- new version 1.5.3 (with rpmrb script)

* Wed Aug 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version 1.5.1 (with rpmrb script)

* Sun Jun 12 2016 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Thu Apr 14 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Fri Apr 08 2016 Vitaly Lipatov <lav@altlinux.ru> 1.3.9-alt1
- new version 1.3.9 (with rpmrb script)
- drop cuneiform requires (ALT bug #31935)

* Sun Jan 17 2016 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt1
- new version 1.3.6 (with rpmrb script)

* Sat Oct 10 2015 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt1
- new version 1.3.5 (with rpmrb script) (ALT bug #31341)
- pack man pages

* Mon May 11 2015 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Wed May 06 2015 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Thu Oct 09 2014 Vitaly Lipatov <lav@altlinux.ru> 1.2.6-alt1
- new version 1.2.6 (with rpmrb script)

* Mon May 19 2014 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt1
- new version 1.2.5 (with rpmrb script)

* Fri Apr 04 2014 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt1
- new version 1.2.4 (with rpmrb script)

* Wed Jan 29 2014 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- new version 1.2.3 (with rpmrb script)

* Tue Jan 14 2014 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Tue Feb 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- new version 1.1.3 (with rpmrb script)

* Fri Dec 07 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Wed Jul 25 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)

* Sat Jul 21 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version 1.0.5 (with rpmrb script)

* Thu Apr 12 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- new version 1.0.4 (with rpmrb script)

* Tue Apr 10 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Thu Mar 29 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Tue Feb 07 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Wed Feb 16 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.32-alt1
- new version 0.9.32 (with rpmrb script)
- add requires to libtiff-utils and ImageMagick, fix djvu-utils package name (closes: #24860)
- add cuneiform requires

* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.31-alt1
- new version (ALT bug 23475), fix build

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.23-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gscan2pdf
  * postclean-05-filetriggers for spec file

* Sat Mar 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.23-alt1
- new version 0.9.23 (with rpmrb script)

* Sun Jan 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.20-alt1
- new version 0.9.20
- cleanup spec, remove LICENCE file

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.19-alt1
- new version 0.9.19 (with rpmrb script)

* Sat Nov 17 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.18-alt1
- new version 0.9.18 (with rpmrb script)
- update buildreq

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.17-alt1
- new version 0.9.17 (with rpmrb script)

* Sun Sep 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.16-alt2
- fix update/clean menus

* Sun Aug 26 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.16-alt1
- new version 0.9.16 (with rpmrb script)
- add perl-Magick to buildreq

* Thu Jul 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.14-alt1
- new version 0.9.14 (with rpmrb script)

* Sat Jun 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.12-alt1
- new version 0.9.12 (with rpmrb script)

* Wed May 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt1
- new version 0.9.9 (with rpmrb script)

* Tue Apr 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- initial build for ALT Linux Sisyphus

* Thu Apr 05 2007 Jeffrey Ratcliffe <ra28145@users.sourceforge.net>
  - Fixed bug calling help
  - Fixed error message caused by update_options sub being called twice.
  - Streamlined image creation (speedup)
  - Adjusted widget justification in scan dialog
  - Suppressed rounded messages from scanadf frontend
  - Remembers scan area
  - Ghosts zoom and rotate buttons if no page selected
  - Fixed bug where custom scan area not hidden when A4 or Letter selected
  - Help update
