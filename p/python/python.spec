# -*- rpm-spec -*-

%define real_name               python
Name: %real_name

Version: 2.7.16
Release: alt1.M90P.1

%define package_name		%real_name
%define weight			1001
%define suffix_ver		2.7
%define require_ver		2.7
%define python_name		%real_name%suffix_ver
%define __python_version	%suffix_ver
%define __python		%_builddir/Python-%version/python
%define nodot_ver		27
# When suffix_ver was removed from real_name
%define noversion_from		%suffix_ver-alt1

%def_with tk
%def_with ssl
%def_with bluez

%ifarch %ix86 x86_64
%def_with valgrind
%else
%def_without valgrind
%endif

%global _optlevel 3

Summary: An interpreted, interactive object-oriented programming language
License: PSF
Group: Development/Python
URL: http://www.python.org/
Packager: Python Development Team <python@packages.altlinux.org>

# ftp://ftp.python.org/pub/python/%version/Python-%version.tar.bz2
Source: Python-%version.tar
#Source1: http://www.python.org/ftp/python/doc/%version/info-%version.tar.bz2
Source2: koi8_u.py
Source3: modules-list-%version.tar
Source8: pythonstart.py
Source9: python.sh
Source10: python.csh
Source11: pythonrc.py
Source12: bdist_altrpm.py

Patch1: python-2.5.1-deb-setup.patch
Patch2: python-2.5.1-deb-distutils-link.patch
Patch3: python-2.5.1-alt-TextTools.patch
Patch4: python-2.6.5-alt-distutils-get_python_lib.patch
# use system libexpat library
Patch5: python-2.7.14-alt-expat.patch
# raise fatal error when extension fails to load
Patch6: python-2.5.1-alt-setup-PyBuildExt-raise.patch
# x64 build patches
Patch8: python-2.7.14-alt-lib64.patch
Patch9: python-2.7-lib64-sysconfig.patch
# add alt to the list of supported distribution
Patch10: python-2.6.2-detect-alt.patch
# add more constants to socketmodule
Patch16: python-2.7rc1-socketmodule-constants.patch
Patch17: python-2.7rc1-socketmodule-constants2.patch
Patch20: python-2.5.4-alt-python-config.patch
Patch21: python-2.6-ctypes-noexecmem.patch
Patch22: python-2.6.6-alt-bdist_altrpm.patch
Patch23: python-2.7.4-alt-linux2-platform.patch
Patch24: python-2.7.10-python-config-ldflags-alt.patch
Patch25: python2-platform-osrelease.patch
Patch26: python-ignore-env-trust-security.patch

# TODO: send upstream
Patch31: python-2.7.14-alt-test_resource-skip-impossible.patch
# TODO: a bug which needs a fix ignored for now
Patch32: python-2.7.14-alt-test_tuple-skip-bug.patch

Patch33: python-2.7.14-upstream-issue31530-patch1.patch
Patch34: python-2.7.14-upstream-issue31530-patch2.patch

# 00104 #
# Only used when "%_lib" == "lib64"
# Another lib64 fix, for distutils/tests/test_install.py; not upstream:
Patch104: 00104-lib64-fix-for-test_install.patch

# XXX ignore pydoc dependencies for now
%add_findreq_skiplist %_bindir/pydoc*
%add_python_req_skip msilib

# Ignore dependencies for Windows
%add_python_req_skip _winreg

# this package python = %version-%release requires all standard python modules
# package python = %require_ver is provided by python-strict and python-relaxed
Requires: %name-base = %version-%release
Requires: %name-modules %name-modules-encodings
Requires: %name-modules-curses %name-modules-xml %name-modules-compiler
Requires: %name-modules-email %name-modules-hotshot %name-modules-bsddb
Requires: %name-modules-logging
Requires: %name-modules-nis

BuildPreReq: rpm >= 4.0.4-alt36.d8, rpm-build-python >= 0.34.4-alt1
# Automatically added by buildreq on Sun Apr 08 2007
BuildRequires: bzlib-devel gcc-c++ libdb4-devel libexpat-devel libgdbm-devel libncursesw-devel libreadline-devel libsqlite3-devel unzip zlib-devel libffi-devel
%{?_with_tk:BuildRequires: tk-devel}
%{?_with_valgrind:BuildRequires: valgrind-devel}
%{?_with_ssl:BuildRequires: libssl-devel}
%{?_with_bluez:BuildRequires: libbluez-devel}
# Not to loose a module which used to be a part of our standard "interface"
# (i.e., no reqs were generated because nis was assumed to be always present).
BuildPreReq: libnsl2-devel
%{?!_without_check:%{?!_disable_check:BuildPreReq: /proc /dev/pts}}

# NB:
# without_bootstrap might cut out quite a few packages;
# initial python build will still be a --nodeps affair,
# those interested are invited to have a closer look.
# -- mike@

%description
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

Programmers can write new built-in modules for Python in C or C++.
Python can be used as an extension language for applications that
need a programmable interface. This package contains most of the
standard Python modules, as well as modules for interfacing to the
Tix widget set for Tk and RPM.

Note that documentation for Python is provided in the python-docs
package.

%package strict
Summary: Python with strict conflicts: using other pythons are prohibited
Group: Development/Python
Requires: %name = %version-%release
Provides: %real_name = %require_ver
Provides: %name-strict = %version-%release
Conflicts: %name-relaxed
Conflicts: python24
Conflicts: python = 2.4
Conflicts: python23
Conflicts: python = 2.3
Obsoletes: %python_name-strict <= %noversion_from
BuildArch: noarch

%description strict
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

This is a python with strict conflicts: using other pythons are prohibited.

%package relaxed
Summary: Python with relaxed conflicts: using with python24 are allowed
Group: Development/Python
Requires: %name = %version-%release
Provides: %real_name = %require_ver
Provides: %name-relaxed = %version-%release
Conflicts: %name-strict
Obsoletes: %python_name-relaxed <= %noversion_from
BuildArch: noarch

%description relaxed
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

This is a python with relaxed conflicts: using with python24 are allowed.

%package base
Summary: Base python modules and executables
Group: Development/Python
Provides: /usr/bin/python
Provides: %python_libdir %python_dynlibdir %python_sitelibdir %python_tooldir
%if "lib" != "%_lib"
Provides: %prefix/lib/%python_name %prefix/lib/%python_name/site-packages %prefix/lib/%python_name/tools
%endif
Provides: %python_name(os.path)
Provides: %python_name(pwd)
Provides: python(abi) = %suffix_ver
Obsoletes: %python_name-base <= %noversion_from
%description base
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

This package contains base python modules and executables.

%package modules
Summary: Standard python modules
Group: Development/Python
Requires: %name-base = %version-%release
Obsoletes: %python_name-modules <= %noversion_from
# We have split nis from python-modules. Therefore, for now,
# we require it in order not to break the past promises. (rpm-build-python
# didn't generate individual Requires on modules provided by python-modules.)
# After a Sisyphus test rebuild, we'll detect the packages needing python2.7(nis),
# actually rebuild them, and after that, we can drop this Requires if we want.
Requires: %name-modules-nis

%description modules
The Python programming language's interpreter can be extended with
dynamically loaded extensions and can be embedded in other programs.
This package contains the header files and libraries needed to do
these types of tasks.

Install this package if you want to develop Python extensions.  The
%name package will also need to be installed.  You'll probably also
want to install the python-docs package, which contains Python
documentation.

%package user-scripts
Summary: Python scripts for user improvements
Group: Development/Python
BuildArch: noarch
Requires: %name-modules = %version-%release

%description user-scripts
Python scripts for user improvements. Current release includes console
autocompletion based on readline for command line interface.

%package modules-distutils
Summary: Python "distutils" module
Group: Development/Python
# distutils used to be a part of python-dev:
Conflicts: %name-dev < 0:2.7.14-alt6
# To mitigate the absence of something after the separation, we should ensure
# that we install maximum Python minus python-dev (cf. python-dev's deps):
# (TODO: don't require extra stuff; however, I believe that
# patching the other specs for this is not a priority task.)
Requires: %name-modules = %version-%release
Requires: %name = %version-%release

%description modules-distutils
The "distutils" modules included with the Python distribution.

distutils are used when preparing Python packages for distribution,
but also at runtime by some Python libraries/executables.

%package modules-encodings
Summary: Python "encodings" module
Group: Development/Python
Requires: %name-modules = %version-%release
Obsoletes: %python_name-modules-encodings <= %noversion_from

%description modules-encodings
Standard Python encoding modules are provided by this package.

Codec modules have names corresponding to normalized encoding
names, e.g. 'utf-8' is implemented by the module 'utf_8.py'.

#%package obsolete
#Summary: Obsoleted python modules
#Group: Development/Python
#Requires: %name-base = %version-%release
#Obsoletes: %python_name-obsolete  <= %noversion_from
#
#%description obsolete
#Python is an interpreted, interactive, object-oriented programming
#language often compared to Tcl, Perl, Scheme or Java. Python includes
#modules, classes, exceptions, very high level dynamic data types and
#dynamic typing. Python supports interfaces to many system calls and
#libraries, as well as to various windowing systems (X11, Motif, Tk,
#Mac and MFC).
#
#This package contains obsolete python modules.

%package modules-curses
Summary: Python "curses" module
Group: Development/Python
Requires: %name-base = %version-%release
Obsoletes: %python_name-modules-curses

%description modules-curses
An interface to the curses library, providing portable terminal
handling. The Curses module provides an interface to the curses library, the
de-facto standard for portable advanced terminal handling.
This extension module is designed to match the API of ncurses, an
open-source curses library hosted on Linux and the BSD variants of UNIX.

%package modules-xml
Summary: Core XML support for Python
Group: Development/Python
Requires: %name-modules = %version-%release
Obsoletes: %python_name-modules-xml <= %noversion_from

%description modules-xml
This package contains three sub-packages:

dom -- The W3C Document Object Model.  This supports DOM Level 1 +
       Namespaces.

parsers -- Python wrappers for XML parsers (currently only supports Expat).

sax -- The Simple API for XML, developed by XML-Dev, led by David Megginson
       and ported to Python by Lars Marius Garshol.  This supports the SAX 2
       API.

%package modules-compiler
Summary: Package for parsing and compiling Python source code
Group: Development/Python
Requires: %name-modules = %version-%release
Obsoletes: %python_name-modules-compiler <= %noversion_from

%description modules-compiler
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

This is a package for parsing and compiling Python source code.

%package modules-email
Summary: A package for parsing, handling, and generating email messages
Group: Development/Python
Requires: %name-modules = %version-%release
Obsoletes: %python_name-modules-email <= %noversion_from

%description modules-email
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

This is a package for parsing, handling, and generating email messages.

%package modules-hotshot
Summary: High-perfomance logging profiler, mostly written in C
Group: Development/Python
Requires: %name-modules = %version-%release
Obsoletes: %python_name-modules-hotshot <= %noversion_from

%description modules-hotshot
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

This package contains high-perfomance logging profiler.

%package modules-bsddb
Summary: Support for BerkeleyDB 3.2 through 4.2
Group: Development/Python
Requires: %name-modules = %version-%release
Obsoletes: %python_name-modules-bsddb <= %noversion_from

%description modules-bsddb
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

This package contains BerkeleyDB support modules.

%package modules-ctypes
Summary: C libraries and data types wrapper helper for Python
Group: Development/Python
Requires: %name-modules = %version-%release
Obsoletes: %python_name-modules-ctypes <= %noversion_from, %python_name-module-ctypes <= %noversion_from
# ALT#18874
Provides: python-module-ctypes = %version-%release
Obsoletes: python-module-ctypes

%description modules-ctypes
ctypes is an advanced ffi (Foreign Function Interface) package for
Python 2.3 and higher.

ctypes allows to call functions exposed from dlls/shared libraries and
has extensive facilities to create, access and manipulate simple and
complicated C data types in Python - in other words: wrap libraries in
pure Python. It is even possible to implement C callback functions in
pure Python.

ctypes now includes a code generator toolchain which allows automatic
creation of library wrappers from C header files.

%package modules-wsgiref
Summary: WSGI Utilities and Reference Implementation
Group: Development/Python
Requires: %name-modules = %version-%release
Obsoletes: %python_name-modules-logging <= %noversion_from

%description modules-wsgiref
The Web Server Gateway Interface (WSGI) is a standard interface
between web server software and web applications written in Python.
Having a standard interface makes it easy to use an application
that supports WSGI with a number of different web servers.

Wsgiref is a reference implementation of the WSGI specification
that can be used to add WSGI support to a web server or framework.  It
provides utilities for manipulating WSGI environment variables and
response headers, base classes for implementing WSGI servers, a demo
HTTP server that serves WSGI applications, and a validation tool that
checks WSGI servers and applications for conformance to the
WSGI specification PEP 333.

%package modules-sqlite3
Summary: DB-API 2.0 interface for SQLite databases
Group: Development/Python
Requires: %name-modules = %version-%release
Obsoletes: %python_name-modules-logging <= %noversion_from

%description modules-sqlite3
SQLite is a C library that provides a lightweight disk-based database
that doesn't require a separate server process and allows accessing
the database using a nonstandard variant of the SQL query language.
Some applications can use SQLite for internal data storage.  It's also
possible to prototype an application using SQLite and then port the
code to a larger database such as PostgreSQL or Oracle.

pysqlite was written by Gerhard Ha:ring and provides a SQL interface
compliant with the DB-API 2.0 specification described by PEP 249.

%package modules-logging
Summary: Logging package for Python
Group: Development/Python
Requires: %name-modules = %version-%release
Requires: %name-modules-multiprocessing
Obsoletes: %python_name-modules-logging <= %noversion_from

%description modules-logging
Logging package for Python. Based on PEP 282 and comments thereto in
comp.lang.python, and influenced by Apache's log4j system.

%package modules-unittest
Summary: Unit testing framework for Python
Group: Development/Python
Requires: %name-modules = %version-%release

%description modules-unittest
Unit testing framawork for Python. The Python unit testing framework,
sometimes referred to as "PyUnit," is a Python language version of JUnit,
by Kent Beck and Erich Gamma.Based on PEP 282 and comments thereto in
comp.lang.python, and influenced by Apache's log4j system.

%package modules-nis
Summary: NIS module from Python
Group: Development/Python
Requires: %name-modules = %version-%release

%description modules-nis
This package contains the "nis" module from Python.

It used to be in %name-modules, but since NIS is deprecated in glibc,
this separate package was made because of extra library dependencies.

%package dev
Summary: The libraries and header files needed for Python development
Group: Development/Python
Requires: %name-modules = %version-%release
Requires: %name-modules-distutils = %version-%release
Requires: %name = %version-%release
Provides: %real_name-devel = %require_ver
Obsoletes: %python_name-modules-dev <= %noversion_from
Provides: lib%name-devel = %version-%release
# require libnsl2-devel, otherwise arch-specific modules may fail to link.
Requires: libnsl2-devel

%description dev
The Python programming language's interpreter can be extended with
dynamically loaded extensions and can be embedded in other programs.
This package contains the header files and libraries needed to do
these types of tasks.

Install this package if you want to develop Python extensions.  The
%name package will also need to be installed.  You'll probably also
want to install the python-docs package, which contains Python
documentation.

%package -n libpython
Summary: Python shared library
Group: Development/Python

%description -n libpython
This package contains Python3 shared library

%package test
Summary: Test suite for standard python modules
Group: Development/Python
Requires: %name-base = %version-%release
AutoReqProv: yes, nopython
Obsoletes: %python_name-test <= %noversion_from

%description test
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

This package contains test suite for standard python modules.

%package tools-i18n
Summary: Scripts to provide i18n support for developers
Group: Development/Python
Requires: %name-modules-compiler = %version-%release
Obsoletes: %python_name-tools-i18n <= %noversion_from

%description tools-i18n
Package provide pygettext and pymsgfmt scripts.
pygettext uses Python's standard tokenize module to scan
Python source code, generating .pot files identical to what GNU xgettext
generates for C and C++ code.

%package tools-webchecker
Summary: This is a simple web tree checker
Group: Development/Python
Requires: %name-modules-email = %version-%release
Requires: %name-modules-tkinter = %version-%release
Obsoletes: %python_name-tools-webchecker <= %noversion_from

%description tools-webchecker
This is a simple web tree checker, useful to find bad links in a web
tree.  It currently checks links pointing within the same subweb for
validity.  The main program is "webchecker.py".  Invoke it with the
option "-?") for more defails.

%package tools-pynche
Summary: The PYthonically Natural Color and Hue Editor
Group: Development/Python
Requires: %name-modules-tkinter = %version-%release
Obsoletes: %python_name-tools-pynche <= %noversion_from

%description tools-pynche
Pynche is a color editor based largely on a similar program that I
originally wrote back in 1987 for the Sunview window system.  That editor
was called ICE, the Interactive Color Editor.  I'd always wanted to port
this program to X but didn't feel like hacking X and C code to do it.  Fast
forward many years, to where Python + Tkinter provides such a nice
programming environment, with enough power, that I finally buckled down and
re-implemented it.  I changed the name because these days, too many other
systems have the acronym CE'.

%package tools-idle
Summary: An Integrated Development Environment for Python
Group: Development/Python
Requires: %name-modules-compiler = %version-%release
Requires: %name-modules-tkinter = %version-%release
Obsoletes: %python_name-tools-idle <= %noversion_from

%description tools-idle
IDLE is a basic editor and interpreter environment that ships with the
standard distribution of Python.  Good for beginners, it also serves as
clear example code for those wanting to implement a moderately
sophisticated, multi-platform GUI application.

%package tools-scripts
Summary: A collection of executable Python scripts from main distribution
Group: Development/Python
Requires: %name-modules-compiler = %version-%release
Requires: %name-modules-email = %version-%release
Requires: %name-modules-hotshot = %version-%release
Requires: %name-modules-tkinter = %version-%release
Requires: %name-dev = %version-%release
%py_requires mx.TextTools
Obsoletes: %python_name-scripts-idle <= %noversion_from

%description tools-scripts
This package contains a collection of executable Python scripts that
are useful while building, extending or managing Python.  Some (e.g.,
dutree or lll) are also generally useful UNIX tools.

%package tools-2to3
Summary: Automated Python 2 to 3 code translator
Group: Development/Python
Requires: %name-modules-logging = %version-%release

%description tools-2to3
This package contains utility for automated Python 2 to 3 code translation.
2to3 is a Python program that reads Python 2.x source code and applies a series
of fixers to transform it into valid Python 3.x code.

%package tools-smtpd
Summary: An RFC 2821 smtp proxy
Group: Development/Python
BuildArch: noarch

%description tools-smtpd
This file implements the minimal SMTP protocol as defined in RFC 821.  It
has a hierarchy of classes which implement the backend functionality for the
smtpd.  A number of classes are provided:
SMTPServer - the base class for the backend.  Raises NotImplementedError
if you try to use it.
DebuggingServer - simply prints each message it receives on stdout.
PureProxy - Proxies all messages to a real smtpd which does final delivery.
MailmanProxy - An experimental hack to work with GNU Mailman <www.list.org>.

%package modules-tkinter
Summary: A graphical user interface for the Python scripting language
Group: Development/Python
Requires: %name-modules = %version-%release
Requires: tk
Provides: tkinter = %require_ver

Obsoletes: %python_name-modules-tkinter <= %noversion_from

%description modules-tkinter
The Tkinter (Tk interface) program is an graphical user interface for
the Python scripting language.

You should install this package if you'd like to use a graphical
user interface for Python programming.

%package modules-json
Summary: Python JSON encoder and decoder
Group: Development/Python
Requires: %name-modules = %version-%release
Provides: python-module-json
Obsoletes: python-module-json

%description modules-json
JSON (JavaScript Object Notation) is a subset of JavaScript syntax
(ECMA-262 3rd edition) used as a lightweight data interchange format.

%package modules-multiprocessing
Summary: Process-based threading interface for Python
Group: Development/Python
Requires: %name-modules-ctypes = %version-%release
Requires: %name-modules-email = %version-%release

%description modules-multiprocessing
This package supports spawning processes using an API similar to the
threading module. The multiprocessing package offers both local and
remote concurrency, effectively side-stepping the Global Interpreter
Lock by using subprocesses instead of threads. Due to this, the
multiprocessing module allows the programmer to fully leverage multiple
processors on a given machine.

%package modules-ensurepip
Summary: Bootstrapping the pip installer
Group: Development/Python
Requires: %name-modules = %version-%release

%description modules-ensurepip
The ensurepip package provides support for bootstrapping the pip
installer into an existing Python installation or virtual environment.

#%package info
#Summary: Info documentation for the Python scripting language
#Group: Development/Python
#
#Obsoletes: %python_name-info <= %noversion_from
#
#%description info
#This archive contains the standard Python documentation in GNU info
#format.  Thanks go to Milan Zamazal <pdm@zamazal.org> for providing this
#conversion to the info format.
#
#Questions and comments on these documents should be directed to
#docs@python.org.

%package devel-static
Summary: Static python library for products with embeded python
Group: Development/Python

Obsoletes: %python_name-devel-static <= %noversion_from

%description devel-static
Python provides two kind of python-library to build application with
embedded-python capability. Using of shared library is preffered and
static library is obsoleted. This package are content static library and
intend only for some stupid application (configure scripts?) that can't
be linked with shared library.

%add_findreq_skiplist %python_tooldir/parseentities.py

%prep
%setup -q -n Python-%version
%undefine _python_compile_skip_x
#mkdir info
#tar -C info -xf #SOURCE1
tar -xf %SOURCE3

rm -r Modules/expat

%patch1 -p2
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%if "lib" != "%_lib"
%patch8 -p1
%patch9 -p1
%patch104 -p1
# TODO: adapt our package to other %%_lib like this:
# < %PATCH104 sed -e 's:lib64:%_lib:g' | patch -p1
%endif

%patch10 -p1
%patch16 -p1
%patch17 -p1
%patch20 -p1
#Fix SELinux execmem problems from Fedora
#This patch ffi_closure_free() implementation needs
#patch21 -p1
%patch22 -p2
install -p -m644 %SOURCE12 -t Lib/distutils/command
%patch23 -p1
%patch24 -p2
%patch25 -p1
%patch26 -p1

%patch31 -p2
#patch32 -p2

##patch33 -p1
##patch34 -p1

# XXX temporary Issue20445 fix
sed -i 's/val1 == nice(2)/val1 == nice(2)+2/' configure.ac

find -type f \( -name \*~ -o -name \*.orig \) -print0 |
	xargs -r0 rm -f --

find -type f -print0 |
    xargs -r0 grep -FZl -- /usr/local/bin/python |
    xargs -r0 sed -i 's@/usr/local/bin/python@/usr/bin/python@' --

xz -9k Misc/{HISTORY,NEWS,cheatsheet}

%build
rm -rf ../build-static
mkdir -p ../build-static
export OPT="$RPM_OPT_FLAGS -fwrapv"
libtoolize --copy --force
autoconf
##cp -rl * ../build-static/

build () {
_Target="$1"
shift
export LDFLAGS="$(pkg-config --libs libnsl)" CPPFLAGS="$(pkg-config --cflags libnsl)"
%ifarch %e2k
cc --version | grep -q '^lcc:1.21' && export LIBS+="-lcxa"
%endif
%configure \
	--with-threads \
	%{subst_with valgrind} \
	%{subst_with tk} \
	--with-system-ffi \
	--with-system-expat \
	--with-libs="$LIBS" \
	--enable-ipv6 \
	$*

%make_build LDFLAGS="-L$PWD" $_Target
}

#pushd ../build-static
##build python
#build all
#popd

build all --enable-shared

#bzip2 info/python*info*
#cat > info/python%nodot_ver.dir <<EOF
#INFO-DIR-SECTION Development/Python
#START-INFO-DIR-ENTRY
#EOF
#cat info/python.dir >> info/python%nodot_ver.dir
#cat >> info/python%nodot_ver.dir <<EOF
#END-INFO-DIR-ENTRY
#EOF

%check
# -l (to find memory leaks) is not compatible with -j...
# Therefore, we reset TESTOPTS (which includes -l by default)
# instead of adding EXTRATESTOPTS.
LC_ALL=C.UTF-8 make test TESTOPTS="-v %_smp_mflags"

%install
rln()
{
	local target=$1; shift
	local source=$1; shift
	target="$(relative "$target" "$source")"
	ln -snf "$target" "%buildroot$source"
}

mkdir -p %buildroot%_mandir
#mkdir -p %buildroot%_infodir
mkdir -p %buildroot%prefix/lib/%python_name/{site-packages,tools}
#install info/python*bz2 info/python%nodot_ver.dir %buildroot%_infodir

#  set the install path
echo '[install_scripts]' >setup.cfg
echo 'install_dir='"%buildroot%_bindir" >>setup.cfg

export LD_LIBRARY_PATH=%buildroot%_libexecdir:$LD_LIBRARY_PATH

makeinstall() {
%make \
	DESTDIR=%buildroot \
	BINDIR=%_bindir \
	LIBDIR=%_libdir \
	MANDIR=%_mandir \
	INCLUDEDIR=%_includedir \
	"$@"
install %SOURCE2 %buildroot%python_libdir/encodings
}

makeinstall install

##pushd ../build-static
##makeinstall bininstall
##popd

mv %buildroot%python_libdir/config/lib%python_name.a %buildroot%_libdir/lib%python_name.a

# cray : hack for hotshot
rm %buildroot%python_libdir/hotshot/stones.py*

# hack for pydoc
mv %buildroot%_bindir/pydoc %buildroot%_bindir/pydoc%suffix_ver

# prepare python-config and python.pc files for alternatives
rm %buildroot%_bindir/python-config %buildroot%_pkgconfigdir/python.pc

# idle
cat <<EOF >%buildroot%python_libdir/idlelib/idle - %buildroot%python_libdir/idlelib/idle.py
#! /usr/bin/%python_name
EOF

rln %python_libdir/idlelib/idle %_bindir/idle%suffix_ver
chmod +x %buildroot%python_libdir/idlelib/idle

mkdir -p %buildroot%python_tooldir

# pynche
rm -f Tools/pynche/*.pyw
cp -r Tools/pynche %buildroot%python_tooldir/
rln %python_tooldir/pynche/pynche %_bindir/pynche%suffix_ver

cp Tools/i18n/*.py %buildroot%python_tooldir/
rln %python_tooldir/pygettext.py %_bindir/pygettext
rln %python_tooldir/msgfmt.py %_bindir/pymsgfmt

cp -r Tools/webchecker/ %buildroot%python_tooldir/
for item in wcgui.py webchecker.py  websucker.py  wsgui.py; do
   rln %python_tooldir/webchecker/$item %_bindir/$(basename $item .py) #%%dirver
done

ln -f Tools/pynche/README Tools/pynche/README.pynche

# Tools/scripts
install -m 755 Tools/scripts/*.py %buildroot%python_tooldir/
rm -f %buildroot%python_tooldir/byext.py
( cd Tools/scripts; ls *.py ) | grep -v "byext.py" | sed 's@^@%python_tooldir/@;p;s/$/o/p;s/o$/c/' > .TOOLS_SCRIPTS

rm -f modules-list.full
for n in %buildroot%python_libdir/*; do
  [ -d "$n" ] || echo "$n"
done >> modules-list.full

echo >modules-exclude
for list in modules-list/*-list modules-list/base-list; do
    name=$(basename $list).tmp
    cat $list >$name
    grep "py$" $list|sed "s|.*|&c|g" >>$name
    grep "py$" $list|sed "s|.*|&o|g" >>$name
    sed <$name -e "s|^[^#]|%python_libdir/&|g"|tee $(basename $list)
done | sort  > modules-exclude

for mod in %buildroot%python_libdir/lib-dynload/*; do
  [ `basename $mod` = _tkinter.so ] || echo "$mod"
done >> modules-list.full
sed "s|%buildroot||g" <modules-list.full |sort|comm -23 - modules-exclude >other-list

# menu support
mkdir -p %buildroot%_menudir
cat > %buildroot%_menudir/idle%version << EOF
#?package(%real_name): needs=text section="Applications/Development/Interpreters" title=Python command=python
#?package(%name-tools-idle): needs="gnome" section="Applications/Development/Development environments" title="IDLE" \
longtitle="IDE for Python %version" command="NO_XALF %_bindir/idle" icon="development_section.xpm"
?package(%name-tools-idle): needs=x11 section="Applications/Development/Development environments" title="IDLE" \
longtitle="IDE for Python %version" command="%_bindir/idle" icon="development_section.xpm"
EOF

chmod -x %buildroot%python_libdir/test/*.py*

find %buildroot -type f -print0 |
	xargs -r0 grep -FZl -- %buildroot |
	xargs -r0 sed -i 's|%buildroot||g' --

touch dev-list
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
if [ "%real_name" != "%name" ]; then
echo %real_name >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name
echo %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name >> base-list
echo %real_name-devel >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
echo %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-devel >> dev-list
fi
echo %real_name-devel >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-dev
%if_with tk
echo tkinter >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%python_name-modules-tkinter
%endif
chmod 644 %buildroot%_sysconfdir/buildreqs/packages/substitute.d/*

%global python_ignored_files site-packages(/.+\\.(pth|egg-info(|/entry_points\\.txt|/namespace_packages\\.txt)))?$
mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
cat > %buildroot%_sysconfdir/buildreqs/files/ignore.d/%name << EOF
^%_libdir/python[^/]*/%python_ignored_files
%if "lib" != "%_lib"
^%prefix/lib/python[^/]*/%python_ignored_files
%endif
EOF

cat >> python.sh <<EOF
#! /bin/bash
export LD_LIBRARY_PATH=%_builddir/Python-%version
%_builddir/Python-%version/python "\$@"
EOF
chmod +x python.sh

%define __python %_builddir/Python-%version/python.sh
%define _python_lib_path %(RPM_BUILD_ROOT=%buildroot LD_LIBRARY_PATH=%buildroot%_libdir %buildroot%_bindir/python -c "import sys,os; path=os.path.normpath(os.environ['RPM_BUILD_ROOT']) ; print ' '.join([ x[len(path):] for x in [ os.path.normpath(x) for x in sys.path] if x[0:len(path)]==path])")
%add_python_req_skip bundlebuilder

# startup user script
install -m 644 %SOURCE8 %buildroot%_sysconfdir
install -d -m 755 %buildroot%_sysconfdir/profile.d
install -m 755 %SOURCE9 %SOURCE10 %buildroot%_sysconfdir/profile.d
install -d -m 755 %buildroot%_sysconfdir/skel
install -m 644 %SOURCE11 %buildroot%_sysconfdir/skel/.pythonrc.py

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%name-base-files.req.list
# %name-base dirlist for %_rpmlibdir/files.req
%python_libdir	%name-base
%python_dynlibdir	%name-base
%python_sitelibdir	%name-base
%python_tooldir	%name-base
EOF
%if "lib" != "%_lib"
cat <<\EOF >>%buildroot%_rpmlibdir/%name-base-files.req.list
%prefix/lib/%python_name	%name-base
%prefix/lib/%python_name/site-packages	%name-base
%prefix/lib/%python_name/tools	%name-base
EOF
%endif

ln -sf %python_name %buildroot%_bindir/%real_name
ln -s %python_name-config %buildroot%_bindir/python-config
ln -s pydoc%suffix_ver %buildroot%_bindir/pydoc
ln -s python-%suffix_ver.pc %buildroot%_pkgconfigdir/%real_name.pc

ln -sf idle%suffix_ver %buildroot%_bindir/idle
ln -s pynche%suffix_ver %buildroot%_bindir/pynche

rm -rf %buildroot%_libdir/%python_name/lib2to3/tests/
rm -f %buildroot%_man1dir/python2.1 %buildroot%_man1dir/python.1

%files

%files strict

%files relaxed

%files base -f base-list
%_mandir/man?/*
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%_bindir/%python_name
%_bindir/%real_name
%_bindir/%{real_name}2
%_bindir/pydoc
%_bindir/pydoc%suffix_ver
%dir %python_libdir
%dir %python_dynlibdir
%dir %python_sitelibdir
%dir %python_tooldir
%doc LICENSE
%doc Misc/{HISTORY,NEWS,cheatsheet}.xz
%if "lib" != "%_lib"
%prefix/lib/%python_name
%endif
%_rpmlibdir/%name-base-files.req.list
%python_libdir/pydoc_data
%python_libdir/importlib
%python_libdir/config
%python_sitelibdir/README
%_includedir/%python_name/pyconfig.h

%files -n libpython
%_libdir/lib%python_name.so.*

%files user-scripts
%_sysconfdir/pythonstart.py
%_sysconfdir/skel/.pythonrc.py
%_sysconfdir/profile.d/*

%files modules -f other-list
%python_libdir/plat-linux2
%exclude %python_libdir/wsgiref.egg-info

%files modules-curses -f modules-curses-list
%python_libdir/curses

%files modules-xml -f modules-xml-list
%python_libdir/xml

%files modules-compiler -f modules-compiler-list
%python_libdir/compiler

%files modules-email -f modules-email-list
%dir %python_libdir/email
%python_libdir/email/*py
%python_libdir/email/*pyc
%python_libdir/email/*pyo
%python_libdir/email/mime

%files modules-hotshot -f modules-hotshot-list
%python_libdir/hotshot

%files modules-bsddb -f modules-bsddb-list
%dir %python_libdir/bsddb
%python_libdir/bsddb/*py
%python_libdir/bsddb/*pyc
%python_libdir/bsddb/*pyo

%files modules-ctypes -f modules-ctypes-list
%dir %python_libdir/ctypes
%python_libdir/ctypes/*.py
%python_libdir/ctypes/*.py?
%python_libdir/ctypes/macholib
%exclude %python_libdir/ctypes/macholib/fetch_macholib*

%files modules-wsgiref
%python_libdir/wsgiref
%python_libdir/wsgiref.egg-info

%files modules-sqlite3 -f modules-sqlite3-list
%dir %python_libdir/sqlite3
%python_libdir/sqlite3/*.py
%python_libdir/sqlite3/*.py?

%files modules-logging -f modules-logging-list
%python_libdir/logging

%files modules-unittest -f modules-unittest-list
%python_libdir/unittest

%files modules-distutils -f modules-distutils-list
%python_libdir/distutils
%exclude %python_libdir/distutils/tests

%files modules-encodings -f modules-encodings-list
%python_libdir/encodings

%files modules-json -f modules-json-list
%python_libdir/json
%exclude %python_libdir/json/tests

%files modules-multiprocessing -f modules-multiprocessing-list
%python_libdir/multiprocessing

%files modules-ensurepip
%exclude %python_libdir/ensurepip/_bundled
%python_libdir/ensurepip/*py
%python_libdir/ensurepip/*pyc
%python_libdir/ensurepip/*pyo

%files modules-nis -f modules-nis-list

#%files obsolete
#%python_libdir/lib-old

# some tools R: p-m-tkinter
%if_with tk
%files tools-idle
%python_libdir/idlelib
%exclude %python_libdir/idlelib/idle_test/
%_bindir/idle
%_bindir/idle%suffix_ver
%exclude %_bindir/idle
%doc Lib/idlelib/README.txt Lib/idlelib/NEWS.txt Lib/idlelib/HISTORY.txt Lib/idlelib/CREDITS.txt
%_menudir/idle%version
%endif

%files tools-2to3
%python_libdir/lib2to3
%_bindir/2to3

%if_with tk
%files tools-pynche
%python_tooldir/pynche
%_bindir/pynche
%_bindir/pynche%suffix_ver
%doc Tools/pynche/README
%endif

%files tools-i18n
%python_tooldir/pygettext.py*
%python_tooldir/msgfmt.py*
%python_tooldir/makelocalealias.py*
%_bindir/pygettext
%_bindir/pymsgfmt

%if_with tk
%files tools-webchecker
%python_tooldir/webchecker/*.py*
%exclude %python_tooldir/webchecker/README
%_bindir/wcgui
%_bindir/webchecker
%_bindir/websucker
%_bindir/wsgui
%doc Tools/webchecker/README
%endif

%files tools-smtpd
%_bindir/smtpd.py

%if_with tk
%files tools-scripts -f .TOOLS_SCRIPTS
%doc Tools/scripts/README Tools/scripts/dutree.doc
%endif

%files dev -f dev-list
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-dev
%_includedir/%python_name
%exclude %_includedir/%python_name/pyconfig.h
%_libdir/lib%python_name.so
%_pkgconfigdir/python.pc
%_pkgconfigdir/python2.pc
%_pkgconfigdir/python-%suffix_ver.pc
%_bindir/%python_name-config
%_bindir/python-config
%_bindir/python2-config

%files test
%python_libdir/test
%python_libdir/ctypes/test
%python_libdir/sqlite3/test
%python_libdir/email/test
%python_libdir/bsddb/test
%python_libdir/distutils/tests

#%files info
#/usr/share/info/*
#%doc Lib/*.doc
#%doc PQR%suffix_ver.pdf PQR%suffix_ver/*

%files devel-static
%_libdir/lib%python_name.a

%if_with tk
%files modules-tkinter
%config %_sysconfdir/buildreqs/packages/substitute.d/%python_name-modules-tkinter
%python_libdir/lib-tk
%exclude %python_libdir/lib-tk/test
%python_libdir/lib-dynload/_tkinter.so
%endif

%changelog
* Fri Jan 24 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.7.16-alt1.M90P.1
- 'Trusted mode': optional modules loading paths restriction

* Mon Apr 01 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.7.16-alt1
- Updated to 2.7.16 (fixes FTBFS with openssl 1.1.1).
- Removed redundant R: alternatives.

* Tue Dec 04 2018 Fr. Br. George <george@altlinux.ru> 2.7.15-alt1
- Version up (now builds with gcc8);
- fix check section LOCALE.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.7.14-alt7.1
- NMU: Rebuild with new openssl 1.1.0.

* Mon Jul 02 2018 Ivan Zakharyaschev <imz@altlinux.org> 2.7.14-alt7
- Made distutils install maximum Python minus python-dev
  to mitigate the separation from python-dev (for building packages).

* Fri Jun 29 2018 Ivan Zakharyaschev <imz@altlinux.org> 2.7.14-alt6
- move distutils into a separate pkg from python-dev
  (because it can be used at runtime by other libs/executables).

* Fri Jun 29 2018 Michael Shigorin <mike@altlinux.org> 2.7.14-alt5
- E2K:
  + support e2kv4 through %%e2k macro (grenka@)
  + reworked -lcxa quirk towards lcc-1.23+ compatibility

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.14-alt4
- Fixed heap-use-after-free bug (Fixes: CVE-2018-1000030).

* Wed May 30 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.7.14-alt3.1
- added cleaning os-release parameters (patch25)

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.14-alt3
- NMU: updated runtime devel dependencies.

* Thu Mar 22 2018 Ivan Zakharyaschev <imz@altlinux.org> 2.7.14-alt2
- buildreq's ignore list (thx grenka@):
  + Make buildreq ignore atomic .egg-info files
    because they are read too often (ALT#34660)
  + Fix escaping of backslash in buildreq's ignore.d regular expression
- Kept nis module despite the deprecation of NIS in glibc because it
  used to be a part of our standard "interface". Split nis from
  python-modules so that the rebuild of dependents will make them
  obtain an explicit dep on it. (python-modules will require it for a
  while not to break the past promise.)
- Fixed detection of linux distribution (thx mrdrew)
- (e2k arch) Link against -lcxa (thx mike@, sem@)
- (.spec) Renamed bootstrap knob to bluez, enabled by default (thx mike@)
- (.spec) Enabled %%check

* Tue Oct 31 2017 Fr. Br. George <george@altlinux.ru> 2.7.14-alt1
- Version up
- Turn off static build that have been lost long ago

* Tue Oct 24 2017 Dmitry V. Levin <ldv@altlinux.org> 2.7.11-alt6
- python-base: compressed documentation files.

* Wed Sep 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.7.11-alt5
- libpython, python-modules: backported upstream fixes
  (Fixes: CVE-2016-0772, CVE-2016-5636)

* Tue Apr 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.7.11-alt4
- Fixed 'random' module regression caused by glibc >= 2.25 (closes: #33355).

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.7.11-alt3.qa1
- NMU: rebuilt against Tcl/Tk 8.6

* Fri Apr 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.11-alt3
- NMU: made some buildreqs/substitute.d optional (closes: #31979)

* Wed Mar 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.11-alt2
- /etc/buildreqs/files/ignore.d/python: fixed on x86_64 and added
  .egg-info/(entry_points|namespace_packages).txt.

* Tue Feb 09 2016 Michael Shigorin <mike@altlinux.org> 2.7.11-alt1.2
- BOOTSTRAP2: make ssl knob separate as python-dev needs python2.7(_ssl)

* Sun Feb 07 2016 Michael Shigorin <mike@altlinux.org> 2.7.11-alt1.1
- BOOTSTRAP:
  + added tk knob (enabled by default)
  + skip bluez, ssl when --with bootstrap (and not by default of course)

* Mon Dec 14 2015 Vladimir Didenko <cow@altlinux.org> 2.7.11-alt1
- New version

* Fri Sep 18 2015 Vladimir Didenko <cow@altlinux.org> 2.7.10-alt1
- New version (closes: #31270)
- Enable bluetooth support (closes: #31261)

* Thu Nov 13 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.7.8-alt1
- New version.

* Thu Jan 30 2014 Fr. Br. George <george@altlinux.ru> 2.7.6-alt3
- Build and install shared build, separate static (was contrariwise).
- Fix for python issue 20445.

* Fri Nov 22 2013 Dmitry V. Levin <ldv@altlinux.org> 2.7.6-alt2
- Relocated _sysconfigdata (required by sysconfig) from -modules to -base.

* Wed Nov 20 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.7.6-alt1
- New version.

* Tue Apr 09 2013 Fr. Br. George <george@altlinux.ru> 2.7.4-alt1
- Version up
- Fix patches
- Move autoconf from prep to build section

* Thu Apr 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.3-alt4
- python-2.7.3-autoconf-sem_open_check-alt.patch

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.3-alt3
- remove -lpython2.7, -L/usr/lib{,64}/python2.7/config from python-config
  --ldflags

* Sun Apr 15 2012 Dmitry V. Levin <ldv@altlinux.org> 2.7.3-alt2
- Removed libpython2.7.a from python-base which was inadvertently
  packaged there in 2.7.3-alt1.

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.3-alt1
- 2.7.3

* Thu Mar 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.2-alt5
- build python binary with static libpython
- split up independent libpython subpackage with shared library
- change optimization to -O3
- build with system ffi
- enable valgrind support
- enable ipv6

* Mon Jan 23 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.2-alt4
- Remove alternatives and post-scripts supporting multiple pythons in system
  (not working for now), pack %%_bindir/python, %%_bindir/pydoc ... (ALT #26844)

* Mon Dec 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.2-alt3
- subprocess and dependant modules moved to python-base (for rpm-build-python)

* Fri Nov 25 2011 Dmitry V. Levin <ldv@altlinux.org> 2.7.2-alt2
- Packaged /usr/bin/python2 symlink to /usr/bin/python2.7 (closes: #26624).

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.2-alt1.1
- Added /usr/bin/python2 symlink (ALT #26624)

* Wed Oct 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.2-alt1
- 2.7.2

* Tue Sep 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6.7-alt2
- Fix build on Linux-3.x kernels

* Tue Sep 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6.7-alt1
- Updated to 2.6.7.

* Fri Jun 24 2011 Dmitry V. Levin <ldv@altlinux.org> 2.6.6-alt5
- python-modules-json: added provides/obsoletes python-module-json.

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.6-alt4
- distutils.command: added bdist_altrpm.py from repository of
  rpm-build-python by request of rt@

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.6-alt3
- Moved wsgiref.egg-info into python-modules-wsgiref (ALT #25274)

* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 2.6.6-alt2
- Corrected interpackage dependencies.
- Rebuilt for soname set-versions and debuginfo.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.6-alt1
- Updated to 2.6.6.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.5-alt3
- Rebuilt with libssl.so.10.

* Fri Mar 26 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.5-alt2
- Fixed critical regression in distutils on x86-64 introduced
  along with previous package release.
- Moved "make test" to %%check section.

* Thu Mar 25 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.6.5-alt1
- Updated to 2.6.5

* Thu Mar 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt4
- Added provides python(abi)= 2.6 (ALT #23220)

* Fri Jan 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt3
- Fixed get_python_lib in distutils.sysconfig

* Mon Dec 21 2009 Alexey Tourbin <at@altlinux.ru> 2.6.4-alt2
- Moved _abcoll.py abc.py genericpath.py strop.so to python-base

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1
- Built for Sisyphus

* Wed Nov 04 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.6.4-alt1
- Updated to 2.6.4

* Mon Jul 20 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.6.2-alt2
- Fixed build for x86_64
- Add build require for new version of rpm-build-python

* Mon Jul 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.6.2-alt1
- Version up to 2.6
- Update PQR documentation
- Skip dependency for _winreg
- Remove libffi v3.0.5 due it included
- Add new subpackages json and multiprocessing
- Add 2to3 migration tool
- patches adapted

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.4-alt7
- Fixed python-config packaging bug introduced in previous build.
- Moved python.pc to alternatives.

* Sat May 16 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.5.4-alt6
- Add python-config to devel subpackage

* Fri Feb 20 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.4-alt5
- %name-base [x86_64]:
  Packaged %prefix/lib/%python_name/tools directory.

* Thu Feb 19 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.4-alt4
- %name-base: Excplicitly provide pathnames listed in
  %_rpmlibdir/%name-base-files.req.list file.

* Wed Feb 18 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.4-alt3
- Packaged %_rpmlibdir/%name-base-files.req.list.
- python-modules-ctypes:
  + Added Provides/Obsoletes python-module-ctypes (closes: #18874).
  + Removed macholib/fetch_macholib* (closes: #18875).

* Sun Feb 15 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.4-alt2
- tools-i18n: Package precompiled files.
- python-dev: Imported pkg-config support.
- Made -strict and -relaxed subpackages noarch.
- Switched to alternatives-0.4.
- Removed obsolete %%update_menus/%%clean_menus calls.
- Turned absolute symlinks into relative.
- spec: s/unzp/unzip/, reduced macro abuse.

* Thu Dec 25 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.5.4-alt1
- updated to 2.5.4 included previous CVE patches

* Fri Oct 31 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.5.2-alt5
- added subpackage python-user-scripts for user scripts support
  with command line autocompletion enabled by default

* Tue Sep 09 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.5.2-alt4
- build with last libdb4 that is libdb4.7 now
- fixed the list of supported distribution for altlinux
- add some fixes from Fedora:
 + security fix for hashlib overflow CVE-2008-2316
 + fix marshalling of objects in xmlrpclib (python bug #1739842)
 + fix sporadic listdir problem (Fedora#451494)
 + add more constants to socketmodule (Fedora#436560)
 + add new API from 2.6, set_wakeup_fd ...

* Fri Sep 05 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.5.2-alt3
- Rebuilded with new libffi v3.0.5 due to ctypes on arm-eabi (#17014)

* Sat Aug 16 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.5.2-alt2
- PQR re-added
- build with libdb4.6

* Wed Aug 13 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.5.2-alt1
- updated to 2.5.2, bugfixs release
- security fix for Python-2.5.2's CVE-2008-1721
- fixed platform.py reports "redhat" sometimes (Mandriva#9482)
- build with last libdb

* Tue Dec 11 2007 Fr. Br. George <george@altlinux.ru> 2.5.1-alt1
- version up
- test part of new modules separated, i18n-utils updated
- new sqlite3 and wsgiref modules
- fix python-2.5.1-alt-expat.patch: define_macros must be defined
- no "obsolete" modules for now
- ctypes module is new to 2.5.*
- docs version up (no more info files), spec and gear-rules adaptation
- patches adapted

* Fri Oct 26 2007 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt13
- python-relaxed: disabled /usr/bin/python automatic provides
- added substitution rule for buildreq: python-dev -> pytnon-devel

* Tue May 15 2007 Dmitry V. Levin <ldv@altlinux.org> 2.4.4-alt12
- Imported build, distutils, locale map (ALT#11495) and PyLocale_strxfrm
  (CVE-2007-2052, ALT#11737) fixes from Debian 2.4.4-4 package.

* Sun Apr 08 2007 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt11
- compiled pyexpat.so module with system libexpat library (#8256)
- moved pyexpat.so from python-modules to python-modules-xml package
- compiled curses modules with ncursesw instead of plain ncurses library
- moved _curses_panel.so from python-modules to python-modules-curses
- made python extensions link with libpython library (backported from svn)
- fixed sre*.py packaging bug (#11399)
- fixed dbm.so module linkage

* Sat Mar 24 2007 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt10
- added py_compile.py and traceback.py to python-base, for rpm-build-python

* Fri Mar 23 2007 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt9
- reconsidered interpackage dependencies, so that python-devel
  depends on all standard python modules
- moved getopt.py from python-modules to python-base

* Sun Mar 18 2007 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt8
- this release prepares python-base to be part of base build system
- /usr/bin/python is now provided by python-base; no file-level
  conflict is induced, and python-strict/relaxed logic must still work
- removed extra python dependencies from python-base; python-base
  is now self-contained
- moved time.so, re.py, and string.py from python-modules to
  python-base, so that python-base provides most common dependencies
- also moved parser.so, token.py, and symbol.py from python-modules-compiler
  to python-base, to satisfy rpm-build-python dependencies
- in %%post scripts, replaced absolute symbolic links with relative ones

* Mon Jan 08 2007 Fr. Br. George <george@altlinux.ru> 2.4.4-alt7
- Documentation search path relocate
- Replace many of 24 and 2.4 with macros (for upcoming 2.5)
- Delete izvrat_ver
- Info file update
- BuildRequires fresh

* Thu Dec 28 2006 Fr. Br. George <george@altlinux.ru> 2.4.4-alt6
- Biarch fix: package /usr/lib/python*

* Tue Dec 26 2006 Fr. Br. George <george@altlinux.ru> 2.4.4-alt5
- Fix TextTools (now mx.TextTools) module import in Tools/scripts

* Sun Dec 24 2006 Fr. Br. George <george@altlinux.ru> 2.4.4-alt4
- Fix #4699: (Tools/scripts/* added in new package)

* Tue Oct 24 2006   Fr. Br. George <george@altlinux.ru> 2.4.4-alt2
- x64 build works again
- Include minor FC patches

* Sat Oct 21 2006  Fr. Br. George <george@altlinux.ru> 2.4.4-alt1
- Version up, realpath() bug is fixed in this version

* Sat Oct 21 2006 Fr. Br. George <george@altlinux.ru> 2.4.3-alt3
- GEAR adapted

* Fri Apr 21 2006 Ivan Fedorov <ns@altlinux.ru> 2.4.3-alt2
- fixed provides (added pwd to base)
- fixed buildreq (libdb4.3-devel -> libdb4-devel)
- removed obsoleted patches

* Sat Apr 08 2006 Ivan Fedorov <ns@altlinux.ru> 2.4.3-alt1
- New version

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.2-alt1.1
- Rebuilt with libreadline.so.5.

* Mon Oct 03 2005 Andrey Orlov <cray@altlinux.ru> 2.4.2-alt1
- New version

* Mon Jul 11 2005 Andrey Orlov <cray@altlinux.ru> 2.4.1-alt5
- Some patches from Anton D. Kachalov included

* Thu Apr 07 2005 Anton D. Kachalov <mouse@altlinux.org> 2.4.1-alt4
- x86_64 support

* Fri Apr 01 2005 Andrey Orlov <cray@altlinux.ru> 2.4.1-alt3
- Some duplicated files excluded
- python2.3.so moved to python-dev package

* Fri Apr 01 2005 Andrey Orlov <cray@altlinux.ru> 2.4.1-alt1
- New Version

* Wed Mar 16 2005 Andrey Orlov <cray@altlinux.ru> 2.4.0-alt9
- IDLE item added into menu
- Broken symlink fixed

* Mon Mar 07 2005 Andrey Orlov <cray@altlinux.ru> 2.4.0-alt5
- Fix version
- Use izvrat_ver

* Mon Mar 07 2005 Andrey Orlov <cray@altlinux.ru> 2.4-alt3
- Info package patched

* Thu Mar 03 2005 Andrey Orlov <cray@altlinux.ru> 2.4-alt1.1
- Documentation in "INFO" re-added
- PQR re-added
- Security patch on SimpleXMLRPC applied
- Compatibility with libdb4.3 fixed
- Providing python2.4(os.path) declared
- New Version

* Wed Nov 10 2004 Andrey Orlov <cray@altlinux.ru> 2.4b2-alt1
- New Version

* Sun Oct 31 2004 Andrey Orlov <cray@altlinux.ru> 2.4b1-alt2
- rpm-build-python >= 0.18 added to build requires;
- New Version;

* Tue Oct 26 2004 Andrey Orlov <cray@altlinux.ru> 2.3.4-alt1
- Static library was put into separated package
- Alternatives config files fixed
- Emacs python mode file fixed
- New version

* Fri Jul 02 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt12
- Requires of tk added to tkinter;

* Sun Jun 06 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt11
- Into dev subpackage added requirements to be used by rpm-build-python
- __future__ module moved into python-base

* Mon May 24 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt10
- triggerpostun added to restore symbol-link after unregegister alternatives;

* Tue May 18 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt9
- Automatic provides n requires detect in module "test" forbidden;

* Mon May 17 2004 Dmitry V. Levin <ldv@altlinux.org> 2.3.3-alt8.1
- Added missing subpackage descriptions.

* Mon May 17 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt8
- Some errors observed during strict/relaxed switching fixed;
- Subpackage slight renamed into relaxed;
- Conditional packaging operators excluded (don't need any more);
- Requirement of bundlebuilder is ignored now;

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt7.6.d
- Using libdb2 excluded

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt7.5.d
- Rebuild with new rpm/python macros

* Tue Apr 13 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt7.4.d
- Rebuild with new rpm/python macros

* Sun Mar 28 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt7.3.d
- Fix new python policy compatibility

* Mon Mar 01 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt7
- Fix some inner dependences;
- Split devel package on devel and test (because of differences in AutoReq
  politics);
- Ready to rebuild with rpm-build-python (AutoReq, AutoProv);

* Sat Feb 21 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt6.5
- Split package python on -base, -modules, -modules-*;
- Some documentation added into python-info package;
- Subpackages python-slight, python-strict created;

* Sat Feb 21 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt6
- Package rebuilded with libdb4.2

* Sun Jan 18 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt5
- Package splitted on python-tools-idle, python-tools-pynche and python-tools-modulator
- Package with i18n tools added (python-tools-i18n)
- Package with webchacker added (python-tools-webchecker)

* Sun Jan 11 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt4
- koi8-u encoding added (thanks to Maxim Tyurin);

* Mon Jan 05 2004 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt3
- Clause "Conflict py21" added

* Mon Dec 29 2003 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt2
- Add documentation in info

* Mon Dec 29 2003 Andrey Orlov <cray@altlinux.ru> 2.3.3-alt1
- New version

* Tue Dec 16 2003 Andrey Orlov <cray@altlinux.ru> 2.3.2-alt6
- Library libpython is built as shared now;

* Wed Dec 10 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.2-alt5
- Relocated emacs site-start.d file to %_sysconfdir/emacs/site-start.d/.

* Thu Nov 27 2003 Andrey Orlov <cray@altlinux.ru> 2.3.2-alt4
- Emacs python-mode files are renamed ( "$" <- "23$" ) to avoid conflict
- Emacs python-mode files are included into alternatives
- Fix some problems on replace idle with idlelib and so on
- Modulator and Pynche moved into python/tools
- Some unused pathes excluded

* Mon Nov 24 2003 Andrey Orlov <cray@altlinux.ru> 2.3.2-alt3
- Emacs python-mode file temporary abandoned

* Fri Nov 21 2003 Andrey Orlov <cray@altlinux.ru> 2.3.2-alt2
- Old patches customized and applied.

* Wed Nov 05 2003 Andrey Orlov <cray@altlinux.ru> 2.3.2-alt1
- Renamed to python23.
- new version  (first try...)

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 2.2.2-alt3.1
- new alternatives config format

* Fri Mar 14 2003 Stanislav Ievlev <inger@altlinux.ru> 2.2.2-alt3
- PreReq fixes

* Thu Mar 13 2003 Stanislav Ievlev <inger@altlinux.ru> 2.2.2-alt2
- moved to new alternatives scheme

* Wed Nov 06 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt1
- 2.2.2 (bugfix release).

* Thu Sep 26 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.2.1-alt4
- rebuilt with tcl 8.4

* Thu Jul 11 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.2.1-alt3
- rebuilt with new tcl layout

* Sun Jun 30 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.1-alt2
- Patched to link with libtinfo.

* Thu Apr 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.2.1-alt1
- 2.2.1 (bugfix release).

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.2-alt10
- Fixed build (do not require db1, db3, db4).

* Thu Mar 07 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt9
- fixed alternatives

* Tue Feb 19 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt8
- return pyexpat.so to package

* Tue Feb 12 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt7
- now we don't use pathfix.py 'cause we want to build python without python

* Wed Jan 30 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.2-alt6
- Added buildreq substitution rules.

* Tue Jan 29 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt5
- fixed compileall module.

* Tue Jan 29 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt4
- fixed alternatives for the pydoc.

* Tue Jan 29 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt3
- Renamed to python22.

* Mon Jan 28 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt2
- added Provides for PYTHON

* Mon Jan 28 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt1
- 2.2
- we must made some changes in package structure later

* Tue Sep 04 2001 Mikhail Zabaluev <mhz@altlinux.ru> 2.1.1-alt3
- Segregated python-docs into a separate package

* Mon Aug 06 2001 Stanislav Ievlev <inger@altlinux.ru> 2.1.1-alt2
- Added emacs to buildreqs

* Wed Aug 01 2001 Stanislav Ievlev <inger@altlinux.ru> 2.1.1-alt1
- 2.1.1
- Light spec cleanup.

* Wed Jun 27 2001 AEN <aen@logic.ru> 2.1-alt1
- new version

* Tue Jan 30 2001 Dmitry V. Levin <ldv@fandra.org> 2.0-ipl5mdk
- Explicit set strip methods.
- Added few patches from
  http://www.python.org/cgi-bin/moinmoin/{Critical,Misc}Patches/

* Mon Jan 15 2001 Dmitry V. Levin <ldv@fandra.org> 2.0-ipl4mdk
- Fix build with new expat-devel.

* Sat Dec 09 2000 Dmitry V. Levin <ldv@fandra.org> 2.0-ipl3mdk
- Specfile cleanup.
- Enabled bsddbmodule.
- Added %_libdir/%%namever/xml.
- Recompiled modules with the correct directory paths.
- Automatically added BuildRequires.

* Wed Nov 29 2000 AEN <aen@logic.ru> 2.0-ipl2mdk
- build for RE
- corrected BuildReq

* Fri Nov 17 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0-1mdk
- 2.0 (95 tests OK. 12 tests skipped: test_al test_cd test_cl test_dl test_gl test_imgfile test_largefile
test_linuxaudiodev test_nis test_sunaudiodev test_winreg test_winsound)
- added emacs mode
- html doc.

* Wed Sep 27 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5.2-12mdk
- removed dependency on tkinter for python to avoid loop.

* Mon Sep 11 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5.2-11mdk
- fixed some hardcoded paths (Geoffrey Lee).
- removed menu entry for interpreter.

* Thu Aug 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.5.2-10mdk
- fixed typo %%%%updates_menus -> %%update_menus

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5.2-9mdk
- automatically added BuildRequires

* Thu Aug  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.5.2-8mdk
- Merge rh patch.
- Macros.
- compile with new tcl.

* Tue May  9 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5.2-7mdk
- added locale module.

* Thu Mar 30 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5.2-6mdk
- menu

* Tue Mar  7 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5.2-5mdk
- idle 0.5.
- compiled with optimization.

* Fri Jan 14 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5.2-4mdk

- added a BuildRequires.

* Sat Dec 04 1999 Florent Villard <warly@mandrakesoft.com>
- add idle, pynche and modulator in the package

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with redhat changes.
- added modulator, and pynche to the python-tools package(r)
- using a files list in the %files section for python-tools(r)
- added conflicts/requires between subpackages so that you cannot
  have an older tkinter installed with a new python.(r)
- added more tools(r)
- rebuild to fix broken tkinter.(r)
- fixed bogus /usr/local/bin/python requirements.(r)
- added patch to import global symbols until we get libtool patched(r)

* Fri Aug 20 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- updated to 1.5.2
- updated patches
- use macro %%_arch instead of %%_target_cpu for file paths

* Tue Apr 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove the dbm support (doen't work with GLBC2.1)

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- add de locale
- fix handling of RPM_OPT_FLAGS

* Thu Feb 11 1999 Michael Johnson <johnsonm@redhat.com>
- added mpzmodule at user request (uses gmp)
- added bsddbmodule at user request (uses db 1.85 interface)

* Mon Feb 08 1999 Michael Johnson <johnsonm@redhat.com>
- add --with-threads at user request
- clean up spec file

* Fri Jan 08 1999 Michael K. Johnson <johnsonm@redhat.com>
- New libc changes ndbm.h to db1/ndbm.h and -ldb to -ldb1

* Thu Sep  3 1998 Jeff Johnson <jbj@redhat.com>
- recompile for RH 5.2.

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- python-docs used to require /usr/bin/sed. Changed to /bin/sed instead

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- fixed the spec file for version 1.5.1
- buildroot (!)

* Mon Apr 20 1998 Michael K. Johnson <johnsonm@redhat.com>
- updated to python 1.5.1
- created our own Python-Doc tar file from 1.5 to substitute for the
  not-yet-released Doc package.
- build _tkinter properly
- use readline again
- build crypt module again
- install rand replacement module
- added a few modules

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to python 1.5
- made /usr/lib/python1.5 file list automatically generated

* Tue Nov 04 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fixed dependencies for python and tkinter

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- pulled out tk-related stuff into tkinter package

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- bunches of scripts used /usr/local/bin/python instead of /usr/bin/python

* Tue Sep 30 1997 Erik Troan <ewt@redhat.com>
- updated for tcl/tk 8.0

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
