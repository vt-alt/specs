%define _unpackaged_files_terminate_build 1
%define soname 3

Name: wxsvg
Version: 1.5.22
Release: alt2
Epoch: 1

Summary: wxSVG is viewer SVG files
License: GPL
Group: Graphics

Url: http://wxsvg.sourceforge.net
Source: %name-%version.tar
Patch: %name-1.5.14-alt.patch

BuildRequires: gcc-c++ libart_lgpl-devel libpango-devel
BuildRequires: libwxGTK3.1-devel libavformat-devel libswscale-devel
BuildRequires: libexpat-devel libexif-devel

%description
wxSVG is viewer SVG files

%package -n lib%name
License: GPL
Group: System/Libraries
Summary: lib%name is C++ library to create, manipulate and render SVG files

%description -n lib%name
lib%name is C++ library to create, manipulate and render SVG files

%package -n lib%name-devel-static
License: GPL
Group: System/Libraries
Summary: lib%name is static C++ library to create, manipulate and render SVG files
Obsoletes: lib%name-static

%description -n lib%name-devel-static
lib%name is static C++ library to create, manipulate and render SVG files

%package -n lib%name-devel
License: GPL
Group: Development/C++
Summary: Development shared library for wxSVG
Requires: lib%name = %EVR

%description -n lib%name-devel
Development shared library for wxSVG

%prep
%setup
%patch -p2

%build
%add_optflags -std=c++11
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc ChangeLog AUTHORS TODO COPYING
%_bindir/*

%files -n lib%name
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*
%exclude %_libdir/*.a

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-devel
%_includedir/wx*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Wed Apr 29 2020 Anton Farygin <rider@altlinux.ru> 1:1.5.22-alt2
- built with gtk3

* Wed Feb 12 2020 Anton Farygin <rider@altlinux.ru> 1:1.5.22-alt1
- 1.5.22

* Wed Aug 28 2019 Anton Farygin <rider@altlinux.ru> 1:1.5.20-alt1
- 1.5.20

* Tue Jul 23 2019 Anton Farygin <rider@altlinux.ru> 1:1.5.19-alt1
- 1.5.19

* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 1:1.5.18-alt2
- explicit -std=c++11
- minor spec cleanup/fixup

* Wed Jun 05 2019 Anton Farygin <rider@altlinux.ru> 1:1.5.18-alt1
- 1.5.18

* Thu Jan 31 2019 Anton Farygin <rider@altlinux.ru> 1:1.5.16-alt1
- 1.5.16

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 1:1.5.15-alt1
- 1.5.15

* Wed Sep 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.5.14-alt4
- svgview: fixed error messages on start without existing svg file specified as argument.

* Tue Sep 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.5.14-alt3
- Rebuilt with support for older branches.

* Thu Aug 16 2018 Anton Midyukov <antohami@altlinux.org> 1:1.5.14-alt2
- Rebuilt with compat-libwxGTK3.0-gtk2

* Thu Aug 09 2018 Anton Farygin <rider@altlinux.ru> 1:1.5.14-alt1
- 1.5.14

* Tue Jun 26 2018 Anton Farygin <rider@altlinux.ru> 1:1.5.13-alt2
- add %%

* Wed Jun 13 2018 Anton Farygin <rider@altlinux.ru> 1:1.5.13-alt2
- rebuilt for ffmpeg-4

* Wed May 30 2018 Anton Farygin <rider@altlinux.ru> 1:1.5.13-alt1
- 1.5.13

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 1:1.5.12-alt2
- rebuilt with debuginfo-enabled ffmpeg

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 1:1.5.12-alt1
- new version

* Sun Oct 04 2015 Anton Midyukov <antohami@altlinux.org> 1:1.5-alt3
- Rebuilt for new gcc5 C++11 ABI.

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.5-alt2
- Rebuilt with gcc5

* Sat Sep 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.5-alt1
- Version 1.5
- Rebuilt with wxGTK3.1

* Sun Dec 01 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.2.1-alt1
- New version
- Rebuild with libwxGTK3.0

* Tue Apr 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.1.14-alt1
- New version

* Sat Sep 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.1.9-alt1
- New version

* Wed May 23 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.1.8-alt1
- New version
- Drop patches

* Sun Feb 26 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.1.6-alt1
- New version
- Update patch from ubuntu

* Fri Feb 10 2012 Sergey Bolshakov <sbolshakov at altlinux.ru> 1:1.0.10-alt1.4
- rebuilt with restored optflags

* Mon Feb 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.10-alt1.3
- Fixed build with libav 0.8

* Mon Jan 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.10-alt1.2
- Fixed build

* Thu Sep 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.10-alt1.1
- Fixed build

* Sat Aug 13 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.10-alt1
- New version
- Add fix-ftbs-libav-0.7.patch

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.8_1-alt2.1
- Rebuilt with updated wxGTK2.9

* Fri Mar 25 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.8_1-alt2
- Rebuild with libwxGTK2.9-devel

* Sun Mar 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.8_1-alt1
- New version

* Sat Nov 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.7_1-alt1
- New version

* Sun Sep 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.6-alt1
- New version

* Mon Jun 21 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.3-alt1
- New version

* Mon Feb 08 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1:1.0.1-alt1
- New version

* Wed Sep 30 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0r-alt2
- Rebuild with new libavcodec, libavformat
- Fix altlinux-policy-shared-lib-contains-devel-so repocop test

* Sun Nov 30 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0r-alt1
- New version
- Remmove depricated ldconfig call in post

* Fri Oct 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0b11-alt1
- New version

* Sat Mar 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0b8-alt2
- Rename lib%name-static -> lib%name-devel-static

* Tue Jan 22 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0b8-alt1
- built for ALT Linux
