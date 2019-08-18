%define _libexecdir %_prefix/libexec
%define so_ver 3
%define gir_version 1.5

%def_enable xps
%def_enable introspection

Name: xreader
Version: 2.2.3
Release: alt1

Summary: A document viewer
Group: Office
License: %gpl2only
Url: https://github.com/linuxmint/xreader

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
Requires: lib%name = %version-%release
Requires: gnome-icon-theme gnome-icon-theme-symbolic icon-theme-adwaita
Requires: gvfs-backend-recent-files
Requires: dconf

%define poppler_ver 0.24.0
%define gtk_ver 3.14.0

BuildPreReq: libpoppler-glib-devel >= %poppler_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: meson
BuildRequires: glib2-devel
BuildRequires: gcc-c++ gnome-common
BuildRequires: intltool yelp-tools itstool
BuildRequires: icon-theme-adwaita libdjvu-devel libgnome-keyring-devel libspectre-devel libtiff-devel
BuildRequires: libxml2-devel libkpathsea-devel libgail3-devel gsettings-desktop-schemas-devel zlib-devel libsecret-devel
%{?_enable_xps:BuildRequires: libgxps-devel}
BuildRequires: libSM-devel libICE-devel libXi-devel
BuildRequires: libxapps-devel
BuildRequires: libwebkit2gtk-devel
BuildRequires: mathjax

%if_enabled introspection
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
%endif

%description
Xreader is a document viewer capable of displaying multiple and single page
document formats like PDF and Postscript

%package -n lib%name
Summary: Library for the %name project
Group: Office

%description -n lib%name
Library for %name project

%package -n lib%name-gir
Summary: GObject introspection data for the Xreader library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Xreader library

%package -n lib%name-devel
Summary: Development tools for the %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files for %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Xreader library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Xreader library

%prep
%setup
%patch0 -p1

[ ! -d m4 ] && mkdir m4

%build
%meson \
  -Ddeprecated_warnings=false \
  -Ddjvu=true \
  -Ddvi=true \
  -Dt1lib=true \
  -Dpixbuf=true \
  -Dcomics=true \
  -Dintrospection=true
%meson_build

%install
%meson_install

subst '/NoDisplay/d' %buildroot%_desktopdir/%name.desktop

%find_lang %name --with-gnome

%files -f %name.lang
%doc AUTHORS NEWS README
%_bindir/xreader*
%dir %_libdir/xreader
%dir %_libdir/xreader/%so_ver
%dir %_libdir/xreader/%so_ver/backends
%_libdir/xreader/%so_ver/backends/*.so
%_libdir/xreader/%so_ver/backends/*.xreader-backend
%_datadir/glib-2.0/schemas/org.x.reader.gschema.xml
%_libexecdir/xreader*
%_desktopdir/%name.desktop
%_datadir/appdata/%name.appdata.xml

%_datadir/dbus-1/services/org.x.reader.Daemon.service
%_datadir/%name/
%_datadir/thumbnailers/xreader.thumbnailer
%_iconsdir/hicolor/*/apps/*
%_man1dir/*.1*

%files -n lib%name
%_libdir/libxreaderdocument.so.%{so_ver}*
%_libdir/libxreaderview.so.%{so_ver}*

%files -n lib%name-devel
%_includedir/xreader
%_libdir/libxreaderdocument.so
%_libdir/libxreaderview.so
%_pkgconfigdir/*.pc

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/XreaderDocument-%gir_version.typelib
%_libdir/girepository-1.0/XreaderView-%gir_version.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/XreaderDocument-%gir_version.gir
%_datadir/gir-1.0/XreaderView-%gir_version.gir
%endif

%changelog
* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- New version

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- New version
- Remove workaround for broken parallel build (fixed by upstream)

* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt2
- Don't use parallel build (it is broken with -j64)

* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- New version

* Wed Dec 26 2018 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- New version

* Wed Dec 5 2018 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- New version

* Wed Nov 21 2018 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- New version

* Fri Sep 14 2018 Vladimir Didenko <cow@altlinux.org> 1.8.5-alt1
- New version

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 1.8.4-alt1
- New version

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt1
- New version

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- New version

* Sat Feb 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1.1
- NMU: rebuild with texlive 2016

* Wed Dec 27 2017 Vladimir Didenko <cow@altlinux.org> 1.6.2-alt1
- New version

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.6.1-alt1
- New version

* Tue Jul 4 2017 Vladimir Didenko <cow@altlinux.org> 1.4.4-alt1
- New version

* Wed Jun 7 2017 Vladimir Didenko <cow@altlinux.org> 1.4.2-alt1
- New version

* Fri May 19 2017 Vladimir Didenko <cow@altlinux.org> 1.4.1-alt1
- New version

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- New version

* Sun Nov 13 2016 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- New version

* Thu Jun 23 2016 Vladimir Didenko <cow@altlinux.org> 1.0.7-alt1
- New version

* Thu May 26 2016 Vladimir Didenko <cow@altlinux.org> 1.0.6-alt1
- New version

* Fri Feb 26 2016 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
