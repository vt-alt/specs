%set_verify_elf_method no

Summary: bootloader and GPU firmware for Raspberry Pi
Name: raspberrypi-firmware
Version: 20200730
Release: alt1
Url: https://github.com/raspberrypi/firmware
License: distributable
Group: System/Kernel and hardware

ExclusiveArch: %arm aarch64

Source0: %name-%version.tar

Requires: u-boot-rpi3

%description
%summary

%install
mkdir -p %buildroot%_datadir
tar -xf %SOURCE0 -C %buildroot%_datadir

%ifarch %arm
%define target_rpi3 %_datadir/u-boot/rpi_3_32b
%define target_rpi4 %_datadir/u-boot/rpi_4_32b
%endif

%ifarch aarch64
%define target_rpi3 %_datadir/u-boot/rpi_3
%define target_rpi4 %_datadir/u-boot/rpi_4
%endif

mkdir -p %buildroot/%target_rpi3
pushd %buildroot/%_datadir/%name
ln bootcode.bin %buildroot/%target_rpi3
ln fixup.dat %buildroot/%target_rpi3
ln fixup_cd.dat %buildroot/%target_rpi3
ln fixup_db.dat %buildroot/%target_rpi3
ln fixup_x.dat %buildroot/%target_rpi3
ln start.elf %buildroot/%target_rpi3
ln start_cd.elf %buildroot/%target_rpi3
ln start_db.elf %buildroot/%target_rpi3
ln start_x.elf %buildroot/%target_rpi3
ln bcm2710-rpi-3-b.dtb %buildroot/%target_rpi3
ln bcm2710-rpi-3-b-plus.dtb %buildroot/%target_rpi3

mkdir -p %buildroot/%target_rpi4
ln fixup4.dat %buildroot/%target_rpi4
ln fixup4cd.dat %buildroot/%target_rpi4
ln fixup4db.dat %buildroot/%target_rpi4
ln fixup4x.dat %buildroot/%target_rpi4
ln start4.elf %buildroot/%target_rpi4
ln start4cd.elf %buildroot/%target_rpi4
ln start4db.elf %buildroot/%target_rpi4
ln start4x.elf %buildroot/%target_rpi4
ln bcm2711-rpi-4-b.dtb %buildroot/%target_rpi4

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
%_datadir/%name
%target_rpi3/*
%target_rpi4/*

%changelog
* Thu Jul 30 2020 Anton Midyukov <antohami@altlinux.org> 20200730-alt1
- New snapshot
- Added overlays and dtb for all boards

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
