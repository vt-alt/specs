# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: kicad-footprints
Summary: Footprint Libraries for kicad (creation of electronic schematic diagrams)
Version: 5.1.4
Release: alt1
Source: %name-%version.tar
License: GPLv2+
Group: Engineering
Url: https://code.launchpad.net/kicad
# Source-url: https://github.com/KiCad/%name/archive/%version.tar.gz

Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch
BuildRequires(pre): cmake rpm-macros-cmake gcc-c++

Obsoletes: kicad-library

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set Footprint Libraries needed by kicad.

%description -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

%name содержит бибиотеки посадочных мест электронных компонентов
для kicad.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%dir %_datadir/kicad
%_datadir/kicad/modules/
%dir %_datadir/kicad/template
%_datadir/kicad/template/fp-lib-table

%changelog
* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 5.1.4-alt1
- new version (5.1.4) with rpmgs script

* Thu Apr 25 2019 Anton Midyukov <antohami@altlinux.org> 5.1.2-alt1
- new version 5.1.2

* Sat Mar 16 2019 Anton Midyukov <antohami@altlinux.org> 5.1.0-alt1
- new version 5.1.0

* Thu Jan 03 2019 Anton Midyukov <antohami@altlinux.org> 5.0.2-alt1
- new version 5.0.2

* Sun Nov 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.1-alt1
- new version 5.0.1

* Wed Jul 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt1.rc3
- Initial build for ALT Sisyphus
