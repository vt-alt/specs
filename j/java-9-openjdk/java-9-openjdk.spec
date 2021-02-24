%add_optflags -fcommon
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-generic-compat
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
BuildRequires: /proc rpm-build-java
%define fedora 30
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version and %%release is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name java-9-openjdk
%define version 9.0.4.11
%define release 6
# note, parametrised macros are order-senisitve (unlike not-parametrized) even with normal macros
# also necessary when passing it as parameter other macros. If not macro, then it is considered as switch
%global debug_suffix_unquoted -debug
# quoted one for shell operations
%global debug_suffix "%{debug_suffix_unquoted}"
%global normal_suffix ""

#if you wont only debug build, but providing java, build only normal build, but  set normalbuild_parameter
%global debugbuild_parameter  slowdebug
%global normalbuild_parameter release
%global debug_warning This package have full debug on. Install only in need, and remove asap.
%global debug_on with full debug on
%global for_debug for packages with debug on

# by default we build normal build always.
%global include_normal_build 1
%if %{include_normal_build}
%global build_loop1 %{normal_suffix}
%else
%global build_loop1 %{nil}
%endif

%global aarch64         aarch64 arm64 armv8
# sometimes we need to distinguish big and little endian PPC64
%global ppc64le         ppc64le
%global ppc64be         ppc64 ppc64p7
%global multilib_arches %{power64} sparc64 x86_64
%global jit_arches      %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} %{arm} s390x
%global aot_arches      x86_64

# By default, we build a debug build during main build on JIT architectures
%ifarch %{jit_arches}
%ifnarch %{arm}
%global include_debug_build 0
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

# if you disable both builds, then build fails
%global build_loop  %{build_loop1} %{build_loop2}
# note, that order  normal_suffix debug_suffix, in case of both enabled,
# is expected in one single case at the end of build
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

# With diabled nss is NSS deactivated, so in NSS_LIBDIR can be wrong path
# the initialisation must be here. LAter the pkg-connfig have bugy behaviour
#looks liekopenjdk RPM specific bug
# Always set this so the nss.cfg file is not broken
%global NSS_LIBDIR %(pkg-config --variable=libdir nss)
%global NSS_LIBS %(pkg-config --libs nss)
%global NSS_CFLAGS %(pkg-config --cflags nss-softokn)
# see https://bugzilla.redhat.com/show_bug.cgi?id=1332456
%global NSSSOFTOKN_BUILDTIME_NUMBER %(pkg-config --modversion nss-softokn || : )
%global NSS_BUILDTIME_NUMBER %(pkg-config --modversion nss || : )
#this is worakround for processing of requires during srpm creation
%global NSSSOFTOKN_BUILDTIME_VERSION %(if [ "x%{NSSSOFTOKN_BUILDTIME_NUMBER}" == "x" ] ; then echo "" ;else echo ">= %{NSSSOFTOKN_BUILDTIME_NUMBER}" ;fi)
%global NSS_BUILDTIME_VERSION %(if [ "x%{NSS_BUILDTIME_NUMBER}" == "x" ] ; then echo "" ;else echo ">= %{NSS_BUILDTIME_NUMBER}" ;fi)


# fix for https://bugzilla.redhat.com/show_bug.cgi?id=1111349
#%global _privatelibs libmawt[.]so.*

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

# Convert an absolute path to a relative path.  Each symbolic link is
# specified relative to the directory in which it is installed so that
# it will resolve properly within chrooted installations.
%global script 'use File::Spec; print File::Spec->abs2rel($ARGV[0], $ARGV[1])'
%global abs2rel %{__perl} -e %{script}

# New Version-String scheme-style defines
%global majorver 9
%global securityver 4

# Standard JPackage naming and versioning defines.
%global origin          openjdk
%global minorver        0
%global buildver        11
%if %{bootstrap_build}
# priority must be 7 digits in total
#setting to 1, so debug ones can have 0
%global priority        00000%{minorver}1
%else
# normal priority for java 9
%define priority %( printf '%01d%02d%02d%02d' %{majorver} %{minorver} %{securityver} %{buildver} )
%endif

%global newjavaver      %{majorver}.%{minorver}.%{securityver}

%global javaver         %{majorver}

# parametrized macros are order-sensitive
%global fullversion     %{name}-%{version}-%{release}
#images stub
%global jdkimage       jdk
# output dir stub
%define buildoutputdir openjdk/build
#we can copy the javadoc to not arched dir, or made it not noarch
%define uniquejavadocdir %{fullversion}
#main id and dir of this jdk
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
# We would like these to be in a package specific subdir,
# but currently systemtap doesn't support that, so we have to
# use the root tapset dir for now. To distinquish between 64
# and 32 bit architectures we place the tapsets under the arch
# specific dir (note that systemtap will only pickup the tapset
# for the primary arch for now). Systemtap uses the machine name
# aka build_cpu as architecture specific directory name.
%global tapsetroot /usr/share/systemtap
%global tapsetdir %{tapsetroot}/tapset/%{_build_cpu}
%endif

# not-duplicated scriplets for normal/debug packages
%global update_desktop_icons /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


























# not-duplicated requires/provides/obsolate for normal/debug packages








# Prevent brp-java-repack-jars from being run.
%global __jar_repack 0

Name:    java-%{majorver}-%{origin}
Version: %{newjavaver}.%{buildver}
Release: alt8_6jpp8.M90P.1
# java-1.5.0-ibm from jpackage.org set Epoch to 1 for unknown reasons,
# and this change was brought into RHEL-4.  java-1.5.0-ibm packages
# also included the epoch in their virtual provides.  This created a
# situation where in-the-wild java-1.5.0-ibm packages provided "java =
# 1:1.5.0".  In RPM terms, "1.6.0 < 1:1.5.0" since 1.6.0 is
# interpreted as 0:1.6.0.  So the "java >= 1.6.0" requirement would be
# satisfied by the 1:1.5.0 packages.  Thus we need to set the epoch in
# JDK package >= 1.6.0 to 1, and packages referring to JDK virtual
# provides >= 1.6.0 must specify the epoch, "java >= 1:1.6.0".

Epoch:   0
Summary: OpenJDK Runtime Environment
Group:   Development/Other

License:  ASL 1.1 and ASL 2.0 and GPL+ and GPLv2 and GPLv2 with exceptions and LGPL+ and LGPLv2 and MPLv1.0 and MPLv1.1 and Public Domain and W3C
URL:      http://openjdk.java.net/

# Source from upstrem OpenJDK9 project. To regenerate, use
# PROJECT_NAME=jdk-updates REPO_NAME=jdk9u VERSION=jdk-%%{majorver}.%%{minorver}.%%{securityver}+%%{buildver} ./generate_source_tarball.sh
#
# Example:
# PROJECT_NAME=jdk-updates REPO_NAME=jdk9u VERSION=jdk-9.0.4+11 ./generate_source_tarball.sh 
Source0:  jdk-updates-jdk%{majorver}u-jdk-%{newjavaver}+%{buildver}.tar.xz

# Custom README for -src subpackage
Source2:  README.md

# Use 'generate_tarballs.sh' to generate the following tarballs
# They are based on code contained in the IcedTea7 project.

# Systemtap tapsets. Zipped up to keep it small.
Source8: systemtap-tapset-3.6.0pre02.tar.xz

# Desktop files. Adapated from IcedTea.
Source9: jconsole.desktop.in
Source10: policytool.desktop.in

# nss configuration file
Source11: nss.cfg.in

# Removed libraries that we link instead
Source12: remove-intree-libraries.sh

# Ensure we aren't using the limited crypto policy
Source13: TestCryptoLevel.java

# Ensure ECDSA is working
Source14: TestECDSA.java

# RPM/distribution specific patches

# Ignore AWTError when assistive technologies are loaded 
Patch1:   accessible-toolkit.patch
# Restrict access to java-atk-wrapper classes
Patch3: java-atk-wrapper-security.patch
# RHBZ 808293
Patch4: PStack-808293.patch
# Allow multiple initialization of PKCS11 libraries
Patch5: multiple-pkcs11-library-init.patch
Patch12: removeSunEcProvider-RH1154143.patch
Patch13: libjpeg-turbo-1.4-compat.patch

#
# OpenJDK specific patches
#

# JVM heap size changes for s390 (thanks to aph)
Patch100: java-1.9.0-openjdk-s390-java-opts.patch
Patch101: sorted-diff.patch
# Type fixing for s390
Patch102: java-1.9.0-openjdk-size_t.patch
Patch103: hotspot-min-max-macros.patch
Patch104: bootcycle_jobs.patch

#Patch300: jstack-pr1845.patch

Patch400: ppc_stack_overflow_fix.patch 
Patch401: aarch64BuildFailure.patch

# Fix AArch64 build issues which got introduced with 9.0.4+11 (January 2018 CPU)
#
# JDK-8195685 AArch64 cannot build with JDK-8174962
# JDK-8196136 AArch64: Correct register use in patch for JDK-8195685
# JDK-8195859 AArch64: vtableStubs gtest fails after 8174962
# JDK-8196221 AArch64: Mistake in committed patch for JDK-8195859
Patch402: JDK-8195685-cannot-build-with-8174962.patch
Patch403: JDK-8196136-correct-register-use-8195685.patch
Patch404: JDK-8195859-vtableStubs-gtest-fails-after-8174962.patch
Patch405: JDK-8196221-mistake-in-8195859.patch

# Non-OpenJDK fixes
Patch1000: enableCommentedOutSystemNss.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libalsa-devel
BuildRequires: binutils
BuildRequires: libcups-devel
BuildRequires: desktop-file-utils
# elfutils only are ok for built without AOT
BuildRequires: libasm-devel libdw-devel libdw-devel-static libelf-devel
BuildRequires: fontconfig
BuildRequires: libfreetype-devel
BuildRequires: libgif-devel
BuildRequires: gcc-c++
BuildRequires: gdb libgdb-devel
BuildRequires: gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel
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
%if %{bootstrap_build}
BuildRequires: java-1.8.0-openjdk-devel
%else
BuildRequires: java-9-openjdk-devel
%endif
# Zero-assembler build requirement.
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

# this is built always, also during debug-only build
# when it is built in debug-only, then this package is just placeholder
Requires: fontconfig
Requires: fonts-type1-xorg

# Requires rest of java
Requires: %{name}-headless = %{epoch}:%{version}-%{release}

Provides: java-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}

# Standard JPackage base provides.
Provides: jre-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver} = %{epoch}:%{version}-%{release}
Provides: jre = %{javaver}
Provides: java-%{origin} = %{epoch}:%{version}-%{release}
Provides: java = %{epoch}:%{javaver}
# Standard JPackage extensions provides.
Provides: java-fonts = %{epoch}:%{version}
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
Patch33: java-9-openjdk-alt-link-fontmanager.patch
Patch34: java-9-openjdk-alt-no-objcopy.patch
Patch35: java-9-openjdk-alt-JDK-8237879.patch
Patch36: java-9-openjdk-9.0.4.11-6.aarch64-fix-errors.patch


%description
The OpenJDK runtime environment.

%if %{include_debug_build}
%package debug
Summary: OpenJDK Runtime Environment %{debug_on}
Group:   Development/Other

%description debug
The OpenJDK runtime environment.
%{debug_warning}
%endif

%if %{include_normal_build}
%package headless
Summary: OpenJDK Runtime Environment
Group:   Development/Other

# Require /etc/pki/java/cacerts.
Requires: ca-trust
# Require javapackages-tools for ownership of /usr/lib/jvm/
Requires: javapackages-tools
# Require zoneinfo data provided by tzdata-java subpackage.
Requires: tzdata-java >= 2015d
# libsctp.so.1 is being `dlopen`ed on demand
Requires: liblksctp lksctp-tools
# there is a need to depend on the exact version of NSS
Requires: libnss %{NSS_BUILDTIME_VERSION}
Requires: libnss %{NSSSOFTOKN_BUILDTIME_VERSION}
# tool to copy jdk's configs - should be Recommends only, but then only dnf/yum eforce it, not rpm transaction and so no configs are persisted when pure rpm -u is run. I t may be consiedered as regression
#Requires:	copy-jdk-configs >= 3.3
# Post requires alternatives to install tool alternatives.
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall tool alternatives.
# in version 1.7 and higher for --family switch

# Standard JPackage base provides.
Provides: jre-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides: jre-headless = %{epoch}:%{javaver}
Provides: java-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: java-headless = %{epoch}:%{javaver}
# Standard JPackage extensions provides.
Provides: jndi = %{epoch}:%{version}
Provides: jndi-ldap = %{epoch}:%{version}
Provides: jndi-cos = %{epoch}:%{version}
Provides: jndi-rmi = %{epoch}:%{version}
Provides: jndi-dns = %{epoch}:%{version}
Provides: jaas = %{epoch}:%{version}
Provides: jsse = %{epoch}:%{version}
Provides: jce = %{epoch}:%{version}
Provides: jdbc-stdext = 4.1
Provides: java-sasl = %{epoch}:%{version}

Requires: java-common
Requires: /proc
Requires(post): /proc


%description headless
The OpenJDK runtime environment without audio and video support.
%endif

%if %{include_debug_build}
%package headless-debug
Summary: OpenJDK Runtime Environment %{debug_on}
Group:   Development/Other


%description headless-debug
The OpenJDK runtime environment without audio and video support.
%{debug_warning}
%endif

%if %{include_normal_build}
%package devel
Summary: OpenJDK Development Environment
Group:   Development/Java

# Require base package.
Requires:         %{name} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install tool alternatives.
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall tool alternatives.
# in version 1.7 and higher for --family switch

# Standard JPackage devel provides.
Provides: java-sdk-%{javaver}-%{origin} = %{epoch}:%{version}
Provides: java-sdk-%{javaver} = %{epoch}:%{version}
#Provides: java-sdk-%{origin} = %{epoch}:%{version}
#Provides: java-sdk = %{epoch}:%{javaver}
Provides: java-%{javaver}-devel = %{epoch}:%{version}
#Provides: java-devel-%{origin} = %{epoch}:%{version}
#Provides: java-devel = %{epoch}:%{javaver}


%description devel
The OpenJDK development tools.
%endif

%if %{include_debug_build}
%package devel-debug
Summary: OpenJDK Development Environment %{debug_on}
Group:   Development/Java


%description devel-debug
The OpenJDK development tools.
%{debug_warning}
%endif

%if %{include_normal_build}
%package jmods
Summary: JMods for OpenJDK
Group:   Development/Java

# Require devel package.
# as jmods are bytecode, they shouldbe ok without any _isa

Provides: java-%{javaver}-%{origin}-jmods = %{epoch}:%{version}-%{release}


%description jmods
The JMods for OpenJDK.
%endif

%if %{include_debug_build}
%package jmods-debug
Summary: JMods for OpenJDK %{debug_on}
Group:   Development/Java


%description jmods-debug
The JMods for OpenJDK.
%{debug_warning}
%endif

%if %{include_normal_build}
%package demo
Summary: OpenJDK Demos
Group:   Development/Other

Requires: %{name} = %{epoch}:%{version}-%{release}

Provides: java-%{javaver}-%{origin}-demo = %{epoch}:%{version}-%{release}


%description demo
The OpenJDK demos.
%endif

%if %{include_debug_build}
%package demo-debug
Summary: OpenJDK Demos %{debug_on}
Group:   Development/Other


%description demo-debug
The OpenJDK demos.
%{debug_warning}
%endif

%if %{include_normal_build}
%package src
Summary: OpenJDK Source Bundle
Group:   Development/Other

Requires: %{name}-headless = %{epoch}:%{version}-%{release}

# Standard JPackage javadoc provides.
Provides: java-src = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-src = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-src = %{epoch}:%{version}-%{release}

%description src
The OpenJDK source bundle.
%endif

%if %{include_debug_build}
%package src-debug
Summary: OpenJDK Source Bundle %{for_debug}
Group:   Development/Other


%description src-debug
The OpenJDK source bundle %{for_debug}.
%endif

%if %{include_normal_build}
%package javadoc
Summary: OpenJDK API Documentation
Group:   Development/Java
Requires: javapackages-tools

# Post requires alternatives to install javadoc alternative.
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall javadoc alternative.
# in version 1.7 and higher for --family switch

# Standard JPackage javadoc provides.
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc = %{epoch}:%{version}-%{release}


%description javadoc
The OpenJDK API documentation.
%endif

%if %{include_normal_build}
%package javadoc-zip
Summary: OpenJDK API Documentation compressed in single archive
Group:   Development/Java
Requires: javapackages-tools

# Post requires alternatives to install javadoc alternative.
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall javadoc alternative.
# in version 1.7 and higher for --family switch

# Standard JPackage javadoc provides.
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc = %{epoch}:%{version}-%{release}


%description javadoc-zip
The OpenJDK API documentation compressed in single archive.
%endif

%if %{include_debug_build}
%package javadoc-debug
Summary: OpenJDK API Documentation %{for_debug}
Group:   Development/Java
Requires: javapackages-tools


%description javadoc-debug
The OpenJDK API documentation %{for_debug}.
%endif

%if %{include_debug_build}
%package javadoc-zip-debug
Summary: OpenJDK API Documentation compressed in single archive %{for_debug}
Group:   Development/Java
Requires: javapackages-tools


%description javadoc-zip-debug
The OpenJDK API documentation compressed in single archive %{for_debug}.
%endif


%if %{include_normal_build}
%package accessibility
Group: Development/Other
Summary: OpenJDK accessibility connector

Requires: java-atk-wrapper
Requires: %{name} = %{epoch}:%{version}-%{release}

Provides: java-%{javaver}-%{origin}-accessiblity = %{epoch}:%{version}-%{release}

%description accessibility
Enables accessibility support in OpenJDK by using java-atk-wrapper. This allows
compatible at-spi2 based accessibility programs to work for AWT and Swing-based
programs.

Please note, the java-atk-wrapper is still in beta, and OpenJDK itself is still
being tuned to be working with accessibility features. There are known issues
with accessibility on, so please do not install this package unless you really
need to.
%endif

%if %{include_debug_build}
%package accessibility-debug
Group: Development/Other
Summary: OpenJDK accessibility connector %{for_debug}


%description accessibility-debug
See normal java-%{version}-openjdk-accessibility description.
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
  echo "you have disabled both include_debug_build and include_debug_build. no go."
  exit 13
fi
%setup -q -c -n %{uniquesuffix ""} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 7 ] ; then
 echo "priority must be 7 digits in total, violated"
 exit 14
fi
cp %{SOURCE2} .

# OpenJDK patches

# Remove libraries that are linked
pushd openjdk
sh %{SOURCE12}
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch12 -p1
%patch13 -p1

# s390 build fixes
%ifarch s390
%patch100 -p1
%patch102 -p1
%endif

%patch101 -p1
#%patch103 -p1
%patch104 -p1

# Zero PPC fixes.
#  TODO: propose them upstream
%patch400 -p1

%patch401 -p1
pushd hotspot
%patch402 -p1
%patch403 -p1
%patch404 -p1
%patch405 -p1
popd

popd # openjdk

%patch1000

# Extract systemtap tapsets
%if_enabled systemtap
tar -x -I xz -f %{SOURCE8}
#%patch300
%if %{include_debug_build}
cp -r tapset tapset%{debug_suffix}
%endif


for suffix in %{build_loop} ; do
  for file in "tapset"$suffix/*.in; do
    OUTPUT_FILE=`echo $file | sed -e s:%{javaver}\.stp\.in$:%{version}-%{release}.%{_arch}.stp:g`
    sed -e s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/lib/server/libjvm.so:g $file > $file.1
# TODO find out which architectures other than i686 have a client vm
%ifarch %{ix86}
    sed -e s:@ABS_CLIENT_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/lib/client/libjvm.so:g $file.1 > $OUTPUT_FILE
%else
    sed -e '/@ABS_CLIENT_LIBJVM_SO@/d' $file.1 > $OUTPUT_FILE
%endif
    sed -i -e s:@ABS_JAVA_HOME_DIR@:%{_jvmdir}/%{sdkdir}:g $OUTPUT_FILE
    sed -i -e s:@INSTALL_ARCH_DIR@:%{archinstall}:g $OUTPUT_FILE
    sed -i -e s:@prefix@:%{_jvmdir}/%{sdkdir}/:g $OUTPUT_FILE
  done
done
# systemtap tapsets ends
%endif

# Prepare desktop files
for suffix in %{build_loop} ; do
for file in %{SOURCE9} %{SOURCE10} ; do
    FILE=`basename $file | sed -e s:\.in$::g`
    EXT="${FILE##*.}"
    NAME="${FILE%.*}"
    OUTPUT_FILE=$NAME$suffix.$EXT
    sed -e s:#JAVA_HOME#:%{sdkbindir}:g $file > $OUTPUT_FILE
    sed -i -e  s:#JRE_HOME#:%{jrebindir}:g $OUTPUT_FILE
    sed -i -e  s:#ARCH#:%{_arch}$suffix:g $OUTPUT_FILE
done
done
%patch33 -p0
%patch34 -p0
%patch35 -p0
%patch36 -p0

# Setup nss.cfg
#sed -e s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g %{SOURCE11} > nss.cfg


%build
# zerg's girar armh hack:
(while true; do date; sleep 7m; done) &
# end armh hack, kill it when girar will be fixed
# How many cpu's do we have?
export NUM_PROC=%(/usr/bin/getconf _NPROCESSORS_ONLN 2> /dev/null || :)
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

EXTRA_CFLAGS="-fstack-protector-strong"
#see https://bugzilla.redhat.com/show_bug.cgi?id=1120792
EXTRA_CFLAGS="$EXTRA_CFLAGS -Wno-error"
EXTRA_CFLAGS="$EXTRA_CFLAGS -fcommon"
EXTRA_CPP_FLAGS="-Wno-error"
EXTRA_CPP_FLAGS="$EXTRA_CPP_FLAGS -fcommon"
%ifarch %{power64} ppc
# fix rpmlint warnings
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif

%if 0%{?fedora} > 23
EXTRA_CFLAGS="$EXTRA_CFLAGS -Wno-error -std=gnu++98  -fno-delete-null-pointer-checks -fno-lifetime-dse -fpermissive"
EXTRA_CPP_FLAGS="$EXTRA_CPP_FLAGS -Wno-error -std=gnu++98 -fno-delete-null-pointer-checks -fno-lifetime-dse"
%endif

(cd openjdk/common/autoconf
 bash ./autogen.sh
)

for suffix in %{build_loop} ; do
if [ "$suffix" = "%{debug_suffix}" ] ; then
debugbuild=%{debugbuild_parameter}
else
debugbuild=%{normalbuild_parameter}
fi

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
    --with-boot-jdk=/usr/lib/jvm/java-1.8.0-openjdk \
%else
    --with-boot-jdk=/usr/lib/jvm/java-9-openjdk \
%endif
    --with-debug-level=$debugbuild \
    --with-native-debug-symbols=internal \
    --enable-unlimited-crypto \
    --with-zlib=system \
    --with-libjpeg=system \
    --with-giflib=system \
    --with-libpng=system \
    --with-lcms=system \
    --with-stdc++lib=dynamic \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --with-num-cores="$NUM_PROC" \
    --disable-javac-server \
    --disable-warnings-as-errors

make \
    JAVAC_FLAGS=-g \
    LOG=trace \
    WARNINGS_ARE_ERRORS="-Wno-error" \
    CFLAGS_WARNINGS_ARE_ERRORS="-Wno-error" \
    %{targets}

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

#build cycles
done

%check

# We test debug first as it will give better diagnostics on a crash
for suffix in %{rev_build_loop} ; do

export JAVA_HOME=$(pwd)/%{buildoutputdir}/images/%{jdkimage}

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE13}
$JAVA_HOME/bin/java --add-opens java.base/javax.crypto=ALL-UNNAMED TestCryptoLevel

# Check ECC is working
$JAVA_HOME/bin/javac -d . %{SOURCE14}
#FIXME make it run after system NSS support?
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE14})|sed "s|\.java||") || true

# Check debug symbols are present and can identify code
find "$JAVA_HOME" -iname '*.so' -print0 | while read -d $'\0' lib
do
  if [ -f "$lib" ] ; then
    echo "Testing $lib for debug symbols"
    # All these tests rely on RPM failing the build if the exit code of any set
    # of piped commands is non-zero.

    # Test for .debug_* sections in the shared object. This is the  main test.
    # Stripped objects will not contain these.
    eu-readelf -S "$lib" | grep "] .debug_"
    test $(eu-readelf -S "$lib" | grep -E "\]\ .debug_(info|abbrev)" | wc --lines) == 2

    # Test FILE symbols. These will most likely be removed by anyting that
    # manipulates symbol tables because it's generally useless. So a nice test
    # that nothing has messed with symbols.
    old_IFS="$IFS"
    IFS=$'\n'
    for line in $(eu-readelf -s "$lib" | grep "00000000      0 FILE    LOCAL  DEFAULT")
    do
     # We expect to see .cpp files, except for architectures like aarch64 and
     # s390 where we expect .o and .oS files
      echo "$line" | grep -E "ABS ((.*/)?[-_a-zA-Z0-9]+\.(c|cc|cpp|cxx|o|oS))?$"
    done
    IFS="$old_IFS"

    # If this is the JVM, look for javaCalls.(cpp|o) in FILEs, for extra sanity checking.
    if [ "`basename $lib`" = "libjvm.so" ]; then
      eu-readelf -s "$lib" | \
        grep -E "00000000      0 FILE    LOCAL  DEFAULT      ABS javaCalls.(cpp|o)$"
    fi

    # Test that there are no .gnu_debuglink sections pointing to another
    # debuginfo file. There shouldn't be any debuginfo files, so the link makes
    # no sense either.
    eu-readelf -S "$lib" | grep 'gnu'
    if eu-readelf -S "$lib" | grep '] .gnu_debuglink' | grep PROGBITS; then
      echo "bad .gnu_debuglink section."
      eu-readelf -x .gnu_debuglink "$lib"
      false
    fi
  fi
done

# Make sure gdb can do a backtrace based on line numbers on libjvm.so
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

#build cycles check
done

%install
STRIP_KEEP_SYMTAB=libjvm*

for suffix in %{build_loop} ; do

# Install the jdk
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}
cp -a %{buildoutputdir}/images/%{jdkimage} \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}


# Install symlink to default soundfont
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/audio
pushd $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/audio
ln -s %{_datadir}/soundfonts/default.sf2
popd

#install jsa directories so we can owe them
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/%{archinstall}/server/
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/%{archinstall}/client/

pushd %{buildoutputdir}/images/%{jdkimage}

%if_enabled systemtap
  # Install systemtap support files.
  install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset
  # note, that uniquesuffix  is in BUILD dir in this case
  cp -a $RPM_BUILD_DIR/%{uniquesuffix ""}/tapset$suffix/*.stp $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset/
  pushd  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset/
   tapsetFiles=`ls *.stp`
  popd
  install -d -m 755 $RPM_BUILD_ROOT%{tapsetdir}
  pushd $RPM_BUILD_ROOT%{tapsetdir}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{sdkdir}/tapset %{tapsetdir})
    for name in $tapsetFiles ; do
      targetName=`echo $name | sed "s/.stp/$suffix.stp/"`
      ln -sf $RELATIVE/$name $targetName
    done
  popd
%endif

  # Remove empty cacerts database.
  rm -f $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/security/cacerts
  # Install cacerts symlink needed by some apps which hardcode the path.
  pushd $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/security
  #  RELATIVE=$(%{abs2rel} %{_sysconfdir}/pki/java \
  #    %{_jvmdir}/%{sdkdir}/lib/security)
      ln -sf /etc/pki/java/cacerts .
  popd

  # Install versioned symlinks.
  pushd $RPM_BUILD_ROOT%{_jvmdir}
    ln -sf %{sdkdir} %{jrelnk}
  popd


  # Install man pages.
  install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
  for manpage in man/man1/*
  do
    # Convert man pages to UTF8 encoding.
    iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
    mv -f $manpage.tmp $manpage
    install -m 644 -p $manpage $RPM_BUILD_ROOT%{_mandir}/man1/$(basename \
      $manpage .1)%{label}.1
  done
  # Remove man pages from jdk image
  rm -rf $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/man

popd


# Install Javadoc documentation.
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
cp -a %{buildoutputdir}/images/docs $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}
cp -a %{buildoutputdir}/bundles/jdk-%{newjavaver}+%{buildver}-docs.zip  $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}.zip

# Install icons and menu entries.
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    openjdk/jdk/src/java.desktop/unix/classes/sun/awt/X11/java-icon${s}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}.png
done

# Install desktop files.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole$suffix policytool$suffix ; do
    desktop-file-install --vendor=%{uniquesuffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

# FIXME: remove SONAME entries from demo DSOs.  See
# https://bugzilla.redhat.com/show_bug.cgi?id=436497

# Find non-documentation demo files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample \
  -type f -o -type l | sort \
  | grep -v README \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  >> %{name}-demo.files"$suffix"
# Find documentation demo files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample \
  -type f -o -type l | sort \
  | grep README \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  | sed 's|^|%%doc |' \
  >> %{name}-demo.files"$suffix"

# TODO find out how to use ext in jdk9

# intentionally after the files generation, as it goes to separate package
# Create links which leads to separately installed java-atk-bridge and allow configuration
# links points to java-atk-wrapper - an dependence
  #pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/lib/%{archinstall}
  #  ln -s %{_libdir}/java-atk-wrapper/libatk-wrapper.so.0 libatk-wrapper.so
  #popd
  #pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/lib/ext
  #   ln -s %{_libdir}/java-atk-wrapper/java-atk-wrapper.jar  java-atk-wrapper.jar
  #popd
  pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/conf/
    echo "#Config file to  enable java-atk-wrapper" > accessibility.properties
    echo "" >> accessibility.properties
    echo "assistive_technologies=org.GNOME.Accessibility.AtkWrapper" >> accessibility.properties
    echo "" >> accessibility.properties
  popd

# moving configfiles to /etc
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

# end, dual install
done
for rpm404_ghostdir in %{_jvmdir}/%{sdkdir}/lib/client/
do
    mkdir -p %buildroot`dirname "$rpm404_ghostdir"`
done
for rpm404_ghost in %{_jvmdir}/%{sdkdir}/lib/server/classes.jsa %{_jvmdir}/%{sdkdir}/lib/client/classes.jsa
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done


# touching all ghosts; hack for rpm 4.0.4

%if %{include_normal_build} 
# intentioanlly only for non-debug
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
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}.png
%{_datadir}/applications/*policytool.desktop
%{_jvmdir}/%{sdkdir}/lib/libjsoundalsa.so
%{_jvmdir}/%{sdkdir}/lib/libsplashscreen.so
%{_jvmdir}/%{sdkdir}/lib/libawt_xawt.so
%{_jvmdir}/%{sdkdir}/lib/libjawt.so
%{_jvmdir}/%{sdkdir}/bin/policytool
%else
%{_jvmdir}/%{sdkdir}/lib/audio/default.sf2
%files
# placeholder
%endif


%if %{include_normal_build} 
%files headless
%_altdir/%altname-java-headless
%_sysconfdir/buildreqs/packages/substitute.d/%name-headless
# important note, see https://bugzilla.redhat.com/show_bug.cgi?id=1038092 for whole issue 
# all config/norepalce files (and more) have to be declared in pretrans. See pretrans
%dir %{_sysconfdir}/.java/.systemPrefs
%dir %{_sysconfdir}/.java
%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{sdkdir}/legal
%{_jvmdir}/%{sdkdir}/release
%{_jvmdir}/%{jrelnk}
%dir %{_jvmdir}/%{sdkdir}/bin
%{_jvmdir}/%{sdkdir}/bin/appletviewer
%{_jvmdir}/%{sdkdir}/bin/idlj
%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/%{sdkdir}/bin/jjs
%{_jvmdir}/%{sdkdir}/bin/jrunscript
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
%{_jvmdir}/%{sdkdir}/lib/libjsig.so
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
%{_jvmdir}/%{sdkdir}/lib/libunpack.so
%{_jvmdir}/%{sdkdir}/lib/libverify.so
%{_jvmdir}/%{sdkdir}/lib/libzip.so
%{_mandir}/man1/appletviewer%{label}.1*
%{_mandir}/man1/idlj%{label}.1*
%{_mandir}/man1/java%{label}.1*
%{_mandir}/man1/jjs%{label}.1*
%{_mandir}/man1/jrunscript%{label}.1*
%{_mandir}/man1/jstatd%{label}.1*
%{_mandir}/man1/keytool%{label}.1*
%{_mandir}/man1/orbd%{label}.1*
%{_mandir}/man1/pack200%{label}.1*
%{_mandir}/man1/rmid%{label}.1*
%{_mandir}/man1/rmiregistry%{label}.1*
%{_mandir}/man1/servertool%{label}.1*
%{_mandir}/man1/tnameserv%{label}.1*
%{_mandir}/man1/unpack200%{label}.1*
%{_mandir}/man1/policytool%{label}.1*
%{_jvmdir}/%{sdkdir}/lib/audio/
%{_jvmdir}/%{sdkdir}/lib/server/
%ghost %{_jvmdir}/%{sdkdir}/lib/client/
%ifarch %{jit_arches}
%ifnarch %{power64}
%attr(644, root, root) %ghost %{_jvmdir}/%{sdkdir}/lib/server/classes.jsa
%attr(644, root, root) %ghost %{_jvmdir}/%{sdkdir}/lib/client/classes.jsa
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
%config  %{etcjavadir}/conf/management/jmxremote.password.template
%config(noreplace) %{etcjavadir}/conf/management/management.properties
%config(noreplace) %{etcjavadir}/conf/net.properties
%config(noreplace) %{etcjavadir}/conf/sound.properties
%config  %{etcjavadir}/conf/accessibility.properties
%{_jvmdir}/%{sdkdir}/conf
%{_jvmdir}/%{sdkdir}/lib/security
%exclude %{_jvmdir}/%{sdkdir}/lib/audio/default.sf2

%files devel
%_altdir/%altname-javac
%_altdir/%altname-javac-versioned
%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%{_jvmdir}/%{sdkdir}/legal
%dir %{_jvmdir}/%{sdkdir}/bin
%{_jvmdir}/%{sdkdir}/bin/appletviewer
%{_jvmdir}/%{sdkdir}/bin/idlj
%{_jvmdir}/%{sdkdir}/bin/jar
%{_jvmdir}/%{sdkdir}/bin/jarsigner
%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/%{sdkdir}/bin/javadoc
%{_jvmdir}/%{sdkdir}/bin/javah
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
%{_jvmdir}/%{sdkdir}/lib/libjelfshim.so
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
%{_mandir}/man1/javah%{label}.1*
%{_mandir}/man1/javap%{label}.1*
%{_mandir}/man1/jconsole%{label}.1*
%{_mandir}/man1/jcmd%{label}.1*
%{_mandir}/man1/jdb%{label}.1*
%{_mandir}/man1/jdeps%{label}.1*
#FIXME enable when aviablable
#%{_mandir}/man1/jdeprscan-%{uniquesuffix}.1*
#FIXME enable when aviablable
#%{_mandir}/man1/jimage-%{uniquesuffix}.1*
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
%{tapsetroot}
%endif

%files jmods
%{_jvmdir}/%{sdkdir}/jmods

%files demo -f %{name}-demo.files
%{_jvmdir}/%{sdkdir}/legal

%files src
%doc README.md
%{_jvmdir}/%{sdkdir}/lib/src.zip

%files javadoc
%_altdir/%altname-javadoc
%_sysconfdir/buildreqs/packages/substitute.d/%name-javadoc
%doc %{_javadocdir}/%{uniquejavadocdir}
%doc --no-dereference %{buildoutputdir}/images/%{jdkimage}/legal

%files javadoc-zip
%doc %{_javadocdir}/%{uniquejavadocdir}.zip
%doc --no-dereference %{buildoutputdir}/images/%{jdkimage}/legal

%files accessibility
#%{_jvmdir}/%{sdkdir}/lib/%{archinstall}/libatk-wrapper.so
#%{_jvmdir}/%{sdkdir}/lib/ext/java-atk-wrapper.jar
#%{_jvmdir}/%{etcjavadir}/conf/accessibility.properties
%endif

%if %{include_debug_build} 
%files debug

%files headless-debug

%files devel-debug

%files jmods-debug

%files demo-debug -f %{name}-demo.files-debug

%files src-debug

%files javadoc-debug

%files javadoc-zip-debug

%files accessibility-debug
%endif


%changelog
* Sat Feb 06 2021 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt8_6jpp8.M90P.1
- p9 bootstrap build for armh

* Thu Dec 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt8_6jpp9
- added alternatives for keytool,policytool,etc

* Sat Dec 12 2020 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt7_6jpp9
- use zerg@'s hack for armh

* Tue Nov 24 2020 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt6_6jpp9
- returned normal priority for java 9

* Mon Nov 23 2020 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt5_6jpp9
- added jjs alternative and fixed /usr/bin/jjs provides

* Sat Nov 07 2020 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt4_6jpp9
- non-bootstrap build with java9

* Tue Oct 06 2020 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt4_6jpp8
- fixed build

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt2_6jpp8.M90P.1
- backport

* Tue Jul 09 2019 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt3_6jpp8
- updated alternatives layout again

* Mon Jul 08 2019 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt2_6jpp8
- new alternatives layout

* Fri Jul 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:9.0.4.11-alt1_6jpp8
- new version

