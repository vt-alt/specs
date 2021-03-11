Name: u-boot-tools
Version: 2021.01
Release: alt2

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware

ExclusiveArch: armh aarch64 mipsel %ix86 x86_64

Provides: uboot-tools = %version-%release
Obsoletes: uboot-tools

Source: %name-%version-%release.tar

BuildRequires: flex libssl-devel

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package contains U-Boot tools.

%prep
%setup

%build
%make_build NO_SDL=1 tools-only_defconfig tools-all

%install
mkdir -p %buildroot%_bindir
install -pm0644 -D tools/env/fw_env.config %buildroot%_sysconfdir/fw_env.config
install -pm0755 tools/{dumpimage,fdtgrep,gen_eth_addr,kwboot,mkimage,mkenvimage,env/fw_printenv} %buildroot%_bindir/
ln -s fw_printenv %buildroot%_bindir/fw_setenv

%files
%config(noreplace) %_sysconfdir/fw_env.config
%_bindir/*

%changelog
* Mon Feb 01 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.01-alt2
- fw_setenv/fw_printenv and sample config packaged

* Tue Jan 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.01-alt1
- 2021.01 released

* Tue Oct 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.10-alt1
- 2020.10 released

* Fri Jul 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.07-alt1
- 2020.07 released

* Tue Apr 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.04-alt1
- 2020.04 released

* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.01-alt1
- 2020.01 released

* Tue Oct 08 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.10-alt1
- 2019.10 released

* Fri Jul 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.07-alt1
- 2019.07 released

* Fri Apr 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Tue Jan 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Fri Jan 11 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- initial
