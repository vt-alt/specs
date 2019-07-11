%define _unpackaged_files_terminate_build 1

Name:    appstream-data-generator
Version: 20190710
Release: alt1
Summary: Collection of tools for generation of appstream-data
Group:   System/Configuration/Packaging
License: GPLv3+

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ cmake
BuildRequires: boost-complete

# /usr/bin/bsdtar
Requires: bsdtar
# /usr/bin/convert
Requires: ImageMagick-tools

%description
Collection of tools for generation of appstream-data

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*

%changelog
* Wed Jul 10 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20190710-alt1
- Added option for processing desktop files
  and converting them into appdata.xml files (Closes: #36994).

* Wed Jul 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20190703-alt1
- Initial build for ALT
