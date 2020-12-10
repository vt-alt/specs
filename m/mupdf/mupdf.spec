Name: mupdf
Version: 1.18.0
Release: alt1
Summary: A lightweight PDF viewer and toolkit
Group: Office
License: GPLv3
Url: http://mupdf.com/
Source0: http://mupdf.com/download/%name-%version-source.tar.gz
Source1: %name.desktop
Source2: debian.tar
Patch1: mupdf-1.18.0-gentoo-fix-oob-in-pdf-layer.patch
Patch2: mupdf-1.18.0-gentoo-fix-oob-in-pixmap.patch

# Automatically added by buildreq on Thu Aug 22 2013
# optimized out: libX11-devel pkg-config xorg-xextproto-devel xorg-xproto-devel
BuildRequires: libXext-devel libfreetype-devel libjbig2dec-devel libjpeg-devel libssl-devel zlib-devel libfreeglut-devel
BuildRequires: libgumbo-devel
BuildRequires: gcc-c++

%description
MuPDF is a lightweight PDF viewer and toolkit written in portable C.
The renderer in MuPDF is tailored for high quality anti-aliased
graphics.  MuPDF renders text with metrics and spacing accurate to
within fractions of a pixel for the highest fidelity in reproducing
the look of a printed page on screen.
MuPDF has a small footprint.  A binary that includes the standard
Roman fonts is only one megabyte.  A build with full CJK support
(including an Asian font) is approximately five megabytes.
MuPDF has support for all non-interactive PDF 1.7 features, and the
toolkit provides a simple API for accessing the internal structures of
the PDF document.  Example code for navigating interactive links and
bookmarks, encrypting PDF files, extracting fonts, images, and
searchable text, and rendering pages to image files is provided.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Provides: %name-static = %version-%release

%description devel
The mupdf-devel package contains header files for developing
applications that use mupdf and static libraries

%prep
%setup -n %name-%version-source -a2
%patch1 -p1
%patch2 -p1

# TODO rebuild with new openjpeg
#BuildRequires: openjpeg-devel
# NOTE: artifex bundled a forked and patched version of lcms2
# TODO: unbundle mujs
rm -rf thirdparty/{curl,freeglut,freetype,gumbo-parser,harfbuzz,jbig2dec,libjpeg,zlib}
sed -i 's/-lopenjpeg //' debian/mupdf.pc

%build
%make_build USE_SYSTEM_LIBS=yes USE_SYSTEM_OPENJPEG=no USE_SYSTEM_MUJS=no

%install
# TODO deal with platform/debian/mupdf.install / iconsdirs
%makeinstall USE_SYSTEM_LIBS=yes USE_SYSTEM_OPENJPEG=no USE_SYSTEM_MUJS=no
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D -m644 debian/%name.xpm %buildroot/%_datadir/pixmaps/%name.xpm
sed 's/@VERSION@/%version/g' < debian/mupdf.pc > mupdf.pc
install -D mupdf.pc %buildroot%_pkgconfigdir/mupdf.pc

%files
%doc %_defaultdocdir/%name
%_bindir/*
%_desktopdir/mupdf.desktop
%_mandir/man1/*
%_datadir/pixmaps/mupdf.xpm

%files devel
%_pkgconfigdir/*
%_includedir/%name
%_libdir/lib*.a

%changelog
* Wed Dec 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.18.0-alt1
- Updated to upstream version 1.18.0 (Fixes: CVE-2017-5991, CVE-2018-10289,
  CVE-2018-16647, CVE-2018-16648, CVE-2019-14975, CVE-2020-26519).

* Thu Oct 18 2018 Fr. Br. George <george@altlinux.ru> 1.13.0-alt3
- Rebuilt with libfreeglut

* Wed Oct 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.13.0-alt2
- NMU: rebuilt with libfreeglut.

* Tue Oct 02 2018 Fr. Br. George <george@altlinux.ru> 1.13.0-alt1
- Autobuild version bump to 1.13.0

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Autobuild version bump to 1.8

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Autobuild version bump to 1.6

* Mon Aug 25 2014 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Autobuild version bump to 1.5
- Partly resurrect debian platform files

* Tue Jun 03 2014 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Autobuild version bump to 1.4

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Autobuild version bump to 1.3
- Fix build
- Keep builtin static openjpeg-2.0 until it arrives in distro

* Wed May 29 2013 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initial build from FC

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.1-2
- rebuild due to "jpeg8-ABI" feature drop

* Wed Jan 09 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 1.1-1
- New release

* Sun May 20 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 1.0-1
- New release

* Wed Mar 14 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 0.9-2
- Fix buffer overflow (#752388)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.9-1
- New release

* Tue May 03 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.8.165-2
- New upstream release
- Fix *.a and *.h permissions

* Sun Mar 27 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.8.15-1
- New upstream release

* Wed Feb 09 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.7-7
- Fix dependency for F13

* Mon Feb 07 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.7-6
- roll back to static libraries  patch for shared libs has been rejected
- Fix spec errors

* Fri Jan 14 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.7-4
- replac poitless macros to command names

* Fri Jan 14 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.7-3
- Create patch for optflags
- Change Summary
- Fix Require for devel package

* Thu Jan 13 2011 Pavel Zhukov <landgraf@fedoraproject.org> -0.7-2
- add Fedora CFLAGS
- create patch for use shared library

* Wed Jan 12 2011 Pavel Zhukov <landgraf@fedoraproject.org>  - 0.7-1
- Initial package
