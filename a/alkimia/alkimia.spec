%define lib_name libalkimia5

Name:    alkimia
Version: 8.0.4
Release: alt1

Summary: Alkimia is the infrastructure for common storage and business logic that will be used by all financial applications in KDE
License: LGPLv2+
Group:	 Office
URL:     http://community.kde.org/Alkimia/libalkimia
# Download from https://download.kde.org/stable/alkimia/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: qt5-webkit-devel
BuildRequires: libgmp_cxx-devel
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-plasma-framework-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: mpir-devel
BuildRequires: doxygen

Requires: lib%name = %version-%release

%description
Alkimia is the infrastructure for common storage and business logic that
will be used by all financial applications in KDE. The target is to
share financial related information over application bounderies.

%package -n lib%name
Summary: A library with common classes and functionality used by finance applications for the KDE SC
Group:   System/Libraries

%description -n lib%name
libalkimia is a library with common classes and functionality used by
finance applications for the KDE SC. Currently it supports a common
class to represent monetary values with arbitrary precision.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: lib%name = %version-%release
Requires: mpir-devel

%description -n lib%name-devel
Headers and other files for develop with %name.

%prep
%setup -q

%build
%K5init no_altplace
%K5build -DCMAKE_SKIP_RPATH=1 \
         -DAPPDATA_INSTALL_DIR=%_datadir

%install
%K5install
%find_lang alkimia --all

%files -f alkimia.lang
%doc README.md
%_bindir/onlinequoteseditor*
%_K5qml/org/kde/alkimia
%_desktopdir/kf5/*.desktop
#_datadir/alkimia5
%_iconsdir/hicolor/*/apps/onlinequoteseditor*
%_datadir/metainfo/*.appdata.xml
%_K5data/plasma/plasmoids/org.wincak.foreigncurrencies2
%_K5srv/*.desktop
%_K5xdgconf/*.knsrc

%files -n lib%name
%_libdir/%lib_name.so.*

%files -n lib%name-devel
%dir %_includedir/alkimia
%_includedir/alkimia/*
%_K5link/%lib_name.so
%_pkgconfigdir/%lib_name.pc
%_libdir/cmake/LibAlkimia*

%changelog
* Wed Dec 23 2020 Andrey Cherepanov <cas@altlinux.org> 8.0.4-alt1
- New version.
- Rename source package to upstream name alkimia.

* Wed Jan 29 2020 Andrey Cherepanov <cas@altlinux.org> 8.0.3-alt1
- New version.

* Thu Oct 10 2019 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 8.0.1-alt1
- New version.

* Mon Apr 16 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt1
- New version.

* Mon Mar 19 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.1-alt1
- New version.

* Fri Feb 16 2018 Andrey Cherepanov <cas@altlinux.org> 7.0-alt1
- New version.

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1.1
- Rebuilt with gmp 5.0.5

* Thu Feb 09 2012 Andrey Cherepanov <cas@altlinux.org> 4.3.2-alt1
- New version 4.3.2

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- Initial build in Sisyphus

