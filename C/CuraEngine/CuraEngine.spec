# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: CuraEngine
Epoch: 1
Version: 4.4.1
Release: alt1

Summary: Engine for processing 3D models into G-code instructions for 3D printers
License: AGPL-3.0
Group: Engineering
Url: https://github.com/Ultimaker/CuraEngine

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

# The cmake stuff would attempt to git clone this:
# TODO package on it's own
%define stb_commit e6afb9cbae4064da8c3e69af3ff5c4629579c1d2
# https://github.com/nothings/stb/archive/%{stb_commit}.tar.gz
Source1: stb.tar

Patch1: %name-rpath.patch
Patch2: %name-static-libstdcpp.patch

# A weird part of cmake stuff that does not work at all, not present in upstream master
Patch3: fix-stb-PATH.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: protobuf-compiler
BuildRequires: pkgconfig(protobuf)
BuildRequires: libpolyclipping-devel
BuildRequires: pkgconfig(RapidJSON)
BuildRequires: libArcus-devel = %version

%description
CuraEngine is a powerful, fast and robust engine for processing 3D
models into 3D printing instruction for Ultimaker and other GCode
based 3D printers. It is part of the larger open source project
called "Cura".

The CuraEngine is a C++ console application for 3D printing GCode
generation. It has been made as a better and faster alternative
to the old Skeinforge engine.

%prep
%setup
tar -xf %SOURCE1

%patch1 -p1
%patch2 -p1
%patch3 -p1

# bundled libraries
rm -rf libs

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF \
       -DCURA_ENGINE_VERSION:STRING=%version \
       -DUSE_SYSTEM_LIBS:BOOL=ON \
       -DCMAKE_CXX_FLAGS_RELEASE_INIT:STRING="%optflags -fPIC" \
       -DStb_INCLUDE_DIRS:PATH=./stb

%cmake_build

%install
%cmakeinstall_std

%check
# Smoke test
%buildroot%_bindir/%name help

%files
%_bindir/*
%doc LICENSE README.md

%changelog
* Sat Jan 25 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt1
- New version 4.4.1

* Fri Dec 21 2018 Anton Midyukov <antohami@altlinux.org> 1:3.6.0-alt1
- New version 3.6.0

* Tue Oct 30 2018 Anton Midyukov <antohami@altlinux.org> 1:3.5.1-alt1
- New version 3.5.1

* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 1:3.4.1-alt1
- New version 3.4.1

* Mon May 21 2018 Anton Midyukov <antohami@altlinux.org> 1:3.3.0-alt1.S1.1
- Rebuilt with protobuf-compiler 3.5.2

* Sun May 06 2018 Anton Midyukov <antohami@altlinux.org> 1:3.3.0-alt1.S1
- New version 3.3.0
- Make sure Fedora CXXFLAGS are used, also -fPIC
- Use new USE_SYSTEM_LIBS option instead of patch+sed

* Sat Feb 24 2018 Anton Midyukov <antohami@altlinux.org> 1:3.2.1-alt1.S1
- New version 3.2.1

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt1
- New version 3.0.3

* Wed Dec 13 2017 Anton Midyukov <antohami@altlinux.org> 1:2.4.0-alt1
- New version 2.4.0

* Sat Nov 25 2017 Igor Vlasenko <viy at altlinux.ru> 15.04-alt2_5
- rebuild with libpolyclipping

* Thu Mar 16 2017 Igor Vlasenko <viy at altlinux.ru> 15.04-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy at altlinux.ru> 15.04-alt1_2
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy at altlinux.ru> 14.12.1-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy at altlinux.ru> 14.03-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy at altlinux.ru> 14.03-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy at altlinux.ru> 14.03-alt1_1
- update to new release by fcimport

* Sat Jun 07 2014 Igor Vlasenko <viy at altlinux.ru> 14.01-alt1_1
- by request of Dmitry Derjavin <dd@>
