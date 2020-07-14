Name: u-boot-sunxi
Version: 2020.04
Release: alt1

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware
Url: http://linux-sunxi.org/U-Boot

ExclusiveArch: armh aarch64

Source: %name-%version-%release.tar

Provides: u-boot-sunxi64 = %version-%release
Obsoletes: u-boot-sunxi64

%ifarch aarch64
%define ATF atf-sunxi >= 2.0
%else
%define ATF %nil
%endif

BuildRequires: %ATF bc ccache dtc >= 1.4 flex
BuildRequires: python3-dev swig

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports boards based on Allwinner SoCs.

See http://linux-sunxi.org/Bootable_SD_card#Bootloader for details.

%prep
%setup

%build
export PYTHON=python3
%ifarch aarch64
boards=$(grep -lr MACH_SUN50I configs |sed 's,^configs/\(.\+\)_defconfig,\1,')
%else
boards=$(grep -lr 'MACH_SUN[4-9]I' configs |sed 's,^configs/\(.\+\)_defconfig,\1,')
%endif
for board in $boards; do
	mkdir build
%ifarch aarch64
	fgrep -q SUN50I_H6 configs/${board}_defconfig && \
		export BL31=%_datadir/atf/sun50i_h6/bl31.bin || \
		export BL31=%_datadir/atf/sun50i_a64/bl31.bin
%endif
	%make_build HOSTCC='ccache gcc' CC='ccache gcc' O=build ${board}_defconfig all
	grep -q '^CONFIG_SPL=y' build/.config && \
	install -pm0644 -D build/u-boot-sunxi-with-spl.bin out/${board}/u-boot-sunxi-with-spl.bin
	rm -rf build
done

%install
mkdir -p %buildroot%_datadir/u-boot
cd out
find . -type f | cpio -pmd %buildroot%_datadir/u-boot

%files
%doc README README.sunxi board/sunxi/README.sunxi64
%_datadir/u-boot/*

%changelog
* Tue Apr 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.04-alt1
- 2020.04 released

* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.01-alt1
- 2020.01 released

* Tue Oct 08 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.10-alt1
- 2019.10 released

* Wed Jul 17 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.07-alt1
- 2019.07 released

* Tue Apr 16 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Tue Jan 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Mon Dec 03 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- 2018.11 released

* Tue Sep 04 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.07-alt1
- 2018.07 released

* Fri Jul 06 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.05-alt1
- 2018.05 released

* Mon Jan 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.01-alt1
- 2018.01 released

* Sun Sep 24 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.09-alt1
- 2017.09 released

* Fri Feb 17 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.01-alt1
- 2017.01 released

* Sun Sep 04 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2016.07-alt1
- 2016.07 released

* Tue Apr 14 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2015.04-alt1
- 2015.04 released

* Tue Jan 13 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2015.01-alt1
- 2015.01 released

* Tue Jun 10 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2014.04-alt1
- 2014.04-sunxi released

* Mon Feb 17 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2013.10-alt1
- 2013.10-sunxi released

* Fri Sep 27 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2013.07-alt2
- 2013.07-sunxi released

* Wed Aug 07 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2013.07-alt1
- initial
