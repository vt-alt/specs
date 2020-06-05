
# obsileted koffice version
%define koffice_ver 4:2.3.70

%define sover 3.2
%define libkexiguiutils libkexiguiutils%sover
%define libkformdesigner libkformdesigner%sover
%define libkexiundo libkexiundo%sover
%define libkexiformutils libkexiformutils%sover
%define libkexiutils libkexiutils%sover
%define libkexicore libkexicore%sover
%define libkexiextendedwidgets libkexiextendedwidgets%sover
%define libkexirelationsview libkexirelationsview%sover
%define libkeximain libkeximain%sover
%define libkexidataviewcommon libkexidataviewcommon%sover
%define libkeximigrate libkeximigrate%sover
%define libkexidatatable libkexidatatable%sover

Name: kexi
Version: 3.2.0
Release: alt4
%K5init no_altplace

Group: Databases
Summary: Visual database applications creator
Url: http://kexi-project.org/
License: GPLv2+ / LGPLv2+

Requires: kde5-kdb-sql-driver

Provides: calligra-kexi = %EVR
Obsoletes: calligra-kexi < %EVR
Provides: koffice-kexi = %koffice_ver
Obsoletes: koffice-kexi < %koffice_ver

Source: kexi-%version.tar
Patch1: alt-ftbfs.patch

# Automatically added by buildreq on Wed Nov 01 2017 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glib2-devel glibc-devel-static glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kproperty kf5-kreport kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libgpg-error libpq-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libssl-devel libstdc++-devel libxcbutil-keysyms mariadb-client perl pkg-config python-base python-modules python3 python3-base python3-module-yieldfrom qt5-base-common qt5-base-devel qt5-declarative-devel qt5-tools-devel rpm-build-python3 ruby ruby-stdlibs xset
#BuildRequires: appstream extra-cmake-modules git-core gtk-update-icon-cache icon-theme-breeze kde4-marble-devel kde5-kdb-devel kf5-karchive-devel kf5-kcrash-devel kf5-kguiaddons-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kparts-devel kf5-kproperty-devel kf5-kreport-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel libmysqlclient-devel libmysqld-devel postgresql-devel python-module-google python3-dev python3-module-zope qt5-tools-devel-static qt5-wayland-devel qt5-webkit-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: icon-theme-breeze
BuildRequires: extra-cmake-modules qt5-tools-devel-static qt5-wayland-devel
#BuildRequires: qt5-webkit-devel
BuildRequires: glib2-devel
BuildRequires: kde5-kdb-devel
BuildRequires: libmysqlclient-devel
# libmysqld-devel
BuildRequires: postgresql-devel
BuildRequires: kf5-karchive-devel kf5-kcrash-devel kf5-kguiaddons-devel kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-kparts-devel kf5-kproperty-devel kf5-kreport-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel

%description
Kexi is a visual database applications creator.
It can be used for creating database schemas, inserting data, performing queries,
and processing data. Forms can be created to provide a custom interface to your data.
All database objects - tables, queries and forms - are stored in the database,
making it easy to share data and design.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Header files and libraries needed for %name development
%description devel
Header files and libraries needed for %name development

%package -n %libkeximigrate
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkeximigrate
%name library

%package -n %libkexidatatable
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkexidatatable
%name library

%package -n %libkexidataviewcommon
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkexidataviewcommon
%name library

%package -n %libkeximain
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkeximain
%name library

%package -n %libkexirelationsview
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkexirelationsview
%name library

%package -n %libkexiextendedwidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkexiextendedwidgets
%name library

%package -n %libkexicore
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkexicore
%name library

%package -n %libkexiutils
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkexiutils
%name library

%package -n %libkexiformutils
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkexiformutils
%name library

%package -n %libkexiundo
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkexiundo
%name library

%package -n %libkformdesigner
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkformdesigner
%name library

%package -n %libkexiguiutils
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkexiguiutils
%name library

%prep
%setup
%patch1 -p1
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.hpp' -o -name '*.h' |
	xargs -r sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%K5build \
    -DRELEASE_BUILD=ON \
    #

%install
%K5install

# remove InitialPreference
for f in %buildroot/%_K5xdgapp/*.desktop ; do
    sed -i '/^InitialPreference=/d' $f
done

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc AUTHORS README*

%files
%_K5bin/kexi*
%_K5plug/kexi/
%_datadir/kexi/
%_K5xdgapp/*kexi*.desktop
%_iconsdir/hicolor/*/apps/kexi*.*

#%files devel
#%_K5link/lib*.so
#%_K5inc/kexi/
#%_K5inc/*.h

%files -n %libkexiguiutils
%_libdir/libkexiguiutils%sover.so.%sover
%_libdir/libkexiguiutils%sover.so.*
%files -n %libkformdesigner
%_libdir/libkformdesigner%sover.so.%sover
%_libdir/libkformdesigner%sover.so.*
%files -n %libkexiundo
%_libdir/libkexiundo%sover.so.%sover
%_libdir/libkexiundo%sover.so.*
%files -n %libkexiformutils
%_libdir/libkexiformutils%sover.so.%sover
%_libdir/libkexiformutils%sover.so.*
%files -n %libkexiutils
%_libdir/libkexiutils%sover.so.%sover
%_libdir/libkexiutils%sover.so.*
%files -n %libkexicore
%_libdir/libkexicore%sover.so.%sover
%_libdir/libkexicore%sover.so.*
%files -n %libkexiextendedwidgets
%_libdir/libkexiextendedwidgets%sover.so.%sover
%_libdir/libkexiextendedwidgets%sover.so.*
%files -n %libkexirelationsview
%_libdir/libkexirelationsview%sover.so.%sover
%_libdir/libkexirelationsview%sover.so.*
%files -n %libkeximain
%_libdir/libkeximain%sover.so.%sover
%_libdir/libkeximain%sover.so.*
%files -n %libkexidataviewcommon
%_libdir/libkexidataviewcommon%sover.so.%sover
%_libdir/libkexidataviewcommon%sover.so.*
%files -n %libkeximigrate
%_libdir/libkeximigrate%sover.so.%sover
%_libdir/libkeximigrate%sover.so.*
%files -n %libkexidatatable
%_libdir/libkexidatatable%sover.so.%sover
%_libdir/libkexidatatable%sover.so.*

%changelog
* Mon Jan 27 2020 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt4
- fix to build with new Qt

* Wed Sep 04 2019 Michael Shigorin <mike@altlinux.org> 3.2.0-alt3
- E2K: strip UTF-8 BOM for lcc < 1.24

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Fri Jun 21 2019 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt1
- new version

* Mon Dec 24 2018 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt2
- fix to build

* Fri Mar 23 2018 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1%ubt
- new version

* Tue Oct 31 2017 Sergey V Turchin <zerg@altlinux.org> 3.0.2-alt1%ubt
- initial build
