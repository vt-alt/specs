%define nm_version 1.4.1-alt1.git20160914
%define _unpackaged_files_terminate_build 1

%def_with gcr

Name: libnma
Version: 1.8.30
Release: alt1
License: GPLv2+ and LGPLv2.1+
Group: Graphical desktop/GNOME
Summary: NetworkManager GUI library
Url: https://gitlab.gnome.org/GNOME/libnma
Vcs: https://gitlab.gnome.org/GNOME/libnma.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson

BuildRequires: libgtk+3-devel libtool
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnm-gir-devel >= %nm_version
BuildRequires: iso-codes-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: mobile-broadband-provider-info
BuildRequires: gtk-doc
%{?_with_gcr:BuildRequires: gcr-libs-devel}

%description
This package contains the library used for integrating GUI tools with
NetworkManager.

%package devel
Group: Development/GNOME and GTK+
Summary: Devel files for NetworkManager GUI library
Requires: %name = %version-%release
Requires: libnm-devel >= %nm_version
Requires: libgtk+3-devel

%description devel
This package contains header and pkg-config files to be used for integrating
GUI tools with NetworkManager.

%package gir
Group: System/Libraries
Summary: GObject introspection data for the libnma
Requires: %name = %version-%release

%description gir
GObject introspection data for the libnma.

%package gir-devel
Group: System/Libraries
Summary: GObject introspection devel data for the libnma
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the libnma.

%package devel-doc
Summary: Development documentation for libnma-devel-doc
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
This package contains development documentation for libnma-devel-doc.

%prep
%setup
%patch -p1

%build
%meson \
	--libexecdir==%_libexecdir/NetworkManager \
	--localstatedir=%_var \
%if_with gcr
	-Dgcr=true \
%else
	-Dgcr=false \
%endif
	-Dintrospection=true \
	-Dvapi=false \
	-Dlibnma_gtk4=false \
	-Dmobile_broadband_provider_info=true \
	-Diso_codes=true \
	-Dgtk_doc=true

%meson_build -v

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc NEWS CONTRIBUTING
%_datadir/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
%_libdir/libnma.so.*

%files devel
%_includedir/libnma/
%_libdir/libnma.so
%_pkgconfigdir/libnma.pc

%files gir
%_libdir/girepository-1.0/NMA-1.0.typelib

%files gir-devel
%_datadir/gir-1.0/NMA-1.0.gir

%files devel-doc
%doc %_datadir/gtk-doc/html/libnma

%changelog
* Fri Jul 03 2020 Mikhail Efremov <sem@altlinux.org> 1.8.30-alt1
- Updated to 1.8.30.

* Thu Mar 26 2020 Mikhail Efremov <sem@altlinux.org> 1.8.28-alt1
- Splitted out from nm-applet.

