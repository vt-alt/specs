Name: u-boot-rockchip
Version: 2020.04
Release: alt1

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

BuildRequires: atf-rockchip >= 2.0
BuildRequires: bc ccache dtc >= 1.4 flex
BuildRequires: python3-dev swig
BuildRequires: python3(elftools.elf.elffile)

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports various Rockchip RK3399 based boards.

%prep
%setup
fgrep -lr CONFIG_ROCKCHIP_RK3399 configs |xargs sed -i \
	-e '/^CONFIG_DEFAULT_FDT_FILE/ s,rockchip/,,' \
	-e '/^CONFIG_BAUDRATE/ s,1500000,115200,'
sed -E '/^CONFIG_DEFAULT_FDT_FILE=/ s,=.+$,="rk3399-sapphire-excavator.dtb",' \
	< configs/evb-rk3399_defconfig > configs/rk3399-sapphire-excavator_defconfig

%build
export PYTHON=python3
export BL31=%_datadir/atf/rk3399/bl31.elf

buildit()
{
  mkdir build
  %make_build O=build ${board}_defconfig all
  install -pm0644 -D build/u-boot.itb out/${board}/u-boot.itb
  grep -q ^CONFIG_TPL= build/.config && {
    build/tools/mkimage -n rk3399 -T rksd -d build/tpl/u-boot-tpl-dtb.bin out/${board}/idbspl.img
    cat build/spl/u-boot-spl-dtb.bin >> out/${board}/idbspl.img
  } || {
    build/tools/mkimage -n rk3399 -T rksd -d build/spl/u-boot-spl.bin out/${board}/idbspl.img
  }
  rm -rf build
}

boards=$(fgrep -lr CONFIG_ROCKCHIP_RK3399 configs |sed 's,^configs/\(.\+\)_defconfig,\1,')
for board in $boards; do buildit; done

%install
mkdir -p %buildroot%_datadir/u-boot
cd out 
find . -type f | cpio -pmd %buildroot%_datadir/u-boot

%files
%doc README doc/README.rockchip
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

* Mon Apr 15 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Wed Mar 06 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Tue Sep 04 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.07-alt1
- 2018.07 released

* Thu Apr 19 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.03-alt1
- 2018.03 released

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
