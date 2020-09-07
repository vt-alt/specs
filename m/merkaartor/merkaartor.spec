%define _unpackaged_files_terminate_build 1

Name: merkaartor
Version: 0.18.4
Release: alt3

Summary: an OpenStreetMap editor
License: GPLv2
Group: Sciences/Geosciences
Url: https://github.com/openstreetmap/merkaartor

# https://github.com/openstreetmap/merkaartor.git
Source: %name-%version.tar
Patch1: %name-0.18.3-fedora-no-git-version.patch
Patch2: %name-%version-upstream-qt5-compat.patch

BuildRequires: boost-devel gcc-c++ glibc-devel-static
BuildRequires: libgdal-devel libproj-devel libexiv2-devel zlib-devel libsqlite3-devel
BuildRequires: qt5-base-devel qt5-svg-devel qt5-tools-devel
BuildRequires: qt5-webengine-devel
BuildRequires: libqtsingleapplication-qt5-devel

%description
Merkaartor is an openstreetmap mapping program.
Merkaartor focuses on providing a visually pleasing but performant
editing environment for free geographical data.

%prep
%setup
%patch1 -p1
%patch2 -p1

# remove bundled libraries
rm -rf 3rdparty

%build
%add_optflags -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H=1
%add_optflags -I%_includedir/qt5/QtSolutions

lrelease-qt5 Merkaartor.pro
qmake-qt5 \
	CONFIG+=release CONFIG+=force_debug_info \
	PREFIX=%_prefix \
	USEWEBENGINE=1 \
	SYSTEM_QTSA=1 \
	TRANSDIR_MERKAARTOR=%_datadir/%name/translations/ \
	-after QMAKE_CFLAGS+='%optflags' \
	-after QMAKE_CXXFLAGS+='%optflags' \
	Merkaartor.pro

%make_build

%install
%make_install INSTALL_ROOT=%buildroot LIB_SUFFIX=%_libsuff install

%files
%_bindir/merkaartor
%_datadir/%name/
%_libdir/%name/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png

%changelog
* Fri Sep 04 2020 Sergey V Turchin <zerg@altlinux.org> 0.18.4-alt3
- Fixed build with qt < 5.15.0.

* Fri Aug 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.18.4-alt2
- Fixed build with qt-5.15.0.

* Thu Jul 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.18.4-alt1
- Updated to upstream version 0.18.4.

* Wed Nov 06 2019 Grigory Ustinov <grenka@altlinux.org> 0.18.3-alt5
- NMU: Rebuild with gdal 3.0.1.

* Sun Oct 06 2019 Vladislav Zavjalov <slazav@altlinux.org> 0.18.3-alt4
- Fix build with libproj 6.2.0 (use DACCEPT_USE_OF_DEPRECATED_PROJ_API_H)

* Fri Mar 29 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.18.3-alt3
- Fixed build with new version of qt5-webkit.
- Rebuilt with system libraries instead of bundled ones.
- Rebuilt with debug info.

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 0.18.3-alt2
- Rebuild with libproj 5.2.0
- Fix build on aarch64

* Sun Nov 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.18.3-alt1.1
- NMU: Rebuild with gdal 2.2.2

* Thu Sep 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.18.3-alt1
- Updated to upstream version 0.18.3.

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.1-alt1.1
- Fixed build with glibc 2.16 & gcc 4.7

* Wed Aug 11 2010 Egor Glukhov <kaman@altlinux.org> 0.16.1-alt1
- 0.16.1

* Thu Aug 13 2009 Grigory Batalov <bga@altlinux.ru> 0.14-alt1
- New upstream release.

* Tue Apr 28 2009 Grigory Batalov <bga@altlinux.ru> 0.13.2-alt2
- Own directory with translations.

* Tue Apr 28 2009 Grigory Batalov <bga@altlinux.ru> 0.13.2-alt1
- New upstream release (OSM API 0.6).

* Thu Apr 23 2009 Grigory Batalov <bga@altlinux.ru> 0.13.1-alt1
- New upstream release.

* Tue Nov 11 2008 Grigory Batalov <bga@altlinux.ru> 0.0.13-alt0.r11862
- New SVN version.
- Translations included (thanks to Maks Vasilev <max@stranger-team.ru>).

* Tue May 27 2008 Grigory Batalov <bga@altlinux.ru> 0.0.11-alt0.r7914
- New SVN version.

* Fri Apr 25 2008 Grigory Batalov <bga@altlinux.ru> 0.0.10-alt1
- Build for ALT Linux.
