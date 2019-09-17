%define _name girara
%define _soname 3
%define _unpackaged_files_terminate_build 1

Name: lib%_name
Version: 0.3.3
Release: alt1

Summary: GTK-based minimalistic user interface library
License: %bsdstyle
Group: System/Libraries
URL: https://pwmt.org/projects/girara
# https://git.pwmt.org/pwmt/girara.git
Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses meson

BuildRequires: libgtk+3-devel >= 3.4 libnotify-devel libpango-devel
BuildRequires: intltool

%description
girara is a library that implements a user interface that focuses on
simplicity and minimalism.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libgtk+3-devel

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
%meson \
	-Denable-notify=true \
	-Denable-json=false

%meson_build -v

%install
%meson_install
%find_lang %name-gtk3-%_soname

%files -f %name-gtk3-%_soname.lang
%doc AUTHORS README LICENSE
%_libdir/*.so.%_soname
%_libdir/*.so.%_soname.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Mon Sep 16 2019 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Mon Dec 24 2018 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Fri Sep 21 2018 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Fri May 25 2018 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Wed Apr 18 2018 Mikhail Efremov <sem@altlinux.org> 0.2.9-alt1
- Updated to 0.2.9.

* Mon Jan 15 2018 Mikhail Efremov <sem@altlinux.org> 0.2.8-alt1
- Updated to 0.2.8.

* Tue Jan 24 2017 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1
- Updated to 0.2.7.

* Wed Apr 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt1
- Updated to 0.2.6.

* Mon Dec 21 2015 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Fri Apr 17 2015 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Fri Oct 17 2014 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Updated to 0.2.3.

* Thu Jul 03 2014 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Enable libnotify support.
- Updated to 0.2.2.

* Fri Feb 21 2014 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Build with GTK+3.
- Updated to 0.2.0.

* Tue Nov 19 2013 Mikhail Efremov <sem@altlinux.org> 0.1.9-alt1
- Updated to 0.1.9.

* Thu Nov 14 2013 Mikhail Efremov <sem@altlinux.org> 0.1.8-alt1
- Updated to 0.1.8.

* Fri Aug 16 2013 Mikhail Efremov <sem@altlinux.org> 0.1.7-alt1
- Updated to 0.1.7.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1
- Package LICENSE.
- Updated to 0.1.6.

* Tue Feb 12 2013 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- Updated to 0.1.5.

* Wed Jan 09 2013 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1
- Updated to 0.1.4.

* Wed Jun 13 2012 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- Updated to 0.1.3.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.

* Thu Mar 15 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Initial build.

