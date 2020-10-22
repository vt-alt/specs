%def_disable bootstrap
%def_with    sources
%def_without doc
%def_without win32
%def_with    tests
# Help index is generated too long, package ready index
%def_without help_index

Name: 	  fpc
Version:  3.2.0
Release:  alt2
Epoch:    3

Summary:  Free Pascal Compiler -- Meta Package
License:  GPL-2.0+ and LGPL-2.1+
Group:    Development/Other
Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: %ix86 x86_64 aarch64

Url: 	 http://www.freepascal.org
Source:  fpcbuild-%version.tar
Source1: fp.desktop
Source2: fp.sh
Source3: fp.cfg
Source4: fp16x16.xpm
Source5: fp48x48.xpm
Source8: fpc.watch
Source9: fpctoc.htx

%ifarch %ix86
%define ppctarget i386-linux
%define ppcname ppc386
%endif
%ifarch x86_64
%define ppctarget x86_64-linux
%define ppcname ppcx64
%endif
%ifarch aarch64
%define ppctarget aarch64-linux
%define ppcname ppca64
%endif

%add_findreq_skiplist %_libdir/libpas2jslib.so
%filter_from_requires /^fpc(pas2js/d

%if_enabled bootstrap
Source10: base.%ppctarget.tar.gz
%endif

# Patches from Mageia
# Fix http://bugs.freepascal.org/view.php?id=23682
Patch1: fpc-fpkeys.patch
# Don't show message on mouse click
Patch3: fpc-mouse-click.patch
# Fix http://bugs.freepascal.org/view.php?id=25280
Patch6: fpc-fix-min-size.patch

# Patches from Debian
Patch12: fpc-fix-FPCDIR-in-fpcmake.patch
Patch13: fpc-fix-encoding-of-localization-files-to-be-utf8.patch
Patch15: fpc-add_arm64_manpage.patch
Patch16: fpc-add-arm64-support.patch
Patch17: fpc-fix-path-of-localization-files.patch
Patch18: fpc-disable_building_gnome1_and_gtk1.patch
Patch19: fpc-fix_FTBFS_on_linux_not_amd64.patch
Patch20: fpc-fix-IDE-data-file-location.patch
Patch21: fpc-fix_source_location_for_documentation.patch
Patch23: fpc-honor_SOURCE_DATE_EPOCH_in_date.patch
Patch24: fpc-prevent_date_in_fpcdocs.patch
Patch26: fpc-relpath.patch
Patch27: fpc-rename-instantfpc-to-ifpc.patch
Patch28: fpc-use-bfd-explicitly.patch
Patch29: fpc-aarch64-paths.patch

# Other patches
# Set path to ide without version and text/ subdirectory. Use ~/fpc/ide instead of ~/.fp for personal stuff for IDE.
Patch30: fpc-fix-path-to-ide.patch
# Add note about install fpc-docs in helpsystem message about missing documentation
Patch31: fpc-docs-message.patch
# Automatically add help index from /usr/share/doc/fpc/fpctoc.htx if it exists
Patch32: fpc-auto-add-help-index.patch
# Show progress in writeidx
Patch33: fpc-writeidx-show-progress.patch

Requires: fpc-units-rtl
Requires: fpc-compiler
Requires: fpc-units-base
Requires: fpc-ide
Requires: fpc-units-fcl
Requires: fpc-units-fv
Requires: fpc-units-gtk2
Requires: fpc-units-db
Requires: fpc-units-gfx
Requires: fpc-units-net
Requires: fpc-units-math
Requires: fpc-units-misc
Requires: fpc-units-multimedia

Requires: rpm-build-fpc

Provides:  freepascal = %EVR
Obsoletes: freepascal < %EVR

BuildRequires(pre): rpm-build-fpc
%if_disabled bootstrap
BuildRequires: fpc-compiler
BuildRequires: fpc-utils
%endif
BuildRequires: libexpat-devel libgdb-devel libncurses-devel libreadline-devel-static python-devel zlib-devel liblzma-devel
BuildRequires: mysql-devel postgresql-devel libunixODBC-devel libsqlite3-devel
BuildRequires: libGL-devel libgtk+2-devel libjpeg-devel
BuildRequires: libstdc++-devel
BuildRequires: libunwind-devel
BuildRequires: python3-dev
BuildRequires: unzip
%if_with doc
BuildRequires: tex4ht texlive-generic-recommended texlive-latex-recommended fpc-units-fcl
%endif

%define fpc_docdir  %_defaultdocdir/%name
%define fpc_fpmdir  %fpc_dir/fpmkinst/%ppctarget
%define fpc_unitdir %fpc_dir/units/%ppctarget

%define makewin32 0

%description
The Free Pascal Compiler is an object pascal compiler supporting both
Delphi and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.  It
provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom
independent class based Free Component Library (FCL) adding many Delphi
extensions and interfacing many popular open source libraries.

Some extensions are added to the language, like function overloading.
Shared libraries can be linked and created. Delphi language extentions
like classes, exceptions, ansi strings and open arrays are also
supported.

This package contains dependency on all FPC packages provided on your
architecture. Experienced users may want to install only packages they
need, and can skip installing this metapackage.

%prep
%setup -n fpcbuild-%version
pushd fpcsrc
%patch1 -p0
%patch3 -p0
%patch6 -p0
popd
%patch12 -p1
%patch13 -p1
#patch15 -p1 TODO see patch16
#patch16 -p1 TODO neew adapt
%patch17 -p2
%patch18 -p1
#patch19 -p1 TODO need adapt
%patch20 -p2
#patch21 -p1
#patch23 -p1
%patch24 -p1
%patch26 -p1
#patch27 -p2
%patch28 -p2
%patch29 -p0
%patch30 -p2
%patch31 -p0
%patch32 -p2
%patch33 -p2

%if_with sources
cp -a fpcsrc{,.orig}
%endif

pushd fpcsrc
sed -i "s|/usr/local/lib|%_libdir|g"      packages/gdbint/src/gdbint.pp
#sed -i "/LINKLIB/s/python/python2.7/"     packages/gdbint/src/gdbint.pp
sed -i "/LINKLIB ncurses/a {\$LINKLIB z}" packages/gdbint/src/gdbint.pp
sed -i "/LINKLIB ncurses/a {\$LINKLIB lzma}" packages/gdbint/src/gdbint.pp
sed -i '/fp/s/\/bin/\/usr\/bin/g'         compiler/utils/samplecfg

%build
export OPT="-vwn -Cg"
export GDBLIBDIR=%_libdir
export LIBGDBFILE=%_libdir/libgdb.a

%if_enabled bootstrap
# bootstrap fpc
mkdir bootstrap
pushd bootstrap
tar xf %SOURCE10
export PATH=$PWD/bin:$PATH
export ppcname="$PWD/lib/fpc/3.2.0/%ppcname"
popd
%else
export ppcname=%ppcname
%endif

pushd fpcsrc
export PATH=$PWD/compiler:$PATH

#Fix path
%ifarch x86_64 aarch64
sed -i "s|/lib/fpc/lexyacc|/lib64/fpc/lexyacc|g" utils/tply/Makefile.fpc
%endif

make build VERBOSE=1 FPC=$ppcname LDCONFIG="$(dirname `gcc -print-file-name=libgcc.a`)"
popd

# Make documentation
# TODO PDF generation does not work
%if_with doc
# FIXME: -j1 as there is a race - seen on "missing" `rtl.xct'.
#make -j1 -C fpcdocs pdf html FPC=$(pwd)/fpcsrc/compiler/%ppcname
make -j1 -C fpcdocs html FPC=$(pwd)/fpcsrc/compiler/%ppcname

# Generate help index to file fpctoc.htx
%if_with help_index
pushd fpcdocs
../fpcsrc/installer/writeidx fpctoc.html
popd
%endif

%endif

%install
pushd fpcsrc
export PATH=./utils/fpcmkcfg/bin/%ppctarget:$PATH
%makeinstall_std INSTALL_PREFIX=%buildroot%_usr FPC=compiler/%ppcname

# this symbolic link must be absolute (so that fpcmake can detect FPCDIR)
ln -s %fpc_dir/%ppcname %buildroot%_bindir/%ppcname

%if_with win32
#Install for win32
%fpc_install_win32 FPC=$PWD/ppc386 FPCMAKE=$PWD/fpcmake -C rtl
%endif

# TODO [HACK] Fix lib dir for x86_64 and remove version from installed path of fpc_dir and unit documentation
%ifarch x86_64 aarch64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif
mv %buildroot%fpc_dir/%version/* %buildroot%fpc_dir
rmdir %buildroot%fpc_dir/%version
mv %buildroot%fpc_docdir-%version %buildroot%fpc_docdir

cp -av utils/pas2js/units/%ppctarget/dirwatch.* %buildroot%fpc_dir/units/%ppctarget/pastojs/

# Install fp.cfg and create fpc.cfg
install -Dpm 644 %SOURCE3 %buildroot%_sysconfdir/fp.cfg
chmod 755 compiler/utils/samplecfg
compiler/utils/samplecfg "%fpc_dir" %buildroot%_sysconfdir

# Fix configuration for depend
install -p -m 644 utils/fppkg/units/%ppctarget/*.{o,ppu} %buildroot%fpc_dir/units/%ppctarget/fppkg/
sed -i "s|\$fpctarget|%ppctarget|g" %buildroot%_sysconfdir/%name.cfg
sed -i "s|\$fpctarget|%ppctarget|g" %buildroot%_sysconfdir/fp.cfg
sed -i "s|/usr/lib|%_libdir|g" %buildroot%_sysconfdir/fp.cfg
sed -i "s|errorn.msg|errorn.msg\n-Fr%fpc_dir/msg/errorru.msg|g" %buildroot%_sysconfdir/%name.cfg
sed -i "s|\$fpcversion|fpc|g" %buildroot%_sysconfdir/%name.cfg

popd

# Install icons and desktop file
mkdir -p %buildroot%_datadir/pixmaps
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_niconsdir
mkdir -p %buildroot%_datadir/applications
install -p -m 644 %SOURCE1 %buildroot%_datadir/applications
mv %buildroot%_bindir/fp %buildroot%_bindir/fp-bin
install -p -m 755 %SOURCE2 %buildroot%_bindir/fp
install -p -m 644 install/unix/fp32x32.xpm %buildroot%_datadir/pixmaps/fp.xpm
install -p -m 644 install/unix/fp32x32.xpm %buildroot%_niconsdir/fp.xpm
install -p -m 644 %SOURCE4 %buildroot%_miconsdir/fp.xpm
install -p -m 644 %SOURCE5 %buildroot%_liconsdir/fp.xpm

#Install src
%if_with sources
mkdir -p %buildroot%_datadir/fpcsrc
cp -fR fpcsrc.orig/* %buildroot%_datadir/fpcsrc
%add_verify_elf_skiplist */fpcsrc/*
%add_findreq_skiplist */fpcsrc/*
%endif

#Install man
make INSTALL_PREFIX=%buildroot%_datadir -C install/man installman

#Instal docs
mkdir -p %buildroot%fpc_docdir
install -p -m 644 install/doc/copying* install/doc/whatsnew.txt install/doc/readme.txt install/doc/faq.txt %buildroot%fpc_docdir

%if_with doc
make INSTALL_DOCDIR=%buildroot%fpc_docdir DESTDIR=%buildroot -C fpcdocs htmlinstall #pdfinstall
%if_with help_index
install -p -m 644 fpcdocs/fpctoc.htx %buildroot%fpc_docdir
%else
install -p -m 644 %SOURCE9 %buildroot%fpc_docdir
%endif
%endif

# Remove hacker ASCII art picture as IDE background by renaming fp.ans to fp.ans.original
mv %buildroot%fpc_dir/ide/fp.ans{,.original}

# Remove installer executable
rm -f %buildroot%_bindir/installer

%files

%package common
Summary: Free Pascal -- Common files and dirs
Group: Development/Other

%description common
The Free Pascal Compiler is a Turbo Pascal 7.0 and Delphi compatible
32/64-bit Pascal Compiler. It comes with a fully compatible TP 7.0
runtime library.  Some extensions are added to the language, like
function overloading. Shared libraries can be linked and created. Basic
Delphi support is already implemented (classes, exceptions,
ansistrings). This package contains the common files and dirs.

%files common
%dir %fpc_dir
%dir %fpc_docdir

%package compiler
Summary: Free Pascal -- Compiler
Group: Development/Other
Requires: %name-common = %{?epoch:%epoch:}%version-%release
Requires: binutils
Obsoletes: fpc <= 2.1-alt3

%description compiler
The Free Pascal Compiler is an object pascal compiler supporting both
Delphi and Turbo Pascal 7.0 dialects as well as Mac pascal dialects.  It
provides a completely portable RunTime Library (RTL) available on many
platforms and compatible with Turbo Pascal, but also a platfrom
independent class based Free Component Library (FCL) adding many Delphi
extensions and interfacing many popular open source libraries.

Some extensions are added to the language, like function overloading.
Shared libraries can be linked and created. Delphi language extentions
like classes, exceptions, ansi strings and open arrays are also
supported.

This package contains the command line compiler.

%files compiler
%config(noreplace) %_sysconfdir/%name.cfg
%if_disabled bootstrap
%config(noreplace) %_sysconfdir/fppkg.cfg
%dir %_sysconfdir/fppkg
%config(noreplace) %_sysconfdir/fppkg/default
%endif
%doc %fpc_docdir/copying*
%doc %fpc_docdir/whatsnew.txt
%doc %fpc_docdir/readme.txt
%doc %fpc_docdir/faq.txt
%_bindir/fpc
%_bindir/ppc*
%_bindir/fpcsubst*
%_bindir/fpcmkcfg*
%_bindir/fppkg
%_bindir/grab_vcsa
%fpc_dir/samplecfg
%fpc_dir/ppc*
%fpc_dir/msg
%_man1dir/fpc.*
%_man1dir/fpcmkcfg.*
%_man1dir/fpcsubst.*
%_man1dir/fppkg.1*
%_man1dir/ppc*.*
%_man1dir/grab_vcsa.*
%_man5dir/fpc.cfg.*

# utils
%package utils
Summary: Free Pascal -- Utils
Group: Development/Other
Obsoletes: fpcmake data2inc

%description utils
This package contains some handy utils for usage with the Free Pascal
Compiler:
  - ppumove     Place multiple units in a shared library
  - ppufiles    Show needed files for units
  - ppudump     Dump the information stored in a .ppu (unit) file
  - fpcmake     Create Makefile from Makefile.fpc
  - h2pas       Convert .h files to pascal units
  - ppdep       Create a dependency file which can be used with
                Makefiles
  - ptop        Source beautifier
  - data2inc    Convert binary/text data to include files
  - plex/pyacc  Pascal Lex/Yacc implementation

%files utils
%doc fpcsrc/utils/fpcm/fpcmake.ini
%_bindir/bin2obj
%_bindir/chmcmd
%_bindir/chmls
%_bindir/data2inc
%_bindir/delp
%_bindir/fpcjres
%_bindir/fpclasschart*
%_bindir/fpcmake
%_bindir/fpcres
%_bindir/fpdoc
%_bindir/fprcp
%_bindir/h2pas
%_bindir/h2paspp
%_bindir/instantfpc
%_bindir/makeskel*
%_bindir/mkarmins
%_bindir/mkx86ins
%_bindir/pas2fpm
%_bindir/pas2jni
%_bindir/pas2ut*
%_bindir/plex
%_bindir/postw32
%_bindir/ppdep
%_bindir/ppudump
%_bindir/ppufiles
%_bindir/ppumove
%_bindir/ptop
%_bindir/ptop.rsj
%_bindir/pyacc
%_bindir/relpath
%_bindir/rmcvsdir
%_bindir/rstconv*
%_bindir/unitdiff*
%if_with doc
%_bindir/writeidx
%endif
# Other utilities
%_bindir/cldrparser
%_bindir/mkinsadd
%_bindir/unihelper
%_bindir/compileserver
%_bindir/json2pas
%_bindir/mka64ins
%_bindir/pas2js
%_bindir/webidl2pas
#
%fpc_dir/lexyacc
%fpc_unitdir/utils-lexyacc
%fpc_fpmdir/utils-lexyacc.fpm
%_man1dir/bin2obj.1*
%_man1dir/chmcmd.1*
%_man1dir/chmls.1*
%_man1dir/data2inc.1*
%_man1dir/delp.1*
%_man1dir/fpcjres.1*
%_man1dir/fpclasschart.1*
%_man1dir/fpcmake.1*
%_man1dir/fpcres.1*
%_man1dir/fpdoc.1*
%_man1dir/fprcp.1*
#_man1dir/instantfpc.1*
%_man1dir/h2pas.1*
%_man1dir/h2paspp.1*
%_man1dir/makeskel.1*
%_man1dir/pas2fpm.1*
%_man1dir/pas2jni.1*
%_man1dir/pas2ut.1*
%_man1dir/plex.1*
%_man1dir/postw32.1*
%_man1dir/ppdep.1*
%_man1dir/ppudump.1*
%_man1dir/ppufiles.1*
%_man1dir/ppumove.1*
%_man1dir/ptop.1*
%_man1dir/pyacc.1*
%_man1dir/relpath.1*
%_man1dir/rmcvsdir.1*
%_man1dir/rstconv.1*
%_man1dir/unitdiff.1*
%_man5dir/fpcmake.5*
%_man5dir/ptop.cfg.5*

# packages/rtl
%package units-rtl
Summary: Free Pascal -- Runtime Library
Group: Development/Other
Requires: %name-compiler = %{?epoch:%epoch:}%version-%release

%description units-rtl
This package contains the Runtime Libraries for the Free Pascal
Compiler.

%files units-rtl
%dir %fpc_dir/units
%dir %fpc_unitdir
%doc %fpc_docdir/rtl-generics
%fpc_unitdir/rtl
%fpc_unitdir/rtl-console
%fpc_unitdir/rtl-generics
%fpc_unitdir/rtl-extra
%fpc_unitdir/rtl-objpas
%fpc_unitdir/rtl-unicode
%fpc_fpmdir/rtl-*.fpm

# packages/base
%package units-base
Summary: Free Pascal -- base units
Group: Development/Other

%description units-base
This package contains Free Pascal units for common libraries. Some of
these units are also required by the Free Component Library:
 - X11 (Xlib, Xutil)
 - NCurses
 - ZLib

%files units-base
%doc %fpc_docdir/hash
%doc %fpc_docdir/iconvenc
%doc %fpc_docdir/ncurses
%doc %fpc_docdir/pasjpeg
%doc %fpc_docdir/paszlib
%doc %fpc_docdir/regexpr
%doc %fpc_docdir/uuid
%fpc_unitdir/fppkg
%fpc_unitdir/hash
%fpc_unitdir/iconvenc
%fpc_unitdir/ncurses
%fpc_unitdir/pasjpeg
%fpc_unitdir/paszlib
%fpc_unitdir/regexpr
%fpc_unitdir/uuid
%fpc_unitdir/x11
%fpc_fpmdir/fppkg.fpm
%fpc_fpmdir/hash.fpm
%fpc_fpmdir/iconvenc.fpm
%fpc_fpmdir/ncurses.fpm
%fpc_fpmdir/pasjpeg.fpm
%fpc_fpmdir/paszlib.fpm
%fpc_fpmdir/regexpr.fpm
%fpc_fpmdir/uuid.fpm
%fpc_fpmdir/x11.fpm

# packages/fcl
%package units-fcl
Summary: Free Pascal -- Free Component Library
Group: Development/Other

%description units-fcl
This package contains the Free Component Library for the Free Pascal
Compiler.

%files units-fcl
%doc %fpc_docdir/fcl-*
%fpc_unitdir/fcl-async
%fpc_unitdir/fcl-base
%fpc_unitdir/fcl-db
%fpc_unitdir/fcl-extra
%fpc_unitdir/fcl-fpcunit
%fpc_unitdir/fcl-image
%fpc_unitdir/fcl-js
%fpc_unitdir/fcl-json
%fpc_unitdir/fcl-net
%fpc_unitdir/fcl-pdf
%fpc_unitdir/fcl-passrc
%fpc_unitdir/fcl-process
%fpc_unitdir/fcl-registry
%fpc_unitdir/fcl-res
%fpc_unitdir/fcl-sdo
%fpc_unitdir/fcl-sound
%fpc_unitdir/fcl-stl
%fpc_unitdir/fcl-web
%fpc_unitdir/fcl-xml
%fpc_fpmdir/fcl-*.fpm

# packages/fv
%package units-fv
Summary: Free Pascal -- Free Vision units
Group: Development/Other

%description units-fv
This package contains the Free Vision units for the Free Pascal
Compiler.

%files units-fv
%doc %fpc_docdir/fv
%fpc_unitdir/fv
%fpc_fpmdir/fv.fpm

# packages/gtk2
%package units-gtk2
Summary: Free Pascal -- GTK+ 2.x units
Group: Development/Other

%description units-gtk2
This package contains Free Pascal units and examples to create
programs with GTK+ 2.x.

%files units-gtk2
%doc %fpc_docdir/gtk2
%fpc_unitdir/gtk2
%fpc_fpmdir/gtk2.fpm

# packages/db
%package units-db
Summary: Free Pascal -- database libraries units
Group: Development/Other

%description units-db
This package contains Free Pascal units with bindings for:
 - MySQL
 - Interbase
 - PostgreSQL
 - Oracle
 - ODBC
 - GDBM
 - SQLite

%files units-db
%doc %fpc_docdir/gdbm
%doc %fpc_docdir/ibase
%doc %fpc_docdir/mysql
%doc %fpc_docdir/odbc
%doc %fpc_docdir/oracle
%doc %fpc_docdir/postgres
%doc %fpc_docdir/pxlib
%doc %fpc_docdir/sqlite
%fpc_unitdir/dblib
%fpc_unitdir/gdbm
%fpc_unitdir/ibase
%fpc_unitdir/ldap
%fpc_unitdir/mysql
%fpc_unitdir/odbc
%fpc_unitdir/oracle
%fpc_unitdir/postgres
%fpc_unitdir/pxlib
%fpc_unitdir/sqlite
%fpc_fpmdir/dblib.fpm
%fpc_fpmdir/gdbm.fpm
%fpc_fpmdir/ibase.fpm
%fpc_fpmdir/ldap.fpm
%fpc_fpmdir/mysql.fpm
%fpc_fpmdir/odbc.fpm
%fpc_fpmdir/oracle.fpm
%fpc_fpmdir/postgres.fpm
%fpc_fpmdir/pxlib.fpm
%fpc_fpmdir/sqlite.fpm

# packages/gfx
%package units-gfx
Summary: Free Pascal -- graphics libraries units
Group: Development/Other
Requires: libX11-devel libXext-devel libXrandr-devel libXxf86dga-devel libXxf86vm-devel
%ifnarch aarch64
Requires: svgalib-devel
%endif

%description units-gfx
This package contains Free Pascal units with bindings for:
 - opengl: OpenGL
 - opengles
 - forms: Forms 0.88
 - svgalib: Svgalib
 - ggi: General Graphical Interface
 - libgd
 - libpng
 - graph
 - cairo

%files units-gfx
%doc %fpc_docdir/ggi
%doc %fpc_docdir/imagemagick
%doc %fpc_docdir/libgd
%doc %fpc_docdir/opengl
%doc %fpc_docdir/opengles
%doc %fpc_docdir/ptc
%doc %fpc_docdir/svgalib
%doc %fpc_docdir/xforms
%fpc_unitdir/cairo
%fpc_unitdir/ggi
%ifnarch aarch64
%fpc_unitdir/graph
%endif
%fpc_unitdir/hermes
%fpc_unitdir/imagemagick
%fpc_unitdir/libgd
%fpc_unitdir/libpng
%ifnarch aarch64
%fpc_unitdir/opencl
%endif
%fpc_unitdir/opengl
%fpc_unitdir/opengles
%fpc_unitdir/ptc
%fpc_unitdir/rsvg
%fpc_unitdir/svgalib
%fpc_unitdir/xforms
%_bindir/fd2pascal
%_man1dir/fd2pascal.1*
%fpc_fpmdir/cairo.fpm
%fpc_fpmdir/ggi.fpm
%ifnarch aarch64
%fpc_fpmdir/graph.fpm
%endif
%fpc_fpmdir/hermes.fpm
%fpc_fpmdir/imagemagick.fpm
%fpc_fpmdir/libgd.fpm
%fpc_fpmdir/libpng.fpm
%ifnarch aarch64
%fpc_fpmdir/opencl.fpm
%endif
%fpc_fpmdir/opengl.fpm
%fpc_fpmdir/opengles.fpm
%fpc_fpmdir/ptc.fpm
%fpc_fpmdir/rsvg.fpm
%fpc_fpmdir/svgalib.fpm
%fpc_fpmdir/xforms.fpm

# packages/net
%package units-net
Summary: Free Pascal -- networking units
Group: Development/Other
#Requires: %name = %version-%release

%description units-net
This package contains Free Pascal units for creating network tools:
 - netdb: NetDB unit for TCP/IP handling
 - libasync: LibAsync unit for easy Asynchronous IO
 - libcurl
 - dbus: D-Bus
 - gnutls
 - googleapi
 - httpd-1.3
 - httpd-2.0
 - httpd-2.2
 - ldap
 - libmagic
 - libmicrohttpd
 - openssl: Open SSL
 - pcap

%files units-net
%doc %fpc_docdir/dbus
%doc %fpc_docdir/gnutls
%doc %fpc_docdir/httpd*
%doc %fpc_docdir/libcurl
%doc %fpc_docdir/libmagic
%doc %fpc_docdir/libmicrohttpd
%doc %fpc_docdir/openssl
%fpc_unitdir/dbus
%fpc_unitdir/fastcgi
%fpc_unitdir/gnutls
%fpc_unitdir/googleapi
%fpc_unitdir/httpd*
%fpc_unitdir/libcurl
%fpc_unitdir/libmagic
%fpc_unitdir/libmicrohttpd
%fpc_unitdir/openssl
%fpc_unitdir/pcap
%fpc_unitdir/vcl-compat
%fpc_unitdir/zorba
%fpc_fpmdir/dbus.fpm
%fpc_fpmdir/fastcgi.fpm
%fpc_fpmdir/gnutls.fpm
%fpc_fpmdir/googleapi.fpm
%fpc_fpmdir/httpd*.fpm
%fpc_fpmdir/libcurl.fpm
%fpc_fpmdir/libmagic.fpm
%fpc_fpmdir/libmicrohttpd.fpm
%fpc_fpmdir/openssl.fpm
%fpc_fpmdir/pcap.fpm
%fpc_fpmdir/vcl-compat.fpm
%fpc_fpmdir/zorba.fpm

# packages/math
%package units-math
Summary: Free Pascal - math units
Group: Development/Other

%description units-math
This package contains Free Pascal math interfacing units for:
 - gmp: Interface for the GNU Multiple Precision Arithmetic Library
 - proj4: Compute projections
 - numlib: numerical computing
 - symbolic: symbolic computing

%files units-math
%doc %fpc_docdir/gmp
%doc %fpc_docdir/numlib
%doc %fpc_docdir/symbolic
%fpc_unitdir/gmp
%fpc_unitdir/numlib
%fpc_unitdir/proj4
%fpc_unitdir/symbolic
%fpc_fpmdir/gmp.fpm
%fpc_fpmdir/numlib.fpm
%fpc_fpmdir/proj4.fpm
%fpc_fpmdir/symbolic.fpm

# packages/misc
%package units-misc
Summary: Free Pascal -- miscellaneous units
Group: Development/Other

%description units-misc
This package contains Free Pascal miscellaneous units for:
 - fppkg: support of FPC packaging system
 - Utmp
 - PasZLib (Pascal-only zlib implementation)

%files units-misc
%_libdir/libpas2jslib.so
%doc %fpc_docdir/aspell
%doc %fpc_docdir/bzip2
%doc %fpc_docdir/cdrom
%doc %fpc_docdir/fftw
%doc %fpc_docdir/gdbint
%doc %fpc_docdir/libsee
%doc %fpc_docdir/libxml2
%doc %fpc_docdir/newt
%doc %fpc_docdir/syslog
%doc %fpc_docdir/tcl
%doc %fpc_docdir/users
%doc %fpc_docdir/utmp
%doc %fpc_docdir/libenet
%ifnarch aarch64 %ix86
%doc %fpc_docdir/libffi
%endif
%doc %fpc_docdir/libfontconfig
%doc %fpc_docdir/libgc
%ifarch %ix86
%doc %fpc_docdir/libc
%fpc_unitdir/libc
%fpc_unitdir/unixutil
%fpc_fpmdir/libc.fpm
%fpc_fpmdir/unixutil.fpm
%endif
%fpc_unitdir/aspell
%fpc_unitdir/bfd
%fpc_unitdir/bzip2
%fpc_unitdir/cdrom
%fpc_unitdir/chm
%fpc_unitdir/fftw
%fpc_unitdir/fpindexer
%fpc_unitdir/fpmkunit
%fpc_unitdir/gdbint
%fpc_unitdir/jni
%fpc_unitdir/libsee
%fpc_unitdir/libtar
%fpc_unitdir/libxml2
%fpc_unitdir/lua
%fpc_unitdir/newt
%fpc_unitdir/pthreads
%fpc_unitdir/syslog
%fpc_unitdir/tcl
%fpc_unitdir/unzip
%fpc_unitdir/users
%fpc_unitdir/utmp
%fpc_unitdir/zlib
%fpc_unitdir/fcl-report
%fpc_unitdir/libcups
%fpc_unitdir/libenet
%ifnarch aarch64 %ix86
%fpc_unitdir/libffi
%endif
%fpc_unitdir/libfontconfig
%fpc_unitdir/libgc
%fpc_unitdir/libusb
%fpc_unitdir/odata
%fpc_unitdir/pastojs
%fpc_unitdir/utils-pas2js
%fpc_unitdir/webidl
%fpc_fpmdir/aspell.fpm
%fpc_fpmdir/bfd.fpm
%fpc_fpmdir/bzip2.fpm
%fpc_fpmdir/cdrom.fpm
%fpc_fpmdir/chm.fpm
%fpc_fpmdir/fftw.fpm
%fpc_fpmdir/fpindexer.fpm
%fpc_fpmdir/fpmkunit.fpm
%fpc_fpmdir/gdbint.fpm
%fpc_fpmdir/jni.fpm
%fpc_fpmdir/libsee.fpm
%fpc_fpmdir/libtar.fpm
%fpc_fpmdir/libxml2.fpm
%fpc_fpmdir/lua.fpm
%fpc_fpmdir/newt.fpm
%fpc_fpmdir/pthreads.fpm
%fpc_fpmdir/syslog.fpm
%fpc_fpmdir/tcl.fpm
%fpc_fpmdir/unzip.fpm
%fpc_fpmdir/users.fpm
%fpc_fpmdir/utmp.fpm
%fpc_fpmdir/zlib.fpm
%fpc_fpmdir/libcups.fpm
%fpc_fpmdir/libenet.fpm
%ifnarch aarch64 %ix86
%fpc_fpmdir/libffi.fpm
%endif
%fpc_fpmdir/libfontconfig.fpm
%fpc_fpmdir/libgc.fpm
%fpc_fpmdir/libusb.fpm
%fpc_fpmdir/odata.fpm
%fpc_fpmdir/pastojs.fpm
%fpc_fpmdir/utils-pas2js.fpm
%fpc_fpmdir/webidl.fpm

# packages/media
%package units-multimedia
Summary: Free Pascal -- multimedia libraries units
Group: Development/Other
Obsoletes: fpc-units-media <= 2.2.0
Provides: fpc-units-media

%description units-multimedia
This package contains Free Pascal multimedia interfacing units for:
 - oggvorbis
 - openal
 - a52
 - dts (http://www.videolan.org/developers/libdca.html)
 - mad
 - modplug

%files units-multimedia
%doc %fpc_docdir/openal
%fpc_unitdir/a52
%fpc_unitdir/dts
%fpc_unitdir/libvlc
%fpc_unitdir/mad
%fpc_unitdir/modplug
%fpc_unitdir/oggvorbis
%fpc_unitdir/openal
%fpc_unitdir/sdl
%fpc_fpmdir/a52.fpm
%fpc_fpmdir/dts.fpm
%fpc_fpmdir/libvlc.fpm
%fpc_fpmdir/mad.fpm
%fpc_fpmdir/modplug.fpm
%fpc_fpmdir/oggvorbis.fpm
%fpc_fpmdir/openal.fpm
%fpc_fpmdir/sdl.fpm

# ide
%package ide
Summary: Free Pascal -- IDE
Group: Development/Other
Requires: %name-common = %EVR
Requires: fpc-units-base = %EVR

%description ide
This package contains the Integrated Development Environment (IDE) for
Free Pascal. The IDE has an internal compiler.

%files ide
%config(noreplace) %_sysconfdir/fp.cfg
%_bindir/fp
%_bindir/fp.rsj
%_bindir/fp-bin
%fpc_dir/ide/*
%fpc_fpmdir/ide.fpm
%_man1dir/fp.1*
%doc %fpc_docdir/ide/readme.ide
%_pixmapsdir/*
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
%_desktopdir/*.desktop

# src
%if_with sources
%package src
Summary: Source of Free Pascal
Group: Development/Other
BuildArch: noarch
#Requires: %name = %version-%release

%description src
This package contains Free Pascal's own source code. It is meant to be
used by the Lazarus IDE.

%files src
%_datadir/fpcsrc
%endif

%if_with doc
%package docs
Group: Documentation
Summary: Free Pascal Compiler - Documentation

%description docs
This package provides documentation for the Free Pascal Compiler in HTML
and PDF format.

%files docs
%doc %fpc_docdir/buttons
%doc %fpc_docdir/chart
%doc %fpc_docdir/fcl
%doc %fpc_docdir/fclres
%doc %fpc_docdir/fpctoc.*
%doc %fpc_docdir/fpdoc
%doc %fpc_docdir/pics
%doc %fpc_docdir/prog
%doc %fpc_docdir/ref
%doc %fpc_docdir/rtl
%doc %fpc_docdir/user
%endif

%if_with win32
# win32
%package win32
Summary: Free Pascal runtime library units cross-compiled for win32
Group: Development/Other
Requires: %name = %{?epoch:%epoch:}%version-%release
#Requires: i386-mingw32msvc-binutils

%description win32
Free Pascal runtime library units cross-compiled for win32.

%files win32
%ifnarch %ix86
%_bindir/ppc386
%fpc_dir/ppc386
%endif
%fpc_files *-win32 rtl
%endif

%changelog
* Fri Oct 02 2020 Andrey Cherepanov <cas@altlinux.org> 3:3.2.0-alt2
- Build without bootstrap.

* Tue Jul 21 2020 Andrey Cherepanov <cas@altlinux.org> 3:3.2.0-alt1
- Downgrade to stable version 3.2.0.
- New network units: gnutls, libmagic and vcl-compat.

* Wed Jan 23 2019 Andrey Cherepanov <cas@altlinux.org> 2:3.3.1-alt0.1
- New version from trunk because it supports gdb 8.x (ALT #35832).

* Wed Dec 20 2017 Andrey Cherepanov <cas@altlinux.org> 2:3.0.4-alt1
- New version.
- Package new units libmicrohttpd, googleapi and fcl-pdf.
- Fix build documentation.

* Thu Mar 02 2017 Andrey Cherepanov <cas@altlinux.org> 2:3.0.2-alt1
- New version
- Build without documentation

* Mon Dec 14 2015 Andrey Cherepanov <cas@altlinux.org> 2:3.0.0-alt1
- New version
- Drop support of gtk1 and gnome1
- Move examples to unit subpackages
- Auto add existing documentation now works even ini file is missing
- Show progress in writeidx

* Thu Oct 22 2015 Andrey Cherepanov <cas@altlinux.org> 2:2.6.4-alt4
- Require rpm-build-fpc (ALT #31394)

* Tue Dec 02 2014 Andrey Cherepanov <cas@altlinux.org> 2:2.6.4-alt3
- Set path to ide without version and text/ subdirectory. Use ~/fpc/ide
  instead of ~/.fp for personal stuff for IDE. (ALT #29549)
- Add note about install fpc-docs in helpsystem message about missing
  documentation
- Build help index generator -- writeidx
- Generate or use generated help index
- Package documentation to %_defaultdocdir/fpc without version
- Automatically add help index from %_defaultdocdir/fpc/fpctoc.htx if it
  exists

* Mon Oct 06 2014 Andrey Cherepanov <cas@altlinux.org> 2:2.6.4-alt2
- Fix pathes in configuration on x86_64

* Wed Aug 13 2014 Andrey Cherepanov <cas@altlinux.org> 2:2.6.4-alt1
- New version
- Apply patches from Debian and Mageia
- Shorten Russian translation of GenericName
- Add watch file for upstream tracking
- Move sources from separate branch to subdirectory

* Fri Dec 06 2013 Andrey Cherepanov <cas@altlinux.org> 2:2.6.2-alt2
- Remove excess optimization on Pentium CPU that causes compile problem
  on AMD CPU (ALT #29635)

* Sun Mar 10 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2:2.6.2-alt1
- New version (ALT #28639)
- Add Requires libX11-devel libXext-devel libXrandr-devel libXxf86dga-devel libXxf86vm-devel svgalib-devel in units-gfx (ALT #26812)

* Tue Aug 28 2012 Repocop Q. A. Robot <repocop@altlinux.org> 2:2.6.0-alt2.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for fpc
  * postclean-03-private-rpm-macros for the spec file

* Fri May 11 2012 Andrey Cherepanov <cas@altlinux.org> 2:2.6.0-alt2.qa1
- Increase epoch to rollback version in p6 branch

* Sun Jan 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1:2.6.0-alt2
- New version 
- Fix (ALT #26509)

* Sat Dec 10 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1:2.6.0-alt1rc1
- RC1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:2.5.20110826-alt2.1
- Rebuild with Python-2.7

* Sat Aug 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1:2.5.20110826-alt2
- Add Epoch for downgrade fpc in t6

* Fri Aug 26 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20110826-alt1
- New development snapshot
- Fix build for x86_64 with bootstrap
- Update spec

* Sat Apr 30 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20110430-alt1
- New development snapshot
- Use bootstrap for build
- Update spec

* Sun Feb 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20110227-alt1
- New development snapshot

* Sun Feb 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20101117-alt1
- New development snapshot
- Update spec

* Thu Sep 09 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20100406-alt3
- Fix (ALT #24050)

* Thu May 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20100406-alt2
- Fix encoding of errorru.msg

* Tue Apr 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.20100406-alt1
- New development version

* Fri Jan 01 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.0-alt1
- New version
- Update descriptions
- Add new subpackage %name-units-math
- Disable build documentation

* Wed Dec 02 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.4-alt4
- Fix fp.desktop

* Thu Oct 01 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.4-alt3
- Add new subpackage %name-common for provide common dirs
- Build docs
- Set BuildArch: noarch in %name-src %name-docs packages

* Wed Sep 30 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.4-alt2
- Update spec for remove workaround for #11921
- Add fpcmake.ini to /usr/share/doc/%name-utils/ (ALT #20638)

* Sun Apr 19 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.2.4-alt1
- 2.2.4
- Switch to git
- Update spec (Thanks ender@)
- Add options for switch off win32 subpackage
- Cross-compiling from non-i386 to i386 is not yet supported at this time. Comment it.

* Sat Aug 16 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.2.2-alt1
- New version
- Update spec
- Rename subpackage fpc-units-media to fpc-units-multimedia

* Wed Dec 12 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0-alt3
- Cleanup fpc-src package for use minimal space. Removed %_datadir/fpcsrc/{ide,installer,tests,utils}
- Rename fp -> fp-bin and fp.sh -> fp (#13701)
- Add BuildRequires: fpc-utils

* Mon Nov 19 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0-alt2
- Fix #13442 (Thanks sbolshakov@)

* Tue Sep 11 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0-alt1
- New version
- Fix #12904 , #12758
- Add ru_utf8 message file and make default
- Add fp.sh: wrapper for copy /etc/fp.cfg -> $HOME/fpc/fp.cfg and start fp

* Wed Aug 01 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.4-alt2
- rebuilt with new fpc

* Tue May 22 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.4-alt1
- New version
- subpackages: fpc-units-rtl, fpc-compiler, fpc-units-base, fpc-ide, fpc-units-fcl, fpc-units-fv,
  fpc-units-gtk, fpc-units-gtk2, fpc-units-gnome1, fpc-units-db, fpc-units-gfx, fpc-units-net,
  fpc-units-misc, fpc-units-media, fpc-src

* Thu Feb 01 2007 Alexey Tourbin <at@altlinux.ru> 2.1-alt3
- updated to svn revision 6276

* Sun Jan 21 2007 Alexey Tourbin <at@altlinux.ru> 2.1-alt2
- updated to svn revision 6095 (fixes x86_64 build)
- packaged %_bindir/msg2inc

* Thu Jan 18 2007 Alexey Tourbin <at@altlinux.ru> 2.1-alt1
- this release is based on 2.1 development branch
- imported compiler/ and rtl/ from svn trunk; adapted for gear
- packaged internal compiler units into fpc-compunits package
- rtl/inc/videoh.inc: changed max screen width from 132 to 240
- fpc-win32: removed mingw32 binutils dependency (internal linker on)

* Sat Sep 16 2006 Alexey Tourbin <at@altlinux.ru> 2.0.4-alt2.1
- removed fpcmake from build requires; this should now build
  on x86_64, but will fail on i586, which is ok

* Sat Sep 16 2006 Alexey Tourbin <at@altlinux.ru> 2.0.4-alt2
- don't strip static libraries

* Sun Sep 10 2006 Alexey Tourbin <at@altlinux.ru> 2.0.4-alt1
- 2.0.2 -> 2.0.4+ (svn revision 4597)
- only fpc and rtl packaged now from here; buncha funky wild-ass
  units to be packaged separately
- fpc-win32 now works on x86_84 (as well as x86)

* Tue May 02 2006 Alexey Tourbin <at@altlinux.ru> 2.0.2-alt1
- 2.0.0 -> 2.0.2, Sisyphus release
- x86_64 build ok
- subpackages: fpc, fpc-utils, fpc-packages, fpc-ide, etc.;
  fpc-win32: cross-compile for win32 (i586 only)
- docs will be packaged separately
- TODO: examples unpackaged

* Fri Oct 21 2005 Alexey Tourbin <at@altlinux.ru> 2.0.0-alt1
- 1.0.10 -> 2.0.0
- fpcdir:='%_libdir/fpc2'; fpcdocdir:='%_defaultdocdir/fpc2'
- forward release for Daedalus

* Tue Feb 11 2004 Sergey P. Kondratyev <seirge@altlinux.ru> 1.0.10-alt1
- new version + docs and examples

* Mon Oct 07 2002 Michael Shigorin <mike@altlinux.ru> 1.0.6-alt1.1
- spec cleanup

* Sat Sep 19 2002 Sergey <skrivulja@erec.ru>
- adopted for Master

