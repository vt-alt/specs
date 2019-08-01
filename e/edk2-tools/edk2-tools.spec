%define TOOL_CHAIN_TAG GCC49
%define openssl_ver 1.1.0j

# More subpackages to come once licensing issues are fixed
Name: edk2-tools
Version: 20190501
Release: alt2
Summary: EFI Development Kit II Tools

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: %name-%version.tar

Source2: openssl.tar
Source3: berkeley-softfloat-3.tar
Source4: Logo.bmp

Patch1: %name-%version.patch

License: BSD
Group: Emulators
Url: http://www.tianocore.org

ExclusiveArch:  %ix86 x86_64 %arm aarch64

BuildRequires: iasl nasm gcc-c++
BuildRequires: python3-devel python3-modules-sqlite3
BuildRequires: libuuid-devel
BuildRequires: bc

%description
This package provides tools that are needed to
build EFI executables and ROMs using the GNU tools.

%package python
Summary: EFI Development Kit II Tools
Group: Development/Python3
BuildArch: noarch

%description python
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.  You do not need to install this package;
you probably want to install edk2-tools only.

%package doc
Summary: Documentation for EFI Development Kit II Tools
Group: Development/Documentation
BuildArch: noarch

%description doc
This package documents the tools that are needed to
build EFI executables and ROMs using the GNU tools.

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
OVMF_FLAGS="${OVMF_FLAGS} -D TLS_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D HTTP_BOOT_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D NETWORK_IP6_ENABLE"
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

%install
# install BaseTools
mkdir -p %buildroot%_bindir \
         %buildroot%_datadir/edk2/Conf \
         %buildroot%_datadir/edk2/Scripts

pushd BaseTools
install --strip \
	Source/C/bin/* \
	%buildroot%_bindir

install \
	BinWrappers/PosixLike/LzmaF86Compress \
	%buildroot%_bindir

install \
	BuildEnv \
	%buildroot%_datadir/edk2

install \
	Conf/*.template \
	%buildroot%_datadir/edk2/Conf

install \
	Scripts/GccBase.lds \
	%buildroot%_datadir/edk2/Scripts

cp -R Source/Python %buildroot%_datadir/edk2/Python

find %buildroot%_datadir/edk2/Python -name "*.pyd" | xargs rm -f

for i in BPDG Ecc GenDepex GenFds GenPatchPcdTable PatchPcdValue TargetTool Trim UPT; do
  echo '#!/bin/sh
export PYTHONPATH=%_datadir/edk2/Python
exec python3 '%_datadir/edk2/Python/$i/$i.py' "$@"' > %buildroot%_bindir/$i
  chmod +x %buildroot%_bindir/$i
done

popd

%files
%_bindir/Brotli
%_bindir/DevicePath
%_bindir/EfiRom
%_bindir/GenCrc32
%_bindir/GenFfs
%_bindir/GenFv
%_bindir/GenFw
%_bindir/GenSec
%_bindir/LzmaCompress
%_bindir/LzmaF86Compress
%_bindir/Split
%_bindir/TianoCompress
%_bindir/VfrCompile
%_bindir/VolInfo
%_datadir/edk2/BuildEnv
%_datadir/edk2/Conf
%_datadir/edk2/Scripts

#%files tools-python
#%_bindir/BPDG
#%_bindir/Ecc
#%_bindir/GenDepex
#%_bindir/GenFds
#%_bindir/GenPatchPcdTable
#%_bindir/PatchPcdValue
#%_bindir/TargetTool
#%_bindir/Trim
#%_bindir/UPT
#%_datadir/edk2/Python/

%files doc
%doc BaseTools/UserManuals/*.rtf

%changelog
* Wed Jul 31 2019 Alexey Shabalin <shaba@altlinux.org> 20190501-alt2
- build as edk2-tools package

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
