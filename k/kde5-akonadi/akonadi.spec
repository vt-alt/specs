%define rname akonadi

%def_enable tools

Name: kde5-%rname
Version: 19.08.2
Release: alt1
%K5init altplace

Group: Databases
Summary: An extensible cross-desktop storage service for PIM
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: %name-database tar bzip2

Source: %rname-%version.tar
Source10: mysql_install_db
Patch1: alt-find-exe.patch
Patch2: alt-mysql-conf.patch
Patch3: alt-mysql-paths.patch
Patch4: alt-mysqlcheck-detached.patch
Patch5: alt-own-mysql-install-db.patch
Patch6: alt-find-resources.patch
Patch7: alt-find-mysql-global-conf.patch

# Automatically added by buildreq on Mon Apr 25 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-designer libqt5-gui libqt5-network libqt5-printsupport libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms libxml2-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs shared-mime-info xml-utils
#BuildRequires: boost-devel-headers extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdesignerplugin-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libsqlite3-devel libxslt-devel python-module-google python3-dev qt5-quick1-devel qt5-tools-devel rpm-build-ruby xsltproc
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: boost-devel extra-cmake-modules qt5-declarative-devel qt5-tools-devel
BuildRequires: xsltproc xml-utils shared-mime-info
BuildRequires: libsqlite3-devel libxslt-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdesignerplugin-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel
BuildRequires: kf5-kcrash-devel

%description
An extensible cross-desktop storage service for PIM data and meta data providing
concurrent read, write, and query access.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kf5-filesystem
%description common
%name common package

%package -n qt5-sql-sqlite3
Summary: SQLite3 driver for Qt5 SQL classes
Group: System/Libraries
Provides: qt5-plugin-sql = 5.5
%description -n qt5-sql-sqlite3
SQLite3 driver for Qt's SQL classes (QSQLITE3)

%package database-1-sqlite
Group: Databases
Summary: %name Qt sqlite database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: qt5-sql-sqlite
Provides: %name-database = %EVR
Provides: %name-database-sqlite = %EVR
%description database-1-sqlite
%name Qt sqlite database

%package database-3-sqlite3
Group: Databases
Summary: %name sqlite database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: qt5-sql-sqlite3
Provides: %name-database = %EVR
Provides: %name-database-sqlite3 = %EVR
%description database-3-sqlite3
%name Akonadi sqlite database

%package database-5-postgresql
Group: Databases
Summary: %name postgresql database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: qt5-sql-postgresql postgresql /usr/bin/pg_dump /usr/bin/pg_restore
Provides: %name-database = %EVR
Provides: %name-database-postgresql = %EVR
%description database-5-postgresql
%name postgresql database

%package database-8-mysql
Group: Databases
Summary: %name mysql database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: qt5-sql-mysql mariadb-server mariadb-client
Provides: %name-database = %EVR
Provides: %name-database-mysql = %EVR
%description database-8-mysql
%name mysql database

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: boost-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5akonadiprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadiprivate
KF5 library

%package -n libkf5akonadiagentbase
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadiagentbase
KF5 library

%package -n libkf5akonadicore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadicore
KF5 library

%package -n libkf5akonadiwidgets
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadiwidgets
KF5 library

%package -n libkf5akonadixml
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadixml
KF5 library

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%K5build \
    -DMYSQLD_EXECUTABLE:FILEPATH=%_sbindir/mysqld \
    -DBUILD_TESTING=OFF \
    -DBUILD_TOOLS=%{?_enable_tools:ON}%{!?_enable_tools:OFF} \
    #
#    -DDATABASE_BACKEND=MYSQL \

%install
%K5install
%K5install_move data kdevappwizard

install -m 0755 %SOURCE10 %buildroot/%_bindir/akonadi5_mysql_install_db
mv %buildroot/%_K5xdgmime/akonadi{,5}-mime.xml

mkdir -p %buildroot/%_K5srv/akonadi/contact
mkdir -p %buildroot/%_K5lib/akonadi5/contact
mkdir -p %buildroot/%_K5plug/akonadi/contacts/plugins/

mkdir -p %buildroot/%_datadir/akonadi5/{agents,contact,plugins,accountwizard}

mkdir %buildroot/%_K5data/akonadi/
mkdir %buildroot/%_K5data/akonadi5/
for f in %buildroot/%_datadir/akonadi5/*.xs* ; do
    fname=`basename $f`
    dname=`dirname $f`
    ln -s `relative %_datadir/akonadi5/$fname %_K5data/akonadi/$fname` %buildroot/%_K5data/akonadi/$fname
    ln -s `relative %_datadir/akonadi5/$fname %_K5data/akonadi5/$fname` %buildroot/%_K5data/akonadi5/$fname
done

%find_lang %name --with-kde --all-name


%files
%_K5dbus_srv/org.freedesktop.Akonadi.Control.service
%_K5bin/akonadi_agent_launcher
%_K5bin/akonadi_agent_server
%_K5bin/akonadi_rds
%_K5bin/akonadi_control
%_K5bin/akonadictl
%_K5bin/akonadiserver
%_K5bin/akonadiselftest
%if_enabled tools
%_K5bin/akonadi2xml
%_K5bin/akonaditest
%_K5bin/akonadi_knut_resource
%_K5plug/akonadi/akonadi_test_searchplugin.so
%_datadir/akonadi5/agents/knutresource.desktop
%_K5data/akonadi_knut_resource/
%endif

%files -n qt5-sql-sqlite3
%_qt5_plugindir/sqldrivers/libqsqlite3.so

%files database-1-sqlite
%files database-3-sqlite3
%files database-5-postgresql
%files database-8-mysql
%config(noreplace) %_K5xdgconf/akonadi/mysql-*.conf
%_bindir/akonadi5_mysql_install_db

%files common -f %name.lang
%dir %_K5plug/akonadi/
%dir %_K5plug/akonadi/contacts/
%dir %_K5plug/akonadi/contacts/plugins/
%dir %_K5lib/akonadi5/
%dir %_K5lib/akonadi5/contact/
%dir %_K5xdgconf/akonadi/
%dir %_K5srv/akonadi/
%dir %_K5srv/akonadi/contact/
%dir %_K5data/akonadi/
%dir %_K5data/akonadi5/
%dir %_datadir/akonadi5/
%dir %_datadir/akonadi5/accountwizard/
%dir %_datadir/akonadi5/agents/
%dir %_datadir/akonadi5/contact/
%dir %_datadir/akonadi5/plugins/
#%config(noreplace) %_K5xdgconf/akonadi.*categories
%_datadir/qlogging-categories5/*.*categories
%_K5cfg/resourcebase.kcfg
%_K5xdgmime/akonadi5-mime.xml
%_K5icon/*/*/apps/*akonadi*.*

%files devel
%_K5bin/asapcat
%_K5plug/designer/akonadi5widgets.so
%_K5inc/akonadi_version.h
%_K5inc/Akonadi*/
%_K5inc/akonadi/
%_K5link/lib*.so
%_K5lib/cmake/KF5Akonadi/
%_K5dbus_iface/*.Akonadi.*.xml
%_K5archdata/mkspecs/modules/qt_Akonadi*.pri
%_datadir/akonadi5/*.xs*
%_K5data/akonadi/*.xs*
%_K5data/akonadi5/*.xs*
%_K5data/kdevappwizard/templates/*akonadi*

%files -n libkf5akonadiprivate
%_K5lib/libKF5AkonadiPrivate.so.5
%_K5lib/libKF5AkonadiPrivate.so.*
%files -n libkf5akonadiagentbase
%_K5lib/libKF5AkonadiAgentBase.so.5
%_K5lib/libKF5AkonadiAgentBase.so.*
%files -n libkf5akonadicore
%_K5lib/libKF5AkonadiCore.so.5
%_K5lib/libKF5AkonadiCore.so.*
%files -n libkf5akonadiwidgets
%_K5lib/libKF5AkonadiWidgets.so.5
%_K5lib/libKF5AkonadiWidgets.so.*

%if_enabled tools
%files -n libkf5akonadixml
%_K5lib/libKF5AkonadiXml.so.5
%_K5lib/libKF5AkonadiXml.so.*
%endif

%changelog
* Wed Oct 23 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Fri Aug 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Tue Jul 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Fri Jun 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue Apr 30 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Apr 11 2019 Sergey V Turchin <zerg@altlinux.org> 19.03.90-alt1
- new version

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Fri Feb 08 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Wed Jan 30 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.1-alt1
- new version

* Thu Jan 24 2019 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2
- rebuild

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Tue Jun 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Sat Jun 09 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt4%ubt
- fix initialize mysql database

* Fri Jun 08 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt3%ubt
- fix apply last fix

* Thu Jun 07 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- fix initialize mysql database

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.2-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Mon Jul 03 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt.1
- rebuild

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- new version

* Thu Jan 12 2017 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt2%ubt
- rebuild with new Qt

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Fri Aug 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Mon Apr 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- new version

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Thu Feb 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Mon Feb 08 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt2
- add fix for agents desktop-files reading encoding

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Dec 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Wed Sep 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt3
- not't search for resources in KDE4 place

* Tue Sep 01 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt2
- add plugins dir

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Aug 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.90-alt1
- new version

* Mon Aug 03 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.80-alt1
- initial build
