# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-generic-compat
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%define with_systemtap 0
# 1.7.0 - added manually
BuildRequires: libfreetype-devel libkrb5-devel
BuildRequires: pkgconfig(gtk+-2.0)
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
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version and %%release is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name java-1.7.0-openjdk
%define version 1.7.0.221
%define release 2.6.18.0
# If debug is 1, OpenJDK is built with all debug info present.
%global debug 0

# we remove the build id notes explicitly to avoid generating (potentially
# conflicting) files in the -debuginfo package
%undefine _missing_build_ids_terminate_build

%global icedtea_version 2.6.18
%global icedtea_snapshot %{nil}
%global hg_tag icedtea-%{icedtea_version}%{icedtea_snapshot}

%global aarch64			aarch64 arm64 armv8
#sometimes we need to distinguish big and little endian PPC64
%global ppc64le			ppc64le
%global ppc64be			ppc64 ppc64p7
%global multilib_arches %{power64} sparc64 x86_64 
%global jit_arches		%{ix86} x86_64 sparcv9 sparc64 %{ppc64be} %{ppc64le} %{aarch64}

# With disabled nss is NSS deactivated, so in NSS_LIBDIR can be wrong path
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

# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=1111349.
# See also https://bugzilla.redhat.com/show_bug.cgi?id=1590796
# as to why some libraries *cannot* be excluded. In particular,
# these are:
# libjsig.so, libjava.so, libjawt.so, libjvm.so and libverify.so
#%global _privatelibs libatk-wrapper[.]so.*|libattach[.]so.*|libawt_headless[.]so.*|libawt[.]so.*|libawt_xawt[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libhprof[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas_unix[.]so.*|libjava_crw_demo[.]so.*|libjavajpeg[.]so.*|libjdwp[.]so.*|libjli[.]so.*|libjsdt[.]so.*|libjsoundalsa[.]so.*|libjsound[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libnpt[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsplashscreen[.]so.*|libsunec[.]so.*|libunpack[.]so.*|libzip[.]so.*|lib[.]so\\(SUNWprivate_.*


# In some cases, the arch used by the JDK does
# not match _arch.
# Also, in some cases, the machine name used by SystemTap
# does not match that given by _build_cpu
%ifarch x86_64
%global archbuild amd64
%global archinstall amd64
%global stapinstall x86_64
%endif
%ifarch ppc
%global archbuild ppc
%global archinstall ppc
%global archdef PPC
%global stapinstall powerpc
%endif
%ifarch %{ppc64be}
%global archbuild ppc64
%global archinstall ppc64
%global archdef PPC
%global stapinstall powerpc
%endif
%ifarch %{ppc64le}
%global archbuild ppc64le
%global archinstall ppc64le
%global archdef PPC64
%global stapinstall powerpc
%endif
%ifarch %{ix86}
%global archbuild i586
%global archinstall i386
%global stapinstall i386
%endif
%ifarch ia64
%global archbuild ia64
%global archinstall ia64
%global stapinstall ia64
%endif
%ifarch s390
%global archbuild s390
%global archinstall s390
%global archdef S390
%global stapinstall s390
%endif
%ifarch s390x
%global archbuild s390x
%global archinstall s390x
%global archdef S390
%global stapinstall s390
%endif
%ifarch %{arm}
%global archbuild arm
%global archinstall arm
%global archdef ARM
%global stapinstall arm
%endif
%ifarch %{aarch64}
%global archbuild aarch64
%global archinstall aarch64
%global archdef AARCH64
%global stapinstall arm64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archbuild sparc
%global archinstall sparc
%global stapinstall %{_build_cpu}
%endif
# 64 bit sparc
%ifarch sparc64
%global archbuild sparcv9
%global archinstall sparcv9
%global stapinstall %{_build_cpu}
%endif
%ifnarch %{jit_arches}
%global archbuild %{_arch}
%global archinstall %{_arch}
%endif

%if %{debug}
%global debugbuild debug_build
%else
%global debugbuild %{nil}
%endif

# If hsbootstrap is 1, build HotSpot alone first and use that in the bootstrap JDK
# You can turn this on to avoid issues where HotSpot is broken in the bootstrap JDK
%ifarch %{jit_arches}
%global hsbootstrap 1
%else
%global hsbootstrap 0
%endif

%global with_pulseaudio 1

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

# Hard-code libdir on 64-bit architectures to make the 64-bit JDK
# simply be another alternative.
%global LIBDIR       %{_libdir}
#backuped original one
%ifarch %{multilib_arches}
%global syslibdir       %{_libdir}
%else
%global syslibdir       %{_libdir}
%endif

# Standard JPackage naming and versioning defines.
%global origin          openjdk
%global top_level_dir_name   %{origin}
%global updatever       221
%global buildver        02
# Keep priority on 7digits in case updatever>9
%global priority        1700%{updatever}
%global javaver         1.7.0

%global fullversion     %{name}-%{version}-%{release}

%global uniquesuffix          %{fullversion}.%{_arch}

%global sdkdir          %{uniquesuffix}
%global jrelnk          jre-%{javaver}-%{origin}-%{version}-%{release}.%{_arch}

%global jredir          %{sdkdir}/jre
%global sdkbindir       %{_jvmdir}/%{sdkdir}/bin
%global jrebindir       %{_jvmdir}/%{jredir}/bin
%global jvmjardir       %{_jvmjardir}/%{uniquesuffix}

%global rpm_state_dir %{_localstatedir}/lib/rpm-state/

#we can copy the javadoc to not arched dir, or made it not noarch
%global uniquejavadocdir       %{fullversion}

%ifarch %{jit_arches}
# Where to install systemtap tapset (links)
# We would like these to be in a package specific subdir,
# but currently systemtap doesn't support that, so we have to
# use the root tapset dir for now. To distinquish between 64
# and 32 bit architectures we place the tapsets under the arch
# specific dir (note that systemtap will only pickup the tapset
# for the primary arch for now). Systemtap uses the machine name
# aka build_cpu as architecture specific directory name.
%global tapsetroot /usr/share/systemtap
%global tapsetdir %{tapsetroot}/tapset/%{stapinstall}
%endif

%if %{debug}
%global buildoutputdir %{top_level_dir_name}/build/linux-%{archbuild}-debug
%else
%global buildoutputdir %{top_level_dir_name}/build/linux-%{archbuild}
%endif

# Prevent brp-java-repack-jars from being run.
%global __jar_repack 0

Name:    java-%{javaver}-%{origin}
Version: %{javaver}.%{updatever}
Release: alt2_2.6.18.0jpp8
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
# JavaScript support is provided by Rhino, which is licensed under MPLv1.1
License:  ASL 1.1 and ASL 2.0 and BSD and BSD with advertising and GPL+ and GPLv2 and GPLv2 with exceptions and IJG and LGPLv2+ and MIT and MPLv1.1 and MPLv2.0 and Public Domain and W3C and zlib
URL:      http://openjdk.java.net/

# Source from upstream IcedTea 2.x project. To regenerate, use
# VERSION=icedtea-${icedtea_version} FILE_NAME_ROOT=openjdk-${VERSION}
# REPO_ROOT=<path to checked-out repository> generate_source_tarball.sh
Source0:  openjdk-icedtea-%{icedtea_version}%{icedtea_snapshot}.tar.xz

# README file
# This source is under maintainer's/java-team's control
Source2:  README.src

# Sources 6-12 are taken from hg clone http://icedtea.classpath.org/hg/icedtea7
# Unless said differently, there is directory with required sources which should be enough to pack/rename

# Class rewrite to rewrite rhino hierarchy
Source5: class-rewriter.tar.gz

# Systemtap tapsets. Zipped up to keep it small.
# last update from IcedTea 2.6.10
Source6: systemtap-tapset-2.6.12.tar.xz

# .desktop files. 
Source7:  policytool.desktop
Source77: jconsole.desktop

# nss configuration file
Source8: nss.cfg

# FIXME: Taken from IcedTea snapshot 877ad5f00f69, but needs to be moved out
# hg clone -r 877ad5f00f69 http://icedtea.classpath.org/hg/icedtea7
Source9: pulseaudio.tar.gz

# Removed libraries that we link instead
Source10: remove-intree-libraries.sh

#http://icedtea.classpath.org/hg/icedtea7/file/933d082ec889/fsg.sh
# file to clean tarball, should be ketp updated as possible
Source1111: fsg.sh

# Remove build ids from binaries
Source11: remove-buildids.sh

# Ensure we aren't using the limited crypto policy
Source12: TestCryptoLevel.java

Source13: java-abrt-launcher

Source20: repackReproduciblePolycies.sh

# RPM/distribution specific patches

# Allow TCK to pass with access bridge wired in
Patch1:   rh1648645-java_access_bridge_loading_java_version_privileged_tck.patch

# Disable access to access-bridge packages by untrusted apps
Patch3:   rh1648644-java_access_bridge_privlidged_security.patch

# Ignore AWTError when assistive technologies are loaded 
Patch4:   rh1648242-accessible_toolkit_crash_do_not_break_jvm.patch

# Build docs even in debug
Patch5:   rh1648254-javadoc_generated_during_all_variants_of_buid.patch

# Add debuginfo where missing
Patch6:   rh1648259-libsaproc_libjsig_compiled_with_g_to_provide_correct_debuginfo.patch

#
# OpenJDK specific patches
#

# Add rhino support
Patch100: rh1649777-add_rhino_support_jdk7.patch

Patch106: rh1648643-comment_out_freetype_check.patch

# allow to create hs_pid.log in tmp (in 700 permissions) if working directory is unwritable
Patch200: rh1648241-abrt_friendly_hs_log_jdk7.patch

#
# Optional component packages
#

# Make the ALSA based mixer the default when building with the pulseaudio based
# mixer
Patch300: rh1649760-make_alsa_based_mixer_default_when_pulseaudio_build.patch

# Make the curves reported by Java's SSL implementation match those of NSS
Patch400: pr1834-rh1022017-reduce_ellipticcurvesextension_to_provide_only_three_nss_supported_nist_curves_23_24_25.patch

# Temporary patches

# 8076221, PR2809: Backport "8076221: Disable RC4 cipher suites" (will appear in 2.7.0)
Patch500: jdk8076221-pr2809-disable_rc4_cipher_suites.patch
# PR3393, RH1273760: Support using RSAandMGF1 with the SHA hash algorithms in the PKCS11 provider (will appear in 2.7.0)
Patch501: pr3393-rh1273760-support_rsaandmgf1_with_sha_in_pkcs11.patch
# End of tmp patches

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libalsa-devel
BuildRequires: libcups-devel
BuildRequires: desktop-file-utils
BuildRequires: libgif-devel
# LCMS 2 is disabled until security issues are resolved
#BuildRequires: lcms2-devel >= 2.5
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXp-devel xorg-printproto-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: wget
BuildRequires: xorg-proto-devel
BuildRequires: ant1.9
BuildRequires: libXinerama-devel
# Provides lsb_release for generating distro id in jdk_generic_profile.sh
BuildRequires: lsb-release
BuildRequires: rhino
BuildRequires: zip
BuildRequires: fontconfig
BuildRequires: fonts-type1-xorg
BuildRequires: zlib > 1.2.3
# Require a build JDK which has a working jar uf (PR1437 / RH1207129)
BuildRequires: java-1.7.0-openjdk-devel >= 1.7.0.111
BuildRequires: fontconfig
#BuildRequires: at-spi-devel
BuildRequires: gawk
BuildRequires: xorg-utils
# Requirements for setting up the nss.cfg
BuildRequires: libnss-devel libnss-devel-static
# Required for NIO2
BuildRequires: libattr-devel
# Build requirements for SunEC system NSS support
BuildRequires: libnss-devel >= 3.16.1
# Required for smartcard support
BuildRequires: libpcsclite libpcsclite-devel
# Required for SCTP support
BuildRequires: liblksctp-devel
# Required for fallback native proxy support
BuildRequires: GConf libGConf-devel libGConf-gir-devel
# PulseAudio build requirements.
%if %{with_pulseaudio}
BuildRequires: libpulseaudio-devel >= 0.9.11
%endif
# Zero-assembler build requirement.
%ifnarch %{jit_arches}
BuildRequires: libffi-devel >= 3.0.10
%endif

# cacerts build requirement.
BuildRequires: openssl
# execstack build requirement.
# no prelink on ARM yet
%ifnarch %{arm} %{aarch64} %{ppc64le}
BuildRequires: prelink
%endif
%if_enabled systemtap
#systemtap build requirement.
BuildRequires: systemtap-sdt-devel
%endif

Requires: fontconfig
Requires: fonts-type1-xorg
#requires rest of java
Requires: %{name}-headless = %{epoch}:%{version}-%{release}


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
Provides: %{_jvmdir}/%{jredir}/lib/%archinstall/server/libjvm.so()(64bit)
Provides: %{_jvmdir}/%{jredir}/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)(64bit)
%else
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so()
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)
Provides: %{_jvmdir}/%{jredir}/lib/%archinstall/server/libjvm.so()
Provides: %{_jvmdir}/%{jredir}/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)
%endif
ExcludeArch: aarch64 ppc64le
# self-deps. gcc8 linkage quirk?
%filter_from_requires /^.usr.lib.jvm.java-1.7.0-openjdk-1.7.0.*jre.lib/d
Source45: rhino.jar
Patch33: java-1.7.0-openjdk-alt-no-Werror.patch

# Obsolete older 1.6 packages as it cannot use the new bytecode
# Obsoletes: java-1.6.0-openjdk
# Obsoletes: java-1.6.0-openjdk-demo
# Obsoletes: java-1.6.0-openjdk-devel
# Obsoletes: java-1.6.0-openjdk-javadoc
# Obsoletes: java-1.6.0-openjdk-src

%description
The OpenJDK runtime environment.

%package headless
Summary: The OpenJDK runtime environment without audio and video support
Group:   Development/Other

# LCMS 2 is disabled until security issues are resolved
#Requires: lcms2 >= 2.5
Requires: libjpeg
# Require /etc/pki/java/cacerts.
Requires: ca-trust
# Require jpackage-utils for ant.
Requires: jpackage-utils >= 1.7.3
# Require zoneinfo data provided by tzdata-java subpackage.
Requires: tzdata-java
# there is need to depnd on exact version of nss
Requires: libnss %{NSS_BUILDTIME_VERSION}
Requires: libnss %{NSSSOFTOKN_BUILDTIME_VERSION}
# tool to copy jdk's configs - should be Recommends only, but then only dnf/yum eforce it, not rpm transaction and so no configs are persisted when pure rpm -u is run. I t may be consiedered as regression
#Requires:	copy-jdk-configs >= 3.3
# Post requires alternatives to install tool alternatives.
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall tool alternatives.
# in version 1.7 and higher for --family switch

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
The OpenJDK runtime environment without audio and video 

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
Provides: java-sdk-%{origin} = %{epoch}:%{version}
Provides: java-sdk = %{epoch}:%{javaver}
Provides: java-%{javaver}-devel = %{epoch}:%{version}
Provides: java-devel-%{origin} = %{epoch}:%{version}
Provides: java-devel = %{epoch}:%{javaver}


%description devel
The OpenJDK development tools.

%package demo
Summary: OpenJDK Demos
Group:   Development/Other

Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
The OpenJDK demos.

%package src
Summary: OpenJDK Source Bundle
Group:   Development/Other

Requires: %{name} = %{epoch}:%{version}-%{release}

%description src
The OpenJDK source bundle.

%package javadoc
Summary: OpenJDK API Documentation
Group:   Development/Java
Requires: jpackage-utils
BuildArch: noarch

# Post requires alternatives to install javadoc alternative.
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall javadoc alternative.
# in version 1.7 and higher for --family switch

# Standard JPackage javadoc provides.
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}

%description javadoc
The OpenJDK API documentation.

%package accessibility
Group: Development/Java
Summary: OpenJDK accessibility connector
Requires: java-atk-wrapper
Requires: %{name} = %{epoch}:%{version}-%{release}

%description accessibility
Enables accessibility support in OpenJDK by using java-at-wrapper. This allows compatible at-spi2 based accessibility programs to work for AWT and Swing-based programs.
Please note, the java-atk-wrapper is still in beta, and also OpenJDK itself is still in phase of tuning to be working with accessibility features.
Although working pretty fine, there are known issues with accessibility on, so do not rather install this package unless you really need.

%prep
%setup -q -c -n %{uniquesuffix} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 7 ] ; then
 echo "priority must be 7 digits in total, violated"
 exit 14
fi
cp %{SOURCE2} .

# OpenJDK patches
%patch100

# pulseaudio support
%if %{with_pulseaudio}
%patch300
%endif

# Temporary fixes
%patch500
%patch501
# End of temporary fixes

# ECC fix
%patch400

# Add systemtap patches if enabled
%if_enabled systemtap
%endif

# Remove libraries that are linked
sh %{SOURCE10}

# Extract the rewriter (to rewrite rhino classes)
tar xzf %{SOURCE5}

# Extract systemtap tapsets
%if_enabled systemtap

tar xf %{SOURCE6}

for file in tapset/*.in; do

    OUTPUT_FILE=`echo $file | sed -e s:%{javaver}\.stp\.in$:%{version}-%{release}.stp:g`
    sed -e s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/server/libjvm.so:g $file > $file.1
# FIXME this should really be %if %{has_client_jvm}
%ifarch %{ix86}
    sed -e s:@ABS_CLIENT_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/client/libjvm.so:g $file.1 > $OUTPUT_FILE
%else
    sed -e '/@ABS_CLIENT_LIBJVM_SO@/d' $file.1 > $OUTPUT_FILE
%endif
    sed -i -e s:@INSTALL_ARCH_DIR@:%{archinstall}:g $OUTPUT_FILE
    sed -i -e s:@prefix@:%{_jvmdir}/%{sdkdir $suffix}/:g $OUTPUT_FILE

done

%endif

# Pulseaudio
%if %{with_pulseaudio}
tar xzf %{SOURCE9}
%endif


%patch3
%patch4

%if %{debug}
%patch5
%patch6
%endif

%patch106
%patch200
sed -i -e 's,DEF_OBJCOPY=/usr/bin/objcopy,DEF_OBJCOPY=/usr/bin/NO-objcopy,' openjdk/hotspot/make/linux/makefiles/defs.make
%patch33 -p1

%build
# How many cpu's do we have?
export NUM_PROC=`/usr/bin/getconf _NPROCESSORS_ONLN 2> /dev/null || :`
export NUM_PROC=${NUM_PROC:-1}

# Build IcedTea and OpenJDK.
%ifarch s390x sparc64 alpha %{power64} %{aarch64}
export ARCH_DATA_MODEL=64
%endif
%ifarch alpha
%global archflags "-mieee"
%endif

# Filter out flags from the optflags macro that cause problems with the OpenJDK build
# We filter out -O flags so that the optimisation of HotSpot is not lowered from O3 to O2
# We filter out -Wall which will otherwise cause HotSpot to produce hundreds of thousands of warnings (100+mb logs)
# We replace it with -Wformat (required by -Werror=format-security) and -Wno-cpp to avoid FORTIFY_SOURCE warnings
# We filter out -fexceptions as the HotSpot build explicitly does -fno-exceptions and it's otherwise the default for C++
%global ourflags %(echo %optflags | sed -e 's|-Wall|-Wformat=2 -Wno-cpp -Wno-error=format-nonliteral|')
# Disable RPM CFLAGS for now as the change appears to cause crashes on x86 RHEL 7.5 multilib
#%global ourcppflags %(echo %ourflags | sed -e 's|-fexceptions||' | sed -r -e 's|-O[0-9]*||')
%global ourcppflags "-fstack-protector-strong"
%global ourldflags %{__global_ldflags}

# Build the re-written rhino jar
mkdir -p rhino/{old,new}

# Compile the rewriter
(cd rewriter 
 javac com/redhat/rewriter/ClassRewriter.java
)

# Extract rhino.jar contents and rewrite
(cd rhino/old 
 jar xf %_sourcedir/rhino.jar
)

java -cp rewriter com.redhat.rewriter.ClassRewriter \
    $PWD/rhino/old \
    $PWD/rhino/new \
    org.mozilla \
    sun.org.mozilla

(cd rhino/old
 for file in `find -type f -not -name '*.class'` ; do
     new_file=../new/`echo $file | sed -e 's#org#sun/org#'`
     mkdir -pv `dirname $new_file`
     cp -v $file $new_file
     sed -ie 's#org\.mozilla#sun.org.mozilla#g' $new_file
 done
)

(cd rhino/new
   jar cfm ../rhino.jar META-INF/MANIFEST.MF sun
)

export SYSTEM_JDK_DIR=/usr/lib/jvm/java-1.7.0-openjdk

# Temporary workaround for ppc64le ; RH1191652
# Need to work around the jre arch directory being
# ppc64 instead of the expected ppc64le
# Taken from IcedTea7 bootstrap-directory-stage1 & PR1765
%ifarch %{ppc64le}
STAGE1_BOOT_RUNTIME=jdk/jre/lib/rt.jar
mkdir -p jdk/bin
ln -sfv ${SYSTEM_JDK_DIR}/bin/java jdk/bin/java
ln -sfv ${SYSTEM_JDK_DIR}/bin/javah jdk/bin/javah
ln -sfv ${SYSTEM_JDK_DIR}/bin/rmic jdk/bin/rmic
ln -sfv ${SYSTEM_JDK_DIR}/bin/jar jdk/bin/jar
ln -sfv ${SYSTEM_JDK_DIR}/bin/native2ascii jdk/bin/native2ascii
ln -sfv ${SYSTEM_JDK_DIR}/bin/javac jdk/bin/javac
ln -sfv ${SYSTEM_JDK_DIR}/bin/javap jdk/bin/javap
ln -sfv ${SYSTEM_JDK_DIR}/bin/idlj jdk/bin/idlj
mkdir -p jdk/lib/modules
mkdir -p jdk/jre/lib && \
cp ${SYSTEM_JDK_DIR}/jre/lib/rt.jar ${STAGE1_BOOT_RUNTIME} && \
chmod u+w ${STAGE1_BOOT_RUNTIME}
mkdir -p jdk/lib && \
ln -sfv ${SYSTEM_JDK_DIR}/lib/tools.jar jdk/lib/tools.jar ; \
# Workaround some older ppc64le builds installing to 'ppc64' rather than 'ppc64le'
if test -d ${SYSTEM_JDK_DIR}/jre/lib/ppc64 ; then \
  ln -sfv ${SYSTEM_JDK_DIR}/jre/lib/ppc64 \
    jdk/jre/lib/%{archinstall} ; \
else \
  ln -sfv ${SYSTEM_JDK_DIR}/jre/lib/%{archinstall} \
    jdk/jre/lib/ ; \
fi
if ! test -d jdk/jre/lib/%{archinstall}; \
  then \
  ln -sfv ./%{archbuild} \
    jdk/jre/lib/%{archinstall}; \
fi
mkdir -p jdk/include && \
for i in ${SYSTEM_JDK_DIR}/include/*; do \
  test -r ${i} | continue; \
  i=`basename ${i}`; \
  rm -f jdk/include/${i}; \
  ln -sv ${SYSTEM_JDK_DIR}/include/${i} jdk/include/${i}; \
done;
export JDK_TO_BUILD_WITH=${PWD}/jdk
%else
export JDK_TO_BUILD_WITH=${SYSTEM_JDK_DIR}
%endif


pushd openjdk >& /dev/null

export ALT_BOOTDIR="$JDK_TO_BUILD_WITH"

# Save old umask as jdk_generic_profile overwrites it
oldumask=`umask`

# Set generic profile
%ifnarch %{jit_arches}
export ZERO_BUILD=true
%endif
# LCMS 2 is disabled until security issues are resolved
export LCMS_CFLAGS="disabled"
export LCMS_LIBS="disabled"
export PKGVERSION="ALTLinux-%{release}-%{_arch} u%{updatever}-b%{buildver}"

source jdk/make/jdk_generic_profile.sh

# Restore old umask
umask $oldumask

# LCMS 2 is disabled until security issues are resolved
export SYSTEM_LCMS=false

# Variable used in hs_err hook on build failures
top_dir_abs_path=$(pwd)/%{top_level_dir_name}

%if %{hsbootstrap}

mkdir bootstrap

make \
  UNLIMITED_CRYPTO=true \
  ANT="/usr/bin/ant1.9" \
  DISTRO_NAME="ALTLinux" \
  DISTRO_PACKAGE_VERSION="${PKGVERSION}" \
  JDK_UPDATE_VERSION=`printf "%02d" %{updatever}` \
  JDK_BUILD_NUMBER=b`printf "%02d" %{buildver}` \
  JRE_RELEASE_VERSION=%{javaver}_`printf "%02d" %{updatever}`-b`printf "%02d" %{buildver}` \
  MILESTONE="fcs" \
  ALT_PARALLEL_COMPILE_JOBS="$NUM_PROC" \
  HOTSPOT_BUILD_JOBS="$NUM_PROC" \
  STATIC_CXX="false" \
  RHINO_JAR="$PWD/../rhino/rhino.jar" \
  GENSRCDIR="$PWD/generated.build" \
  FT2_CFLAGS="`pkg-config --cflags freetype2` " \
  FT2_LIBS="`pkg-config --libs freetype2` " \
  DEBUG_CLASSFILES="true" \
  DEBUG_BINARIES="true" \
  STRIP_POLICY="no_strip" \
  JAVAC_WARNINGS_FATAL="false" \
  INSTALL_LOCATION=%{_jvmdir}/%{sdkdir} \
  SYSTEM_NSS="" \
  NSS_LIBS="%{NSS_LIBS} -lfreebl" \
  NSS_CFLAGS="%{NSS_CFLAGS}" \
  ECC_JUST_SUITE_B="true" \
  SYSTEM_GSETTINGS="true" \
  BUILD_JAXP=false BUILD_JAXWS=false BUILD_LANGTOOLS=false BUILD_JDK=false BUILD_CORBA=false \
  ALT_JDK_IMPORT_PATH=${JDK_TO_BUILD_WITH} ALT_OUTPUTDIR=${PWD}/bootstrap \
  EXTRA_CFLAGS="%{ourcppflags}" EXTRA_LDFLAGS="%{ourldflags}" \
  %{debugbuild} || ( pwd; find $top_dir_abs_path -name "hs_err_pid*.log" | xargs cat && false )

export VM_DIR=bootstrap-vm/jre/lib/%{archinstall}/server
cp -dR $(readlink -e ${SYSTEM_JDK_DIR}) bootstrap-vm
rm -vf ${VM_DIR}/libjvm.so
if [ ! -e ${VM_DIR} ] ; then mkdir -p ${VM_DIR}; fi
cp -av bootstrap/hotspot/import/jre/lib/%{archinstall}/server/libjvm.so ${VM_DIR}

export ALT_BOOTDIR=${PWD}/bootstrap-vm
  
%endif

# ENABLE_FULL_DEBUG_SYMBOLS=0 is the internal HotSpot option
# to turn off the stripping of debuginfo. FULL_DEBUG_SYMBOLS
# does the same for product builds, but is ignored on non-product builds.
make \
  UNLIMITED_CRYPTO=true \
  ANT="/usr/bin/ant1.9" \
  DISTRO_NAME="ALTLinux" \
  DISTRO_PACKAGE_VERSION="${PKGVERSION}" \
  JDK_UPDATE_VERSION=`printf "%02d" %{updatever}` \
  JDK_BUILD_NUMBER=b`printf "%02d" %{buildver}` \
  JRE_RELEASE_VERSION=%{javaver}_`printf "%02d" %{updatever}`-b`printf "%02d" %{buildver}` \
  MILESTONE="fcs" \
  ALT_PARALLEL_COMPILE_JOBS="$NUM_PROC" \
  HOTSPOT_BUILD_JOBS="$NUM_PROC" \
  STATIC_CXX="false" \
  RHINO_JAR="$PWD/../rhino/rhino.jar" \
  GENSRCDIR="$PWD/generated.build" \
  FT2_CFLAGS="`pkg-config --cflags freetype2` " \
  FT2_LIBS="`pkg-config --libs freetype2` " \
  DEBUG_CLASSFILES="true" \
  DEBUG_BINARIES="true" \
  STRIP_POLICY="no_strip" \
  JAVAC_WARNINGS_FATAL="false" \
  INSTALL_LOCATION=%{_jvmdir}/%{sdkdir} \
  SYSTEM_NSS="" \
  NSS_LIBS="%{NSS_LIBS} -lfreebl" \
  NSS_CFLAGS="%{NSS_CFLAGS}" \
  ECC_JUST_SUITE_B="true" \
  SYSTEM_GSETTINGS="true" \
  EXTRA_CFLAGS="%{ourcppflags}" EXTRA_LDFLAGS="%{ourldflags}" \
  %{debugbuild} || ( pwd; find $top_dir_abs_path -name "hs_err_pid*.log" | xargs cat && false )

popd >& /dev/null

export JAVA_HOME=$(pwd)/%{buildoutputdir}/j2sdk-image

# Install java-abrt-launcher
mkdir  $JAVA_HOME/jre-abrt
mkdir  $JAVA_HOME/jre-abrt/bin
mv $JAVA_HOME/jre/bin/java $JAVA_HOME/jre-abrt/bin/java
ln -s %{_jvmdir}/%{sdkdir}/jre/lib $JAVA_HOME/jre-abrt/lib
cat %{SOURCE13} | sed -e s:@JAVA_PATH@:%{_jvmdir}/%{sdkdir}/jre-abrt/bin/java:g -e s:@LIB_DIR@:%{LIBDIR}/libabrt-java-connector.so:g >  $JAVA_HOME/jre/bin/java
chmod 755 $JAVA_HOME/jre/bin/java

# Install nss.cfg right away as we will be using the JRE above
cp -a %{SOURCE8} $JAVA_HOME/jre/lib/security/
sed -i -e s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g $JAVA_HOME/jre/lib/security/nss.cfg

# Build pulseaudio and install it to JDK build location
%if %{with_pulseaudio}
pushd pulseaudio
# IT_CFLAGS="-g" is needed so that debug info symbols get produced.
# See RHBZ#1657863.
make JAVA_HOME=$JAVA_HOME -f Makefile.pulseaudio IT_CFLAGS="-g"
cp -pPRf build/native/libpulse-java.so $JAVA_HOME/jre/lib/%{archinstall}/
cp -pPRf build/pulse-java.jar $JAVA_HOME/jre/lib/ext/
popd
%endif

# Copy tz.properties
echo "sun.zoneinfo.dir=/usr/share/javazi" >> $JAVA_HOME/jre/lib/tz.properties

#remove all fontconfig files. This change should be usptreamed soon
rm -f %{buildoutputdir}/j2re-image/lib/fontconfig*.properties.src
rm -f %{buildoutputdir}/j2re-image/lib/fontconfig*.bfc
rm -f %{buildoutputdir}/j2sdk-image/jre/lib/fontconfig*.properties.src
rm -f %{buildoutputdir}/j2sdk-image/jre/lib/fontconfig*.bfc
rm -f %{buildoutputdir}/lib/fontconfig*.properties.src
rm -f %{buildoutputdir}/lib/fontconfig*.bfc

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE12}
$JAVA_HOME/bin/java TestCryptoLevel

sh %{SOURCE11} ${JAVA_HOME}

%check
export JAVA_HOME=$(pwd)/%{buildoutputdir $suffix}/j2sdk-image


%install
unset JAVA_HOME
STRIP_KEEP_SYMTAB=libjvm*

# There used to be a link to the soundfont.
# This is now obsolete following the inclusion of 8140620/PR2710

pushd %{buildoutputdir}/j2sdk-image

#install jsa directories so we can owe them
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{archinstall}/server/
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{archinstall}/client/

  # Install main files.
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  cp -a jre-abrt bin include lib src.zip $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
  cp -a jre/bin jre/lib $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
  cp -a ASSEMBLY_EXCEPTION LICENSE THIRD_PARTY_README $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}

%if_enabled systemtap
  # Install systemtap support files.
  install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset
  cp -a $RPM_BUILD_DIR/%{uniquesuffix}/tapset/*.stp $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset/
  install -d -m 755 $RPM_BUILD_ROOT%{tapsetdir}
  pushd $RPM_BUILD_ROOT%{tapsetdir}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{sdkdir}/tapset %{tapsetdir})
    ln -sf $RELATIVE/*.stp .
  popd
%endif

  # Install cacerts symlink.
  rm -f $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/cacerts
  pushd $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security
    RELATIVE=$(%{abs2rel} %{_sysconfdir}/pki/java \
      %{_jvmdir}/%{jredir}/lib/security)
    ln -sf $RELATIVE/cacerts .
  popd

  # Install extension symlinks.
  install -d -m 755 $RPM_BUILD_ROOT%{jvmjardir}
  pushd $RPM_BUILD_ROOT%{jvmjardir}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{jredir}/lib %{jvmjardir})
    ln -sf $RELATIVE/jsse.jar jsse-%{version}.jar
    ln -sf $RELATIVE/jce.jar jce-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-ldap-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-cos-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-rmi-%{version}.jar
    ln -sf $RELATIVE/rt.jar jaas-%{version}.jar
    ln -sf $RELATIVE/rt.jar jdbc-stdext-%{version}.jar
    ln -sf jdbc-stdext-%{version}.jar jdbc-stdext-3.0.jar
    ln -sf $RELATIVE/rt.jar sasl-%{version}.jar
    for jar in *-%{version}.jar
    do
      if [ x%{version} != x%{javaver} ]
      then
        ln -sf $jar $(echo $jar | sed "s|-%{version}.jar|-%{javaver}.jar|g")
      fi
      ln -sf $jar $(echo $jar | sed "s|-%{version}.jar|.jar|g")
    done
  popd

  # Install JCE policy symlinks.
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmprivdir}/%{uniquesuffix}/jce/vanilla

  # Install versioned symlinks.
  pushd $RPM_BUILD_ROOT%{_jvmdir}
    ln -sf %{jredir} %{jrelnk}
  popd

  pushd $RPM_BUILD_ROOT%{_jvmjardir}
    ln -sf %{sdkdir} %{jrelnk}
  popd

  # Remove javaws man page
  rm -f man/man1/javaws*

  # Install man pages.
  install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
  for manpage in man/man1/*
  do
    # Convert man pages to UTF8 encoding.
    iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
    mv -f $manpage.tmp $manpage
    install -m 644 -p $manpage $RPM_BUILD_ROOT%{_mandir}/man1/$(basename \
      $manpage .1)-%{uniquesuffix}.1
  done

  # Install demos and samples.
  cp -a demo $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  mkdir -p sample/rmi
  mv bin/java-rmi.cgi sample/rmi
  cp -a sample $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}

popd


# Install Javadoc documentation.
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
cp -a %{buildoutputdir}/docs $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}

# Install icons and menu entries.
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    %{top_level_dir_name}/jdk/src/solaris/classes/sun/awt/X11/java-icon${s}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}.png
done

# Install desktop files.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in %{SOURCE7} %{SOURCE77} ; do
    sed -i "s/#ARCH#/%{_arch}-%{release}/g" $e
    sed -i "s|/usr/bin|%{sdkbindir}/|g" $e
    desktop-file-install --vendor=%{uniquesuffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

# Find JRE directories.
find $RPM_BUILD_ROOT%{_jvmdir}/%{jredir} -type d \
  | grep -v jre/lib/security \
  | sed 's|'$RPM_BUILD_ROOT'|%%dir |' \
  > %{name}.files-headless
# Find JRE files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{jredir} -type f -o -type l \
  | grep -v jre/lib/security \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  > %{name}.files.all
#split %{name}.files to %{name}.files-headless and %{name}.files
#see https://bugzilla.redhat.com/show_bug.cgi?id=875408
NOT_HEADLESS=\
"%{_jvmdir}/%{uniquesuffix}/jre/lib/%{archinstall}/libjsoundalsa.so 
%{_jvmdir}/%{uniquesuffix}/jre/lib/%{archinstall}/libpulse-java.so 
%{_jvmdir}/%{uniquesuffix}/jre/lib/%{archinstall}/libsplashscreen.so 
%{_jvmdir}/%{uniquesuffix}/jre/lib/%{archinstall}/libjavagtk.so
%{_jvmdir}/%{uniquesuffix}/jre/lib/%{archinstall}/xawt/libmawt.so
%{_jvmdir}/%{uniquesuffix}/jre/bin/policytool
%{_jvmdir}/%{uniquesuffix}/jre-abrt/lib/%{archinstall}/libjsoundalsa.so 
%{_jvmdir}/%{uniquesuffix}/jre-abrt/lib/%{archinstall}/libpulse-java.so 
%{_jvmdir}/%{uniquesuffix}/jre-abrt/lib/%{archinstall}/libsplashscreen.so 
%{_jvmdir}/%{uniquesuffix}/jre-abrt/lib/%{archinstall}/libjavagtk.so
%{_jvmdir}/%{uniquesuffix}/jre-abrt/lib/%{archinstall}/xawt/libmawt.so"
#filter  %{name}.files from  %{name}.files.all to  %{name}.files-headless
ALL=`cat %{name}.files.all`
for file in $ALL ; do 
  INLCUDE="NO" ; 
  for blacklist in $NOT_HEADLESS ; do
#we can not match normally, because rpmbuild will evaluate !0 result as script failure
    q=`expr match "$file" "$blacklist"` || :
    l=`expr length  "$blacklist"` || :
    if [ $q -eq $l  ]; then 
      INLCUDE="YES" ; 
    fi;
  done
    if [ "x$INLCUDE" = "xNO"  ]; then 
      echo "$file" >> %{name}.files-headless
    else
      echo "$file" >> %{name}.files
    fi
done
# Find demo directories.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample -type d \
  | sed 's|'$RPM_BUILD_ROOT'|%%dir |' \
  > %{name}-demo.files

# FIXME: remove SONAME entries from demo DSOs.  See
# https://bugzilla.redhat.com/show_bug.cgi?id=436497

# Find non-documentation demo files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample \
  -type f -o -type l | sort \
  | grep -v README \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  >> %{name}-demo.files
# Find documentation demo files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample \
  -type f -o -type l | sort \
  | grep README \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  | sed 's|^|%%doc |' \
  >> %{name}-demo.files

# Create links which leads to separately installed java-atk-bridge and allow configuration
# links points to java-atk-wrapper - an dependence
  pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/lib/%{archinstall}
    ln -s %{syslibdir}/java-atk-wrapper/libatk-wrapper.so.0 libatk-wrapper.so
  popd
  pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/lib/ext
     ln -s %{syslibdir}/java-atk-wrapper/java-atk-wrapper.jar  java-atk-wrapper.jar
  popd
  pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/lib/
    echo "#Config file to  enable java-atk-wrapper" > accessibility.properties
    echo "" >> accessibility.properties
    echo "assistive_technologies=org.GNOME.Accessibility.AtkWrapper" >> accessibility.properties
    echo "" >> accessibility.properties
  popd

bash %{SOURCE20} $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir} %{javaver}
# https://bugzilla.redhat.com/show_bug.cgi?id=1183793
touch -t 201401010000 $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir $suffix}/lib/security/java.security
for rpm404_ghost in %{_jvmdir}/%{jredir}/lib/%{archinstall}/server/classes.jsa %{_jvmdir}/%{jredir}/lib/%{archinstall}/client/classes.jsa
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done

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
Exec=%{_jvmdir}/%{jredir}/bin/jcontrol
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
Exec=%{_jvmdir}/%{jredir}/bin/javaws %%u
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
%{_bindir}/java	%{_jvmdir}/%{jredir}/bin/java	%priority
%_man1dir/java.1.gz	%_man1dir/java%{label}.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
# binaries and manuals
for i in keytool policytool servertool pack200 unpack200 \
orbd rmid rmiregistry tnameserv
do
  if [ -e %{_jvmdir}/%{jredir}/bin/$i ]; then
    cat <<EOF >>%buildroot%_altdir/%name-java-headless
%_bindir/$i	%{_jvmdir}/%{jredir}/bin/$i	%{_jvmdir}/%{jredir}/bin/java
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
  fi
done

%if_enabled control_panel
cat <<EOF >>%buildroot%_altdir/%name-java
%{_bindir}/ControlPanel	%{_jvmdir}/%{jredir}/bin/ControlPanel	%{_jvmdir}/%{jredir}/bin/java
%{_bindir}/jcontrol	%{_jvmdir}/%{jredir}/bin/jcontrol	%{_jvmdir}/%{jredir}/bin/java
EOF
%endif
# ----- JPackage compatibility alternatives ------
cat <<EOF >>%buildroot%_altdir/%name-java-headless
%{_jvmdir}/jre	%{_jvmdir}/%{jredir}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{origin}	%{_jvmdir}/%{jredir}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{javaver}	%{_jvmdir}/%{jredir}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{javaver}-%{origin}	%{_jvmdir}/%{jredir}	%{_jvmdir}/%{jredir}/bin/java
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



# intentioanlly only for non-debug
%files -f %{name}.files
%_sysconfdir/buildreqs/packages/substitute.d/%name
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}.png

# important note, see https://bugzilla.redhat.com/show_bug.cgi?id=1038092 for whole issue 
# all config/norepalce files (and more) have to be declared in pretrans. See pretrans
%files headless  -f %{name}.files-headless
%_altdir/%altname-java-headless
%_sysconfdir/buildreqs/packages/substitute.d/%name-headless
%doc %{_jvmdir}/%{sdkdir}/ASSEMBLY_EXCEPTION
%doc %{_jvmdir}/%{sdkdir}/LICENSE
%doc %{_jvmdir}/%{sdkdir}/THIRD_PARTY_README
%dir %{_jvmdir}/%{sdkdir}
%dir %{_jvmdir}/%{sdkdir}/jre/lib/
%dir %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}
%ifarch x86_64
%dir %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/xawt
%endif
%{_jvmdir}/%{jrelnk}
%{_jvmjardir}/%{jrelnk}
%{_jvmprivdir}/*
%{jvmjardir}
%dir %{_jvmdir}/%{jredir}/lib/security
%{_jvmdir}/%{jredir}/lib/security/cacerts
%dir %{_jvmdir}/%{jredir %%1}/lib/security/policy/unlimited/
%dir %{_jvmdir}/%{jredir %%1}/lib/security/policy/limited/
%dir %{_jvmdir}/%{jredir %%1}/lib/security/policy/
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/policy/unlimited/US_export_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/policy/unlimited/local_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/policy/limited/US_export_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/policy/limited/local_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/blacklisted.certs
%config(noreplace) %{_jvmdir}/%{jredir}/lib/logging.properties
%{_mandir}/man1/java-%{uniquesuffix}.1*
%{_mandir}/man1/keytool-%{uniquesuffix}.1*
%{_mandir}/man1/orbd-%{uniquesuffix}.1*
%{_mandir}/man1/pack200-%{uniquesuffix}.1*
%{_mandir}/man1/rmid-%{uniquesuffix}.1*
%{_mandir}/man1/rmiregistry-%{uniquesuffix}.1*
%{_mandir}/man1/servertool-%{uniquesuffix}.1*
%{_mandir}/man1/tnameserv-%{uniquesuffix}.1*
%{_mandir}/man1/unpack200-%{uniquesuffix}.1*
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/nss.cfg
# removed %%{_jvmdir}/%%{jredir}/lib/audio/
# see soundfont in %%install
%ifarch %{jit_arches}
%attr(444, root, root) %ghost %{_jvmdir}/%{jredir}/lib/%{archinstall}/server/classes.jsa
%attr(444, root, root) %ghost %{_jvmdir}/%{jredir}/lib/%{archinstall}/client/classes.jsa
%endif
%{_jvmdir}/%{jredir}/lib/%{archinstall}/server/
%{_jvmdir}/%{jredir}/lib/%{archinstall}/client/
%{_sysconfdir}/.java/
%{_sysconfdir}/.java/.systemPrefs
%{_jvmdir}/%{sdkdir}/jre-abrt
# sisyphus_check
%dir %{_jvmdir}/%{jredir}/lib/security/policy
%dir %{_jvmdir}/%{jredir}/lib/security/policy/limited
%dir %{_jvmdir}/%{jredir}/lib/security/policy/unlimited


%files devel
%_altdir/%altname-javac
%_altdir/%altname-javac-versioned
%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%doc %{_jvmdir}/%{sdkdir}/ASSEMBLY_EXCEPTION
%doc %{_jvmdir}/%{sdkdir}/LICENSE
%doc %{_jvmdir}/%{sdkdir}/THIRD_PARTY_README
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/lib
%if_enabled systemtap
%dir %{_jvmdir}/%{sdkdir}/tapset
%endif
%{_jvmdir}/%{sdkdir}/bin/*
%{_jvmdir}/%{sdkdir}/include/*
%{_jvmdir}/%{sdkdir}/lib/*
%if_enabled systemtap
%{_jvmdir}/%{sdkdir}/tapset/*.stp
%endif
%{_jvmjardir}/%{sdkdir}
%{_datadir}/applications/*jconsole.desktop
%{_datadir}/applications/*policytool.desktop
%{_mandir}/man1/appletviewer-%{uniquesuffix}.1*
%{_mandir}/man1/apt-%{uniquesuffix}.1*
%{_mandir}/man1/extcheck-%{uniquesuffix}.1*
%{_mandir}/man1/idlj-%{uniquesuffix}.1*
%{_mandir}/man1/jar-%{uniquesuffix}.1*
%{_mandir}/man1/jarsigner-%{uniquesuffix}.1*
%{_mandir}/man1/javac-%{uniquesuffix}.1*
%{_mandir}/man1/javadoc-%{uniquesuffix}.1*
%{_mandir}/man1/javah-%{uniquesuffix}.1*
%{_mandir}/man1/javap-%{uniquesuffix}.1*
%{_mandir}/man1/jconsole-%{uniquesuffix}.1*
%{_mandir}/man1/jcmd-%{uniquesuffix}.1*
%{_mandir}/man1/jdb-%{uniquesuffix}.1*
%{_mandir}/man1/jhat-%{uniquesuffix}.1*
%{_mandir}/man1/jinfo-%{uniquesuffix}.1*
%{_mandir}/man1/jmap-%{uniquesuffix}.1*
%{_mandir}/man1/jps-%{uniquesuffix}.1*
%{_mandir}/man1/jrunscript-%{uniquesuffix}.1*
%{_mandir}/man1/jsadebugd-%{uniquesuffix}.1*
%{_mandir}/man1/jstack-%{uniquesuffix}.1*
%{_mandir}/man1/jstat-%{uniquesuffix}.1*
%{_mandir}/man1/jstatd-%{uniquesuffix}.1*
%{_mandir}/man1/native2ascii-%{uniquesuffix}.1*
%{_mandir}/man1/policytool-%{uniquesuffix}.1*
%{_mandir}/man1/rmic-%{uniquesuffix}.1*
%{_mandir}/man1/schemagen-%{uniquesuffix}.1*
%{_mandir}/man1/serialver-%{uniquesuffix}.1*
%{_mandir}/man1/wsgen-%{uniquesuffix}.1*
%{_mandir}/man1/wsimport-%{uniquesuffix}.1*
%{_mandir}/man1/xjc-%{uniquesuffix}.1*
%if_enabled systemtap
%{tapsetroot}
%endif

%files demo -f %{name}-demo.files
%doc %{_jvmdir}/%{sdkdir}/LICENSE

%files src
%doc README.src
%{_jvmdir}/%{sdkdir}/src.zip

%files javadoc
%_altdir/%altname-javadoc
%_sysconfdir/buildreqs/packages/substitute.d/%name-javadoc
%doc %{_javadocdir}/%{uniquejavadocdir}
%doc %{buildoutputdir}/j2sdk-image/jre/LICENSE

%files accessibility
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libatk-wrapper.so
%{_jvmdir}/%{jredir}/lib/ext/java-atk-wrapper.jar
%{_jvmdir}/%{jredir}/lib/accessibility.properties

%changelog
* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.221-alt2_2.6.18.0jpp8
- new alternatives layout

* Fri Jun 28 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.221-alt1_2.6.18.0jpp8
- new version

* Sun Jun 03 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.181-alt1_2.6.14.8jpp8
- new version

* Sun Jun 03 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.141-alt1_2.6.10.1jpp8
- new version

* Sun Jun 03 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.111-alt1_2.6.7.2jpp8
- new version

* Fri Apr 13 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.79-alt9_2.5.5.0jpp7
- added BR: docbook-style-xsl

* Fri Apr 06 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.79-alt8_2.5.5.0jpp7
- desktop files cleanup, fixes for bootstrap

* Fri Apr 06 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.79-alt7_2.5.5.0jpp7
- use ant1.9-nodeps

* Fri Apr 06 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.79-alt6_2.5.5.0jpp7
- Requires: ca-certificates-java

* Mon Nov 27 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.79-alt5_2.5.5.0jpp7
- removed obsolete exports in jvmjardir
- removed obsolete security policy alternatives in _jvmprivdir
- added java-1.x.0-openjdk alternative in jvmdir

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.79-alt4_2.5.5.0jpp7
- fixed java-headless provides

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.79-alt3_2.5.5.0jpp7
- fixed build (built with ant1.9)

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.79-alt2_2.5.5.0jpp7
- added javadoc alternatives
- supports build with gcc 5
- now creates classes.jsa in %%post

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.79-alt1_2.5.5.0jpp7
- new jpp release

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.25-alt2_2.3.10.3jpp7
- added /usr/lib/jvm/java-1.7.0-openjdk alternative in javac

* Tue Oct 13 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0:1.7.0.25-alt1_2.3.10.3jpp7.3
- rebuild with gcc 4.9

* Tue Oct 13 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0:1.7.0.25-alt1_2.3.10.3jpp7.2
- bootstrap build

* Fri Oct 09 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0:1.7.0.25-alt1_2.3.10.3jpp7.1
- build hackarouded

* Fri Jun 06 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.25-alt1_2.3.10.3jpp7
- converted from JPackage by jppimport script

* Wed Mar 20 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.9-alt1_2.3.8.0jpp7
- fc update

* Thu Oct 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.9-alt1_2.3.3jpp7
- new release

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.6-alt1_2.3.1.2jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.3-alt4_2.2.1.8jpp7
- applied repocop patches

* Thu Jul 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.3-alt3_2.2.1.8jpp7
- removed Obsoletes: on java-1.6.0-openjdk

* Tue Jul 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.3-alt2_2.2.1.8jpp7
- new version 2.2

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.3-alt2_2.1.1jpp7
- dropped libat-spi dependency

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.3-alt1_2.1.1jpp7
- Sisyphus release

* Thu Feb 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.1-alt1_2.0.3jpp5.M60T.1
- backport

* Thu Feb 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.1-alt1_2.0.3jpp6
- new version

