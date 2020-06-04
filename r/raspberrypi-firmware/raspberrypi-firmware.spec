%set_verify_elf_method no

Summary: bootloader and GPU firmware for Raspberry Pi
Name: raspberrypi-firmware
Version: 20200527
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
Source18: bcm2711-rpi-4-b.dtb

Requires: u-boot-rpi3

%description
%summary

%install
%ifarch %arm
%define target_rpi3 %_datadir/u-boot/rpi_3_32b
%define target_rpi4 %_datadir/u-boot/rpi_4_32b
%endif

%ifarch aarch64
%define target_rpi3 %_datadir/u-boot/rpi_3
%define target_rpi4 %_datadir/u-boot/rpi_4
%endif

%__install -d %buildroot/%target_rpi3
%__install -m644 %SOURCE0 %buildroot/%target_rpi3
%__install -m644 %SOURCE1 %buildroot/%target_rpi3
%__install -m644 %SOURCE2 %buildroot/%target_rpi3
%__install -m644 %SOURCE3 %buildroot/%target_rpi3
%__install -m644 %SOURCE4 %buildroot/%target_rpi3
%__install -m644 %SOURCE5 %buildroot/%target_rpi3
%__install -m644 %SOURCE6 %buildroot/%target_rpi3
%__install -m644 %SOURCE7 %buildroot/%target_rpi3
%__install -m644 %SOURCE8 %buildroot/%target_rpi3
%__install -d %buildroot/%_docdir/%name
%__install -m644 %SOURCE9 %buildroot/%_docdir/%name
%__install -d %buildroot/%target_rpi4
%__install -m644 %SOURCE10 %buildroot/%target_rpi4
%__install -m644 %SOURCE11 %buildroot/%target_rpi4
%__install -m644 %SOURCE12 %buildroot/%target_rpi4
%__install -m644 %SOURCE13 %buildroot/%target_rpi4
%__install -m644 %SOURCE14 %buildroot/%target_rpi4
%__install -m644 %SOURCE15 %buildroot/%target_rpi4
%__install -m644 %SOURCE16 %buildroot/%target_rpi4
%__install -m644 %SOURCE17 %buildroot/%target_rpi4
%__install -m644 %SOURCE18 %buildroot/%target_rpi4

cp -a %buildroot/%target_rpi3/bootcode.bin %buildroot/%target_rpi4

%ifarch aarch64
cat>%buildroot/%target_rpi4/config.txt<<EOF
arm_64bit=1
EOF
%endif

tee --append %buildroot/%target_rpi3/config.txt %buildroot/%target_rpi4/config.txt<<EOF
enable_uart=1
disable_overscan=1
dtparam=audio=on
EOF

cat>>%buildroot/%target_rpi4/config.txt<<EOF
dtoverlay=vc4-fkms-v3d
EOF

%files
%target_rpi3/*
%target_rpi4/*
%doc %_docdir/%name

%changelog
* Tue Jun 02 2020 Dmitry Terekhin <jqt4@altlinux.org> 20200527-alt1
- Added parameter in config.txt for RPi4:
- dtoverlay=vc4-fkms-v3d
- New snapshot

* Thu Apr 16 2020 Anton Midyukov <antohami@altlinux.org> 20200228-alt3
- Also added parameters in config.txt for RPi3:
- disable_overscan=1
- dtparam=audio=on

* Wed Apr 01 2020 Dmitry Terekhin <jqt4@altlinux.org> 20200228-alt2
- Added parameters in config.txt for RPi4:
- disable_overscan=1
- dtparam=audio=on

* Wed Mar 04 2020 Dmitry Terekhin <jqt4@altlinux.org> 20200228-alt1
- new snapshot

* Thu Nov 14 2019 Dmitry Terekhin <jqt4@altlinux.org> 20191105-alt2
- Added bcm2711-rpi-4-b.dtb for the RasPi4 firmware's work

* Tue Nov 05 2019 Dmitry Terekhin <jqt4@altlinux.org> 20191105-alt1
- new snapshot

* Tue Oct 08 2019 Anton Midyukov <antohami@altlinux.org> 20190926-alt2
- Add support u-boot-rpi3-2019.10

* Thu Sep 26 2019 Dmitry Terekhin <jqt4@altlinux.org> 20190926-alt1
- new snapshot

* Sat Jul 20 2019 Anton Midyukov <antohami@altlinux.org> 20190716-alt1
- new snapshot

* Sat Feb 16 2019 Anton Midyukov <antohami@altlinux.org> 20190213-alt1
- Initial build
