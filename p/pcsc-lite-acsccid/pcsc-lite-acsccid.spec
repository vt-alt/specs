Name: pcsc-lite-acsccid
Version: 1.1.8
Release: alt1

Summary: PCSC Driver for ACS CCID Based Smart Card Readers
License: LGPLv2.1+
Group: System/Servers

Url: http://acsccid.sourceforge.net/
Source: %name-%version.tar
Patch: %name-1.1.0-alt-ACR38U-CCID-rule.patch

BuildRequires: libusb-devel libpcsclite-devel flex

Provides: pcsc-acsccid = %version-%release
Obsoletes: pcsc-acsccid < %version-%release

%description
This package contains a ACS USB CCID (Chip/Smart Card Interface
Devices) driver.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --enable-composite-as-multislot --enable-twinserial
%make

%install
%makeinstall_std
mkdir -p %buildroot/lib/udev
mkdir %buildroot/lib/udev/rules.d
sed 's:GROUP="pcscd":GROUP="scard":' <src/92_pcscd_acsccid.rules >%buildroot/lib/udev/rules.d/92_pcscd_acsccid.rules

%files
%doc AUTHORS COPYING README
/lib/udev/rules.d/*.rules
%_libdir/pcsc/drivers/*

%changelog
* Fri Jan 10 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.8-alt1
- New version.

* Sat Jul 27 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt1
- New version.

* Wed Oct 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.6-alt1
- New version.

* Wed Oct 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- new version 1.1.4

* Thu Sep 15 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- New version 1.1.3

* Wed Sep 23 2015 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- 1.1.0
- updated patch (is it still needed?)

* Mon Dec 17 2012 Ivan Ovcherenko <asdus@altlinux.org> 1.0.4-alt1
- Updated to 1.0.4

* Tue Sep 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.3-alt2
- added 072f:90cc USB ID

* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Nov 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt0.20110919
- 1.0.3-20110919

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1
- initial
