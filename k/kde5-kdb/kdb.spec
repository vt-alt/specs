%define rname kdb

%define sover 4
%define libkdb3 libkdb3%sover

Name: kde5-%rname
Version: 3.2.0
Release: alt3
%K5init altplace

Group: System/Libraries
Summary: Database connectivity and creation framework
Url: http://www.kde.org
License: LGPL-2.0-only

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Nov 01 2017 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libEGL-devel libGL-devel libpq-devel libqt5-core libqt5-gui libqt5-network libqt5-widgets libqt5-xml libsasl2-3 libssl-devel libstdc++-devel mariadb-client perl pkg-config python-base python-modules python-modules-compiler python3 python3-base python3-module-yieldfrom qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: appstream extra-cmake-modules git-core kf5-kcoreaddons-devel libicu-devel libmysqlclient-devel libmysqld-devel libsqlite3-devel postgresql-devel python-module-google python3-dev python3-module-zope qt5-wayland-devel rpm-build-ruby sqlite3
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-wayland-devel
BuildRequires: libicu-devel
BuildRequires: libmysqlclient-devel postgresql-devel sqlite3 libsqlite3-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: rpm-build-python3 python3(shlex)

%description
KDb is a database connectivity and creation framework, consisted of a general-purpose
C++ Qt library and set of plugins delivering support for various database vendors.

%package sql-3-postgres
Summary: MySQL driver %name
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %name-sql-driver
%description sql-3-postgres
MySQL driver for %name

%package sql-5-mysql
Summary: MySQL driver %name
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %name-sql-driver
%description sql-5-mysql
MySQL driver for %name

%package sql-7-sqlite
Summary: SQlite driver %name
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %name-sql-driver
%description sql-7-sqlite
SQlite driver for %name

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kf5-kcoreaddons-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkdb3
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkdb3
%name library


%prep
%setup -n %rname-%version

%build
export PATH=$PWD/bin:$PATH
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    -DPYTHON_EXECUTABLE=%__python3 \
    #

%install
%K5install

sed -i 's|[[:space:]]icu-lo||' %buildroot/%_pkgconfigdir/KDb3.pc
sed -i 's|[[:space:]]KF5CoreAddons||' %buildroot/%_pkgconfigdir/KDb3.pc

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files sql-7-sqlite
%_K5plug/kdb3/kdb_sqlitedriver.so
%_K5plug/kdb3/sqlite3/

%files sql-5-mysql
%_K5plug/kdb3/kdb_mysqldriver.so

%files sql-3-postgres
%_K5plug/kdb3/kdb_postgresqldriver.so

%files devel
%_K5bin/kdb3_sqlite3_dump
#%_K5inc/kdb_version.h
%_K5inc/KDb3/
%_K5link/lib*.so
%_K5lib/cmake/KDb3/
%_pkgconfigdir/KDb3.pc
%_K5archdata/mkspecs/modules/qt_KDb3.pri

%files -n %libkdb3
%_K5lib/libKDb3.so.*

%changelog
* Mon Mar 23 2020 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt3
- build with python3

* Tue Nov 19 2019 Ivan A. Melnikov <iv@altlinux.org> 3.2.0-alt2
- fix build with PostgreSQL 12 (upstream changes by
  Pino Toscano <pino at kde dot org>)

* Fri Jun 21 2019 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt1
- new version

* Thu Feb 07 2019 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt5
- build with libmysqlclient

* Wed Feb 06 2019 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt4
- build with libmariadb

* Fri Oct 26 2018 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt3
- rebuild with new icu

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt2
- fix build requires

* Fri Mar 23 2018 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1
- new version

* Wed Nov 01 2017 Sergey V Turchin <zerg@altlinux.org> 3.0.2-alt1
- initial build
