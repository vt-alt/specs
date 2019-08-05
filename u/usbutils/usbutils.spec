Name: usbutils
Version: 012
Release: alt1

Summary: Linux USB utilities
License: GPLv2+
Group: System/Kernel and hardware

Url: http://sourceforge.net/projects/linux-usb/
# git://github.com/gregkh/usbutils.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: pkgconfig(libusb-1.0) >= 1.0.14
BuildRequires: pkgconfig(libudev) >= 196

%description
usbutils contains an utility (lsusb) for inspecting devices connected to
the USB bus.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --datadir=%_datadir/misc
%make_build

%install
%makeinstall
rm -f %buildroot%_bindir/lsusb.py

%files
%_bindir/*
%_man1dir/*
%_man8dir/*
%doc NEWS README.md

%changelog
* Thu Aug 01 2019 Alexey Shabalin <shaba@altlinux.org> 012-alt1
- new version 012

* Tue Oct 16 2018 Alexey Shabalin <shaba@altlinux.org> 010-alt1
- new version 010

* Tue Jan 09 2018 Alexey Shabalin <shaba@altlinux.ru> 009-alt1
- 009

* Thu Aug 13 2015 Alexey Shabalin <shaba@altlinux.ru> 008-alt1
- 008

* Wed Jul 31 2013 Alexey Shabalin <shaba@altlinux.ru> 007-alt1
- 007

* Mon May 13 2013 Alexey Shabalin <shaba@altlinux.ru> 006-alt1
- 006

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.90-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Sep 07 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.90-alt2
- use usbids instead of hwdatabase

* Fri Aug 13 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.90-alt1
- 0.90

* Mon Apr 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.87-alt1
- 0.87

* Thu Aug 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.86-alt1
- 0.86

* Thu Jun 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.84-alt1
- 0.84

* Fri May 08 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.82-alt1
- 0.82

* Tue Apr 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.81-alt1
- 0.81
- drop usbtree

* Mon Apr 06 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.73-alt2
- fix buildreqs
- fix the parsing of bus number >= 08 in tree mode (Debian)

* Wed Oct 24 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.73-alt1
- 0.73

* Mon Oct 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.72-alt1
- NMU:
  + 0.72
  + add Url

* Tue Feb 01 2005 Anton Farygin <rider@altlinux.ru> 0.70-alt1
- new version

* Thu Dec 23 2004 Anton Farygin <rider@altlinux.ru> 0.11-alt5
- usb.ids moved to hwdatabase
- added patches from fedora:
    * usbutils-0214.patch - fix various brokenness
    * usbutils-0.11-hidcc.patch - patch from Aurelien Jarno for unknown 
      HID Country Code entries in usb.ids

* Thu Sep 09 2004 Alexey Gladkov <legion@altlinux.ru> 0.11-alt3
- update usb.ids;
- usbtree script added;
- the latest usb.ids contain entries that usbutils doesn't handle (HCC lines);

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.11-alt1
- 0.11
- Updated usb.ids file
- Rebuilt in new environment

* Thu Dec 06 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9-alt1
- 0.9
- Updated usb.ids file

