%define debug_level 1

Name: seabios
Version: 1.13.0
Release: alt2
Summary: Open-source legacy BIOS implementation

Group: Emulators
BuildArch: noarch
ExclusiveArch: x86_64
License: LGPLv3
Url: http://www.seabios.org

# git://git.seabios.org/seabios.git
Source: %name-%version.tar
Patch: %name-%version-snapshot.patch

Patch0001: 0001-Workaround-for-a-win8.1-32-S4-resume-bug.patch
Patch0002: 0002-reserve-more-memory-on-fseg.patch
Patch0003: 0003-vgabios-Reorder-video-modes-to-work-around-a-Windows.patch

Source10: config.vga.cirrus
Source11: config.vga.isavga
Source12: config.vga.qxl
Source13: config.vga.stdvga
Source14: config.vga.vmware
Source15: config.csm
Source16: config.coreboot
Source17: config.seabios-128k
Source18: config.seabios-256k
Source19: config.vga.virtio
Source20: config.vga.bochs-display
Source21: config.vga.ramfb
Source22: config.vga.ati

BuildRequires: python3
BuildRequires: acpica
Conflicts: qemu-common < 1.6.0-alt1

%description
SeaBIOS is an open-source legacy BIOS implementation which can be used as
a coreboot payload. It implements the standard BIOS calling interfaces
that a typical x86 proprietary BIOS implements.

%package -n seavgabios
Summary: Seavgabios for x86
Group: Emulators
BuildArch: noarch

%description -n seavgabios
SeaVGABIOS is an open-source VGABIOS implementation.

%set_verify_elf_skiplist %_datadir/%name/bios*.bin

%prep
%setup -q
%patch -p1

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1

echo %version > .version

%build
export CFLAGS="$RPM_OPT_FLAGS"
mkdir -p binaries

build_bios() {
	make clean distclean
	cp $1 .config
	echo "CONFIG_DEBUG_LEVEL=%{debug_level}" >> .config
	make oldnoconfig V=1
	make V=1 \
		EXTRAVERSION="-%{release}" \
		PYTHON=python3 \
		HOSTCC=gcc \
		$4

	cp out/$2 binaries/$3
}

# seabios
build_bios %SOURCE15 Csm16.bin bios-csm.bin
build_bios %SOURCE16 bios.bin.elf bios-coreboot.bin
build_bios %SOURCE17 bios.bin bios.bin
build_bios %SOURCE18 bios.bin bios-256k.bin

# seavgabios
for config in %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14 %SOURCE19 %SOURCE20 %SOURCE21 %SOURCE22 ; do
	name=${config#*config.vga.}
	build_bios ${config} vgabios.bin vgabios-${name}.bin out/vgabios.bin
done

%install
mkdir -p %buildroot%_datadir/%name
install -m 0644 binaries/bios.bin %buildroot%_datadir/%name/bios.bin
install -m 0644 binaries/bios-256k.bin %buildroot%_datadir/%name/bios-256k.bin
install -m 0644 binaries/bios-csm.bin %buildroot%_datadir/%name/bios-csm.bin
install -m 0644 binaries/bios-coreboot.bin %buildroot%_datadir/%name/bios-coreboot.bin

mkdir -p %buildroot%_datadir/seavgabios
install -m 0644 binaries/vgabios*.bin %buildroot%_datadir/seavgabios
ln -r -s %buildroot%_datadir/seavgabios/vgabios-isavga.bin %buildroot%_datadir/seavgabios/vgabios.bin

%files
%doc COPYING COPYING.LESSER README
%dir %_datadir/%name
%_datadir/%name/bios*.bin

%files -n seavgabios
%dir %_datadir/seavgabios
%_datadir/seavgabios/vgabios*.bin

%changelog
* Mon Jul 20 2020 Alexey Shabalin <shaba@altlinux.org> 1.13.0-alt2
- disable cross build

* Fri Dec 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.0-alt1
- 1.13.0
- build vgabios-ati

* Tue Apr 02 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.1-alt1
- 1.12.1

* Wed Nov 28 2018 Alexey Shabalin <shaba@altlinux.org> 1.12.0-alt1
- 1.12.0

* Fri Aug 24 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.2-alt1
- 1.11.2
- fixed VGA VID and DID for vmware and virtio
- added VGA DISPLAY_BOCHS and RAMFB

* Mon Apr 02 2018 Alexey Shabalin <shaba@altlinux.ru> 1.11.1-alt1
- 1.11.1
- Build with Python 3

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0
- Add patches from RHEL

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.3-alt1
- 1.10.3

* Thu Apr 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.2-alt1
- rebuild with ubt macros

* Fri Apr 21 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.2-alt1
- 1.10.2
- Don't attempt to use generic reboot mechanisms on QEMU

* Fri Dec 09 2016 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Fri May 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Tue Dec 15 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0
- build vgabios-virtio

* Fri Jun 19 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Mar 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Tue Nov 18 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.5.1-alt1
- 1.7.5.1

* Tue Aug 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.5-alt2
- Fix PCI-e hotplug

* Mon Jun 02 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.5-alt1
- 1.7.5

* Fri Apr 18 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt2
- upstream snapshot 0784d04cb6f6e5c893aaf368091f20326fb847fe
- build 256k bios images for qemu 2.0

* Wed Jan 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Wed Oct 09 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.3.2-alt1
- 1.7.3.2

* Fri Aug 16 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.3.1-alt1
- 1.7.3.1

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.3-alt2
- move seabios binary to _datadir

* Thu Aug 08 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Thu Jul 04 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.2.2-alt1
- 1.7.2.2

* Tue May 07 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.2.1-alt1
- 1.7.2.1

* Tue Feb 19 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt2
- add seavgabios package

* Tue Feb 19 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Fri Sep 28 2012 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.3.2-alt1
- 1.6.3.2

* Fri Dec 02 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.3.1-alt1
- 1.6.3.1

* Thu Oct 13 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Thu Aug 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1.git8e3014
- upstream git snapshot 8e301472e324b6d6496d8b4ffc66863e99d7a505

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.3-alt1
- 0.6.1.3

* Fri Dec 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.2-alt1
- initial build for ALT Linux Sisyphus
