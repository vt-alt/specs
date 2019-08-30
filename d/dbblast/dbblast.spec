Name: dbblast
Version: 0.1.8
Release: alt13

Summary: Dust bunny blaster
License: GPLv2+
Group: Graphics

URL: http://dbblast.sourceforge.net/
Source: http://download.sourceforge.net/dbblast/dbblast-qt4-v%{version}.tar.gz
Patch1: dbblast-0.1.7-build.patch
Patch2: dbblast-0.1.8-gcc43.patch
Patch3: dbblast-0.1.8-alt-exiv2-0.27.2.patch

# Automatically added by buildreq on Mon Jul 20 2009
BuildRequires: gcc-c++ libexiv2-devel libqt4-devel

%description
Dbblast (Dust bunny blaster) is a utility that automatically removes dust spots
or "bunnies" from .jpg images taken with digital SLR's. It can be run in batch
mode from either a GUI or from the command line.

%prep
%setup
find . -type f -print0  | xargs -r0 %__subst "s,\r,,"
%patch1 -p1
%patch2 -p1
%patch3 -b .exiv2

# fix path to exiv2
subst 's@/usr/local/@/usr/@' dbblast.pro

%build
export PATH=%_qt4dir/bin:$PATH
qmake dbblast.pro

%make_build CXX="g++ %optflags"

%install
install -pD -m755 dbblast %buildroot%_bindir/dbblast
install -d -m755 %buildroot/usr/share/dbblast
cp helpdocs/* %buildroot/usr/share/dbblast

%files
%_bindir/*
%_datadir/*

%changelog
* Sun Aug 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt13
- rebuilt against libexiv2.so.27

* Tue Jun 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt12
- rebuilt against libexiv2.so.26

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt11
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.8-alt10.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt10
- rebuilt against libexiv2.so.13

* Fri Jan 25 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt9
- rebuilt against libexiv2.so.12

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt8
- rebuilt against libexiv2.so.11

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 0.1.8-alt7
- Rebuild with libexiv2.so.9.

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 0.1.8-alt6
- Rebuild with libexiv2.so.6.

* Mon Jul 20 2009 Victor Forsyuk <force@altlinux.org> 0.1.8-alt5
- Rebuild with libexiv2.so.5.
- Switch from qt3-linked to qt4 dbblast flavor.

* Tue Nov 04 2008 Victor Forsyuk <force@altlinux.org> 0.1.8-alt4
- Fix FTBFS with gcc4.3.

* Mon Oct 06 2008 Victor Forsyuk <force@altlinux.org> 0.1.8-alt3
- Fix build requirements.

* Fri Jun 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.8-alt2.1
- Automated rebuild due to libexiv2.so.2 -> libexiv2.so.4 soname change.

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 0.1.8-alt2
- Rebuild with new libexiv2.

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.1.8-alt1
- 0.1.8

* Tue Oct 02 2007 Victor Forsyuk <force@altlinux.org> 0.1.7-alt1
- 0.1.7

* Wed May 23 2007 Victor Forsyuk <force@altlinux.org> 0.1.6-alt1
- 0.1.6

* Tue Mar 20 2007 Victor Forsyuk <force@altlinux.org> 0.1.5-alt1
- 0.1.5

* Tue Feb 13 2007 Victor Forsyuk <force@altlinux.org> 0.1.4-alt1
- Initial build.
