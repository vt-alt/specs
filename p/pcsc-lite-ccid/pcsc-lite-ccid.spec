Name: pcsc-lite-ccid
Version: 1.4.31
Release: alt1

Summary: USB CCID IFD Handler
Group: System/Libraries
License: LGPL
URL: https://pcsclite.apdu.fr/

Requires: pcsc-lite

Source: %name-%version.tar
Source1: PCSC.tar
Patch1: ccid-disable-examples-build.patch

BuildRequires: flex libpcsclite-devel libusb-devel

Provides: ccid = %version-%release
Obsoletes: ccid < %version-%release

%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
This package provides generic USB CCID (Chip/Smart Card Interface
Devices) driver for PC/SC Lite.

%prep
%setup
# Do not build examples requires contrib from external repository
%patch1 -p1
cp README.md README
# Copy pcsc-lite
tar xf %SOURCE1

%build
%autoreconf
%configure --enable-twinserial
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/lib/udev/rules.d/
cp -a src/92_pcscd_ccid.rules %buildroot/lib/udev/rules.d/

%files
%doc contrib/Kobil_mIDentity_switch/README_Kobil_mIDentity_switch.txt
%doc AUTHORS README.md NEWS SCARDGETATTRIB.txt SCARDCONTOL.txt
%config(noreplace) %_sysconfdir/reader.conf.d/libccidtwin
%ifddir/ifd-ccid.bundle
%_libdir/pcsc/drivers/serial/libccidtwin.so
/lib/udev/rules.d/92_pcscd_ccid.rules

%changelog
* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.31-alt1
- New version.

* Thu Feb 22 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.29-alt1
- New version.

* Sat Oct 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.4.28-alt1
- New version

* Sun May 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.4.27-alt1
- New version

* Thu May 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.26-alt2
- pcsc: fixed realloc usage.

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.4.26-alt1
- new version 1.4.26

* Thu Sep 15 2016 Andrey Cherepanov <cas@altlinux.org> 1.4.24-alt1
- New version 1.4.24
- Drop obsoleted patch
- Build from upstream Git repository

* Mon Sep 21 2015 Michael Shigorin <mike@altlinux.org> 1.4.20-alt1
- 1.4.20 (closes: #31292)

* Tue May 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt3
- Add JaCarta Flash support (ALT #27377)

* Wed Mar 21 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt2
- Add JaCarta support (Alladin)

* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt1
- [1.4.5]

* Sun Jun 27 2010 Alexey I. Froloff <raorn@altlinux.org> 1.3.13-alt1
- [1.3.13]

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.11-alt1
- Initial build

