%define _unpackaged_files_terminate_build 1

%define rname kreport

%define kreport_sover 4
%define libkreport libkreport3%kreport_sover

Name:    kf5-kreport
Summary: Framework for creation and generation of reports
Version: 3.2.0
Release: alt3
Group:   Development/KDE and QT
License: LGPLv2+
Url:     https://community.kde.org/KReport

%K5init

# git://anongit.kde.org/kreport.git
Source: %name-%version.tar
# FC
Patch1: kf5-kreport-3.0.2-fedora-pkgconfig.patch
# SuSE
Patch10: Fix-kexi-build-with-GCC-10.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel qt5-declarative-devel
#qt5-webkit-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kguiaddons-devel kf5-kwidgetsaddons-devel
#BuildRequires: kde5-marble-devel
BuildRequires: kf5-kproperty-devel
BuildRequires: python cmake pkgconfig

%description
A framework for creation and generation of reports in multiple formats.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Summary: Developer files for %name
Group: Development/KDE and QT
%description devel
This package contains libraries and header files for
developing applications that use %name.

%package -n %libkreport
Group: System/Libraries
Summary: %name library
Requires: %name-common = %EVR
%description -n %libkreport
%name library

%prep
%setup
%patch1 -p1
%patch10 -p1

%build
%K5build \
	-DINCLUDE_INSTALL_DIR:PATH=%_K5inc

%install
%K5install

%files common

%files
%dir %_K5plug/kreport3/
%_K5plug/kreport3/org.kde.kreport.*.so
%_datadir/kservicetypes5/kreport_elementplugin.desktop
# .rcc icon resources
%_datadir/kreport3/

%files devel
%_K5inc/KReport3/
%_K5link/lib*.so
%_libdir/cmake/KReport3/
%_pkgconfigdir/KReport3.pc
%_K5archdata/mkspecs/modules/qt_KReport3.pri

%files -n %libkreport
%doc COPYING.LIB
%_K5lib/libKReport3.so.%kreport_sover
%_K5lib/libKReport3.so.*

%changelog
* Thu Aug 27 2020 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt3
- add fix to build kexi with new gcc

* Mon Jul 08 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.0-alt2
- Spec and build dependencies cleanup.

* Fri Jun 21 2019 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt1
- new version

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt3
- NMU: remove %%ubt from release

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.0-alt2
- Rebuilt for aarch64.

* Wed Mar 21 2018 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1
- new version

* Thu Nov 16 2017 Sergey V Turchin <zerg@altlinux.org> 3.0.2-alt2
- split library to separate package

* Thu Aug 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2-alt1
- Initial build for ALT.

* Fri Aug 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-4
- move rcc icon resource to main/runtime pkg, runtime complains if missing

* Sat Aug 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-3
- add/tighten dep on kproperty

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-2
- fix/sanitize pkgconfig deps

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-1
- 3.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-0.1
- first try
