%define ver_major 1
%def_disable static

Name: libwacom
Version: %ver_major.1
Release: alt1

Summary: A Wacom tablets library
Group: System/Libraries
License: BSD-like
Url: https://github.com/linuxwacom/libwacom

Source: %url/releases/download/%name-%version/%name-%version.tar.bz2

Requires: %name-data = %version-%release

BuildRequires: glib2-devel libgudev-devel libxml2-devel doxygen
# for check
BuildRequires: /proc

%description
%name is a library to identify Wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package data
Summary: Tablets data for %name
Group: System/Libraries
BuildArch: noarch

%description data
%name is a library to identify wacom tablets and their model-specific
features.

This package contains tablets/stylus data for %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-doc
The %name-devel-doc package contains documentation for
developing applications that use %name.

%prep
%setup

%build
%autoreconf
%configure \
    %{subst_enable static} \
    --with-udev-dir=/lib/udev

%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/%name-list-local-devices
%_libdir/*.so.*
%_udevrulesdir/65-libwacom.rules
%_man1dir/libwacom-list-local-devices.1*
%doc NEWS README* COPYING

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files data
%dir %_datadir/%name
%_datadir/%name/*.tablet
%_datadir/%name/*.stylus
%_datadir/%name/layouts/

#%files devel-doc
#%_datadir/gtk-doc/html/*

%changelog
* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Tue Aug 27 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.33-alt1
- 0.33

* Mon Nov 05 2018 Yuri N. Sedunov <aris@altlinux.org> 0.32-alt1
- 0.32

* Sat Aug 11 2018 Yuri N. Sedunov <aris@altlinux.org> 0.31-alt1
- 0.31

* Tue May 22 2018 Yuri N. Sedunov <aris@altlinux.org> 0.30-alt1
- 0.30 (new %%url)

* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.29-alt1
- 0.29

* Sat Feb 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28-alt1
- 0.28

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.27-alt1
- 0.27

* Sun Aug 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt1
- 0.26

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25-alt1
- 0.25

* Sun Feb 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.24-alt1
- 0.24

* Sun Jan 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt1
- 0.23

* Sun Jul 24 2016 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22

* Sun Jun 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.21-alt1
- 0.21

* Fri Jun 10 2016 Yuri N. Sedunov <aris@altlinux.org> 0.20-alt1
- 0.20

* Thu Apr 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.19-alt1
- 0.19

* Wed Feb 03 2016 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt1
- 0.18

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt1
- 0.17

* Sun Nov 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.16-alt1
- 0.16

* Sat Jul 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt1
- 0.15

* Sun Apr 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13

* Fri Mar 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- 0.11

* Sat Aug 23 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Mon May 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Wed Jan 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- 0.8

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Wed Feb 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- 0.7

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Mon Jun 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4

* Tue Feb 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- 0.3

* Tue Jan 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2

* Fri Jan 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

