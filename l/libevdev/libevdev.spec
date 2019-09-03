%define api_ver 1.0
%def_disable doc
%def_enable check

Name: libevdev
Version: 1.8.0
Release: alt1

Summary: kernel evdev device wrapper library
Group: System/Libraries
License: MIT
Url: http://www.freedesktop.org/wiki/Software/libevdev

Source: http://www.freedesktop.org/software/%name/%name-%version.tar.xz

BuildRequires: glibc-kernheaders libcheck-devel python-modules python-module-setuptools
%{?_enabled_doc:BuildRequires: doxygen}

%description
%name is a wrapper library for evdev devices.

%package devel
Summary: kernel evdev device wrapper library development package
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	--disable-gcov

%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/mouse-dpi-tool
%_bindir/touchpad-edge-detector
%_bindir/libevdev-tweak-device
%_libdir/libevdev.so.*
%doc COPYING

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_man3dir/%name.3.*

%changelog
* Mon Aug 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Wed Jun 05 2019 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Fri Oct 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Thu Mar 08 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.9-alt1
- 1.5.9

* Mon Jan 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.8-alt1
- 1.5.8

* Thu May 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.7-alt1
- 1.5.7

* Fri Jan 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.6-alt1
- 1.5.6

* Sun Dec 04 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5

* Fri Aug 26 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Mon Aug 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Thu Jun 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Mon May 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Fri Jan 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.6-alt1
- 1.4.6

* Wed Nov 11 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Tue Sep 01 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Sat Apr 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Wed Apr 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Mar 05 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Sun Dec 07 2014 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Sun Nov 16 2014 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Wed Sep 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Mon Aug 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.99.902-alt1
- 1.2.99.902

* Thu Jun 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Wed Apr 30 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Tue Feb 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Fri Sep 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1.1
- disable coverage testing

* Fri Sep 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- first build for Sisyphus


