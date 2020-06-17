%define soname 4
Name: libdvdnav
Version: 6.1.0
Release: alt1
Summary: DVD Navigation library
License: GPLv2+
Group: System/Libraries
URL: https://www.videolan.org/developers/libdvdnav.html

Source: %name-%version.tar

BuildRequires: libdvdread-devel

%description
%name is a library that allows easy use of sophisticated DVD
navigation features such as DVD menus, multiangle playback and even
interactive DVD games.

%package devel
Summary: Development environment for %name
Group: Development/C
Requires: %name = %EVR
Requires: libdvdread-devel >= 6.1.0

%description devel
%name provides support to applications wishing to make use of DVD
navigation features.
This package contains development files you can use to develop
applications.

%prep
%setup -q

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install
rm -rf %buildroot%_docdir/%name

%files
%_libdir/*.so.*

%files devel
%doc AUTHORS README TODO
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Apr 17 2020 Anton Farygin <rider@altlinux.ru> 6.1.0-alt1
- 6.1.0

* Sat Oct 25 2014 Valery Inozemtsev <shrek@altlinux.ru> 5.0.1-alt1
- 5.0.1

* Sun Feb 24 2013 Valery Inozemtsev <shrek@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Fri May 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 4.1.3-alt4
- fixed #27197

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.1.3-alt3
- rebuild

* Sat May 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.1.3-alt2
- requires libdvdcss (closes: #23473)

* Mon Jun 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.1.3-alt1
- 4.1.3

* Sun Aug 10 2008 Led <led@altlinux.ru> 0.1.10-alt8
- added version script (%name-altlinux.ver) (fixed #16013)

* Sat Aug 09 2008 Led <led@altlinux.ru> 0.1.10-alt7
- fixed %name-0.1.10-mplayer.patch

* Sat Feb 09 2008 Led <led@altlinux.ru> 0.1.10-alt6
- build with internal libdvdread again (for use in vlc, #13901)

* Thu Jan 10 2008 Led <led@altlinux.ru> 0.1.10-alt5
- updated:
  + %name-0.1.10-mplayer.patch
  + %name-0.1.10-mplayer-ext_libdvdread.patch
- fixed #13900

* Sat Dec 22 2007 Led <led@altlinux.ru> 0.1.10-alt4
- added:
  + %name-0.1.10-mplayer.patch (from MPlayer team's SVN of
    %name)
  + %name-0.1.10-mplayer-ext_libdvdread.patch
- updated %name-0.1.10-mplayer-alt-tmpdir.patch
- cleaned up BuildRequires
- fixed License

* Fri Jan 26 2007 Led <led@altlinux.ru> 0.1.10-alt3
- added %name-0.1.10-alt-tmpdir.patch
- cleaned up spec
- built with libdvdcss

* Wed Feb 08 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.10-alt2
- Fixed header installation directory
- Run autogen.sh before configure

* Sun Oct 23 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.10-alt1
- 0.1.10
- Spec cleanup
- Added boilerplate files to the doc list

* Thu Aug 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1.9-alt1
- new version.

* Sun Apr 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1.7-alt1
- new version.

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 0.1.3-alt2
- Russian summary
- rebuild (gcc 3.2)

* Mon Aug 05 2002 Rider <rider@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Sat Jun 01 2002 Rider <rider@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Tue Apr 30 2002 Rider <rider@altlinux.ru> 0.1.0-alt1
- first build
