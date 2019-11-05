%define gcc_branch 4.8

# this package can be compiled as cross tool, by defining _cross_platform
# i.e. rpmbuild -ba --define '_cross_platform armh-alt-linux-gnueabi' gcc4.spec
# note though, resulting packages aren't usual cross tools and not supposed
# to be used nor even installed on build host.

%define if_gcc_arch() %if %(A='%{?_cross_platform:%_cross_platform}%{!?_cross_platform:%_target_platform}'; [ %1 = ${A%%%%-*} ] && echo 1 || echo 0)

Name: gcc%gcc_branch
Version: 4.8.2
Release: alt7

Summary: GNU Compiler Collection
# libgcc, libgfortran, libmudflap, libgomp, libstdc++ and crtstuff have
# GCC Runtime Exception.
License: GPLv3+, GPLv3+ with exceptions and GPLv2+ with exceptions
Group: Development/C
Url: http://gcc.gnu.org/
ExcludeArch: aarch64 ppc64le

%ifarch ppc
# On ppc32, we build a 64-bit compiler with default 32-bit mode.
%define _target_platform ppc64-alt-linux
%endif

%define priority 482
%define snapshot 20140120
%define srcver %version-%snapshot
%define srcfilename gcc-%srcver
%define srcdirname gcc-%srcver
%define os_release %distribution, build %version-%release
%define psuffix -%gcc_branch
%define _libexecdir /usr/libexec

%ifdef _cross_platform
%define _cross_lib %_prefix/lib
%define gcc_target_libdir %_cross_lib/gcc/%_cross_platform/%gcc_branch
%define gcc_target_libexecdir %_libexecdir/gcc/%_cross_platform/%gcc_branch
%define gcc_target_platform %_cross_platform
%else
%define gcc_target_libdir %_libdir/gcc/%_target_platform/%gcc_branch
%define gcc_target_libexecdir %_libexecdir/gcc/%_target_platform/%gcc_branch
%define gcc_target_platform %_target_platform
%endif

%define gcc_gdb_auto_load %_datadir/gdb/auto-load%_libdir/
%define gcc_doc_dir %_docdir/gcc%psuffix
# due to -z relro by default
%define binutils_deps binutils >= 1:2.24.0

%ifarch x86_64
%define compat_platform i586-alt-linux
%define gcc_target_lib32dir /usr/lib/gcc/%compat_platform/%gcc_branch
%define gxx32idir %_includedir/c++/%gcc_branch/%compat_platform
%define gxx64idir %_includedir/c++/%gcc_branch/%_target_platform
%endif

%define ada_binaries gnatbind gnatchop gnatclean gnatfind gnatkr gnatlink gnatls gnatmake gnatname gnatprep gnatxref
%define java_binaries gappletviewer gcj-dbtool gcjh gij gjar gjarsigner gjavah gkeytool gorbd grmic grmid grmiregistry gserialver gtnameserv jcf-dump jv-convert

%define libquadmath_arches	%ix86 x86_64
%define libasan_arches		%ix86 x86_64 %arm
%define libtsan_arches		x86_64
%define libatomic_arches	%ix86 x86_64 %arm aarch64
%define libitm_arches		%ix86 x86_64 %arm aarch64

%set_compress_method xz
%ifarch %arm
# due to libmudflap, libmudflapth and libitm
%set_verify_elf_method unresolved=relaxed textrel=relaxed
%else
# due to libmudflap and libmudflapth
%set_verify_elf_method unresolved=relaxed
%endif
# due to libtool.m4-gcj.patch
%set_libtool_version 2.4
# support for Cygnus-style trees has been removed in newer automake versions
%set_automake_version 1.11

# Build parameters.
%ifdef _cross_platform

%def_without java

%def_enable compat
%def_disable multilib
%def_with cxx
%def_without fortran
%def_without objc
%def_disable objc_gc
%def_without ada
%def_without go
%define REQ >=

%else # _cross_platform

%def_enable compat
%def_enable multilib
%def_with cxx
%def_with fortran
%ifnarch ppc ppc64
%def_with objc
%else
%def_without objc
%endif
%def_disable objc_gc
# If you don't have already a usable gcc-java and libgcj for your arch,
# do on some arch which has it rpmbuild -bc --with java_tar gcc4.spec
# which creates libjava-classes-%version-%release.tar
# With this then on the new arch do rpmbuild -ba -v --with java_bootstrap gcc4.spec
%def_without java_tar
%def_without java_bootstrap
%if_disabled compat
%define REQ =
%ifarch %ix86 x86_64
%def_with ada
%def_with go
%else
%def_without ada
%def_without go
%endif
%else
%define REQ >=
%def_without ada
%endif

%endif # _cross_platform

%def_without pdf
%def_disable doxygen
%def_disable check

%define buildtarget obj-%gcc_target_platform

Source: %srcfilename.tar
%{?_with_java_bootstrap:Source1: libjava-classes-%version-%release.tar}

# Fedora patches.
Patch100: gcc48-hack.patch
Patch101: gcc48-java-nomulti.patch
Patch102: gcc48-ppc32-retaddr.patch
Patch104: gcc48-i386-libgomp.patch
Patch106: gcc48-libgomp-omp_h-multilib.patch
Patch107: gcc48-libtool-no-rpath.patch
Patch110: gcc48-pr38757.patch
Patch113: gcc48-pr56564.patch
Patch114: gcc48-pr56493.patch
Patch115: gcc48-color-auto.patch
Patch116: gcc48-pr28865.patch
Patch118: gcc48-pr60137.patch
Patch119: gcc48-pr60010.patch
Patch120: gcc48-pr60046.patch

# Debian patches.
Patch200: gcc-d-lang.diff
Patch201: gcc-textdomain.diff
Patch202: libstdc++-doclink.diff
Patch203: libstdc++-man-3cxx.diff
Patch204: libstdc++-python3.diff
Patch205: libjava-stacktrace.diff
Patch206: libjava-sjlj.diff
Patch207: libjava-disable-plugin.diff
Patch208: libjava-fixed-symlinks.diff
Patch209: boehm-gc-getnprocs.diff
Patch210: arm-sanitizer.diff
Patch211: fix-ffi_call_VFP-with-no-VFP-argument.diff
Patch212: libstdc++-arm-wno-abi.diff
Patch213: gccgo-version.diff
Patch214: alt-gcc-base-version.diff
Patch215: pr57211.diff
Patch216: libgcc-no-limits-h.diff
Patch217: testsuite-hardening-format.diff
Patch218: testsuite-hardening-printf-types.diff
Patch219: testsuite-hardening-updates.diff
Patch220: pr47818.diff
Patch221: ada-gcc-name.diff
Patch222: ada-symbolic-tracebacks.diff
Patch223: libjava-armel-unwind.diff

# ALT patches.
Patch700: alt-_GCC_AUTOCONF_VERSION.patch
Patch701: alt-install.patch
Patch702: alt-nowrap.patch
Patch703: alt-libatomic-makefile.patch
Patch704: alt-libgfortran-makefile.patch
Patch705: alt-libjava-disable-static.patch
Patch706: alt-libjava-makefile.patch
Patch707: alt-libjava-ltdl.patch
Patch708: alt-ada-link.patch
Patch709: alt-as-needed.patch
Patch710: deb-testsuite-as-needed.patch
Patch711: alt-defaults-format-security.patch
Patch712: alt-testsuite-format.patch
Patch713: alt-defaults-_FORTIFY_SOURCE.patch
Patch714: alt-testsuite-_FORTIFY_SOURCE.patch
Patch715: alt-spp-buffer-size.patch
Patch716: alt-defaults-ssp.patch
Patch717: alt-escalate-always-overflow.patch
Patch718: alt-libgo-weak.patch
Patch729: alt-fix-build-with-glibc2.26-ucontext.patch
Patch731: gcc-asan-fix-missing-include-signal-h.patch
Patch732: alt-fix-texi2pod-perl.patch
Patch733: alt-Fix-option-handling-when--std=gnu++14-is-not-used-PR-69865.patch
Patch734: alt-fix-build-with-texinfo.patch
Patch735: alt-fix-build-with-glibc2.26-sigaltstack-__res_state.patch
Patch800: alt-libtool.m4-gcj.patch

Obsoletes: egcs gcc3.0 gcc3.1
Conflicts: glibc-devel < 2.2.6
Requires(pre): gcc-common >= 1.4.7
Requires: cpp%gcc_branch = %EVR
Requires: %binutils_deps, glibc-devel
%ifndef _cross_platform
Requires: libgcc1 %REQ %EVR
%ifarch %libatomic_arches
Requires: libatomic1 %REQ %EVR
%endif
%ifarch %libasan_arches
Requires: libasan0 = %EVR
%endif
%ifarch %libitm_arches
Requires: libitm1 %REQ %EVR
%endif
%ifarch %libtsan_arches
Requires: libtsan0 %REQ %EVR
%endif
%endif
BuildPreReq: rpm-build >= 4.0.4-alt39, %binutils_deps
%set_gcc_version 4.9
BuildPreReq: gcc%_gcc_version-c++ coreutils flex makeinfo
BuildPreReq: libelf-devel libmpc-devel libmpfr-devel
# due to manpages
BuildPreReq: perl-Pod-Parser
BuildPreReq: zlib-devel
%{?_with_ada:BuildPreReq: gcc-gnat}
%{?_with_java:BuildPreReq: %{?_without_java_bootstrap: jdkgcj} /usr/share/java/ecj.jar fastjar imake libXext-devel libXt-devel libXtst-devel libalsa-devel libart_lgpl-devel libgtk+2-devel libltdl-devel sharutils xorg-cf-files xorg-inputproto-devel unzip zip}
%{?_with_objc:%{?_enable_objc_gc:BuildPreReq: libgc-devel}}
%{?_enable_doxygen:BuildPreReq: doxygen graphviz tetex-latex}
%{?_with_pdf:BuildPreReq: tetex-dvips}
%{?!_without_check:%{?!_disable_check:BuildRequires: dejagnu, glibc-devel-static, /proc, /dev/pts}}
%{?_cross_platform:BuildPreReq: %_cross_platform-binutils}

####################################################################
# GCC Compiler

%description
This package contains the GNU Compiler Collection version %version.
You'll need this package in order to compile C code.
It is also required for all other GCC compilers.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
gcc%psuffix
in order to explicitly use the GNU C compiler version %version.

####################################################################
# GCC plugin

%package plugin-devel
Summary: GCC Plugin header files
Group: Development/Other
Provides: libgcc%gcc_branch-plugin-devel = %version
Requires: %name = %EVR

%description plugin-devel
This package contains header files required to build GCC plugins.

####################################################################
# GCC library

%package -n libgcc1
Summary: GCC shared support library
Group: System/Libraries
Provides: libgcc = %version
Provides: libgcc3.2 = %version
Provides: libgcc3.3 = %version
Provides: libgcc3.4 = %version
Provides: libgcc4.1 = %version
Provides: libgcc4.3 = %version
Provides: libgcc4.4 = %version
Provides: libgcc4.5 = %version
Obsoletes: libgcc < %version
Obsoletes: libgcc3.2 < %version
Obsoletes: libgcc3.3 < %version
Obsoletes: libgcc3.4 < %version
Obsoletes: libgcc4.1 < %version
Obsoletes: libgcc4.3 < %version
Obsoletes: libgcc4.4 < %version
Obsoletes: libgcc4.5 < %version

%description -n libgcc1
This package contains GCC shared support library which is needed
e.g. for exception handling support.

####################################################################
# Atomic library

%package -n libatomic1
Summary: The GNU Atomic library
Group: System/Libraries
Requires: libgcc1 %REQ %EVR

%description -n libatomic1
This package contains the GNU Atomic library which is a GCC support
runtime library for atomic operations not supported by hardware.

%package -n libatomic%gcc_branch-devel-static
Summary: The GNU Atomic static library
Group: Development/C
Requires: libatomic1 %REQ %EVR

%description -n libatomic%gcc_branch-devel-static
This package contains GNU Atomic static library.

####################################################################
# Address Sanitizer library

%package -n libasan0
Summary: The Address Sanitizer runtime library
Group: System/Libraries
Requires: libgcc1 %REQ %EVR

%description -n libasan0
This package contains the Address Sanitizer runtime library
which is used for -fsanitize=address instrumented programs.

%package -n libasan%gcc_branch-devel-static
Summary: The Address Sanitizer static library
Group: Development/C
Requires: libasan0 %REQ %EVR

%description -n libasan%gcc_branch-devel-static
This package contains Address Sanitizer static library.

####################################################################
# Thread Sanitizer library

%package -n libtsan0
Summary: The Thread Sanitizer runtime library
Group: System/Libraries
Requires: libgcc1 %REQ %EVR

%description -n libtsan0
This package contains the Thread Sanitizer runtime library
which is used for -fsanitize=thread instrumented programs.

%package -n libtsan%gcc_branch-devel-static
Summary: The Thread Sanitizer static library
Group: Development/C
Requires: libtsan0 %REQ %EVR

%description -n libtsan%gcc_branch-devel-static
This package contains Thread Sanitizer static library.

####################################################################
# ITM library

%package -n libitm1
Summary: The GNU Transactional Memory library
Group: System/Libraries
Requires: libgcc1 %REQ %EVR

%description -n libitm1
This package contains the GNU Transactional Memory library
which is a GCC transactional memory support runtime library.

%package -n libitm%gcc_branch-devel-static
Summary: The GNU Transactional Memory static library
Group: Development/C
Requires: libitm1 %REQ %EVR

%description -n libitm%gcc_branch-devel-static
This package contains GNU Transactional Memory static libraries.

####################################################################
# OpenMP library

%package -n libgomp1
Summary: GCC OpenMP shared support library
Group: System/Libraries
Provides: libgomp = %version
Provides: libgomp4.1 = %version
Provides: libgomp4.3 = %version
Provides: libgomp4.4 = %version
Provides: libgomp4.5 = %version
Obsoletes: libgomp < %version
Obsoletes: libgomp4.1 < %version
Obsoletes: libgomp4.3 < %version
Obsoletes: libgomp4.4 < %version
Obsoletes: libgomp4.5 < %version

%description -n libgomp1
This package contains GCC OpenMP shared support library.

%package -n libgomp%gcc_branch-devel
Summary: GCC OpenMP support files
Group: Development/Other
Requires: libgomp1 %REQ %EVR
Requires: glibc-devel

%description -n libgomp%gcc_branch-devel
This package contains GCC OpenMP headers and library.

%package -n libgomp%gcc_branch-devel-static
Summary: GCC OpenMP static support library
Group: Development/Other
Requires: libgomp%gcc_branch-devel = %EVR

%description -n libgomp%gcc_branch-devel-static
This package contains GCC OpenMP static library.

####################################################################
# mudflap library

%package -n libmudflap0
Summary: GCC mudflap shared support libraries
Group: System/Libraries
Provides: libmudflap = %version
Provides: libmudflap4.1 = %version
Provides: libmudflap4.3 = %version
Provides: libmudflap4.4 = %version
Provides: libmudflap4.5 = %version
Obsoletes: libmudflap < %version
Obsoletes: libmudflap4.1 < %version
Obsoletes: libmudflap4.3 < %version
Obsoletes: libmudflap4.4 < %version
Obsoletes: libmudflap4.5 < %version

%description -n libmudflap0
This package contains GCC shared support libraries which are needed for
mudflap support.

%package -n libmudflap%gcc_branch-devel
Summary: GCC mudflap support files
Group: Development/Other
Provides: libmudflap-devel = %version
Requires: libmudflap0 %REQ %EVR
Requires: glibc-devel

%description -n libmudflap%gcc_branch-devel
This package contains headers and libraries for building
mudflap-instrumented programs.
To instrument a non-threaded program, add -fmudflap option to GCC and
when linking add -lmudflap, for threaded programs also add -fmudflapth
and -lmudflapth.

%package -n libmudflap%gcc_branch-devel-static
Summary: GCC mudflap static support libraries
Group: Development/Other
Provides: libmudflap-devel-static = %version
Requires: libmudflap%gcc_branch-devel = %EVR

%description -n libmudflap%gcc_branch-devel-static
This package contains static libraries for building statically linked
mudflap-instrumented programs.

####################################################################
# quadmath library
%package -n libquadmath0
Summary: GCC __float128 shared support library
Group: System/Libraries

%description -n libquadmath0
This package contains GCC shared support library which is needed
for __float128 math support and for Fortran REAL*16 support.

%package -n libquadmath%gcc_branch-devel
Summary: GCC __float128 support files
Group: Development/Other
Requires: libquadmath0 %REQ %EVR

%description -n libquadmath%gcc_branch-devel
This package contains headers for building Fortran programs using
REAL*16 and programs using __float128 math.

%package -n libquadmath%gcc_branch-devel-static
Summary: GCC __float128 static support library
Group: Development/Other
Requires: libquadmath%gcc_branch-devel = %EVR

%description -n libquadmath%gcc_branch-devel-static
This package contains static libraries for building Fortran programs
using REAL*16 and programs using __float128 math.

####################################################################
# Preprocessor

%package -n cpp%gcc_branch
Summary: The GNU C-Compatible Compiler Preprocessor
Group: Development/C
Obsoletes: gcc-cpp egcs-cpp cpp3.0 cpp3.1
Requires(pre): gcc-common >= 1.4.7

%description -n cpp%gcc_branch
Cpp is the GNU C-Compatible Compiler Preprocessor.
The C preprocessor is a 'macro processor' which is used automatically
by the C compiler to transform your program before actual
compilation. It is called a macro processor because it allows
you to define 'macros,' which are abbreviations for longer
constructs.

The C preprocessor provides four separate facilities that you can use as
you see fit:

* Inclusion of header files. These are files of declarations that can be
  substituted into your program.
* Macro expansion. You can define 'macros,' which are abbreviations for
  arbitrary fragments of C code, and then the C preprocessor will replace
  the macros with their definitions throughout the program.
* Conditional compilation. Using special preprocessing directives,
  you can include or exclude parts of the program according to various
  conditions.
* Line control. If you use a program to combine or rearrange source files
  into an intermediate file which is then compiled, you can use line
  control to inform the compiler about where each source line originated.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
cpp%psuffix
in order to explicitly use the GNU C Preprocessor version %version.

####################################################################
# C++ Libraries

%package -n libstdc++6
Summary: GNU Standard C++ library
Group: System/Libraries
AutoReq: yes, nopython
Provides: libstdc++ = %version
Provides: libstdc++3.4 = %version
Provides: libstdc++4.1 = %version
Provides: libstdc++4.3 = %version
Provides: libstdc++4.4 = %version
Provides: libstdc++4.5 = %version
Obsoletes: libstdc++ < %version
Obsoletes: libstdc++3.4 < %version
Obsoletes: libstdc++4.1 < %version
Obsoletes: libstdc++4.3 < %version
Obsoletes: libstdc++4.4 < %version
Obsoletes: libstdc++4.5 < %version
Requires: libgcc1 %REQ %EVR
# due to TLS (#9732)
Requires(pre): glibc-core >= 6:2.3.6-alt7

%description -n libstdc++6
This package contains a rewritten standard compliant GCC Standard C++
Library.

%package -n libstdc++%gcc_branch-devel
Summary: Header files and libraries for C++ development
Group: Development/C++
Obsoletes: libstdc++3.0-devel libstdc++3.1-devel
Requires(pre): gcc-c++-common >= 1.4.7
Requires: libstdc++6 %REQ %EVR
Requires: glibc-devel

%description -n libstdc++%gcc_branch-devel
This is the GNU implementation of the standard C++ libraries.
This package includes the header files and libraries needed for C++
development.  This includes rewritten implementation of STL.

%package -n libstdc++%gcc_branch-devel-static
Summary: Static libraries for C++ development
Group: Development/C++
Obsoletes: libstdc++3.0-devel-static libstdc++3.1-devel-static
Requires(pre): gcc-c++-common >= 1.4.7
Requires: libstdc++%gcc_branch-devel = %EVR

%description -n libstdc++%gcc_branch-devel-static
This is the GNU implementation of the standard C++ libraries.
This package includes static library needed for C++ development.

####################################################################
# C++ Compiler

%package c++
Summary: C++ support for gcc
Group: Development/C++
Obsoletes: egcs-c++ gcc3.0-c++ gcc3.1-c++
Requires(pre): gcc-c++-common >= 1.4.7
Requires: %name = %EVR
Requires: libstdc++%gcc_branch-devel = %EVR

%description c++
This package adds C++ support to the GNU Compiler Collection.
It includes support for most of the current C++ specification,
including templates and exception handling.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
g++%psuffix
in order to explicitly use the GNU C++ compiler version %version.

####################################################################
# Objective-C Libraries

%package -n libobjc4
Summary: Objective-C runtime library
Group: System/Libraries
Requires: libgcc1 %REQ %EVR

%description -n libobjc4
This package contains Objective-C shared library which is needed to run
Objective-C dynamically linked programs.

%package -n libobjc%gcc_branch-devel
Summary: Header files and library for Objective-C development
Group: Development/Other
Requires(pre): gcc-common >= 1.4.7
Requires: libobjc4 %REQ %EVR
Requires: glibc-devel

%description -n libobjc%gcc_branch-devel
This is the GNU implementation of the standard Objective-C libraries.
This package includes the header files and library needed for
Objective-C development.

%package -n libobjc%gcc_branch-devel-static
Summary: Static libraries for Objective-C development
Group: Development/Other
Requires(pre): gcc-common >= 1.4.7
Requires: libobjc%gcc_branch-devel = %EVR

%description -n libobjc%gcc_branch-devel-static
This is the GNU implementation of the standard Objective-C libraries.
This package includes the static library needed for Objective-C
development.

####################################################################
# Objective-C Compiler

%package objc
Summary: Objective-C support for GCC
Group: Development/Other
Obsoletes: gcc3.0-objc gcc3.1-objc
Requires(pre): gcc-common >= 1.4.7
Requires: %name = %EVR
Requires: libobjc%gcc_branch-devel = %EVR

%description objc
This package provides Objective-C support for the GCC.
Mainly used on systems running NeXTSTEP, Objective-C is an
object-oriented derivative of the C language.

%package objc++
Summary: Objective-C++ support for GCC
Group: Development/Other
Requires(pre): gcc-common >= 1.4.7
Requires: %name-objc = %EVR, %name-c++ = %EVR

%description objc++
This package provides Objective-C++ support for the GCC.

####################################################################
# GNU Fortran Library

%package -n libgfortran3
Summary: GNU Fortran runtime library
Group: System/Libraries
Requires: libgcc1 %REQ %EVR
%ifarch %libquadmath_arches
Requires: libquadmath0 %REQ %EVR
%endif
Provides: libgfortran = %version
Provides: libgfortran4.3 = %version
Provides: libgfortran4.4 = %version
Provides: libgfortran4.5 = %version
Obsoletes: libgfortran4.3 < %version
Obsoletes: libgfortran4.4 < %version
Obsoletes: libgfortran4.5 < %version

%description -n libgfortran3
This package contains GNU Fortran shared library which is needed to run
GNU Fortran dynamically linked programs.

%package -n libgfortran%gcc_branch-devel
Summary: Header files and library for GNU Fortran development
Group: Development/Other
Requires(pre): gcc-fortran-common >= 1.4.7
Requires: libgfortran3 %REQ %EVR
%ifarch %libquadmath_arches
Requires: libquadmath%gcc_branch-devel = %EVR
%endif
Requires: glibc-devel

%description -n libgfortran%gcc_branch-devel
This is the GNU implementation of the standard GNU Fortran libraries.
This package includes the header files and library needed for GNU
Fortran development.

%package -n libgfortran%gcc_branch-devel-static
Summary: Static libraries for GNU Fortran development
Group: Development/Other
Requires(pre): gcc-fortran-common >= 1.4.7
Requires: libgfortran%gcc_branch-devel = %EVR

%description -n libgfortran%gcc_branch-devel-static
This is the GNU implementation of the standard GNU Fortran libraries.
This package includes the static library needed for GNU Fortran
development.

####################################################################
# GNU Fortran Compiler

%package fortran
Summary: GNU Fortran support for gcc
Group: Development/Other
Obsoletes: gcc3.0-g77 gcc3.1-g77
Requires(pre): gcc-fortran-common >= 1.4.7
Requires: %name = %EVR
Requires: libgfortran%gcc_branch-devel = %EVR

%description fortran
This package provides support for compiling GNU Fortran
programs with the GNU Compiler Collection.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
fortran%psuffix
in order to explicitly use the GNU Fortran compiler version %version.

####################################################################
# Java Libraries

%package -n libgcj_bc1
Summary: GNU libgcj_bc shared library
Group: System/Libraries
Provides: libgcj_bc = %version
Provides: libgcj_bc4.1 = %version
Provides: libgcj_bc4.3 = %version
Provides: libgcj_bc4.4 = %version
Provides: libgcj_bc4.5 = %version
Obsoletes: libgcj_bc4.1 < %version
Obsoletes: libgcj_bc4.3 < %version
Obsoletes: libgcj_bc4.4 < %version
Obsoletes: libgcj_bc4.5 < %version
Conflicts: libgcj4.3 < 0:4.3.2-alt4
Conflicts: libgcj4.1 < 0:4.1.2-alt5

%description -n libgcj_bc1
This package contains GNU libgcj_bc shared library.

%package -n libgcj%gcc_branch
Summary: GNU Java runtime libraries
Group: System/Libraries
Provides: libgcj = %version
Obsoletes: libgcj3.0 libgcj3.1 libgcj3.2
Requires: zip >= 2.1
Requires: libgcc1 %REQ %EVR
Requires: libgcj_bc1 %REQ %EVR
Requires: libgcj%gcc_branch-jar = %EVR
Conflicts: libgcj4.1 < 0:4.1.2-alt5

%description -n libgcj%gcc_branch
The Java(tm) runtime library. You will need this package to run your Java
programs compiled using the Java compiler from GNU Compiler Collection (gcj).

%package -n libgcj%gcc_branch-plugins
Summary: GNU Java plugins
Group: System/Libraries
Provides: libgcj-plugins = %version
Obsoletes: libgcj3.0-plugins libgcj3.1-plugins libgcj3.2-plugins
Requires: libgcj%gcc_branch = %EVR

%description -n libgcj%gcc_branch-plugins
The GNU Java plugins.

%package -n libgcj%gcc_branch-devel
Summary: Header files and libraries for Java development
Group: Development/Java
Provides: libgcj-devel = %version
Obsoletes: libgcj3.0-devel libgcj3.1-devel
Conflicts: libgcj3.4-devel < 0:3.4.5-alt5
Requires: libgcj%gcc_branch = %EVR, zlib-devel

%description -n libgcj%gcc_branch-devel
The Java(tm) development libraries and include files. You will need this
package to compile your Java programs using the GCC Java compiler (gcj).

%package -n libgcj%gcc_branch-devel-static
Summary: Static libraries for Java development
Group: Development/Java
Provides: libgcj-devel-static = %version
Obsoletes: libgcj3.0-devel-static libgcj3.1-devel-static
Requires: libgcj%gcc_branch-devel = %EVR

%description -n libgcj%gcc_branch-devel-static
The Java(tm) static libraries. You may need this
package to compile your Java programs using the GCC Java compiler (gcj).

%package -n libgcj%gcc_branch-jar
Summary: libgcj jar files
Group: Development/Java
BuildArch: noarch
Requires: libgcj-common >= 1.4.16
Provides: libgcj-jar = %version

%description -n libgcj%gcc_branch-jar
This package contains libgcj *.jar files.

%package -n libgcj%gcc_branch-src
Summary: Java library sources from GCC Java compiler
Group: Development/Java
BuildArch: noarch
Requires: libgcj%gcc_branch = %EVR
Provides: libgcj-src = %version

%description -n libgcj%gcc_branch-src
The Java(tm) runtime library sources for use in Eclipse.

####################################################################
# Java Compiler

%if_with java
%package java
Summary: Java support for gcc
Group: Development/Java
Provides: gcc-java = %version, %_bindir/gcj
Obsoletes: gcc3.0-java gcc3.1-java gcj3.1-tools
Requires(pre): %alternatives_deps, gcc-java-common >= 1.4.13
Requires: %name = %EVR, libgcj%gcc_branch-devel = %EVR
# due to GC requirements:
# GC Warning: Couldn't read /proc/stat
# GC Warning: GC_get_nprocs() returned -1
# Couldn't read /proc/self/stat
Requires: /proc
Requires: /usr/share/java/ecj.jar

%description java
This package adds support for compiling Java(tm) programs and
bytecode into native code.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
gcj%psuffix
in order to explicitly use the GNU Java compiler version %version.
%endif

####################################################################
# Ada 95 Libraries

%package -n libgnat%gcc_branch
Summary: Ada 95 runtime libraries
Group: System/Libraries
Requires: libgcc1 %REQ %EVR

%description -n libgnat%gcc_branch
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries.  It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the
Posix 1003.5 Binding (Florist).

%package -n libgnat%gcc_branch-devel
Summary: Header files and libraries for Ada 95 development
Group: Development/Other
Requires(pre): gcc-common >= 1.4.7
Requires: libgnat%gcc_branch = %EVR

%description -n libgnat%gcc_branch-devel
This is the GNU implementation of the standard Ada 95 libraries.
This package includes the include files and libraries needed for
Ada 95 development.

%package -n libgnat%gcc_branch-devel-static
Summary: Static libraries for Ada 95 development
Group: Development/Other
Requires(pre): gcc-common >= 1.4.7
Requires: libgnat%gcc_branch-devel = %EVR

%description -n libgnat%gcc_branch-devel-static
This is the GNU implementation of the standard Ada 95 libraries.  This
package includes the static libraries needed for Ada 95 development.

####################################################################
# Ada 95 Compiler

%package gnat
Summary: Ada 95 support for gcc
Group: Development/Other
Obsoletes: gcc4.7-gnat gcc4.6-gnat gcc4.5-gnat gcc4.4-gnat gcc4.3-gnat gcc4.2-gnat gcc4.1-gnat
Requires(pre): gcc-gnat-common
Requires: %name = %EVR
Requires: libgnat%gcc_branch-devel = %EVR

%description gnat
This package provides support for compiling Ada 95
programs with the GNU Compiler Collection.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
gnat%psuffix
in order to explicitly use the GNU Ada compiler version %version.

####################################################################
# Go Libraries

%package -n libgo4
Summary: Go runtime libraries
Group: System/Libraries
Requires: libgcc1 %REQ %EVR

%description -n libgo4
This package contains the shared libraries required to run programs
compiled with the GNU Go compiler if they are compiled to use
shared libraries.

%package -n libgo%gcc_branch-devel
Summary: Header files and libraries for Go development
Group: Development/Other
Requires(pre): gcc-common >= 1.4.7
Requires: libgo4 %REQ %EVR

%description -n libgo%gcc_branch-devel
This package includes the include files and libraries needed for
Go development.

%package -n libgo%gcc_branch-devel-static
Summary: Static libraries for Go development
Group: Development/Other
Requires(pre): gcc-common >= 1.4.7
Requires: libgo%gcc_branch-devel = %EVR

%description -n libgo%gcc_branch-devel-static
This package includes the static libraries needed for Go development.

####################################################################
# Go Compiler
%package go
Summary: Go support for GCC
Group: Development/Other
Requires(pre): gcc-go-common >= 1.4.15
Requires: %name = %EVR
Requires: libgo%gcc_branch-devel = %EVR

%description go
This package provides support for compiling Go
programs with the GNU Compiler Collection.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
go%psuffix
in order to explicitly use the GNU Go compiler version %version.
####################################################################
# GCC localization

%package locales
Summary: The GNU Compiler Collection native language support files
Group: Development/C
#This version of gcc is not built on some architectures (read aarch64),
#but locales subpackage has dependency on (non-noarch) gcc package.
#BuildArch: noarch
Requires: %name = %EVR

%description locales
This packages contains files required for native language support for
the GNU Compiler Collection.

####################################################################
# GCC documentation

%package doc
Summary: GCC documentation
Group: Development/Other
BuildArch: noarch
Conflicts: gcc3.0-doc
Conflicts: gcc3.1-doc
Conflicts: gcc3.2-doc
Conflicts: gcc3.3-doc
Conflicts: gcc3.4-doc
Conflicts: gcc4.1-doc
Conflicts: gcc4.3-doc
Conflicts: gcc4.4-doc
Conflicts: gcc4.5-doc
Conflicts: gcc4.6-doc
Conflicts: gcc4.7-doc
Obsoletes: gcc3.0-doc gcc3.1-doc gcc3.2-doc gcc3.3-doc gcc3.4-doc gcc4.1-doc gcc4.3-doc gcc4.4-doc gcc4.5-doc gcc4.6-doc gcc4.7-doc

%description doc
This package contains documentation for the GNU Compiler Collection
version %version.

%prep
%setup -n %srcdirname

# Fedora patches.
%patch100 -p0
%patch101 -p0
%patch102 -p0
%patch104 -p0
%patch106 -p0
%patch107 -p0
%patch110 -p0
%patch113 -p0
%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch118 -p0
%patch119 -p0
%patch120 -p0

# Debian patches.
%patch200 -p2
%patch201 -p2
%patch202 -p2
%patch203 -p2
%patch204 -p2
%patch205 -p2
%patch206 -p2
%patch207 -p2
%patch208 -p2
%patch209 -p2
%patch210 -p2
%patch211 -p2
%patch212 -p2
%patch213 -p2
%patch214 -p2
%patch215 -p2
%patch216 -p2
%patch217 -p2
%patch218 -p2
%patch219 -p2
%patch220 -p2
%patch221 -p2
%patch222 -p2
%ifarch %arm
%patch223 -p2
%endif

# ALT patches.
%patch700 -p1
%patch701 -p1
%patch702 -p1
%patch703 -p1
%patch704 -p1
%patch705 -p1
%patch706 -p1
%patch707 -p1
%patch708 -p1
%patch709 -p1
%patch710 -p1
%patch711 -p1
%patch712 -p1
%patch713 -p1
%patch714 -p1
%patch715 -p1
%patch716 -p1
%patch717 -p1
%patch718 -p1
%patch729 -p1
%patch731 -p1
%patch732 -p1
%patch733 -p1
%patch734 -p1
%patch735 -p1

# Set proper version info.
echo %gcc_branch > gcc/BASE-VER
echo %version > gcc/FULL-VER
echo '%distribution %version-%release' > gcc/DEV-PHASE

# due to autoconf >= 2.69
> libgo/config/go.m4

# This testcase does not compile.
rm libjava/testsuite/libjava.lang/PR35020*

# This test causes fork failures, because it spawns way too many threads
rm -f gcc/testsuite/go.test/test/chan/goroutines.go

%if_with java_bootstrap
tar xf %SOURCE1
%endif

# Remove -I- gcc option.
find -type f -name Makefile\* -print0 |
	xargs -r0 fgrep -Zle '-I- ' -- |
	xargs -r0 sed -i 's/-I- //g' --

# Disable unwanted multilib builds.
%ifarch x86_64 mips mipsel mips64 mips64el riscv64 ppc64le
sed -i 's/\$(CC_FOR_TARGET) --print-multi-lib/echo '"'.;'/" Makefile.*
sed -i 's/\${CC-gcc} --print-multi-lib/echo '"'.;'/" config-ml.in
sed -i 's/\[ -z "\$(MULTIDIRS)" \]/true/' config-ml.in
%endif

find -type f -name \*.orig -delete -print

# Automake >= 1.10 behaviour changed.
find -name Makefile.am -print0 |
	xargs -r0 fgrep -lZ '_LINK = ' -- |
	xargs -r0 sed -i '/_LDFLAGS)/! s/^\([^ ]\+\)_LINK = \$([^ ]\+)/& \$(\1_LDFLAGS)/' --

# Misdesign in libstdc++.
cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

# Never build with bundled libltdl.
rm -r libjava/libltdl

# Remove harmful autotools redeclarations.
>config/override.m4
>libjava/shlibpath.m4

# Replace m4_rename with m4_rename_force to fix build with autoconf >= 2.64.
if fgrep -wqs m4_rename_force /usr/share/autoconf/m4sugar/m4sugar.m4; then
	find -type f -name configure.ac -print0 |
		xargs -r0 fgrep -wlZ 'm4_rename' |
		xargs -r0 sed -i 's/\<m4_rename\>/&_force/' --
fi

# Adjust libstdc++ docs and its doxygen config.
%define onlinedocs http://gcc.gnu.org/onlinedocs
find libstdc++-v3/doc/ -type f -print0 |
	xargs -r0 grep -FZl libstdc++-html-USERS -- |
	xargs -r0 sed -i 's|libstdc++-html-USERS|%onlinedocs/libstdc++/&|' --
find libstdc++-v3/doc/ -type f -print0 |
	xargs -r0 grep -FZl '"latest-doxygen/' -- |
	xargs -r0 sed -i 's|"latest-doxygen/|"%onlinedocs/libstdc++/latest-doxygen/|' --
sed -i "s|\\(^INCLUDE_PATH[[:space:]]\\+=\\)[[:space:]]*$|\\1 $PWD/%buildtarget/%_target_platform/libstdc++-v3/include|" \
	libstdc++-v3/doc/doxygen/user.cfg.in


%build
libtoolize --copy --install --force
install -pm644 %_datadir/libtool/aclocal/*.m4 .
patch -p0 < %_sourcedir/alt-libtool.m4-gcj.patch

%ifdef _cross_platform
# Pretend this isn't cross-compiler
sed -i -e 's/^[[:blank:]]\+libstdcxx_incdir.\+target_alias.\+libstdcxx_incdir.\+$/:/' gcc/configure.ac
sed -i -e '/^INTERNAL_CFLAGS/ s,@CROSS@,,' -e 's,^\(CROSS_SYSTEM_HEADER_DIR\).\+$,\1 = %_includedir,' gcc/Makefile.in
# Do not try to build libgcc_s.so, supplemental libgcc*.a are still needed
sed -i -e '/^all: libgcc_eh.a/ s,libgcc_s$(SHLIB_EXT),,' -e 's,$(SHLIB_INSTALL),,' libgcc/Makefile.in
%endif

# Regenerate configure scripts.
for f in */aclocal.m4; do
	d="${f%%/*}"
	grep ^m4_include "$d"/aclocal.m4 |
		egrep -v '\[(libltdl/)?acinclude\.m4\]' >acinclude.m4~ ||:
	touch "$d"/acinclude.m4
	cat "$d"/acinclude.m4 >>acinclude.m4~
	mv acinclude.m4~ "$d"/acinclude.m4
	%autoreconf "$d"
	sh -n "$d"/configure
done

# Libtoolize now removes those of its build-aux files
# that haven't been installed during its invocation.
# Invoke libtoolize once more to install missing files.
# libatomic is just one of those directories that could
# be used to install all necessary build-aux files.
%autoreconf libatomic

# Hack to avoid building multilib libjava
# This hack is from Fedora's spec;
# we can't make a patch of, as Makefile.in is autogenerated;
# we can't patch Makefile.am directly, as automake
# will see 'else' and 'endif' and complain.
# Der Teufel soll das buserieren.
perl -pi -e 's/^all: all-recursive/ifeq (\$(MULTISUBDIR),)\nall: all-recursive\nelse\nall:\n\techo Multilib libjava build disabled\nendif/' libjava/Makefile.in
perl -pi -e 's/^install: install-recursive/ifeq (\$(MULTISUBDIR),)\ninstall: install-recursive\nelse\ninstall:\n\techo Multilib libjava install disabled\nendif/' libjava/Makefile.in
perl -pi -e 's/^check: check-recursive/ifeq (\$(MULTISUBDIR),)\ncheck: check-recursive\nelse\ncheck:\n\techo Multilib libjava check disabled\nendif/' libjava/Makefile.in

./contrib/gcc_update --touch

rm -rf %buildtarget
mkdir %buildtarget
pushd %buildtarget

%if_with java
[ -f /proc/self/maps ] || exit 1

%if_without java_bootstrap
if [ -x %gcc_target_libexecdir/ecj1 ]; then
export PATH=%gcc_target_libexecdir:$PATH
else
mkdir java_hacks
pushd java_hacks
cat >ecj1 <<EOF
#!/bin/sh
exec gij -cp /usr/share/java/ecj.jar org.eclipse.jdt.internal.compiler.batch.GCCMain "\$@"
EOF
chmod +x ecj1
export PATH=`pwd`${PATH:+:$PATH}
popd
fi
%endif #with_java_bootstrap
%endif #with_java

%if_with ada
rm -rf ada_hacks
for n in gnat %ada_binaries; do
	if [ -f "%_bindir/$n" ]; then
		continue
	fi
	if [ ! -f "%_bindir/$n%psuffix" ]; then
		echo "%_bindir/$n not found!" >&2
		exit 1
	fi
	mkdir -p ada_hacks
	ln -s "%_bindir/$n%psuffix" ada_hacks/"$n"
done
if [ -d ada_hacks ]; then
	export PATH="$PWD/ada_hacks${PATH:+:"$PATH"}"
fi
%endif

%define _configure_script ../configure
%define _configure_target --host=%_target_platform --build=%_target_platform --target=%gcc_target_platform
%remove_optflags -frecord-gcc-switches %optflags_nocpp %optflags_notraceback
export CC=%__cc \
	CFLAGS="%optflags" \
	CXXFLAGS="%optflags" \
	FFLAGS="%optflags" \
	GCJFLAGS="%optflags" \
	TCFLAGS="%optflags" \
	XCFLAGS="%optflags" \
	ac_cv_file__proc_self_exe=yes \
	gcc_cv_libc_provides_ssp=yes \
	libffi_cv_ro_eh_frame=yes \
	#

%configure \
	--enable-shared \
%ifdef _cross_platform
	--libdir=%_cross_lib \
	--disable-libssp \
	--disable-libgomp \
	--disable-libmudflap \
	--disable-libquadmath \
	--disable-libgfortran \
	--disable-libstdc++-v3 \
%else
	--enable-bootstrap \
%endif
	--program-suffix=%psuffix \
	--with-slibdir=/%_lib \
	--with-bugurl=http://bugzilla.altlinux.org \
	--enable-__cxa_atexit \
	--enable-threads=posix \
	--enable-checking=release \
	--with-system-zlib \
	--without-included-gettext \
	%{subst_enable multilib} \
	--enable-gnu-unique-object \
	--enable-linker-build-id \
	--with-linker-hash-style=gnu \
	--enable-languages="c%{?_with_cxx:,c++}%{?_with_fortran:,fortran}%{?_with_objc:,objc%{?_with_cxx:,obj-c++}}%{?_with_java:,java}%{?_with_ada:,ada}%{?_with_go:,go},lto" \
	--enable-plugin \
	%{?_with_objc:%{?_enable_objc_gc:--enable-objc-gc}} \
%if_with java
	--enable-java-awt=gtk \
	--with-native-libdir=%_libdir/gcj%psuffix \
	--with-ecj-jar=/usr/share/java/ecj.jar \
	--with-java-home=%_prefix/lib/jvm/java-1.5.0-gcj%psuffix-1.5.0.0/jre \
	--enable-libgcj-multifile \
	--disable-libjava-multilib \
	%{?_without_java_bootstrap:--enable-java-maintainer-mode} \
%endif
%ifndef	_cross_platform
%ifarch %ix86
	--with-arch=%_target_cpu --with-tune=generic \
%endif
%ifarch x86_64
	--with-arch_32=i586 --with-tune_32=generic \
	--with-multilib-list=m64,m32,mx32 \
%endif
%ifarch ppc ppc64
	--disable-softfloat --enable-secureplt \
	--with-long-double-128 \
%endif
%ifarch ppc
	--with-cpu=default32 \
%endif
%endif #_cross_platform
%if_gcc_arch armh
	--with-cpu=cortex-a8 --with-tune=cortex-a8 --with-arch=armv7-a \
	--with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux \
	--disable-sjlj-exceptions \
%endif
%if_gcc_arch arm
	--with-arch=armv5te --with-float=soft --with-abi=aapcs-linux \
	--disable-sjlj-exceptions \
%endif
	#

%make_build MAKEINFOFLAGS=--no-split \
	BOOT_CFLAGS='%optflags' %{?!_cross_platform:bootstrap}

%if_enabled doxygen
%make_build -C %_target_platform/libstdc++-v3/doc doc-html-doxygen
%make_build -C %_target_platform/libstdc++-v3/doc doc-man-doxygen
%endif #enabled_doxygen
popd #%buildtarget

# build printable documentation
%if_with pdf
(cd gcc/doc; for f in gcc cpp cppinternals; do
  texi2dvi -p -t @afourpaper -t @finalout -I ../doc/include $f.texi
done)
%if_with fortran
(cd gcc/f; for f in gfortran; do
  texi2dvi -p -t @afourpaper -t @finalout -I ../doc/include $f.texi
done)
%endif #with_fortran
%if_with java
(cd gcc/java; for f in gcj
  texi2dvi -p -t @afourpaper -t @finalout -I ../doc/include $f.texi
done)
%endif #with_java
%if_with ada
(cd gcc/ada; for f in gnat_rm gnat_ug_unx; do
  texi2dvi -p -t @afourpaper -t @finalout -I ../doc/include $f.texi
done
mv gnat_ug_unx.pdf gnat_ug.pdf
)
%endif #with_ada
%endif #with_pdf

%if_with ada
# for testsuite
(cd %buildtarget/gcc; ln -s ada/rts/libgnat%psuffix.so .)
%endif

%if_with java_tar
find libjava -name \*.h -type f | xargs grep -l '// DO NOT EDIT THIS FILE - it is machine generated' > libjava-classes.list
find libjava -name \*.class -type f >> libjava-classes.list
find libjava/testsuite -name \*.jar -type f >> libjava-classes.list
tar cf - -T libjava-classes.list | bzip2 -9 > %_sourcedir/libjava-classes-%version-%release.tar.bz2
%endif

%check
[ -w /dev/ptmx -a -f /proc/self/maps ] || exit
cd %buildtarget
GCC_TOLERATE_ALWAYS_OVERFLOW=1 make -k check ||:
../contrib/test_summary ||:

%install
mkdir -p %buildroot%gcc_doc_dir

# Copy various doc files here and there
CopyDocs()
{
	local n="$1"
	shift
	mkdir -p "%buildroot%gcc_doc_dir/$n"
	local d="$1"
	shift
	local f
	for f in "$d"/*{README,NEWS,LICENSE,THREADS}*; do
		[ -f "$f" ] || continue
		install -pv -m644 "$f" "%buildroot%gcc_doc_dir/$n/"
	done
}

CopyDocs gcc gcc

%if_with cxx
CopyDocs g++ gcc/cp
CopyDocs libstdc++ libstdc++-v3
cp -av libstdc++-v3/doc/html %buildroot%gcc_doc_dir/libstdc++/
if [ -d %buildtarget/%_target_platform/libstdc++-v3/doc/doxygen/html ]; then
	cp -a %buildtarget/%_target_platform/libstdc++-v3/doc/doxygen/html \
		%buildroot%gcc_doc_dir/libstdc++/
fi
if [ -d %buildtarget/%_target_platform/libstdc++-v3/doc/doxygen/man ]; then
	cp -a %buildtarget/%_target_platform/libstdc++-v3/doc/doxygen/man/man3 \
		%buildroot%_mandir/
fi
%endif #with_cxx

%if_with fortran
CopyDocs gfortran gcc/f
%endif #with_fortran

%if_with objc
CopyDocs libobjc libobjc
%endif #with_objc

%if_with java
CopyDocs boehm-gc boehm-gc
CopyDocs libjava libjava
%endif #with_java

%if_with go
CopyDocs libgo gcc/go
%endif #with_go

pushd %buildtarget
%make_install install DESTDIR=%buildroot
popd #%buildtarget

# Remove install-tools.
rm -r %buildroot{%gcc_target_libdir,%gcc_target_libexecdir}/install-tools

# Rename binaries which will be packaged under alternatives control.
pushd %buildroot%_bindir
	rm -vf %gcc_target_platform-gcc-%version {%gcc_target_platform-,}c++%psuffix
	%{?_with_java:rm gnative2ascii*}
	for n in \
	  cpp \
	  gcc gcov \
	  %{?_with_cxx:g++} \
	  %{?_with_fortran:gfortran} \
	  %{?_with_java:gcj %java_binaries} \
	  %{?_with_ada:gnat %ada_binaries} \
	  %{?_with_go:gccgo} \
	  ; do
		[ -f "%gcc_target_platform-$n%psuffix" ] ||
			mv -v "$n%psuffix" "%gcc_target_platform-$n%psuffix"
		ln -snf "%gcc_target_platform-$n%psuffix" "$n%psuffix"
	done
popd

%ifdef _cross_platform
rm %buildroot%_libdir/libiberty.a
rm -rf %buildroot/%_lib
cat > %buildroot%gcc_target_libdir/libgcc_s.so << 'E_O_F'
/* GNU ld script
   Use the shared library, but some functions are only in
   the static library.  */
GROUP ( libgcc_s.so.1 libgcc.a )
E_O_F
%else
pushd %buildroot%_libdir
	rm lib*.la %{?_with_java:*/lib*.la}
	rm libssp* libiberty.a
	mv *.a %buildroot%gcc_target_libdir/
%ifnarch mips mipsel s390x ppc64le riscv64
	mv *.o %buildroot%gcc_target_libdir/
%endif
	for f in *.so; do
		v=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
		[ -f "$v" ]
		ln -s ../../../"$v" "%buildroot%gcc_target_libdir/$f"
		rm "$f"
	done
popd
pushd %buildroot/%_lib
	for f in *.so; do
		if v="$(readlink "$f")"; then
			ln -s ../../../../../%_lib/"$v" \
				"%buildroot%gcc_target_libdir/$f"
			rm "$f"
		else
			mv "$f" "%buildroot%gcc_target_libdir/"
		fi
	done
popd

# Relocate itm, gomp and gfortran files.
mv %buildroot%_libdir/libitm.spec %buildroot%gcc_target_libdir/
mv %buildroot%_libdir/libgomp.spec %buildroot%gcc_target_libdir/
mv %buildroot%_libdir/libgfortran.spec %buildroot%gcc_target_libdir/
%endif

# Package fixed *limits.h
mv %buildroot%gcc_target_libdir/include{-fixed,}/limits.h
mv %buildroot%gcc_target_libdir/include{-fixed,}/syslimits.h

# Remove precompiled headers.
rm -rf %buildroot%_includedir/c++/*/*/*/*.gch

%if_with ada
# Dispatch Ada 95 libraries.
pushd %buildroot%gcc_target_libdir
	for n in gnat gnarl; do
		mv adalib/lib$n-*.so %buildroot%_libdir/
		rm adalib/lib$n.so
		ln -s ../../../lib$n-*.so lib$n.so
		ln -s ../../../lib$n-*.so lib$n%psuffix.so
	done
	mv adalib/*.a .
popd
%endif #with_ada

%if_with java
# gcj -static doesn't work properly anyway, unless using --whole-archive
find %buildroot \( \
	-name libgcj.a -o \
	-name libgij.a -o \
	-name libgtkpeer.a -o \
	-name libgcj_bc.a -o \
	-name libgcj-tools.a -o \
	-name libjavamath.a \
	-name libjvm.a \) -delete

# Relocate Java headers to version-specific compiler directory.
mv %buildroot%_includedir/c++/%gcc_branch/{java,javax,gnu} %buildroot%gcc_target_libdir/include/
mv %buildroot%_includedir/c++/%gcc_branch/gcj/* %buildroot%gcc_target_libdir/include/gcj/
rmdir %buildroot%_includedir/c++/%gcc_branch/gcj

# Fix libgcj.spec and move it to compiler-specific directory.
sed -i 's/lib: /&%%{static:%%eJava programs cannot be linked statically}/' \
	%buildroot%_libdir/libgcj.spec
mv %buildroot%_libdir/libgcj.spec %buildroot%gcc_target_libdir/

mkdir -p %buildroot%_libdir/gcj%psuffix/classmap.db.d

# libgcj-src files
make DESTDIR=%buildroot -C %buildtarget/%_target_platform/libjava install-src.zip
%endif #with_java

%ifndef _cross_platform
%ifarch x86_64
mkrel32()
{
	local d32=$1 d64=$2 rel; shift 2
	mkdir -p %buildroot$d32
	rel=$(relative $d32 $d64/32)
	ln -s $rel %buildroot$d64/32
}

mkrel32 %gcc_target_lib32dir %gcc_target_libdir
%if_with cxx
mkrel32 %gxx32idir %gxx64idir
%endif
%endif # x86_64
%endif # _cross_platform

# buildreq substitution rules.
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
for n in \
    cpp gcc gcc-plugin-devel \
%ifarch %libatomic_arches
    libatomic-devel-static \
%endif
%ifarch %libasan_arches
    libasan-devel-static \
%endif
%ifarch %libtsan_arches
    libtsan-devel-static \
%endif
%ifarch %libitm_arches
    libitm-devel-static \
%endif
    libgomp-devel libgomp-devel-static \
    libmudflap-devel libmudflap-devel-static \
    %{?_with_cxx:gcc-c++ libstdc++-devel libstdc++-devel-static} \
    %{?_with_fortran:gcc-fortran libgfortran-devel libgfortran-devel-static} \
    %{?_with_fortran:libquadmath-devel libquadmath-devel-static} \
    %{?_with_ada:gcc-gnat libgnat libgnat-devel libgnat-devel-static} \
    %{?_with_java:gcc-java libgcj libgcj-plugins libgcj-devel} \
    %{?_with_objc:gcc-objc libobjc-devel libobjc-devel-static %{?_with_cxx:gcc-objc++}} \
    %{?_with_go:gcc-go libgo-devel libgo-devel-static} \
    ; do
	pref="${n%%%%-*}"
	suf="${n#$pref}"
	t="${pref}%gcc_branch$suf"
	echo "$n" >"%buildroot%_sysconfdir/buildreqs/packages/substitute.d/$t"
done
chmod 644 %buildroot%_sysconfdir/buildreqs/packages/substitute.d/*

# buildreq ignore rules.
mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
cat >%buildroot%_sysconfdir/buildreqs/files/ignore.d/%name <<EOF
^%gcc_target_libdir(/include)?$
^%gcc_target_libexecdir(/include)?$
EOF

%if_with cxx
# no valid g++ manpage exists in 4.1+ series.
rm %buildroot%_man1dir/g++%psuffix.1
ln -s gcc%psuffix.1.xz %buildroot%_man1dir/g++%psuffix.1.xz

%ifndef _cross_platform
mkdir -p %buildroot%gcc_gdb_auto_load
mv -f %buildroot%_libdir/libstdc++*gdb.py* %buildroot%gcc_gdb_auto_load
pushd libstdc++-v3/python
for i in `find . -name \*.py`; do
  touch -r $i %buildroot%_datadir/gcc%psuffix/python/$i
done
touch -r hook.in %buildroot%gcc_gdb_auto_load/libstdc++*gdb.py
popd
%endif
%endif #with_cxx

%find_lang gcc%psuffix
%find_lang --append --output gcc%psuffix.lang cpplib%psuffix
%add_findprov_lib_path %_libdir/gcj%psuffix

%files
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%dir %gcc_doc_dir/
%gcc_doc_dir/gcc/
%_bindir/gcc%psuffix
%_bindir/gcov%psuffix
%_bindir/gcc-ar%psuffix
%_bindir/gcc-nm%psuffix
%_bindir/gcc-ranlib%psuffix
%_bindir/%gcc_target_platform-gcc%psuffix
%_bindir/%gcc_target_platform-gcov%psuffix
%_bindir/%gcc_target_platform-gcc-ar%psuffix
%_bindir/%gcc_target_platform-gcc-nm%psuffix
%_bindir/%gcc_target_platform-gcc-ranlib%psuffix
%_man1dir/gcc%psuffix.*
%_man1dir/gcov%psuffix.*
%dir %gcc_target_libdir/
%dir %gcc_target_libdir/include/
%gcc_target_libdir/include/float.h
%gcc_target_libdir/include/iso646.h
%gcc_target_libdir/include/limits.h
%gcc_target_libdir/include/stdalign.h
%gcc_target_libdir/include/stdarg.h
%gcc_target_libdir/include/stdfix.h
%gcc_target_libdir/include/stdbool.h
%gcc_target_libdir/include/stddef.h
%gcc_target_libdir/include/stdint.h
%gcc_target_libdir/include/stdint-gcc.h
%gcc_target_libdir/include/stdnoreturn.h
%gcc_target_libdir/include/syslimits.h
%gcc_target_libdir/include/unwind.h
%gcc_target_libdir/include/varargs.h

%if_gcc_arch arm
%gcc_target_libdir/include/arm_neon.h
%gcc_target_libdir/include/mmintrin.h
%gcc_target_libdir/include/unwind-arm-common.h
%endif
%if_gcc_arch armh
%gcc_target_libdir/include/arm_neon.h
%gcc_target_libdir/include/mmintrin.h
%gcc_target_libdir/include/unwind-arm-common.h
%endif
%if_gcc_arch aarch64
%gcc_target_libdir/include/arm_neon.h
%endif
%ifndef _cross_platform
%ifarch %ix86 x86_64
%gcc_target_libdir/include/*intrin*.h
%gcc_target_libdir/include/cpuid.h
%gcc_target_libdir/include/cross-stdarg.h
%gcc_target_libdir/include/mm3dnow.h
%gcc_target_libdir/include/mm_malloc.h
%endif
%ifarch ppc ppc64
%gcc_target_libdir/include/altivec.h
%gcc_target_libdir/include/paired.h
%gcc_target_libdir/include/ppc-asm.h
%gcc_target_libdir/include/ppu_intrinsics.h
%gcc_target_libdir/include/si2vmx.h
%gcc_target_libdir/include/spe.h
%gcc_target_libdir/include/spu2vmx.h
%gcc_target_libdir/include/vec_types.h
%endif
%endif
%gcc_target_libdir/crt*.o
%gcc_target_libdir/libgcc_s.so
%gcc_target_libdir/libgcc*.a
%gcc_target_libdir/libgcov.a
%ifarch %libatomic_arches
%gcc_target_libdir/libatomic.so
%endif
%ifarch %libasan_arches
%gcc_target_libdir/libasan_preinit.o
%gcc_target_libdir/libasan.so
%endif
%ifarch %libitm_arches
%gcc_target_libdir/libitm.so
%gcc_target_libdir/libitm.spec
%endif
%ifarch %libtsan_arches
%gcc_target_libdir/libtsan.so
%endif
%ifndef _cross_platform
%ifarch x86_64
%dir %gcc_target_lib32dir/
%gcc_target_libdir/32
%endif
%endif
%dir %gcc_target_libexecdir/
%dir %gcc_target_libexecdir/plugin/
%gcc_target_libexecdir/collect2
%gcc_target_libexecdir/lto-wrapper
%gcc_target_libexecdir/lto1
%gcc_target_libexecdir/liblto_plugin.so*
%gcc_target_libexecdir/plugin/gengtype

%if_with java
%exclude %_bindir/aot-compile%psuffix
%exclude %_bindir/rebuild-gcj-db%psuffix
%exclude %_libdir/logging.properties
%exclude %_libdir/security/classpath.security
%exclude %_man1dir/aot-compile-*
%exclude %_man1dir/gjdoc-*
%exclude %_man1dir/gnative2ascii-*
%exclude %_man1dir/rebuild-gcj-db-*
%endif

%if_with fortran
%exclude %gcc_target_libdir/libgfortranbegin.la
%endif

%exclude %gcc_target_libdir/include-fixed
%exclude %gcc_target_libdir/include/ssp
%exclude %gcc_target_libdir/libcaf_single.la
%exclude %gcc_target_libdir/plugin/gtype.state
%exclude %gcc_target_libexecdir/liblto_plugin.la
%exclude %_datadir/locale/de/LC_MESSAGES/libstdc++.mo
%exclude %_datadir/locale/fr/LC_MESSAGES/libstdc++.mo
%exclude %_man7dir/fsf-funding.7*
%exclude %_man7dir/gfdl.7*
%exclude %_man7dir/gpl.7*

%if_disabled compat
%files -n libgcc1
/%_lib/libgcc_s.so.*

%ifarch %libatomic_arches
%files -n libatomic1
%_libdir/libatomic.so.*
%endif
%endif

%ifarch %libasan_arches
%files -n libasan0
%_libdir/libasan.so.0*
%endif

%if_disabled compat
%ifarch %libtsan_arches
%files -n libtsan0
%_libdir/libtsan.so.*
%endif

%ifarch %libitm_arches
%files -n libitm1
%_libdir/libitm.so.*
%endif

%files -n libgomp1
%_libdir/libgomp.so.*
%endif #compat

%files -n libmudflap0
%_libdir/libmudflap*.so.*

%if_disabled compat
%ifarch %libquadmath_arches
%files -n libquadmath0
%_libdir/libquadmath.so.0*
%endif
%endif #compat

%ifndef _cross_platform

%files plugin-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/gcc%gcc_branch-plugin-devel
%gcc_target_libdir/plugin/include/

%ifarch %libatomic_arches
%files -n libatomic%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libatomic%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libatomic.a
%endif

%ifarch %libasan_arches
%files -n libasan%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libasan%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libasan.a
%endif

%ifarch %libtsan_arches
%files -n libtsan%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libtsan%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libtsan.a
%endif

%files -n libgomp%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgomp%gcc_branch-devel
%dir %gcc_target_libdir/
%dir %gcc_target_libdir/include/
%gcc_target_libdir/include/omp.h
%gcc_target_libdir/libgomp.so
%gcc_target_libdir/libgomp.spec

%files -n libgomp%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libgomp%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libgomp.a

%ifarch %libitm_arches
%files -n libitm%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libitm%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libitm.a
%endif

%files -n libmudflap%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libmudflap%gcc_branch-devel
%dir %gcc_target_libdir/
%dir %gcc_target_libdir/include/
%gcc_target_libdir/include/mf-runtime.h
%gcc_target_libdir/libmudflap*.so

%files -n libmudflap%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libmudflap%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libmudflap*.a

%ifarch %libquadmath_arches
%files -n libquadmath%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libquadmath%gcc_branch-devel
%dir %gcc_target_libdir/
%dir %gcc_target_libdir/include/
%gcc_target_libdir/include/quadmath.h
%gcc_target_libdir/include/quadmath_weak.h
%gcc_target_libdir/libquadmath.so

%files -n libquadmath%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libquadmath%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libquadmath.a
%endif

%endif # _cross_platform

%files -n cpp%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/cpp%gcc_branch
%_bindir/cpp%psuffix
%_bindir/%gcc_target_platform-cpp%psuffix
%_man1dir/cpp%psuffix.*
%dir %gcc_target_libexecdir/
%gcc_target_libexecdir/cc1

%if_with cxx
%if_disabled compat
%files -n libstdc++6
%_libdir/libstdc++.so.*
%dir %gcc_gdb_auto_load/
%gcc_gdb_auto_load/libstdc*gdb.py*
%dir %_datadir/gcc%psuffix/
%_datadir/gcc%psuffix/python/
%endif # compat

%ifndef _cross_platform

%files -n libstdc++%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libstdc++%gcc_branch-devel
%dir %gcc_doc_dir/
%gcc_doc_dir/libstdc++
%_includedir/c++/*
%dir %gcc_target_libdir/
%gcc_target_libdir/libstdc++.so
%gcc_target_libdir/libsupc++.a
%ifarch x86_64
%dir %gxx32idir/
%gxx64idir/32
%endif

%files -n libstdc++%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libstdc++%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libstdc++.a

%endif # _cross_platform

%files c++
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-c++
%dir %gcc_doc_dir/
%gcc_doc_dir/g++
%_bindir/g++%psuffix
%_bindir/%gcc_target_platform-g++%psuffix
%_man1dir/g++%psuffix.*
%dir %gcc_target_libexecdir/
%gcc_target_libexecdir/cc1plus
%endif #with_cxx

%if_with objc
%if_disabled compat
%files -n libobjc4
%_libdir/libobjc*.so.*
%endif # compat

%files -n libobjc%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libobjc%gcc_branch-devel
%dir %gcc_doc_dir/
%gcc_doc_dir/libobjc/
%dir %gcc_target_libdir/
%gcc_target_libdir/libobjc*.so
%dir %gcc_target_libdir/include/
%gcc_target_libdir/include/objc/

%files -n libobjc%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libobjc%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libobjc*.a

%files objc
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-objc
%dir %gcc_target_libexecdir/
%gcc_target_libexecdir/cc1obj

%if_with cxx
%files objc++
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-objc++
%dir %gcc_target_libexecdir/
%gcc_target_libexecdir/cc1objplus
%endif #with_cxx
%endif #with_objc

%if_with fortran
%if_disabled compat
%files -n libgfortran3
%_libdir/libgfortran.so.*
%endif # compat

%ifndef _cross_platform

%files -n libgfortran%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgfortran%gcc_branch-devel
%dir %gcc_target_libdir/
%gcc_target_libdir/libgfortran.so
%gcc_target_libdir/finclude/

%files -n libgfortran%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libgfortran%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libgfortran.a

%endif # _cross_platform

%files fortran
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-fortran
%_bindir/gfortran%psuffix
%_bindir/%gcc_target_platform-gfortran%psuffix
%_man1dir/gfortran%psuffix.*
%dir %gcc_target_libdir/
%gcc_target_libdir/libgfortran.spec
%gcc_target_libdir/libgfortranbegin.a
%gcc_target_libdir/libcaf_single.a
%dir %gcc_target_libexecdir/
%gcc_target_libexecdir/f951
%endif #with_fortran

%if_with java
%if_disabled compat
%files -n libgcj_bc1
%_libdir/libgcj_bc*.so.*
%endif # compat

%files -n libgcj%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch
%_libdir/libgcj-*.so.*
%_libdir/libgcj.so.*
%_libdir/libgij.so.*
%dir %_libdir/gcj%psuffix/
%dir %_libdir/gcj%psuffix/classmap.db.d/
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %_libdir/gcj%psuffix/classmap.db
%_libdir/gcj%psuffix/libjavamath.so
%_libdir/gcj%psuffix/libjvm.so

%files -n libgcj%gcc_branch-plugins
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch-plugins
%dir %_libdir/gcj%psuffix/
%_libdir/gcj%psuffix/lib*
%exclude %_libdir/gcj%psuffix/libjavamath.so
%exclude %_libdir/gcj%psuffix/libjvm.so

%files -n libgcj%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch-devel
%dir %gcc_doc_dir/
%gcc_doc_dir/boehm-gc
%gcc_doc_dir/libjava
%_pkgconfigdir/libgcj*.pc
%dir %gcc_target_libdir/
%gcc_target_libdir/libgcj.spec
%gcc_target_libdir/libgcj*.so
%gcc_target_libdir/libgij.so
%dir %gcc_target_libdir/include/
%gcc_target_libdir/include/j*.h
%gcc_target_libdir/include/java/
%gcc_target_libdir/include/javax/
%gcc_target_libdir/include/gnu/
%gcc_target_libdir/include/gcj/

%files -n libgcj%gcc_branch-jar
%_datadir/java/*.jar

%files -n libgcj%gcc_branch-src
%_datadir/java/*.zip

%files java
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-java
%_altdir/java%gcc_branch
%_bindir/*gappletviewer%psuffix
%_bindir/gc-analyze%psuffix
%_bindir/*gcj%psuffix
%_bindir/*gcj-dbtool%psuffix
%_bindir/*gcjh%psuffix
%_bindir/*gij%psuffix
%_bindir/*gjar%psuffix
%_bindir/*gjarsigner%psuffix
%_bindir/*gjavah%psuffix
%_bindir/*gkeytool%psuffix
%_bindir/*gorbd%psuffix
%_bindir/*grmic%psuffix
%_bindir/*grmid%psuffix
%_bindir/*grmiregistry%psuffix
%_bindir/*gserialver%psuffix
%_bindir/*gtnameserv%psuffix
%_bindir/*jcf-dump%psuffix
%_bindir/*jv-convert%psuffix
%_man1dir/gappletviewer%psuffix.*
%_man1dir/gc-analyze%psuffix.*
%_man1dir/gcj%psuffix.*
%_man1dir/gcj-dbtool%psuffix.*
%_man1dir/gcjh%psuffix.*
%_man1dir/gij%psuffix.*
%_man1dir/gjar%psuffix.*
%_man1dir/gjarsigner%psuffix.*
%_man1dir/gjavah%psuffix.*
%_man1dir/gkeytool%psuffix.*
%_man1dir/gorbd%psuffix.*
%_man1dir/grmic%psuffix.*
%_man1dir/grmid%psuffix.*
%_man1dir/grmiregistry%psuffix.*
%_man1dir/gserialver%psuffix.*
%_man1dir/gtnameserv%psuffix.*
%_man1dir/jcf-dump%psuffix.*
%_man1dir/jv-convert%psuffix.*
%dir %gcc_target_libexecdir/
%gcc_target_libexecdir/ecj1
%gcc_target_libexecdir/jc1
%gcc_target_libexecdir/jvgenmain
%endif #with_java

%if_with ada
%files gnat
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-gnat
%_bindir/%gcc_target_platform-gnat*%psuffix
%_bindir/gnat*%psuffix
%dir %gcc_target_libdir/
%gcc_target_libdir/ada*
%dir %gcc_target_libexecdir/
%gcc_target_libexecdir/gnat1

%files -n libgnat%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgnat%gcc_branch
%_libdir/libgna*.so

%files -n libgnat%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgnat%gcc_branch-devel
%dir %gcc_target_libdir/
%gcc_target_libdir/libgna*.so
%ifarch %ix86 x86_64
%gcc_target_libdir/libgmem.a
%endif

%files -n libgnat%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libgnat%gcc_branch-devel-static
%dir %gcc_target_libdir/
%gcc_target_libdir/libgna*.a
%endif #with_ada

%if_with go
%files go
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-go
%_bindir/gccgo%psuffix
%_bindir/%gcc_target_platform-gccgo%psuffix
%_man1dir/gccgo%psuffix.*
%dir %gcc_target_libexecdir/
%gcc_target_libexecdir/go1

%files -n libgo4
%_libdir/libgo.so.4*

%files -n libgo%gcc_branch-devel
%dir %gcc_doc_dir/
%gcc_doc_dir/libgo/
%config %_sysconfdir/buildreqs/packages/substitute.d/libgo%gcc_branch-devel
%dir %gcc_target_libdir/
%gcc_target_libdir/libgo.so
%gcc_target_libdir/libgobegin.a
%_libdir/go/%gcc_branch/

%files -n libgo%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libgo%gcc_branch-devel-static
%gcc_target_libdir/libgo.a
%endif #with_go

%files locales -f gcc%psuffix.lang

%ifndef _cross_platform

%files doc
%{?_enable_doxygen:%_man3dir/*}
%_infodir/cpp*.info*
%_infodir/gcc*.info*
%_infodir/libitm.info*
%_infodir/libgomp*.info*
%{?_with_fortran:%_infodir/gfortran.info*}
%{?_with_java:%_infodir/gcj.info*}
%{?_with_java:%_infodir/cp-tools.info*}
%{?_with_ada:%_infodir/gnat*.info*}

%if_with pdf
%doc gcc/doc/cpp*.pdf
%doc gcc/doc/gcc*.pdf
%{?_with_fortran:%doc gcc/doc/gfortran.pdf}
%{?_with_ada:%doc gcc/doc/gnat*.pdf}
%endif #with_pdf

%endif # _cross_platform

%changelog
* Fri Oct 04 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.8.2-alt7
- Fixed build with libtool 2.4.6 (ldv@).
- doc: dropped libquadmath.info.

* Sat Sep 29 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.8.2-alt6.1
- Dropped redundant libcloog-isl-devel build dependency.
- Exclude aarch64 architecture.

* Fri Jan 12 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.8.2-alt6
- Rebuilt with gcc 4.8.
- Fixed build with glibc 2.26, and texinfo 6.5.
- Disabled java support.
- Dropped alternatives.

* Mon Feb 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.8.2-alt5
- Changed compress_method to xz.

* Tue Sep 23 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.8.2-alt4
- Built in gcc4.9 compatibility mode.

* Tue Apr 08 2014 Dmitry V. Levin <ldv@altlinux.org> 4.8.2-alt3
- Synced with Fedora gcc-4.8.2-15.
- Packaged %_bindir/gcc-{ar,nm,ranlib}-4.8 (reported by led@).

* Mon Feb 17 2014 Dmitry V. Levin <ldv@altlinux.org> 4.8.2-alt2
- gnat: added alternatives support.

* Mon Feb 10 2014 Dmitry V. Levin <ldv@altlinux.org> 4.8.2-alt1
- Updated to redhat/gcc-4_8-branch r206854.
- Synced with Fedora gcc-4.8.2-14 and Debian gcc-4.8.2-15.

* Tue Jan 07 2014 Dmitry V. Levin <ldv@altlinux.org> 4.7.2-alt8
- Fixed build with GNU Autoconf >= 2.69.
- Changed build to use GNU Automake 1.11.

* Thu Jan 24 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7.2-alt7
- libgfortran3, libitm1: added a strict requirement on libgcc1.

* Wed Jan 09 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7.2-alt6
- libgcj: fixed GCJ_ENDORSED_DIRS (by Igor Vlasenko; closes: #28319).
- libgcj-jar: dropped %_datadir/java/gcj%gcc_branch-endorsed/.

* Fri Nov 16 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7.2-alt5
- Synced with fedora gcc-4.7.2-8.

* Mon Oct 29 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7.2-alt4
- Synced with fedora gcc-4.7.2-5.

* Mon Oct 01 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.7.2-alt3
- relocate libquadmath and libitm info files to doc subpackage
- add libquadmath substitute rule for buildreq

* Mon Oct 01 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.7.2-alt2
- force linker hash style to gnu

* Mon Sep 24 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.7.2-alt1
- 4.7.2

* Mon Aug 27 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6.3-alt7
- Backported upstream changes to fix build with glibc-2.16.
- Disabled go backend for a while because it doesn't build
  with glibc-2.16.

* Fri Aug 24 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6.3-alt6
- Define _FORTIFY_SOURCE only for optimization level 2 or higher.
- libgfortran4.6-devel: fixed non-strict dependency on libquadmath4.6-devel.

* Mon Aug 20 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6.3-alt5
- Go language support packaged (closes: #27654)

* Mon Jul 30 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6.3-alt4
- armh: use ld-linux-armhf.so.3 as dynamic linker
- armh: set defaults to hard-float for armv7

* Fri Jun 15 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6.3-alt3
- fixed enforced FORTIFY_SOURCE with no opt-out

* Wed May 30 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6.3-alt2
- package gfortran.spec, mistakenly omitted in prev release

* Tue May 15 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6.3-alt1
- 4.6.3

* Wed Apr 11 2012 Dmitry V. Levin <ldv@altlinux.org> 4.5.3-alt3
- Updated to build with libtool 2.4.2.

* Tue Apr 03 2012 Dmitry V. Levin <ldv@altlinux.org> 4.5.3-alt2
- Merged with gcc-4_5-branch@186094.
- gcc4.5, libstdc++4.5-devel:
  packaged directories and symlinks for -m32 on x86_64.

* Wed Jan 11 2012 Dmitry V. Levin <ldv@altlinux.org> 4.5.3-alt1
- Merged with gcc-4_5-branch@183083.
- Renamed subpackages to ease subsequent gcc updates:
  libgcc4.5 -> libgcc1,
  libgcj_bc4.5 -> libgcj_bc1,
  libgomp4.5 -> libgomp1,
  libgfortran4.5 -> libgfortran3,
  libmudflap4.5 -> libmudflap0,
  libobjc4.5 -> libobjc2,
  libstdc++4.5 -> libstdc++6,
  libgcc4.5-plugin-devel -> gcc4.5-plugin-devel.

* Tue Feb 08 2011 Dmitry V. Levin <ldv@altlinux.org> 4.5.1-alt8
- Dropped -debug subpackages.
- Rebuilt for debuginfo.

* Wed Dec 01 2010 Kirill A. Shutemov <kas@altlinux.org> 4.5.1-alt7
- Synced with Fedora 4.5.1-6.

* Tue Nov 16 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.1-alt6
- Fixed build with new perl.

* Mon Nov 15 2010 Kirill A. Shutemov <kas@altlinux.org> 4.5.1-alt5
- Synced with Fedora 4.5.1-5.

* Mon Nov 08 2010 Kirill A. Shutemov <kas@altlinux.org> 4.5.1-alt4
- Fixed PR46364: g++ ICE with -O3.

* Mon Nov 08 2010 Kirill A. Shutemov <kas@altlinux.org> 4.5.1-alt3
- Fixed PR45969: ICE in build_binary_op, at c-typeck.c:9833

* Sun Nov 07 2010 Kirill A. Shutemov <kas@altlinux.org> 4.5.1-alt2
- Fixed build.
- Fixed PR45447: ICE with '-g -femit-struct-debug-baseonly' on ARM
  (closes: 24441).

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 4.5.1-alt1
- Synced with Fedora 4.5.1-4.
- Update Debian patches.
- Drop libffi4: no users in Sisyphus.
- Package GCC plugin header files into libgcc%%gcc_branch-plugin-devel.

* Wed Oct 13 2010 Dmitry V. Levin <ldv@altlinux.org> 4.4.5-alt1
- Synced with Fedora 4.4.5-1.

* Sat Aug 21 2010 Kirill A. Shutemov <kas@altlinux.org> 4.4.4-alt3
- Add Obsoletes/Provides to libffi4.

* Wed Aug 18 2010 Kirill A. Shutemov <kas@altlinux.org> 4.4.4-alt2
- Package libffi.so.4 for compatibility reason.

* Fri Aug 13 2010 Kirill A. Shutemov <kas@altlinux.org> 4.4.4-alt1
- Synced with Fedora 4.4.4-13

* Thu Aug 12 2010 Kirill A. Shutemov <kas@altlinux.org> 4.4.3-alt3
- Drop libffi* packages

* Fri Mar 19 2010 Kirill A. Shutemov <kas@altlinux.org> 4.4.3-alt2
- Synced with 4.4.3-10
  + PR tree-optimization/42890 (closes: 23083)

* Fri Jan 22 2010 Kirill A. Shutemov <kas@altlinux.org> 4.4.3-alt1
- Synced with FC 4.4.3-1.
  + re-add --param max-vartrack-size patch, but this time with default
    50mil instead of 5mil (closes: 22797).

* Wed Jan 13 2010 Dmitry V. Levin <ldv@altlinux.org> 4.4.2-alt4
- Rebuilt for rtld(GNU_UNIQUE) autodependencies.

* Sat Jan 09 2010 Dmitry V. Levin <ldv@altlinux.org> 4.4.2-alt3
- Added provides/obsoletes for libgomp4.1 to libgomp4.4.
- Added provides/obsoletes for libmudflap4.1 to libmudflap4.4.

* Fri Jan 08 2010 Dmitry V. Levin <ldv@altlinux.org> 4.4.2-alt2
- Synced with FC 4.4.2-20.
- Fixed build with fresh autoconf.

* Tue Oct 20 2009 Kirill A. Shutemov <kas@altlinux.org> 4.4.2-alt1
- Synced with FC 4.4.2-7
- Implement java bootstrap facility
- Workaround PR41468(ARM-specific).

* Mon Oct 05 2009 Dmitry V. Levin <ldv@altlinux.org> 4.4.1-alt3
- Updated ARM-specific fix for TEXTRELs in C++ shared objects (by Kirill A. Shutemov).

* Thu Oct 01 2009 Dmitry V. Levin <ldv@altlinux.org> 4.4.1-alt2
- Moved "make check" to %%check section.
- Packaged ARM-specific header files (by Kirill A. Shutemov).
- Implemented ASM_PREFERRED_EH_DATA_FORMAT macros for ARM (by Kirill A. Shutemov).

* Tue Aug 18 2009 Dmitry V. Levin <ldv@altlinux.org> 4.4.1-alt1
- Synced with FC 4.4.1-2.fc11 (4.4.1-20090729, svn revision 150210).

* Tue Jul 14 2009 Dmitry V. Levin <ldv@altlinux.org> 4.4.0-alt6
- Escalated "will always overflow destination buffer" warning to error.

* Mon Jul 13 2009 Dmitry V. Levin <ldv@altlinux.org> 4.4.0-alt5
- Synced with FC 4.4.0-12 (4.4.0-20090708, svn revision 149391).

* Tue Jul 07 2009 Dmitry V. Levin <ldv@altlinux.org> 4.4.0-alt4
- Synced with FC 4.4.0-10 (4.4.0-20090623, svn revision 148856).

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 4.4.0-alt3
- Synced with FC 4.4.0-5 (4.4.0-20090514, svn revision 147523).
- Removed obsolete %%install_info/%%uninstall_info calls.

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 4.4.0-alt2
- Synced with FC 4.4.0-4 (4.4.0-20090506, svn revision 147193).

* Mon May 04 2009 Dmitry V. Levin <ldv@altlinux.org> 4.4.0-alt1
- Updated to FC 4.4.0-3 (4.4.0-20090427, svn revision 146836).
- Updated Debian patches to 4.4.0-1.
- Updated ALT patches.
- Turned on -Wformat -Wformat-security by default.

* Sun May 03 2009 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt10
- Fixed build with fresh autotools.
- Relaxed interpackage dependencies for better co-existance with gcc 4.4.x.

* Mon Apr 06 2009 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt9
- Updated gcc4.3-java ecj build dependencies (2nd part of #18580 fix).

* Mon Apr 06 2009 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt8
- Fixed ada FTBFS by removing -I- gcc option from makefiles.
- Updated gcc4.3-java ecj dependencies (1st part of #18580 fix).

* Tue Dec 02 2008 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt7
- Updated gcc4.3-java build dependencies.

* Fri Nov 21 2008 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt6
- libffi4.3: Provides/Obsoletes libffi4.1 (closes: #17887).
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Switched to alternatives-0.4.

* Thu Nov 06 2008 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt5
- Updated to FC 4.3.2-7 (4.3.2-20081105, svn snapshot 141601).
- Moved %_datadir/java/*.jar to new libgcj%gcc_branch-jar noarch subpackage.
- Packaged gcc4.3-locales, gcc4.3-doc and libgcj4.3-src subpackages as noarch.

* Sat Nov 01 2008 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt4
- Fixed libgcj4.1 coexistance issues.

* Wed Oct 22 2008 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt3
- Fixed java build.
- Reenabled java on ix86/x86_64.

* Mon Oct 20 2008 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt2
- Enhanced testsuite.
- Fixed libstdc++ doxygenated reference (closes: #3891).
- Optionally genereate libstdc++ doxygenated manpages (#15361).
- Merged ARM-related Debian patches (kas@).
- Merged Debian patch to support ObjC on ARM EABI and
  enabled ObjC on ARM (kas@).

* Mon Oct 13 2008 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt1
- Updated to FC 4.3.2-6 (4.3.2-20081008, svn snapshot 140973).
- Updated Debian patches to 4.3.2-1.
- Updated ALT patches.
- Disabled java for a while.
- Dropped libstdc++%gcc_branch-devel-precompiled subpackage.
- Changed link spec to pass -Wl,-z,relro to the linker by default.

* Sun Jun 08 2008 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt3
- Removed c++filt from alternatives (at@).
- Added libgcj-src subpackage (viy@).
- Moved NLS files to new locales subpackage (closes: #11510).
- Do not package changelog files.

* Mon Mar 03 2008 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt2
- Fixed build with fresh makeinfo (avm@).

* Thu Feb 21 2008 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt1
- Updated to RH gcc-4.1.2-14.el5.

* Wed Oct 31 2007 Alex V. Myltsev <avm@altlinux.ru> 4.1.1-alt12
- Enabled multilib.

* Tue Jan 23 2007 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt11
- Updated to FC gcc-4.1.1-51.

* Sat Oct 14 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt10
- Updated to FC gcc-4.1.1-30.
- Removed libssp* subpackages (#10119).

* Sun Oct 08 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt9
- Added -D_FORTIFY_SOURCE=2 to default preprocessor options.
- Added -fstack-protector to default compiler options.
- Changed PARAM_SSP_BUFFER_SIZE from 8 to 4.

* Sun Oct 01 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt8
- Updated to FC gcc-4.1.1-28.
- Added --hash-style=gnu to default link options.

* Wed Sep 20 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt7
- Updated to FC gcc-4.1.1-24.
- Added /proc to java subpackage requirements.

* Tue Sep 12 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt6
- Updated to FC gcc-4.1.1-21.

* Fri Sep 08 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt5
- Updated to FC gcc-4.1.1-20.

* Thu Jun 29 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt4
- Updated to FC gcc-4.1.1-6.
- libstdc++4.1: Add requirement on glibc-core >= 6:2.3.6-alt7 (#9732).

* Thu Jun 22 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt3
- Updated to FC gcc-4.1.1-5.

* Tue Jun 13 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt2
- Updated to FC gcc-4.1.1-2.

* Thu May 25 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt1
- Updated to FC gcc-4.1.1-1.

* Fri May 19 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt4
- Updated to FC gcc-4.1.0-19.

* Mon May 15 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt3
- Updated to FC gcc-4.1.0-18.

* Sun May 14 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt2
- Updated to FC gcc-4.1.0-17.

* Sat May 13 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt1.1
- Corrected libgfortran%gcc_branch dependencies.

* Sat May 13 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt1
- Updated to FC gcc-4.1.0-16.

* Tue May 09 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.8
- Updated to FC gcc-4.1.0-15.

* Mon May 08 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.7
- Updated to FC gcc-4.1.0-14.

* Wed May 03 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.6
- Updated to FC gcc-4.1.0-13.

* Mon May 01 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.5
- Updated to FC gcc-4.1.0-12.

* Tue Apr 25 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.4
- Updated to FC gcc-4.1.0-11.

* Fri Apr 21 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.3
- Updated to FC gcc-4.1.0-10.

* Thu Apr 20 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.2
- Updated to FC gcc-4.1.0-9.

* Fri Apr 14 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.1
- Updated to FC gcc-4.1.0-8.
- Reviewed and updated patches.
- Reviewed and updated package dependencies.

* Thu Mar 09 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt2
- Relocated ffitarget.h (#9213).

* Wed Mar 08 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt1
- Updated to 3_4-rhl-branch 20051201 (RH gcc-3.4.5-2).

* Thu Mar 02 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.4-alt4
- Pass --as-needed option to GNU ld by default.
- Fixed build with make >= 3.81beta4.
- Fixed deplibs build issues on x86_64.
- Bootstrapped gnat for x86_64.
- Updated build dependencies.

* Thu Oct 20 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.4-alt3
- Fixed libgcj build to link with system libltdl.

* Wed Oct 12 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.4-alt2
- Updated to 3_4-rhl-branch 20050721 (RH gcc-3.4.4-2).
- Moved libgcj AWT peer library to separate subpackage.

* Thu Jun 23 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.4-alt1
- Updated to 3_4-rhl-branch 20050608.
- Reenabled java by default on all arches.
- Enabled build with make-3.81beta3.

* Fri Mar 18 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt6
- Merged with gcc-3_4-branch 20050314.
- Enabled testsuite by default.
- Packaged precompiled header files in separate subpackage.

* Mon Feb 28 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt5
- Updated to gcc-3_4-branch 20050222 (RH gcc-3.4.3-20).
- Removed bogus install dependence on make.
- Upgraded build and install dependencies on binutils.

* Sat Feb 12 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt4
- Updated to gcc-3_4-branch 20050210 (RH gcc-3.4.3-18).

* Tue Feb 08 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt3
- Updated to gcc-3_4-branch 20050125 (RH gcc-3.4.3-17).

* Thu Jan 13 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt2
- Updated to gcc-3_4-branch 20050105 (RH gcc-3.4.3-13).
- Converted alternatives config files to new format (0.2.0).

* Thu Dec 30 2004 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt1
- Updated to gcc-3_4-branch 20041227 (RH gcc-3.4.3-11).

* Tue Dec 28 2004 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt0.1
- Updated to gcc-3_4-branch 20041213 (RH gcc-3.4.3-10).
- Reviewed and updated patches.
- Reviewed and updated package dependencies.

* Sat May 15 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt5
- Rebuilt with binutils-2.15.90.0.3 and glibc-2.3.x.

* Tue Apr 20 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt4
- Synced with RH gcc-3.3.3-7 (gcc-3_3-branch 20040413).

* Fri Apr 09 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt3
- Synced with RH gcc-3.3.3-6 (gcc-3_3-branch 20040327).

* Wed Mar 17 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt2
- Synced with RH gcc-3.3.3-3 (gcc-3_3-branch 20040312).

* Fri Feb 20 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt1
- Synced with RH gcc-3.3.3-2 (gcc-3_3-branch 20040217).

* Thu Jan 22 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt0.2
- Synced with RH gcc-3.3.2-7 (gcc-3_3-branch 20040120).

* Sat Jan 03 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt0.1
- Synced with RH gcc-3.3.2-5 (gcc-3_3-branch 20031219).
- Minor specfile tweaks to ease gcc3.2/gcc3.3 upgrade.

* Wed Dec 24 2003 Dmitry V. Levin <ldv@altlinux.org> 3.3.2-alt1
- Updated to RH gcc-3.3.2-3 (gcc-3_3-branch 20031203),
  with -pie support.
- Updated patches.
- Relocated libgcc_s.so to %%gcc_target_libdir.
- Changed %%gcc_target_libdir/*.so symlink values.
- Packaged GNU Treelang compiler.
- Packaged GNAT (without alternatives support yet).

* Thu Oct 16 2003 Dmitry V. Levin <ldv@altlinux.org> 3.2.3-alt2
- Finalized alternatives transition.

* Wed Oct 15 2003 Stanislav Ievlev <inger@altlinux.ru> 3.2.3-alt1.4
- g++ manpage doesn't exist in 3.2 series, made symlink to gcc's manpage.

* Wed Oct 15 2003 Stanislav Ievlev <inger@altlinux.ru> 3.2.3-alt1.3
- added alternatives to g++ man-page, require more recent gcc-common version

* Tue Oct 14 2003 Stanislav Ievlev <inger@altlinux.ru> 3.2.3-alt1.2
- fix java alternatives config

* Tue Oct 14 2003 Stanislav Ievlev <inger@altlinux.ru> 3.2.3-alt1.1
- new alternatives support

* Mon Jun 09 2003 Dmitry V. Levin <ldv@altlinux.org> 3.2.3-alt1
- Updated to gcc_3_2-branch (20030506), dropped all non-alt patches.
- Merged:
  + RH: gcc-3_2-rhl8-branch (patches for fastjar,libffi,libiberty,libobjc);
  + Debian: gcc-3.2_3.2.3ds9-4 (15 patches);
  + SuSE (5 patches);
  + MDK (6 patches).
- Packaged libffi.
- Note that there are no rhl8-specific gcc patches in this release.

* Fri Nov 29 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt2
- Fixed typo in "%%triggerpostun c++".

* Tue Nov 26 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt1
- Updated to 3.2.1 release (3.2.1 20021119).
- Following patches merged upstream:
  + trunc_int_for_mode;
  + x86_64-q_regs_operand;
  + fold-const2;
  + i386-pr7242;
  + i386-pr7242;
  + loop-prefetch;
  + libstdc++-glibc23-1;
  + libstdc++-glibc23-2;
  + libstdc++-glibc23-3;
  + libstdc++-glibc23-4;
  + interface_only.
- Updated patches: tls, doc-gcov.
- Dropped patches: c++-tail-pad-backout.
- Added missing provides to gcc subpackage.
- Removed soname provides from -debug subpackages.
- Removed %_libdir/libstdc++.{so,a} (no longer needed).
- Moved java wrappers to separate subpackage (jdkgcj).
- Moved gccbug to separate subpackage (gcc-common).
- Removed prefixes from: jar grepjar rmic rmiregistry.
- Migrated to new alternatives scheme.

* Mon Sep 30 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt0.4
- Merged with rh gcc-3.2-7:
  * Tue Sep  3 2002 Bill Nottingham <notting@redhat.com> 3.2-7
  - fix calling of C++ destructors in certain cases
  * Tue Sep  3 2002 Jakub Jelinek <jakub@redhat.com> 3.2-6
  - update from CVS (but revert C++ tail padding patches
    for now)
  - further fixes to make libstdc++-v3 build on glibc 2.3
  - run libstdc++-v3 make check-abi on IA-32 during testing
  * Fri Aug 30 2002 Jakub Jelinek <jakub@redhat.com> 3.2-5
  - disable tail copy patches, they seem to still have problems
  - make libstdc++-v3 build on glibc 2.3 (and use thread-local
    locale model)
- libstdc++%gcc_branch:
  Added explicit versioned dependence on libgcc%gcc_branch (#0001332).
- %name-java: fixed update-alternatives.

* Fri Sep 06 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt0.3
- Disabled c++-tail-pad patch (causes internal errors in cpp code).
- Switched back to default stripping policy:
  make use of new (rpm-build >= 4.0.4-alt3) strip feature.
- Moved unstripped shared libraries to -debug subpackages.

* Fri Aug 30 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt0.2
- Merged with rh gcc-3.2-4:
  * Wed Aug 26 2002 Jakub Jelinek <jakub@redhat.com> 3.2-4
  - reorder alpha_encode_section_info checks slightly to fix an ICE
    when building glibc and to take better advantage of visibility
    attribute on Alpha
  - as gdb is not there yet, disable -momit-leaf-frame-pointer
    by default for now on IA-32
  - fix IA-64 bootstrap with tail padding patch (Jason Merrill, Daniel Berlin)
  - fix x86-64 %%RIP to %%rip, only output (%%rip) if no other relocation
    is used (Richard Henderson)
  * Fri Aug 23 2002 Jakub Jelinek <jakub@redhat.com> 3.2-3
  - take advantage of __attribute__((visibility())) on Alpha
  - avoid copying tail padding (Jason Merrill)
- Use /bin/readlink.
- Added "Conflicts: glibc-devel < 2.2.6".
- Raised alternatives priority from 15 to 30.

* Mon Aug 26 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt0.1
- Updated to snapshot 20020822.
- Merged ALT patches from 2.96 branch.
- Merged with rh gcc-3.2-2:
  * Thu Aug 22 2002 Jakub Jelinek <jakub@redhat.com> 3.2-2
  - fixed Dwarf2 DW_OP_GNU_push_tls_address patch from Richard Henderson.
  - don't mention removed -a and -ax options in the documentation
    (Nathan Sidwell, #72233).
  - fixed __typeof() followed by __asm() redirection from Alexandre Oliva.

* Wed Aug 21 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2-alt3
- Rewritten interpackage dependencies to make peace with other
  versions of GCC which may be installed in the system.
- Dropped gnat.
- Added %%with/%%without logic for conditional build.
- Cleaned up descriptions.
- Cleaned up %%prep and %%build sections.
- Rewritten %%install section (no idea how it could work before).
- Set proper version information.
- Fixed doc package (info documentation was incomplete).
- Relocated documentation to %_docdir/gcc-%version/.
- Relocated libgcj headers back to compiler-specific include directory.
- Renamed libf2c* to libg2c*.
- Libificated libg2c and libobjc packages.
- gcc: moved gccbug under update-alternatives control.
- c++: moved c++filt under update-alternatives control.
- libobjc: added libobjc_gc.* libraries.
- java: moved under update-alternatives control.
  (AKA: java now should be usable).
- Moved some manpages under update-alternatives control.
- Added buildreq substitution rules.
- Added buildreq ignore rules.
- Raised alternatives priority from 5 to 15.

* Mon Aug 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.2-alt2
- Synced with release tarball: 3.2 20020814 (release).
- Removed some patches - there are in tarball now.

* Tue Aug 13 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.2-alt1
- 3.2
- Added some Cooker & RawHide patches
- Fixed update-alternatives

* Mon Jun 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.1.1-alt1
- First build for Sisyphus
- Added some patches from CooKer
- Added patches from RH & Suse
