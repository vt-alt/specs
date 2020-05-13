%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
%define git 059a495

Name: spirv-headers
Version: 1.4.1
Release: alt0.1.g%{git}

Summary: machine-readable files for the SPIR-V Registry
Group: Development/C++
License: BSD

BuildArch: noarch

URL: https://github.com/KhronosGroup/SPIRV-Headers
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version-%git.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
This repository contains machine-readable files for the SPIR-V Registry. This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction set and the extended instruction sets.
* The XML registry file.
* A tool to build the headers from the JSON grammar.

%prep
%setup -n %name-%version-%git

%build
%_cmake
%cmake_build
%cmakeinstall_std

%files
%doc *.md example
%dir %_includedir/spirv
%_includedir/spirv/*

%changelog
* Thu Aug 29 2019 L.A. Kostis <lakostis@altlinux.ru> 1.4.1-alt0.1.g059a495
- Updated to GIT 059a495.

* Thu May 02 2019 L.A. Kostis <lakostis@altlinux.ru> 1.3.7-alt0.1.g2434b89
- Initial build for Sisyphus.
