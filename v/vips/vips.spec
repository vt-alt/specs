%def_enable introspection
%def_enable gtk_doc
%def_disable static

Name: vips
Version: 8.10.1
Release: alt1

Summary: Large image processing library

License: LGPLv2.1
Group: Graphics
Url: https://libvips.github.io/libvips/

# Source0-url: https://github.com/libvips/libvips/archive/v%version.tar.gz
Source0: %name-%version.tar
Source100: vips.watch

BuildRequires: rpm-build-python3
BuildRequires: libxml2-devel libexpat-devel
BuildRequires: gcc-c++ libImageMagick-devel libcfitsio-devel libexif-devel libfftw3-devel
BuildRequires: liblcms2-devel libmatio-devel liborc-devel libpango-devel openexr-devel
BuildRequires: libjpeg-devel libpng-devel libtiff-devel libgif-devel libimagequant-devel
BuildRequires: libwebp-devel libopenslide-devel librsvg-devel libpoppler-glib-devel

%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgdk-pixbuf-gir-devel}


%define majorver %(echo %version |cut -d. -f1,2)

%description
VIPS is an image processing library. It is good for very large
images (ie.  larger than the amount of RAM in your machine),
and for working with colour.  It includes a C++ API, complete
man pages, a command-line interface, automatic threading and
an operation database. There are several user interfaces built
on top of VIPS: for example "nip2".

%package -n lib%name
Summary: VIPS development kit
Group: System/Libraries

%package -n lib%name-devel
Summary: VIPS development kit
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < 7.16.3-alt3

%package -n lib%name-devel-doc
Summary: VIPS development kit documentation
Group: Development/C
BuildArch: noarch

%package -n lib%name-devel-static
Summary: VIPS static libraries
Group: Development/C
Requires: lib%name-devel = %version-%release
Provides: %name-devel-static = %version-%release
Obsoletes: %name-devel-static < 7.16.3-alt3

%package -n lib%name-gir
Summary: GObject introspection data for VIPS
Group: System/Libraries
Requires: %name = %EVR

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for VIPS
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %EVR
Requires: lib%name-gir = %EVR

%description -n lib%name
Shared libraries for VIPS.

%description -n lib%name-devel
Development libraries and header files for VIPS.

%description -n lib%name-devel-doc
This package contains development documentation for VIPS.

%description -n lib%name-devel-static
Static libraries for developing statically linked VIPS applications.

%description -n lib%name-gir
GObject introspection data for VIPS.

%description -n lib%name-gir-devel
GObject introspection devel data for VIPS.

%prep
%setup
%__subst "s|/usr/bin/python$|%__python3|" tools/vipsprofile
# Avoid setting RPATH to /usr/lib64 on 64-bit builds
# The DIE_RPATH_DIE trick breaks the build wrt gobject-introspection
#sed -i 's|sys_lib_dlsearch_path_spec="|sys_lib_dlsearch_path_spec="/%{_lib} %{_libdir} |' configure

%build
gtkdocize --copy --docdir doc --flavour no-tmpl
glib-gettextize --force --copy
%autoreconf
%configure %{subst_enable static} \
           %{subst_enable introspection} \
           %{?_enable_gtk_doc --enable-gtk-doc}
%make_build

%install
%makeinstall_std
%find_lang vips%majorver
find %buildroot \( -name '*.la' -o -name '*.a' \) -exec rm -f {} ';'
# remove unneeded wrapper
rm -fv %buildroot%_bindir/vips%majorver

%files -f vips%{majorver}.lang
%_bindir/*
%_man1dir/*
#_docdir/vips

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/vips/
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib*.a
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir
%endif

# TODO:
# - OpenSlide, v4l
# - package python bindings

%changelog
* Sat Sep 05 2020 Vitaly Lipatov <lav@altlinux.ru> 8.10.1-alt1
- new version 8.10.1 (with rpmrb script)

* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 8.9.2-alt1
- new version 8.9.2 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 8.9.0-alt2
- enable build with poppler-glib, rsvg, libgif, libimagequant

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 8.9.0-alt1
- NMU: new version 8.9.0 (with rpmrb script)
- update source url, update watch file
- pack gir subpackages

* Tue May 29 2018 Anton Farygin <rider@altlinux.ru> 8.4.5-alt3
- rebuilt for ImageMagick

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 8.4.5-alt2
- rebuilt for ImageMagick

* Sun Dec 11 2016 Michael Shigorin <mike@altlinux.org> 8.4.5-alt1
- new version (watch file uupdate)

* Sat Nov 12 2016 Michael Shigorin <mike@altlinux.org> 8.4.4-alt1
- new version (watch file uupdate)

* Thu Oct 13 2016 Michael Shigorin <mike@altlinux.org> 8.4.2-alt1
- new version (watch file uupdate)

* Sat Sep 24 2016 Michael Shigorin <mike@altlinux.org> 8.4.1-alt1
- new version (watch file uupdate)

* Fri Aug 05 2016 Michael Shigorin <mike@altlinux.org> 8.3.3-alt1
- new version (watch file uupdate)

* Tue Jul 26 2016 Michael Shigorin <mike@altlinux.org> 8.3.2-alt1
- new version (watch file uupdate)

* Wed May 11 2016 Michael Shigorin <mike@altlinux.org> 8.3.1-alt1
- new version (watch file uupdate)

* Fri Apr 15 2016 Michael Shigorin <mike@altlinux.org> 8.3.0-alt1
- new version (watch file uupdate)

* Tue Mar 22 2016 Michael Shigorin <mike@altlinux.org> 8.2.3-alt1
- new version (watch file uupdate)

* Thu Jan 28 2016 Michael Shigorin <mike@altlinux.org> 8.2.2-alt1
- new version (watch file uupdate)

* Mon Jan 11 2016 Michael Shigorin <mike@altlinux.org> 8.2.1-alt1
- new version (watch file uupdate)

* Thu Oct 15 2015 Michael Shigorin <mike@altlinux.org> 8.1.1-alt1
- new version (watch file uupdate)

* Wed Oct 07 2015 Michael Shigorin <mike@altlinux.org> 8.1.0-alt1
- new version (watch file uupdate)

* Wed May 06 2015 Michael Shigorin <mike@altlinux.org> 8.0.2-alt1
- new version (watch file uupdate)

* Mon May 04 2015 Michael Shigorin <mike@altlinux.org> 8.0.1-alt1
- new version (watch file uupdate)

* Fri Feb 13 2015 Michael Shigorin <mike@altlinux.org> 7.42.3-alt1
- new version (watch file uupdate)

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 7.42.2-alt1
- new version (watch file uupdate)

* Fri Oct 10 2014 Michael Shigorin <mike@altlinux.org> 7.40.11-alt1
- new version (watch file uupdate)

* Wed Oct 01 2014 Michael Shigorin <mike@altlinux.org> 7.40.10-alt1
- new version (watch file uupdate)

* Tue Sep 23 2014 Michael Shigorin <mike@altlinux.org> 7.40.9-alt1
- new version (watch file uupdate)

* Wed Sep 10 2014 Michael Shigorin <mike@altlinux.org> 7.40.8-alt1
- new version (watch file uupdate)

* Tue Sep 09 2014 Michael Shigorin <mike@altlinux.org> 7.40.7-alt1
- new version (watch file uupdate)

* Mon Aug 25 2014 Michael Shigorin <mike@altlinux.org> 7.40.6-alt1
- new version (watch file uupdate)

* Tue Aug 12 2014 Michael Shigorin <mike@altlinux.org> 7.40.5-alt1
- new version (watch file uupdate)

* Thu Jul 17 2014 Michael Shigorin <mike@altlinux.org> 7.40.4-alt1
- new version (watch file uupdate)

* Fri Jul 04 2014 Michael Shigorin <mike@altlinux.org> 7.40.3-alt1
- new version (watch file uupdate)

* Mon Jun 30 2014 Michael Shigorin <mike@altlinux.org> 7.40.2-alt1
- new version (watch file uupdate)

* Wed Jun 25 2014 Michael Shigorin <mike@altlinux.org> 7.40.1-alt1
- new version (watch file uupdate)

* Thu Jun 19 2014 Michael Shigorin <mike@altlinux.org> 7.38.6-alt1
- new version (watch file uupdate)
- built with openslide

* Wed Apr 02 2014 Michael Shigorin <mike@altlinux.org> 7.38.5-alt1
- new version (watch file uupdate)
- build with lcms2 instead of lcms (closes: #29945)

* Mon Jan 20 2014 Michael Shigorin <mike@altlinux.org> 7.38.1-alt1
- new version (watch file uupdate)

* Sun Dec 22 2013 Michael Shigorin <mike@altlinux.org> 7.36.5-alt1
- new version (watch file uupdate)

* Sat Nov 23 2013 Michael Shigorin <mike@altlinux.org> 7.36.4-alt1
- new version (watch file uupdate)

* Tue Nov 12 2013 Michael Shigorin <mike@altlinux.org> 7.36.3-alt1
- new version (watch file uupdate)

* Thu Oct 24 2013 Michael Shigorin <mike@altlinux.org> 7.36.2b-alt1
- new version (watch file uupdate)

* Sun Oct 13 2013 Michael Shigorin <mike@altlinux.org> 7.36.1-alt1
- new version (watch file uupdate)

* Mon Jul 22 2013 Michael Shigorin <mike@altlinux.org> 7.34.1-alt1
- new version (watch file uupdate)
- get rid of %%_libdir in RPATH (kludge borrowed from fedora spec)
- get lost translations back

* Wed May 22 2013 Michael Shigorin <mike@altlinux.org> 7.32.3-alt1
- new version (watch file uupdate)

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 7.30.7-alt2
- Rebuild with new libImageMagick

* Tue Apr 09 2013 Michael Shigorin <mike@altlinux.org> 7.32.2-alt1
- new version (watch file uupdate)

* Fri Mar 22 2013 Michael Shigorin <mike@altlinux.org> 7.32.1-alt1
- new version (watch file uupdate)
- disabled autoreconf

* Thu Feb 28 2013 Michael Shigorin <mike@altlinux.org> 7.30.8-alt1
- new version (watch file uupdate)

* Wed Feb 20 2013 Michael Shigorin <mike@altlinux.org> 7.30.7-alt1
- new version (watch file uupdate)
- dropped patch (merged upstream)

* Sun Oct 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.30.3-alt1.4
- Rebuilt with libmatio 1.5.0

* Wed Oct 24 2012 Michael Shigorin <mike@altlinux.org> 7.30.3-alt1.3
- patched vipsCC.pc and dropped "bootstrap" scaffolding altogether

* Tue Oct 23 2012 Michael Shigorin <mike@altlinux.org> 7.30.3-alt1.2
- actually bootstrap 7.30 by temporarily dropping vipsCC-7.30.pc
  + there's a new shiny knob for bootstrapping, btw

* Fri Oct 12 2012 Michael Shigorin <mike@altlinux.org> 7.30.3-alt1
- new version (watch file uupdate)

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.28.9-alt1.1
- Rebuilt with libpng15

* Mon Sep 17 2012 Michael Shigorin <mike@altlinux.org> 7.30.2-alt1
- new version (watch file uupdate)

* Thu Aug 23 2012 Michael Shigorin <mike@altlinux.org> 7.30.0-alt1
- new version (watch file uupdate)

* Mon Jul 09 2012 Michael Shigorin <mike@altlinux.org> 7.28.9-alt1
- new version (watch file uupdate)

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 7.28.5-alt1.1
- Rebuild with new libImageMagick

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 7.28.5-alt1
- new version (watch file uupdate)

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 7.28.4-alt1
- 7.28.4

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.26.7-alt1.1
- Fixed build

* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 7.26.7-alt1
- 7.26.7
- drop RPATH

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 7.26.3-alt1
- 7.26.3 (thx fedorawatch)
- drop man3 following upstream
- built with orc, cfitsio

* Mon Apr 04 2011 Michael Shigorin <mike@altlinux.org> 7.24.4-alt1
- 7.24.4

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 7.24.2-alt1
- 7.24.2 (thanks force@)

* Sat Oct 16 2010 Michael Shigorin <mike@altlinux.org> 7.22.4-alt1
- 7.22.4
- minor spec cleanup

* Sat Oct 16 2010 Michael Shigorin <mike@altlinux.org> 7.22.3-alt1
- 7.22.3 fixes CVE-2010-3364 (insecure library loading);
  thanks crux@ for heads-up (closes: #24330)

* Mon Sep 13 2010 Anton Farygin <rider@altlinux.ru> 7.22.2-alt1.1
- NMU: rebuild with new libImageMagick

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 7.22.2-alt1
- 7.22.2

* Wed Jul 14 2010 Anton Farygin <rider@altlinux.ru> 7.20.4-alt1.1
- NMU: rebuild with new libImageMagick

* Thu Dec 03 2009 Victor Forsyuk <force@altlinux.org> 7.20.4-alt1
- 7.20.4
- Build with all libraries vips can make use of (fftw3, openexr etc).

* Mon Aug 10 2009 Michael Shigorin <mike@altlinux.org> 7.18.2-alt1
- 7.18.2

* Fri Mar 20 2009 Michael Shigorin <mike@altlinux.org> 7.16.4-alt1
- 7.16.4
- autoreconf

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt3
- performed libification
- disabled static subpackage by default
- added Packager:
- minor spec cleanup

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt2
- applied repocop patch

* Mon Nov 17 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt1
- 7.16.3

* Tue Oct 07 2008 Michael Shigorin <mike@altlinux.org> 7.16.2-alt1
- 7.16.2
- spec cleanup
- NB: this package seeks proper maintainer

* Tue Jun 21 2005 Anatoly Yakushin <jaa@altlinux.ru> 7.10.10-alt1
- new stable version

* Wed Mar 09 2005 Anatoly Yakushin <jaa@altlinux.ru> 7.10.8-alt1
- new stable version

* Wed Dec 17 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.9.0-alt2
- delete *.la files

* Thu Oct 23 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.9.0-alt1
- new version. spec clean

* Mon Sep 15 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.11-alt1
- new version

* Thu May 22 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.8-alt2
- bug fix spec file

* Thu May 08 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.8-alt1
- adapting spec from Sisyphus

* Mon Feb 3 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.6-2
- hack to change default install prefix to /usr/local

* Thu Jan 30 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.7-1
- first stab at an rpm package for vips
