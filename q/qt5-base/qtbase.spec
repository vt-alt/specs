%define IF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define IF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define IF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define IF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"
%define IF_ver_eq() %if "%(rpmvercmp '%1' '%2')" == "0"
%define IF_ver_not_gt() %if "%(rpmvercmp '%1' '%2')" <= "0"
%define IF_ver_not_gteq() %if "%(rpmvercmp '%1' '%2')" < "0"
%define IF_ver_not_lt() %if "%(rpmvercmp '%2' '%1')" <= "0"
%define IF_ver_not_lteq() %if "%(rpmvercmp '%2' '%1')" < "0"
%define IF_ver_not_eq() %if "%(rpmvercmp '%1' '%2')" != "0"

#def_enable qtchooser
%def_disable bootstrap
%def_enable sql_pgsql
%def_enable sql_odbc
%def_enable sql_ibase
%def_disable sql_tds
%def_disable sql_sqlite2
%def_enable pulse
%def_disable journald

%define platform linux-g++
%define graphicssystem raster
%ifarch %arm
%define opengl_type es2
%else
%define opengl_type desktop
%endif
%define harfbuzz_req 2.0
%define harfbuzz_ver %{get_version libharfbuzz-devel}

%global qt_module  qtbase
%define gname  qt5
Name: qt5-base
%define major  5
Version: 5.12.5
Release: alt1
%define libname  lib%gname

Group: System/Libraries
Summary: Qt%major - QtBase components
License: LGPLv2 with exceptions / GPLv3 with exceptions
Url: http://qt.io/

Source: %qt_module-everywhere-src-%version.tar
Source1: rpm-macros
Source2: rpm-macros-addon
# FC
Patch1: qtbase-opensource-src-5.7.1-QT_VERSION_CHECK.patch
Patch2: qtbase-opensource-src-5.7.1-moc_macros.patch
# bugreports.qt.io
Patch11: QTBUG-35459.patch
Patch12: xcberror_filter.patch
# upstream
# SuSE
Patch100: disable-rc4-ciphers-bnc865241.diff
# ALT
Patch1000: alt-sql-ibase-firebird.patch
Patch1001: alt-enable-ft-lcdfilter.patch
Patch1002: alt-dont-require-plugin-file.patch
Patch1003: alt-ca-certificates-path.patch
Patch1004: alt-timezone.patch
Patch1005: alt-hidpi_scale_at_192.patch
Patch1006: e2k-qt-5.12.4.patch
Patch1007: alt-decrease-iconloader-fallback-depth.patch
Patch1008: alt-mkspecs-features.patch
Patch1009: alt-false-detect-groupswitchmodifier.patch

# macros
%define _qt5 %gname
%include %SOURCE1

# dynamically probing plugins
%add_findreq_skiplist %_qt5_plugindir/platformthemes/*.so

# Automatically added by buildreq on Fri Sep 20 2013 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel glibc-devel-static gstreamer-devel libEGL-devel libGL-devel libX11-devel libXext-devel libXfixes-devel libXrender-devel libatk-devel libcairo-devel libcom_err-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgst-plugins libkrb5-devel libpango-devel libpng-devel libpq-devel libssl-devel libstdc++-devel libwayland-client libwayland-server libxcb-devel libxcb-render-util libxcbutil-icccm libxcbutil-image libxcbutil-keysyms libxml2-devel pkg-config python-base python3 python3-base ruby ruby-stdlibs xorg-fixesproto-devel xorg-inputproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: firebird-devel gcc-c++ gst-plugins-devel libXi-devel libalsa-devel libcups-devel libdbus-devel libfreetds-devel libgtk+2-devel libicu-devel libjpeg-devel libmysqlclient-devel libpcre-devel libpulseaudio-devel libsqlite3-devel libudev-devel libunixODBC-devel libxcb-render-util-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel postgresql-devel python-module-distribute rpm-build-python3 rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): libharfbuzz-devel
BuildRequires: gcc-c++ libcups-devel libdbus-devel libicu-devel libjpeg-devel libpng-devel
BuildRequires: libproxy-devel libssl-devel
BuildRequires: libpcre2-devel libudev-devel libEGL-devel libdrm-devel libgbm-devel zlib-devel libgtk+3-devel
BuildRequires: libmtdev-devel libinput-devel libts-devel
BuildRequires: pkgconfig(gl) pkgconfig(glesv2) pkgconfig(egl)
BuildRequires: libSM-devel libICE-devel
BuildRequires: libX11-devel libXi-devel libxkbcommon-devel libxkbcommon-x11-devel
BuildRequires: libxcb-render-util-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel
BuildRequires: libalsa-devel
BuildRequires: libat-spi2-core-devel
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}
%{?_enable_journald:BuildRequires: pkgconfig(libsystemd-journal)}
%{?_enable_sql_tds:BuildRequires: libfreetds-devel}
%{?_enable_sql_ibase:BuildRequires: firebird-devel}
%{?_enable_sql_odbc:BuildRequires: libunixODBC-devel}
%{?_enable_sql_pgsql:BuildRequires: postgresql-devel libpq-devel libecpg-devel-static}
%{?_enable_sql_sqlite2:BuildRequires: libsqlite-devel}
BuildRequires: libmysqlclient-devel
BuildRequires: libsqlite3-devel
%if_disabled bootstrap
BuildRequires: qt5-base-devel qt5-tools
%endif
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel

%description
Qt is a software toolkit for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package common
Summary: Common package for Qt%major
Group: System/Configuration/Other
Requires: common-licenses
%description common
Common package for Qt%major

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: pkgconfig(gl) pkgconfig(egl)
Requires: rpm-macros-%gname = %EVR
Requires: gcc-c++
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package -n rpm-macros-%gname
Summary: Set of RPM macros for packaging Qt%major-based applications
Group: Development/KDE and QT
BuildArch: noarch
Requires: %name-common = %version-%release
%description -n rpm-macros-%gname
Set of RPM macros for packaging Qt%major-based applications for %distribution
Install this package if you want to create RPM packages that use Qt%major

%package static
Group: Development/KDE and QT
Summary: Static library files for %name
Requires: %name-devel = %EVR
Requires: pkgconfig(fontconfig)
Requires: pkgconfig(glib-2.0)
Requires: pkgconfig(zlib)
%description static
%summary.

%package doc
Summary: Document for developing apps which will use Qt%{major}
Group: Development/KDE and QT
Requires: %name-common = %EVR
#Requires: %gname-assistant
%description doc
This package contains documentation and sources for example programs.

%package -n qt5-qtbase
Summary: qt5-qtbase compatibility package
Group: System/Libraries
BuildArch: noarch
Requires: lib%{gname}-concurrent
Requires: lib%{gname}-core
Requires: lib%{gname}-dbus
Requires: lib%{gname}-network
Requires: lib%{gname}-sql
Requires: lib%{gname}-test
Requires: lib%{gname}-xml
%description -n qt5-qtbase
qt5-qtbase compatibility package

%package -n qt5-qtbase-gui
Summary: qt5-qtbase-gui compatibility package
Group: System/Libraries
BuildArch: noarch
Requires: lib%{gname}-gui
Requires: lib%{gname}-opengl
Requires: lib%{gname}-printsupport
Requires: lib%{gname}-widgets
Requires: lib%{gname}-xcbqpa
Provides: qt5-qtbase-x11 = %version-%release
%description -n qt5-qtbase-gui
qt5-qtbase-gui compatibility package

%package -n %gname-sql
BuildArch: noarch
Group: System/Libraries
Summary: Meta-package for SQL support of Qt%major GUI toolkit
Requires: %name-common = %EVR
Requires: %gname-sql-mysql = %EVR
Requires: %gname-sql-sqlite = %EVR
%{?_enable_sql_ibase:Requires: %gname-sql-interbase = %EVR}
%{?_enable_sql_pgsql:Requires: %gname-sql-postgresql = %EVR}
%{?_enable_sql_odbc:Requires: %gname-sql-odbc = %EVR}
%{?_enable_sql_tds:Requires: %gname-sql-tds = %EVR}
%{?_enable_sql_sqlite2:Requires: %gname-sql-sqlite2 = %EVR}
%description -n %gname-sql
Meta-package for SQL support of Qt%major GUI toolkit

%package -n %gname-sql-odbc
Summary: ODBC drivers for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-odbc
ODBC driver for Qt's SQL classes (QODBC)

%package -n %gname-sql-tds
Summary: FreeTDS(Sybase) driver for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-tds
FreeTDS(Sybase) driver for Qt's SQL classes (QTDS)

%package -n %gname-sql-mysql
Summary: MySQL driver for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-mysql
MySQL driver for Qt's SQL classes (QMYSQL)

%package -n %gname-sql-postgresql
Summary: PostgreSQL drivers for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-postgresql
PostgreSQL driver for Qt's SQL classes (QPSQL)

%package -n %gname-sql-interbase
Summary: InterBase drivers for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-interbase
InterBase driver for Qt's SQL classes (QIBASE)

#%package -n %gname-sql-sqlite
#Summary: SQLite driver for Qt%major SQL classes
#Group: System/Libraries
#Requires: %name-common = %EVR
#Provides: %gname-plugin-sql = %EVR
#%description -n %gname-sql-sqlite
#SQLite driver for Qt's SQL classes (QSQLITE)

%package -n %gname-sql-sqlite2
Summary: SQLite2 driver for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-sqlite2
SQLite2 driver for Qt's SQL classes (QSQLITE2)

%package -n lib%{gname}-sql
Summary: SQL support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
# sqlite plugin included
Provides: %gname-plugin-sql = %EVR
Provides: %gname-sql-sqlite = %EVR
%description -n lib%{gname}-sql
SQL support library for the Qt%major toolkit

%package -n lib%{gname}-core
Summary: Core library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
Requires: glibc-gconv-modules
%description -n lib%{gname}-core
Core library for the Qt%major toolkit

%package -n lib%{gname}-gui
Summary: GUI support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-gui
GUI support library for the Qt%major toolkit

%package -n lib%{gname}-dbus
Summary: DBus support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-dbus
DBus support library for the Qt%major toolkit

%package -n lib%{gname}-network
Summary: Network support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-network
Network support library for the Qt%major toolkit

%package -n lib%{gname}-opengl
Summary: OpenGL support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-opengl
OpenGL support library for the Qt%major toolkit

%package -n lib%{gname}-xml
Summary: XML support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-xml
XML support library for the Qt%major toolkit

%package -n lib%{gname}-concurrent
Summary: Multi-threading concurrence support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-concurrent
Multi-threading concurrence support library for the Qt%major toolkit

%package -n lib%{gname}-printsupport
Summary: Printing support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-printsupport
Printing support library for the Qt%major toolkit

%package -n lib%{gname}-test
Summary: Testing support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-test
Testing support library for the Qt%major toolkit

%package -n lib%{gname}-widgets
Summary: Widgets library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-widgets
Widgets library for the Qt%major toolkit

%package -n lib%{gname}-eglfsdeviceintegration
Summary: EGL integration library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-eglfsdeviceintegration
EGL integration library for the Qt%major toolkit

%package -n lib%{gname}-xcbqpa
Summary: EGL integration library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-xcbqpa
EGL integration library for the Qt%major toolkit

%package -n lib%{gname}-eglfskmssupport
Summary: EGL integration library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-eglfskmssupport
EGL integration library for the Qt%major toolkit

%prep
%define icu_ver %{get_version libicu-devel}
%IF_ver_gteq %icu_ver 5.9
%def_enable system_icu
%else
%def_disable system_icu
%endif

%setup -n %qt_module-everywhere-src-%version
%patch1 -p1
%patch2 -p1
#
%patch11 -p1 -b .QTBUG
#%patch12 -p1
#
%patch100 -p1
#
%patch1000 -p1 -b .ibase
#%patch1001 -p1 -b .lcd
%patch1002 -p1 -b .plugin-file
%patch1003 -p1 -b .ca-bundle
%patch1004 -p1 -b .timezone
#%patch1005 -p1 -b .hidpi-scale
%ifarch %e2k
%patch1006 -p1 -b .e2k
%endif
%patch1007 -p1
%patch1008 -p1
%patch1009 -p1

# install optflags
%add_optflags %optflags_shared
sed -i "s|^\s*QMAKE_CFLAGS_OPTIMIZE\s*=.*$|QMAKE_CFLAGS_OPTIMIZE = %optflags|" mkspecs/common/gcc-base.conf
QMAKE_CFLAGS_OPTIMIZE_FULL=`echo %optflags | sed 's|-O[[:digit:]]||'`
QMAKE_CFLAGS_OPTIMIZE_FULL+=" -O3"
sed -i "s|^\s*QMAKE_CFLAGS_OPTIMIZE_FULL\s*=.*$|QMAKE_CFLAGS_OPTIMIZE_FULL = $QMAKE_CFLAGS_OPTIMIZE_FULL|" mkspecs/common/gcc-base.conf

#sed -i -e "s|^\(QMAKE_LFLAGS_RELEASE.*\)|\1 $RPM_LD_FLAGS|" \
#  mkspecs/common/g++-unix.conf

# remove some bundled libs to ensure they're not accidentally used
pushd src/3rdparty
rm -rf freetype libjpeg libpng zlib xcb
popd

%build
unset QTDIR QTLIB QTINC
export QT_DIR="$PWD"
export PATH=$QT_DIR/bin:$PATH
export LD_LIBRARY_PATH=$QT_DIR/lib:$LD_LIBRARY_PATH
export QT_PLUGIN_PATH=$QT_DIR/plugins

./configure -v \
    -opensource \
    -confirm-license \
    -prefix %_qt5_prefix \
    -archdatadir %_qt5_archdatadir \
    -bindir %_qt5_bindir \
    -datadir %_qt5_datadir \
    -docdir %_qt5_docdir \
    -examplesdir %_qt5_examplesdir \
    -headerdir %_qt5_headerdir \
    -importdir %_qt5_importdir \
    -qmldir %_qt5_qmldir \
    -libdir %_qt5_libdir \
    -libexecdir %_qt5_libexecdir \
    -plugindir %_qt5_plugindir \
    -sysconfdir %_qt5_sysconfdir \
    -translationdir %_qt5_translationdir \
    -platform %platform \
    -release \
    -shared \
    -pkg-config \
    -optimized-qmake \
    -accessibility \
    -dbus-linked \
    -fontconfig \
    -glib \
    -gtk \
%if_enabled system_icu
    -icu \
    -no-iconv \
%else
    -no-icu \
    -iconv \
%endif
    -openssl-linked \
    -libproxy \
    -make examples \
    -no-compile-examples \
    -nomake tests \
    -make tools \
    -no-pch \
    -no-rpath \
    -no-separate-debug-info \
    -no-strip \
    -no-use-gold-linker \
%ifarch %ix86
    -no-sse2 \
%endif
%ifarch %ix86 x86_64
    -reduce-relocations \
%else
    -no-reduce-relocations \
%endif
    -opengl %opengl_type -egl -eglfs -kms \
    -system-sqlite \
    %{?_enable_sql_tds:-plugin-sql-tds}%{!?_enable_sql_tds:-no-sql-tds} \
    %{?_enable_sql_ibase:-plugin-sql-ibase}%{!?_enable_sql_ibase:-no-sql-ibase} \
    %{?_enable_sql_pgsql:-plugin-sql-psql}%{!?_enable_sql_pgsql:-no-sql-psql} \
    %{?_enable_sql_sqlite2:-plugin-sql-sqlite2}%{!?_enable_sql_sqlite2:-no-sql-sqlite2} \
    %{?_enable_sql_odbc:-plugin-sql-odbc}%{!?_enable_sql_odbc:-no-sql-odbc} \
    -system-libjpeg \
    -system-libpng \
    -system-pcre \
    -system-zlib \
%IF_ver_gteq %harfbuzz_ver %harfbuzz_req
    -system-harfbuzz \
%else
    -qt-harfbuzz \
%endif
    -sm -xcb -xcb-xinput -system-xcb \
    -xkb -xkbcommon \
    #

%make_build
%if_disabled bootstrap
[ -d doc/qtcore ] || %make docs ||:
%endif

%install
make install INSTALL_ROOT=%buildroot
%if_disabled bootstrap
[ -d doc/qtcore ] && %make INSTALL_ROOT=%buildroot install_docs ||:
%endif

# uninstall optflags
sed -i "s|^\s*QMAKE_CFLAGS_OPTIMIZE\s*=.*$|QMAKE_CFLAGS_OPTIMIZE = -O2|" %buildroot%_qt5_archdatadir/mkspecs/common/gcc-base.conf
sed -i "s|^\s*QMAKE_CFLAGS_OPTIMIZE_FULL\s*=.*$|QMAKE_CFLAGS_OPTIMIZE_FULL = -O3|" %buildroot%_qt5_archdatadir/mkspecs/common/gcc-base.conf

# create/own dirs
mkdir -p %buildroot/{%_qt5_archdatadir/mkspecs/modules,%_qt5_importdir,%_qt5_qmldir,%_qt5_libexecdir,%_qt5_translationdir,%_qt5_docdir,%_qt5_examplesdir}
mkdir -p %buildroot/%_qt5_plugindir/{accessible,iconengines,script,styles}/

# debug logging config
mkdir -p %buildroot/%_sysconfdir/qt5/
cat >%buildroot/%_sysconfdir/qt5/qtlogging.ini <<__EOF__
[Rules]
*.debug=false
qt.qpa.xcb.xcberror.warning=false
__EOF__
ln -s `relative %_sysconfdir/qt5/qtlogging.ini %_qt5_datadir/qtlogging.ini` %buildroot/%_qt5_datadir/qtlogging.ini

# remove .la files
rm -rf %buildroot/%_qt5_libdir/*.la

# .pc
mkdir -p %buildroot/%_pkgconfigdir/
cat >%buildroot/%_pkgconfigdir/Qt%major.pc<<__EOF__
prefix=%_qt5_prefix
archdatadir=%_qt5_archdatadir
bindir=%_qt5_bindir
datadir=%_qt5_datadir

docdir=%_qt5_docdir
examplesdir=%_qt5_examplesdir
headerdir=%_qt5_headerdir
importdir=%_qt5_importdir
qmldir=%_qt5_qmldir
libdir=%_qt5_libdir
libexecdir=%_qt5_libexecdir
moc=%_qt5_bindir/moc
plugindir=%_qt5_plugindir
qmake=%_qt5_bindir/qmake
settingsdir=%_qt5_settingsdir
sysconfdir=%_qt5_sysconfdir
translationdir=%_qt5_translationdir

Name: Qt%major
Description: Qt%major Configuration
Version: 5.12.5
__EOF__

# rpm macros
install -d -m 0755 %buildroot/%_rpmmacrosdir/
cat >%buildroot/%_rpmmacrosdir/%gname <<__EOF__
%%_qt5 %_qt5
%%_qt5_epoch %{?epoch}%{!?epoch:0}
%%_qt5_version %version
%%_qt5_evr %EVR
__EOF__
cat %SOURCE1 | sed 's|define[[:space:]][[:space:]]*||' >>%buildroot/%_rpmmacrosdir/%gname
cat %SOURCE2 >>%buildroot/%_rpmmacrosdir/%gname

# create compatibility symlinks to dirs
for d in imports libexec mkspecs plugins ; do
ln -s `relative %_qt5_archdatadir/$d %_qt5_prefix/$d` %buildroot/%_qt5_prefix/$d
done
ln -s `relative %_qt5_docdir %_qt5_prefix/doc` %buildroot/%_qt5_prefix/doc

# install binaries to %_bindir
mkdir %buildroot/%_bindir
ls -1d %buildroot/%_qt5_bindir/* | \
while read f ; do
    [ -f "$f" ] || continue
    fname=`basename $f`
    mv $f %buildroot/%_bindir/$fname-%gname
    ln -s `relative %_bindir/$fname-%gname %_qt5_bindir/$fname-%gname` %buildroot/%_qt5_bindir/$fname
done

# qtchooser conf
%if_enabled qtchooser
  mkdir -p %buildroot%_sysconfdir/xdg/qtchooser
  pushd    %buildroot%_sysconfdir/xdg/qtchooser
    echo "%_qt5_bindir" >  %{gname}.conf
    echo "%_qt5_prefix" >> %{gname}.conf
  popd
%endif

## .prl/.la files
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %buildroot/%_qt5_libdir
for prl_file in libQt%{major}*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

# install libs into qt prefix
mkdir -p %buildroot/%_qt5_prefix/lib
ls -1d %buildroot/%_qt5_libdir/*.{a,so,prl} 2>/dev/null | \
while read f ; do
    [ -d "$f" ] && continue
    fname=`basename $f`
    ln -s `relative $f %buildroot/%_qt5_prefix/lib/$fname` %buildroot/%_qt5_prefix/lib/$fname
done
# link includes into qt prefix
ln -s `relative %buildroot/%_qt5_headerdir %buildroot/%_qt5_prefix/include` %buildroot/%_qt5_prefix/include


%if 0%{?qtchooser}
%files
# not editable config files, so not using %%config here
%dir %_sysconfdir/xdg/qtchooser
%_sysconfdir/xdg/qtchooser/*.conf
%endif

%files -n qt5-qtbase
%files -n qt5-qtbase-gui

%files common
%doc LICENSE.*
%dir %_sysconfdir/qt5/
%dir %_qt5_docdir/
%dir %_qt5_archdatadir/
%dir %_qt5_examplesdir/
%dir %_qt5_importdir/
%dir %_qt5_qmldir/
%dir %_qt5_translationdir/
%dir %_qt5_prefix/
%dir %_qt5_prefix/doc/
%dir %_qt5_prefix/imports/
%dir %_qt5_prefix/lib/
%dir %_qt5_prefix/libexec/
%dir %_qt5_prefix/plugins/
%if "%_qt5_prefix" != "%_qt5_datadir"
%dir %_qt5_datadir/
%endif
%dir %_qt5_libexecdir/
%dir %_qt5_plugindir/
%dir %_qt5_plugindir/accessible/
%dir %_qt5_plugindir/bearer/
%dir %_qt5_plugindir/egldeviceintegrations/
%dir %_qt5_plugindir/generic/
%dir %_qt5_plugindir/iconengines/
%dir %_qt5_plugindir/imageformats/
%dir %_qt5_plugindir/platforminputcontexts/
%dir %_qt5_plugindir/platforms/
%dir %_qt5_plugindir/platformthemes/
%dir %_qt5_plugindir/printsupport/
%dir %_qt5_plugindir/script/
%dir %_qt5_plugindir/sqldrivers/
%dir %_qt5_plugindir/styles/
%dir %_qt5_plugindir/xcbglintegrations/
%config(noreplace) %_sysconfdir/qt5/qtlogging.ini
%_qt5_datadir/qtlogging.ini

%files doc
%if_disabled bootstrap
%doc %_qt5_docdir/*
%exclude %_qt5_docdir/global/
%endif
%_qt5_examplesdir/*

%files -n rpm-macros-%gname
%_rpmmacrosdir/%gname

%files devel
%_qt5_docdir/global/
%dir %_qt5_bindir
%_bindir/moc*
%_qt5_bindir/moc*
%_bindir/qdbuscpp2xml*
%_qt5_bindir/qdbuscpp2xml*
%_bindir/qdbusxml2cpp*
%_qt5_bindir/qdbusxml2cpp*
%_bindir/fixqt4headers.pl*
%_qt5_bindir/fixqt4headers.pl*
%_bindir/qmake*
%_qt5_bindir/qmake*
%_bindir/rcc*
%_qt5_bindir/rcc*
%_bindir/syncqt*
%_qt5_bindir/syncqt*
%_bindir/uic*
%_qt5_bindir/uic*
%_bindir/qlalr*
%_qt5_bindir/qlalr*
%_bindir/qvkgen*
%_qt5_bindir/qvkgen*
%dir %_qt5_headerdir
%dir %_qt5_prefix/include/
%_qt5_headerdir/Qt*/
%dir %_qt5_prefix/mkspecs/
%_qt5_archdatadir/mkspecs/
%_qt5_prefix/lib/libQt%{major}*.prl
%_qt5_libdir/libQt%{major}*.prl
%_qt5_prefix/lib/libQt%{major}*.so
%_qt5_libdir/libQt%{major}*.so
%dir %_qt5_libdir/cmake/
%_qt5_libdir/cmake/Qt%{major}*/
%_pkgconfigdir/Qt%{major}.pc
%_pkgconfigdir/Qt%{major}Concurrent.pc
%_pkgconfigdir/Qt%{major}Core.pc
%_pkgconfigdir/Qt%{major}DBus.pc
%_pkgconfigdir/Qt%{major}Gui.pc
%_pkgconfigdir/Qt%{major}Network.pc
%_pkgconfigdir/Qt%{major}OpenGL.pc
%_pkgconfigdir/Qt%{major}PrintSupport.pc
%_pkgconfigdir/Qt%{major}Sql.pc
%_pkgconfigdir/Qt%{major}Test.pc
%_pkgconfigdir/Qt%{major}Widgets.pc
%_pkgconfigdir/Qt%{major}Xml.pc

%files devel-static
%_qt5_libdir/libQt%{major}*.a
%_qt5_prefix/lib/libQt%{major}*.a
%_pkgconfigdir/Qt%{major}OpenGLExtensions.pc

%files -n %gname-sql

# packaged with sql library
#%if_enabled sql_sqlite
#%files -n %gname-sql-sqlite
#%_qt5_plugindir/sqldrivers/libqsqlite.so
#%endif

%if_enabled sql_ibase
%files -n %gname-sql-interbase
%_qt5_plugindir/sqldrivers/libqsqlibase.so
%endif

%files -n %gname-sql-mysql
%_qt5_plugindir/sqldrivers/libqsqlmysql.so

%if_enabled sql_odbc
%files -n %gname-sql-odbc
%_qt5_plugindir/sqldrivers/libqsqlodbc.so
%endif

%if_enabled sql_pgsql
%files -n %gname-sql-postgresql
%_qt5_plugindir/sqldrivers/libqsqlpsql.so
%endif

%if_enabled sql_tds
%files -n %gname-sql-tds
%_qt5_plugindir/sqldrivers/libqsqltds.so
%endif

%if_enabled sql_sqlite2
%files -n %gname-sql-sqlite2
%_qt5_plugindir/sqldrivers/libqsqlite2.so
%endif

%files -n lib%{gname}-core
%_qt5_libdir/libQt%{major}Core.so.*

%files -n lib%{gname}-concurrent
%_qt5_libdir/libQt%{major}Concurrent.so.*

%files -n lib%{gname}-dbus
%_qt5_libdir/libQt%{major}DBus.so.*

%files -n lib%{gname}-gui
%_qt5_libdir/libQt%{major}Gui.so.*
%_qt5_plugindir/egldeviceintegrations/*
%_qt5_plugindir/generic/*
%_qt5_plugindir/imageformats/*
%_qt5_plugindir/platforminputcontexts/*
%_qt5_plugindir/platforms/*
%_qt5_plugindir/platformthemes/*
%_qt5_plugindir/xcbglintegrations/*

%files -n lib%{gname}-network
%_qt5_libdir/libQt%{major}Network.so.*
%_qt5_plugindir/bearer/*

%files -n lib%{gname}-opengl
%_qt5_libdir/libQt%{major}OpenGL.so.*

%files -n lib%{gname}-printsupport
%_qt5_libdir/libQt%{major}PrintSupport.so.*
%_qt5_plugindir/printsupport/*

%files -n lib%{gname}-sql
%_qt5_libdir/libQt%{major}Sql.so.*
%_qt5_plugindir/sqldrivers/libqsqlite.so

%files -n lib%{gname}-test
%_qt5_libdir/libQt%{major}Test.so.*

%files -n lib%{gname}-widgets
%_qt5_libdir/libQt%{major}Widgets.so.*
#%_qt5_plugindir/accessible/*

%files -n lib%{gname}-xml
%_qt5_libdir/libQt%{major}Xml.so.*

%files -n lib%{gname}-eglfsdeviceintegration
%_qt5_libdir/libQt%{major}EglFSDeviceIntegration.so.*

%files -n lib%{gname}-xcbqpa
%_qt5_libdir/libQt%{major}XcbQpa.so.*

%files -n lib%{gname}-eglfskmssupport
%_qt5_libdir/libQt%{major}EglFsKmsSupport.so.*


%changelog
* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt4
- add fix against QTBUG-49771 (thanks darktemplar@alt)

* Mon Aug 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt3
- fix to build with old libharfbuzz

* Mon Aug 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt2
- don't fail whan compile docs

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Mon Mar 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Mon Mar 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt3
- build with new libmysqlclient

* Thu Feb 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt2
- package examples

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Wed Oct 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt3
- rebuild with new icu

* Wed Oct 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.11.2-alt2%ubt
- NMU: fixed debuginfo generation.

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Wed Aug 29 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt3%ubt
- link with openssl

* Thu Aug 16 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt2%ubt
- build docs

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1%ubt
- new version

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt2%ubt
- rebuild with new icu

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1%ubt
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Wed Mar 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt.2
- build docs

* Mon Feb 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt.1
- use iconv with icu < 60
- don't build docs

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Mon Oct 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt2%ubt
- build docs

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Thu Oct 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt14%ubt
- decrease iconloader fallback icon names depth

* Fri Aug 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt13%ubt
- fix compile qt-based apps with lcc compiler

* Tue Aug 22 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt12%ubt
- add e2k support

* Fri Aug 18 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt11%ubt
- revert previous changes

* Thu Aug 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt10%ubt
- fix hidpi scaling when factor == 1

* Fri Jul 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt9%ubt
- sync patches with FC

* Fri Jun 30 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt8%ubt
- disable debug messages via /usr/share/qt5/qtlogging.ini by default

* Mon Jun 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt7%ubt
- fix to build with session management

* Mon Jun 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt6.S1
- ignore GTK3 dependencies

* Fri Jun 02 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt5%ubt
- fix calculate pixel density

* Thu Jun 01 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt4%ubt
- calculate pixel density like GNOME

* Wed Mar 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt3%ubt
- disable debug output by default
- update SuSE patches

* Wed Mar 22 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt2%ubt
- rebuild

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1%ubt
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Thu Jul 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt3
- update SuSE patches

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt2
- build with egldevice support

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Fri Mar 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt9
- fix detect timezone

* Mon Feb 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt7
- fix find ca-bundle.crt

* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt6
- disable annoing qdbusconnection debug mesaage

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt5
- add patches against crashes when disconnect displays

* Thu Dec 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt4
- add qt5-qtbase-gui and qt5-qtbase compat packages

* Thu Oct 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt3
- sync SuSE patches

* Fri Oct 23 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- build docs

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Tue Oct 13 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt4
- make rpm-macros package noarch (ALT#31357)

* Tue Jul 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt3
- link include directory to qt prefix

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt2
- build docs

* Fri Jul 03 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt3
- 5.4.2 release

* Mon Jun 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt2
- build docs

* Fri Jun 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed May 13 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt3
- add %%installqt5
- add some dirs to common package

* Thu Apr 02 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt2
- build docs

* Tue Feb 24 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 23 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt3
- fix build requires

* Mon Dec 22 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt2
- build docs

* Thu Dec 11 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt2
- build docs

* Tue Sep 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Wed Aug 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt7
- build docs

* Tue Aug 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt6
- rebuild with new xcb

* Thu Jul 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt4.M70P.1
- built for M70P

* Thu Jul 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt5
- fix install_qt5 macro

* Wed Jul 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt3.M70P.1
- built for M70P

* Wed Jul 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt4
- fix qmake_qt5 macro

* Thu Jul 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt2.M70P.1
- built for M70P

* Thu Jul 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt3
- fix xcb-xkb usage (ALT#30153)

* Mon Jun 30 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1.M70P.1
- built for M70P

* Mon Jun 30 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt2
- build docs
- add _qt5_qmldir macro

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Wed Jun 04 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt2
- build docs

* Fri May 30 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Sat Mar 01 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt3.M70P.2
- build docs

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt3.M70P.1
- built for M70P

* Wed Feb 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt4
- add sql accumulating subpackage

* Tue Feb 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt3
- don't require plugin files for cmake scripts (ALT#29844)

* Thu Feb 20 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt2
- build docs

* Wed Feb 12 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Wed Nov 27 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3.M70P.1
- built for M70P

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt4
- fix crash whith xcb-1.9.3 ABI change (FDO#71507)

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2.M70P.2
- build docs

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2.M70P.1
- built for M70P

* Fri Oct 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3
- turn on freetype lcdfilter

* Thu Oct 24 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- build docs

* Mon Sep 23 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
