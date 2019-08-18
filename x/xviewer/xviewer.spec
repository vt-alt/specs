%define _libexecdir %_prefix/libexec
%define api_ver 3.0
%def_enable color_management
%def_enable introspection

Name: xviewer
Version: 2.2.1
Release: alt1

Summary: Fast and functional image viewer.
License: %gpl2plus
Group: Graphics
Url: https://github.com/linuxmint/xviewer

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-gnome rpm-build-licenses

# From configure.in
BuildRequires: gnome-common intltool yelp-tools
BuildRequires: gtk-doc
BuildPreReq: libgtk+3-devel >= 3.14.0
BuildPreReq: libgio-devel >= 2.38.0
BuildPreReq: libcinnamon-desktop-devel >= 3.8.0
BuildPreReq: gnome-icon-theme >= 2.19.1
BuildPreReq: shared-mime-info >= 0.60
BuildPreReq: libexempi-devel >= 1.99.5
BuildPreReq: libexif-devel >= 0.6.14
%{?_enable_color_management:BuildPreReq: liblcms2-devel}
BuildPreReq: libjpeg-devel librsvg-devel
BuildPreReq: libpeas-devel >= 0.7.4
BuildRequires: libXt-devel libxml2-devel perl-XML-Parser zlib-devel gsettings-desktop-schemas-devel
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.10.2 libgtk+3-gir-devel}

%description
This is Xviewer, a fast and functional image viewer.

%package devel
Summary: Development files for Xviewer viewer
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains files necessary to develop plugins for Xviewer.

%package gir
Summary: GObject introspection data for the Xviewer
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Xviewer

%package gir-devel
Summary: GObject introspection devel data for the Xviewer
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Xviewer

%package tests
Summary: Tests for the Xviewer
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the Xviewer GUI.


%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure \
    --with-libexif \
    %{?_enable_color_management:--with-cms} \
    --with-xmp \
    --with-libjpeg \
    --disable-schemas-compile


%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_datadir/%name/
%dir %_libdir/%name
%_libdir/%name/lib%name.so
%_iconsdir/hicolor/*/apps/%{name}*.*
%config %_datadir/glib-2.0/schemas/org.x.viewer.enums.xml
%config %_datadir/glib-2.0/schemas/org.x.viewer.gschema.xml
%_datadir/GConf/gsettings/xviewer.convert
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS HACKING MAINTAINERS NEWS
%doc README THANKS TODO

%files devel
%dir %_includedir/%name-%api_ver/%name
%_includedir/%name-%api_ver/%name/*.h
%_pkgconfigdir/%name.pc

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*.typelib

%files gir-devel
%_datadir/gir-1.0/*.gir
%endif

%exclude %_libdir/%name/lib%name.la

%changelog
* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- New version

* Wed Jun 26 2019 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- New version

* Wed Dec 26 2018 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- New version

* Wed Dec 5 2018 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- New version

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- New version

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- New version

* Tue May 8 2018 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- New version

* Mon Mar 5 2018 Vladimir Didenko <cow@altlinux.org> 1.6.1-alt2
- Fix build with new libgnome-desktop3

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.6.1-alt1
- New version

* Tue Jul 4 2017 Vladimir Didenko <cow@altlinux.org> 1.4.3-alt1
- New version

* Wed Jun 7 2017 Vladimir Didenko <cow@altlinux.org> 1.4.2-alt1
- New version

* Fri May 19 2017 Vladimir Didenko <cow@altlinux.org> 1.4.1-alt1
- New version

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- New version

* Sun Nov 13 2016 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- New version

* Thu Jun 23 2016 Vladimir Didenko <cow@altlinux.org> 1.0.4-alt1
- New version

* Thu May 26 2016 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- New version

* Mon Feb 29 2016 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
