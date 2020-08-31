%define _unpackaged_files_terminate_build 1

%define rname kproperty

%define kproperty_sover 4
%define libkpropertycore libkpropertycore3%kproperty_sover
%define libkpropertywidgets libkpropertywidgets3%kproperty_sover

Name:    kf5-kproperty
Summary: Property editing framework with editor widget
Version: 3.2.0
Release: alt2
Group:   Development/KDE and QT
License: LGPLv2+
Url:     https://community.kde.org/KProperty

# git://anongit.kde.org/kproperty.git
Source: %name-%version.tar
Patch1: kf5-kproperty-3.0.2-fedora-pkgconfig.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kguiaddons-devel kf5-kwidgetsaddons-devel
BuildRequires: cmake pkgconfig

%description
A property editing framework with editor widget similar to what is
known from Qt Designer.

%package devel
Summary: Developer files for %name
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description devel
%{summary}.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Conflicts: kf5-kproperty < %EVR
%description common
%name common package

%package -n %libkpropertycore
Group: System/Libraries
Summary: %name library
Requires: %name-common = %EVR
%description -n %libkpropertycore
%name library

%package -n %libkpropertywidgets
Group: System/Libraries
Summary: %name library
Requires: %name-common = %EVR
%description -n %libkpropertywidgets
%name library

%prep
%setup
%patch1 -p1

%build
%K5build \
	-DINCLUDE_INSTALL_DIR:PATH=%_K5inc

%install
%K5install

%files common
%_datadir/kproperty3/

%files devel
%_K5inc/KPropertyCore3/
%_K5lib/cmake/KPropertyCore3/
%_K5lib/pkgconfig/KPropertyCore3.pc
%_K5inc/KPropertyWidgets3/
%_K5link/lib*.so
%_K5lib/cmake/KPropertyWidgets3/
%_K5lib/pkgconfig/KPropertyWidgets3.pc

%files -n %libkpropertycore
%_K5lib/libKPropertyCore3.so.%kproperty_sover
%_K5lib/libKPropertyCore3.so.*
%files -n %libkpropertywidgets
%_K5lib/libKPropertyWidgets3.so.%kproperty_sover
%_K5lib/libKPropertyWidgets3.so.*

%changelog
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

* Thu Aug 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2-alt1
- Initial build for ALT.

* Fri Aug 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-4
- move rcc icon resources to main/runtime pkg

* Sat Aug 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-3
- fix pkgconfig harder

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-2
- fix/sanitize pkgconfig deps

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-1
- 3.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Rex Dieter <rdieter@fedoraproject.org> -  3.0.1-1
- first try
