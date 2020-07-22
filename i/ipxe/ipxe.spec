
%def_enable efi_ia32

%define formats rom
# PCI IDs (vendor,product) of the ROMS we want for QEMU
#
#    pcnet32: 0x1022 0x2000
#   ne2k_pci: 0x10ec 0x8029
#      e1000: 0x8086 0x100e
#    rtl8139: 0x10ec 0x8139
# virtio-net: 0x1af4 0x1000
#   eepro100: 0x8086 0x1209
#     e1000e: 0x8086 0x10d3
#    vmxnet3: 0x15ad 0x07b0

%define qemuroms 10222000 10ec8029 8086100e 10ec8139 1af41000 80861209 808610d3 15ad07b0
%define date 20190817
%define hash 0b3000bb

Name: ipxe
Version: %date
Release: alt1.git%{hash}
Epoch: 1

Summary: PXE boot firmware
License: GPLv2 with additional permissions and BSD
Group: Networking/Other
Url: http://ipxe.org/
#Vcs-Git: git://git.ipxe.org/ipxe.git
ExclusiveArch: x86_64

Provides: gpxe
Obsoletes: gpxe

Source: %name-%version.tar
Patch: %name-%version.patch

Requires: ipxe-bootimgs
BuildRequires: genisoimage mtools syslinux binutils-devel edk2-tools
BuildRequires: liblzma-devel

%description
iPXE is the leading open source network boot firmware.
It provides a full PXE implementation enhanced with additional features such as:
- boot from a web server via HTTP
- boot from an iSCSI SAN
- boot from a Fibre Channel SAN via FCoE
- boot from an AoE SAN
- boot from a wireless network
- boot from a wide-area network
- boot from an Infiniband network
- control the boot process with a script

You can use iPXE to replace the existing PXE ROM on your network card,
or you can chainload into iPXE to obtain the features of iPXE without the hassle of reflashing.

%package bootimgs
Summary: Network boot loader images in bootable USB, CD, floppy and GRUB formats
Group: Development/Tools
BuildArch: noarch
Provides: gpxe-bootimgs
Obsoletes: gpxe-bootimgs

%description bootimgs
iPXE is an implementation of the PXE specification for network
booting, with extensions to allow additional features such as booting
via HTTP, iSCSI, and AoE.

This package contains the iPXE boot images in USB, CD, floppy, and PXE
UNDI formats.

%package roms
Summary: Network boot loader roms in .rom format
Group: Development/Tools
BuildArch: noarch
Requires: %name-roms-qemu = %EVR
Provides: gpxe-roms
Obsoletes: gpxe-roms

%description roms
iPXE is an implementation of the PXE specification for network
booting, with extensions to allow additional features such as booting
via HTTP, iSCSI, and AoE.

This package contains the iPXE roms in .rom format.

%package roms-qemu
Summary: Network boot loader roms supported by QEMU, .rom format
Group: Development/Tools
BuildArch: noarch
Provides: gpxe-roms-qemu
Obsoletes: gpxe-roms-qemu

%description roms-qemu
iPXE is an implementation of the PXE specification for network
booting, with extensions to allow additional features such as booting
via HTTP, iSCSI, and AoE.

This package contains the iPXE ROMs for devices emulated by QEMU, in
.rom format.

%prep
%setup
%patch -p1

%build
cd src

# ath9k drivers are too big for an Option ROM, and ipxe devs say it doesn't
# make sense anyways
# http://lists.ipxe.org/pipermail/ipxe-devel/2012-March/001290.html
rm -rf drivers/net/ath/ath9k

make_ipxe() {
    %make_build \
	NO_WERROR=1 \
	V=1 \
	GITVERSION=%hash \
        "$@"
}

make_ipxe bin-i386-efi/ipxe.efi bin-x86_64-efi/ipxe.efi

make_ipxe ISOLINUX_BIN=/usr/lib/syslinux/isolinux.bin \
	bin/undionly.kpxe \
	bin/ipxe.{dsk,iso,usb,lkrn} \
	allroms

# build roms with efi support for qemu
mkdir bin-combined
for rom in %qemuroms; do
  make_ipxe CONFIG=qemu bin/${rom}.rom
%if_enabled efi_ia32
  make_ipxe CONFIG=qemu bin-i386-efi/${rom}.efidrv
%endif
  make_ipxe CONFIG=qemu bin-x86_64-efi/${rom}.efidrv
  vid="0x${rom%%????}"
  did="0x${rom#????}"
  EfiRom -f "$vid" -i "$did" --pci23 \
         -b  bin/${rom}.rom \
%if_enabled efi_ia32
         -ec bin-i386-efi/${rom}.efidrv \
%endif
         -ec bin-x86_64-efi/${rom}.efidrv \
         -o  bin-combined/${rom}.rom

  EfiRom -d  bin-combined/${rom}.rom
  # truncate to at least 256KiB
  truncate -s \>256K bin-combined/${rom}.rom
  # verify rom fits in 256KiB
  test $(stat -c '%%s' bin-combined/${rom}.rom) -le $((256 * 1024))
done

%install
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/%name.efi

pushd src/bin/

install -pm0644 undionly.kpxe ipxe.{iso,usb,dsk,lkrn}  %buildroot%_datadir/%name

for fmt in %formats; do
 for img in *.${fmt}; do
      if [ -e $img ]; then
   cp -a $img %buildroot%_datadir/%name/
   echo %_datadir/%name/$img >> ../../${fmt}.list
  fi
 done
done
popd

cp -a src/bin-i386-efi/ipxe.efi %buildroot/%_datadir/%name/ipxe-i386.efi
cp -a src/bin-x86_64-efi/ipxe.efi %buildroot/%_datadir/%name/ipxe-x86_64.efi

# the roms supported by qemu will be packaged separatedly
# remove from the main rom list and add them to qemu.list
for fmt in rom ; do
 for rom in %qemuroms ; do
  sed -i -e "/\/${rom}.${fmt}/d" ${fmt}.list
  echo %_datadir/%name/${rom}.${fmt} >> qemu.${fmt}.list
 done
done
for rom in %qemuroms; do
  cp src/bin-combined/${rom}.rom %buildroot/%_datadir/%name.efi/
  echo %_datadir/%name.efi/${rom}.rom >> qemu.${fmt}.list
done

pxe_link() {
  ln -r -s %buildroot%_datadir/%name/$1.rom %buildroot%_datadir/%name/pxe-$2.rom
  ln -r -s %buildroot%_datadir/%name.efi/$1.rom %buildroot%_datadir/%name.efi/efi-$2.rom
}

pxe_link 8086100e e1000
pxe_link 10ec8029 ne2k_pci
pxe_link 10222000 pcnet
pxe_link 10ec8139 rtl8139
pxe_link 1af41000 virtio
pxe_link 80861209 eepro100
pxe_link 808610d3 e1000e
pxe_link 15ad07b0 vmxnet3

%files bootimgs
%_datadir/%name/ipxe.iso
%_datadir/%name/ipxe.usb
%_datadir/%name/ipxe.dsk
%_datadir/%name/ipxe.lkrn
%_datadir/%name/ipxe-i386.efi
%_datadir/%name/ipxe-x86_64.efi
%_datadir/%name/undionly.kpxe
%doc COPYING COPYING.GPLv2 COPYING.UBDL

%files roms -f rom.list
%doc COPYING COPYING.GPLv2 COPYING.UBDL

%files roms-qemu -f qemu.rom.list
%doc COPYING COPYING.GPLv2 COPYING.UBDL
%dir %_datadir/%name
%_datadir/%name/pxe-*.rom
%dir %_datadir/%name.efi
%_datadir/%name.efi/efi-*.rom

%changelog
* Thu Sep 12 2019 Alexey Shabalin <shaba@altlinux.org> 1:20190817-alt1.git0b3000bb
- update to latest upstream snapshot

* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 1:20180825-alt2.git133f4c47
- disable cross build

* Tue Nov 27 2018 Alexey Shabalin <shaba@altlinux.org> 1:20180825-alt1.git133f4c47
- update to latest upstream snapshot

* Fri Apr 27 2018 Alexey Shabalin <shaba@altlinux.ru> 1:20180420-alt1.git960d1e36%ubt
- update to latest upstream snapshot

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1:20170830-alt1.git75acb3c7%ubt
- update to latest upstream snapshot

* Thu Apr 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1:20161208-alt1.git26050fd%ubt
- rebuild with ubt macros

* Wed Dec 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:20161208-alt1.git26050fd
- update to latest upstream snapshot
- build e1000e,vmxnet3 rom

* Tue Jun 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:20150821-alt1.git4e03af8
- rollback to 20150821

* Wed May 25 2016 Alexey Shabalin <shaba@altlinux.ru> 20160525-alt1.gitf42b258
- update to latest upstream snapshot
- Enable IPv6 for in qemu config

* Mon May 18 2015 Alexey Shabalin <shaba@altlinux.ru> 20150516-alt1.gita91b1f7
- update to latest upstream snapshot
- include patches from QEMU submodule
- distribute additional permissions on top of GPLv2 ("UBDL")
- define version of package as date of upstream snapshot

* Fri Apr 18 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt4.git93acb5d
- upstream git snapshot 93acb5d8d0635b8f7726bd993cde4a90a6b1d723

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt3.git55201e2
- upstream git snapshot 55201e2d0e60003edfd7e2c7c4c592136b000f44
- build UEFI drivers for QEMU
- move roms from _libexecdir to _datadir

* Fri Aug 12 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt2.git174df77
- add Provides Obsoletes for gpxe

* Thu Aug 11 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1.git174df77
- Initial build.
