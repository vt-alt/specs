%define api_ver 1.0

%def_enable tests
%def_enable docs
%def_enable introspection
%def_enable vala
# failed to init libusb in hasher
%def_disable check

Name: libgusb
Version: 0.3.4
Release: alt1

Summary: GLib wrapper around libusb1
Group: System/Libraries
License: LGPL-2.1
Url: https://gitorious.org/gusb/

# VCS: https://github.com/hughsie/libgusb.git
Source: http://people.freedesktop.org/~hughsient/releases/%name-%version.tar.xz

BuildRequires(pre): meson
BuildRequires: libgio-devel >= 2.44 libusb-devel >= 1.0.22
BuildRequires: gobject-introspection-devel
%{?_enable_docs:BuildRequires: gtk-doc}
%{?_enable_vala:BuildRequires: vala-tools}

%description
GUsb is a GObject wrapper for libusb that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package devel
Summary: Libraries and headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
GLib headers and libraries for the GUsb library.

%package gir
Summary: GObject introspection data for GUsb
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GUsb library.

%package gir-devel
Summary: GObject introspection devel data for GUsb
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GUsb library.

%package devel-doc
Summary: Development documentation for GUsb
Group: Development/C
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package provides documentation for developing
applications that use GUsb library.


%prep
%setup

%build
%meson \
	-Dusb_ids=%_datadir/misc/usb.ids \
        %{?_disable_docs:-Ddocs=false} \
        %{?_disable_tests:-Dtests=false} \
	%{?_disable_introspection:-Dintrospection=false} \
        %{?_disable_vala:-Dvapi=false}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/%name.so.*
%doc README* AUTHORS NEWS

%files devel
%_bindir/gusbcmd
%_includedir/gusb-1/
%_libdir/%name.so
%_pkgconfigdir/gusb.pc
%{?_enable_vala:%_vapidir/gusb.*}

%if_enabled introspection
%files gir
%_typelibdir/GUsb-%api_ver.typelib

%files gir-devel
%_girdir/GUsb-%api_ver.gir
%endif

%if_enabled docs
%files devel-doc
%_datadir/gtk-doc/html/gusb/
%endif

%changelog
* Sun Mar 15 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Sat Feb 01 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Tue Jan 07 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1
- updated License tag

* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.11-alt1
- 0.2.11

* Mon Apr 17 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt1
- 0.2.10

* Sat Mar 26 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.9-alt1
- 0.2.9

* Sat Dec 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.8-alt1
- 0.2.8

* Sun Sep 20 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- 0.2.7

* Thu Jul 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6

* Mon Jun 01 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Mon Jan 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Thu Dec 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Thu Nov 27 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Sun Nov 23 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Sat Mar 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Sat Feb 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Sun Jan 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4
- new -gir{,-devel} subpackages
- added Vala bindings to -devel subpackage

* Thu Jan 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- adapted for Sisyphus

* Mon Dec 05 2011 Richard Hughes <richard@hughsie.com> 0.1.3-1
- New upstream version
- Add a missing error enum value

* Fri Nov 11 2011 Richard Hughes <richard@hughsie.com> 0.1.2-1
- New upstream version
- Ignore EBUSY when trying to detach a detached kernel driver

* Tue Nov 01 2011 Richard Hughes <richard@hughsie.com> 0.1.1-1
- New upstream version

* Thu Sep 15 2011 Richard Hughes <richard@hughsie.com> 0.1.0-1
- Initial version for Fedora package review
