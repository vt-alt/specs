%define _libexecdir %_prefix/libexec
%define oldname eog2
%define ver_major 3.32
%define xdg_name org.gnome.eog
%define api_ver 3.0
%def_enable color_management
%def_enable introspection
%def_enable gtk_doc
# python-behave required
%def_disable installed_tests

Name: eog
Version: %ver_major.2
Release: alt1

Summary: Eye Of Gnome
License: %gpl2plus
Group: Graphics
Url: https://wiki.gnome.org/Apps/EyeOfGnome

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Provides: %oldname = %version-%release
Obsoletes: %oldname < 2.14.2-alt1

%add_findprov_lib_path %_libdir/%name
%set_typelibdir %_libdir/%name/girepository-1.0
%set_girdir %_datadir/%name/gir-1.0

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_path %_libdir/%name/plugins
# required dogtail and behave use python2
#%{?_enable_installed_tests:%_libexecdir/%name/installed-tests}

BuildRequires(pre): meson rpm-build-gnome rpm-build-licenses
BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-devel yelp-tools libappstream-glib-devel
BuildPreReq: libgtk+3-devel >= 3.22
BuildPreReq: libgio-devel >= 2.42.0
BuildPreReq: libgnome-desktop3-devel >= 3.0
BuildPreReq: gnome-icon-theme >= 2.19.1
BuildPreReq: shared-mime-info >= 0.60
BuildPreReq: libexempi-devel >= 1.99.5
BuildPreReq: libexif-devel >= 0.6.14
%{?_enable_color_management:BuildPreReq: liblcms2-devel}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
BuildPreReq: libjpeg-devel librsvg-devel
BuildPreReq: libpeas-devel >= 0.7.4
BuildRequires: libXt-devel libxml2-devel perl-XML-Parser zlib-devel gsettings-desktop-schemas-devel
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.10.2 libgtk+3-gir-devel}

%description
This is the Eye of GNOME, an image viewer program. It is meant to be
a fast and functional image viewer as well as an image cataloging
program.

%package devel
Summary: Development files for EOG viewer
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains files necessary to develop plugins for Eye of GNOME.

%package devel-doc
Summary: Development documentation for EOG viewer
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains documentation necessary to develop plugins for Eye
of GNOME.

%package gir
Summary: GObject introspection data for the EOG
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Eye of GNOME

%package gir-devel
Summary: GObject introspection devel data for the EOG
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Eye of GNOME

%package tests
Summary: Tests for the EOG
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the EOG GUI.


%prep
%setup

%build
%meson \
    -Dlibexif=true \
    -Dxmp=true \
    -Dlibjpeg=true \
    -Dlibrsvg=true \
    -Denable-schemas-compile=false \
    %{?_enable_introspection:-Dintrospection=true} \
    %{?_enable_color_management:-Dcms=true} \
    %{?_enable_installed_tests:-Dinstalled-tests=true} \
    %{?_enable_gtk_doc:-Dgtk_doc=true}

%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%dir %_datadir/%name
%_datadir/%name/icons/
%dir %_libdir/%name
%_libdir/%name/lib%name.so
%dir %_libdir/%name/plugins/
%_libdir/%name/plugins/*.so
%_libdir/%name/plugins/*.plugin
%_iconsdir/hicolor/*/apps/%{xdg_name}*.*
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%config %_datadir/glib-2.0/schemas/%xdg_name.enums.xml
%_datadir/GConf/gsettings/eog.convert
%_datadir/metainfo/%name.appdata.xml
%doc AUTHORS HACKING MAINTAINERS NEWS
%doc README THANKS TODO

%files devel
%dir %_includedir/%name-%api_ver/%name
%_includedir/%name-%api_ver/%name/*.h
%_pkgconfigdir/%name.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files gir
%_libdir/%name/girepository-1.0/Eog-%api_ver.typelib

%files gir-devel
%_datadir/%name/gir-1.0/Eog-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/%name/installed-tests/
%_datadir/installed-tests/%name/
%endif


%changelog
* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.4-alt1
- 3.28.4

* Mon Jul 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Thu Apr 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.28.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Thu Nov 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.5-alt1
- 3.20.5

* Sun Aug 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4 (CVE-2016-6855)

* Mon Jun 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sun Feb 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2 (CVE-2013-7447)

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Sep 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.92-alt1
- 3.17.92

* Tue Aug 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Thu Nov 20 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Thu Sep 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Jul 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Sat Jun 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Tue Nov 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Sep 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Sat Jun 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sun Apr 10 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- fixed typelib/gir install

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Mar 09 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.91-alt1
- 2.91.91

* Tue Nov 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Mon Oct 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Sep 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.92-alt1
- 2.31.92

* Wed Sep 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.91-alt1
- 2.31.91

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon May 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Thu Dec 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Sun Aug 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90
- updated buildreqs

* Wed Jul 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Wed Jun 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt2
- fixed install for automake-1.11

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Mon Jan 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3.1-alt1
- 2.24.3.1

* Mon Dec 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt2
- updated buildreqs

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Mon Oct 27 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- rebuild against libgnome-desktop-2.so.7

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Mon Sep 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- New version (2.22.3).

* Sat Apr 12 2008 Alexey Rusakov <ktirf@altlinux.org> 2.22.1-alt1
- New version (2.22.1).
- Build with libexempi.
- Updated buildreqs.
- Added update/cleanup_menus macros (thanks to repocop).

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 2.20.3-alt1.1
- Rebuilt with python-2.5.

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.3-alt1
- new version (2.20.3)
- add Packager

* Tue Oct 16 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.1-alt1
- new version (2.20.1)
- use rpm-build-gnome and rpm-build-licenses.
- added devel subpackage
- updated dependencies and files list
- removed no more needed subst that fixed building with liblcms.

* Thu Feb 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt2
- added autoreconf to fix build on x86_64.

* Wed Jan 31 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version 2.16.3 (with rpmrb script)
- exclude scrollkeeper files explicitly.

* Sat Sep 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version (2.16.1)
- updated dependencies

* Tue Jul 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt1
- new version 2.15.90.
- -Denable-scrollkeeper=false actually works, no more need to %%exclude files.

* Mon Jun 19 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2
- fixed building with lcms and enabled color_management.
- removed '2' from the package name.

* Sat Apr 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Sat Feb 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version (2.13.90)
- cleaned up the spec, revised dependencies
- removed Debian menu support

* Thu Jan 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.4-alt1
- new version

* Thu Jan 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.3-alt1
- new version

* Sun Nov 13 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- New version.
- BuildReqs updated.

* Tue Oct 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version
- Updated dependencies from configure.in

* Wed Oct 05 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed unneeded buildreqs.

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1.1
- rebuild against libexif.so.12.

* Tue Mar 29 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Sun Mar 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.0-alt1
- 2.9.0

* Wed Dec 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Thu Apr 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Sat Mar 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt1
- 2.5.6

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Fri Sep 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- rebuild with new libexif 0.5.12.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Thu Jul 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Wed Jul 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Fri Jun 06 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Wed Apr 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Jan 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Tue Nov 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Tue Oct 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.0-alt1
- 1.1.0
- buildreqs/reqs updated (eog uses libglade2 now)
- %%files section fixed.

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt2
- rebuild with new pango, gtk+

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3
- updated buildrequires

* Thu Jul 04 2002 Igor Androsov <blake@altlinux.ru> 1.0.1-alt1
- First build for Sisyphus.
