%define qIF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define qIF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define qIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define qIF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%define my_gcc_ver 5
%qIF_ver_gteq %ubt_id M90
%define my_gcc_ver 0
%endif

%define binutils_ver %{get_version binutils}
%define _keep_libtool_files 1
#define _optlevel s
%def_disable bootstrap
%def_disable debug
%def_disable static_thread
%def_enable shared_thread
%def_enable docs
%def_enable sql_pgsql
%def_enable sql_odbc
%def_enable sql_sqlite2
%def_enable sql_ibase
%def_disable sql_tds
%def_enable gtkstyle
%def_enable glib
%def_enable versioning_hack

%define platform linux-g++
%define graphicssystem raster
%ifarch %arm
%define opengl_type es2
%else
%define opengl_type desktop
%endif

# Versions
%define rname	qt
%define major	4
%define minor	8
%define bugfix	7
%define beta	%nil
%define rlz alt19

Name: %rname%major
Version: %major.%minor.%bugfix
Release: %rlz

%define qtdir	%_libdir/%name
%add_findprov_lib_path	%qtdir/lib

Group: System/Libraries
Summary: Shared library for the Qt%major GUI toolkit
Url: http://qt-project.org/
License: GPLv3 / LGPLv2.1

Requires: lib%name
Requires: %name-sql
Requires: %name-assistant
Requires: %name-dbus

Source0: qt-everywhere-opensource-src-%version%beta.tar
Source1: qt4-compat-map
Source2: qt4-compat-lds
Source3: rpmmacros
#
Source8: qtX-README.ALT
#
Source21: qt4-assistant.desktop
Source22: qt4-designer.desktop
Source23: qt4-linguist.desktop
Source24: qt4-qtconfig.desktop
Source25: qt4-qtdemo.desktop

Source101: %rname.16.png
Source102: %rname.32.png
Source103: %rname.48.png
Source104: %rname.64.png

# upstream
# security
# KDE-QT
Patch101: 0180-window-role.diff
Patch102: 0188-fix-moc-parser-same-name-header.diff
Patch103: 0191-listview-alternate-row-colors.diff
Patch104: 0195-compositing-properties.diff
Patch105: 0225-invalidate-tabbar-geometry-on-refresh.patch
# FC
Patch200: qt-aarch64.patch
Patch201: qt-everywhere-opensource-src-4.8.5-QTBUG-22829.patch
Patch202: qt-4.0.1-sans-mono.patch
Patch203: qt-everywhere-opensource-src-4.6.2-cups.patch
Patch204: qt-everywhere-opensource-src-4.6.3-glib_eventloop_nullcheck.patch
Patch205: qt-x11-opensource-src-4.5.1-enable_ft_lcdfilter.patch
Patch206: qt-everywhere-opensource-src-4.8.3-qdbusconnection_no_debug.patch
Patch207: qt-everywhere-opensource-src-4.8.1-icu_no_debug.patch
Patch208: qt-everywhere-opensource-src-4.8.6-systemtrayicon.patch
Patch209: qt-everywhere-opensource-src-4.8.5-QTBUG-21900.patch
Patch210: qt-everywhere-opensource-src-4.8.0-QTBUG-22037.patch
Patch211: qt-everywhere-opensource-src-4.8.2--assistant-crash.patch
Patch212: qt-everywhere-opensource-src-4.8.0-tp-qtreeview-kpackagekit-crash.patch
Patch213: qt-everywhere-opensource-src-4.8.3-no_Werror.patch
Patch214: qt-everywhere-opensource-src-4.8.5-QTBUG-4862.patch
Patch215: qt-everywhere-opensource-src-4.8.5-qt_plugin_path.patch
Patch216: qt-everywhere-opensource-src-4.8.6-QTBUG-34614.patch
Patch217: qt-everywhere-opensource-src-4.8.5-QTBUG-35459.patch
Patch218: qt-everywhere-opensource-src-4.8.7-alsa-1.1.patch
Patch219: qt-everywhere-opensource-src-4.8.7-gcc6.patch
# Debian
Patch301: CVE-2018-15518.patch
Patch302: CVE-2018-19869.patch
Patch303: CVE-2018-19870.patch
Patch304: CVE-2018-19871.patch
Patch305: CVE-2018-19872.patch
Patch306: CVE-2018-19873.patch
# ALT
Patch501: qt-4.8.5-alt-honor-SUSv3-locales.patch
Patch502: qt-4.7.2-alt-ca-certificates-path.patch
Patch503: qt-4.7.3-alt-qt-config-add-webkit.patch
Patch504: qt-4.7.0-alt-fix-gl-loading.patch
Patch505: qt-4.0.1-alt-iso_c_extension.patch
Patch506: qt-4.8.7-alt-kde-breeze.patch
Patch507: qt-4.8.6-alt-disable-gstreamer.patch
Patch508: qt-4.7.4-alt-buildkey.patch
Patch509: qt-4.7.0-alt-qtconfig_add_translator.patch
Patch510: qt-4.8.0-alt-ldflags.patch
Patch511: qt-4.3.2-alt-checkbox-indicator-plastique.patch
Patch512: qt-4.3.4-alt-uitools-shared.patch
Patch513: qt-4.8.6-alt-fix-ssl-loading.patch
Patch514: qt-4.8.5-alt-fix-resolv-loading.patch
Patch515: qt-4.6.1-alt-xmlpatterns-fexceptions.patch
Patch516: qt-4.7.1-alt-sql-ibase-firebird.patch
Patch517: alt-sql-mysql.patch
# SuSE
Patch701: handle-tga-files-properly.diff
Patch702: build-qvfb-tool.diff
Patch703: libqt4-libtool-nodate.diff
Patch704: qfatal-noreturn.diff
Patch705: fix-build-icu59.patch
#
Patch706: qt-never-strip.diff
Patch707: rcc-stable-dirlisting.diff
Patch708: no-ssl3.patch
Patch709: qt4-openssl-1.1.0pre-3.patch
Patch710: qt-everywhere-opensource-src-4.8.7-openssl.patch
# fixes for LibreOffice-kde QTBUG 37380,34614,38585
Patch800: glib-honor-ExcludeSocketNotifiers-flag.diff
Patch801: l-qclipboard_delay.patch
# Sergey A. Sukiyazov <sergey.sukiyazov NEAR gmail.com>
Patch9100: 9100-qt-core-fix-iconvcodec.patch
#
Patch9102: 9102-qt-gui-menubar_activate.patch
Patch9103: 9103-qt-gui-fix_shortcuts.patch
Patch9104: 9104-qt-gui-fix_loss_mouse_button_release_event.patch
Patch9105: 9105-qt-qt3support-menubar_activate.patch
Patch9106: 9107-qt-webkit-fix_graphicscontextqt.patch


# Automatically added by buildreq on Thu Apr 07 2011 (-bi)
# optimized out: alternatives elfutils fontconfig fontconfig-devel glib2-devel gstreamer-devel libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXv-devel libatk-devel libcairo-devel libcom_err-devel libdbus-devel libfreetype-devel libgdk-pixbuf-devel libgio-devel libgst-plugins libkrb5-devel libpango-devel libpng-devel libpq-devel libqt4-devel libqt4-sql-sqlite libssl-devel libstdc++-devel libtiff-devel libunixODBC-devel libxml2-devel pkg-config python-base ruby xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: firebird-devel gcc-c++ glibc-devel-static gst-plugins-devel libalsa-devel libcups-devel libfreetds-devel libgtk+2-devel libjpeg-devel libmng-devel libmysqlclient-devel libpulseaudio-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libsqlite-devel libsqlite3-devel makedepend phonon-devel postgresql-devel rpm-build-ruby
%if "%my_gcc_ver" == "0"
BuildRequires: gcc-c++
%else
%set_gcc_version %my_gcc_ver
BuildRequires: gcc%{my_gcc_ver}-c++
%endif
BuildRequires(pre): rpm-build-ubt
BuildRequires: libfreetype-devel pkg-config rpm-utils rpm-macros-alternatives browser-plugins-npapi-devel
BuildRequires: libcups-devel libalsa-devel
BuildRequires: libstdc++-devel libcom_err-devel libicu-devel libffi-devel
BuildRequires: libjpeg-devel libmng-devel libpng-devel zlib-devel libtiff-devel
BuildRequires: libxml2-devel libxslt-devel libreadline-devel libpam0-devel
BuildRequires: libmysqlclient-devel libsqlite3-devel
BuildRequires: bison pkg-config
BuildRequires: fontconfig-devel libssl-devel libkrb5-devel libdbus-devel
BuildRequires: libatk-devel libcairo-devel libgdk-pixbuf-devel libgio-devel libpango-devel
BuildRequires: libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXcursor-devel libXext-devel
%if "%opengl_type" == "es2" || "%opengl_type" == "es1"
BuildRequires: libGLES-devel
%endif
BuildRequires: libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXv-devel
BuildRequires: xorg-proto-devel libXtst-devel
%{?_enable_sql_tds:BuildRequires: libfreetds-devel}
%{?_enable_sql_pgsql:BuildRequires: postgresql-devel postgresql-devel-static}
%{?_enable_sql_ibase:BuildRequires: firebird-devel}
%{?_enable_gtkstyle:BuildRequires: libgtk+2-devel}
%{?_enable_glib:BuildRequires: glib2-devel}
%{?_enable_sql_sqlite2:BuildRequires: libsqlite-devel}
%{?_enable_sql_odbc:BuildRequires: libunixODBC-devel}


%description
Qt is a GUI software toolkit. Qt simplifies the task of writing and maintaining
GUI (graphical user interface) applications for the X Windows system.
It has everything you need to create professional GUI applications.
And it enables you to create them quickly.
Qt is multi-platform toolkit written in C++ and is fully object-oriented.
This package contains the shared library needed to run Qt%major applications, as
well as the README files for Qt.

##############################################
%package common
Summary: Common package for Qt%major
Group: System/Libraries
Requires: common-licenses
%description common
Common package for Qt%major

##############################################
%package -n lib%name
BuildArch: noarch
Summary: Shared library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: lib%name-core
Requires: lib%name-gui
Requires: lib%name-network
Requires: lib%name-opengl
Requires: lib%name-sql
Requires: lib%name-xml
Requires: lib%name-qt3support
Requires: lib%name-svg
Requires: lib%name-script
Requires: lib%name-designer
Requires: lib%name-uitools
Requires: lib%name-xmlpatterns
Requires: lib%name-multimedia
Requires: lib%name-help
Requires: lib%name-declarative
Requires: lib%name-clucene
Requires: lib%name-dbus
Provides: lib%name-x11 = %version-%release
Provides: %name-x11 = %version-%release
Provides: qt-x11 = %version-%release
Provides: qt = %version-%release

%description -n lib%name
Qt is a GUI software toolkit. Qt simplifies the task of writing and maintaining
GUI (graphical user interface) applications for X Windows System.
Qt is written in C++ and is fully object-oriented. It has everything you need
to create professional GUI applications. And it enables you to create them
quickly.

Qt is a multi-platform toolkit. When developing software with Qt, you can run
it on the X Window System (Unix/X11) or Microsoft Windows NT and Windows 95/98
or framebuffer devices.
Simply recompile your source code on the platform you want.

This package contains the shared library needed to run Qt%major applications, as
well as the README files for Qt.

##############################################
%package -n lib%{name}-qt3support
Summary: Qt3 support library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-qt3support
Qt3 support library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-core
Summary: Core library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
Requires: glibc-gconv-modules
%description -n lib%{name}-core
Core library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-gui
Summary: GUI support library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
Provides: libqtgui%major = %version-%release
Conflicts: yachat < 3.1.0 yapsi < 3.1.0
%description -n lib%{name}-gui
GUI support library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-dbus
Summary: DBus support library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-dbus
DBus support library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-network
Summary: Network support library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-network
Network support library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-uitools
Summary: Designer UI tools library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-uitools
Designer UI tools library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-svg
Summary: SVG support for the Qt%major GUI toolkit
Group: System/Libraries
%description -n lib%{name}-svg
Support for rendering Scalable Vector Graphics (SVG)
drawings and animations for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-opengl
Summary: OpenGL support library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-opengl
OpenGL support library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-sql
Summary: SQL support library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-sql
SQL support library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-test
Summary: Unit Testing Library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-test
Unit Testing Library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-designer
Summary: Libraries for the Qt%major Designer
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-designer
Libraries for the Qt%major Designer

##############################################
%package -n lib%{name}-xml
Summary: XML support library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-xml
XML support library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-script
Summary: Scripting support library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-script
Qt Script is based on the ECMAScript scripting language, as defined in
standard ECMA-262. Microsoft's JScript, and Netscape's JavaScript are
also based on the ECMAScript standard.

##############################################
%package -n lib%{name}-xmlpatterns
Summary: XmlPatterns library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-xmlpatterns
XmlPatterns library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-scripttools
Summary: ScriptTools library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-scripttools
ScriptTools library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-help
Summary: Help library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-help
Help library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-clucene
Summary: CLucene library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-clucene
CLucene library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-multimedia
Summary: Multimedia framework library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-multimedia
Multimedia framework library for the Qt%major GUI toolkit

##############################################
%package -n lib%{name}-declarative
Summary: Ddeclarative framework library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%{name}-declarative
Declarative framework library for the Qt%major GUI toolkit
Declarative module provides a declarative framework
for building highly dynamic, custom user interfaces

##############################################
%package devel
BuildArch: noarch
Group: System/Libraries
Summary: Meta-package for development with Qt%major GUI toolkit
Requires: lib%name-devel
Requires: %name-designer
Requires: %name-assistant
Requires: %name-qvfb
%if_enabled docs
Requires: %name-doc
%endif
%description devel
Meta-package for development with Qt%major GUI toolkit

##############################################
%package -n lib%name-devel
Summary: Header files and libraries for developing apps which will use Qt%major
Group: Development/KDE and QT
Requires: libssl-devel freetype2-devel fontconfig-devel libpng-devel zlib-devel
Requires: libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXcursor-devel libXext-devel
Requires: libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXv-devel
Requires: xorg-proto-devel libXtst-devel
Requires: libdbus-devel
%if_disabled bootstrap
Requires: phonon-devel
Requires: libqt4-webkit-devel
%endif
# for qcollectiongenerator
Requires: lib%name-sql-sqlite
Requires: rpm-macros-%{name} = %{version}-%{release}
Provides: lib%name-devel-cxx = %__gcc_version_base
%description -n lib%name-devel
Qt is a GUI software toolkit. Qt simplifies the task of writing and maintaining
GUI (graphical user interface) applications for X Windows.

Qt is written in C++ and is fully object-oriented. It has everything you need
to create professional GUI applications. And it enables you to create them
quickly.

Qt is a multi-platform toolkit. When developing software with Qt, you can run
it on the X Window System (Unix/X11) or Microsoft Windows NT and Windows 95/98.
Simply recompile your source code on the platform you want.

This package contains the files necessary to develop applications

##############################################
%package -n lib%name-devel-static
Summary: Version of the Qt GUI toolkit for static linking
Group: Development/KDE and QT
Requires: lib%name-devel
Obsoletes: %name-devel-static
%description -n lib%name-devel-static
This package package contains the files necessary to link applications
to the Qt GUI toolkit statically (rather than dynamically).
Statically linked applications don't require the library to be installed
on the system running the application.

##############################################
%package qml
Summary: QML modules Qt%major
Group: Development/KDE and QT
Requires: lib%name-devel
%description qml
The package contains a QML modules and viewer for the Qt%major toolkit.

##############################################
%package designer
Summary: Designer for the Qt%major
Group: Development/KDE and QT
Requires: lib%name-devel
%description designer
The package contains an User Interface designer
tool for the Qt%major toolkit.

##############################################
%package -n lib%name-styles
Summary: Extra styles for the Qt GUI toolkit
Group: System/Libraries
Requires: %name-common
%description -n lib%name-styles
Extra styles (themes) for the Qt GUI toolkit.

##############################################
%package sql
BuildArch: noarch
Group: System/Libraries
Summary: Meta-package for SQL support of Qt%major GUI toolkit
Requires: lib%name-sql-mysql
Requires: lib%name-sql-sqlite
%if_enabled sql_tds
Requires: lib%name-sql-tds
%endif
%if_enabled sql_ibase
Requires: lib%name-sql-interbase
%endif
%if_enabled sql_pgsql
Requires: lib%name-sql-postgresql
%endif
%if_enabled sql_ibase
Requires: lib%name-sql-interbase
%endif
%if_enabled sql_sqlite2
Requires: lib%name-sql-sqlite2
%endif
%if_enabled sql_odbc
Requires: lib%name-sql-odbc
%endif
%if_enabled sql_tds
Requires: lib%name-sql-tds
%endif
%description sql
Meta-package for SQL support of Qt%major GUI toolkit

##############################################
%package -n lib%name-sql-odbc
Summary: ODBC drivers for Qt%major SQL classes
Group: System/Libraries
Provides: lib%name-plugin-sql = %version-%release
%description -n lib%name-sql-odbc
ODBC driver for Qt's SQL classes (QODBC)

##############################################
%package -n lib%name-sql-tds
Summary: FreeTDS(Sybase) driver for Qt%major SQL classes
Group: System/Libraries
Provides: lib%name-plugin-sql = %version-%release
%description -n lib%name-sql-tds
FreeTDS(Sybase) driver for Qt's SQL classes (QTDS)

##############################################
%package -n lib%name-sql-mysql
Summary: MySQL driver for Qt%major SQL classes
Group: System/Libraries
Provides: lib%name-plugin-sql = %version-%release
%description -n lib%name-sql-mysql
MySQL driver for Qt's SQL classes (QMYSQL)

##############################################
%package -n lib%name-sql-postgresql
Summary: PostgreSQL drivers for Qt%major SQL classes
Group: System/Libraries
Provides: lib%name-plugin-sql = %version-%release
%description -n lib%name-sql-postgresql
PostgreSQL driver for Qt's SQL classes (QPSQL)

##############################################
%package -n lib%name-sql-interbase
Summary: InterBase drivers for Qt%major SQL classes
Group: System/Libraries
Provides: lib%name-plugin-sql = %version-%release
%description -n lib%name-sql-interbase
InterBase driver for Qt's SQL classes (QIBASE)

##############################################
%package -n lib%name-sql-sqlite
Summary: SQLite driver for Qt%major SQL classes
Group: System/Libraries
Provides: lib%name-plugin-sql = %version-%release
%description -n lib%name-sql-sqlite
SQLite driver for Qt's SQL classes (QSQLITE)

##############################################
%package -n lib%name-sql-sqlite2
Summary: SQLite2 driver for Qt%major SQL classes
Group: System/Libraries
Provides: lib%name-plugin-sql = %version-%release
%description -n lib%name-sql-sqlite2
SQLite2 driver for Qt's SQL classes (QSQLITE2)

##############################################
%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt%{major}
Group: Development/KDE and QT
Requires: %name-common = %version
Requires: %name-assistant = %version
Requires: %name-doc-html = %version
#Requires: %name-doc-man = %version
Requires: %name-doc-examples = %version
%description doc
This package contains documentation and sources for example programs.

##############################################
%package doc-html
BuildArch: noarch
Summary: Document for developing apps which will use Qt%{major}
Group: Development/KDE and QT
Requires: %name-common = %version
%description doc-html
This package contains documentation in html format.

##############################################
%package doc-man
BuildArch: noarch
Summary: Document for developing apps which will use Qt%{major}
Group: Development/KDE and QT
Requires: %name-common = %version
%description doc-man
This package contains documentation in man format.

##############################################
%package doc-examples
BuildArch: noarch
Summary: Examples for developing apps which will use Qt%{major}
Group: Development/KDE and QT
Requires: %name-common
Requires: %name-doc-examples-src
Requires: %name-doc-examples-bin
%description doc-examples
This package contains example programs.

##############################################
%package doc-examples-src
BuildArch: noarch
Summary: Examples sources for developing apps which will use Qt%{major}
Group: Development/KDE and QT
Requires: %name-common
%description doc-examples-src
This package contains sources of example programs.

##############################################
%package doc-examples-bin
Summary: Examples binaries for developing apps which will use Qt%{major}
Group: Development/KDE and QT
Requires: %name-common
Requires: %name-doc-examples-src
%description doc-examples-bin
This package contains binaries of example programs.

##############################################
%package assistant
Summary: Assistant for the Qt%major
Group: Text tools
Requires: %name-common
Requires: lib%name-sql-sqlite
%description assistant
This package contains an documentation browser
for the Qt%major toolkit and Qt-based programs.

##############################################
%package qvfb
Summary: Virtual frame buffer for Qt for Embedded Linux
Group: Emulators
Requires: %name-common
%description qvfb
Virtual frame buffer for Qt for Embedded Linux

##############################################
%package dbus
Summary: D-Bus utilities for the Qt%major
Group: System/Configuration/Other
Requires: %name-common
Requires: dbus-tools-gui
%description dbus
This package contains D-Bus utilities
for the Qt%major toolkit and Qt-based programs.

##############################################
%package -n rpm-macros-%{name}
Version: %major.%minor.%bugfix
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/KDE and QT
BuildArch: noarch
Requires: %name-common
%description -n rpm-macros-%{name}
Set of RPM macros for packaging %name-based applications for %distribution
Install this package if you want to create RPM packages that use %name

##############################################
%package -n rpm-build-%{name}
Version: %major.%minor.%bugfix
Summary: Set of RPM-related scripts for packaging %name-based applications
Group: Development/KDE and QT
Requires: %name-common
%description -n rpm-build-%{name}
Set of RPM-related scripts for packaging %name-based applications for %distribution
Install this package if you want to create RPM packages that use %name

##############################################
%prep
%define buildsubdir qt-everywhere-opensource-src-%version%beta

%setup -q -n %buildsubdir
# upstream
# security
# KDE-QT
#%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
# FC
%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p0
%patch217 -p1
%patch218 -p1
%patch219 -p1
# Debian
%patch301 -p1
%patch302 -p1
%patch303 -p1
%patch304 -p1
%patch305 -p1
%patch306 -p1
# ALT
%patch501 -p1
%patch502 -p1
%patch503 -p1
%patch504 -p1
%patch505 -p1
%patch506 -p1
%patch507 -p1
%patch508 -p1
###%patch509 -p1
%patch510 -p1
%patch511 -p1
%patch512 -p1
%patch513 -p1
%patch514 -p1
%patch515 -p1
%patch516 -p1
%patch517 -p1

%patch701 -p0
%patch702 -p0
%patch703 -p0
%patch704 -p0
%patch705 -p1
#
%patch706 -p0
%patch707 -p1
%patch708 -p1
%patch709 -p1
%patch710 -p1

%patch800 -p1
%patch801 -p0

%patch9100 -p1
#
%patch9102 -p1
%patch9103 -p1
%patch9104 -p1
%patch9105 -p1

sed -i "s|-O2||" mkspecs/*/qmake.conf
sed -i "s|-O2||" mkspecs/common/g++.conf
%if_enabled debug
sed -i "s|^CFG_DEBUG=.*|CFG_DEBUG=yes|" ./configure
%else
sed -i "s|^CFG_DEBUG=.*|CFG_DEBUG=no|" ./configure
%endif


%build
%add_optflags -std=gnu++98 -Wno-deprecated -DOPENSSL_LOAD_CONF -DOPENSSL_NO_SSL2
# install %%optflags
subst "s|^\s*QMAKE_CFLAGS\s*=.*$|QMAKE_CFLAGS = %optflags -DGLX_GLXEXT_LEGACY|" mkspecs/*/qmake.conf
subst "s|^\s*QMAKE_CFLAGS\s*=.*$|QMAKE_CFLAGS = %optflags -DGLX_GLXEXT_LEGACY|" mkspecs/common/g++.conf

# don't strip binaries during install
subst "s|^QMAKE_STRIP.*=.*|QMAKE_STRIP =|" mkspecs/common/linux.conf

# versioning hack
grep -q "^\s*QMAKE_LFLAGS_SONAME\s*\+" src/corelib/corelib.pro \
    || echo "QMAKE_LFLAGS_SONAME += " >> src/corelib/corelib.pro
%if_enabled versioning_hack
sed -i 's|^\s*QMAKE_LFLAGS_SONAME\s*\+.*$|QMAKE_LFLAGS_SONAME += -Wl,--version-script=%_sourcedir/qt4-compat-map -Wl,%_sourcedir/qt4-compat-lds|' src/corelib/corelib.pro
%else
sed -i 's|^\s*QMAKE_LFLAGS_SONAME\s*\+.*$|QMAKE_LFLAGS_SONAME += |' src/corelib/corelib.pro
%endif

export QT_DIR="$PWD"
export PATH=$QT_DIR/bin:$PATH
export LD_LIBRARY_PATH=$QT_DIR/lib:$LD_LIBRARY_PATH
export QT_PLUGIN_PATH=$QT_DIR/plugins
export CFLAGS="%optflags" CXXFLAGS="%optflags"

CNFGR="\
	-I%_includedir/pgsql/ -I%_includedir/mysql/ \
	-I/usr/include/fontconfig \
        -prefix %qtdir \
	-bindir %qtdir/bin \
	-docdir %_docdir/%name \
	-headerdir %_includedir/%name \
	-libdir %_libdir \
	-translationdir %_datadir/%name/translations \
	-plugindir %qtdir/plugins \
	-importdir %qtdir/imports \
	-sysconfdir %_sysconfdir/xdg \
	-datadir %_datadir/%name \
	-examplesdir %_datadir/%name/examples \
	-demosdir %_datadir/%name/demos \
	\
	-platform %platform \
	%{?_enable_debug:-debug}%{!?_enable_debug:-release} -verbose -no-separate-debug-info \
	-largefile -stl -fast -no-rpath -no-exceptions -no-g++-exceptions -accessibility -no-pch -icu \
%qIF_ver_gteq %binutils_ver 2.18
	-reduce-relocations \
%endif
	\
	-graphicssystem %graphicssystem -opengl %opengl_type \
	-system-zlib -cups -openssl-linked \
	-no-webkit \
	-xmlpatterns -scripttools \
	-multimedia -declarative \
	-no-nas-sound -no-nis -iconv \
	-no-phonon -no-gstreamer \
	%{?_enable_gtkstyle: -gtkstyle}%{!?_enable_gtkstyle: -no-gtkstyle} \
	%{?_enable_glib: -glib}%{!?_enable_glib: -no-glib} \
	\
	-dbus-linked \
	\
	-sm -mitshm -fontconfig -xfixes -xshape -xcursor -xinerama -xrender -xrandr -xkb -xinput -xsync \
	\
	-svg \
	-system-libpng -system-libjpeg -system-libmng -system-libtiff"
#	-DQT_USE_APPROXIMATE_CURSORS \
#	-xvideo \

CNFGR_STATIC=" -static \
	-qt-sql-mysql -qt-sql-sqlite -system-sqlite \
	%{?_enable_sql_tds:-qt-sql-tds} \
	%{?_enable_sql_ibase:-qt-sql-ibase} \
	%{?_enable_sql_pgsql:-qt-sql-psql} \
	%{?_enable_sql_sqlite2:-qt-sql-sqlite2} \
	%{?_enable_sql_odbc:-qt-sql-odbc}"

CNFGR_SHARED=" -shared \
	-plugin-sql-mysql -plugin-sql-sqlite -system-sqlite \
	%{?_enable_sql_tds:-plugin-sql-tds} \
	%{?_enable_sql_ibase:-plugin-sql-ibase} \
	%{?_enable_sql_pgsql:-plugin-sql-psql} \
	%{?_enable_sql_sqlite2:-plugin-sql-sqlite2} \
	%{?_enable_sql_odbc:-plugin-sql-odbc}"

is_building=""
clean_but_lib()
{
    [ -n "$is_building" ] || return
    mkdir -p lib-built
    cp -ar lib/* lib-built
    make confclean
    rm -rf lib/*
}

# Build   STATIC THREADED   libraries #
%if_enabled static_thread
if ! [ -e lib/libQtCore.a ] ; then
echo -e "o\nyes" |./configure $CNFGR_STATIC $CNFGR -nomake examples -nomake demos -nomake tests -nomake docs -nomake translations
%make_build -C src
%make_build -C tools/designer/src/uitools
is_building=1
clean_but_lib
fi
%endif #static_thread

# Build   SHARED THREADED   libraries #
%if_enabled shared_thread
if ! [ -e lib/libQtCore.so ] ; then
echo -e "o\nyes" |./configure $CNFGR_SHARED $CNFGR %{!?_enable_docs:-nomake examples -nomake demos -nomake tests -nomake docs}
%make_build
fi
%if_enabled sql_sqlite2
%make_build -C src/plugins/sqldrivers/sqlite2
%endif
%if_enabled docs
[ -d doc-build ] || %make_build docs
%endif
%endif #shared_thread

# compile translations
LD_LIBRARY_PATH=./lib ./bin/lrelease ./translations/*.ts
rm -f ./translations/*_untranslated.qm


%install
%if_enabled debug
%set_strip_method none
%endif

export QTDIR=%qtdir
export QT_DIR="$PWD"
export PATH=$QT_DIR/bin:%buildroot/%qtdir/bin:$PATH
export MANPATH=%qtdir/doc/man:$MANPATH
export LD_LIBRARY_PATH=$QT_DIR/lib:$LD_LIBRARY_PATH

install -d -m 0755 %buildroot/%_bindir
install -d -m 0755 %buildroot/%qtdir/plugins/codecs/
install -d -m 0755 %buildroot/%qtdir/plugins/crypto/
install -d -m 0755 %buildroot/%qtdir/plugins/accessible/
install -d -m 0755 %buildroot/%qtdir/plugins/styles/
install -d -m 0755 %buildroot/%qtdir/imports/QtWebKit

%make INSTALL_ROOT=%buildroot install
[ -x %buildroot/%qtdir/bin/qdoc3 ] \
    || install -m 0755 bin/qdoc3 %buildroot/%qtdir/bin/
%if_enabled sql_sqlite2
%make INSTALL_ROOT=%buildroot install -C src/plugins/sqldrivers/sqlite2
%endif


%if_enabled docs
# apply docs
mkdir -p %buildroot/%_docdir/
ln -s `relative %_docdir/%name %_datadir/%name/doc` %buildroot/%_datadir/%name/doc
%endif
ln -s `relative %_docdir/%name %qtdir/doc` %buildroot/%qtdir/doc

# install rpm macros
install -d -m 0755 %buildroot/%_rpmmacrosdir/
install -m 0644 %SOURCE3 %buildroot/%_rpmmacrosdir/%name

# install settings directory
install -d -m 0755 %buildroot/%_sysconfdir/xdg/
ln -s ../../../%_sysconfdir/xdg %buildroot/%qtdir/settings

# install tools
install -m 775 bin/findtr %buildroot/%qtdir/bin/
pushd %buildroot/%qtdir/bin/
for f in `ls -1`; do
    ln -s ../..%qtdir/bin/$f %buildroot/%_bindir/$f-%name
done
popd

# install libraries
#
mkdir -p %buildroot/%qtdir/lib
pushd %buildroot/%_libdir
for f in lib*.so.*; do
    ln -s ../../$f %buildroot/%qtdir/lib/
    [ -f $f ] \
	&& ln -sf $f %buildroot/%qtdir/lib/`echo $f| sed "s|\(.*\.so\).*|\1|"`
done
popd
%if_enabled static_thread
for f in lib-built/lib*.a lib-built/lib*.la; do
install -m0644 $f %buildroot/%qtdir/lib/
done
%endif
#
ln -s %name %buildroot/%_libdir/%rname-%version

# clean from WebKit
rm -f %buildroot/%qtdir/imports/QtWebKit/*
rm -f %buildroot/%_libdir/libQtWebKit.*
rm -f %buildroot/%qtdir/lib/libQtWebKit.*
rm -f %buildroot/%_includedir/%name/QtWebKit/*
rm -f %buildroot/%_pkgconfigdir/QtWebKit.pc

# install qdbus alternative
QDBUS_ALTPRIO=`printf '%%.2d%%.2d%%.2d%%.2d\n' 0 %major %minor %bugfix`
mkdir -p %buildroot/%_altdir/
cat > %buildroot/%_altdir/qdbus-%name <<__EOF__
%_bindir/qdbus %qtdir/bin/qdbus $QDBUS_ALTPRIO
__EOF__
cat > %buildroot/%_altdir/qdbusviewer-%name <<__EOF__
%_bindir/qdbusviewer %qtdir/bin/qdbusviewer $QDBUS_ALTPRIO
__EOF__
mkdir -p %buildroot/usr/lib/kde4/bin/
ln -s `relative %qtdir/bin/qdbus /usr/lib/kde4/bin/qdbus` %buildroot/usr/lib/kde4/bin/qdbus

# install translations
#install -m 644 ./translations/*.qm %buildroot/%qtdir/translations
mkdir -p %buildroot/%_datadir/%name/translations
ln -s ../../../%_datadir/%name/translations %buildroot/%qtdir/translations
mkdir -p %buildroot/%_datadir/%name/phrasebooks
ln -s ../../../%_datadir/%name/phrasebooks %buildroot/%qtdir/phrasebooks
# findlang
rm -f *.lang
for f in %buildroot/%_datadir/%name/translations/*.qm
do
    APP=`echo "$f"| sed -e 's|^.*/\(.*\)_\([a-z][a-z]\)[^[:alpha:]].*|\1|'`
    LNG=`echo "$f"| sed -e 's|^.*/\(.*\)_\([a-z][a-z]\)[^[:alpha:]].*|\2|'`
    FILE=%%_datadir/%name/translations/`basename "$f"`
    if ! [ -f $APP.lang ]; then
	echo "%%defattr(644,root,root,755)" > $APP.lang
    fi
    echo "%%lang($LNG) $FILE" >>$APP.lang
done
cat linguist.lang >> designer.lang

# install pkgconfig files
#mkdir -p %buildroot/%_libdir/pkgconfig
#for f in %buildroot/%_libdir/*.pc; do
#    mv $f %buildroot/%_libdir/pkgconfig/
#done
sed -i "s|\(-L\${libdir}\)|-L%qtdir/lib \1|" %buildroot/%_libdir/pkgconfig/*.pc

# install includes
mkdir -p %buildroot/%_includedir/
ln -s ../../../%_includedir/%name %buildroot/%qtdir/include

# install designer templates
#install -d -m 0755 %buildroot/%qtdir/tools/designer/templates
#cp -fR tools/designer/templates/*.ui %buildroot/%qtdir/tools/designer/templates

# Ship qmake stuff
ln -s ../../../%_datadir/%name/mkspecs %buildroot/%qtdir/mkspecs
# uninstall optflags
subst "s|^\s*QMAKE_CFLAGS\s*=.*$|QMAKE_CFLAGS	= -pipe|" %buildroot/%qtdir/mkspecs/*/qmake.conf
subst "s|^\s*QMAKE_CFLAGS\s*=.*$|QMAKE_CFLAGS	= -pipe|" %buildroot/%qtdir/mkspecs/common/g++.conf
# fix lib*.so placement
subst "s|^\s*QMAKE_LIBDIR_QT\s*=.*$|QMAKE_LIBDIR_QT		= %qtdir/lib|" %buildroot/%qtdir/mkspecs/*/qmake.conf
subst "s|^\s*QMAKE_LIBDIR_QT\s*=.*$|QMAKE_LIBDIR_QT		= %qtdir/lib|" %buildroot/%qtdir/mkspecs/common/g++.conf
%if_enabled versioning_hack
## fix QMAKE_LFLAGS_SONAME
#for f in %buildroot/%_datadir/%name/mkspecs/*/qmake.conf
#do
#    subst "s|^.*QMAKE_LFLAGS_SONAME.*$|QMAKE_LFLAGS_SONAME     = -Wl,-soname,|g" $f
#done
%endif


# install documentation
#install -d -m 0755 %buildroot/%_docdir/%name/doc/html
#install -m 0644 doc/html/*.html %buildroot/%_docdir/%name/doc/html
install -d -m 0755 %buildroot/%_docdir/%name/
cat > %buildroot/%_docdir/%name/LICENSE.txt <<__EOF__
see %license in %_datadir/license
__EOF__
for f in LGPL_EXCEPTION.txt LICENSE.PREVIEW.COMMERCIAL
do
    f2=`echo "$f"| sed 's|\.[Tt][Xx][Tt]$||'`
    install -m 0644 $f %buildroot/%_docdir/%name/${f2}.txt
done

# Install a README
install -m 0644 %SOURCE8 %buildroot/%_docdir/%name/README.ALT.txt
sed -i 's|@QT@|%name|g' %buildroot/%_docdir/%name/README.ALT.txt
sed -i 's|@QTDIR@|%qtdir|g' %buildroot/%_docdir/%name/README.ALT.txt
sed -i 's|@QtVersion@|%version|g' %buildroot/%_docdir/%name/README.ALT.txt
sed -i 's|@PackageVersion@|%version-%release|g' %buildroot/%_docdir/%name/README.ALT.txt
sed -i 's|@QTHOME@|~/.config/|g' %buildroot/%_docdir/%name/README.ALT.txt

# Install man pages
#install -d -m 0755 %buildroot/%_mandir/man1/
#for i in %_builddir/%buildsubdir/doc/man/man1/* ; do
#   install -m 0644 $i %buildroot/%_mandir/man1/
#done
#pushd %buildroot/%_mandir/man1
#    for i in $(find . -name \*.1);do
#	mv -f $i ${i}qt%major%minor%bugfix
#    done
#popd
#install -d -m 0755 %buildroot/%_mandir/man3/
#for i in %_builddir/%buildsubdir/doc/man/man3/* ; do
#   install -m 0644 $i %buildroot/%_mandir/man3/
#done
#
#pushd %buildroot/%_mandir/
#    for i in $(find . -name Q\*);do
#	perl -pi -e 's|3qt|3qt%major%minor%bugfix|g' $i
#    done
#    for i in $(find . -name \*.3qt);do
#	mv -f $i ${i}%major%minor%bugfix
#    done
#popd

# David - 3.0.1-2mdk - Install .pri files needed to build examples and demos
install -d -m 0755 %buildroot/%qtdir/src/
for i in %_builddir/%buildsubdir/src/*.pri; do
   install -m 0644 $i %buildroot/%qtdir/src/
done

%if_enabled docs
# examples and demos
> %_builddir/%buildsubdir/examples_bin_list
> %_builddir/%buildsubdir/examples_bin_list_exclude
for m in examples demos
do
    pushd %buildroot/%_datadir/%name
	find $m -type d | while read d; do mkdir -p %buildroot/%qtdir/$d; done
    popd
    pushd %buildroot/%_datadir/%name/$m
	find -type f -name Makefile | while read f; do rm -f "$f"; done
	find -type f -name \*.o | while read f; do rm -f "$f"; done
	#find -type f -name README | \
	#while read readme_file
	#do
	#    cat $readme_file >${readme_file}.tmp
	#    echo -e "Before try to build one of these $m, you need to:\n" > $readme_file
	#    echo "export QTDIR=\"%{qtdir}/\" PATH=\"%{qtdir}/bin:\$PATH\"" >> $readme_file
	#    echo -e "\n\n" >> $readme_file
	#    cat ${readme_file}.tmp >> $readme_file
	#    rm -f ${readme_file}.tmp
	#done
	find ./ -type f -executable | sed "s|^\.||" | \
	while read e
	do
	    echo "%_datadir/%name/$m/$e" >>%_builddir/%buildsubdir/examples_bin_list
	    echo "%%exclude %_datadir/%name/$m/$e" >>%_builddir/%buildsubdir/examples_bin_list_exclude
	    subdir=`dirname $e`
	    mv ./$e %buildroot/%qtdir/$m/$subdir/
	    ln -s `relative %qtdir/$m/$e %_datadir/%name/$m/$e` ./$e
	done
    popd
done
%endif

pushd %buildroot/%_datadir/%name/mkspecs/
rm -rf default
ln -sf %platform default
popd

# Install .desktop files
install -d -m 0755 %buildroot/%_desktopdir/
install -m 0644 %SOURCE21 %buildroot/%_desktopdir/%name-assistant.desktop
install -m 0644 %SOURCE22 %buildroot/%_desktopdir/%name-designer.desktop
install -m 0644 %SOURCE23 %buildroot/%_desktopdir/%name-linguist.desktop
install -m 0644 %SOURCE24 %buildroot/%_desktopdir/%name-qtconfig.desktop
install -m 0644 %SOURCE25 %buildroot/%_desktopdir/%name-qtdemo.desktop
# Icons
mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m 644 %SOURCE101 %buildroot/%_iconsdir/hicolor/16x16/apps/%name.png
install -m 644 %SOURCE102 %buildroot/%_iconsdir/hicolor/32x32/apps/%name.png
install -m 644 %SOURCE103 %buildroot/%_iconsdir/hicolor/48x48/apps/%name.png
install -m 644 %SOURCE104 %buildroot/%_iconsdir/hicolor/64x64/apps/%name.png



%files
%files -n lib%name
%files sql
%files devel

%files common -f qt.lang
%dir %qtdir/bin
%dir %qtdir/
%dir %qtdir/lib/
%dir %_datadir/%name/
%if_enabled docs
%dir %_datadir/%name/doc
%endif
%dir %qtdir/phrasebooks/
%dir %_datadir/%name/phrasebooks/
%dir %qtdir/translations/
%dir %_datadir/%name/translations/
%dir %qtdir/plugins/
%dir %qtdir/plugins/graphicssystems/
%dir %qtdir/plugins/codecs/
%dir %qtdir/plugins/sqldrivers/
%dir %qtdir/plugins/imageformats/
%dir %qtdir/plugins/inputmethods/
%dir %qtdir/plugins/iconengines/
%dir %qtdir/plugins/crypto/
%dir %qtdir/plugins/script/
%dir %qtdir/plugins/accessible/
%dir %qtdir/plugins/bearer/
%dir %qtdir/plugins/styles
%dir %qtdir/plugins/qmltooling
%dir %qtdir/imports/
%dir %qtdir/imports/Qt/
%dir %qtdir/imports/Qt/labs/
%dir %qtdir/imports/QtWebKit/
%qtdir/settings
%_libdir/%rname-%version
%_iconsdir/hicolor/*/apps/%name.png
%dir %_docdir/%name/
%qtdir/doc
#
%qtdir/mkspecs/
%dir %_datadir/%name/mkspecs/
#
%dir %qtdir/src/

%files -n lib%{name}-qt3support -f qtconfig.lang
%qtdir/bin/qtconfig
%_bindir/qtconfig-%name
%qtdir/lib/libQt3Support.so.*
%_libdir/libQt3Support.so.*
%qtdir/plugins/accessible/libqtaccessiblecompatwidgets.*
%_desktopdir/%name-qtconfig.desktop

%files -n lib%{name}-core
%qtdir/lib/libQtCore.so.*
%_libdir/libQtCore.so.*
%qtdir/plugins/codecs/lib*.so

%files -n lib%{name}-gui
%qtdir/lib/libQtGui.so.*
%_libdir/libQtGui.so.*
%qtdir/plugins/imageformats/libqjpeg.*
%qtdir/plugins/imageformats/libqgif.*
%qtdir/plugins/imageformats/libqmng.*
%qtdir/plugins/imageformats/libqtiff.*
%qtdir/plugins/imageformats/libqico.*
%qtdir/plugins/imageformats/libqtga.*
%qtdir/plugins/accessible/libqtaccessiblewidgets.*
%qtdir/plugins/inputmethods/libqimsw-*.*

%files -n lib%{name}-script
%qtdir/lib/libQtScript.so.*
%_libdir/libQtScript.so.*
%qtdir/plugins/script/libqtscriptdbus.so

%files -n lib%{name}-uitools
%qtdir/lib/libQtUiTools.so.*
%_libdir/libQtUiTools.so.*

%files -n lib%{name}-network
%qtdir/lib/libQtNetwork.so.*
%_libdir/libQtNetwork.so.*
%qtdir/plugins/bearer/libqgenericbearer.so
%qtdir/plugins/bearer/libqnmbearer.so
%qtdir/plugins/bearer/libqconnmanbearer.so

%files -n lib%{name}-opengl
%qtdir/lib/libQtOpenGL.so.*
%_libdir/libQtOpenGL.so.*
%qtdir/plugins/graphicssystems/libqglgraphicssystem.so
%if "%opengl_type" == "es2" || "%opengl_type" == "es1"
%qtdir/lib/libQtMeeGoGraphicsSystemHelper.so.*
%_libdir/libQtMeeGoGraphicsSystemHelper.so.*
%qtdir/plugins/graphicssystems/libqmeegographicssystem.so
%endif

%files -n lib%{name}-sql
%qtdir/lib/libQtSql.so.*
%_libdir/libQtSql.so.*

%files -n lib%{name}-xml
%qtdir/lib/libQtXml.so.*
%_libdir/libQtXml.so.*

%files -n lib%{name}-svg
%qtdir/lib/libQtSvg.so.*
%_libdir/libQtSvg.so.*
%qtdir/plugins/imageformats/libqsvg.so
%qtdir/plugins/iconengines/libqsvgicon.so

%files -n lib%{name}-designer
%qtdir/lib/libQtDesigner.so.*
%_libdir/libQtDesigner.so.*
%qtdir/lib/libQtDesignerComponents.so.*
%_libdir/libQtDesignerComponents.so.*

%files -n lib%{name}-multimedia
%qtdir/lib/libQtMultimedia.so.*
%_libdir/libQtMultimedia.so.*

%files -n lib%{name}-declarative
%_bindir/qmlviewer-qt4
%qtdir/bin/qmlviewer
%qtdir/lib/libQtDeclarative.so.*
%_libdir/libQtDeclarative.so.*
%qtdir/plugins/qmltooling/libqmldbg_tcp.so
%qtdir/plugins/qmltooling/libqmldbg_inspector.so
%qtdir/imports/Qt/labs/folderlistmodel
%qtdir/imports/Qt/labs/gestures
%qtdir/imports/Qt/labs/particles
%qtdir/imports/Qt/labs/shaders

%files dbus
%_bindir/qdbusviewer-%name
%qtdir/bin/qdbusviewer
%_altdir/qdbusviewer-%name
%_bindir/qdbus-%name
%qtdir/bin/qdbus
%_altdir/qdbus-%name
/usr/lib/kde4/bin/qdbus
%files -n lib%{name}-dbus
%qtdir/lib/libQtDBus.so.*
%_libdir/libQtDBus.so.*

%files -n lib%{name}-test
%qtdir/lib/libQtTest.so.*
%_libdir/libQtTest.so.*

%files -n lib%{name}-help -f qt_help.lang
%qtdir/lib/libQtHelp.so.*
%_libdir/libQtHelp.so.*
#
%qtdir/bin/qhelpconverter
%qtdir/bin/qhelpgenerator
%_bindir/qhelpconverter-%name
%_bindir/qhelpgenerator-%name

%files -n lib%{name}-clucene
%qtdir/lib/libQtCLucene.so.*
%_libdir/libQtCLucene.so.*

%files -n lib%{name}-xmlpatterns
%qtdir/bin/xmlpatterns
%qtdir/bin/xmlpatternsvalidator
%_bindir/xmlpatterns-%name
%_bindir/xmlpatternsvalidator-%name
%qtdir/lib/libQtXmlPatterns.so.*
%_libdir/libQtXmlPatterns.so.*

%files -n lib%{name}-scripttools
%qtdir/lib/libQtScriptTools.so.*
%_libdir/libQtScriptTools.so.*

%files -n lib%name-devel
%doc %_docdir/%name/*.txt
#
%_bindir/qmlplugindump-qt4
%qtdir/bin/qmlplugindump
%_bindir/qcollectiongenerator-%name
%qtdir/bin/qcollectiongenerator
%_bindir/qttracereplay-%name
%qtdir/bin/qttracereplay
%qtdir/bin/findtr
%_bindir/findtr-%name
%qtdir/bin/moc
%_bindir/moc-%name
%qtdir/bin/lrelease
%_bindir/lrelease-%name
%qtdir/bin/lconvert
%_bindir/lconvert-%name
%qtdir/bin/lupdate
%_bindir/lupdate-%name
%qtdir/bin/pixeltool
%_bindir/pixeltool-%name
%qtdir/bin/rcc
%_bindir/rcc-%name
%qtdir/bin/qt3to4
%_bindir/qt3to4-%name
%qtdir/bin/qdbuscpp2xml
%_bindir/qdbuscpp2xml-%name
%qtdir/bin/qdbusxml2cpp
%_bindir/qdbusxml2cpp-%name
%qtdir/bin/qmake
%_bindir/qmake-%name
%qtdir/bin/uic
%_bindir/uic-%name
%qtdir/bin/uic3
%_bindir/uic3-%name
%qtdir/bin/qdoc3
%_bindir/qdoc3-%name
#
%_includedir/%name
%qtdir/include
#
%qtdir/lib/*.so
%_libdir/*.so
%_libdir/*.prl
#
%qtdir/plugins/graphicssystems/libqtracegraphicssystem.so
#
%_datadir/%name/mkspecs/common
%_datadir/%name/mkspecs/features
%_datadir/%name/mkspecs/default
%_datadir/%name/mkspecs/*linux*
%_datadir/%name/mkspecs/qconfig.pri
#
%qtdir/src/*
%_datadir/%name/q3porting.xml
#
%_libdir/pkgconfig/*.pc

%files designer -f designer.lang
%_bindir/designer*
%_bindir/linguist*
#
%_datadir/%name/phrasebooks/*.qph
#
%dir %qtdir/plugins/designer
%qtdir/plugins/designer/*
%qtdir/bin/designer*
%qtdir/bin/linguist*
#
%_desktopdir/%name-linguist.desktop
%_desktopdir/%name-designer.desktop

%if_enabled sql_odbc
%files -n lib%name-sql-odbc
%qtdir/plugins/sqldrivers/libqsqlodbc.*
%endif

%if_enabled sql_pgsql
%files -n lib%name-sql-postgresql
%qtdir/plugins/sqldrivers/libqsqlpsql.*
%endif

%if_enabled sql_ibase
%files -n lib%name-sql-interbase
%qtdir/plugins/sqldrivers/libqsqlibase.*
%endif

%files -n lib%name-sql-mysql
%qtdir/plugins/sqldrivers/libqsqlmysql.*

%if_enabled sql_tds
%files -n lib%name-sql-tds
%qtdir/plugins/sqldrivers/libqsqltds.*
%endif

%files -n lib%name-sql-sqlite
%qtdir/plugins/sqldrivers/libqsqlite.*

%if_enabled sql_sqlite2
%files -n lib%name-sql-sqlite2
%qtdir/plugins/sqldrivers/libqsqlite2.*
%endif

%files assistant -f assistant.lang
%_bindir/assistant-%name
%qtdir/bin/assistant
%_desktopdir/%name-assistant.desktop

%files qvfb -f qvfb.lang
%_bindir/qvfb-%name
%qtdir/bin/qvfb
#%_desktopdir/%name-qvfb.desktop

%if_enabled docs
%files doc
%exclude %_datadir/%name/mkspecs/*

%files doc-html
%dir %_docdir/%name/
%dir %_docdir/%name/html/
%doc %_docdir/%name/html/*
%dir %_docdir/%name/src/
%doc %_docdir/%name/src/*
%dir %_docdir/%name/qch/
%doc %_docdir/%name/qch/*

%files doc-examples

%files doc-examples-bin -f examples_bin_list
%_bindir/qtdemo-%name
%qtdir/bin/qtdemo
%_desktopdir/%name-qtdemo.desktop
%qtdir/examples
%qtdir/demos

%files doc-examples-src -f examples_bin_list_exclude
%_datadir/%name/examples
%_datadir/%name/demos

#%files doc-man
#%doc %_mandir/man1/*
#%doc %_mandir/man3/*
%endif
#end if_enabled docs

%if_enabled static_thread
%files -n lib%name-devel-static
%qtdir/lib/lib*.a
%qtdir/lib/lib*.la
%endif

%files -n rpm-macros-%{name}
%_rpmmacrosdir/%name


%changelog
* Fri Aug 30 2019 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt19
- fix changelog

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt18
- build with modern compiler

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt17
- security fix
  (Fixes: CVE-2018-15518, CVE-2018-19869, CVE-2018-19870,
  CVE-2018-19871, CVE-2018-19872, CVE-2018-19873)

* Mon Apr 08 2019 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt16
- fix requires

* Mon Apr 08 2019 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt15
- update build requires (ALT#36530)

* Thu Feb 07 2019 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt14
- fix to build with new libmysqlclient

* Wed Aug 29 2018 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt13%ubt
- link with openssl

* Wed May 30 2018 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt12%ubt
- update requires
- fix to build

* Fri May 12 2017 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt11%ubt
- rebuild with new libmng

* Thu Apr 06 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.8.7-alt10%ubt
- moc: fixed work with glibc >= 2.25.

* Wed Feb 01 2017 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt9%ubt
- build with gcc6

* Wed Apr 27 2016 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt8
- support KDE5 colors

* Mon Apr 25 2016 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt7
- set Breeze style and icons for KDE4 by default

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt6
- support KDE4 plugins by default

* Thu Dec 10 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt5
- add aarch64 support

* Fri Oct 02 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt4
- adds patch for sni-qt system tray plugin support

* Fri Sep 25 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt3
- add qdbus symlink for KDE4

* Thu Jul 02 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt2
- rebuild with gcc5

* Tue May 26 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.7-alt1
- new version

* Mon May 18 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.6-alt6
- fix requires

* Mon Apr 20 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.6-alt5
- build qtwebkit in separate package

* Fri Jan 23 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.6-alt3.M70P.1
- build for M70P

* Fri Jan 23 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.6-alt4
- fix mnemonic menu shortcuts

* Thu Oct 02 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.6-alt2.M70P.1
- built for M70P

* Fri Sep 26 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.6-alt3
- build without gstreamer

* Mon Sep 01 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.6-alt1.M70P.1
- built for M70P

* Thu Aug 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.6-alt2
- add fixes for LibreOffice-kde from QTBUGs 37380,34614,38585

* Mon May 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.6-alt0.M70P.1
- built for M70P

* Thu Apr 24 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.6-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt5.M70P.1
- built for M70P

* Wed Feb 26 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt6
- add large XML entities support

* Thu Dec 19 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt5
- disable mnemonic shortcuts in menus

* Mon Dec 02 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt3.M70P.2
- built for M70P

* Fri Nov 29 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt4
- don't apply patch for cups-1.6 printers discovery (ALT#29609)

* Fri Nov 22 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt3
- use constant docs dir

* Sat Nov 16 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1.M70P.1
- built for M70P

* Fri Nov 15 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt2
- package examples unarchived to make in available in qtcreator
- add patch for cups-1.6 printers discovery

* Wed Jul 24 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M70P.1
- built for M70P

* Wed Jul 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version

* Thu Jun 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt5
- rebuilt with new unixODBC

* Fri Apr 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt4
- update patch against QTBUG-22829

* Fri Mar 22 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2.M60P.1
- built for M60P

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt3
- add qmake_qt4 macro (ALT#28724)

* Fri Feb 15 2013 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2
- add fix against QTBUG-29082 (ALT #28557)

* Mon Dec 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Fri Nov 30 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1.M60P.1
- built for M60P

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2
- update FC patches
- disable SSL compression by default

* Fri Oct 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Mon Sep 17 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Sun Sep 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt4
- built with libtiff5

* Fri Aug 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt2
- don't require libtiff-devel

* Wed May 23 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- build for M60P

* Tue May 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Fri Apr 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1.M60P.1
- build for M60P

* Fri Apr 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt2
- add patches against broken TGA-files and Calligra crash

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Thu Mar 29 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Jan 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version
- set graphicssystem to raster by default
- update SuSE and FC patches

* Thu Dec 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt3.M60P.1
- built for M60P

* Thu Dec 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt4
- add patch to fix libreoffice crash (libreoffice-kde must be patched too)

* Tue Dec 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt3
- fix moc to work with boost-1.48 (ALT#26677)

* Thu Sep 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1.M60P.1
- built for M60P

* Thu Sep 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2
- add upstream fix to blacklist DigiNotar certs

* Thu Sep 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Tue Jul 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2.M60P.1
- built for M60P

* Tue Jul 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt3
- don't force search for KDE4 plugins (ALT#25857)

* Fri Jun 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- add provides for skype

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Wed Apr 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt3
- add patch against fraudulent ssl-certificates
- add patch to fix 24bpp colors

* Wed Apr 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt2
- exclude designer phonon plugin

* Mon Mar 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Mon Feb 14 2011 Alexey Tourbin <at@altlinux.ru> 4.7.1-alt2
- rebuilt for debuginfo
- enabled strict dependencies between subpackages
- disabled symbol versioning
- disabled libqt4-devel-static

* Thu Dec 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Mon Nov 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt5
- fix devel subpackage requires

* Wed Oct 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt4
- fix to build QtWebkit with phonon
- remove automatic dependency to libqt4-core
- update webkit-fix_graphicscontextqt.patch; thanks corwin@alt

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt3
- rebuilt with new openssl (ALT#24234)
- built without phonon

* Thu Sep 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt2
- fix webkit links underline rendering; thanks corwin@alt

* Tue Sep 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt1
- 4.7.0 release

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt0.6
- 4.7.0-rc1

* Fri Aug 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt0.5
- update code from qt/4.7-stable

* Wed Aug 04 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt0.4
- update code from qt/4.7-stable

* Wed Aug 04 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt0.3
- add fix for painting lines whith float coordinates

* Fri Jul 23 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt0.2
- add conflicts with old yachat

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt0.1
- snapshot from 4.7-stable branch

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version
- move qcollectiongenerator to lib%name-devel package

* Tue May 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt5.M51.1
- built for M51

* Tue May 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt6
- add requires to phonon-devel to lib%name-devel package

* Mon May 24 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt4.M51.1
- built for M51

* Mon May 24 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt5
- add requires to phonon-devel to devel package

* Fri May 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt4
- don't build static libraries and docs on arm; thanks boyarsh@alt

* Wed May 19 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt2.M51.1
- built for M51

* Wed May 19 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt3
- update kde-qt patches
- add cups fixes
- add fixes for CVE-2010-0047 CVE-2010-0051 CVE-2010-0054 CVE-2010-0648
  CVE-2010-0656 CVE-2010-0046 CVE-2010-0049 CVE-2010-0050 CVE-2010-0052
  (ALT#23506)

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1.M51.1
- build for M51

* Fri Feb 19 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt2
- add KDE4 plugins dir to search patch
- add automatic requires to libqt4-core

* Mon Feb 15 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Wed Jan 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- built kde-qt/4.6.1-patched
- fix path to ca-bundle.crt

* Thu Jan 14 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt0.1
- update to kde-qt/4.6-stable-patched/de4d4af3023bde675283b42220d01ded692fdbc2

* Mon Dec 07 2009 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Thu Nov 19 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt2.M51.1
- built for M51

* Wed Nov 18 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt3
- add patch to avoid dbus deadlock

* Tue Nov 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1.M50P.1
- built for p5

* Mon Nov 02 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.5.3-alt2.1
- not use -pch on arm

* Wed Oct 28 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt2
- fix to compile docs

* Tue Oct 27 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version
- improve initial style setup
- fix conflict icons with qt3
- update icons, desktop-files
- use kde-qt(http://gitorious.org/+kde-developers/qt/kde-qt) for sources

* Mon Sep 28 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt7
- fix search for netscape plugins

* Fri Sep 11 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt6
- add patch to fix CVE-2009-2700
- patch from kde-qt to add support for isOpen in mysql driver plugin
- add patch from MDV to fix qmake wformat patch

* Wed Aug 26 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt5
- update fix_shortcuts.patch

* Thu Aug 13 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt4
- update kde-qt patches

* Thu Jul 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt3
- add patches from Sergey A. Sukiyazov:
  fix to initialize iconvcodec without QApplication
  fix posible lost of mouse release event
  activate application menu bar by Shift+F10, Ctrl+Super_L, Ctrl+Super_R
  allow Key as Alt+Key menu shortcuts when keyboard layout changed

* Tue Jul 07 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1.M50.1
- built for M50

* Mon Jul 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt2
- fix libQtCore execution
- built with default optlevel

* Mon Jun 29 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version
- update kde-qt(qt-copy) patches

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt4
- fix default netscape plugins path
- update qt-copy patches

* Thu May 21 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt2.M50.1
- built for M50

* Fri May 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt3
- rebuilt with new gcc
- update qt-copy patches

* Mon Apr 27 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt2
- update qt-copy patches

* Thu Apr 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version
- package qdoc3

* Tue Apr 07 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt4
- improve provides to allow install various skype rpms

* Wed Apr 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt3
- built with glib loop support
- built gtkstyle
- make doc-html subpackage noarch

* Fri Mar 27 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt2
- inmprove subpackages requires

* Wed Mar 25 2009 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Wed Mar 11 2009 Sergey V Turchin <zerg at altlinux dot org> 4.4.3-alt8
- sync patches with qt-copy

* Tue Mar 03 2009 Sergey V Turchin <zerg at altlinux dot org> 4.4.3-alt7
- move rpm macros to rpm-macros-%name subpackage

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 4.4.3-alt6
- fix qdbus alternative

* Wed Feb 25 2009 Sergey V Turchin <zerg at altlinux dot org> 4.4.3-alt5
- add patch from qt-copy to fix KDE4 system tray background
- add alternative for qdbus to be in %%_bindir

* Tue Jan 27 2009 Sergey V Turchin <zerg at altlinux dot org> 4.4.3-alt4
- sync patches with qt-copy

* Tue Jan 27 2009 Sergey V Turchin <zerg at altlinux dot org> 4.4.3-alt3
- applied lcd patches from https://bugs.launchpad.net/ubuntu/+source/qt4-x11/+bug/217729
  fixes #18560; thanks morozov@alt
- removed deprecated macroses from specfile

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.3-alt2
- built with ibase(firebird) sql driver

* Wed Oct 22 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.3-alt1
- new version
- detect new ld to build with -reduce-relocations
- update qt-copy patches
- add some fixes from SuSE

* Fri Sep 26 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.2-alt3
- fix patch for QCalendar

* Thu Sep 25 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.2-alt2
- reapply patch to show day on QCalendar navigation bar

* Thu Sep 18 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.2-alt1
- new version

* Thu Jul 31 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.1-alt1
- new version
- sync qt-copy patches with MDK

* Wed Jun 18 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.0-alt4
- built with linked libssl
- fix assistant requires

* Wed May 14 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.0-alt3
- fix to add xmlpatterns to QT_CONFIG

* Tue May 13 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.0-alt2
- sync qt-copy patches with MDK

* Wed May 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.0-alt1
- new version

* Mon May 05 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.0-alt0.2
- built for Sysyphus

* Thu Apr 17 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4.0-alt0.1
- intial build

* Tue Apr 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.3.4-alt5
- fix to compile

* Tue Apr 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.3.4-alt4
- locate libssl.so.4 and libssl.so too

* Tue Apr 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.3.4-alt3
- fix to dlopen libssl.so.6 instead of libssl.so

* Tue Mar 11 2008 Sergey V Turchin <zerg at altlinux dot org> 4.3.4-alt2
- remove compiler version from QT_BUILD_KEY

* Mon Mar 03 2008 Sergey V Turchin <zerg at altlinux dot org> 4.3.4-alt1
- new version
- fix package license
- built UiTools as shared library
- remove Makefiles and object files from examples

* Mon Jan 14 2008 Sergey V Turchin <zerg at altlinux dot org> 4.3.3-alt2
- show day on qcalendar navigation bar (#13619)

* Mon Dec 17 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.3-alt1
- new version
- sync patches with qt-copy

* Tue Oct 30 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.2-alt3
- change checkbox mark in Plastique style

* Fri Oct 12 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.2-alt2
- don't apply patches for compositing features support (fixes #13018)

* Thu Oct 04 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.2-alt1
- new version
- sync patches with qt-copy

* Thu Aug 30 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.1-alt3
- add patch to fix buffer overflow

* Tue Aug 14 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.1-alt2
- fix qsa-examples.tar.bz2 file conflicts

* Thu Aug 09 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.1-alt1
- new version
- sync patches with qt-copy (fixes CVE-2007-3388)

* Fri Aug 03 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.0-alt5
- don't apply 0172-prefer-xrandr-over-xinerama.diff (fixes #12396)

* Tue Jun 19 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.0-alt3
- add upstream fix do don't connect destroyed widget in stylesheet

* Tue Jun 19 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.0-alt2
- sync patches with qt-copy
- add provides %%name-x11 = %%version-%%release

* Fri Jun 01 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3.0-alt1
- new version
- remove wrap_kde_malloc.cpp from docs
- don't apply patch for alternate buttons to open application menu (#11945)
- update patches from qt-copy

* Tue Apr 03 2007 Sergey V Turchin <zerg at altlinux dot org> 4.2.3-alt8
- add patch against UTF-8 bug

* Fri Mar 30 2007 Sergey V Turchin <zerg at altlinux dot org> 4.2.3-alt7
- built without libaudio

* Thu Mar 29 2007 Sergey V Turchin <zerg at altlinux dot org> 4.2.3-alt6
- update uk translation

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 4.2.3-alt5
- built without NAS

* Wed Mar 21 2007 Sergey V Turchin <zerg at altlinux dot org> 4.2.3-alt4
- rebuild

* Tue Mar 20 2007 Sergey V Turchin <zerg at altlinux dot org> 4.2.3-alt3
- fix timers long wait when system time moving back; thanks stanv@alt

* Fri Mar 16 2007 Sergey V Turchin <zerg at altlinux dot org> 4.2.3-alt2
- include qt dbus tools, missing plugins
- symlink all programs to %_bindir

* Wed Mar 14 2007 Sergey V Turchin <zerg at altlinux dot org> 4.2.3-alt1
- new version

* Mon Mar 12 2007 Sergey V Turchin <zerg at altlinux dot org> 4.2.2-alt6
- update ru and uk translations
  thanks andi from ukr.net and arysin from gmail.com

* Wed Jan 10 2007 Sergey V Turchin <zerg at altlinux dot org> 4.2.2-alt5
- update QSA to 1.2.2

* Fri Dec 29 2006 Sergey V Turchin <zerg at altlinux dot org> 4.2.2-alt4
- fix QSA examples file owner package

* Mon Dec 25 2006 Sergey V Turchin <zerg at altlinux dot org> 4.2.2-alt3
- rebuilt with new dbus

* Thu Dec 14 2006 Sergey V Turchin <zerg at altlinux dot org> 4.2.2-alt2
- fix requires

* Tue Dec 05 2006 Sergey V Turchin <zerg at altlinux dot org> 4.2.2-alt1
- new version

* Fri Oct 20 2006 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Fri Oct 20 2006 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt4
- update patch for qimage

* Thu Oct 19 2006 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt3
- add patch for qimage

* Tue Oct 17 2006 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt2
- merge qt-copy patches

* Wed Oct 04 2006 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Thu Sep 28 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.4-alt2
- built with QSA

* Tue Sep 12 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.4-alt1
- new version

* Tue Jun 13 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt4
- fix compile with MySQL-4.0.x

* Sat Jun 10 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt3
- hardcode %qtdir/lib to QMAKE_LIBDIR_QT in qmake.conf

* Fri Jun 09 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt2
- fix for QyQt4 configure.py

* Wed May 31 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version
- fix build with installed %name-devel

* Wed May 17 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt7
- turn on versioning hack
- fix pkgconfig files

* Mon May 15 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt6
- rebuilt with new gcc

* Thu Apr 20 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt5
- fix QMAKE_LIBDIR_QT

* Thu Apr 20 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt4
- fix lib*.so symlinks 

* Thu Apr 20 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt3
- temporary built without QSA to resolve soname conflict with libqt3-qsa

* Wed Apr 19 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt2
- build sqlite2 plugin
- build QSA
- move libs to %_libdir
- fix Categories in .desktop-s

* Thu Apr 06 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version
- disable hidden visibility for gcc-3.x
- built with -Os

* Sun Feb 26 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Fri Jan 27 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt2
- removed target cpu name from Qt buildkey

* Wed Dec 21 2005 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Mon Nov 07 2005 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt2
- enable -fvisibility for gcc-3.4
- add rpm macros %%_qt4dir for devel
- add patch from Sergey A. Sukiyazov for activating first menu in menubar
  (if present) by pressing F10 or Super_L/R (Win_L/R)
- fix owner-package of /usr/lib/qt4/doc; move some dirs to %name-common

* Tue Oct 25 2005 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt1
- new Qt4

* Thu Jun 02 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.4-alt6
- merge patches from SuSE (patch for fast malloc)

* Tue May 31 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.4-alt5
- rebuild with new postgress

* Mon Apr 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.4-alt4
- add patches from Sergey A. Sukiyazov
- build static library
- x86_64 fixes, thanks mouse@altlinux

* Mon Mar 14 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.4-alt3
- qsa-1.1.2
- don't package designer translation

* Wed Feb 16 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.4-alt2
- restore original manpages
- restore designer translations

* Tue Feb 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.4-alt1
- new version

* Mon Jan 17 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.3-alt9
- rebuild with gcc3.4

* Wed Dec 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.3-alt8
- fix requires for libqt3-devel

* Fri Dec 10 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.3-alt7
- build imageformats and styles into plugins
- remove libjpeg,libmng,libpng,libGLU devels requires from libqt3-devel
- new qsa version
- remove 0054-qaccel_repeat_60625.patch
- split doc package
- build light version for installer stage2

* Thu Nov 04 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.3-alt6
- remove -fno-exceptions from QMAKE_CFLAGS_RELEASE
- move settings to separate package

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.3-alt5
- export QTINC and QTLIB environment variables in %_sysconfdir/profile.d

* Wed Oct 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.3-alt4
- sync patches with qt-copy
- build with system libmng

* Mon Aug 23 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.3-alt3
- fix provides from %name-qsa-devel
- add link to %_libdir/qt-%version
- add patch to fix xpm handling

* Wed Aug 18 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.3-alt2
- fix manpages
- add patch to fix gif handling

* Thu Aug 12 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.3-alt1
- new version
- sync patches with qt-copy

* Fri Aug 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt5
- don't package Designer translation files because overtranslation
  reserved words.

* Thu Jun 10 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt4
- update russian translations
- fix QMAKE_LFLAGS_SONAME in $QTDIR/mkspecs/*/qmake.conf (#4326)

* Tue May 25 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt3
- add patch to fix qfontdatabase caching

* Mon May 24 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt2
- add patch from qt-copy against kde menu width

* Wed May 19 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- new version
- remove provides libqt3-gcc_compiled

* Thu Apr 29 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt6
- rebuild with new glibc-2.3.3
- add patches from qt-copy for QImage->QPixmap conversions
- make buildable without unixODBC

* Mon Apr 26 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt5
- add patch form FC for Sans font name
- fix default qtrc

* Wed Apr 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt4
- update Russian translations
- add designer translation by Valia V. Vaneeva <fattie@altlinux>
- add *.desktop for menus
- fix crash KDevelop when click .ui in file tree view
- fix compile programs with -pedantic

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt3
- temporary provide libqt3-gcc_compiled

* Thu Mar 04 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt2
- rebuild with internal libmng

* Tue Mar 02 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version
- build with: shared sqlite, dlopen OpenGL

* Wed Feb 04 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Tue Feb 03 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt4
- add provides versioning lib%name(CXX%%__gcc_version_major)
- add Russian translations

* Tue Jan 13 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt3
- rebuild with gcc3.3

* Thu Dec 25 2003 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- removed fast-mallock.patch
- add versioning
- add translation support for qtconfig and designer

* Tue Nov 25 2003 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Mon Oct 27 2003 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version
- build with new qsa-1.0.1

* Mon Jul 07 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt10
- build without -fno-use-cxa-atexit

* Tue Jun 24 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt9
- add localization patch by  raorn at altlinux.ru

* Mon Jun 16 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt8
- add patch from qt-copy
- build with nas
- remove unusable sources and patches

* Tue May 20 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt7
- remove requires libXft
- build with Xft from XFree86
- add RH patches

* Mon Apr 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt6
- add xrandr patches

* Thu Apr 17 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt5
- fix typing in xx_XX.CP1251 locale

* Tue Apr 15 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt4
- fix missing file qsa.prf in lib%name-qsa-devel
- fix placement of qsa plugins
- fix build examples and tutorial

* Wed Apr 09 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt3
- build with QT_USE_APPROXIMATE_CURSORS (XFree-4.3 have nice cursors)

* Wed Mar 19 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.2-alt2
- don't apply Patch14 (aa by default)

* Thu Mar 13 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.2-alt1
- new version
- build new QSA beta3

* Thu Feb 06 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt3
- build new QSA beta2
- add RH && MDK patches

* Wed Jan 08 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt2
- disable objprelink
- build QSA (Qt Stript for Applications) 1.0-beta2pre1

* Tue Dec 17 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- new version

* Mon Nov 18 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- add patches from RH
- build libraries libeditor libdesigner libqassistantclient

* Mon Nov 18 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- add patches from MDK
- add patch1000 from ASP
- use tarball from Trolltech
- disable old patches

* Mon Nov 11 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- release
- update from cvs of qt-copy

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 3.1.0-alt0.6.kde3rc2
- changelog fix

* Tue Nov 05 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.6.kde31rc2
- qt-copy for KDE-3.1.rc2 (20021104)

* Tue Oct 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.5.beta2qtcopy
- qt-copy for KDE-3.1.rc1

* Mon Oct 21 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.4.beta2
- update from cvs of qt-copy
- add RH patches for Xft2 ported
  by Albert R. Valiev <darkstar@altlinux.ru>

* Mon Oct 14 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.3.beta2
- qt-copy of 3.1beta2 from kde.org

* Wed Oct 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.2.beta2
- 3.1beta2
- incrase %%release to upgrade Qt from Daedalus
- compile with xft2 (without patches)

* Mon Oct 07 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt14
- compile with xft2 (add RH patches)

* Thu Oct 03 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt12
- fix requires && provides

* Wed Oct 02 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt11
- fix conflicts

* Wed Oct 02 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.4-alt10
- fix provides && conflicts
- rebuild with new libGLU
- build designer without KDE

* Thu Sep 26 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt9
- add default config
- build designer with KDE
- fix provides

* Mon Sep 16 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt8
- rebuild with new XFree86

* Wed Sep 11 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.4-alt3.junuior
- build for Junior

* Mon Sep 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt7
- build with objprelink

* Wed Sep 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt6
- build with gcc 3.2

* Fri Aug 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt5
- fix %%build to
  don't search libs in
  %buildroot
  when start qt only based application.
  This fix launching apps  like licq psi,
  change styles in kcontrol
  and more bugs

* Tue Aug 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt4
- disable patches 600-700
- Conflicts: kdelibs < 3.0.2-alt4
- remove fixes qconfig.h for pyqt (styles compiled in)

* Tue Aug 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt3
- rebuild with motif style
- fix qconfig.h for pyqt

* Wed Jul 31 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt2
- fix symlinks in %_libdir

* Mon Jul 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.5-alt1
- new version
- build without kde because not need
- some patches from cooker and rawhide
- add patches from Sergey A. Sukiyazov <corwin@micom.net.ru>
  and kde.ru

* Fri May 24 2002 ZerG <zerg@altlinux.ru> 3.0.4-alt2
- qt-copy for KDE 3.0.1
- fix homedir to ~/.qt3
- build designer with kde

* Mon May 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.4-alt1
- new version

* Fri Apr 19 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt3
- split

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- snapshot for KDE3

* Wed Mar 27 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- new version

* Fri Mar 22 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt0.1.rc5
- snapshot for KDE3 rc3

* Tue Mar 12 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version

* Fri Feb 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Thu Oct 11 2001 Sergey V Turchin <zerg@altlinux.ru> 2.3.1-alt7
- build with new libpng
- add %%_libdir/libqt.so to lib%%name-devel

* Sat Sep 15 2001 Sergey Vlasov <vsu@altlinux.ru> 2.3.1-alt6
- don't compile designer with the static library
- don't compile examples and tutorial - it just wastes time
- run "make clean" after static libraries to get rid of non-PIC objects
- build libqxt with RPM_OPT_FLAGS
- do not install designer/pics - they are not needed at runtime
- install designer templates, examples and tools

* Tue Aug 21 2001 AEN <aen@logic.ru> 2.3.1-alt5
- ttf2ps fixed

* Thu Aug 16 2001 Sergey V Turchin <zerg@altlinux.ru> 2.3.1-alt4
- move all libqxt to lib%name-Xt package
- move documentation to %name-doc package
- add %name-xim-20010617.diff %name-qclipboard-20010617.diff
  and %name-qstring-toDouble-i18n-20010617.diff patches

* Wed Aug 15 2001 Sergey V Turchin <zerg@altlinux.ru> 2.3.1-alt3
- clean spec & disable enc.patch
- build packages with static libs

* Wed Jul 18 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.1-8mdk
- Re-upload with non broken BuildRequires

* Wed Jul 18 2001 Stefan van der Eijk <stefan@eijk.nu> 2.3.1-7mdk
- BuildRequires:      kdelibs-devel
- Removed BuildRequires:      Mesa-common XFree86-devel XFree86-libs
  db1 db3 gawk glibc-devel libstdc++-devel zlib-devel zlib1

* Tue Jul 17 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.1-6mdk
- Fix a typo when we create /usr/lib/qt2/lib/libqt-mt.so.%%version link

* Fri Jul 06 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.1-5mdk
- Fix build on alpha (Jeff Garzik)

* Thu Jul 05 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.1-4mdk
- Fix name for static libraries
- Add few BuildRequires and Obsoletes
- Add support for ia64

* Sun Jul 01 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.1-3mdk
- Rebuild with KDE (2.2.beta1) support
- Fix few Provides: and PreReq:
- Complete BuildRequires: for Linux-Mandrake 7.2

* Sat Jun 23 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.1-2mdk
- Rewrite %%build section (so, fix designer and some problems with rpath)
- Rewrite few sections of %%install (i.e. don't build in %%install)
- Complete %%install section according to %%build section
- Disable thread support for Linux-Mandrake 7.2
- Use system zlib and libpng instead sources provided in Qt package (8.0 and 8.1)
- Allow documentation to be used in designer (you need to
  "export QTDIR=/usr/lib/qt2/" if it's not already done)
- Add some missing BuildRequires
- Fix Makefiles in examples and tutorials

* Sun Jun 17 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.1-1mdk
- 2.3.1
- Add tests to automatically build right packages for right distribution
- Add %%files sections for all supported LMDK distributions
- Rewrite some sections of this spec to allow clean updates
- Remove qt-2.3.0-printing.patch.bz2
- Don't apply qt-2.3.0-qpsprinter-gbkprint.patch.bz2 at present time
- Disable kde support at present time
- Clean spec: bzip2 and rename qpsprinter-gbkprint.patch according to LMDK
  policy and add missing comments to make spec understandable by everybody
  (pacakgers, please to don't be lazzy and think you are not the only one who
  modify spec files)
- Fix few incorrect symlinks
- Rename static-libraries package to libqt2-static-devel (8.1)

* Thu May 31 2001 DU Xiaoming <dxiaoming@mandrakesoft.com> 2.3.0-6mdk
- Add a patch for simplified chinese printing.

* Fri Apr 20 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.0-5mdk
- Rebuild against latest GCC

* Wed Apr 18 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.0-4mdk
- Rebuild with kde support

* Sun Apr 08 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.0-3mdk
- Rebuild with latest GCC

* Sun Mar 18 2001  Daouda Lo <daouda@mandrakesoft.com> 2.3.0-2mdk
- patched to handle X fonts well

* Thu Mar 08 2001 David BAUDENS <baudens@mandrakesoft.com> 2.3.0-1mdk
- 2.3.0

* Tue Feb 20 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2.4-3mdk
- Rebuild to try to remove dependancies on libmng0 (thanks to Guillaume)

* Tue Feb 20 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2.4-2mdk
- Rebuild with libmng-1.0.0

* Sat Jan 27 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2.3-9mdk
- Use sources from TrollTech
- Remove patch #1
- Add two patches from David FAURE

* Wed Jan 17 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2.3-8mdk
- Enable KDE support
- Use optimizations

* Tue Dec 26 2000 Daouda Lo <daouda@mandrakesoft.com> 2.2.3-7mdk
- AA support (build with -xft) -> with freetype2 + XFree-4.0.2 (see cooker)
- cleanups

* Fri Dec 22 2000 Daouda Lo <daouda@ke.mandrakesoft.com> 2.2.3-6mdk
- fix symlinks
- cleanups

* Thu Dec 21 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.2.3-5mdk
- add a libqt.so as quick hack for myself to build Licq.
- need fix: fix bad symlinks in /usr/lib.

* Tue Dec 19 2000  Daouda Lo <daouda@mandrakesoft.com> 2.2.3-4mdk
- links to include files in /usr/lib/qt2/include

* Mon Dec 18 2000  Daouda <daouda@mandrakesoft.com> 2.2.3-2mdk
- provides libs in %_libdir , some packages need this to build

* Mon Dec 18 2000  Daouda Lo <daouda@mandrakesoft.com> 2.2.3-2mdk
- big changes : package splitted in 4 entities
- fix gcc internal error (drawback-> -O2 opt :(
- merge with big dadou cleanups
- lib policy
- Enable libmng support
- Enable threads
- Rewrite spec to make it LMDK compliant
- Remove doc packages (most of doc is in devel package now)
- Remove rpath
- Libdification
- Add longtitle to Qt Designer menu entry
- Fix groups
- Make rpmlint happy (at least, nearly)

* Thu Nov 23 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2.2-2mdk
- Update to 2.2.2 package on cooker.

* Tue Nov 21 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2.2-1mdk
- Update to 2.2.2 package

* Wed Nov  8 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.1-5mdk
- Add gcc2.96 patches from redhat.

* Thu Nov 02 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2.1-4mdk
- Added msg2qm utility back per request from Cookers
- Recompile for gcc 2.96

* Tue Oct 24 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2.1-3mdk
- Attempting to fix patch so that it builds on it's own (I can not use RCS
  patches that are sent to me).
- Rebuild with no exceptions

* Mon Oct 23 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2.1-2mdk
- Added patch 0 from David Faure

* Fri Oct 06 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2.1-1mdk
- Update to 2.2.1 package

* Mon Sep 25 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-4mdk
- Some KDE related patches

* Fri Sep 22 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-3mdk
- Some KDE related patches

* Thu Sep 07 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-2mdk
- Changed liscense from QPL to GPL

* Thu Sep 07 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-1mdk
- Upgraded to final realease version

* Fri Aug 25 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-0.7mdk
- Some KDE related patches

* Mon Aug 21 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-0.6mdk
- Some KDE related patches

* Sat Aug 19 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-0.5mdk
- Some KDE related patches

* Wed Aug 16 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-0.4mdk
- Some KDE related patches

* Fri Aug 11 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-0.3mdk
- Fixed designer templates and support files in devel package.
- Added menu for designer

* Thu Aug 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-0.2mdk
- Fixed location of docs
- Fixed designer location and location of libs required by designer.

* Tue Aug 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.2-0.1mdk
- Updated to qt2 2.2 beta 1 as required by KDE
- Updated code

* Sat Jul 29 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.1-10mdk
- Some KDE related patches

* Fri Jul 28 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.1-9mdk
- Some KDE related patches

* Wed Jul 19 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.1-8mdk
- This is 2.2beta0
- Updated code patches
- BM

* Tue Jul 18 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.1-7mdk
- Updated code patches

* Mon Jul 17 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.1-6mdk
- Updated again some more patches by the kde2 team

* Sun Jul 16 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.1-5mdk
- Updated again some patches for kde2

* Sat Jul 15 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.1-4mdk
- Updated some patches for KDE
- be pedantic and add some symlinks to /usr/bin
- fixed long standing unfixed typo
- package is not relocatable (???)
- NOTE: package maintainer remains: molnarc@mandrakesoft.com

* Mon Jun 19 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.1-2mdk
- Updated spec file to save room. New spec file sent by cooker user
- taki@cloud.matav.sulinet.hu

* Fri Jun 02 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.1-1mdk
- updated to qt2.1.1

* Mon May 15 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.0-6mdk
- recompiled with jpeg support needed by kde2

* Sat May  6 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.1.0-5mdk
- fixed conflicting files in qt2 and qt2-devel

* Mon Apr 17 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.0-4mdk
- changed back to QTDIR being /usr/lib/qt2

* Sun Apr 16 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.0-3mdk
- bowed to a bunch of email complaints and moved the development dir
  from /usr/lib/qt2/... to /usr/include/qt2/.... QTDIR=/usr/include/qt2

* Sat Apr 15 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.0-2mdk
- Fixed a missing libqt2.so link.

* Fri Apr 14 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1.0-1mdk
- Update to release version 2.1.0

* Fri Mar 24 2000 David Faure <david@mandrakesoft.com> 2.1.0-0.3.1mdk
- Upgraded to 2.1 beta 3
- Removed libqimgio2, now part of qt
- Changed installation directories to respect a QTDIR (/usr/lib/qt-2.1.0)
- Allows to keep Qt 2.0 and Qt 1.x around.
- Removed BuildArchitectures hack.

* Wed Jan 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.0.1-10mdk
- BuildArchitectures only on non-x86.

* Tue Jan 18 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0.1-9mdk
- removed BuildArchitecture

* Sat Oct 23 1999 Stefan van der Eijk <s.vandereijk@chello.nl>
- Add "alpha" as build architecture (pixel's rebuild)

* Mon Sep 20 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Add libqgl2.a and libqimgio2.a to make KDE 2.0 happy
- replace qstrlist.h with a version that works
- rename /usr/lib/libqt.a to /usr/lib/libqt2.a to avoid conflict with
  qt 1.44
- Add libqt2.so link to libqt.so.2 so we can do -lqt2

* Tue Jul 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- First version for Mandrake distribution.
