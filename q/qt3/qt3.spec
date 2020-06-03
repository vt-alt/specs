%define debug 0
%define qt_copy 0
%define building 0

%define _keep_libtool_files 1
%define _optlevel s
%define static_nonthr 0
%define static_thread 1
%define shared_nonthr 0
%define shared_thread 1
%define build_xt 0
%define build_qsa 1
%define build_odbc 1
%define build_sqlite 0
%define with_settings 0
%define with_nas 0
%define versioning_hack 1

# Versions
%define rname	qt
%define major	3
%define minor	3
%define bugfix	8d
%define beta	%nil
%define qsa_major 1
%define qsa_minor 1
%define qsa_bugfix 5
%define rlz alt14
Name: %rname%major
Version: %major.%minor.%bugfix
Release: %rlz
%define qsa_ver %qsa_major.%qsa_minor.%qsa_bugfix

%define qtdir	%_libdir/%rname%major
%define libname	lib%rname%major
%define kdedir  %prefix

Summary: Shared library for the Qt%major GUI toolkit
License: GPLv2 / GPLv3 / QPL
Group: System/Libraries

Url: http://www.trolltech.com/products/qt/

%if %qt_copy
Source0: qt-copy-%version%beta.tar
%else
Source0: ftp://ftp.trolltech.com/qt/source/%rname-x11-free-%version%beta.tar
%endif
%ifdef nosource
NoSource: 0
%endif
%if %with_settings
Source1: qtX-set-QTDIR-environment-csh
Source2: qtX-set-QTDIR-environment-sh
%endif
#
Source5: qtX-designer-sh
Source6: qtX-assistant-sh
Source8: qtX-README.distribution
Source9: qtX-linguist-sh
%if %with_settings
Source10: qtrc
%endif
Source11: qt-ru-3.3.2-20040604.tar
Source12: wrap_kde_malloc.cpp
#
Source21: qt3-assistant.desktop
Source22: qt3-designer.desktop
Source23: qt3-linguist.desktop
Source24: qt3-qtconfig.desktop

Source101: %rname.16.png
Source102: %rname.32.png
Source103: %rname.48.png

%if %build_qsa
Source1000: qsa-x11-free-%qsa_ver.tar
%endif

# FC
Patch2: qt-3.0.5-nodebug.patch
Patch3: qt-3.3.8d-xim.patch
Patch4: qt-3.1.0-makefile.patch
Patch5: qt-x11-free-3.1.0-editor.patch
Patch6: qt-x11-free-3.1.0-assistant.patch
Patch7: qt-x11-free-3.2.2-designer.patch
Patch8: qt-x11-free-3.1.1-qmotif.patch
Patch9: qt-x11-free-3.3.8b-uic-multilib-ALT.patch
Patch10: qt-x11-free-3.1.0-header.patch
Patch11: qt-x11-free-3.3.4-mono.patch
Patch12: qt-x11-free-3.3.8d-strip.patch
Patch13: qt-x11-free-3.3.4-qfontdatabase_x11.patch
Patch14: qt-x11-free-3.3.8d-gcc4-buildkey.patch
Patch15: qt-visibility-alt.patch
Patch16: qt-x11-free-3.3.7-umask.patch
Patch17: qt-3.3.6-fontrendering-214371.patch
Patch18: qt-3.3.8-fontrendering-#214570.patch
Patch19: qt-3.3.8-fontrendering-as_IN-209972.patch

# MDK
Patch21: qt-3.0.5-fix-pyqt-config.patch
Patch22: qt3-opentype-aliasing.patch

# SuSE
Patch30: qt3-never-strip.diff
Patch31: shut-up.diff
#
Patch33: lib64-plugin-support.diff
Patch34: pluginmanager-fix.diff
#
Patch38: kmenu-search-fix.diff

# Qt-copy
Patch51: 0046-qiconview-no-useless-scrollbar.diff
Patch52: 0078-argb-visual-hack.patch
Patch53: 0088-fix-xinput-clash.diff

# ALT
Patch100: qt-3.3.3-alt-homedir.patch
Patch101: qt-3.3.0-alt-honor-SUSv3-locales.patch %{nil by raorn@alt}
Patch102: qt-3.2.3-alt-designer_add_translator.patch
Patch103: qt-3.2.3-alt-qtconfig_add_translator.patch
Patch104: qt-3.3.5-alt-buildkey-nomachine.patch
Patch105: qt-3.3.0-alt-shared_libs.patch
Patch106: qt-3.3.1-alt-iso_c_extension.patch
Patch107: qt-x11-free-3.3.6-alt-maccyrillic.patch
Patch108: qt-3.3.8d-alt-arm-no-packed-pointers.patch
Patch109: qt-x11-free-3.3.8d-Lib64.patch
Patch110: qt-3.3.8d-full-hiden-item-QIconView.patch
Patch111: qt-3.3.8d-alt-fix-build-pgsql.patch

# Sergey A. Sukiyazov <sukiyazov@mail.ru>
Patch9000: 9000-qt-x11-free-3.3.3-menubar.patch
Patch9001: 9001-qt-x11-free-3.3.3-psprinter-ALT.patch
Patch9002: 9002-qt-x11-free-3.3.6-strlist.patch
Patch9003: 9003-qt-x11-free-3.3.3-textstream.patch
Patch9004: 9004-qt-x11-free-3.3.4-uridrag.patch
Patch9005: 9005-qt-x11-free-3.3.8b-codecs.patch
Patch9006: 9006-qt-x11-free-3.3.3-codecs-utf8.patch
Patch9007: 9100-qt-x11-free-3.3.8-fix_shortcuts.patch

# security

# Automatically added by buildreq on Wed Sep 04 2002
#BuildRequires: XFree86-devel XFree86-libs freetype2-devel gcc-c++ libMySQL-devel libcups-devel libjpeg-devel liblcms libmng-devel libpng-devel libssl libstdc++-devel libunixODBC-devel postgresql-devel postgresql-libs zlib-devel

BuildRequires: libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXcursor-devel libXext-devel
BuildRequires: libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXv-devel libXft-devel libXmu-devel
BuildRequires: xorg-proto-devel
#
BuildRequires: freetype2-devel libGLU-devel
BuildRequires: libcups-devel libssl libcups-devel
BuildRequires: libbeecrypt liblcms gcc-c++ libstdc++-devel
BuildRequires: libmng-devel libjpeg-devel libpng-devel zlib-devel
BuildRequires: postgresql-devel libpq-devel libMySQL-devel
BuildRequires: bison
%if %build_sqlite
BuildRequires: sqlite-devel
%endif
%if %with_nas
BuildRequires: libaudio-devel
%endif
BuildRequires: fontconfig-devel 
%if %build_odbc
BuildRequires: libunixODBC-devel
#libiodbc-devel
%endif
#BuildRequires: libXft-devel

Requires: lib%name, %name-sql, %name-doc %name-assistant

%description
Qt is a GUI software toolkit. Qt simplifies the task of writing and maintaining
GUI (graphical user interface) applications for the X Windows system.
It has everything you need to create professional GUI applications.
And it enables you to create them quickly.
Qt is multi-platform toolkit written in C++ and is fully object-oriented.
This package contains the shared library needed to run Qt%major applications, as
well as the README files for Qt.

##############################################
%package -n lib%name
Summary: Shared library for the Qt%major GUI toolkit
Group: System/Libraries
Requires: common-licenses
%if %with_settings
Conflicts: libqt3-settings
%else
Requires: libqt3-settings = %major.%minor
%endif

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
%package -n lib%name-devel
Summary: Header files and libraries for developing apps which will use Qt%major
Group: Development/KDE and QT
PreReq: lib%name = %version-%release
Requires: freetype2-devel fontconfig-devel zlib-devel
Requires: libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXcursor-devel libXext-devel
Requires: libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXv-devel libXft-devel libXmu-devel
Requires: xorg-proto-devel
%if %with_nas
Requires: libaudio-devel
%endif
Provides: %name-devel = %version-%release, lib%name-devel-cxx = %__gcc_version_base
Obsoletes: %name-devel < %version-%release
Requires: rpm-macros-%name = %version-%release

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
Requires: lib%name-devel = %version-%release
Obsoletes: %name-devel-static

%description -n lib%name-devel-static
This package package contains the files necessary to link applications
to the Qt GUI toolkit statically (rather than dynamically).
Statically linked applications don't require the library to be installed
on the system running the application.

##############################################
%package -n lib%name-xt
Summary: An Xt (X Toolkit) compatibility add-on for the Qt GUI toolkit
Group: System/Libraries
PreReq: lib%name = %version-%release
Provides: %name-xt, %name-xt-devel, lib%name-xt-devel
Obsoletes: %name-xt, %name-xt-devel, lib%name-xt-devel
%if %static_nonthr || %static_thread
Provides: %name-xt-devel-static, lib%name-xt-devel-static
Obsoletes: %name-xt-devel-static, lib%name-xt-devel-static
%endif

%description -n lib%name-xt
An Xt (X Toolkit) compatibility add-on for the Qt GUI toolkit

##############################################
%package designer
Summary: Designer for the Qt%major
Group: Development/KDE and QT
PreReq: lib%name-devel = %version-%release
#Provides: %name-designer
#Obsoletes: %name-designer

%description designer
The package contains an User Interface designer
tool for the Qt%major toolkit.

##############################################
%package -n lib%name-styles
Summary: Extra styles for the Qt GUI toolkit
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-styles
Extra styles (themes) for the Qt GUI toolkit.

##############################################
%package -n lib%name-odbc
Summary: ODBC drivers for Qt's SQL classes
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: lib%name-plugin-sql = %version-%release

%description -n lib%name-odbc
ODBC driver for Qt's SQL classes (QSQL)

##############################################
%package sql
Group: System/Libraries
Summary: Amount package for SQL support of Qt%major GUI toolkit
Requires: lib%name-mysql
Requires: lib%name-postgresql
%if %build_sqlite
Requires: lib%name-sqlite
%endif
%if %build_odbc
Requires: lib%name-odbc
%endif
BuildArch: noarch
%description sql
Amount package for SQL support of Qt%major GUI toolkit

##############################################
%package -n lib%name-mysql
Summary: MySQL driver for Qt's SQL classes
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: lib%name-plugin-sql = %version-%release

%description -n lib%name-mysql
MySQL driver for Qt's SQL classes (QSQL)

##############################################
%package -n lib%name-postgresql
Summary: PostgreSQL drivers for Qt's SQL classes
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: lib%name-plugin-sql = %version-%release

%description -n lib%name-postgresql
PostgreSQL driver for Qt's SQL classes (QSQL)

##############################################
%package -n lib%name-sqlite
Summary: SQLite driver for Qt's SQL classes
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: lib%name-plugin-sql = %version-%release

%description -n lib%name-sqlite
SQLite driver for Qt's SQL classes (QSQL)

##############################################
%package doc
Summary: Document for developing apps which will use Qt%major
Group: Development/KDE and QT
#Obsoletes: %name-doc
#Provides: %rname-doc = %version-%release
Requires: lib%name-devel = %version
Requires: %name-assistant = %version
Requires: %name-doc-html = %version
Requires: %name-doc-man = %version
Requires: %name-doc-examples = %version
BuildArch: noarch

%description doc
This package contains documentation and sources for example programs.

##############################################
%package doc-html
Summary: Document for developing apps which will use Qt%major
Group: Development/KDE and QT
Conflicts: qt3-doc <= 3.3.3-alt6

%description doc-html
This package contains documentation in html format.

##############################################
%package doc-man
Summary: Document for developing apps which will use Qt%major
Group: Development/KDE and QT
Conflicts: qt3-doc <= 3.3.3-alt6
BuildArch: noarch

%description doc-man
This package contains documentation in man format.

##############################################
%package doc-examples
Summary: Examples for developing apps which will use Qt%major
Group: Development/KDE and QT
Conflicts: qt3-doc <= 3.3.3-alt6
BuildArch: noarch

%description doc-examples
This package contains sources for example programs.

##############################################
%package assistant
Summary: Assistant for the Qt%major
Group: Text tools
PreReq: lib%name = %version-%release
#Provides: %name-assistant
#Obsoletes: %name-assistant
Conflicts: qt3-doc <= 3.3.3-alt6

%description assistant
This package contains an documentation browser
for the Qt%major toolkit and Qt-based programs.

##############################################
%package -n lib%name-qsa
Summary: Qt Script for Applications (QSA)
Group: System/Libraries
Requires: lib%name >= %version-%release
%description -n lib%name-qsa
Qt Script for Applications is a framework which enables the
user to make Qt/C++ applications scriptable. The end users of the
Qt/C++ applications can modify and extend the application dynamically.

##############################################
%package -n lib%name-qsa-devel
Summary: Development files for QSA
Group: Development/KDE and QT
Requires: lib%name-qsa = %version-%release
Provides: lib%name-qsa-devel-cxx = %__gcc_version_base
%description -n lib%name-qsa-devel
Headers and other development files of
Qt Script for Applications (QSA)

##############################################
%package -n lib%name-light
Summary: Light version of Qt%major for installer
Group: System/Libraries
Conflicts: lib%name
%if %with_settings
Conflicts: libqt3-settings
%else
Requires: libqt3-settings = %major.%minor
%endif
%description -n lib%name-light
Light version of Qt%major for installer

##############################################

%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
Conflicts: libqt3-devel <= 3.3.8b-alt7
%description -n rpm-macros-%name
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep
%if %qt_copy
%define buildsubdir qt-copy-%version%beta
%else
%define buildsubdir %rname-x11-free-%version%beta
%endif

%setup -n %buildsubdir

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
# motif
#%patch8 -p1
%patch9 -p1
%patch10 -p1
# monospace
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
# visibility
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

#%patch21 -p1
%patch22 -p1

%patch30 -p0
%patch31 -p0
#
%ifarch x86_64
%patch33 -p0
%endif
%patch34 -p0
#
%patch38 -p0

%patch51 -p0
##%patch52 -p0	# Include to 3.5.13.2
%patch53 -p0

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1

# Corwin
%patch9000 -p1
%patch9001 -p1
%patch9002 -p1
#%patch9003 -p1
#%patch9004 -p1
%patch9005 -p1
%patch9006 -p1
%patch9007 -p1

%if %build_qsa
rm -rf qsa-x11*
tar xf %SOURCE1000
mv qsa-x11* qsa-x11
pushd qsa-x11/src/qsa
sed -i "s|^VERSION\s*=.*|VERSION = 0.%qsa_ver|" qsa.pro
popd
%endif

pushd translations
rm -f ./*.qm
tar xf %SOURCE11
popd

perl -pi -e "s,-O2,%optflags -DGLX_GLXEXT_LEGACY,g" mkspecs/*/qmake.conf
#perl -pi -e "s,-fpic,-fPIC,g" mkspecs/*/qmake.conf
perl -pi -e "s|-Wl,-rpath,| |" mkspecs/*/qmake.conf
#perl -pi -e "s|^CFG_NEWABI=.*|CFG_NEWABI=yes|" ./configure

rm -rf tools/designer/examples
find . -type d -name CVS| xargs rm -rf
find . -type f -name .cvsignore | xargs rm -f

# Create a qmake target for linking without libstdc++ - avoid bloat if
# possible...
#pushd mkspecs
#for i in *-g++ qws/*-g++; do
#   [ -d $i ] || continue
#   TARGET=`echo $i |sed -e 's,g++$,gcc,'`
#   cp -aR $i $TARGET
#   perl -pi -e "s,g\+\+,gcc,g;s,^(QMAKE_LIBS[[:space:]]*=.*),\1 -lsupc++,g" $TARGET/*
#done
#popd
#perl -pi -e 's,^(.*linux.*)-g\+\+(.*),\1-gcc\2,' configure
#perl -pi -e 's,^(.*CXX.*LFLAGS.*),\1 -lsupc++,' qmake/GNUmakefile.in

[ -f Makefile.cvs ] && make -f Makefile.cvs

%build
%if %versioning_hack
#if "%%__gcc_version_major" == "4"
cat > ./src/libqt_add.map <<__EOF__
CXX3 {
    global:
	extern "C++"  {
	    QObject::QObject*;
	    QString::QString*;
	};
};
__EOF__
perl -pi -e "s|^QMAKE_LFLAGS_SONAME.*|QMAKE_LFLAGS_SONAME	= -Wl,-soname, -Wl,--version-script=\\$\(QTDIR\)/src/libqt_add.map|" mkspecs/*/qmake.conf
%endif

%define platform linux-g++
%ifarch x86_64
%add_optflags -DUSE_LIB64_PATHES
%endif

export QTDIR=$(`which pwd`)
export PATH=$QTDIR/bin:$QTDIR/qmake:$PATH
export LD_LIBRARY_PATH=$QTDIR/lib:$LD_LIBRARY_PATH
export KDEDIR=%kdedir
export CFLAGS="%optflags" CXXFLAGS="%optflags"

#	-I%qtdir/include \
#	-L%qtdir/lib \
CNFGR="\
	-L/usr/X11R6/%_lib \
	-L`pwd`/Xinerama \
	-L%_libdir \
	-I%_includedir/pgsql/ -I%_includedir/mysql/ \
	-I/usr/X11R6/include/X11/Xft -I/usr/include/fontconfig \
        -prefix %qtdir \
	-bindir %qtdir/bin \
	-docdir %_docdir/qt-%version \
	-headerdir %qtdir/include \
	-libdir %_libdir \
	-plugindir %qtdir/plugins \
	-translationdir %qtdir/translations \
	\
%if %debug
	-debug \
%else
	-release \
%endif
	-platform %platform
	-largefile -stl -fast -verbose \
	-no-exceptions -no-g++-exceptions \
	\
	-system-zlib -cups -ipv6 \
%if %with_nas
	-system-nas-sound \
%else
	-no-nas-sound \
%endif
	-no-nis \
	\
        -enable-kernel -enable-tools  -enable-widgets -enable-dialogs \
	-enable-iconview -enable-workspace -enable-network -enable-canvas \
	-enable-table -enable-xml \
	\
	-enable-opengl \
	-dlopen-opengl \
	\
	-enable-sql \
	\
	-DQT_USE_APPROXIMATE_CURSORS \
	-sm -xshape -xcursor -xinerama -xrender -xrandr -xft -xkb \
	-tablet \
	\
	-qt-gif \
	-system-libpng -system-libjpeg -system-libmng \
	\
	-qt-style-windows -plugin-style-platinum \
	-plugin-style-cde -plugin-style-motifplus \
	-plugin-style-motif -plugin-style-sgi"

CNFGR_STATIC=" -static \
	-qt-sql-mysql -qt-sql-psql \
%if %build_sqlite
	-qt-sql-sqlite \
%endif
%if %build_odbc
	 -qt-sql-odbc \
%endif
	-qt-imgfmt-png -qt-imgfmt-jpeg -qt-imgfmt-mng \
	"
CNFGR_SHARED=" -shared \
	-plugin-sql-mysql -plugin-sql-psql \
%if %build_sqlite
	-plugin-sql-sqlite \
%endif
%if %build_odbc
	 -plugin-sql-odbc \
%endif
	-plugin-imgfmt-png -plugin-imgfmt-jpeg -plugin-imgfmt-mng \
	"

is_building=""

clean_but_lib()
{
[ -n "$is_building" ] || return
if [ -n "$1" ]; then
    dirsuffix="$1"
else
    dirsuffix="builded"
fi
    mkdir -p lib-"$dirsuffix"
    cp -ar lib/* lib-"$dirsuffix"
    make distclean
    rm -rf lib/*
}

# Build STATIC NON-THREADED libraries #
%if %static_nonthr
echo "yes" |./configure $CNFGR $CNFGR_STATIC -no-thread
%make_build symlinks src-qmake src-moc sub-src
%if %build_xt
%make_build -C extensions/xt/src
%endif
is_building=1
clean_but_lib
%endif #static_nonthr

# Build   STATIC THREADED   libraries #
%if %static_thread
echo "yes" |./configure $CNFGR $CNFGR_STATIC -thread
%make_build symlinks src-qmake src-moc sub-src
%if %build_xt
%make_build -C extensions/xt/src
%endif
is_building=1
clean_but_lib
%endif #static_thread

# Build SHARED NON-THREADED libraries #
%if %shared_nonthr
clean_but_lib
echo "yes" |./configure $CNFGR $CNFGR_SHARED -no-thread
%make_build symlinks src-qmake src-moc sub-src
%if %build_xt
%make_build -C extensions/xt/src
%endif
is_building=1
clean_but_lib
%endif #shared_nonthr

# Build   SHARED THREADED   libraries #
%if %shared_thread
echo "yes" |./configure $CNFGR $CNFGR_SHARED -thread
%make_build symlinks src-qmake src-moc sub-src sub-tools
%make_build -C plugins/src
#
%make_build -C tools/mergetr
%make_build -C tools/msg2qm
%make_build -C tools/qembed
%make_build -C tools/designer/tools/conv2ui
%if %build_xt
%make_build -C extensions/xt/src
%endif
#
%make_build -C examples distclean
%make_build -C tutorial distclean
#
# qsa
%if %build_qsa
pushd qsa-x11
subst "s|^SUBDIRS.*=.*|SUBDIRS = src|" ./qsa.pro
PATH=%_builddir/%buildsubdir/bin:$PATH QTDIR=%_builddir/%buildsubdir ./configure
pushd src/qsa
qmake
popd
%make_build
popd
%endif
%endif #shared_thread

# compile translations
LD_LIBRARY_PATH=./lib ./bin/lrelease ./translations/*.ts
rm -f ./translations/*_untranslated.qm

%install
%if %debug
%set_strip_method none
%endif
export QTDIR=%qtdir
export PATH=%qtdir/bin:%buildroot/%qtdir/bin:$PATH
export MANPATH=%qtdir/doc/man:$MANPATH
export LD_LIBRARY_PATH=%buildroot/%qtdir/lib:$LD_LIBRARY_PATH
export KDEDIR=%kdedir

# Work around for a broken make install
install -d -m 0755 %buildroot/%_bindir

%make INSTALL_ROOT=%buildroot install
# Work around for a broken make install
%make INSTALL_ROOT=%buildroot install -C plugins/src

rm -f %buildroot/%qtdir/bin/{moc,qmake}
cp -Lf bin/{moc,qmake} %buildroot/%qtdir/bin

ln -s ../../../%_sysconfdir/%rname%major %buildroot/%qtdir/etc
install -d -m 0755 %buildroot/%_sysconfdir/%rname%major/settings
%if %with_settings
# install config
install -m 644 %SOURCE10 %buildroot/%_sysconfdir/%rname%major/settings
%endif

# install rpm macros
install -d -m 0755 %buildroot/%_rpmmacrosdir/
cat >%buildroot/%_rpmmacrosdir/%name <<__EOF__
%%_%{name}dir %_libdir/%name
__EOF__

# install tools
install -m 775 bin/{conv2ui,findtr,qt20fix,qtrename140} %buildroot/%qtdir/bin
install -m 775 tools/mergetr/mergetr %buildroot/%qtdir/bin
install -m 775 tools/msg2qm/msg2qm %buildroot/%qtdir/bin
install -m 775 tools/qembed/qembed %buildroot/%qtdir/bin
pushd %buildroot/%qtdir/bin/
for f in `ls -1`; do
    ln -s ../..%qtdir/bin/$f %buildroot/%_bindir/$f-%name
done
popd

mv %buildroot/%qtdir/bin/designer %buildroot/%qtdir/bin/designer-real
install -m 0755 %SOURCE5 %buildroot/%qtdir/bin/designer
sed -i 's,@QTDIR@,%qtdir,g' %buildroot/%qtdir/bin/designer
#
mv %buildroot/%qtdir/bin/assistant %buildroot/%qtdir/bin/assistant-real
install -m 0755 %SOURCE6 %buildroot/%qtdir/bin/assistant
sed -i 's,@QTDIR@,%qtdir,g' %buildroot/%qtdir/bin/assistant
#
mv %buildroot/%qtdir/bin/linguist %buildroot/%qtdir/bin/linguist-real
install -m 0755 %SOURCE9 %buildroot/%qtdir/bin/linguist
sed -i 's,@QTDIR@,%qtdir,g' %buildroot/%qtdir/bin/linguist
#

# install libraries
#
mkdir -p %buildroot/%qtdir/lib/
#
%if !%build_xt
rm -f %buildroot/%_libdir/*qxt*
%endif
#
%if %static_thread
install -m0644 lib-builded/libqt-mt.a %buildroot/%_libdir/
install -m0644 lib-builded/libqt-mt.la %buildroot/%_libdir/
%endif
%if %static_nonthr
install -m0644 lib-builded/libqt.a %buildroot/%_libdir/
install -m0644 lib-builded/libqt.la %buildroot/%_libdir/
%endif
%if %build_qsa
    install -m0755 %_builddir/%buildsubdir/lib/libqsa.so.0.%qsa_major.%qsa_minor %buildroot/%_libdir
    ln -sf libqsa.so.0.%qsa_major.%qsa_minor %buildroot/%_libdir/libqsa.so
    ln -sf libqsa.so.0.%qsa_major.%qsa_minor %buildroot/%_libdir/libqsa.so.0
    ln -sf libqsa.so.0.%qsa_major.%qsa_minor %buildroot/%_libdir/libqsa.so.0.%qsa_major
    mkdir -p %buildroot/%qtdir/plugins/qsa
    #install -m 0755 %_builddir/%buildsubdir/plugins/qsa/* %buildroot/%qtdir/plugins/qsa
%endif
#
mkdir -p %buildroot/%qtdir/lib
pushd %buildroot/%_libdir
for f in lib*.so.*; do
    ln -s ../../$f %buildroot/%qtdir/lib/
    [ -f $f ] \
	&& ln -sf $f %buildroot/%qtdir/lib/`echo $f| sed "s|\(.*\.so\).*|\1|"`
done
popd
#
ln -s %name %buildroot/%_libdir/%rname-%version

# install translations
install -m 644 ./translations/*.qm %buildroot/%qtdir/translations

# move pkgconfig to right place
#mv %buildroot/%qtdir/lib/pkgconfig %buildroot/%_libdir
sed -i "s|\(-L\${libdir}\)|-L%qtdir/lib \1|" %buildroot/%_libdir/pkgconfig/*.pc

# install plugins
#install -m 0755 %_builddir/%buildsubdir/plugins/sqldrivers/*.so %buildroot/%qtdir/plugins/sqldrivers/
#install -m 0755 %_builddir/%buildsubdir/plugins/designer/*.so %buildroot/%qtdir/plugins/designer/
if [ "%_lib" == lib64 ]
then
 for i in %buildroot/%qtdir/plugins/*/*.so; do
    mv "$i" $(echo "$i"| sed "s|\.so|.lib64.so|")
 done
fi
mkdir -p %buildroot/%qtdir/plugins/crypto

# install includes
#for i in include/* include/*/*; do [ -e $i ] || rm $i; done # Get rid of windows or mac specific links
#cp -frL include/* %buildroot/%qtdir/include
install -m 0644 tools/designer/designer/database*.h %buildroot/%qtdir/include
%if %build_qsa
pushd include
> ../qsa-includes.list
> ../qsa-includes-exclude.list
for f in qs*.h
do
    if [ -L "$f" ]; then
	readlink "$f"| grep -q qsa-x11 || continue
    else
	continue
    fi
    echo "%qtdir/include/$f" >> ../qsa-includes.list
    echo "%%exclude %qtdir/include/$f" >> ../qsa-includes-exclude.list
    install -m0644 $f %buildroot/%qtdir/include/$f
done
popd
%endif
mkdir -p %buildroot/%_includedir
ln -s %qtdir/include %buildroot/%_includedir/%name

# install designer templates
install -d -m 0755 %buildroot/%qtdir/tools/designer/templates
cp -fR tools/designer/templates/*.ui %buildroot/%qtdir/tools/designer/templates

# Ship qmake stuff
rm -rf %buildroot/%qtdir/mkspecs/linux*
cp -ar mkspecs/linux* %buildroot/%qtdir/mkspecs
%if !%shared_nonthr
# Patch qmake to use qt-mt unconditionally
perl -pi -e "s,-lqt ,-lqt-mt ,g;s,-lqt$,-lqt-mt,g" %buildroot/%qtdir/mkspecs/*/qmake.conf
%endif
%if %versioning_hack
# fix QMAKE_LFLAGS_SONAME
for f in %buildroot%qtdir/mkspecs/*/qmake.conf
do
    subst "s|^.*QMAKE_LFLAGS_SONAME.*$|QMAKE_LFLAGS_SONAME     = -Wl,-soname,|g" $f
done
%endif

# install documentation
#install -d -m 0755 %buildroot/%_docdir/%rname-%version/doc/html
#%%if %qt_copy
#rm -rf doc/html/designer
#%%endif
#install -m 0644 doc/html/*.html %buildroot/%_docdir/%rname-%version/doc/html

# David - 3.0.0-0.11mdk - Install missing documentation
install -d -m 0755 %buildroot/%_docdir/qt-%version/
#install -m 0644 %_builddir/%buildsubdir/ANNOUNCE  %buildroot/%_docdir/qt-%version/
cat > %buildroot/%_docdir/qt-%version/LICENSE <<__EOF__
see QPL-1.0, GPL-2 and GPL-3 in %_datadir/license
__EOF__
install -m 0644 %_builddir/%buildsubdir/PLATFORMS %buildroot/%_docdir/qt-%version/
install -m 0644 %_builddir/%buildsubdir/FAQ       %buildroot/%_docdir/qt-%version/
install -m 0644 %_builddir/%buildsubdir/README*    %buildroot/%_docdir/qt-%version/
%if !%qt_copy
install -m 0644 %_builddir/%buildsubdir/changes*  %buildroot/%_docdir/qt-%version/
%endif

# Install a README
install -m 0644 %SOURCE8 %buildroot/%_docdir/qt-%version/README.distribution
sed -i 's|@QT@|%name|g' %buildroot/%_docdir/qt-%version/README.distribution
sed -i 's|@QTDIR@|%qtdir|g' %buildroot/%_docdir/qt-%version/README.distribution
sed -i 's|@QTHOME@|~/.qt%major/|g' %buildroot/%_docdir/qt-%version/README.distribution
sed -i 's|@QtVersion@|%version|g' %buildroot/%_docdir/qt-%version/README.distribution
sed -i 's|@PackageVersion@|%version-%release|g' %buildroot/%_docdir/qt-%version/README.distribution

# wrap qt malloc
install -m 0644 %SOURCE12 %buildroot/%_docdir/qt-%version/

%if %build_qsa
mkdir -p %buildroot/%_docdir/qsa-%version/html
mkdir -p %buildroot/%qtdir/doc
install -m 0644 qsa-x11/doc/html/*.html %buildroot/%_docdir/qsa-%version/html
ln -s ../../../../%_docdir/qsa-%version/html %buildroot/%qtdir/doc/qsa
install -m 0644 qsa-x11/README %buildroot/%_docdir/qsa-%version/README
#install -m 0644 qsa-x11/RELEASENOTES %buildroot/%_docdir/qsa-%version/RELEASENOTES
pushd qsa-x11
tar jcf %buildroot/%_docdir/qsa-%version/examples.tar.bz2 examples/
popd
%endif

# Install man pages
install -d -m 0755 %buildroot/%_mandir/man1/
for i in %_builddir/%buildsubdir/doc/man/man1/* ; do
   install -m 0644 $i %buildroot/%_mandir/man1/
done
#
pushd %buildroot/%_mandir/man1
    for i in $(find . -name \*.1);do
	mv -f $i ${i}qt%major%minor%bugfix
    done
popd
#
#
install -d -m 0755 %buildroot/%_mandir/man3/
for i in %_builddir/%buildsubdir/doc/man/man3/* ; do
   install -m 0644 $i %buildroot/%_mandir/man3/
done
#
pushd %buildroot/%_mandir/
    for i in $(find . -name Q\*);do
	perl -pi -e 's|3qt|3qt%major%minor%bugfix|g' $i
    done
    for i in $(find . -name \*.3qt);do
	mv -f $i ${i}%major%minor%bugfix
    done
popd

# David - 3.0.1-2mdk - Install .pri files needed to build examples and tutorials
install -d -m 0755 %buildroot/%qtdir/src/
for i in %_builddir/%buildsubdir/src/*.pri; do
   install -m 0644 $i %buildroot/%qtdir/src/
done

# David - 3.0.0-0.11mdk - Provide a qmake.cache for examples
cp -pf %_builddir/%buildsubdir/.qmake.cache %_builddir/%buildsubdir/.qmake.cache.tmp
perl -pi -e "s|^QT_SOURCE_TREE.*|QT_SOURCE_TREE = %qtdir|" %_builddir/%buildsubdir/.qmake.cache.tmp
perl -pi -e "s|^QT_BUILD_TREE.*|QT_BUILD_TREE = %qtdir|" %_builddir/%buildsubdir/.qmake.cache.tmp
perl -pi -e "s|^QMAKE_MOC.*|QMAKE_MOC = %qtdir/bin/moc|" %_builddir/%buildsubdir/.qmake.cache.tmp
perl -pi -e "s|^QMAKE_UIC.*|QMAKE_UIC = %qtdir/bin/uic -L $$QT_BUILD_TREE/plugins|" %_builddir/%buildsubdir/.qmake.cache.tmp
perl -pi -e "s|^QMAKE_QMAKE.*|QMAKE_QMAKE = %qtdir/bin/qmake|" %_builddir/%buildsubdir/.qmake.cache.tmp
perl -pi -e "s|^QMAKE_MOC_SRC.*|QMAKE_MOC_SRC = %qtdir/src/moc|" %_builddir/%buildsubdir/.qmake.cache.tmp
perl -pi -e "s|^QMAKE_INCDIR_QT.*|QMAKE_INCDIR_QT = %qtdir/include|" %_builddir/%buildsubdir/.qmake.cache.tmp
perl -pi -e "s|^QMAKE_LIBDIR_QT.*|QMAKE_LIBDIR_QT = %qtdir/lib|" %_builddir/%buildsubdir/.qmake.cache.tmp
perl -pi -e "s|^QMAKE_LIBDIR_FLAGS.*|QMAKE_LIBDIR_FLAGS += -lXinerama|" %_builddir/%buildsubdir/.qmake.cache.tmp

## David - 3.0.0-0.11mdk - Examples and tutorial
cp -ar %_builddir/%buildsubdir/examples/ %buildroot/%_docdir/qt-%version
cp -p %_builddir/%buildsubdir/.qmake.cache.tmp %buildroot/%_docdir/qt-%version/examples/.qmake.cache
perl -pi -e "s|^QMAKE.*|QMAKE = %qtdir/bin/qmake|" %buildroot/%_docdir/qt-%version/examples/Makefile

# David - 3.0.0-0.11mdk - Provide a qmake.cache for tutorial
cp -ar %_builddir/%buildsubdir/tutorial/ %buildroot/%_docdir/qt-%version
cp -p %_builddir/%buildsubdir/.qmake.cache.tmp %buildroot/%_docdir/qt-%version/tutorial/.qmake.cache
perl -pi -e "s|^QMAKE.*|QMAKE = %qtdir/bin/qmake|" %buildroot/%_docdir/qt-%version/tutorial/Makefile

# David - 3.0.0-0.11mdk - Set qmake.cache to right directory
find %buildroot/%_docdir/qt-%version/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../.qmake.cache|.qmake.cache|"
#find %buildroot/%_docdir/qt-%version/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../.qmake.cache|../.qmake.cache|"

# David - 3.0.0-0.11mdk - Fix include directory for examples
find %buildroot/%_docdir/qt-%version/examples -name Makefile | xargs perl -pi -e "s|../../../include|%qtdir/include|"

# David - 3.0.0-0.11mdk - Fix include directory for examples
find %buildroot/%_docdir/qt-%version/examples -name Makefile | xargs perl -pi -e "s|../../include|%qtdir/include|"

# David - 3.0.1-2mdk - Fix lib directory for examples
find %buildroot/%_docdir/qt-%version/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../../../lib/libqt-mt.prl|%qtdir/lib/libqt-mt.prl|"
find %buildroot/%_docdir/qt-%version/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../../lib/libqt-mt.prl|%qtdir/lib/libqt-mt.prl|"
find %buildroot/%_docdir/qt-%version/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../lib/libqt-mt.prl|%qtdir/lib/libqt-mt.prl|"

find %buildroot/%_docdir/qt-%version/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../src/qt_professional.pri|%qtdir/src/qt_professional.pri|"

# David - 3.0.0-0.11mdk - Set RPM_BUILD_DIR to QTDIR
find %buildroot/%_docdir/qt-%version/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|%_builddir/%buildsubdir|%qtdir|"

# David - 3.0.1-2mdk - Explain in examples README that QTDIR need to be set
#                      before try to build one of them
cd %buildroot/%_docdir/qt-%version/examples/
cat README > README.tmp
echo "Before try to build one of these examples, you need to:" > README
echo "" >> README
echo "export QTDIR=\"%qtdir/\"" >> README
echo "" >> README
echo "" >> README
cat README.tmp >> README
rm -f README.tmp
cd -

# David - 3.0.1-2mdk - Fix PATH to tutorial.html in tutorials README
perl -pi -e "s|../doc/html/tutorial.html|%qtdir/doc/html/tutorial.html|" %buildroot/%_docdir/qt-%version/tutorial/README

# David - 3.0.1-2mdk - Explain in tutorials README that QTDIR need to be set
#                      before try to build one of them
cd %buildroot/%_docdir/qt-%version/tutorial/
cat README > README.tmp
echo "Before try to build one of these examples, you need to:" > README
echo "" >> README
echo "export QTDIR=\"%qtdir/\"" >> README
echo "" >> README
echo "" >> README
cat README.tmp >> README
rm -f README.tmp
cd -

# David - 3.0.0-0.11mdk - Install examples. They are usefull only for people who
#                         want learn to use Qt. We assume they are rarely used
#                         So, we can compress them to save space.
cd %buildroot/%_docdir/qt-%version/
tar jcf %buildroot/%_docdir/qt-%version/examples.tar.bz2 examples/
rm -fr examples/
cd -

# David - 3.0.0-0.11mdk - Install tutorial. It is usefull only for people who
#                         want learn to use Qt. We assume it is rarely used.
#                         So, we can compress it to save space.
cd %buildroot/%_docdir/qt-%version/
tar jcf %buildroot/%_docdir/qt-%version/tutorial.tar.bz2 tutorial/
rm -fr tutorial/
cd -

# David - 3.0.0-0.11mdk - Create a fake QTDIR (because Qt doesn't care of FHS
#                         and want all its directories in its own directory...)
cd %buildroot/%qtdir/
install -d -m 0755 doc
ln -s ../../../share/doc/qt-%version/html/ doc/html
cd -

%if %with_settings
install -d -m 0755 %buildroot/%_sysconfdir/profile.d/
install -m 0755 %SOURCE1 %buildroot/%_sysconfdir/profile.d/qt%{major}dir.csh
sed -i 's,@QTDIR@,%qtdir,g' %buildroot/%_sysconfdir/profile.d/qt%{major}dir.csh
install -m 0755 %SOURCE2 %buildroot/%_sysconfdir/profile.d/qt%{major}dir.sh
sed -i 's,@QTDIR@,%qtdir,g' %buildroot/%_sysconfdir/profile.d/qt%{major}dir.sh
%endif

pushd %buildroot/%qtdir/mkspecs/
rm -rf default
%ifarch x86_64
ln -sf linux-g++-64 default
%else
ln -sf linux-g++ default
%endif
popd

# Install .desktop files
install -d -m 0755 %buildroot/%_datadir/applications/
install -m 0644 %SOURCE21 %buildroot/%_datadir/applications/qt3-assistant.desktop
install -m 0644 %SOURCE22 %buildroot/%_datadir/applications/qt3-designer.desktop
install -m 0644 %SOURCE23 %buildroot/%_datadir/applications/qt3-linguist.desktop
install -m 0644 %SOURCE24 %buildroot/%_datadir/applications/qt3-qtconfig.desktop
# Icons
mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
install -m 644 %SOURCE101 %buildroot/%_iconsdir/hicolor/16x16/apps/%rname.png
install -m 644 %SOURCE102 %buildroot/%_iconsdir/hicolor/32x32/apps/%rname.png
install -m 644 %SOURCE103 %buildroot/%_iconsdir/hicolor/48x48/apps/%rname.png


%files
%files sql
%files -n lib%name
%if %with_settings
%config(noreplace) %_sysconfdir/profile.d/qt3dir.csh
%config(noreplace) %_sysconfdir/profile.d/qt3dir.sh
%endif
#
%dir %qtdir/phrasebooks/
%dir %qtdir/translations/
%qtdir/translations/qt_*.qm
%qtdir/translations/qtconfig_*.qm
#
%_libdir/%rname-%version
%dir %qtdir/
%dir %qtdir/lib/
%qtdir/lib/*.so.*
%if %build_qsa
%exclude %qtdir/lib/libqsa.so.*
%endif
%_libdir/*.so.*
%if %build_qsa
%exclude %_libdir/libqsa.so.*
%endif
%if %build_xt
%exclude %qtdir/lib/libqxt.so.*
%exclude %_libdir/libqxt.so.*
%endif
#
%dir %qtdir/bin
%qtdir/bin/qtconfig
%_bindir/qtconfig-qt3
#
%dir %qtdir/plugins/
%dir %qtdir/plugins/sqldrivers/
%qtdir/plugins/imageformats
%qtdir/plugins/inputmethods
%qtdir/plugins/styles
%qtdir/plugins/crypto
#
%_iconsdir/hicolor/*/apps/%rname.png
%_datadir/applications/qt3-qtconfig.desktop
#
%qtdir/etc
%if %with_settings
%_sysconfdir/%rname%major
%endif

%files -n lib%name-devel -f qsa-includes-exclude.list
%dir %_docdir/qt-%version/
%dir %qtdir/doc/
#%doc %_docdir/qt-%version/ANNOUNCE
%doc %_docdir/qt-%version/FAQ
%doc %_docdir/qt-%version/LICENSE
%doc %_docdir/qt-%version/PLATFORMS
%doc %_docdir/qt-%version/README*
%doc %_docdir/qt-%version/wrap_kde_malloc.cpp
%if !%qt_copy
%doc %_docdir/qt-%version/changes*
%endif
#
%qtdir/bin/conv2ui
%_bindir/conv2ui-%name
%qtdir/bin/createcw
%_bindir/createcw-%name
%qtdir/bin/moc
%_bindir/moc-%name
%qtdir/bin/uic
%_bindir/uic-%name
%qtdir/bin/findtr
%_bindir/findtr-%name
%qtdir/bin/lrelease
%_bindir/lrelease-%name
%qtdir/bin/lupdate
%_bindir/lupdate-%name
%qtdir/bin/mergetr
%qtdir/bin/makeqpf
%_bindir/makeqpf-%name
%_bindir/mergetr-%name
%qtdir/bin/msg2qm
%_bindir/msg2qm-%name
%qtdir/bin/qembed
%_bindir/qembed-%name
%qtdir/bin/qt20fix
%_bindir/qt20fix-%name
%qtdir/bin/qtrename140
%_bindir/qtrename140-%name
%qtdir/bin/qm2ts
%_bindir/qm2ts-%name
%qtdir/bin/qmake
%_bindir/qmake-%name
#
%_includedir/%name
%qtdir/include
%qtdir/lib/*.so
%if %build_qsa
%exclude %qtdir/lib/libqsa.so
%endif
%if %build_xt
%exclude %qtdir/include/qxt.h
%exclude %qtdir/lib/libqxt.so
%endif
#
%dir %qtdir/mkspecs/
%dir %qtdir/mkspecs/features/
%qtdir/mkspecs/default
%qtdir/mkspecs/*linux*
#
%dir %qtdir/src/
%qtdir/src/*
#
%_libdir/pkgconfig/*.pc
#
#%_rpmmacrosdir/%name
%exclude %_rpmmacrosdir/*

%files designer
%_bindir/designer*
%_bindir/linguist*
#
%qtdir/phrasebooks/*.qph
#%qtdir/translations/designer_*.qm
%qtdir/translations/linguist_*.qm
#
%dir %qtdir/plugins/designer
%qtdir/plugins/designer/*
%qtdir/bin/designer*
%qtdir/bin/linguist*
#
%_datadir/applications/qt3-linguist.desktop
%_datadir/applications/qt3-designer.desktop
#
%dir %qtdir/tools/
%dir %qtdir/tools/designer/
%dir %qtdir/tools/designer/templates/
%qtdir/tools/designer/templates/*.ui
#

%if %build_odbc
%files -n lib%name-odbc
%qtdir/plugins/sqldrivers/libqsqlodbc*
%endif

%files -n lib%name-postgresql
%qtdir/plugins/sqldrivers/libqsqlpsql*

%files -n lib%name-mysql
%qtdir/plugins/sqldrivers/libqsqlmysql*

%if %build_sqlite
%files -n lib%name-sqlite
%qtdir/plugins/sqldrivers/libqsqlite*
%endif

%files assistant
%_bindir/assistant-qt3
%qtdir/bin/assistant
%qtdir/bin/assistant-real
%qtdir/translations/assistant_*.qm
%_datadir/applications/qt3-assistant.desktop

%files doc
%files doc-html
%qtdir/doc/html
%dir %_docdir/qt-%version/
%dir %_docdir/qt-%version/html/
%doc %_docdir/qt-%version/html/*

%files doc-examples
%doc %_docdir/qt-%version/*.bz2

%files doc-man
%doc %_mandir/man1/*
%doc %_mandir/man3/*

%if %build_xt
%files -n lib%name-xt
%qtdir/include/qxt.h
%qtdir/lib/libqxt.so
%qtdir/lib/libqxt.so.*
%_libdir/libqxt.so.*
%if %static_nonthr || %static_thread
%qtdir/lib/libqxt.a
%endif
%endif

#%files -n lib%name-styles
#%dir %qtdir/plugins/styles
#%qtdir/plugins/styles/*

%files -n lib%name-qsa
%doc %_docdir/qsa-%version/README
#%doc %_docdir/qsa-%version/RELEASENOTES
%_libdir/libqsa.so.*
%qtdir/lib/libqsa.so.*
%qtdir/plugins/qsa

%files -n lib%name-qsa-devel -f qsa-includes.list
%doc %qtdir/doc/qsa
%dir %_docdir/qsa-%version
%doc %_docdir/qsa-%version/html
%doc %_docdir/qsa-%version/examples*
%qtdir/lib/libqsa.so
%dir %qtdir/mkspecs/features/qsa.prf

%files -n lib%name-devel-static
%_libdir/libqt-mt.a
%_libdir/libqt-mt.la

%files -n rpm-macros-%name
%_rpmmacrosdir/*

%changelog
* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 3.3.8d-alt14
- rebuild without sqlite support (ALT bug 37985)

* Thu Nov 21 2019 Ivan A. Melnikov <iv@altlinux.org> 3.3.8d-alt13
- (NMU) Fix build with PostgreSQL 12

* Thu Nov 29 2018 Ivan A. Melnikov <iv@altlinux.org> 3.3.8d-alt12
- (NMU) Fix build with recent postgresql-devel

* Wed May 30 2018 Sergey V Turchin <zerg@altlinux.org> 3.3.8d-alt11
- update requires

* Fri May 12 2017 Sergey V Turchin <zerg@altlinux.org> 3.3.8d-alt10
- rebuild with new libmng

* Thu Nov 05 2015 Michael Shigorin <mike@altlinux.org> 3.3.8d-alt9
- Hardwire "CXX3" for any gcc not just 4.x (thx glebfm@ for suggestion).

* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 3.3.8d-alt8
- Some doc subpackages made noarch.
- Minor spec cleanup.

* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 3.3.8d-alt7
- Rebuilt for gcc5 C++11 ABI.

* Fri Nov 01 2013 Roman Savochenko <rom_as@altlinux.ru> 3.3.8d-alt6
- Icons hide fix.

* Tue Jul 09 2013 Roman Savochenko <rom_as@altlinux.ru> 3.3.8d-alt5
- QMAKE_LIBDIR_QT = $(QTDIR)/lib64 return to QMAKE_LIBDIR_QT = $(QTDIR)/lib.

* Sat Jun 22 2013 Roman Savochenko <rom_as@altlinux.ru> 3.3.8d-alt4
- Update to last Trinity 3.3.8d, branch origin/v3.5.13-sru (tag v3.5.13.2)

* Tue Feb 12 2013 Sergey V Turchin <zerg@altlinux.org> 3.3.8d-alt3
- rebuilt (ALT #28444)

* Wed Jan 23 2013 Roman Savochenko <rom_as@altlinux.ru> 3.3.8d-alt2
- Update to last Trinity 3.3.8d, branch origin/v3.5.13-sru

* Tue Oct 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.8d-alt1.2
- Fixed (thnx, Gentoo!) crash with libpng15 (ALT #27817)

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.8d-alt1.1
- Rebuilt with libpng15

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 3.3.8d-alt0.M60P.1
- built for M60P

* Wed Nov 16 2011 Sergey V Turchin <zerg@altlinux.org> 3.3.8d-alt1
- using Trinity 3.3.8d

* Mon May 23 2011 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt16
- desktop-files cleanup

* Thu May 19 2011 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt15
- apply repocop fixes

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt14
- fix build requires

* Wed Mar 09 2011 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt13
- rebuilt

* Fri Jan 14 2011 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt12
- fix Comment in qt3-qtconfig.desktop

* Tue Nov 09 2010 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt11
- fix requires

* Thu Oct 21 2010 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt10
- rebuilt

* Thu Jul 22 2010 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt9
- fix to build

* Mon Jan 18 2010 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt8
- move rpm macros to separate package

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt7
- fix to apply patch for menu shortcuts

* Fri Jul 24 2009 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt6
- add patch from Sergey A. Sukiyazov
  allow Key as Alt+Key menu shortcuts when keyboard layout changed

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt5
- rebuilt

* Fri May 08 2009 Sergey V Turchin <zerg@altlinux.org> 3.3.8b-alt4
- rebuilt with new gcc
- remove deprecated macroses from specfile

* Wed Oct 22 2008 Sergey V Turchin <zerg at altlinux dot org> 3.3.8b-alt3
- rebuilt with new gcc

* Thu Mar 13 2008 Sergey V Turchin <zerg at altlinux dot org> 3.3.8b-alt2
- add patches from qt-copy:
  to handle _NET_WM_SYNC_REQUEST
  to fix compile errors with newer X.org

* Tue Jan 22 2008 Sergey V Turchin <zerg at altlinux dot org> 3.3.8b-alt1
- new version
- fix package license

* Mon Oct 22 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt12
- remove wrong symlink from mkspecs/default/

* Thu Aug 30 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt11
- add patch to fix buffer overflow

* Wed Aug 01 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt10
- sync patches with RH, Qt-copy (fixes font substinitions)

* Mon Jul 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt9
- add patches to fix CVE-2007-3388

* Mon Jul 02 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt8
- add patch to fix compile on ARM

* Fri Jun 08 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt7
- sync patches with qt-copy

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt6
- own plugins/crypto directory

* Mon Apr 02 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt5
- add patch against utf8 bug

* Thu Mar 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt4
- don't apply Patch108 for #7322 (fixed another way by Trolltech)

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt3
- rebuilt

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt2
- built without NAS

* Fri Mar 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.8-alt1
- new version
- symlink all programs to %_bindir

* Wed Jan 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.3.7-alt2
- update QSA to 1.1.5
- don't delete file when moved to unwritable destination (#7322)

* Fri Oct 20 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.7-alt1
- new version

* Tue Oct 10 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.6-alt10
- rebuilt with new glibc

* Thu Sep 28 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.6-alt9
- hack soname for libqsa to availe bild non-hacked libqsa soname for Qt4

* Mon Jun 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.6-alt8
- fix build on x86_64

* Fri Jun 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.6-alt7
- add patch for MacCyrillic encoding by Alexey Morozov

* Mon May 15 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.6-alt6
- rebuilt with new gcc

* Thu Apr 20 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.6-alt5
- fix lib*.so symlinks

* Tue Apr 18 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.6-alt4
- new QSA-1.1.4
- move libs to %_libdir

* Wed Apr 12 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.6-alt3
- fix Categories in designer-qt3.desktop

* Thu Apr 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.6-alt2
- apply fixed Patch9002; 10x Sergey A. Sukiyazov

* Mon Apr 03 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.6-alt1
- new version
- fix symlinks in %_bindir
- disable plugins hidden visibility for gcc-3.x

* Tue Mar 21 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.5-alt5
- fix build requires
- built with -Os
- make amount package for SQL drivers

* Thu Jan 26 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.5-alt4
- removed target cpu name from Qt buildkey

* Wed Jan 25 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.5-alt3
- fix build options

* Wed Jan 25 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3.5-alt2
- remove fast-malloc patch
- sync patches with Qt-copy and SuSE
- remove menufiles

* Mon Nov 28 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.5-alt1
- new version
- add gcc visibility patch

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

* Thu Feb 06 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2.4-1mdk
- 2.2.4

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

* Tue Dec 11 2000 David BAUDENS <baudens@mandrakesoft.com> 2.2.3-1mdk
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

* Tue Jun 21 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 2.1.1-3mdk
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

* Sat Aug  8 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- replace qstrlist.h with a version that works

* Sat Aug  8 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- rename /usr/lib/libqt.a to /usr/lib/libqt2.a to avoid conflict with
  qt 1.44
- Add libqt2.so link to libqt.so.2 so we can do -lqt2

* Tue Jul 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- First version for Mandrake distribution.
