%define _unpackaged_files_terminate_build 1

Name: libfprint2
Version: 1.90.7
Release: alt1

Summary: Tool kit for fingerprint scanner
License: LGPLv2+
Group: System/Libraries

Url: http://www.freedesktop.org/wiki/Software/fprint/libfprint
# git://anongit.freedesktop.org/libfprint/libfprint
# https://gitlab.freedesktop.org/libfprint/libfprint
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: libusb-devel libnss-devel glib2-devel libImageMagick-devel libXv-devel libpixman-devel
BuildRequires: gcc-c++ doxygen 
BuildRequires: libgio-devel libgusb-devel libudev-devel gtk-doc libcairo-devel cmake
BuildRequires: /proc python3-module-pygobject3
BuildRequires: gobject-introspection-devel libgusb-gir-devel

%description
The fprint project aims to support for consumer fingerprint reader
devices.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for %name

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for %name

%prep
%setup
%patch -p1

%build
%meson -Ddrivers=all \
       -Dintrospection=true \
       -Dudev_rules=true \
       -Dudev_rules_dir=%_sysconfdir/udev/rules.d/ \
       -Dgtk-examples=false \
       -Ddoc=true
export LD_LIBRARY_PATH="libfprint"
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc COPYING INSTALL NEWS TODO THANKS AUTHORS README
%_libdir/*.so.*
%_sysconfdir/udev/rules.d/60-libfprint-2-autosuspend.rules

%files gir
%_libdir/girepository-1.0/*.typelib

%files devel
%doc HACKING.md
%doc %_datadir/gtk-doc/html/libfprint-2
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/libfprint-2.pc

%files gir-devel
%_datadir/gir-1.0/*.gir

%changelog
* Mon Apr 05 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.90.7-alt1
- Updated to upstream version 1.90.7.
- Enabled introspection since it's required for fprintd tests now.

* Wed Sep 30 2020 Anton Farygin <rider@altlinux.ru> 1.90.3-alt1
- 1.90.3

* Wed Aug 12 2020 Anton Farygin <rider@altlinux.ru> 1.90.2-alt1
- 1.90.2

* Tue Feb 04 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0-alt1
- new version
  + build system switched to meson by upstream
  + add meson, libgio-devel, libgusb-devel, libudev-devel, gtk-doc to BR:
  + remove fix for e2k

* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- fix build on e2k with lcc
- minor spec cleanup

* Fri Aug 18 2017 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1
- new version

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 0.4.0-alt3
- Rebuild with new libImageMagick

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 0.4.0-alt2
- Rebuild with new libImageMagick

* Thu Oct 25 2012 Ivan Ovcherenko <asdus@altlinux.org> 0.4.0-alt1
- 0.4.0 with git updates

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.2.0-alt3
- Rebuild with new libImageMagick

* Mon Sep 13 2010 Anton Farygin <rider@altlinux.ru> 0.2.0-alt2
- rebuild with new libImageMagick

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 0.2.0-alt1
- new version

* Sat Jun 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt0.pre2
- 0.1.0-pre2

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt0.pre1
- 0.1.0-pre1

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.6-alt2
- rebuild with libMagickCore.so.1

* Sat May 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.6-alt1
- initial release

