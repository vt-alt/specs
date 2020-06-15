# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global with_check 1
%add_python3_compile_include %_libexecdir/cura

Name: cura
Epoch: 1
Version: 4.6.1
Release: alt1
Summary: 3D printer control software
License: LGPLv3+

Group: Engineering
Url: https://github.com/Ultimaker/Cura
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

# OpenSUSE path
# PATCH-FIX-OPENSUSE disable-code-style-check.patch code style is no distro buisiness
Patch1:         disable-code-style-check.patch
# PATCH-FIX-OPENSUSE fix-runtime.patch
Patch2:         fix-runtime.patch
# PATCH-FIX-OPENSUSE fix-crash-on-start.patch
Patch3:         fix-crash-on-start.patch
# PATCH-FIX-OPENSUSE -- avoid bad UI layout and crash in preview
Patch4:         0001-Avoid-crash-caused-by-KDE-qqc2-desktop-style.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: python3-devel
BuildRequires: Uranium >= %version
# Tests
%if 0%{?with_check}
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pip
BuildRequires: python3-module-savitar
BuildRequires: python3-module-requests
%endif

%py3_requires serial zeroconf
Requires: python3-module-savitar = %version
Requires: Uranium = %version
Requires: qt5-quickcontrols
Requires: qt5-quickcontrols2
Requires: qt5-graphicaleffects
Requires: CuraEngine = %epoch:%version
Requires: cura-fdm-materials = %version
Requires: 3dprinter-udev-rules


%description
Cura is a project which aims to be an single software solution for 3D printing.
While it is developed to be used with the Ultimaker 3D printer, it can be used
with other RepRap based designs.

Cura prepares your model for 3D printing. For novices, it makes it easy to get
great results. For experts, there are over 200 settings to adjust to your
needs. As it's open source, our community helps enrich it even more.

# see: https://github.com/Ultimaker/Cura/issues/5142
%define cura_cloud_api_root https://api.ultimaker.com
%define cura_cloud_api_version 1
%define cura_cloud_account_api_root https://account.ultimaker.com

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Wrong end of line encoding
dos2unix docs/How_to_use_the_flame_graph_profiler.md

# Wrong shebang
%__subst '1s=^#!%_bindir/\(python\|env python\)3*=#!%__python3=' cura_app.py

%build
%cmake -DCURA_VERSION:STRING=%version \
       -DCURA_BUILDTYPE=RPM \
       -DCURA_CLOUD_API_ROOT:STRING=%cura_cloud_api_root \
       -DCURA_CLOUD_API_VERSION:STRING=%cura_cloud_api_version \
       -DCURA_CLOUD_ACCOUNT_API_ROOT:STRING=%cura_cloud_account_api_root \
       -DLIB_SUFFIX:STR=
%cmake_build

%install
%cmakeinstall_std

%find_lang cura fdmextruder.def.json fdmprinter.def.json --output=%name.lang

%check
%if 0%{?with_check}
python3 -m pip freeze
python3 -m pytest -v -k "not TestCollidesWithAreas"
%endif

desktop-file-validate %buildroot%_datadir/applications/%name.desktop

%files -f %name.lang
%doc LICENSE README.md
%python3_sitelibdir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/metainfo/%name.appdata.xml
%_iconsdir/hicolor/*/apps/%name-icon.png
%_datadir/mime/packages/%name.xml
%_bindir/%name
%_libexecdir/%name

%changelog
* Thu May 07 2020 Anton Midyukov <antohami@altlinux.org> 1:4.6.1-alt1
- New version 4.6.1

* Tue Mar 24 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt2
- Avoid crash caused by KDE qqc2 desktop style

* Sun Jan 26 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt1.1
- Fix requires

* Sat Jan 25 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt1
- New version 4.4.1

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.6.0-alt2.1
- NMU: remove rpm-build-ubt from BR:

* Fri Apr 19 2019 Anton Midyukov <antohami@altlinux.org> 1:3.6.0-alt1.1
- Not rebuild locales files

* Fri Dec 21 2018 Anton Midyukov <antohami@altlinux.org> 1:3.6.0-alt1
- New version 3.6.0

* Wed Oct 31 2018 Anton Midyukov <antohami@altlinux.org> 1:3.5.1-alt1
- New version 3.5.1

* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 1:3.4.1-alt1
- New version 3.4.1

* Mon May 07 2018 Anton Midyukov <antohami@altlinux.org> 1:3.3.0-alt1.S1
- New version 3.3.0

* Sat Feb 24 2018 Anton Midyukov <antohami@altlinux.org> 1:3.2.1-alt1.S1
- New version 3.2.1
- Disable tests

* Sat Jan 06 2018 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt2
- Fix fail start with nvidia proprietary driver.

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt1
- New version 3.0.3

* Wed Dec 13 2017 Anton Midyukov <antohami@altlinux.org> 1:2.4.0-alt1
- New version 2.4.0

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 15.04.4-alt3
- NMU: sync with fc cura-15.04.4-4

* Thu Mar 17 2016 Andrey Cherepanov <cas@altlinux.org> 15.04.4-alt2
- Initial build in Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 15.04.4-alt1_2
- update to new release by fcimport

* Thu Nov 26 2015 Igor Vlasenko <viy@altlinux.ru> 15.02.1-alt1_4
- new version

