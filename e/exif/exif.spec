Name: exif
Version: 0.6.22
Release: alt1

Summary: exif is a small command-line utility to show EXIF information hidden in JPEG files
License: GPLv2+
Group: Graphics

Url: http://libexif.github.io
Source: https://github.com/libexif/exif/releases/download/exif-0_6_22-release/%name-%version.tar.xz

# Need 0.6.18 for exif_loader_get_buf (see configure.ac):
%define libexif_ver 0.6.22

Requires: libexif >= %libexif_ver
BuildPreReq: libexif-devel >= %libexif_ver

# Automatically added by buildreq on Mon Aug 30 2010
# ... and manually removed libexif-devel as we already set versioned req
BuildRequires: libpopt-devel

%description
exif is a small command-line utility to show EXIF information embedded in JPEG files.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_man1dir/*

%changelog
* Wed May 27 2020 Dmitriy Khanzhin <jinn@altlinux.org> 0.6.22-alt1
- 0.6.22

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.21-alt1
- 0.6.21

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.20-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Jan 13 2011 Victor Forsiuk <force@altlinux.org> 0.6.20-alt1
- 0.6.20

* Mon Aug 30 2010 Victor Forsiuk <force@altlinux.org> 0.6.19-alt1
- 0.6.19

* Wed Dec 10 2008 Victor Forsyuk <force@altlinux.org> 0.6.17-alt1
- 0.6.17

* Wed Sep 05 2007 Victor Forsyuk <force@altlinux.org> 0.6.15-alt1
- 0.6.15

* Mon Sep 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.9-alt1
- new version.

* Fri Sep 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6-alt2
- rebuild with new libexif-0.5.12
- updated buildreqs.

* Mon Jan 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6-alt1
- new version.

* Wed Oct 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.5-alt1
- Rebuild in new environment.
- 0.5

* Mon Mar 04 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.2-alt1
- First build for Sisyphus.
