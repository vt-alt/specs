Name: u-boot-tools
Version: 2019.07
Release: alt1

Summary: Das U-Boot
License: GPL
Group: System/Kernel and hardware

ExclusiveArch: armh aarch64 %ix86 x86_64

Provides: uboot-tools = %version-%release
Obsoletes: uboot-tools

Source: %name-%version-%release.tar

BuildRequires: flex libssl-devel libSDL-devel

%def_without sandbox

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package contains sandboxed U-Boot and tools.

%prep
%setup

%build
echo CONFIG_HOST_32BIT=y >> configs/sandbox_defconfig
echo CONFIG_TOOLS_DEBUG=y >> configs/sandbox_defconfig 
%make_build sandbox_defconfig %{?_with_sandbox:all}%{!?_with_sandbox:tools}

%install
mkdir -p %buildroot%_bindir
install -pm0755 tools/{dumpimage,fdtgrep,gen_eth_addr,mkimage,mkenvimage} %{?_with_sandbox:u-boot} %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Fri Jul 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.07-alt1
- 2019.07 released

* Fri Apr 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Tue Jan 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Fri Jan 11 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- initial
