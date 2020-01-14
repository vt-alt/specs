%define glib2_version 1.0
%define _libexecdir %_prefix/libexec
%define apiversion 1.5.0
%define _name atril

%def_disable introspection
%def_disable libs_subpackage
%def_disable dbus

# it uses webkit
%def_disable epub

Name:           %_name-gtk
Version:        1.22.3
Release:        alt2
Summary:        Document viewer

License:        GPLv2+ and GFDL-1.1+
Group:          Publishing
URL:            https://github.com/mate-desktop/atril
Source0:        %name-%version.tar
# Russian translation updates
Source1:        ru.po
Source2:        help_ru.po
Patch:          %_name-%version-%release.patch

BuildRequires:  libgtk+3-devel
BuildRequires:  glib2-devel
BuildRequires:  libgio-devel
BuildRequires:  libpoppler-glib-devel
BuildRequires:  libXt-devel
BuildRequires:  libtiffxx-devel libtiff-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libspectre-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  t1lib-devel
BuildRequires:  xml-utils
BuildRequires:  yelp-tools
BuildRequires:  gtk-doc
BuildRequires:  gcc-c++
%{?_enable_introspection:BuildRequires:  gobject-introspection-devel}
%{?_enable_epub:BuildRequires: libwebkit2gtk-devel}

BuildRequires:  mate-common
BuildRequires:  libcairo-devel
BuildRequires:  libcairo-gobject-devel
BuildRequires:  libgail3-devel
BuildRequires:  libxml2-devel
BuildRequires:  libX11-devel
BuildRequires:  zlib-devel
BuildRequires:  libSM-devel
BuildRequires:  libgxps-devel

# for the caja properties page
#BuildRequires: mate-file-manager-devel
# for the dvi backend
BuildRequires: libkpathsea-devel
# for the djvu backend
BuildRequires: libdjvu-devel

%if_enabled libs_subpackage
Requires: lib%{name} = %{version}-%{release}
%else
Provides: lib%{name} = %{version}-%{release}
Obsoletes: lib%{name} < %{version}-%{release}
Conflicts: mate-document-viewer-libs

%add_findprov_skiplist %_libdir/*
%filter_from_requires /^\(debug\(64\)\?(\)\?libatril\(document\|view\)\.so\.[[:digit:]]/d
%endif

Conflicts: mate-document-viewer

%define _unpackaged_files_terminate_build 1

%description
Atril is simple multi-page document viewer. It can display and print
Portable Document Format (PDF), PostScript (PS) and Encapsulated
PostScript (EPS) files. When supported by the document format, atril
allows searching for text, copying text to the clipboard, hypertext
navigation, table-of-contents bookmarks and editing of forms.

Support for other document formats such as DVI and DJVU can be added by
installing additional backends.

(version without MATE-specific)

%package -n lib%name
Summary: Libraries for the atril document viewer
Group: System/Libraries
Conflicts: mate-document-viewer-libs

%description -n lib%name
This package contains shared libraries needed for atril


%package -n lib%name-devel
Summary: Support for developing backends for the atril document viewer
Group: Development/C
Requires: lib%name = %{version}-%{release}
Conflicts: mate-document-viewer-devel

%description -n lib%name-devel
This package contains libraries and header files needed for atril
backend development.


%package dvi
Summary: Atril backend for dvi files
Group: Publishing
Requires: %name = %{version}-%{release}
# For /usr/bin/mktexpk  at least
Requires: texlive
Conflicts: mate-document-viewer-devel

%description dvi
This package contains a backend to let atril display dvi files.


%package djvu
Summary: Atril backend for djvu files
Group: Publishing
Requires: %name = %{version}-%{release}
Conflicts: mate-document-viewer-djvu

%description djvu
This package contains a backend to let atril display djvu files.

%package pixbuf
Summary: Atril backend for graphics files
Group: Publishing
Requires: %name = %{version}-%{release}
Conflicts: mate-document-viewer-pixbuf

%description pixbuf
This package contains a backend to let atril display graphics files.

%package xps
Summary: Atril backend for xps files
Group: Publishing
Requires: %name = %{version}-%{release}
Conflicts: mate-document-viewer-xps

%description xps
This package contains a backend to let atril display xps files.

%package epub
Summary: Atril backend for ePub documents
Group: Publishing
Requires: %name = %{version}-%{release}
Conflicts: mate-document-viewer-djvu

%description epub
This package contains a backend to let atril display ePub documents.

%prep
%setup
%patch -p1
cp -a %SOURCE1 po/ru.po
cp -a %SOURCE2 help/ru/ru.po

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static \
	--disable-scrollkeeper \
	--enable-comics \
	--enable-dvi=yes \
	--enable-djvu=yes \
	--enable-t1lib=yes \
	--enable-pixbuf=yes \
	--enable-xps=yes \
	%{subst_enable epub} \
	%{subst_enable introspection} \
	--without-keyring \
	--disable-caja \
	--without-matedesktop \
	%{subst_enable dbus} \
	--disable-gtk-doc

%make_build V=1 LIBTOOL=/usr/bin/libtool

%install
%makeinstall_std

%find_lang %_name

mkdir -p %buildroot%{_datadir}/applications
/bin/rm -rf %buildroot/var/scrollkeeper
# Get rid of static libs and .la files.
rm -f %buildroot%{_libdir}/atril/3/backends/*.la
rm -f %buildroot%{_libdir}/atril/3/backends/*.a
rm -f %buildroot%{_libdir}/*.la
rm -f %buildroot%{_libdir}/*.a

# don't ship icon caches
rm -f %buildroot%{_datadir}/icons/hicolor/icon-theme.cache

%files -f %_name.lang
%{_bindir}/*
%{_datadir}/atril/
%_desktopdir/%_name.desktop
%{_datadir}/icons/hicolor/*/apps/atril.*
%{_mandir}/man1/atril*.1.*
%if_enabled dbus
%{_libexecdir}/atrild
%{_datadir}/dbus-1/services/org.mate.atril.Daemon.service
%endif
%{_datadir}/glib-2.0/schemas/org.mate.Atril.gschema.xml
%{_datadir}/thumbnailers/atril.thumbnailer
%{_datadir}/help/*/*

# don't package appdata file:
# for atril-gtk there should be changed description at least
%exclude %_datadir/metainfo/atril.appdata.xml

%if_enabled libs_subpackage
%files -n lib%name
%endif
%doc README COPYING NEWS AUTHORS
%{_libdir}/libatrilview.so.*
%{_libdir}/libatrildocument.so.*
%dir %{_libdir}/atril
%dir %{_libdir}/atril/3
%dir %{_libdir}/atril/3/backends
%{_libdir}/atril/3/backends/libpdfdocument.so
%{_libdir}/atril/3/backends/pdfdocument.atril-backend
%{_libdir}/atril/3/backends/libpsdocument.so
%{_libdir}/atril/3/backends/psdocument.atril-backend
%{_libdir}/atril/3/backends/libtiffdocument.so
%{_libdir}/atril/3/backends/tiffdocument.atril-backend
%{_libdir}/atril/3/backends/libcomicsdocument.so
%{_libdir}/atril/3/backends/comicsdocument.atril-backend
%if_enabled introspection
%{_libdir}/girepository-1.0/AtrilDocument-*.typelib
%{_libdir}/girepository-1.0/AtrilView-*.typelib
%endif

%if_enabled libs_subpackage
%files -n lib%name-devel
%dir %{_includedir}/atril
%{_includedir}/atril/%apiversion
%{_libdir}/libatrilview.so
%{_libdir}/libatrildocument.so
%{_libdir}/pkgconfig/atril-view-*.pc
%{_libdir}/pkgconfig/atril-document-*.pc
%if_enabled introspection
%{_datadir}/gir-1.0/AtrilDocument-*.gir
%{_datadir}/gir-1.0/AtrilView-*.gir
%endif
%else
%exclude %_includedir/atril/
%exclude %_libdir/pkgconfig/atril-*.pc
%exclude %_libdir/libatril*.so
%endif

%files dvi
%{_libdir}/atril/3/backends/libdvidocument.so*
%{_libdir}/atril/3/backends/dvidocument.atril-backend

%files djvu
%{_libdir}/atril/3/backends/libdjvudocument.so
%{_libdir}/atril/3/backends/djvudocument.atril-backend

%files xps
%{_libdir}/atril/3/backends/libxpsdocument.so*
%{_libdir}/atril/3/backends/xpsdocument.atril-backend

%files pixbuf
%{_libdir}/atril/3/backends/libpixbufdocument.so*
%{_libdir}/atril/3/backends/pixbufdocument.atril-backend

%if_enabled epub
%files epub
%{_libdir}/atril/3/backends/libepubdocument.so*
%{_libdir}/atril/3/backends/epubdocument.atril-backend
%{_libdir}/atril/3/backends/epub/
%endif

%changelog
* Mon Jan 13 2020 Mikhail Efremov <sem@altlinux.org> 1.22.3-alt2
- Patch from upstream:
    tiff: Handle failure from TIFFReadRGBAImageOriented
      (fixes: CVE-2019-11459).
- dvi: Require texlive.
- Update Russian translation (thx Olesya Gerasimenko).

* Tue Dec 24 2019 Mikhail Efremov <sem@altlinux.org> 1.22.3-alt1
- Updated to 1.22.3.

* Fri Nov 08 2019 Mikhail Efremov <sem@altlinux.org> 1.22.2-alt1
- Updated to 1.22.2.

* Wed May 15 2019 Mikhail Efremov <sem@altlinux.org> 1.22.1-alt1
- Updated to 1.22.1.

* Mon Mar 04 2019 Mikhail Efremov <sem@altlinux.org> 1.22.0-alt1
- Updated to 1.22.0.

* Fri Nov 16 2018 Mikhail Efremov <sem@altlinux.org> 1.21.1-alt1
- Updated url.
- Updated to 1.21.1.

* Thu Sep 06 2018 Mikhail Efremov <sem@altlinux.org> 1.21.0-alt1
- Patch from upstream:
  + libview: fix build without epub.
- Updated to 1.21.0.

* Mon Apr 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16.1-alt2
- fix parallel build

* Sat Feb 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.16.1-alt1.1
- NMU: rebuild with texlive 2016

* Thu Nov 10 2016 Mikhail Efremov <sem@altlinux.org> 1.16.1-alt1
- Updated to 1.16.1.

* Tue Sep 20 2016 Mikhail Efremov <sem@altlinux.org> 1.16.0-alt1
- Updated to 1.16.0.

* Tue May 24 2016 Mikhail Efremov <sem@altlinux.org> 1.14.1-alt1
- Updated to 1.14.1.

* Mon Apr 11 2016 Mikhail Efremov <sem@altlinux.org> 1.14.0-alt1
- Updated to 1.14.0.

* Fri Dec 18 2015 Mikhail Efremov <sem@altlinux.org> 1.12.2-alt1
- Updated to 1.12.2.

* Fri Nov 06 2015 Mikhail Efremov <sem@altlinux.org> 1.12.0-alt1
- Patch from upstream:
  + dvi: fix crash due to regression.
- Updated to 1.12.0.

* Wed Oct 28 2015 Mikhail Efremov <sem@altlinux.org> 1.11.0-alt1
- Disabled DBUS support.
- Drop mate-icon-theme-devel from BR.
- Drop obsoleted patches.
- Updated to 1.11.0.

* Tue Jun 16 2015 Mikhail Efremov <sem@altlinux.org> 1.10.0-alt1
- Don't use MateAboutDialog.
- Update "Drop lockdown functionality" patch.
- Drop obsoleted patches.
- Updated to 1.10.0.

* Mon Nov 10 2014 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1
- Updated to 1.8.1.

* Wed Mar 12 2014 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1
- Don't package atril libs as separate subpackage.
- Updated to 1.8.0.

* Tue Feb 25 2014 Mikhail Efremov <sem@altlinux.org> 1.7.90-alt1.git20140225
- Upstream git snapshot (master branch).

* Mon Aug 12 2013 Mikhail Efremov <sem@altlinux.org> 1.6.1-alt1
- Fix descriptions.
- Updated to 1.6.1.

* Tue May 28 2013 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt2
- Fix path to the documentation page.
- Drop lockdown functionality.
- Build without MATE-specific.
- Rename to atril-gtk.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6.0-alt1_0.qa1
- NMU: rebuilt with libarchive.so.13.

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_0
- new version

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt3_0
- added Req: mate-desktop (closes: 28634)

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0
dropped obsolete mate-conf BR:

* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1.1.1
- fixed build

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

