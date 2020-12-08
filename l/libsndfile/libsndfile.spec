Name: libsndfile
Version: 1.0.30
Release: alt2

Summary: A library to handle various audio file formats
Group: System/Libraries
License: LGPL
Url: http://www.mega-nerd.com/%name/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

# Was: %url/files/%name-%version.tar.gz
# Now: https://github.com/libsndfile/libsndfile.git
Source: %name-%version.tar

Patch0: libsndfile-1.0.30-system-gsm.patch
Patch1: libsndfile-1.0.25-zerodivfix.patch

BuildRequires: gcc-c++ libalsa-devel libflac-devel libsqlite3-devel libvorbis-devel libgsm-devel
BuildRequires: autogen
BuildRequires: libopus-devel
# for check
BuildRequires: python-modules

%description
%name is a C library for reading and writing sound files such as
AIFF, AU and WAV files through one standard interface. It can currently
read/write 8, 16, 24 and 32-bit PCM files as well as 32-bit floating
point WAV files and a number of compressed formats.

This package contains shared library required for %name-based applications.

%package devel
Summary: Development environment for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required
in development of the %name-based applications.

%package utils
Summary: Utilities for %name
Group: Sound
Requires: %name = %version-%release

%description utils
This package contains utilities for %name

%prep
%setup -q
%patch0 -p2 -b .systemgsm
%patch1 -p1 -b .zerodivfix
rm -r src/GSM610

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot \
      htmldir=%_docdir/%name-devel-%version/html install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%make check

%files
%doc AUTHORS NEWS
%_libdir/*.so.*

%files devel
%doc %_docdir/%name-devel-%version
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files utils
%_bindir/*
%_man1dir/*.1*

%changelog
* Mon Dec 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.30-alt2
- Updated build dependencies for external libraries detection.

* Thu Dec 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.30-alt1
- Updated to upstream version 1.0.30 (Fixes: CVE-2017-8362, CVE-2017-14245,
  CVE-2017-14246, CVE-2017-14634, CVE-2018-13139, CVE-2018-13419, CVE-2018-19432,
  CVE-2018-19661, CVE-2018-19662, CVE-2018-19758, CVE-2019-3832)

* Fri Sep 07 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.0.28-alt2
- fixes: CVE-2017-6892, CVE-2017-12562

* Wed Sep 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0.28-alt1
- 1.0.28 (Fixes: CVE-2017-7585, CVE-2017-7586, CVE-2017-7741, CVE-2017-7742)

* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.27-alt1
- 1.0.27 (fixed CVE-2014-9496, CVE-2014-9756, CVE-2015-7805)

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.25-alt1.1
- Removed bad RPATH

* Fri Jul 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.25-alt1
- 1.0.25

* Wed Mar 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.24-alt1
- 1.0.24

* Fri Mar 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.23-alt2
- rebuild for debuginfo

* Sat Oct 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.23-alt1
- 1.0.23

* Tue Oct 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.22-alt1
- 1.0.22

* Mon Mar 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.21-alt1
- 1.0.21

* Fri May 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt1
- fixed potential heap overflow in VOC file parser (closes: #20051)

* Wed Mar 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.19-alt1
- fixed CVE-2009-0186

* Sun Feb 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.18-alt1
- 1.0.18

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt5
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Oct 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt4
- fixed build

* Wed Sep 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt3
- fixed heap-based buffer overflow in flac.c

* Thu Mar 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt2
- rebuild with flac-1.1.4

* Sat Dec 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt1
- 1.0.17
- added libsndfile-1.0.17+flac-1.1.3.patch.gz

* Sun May 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.16-alt1
- 1.0.16

* Tue Nov 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Tue Mar 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Wed Feb 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.7-alt1
- 1.0.7
- do not build devel-static subpackage by default.
- new url.

* Thu Nov 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.5-alt2
- use libtool_1.4
- don't package .la files.

* Sat May 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Wed Apr 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue Dec 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Sep 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.1-alt2
- Added pkgconfig files to devel

* Thu Sep 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.1-alt1
- 1.0.1
- Fixed configure.in
- Disabled parallel building

* Thu Apr 11 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.0.27-alt2
- Fixed memleak in sf_open_read
- Some fixes in spec

* Wed Mar 06 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.0.27-alt1
- 0.0.27

* Mon Oct 01 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.0.26-alt1
- 0.0.26

* Wed Sep 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.0.25-alt1
- 0.0.25
- Moved static library to devel-static subpackage.

* Fri Jan 19 2001 Dmitry V. Levin <ldv@fandra.org> 0.0.22-ipl1
- Initial revision.
