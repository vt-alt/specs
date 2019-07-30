%define _unpackaged_files_terminate_build 1
%def_enable libwebpmux
%def_enable libwebpdemux
%def_enable libwebpdecoder
%define soversion 7

Name: libwebp
Version: 1.0.3
Release: alt1

Summary: Library and tools for the WebP graphics format
License: BSD
Group: System/Libraries
Url: http://webmproject.org/
Source: https://storage.googleapis.com/downloads.webmproject.org/releases/webp/%name-%version.tar.gz
# init only
Patch: %name-0.4.1-alt-lfs.patch

BuildRequires: libjpeg-devel libpng-devel libtiff-devel libgif-devel
BuildRequires: libfreeglut-devel

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package -n %name%soversion
Summary: Libraries for the WebP graphics format
Group: System/Libraries
Provides: %name = %version-%release
Obsoletes: libwebp = 0.4.0-alt1

%description -n %name%soversion
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package devel
Summary: Development files for libwebp, a library for the WebP format
Group: Development/C
Requires: %name%soversion = %version-%release

%description devel
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package tools
Summary: The WebP command line tools
Group: System/Libraries
Requires: %name%soversion = %version-%release

%description tools
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%prep
%setup
%patch -b .lfs

%build
%autoreconf
%configure --disable-static \
	%{subst_enable libwebpmux} \
	%{subst_enable libwebpdemux} \
	%{subst_enable libwebpdecoder}
%make_build

%install
%makeinstall_std

%files -n %name%soversion
%_libdir/%name.so.*
%{?_enable_libwebpmux:%_libdir/%{name}mux.so.*}
%{?_enable_libwebpdemux:%_libdir/%{name}demux.so.*}
%{?_enable_libwebpdecoder:%_libdir/%{name}decoder.so.*}

%files devel
%dir %_includedir/webp
%_includedir/webp/decode.h
%_includedir/webp/encode.h
%_includedir/webp/types.h
%if_enabled libwebpmux
%_includedir/webp/mux.h
%_includedir/webp/mux_types.h
%endif
%{?_enable_libwebpdemux:%_includedir/webp/demux.h}
%_libdir/%name.so
%{?_enable_libwebpmux:%_libdir/%{name}mux.so}
%{?_enable_libwebpdemux:%_libdir/%{name}demux.so}
%{?_enable_libwebpdecoder:%_libdir/%{name}decoder.so}
%_pkgconfigdir/%name.pc
%{?_enable_libwebpmux:%_pkgconfigdir/%{name}mux.pc}
%{?_enable_libwebpdemux:%_pkgconfigdir/%{name}demux.pc}
%{?_enable_libwebpdecoder:%_pkgconfigdir/%{name}decoder.pc}

%files tools
%_bindir/cwebp
%_bindir/dwebp
%_man1dir/cwebp.1.*
%_man1dir/dwebp.1.*

%if_enabled libwebpmux
%_bindir/gif2webp
%_bindir/img2webp
%_bindir/webpinfo
%_bindir/webpmux
%_man1dir/gif2webp.1.*
%_man1dir/webpinfo.1.*
%_man1dir/webpmux.1.*
%_man1dir/img2webp.1.*
%endif
%{?_enable_libwebpdemux:%_bindir/vwebp}
%{?_enable_libwebpdemux:%_man1dir/vwebp.1.*}

%changelog
* Sun Jul 14 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sat Jan 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Thu Nov 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Thu Oct 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2.1
- rebuilt with improved libfreeglut-devel

* Wed Oct 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2
- rebuild against libglut.so.3 from libGLUT package

* Sat Apr 21 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Nov 30 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Wed Feb 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Wed Dec 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2 (fixed CVE-2016-8888, CVE-2016-9085)

* Thu Aug 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Nov 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Mon Mar 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Sat Aug 23 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Thu Feb 13 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0-alt2.2
- libwebp5: add O: libwebp = 0.4.0-alt1.

* Wed Feb 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0-alt2.1
- libwebp5: remove obsolete.

* Wed Feb 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0-alt2
- libwebp: add so version to package name.

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Mon Oct 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Thu Apr 11 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Tue Mar 05 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.1
- Rebuilt with libpng15

* Mon Jan 09 2012 Victor Forsiuk <force@altlinux.org> 0.1.3-alt1
- 0.1.3

* Wed Jul 13 2011 Victor Forsiuk <force@altlinux.org> 0.1.2-alt1
- Initial build.
