%define soversion 2

Name: faad
Version: 2.10.0
Release: alt1

Summary: FAAD is a Freeware Advanced Audio Decoder
License: GPL-2.0-or-later
Group: Sound

Url: http://www.audiocoding.com
# https://github.com/knik0/faad2/releases
Source: faad2-%version.tar

%define libsndfile_ver 1.0.5

BuildRequires(pre): libsndfile >= %libsndfile_ver

BuildRequires: gcc-c++ id3lib-devel libstdc++-devel zlib-devel

%description
FAAD is a LC, MAIN and LTP profile MPEG2 and MPEG-4 AAC decoder.

%package -n lib%name%soversion
Summary: Freeware Advanced Audio Decoder (FAAD) libraries
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n lib%name%soversion
This package contains Freeware Advanced Audio Decoder (FAAD) shared
libraries.

%package -n lib%name-devel
Summary: Development files for the FAAD AAC decoder libraries
Group: Development/C++
Requires: lib%name%soversion = %version-%release
Requires: libsndfile-devel >= %libsndfile_ver

%description -n lib%name-devel
This package provides header files development libraries and
documentation for lib%name.

%prep
%setup -n faad2-%version

find ./ -type f -name "Makefile*" -print0 | \
xargs -r0 subst 's,^\(CFLAGS\),AM_\1,g
		    s,^\(LDFLAGS\),AM_\1,g
		    s,^[[:blank:]*],\t,' --

%build
%add_optflags %optflags_shared
#_buildshell ./bootstrap
%autoreconf
%configure \
	--disable-static \
	--without-drm \
	#

%make_build

%install
%makeinstall_std

# remove non-packaged files
rm -f %buildroot%_libdir/*.la

%files
%_bindir/*
%_man1dir/*

%files -n lib%name%soversion
%_libdir/*.so.%{soversion}*
%doc AUTHORS ChangeLog NEWS README TODO

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/faad2.pc

%changelog
* Sat Feb 06 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.10.0-alt1
- Updated to 2.10.0.
- Packaged faad man page.
- lib%name-devel: packaged pkgconfig file.
- Fixed license field.

* Wed Mar 06 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.7-alt6
- Removed xmms plugin subpackage.

* Fri Jul 28 2017 Michael Shigorin <mike@altlinux.org> 2.7-alt5
- BOOTSTRAP: introduced xmms knob (still on by default)

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt4
- Rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt3
- Rebuilt for soname set-versions

* Wed Aug 12 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.7-alt2
- made libmp4ff shared and installable (sbolshakov@).

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.7-alt1
- 2.7 release.
- Remove unneeded ldconfig calls.
- libfaad package renamed to libfaad2.

* Tue Apr 08 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.6.1-alt4
- Disable DRM support: fixes #14873.

* Tue Mar 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.6.1-alt3
- Fix #8750.

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.6.1-alt2
- Fix #13893: renamed xmms-input-faad to xmms-in-faad.

* Tue Nov 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.6.1-alt1
- 2.6.1 release.

* Mon Oct 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.6-alt1
- 2.6 release. 

* Tue Jul 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0-alt3.20040923
- Tuned buildrequires.

* Tue Jul 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0-alt2.20040923
- Added gcc4 patch.

* Thu Jan 27 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt1.2_20040923
- libfaad do not more provides libmp4v2.

* Tue Jan 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt1.1_20040923
- updated to 20040923 cvs snapshot.

* Mon May 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt1
- 2.0 release.

* Mon Dec 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt0.7rc3
- install more headers so that libfaad{,-devel} will provide
  libmp4v2{,-devel}.

* Mon Dec 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt0.6rc3
- do not package .la files.

* Thu Nov 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt0.5rc3
- 2.0rc3.

* Sat Jun 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1-alt1
- First build for Sisyphus.

