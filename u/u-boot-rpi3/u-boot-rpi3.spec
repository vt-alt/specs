Name: u-boot-rpi3
Version: 2020.04
Release: alt1

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware

ExclusiveArch: armh aarch64

Source: %name-%version-%release.tar

BuildRequires: bc dtc >= 1.4 flex

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports Raspberry Pi 3/4 boards.

%ifarch armh
%define rpi rpi_3_32b rpi_3_b_plus_32b rpi_4_32b
%define img kernel7.img
%endif
%ifarch aarch64
%define rpi rpi_3 rpi_3_b_plus rpi_4
%define img kernel8.img
%endif

%prep
%setup

%build
for board in %rpi; do
	mkdir build
        %make_build O=build ${board}_defconfig all
        install -pm0644 -D build/u-boot.bin out/${board}/%img
        rm -rf build
done

%install
mkdir -p %buildroot%_datadir/u-boot
cd out
find . -type f | cpio -pmd %buildroot%_datadir/u-boot

%files
%doc README
%_datadir/u-boot/*

%changelog
* Tue Apr 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.04-alt1
- 2020.04 released

* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.01-alt1
- 2020.01 released

* Wed Oct 09 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.10-alt2
- added 32-bit 3b+ variant just for completeness

* Tue Oct 08 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.10-alt1
- 2019.10 released

* Tue Jul 16 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.07-alt1
- 2019.07 released

* Tue Apr 16 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Tue Jan 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Mon Dec 03 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- 2018.11 released

* Tue Sep 04 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.07-alt1
- 2018.07 released

* Fri Jun 22 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.05-alt2
- use flat directory layout for dtbs

* Thu Jun 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.05-alt1
- 2018.05 released

* Mon Jan 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.01-alt1
- 2018.01 released

* Tue Feb 07 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.01-alt1
- initial
