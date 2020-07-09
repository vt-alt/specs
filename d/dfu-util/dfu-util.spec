Name: dfu-util
Version: 0.9
Release: alt2

Summary: USB Device Firmware Upgrade tool

License: GPLv2+
Group: Development/Tools
Url: http://dfu-util.sourceforge.net/

Source: http://dfu-util.sourceforge.net/releases/%name-%version.tar

BuildRequires: gcc
BuildRequires: libusb-devel

%description
USB Device Firmware Upgrade (DFU) is an official USB device class specification
of the USB Implementers Forum. It specifies a vendor and device independent way
of updating the firmware of a USB device. The idea is to have only one
vendor-independent firmware update tool as part of the operating system, which
can then (given a particular firmware image) be downloaded into the device.

In addition to firmware download, it also specifies firmware upload, i.e.
loading the currently installed device firmware to the USB Host.

The DFU specification can be found at:
 http://www.usb.org/developers/devclass_docs/usbdfu10.pdf

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc --no-dereference COPYING
%doc ChangeLog README DEVICES.txt TODO
%_bindir/dfu-prefix
%_bindir/dfu-suffix
%_bindir/dfu-util
%_man1dir/*

%changelog
* Tue Jun 30 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt2
- manual build

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_9
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_8
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_7
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_6
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_5
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_4
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_2
- update to new release by fcimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_1
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_3
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_2
- update to new release by fcimport

* Mon Jun 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_4
- update to new release by fcimport

* Fri Dec 14 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_3
- converted for ALT Linux by srpmconvert tools

