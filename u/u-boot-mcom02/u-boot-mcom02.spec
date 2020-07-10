Name: u-boot-mcom02
Version: 2019.01.0.11
Release: alt1

Summary: Das U-Boot
License: GPL
Group: System/Kernel and hardware
Url: https://github.com/elvees/u-boot

ExclusiveArch: armh

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: bc ccache dtc >= 1.4 flex
BuildRequires: python-devel swig
BuildRequires: python2.7(multiprocessing)

Requires: mtd-utils

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports various ELVEES MCom-02 based boards.

%package firmware-tools
Group: System/Kernel and hardware
Summary: U-Boot Firmware tools for MCom-02

%description firmware-tools
U-Boot Firmware tools for MCom-02. Contains mcom02-fw-update tool which allows one
to update U-Boot firmware on MCom-02 based board.

%prep
%setup
%patch0 -p1

%build

build_func() {
	for board in ${@:2}; do
		mkdir build
		%make_build HOSTCC='ccache gcc' CC='ccache gcc' DEVICE_TREE=${board} O=build ${1}_defconfig all
		install -Dpm0644 build/u-boot.mcom out/${1}/${board}-uboot.img
		rm -rf build
	done
}

build_func "saluted1" \
	"mcom02-salute-el24d1-r1.3" \
	"mcom02-salute-el24d1-r1.4" \
	"mcom02-salute-el24d1-r1.5"

build_func "saluted2" \
	"mcom02-salute-el24d2-r1.1"

build_func "salutepm" \
	"mcom02-salute-el24pm1-r1.1-1.2-om1-r1.1-1.2" \
	"mcom02-salute-el24pm2-r1.0-1.1-om1-r1.2"

echo 'SUBSYSTEM=="mtd", ATTR{name}!="", SYMLINK+="mtd/by-name/$attr{name}"' > 10-persistent-mtd.rules

%install
install -Dpm0755 tools/mcom02-fw-update %buildroot%_sbindir/mcom02-fw-update
install -Dpm0644 tools/env/fw_env.config %buildroot%_sysconfdir/fw_env.config
install -Dpm0644 10-persistent-mtd.rules %buildroot%_sysconfdir/udev/rules.d/10-persistent-mtd.rules
install -Dpm0644 README %buildroot%_datadir/doc/README
install -Dpm0644 README.mcom02 %buildroot%_datadir/doc/README.mcom02

mkdir -p %buildroot%_datadir/u-boot
cd out
find . -type f | cpio -pmd %buildroot%_datadir/u-boot

%files
%_datadir/u-boot/*
%_datadir/doc/*

%files firmware-tools
%_sbindir/mcom02-fw-update
%_sysconfdir/fw_env.config
%_sysconfdir/udev/rules.d/10-persistent-mtd.rules

%changelog
* Thu Jul 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01.0.11-alt1
- Update for 2019.01.0.11-alt1

* Mon Jul 08 2019 RnD Center ELVEES <rnd_elvees@altlinux.org> 2019.01.0.6-alt1
- Update for 2019.01.0.6-alt1

* Wed Jul 03 2019 RnD Center ELVEES <rnd_elvees@altlinux.org> 2019.01.0.5-alt1
- initial
