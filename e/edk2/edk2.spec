%define TOOL_CHAIN_TAG GCC49
%define openssl_ver 1.1.1d

# More subpackages to come once licensing issues are fixed
Name: edk2
Version: 20200229
Release: alt1
Summary: EFI Development Kit II

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: %name-%version.tar

Source2: openssl.tar
Source3: berkeley-softfloat-3.tar
Source4: Logo.bmp

Patch1: %name-%version.patch

License: BSD-2-Clause
Group: Emulators
Url: http://www.tianocore.org

ExclusiveArch: x86_64

BuildRequires: iasl nasm gcc-c++
BuildRequires: python3-devel python3-modules-sqlite3
BuildRequires: libuuid-devel
BuildRequires: bc

%description
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.

%package ovmf
Summary: Open Virtual Machine Firmware
Group: Emulators
License: BSD-2-Clause and OpenSSL
BuildArch: noarch
Provides: edk2-ovmf-x86_64 = %EVR
Requires: ipxe-roms-qemu
Requires: seavgabios

%description ovmf
EFI Development Kit II
Open Virtual Machine Firmware

%package ovmf-ia32
Summary: Open Virtual Machine Firmware
Group: Emulators
License: BSD-2-Clause and OpenSSL
BuildArch: noarch

%description ovmf-ia32
EFI Development Kit II
Open Virtual Machine Firmware (ia32)

%package efi-shell
Summary: EFI Development Kit II
Group: System/Kernel and hardware
Provides: efi-shell = 2.2
Obsoletes: efi-shell

%description efi-shell
EFI Development Kit II implementation of UEFI Shell 2.0+

%prep
%setup -q
%patch1 -p1

cp -f %SOURCE4 MdeModulePkg/Logo/

# cleanup
find . -name '*.efi' -print0 | xargs -0 rm -f
rm -rf BaseTools/Bin \
	UefiCpuPkg/ResetVector/Vtf0/Bin/*.raw \
	EdkCompatibilityPkg/Other \
	AppPkg \
	DuetPkg/BootSector/bin \
	StdLib/LibC/Main/Ia32/ftol2.obj \
	BeagleBoardPkg/Debugger_scripts/rvi_dummy.axf \
	BaseTools/Source/Python/*/*.pyd \
	BaseTools/Source/Python/UPT/Dll/sqlite3.dll \
	Vlv2TbltDevicePkg/GenBiosId \
	Vlv2TbltDevicePkg/*.exe \
	ArmPkg/Library/GccLto/liblto-*.a

# Ensure old shell and binary packages are not used
rm -rf EdkShellBinPkg
rm -rf EdkShellPkg
rm -rf FatBinPkg
rm -rf ShellBinPkg

# add openssl
mkdir -p CryptoPkg/Library/OpensslLib/openssl
tar -xf %SOURCE2 --strip-components 1 --directory CryptoPkg/Library/OpensslLib/openssl

# add /berkeley-softfloat-3
mkdir -p ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3
tar -xf %SOURCE3 --strip-components 1 --directory ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3

%build
export PYTHON_COMMAND=%__python3
source ./edksetup.sh

# compiler
CC_FLAGS="-t %TOOL_CHAIN_TAG"

# common features
#CC_FLAGS="${CC_FLAGS} --cmd-len=65536 -b DEBUG --hash"
CC_FLAGS="${CC_FLAGS} -b RELEASE"
#CC_FLAGS="${CC_FLAGS} -b DEBUG --hash"
CC_FLAGS="${CC_FLAGS} --cmd-len=65536"
CC_FLAGS="${CC_FLAGS} -D NETWORK_IP6_ENABLE"
CC_FLAGS="${CC_FLAGS} -D TPM2_ENABLE"

# ovmf features
OVMF_FLAGS="${CC_FLAGS}"
OVMF_FLAGS="${OVMF_FLAGS} -D NETWORK_TLS_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D NETWORK_HTTP_BOOT_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D FD_SIZE_2MB"

# ovmf + secure boot features
OVMF_SB_FLAGS="${OVMF_FLAGS}"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D SECURE_BOOT_ENABLE"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D SMM_REQUIRE"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D EXCLUDE_SHELL_FROM_FD"

# arm firmware features
#ARM_FLAGS="-t %TOOL_CHAIN_TAG -b DEBUG --cmd-len=65536"
ARM_FLAGS="${CC_FLAGS}"
ARM_FLAGS="${ARM_FLAGS} -D DEBUG_PRINT_ERROR_LEVEL=0x8040004F"


unset MAKEFLAGS

# prepare
#cp /usr/share/seabios/bios-csm.bin OvmfPkg/Csm/Csm16/Csm16.bin
#cp /usr/share/seabios/bios-csm.bin corebootPkg/Csm/Csm16/Csm16.bin
%make_build \
	 -C BaseTools


#(cd UefiCpuPkg/ResetVector/Vtf0; python Build.py)

#mkdir -p FatBinPkg/EnhancedFatDxe/{X64,Ia32}
#source ./edksetup.sh

# build ovmf (x64)
mkdir -p OVMF
build ${OVMF_FLAGS} -a X64 -p OvmfPkg/OvmfPkgX64.dsc
cp Build/OvmfX64/*/FV/OVMF_*.fd OVMF
rm -rf Build/OvmfX64
# build ovmf with secure boot
build ${OVMF_SB_FLAGS} -a IA32 -a X64 -p OvmfPkg/OvmfPkgIa32X64.dsc
cp Build/Ovmf3264/*/FV/OVMF_CODE.fd OVMF/OVMF_CODE.secboot.fd

# build shell
build ${OVMF_FLAGS} -a X64 -p ShellPkg/ShellPkg.dsc

# build ovmf-ia32
mkdir -p ovmf-ia32
build ${OVMF_FLAGS} -a IA32 -p OvmfPkg/OvmfPkgIa32.dsc
cp Build/OvmfIa32/*/FV/OVMF_CODE.fd ovmf-ia32/
rm -rf Build/OvmfIa32
# build ovmf-ia32 with secure boot
build ${OVMF_SB_FLAGS} -a IA32 -p OvmfPkg/OvmfPkgIa32.dsc
cp Build/OvmfIa32/*/FV/OVMF_CODE.fd ovmf-ia32/OVMF_CODE.secboot.fd

%install

# shell
install -pm0644 -D Build/Shell/RELEASE_%TOOL_CHAIN_TAG/X64/ShellPkg/Application/Shell/Shell/OUTPUT/Shell.efi \
	%buildroot%_libdir/efi/shell.efi

#install OVMF
mkdir -p %buildroot%_datadir/edk2
cp -a OVMF %buildroot%_datadir/
ln -r -s %buildroot%_datadir/OVMF %buildroot%_datadir/edk2/ovmf

cp -a ovmf-ia32 %buildroot%_datadir/edk2


%files ovmf
#%doc FatBinPkg/License.txt
%doc OvmfPkg/License.txt
%_datadir/OVMF
%dir %_datadir/edk2
%_datadir/edk2/ovmf

%files ovmf-ia32
%doc OvmfPkg/License.txt
%_datadir/edk2/ovmf-ia32

%files efi-shell
%_libdir/efi/shell.efi

%changelog
* Sat May 16 2020 Alexey Shabalin <shaba@altlinux.org> 20200229-alt1
- edk2-stable202002 (Fixes: CVE-2019-14575, CVE-2019-14559, CVE-2019-14587, CVE-2019-14558, CVE-2019-14586, CVE-2019-14563)

* Wed Dec 18 2019 Alexey Shabalin <shaba@altlinux.org> 20191122-alt1
- edk2-stable201911 (Fixes: CVE-2019-14553, CVE-2019-13224, CVE-2019-13225)

* Wed Jul 31 2019 Alexey Shabalin <shaba@altlinux.org> 20190501-alt2
- build ovmf and efi-shell only

* Wed Jun 19 2019 Alexey Shabalin <shaba@altlinux.org> 20190501-alt1
- edk2-stable201905 (Fixes: CVE-2018-12182)

* Tue Apr 02 2019 Alexey Shabalin <shaba@altlinux.org> 20190308-alt1
- edk2-stable201903 (Fixes: CVE-2018-12178, CVE-2018-12180, CVE-2018-12181, CVE-2018-3630)

* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 20181113-alt1
- edk2-stable201811

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 20170720-alt3%ubt
- snapshot of UDK2017 branch

* Mon Sep 18 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 20170720-alt2%ubt
- added efi-shell subpackage

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 20170720-alt1%ubt
- snapshot of UDK2017 branch

* Thu Jan 12 2017 Alexey Shabalin <shaba@altlinux.ru> 20161227-alt1
- UDK2017 branch

* Wed May 25 2016 Alexey Shabalin <shaba@altlinux.ru> 20160518-alt1
- master snapshot 855743f7177459bea95798e59b6b18dab867710c

* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 20151225-alt1.svn19549
- build from branche UDK2015

* Wed Jun 24 2015 Alexey Shabalin <shaba@altlinux.ru> 20150616svn17642-alt2
- buils ovmf as noarch

* Wed Jun 17 2015 Alexey Shabalin <shaba@altlinux.ru> 20150616svn17642-alt1
- svn snapshot r17642
- add ovmf package

* Mon Oct 06 2014 Alexey Shabalin <shaba@altlinux.ru> 20140722svn2674-alt1
- svn snapshot r2674

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1.svn2594
- initial build
