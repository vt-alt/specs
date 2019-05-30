%define _unpackaged_files_terminate_build 1

%def_enable bootstrap
%def_disable ibmlibs
%set_verify_elf_method no

# stable branches support uses this macro
%define qIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"

Name: mono
Version: 5.20.1.19
Release: alt2
Summary: Cross-platform, Open Source, .NET development framework

Group: Development/Other
License: MIT
Url: http://www.mono-project.com

# https://github.com/mono/mono.git
Source: %name-%version.tar

# by running the following command:
# sn -k mono.snk
# Dec 2015 ALT
Source2: mono.snk
Source3: monolite.tar.gz
Source4: mono-cert-sync.filetrigger

# External dependencies (git submodules)
Source5: Newtonsoft.Json-%version.tar
Source6: api-doc-tools-%version.tar
Source7: Lucene.Net.Light-%version.tar
Source8: SharpZipLib-%version.tar
Source9: api-snapshot-%version.tar
Source10: aspnetwebstack-%version.tar
Source11: binary-reference-assemblies-%version.tar
Source12: bockbuild-%version.tar
Source13: boringssl-%version.tar
Source14: cecil-%version.tar
Source15: cecil-legacy-%version.tar
Source16: corefx-%version.tar
Source17: corert-%version.tar
Source18: ikdasm-%version.tar
Source19: ikvm-%version.tar
Source20: linker-%version.tar
Source21: linker-cecil-%version.tar
Source22: nuget-buildtasks-%version.tar
Source23: nunit-lite-%version.tar
Source24: roslyn-binaries-%version.tar
Source25: rx-%version.tar
Source26: xunit-binaries-%version.tar

Patch1: %name-alt-linking1.patch
Patch2: %name-alt-linking2.patch
Patch3: %name-alt-monodoc-sourcesdir.patch
Patch4: %name-alt-mcs-no-parallel-build.patch
Patch5: %name-upstream-crash-Use-safer-invalid-free-test-12864.patch

BuildRequires(pre): rpm-build-mono >= 2.0
BuildRequires(pre): rpm-build-ubt
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gettext-devel
BuildRequires: libgdiplus-devel >= 2.10
BuildRequires: pkg-config
BuildRequires: valgrind-devel
BuildRequires: zlib-devel
BuildRequires: python-modules-json
BuildRequires: perl-Pod-Usage

# http://www.mono-project.com/docs/about-mono/releases/4.0.0/#npgsql
#Obsoletes: mono-data-postgresql
# http://www.mono-project.com/docs/about-mono/releases/4.0.0/#entityframework
# Obsoletes: mono-entityframework

# Yes, mono actually depends on itself, because
# we deleted the bootstrapping binaries. If you
# need to bootstrap mono, comment out this BuildRequires
# and don't delete the binaries in %%prep.

%if_enabled bootstrap
# for bootstrap, use bundled monolite instead of local mono
%else
BuildRequires: %name-devel-full >= 5.0
%endif

# Interfaces of slightly older versions are required, upstream corrects it by modifying 'Requires'
%define __find_provides sh -c '/usr/lib/rpm/find-provides | sort | uniq'
%define __find_requires sh -c '/usr/lib/rpm/find-requires | sort | uniq | grep ^... | \
	sed "s/mono\(Mono.Cecil\).*/mono\(Mono.Cecil\) = 0.10.3.0/" | \
	sed "s/mono\(System.Collections.Immutable\).*/mono\(System.Collections.Immutable\) = 1.2.1.0/" | \
	sed "s/mono\(System.IO.Compression\).*/mono\(System.IO.Compression\) = 4.0.0.0/" | \
	sed "s/mono\(System.Security.Cryptography.Algorithms\).*/mono\(System.Security.Cryptography.Algorithms\) = 4.3.1.0/" | \
	sed "s/mono\(System.Text.Encoding.CodePages\).*/mono\(System.Text.Encoding.CodePages\) = 4.1.0.0/" | \
	sed "s/mono\(System.ValueTuple\).*/mono\(System.ValueTuple\) = 4.0.3.0/" | \
	sed "s/mono\(System.Xml.XPath.XDocument\).*/mono\(System.Xml.XPath.XDocument\) = 4.1.1.0/" | \
	sed "s/mono\(System.Diagnostics.StackTrace\).*/mono\(System.Diagnostics.StackTrace\) = 4.1.1.0/" | \
	sed "/mono\(System.Runtime.Loader\).*/d"'

%description
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine (as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

%package core
Summary: The Mono CIL runtime, suitable for running .NET code
Group: Development/Other
Requires: /proc
Requires: ca-certificates
Conflicts: mono4-core < %EVR
Conflicts: mono < 3.0
Conflicts: mono-mscorlib  < 3.0
Conflicts: monodis < 3.0
Conflicts: libmono < 3.0
Obsoletes: mono4-core
Provides: mono4-core = %EVR

%description core
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,
I18N, Cairo and Mono.*).

%package winfx
Summary: Mono implementation of core WinFX APIs
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-winfx < %EVR
Obsoletes: mono4-winfx
Provides: mono4-winfx = %EVR

%description winfx
Open source implementation of core WinFX APIs

%package mvc
Summary: Mono implementation of ASP.NET MVC
Group: Development/Other
Requires: %name-dyndata = %EVR
Conflicts: mono4-mvc < %EVR
Obsoletes: mono4-mvc
Provides: mono4-mvc = %EVR

%description mvc
This is the Mono implementation of ASP.NET MVC

%package mvc-devel
Summary: Development files for  ASP.NET MVC
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-mvc-devel < %EVR
Obsoletes: mono4-mvc-devel
Provides: mono4-mvc-devel = %EVR


%description mvc-devel
This is the Mono implementation of ASP.NET MVC

%package dyndata
Summary: Dynamic data dll for both web and mvc
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-dyndata < %EVR
Obsoletes: mono4-dyndata
Provides: mono4-dyndata = %EVR

%description dyndata
This is dll needed for implementation of ASP.NET MVC and for web services too

%package full
Summary: full runtime virtual package
Group: Development/Other
Requires: %name-dyndata = %EVR
Requires: %name-data = %EVR
Requires: %name-mvc = %EVR
Requires: %name-extras = %EVR
Requires: %name-winfx = %EVR
Requires: %name-locale-extras = %EVR
Requires: %name-reactive = %EVR
Requires: %name-reactive-winforms = %EVR
Requires: %name-wcf = %EVR
Requires: %name-winforms = %EVR
Requires: %name-data-oracle = %EVR
Requires: %name-data-sqlite = %EVR
%if_enabled ibmlibs
Requires: %name-ibm-data-db2 = %EVR
%endif
Requires: %name-monodoc = %EVR
Requires: %name-mono2-compat = %EVR
Conflicts: mono4-full < %EVR
Obsoletes: mono4-full
Provides: mono4-full = %EVR

%description full
Virtual package containing all non-devel packages from mono

%package devel-full
Summary: full development virtual package
Group:Development/Other
Requires: %name-devel = %EVR
Requires: %name-full = %EVR
Requires: %name-reactive-devel = %EVR
Requires: %name-web-devel = %EVR
Requires: %name-mvc-devel = %EVR
Requires: %name-monodoc-devel = %EVR
Requires: %name-nunit = %EVR
Requires: %name-mono2-compat-devel = %EVR
Conflicts: mono4-devel-full < %EVR
Obsoletes: mono4-devel-full
Provides: mono4-devel-full = %EVR
%qIF_ver_lt %ubt_id S1
Conflicts: %name-nunit-devel < %EVR
Obsoletes: %name-nunit-devel
Provides: %name-nunit-devel = %EVR
%endif

%description devel-full
Virtual package containing all devel packages from mono

%package devel
Summary: Development tools for Mono
Group: Development/Other
Requires: %name-core = %EVR
Requires: pkg-config
Requires: glib2-devel
Conflicts: mono4-devel < %EVR
Obsoletes: mono4-devel
Provides: mono4-devel = %EVR
%qIF_ver_lt %ubt_id S1
Conflicts: mono-mcs < %EVR
Provides: mono-mcs = %EVR
Obsoletes: mono-mcs
Requires: rpm-build-mono
%endif

%description devel
This package completes the Mono developer toolchain with the mono profiler,
assembler and other various tools.

%package locale-extras
Summary: Extra locale information for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-locale-extras < %EVR
Obsoletes: mono4-locale-extras
Provides: mono4-locale-extras = %EVR

%description locale-extras
This package contains assemblies to support I18N applications for
non-latin alphabets.

%package extras
Summary: Provides the infrastructure for running and building daemons and services with Mono as well as various stub assemblies
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-extras < %EVR
Obsoletes: mono4-extras
Provides: mono4-extras = %EVR

%description extras
This package provides the library and application to run services
and daemons with Mono. It also includes stubs for the following
assemblies: Microsoft.Vsa,
System.Configuration.Install, System.Management, System.Messaging.

%package reactive
License: MIT License (or similar) ; Apache License 2.0
Summary: Reactive Extensions for Mono core libraries
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-reactive < %EVR
Obsoletes: mono4-reactive
Provides: mono4-reactive = %EVR

%description reactive
Reactive Extensions for Mono, this packages don't depend on
desktop-specific features.

%package reactive-winforms
License: MIT License (or similar) ; Apache License 2.0
Summary: Reactive Extensions for Mono desktop-specific libraries
Group: Development/Other
Requires: %name-core = %EVR
Requires: %name-reactive = %EVR
Conflicts: mono4-reactive-winforms < %EVR
Obsoletes: mono4-reactive-winforms
Provides: mono4-reactive-winforms = %EVR

%description reactive-winforms
Reactive Extensions for Mono, desktop-specific packages (winforms,
windows threading).

%package reactive-devel
Summary: Development files for system.web
Group: Development/Other
Requires: %name-core = %EVR
Requires: %name-reactive = %EVR
Requires: pkg-config
Conflicts: mono4-reactive-devel < %EVR
Obsoletes: mono4-reactive-devel
Provides: mono4-reactive-devel = %EVR

%description reactive-devel
This package provides the .pc file for %name-rx

%package winforms
Summary: Windows Forms implementation for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-winforms < %EVR
Obsoletes: mono4-winforms
Provides: mono4-winforms = %EVR

%description winforms
This package provides a fully managed implementation of
System.Windows.Forms, the default graphical toolkit for .NET
applications.

%package wcf
Summary: Mono implementation of Windows Communication Foundation
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-wcf < %EVR
Obsoletes: mono4-wcf
Provides: mono4-wcf = %EVR

%description wcf
This package provides an implementation of WCF, the Windows Communication
Foundation.

%package web
Summary: ASP.NET, Remoting, and Web Services for Mono
Group: Development/Other
Requires: %name-dyndata = %EVR
Conflicts: mono4-web < %EVR
Obsoletes: mono4-web
Provides: mono4-web = %EVR

%description web
This package provides the ASP.NET libraries and runtime for
development of web application, web services and remoting support.

%package web-devel
Summary: Development files for system.web
Group: Development/Other
Requires: %name-core = %EVR
Requires: %name-web = %EVR
Requires: pkg-config
Conflicts: mono4-web-devel < %EVR
Obsoletes: mono4-web-devel
Provides: mono4-web-devel = %EVR

%description web-devel
This package provides the .pc file for %name-web

%package data
Summary: Database connectivity for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-data < %EVR
Obsoletes: mono4-data
Provides: mono4-data = %EVR

%description data
This package provides a Mono assembly to facilitate data access
and manipulation with databases, LDAP compatible directory servers
and/or XML data exchange. Beyond the ADO.NET, Novell.LDAP and
System.DirectoryServices assemblies, it also includes a command
line sql application as well as the Microsoft SQL Server and ODBC
data providers.

%package data-sqlite
Summary: sqlite database connectivity for Mono
Group: Development/Other
Requires: %name-core = %EVR
Requires: sqlite
Conflicts: mono4-data-sqlite < %EVR
Obsoletes: mono4-data-sqlite
Provides: mono4-data-sqlite = %EVR

%description data-sqlite
This package contains the ADO.NET Data provider for the sqlite
database.

%package data-oracle
Summary: Oracle database connectivity for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-data-oracle < %EVR
Obsoletes: mono4-data-oracle
Provides: mono4-data-oracle = %EVR

%description data-oracle
This package contains the ADO.NET Data provider for the Oracle
database.

%if_enabled ibmlibs
%package   ibm-data-db2
Summary: IBM DB2 database connectivity for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-ibm-data-db2 < %EVR
Obsoletes: mono4-ibm-data-db2
Provides: mono4-ibm-data-db2 = %EVR

%description ibm-data-db2
This package contains the ADO.NET Data provider for the IBM DB2
Universal database.
%endif

%package monodoc
Summary: The %name documentation system
Group: Documentation
Requires: %name-core = %EVR
Conflicts: mono4-monodoc < %EVR
Obsoletes: mono4-monodoc
Provides: mono4-monodoc = %EVR
%qIF_ver_lt %ubt_id S1
Conflicts: monodoc < %EVR
Provides: monodoc = %EVR
Obsoletes: monodoc
%endif

%description monodoc
monodoc is the documentation package for the mono .NET environment

%package  monodoc-devel
Summary: .pc file for monodoc
Group: Documentation
Requires: %name-core = %EVR
Requires: %name-monodoc = %EVR
Requires: pkg-config
Conflicts: mono4-monodoc-devel < %EVR
Obsoletes: mono4-monodoc-devel
Provides: mono4-monodoc-devel = %EVR
%qIF_ver_lt %ubt_id S1
Conflicts: monodoc-devel < %EVR
Provides: monodoc-devel = %EVR
Obsoletes: monodoc-devel
%endif

%description monodoc-devel
Development file for monodoc

%package nunit
Summary:        NUnit Testing Framework
Group:          Development/Other
Requires:       mono-core = %EVR

%description nunit
NUnit is a unit-testing framework for all .Net languages.  Initially
ported from JUnit, the current release, version 2.2,  is the fourth
major release of this  Unit based unit testing tool for Microsoft .NET.
It is written entirely in C# and  has been completely redesigned to
take advantage of many .NET language		 features, for example
custom attributes and other reflection related capabilities. NUnit
brings xUnit to all .NET languages.

%package mono2-compat
Summary:        A Library for embedding Mono in your Application
Requires:       %name-core = %EVR
Group:          Development/Other

%description mono2-compat
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

A Library for embedding Mono in your Application.

%package mono2-compat-devel
Summary:        Development files for libmono
Group:          Development/Other
Requires:       %name-mono2-compat = %EVR
Requires:       %name-core = %EVR

%description mono2-compat-devel
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Development files for libmono.

%define gac_dll(dll)  %_monogacdir/%1 \
%_monodir/4.5/%1.dll \
%nil
%define mono_bin(bin) %_bindir/%1 \
%_monodir/4.5/%1.exe \
%_monodir/4.5/%1.pdb \
%nil
%define dll_so(dll) \
%_monodir/4.5/%1.dll \
%_monodir/4.5/%1.dll.so \
%nil

%prep
%setup

pushd external/Newtonsoft.Json                         ; tar xf %SOURCE5  --strip-components=1 ; popd
pushd external/api-doc-tools                           ; tar xf %SOURCE6  --strip-components=1 ; popd
pushd external/api-doc-tools/external/Lucene.Net.Light ; tar xf %SOURCE7  --strip-components=1 ; popd
pushd external/api-doc-tools/external/SharpZipLib      ; tar xf %SOURCE8  --strip-components=1 ; popd
pushd external/api-snapshot                            ; tar xf %SOURCE9  --strip-components=1 ; popd
pushd external/aspnetwebstack                          ; tar xf %SOURCE10 --strip-components=1 ; popd
pushd external/binary-reference-assemblies             ; tar xf %SOURCE11 --strip-components=1 ; popd
pushd external/bockbuild                               ; tar xf %SOURCE12 --strip-components=1 ; popd
pushd external/boringssl                               ; tar xf %SOURCE13 --strip-components=1 ; popd
pushd external/cecil                                   ; tar xf %SOURCE14 --strip-components=1 ; popd
pushd external/cecil-legacy                            ; tar xf %SOURCE15 --strip-components=1 ; popd
pushd external/corefx                                  ; tar xf %SOURCE16 --strip-components=1 ; popd
pushd external/corert                                  ; tar xf %SOURCE17 --strip-components=1 ; popd
pushd external/ikdasm                                  ; tar xf %SOURCE18 --strip-components=1 ; popd
pushd external/ikvm                                    ; tar xf %SOURCE19 --strip-components=1 ; popd
pushd external/linker                                  ; tar xf %SOURCE20 --strip-components=1 ; popd
pushd external/linker/cecil                            ; tar xf %SOURCE21 --strip-components=1 ; popd
pushd external/nuget-buildtasks                        ; tar xf %SOURCE22 --strip-components=1 ; popd
pushd external/nunit-lite                              ; tar xf %SOURCE23 --strip-components=1 ; popd
pushd external/roslyn-binaries                         ; tar xf %SOURCE24 --strip-components=1 ; popd
pushd external/rx                                      ; tar xf %SOURCE25 --strip-components=1 ; popd
pushd external/xunit-binaries                          ; tar xf %SOURCE26 --strip-components=1 ; popd

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%if_enabled bootstrap
mkdir -p mcs/class/lib/monolite-linux
pushd mcs/class/lib/monolite-linux
tar xzf %SOURCE3
monolitename="$(tar tzf %SOURCE3 | head -n 1 | sed -e 's:/$::')"
if [ -n "$monolitename" ] ; then
    mv "$monolitename" "$(echo "$monolitename" | sed -e 's:monolite-linux-::' -e 's:-latest::')"
fi
popd
%endif

# fix imports, otherwise dependencies on devel packages are created
find . -type f -iname '*.cs' -print0 | xargs -0 \
    sed -i \
        -e 's:"libgdk-x11-2.0.so":"libgdk-x11-2.0.so.0":g' \
        -e 's:"libgdk_pixbuf-2.0.so":"libgdk_pixbuf-2.0.so.0":g' \
        -e 's:"libgobject-2.0.so":"libgobject-2.0.so.0":g' \
        -e 's:"libgtk-x11-2.0.so":"libgtk-x11-2.0.so.0":g' \
        -e 's:"libgmodule-2.0.so":"libgmodule-2.0.so.0":g' \
        -e 's:"libglib-2.0.so":"libglib-2.0.so.0":g'

# modifications for Mono 4
%__subst "s#mono/2.0#mono/4.5#g" data/mono-nunit.pc.in

%if_enabled bootstrap
export PATH=$PATH:mcs/class/lib/monolite-linux/
%endif

%build
%add_optflags -fno-strict-aliasing

NOCONFIGURE=yes sh ./autogen.sh
%configure --disable-rpath \
           --with-moonlight=no \
           --with-spectre-mitigation=yes \
           --enable-dynamic-btls

%make

%install
%if_enabled bootstrap
export PATH=$PATH:mcs/class/lib/monolite-linux/
%endif

%makeinstall_std

# copy the mono.snk key into /etc/pki/mono
mkdir -p %buildroot%_sysconfdir/pki/mono
install -p -m0644 %SOURCE2 %buildroot%_sysconfdir/pki/mono/

# C5 is not installed, see commit 0af35dd5

# remove Windows-only stuff
rm -rfv %buildroot%_monodir/*/Mono.Security.Win32*
rm -fv %buildroot%_libdir/libMonoSupportW.*
# remove libgc cruft
rm -rfv %buildroot%_datadir/libgc-mono
# remove stuff that we don't package*
rm -fv %buildroot%_man1dir/cilc.1*
rm -fv %buildroot%_man1dir/mdb2ppdb.1*
rm -fv %buildroot%_monodir/*/browsercaps-updater.*
rm -fv %buildroot%_monodir/*/culevel.*

rm -fv %buildroot%_monodir/*/mscorlib.dll.so
rm -fv %buildroot%_monodir/*/mcs.exe.so
rm -rfv %buildroot%_bindir/mono-configuration-crypto
rm -rfv %buildroot%_mandir/man?/mono-configuration-crypto*

%if_disabled ibmlibs
rm -rfv %buildroot%_monogacdir/IBM.Data.DB2
rm -fv %buildroot%_monodir/4.5/IBM.Data.DB2.dll
%endif

rm -fv %buildroot%_monodir/4.5/mono-shlib-cop.exe.config
rm -fv %buildroot%_monodir/4.5/sqlmetal.exe.config
rm -fv %buildroot%_monodir/4.5/xbuild.exe.config

rm -fv %buildroot%_libdir/libmono-2.0.a
rm -fv %buildroot%_libdir/libmono-2.0.la
rm -fv %buildroot%_libdir/libmonoboehm-2.0.a
rm -fv %buildroot%_libdir/libmonosgen-2.0.a
rm -rfv %buildroot%_libdir/mono/lldb
rm -rfv %buildroot%_datadir/mono-2.0/mono/profiler

mkdir -p  %buildroot%_sysconfdir/mono-2.0/
mkdir -p  %buildroot%_sysconfdir/mono-4.5/
mkdir -p  %buildroot%_sysconfdir/mono-4.0/
mkdir -p  %buildroot%_monodir/3.5-api/
mkdir -p  %buildroot%_monodir/2.0-api/
mkdir -p  %buildroot%_monodir/4.0-api/
mkdir -p  %buildroot%_monodir/4.5-api/

# install file trigger
install -pD -m755 %SOURCE4 %buildroot%_rpmlibdir/mono-cert-sync.filetrigger

%qIF_ver_lt %ubt_id S1
ln -s mcs %buildroot%_bindir/gmcs
%endif

%find_lang mcs


%files core -f mcs.lang
%qIF_ver_lt %ubt_id S1
%_bindir/gmcs
%endif
%doc .github/CONTRIBUTING.md LICENSE COPYING.LIB NEWS README.md PATENTS.TXT
%_rpmlibdir/mono-cert-sync.filetrigger
%_sysconfdir/mono-4.5/
%_sysconfdir/mono-4.0/
%dir %_sysconfdir/mono/4.5/
%dir %_monodir
%dir %_monodir/4.5
%dir %_monodir/4.0
%_bindir/mono
%_bindir/mono-test-install
%_bindir/mono-gdb.py
%ifarch %ix86 x86_64 armh
%_bindir/mono-boehm
%endif
%_bindir/mono-service2
%_bindir/mono-sgen
%_bindir/mono-sgen-gdb.py
%mono_bin csharp
%mono_bin cert-sync
%mono_bin certmgr
%mono_bin chktrust
%mono_bin gacutil
%mono_bin ikdasm
%mono_bin lc
%_bindir/gacutil2
%mono_bin mcs
%mono_bin mozroots
%mono_bin pdb2mdb
%mono_bin setreg
%mono_bin sn
%_bindir/csc
%_bindir/csc-dim
%_monodir/4.5/csc.*
%_monodir/4.5/dim
%_bindir/mono-heapviz
%_bindir/mprof-report
%_man1dir/certmgr.1*
%_man1dir/chktrust.1*
%_man1dir/gacutil.1*
%_man1dir/mcs.1*
%_man1dir/mono.1*
%_man1dir/mozroots.1*
%_man1dir/setreg.1*
%_man1dir/sn.1*
%_man5dir/mono-config.5*
%_man1dir/csharp.1*
%_man1dir/pdb2mdb.1*
%_man1dir/lc.1*
%_man1dir/mprof-report.1*
%_man1dir/cert-sync.1*
%_libdir/libMonoPosixHelper.so*
%_libdir/*profiler*.so.*
%_libdir/libmono-btls-shared.so*
%_libdir/libmono-native.so.*
%_monodir/4.0/Mono.Posix.dll
%_monodir/4.0/mscorlib.dll


%dir %_monodir/gac
%gac_dll Commons.Xml.Relaxng
%gac_dll ICSharpCode.SharpZipLib
%gac_dll Mono.Debugger.Soft
%_monogacdir/Mono.Cecil
%gac_dll cscompmgd
%gac_dll Microsoft.VisualC
%gac_dll Mono.Cairo
%gac_dll Mono.CompilerServices.SymbolWriter
%gac_dll Mono.CSharp
%gac_dll System.Drawing
%gac_dll Mono.Management
%gac_dll Mono.Posix
%gac_dll Mono.Security
%gac_dll Mono.Simd
%gac_dll System
%gac_dll System.Configuration
%gac_dll System.Core
%gac_dll System.Security
%gac_dll System.Xml
%gac_dll System.Deployment
%gac_dll System.Reflection.Context
%gac_dll Mono.Tasklets
%gac_dll System.Net
%gac_dll System.Xml.Linq
%gac_dll SMDiagnostics
%dir %_sysconfdir/mono
%dir %_sysconfdir/mono/mconfig
%config (noreplace) %_sysconfdir/mono/config
%config (noreplace) %_sysconfdir/mono/4.5/settings.map
%config (noreplace) %_sysconfdir/mono/4.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %_sysconfdir/mono/4.5/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %_sysconfdir/mono/4.5/machine.config
%config (noreplace) %_sysconfdir/mono/4.5/web.config
%config (noreplace) %_sysconfdir/mono/4.0/machine.config
%config (noreplace) %_sysconfdir/mono/4.0/web.config
%config (noreplace) %_sysconfdir/mono/4.0/settings.map
%dir %_sysconfdir/mono/4.0
%_bindir/dmcs
%mono_bin ccrewrite
%_man1dir/ccrewrite.1*
%dir %_monodir/4.5/Facades

%_monodir/4.5/mscorlib.dll
%_monodir/4.5/mscorlib.pdb
%gac_dll Microsoft.CSharp
%gac_dll System.Dynamic
%gac_dll System.ComponentModel.Composition
%gac_dll System.Numerics
%gac_dll System.Runtime.DurableInstancing
%gac_dll Mono.CodeContracts

%dir %_monodir/mono-configuration-crypto/
%dir %_monodir/mono-configuration-crypto/4.5/
%_monodir/mono-configuration-crypto/4.5/*
%gac_dll CustomMarshalers
%gac_dll I18N.West
%gac_dll I18N
%gac_dll System.Json
%gac_dll Mono.Parallel
%gac_dll System.Json.Microsoft
%_monodir/4.5/Facades/*.dll
%_monodir/4.5/Facades/*.pdb
%gac_dll System.IO.Compression
%gac_dll System.IO.Compression.FileSystem
%gac_dll System.Net.Http
%gac_dll System.Net.Http.WebRequest
%gac_dll System.Threading.Tasks.Dataflow
%gac_dll System.Numerics.Vectors
%gac_dll System.ServiceModel.Internals
%exclude %_monodir/4.5/System.Runtime.Caching.dll
%exclude %_monodir/4.5/System.Xaml.dll
%exclude %_monogacdir/System.Runtime.Caching/*
%exclude %_monogacdir/System.Xaml/*
%exclude %_sysconfdir/mono/4.0/Browsers/Compat.browser
%dir %_monodir/gac/Mono.Btls.Interface
%_monodir/gac/Mono.Btls.Interface/*
%_monodir/4.5/Mono.Btls.Interface.dll
%dll_so Microsoft.CodeAnalysis
%dll_so Microsoft.CodeAnalysis.CSharp
%dll_so System.Collections.Immutable
%dll_so System.Reflection.Metadata

%_libdir/libmonosgen-2.0.so.*
%ifarch %ix86 x86_64 armh
%_libdir/libmonoboehm-2.0.so.*
%endif
%_monodir/4.0-api
%_monodir/4.5-api
%_monodir/4.6-api
%_monodir/4.7-api

%post core
cert-sync %_sysconfdir/pki/tls/certs/ca-bundle.crt

%files dyndata
%gac_dll System.Web.DynamicData

%files full

%files devel-full

%files devel
%_sysconfdir/pki/mono/
%mono_bin mono-api-info
%mono_bin illinkanalyzer
%_bindir/mono-package-runtime
%_bindir/monograph
%_bindir/sgen-grep-binprot
%_bindir/csi
%_monodir/4.5/mono-api-diff.exe
%_monodir/4.5/mono-api-diff.pdb
%_monodir/4.5/csi.*
%_bindir/vbc
%_monodir/4.5/vbc.*
%_monodir/4.5/VBCSCompiler.*
%_monodir/4.5/mono-symbolicate.exe
%_monodir/4.5/mono-symbolicate.pdb
%_monodir/4.5/Microsoft.CodeAnalysis.CSharp.Scripting.dll
%_monodir/4.5/Microsoft.CodeAnalysis.Scripting.dll
%_monodir/4.5/Microsoft.CodeAnalysis.VisualBasic.dll
%_monodir/2.0-api/*
%_monodir/3.5-api/*
%_monodir/4.5.1-api/*
%_monodir/4.5.2-api/*
%_monodir/4.6.1-api/*
%_monodir/4.6.2-api/*
%_monodir/4.7.1-api/*
%_monodir/4.7.2-api/*
%_monodir/msbuild/15.0/bin/Roslyn
%_bindir/mono-symbolicate
%mono_bin xbuild
%_monodir/4.5/xbuild.rsp
%mono_bin genxs
%_monodir/4.5/ictool*
%_monodir/4.5/mod*
%mono_bin al
%_bindir/al2
%mono_bin caspol
%mono_bin cert2spc
%mono_bin dtd2rng
%mono_bin dtd2xsd
%mono_bin ilasm
%mono_bin installvst
%_monodir/4.5/installutil*
%mono_bin macpack
%mono_bin mkbundle
%mono_bin makecert
%mono_bin mono-cil-strip
%_bindir/mono-find-provides
%_bindir/mono-find-requires
%_bindir/monodis
%mono_bin monolinker
%mono_bin mono-shlib-cop
%mono_bin mono-xmltool
%mono_bin monop
%_bindir/monop2
%mono_bin permview
%_bindir/peverify
%mono_bin resgen
%_bindir/resgen2
%mono_bin sgen
%mono_bin secutil
%mono_bin signcode
%mono_bin cccheck
%mono_bin crlupdate
%mono_bin mdbrebase
%_libexecdir/mono-source-libs/
%_bindir/pedump
%_man1dir/resgen.1*
%_man1dir/al.1*
%_man1dir/cert2spc.1*
%_man1dir/dtd2xsd.1*
%_man1dir/genxs.1*
%_man1dir/ilasm.1*
%_man1dir/macpack.1*
%_man1dir/makecert.1*
%_man1dir/mkbundle.1*
%_man1dir/mono-cil-strip.1*
%_man1dir/monodis.1*
%_man1dir/monolinker.1*
%_man1dir/mono-profilers.1*
%_man1dir/mono-shlib-cop.1*
%_man1dir/mono-xmltool.1*
%_man1dir/monop.1*
%_man1dir/permview.1*
%_man1dir/secutil.1*
%_man1dir/sgen.1*
%_man1dir/signcode.1*
%_man1dir/xbuild.1*
%_man1dir/mono-api-info.1*
%_man1dir/cccheck.1*
%_man1dir/crlupdate.1*
%_man1dir/illinkanalyzer.1*
%gac_dll PEAPI
%gac_dll Microsoft.Build
%gac_dll Microsoft.Build.Engine
%gac_dll Microsoft.Build.Framework
%_monogacdir/Microsoft.Build.Tasks.Core
%gac_dll Microsoft.Build.Tasks.v4.0
%gac_dll Microsoft.Build.Utilities.v4.0
%_monogacdir/Microsoft.Build.Utilities.Core
%_monogacdir/Microsoft.Build.Tasks.v12.0
%_monogacdir/Microsoft.Build.Utilities.v12.0
%gac_dll Mono.Profiler.Log
%gac_dll Mono.XBuild.Tasks
%gac_dll System.Windows
%gac_dll System.Xml.Serialization
%_monodir/4.5/Microsoft.Common.tasks
%_monodir/4.5/MSBuild/Microsoft.Build*
%_monodir/4.5/Microsoft.Build.xsd
%_monodir/4.5/Microsoft.CSharp.targets
%_monodir/4.5/Microsoft.Common.targets
%_monodir/4.5/Microsoft.VisualBasic.targets
%_monodir/xbuild/
%_monodir/xbuild-frameworks/
%_libdir/libikvm-native.so
%_libdir/libmonosgen-2.0.so
%ifarch %ix86 x86_64 armh
%_libdir/libmonoboehm-2.0.so
%endif
%_libdir/libMonoPosixHelper.a
%_libdir/*profiler*.so
%_libdir/*profiler*.a
%_libdir/libikvm-native.a
%_libdir/libmono-native.so
%_libdir/libmono-native.a
%_pkgconfigdir/dotnet.pc
%_pkgconfigdir/mono-cairo.pc
%_pkgconfigdir/mono.pc
%_pkgconfigdir/monosgen-2.pc
%_pkgconfigdir/cecil.pc
%_pkgconfigdir/dotnet35.pc
%_pkgconfigdir/mono-lineeditor.pc
%_pkgconfigdir/mono-options.pc
%_pkgconfigdir/wcf.pc
%_pkgconfigdir/xbuild12.pc

%files locale-extras
%gac_dll I18N.CJK
%gac_dll I18N.MidEast
%gac_dll I18N.Other
%gac_dll I18N.Rare

%files extras
%mono_bin mono-service
%_monogacdir/mono-service
%gac_dll System.Configuration.Install
%gac_dll System.Management
%gac_dll System.Messaging
%gac_dll System.ServiceProcess
%gac_dll System.Runtime.Caching
%gac_dll System.Xaml
%gac_dll Mono.Messaging.RabbitMQ
%gac_dll Mono.Messaging
%gac_dll RabbitMQ.Client
%_monodir/4.5/RabbitMQ.Client.Apigen*
%_man1dir/mono-service.1*

%files reactive
%gac_dll System.Reactive.Core
%gac_dll System.Reactive.Debugger
%gac_dll System.Reactive.Experimental
%gac_dll System.Reactive.Interfaces
%gac_dll System.Reactive.Linq
%gac_dll System.Reactive.Observable.Aliases
%gac_dll System.Reactive.PlatformServices
%gac_dll System.Reactive.Providers
%gac_dll System.Reactive.Runtime.Remoting

%files reactive-winforms
%gac_dll System.Reactive.Windows.Forms
%gac_dll System.Reactive.Windows.Threading

%files reactive-devel
%_pkgconfigdir/reactive.pc

%files wcf
%gac_dll System.IdentityModel
%gac_dll System.IdentityModel.Selectors
%gac_dll System.ServiceModel
%gac_dll System.ServiceModel.Activation
%gac_dll System.ServiceModel.Discovery
%gac_dll System.ServiceModel.Routing
%gac_dll System.ServiceModel.Web

%files web
%mono_bin disco
%mono_bin httpcfg
%mono_bin mconfig
%mono_bin soapsuds
%mono_bin svcutil
%mono_bin wsdl
%_bindir/wsdl2
%mono_bin xsd
%mono_bin mono-api-html
%gac_dll Microsoft.Web.Infrastructure
%gac_dll Mono.Http
%gac_dll System.ComponentModel.DataAnnotations
%gac_dll System.Net.Http.Formatting
%gac_dll System.Runtime.Remoting
%gac_dll System.Runtime.Serialization.Formatters.Soap
%gac_dll System.Web
%gac_dll System.Web.Abstractions
%gac_dll System.Web.Routing
%gac_dll System.Web.Services
%gac_dll System.Web.ApplicationServices
%gac_dll System.Web.Http
%gac_dll System.Web.Http.SelfHost
%gac_dll System.Web.Http.WebHost
%gac_dll System.Web.Razor
%gac_dll System.Web.WebPages
%gac_dll System.Web.WebPages.Deployment
%gac_dll System.Web.WebPages.Razor
%gac_dll System.Web.Mobile
%gac_dll System.Web.RegularExpressions
%gac_dll System.Workflow.Activities
%gac_dll System.Workflow.ComponentModel
%gac_dll System.Workflow.Runtime

%_man1dir/disco.1*
%_man1dir/httpcfg.1*
%_man1dir/mconfig.1*
%_man1dir/soapsuds.1*
%_man1dir/wsdl.1*
%_man1dir/xsd.1*
%config (noreplace) %_sysconfdir/mono/browscap.ini
%config (noreplace) %_sysconfdir/mono/2.0/Browsers/Compat.browser
%config (noreplace) %_sysconfdir/mono/4.0/Browsers/Compat.browser
%config (noreplace) %_sysconfdir/mono/4.5/Browsers/Compat.browser
%config (noreplace) %_sysconfdir/mono/2.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %_sysconfdir/mono/mconfig/config.xml

%files web-devel
%_pkgconfigdir/aspnetwebstack.pc

%files winforms
%gac_dll Accessibility
%gac_dll Mono.WebBrowser
%gac_dll System.Design
%gac_dll System.Drawing.Design
%gac_dll System.Windows.Forms
%gac_dll System.Windows.Forms.DataVisualization

%files mvc
%gac_dll System.Web.Extensions
%gac_dll System.Web.Extensions.Design
%gac_dll System.Web.Mvc

%files mvc-devel
%_pkgconfigdir/system.web.extensions.design_1.0.pc
%_pkgconfigdir/system.web.extensions_1.0.pc
%_pkgconfigdir/system.web.mvc.pc
%_pkgconfigdir/system.web.mvc2.pc
%_pkgconfigdir/system.web.mvc3.pc

%files winfx
%gac_dll WindowsBase

%files data
%mono_bin sqlsharp
%mono_bin sqlmetal
%gac_dll System.Data
%gac_dll System.Data.DataSetExtensions
%gac_dll System.Data.Entity
%gac_dll System.Data.Linq
%gac_dll System.Data.Services
%gac_dll System.Data.Services.Client
%gac_dll System.DirectoryServices
%gac_dll System.DirectoryServices.Protocols
%gac_dll System.EnterpriseServices
%gac_dll System.Runtime.Serialization
%gac_dll System.Transactions
%gac_dll Mono.Data.Tds
%gac_dll Novell.Directory.Ldap
%gac_dll WebMatrix.Data
%_man1dir/sqlsharp.1*

%files data-sqlite
%gac_dll Mono.Data.Sqlite

%files data-oracle
%gac_dll System.Data.OracleClient

%if_enabled ibmlibs
%files  ibm-data-db2
%gac_dll IBM.Data.DB2
%endif

%files monodoc
%_monogacdir/monodoc
%_monodir/monodoc/*
%ifnarch  ppc
%_datadir/monodoc
%endif
%mono_bin mdoc
%_bindir/mod
%_bindir/mdoc-*
%_bindir/mdass*
%_bindir/mdval*
%_bindir/monodoc*
%_man1dir/monodocer.1*
%_man5dir/mdoc.5*
%_man1dir/mdoc-*
%_man1dir/mdoc.1.*
%_man1dir/mdassembler*
%_man1dir/monodocs2html.1*
%_man1dir/mdvalidater.1*
%_man1dir/mono-symbolicate.1*

%files  monodoc-devel
%_pkgconfigdir/monodoc.pc

%files nunit
%_pkgconfigdir/mono-nunit.pc
%_bindir/nunit-console
%_bindir/nunit-console2
%_bindir/nunit-console4
%_monodir/4.5/nunit-console.exe
%_monodir/4.5/nunit-console.exe.config
%_monodir/4.5/nunit-console.pdb
%gac_dll nunit-console-runner
%gac_dll nunit.core
%gac_dll nunit.core.extensions
%gac_dll nunit.core.interfaces
%gac_dll nunit.framework
%gac_dll nunit.framework.extensions
%gac_dll nunit.mocks
%gac_dll nunit.util

%files mono2-compat
%_sysconfdir/mono-2.0/
%dir %_sysconfdir/mono/2.0
%config (noreplace) %_sysconfdir/mono/2.0/machine.config
%config (noreplace) %_sysconfdir/mono/2.0/settings.map
%config (noreplace) %_sysconfdir/mono/2.0/web.config
%_libdir/libmono-2.0.so.1*

%files mono2-compat-devel
%_includedir/mono-2.0
%_datadir/mono-2.0
%_libdir/libmono-2.0.so
%_pkgconfigdir/mono-2.pc

%changelog
* Tue May 28 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.20.1.19-alt2
- Rebuilt with patch from upstream pull request #12864.

* Mon Apr 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.20.1.19-alt1
- Updated to upstream version 5.20.1.19.

* Thu Jan 24 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.18.0.240-alt1
- Updated to upstream version 5.18.0.240.

* Mon Oct 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.14.0.177-alt1
- Updated to upstream version 5.14.0.177.

* Wed May 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.10.0.157-alt4
- Updated interpackage dependencies.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.10.0.157-alt3
- Fixed build on some architectures.

* Fri Apr 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.10.0.157-alt2
- Updated interpackage dependencies.

* Fri Mar 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.10.0.157-alt1
- Updated to upstream version 5.10.0.157.

* Mon Sep 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt8
- Updated provides.
- Fixed monodoc directory.

* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt7
- Added file trigger to run cert-sync tool on certificates update.

* Fri Sep 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt6
- Rebuilt with support of %%ubt macro.

* Fri Jul 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt5
- Fixed unresolved symbols
- Added post-install action for mono-core to import certificates

* Wed Jul 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt4
- Installed msbuild config files

* Mon Jul 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt3
- Fixed circular dependency between mono-core and mono-devel
- Packaged mono-2 parts

* Mon Jul 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt2
- Updated package metadata

* Wed Jul 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt1
- Updated to stable upstream release version 5.0.1.1

* Tue Nov 22 2016 Denis Medvedev <nbr@altlinux.org> 4.6.2.7-alt4
- fix libraries for profiler

* Mon Nov 21 2016 Denis Medvedev <nbr@altlinux.org> 4.6.2.7-alt3
- fix for profiler-iomap

* Fri Nov 18 2016 Denis Medvedev <nbr@altlinux.org> 4.6.2.7-alt2
- fix place of monoPosixHelper for x86_64

* Thu Oct 06 2016 Denis Medvedev <nbr@altlinux.org> 4.6.2.7-alt1
- new version.

* Sun Jul 17 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt9
- Moved library libMonoPosixHelper to arch-depended dir (fixes #32246).

* Sun Jan 24 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt8
- Removing remains of mono2

* Tue Jan 19 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt7
- rpm-build-mono4 integration

* Mon Jan 18 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt6
- Added missing mono4-data to mono4-full

* Fri Jan 15 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt4
- Fixed dependence on mono4-full

* Thu Jan 14 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt3
- Virtual packages mono4-full and mono4-devel added

* Sun Dec 27 2015 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt2
- Self compile

* Mon Dec 07 2015 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt1
- Initial build of 4.* version (based on Fedora core spec)


:
