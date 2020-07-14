Name: libump-mcom02
Version: 1.0
Release: alt2

Summary: Unified Memory Provider library for MCom-02 GPU
License: Apache-2.0
Group: System/Libraries
ExclusiveArch: armh

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%set_verify_elf_method no

%description
Unified Memory Provider (UMP) library for Mali GPU found in MCom-02 SoC

%package devel
Group:    Development/C
Summary:  Development files for libump-mcom02

%description devel
Development files for libump-mcom02

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/libUMP.so.*

%files devel
%_libdir/libUMP.so
%_pkgconfigdir/libUMP*
%_includedir/ump

%changelog
* Thu Jul 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt2
- removed irrelevant Url: tag

* Wed Oct 31 2018 RnD Center ELVEES <rnd_elvees@altlinux.org> 1.0-alt1
Initial build for ALT
