Name: udisks2-qt5
Version: 5.0.6
Release: alt1
Summary: Qt5 binding for udisks2
License: LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/udisks2-qt5
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
BuildRequires: gcc-c++ qt5-base-devel

%description
This package provides a Qt5 binding for udisks2.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name
This package provides a Qt5 binding for udisks2.

%package devel
Summary: Development package for %name
Group: Development/KDE and QT
Requires: qt5-base-devel

%description devel
Header files and libraries for %name.

%prep
%setup
subst 's|/lib|/%_lib|' udisks2.pro

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%_prefix \
    VERSION=%version \
    LIB_INSTALL_DIR=%_libdir \
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n lib%name
%doc CHANGELOG.md
%_libdir/lib%name.so.5*

%files devel
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Wed Jul 07 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.6-alt1
- New version (5.0.6).

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.5-alt1
- New version (5.0.5) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.4-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
