%define _name gimplensfun
%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-lensfun
Version: 0.2.5
Release: alt0.2

Summary: lens distortion correction plugin for Gimp
License: GPLv3
Group: Graphics

Url: http://seebk.github.io/GIMP-Lensfun/
Source: %url%_name-%version.tar
Patch: %_name-0.2.3-alt-makefile.patch

Requires: gimp >= 2.6
BuildRequires: gcc-c++ libexiv2-devel libgimp-devel libgomp-devel liblensfun-devel

%description
GimpLensfun is a Gimp plugin to correct lens distortion using the
lensfun library and database.

%prep
%setup -n %_name-%version
rm -rf bin
%patch -p1 -b .makefile

%build
%make

%install
install -pD gimp-lensfun %buildroot%gimpplugindir/plug-ins/gimp-lensfun

#export DESTDIR=%buildroot
#gimptool-2.0 --install-admin-bin %_name

%files
%gimpplugindir/plug-ins/gimp-lensfun
%doc README.txt CHANGES.txt

%changelog
* Sun Aug 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt0.2
- updated to 0.2.4-9-gc5eaf97
- built against libexiv2.so.27

* Tue Jun 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt0.1
- updated to 0.2.4-3-g1d43d6b
- built against libexiv2.so.26

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt0.3
- rebuilt against liblensfun.so.1

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt0.2
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.4-alt0.1.1
- Rebuilt for gcc5 C++11 ABI.

* Sat Dec 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt0.1
- updated to 0.2.4-dev (b09f17a2), fixed for liblensfun-0.3.0

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt2
- rebuilt against libexiv2.so.13

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Thu Jan 24 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt2
- rebuilt against libexiv2.so.12

* Thu Jul 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Wed May 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt2
- fixed install for gimp-2.8

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt2
- rebuilt against libexiv2.so.11

* Fri Sep 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2

* Mon Jan 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

