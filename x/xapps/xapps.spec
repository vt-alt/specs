%define translations_name xapp

Name: xapps
Version: 1.4.8
Release: alt1

Summary: Libraries and common resources for XApps
License: %gpl3only
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/xapps
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar

Requires: lib%name = %version-%release
BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.in
BuildPreReq: intltool >= 0.35
BuildPreReq: libgtk+3-devel >= 3.3.6
BuildPreReq: glib2-devel >= 2.35.0
BuildPreReq: libgio-devel >= 2.28.0
BuildPreReq: gtk-doc >= 1.4
BuildPreReq: gnome-common >= 2.8.0
BuildPreReq: gsettings-desktop-schemas-devel >= 3.5.91

BuildRequires: meson
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libgnomekbd-devel
BuildRequires: vala-tools
BuildRequires: rpm-build-python rpm-build-python3
BuildRequires: python-module-pygobject3-devel
BuildRequires: python3-module-pygobject3-devel

%description
Libraries and common resources for XApps

%package -n %name-schemas
Summary: A collection of GSettings schemas for XApps
Group: Graphical desktop/GNOME
BuildArch: noarch

%description -n %name-schemas
A collection of GSettings schemas for XApps

%package -n %name-utils
Summary: A collection of utils for XApps
Group: Graphical desktop/GNOME
BuildArch: noarch

%description -n %name-utils
A collection of utils for XApps

%package -n %name-icons
Summary: XApps icons
Group: Graphical desktop/GNOME
BuildArch: noarch

%description -n %name-icons
XApps icons.

%package -n lib%name
Summary: XApps core libraries
Group: Graphical desktop/GNOME

%description -n lib%name
XApps libraries.

%package -n lib%name-devel
Summary: XApps development libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
XApps development libraries and includes

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

%package -n python-module-%name-overrides
Summary: Python Xapp overrides Library
Group: Development/Python

%description -n python-module-%name-overrides
Python Xapp overrides Library

%package -n python3-module-%name-overrides
Summary: Python3 Xapp overrides Library
Group: Development/Python3

%description -n python3-module-%name-overrides
Python3 Xapp overrides Library

%prep
%setup -q -n %name-%version

%build
%meson -D deprecated_warnings=false
%meson_build

%install
%meson_install

%find_lang %translations_name

%files -n %name-schemas
%_datadir/glib-2.0/schemas/org.x.apps.*.xml

%files -n %name-icons
%_datadir/icons/hicolor/scalable/actions/*
%_datadir/icons/hicolor/scalable/categories/*

%files -n %name-utils
%_bindir/xfce4-set-wallpaper
# TODO: this scripts don't work without modifications in Alt Linux. Need to fix.
%exclude %_bindir/pastebin
%exclude %_bindir/upload-system-info


%files -n lib%name -f %translations_name.lang
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_vapidir/xapp.vapi
%_vapidir/xapp.deps
%_datadir/glade/catalogs/xapp-glade-catalog.xml

%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*

%files -n python-module-%name-overrides
%python_sitelibdir/gi/overrides/XApp.py*

%files -n python3-module-%name-overrides
%python3_sitelibdir/gi/overrides/XApp.py
%python3_sitelibdir/gi/overrides/__pycache__/*

%changelog
* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 1.4.8-alt1
- 1.4.8

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 1.4.7-alt1
- 1.4.7

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 1.4.5-alt1
- 1.4.5

* Tue Dec 4 2018 Vladimir Didenko <cow@altlinux.org> 1.4.4-alt1
- 1.4.4

* Tue Nov 20 2018 Vladimir Didenko <cow@altlinux.org> 1.4.2-alt1
- 1.4.2

* Wed Oct 31 2018 Vladimir Didenko <cow@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Sep 14 2018 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Sep 6 2018 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1.1
- Rebuild with pygobject 3.30

* Sat Apr 28 2018 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- 1.2.0-1-g6b33ff3

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 1.0.4-alt1
- 1.0.4

* Thu May 18 2017 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- 1.0.3

* Wed Nov 23 2016 Vladimir Didenko <cow@altlinux.org> 1.0.2-alt1
- 1.0.2-3-g4b700fe

* Tue Sep 27 2016 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
