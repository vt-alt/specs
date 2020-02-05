Name: cura-fdm-materials
Version: 4.4.1
Release: alt1
Summary: Cura FDM Material database
License: Public Domain
Group: Engineering
Url: https://github.com/Ultimaker/fdm_materials
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%description
Cura material files.

These files are needed to work with printers like Ultimaker 2+ and Ultimaker 3.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%dir %_datadir/cura
%dir %_datadir/cura/resources
%_datadir/cura/resources/materials

%changelog
* Sat Jan 25 2020 Anton Midyukov <antohami@altlinux.org> 4.4.1-alt1
- new version 4.4.1

* Fri Dec 21 2018 Anton Midyukov <antohami@altlinux.org> 3.6.0-alt1
- new version 3.6.0

* Tue Oct 30 2018 Anton Midyukov <antohami@altlinux.org> 3.5.1-alt1
- new version 3.5.1

* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt1
- new version 3.4.1

* Sun May 06 2018 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1
- new version 3.3.0

* Fri Feb 23 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1
- new version 3.2.1

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1
- New version 3.0.3

* Wed Nov 22 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for ALT Sisyphus.
