%define api_ver 3.0
%define ver_major 4.2

%def_enable exempi
%def_enable tracker
%def_enable introspection
%def_enable selinux

Name: nemo
Version: %ver_major.2
Release: alt1

Summary: default file manager for Cinnamon
License: GPLv2+
Group: Graphical desktop/GNOME
URL: https://github.com/linuxmint/nemo

Source: %name-%version.tar

Patch: %name-%version-%release.patch

Provides: %name = %version-%release

Requires: %name-translations

%define pkgconfig_ver 0.8
%define icon_theme_ver 2.10.0
%define desktop_file_utils_ver 0.8

%define glib_ver 2.31.9
%define desktop_ver 2.6.1
%define pango_ver 1.28.3
%define gtk_ver 3.9.10
%define libxml2_ver 2.7.8
%define exif_ver 0.6.20
%define exempi_ver 2.2.0
%define gir_ver 0.10.2
%define notify_ver 0.7.0
%define tracker_ver 0.16

Requires(pre): lib%name = %version-%release
Requires: gnome-icon-theme >= %icon_theme_ver

Requires: shared-mime-info
Requires: common-licenses
Requires: gvfs >= 1.9.1

BuildRequires(pre): meson rpm-build-gnome rpm-build-licenses rpm-build-gir
BuildPreReq: pkgconfig >= %pkgconfig_ver
BuildPreReq: desktop-file-utils >= %desktop_file_utils_ver
# for %%check
BuildRequires: xvfb-run dbus-tools-gui /proc

# From configure.in
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libcinnamon-desktop-devel >= %desktop_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgail3-devel
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: intltool >= 0.40.1
BuildPreReq: libexif-devel >= %exif_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildRequires: meson
BuildRequires: libX11-devel xorg-xproto-devel
BuildRequires: docbook-utils gtk-doc
BuildRequires: python3-module-polib python3-module-pygobject3
BuildRequires: libxapps-devel >= 1.0.4
%{?_enable_exempi:BuildPreReq: libexempi-devel >= %exempi_ver}
%{?_enable_tracker:BuildPreReq: tracker-devel >= %tracker_ver}
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}
%{?_enable_selinux:BuildRequires: libselinux-devel}

%description
Nemo integrates access to files, applications, media, Internet-based
resources and the Web.  Nemo delivers a dynamic and rich user
experience.  Nemo is an free software project developed under the
GNU General Public License and is a core component of the Cinnamon desktop
project.

%package -n lib%name
Summary: Shared libraries needed to run Nemo
Group: System/Libraries

%description -n lib%name
This package contains shared libraries needed to run Nemo and its
components.

%package -n lib%name-devel
Summary: Libraries and include files for developing Nemo components
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides the necessary development libraries and include
files to allow you to develop Nemo components.

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: lib%name-devel < %version-%release
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for the %name.

%package -n lib%name-gir
Summary: GObject introspection data for the nemo-extension library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the nemo-extension library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the nemo-extension library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the nemo-extension library

%define _bonobo_servers_dir %_libdir/bonobo/servers

%prep
%setup -q
%patch0 -p1

rm -f data/*.desktop

# make check using xvfb-run
subst 's@\.\/@xvfb-run -a ./@' eel/check-eel src/check-nemo

%build
%meson -D deprecated_warnings=false -D gtk_doc=false
%meson_build

%install
%meson_install

# The license
ln -sf %_licensedir/LGPL-2 COPYING


%files
%_bindir/*
%_libexecdir/nemo-convert-metadata
%_libexecdir/nemo-extensions-list
%_datadir/mime/packages/nemo.xml
%_datadir/applications/*.desktop
%_datadir/%name
%_iconsdir/hicolor/*/*/*
%_datadir/dbus-1/services/nemo.FileManager1.service
%_datadir/dbus-1/services/nemo.service
%_datadir/gtksourceview-2.0/language-specs/nemo_action.lang
%_datadir/gtksourceview-3.0/language-specs/nemo_action.lang
%_datadir/polkit-1/actions/org.nemo.root.policy
# gsettings schemas
%config %_datadir/glib-2.0/schemas/org.nemo.gschema.xml
# docs
%doc --no-dereference COPYING
%doc AUTHORS NEWS README.md THANKS
%_man1dir/*

%files -n lib%name
%_libdir/libnemo-extension.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc docs/*.{txt,html}

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/*

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*
%endif


%changelog
* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 4.2.2-alt1
- 4.2.2

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 4.2.1-alt1
- 4.2.1

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Thu Jan 24 2019 Yuri N. Sedunov <aris@altlinux.org> 4.0.6-alt2
- rebuilt against libexempi.so.8
- updated build dependencies

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 4.0.6-alt1
- 4.0.6-1-g33ab105

* Tue Dec 4 2018 Vladimir Didenko <cow@altlinux.org> 4.0.3-alt1
- 4.0.3-4-gb4d6a97

* Tue Nov 20 2018 Vladimir Didenko <cow@altlinux.org> 4.0.2-alt1
- 4.0.2

* Fri Nov 2 2018 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt1
- 4.0.0

* Tue Oct 23 2018 Vladimir Didenko <cow@altlinux.org> 3.8.6-alt2
- make desktop icons visible by default (closes: #35541)

* Fri Sep 14 2018 Vladimir Didenko <cow@altlinux.org> 3.8.6-alt1
- 3.8.6

* Mon Jul 23 2018 Vladimir Didenko <cow@altlinux.org> 3.8.5-alt1
- 3.8.5

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 3.8.3-alt1
- 3.8.3-4-g17734bf

* Mon May 7 2018 Vladimir Didenko <cow@altlinux.org> 3.8.2-alt1
- 3.8.2-1-gac888ea

* Thu May 3 2018 Vladimir Didenko <cow@altlinux.org> 3.8.1-alt1
- 3.8.1-4-gb35c12b

* Wed Dec 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.5-alt1
- 3.6.5

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 3.6.4-alt1
- 3.6.4

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.2-alt1
- 3.6.2-7-g5842a47

* Wed Aug 23 2017 Vladimir Didenko <cow@altlinux.org> 3.4.7-alt1
- 3.4.7

* Fri Jul 7 2017 Vladimir Didenko <cow@altlinux.org> 3.4.6-alt1
- 3.4.6

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 3.4.5-alt1
- 3.4.5-4-g25fe370

* Thu Jun 8 2017 Vladimir Didenko <cow@altlinux.org> 3.4.2-alt1
- 3.4.2-4-g83812fd

* Sat May 20 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt2
- set default desktop font (closes: #33485)

* Fri May 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 3.2.2-alt1
- 3.2.2

* Fri Nov 11 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Oct 4 2016 Vladimir Didenko <cow@altlinux.org> 3.0.6-alt2
- 3.0.6-48-gaff8272: fixes desktop redraw issue

* Fri Jun 24 2016 Vladimir Didenko <cow@altlinux.org> 3.0.6-alt1
- 3.0.6

* Wed Jun 1 2016 Vladimir Didenko <cow@altlinux.org> 3.0.5-alt1
- 3.0.5

* Tue May 24 2016 Vladimir Didenko <cow@altlinux.org> 3.0.3-alt1
- 3.0.3

* Fri May 20 2016 Vladimir Didenko <cow@altlinux.org> 3.0.2-alt1
- 3.0.2

* Fri May 13 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- 3.0.1-4-gdedb4f8

* Tue Apr 26 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Mar 16 2016 Vladimir Didenko <cow@altlinux.org> 2.8.7-alt2.git20160420
- git20160420 (94c6036)

* Wed Mar 16 2016 Vladimir Didenko <cow@altlinux.org> 2.8.7-alt1
- 2.8.7

* Mon Dec 14 2015 Vladimir Didenko <cow@altlinux.org> 2.8.6-alt1
- 2.8.6

* Tue Nov 24 2015 Vladimir Didenko <cow@altlinux.org> 2.8.5-alt1
- 2.8.5

* Mon Nov 16 2015 Vladimir Didenko <cow@altlinux.org> 2.8.4-alt1
- 2.8.4-2-g6022095

* Tue Oct 27 2015 Vladimir Didenko <cow@altlinux.org> 2.8.1-alt1
- 2.8.1

* Wed Oct 21 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0-1-g4252c3e

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.7.0-alt1
- 2.7.0

* Tue Jun 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.7-alt1
- 2.6.7

* Tue Jun 16 2015 Vladimir Didenko <cow@altlinux.org> 2.6.6-alt1
- 2.6.6

* Thu May 28 2015 Vladimir Didenko <cow@altlinux.org> 2.6.5-alt1
- 2.6.5

* Sat May 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.3-alt1
- 2.6.3-5-g9d971fe

* Wed May 20 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri May 8 2015 Vladimir Didenko <cow@altlinux.org> 2.5.1-alt2
- git20150505

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.1-alt1
- 2.5.1

* Tue Nov 25 2014 Vladimir Didenko <cow@altlinux.org> 2.4.4-alt1
- 2.4.4

* Tue Nov 11 2014 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- 2.4.1

* Wed Nov 5 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0-2-gc3d7c1e

* Tue Oct 14 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- git20141011

* Thu Aug 21 2014 Vladimir Didenko <cow@altlinux.org> 2.2.4-alt1
- 2.2.4

* Tue Jul 22 2014 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- 2.2.3

* Mon May 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1

* Wed Apr 27 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt2
- 2.2.0-11-ge78efe4

* Mon Apr 7 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Tue Mar 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.7-alt2
- build with gnome-3.12

* Mon Nov 25 2013 Vladimir Didenko <cow@altlinux.org> 2.0.7-alt1
- 2.0.7-1-g730e132

* Tue Nov 12 2013 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt1
- 2.0.6

* Tue Nov 5 2013 Vladimir Didenko <cow@altlinux.org> 2.0.5-alt1
- 2.0.5

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt4
- rebuild for GNOME-3.10

* Mon Sep 16 2013 Vladimir Didenko <cow@altlinux.org> 1.8.5-alt3
- git20130915

* Fri Sep 6 2013 Vladimir Didenko <cow@altlinux.org> 1.8.5-alt2
- supress gtk DEPRECATED to build with gtk-3.9

* Wed Aug 12 2013 Vladimir Didenko <cow@altlinux.org> 1.8.5-alt1
- 1.8.5-68-g60bbdec

* Wed Aug 12 2013 Vladimir Didenko <cow@altlinux.org> 1.8.4-alt3
- updated translations

* Mon Aug 12 2013 Vladimir Didenko <cow@altlinux.org> 1.8.4-alt2
- dropped background manager patch

* Wed Aug 7 2013 Vladimir Didenko <cow@altlinux.org> 1.8.4-alt1
- 1.8.4-12-gd9c3464

* Wed Jun 5 2013 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- 1.8.3

* Tue May 21 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt1
- 1.8.2

* Fri May 17 2013 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon May 6 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Apr 26 2013 Vladimir Didenko <cow@altlinux.org> 1.7.3-alt1
- 1.7.3-6-g91617c8

* Fri Apr 5 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt4
- rebuilt for Sisyphus

* Fri Mar 22 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt3
- don't show desktop icons on default
- don't autostart nemo

* Tue Mar 12 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt2
- clean up code to build with gnome-3.7

* Wed Feb 20 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt1
- update to 1.7.1

* Thu Dec 6 2012 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt2
- Added directory for extensions

* Thu Nov 15 2012 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt1
- update to 1.1.2
- fixed Open in terminal functionality

* Tue Nov 13 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.1.1-alt1
- update to 1.1.1

* Tue Nov 6 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.1.0-alt1
- update to 1.1.0

* Thu Nov 1 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.0.7-alt1
- update to 1.0.7

* Mon Oct 8 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.0.3-alt1
- update to 1.0.3

* Thu Oct 4 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.0.2-alt1
- First build
