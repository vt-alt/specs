%define _unpackaged_files_terminate_build 1

Name: xpdf
Version: 4.03
Release: alt1

Summary: The PDF viewer and tools
License: GPLv2 or GPLv3
Group: Office
Packager: Andrew Savchenko <bircoph@altlinux.org>

URL: https://www.xpdfreader.com
# https://xpdfreader-dl.s3.amazonaws.com/%name-%version.tar.gz
Source0: xpdf-%version.tar
Source1: xpdf.desktop

Source2: xpdf-arabic.tar
Source3: xpdf-chinese-simplified.tar
Source4: xpdf-chinese-traditional.tar
Source5: xpdf-cyrillic.tar
Source6: xpdf-greek.tar
Source7: xpdf-hebrew.tar
Source8: xpdf-japanese.tar
Source9: xpdf-korean.tar
Source10: xpdf-latin2.tar
Source11: xpdf-thai.tar
Source12: xpdf-turkish.tar

# Gentoo patches
Patch1: xpdf-automagic.patch
Patch2: xpdf-visibility.patch
Patch3: xpdf-shared-libs.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: libcups-devel qt5-base-devel libpaper-devel libpng-devel
BuildRequires: libfreetype-devel fontconfig-devel zlib-devel
BuildRequires: desktop-file-utils librsvg-utils

# xpdf is a virtual package with is a full setup of xpdf
Requires: %name-viewer = %EVR %name-utils = %EVR
Requires: %name-i18n = %EVR %name-desktop = %EVR

%define desc \
The Xpdf open source project includes a PDF viewer along with a \
collection of command line tools which perform various functions on \
PDF files.

%description
%desc

%package common
Summary: The PDF viewer and tools --- common files
Group: Office
BuildArch: noarch
Requires: fonts-type1-urw

%description common
%desc

This package contains common files (config and common documentation)
needed by the other xpdf packages.

%package viewer
Summary: The PDF viewer and tools --- the PDF viewer
Group: Office
Requires: %name-common = %EVR qt5-svg
Obsoletes: xpdf-reader

%description viewer
%desc

This package contains xpdf itself, a PDF viewer for X11. xpdf is designed to
be small and efficient. xpdf supports encrypted PDF files. Standard X fonts,
Truetype fonts and Type 1 fonts are supported.

%package utils
Summary: The PDF viewer and tools --- the PDF utils
Group: Office
Requires: %name-common = %EVR

%description utils
%desc

This package contains various xpdf tools to process and convert PDF
files.

%package i18n
Summary: The PDF viewer and tools --- i18n encoding maps
Group: Office
BuildArch: noarch
Obsoletes: xpdf-chinese-simplified xpdf-chinese-traditional xpdf-japanese xpdf-korean
License: (GPLv2 or GPLv3) and BSD

%description i18n
%desc

This package provides encoding maps required to support non-UTF-8
national fonts for various languages: arabic, chinese-simplified,
chinese-traditional, cyrillic, greek, hebrew, japanes, korean,
latin2, thai, turkish.

%package desktop
Summary: The PDF viewer and tools --- desktop files
Group: Office
BuildArch: noarch
Requires: %name-viewer = %EVR

%description desktop
%desc

This package contains desktop integration files for the XPDF
viewer.

%prep
%setup -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i \
    "s|/usr/local/etc|%_sysconfdir|;
     s|/usr/local|%_prefix|;
     s|^#fontFile|fontFile|;
     s|/ghostscript/fonts|/type1/urw|;
     s|^#textEncoding|textEncoding|;
     s|^#enableFreeType|enableFreeType|;
     s|^#antialias|antialias|;
     " \
    doc/sample-xpdfrc

sed -i "s|/usr/local|%_prefix|" */add-to-xpdfrc

%build
mycmakeargs=(
    -DBUILD_SHARED_LIBS=ON
    -DCMAKE_SKIP_RPATH=OFF
    -DCMAKE_SKIP_INSTALL_RPATH=OFF
    -DA4_PAPER=ON
    -DNO_FONTCONFIG=OFF
    -DNO_TEXT_SELECT=ON
    -DOPI_SUPPORT=ON
    -DSPLASH_CMYK=ON
    -DWITH_LIBPAPER=ON
    -DWITH_LIBPNG=ON
    -DXPDFWIDGET_PRINTING=ON
    -DSYSTEM_XPDFRC="%_sysconfdir/xpdfrc"
)
%cmake "${mycmakeargs[@]}"

%cmake_build VERBOSE=1

# xpdf upstream provides only svg icon, so generate png icons
sizes="16 22 24 32 36 48 64 72 96 128 192 256 384 512 1024"
cd xpdf-qt
mkdir $sizes
for i in $sizes; do
    rsvg-convert xpdf-icon.svg -w $i -h $i -o $i/xpdf.png
done

%install
%cmakeinstall_std

desktop-file-install --dir %buildroot%_desktopdir %{SOURCE1}

# install icons
sizes="16 22 24 32 36 48 64 72 96 128 192 256 384 512 1024"
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps
cp xpdf-qt/xpdf-icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/
for s in $sizes; do
	mkdir -p %buildroot%_iconsdir/hicolor/${s}x${s}/apps
	cp xpdf-qt/$s/xpdf.png %buildroot%_iconsdir/hicolor/${s}x${s}/apps/
done

mkdir -p %buildroot%_sysconfdir
cp doc/sample-xpdfrc %buildroot%_sysconfdir/xpdfrc

# rename pdf* -> xpdf* to avoid file collisions
for d in "bin" "share/man/man1"; do
	pushd "%buildroot%_prefix/${d}"
	for i in pdf*; do
		mv "${i}" "x${i}"
	done
	popd
done

# install i18n files and update xpdfrc
for i in arabic chinese-simplified chinese-traditional cyrillic greek \
		 hebrew japanese korean latin2 thai turkish; do
	mkdir -p "%buildroot%_datadir/xpdf/${i}"
	cp -a -t "%buildroot%_datadir/xpdf/${i}" \
		$(find -O3 "xpdf-${i}" -maxdepth 1 -mindepth 1 \
			! -name README ! -name add-to-xpdfrc)

	cat "xpdf-${i}/add-to-xpdfrc" >> "%buildroot%_sysconfdir/xpdfrc"
done

%files

%files common
%doc ANNOUNCE CHANGES README
%config(noreplace) %_sysconfdir/xpdfrc
%_man5dir/*

%files viewer
%_bindir/xpdf
%_man1dir/xpdf.1*

%files utils
%exclude %_bindir/xpdf
%_bindir/xpdf*
%exclude %_man1dir/xpdf.1*
%_man1dir/xpdf*
%_libdir/xpdf/*.so

%files i18n
%_datadir/xpdf/*

%files desktop
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Jan 30 2021 Andrew Savchenko <bircoph@altlinux.org> 4.03-alt1
- Version bump
- Many bugfixes, including security, including, but not limited to:
  Fixes: CVE-2020-25725, CVE-2020-35376

* Mon Nov 09 2020 Andrew Savchenko <bircoph@altlinux.org> 4.02-alt2
- Switch from inkscape to rsvg-convert for svg->png generation.

* Sun Mar 08 2020 Andrey Savchenko <bircoph@altlinux.org> 4.02-alt1
- Major version bump and repackaging.

* Tue Feb 12 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.03-alt2
- Rebuilt with default gcc-c++.

* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.03-alt1.1
- Disabled -Wtrampolines flag

* Sun Aug 28 2011 Victor Forsiuk <force@altlinux.org> 3.03-alt1
- 3.03

* Wed Mar 30 2011 Victor Forsiuk <force@altlinux.org> 3.02-alt11
- Build without t1lib to close denial of service vulnerability. This fix should
  address CVE-2011-0764. See also http://www.kb.cert.org/vuls/id/376500.

* Thu Oct 14 2010 Victor Forsiuk <force@altlinux.org> 3.02-alt10
- Security fixes: CVE-2010-3702, CVE-2010-3704.

* Mon Oct 04 2010 Victor Forsiuk <force@altlinux.org> 3.02-alt9
- Re-apply patch for removing pdf restrictions check. Closes bug: #9923.
- Better .desktop file.

* Fri Oct 01 2010 Victor Forsiuk <force@altlinux.org> 3.02-alt8
- Compile with g++-4.3 due to scrolling speed regression with gcc 4.4.x.

* Sun Nov 15 2009 Victor Forsyuk <force@altlinux.org> 3.02-alt7
- Apply xpdf-3.02pl4 security patch to fix:
  CVE-2009-3603, CVE-2009-3604, CVE-2009-3605, CVE-2009-3606,
  CVE-2009-3608, CVE-2009-3609.

* Tue Jul 07 2009 Victor Forsyuk <force@altlinux.org> 3.02-alt6
- Drop the xpdf-utils subpackage. Let poppler provides those utilities.

* Wed Apr 22 2009 Victor Forsyuk <force@altlinux.org> 3.02-alt5
- Apply xpdf-3.02pl3 security patch to fix:
  CVE-2009-0146, CVE-2009-0147, CVE-2009-0166, CVE-2009-0799,
  CVE-2009-0800, CVE-2009-1179, CVE-2009-1180, CVE-2009-1181,
  CVE-2009-1182, CVE-2009-1183, CVE-2009-1187, CVE-2009-1188.
- Remove obsolete install time scripts.
- Build language support packages as noarch.
- Apply bunch of debian and RH patches.

* Mon Apr 14 2008 Victor Forsyuk <force@altlinux.org> 3.02-alt4
- Desktop file mime entry fix.

* Mon Nov 12 2007 Victor Forsyuk <force@altlinux.org> 3.02-alt3
- Security fixes:
  - CVE-2007-4352
  - CVE-2007-5392
  - CVE-2007-5393

* Wed Aug 08 2007 Victor Forsyuk <force@altlinux.org> 3.02-alt2
- Security fix, see CVE-2007-3387.

* Mon Mar 05 2007 Victor Forsyuk <force@altlinux.org> 3.02-alt1
- New version.

* Tue May 23 2006 Victor Forsyuk <force@altlinux.ru> 3.01-alt6
- Fix build with gcc4.
- Switch from Debian-style menu to .desktop file.
- Fix BTS#9300.

* Fri Mar 03 2006 Victor Forsyuk <force@altlinux.ru> 3.01-alt5
- Fix program icon locations.

* Sat Feb 18 2006 Victor Forsyuk <force@altlinux.ru> 3.01-alt4
- Security patch to fix CVE-2006-0301.

* Fri Jan 13 2006 Victor Forsyuk <force@altlinux.ru> 3.01-alt3
- Security fix (CVE-2005-3191). Apply both recent security patches
  from Fedora package.

* Wed Dec 07 2005 Victor Forsyuk <force@altlinux.ru> 3.01-alt2pl1
- Security fix (CAN-2005-3193).
- Updated japanese and korean support packages.
- Fix allocation size for 64bit architecture.
- Fix to don't use freetype internals.
- Apply upstream patch to fix resize/redraw.

* Fri Aug 19 2005 Victor Forsyuk <force@altlinux.ru> 3.01-alt1
- 3.01
- Reworked remove_protections patch.

* Mon Aug 15 2005 Victor Forsyuk <force@altlinux.ru> 3.00-alt6pl3
- Add patch to fix xpdf DoS, CAN-2005-2097.
- Updated buildreqs.

* Wed Jan 19 2005 Victor Forsyuk <force@altlinux.ru> 3.00-alt5pl3
- Add patch to address CAN-2005-0064.
- Add patch to set 'match' as default psPaperSize.
- Fix bug #5659 (patch from Debian).

* Wed Dec 22 2004 Victor Forsyuk <force@altlinux.ru> 3.00-alt4pl2
- Add patch to address CAN-2004-1125 vulnerability.

* Tue Nov 16 2004 Victor Forsyuk <force@altlinux.ru> 3.00-alt3
- Fix build with new (post-2.1.5) freetype2.

* Thu Oct 21 2004 Stanislav Ievlev <inger@altlinux.org> 3.00-alt2
- bump release number for sisyphus

* Mon Oct 18 2004 Stanislav Ievlev <inger@altlinux.org> 3.00-alt1.1
- sec fix

* Thu May 06 2004 Victor Forsyuk <force@altlinux.ru> 3.00-alt1
- New version.
- Updated language support packages.
- Enable multithread and wordlist configure options.
- Added mimetypes to menu and change menu section.

* Wed Oct 22 2003 Victor Forsyuk <force@altlinux.ru> 2.03-alt1
- New version.
- Updated cyrillic and greek support packages.
- Added patch (PLD) for disabling print and copy protection.
- Added patch (RHL) for secure temp file creation.
- Added patch (RHL) to fix huge memory leak.
- Final decision: build with openmotif :))
- Better subpackages split (Debian-like).

* Mon Oct 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.02pl1-alt1.1
- Rebuilt with libt1.so.5

* Thu Jun 19 2003 Victor Forsyuk <force@altlinux.ru> 2.02pl1-alt1
- security update

* Sun Feb 02 2003 Victor Forsyuk <force@altlinux.ru> 2.01-alt3
- move thai language support to main xpdf package
- openmotif cause warning messages on stderror when exiting xpdf
  and we have patch to avoid SEGV with lesstif, so switch back
  to lesstif.

* Wed Jan 08 2003 Victor Forsyuk <force@altlinux.ru> 2.01-alt2
- added official security patch (pdfto* can be used as filters)
- added nonumericlocale patch to avoid SEGV caused by LC_NUMERIC with ',' as
  decimal point
- added "-fno-exceptions -fno-rtti" to CXXFLAGS
- switch from xpdf-handle-url to url_handler.sh (provided by urlview package)

* Tue Dec 17 2002 Victor Forsyuk <force@altlinux.ru> 2.01-alt1
- new version
- switch from lesstif to openmotif: fixes BTS #0001657 and #0001737

* Wed Nov 06 2002 Victor Forsyuk <force@altlinux.ru> 2.00-alt1
- new version
- use freetype2 unconditionally
- add build requirement for t1lib-devel
- purge eliminated configure parameters
- move out asian languages support (huge!) to separate packages
- install xpdf-url-handler script to be used as urlCommand

* Mon Oct 28 2002 AEN <aen@altlinux.ru> 1.01-alt1
- new spec from MDK
- new version

* Mon Oct 29 2001 AEN <aen@logic.ru> 0.93-alt2
- built with freetype2

* Mon Oct 29 2001 AEN <aen@logic.ru> 0.93-alt1
- new version

* Thu Dec 07 2000 AEN <aen@logic.ru>
- new version
- build for RE
* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 0.91-7mdk
- Rebuild with gcc-2.96 & glibc-2.2

* Mon Oct 09 2000 Daouda Lo <daouda@mandrakesoft.com> 0.91-6mdk
- build with generic optflags (ghibo )

* Mon Oct 09 2000 Daouda Lo <daouda@mandrakesoft.com> 0.91-5mdk
- icons

* Sat Oct 07 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.91-4mdk
- fixed 0.91-t1urw patch.

* Sat Oct 07 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.91-3mdk
- re-adapted patch 0.90-t1urw to version 0.91 (it allows to use
  Type1 URW fonts for standard PDF 14 fonts for better quality).

* Fri Oct 06 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.91-2mdk
- fixed a typo in %post and %postun scripts.
- added icons.
- added rgb, patch from RedHat.
- enabled opi.

* Tue Aug 15 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.91-1mdk
- s|0.90|0.91| aka decrypt me babe.
- remove the font patch.

* Wed Aug 09 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.90-11mdk
- BM
- spechelper

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.90-10mdk
- automatically added BuildRequires

* Fri Apr 21 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.90-9mdk
- removed xpdf.desktop also from the %install stage.

* Sat Apr 01 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.90-8mdk
- updated for t1lib 1.0.1.
- added things for new menu entry.
- removed xpdf.desktop.

* Thu Mar 02 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.90-7mdk
- increased default antialias font level from low to high. Files look
  nicer.

* Tue Feb 08 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 0.90-6mdk
- Correct the URL in the spec file
- remove egcs as build require

* Thu Jan 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.90-5mdk
- Fix build as non-root.

* Sat Dec 18 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- fixed a bug for Times-Italic and Helvetica-BoldOblique name in URW fonts.

* Tue Dec 07 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix for gcc-2.95.

* Fri Nov 11 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- built for Oxygen.

* Mon Sep 27 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- added patch to use aliased Type 1 URW fonts by default for standard
  14 PDF fonts.
- added Preston Brown <pbrown@redhat.com>'s zapf patch.

* Wed Aug 11 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- update to version 0.90.
- strip binaries.
- added t1lib dependencies.

* Thu May  6 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- converted wmconfig to desktop entry

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Nov 30 1998 Preston Brown <pbrown@redhat.com>
- updated to 0.80

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- patched to compile with new, stricter egcs

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.7a

* Thu Nov 20 1997 Otto Hammersmith <otto@redhat.com>
- added changelog
- added wmconfig
