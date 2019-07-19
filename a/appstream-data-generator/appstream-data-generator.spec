%define _unpackaged_files_terminate_build 1

# Use current date as version

Name:    appstream-data-generator
Version: 20190718
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
* Thu Jul 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20190718-alt1
- Improved icons processing.
- Converted icons now should keep transparency.
- Added option to keep processing appdata even if icons weren't found.

* Tue Jul 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20190716-alt1
- Fixed processing symlinks when looking for icons.

* Fri Jul 12 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20190712-alt2
- Improved processing of options "additionaldesktopnames", "additionalpackages"
  and "skiplanguageslist."

* Fri Jul 12 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20190712-alt1
- Updated option descriptions in help message (Closes: #37021).
- Added options to configure generation of
  metadata_license and project_license tags 
  in appdata generated from desktop files (Closes: #37022).
- Added options to skip or exclusively process specified
  desktop files if desktop files convertion is enabled.

* Wed Jul 10 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20190710-alt1
- Added option for processing desktop files
  and converting them into appdata.xml files (Closes: #36994).

* Wed Jul 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20190703-alt1
- Initial build for ALT
