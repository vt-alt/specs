Name: flashrom
Version: 1.2
Release: alt1

Summary: Universal flash programming utility
License: %gpl2plus
Group: System/Kernel and hardware

Url: http://flashrom.org/Flashrom
# Homepage: http://www.flashrom.org
# https://review.coreboot.org/flashrom.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: libftdi1-devel libpci-devel zlib-devel libusb-compat-devel

%description
flashrom is a tool for identifying, reading, writing,
verifying and erasing flash chips. It's often used to flash
BIOS/EFI/coreboot/firmware/optionROM images in-system using a
supported mainboard, but it also supports flashing of network
cards (NICs), SATA controller cards, and other external devices
which can program flash chips.

It supports a wide range of DIP32, PLCC32, DIP8, SO8/SOIC8,
TSOP32/40/48, and BGA chips, which use various protocols such as
LPC, FWH, parallel flash, or SPI.

The tool can be used to flash BIOS/firmware images for example --
be it proprietary BIOS images or coreboot (previously known as
LinuxBIOS) images.

It can also be used to read the current existing BIOS/firmware
from a flash chip.

%prep
%setup

%build
%define _optlevel s
%add_optflags -Werror -Wno-error=deprecated-declarations
%make_build CFLAGS="%optflags" PREFIX=%_prefix 

%install
install -dm755 %buildroot%_sbindir
%make_install PREFIX=%buildroot%_prefix install

%files
%doc README
%_sbindir/*
%_man8dir/*

%changelog
* Tue Jun 16 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.2-alt1
- The first and hopefully not the last release of 2020
- Support MT25QU256 for Baikal-M firmware

* Tue Jul 30 2019 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- 1.0 -> 1.1

* Fri May 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Updated to upstream version 1.0.

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.9-alt2
- Updated build dependencies.

* Thu Mar 17 2016 Michael Shigorin <mike@altlinux.org> 0.9.9-alt1
- new version (watch file uupdate)

* Mon Mar 02 2015 Michael Shigorin <mike@altlinux.org> 0.9.8-alt1
- new version (watch file uupdate)

* Sat Aug 17 2013 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- new version (watch file uupdate)
- added FTDI support

* Thu Aug 23 2012 Michael Shigorin <mike@altlinux.org> 0.9.6.1-alt1
- new version (watch file uupdate)

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 0.9.5.2-alt1
- 0.9.5.2

* Fri Mar 02 2012 Michael Shigorin <mike@altlinux.org> 0.9.5.1-alt1
- 0.9.5.1

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1
- new version (uupdate from watch file)

* Sat Jan 24 2009 Led <led@altlinux.ru> 0.0-alt0.1
- initial build
