%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DCMAKE_INSTALL_LIBDIR=%_datadir
%define git 07f259e

Name: spirv-headers
Version: 1.5.4
Release: alt2.g%{git}
Epoch: 1

Summary: machine-readable files for the SPIR-V Registry
Group: Development/C++
License: BSD

BuildArch: noarch

URL: https://github.com/KhronosGroup/SPIRV-Headers
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
This repository contains machine-readable files for the SPIR-V Registry. This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction set and the extended instruction sets.
* The XML registry file.
* A tool to build the headers from the JSON grammar.

%prep
%setup -n %name-%version

%build
%_cmake
%cmake_build
%cmakeinstall_std

%files
%doc *.md example
%dir %_includedir/spirv
%dir %_datadir/cmake/SPIRV-Headers
%_includedir/spirv/*
%_datadir/cmake/SPIRV-Headers/*

%changelog
* Sun Jun 27 2021 L.A. Kostis <lakostis@altlinux.ru> 1:1.5.4-alt2.g07f259e
- Updated to GIT 07f259e (as required by vulkan SDK).

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 1:1.5.4-alt1.gbcf5521
- Update to GIT bcf5521 (as required by SPIRV-Tools).

* Mon Feb 15 2021 L.A. Kostis <lakostis@altlinux.ru> 1:1.5.4-alt1
- Update to 1.5.4.raytracing.fixed.

* Sun Feb 14 2021 Nazarov Denis <nenderus@altlinux.org> 1:1.5.3-alt0.3
- Rollback to 1.5.3-alt0.2 (ALT #39671)

* Fri Feb 05 2021 Nazarov Denis <nenderus@altlinux.org> 1.5.4-alt0.1
- Update to 1.5.4.raytracing.fixed

* Tue Sep 08 2020 L.A. Kostis <lakostis@altlinux.ru> 1.5.3-alt0.2
- Update to 1.5.3.reservations1.

* Thu Jun 04 2020 L.A. Kostis <lakostis@altlinux.ru> 1.5.3-alt0.1
- Updated to 1.5.3.
- Added cmake files.

* Thu Aug 29 2019 L.A. Kostis <lakostis@altlinux.ru> 1.4.1-alt0.1.g059a495
- Updated to GIT 059a495.

* Thu May 02 2019 L.A. Kostis <lakostis@altlinux.ru> 1.3.7-alt0.1.g2434b89
- Initial build for Sisyphus.
