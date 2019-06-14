%def_with pstoedit
%def_disable static

Name: autotrace
Version: 0.31.1
Release: alt9

Summary: Bitmap to vector graphics converter
Summary(ru_RU.UTF-8): Программа трассировки растровых изображений.
Group: Graphics
License: GPLv2+ and LGPLv2+
Url: http://%name.sourceforge.net/

Source: %name-%version.tar
Patch: %name-0.31.1-configure_in-deb-alt.patch
Patch1: %name-0.31.1-makefile_am-deb.patch
Patch2: %name-0.31.1-docs-deb.patch
Patch3: %name-0.31.1-gcc41-deb.patch
Patch4: %name-0.31.1-pc_in-deb.patch
Patch5: %name-0.31.1-unneeded_libs-alt.patch
Patch6: %name-0.31.1-libpng-1.5.patch
Patch7: %name-0.31.1-CVE-2013-1953-deb.patch
Patch8: %name-0.31.1-CVE-2016-7392.patch

%define pstoedit_ver 3.32

Requires: lib%name = %version-%release
BuildRequires(pre):rpm-build-ubt

%if_with pstoedit
BuildPreReq: libpstoedit-devel >= %pstoedit_ver
%endif

# Automatically added by buildreq on Mon Jan 08 2007
#BuildRequires: gcc-c++ glibc-devel-static libImageMagick-devel libpng-devel libpstoedit-devel
BuildRequires: libImageMagick-devel libpng-devel libpstoedit-devel

%description
The aim of the AutoTrace project is the development of a freely
available application with a functionality similar to CorelTrace or
Adobe Streamline. I hope that it will become better than all
commercially available programs. In some aspects it is already better.

Supported formats:
Input BMP, TGA, PNM, PPM, PGM, PBM and those supported by ImageMagick.
Export Postscript, svg, xfig, swf, pstoedit, emf, dxf, cgm, mif, p2e and sk

%description -l ru_RU.UTF-8
%name - программа преобразования растровых изображений в векторные.

Поддерживаемые форматы:
Растровые: BMP, TGA, PNM, PPM, PGM, PBM и прочие, поддерживаемые программой ImageMagick.
Векторные: Postscript, svg, xfig, swf, pstoedit, emf, dxf, cgm, mif, p2e и sk

%package -n lib%name
Summary: Shared library for %name
Group: System/Libraries
License: LGPL

%description -n lib%name
Shared library needed to run %name.

%package -n lib%name-devel
Summary: Development package of %name
Group: Development/C
License: LGPL
Requires: lib%name = %version-%release
Requires: libImageMagick-devel
%if_with pstoedit
Requires: libpstoedit-devel >= %pstoedit_ver
%endif

%description -n lib%name-devel
Headers files needed to compile programs using lib%name.

%package -n lib%name-devel-static
Summary: Static version of lib%name
Group: System/Libraries
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static library required for packaging statically
linked software using lib%name.

%prep
%setup -q -n %name-%version
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p1
%patch8 -p1


%build
%ifdef cvs_date
%__subst 's@autoconf@autoconf_2.5@' autogen.sh
%__subst 's@autoheader@autoheader_2.5@' autogen.sh
./autogen.sh
%endif

autoreconf -fisv
%configure %{subst_enable static} \
%if_without pstoedit
	--without-pstoedit
%endif

%__subst s/-lstdc++// Makefile
%make_build
%__subst s/-lstdc++// %name-config

%install
%makeinstall

%files
%_bindir/%name
%_man1dir/*
%doc README* NEWS AUTHORS ChangeLog THANKS HACKING

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/%name
%_libdir/*.so
%_libdir/pkgconfig/*
%_datadir/aclocal/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Wed Jun 05 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.31.1-alt9
- resurrect in sisyphus

* Fri Aug 18 2017 Anton Farygin <rider@altlinux.ru> 0.31.1-alt8%ubt
- Rebuild with new libImageMagick.

* Tue Jul 25 2017 Anton Farygin <rider@altlinux.ru> 0.31.1-alt7%ubt
- fixed CVE-2016-7392

* Fri May 06 2016 Anton Farygin <rider@altlinux.ru> 0.31.1-alt6
- fixed CVE-2013-1953

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 0.31.1-alt5
- Rebuild with new libImageMagick

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 0.31.1-alt4
- Rebuild with new libImageMagick

* Tue Sep 18 2012 Anton Farygin <rider@altlinux.ru> 0.31.1-alt3
- cleanup spec
- add patch from gentoo for fix build with new libpng

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.31.1-alt2.4.1
- Rebuild with new libImageMagick

* Mon Sep 13 2010 Anton Farygin <rider@altlinux.ru> 0.31.1-alt2.4
- rebuild with new libImageMagick

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 0.31.1-alt2.3
- rebuild with new libImageMagick

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.31.1-alt2.2
- Removed obsolete post_ldconfig/postun_ldconfig calls.
- Rebuilt with libMagickCore.so.2.

* Sat Dec 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.31.1-alt2.1
- Automated rebuild with libImageMagick-6.4.x.

* Mon Jan 08 2007 Yury Aliaev <mutabor@altlinux.org> 0.31.1-alt2
- Fixed for modern Sisyphus building environment (much thanks to Debian people :))

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.31.1-alt1.6.1
- Rebuilt for new pkg-config dependencies.

* Thu Sep 15 2005 Anton Farygin <rider@altlinux.ru> 0.31.1-alt1.6
- rebuild with libMagick.so.9

* Mon Sep 12 2005 Anton Farygin <rider@altlinux.ru> 0.31.1-alt1.5
- rebuild with new libImageMagick

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.31.1-alt1.4.1.1
- Rebuilt with libstdc++.so.6.

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.31.1-alt1.4.1
- Rebuilt with libtiff.so.4.

* Thu May 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.31.1-alt1.4
- fixed build.

* Thu Dec 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.31.1-alt1.3
- do not package .la files.
- devel-static subpackage is optional. 

* Tue Sep 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.31.1-alt1.2
- rebuild due ImageMagick depends on new libexif.

* Mon Sep 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.31.1-alt1.1
- updated buildreqs.

* Wed Nov 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.31.1-alt1
- 0.31.1

* Fri Oct 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.31.0-alt1
- 0.31.0

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.30.5-alt0.5cvs20020917
- fix changelog entry

* Mon Sep 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.30.5-alt0.5
- 0.30.5 from cvs
- built w/o libming (SWF output disabled) and pstoedit support.
- we have shared library now.

* Thu Apr 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.30-alt0.5
- 0.30

* Sat Mar 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.29-alt0.5
- First build for Sisyphus w/o shared library (makefile don't 
  supports it) and w/o swf-output support, it requires libming.
