%add_optflags -fcommon
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-generic-compat
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# from java9/hotspot/make/lib/JvmOverrideFiles.gmk:
# Performance measurements show that by compiling GC related code, we could
# significantly reduce the GC pause time on 32 bit Linux/Unix platforms by
# compiling without the PIC flag (-fPIC on linux).
# See 6454213 for more details.
# for arm it is fix by Gleb Fotengauer-Malinovskiy <glebfm@altlinux.org>
%if "%_libsuff" != "64"
%set_verify_elf_method textrel=relaxed
%endif

BuildRequires: ca-certificates-java
%def_enable accessibility
%def_disable javaws
%def_disable moz_plugin
%def_disable control_panel
%def_disable desktop
%def_disable systemtap
BuildRequires: unzip gcc-c++ libstdc++-devel-static
BuildRequires: libXext-devel libXrender-devel libXcomposite-devel
BuildRequires(pre): browser-plugins-npapi-devel lsb-release
BuildRequires(pre): rpm-macros-java
%set_compress_method none
%filter_from_requires /.usr.bin.java/d
%define oldname java-openjdk
BuildRequires: /proc rpm-build-java
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version and %%release is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 10.0.2.13
%define release 7
# RPM conditionals so as to be able to dynamically produce
# slowdebug/release builds. See:
# http://rpm.org/user_doc/conditional_builds.html
#
# Examples:
#
# Produce release *and* slowdebug builds on x86_64 (default):
# $ rpmbuild -ba java-1.8.0-openjdk.spec
#
# Produce only release builds (no slowdebug builds) on x86_64:
# $ rpmbuild -ba java-1.8.0-openjdk.spec --without slowdebug
#
# Only produce a release build on x86_64:
# $ fedpkg mockbuild --without slowdebug
#
# Only produce a debug build on x86_64:
# $ fedpkg local --without release
#
# Enable slowdebug builds by default on relevant arches.
%bcond_without slowdebug
# Enable release builds by default on relevant arches.
%bcond_without release

# note: parametrized macros are order-sensitive (unlike not-parametrized) even with normal macros
# also necessary when passing it as parameter to other macros. If not macro, then it is considered a switch
# see the difference between global and define:
# See https://github.com/rpm-software-management/rpm/issues/127 to comments at  "pmatilai commented on Aug 18, 2017"
# (initiated in https://bugzilla.redhat.com/show_bug.cgi?id=1482192)
%global debug_suffix_unquoted -slowdebug
# quoted one for shell operations
%global debug_suffix "%{debug_suffix_unquoted}"
%global normal_suffix ""

# if you want only debug build but providing java build only normal build but set normalbuild_parameter
%global debug_warning This package has full debug on. Install only in need and remove asap.
%global debug_on with full debug on
%global for_debug for packages with debug on

%if %{with release}
%global include_normal_build 1
%else
%global include_normal_build 1
%endif

%if %{include_normal_build}
%global build_loop1 %{normal_suffix}
%else
%global build_loop1 %{nil}
%endif

%global aarch64         aarch64 arm64 armv8
# we need to distinguish between big and little endian PPC64
%global ppc64le         ppc64le
%global ppc64be         ppc64 ppc64p7
%global multilib_arches %{power64} sparc64 x86_64
%global jit_arches      %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} %{arm} s390x
%global aot_arches      x86_64

# By default, we build a debug build during main build on JIT architectures
%if %{with slowdebug}
%ifarch %{jit_arches}
%ifnarch %{arm}
%global include_debug_build 0
%else
%global include_debug_build 0
%endif
%else
%global include_debug_build 0
%endif
%else
%global include_debug_build 0
%endif

%if %{include_debug_build}
%global build_loop2 %{debug_suffix}
%else
%global build_loop2 %{nil}
%endif

# if you disable both builds, then the build fails
%global build_loop  %{build_loop1} %{build_loop2}
# note: that order: normal_suffix debug_suffix, in case of both enabled
# is expected in one single case at the end of the build
%global rev_build_loop  %{build_loop2} %{build_loop1}

%ifarch %{jit_arches}
%global bootstrap_build 1
%else
%global bootstrap_build 1
%endif

%if %{bootstrap_build}
%global targets bootcycle-images all docs
%else
%global targets all docs
%endif


# Filter out flags from the optflags macro that cause problems with the OpenJDK build
# We filter out -O flags so that the optimization of HotSpot is not lowered from O3 to O2
# We filter out -Wall which will otherwise cause HotSpot to produce hundreds of thousands of warnings (100+mb logs)
# We replace it with -Wformat (required by -Werror=format-security) and -Wno-cpp to avoid FORTIFY_SOURCE warnings
# We filter out -fexceptions as the HotSpot build explicitly does -fno-exceptions and it's otherwise the default for C++
%global ourflags %(echo %optflags | sed -e 's|-Wall|-Wformat -Wno-cpp|' | sed -r -e 's|-O[0-9]*||')
%global ourcppflags %(echo %ourflags | sed -e 's|-fexceptions||')
%global ourldflags %{__global_ldflags}

# With disabled nss is NSS deactivated, so NSS_LIBDIR can contain the wrong path
# the initialization must be here. Later the pkg-config have buggy behavior
# looks like openjdk RPM specific bug
# Always set this so the nss.cfg file is not broken
%global NSS_LIBDIR %(pkg-config --variable=libdir nss)
%global NSS_LIBS %(pkg-config --libs nss)
%global NSS_CFLAGS %(pkg-config --cflags nss-softokn)
# see https://bugzilla.redhat.com/show_bug.cgi?id=1332456
%global NSSSOFTOKN_BUILDTIME_NUMBER %(pkg-config --modversion nss-softokn || : )
%global NSS_BUILDTIME_NUMBER %(pkg-config --modversion nss || : )
# this is workaround for processing of requires during srpm creation
%global NSSSOFTOKN_BUILDTIME_VERSION %(if [ "x%{NSSSOFTOKN_BUILDTIME_NUMBER}" == "x" ] ; then echo "" ;else echo ">= %{NSSSOFTOKN_BUILDTIME_NUMBER}" ;fi)
%global NSS_BUILDTIME_VERSION %(if [ "x%{NSS_BUILDTIME_NUMBER}" == "x" ] ; then echo "" ;else echo ">= %{NSS_BUILDTIME_NUMBER}" ;fi)


# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=1111349.
# See also https://bugzilla.redhat.com/show_bug.cgi?id=1590796
# as to why some libraries *cannot* be excluded. In particular,
# these are:
# libjsig.so, libjava.so, libjawt.so, libjvm.so and libverify.so
#%global _privatelibs libjsoundalsa[.]so.*|libsplashscreen[.]so.*|libawt_xawt[.]so.*|libjli[.]so.*|libattach[.]so.*|libawt[.]so.*|libextnet[.]so.*|libawt_headless[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas_unix[.]so.*|libjavajpeg[.]so.*|libjdwp[.]so.*|libjimage[.]so.*|libjsound[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmanagement_agent[.]so.*|libmanagement_ext[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libprefs[.]so.*|librmi[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsunec[.]so.*|libunpack[.]so.*|libzip[.]so.*|lib[.]so\\(SUNWprivate_.*


# In some cases, the arch used by the JDK does
# not match _arch.
# Also, in some cases, the machine name used by SystemTap
# does not match that given by _build_cpu
%ifarch x86_64
%global archinstall amd64
%endif
%ifarch ppc
%global archinstall ppc
%endif
%ifarch %{ppc64be}
%global archinstall ppc64
%endif
%ifarch %{ppc64le}
%global archinstall ppc64le
%endif
%ifarch %{ix86}
%global archinstall i686
%endif
%ifarch ia64
%global archinstall ia64
%endif
%ifarch s390
%global archinstall s390
%endif
%ifarch s390x
%global archinstall s390x
%endif
%ifarch %{arm}
%global archinstall arm
%endif
%ifarch %{aarch64}
%global archinstall aarch64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archinstall sparc
%endif
# 64 bit sparc
%ifarch sparc64
%global archinstall sparcv9
%endif
%ifnarch %{jit_arches}
%global archinstall %{_arch}
%endif



%if_enabled systemtap
%global with_systemtap 1
%else
%global with_systemtap 0
%endif

# New Version-String scheme-style defines
%global majorver 10
%global securityver 2

# Standard JPackage naming and versioning defines
%global origin          openjdk
%global origin_nice     OpenJDK
%global top_level_dir_name   %{origin}
%global minorver        0
%global buildver        13
%if %{bootstrap_build}
# priority must be 7 digits in total
# setting to 1, so debug ones can have 0
%global priority        00000%{minorver}10
%else
# normal priority for java 10
%define priority %(printf '%02d%02d%02d%02d' %{majorver} %{minorver} %{securityver} %{buildver} )
%endif
%global newjavaver      %{majorver}.%{minorver}.%{securityver}

%global javaver         %{majorver}

# parametrized macros are order-sensitive
%global compatiblename  java-%{majorver}-%{origin}
%global fullversion     %{compatiblename}-%{version}-%{release}
# images stub
%global jdkimage       jdk
# output dir stub
%define buildoutputdir openjdk/build
# we can copy the javadoc to not arched dir, or make it not noarch
%define uniquejavadocdir %{fullversion}
# main id and dir of this jdk
%define uniquesuffix %{fullversion}.%{_arch}

%global etcjavasubdir     %{_sysconfdir}/java/java-%{javaver}-%{origin}
%define etcjavadir()      %{expand:%{etcjavasubdir}/%{uniquesuffix}}
# Standard JPackage directories and symbolic links.
%define sdkdir %{uniquesuffix}
%define jrelnk jre-%{javaver}-%{origin}-%{version}-%{release}.%{_arch}

%define sdkbindir %{_jvmdir}/%{sdkdir}/bin
%define jrebindir %{_jvmdir}/%{sdkdir}/bin

%global rpm_state_dir %{_localstatedir}/lib/rpm-state/

%if_enabled systemtap
# Where to install systemtap tapset (links)
# We would like these to be in a package specific sub-dir,
# but currently systemtap doesn't support that, so we have to
# use the root tapset dir for now. To distinguish between 64
# and 32 bit architectures we place the tapsets under the arch
# specific dir (note that systemtap will only pickup the tapset
# for the primary arch for now). Systemtap uses the machine name
# aka build_cpu as architecture specific directory name.
%global tapsetroot /usr/share/systemtap
%global tapsetdirttapset %{tapsetroot}/tapset/
%global tapsetdir %{tapsetdirttapset}/%{_build_cpu}
%endif

# not-duplicated scriptlets for normal/debug packages
%global update_desktop_icons /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

























# not-duplicated requires/provides/obsoletes for normal/debug packages







# Prevent brp-java-repack-jars from being run
%global __jar_repack 0

Name:    java-10-openjdk
Version: %{newjavaver}.%{buildver}
Release: alt5_7jpp8.M90P.1
# java-1.5.0-ibm from jpackage.org set Epoch to 1 for unknown reasons
# and this change was brought into RHEL-4. java-1.5.0-ibm packages
# also included the epoch in their virtual provides. This created a
# situation where in-the-wild java-1.5.0-ibm packages provided "java =
# 1:1.5.0". In RPM terms, "1.6.0 < 1:1.5.0" since 1.6.0 is
# interpreted as 0:1.6.0. So the "java >= 1.6.0" requirement would be
# satisfied by the 1:1.5.0 packages. Thus we need to set the epoch in
# JDK package >= 1.6.0 to 1, and packages referring to JDK virtual
# provides >= 1.6.0 must specify the epoch, "java >= 1:1.6.0".

Epoch:   0
Summary: %{origin_nice} Runtime Environment %{majorver}
Group:   Development/Other

# HotSpot code is licensed under GPLv2
# JDK library code is licensed under GPLv2 with the Classpath exception
# The Apache license is used in code taken from Apache projects (primarily JAXP & JAXWS)
# DOM levels 2 & 3 and the XML digital signature schemas are licensed under the W3C Software License
# The JSR166 concurrency code is in the public domain
# The BSD and MIT licenses are used for a number of third-party libraries (see THIRD_PARTY_README)
# The OpenJDK source tree includes the JPEG library (IJG), zlib & libpng (zlib), giflib and LCMS (MIT)
# The test code includes copies of NSS under the Mozilla Public License v2.0
# The PCSClite headers are under a BSD with advertising license
# The elliptic curve cryptography (ECC) source code is licensed under the LGPLv2.1 or any later version
License:  ASL 1.1 and ASL 2.0 and BSD and BSD with advertising and GPL+ and GPLv2 and GPLv2 with exceptions and IJG and LGPLv2+ and MIT and MPLv2.0 and Public Domain and W3C and zlib
URL:      http://openjdk.java.net/


# to regenerate source0 (jdk) and source8 (jdk's taspets) run update_package.sh
# update_package.sh contains hard-coded repos, revisions, tags, and projects to regenerate the source archives
Source0: jdk-updates-jdk%{majorver}u-jdk-%{newjavaver}+%{buildver}.tar.xz
Source8: systemtap_3.2_tapsets_hg-icedtea8-9d464368e06d.tar.xz

# Desktop files. Adapted from IcedTea
Source9: jconsole.desktop.in

# nss configuration file
Source11: nss.cfg.in

# Removed libraries that we link instead
Source12: remove-intree-libraries.sh

# Ensure we aren't using the limited crypto policy
Source13: TestCryptoLevel.java

# Ensure ECDSA is working
Source14: TestECDSA.java

############################################
#
# RPM/distribution specific patches
#
############################################

# NSS via SunPKCS11 Provider (disabled comment
# due to memory leak).
Patch1000: enableCommentedOutSystemNss.patch

# Ignore AWTError when assistive technologies are loaded
Patch1:    accessible-toolkit.patch
# Restrict access to java-atk-wrapper classes
Patch2:    java-atk-wrapper-security.patch
Patch3:    libjpeg-turbo-1.4-compat.patch
# Follow system wide crypto policy RHBZ#1249083
Patch4:    RHBZ-1249083-system-crypto-policy-PR3183.patch
# System NSS via SunEC Provider
Patch5:    RHBZ-1565658-system-nss-SunEC.patch

#############################################
#
# OpenJDK specific patches
#
#############################################

# s390 (Zero) build does not bootcycle without this patch
# Already in JDK-11. Missing backports.
Patch100:  JDK-8201495-s390-java-opts.patch
# See JDK-8198844. This won't be needed any more in
# JDK 11+
Patch101:  sorted-diff.patch
# Type fixing for s390 (Zero). Not upstream.
Patch102:  java-openjdk-s390-size_t.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libalsa-devel
BuildRequires: binutils
BuildRequires: libcups-devel
BuildRequires: desktop-file-utils
# elfutils only are OK for build without AOT
BuildRequires: libasm-devel libdw-devel libdw-devel-static libelf-devel
BuildRequires: fontconfig
BuildRequires: libfreetype-devel
BuildRequires: libgif-devel
BuildRequires: gcc-c++
BuildRequires: gdb libgdb-devel
BuildRequires: gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires: liblcms2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libxslt xsltproc
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
# Requirements for setting up the nss.cfg
BuildRequires: libnss-devel libnss-devel-static
BuildRequires: xorg-proto-devel
BuildRequires: zip
BuildRequires: javapackages-filesystem
%if %{bootstrap_build}
BuildRequires: java-9-openjdk-devel
%else
BuildRequires: java-10-openjdk-devel
%endif
# Zero-assembler build requirement
%ifnarch %{jit_arches}
BuildRequires: libffi-devel
%endif
BuildRequires: tzdata-java >= 2015d
# Earlier versions have a bug in tree vectorization on PPC
BuildRequires: gcc >= 4.8.3
# Build requirements for SunEC system NSS support
BuildRequires: libnss-devel >= 3.16.1

%if_enabled systemtap
BuildRequires: systemtap-sdt-devel
%endif

# this is always built, also during debug-only build
# when it is built in debug-only this package is just placeholder
Requires: fontconfig
Requires: fonts-type1-xorg
# Requires rest of java
Requires: %{name}-headless = %{epoch}:%{version}-%{release}
# for java-X-openjdk package's desktop binding
Requires: gtk3-demo libgail3 libgtk+3 libgtk+3-schemas

Provides: java-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}

# Standard JPackage base provides
Provides: jre = %{javaver}
Provides: jre-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver} = %{epoch}:%{version}-%{release}
Provides: java-%{origin} = %{epoch}:%{version}-%{release}
Provides: java = %{epoch}:%{javaver}
Source44: import.info

%define altname %name
%define label -%{name}
%define javaws_ver      %{javaver}

%if "%{_lib}" == "lib64"
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so()(64bit)
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)(64bit)
Provides: %{_jvmdir}/%{sdkdir}/lib/%archinstall/server/libjvm.so()(64bit)
Provides: %{_jvmdir}/%{sdkdir}/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)(64bit)
%else
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so()
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)
Provides: %{_jvmdir}/%{sdkdir}/lib/%archinstall/server/libjvm.so()
Provides: %{_jvmdir}/%{sdkdir}/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)
%endif
Provides: java = %EVR
Patch33: java-10-openjdk-alt-link-fontmanager.patch
Patch34: java-9-openjdk-alt-no-objcopy.patch
Patch35: java-9-openjdk-alt-JDK-8237879.patch
Patch36: java-10-openjdk-10.0.2.13-7.aarch64-fix-errors.patch

%description
The %{origin_nice} runtime environment.

%if %{include_debug_build}
%package slowdebug
Summary: %{origin_nice} Runtime Environment %{majorver} %{debug_on}
Group:   Development/Other

%description slowdebug
The %{origin_nice} runtime environment.
%{debug_warning}
%endif

%if %{include_normal_build}
%package headless
Summary: %{origin_nice} Headless Runtime Environment %{majorver}
Group:   Development/Other

# Require /etc/pki/java/cacerts
Requires: ca-trust
# Require javapackages-filesystem for ownership of /usr/lib/jvm/ and macros
Requires: javapackages-filesystem
# Require zone-info data provided by tzdata-java sub-package
Requires: tzdata-java >= 2015d
# libsctp.so.1 is being `dlopen`ed on demand
Requires: liblksctp lksctp-tools
# there is a need to depend on the exact version of NSS
Requires: libnss %{NSS_BUILDTIME_VERSION}
Requires: libnss %{NSSSOFTOKN_BUILDTIME_VERSION}
# tool to copy jdk's configs - should be Recommends only, but then only dnf/yum enforce it,
# not rpm transaction and so no configs are persisted when pure rpm -u is run. It may be
# considered as regression
#Requires: copy-jdk-configs >= 3.3
# Post requires alternatives to install tool alternatives
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall tool alternatives
# in version 1.7 and higher for --family switch
# for optional support of kernel stream control, card reader and printing bindings
Requires: liblksctp lksctp-tools libpcsclite cups

# Standard JPackage base provides
Provides: jre-headless = %{epoch}:%{javaver}
Provides: jre-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: java-headless = %{epoch}:%{javaver}

Requires: java-common
Requires: /proc
Requires(post): /proc
Provides: java-headless = %EVR


%description headless
The %{origin_nice} runtime environment %{majorver} without audio and video support.
%endif

%if %{include_debug_build}
%package headless-slowdebug
Summary: %{origin_nice} Runtime Environment %{debug_on}
Group:   Development/Other


%description headless-slowdebug
The %{origin_nice} runtime environment %{majorver} without audio and video support.
%{debug_warning}
%endif

%if %{include_normal_build}
%package devel
Summary: %{origin_nice} Development Environment %{majorver}
Group:   Development/Java

# Requires base package
Requires:         %{name} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install tool alternatives
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall tool alternatives
# in version 1.7 and higher for --family switch

# Standard JPackage devel provides
Provides: java-sdk-%{javaver}-%{origin} = %{epoch}:%{version}
Provides: java-sdk-%{javaver} = %{epoch}:%{version}
#Provides: java-sdk-%%{origin}% = %%{epoch}:%%{version}
#Provides: java-sdk% = %%{epoch}:%%{javaver}
Provides: java-%{javaver}-devel = %{epoch}:%{version}
Provides: java-%{javaver}-%{origin}-devel = %{epoch}:%{version}
Provides: java-devel = %EVR
#Provides: java-devel-%%{origin}% = %%{epoch}:%%{version}
#Provides: java-devel% = %%{epoch}:%%{javaver}


%description devel
The %{origin_nice} development tools %{majorver}.
%endif

%if %{include_debug_build}
%package devel-slowdebug
Summary: %{origin_nice} Development Environment %{majorver} %{debug_on}
Group:   Development/Java


%description devel-slowdebug
The %{origin_nice} development tools %{majorver}.
%{debug_warning}
%endif

%if %{include_normal_build}
%package jmods
Summary: JMods for %{origin_nice} %{majorver}
Group:   Development/Java

# Requires devel package
# as jmods are bytecode, they should be OK without any _isa

Provides: java-jmods = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-jmods = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-jmods = %{epoch}:%{version}-%{release}


%description jmods
The JMods for %{origin_nice}.
%endif

%if %{include_debug_build}
%package jmods-slowdebug
Summary: JMods for %{origin_nice} %{majorver} %{debug_on}
Group:   Development/Java


%description jmods-slowdebug
The JMods for %{origin_nice} %{majorver}.
%{debug_warning}
%endif

%if %{include_normal_build}
%package demo
Summary: %{origin_nice} Demos %{majorver}
Group:   Development/Other

Requires: %{name} = %{epoch}:%{version}-%{release}

Provides: java-demo = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-demo = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-demo = %{epoch}:%{version}-%{release}


%description demo
The %{origin_nice} demos %{majorver}.
%endif

%if %{include_debug_build}
%package demo-slowdebug
Summary: %{origin_nice} Demos %{majorver} %{debug_on}
Group:   Development/Other


%description demo-slowdebug
The %{origin_nice} demos %{majorver}.
%{debug_warning}
%endif

%if %{include_normal_build}
%package src
Summary: %{origin_nice} Source Bundle %{majorver}
Group:   Development/Other

Requires: %{name}-headless = %{epoch}:%{version}-%{release}

# Standard JPackage sources provides
Provides: java-src = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-src = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-src = %{epoch}:%{version}-%{release}

%description src
The java-%{origin}-src sub-package contains the complete %{origin_nice} %{majorver}
class library source code for use by IDE indexers and debuggers.
%endif

%if %{include_debug_build}
%package src-slowdebug
Summary: %{origin_nice} Source Bundle %{majorver} %{for_debug}
Group:   Development/Other


%description src-slowdebug
The java-%{origin}-src-slowdebug sub-package contains the complete %{origin_nice} %{majorver}
 class library source code for use by IDE indexers and debuggers. Debugging %{for_debug}.
%endif

%if %{include_normal_build}
%package javadoc
Summary: %{origin_nice} %{majorver} API documentation
Group:   Development/Java
Requires: javapackages-filesystem

# Post requires alternatives to install javadoc alternative
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall javadoc alternative
# in version 1.7 and higher for --family switch

# Standard JPackage javadoc provides
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc = %{epoch}:%{version}-%{release}

%description javadoc
The %{origin_nice} %{majorver} API documentation.
%endif

%if %{include_normal_build}
%package javadoc-zip
Summary: %{origin_nice} %{majorver} API documentation compressed in single archive
Group:   Development/Java
Requires: javapackages-filesystem

# Post requires alternatives to install javadoc alternative
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall javadoc alternative
# in version 1.7 and higher for --family switch

# Standard JPackage javadoc provides
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc = %{epoch}:%{version}-%{release}

%description javadoc-zip
The %{origin_nice} %{majorver} API documentation compressed in single archive.
%endif

%if %{include_debug_build}
%package javadoc-slowdebug
Summary: %{origin_nice} %{majorver} API documentation %{for_debug}
Group:   Development/Java
Requires: javapackages-filesystem


%description javadoc-slowdebug
The %{origin_nice} %{majorver} API documentation %{for_debug}.
%endif

%if %{include_debug_build}
%package javadoc-zip-slowdebug
Summary: %{origin_nice} %{majorver} API documentation compressed in single archive %{for_debug}
Group:   Development/Java
Requires: javapackages-filesystem


%description javadoc-zip-slowdebug
The %{origin_nice} %{majorver} API documentation compressed in single archive %{for_debug}.
%endif


%prep
if [ %{include_normal_build} -eq 0 -o  %{include_normal_build} -eq 1 ] ; then
  echo "include_normal_build is %{include_normal_build}"
else
  echo "include_normal_build is %{include_normal_build}, thats invalid. Use 1 for yes or 0 for no"
  exit 11
fi
if [ %{include_debug_build} -eq 0 -o  %{include_debug_build} -eq 1 ] ; then
  echo "include_debug_build is %{include_debug_build}"
else
  echo "include_debug_build is %{include_debug_build}, thats invalid. Use 1 for yes or 0 for no"
  exit 12
fi
if [ %{include_debug_build} -eq 0 -a  %{include_normal_build} -eq 0 ] ; then
  echo "You have disabled both include_debug_build and include_normal_build. That is a no go."
  exit 13
fi
%setup -q -c -n %{uniquesuffix ""} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 8 ] ; then
 echo "priority must be 8 digits in total, violated"
 exit 14
fi

# OpenJDK patches

# Remove libraries that are linked
sh %{SOURCE12}
pushd %{top_level_dir_name}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%patch101 -p1
%patch102 -p1

popd # openjdk

%patch1000

# Extract systemtap tapsets
%if_enabled systemtap
tar --strip-components=1 -x -I xz -f %{SOURCE8}
%if %{include_debug_build}
cp -r tapset tapset%{debug_suffix}
%endif


for suffix in %{build_loop} ; do
  for file in "tapset"$suffix/*.in; do
    OUTPUT_FILE=`echo $file | sed -e "s:\.stp\.in$:%{version}-%{release}.%{_arch}.stp:g"`
    sed -e "s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/lib/server/libjvm.so:g" $file > $file.1
# TODO find out which architectures other than i686 have a client vm
%ifarch %{ix86}
    sed -e "s:@ABS_CLIENT_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/lib/client/libjvm.so:g" $file.1 > $OUTPUT_FILE
%else
    sed -e "/@ABS_CLIENT_LIBJVM_SO@/d" $file.1 > $OUTPUT_FILE
%endif
    sed -i -e "s:@ABS_JAVA_HOME_DIR@:%{_jvmdir}/%{sdkdir}:g" $OUTPUT_FILE
    sed -i -e "s:@INSTALL_ARCH_DIR@:%{archinstall}:g" $OUTPUT_FILE
    sed -i -e "s:@prefix@:%{_jvmdir}/%{sdkdir}/:g" $OUTPUT_FILE
  done
done
# systemtap tapsets ends
%endif

# Prepare desktop files
for suffix in %{build_loop} ; do
for file in %{SOURCE9}; do
    FILE=`basename $file | sed -e s:\.in$::g`
    EXT="${FILE##*.}"
    NAME="${FILE%.*}"
    OUTPUT_FILE=$NAME$suffix.$EXT
    sed    -e  "s:@JAVA_HOME@:%{sdkbindir}:g" $file > $OUTPUT_FILE
    sed -i -e  "s:@JRE_HOME@:%{jrebindir}:g" $OUTPUT_FILE
    sed -i -e  "s:@ARCH@:%{_arch}$suffix:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_MAJOR_VERSION@:%{majorver}:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VENDOR@:%{origin}:g" $OUTPUT_FILE
done
done

# Setup nss.cfg
sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE11} > nss.cfg
%patch33 -p0
%patch34 -p0
%patch35 -p0
%patch36 -p0


%build
# zerg's girar armh hack:
(while true; do date; sleep 7m; done) &
# end armh hack, kill it when girar will be fixed
# How many CPU's do we have?
#export NUM_PROC=%(/usr/bin/getconf _NPROCESSORS_ONLN 2> /dev/null || :)
export NUM_PROC=${NUM_PROC:-1}
%if 0%{?_smp_ncpus_max}
# Honor %%_smp_ncpus_max
[ ${NUM_PROC} -gt %{?_smp_ncpus_max} ] && export NUM_PROC=%{?_smp_ncpus_max}
%endif

%ifarch s390x sparc64 alpha %{power64} %{aarch64}
export ARCH_DATA_MODEL=64
%endif
%ifarch alpha
export CFLAGS="$CFLAGS -mieee"
%endif

# We use ourcppflags because the OpenJDK build seems to
# pass EXTRA_CFLAGS to the HotSpot C++ compiler...
# Explicitly set the C++ standard as the default has changed on GCC >= 6
EXTRA_CFLAGS="%ourcppflags -std=gnu++98 -Wno-error -fno-delete-null-pointer-checks -fno-lifetime-dse"
EXTRA_CPP_FLAGS="%ourcppflags -std=gnu++98 -fno-delete-null-pointer-checks -fno-lifetime-dse"

%ifarch %{power64} ppc
# fix rpmlint warnings
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif
export EXTRA_CFLAGS

(cd %{top_level_dir_name}/make/autoconf
 bash ./autogen.sh
)

for suffix in %{build_loop} ; do
if [ "x$suffix" = "x" ] ; then
  debugbuild=release
else
  # change --something to something
  debugbuild=`echo $suffix  | sed "s/-//g"`
fi

# Variable used in hs_err hook on build failures
top_dir_abs_path=$(pwd)/%{top_level_dir_name}

mkdir -p %{buildoutputdir}
pushd %{buildoutputdir}

bash ../configure \
%ifnarch %{jit_arches}
    --with-jvm-variants=zero \
%endif
%ifarch %{ppc64le}
    --with-jobs=1 \
%endif
    --with-version-build=%{buildver} \
    --with-version-pre="" \
    --with-version-opt="" \
%if %{bootstrap_build}
    --with-boot-jdk=/usr/lib/jvm/java-9-openjdk \
%else
    --with-boot-jdk=/usr/lib/jvm/java-10-openjdk \
%endif
    --with-debug-level=$debugbuild \
    --with-native-debug-symbols=internal \
    --enable-unlimited-crypto \
    --disable-system-nss \
    --with-zlib=system \
    --with-libjpeg=system \
    --with-giflib=system \
    --with-libpng=system \
    --with-lcms=system \
    --with-stdc++lib=dynamic \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --with-extra-ldflags="%{ourldflags}" \
    --with-num-cores="$NUM_PROC" \
    --disable-javac-server \
    --disable-warnings-as-errors

make \
    JAVAC_FLAGS=-g \
    LOG=trace \
    WARNINGS_ARE_ERRORS="-Wno-error" \
    CFLAGS_WARNINGS_ARE_ERRORS="-Wno-error" \
    %{targets} || ( pwd; find $top_dir_abs_path -name "hs_err_pid*.log" | xargs cat && false )

make docs-zip

# the build (erroneously) removes read permissions from some jars
# this is a regression in OpenJDK 7 (our compiler):
# http://icedtea.classpath.org/bugzilla/show_bug.cgi?id=1437
find images/%{jdkimage} -iname '*.jar' -exec chmod ugo+r {} \;

# remove redundant *diz and *debuginfo files
find images/%{jdkimage} -iname '*.diz' -exec rm {} \;
find images/%{jdkimage} -iname '*.debuginfo' -exec rm {} \;

# Build screws up permissions on binaries
# https://bugs.openjdk.java.net/browse/JDK-8173610
find images/%{jdkimage} -iname '*.so' -exec chmod +x {} \;
find images/%{jdkimage}/bin/ -exec chmod +x {} \;

popd >& /dev/null

# Install nss.cfg right away as we will be using the JRE above
export JAVA_HOME=$(pwd)/%{buildoutputdir}/images/%{jdkimage}

# Install nss.cfg right away as we will be using the JRE above
#install -m 644 nss.cfg $JAVA_HOME/conf/security/

# Use system-wide tzdata
rm $JAVA_HOME/lib/tzdb.dat
ln -s %{_datadir}/javazi-1.8/tzdb.dat $JAVA_HOME/lib/tzdb.dat

# build cycles
done

%check

# We test debug first as it will give better diagnostics on a crash
for suffix in %{rev_build_loop} ; do

export JAVA_HOME=$(pwd)/%{buildoutputdir}/images/%{jdkimage}

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE13}
$JAVA_HOME/bin/java --add-opens java.base/javax.crypto=ALL-UNNAMED TestCryptoLevel

# Check ECC is working
#$JAVA_HOME/bin/javac -d . %{SOURCE14}
#$JAVA_HOME/bin/java $(echo $(basename %{SOURCE14})|sed "s|\.java||")

# Check debug symbols are present and can identify code
find "$JAVA_HOME" -iname '*.so' -print0 | while read -d $'\0' lib
do
  if [ -f "$lib" ] ; then
    echo "Testing $lib for debug symbols"
    # All these tests rely on RPM failing the build if the exit code of any set
    # of piped commands is non-zero.

    # Test for .debug_* sections in the shared object. This is the main test
    # Stripped objects will not contain these
    eu-readelf -S "$lib" | grep "] .debug_"
    test $(eu-readelf -S "$lib" | grep -E "\]\ .debug_(info|abbrev)" | wc --lines) == 2

    # Test FILE symbols. These will most likely be removed by anything that
    # manipulates symbol tables because it's generally useless. So a nice test
    # that nothing has messed with symbols
    old_IFS="$IFS"
    IFS=$'\n'
    for line in $(eu-readelf -s "$lib" | grep "00000000      0 FILE    LOCAL  DEFAULT")
    do
     # We expect to see .cpp files, except for architectures like aarch64 and
     # s390 where we expect .o and .oS files
      echo "$line" | grep -E "ABS ((.*/)?[-_a-zA-Z0-9]+\.(c|cc|cpp|cxx|o|oS))?$"
    done
    IFS="$old_IFS"

    # If this is the JVM, look for javaCalls.(cpp|o) in FILEs, for extra sanity checking
    if [ "`basename $lib`" = "libjvm.so" ]; then
      eu-readelf -s "$lib" | \
        grep -E "00000000      0 FILE    LOCAL  DEFAULT      ABS javaCalls.(cpp|o)$"
    fi

    # Test that there are no .gnu_debuglink sections pointing to another
    # debuginfo file. There shouldn't be any debuginfo files, so the link makes
    # no sense either
    eu-readelf -S "$lib" | grep 'gnu'
    if eu-readelf -S "$lib" | grep '] .gnu_debuglink' | grep PROGBITS; then
      echo "bad .gnu_debuglink section."
      eu-readelf -x .gnu_debuglink "$lib"
      false
    fi
  fi
done

# Make sure gdb can do a backtrace based on line numbers on libjvm.so
# javaCalls.cpp:58 should map to:
# http://hg.openjdk.java.net/jdk8u/jdk8u/hotspot/file/ff3b27e6bcc2/src/share/vm/runtime/javaCalls.cpp#l58 
# Using line number 1 might cause build problems. See:
# https://bugzilla.redhat.com/show_bug.cgi?id=1539664
# https://bugzilla.redhat.com/show_bug.cgi?id=1538767
gdb -q "$JAVA_HOME/bin/java" <<EOF | tee gdb.out
handle SIGSEGV pass nostop noprint
handle SIGILL pass nostop noprint
set breakpoint pending on
break javaCalls.cpp:1
commands 1
backtrace
quit
end
run -version
EOF
grep 'JavaCallWrapper::JavaCallWrapper' gdb.out

# Check src.zip has all sources. See RHBZ#1130490
jar -tf $JAVA_HOME/lib/src.zip | grep 'sun.misc.Unsafe'

# Check class files include useful debugging information
$JAVA_HOME/bin/javap -l java.lang.Object | grep "Compiled from"
$JAVA_HOME/bin/javap -l java.lang.Object | grep LineNumberTable
$JAVA_HOME/bin/javap -l java.lang.Object | grep LocalVariableTable

# Check generated class files include useful debugging information
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep "Compiled from"
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep LineNumberTable
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep LocalVariableTable

# build cycles check
done

%install
STRIP_KEEP_SYMTAB=libjvm*

for suffix in %{build_loop} ; do

# Install the jdk
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}
cp -a %{buildoutputdir}/images/%{jdkimage} \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}

# Install jsa directories so we can owe them
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/%{archinstall}/server/
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/%{archinstall}/client/
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/client/ || true  ; # sometimes is here, sometimes not, ifout it or || true it out

pushd %{buildoutputdir}/images/%{jdkimage}

%if_enabled systemtap
  # Install systemtap support files
  install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset
  # note, that uniquesuffix  is in BUILD dir in this case
  cp -a $RPM_BUILD_DIR/%{uniquesuffix ""}/tapset$suffix/*.stp $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset/
  pushd  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset/
   tapsetFiles=`ls *.stp`
  popd
  install -d -m 755 $RPM_BUILD_ROOT%{tapsetdir}
  for name in $tapsetFiles ; do
    targetName=`echo $name | sed "s/.stp/$suffix.stp/"`
    ln -sf %{_jvmdir}/%{sdkdir}/tapset/$name $RPM_BUILD_ROOT%{tapsetdir}/$targetName
  done
%endif

  # Remove empty cacerts database
  rm -f $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/security/cacerts
  # Install cacerts symlink needed by some apps which hard-code the path
  pushd $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/security
      ln -sf /etc/pki/java/cacerts .
  popd

  # Install version-ed symlinks
  pushd $RPM_BUILD_ROOT%{_jvmdir}
    ln -sf %{sdkdir} %{jrelnk}
  popd


  # Install man pages
  install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
  for manpage in man/man1/*
  do
    # Convert man pages to UTF8 encoding
    iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
    mv -f $manpage.tmp $manpage
    install -m 644 -p $manpage $RPM_BUILD_ROOT%{_mandir}/man1/$(basename \
      $manpage .1)%{label}.1
  done
  # Remove man pages from jdk image
  rm -rf $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/man

popd


# Install Javadoc documentation
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
cp -a %{buildoutputdir}/images/docs $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}
cp -a %{buildoutputdir}/bundles/jdk-%{newjavaver}+%{buildver}-docs.zip  $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}.zip

# Install icons and menu entries
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    %{top_level_dir_name}/src/java.desktop/unix/classes/sun/awt/X11/java-icon${s}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-%{origin}.png
done

# Install desktop files
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole$suffix ; do
    desktop-file-install --vendor=%{uniquesuffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

# FIXME: remove SONAME entries from demo DSOs. See
# https://bugzilla.redhat.com/show_bug.cgi?id=436497

# copy samples next to demos; samples are mostly js files
cp -r %{top_level_dir_name}/src/sample  $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/


# moving config files to /etc
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib
mv $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/conf/  $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}
mv $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/lib/security  $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib
pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}
  ln -s %{etcjavadir -- $suffix}/conf  ./conf
popd
pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/lib
  ln -s %{etcjavadir -- $suffix}/lib/security  ./security
popd
# end moving files to /etc

# stabilize permissions
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -name "*.so" -exec chmod 755 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -type d -exec chmod 755 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/legal -type f -exec chmod 644 {} \; ; 

# end, dual install
done
for rpm404_ghost in %{_jvmdir}/%{sdkdir}/lib/server/classes.jsa %{_jvmdir}/%{sdkdir}/lib/client/classes.jsa
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done


%if %{include_normal_build}
# intentionally only for non-debug
%endif

export LANG=ru_RU.UTF-8
if stat -t %buildroot/usr/share/applications/*policytool.desktop; then
  sed -i 's,^Categories=.*,Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};,' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Name --set-value='OpenJDK %majorver Policy Tool' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Comment --set-value='Manage OpenJDK %majorver policy files' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Name[ru] --set-value='Настройка политик OpenJDK %majorver' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Comment[ru] --set-value='Управление файлами политик OpenJDK %majorver' %buildroot/usr/share/applications/*policytool.desktop
fi
sed -i 's,^Categories=.*,Categories=Development;Profiling;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};,' %buildroot/usr/share/applications/*jconsole.desktop
#Name=OpenJDK 8 Monitoring & Management Console
desktop-file-edit --set-key=Name --set-value='OpenJDK %majorver Management Console' %buildroot/usr/share/applications/*jconsole.desktop
#Comment=Monitor and manage OpenJDK applications
desktop-file-edit --set-key=Comment --set-value='Monitor and manage OpenJDK %majorver' %buildroot/usr/share/applications/*jconsole.desktop
desktop-file-edit --set-key=Name[ru] --set-value='Консоль OpenJDK %majorver' %buildroot/usr/share/applications/*jconsole.desktop
desktop-file-edit --set-key=Comment[ru] --set-value='Мониторинг и управление приложениями OpenJDK %majorver' %buildroot/usr/share/applications/*jconsole.desktop

##### javadoc Alt specific #####
echo java-javadoc >java-javadoc-buildreq-substitute
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
install -m644 java-javadoc-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-javadoc
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/%altname-javadoc<<EOF
%{_javadocdir}/java	%{_javadocdir}/%{uniquejavadocdir}/api	%{priority}
EOF


##################################################
# --- alt linux specific, shared with openjdk ---#
##################################################

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/jvisualvm ]; then
  cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-jvisualvm.desktop << EOF
[Desktop Entry]
Name=Java VisualVM (OpenJDK %{javaver})
Comment=Java Virtual Machine Monitoring, Troubleshooting, and Profiling Tool
Exec=%{_jvmdir}/%{sdkdir}/bin/jvisualvm
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;Profiling;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
fi

%if_enabled control_panel
# ControlPanel freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-control-panel.desktop << EOF
[Desktop Entry]
Name=Java Control Panel (OpenJDK %{javaver})
Name[ru]=Настройка Java (OpenJDK %{javaver})
Comment=Java Control Panel
Comment[ru]=Панель управления Java
Exec=%{_jvmdir}/%{sdkdir}/bin/jcontrol
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif

%if_enabled javaws
# javaws freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-javaws.desktop << EOF
[Desktop Entry]
Name=Java Web Start ((OpenJDK %{javaver}))
Comment=Java Application Launcher
MimeType=application/x-java-jnlp-file;
Exec=%{_jvmdir}/%{sdkdir}/bin/javaws %%u
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif

# Install substitute rules for buildreq
echo java >j2se-buildreq-substitute
echo java-headless >j2se-headless-buildreq-substitute
echo java-devel >j2se-devel-buildreq-substitute
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
install -m644 j2se-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name
install -m644 j2se-headless-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-headless
install -m644 j2se-devel-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-devel

install -d %buildroot%_altdir

# J2SE alternative
cat <<EOF >%buildroot%_altdir/%name-java-headless
%{_bindir}/java	%{_jvmdir}/%{sdkdir}/bin/java	%priority
%_man1dir/java.1.gz	%_man1dir/java%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/java
EOF
# binaries and manuals
for i in jjs keytool policytool servertool pack200 unpack200 \
orbd rmid rmiregistry tnameserv
do
  if [ -e %buildroot%{_jvmdir}/%{sdkdir}/bin/$i ]; then
    cat <<EOF >>%buildroot%_altdir/%name-java-headless
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/java
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/java
EOF
  fi
done

%if_enabled control_panel
cat <<EOF >>%buildroot%_altdir/%name-java
%{_bindir}/ControlPanel	%{_jvmdir}/%{sdkdir}/bin/ControlPanel	%{_jvmdir}/%{sdkdir}/bin/java
%{_bindir}/jcontrol	%{_jvmdir}/%{sdkdir}/bin/jcontrol	%{_jvmdir}/%{sdkdir}/bin/java
EOF
%endif
# ----- JPackage compatibility alternatives ------
cat <<EOF >>%buildroot%_altdir/%name-java-headless
%{_jvmdir}/jre	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/jre-%{origin}	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/jre-%{javaver}	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/jre-%{javaver}-%{origin}	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/java
EOF
# ----- end: JPackage compatibility alternatives ------


# Javac alternative
cat <<EOF >%buildroot%_altdir/%name-javac
%_bindir/javac	%{_jvmdir}/%{sdkdir}/bin/javac	%priority
%_man1dir/javac.1.gz	%_man1dir/javac%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF

# binaries and manuals
for i in appletviewer extcheck idlj jar jarsigner javadoc javah javap jdb native2ascii rmic serialver apt jconsole jinfo jmap jmc jps jsadebugd jstack jstat jstatd \
jhat jrunscript jvisualvm schemagen wsgen wsimport xjc
do
  if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/$i ]; then
  cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
  fi
done
# binaries w/o manuals
for i in HtmlConverter
do
  cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
done

# ----- JPackage compatibility alternatives ------
cat <<EOF >>%buildroot%_altdir/%name-javac
%{_jvmdir}/java	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/java-%{origin}	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
cat <<EOF >>%buildroot%_altdir/%name-javac-versioned
%{_jvmdir}/java-%{javaver}	%{_jvmdir}/%{sdkdir}	%priority
%{_jvmdir}/java-%{javaver}-%{origin}	%{_jvmdir}/%{sdkdir}	%priority
EOF

# ----- end: JPackage compatibility alternatives ------

# hack (see #11383) to enshure that all man pages will be compressed
for i in $RPM_BUILD_ROOT%_man1dir/*.1; do
    [ -f $i ] && gzip -9 $i
done

##################################################
# - END alt linux specific, shared with openjdk -#
##################################################


echo "install passed past alt linux specific."

%post headless
# java should be available ASAP
%force_update_alternatives

%ifarch %{jit_arches}
# MetaspaceShared::generate_vtable_methods not implemented for PPC JIT
%ifnarch %{power64}
#see https://bugzilla.redhat.com/show_bug.cgi?id=513605
java=%{jrebindir}/java
if [ -f /proc/cpuinfo ] && ! [ -d /.ours ] ; then #real workstation; not a mkimage-profile, etc
    $java -Xshare:dump >/dev/null 2>/dev/null
fi
%endif
%endif

%if %{include_normal_build}
%files
%_sysconfdir/buildreqs/packages/substitute.d/%name
# main package builds always
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}-%{origin}.png
%{_jvmdir}/%{sdkdir}/lib/libjsoundalsa.so
%{_jvmdir}/%{sdkdir}/lib/libsplashscreen.so
%{_jvmdir}/%{sdkdir}/lib/libawt_xawt.so
%{_jvmdir}/%{sdkdir}/lib/libjawt.so
%else
%files
# placeholder
%endif


%if %{include_normal_build}
%files headless
%_altdir/%altname-java-headless
%_sysconfdir/buildreqs/packages/substitute.d/%name-headless
# important note, see https://bugzilla.redhat.com/show_bug.cgi?id=1038092 for whole issue
# all config/noreplace files (and more) have to be declared in pretrans. See pretrans
%{_jvmdir}/%{sdkdir}/legal
%dir %{_sysconfdir}/.java/.systemPrefs
%dir %{_sysconfdir}/.java
%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{sdkdir}/release
%{_jvmdir}/%{jrelnk}
%dir %{_jvmdir}/%{sdkdir}/bin
%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/%{sdkdir}/bin/jjs
%{_jvmdir}/%{sdkdir}/bin/keytool
%{_jvmdir}/%{sdkdir}/bin/orbd
%{_jvmdir}/%{sdkdir}/bin/pack200
%{_jvmdir}/%{sdkdir}/bin/rmid
%{_jvmdir}/%{sdkdir}/bin/rmiregistry
%{_jvmdir}/%{sdkdir}/bin/servertool
%{_jvmdir}/%{sdkdir}/bin/tnameserv
%{_jvmdir}/%{sdkdir}/bin/unpack200
%dir %{_jvmdir}/%{sdkdir}/lib
%{_jvmdir}/%{sdkdir}/lib/classlist
%{_jvmdir}/%{sdkdir}/lib/jexec
%{_jvmdir}/%{sdkdir}/lib/jrt-fs.jar
%{_jvmdir}/%{sdkdir}/lib/modules
%{_jvmdir}/%{sdkdir}/lib/psfont.properties.ja
%{_jvmdir}/%{sdkdir}/lib/psfontj2d.properties
%{_jvmdir}/%{sdkdir}/lib/tzdb.dat
%dir %{_jvmdir}/%{sdkdir}/lib/jli
%{_jvmdir}/%{sdkdir}/lib/jli/libjli.so
%{_jvmdir}/%{sdkdir}/lib/jvm.cfg
%{_jvmdir}/%{sdkdir}/lib/libattach.so
%{_jvmdir}/%{sdkdir}/lib/libawt.so
%{_jvmdir}/%{sdkdir}/lib/libextnet.so
%{_jvmdir}/%{sdkdir}/lib/libjsig.so
%{_jvmdir}/%{sdkdir}/lib/libawt_headless.so
%{_jvmdir}/%{sdkdir}/lib/libdt_socket.so
%{_jvmdir}/%{sdkdir}/lib/libfontmanager.so
%{_jvmdir}/%{sdkdir}/lib/libinstrument.so
%{_jvmdir}/%{sdkdir}/lib/libj2gss.so
%{_jvmdir}/%{sdkdir}/lib/libj2pcsc.so
%{_jvmdir}/%{sdkdir}/lib/libj2pkcs11.so
%{_jvmdir}/%{sdkdir}/lib/libjaas_unix.so
%{_jvmdir}/%{sdkdir}/lib/libjava.so
%{_jvmdir}/%{sdkdir}/lib/libjavajpeg.so
%{_jvmdir}/%{sdkdir}/lib/libjdwp.so
%{_jvmdir}/%{sdkdir}/lib/libjimage.so
%{_jvmdir}/%{sdkdir}/lib/libjsound.so
%{_jvmdir}/%{sdkdir}/lib/liblcms.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement_agent.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement_ext.so
%{_jvmdir}/%{sdkdir}/lib/libmlib_image.so
%{_jvmdir}/%{sdkdir}/lib/libnet.so
%{_jvmdir}/%{sdkdir}/lib/libnio.so
%{_jvmdir}/%{sdkdir}/lib/libprefs.so
%{_jvmdir}/%{sdkdir}/lib/librmi.so
%{_jvmdir}/%{sdkdir}/lib/libsaproc.so
%{_jvmdir}/%{sdkdir}/lib/libsctp.so
#%{_jvmdir}/%{sdkdir}/lib/libsunec.so
%{_jvmdir}/%{sdkdir}/lib/libunpack.so
%{_jvmdir}/%{sdkdir}/lib/libverify.so
%{_jvmdir}/%{sdkdir}/lib/libzip.so
%{_mandir}/man1/java%{label}.1*
%{_mandir}/man1/jjs%{label}.1*
%{_mandir}/man1/keytool%{label}.1*
%{_mandir}/man1/orbd%{label}.1*
%{_mandir}/man1/pack200%{label}.1*
%{_mandir}/man1/rmid%{label}.1*
%{_mandir}/man1/rmiregistry%{label}.1*
%{_mandir}/man1/servertool%{label}.1*
%{_mandir}/man1/tnameserv%{label}.1*
%{_mandir}/man1/unpack200%{label}.1*
%{_jvmdir}/%{sdkdir}/lib/server/
%{_jvmdir}/%{sdkdir}/lib/client/
%ifarch %{jit_arches}
%ifnarch %{power64}
%attr(444, root, root) %ghost %{_jvmdir}/%{sdkdir}/lib/server/classes.jsa
%attr(444, root, root) %ghost %{_jvmdir}/%{sdkdir}/lib/client/classes.jsa
%endif
%endif
%dir %{etcjavasubdir}
%dir %{etcjavadir}
%dir %{etcjavadir}/lib
%dir %{etcjavadir}/lib/security
%{etcjavadir}/lib/security/cacerts
%dir %{etcjavadir}/conf
%dir %{etcjavadir}/conf/management
%dir %{etcjavadir}/conf/security
%dir %{etcjavadir}/conf/security/policy
%dir %{etcjavadir}/conf/security/policy/limited
%dir %{etcjavadir}/conf/security/policy/unlimited
%config(noreplace) %{etcjavadir}/lib/security/default.policy
%config(noreplace) %{etcjavadir}/lib/security/blacklisted.certs
%config(noreplace) %{etcjavadir}/conf/security/policy/limited/exempt_local.policy
%config(noreplace) %{etcjavadir}/conf/security/policy/limited/default_local.policy
%config(noreplace) %{etcjavadir}/conf/security/policy/limited/default_US_export.policy
%config(noreplace) %{etcjavadir}/conf/security/policy/unlimited/default_local.policy
%config(noreplace) %{etcjavadir}/conf/security/policy/unlimited/default_US_export.policy
 %{etcjavadir}/conf/security/policy/README.txt
%config(noreplace) %{etcjavadir}/conf/security/java.policy
%config(noreplace) %{etcjavadir}/conf/security/java.security
%config(noreplace) %{etcjavadir}/conf/logging.properties
#%config(noreplace) %{etcjavadir}/conf/security/nss.cfg
%config(noreplace) %{etcjavadir}/conf/management/jmxremote.access
# this is conifg template, thus not config-noreplace
%config  %{etcjavadir}/conf/management/jmxremote.password.template
%config(noreplace) %{etcjavadir}/conf/management/management.properties
%config(noreplace) %{etcjavadir}/conf/net.properties
%config(noreplace) %{etcjavadir}/conf/sound.properties
%{_jvmdir}/%{sdkdir}/conf
%{_jvmdir}/%{sdkdir}/lib/security

%files devel
%_altdir/%altname-javac
%_altdir/%altname-javac-versioned
%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%dir %{_jvmdir}/%{sdkdir}/bin
%{_jvmdir}/%{sdkdir}/bin/appletviewer
%{_jvmdir}/%{sdkdir}/bin/idlj
%{_jvmdir}/%{sdkdir}/bin/jar
%{_jvmdir}/%{sdkdir}/bin/jarsigner
%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/%{sdkdir}/bin/javadoc
%{_jvmdir}/%{sdkdir}/bin/javap
%{_jvmdir}/%{sdkdir}/bin/jconsole
%{_jvmdir}/%{sdkdir}/bin/jcmd
%{_jvmdir}/%{sdkdir}/bin/jdb
%{_jvmdir}/%{sdkdir}/bin/jdeps
%{_jvmdir}/%{sdkdir}/bin/jdeprscan
%{_jvmdir}/%{sdkdir}/bin/jimage
%{_jvmdir}/%{sdkdir}/bin/jhsdb
%{_jvmdir}/%{sdkdir}/bin/jinfo
%{_jvmdir}/%{sdkdir}/bin/jlink
%{_jvmdir}/%{sdkdir}/bin/jmap
%{_jvmdir}/%{sdkdir}/bin/jmod
%{_jvmdir}/%{sdkdir}/bin/jps
%{_jvmdir}/%{sdkdir}/bin/jrunscript
%{_jvmdir}/%{sdkdir}/bin/jshell
%{_jvmdir}/%{sdkdir}/bin/jstack
%{_jvmdir}/%{sdkdir}/bin/jstat
%{_jvmdir}/%{sdkdir}/bin/jstatd
%{_jvmdir}/%{sdkdir}/bin/rmic
%{_jvmdir}/%{sdkdir}/bin/schemagen
%{_jvmdir}/%{sdkdir}/bin/serialver
%{_jvmdir}/%{sdkdir}/bin/wsgen
%{_jvmdir}/%{sdkdir}/bin/wsimport
%{_jvmdir}/%{sdkdir}/bin/xjc
%ifarch %{aot_arches}
%{_jvmdir}/%{sdkdir}/bin/jaotc
%endif
%{_jvmdir}/%{sdkdir}/include
%{_jvmdir}/%{sdkdir}/lib/ct.sym
%if_enabled systemtap
%{_jvmdir}/%{sdkdir}/tapset
%endif
%{_datadir}/applications/*jconsole.desktop
%{_mandir}/man1/appletviewer%{label}.1*
%{_mandir}/man1/idlj%{label}.1*
%{_mandir}/man1/jar%{label}.1*
%{_mandir}/man1/jarsigner%{label}.1*
%{_mandir}/man1/javac%{label}.1*
%{_mandir}/man1/javadoc%{label}.1*
%{_mandir}/man1/javap%{label}.1*
%{_mandir}/man1/jconsole%{label}.1*
%{_mandir}/man1/jcmd%{label}.1*
%{_mandir}/man1/jdb%{label}.1*
%{_mandir}/man1/jdeps%{label}.1*
%{_mandir}/man1/jinfo%{label}.1*
%{_mandir}/man1/jmap%{label}.1*
%{_mandir}/man1/jps%{label}.1*
%{_mandir}/man1/jrunscript%{label}.1*
%{_mandir}/man1/jstack%{label}.1*
%{_mandir}/man1/jstat%{label}.1*
%{_mandir}/man1/jstatd%{label}.1*
%{_mandir}/man1/rmic%{label}.1*
%{_mandir}/man1/schemagen%{label}.1*
%{_mandir}/man1/serialver%{label}.1*
%{_mandir}/man1/wsgen%{label}.1*
%{_mandir}/man1/wsimport%{label}.1*
%{_mandir}/man1/xjc%{label}.1*
%if_enabled systemtap
%dir %{tapsetroot}
%dir %{tapsetdirttapset}
%dir %{tapsetdir}
%{tapsetdir}/*%{_arch}.stp
%endif

%files jmods
%{_jvmdir}/%{sdkdir}/jmods

%files demo
%{_jvmdir}/%{sdkdir}/legal
%{_jvmdir}/%{sdkdir}/demo
%{_jvmdir}/%{sdkdir}/sample

%files src
%{_jvmdir}/%{sdkdir}/legal
%{_jvmdir}/%{sdkdir}/lib/src.zip

%files javadoc
%_altdir/%altname-javadoc
%_sysconfdir/buildreqs/packages/substitute.d/%name-javadoc
%doc %{_javadocdir}/%{uniquejavadocdir}
%doc --no-dereference %{buildoutputdir}/images/%{jdkimage}/legal

# this puts huge file to /usr/share
# unluckily ti is really a documentation file
# and unluckily it really is architecture-dependent, as eg. aot and grail are now x86_64 only
# same for debug variant
%files javadoc-zip
%doc %{_javadocdir}/%{uniquejavadocdir}.zip
%doc --no-dereference %{buildoutputdir}/images/%{jdkimage}/legal
%endif

%if %{include_debug_build}
%files slowdebug

%files headless-slowdebug

%files devel-slowdebug

%files jmods-slowdebug

%files demo-slowdebug

%files src-slowdebug

%files javadoc-slowdebug

%files javadoc-zip-slowdebug
%endif


%changelog
* Wed Feb 24 2021 Igor Vlasenko <viy@altlinux.org> 0:10.0.2.13-alt5_7jpp8.M90P.1
- p9 bootstrap

* Thu Dec 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:10.0.2.13-alt5_7jpp9
- added alternatives for keytool, policytool, etc
- non-bootstrap build

* Sat Dec 12 2020 Igor Vlasenko <viy@altlinux.ru> 0:10.0.2.13-alt4_7jpp9
- use zerg@'s hack for armh

* Mon Nov 23 2020 Igor Vlasenko <viy@altlinux.ru> 0:10.0.2.13-alt3_7jpp9
- added jjs alternative and fixed /usr/bin/jjs provides

* Tue Oct 06 2020 Igor Vlasenko <viy@altlinux.ru> 0:10.0.2.13-alt2_7jpp9
- fixed build

* Tue Jul 09 2019 Igor Vlasenko <viy@altlinux.ru> 0:10.0.2.13-alt1_7jpp9
- new version

