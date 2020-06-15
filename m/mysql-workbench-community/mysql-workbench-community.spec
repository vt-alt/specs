Name: mysql-workbench-community
Version: 8.0.20
Release: alt1

Summary: A MySQL visual database modeling tool

License: GPL-2.0-or-later and LGPL-2.0-or-later and CC-BY-3.0 and MIT and Scintilla and Public-Domain
Group: Development/Databases
Url: http://wb.mysql.com
Source0: %name-%version.tar.gz
Source1: antlr-4.7.1-complete.jar
Source2: antlr4-cpp-runtime-4.7.1-source.zip

# https://www.mysql.com/support/supportedplatforms/workbench.html
ExclusiveArch: %ix86 x86_64

Patch1: mysql-workbench-mariadb-build.patch
Patch2: mysql-workbench-mariadb-check.patch
Patch3: mysql-workbench-6.3.4-c++11.patch
Patch4: %name-6.3.4-alt-gcc6.patch
Patch5: mysql-workbench-community-6.3.10-32bit.patch
Patch6: mysql-workbench-community-8.0.15-antlr4-runtime.patch
Patch7: mysql-workbench-8.0.17.suppress-unsupported.patch

Provides: mysql-workbench-oss = %version-%release
Obsoletes: mysql-workbench-oss < %version-%release
Provides: mysql-workbench-gpl = %version-%release
Obsoletes: mysql-workbench-gpl < %version-%release

Provides: mysql-administrator = %version-%release
Obsoletes: mysql-administrator < %version-%release

Provides: mysql-query-browser = %version-%release
Obsoletes: mysql-query-browser < %version-%release

# "_mforms" and "grt" are accessable from "MySQL Workbench GRT Shell" only.
%add_python_req_skip _mforms grt mforms

# internal Workbench's libraries
%add_python_req_skip wb workbench cairo_utils wb_common

# shell_snippets.py is not pure Python
%add_findreq_skiplist */mysql-workbench/shell_snippets.py

# templates only
%add_findreq_skiplist */mysql-workbench/script_templates/*

%add_findreq_skiplist */mysql-workbench/libraries/grt_python_debugger.py

Requires: python-module-paramiko python-module-pexpect
Requires: mysql-client gnome-keyring
Requires: %name-data = %version

# https://bugzilla.altlinux.org/35600
Requires: glibc-devel

BuildRequires(pre): unzip
BuildRequires(pre): rpm-build-xdg

# MySQL only
BuildRequires: libmysqlclient-devel
BuildConflicts: libmariadb-devel

# Automatically added by buildreq on Sun Mar 20 2011
# and edited manualy
# - removed mysql-workbench-gpl
# - boost-devel-headers changed to boost-devel
BuildRequires: boost-devel gcc-c++ libglade-devel libgnome-devel libgtkmm2-devel liblua5-devel libpcre-devel libsqlite3-devel libuuid-devel libxml2-devel libzip-devel python-devel

BuildRequires: boost-signals-devel

BuildRequires: libGL-devel
BuildRequires: libctemplate-devel
BuildRequires: libiodbc-devel

# 6.3.4
BuildRequires(pre): rpm-macros-cmake cmake
#BuildRequires: mysql-connector-c++-devel
BuildRequires: libXdmcp-devel libXdamage-devel libXxf86vm-devel
BuildRequires: swig libgdal-devel libpcrecpp-devel libpixman-devel libexpat-devel libvsqlite++-devel
BuildRequires: libgnome-keyring-devel libharfbuzz-devel libxshmfence-devel tinyxml-devel

# 6.3.8
BuildRequires: boost-locale-devel

# 6.3.10
BuildRequires: libgtk+3-devel wayland-protocols libxkbcommon-devel libgtkmm3-devel libproj-devel
BuildRequires: mysql-connector-c++-devel >= 1.1.9

# 6.3.10 antlr-3.4-complete.jar
BuildRequires: java-1.8.0-openjdk stringtemplate

# 8.0.15
BuildRequires: libdrm-devel libsecret-devel libssl-devel libfribidi-devel libmount-devel libblkid-devel
BuildRequires: libtiff-devel libpng-devel libepoxy-devel libwayland-cursor-devel libwayland-egl-devel
BuildRequires: libXinerama-devel libXi-devel libXrandr-devel libXcursor-devel libXcomposite-devel
BuildRequires: libat-spi2-core-devel at-spi2-atk-devel
BuildRequires: libssh-devel >= 0.8.5

# 8.0.19
BuildRequires: libthai-devel libdatrie-devel rapidjson

# 8.0.20
BuildRequires: libbrotli-devel libgcrypt-devel

%description
MySQL Workbench is modeling tool that allows you to
design and generate MySQL databases graphically.

Some parts of code have separate licenses.
Look to %_defaultdocdir/%name-%version/License.txt

%package data
Summary: Architecture independent files for %name
License: GPL-2.0-or-later and LGPL-2.0-or-later and CC-BY-3.0 and MIT and Scintilla and Public-Domain
Group: Development/Databases
BuildArch: noarch
Conflicts: %name < %version
Conflicts: mysql-workbench-gpl-data

%description data
Architecture independent files for %name

Some parts of code have separate licenses.
Look to %_defaultdocdir/%name-%version/License.txt

%prep

%setup -q

#patch1 -p1
#patch2 -p1
#patch3 -p1
#patch4 -p2
#ifarch %ix86
#patch5 -p1
#endif
%patch6 -p2
%patch7 -p2

sed -i "s|pcre.h|pcre/pcre.h|" library/grt/src/grtpp_shell.cpp
sed -i "s|ldconfig|/sbin/ldconfig|" frontend/linux/workbench/mysql-workbench.in

%set_verify_elf_method unresolved=relaxed

%build

mkdir %_builddir/%name-%version/ANTLR-CPP
pushd %_builddir/%name-%version/ANTLR-CPP
 unzip %SOURCE2
 mkdir build && mkdir run && cd build
 cmake ..
 make
 DESTDIR=%_builddir/%name-%version/ANTLR-CPP make install
popd

%ifarch %ix86
%add_optflags -Wno-error=format=
%endif

#8.0.17: wb_context_ui_home.cpp:59:10: fatal error: include <zip.h>
%add_optflags -I/usr/include/libzip

#8.0.19: https://lists.altlinux.org/pipermail/devel/2020-March/210126.html
sed -i "s/ -Wno-deprecated-copy//g" CMakeLists.txt

%cmake \
    -DWITH_ANTLR_JAR=%SOURCE1 \
    -DANTLR4_INCLUDE_DIR=%_builddir/%name-%version/ANTLR-CPP/usr/local/include \
    -DANTLR4_LIBRARIES="-static -L%_builddir/%name-%version/ANTLR-CPP/dist -lantlr4-runtime" \
#

cd BUILD
#make_build VERBOSE=1
%make_build

%install
pushd %_builddir/%name-%version/BUILD
make install DESTDIR=%buildroot
popd

mkdir -p %buildroot%_niconsdir
cp %_builddir/%name-%version/images/icons/MySQLWorkbench-32.png %buildroot%_niconsdir/mysql-workbench.png

mkdir -p %buildroot%_iconsdir/hicolor/32x32/mimetypes
cp %_builddir/%name-%version/images/icons/MySQLPlugin-32.png %buildroot%_iconsdir/hicolor/32x32/mimetypes/application-vnd.mysql-workbench-plugin.png
cp %_builddir/%name-%version/images/icons/MySQLWorkbenchDocIcon32x32.png %buildroot%_iconsdir/hicolor/32x32/mimetypes/application-vnd.mysql-workbench-model.png

pushd %_builddir/%name-%version/ANTLR-CPP/dist
 cp -a *.so* %buildroot/%_libdir/mysql-workbench/
popd

%files
%exclude %_libdir/mysql-workbench/modules/*.py?

%exclude %_datadir/applications/*.desktop
%exclude %_datadir/mysql-workbench/*

%doc License.txt README.md AUTHORS
%exclude %_datadir/doc/mysql-workbench/License.txt
%exclude %_datadir/doc/mysql-workbench/README.md

%_bindir/mysql-workbench
%_bindir/mysql-workbench-bin
%_bindir/wbcopytables
%_bindir/wbcopytables-bin
%dir %_libdir/mysql-workbench
%_libdir/mysql-workbench/*

%files data
%_datadir/applications/*.desktop
%dir %_datadir/mysql-workbench
%_datadir/mysql-workbench/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/128x128/apps/*
%_iconsdir/hicolor/16x16/mimetypes/*
%_iconsdir/hicolor/32x32/mimetypes/*
%_iconsdir/hicolor/48x48/mimetypes/*
%_iconsdir/hicolor/128x128/mimetypes/*
%_xdgmimedir/packages/*.xml
%_xdgdatadir/mime-info/*.mime

%changelog
* Thu Jun 04 2020 Sergey Y. Afonin <asy@altlinux.org> 8.0.20-alt1
- Updated to last release (ALT #38563)

* Thu Mar 19 2020 Sergey Y. Afonin <asy@altlinux.org> 8.0.19-alt1
- Updated to last release
- Removed all -Wno-error= for x86_64 in spec file
- Removed hack for http://bugs.mysql.com/97116
- Removed -Wno-deprecated-copy from CMakeLists.txt (gcc8 not supported it)
- Not used mysql-workbench-community-6.3.10-32bit.patch
- Updated License tag to SPDX syntax

* Tue Oct 08 2019 Sergey Y. Afonin <asy@altlinux.org> 8.0.17-alt1
- Updated to last release
- Removed -Werror from CMakeLists.txt (http://bugs.mysql.com/97116)
- Disabled "Unsupported Operating System" warning
- Added "Requires: glibc-devel" (ALT #35600)

* Thu Feb 21 2019 Sergey Y. Afonin <asy@altlinux.ru> 8.0.15-alt1
- Updated to last release
- Updated antlr jar to antlr-4.7.1-complete.jar from http://www.antlr4.org/download/
- Added antlr4-cpp-runtime-4.7.1-source.zip from http://www.antlr4.org/download/
- Added -Wno-error=maybe-uninitialized
- Changed libmysqlclient20-devel to libmysqlclient-devel in BuildRequires
  (libmariadb-devel doesn't provide libmysqlclient-devel since 10.2.15-alt3)
- Removed "Packager" field

* Tue Jul 03 2018 Sergey Y. Afonin <asy@altlinux.ru> 6.3.10-alt2
- Added rpm-build-xdg to BuildRequires

* Mon Jun 25 2018 Sergey Y. Afonin <asy@altlinux.ru> 6.3.10-alt1
- Updated to last release (thanks to viy@altlinux)
- Added ExclusiveArch: %%ix86 x86_64
- Added antlr-3.4-complete.jar from http://www.antlr3.org/download/ for build
- Added -Wno-error=deprecated-declarations
- Switched to libmysqlclient20-devel (from MySQL)
- Disabled patches for MariaDB
- Disabled c++11.patch and gcc6.patch patches
- Added -Wno-error=format= for %%ix86
- Added mysql-workbench-community-6.3.10-32bit.patch for %%ix86

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.4-alt3
- Updated build with gcc-6

* Fri Oct 23 2015 Sergey Y. Afonin <asy@altlinux.ru> 6.3.4-alt2
- updated mysql-workbench-6.3.4-c++11.patch from http://bugs.mysql.com/78668

* Mon Oct 12 2015 Sergey Y. Afonin <asy@altlinux.ru> 6.3.4-alt1
- Updated to last release (renamed to mysql-workbench-community)
- Removed patches for mysql-workbench 5.x
- Fixed build with new libsigc++ (requires "-std=c++11" for c++)
- Added draft patch for support administration of MariaDB 10

* Fri Oct 09 2015 Sergey Y. Afonin <asy@altlinux.ru> 5.2.47-alt2
- Changed "MySQL-client" to "mysql-client" in "Requires" (ALT #31271)
- Used %%gpllgpl2only macro instead of %%gpl2only
- Warning: libmysqlclient-devel of MariaDB is used since 5.2.47-alt1.1

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.2.47-alt1.1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.47-alt1.1
- Rebuilt with new ctemplate

* Sat Mar 02 2013 Sergey Y. Afonin <asy@altlinux.ru> 5.2.47-alt1
- Update to last release

* Sun Jul 29 2012 Evgeny Sinelnikov <sin@altlinux.ru> 5.2.41-alt1
- Update to last release

* Thu Apr 26 2012 Evgeny Sinelnikov <sin@altlinux.ru> 5.2.39-alt1
- Update to last release
- Fix and delete unneeded old patches
- Add icon and mime files

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.33-alt2.2
- Rebuilt with new glib2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.33-alt2.1
- Rebuild with Python-2.7

* Mon Mar 21 2011 Sergey Y. Afonin <asy@altlinux.ru> 5.2.33-alt2
- fixed building with libgtkmm2-2.24.0 (thanks to <iv@altlinux.org>)
- moved library.forms.Makefile.am.patch to alt-build.patch
- updated alt-build.patch for building with new libglade-devel
  (without requires libxml2-devel; thanks to <at@altlinux.ru>)
- fixed relative requires between mysql-workbench-gpl and
  mysql-workbench-gpl-data subpackages

* Sun Mar 13 2011 Sergey Y. Afonin <asy@altlinux.ru> 5.2.33-alt1
- New version

* Wed Dec 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.31a-alt1
- 5.2.31a

* Wed Oct 13 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.2.29-alt1
- New version
- Architecture independent files moved to mysql-workbench-gpl-data subpackage
- Removed "Vendor" tag: not need in ALT Linux

* Mon Sep 27 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.2.28-alt1
- New version

* Sun Aug 15 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.2.26-alt1
- New version
- added libGL-devel to BuildRequires (14/08/2010 test rebuild failed for
  5.2.25-alt1 with "configure: error: OpenGL headers not found")

* Thu Jul 08 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.2.25-alt1
- New version, renamed from mysql-workbench-oss to mysql-workbench-gpl
- Removed patch for linking problem with my_stat() (fixed in mainstream)
- Removed python-devel-static and rpm-build-compat from BuildRequires

* Sun May 02 2010 Evgeny Sinelnikov <sin@altlinux.ru> 5.2.20-alt1
- Update to new release (5.2.20 Beta 10)
- Fix linking problem with my_stat()

* Wed Apr 21 2010 Evgeny Sinelnikov <sin@altlinux.ru> 5.2.19-alt1
- Build new version for Sisyphus

* Fri Apr 02 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.2.16-alt1
- Initial build for AltLinux (5.2.16 Beta 6)
