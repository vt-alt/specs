%define _libexecdir %_prefix/libexec
%define ver_major 4.2
%define api_ver 3.0
%def_disable static
%def_enable gtk_doc
%def_enable introspection

Name: cinnamon-desktop
Version: %ver_major.0
Release: alt1

Summary: Library with common API for various Cinnamon modules
License: %gpl2plus, %fdl
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/cinnamon-desktop
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: lib%name = %version-%release
Requires: icon-theme-hicolor
# use pnp.ids from hwdatabase package
Requires: hwdatabase >= 0.3.31-alt1

BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.in
BuildPreReq: intltool >= 0.35
BuildPreReq: libgtk+3-devel >= 3.3.6
BuildPreReq: glib2-devel >= 2.35.0
BuildPreReq: libgio-devel >= 2.28.0
BuildPreReq: yelp-tools itstool
BuildPreReq: gtk-doc >= 1.4
BuildPreReq: gnome-common >= 2.8.0
BuildPreReq: gsettings-desktop-schemas-devel >= 3.5.91
BuildRequires: meson
BuildRequires: iso-codes-devel
BuildRequires: libSM-devel libXrandr-devel libXext-devel xkeyboard-config-devel libxkbfile-devel
BuildRequires: hwdatabase >= 0.3.31-alt1
BuildRequires: libpulseaudio-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel gsettings-desktop-schemas-gir-devel}
BuildRequires: libaccountsservice-devel

%description
Cinnamon is a Linux desktop which provides advanced innovative features
and a traditional user experience. The desktop layout is similar to Gnome 2.
The underlying technology is forked from Gnome Shell. The emphasis is
put on making users feel at home and providing them with an easy to use and
comfortable desktop experience. The Cinnamon Desktop provides the core libraries
for the Cinnamon desktop.

%package -n %name-schemas
Summary: A collection of GSettings schemas for Cinnamon
Group: Graphical desktop/GNOME
License: %lgpl2plus
BuildArch: noarch

%description -n %name-schemas
A collection of GSettings schemas for Cinnamon

%package -n %name-data
Summary: Data files for Cinnamon desktop libraries
Group: Graphical desktop/GNOME
License: %lgpl2plus

%description -n %name-data
Data files for Cinnamon desktop libraries

%package -n lib%name
Summary: Cinnamon desktop core libraries
Group: Graphical desktop/GNOME
License: %lgpl2plus
Requires: %name-schemas
Requires: %name-data

%description -n lib%name
Cinnamon desktop libraries.

%package -n lib%name-devel
Summary: Cinnamon desktop development libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release
License: %lgpl2plus, %fdl

%description -n lib%name-devel
Cinnamon desktop libraries and header files for creating GNOME applications.

%if_enabled static
%package -n lib%name-devel-static
Summary: Cinnamon desktop develop libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release
License: %lgpl2plus

%description -n lib%name-devel-static
Cinnamon desktop static libraries for creating Cinnamon applications.
%endif

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library


%prep
%setup -q -n %name-%version
%patch0 -p1
[ ! -d m4 ] && mkdir m4

%build
%meson -Dpnp-ids-path=/usr/share/hwdata/pnp.ids -Ddeprecation-flags=false
%meson_build

%install
%meson_install

%find_lang --with-gnome --output=%name.lang %name fdl gpl lgpl

%files -n %name-schemas
%_datadir/glib-2.0/schemas/org.cinnamon.*.xml

%files -n %name-data
%_datadir/lib%name/*

%files -n lib%name -f %name.lang
%_libdir/*.so.*
%doc AUTHORS README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*
%endif


%changelog
* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Tue Nov 20 2018 Vladimir Didenko <cow@altlinux.org> 4.0.1-alt1
- 4.0.1

* Wed Oct 31 2018 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt1
- 4.0.0

* Mon May 7 2018 Vladimir Didenko <cow@altlinux.org> 3.8.1-alt1
- 3.8.1

* Sat Apr 28 2018 Vladimir Didenko <cow@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Nov 22 2017 Vladimir Didenko <cow@altlinux.org> 3.6.2-alt1
- 3.6.2

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.0-alt1
- 3.6.0

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 3.4.2-alt1
- 3.4.2

* Fri Jun 2 2017 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- 3.4.1

* Thu May 4 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 3.2.4-alt1
- 3.2.4

* Mon Dec 12 2016 Vladimir Didenko <cow@altlinux.org> 3.2.2-alt1
- 3.2.2

* Fri Dec 9 2016 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt1
- 3.2.1-4-g08ac1dd

* Fri Nov 18 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt3
- return call of pam_setcred() function

* Fri Nov 18 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt2
- return call of pam_acct_mgmt() but ignore its returned code

* Sun Nov 13 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri May 20 2016 Vladimir Didenko <cow@altlinux.org> 3.0.2-alt1
- 3.0.2

* Thu May 12 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Apr 25 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Mar 16 2016 Vladimir Didenko <cow@altlinux.org> 2.8.1-alt1
- 2.8.1

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue Jun 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.5-alt1
- 2.6.5

* Tue Jun 2 2015 Vladimir Didenko <cow@altlinux.org> 2.6.4-alt1
- 2.6.4

* Sat May 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.2-alt1
- 2.6.2

* Tue May 19 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri May 8 2015 Vladimir Didenko <cow@altlinux.org> 2.5.1-alt2
- git 20150506

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.1-alt1
- 2.5.1

* Tue Nov 25 2014 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt1
- 2.4.2

* Mon Nov 10 2014 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon Oct 20 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt2
- change default background path

* Tue Oct 14 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- git20141014

* Thu May 29 2014 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt2
- remove not needed more locale schema

* Wed May 21 2014 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- 2.2.3

* Mon May 12 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2

* Mon May 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Thu Apr 10 2014 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt4
- return org.cinnamon.system.locale schema

* Mon Apr 7 2014 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt3
- git20140324

* Tue Mar 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt2
- build with gnome-3.12

* Mon Nov 25 2013 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue Nov 5 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- 2.0.2

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt3
- rebuild for GNOME-3.10

* Mon Sep 16 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt2
- git20130905

* Tue Aug 27 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- Initial build
