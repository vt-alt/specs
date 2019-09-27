%set_verify_elf_method no

Summary: bootloader and GPU firmware for Raspberry Pi
Name: raspberrypi-firmware
Version: 20190926
Release: alt1
Url: https://github.com/raspberrypi/firmware
License: distributable
Group: System/Kernel and hardware

ExclusiveArch: %arm aarch64

Source0: bootcode.bin
Source1: fixup.dat
Source2: fixup_cd.dat
Source3: fixup_db.dat
Source4: fixup_x.dat
Source5: start.elf
Source6: start_cd.elf
Source7: start_db.elf
Source8: start_x.elf
Source9: LICENCE.broadcom
Source10: fixup4.dat
Source11: fixup4cd.dat
Source12: fixup4db.dat
Source13: fixup4x.dat
Source14: start4.elf
Source15: start4cd.elf
Source16: start4db.elf
Source17: start4x.elf

Requires: u-boot-rpi3

%description
%summary

%install
%ifarch %arm
%define target %_datadir/u-boot/rpi_3_32b
%endif

%ifarch aarch64
%define target %_datadir/u-boot/rpi_3
%endif

%__install -d %buildroot/%target
%__install -m644 %SOURCE0 %buildroot/%target
%__install -m644 %SOURCE1 %buildroot/%target
%__install -m644 %SOURCE2 %buildroot/%target
%__install -m644 %SOURCE3 %buildroot/%target
%__install -m644 %SOURCE4 %buildroot/%target
%__install -m644 %SOURCE5 %buildroot/%target
%__install -m644 %SOURCE6 %buildroot/%target
%__install -m644 %SOURCE7 %buildroot/%target
%__install -m644 %SOURCE8 %buildroot/%target
%__install -d %buildroot/%_docdir/%name
%__install -m644 %SOURCE9 %buildroot/%_docdir/%name
%__install -m644 %SOURCE10 %buildroot/%target
%__install -m644 %SOURCE11 %buildroot/%target
%__install -m644 %SOURCE12 %buildroot/%target
%__install -m644 %SOURCE13 %buildroot/%target
%__install -m644 %SOURCE14 %buildroot/%target
%__install -m644 %SOURCE15 %buildroot/%target
%__install -m644 %SOURCE16 %buildroot/%target
%__install -m644 %SOURCE17 %buildroot/%target

echo 'enable_uart=1' > %buildroot/%target/config.txt

%files
%target/*
%doc %_docdir/%name

%changelog
* Thu Sep 26 2019 Dmitry Terekhin <jqt4@altlinux.org> 20190926-alt1
- new snapshot

* Sat Jul 20 2019 Anton Midyukov <antohami@altlinux.org> 20190716-alt1
- new snapshot

* Sat Feb 16 2019 Anton Midyukov <antohami@altlinux.org> 20190213-alt1
- Initial build
