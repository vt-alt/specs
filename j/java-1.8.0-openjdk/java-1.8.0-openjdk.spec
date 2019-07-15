# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-generic-compat
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
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
%define name java-1.8.0-openjdk
%define version 1.8.0.212.b04
%define release 0
# note: parametrized macros are order-sensitive (unlike not-parametrized) even with normal macros
# also necessary when passing it as parameter to other macros. If not macro, then it is considered a switch
%global debug_suffix_unquoted -debug
# quoted one for shell operations
%global debug_suffix "%{debug_suffix_unquoted}"
%global normal_suffix ""

# if you want only debug build but providing java build only normal build but set normalbuild_parameter
%global debugbuild_parameter  slowdebug
%global normalbuild_parameter release
%global debug_warning This package has full debug on. Install only in need and remove asap.
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
# we need to distinguish between big and little endian PPC64
%global ppc64le         ppc64le
%global ppc64be         ppc64 ppc64p7
%global multilib_arches %{power64} sparc64 x86_64
%global jit_arches      %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64}

# By default, we build a debug build during main build on JIT architectures
%ifarch %{jit_arches}
%global include_debug_build 0
%else
%global include_debug_build 0
%endif

# Shenandoah HotSpot used everywhere, but built only on x86_64 and AArch64
%ifarch x86_64 %{aarch64}
%global use_shenandoah_hotspot 1
%else
%global use_shenandoah_hotspot 0
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
%global targets bootcycle-images docs
%else
%global targets all
%endif


# Filter out flags from the optflags macro that cause problems with the OpenJDK build
# We filter out -Wall which will otherwise cause HotSpot to produce hundreds of thousands of warnings (100+mb logs)
# We filter out -O flags so that the optimization of HotSpot is not lowered from O3 to O2
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
#%global _privatelibs libatk-wrapper[.]so.*|libattach[.]so.*|libawt_headless[.]so.*|libawt[.]so.*|libawt_xawt[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libhprof[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas_unix[.]so.*|libjava_crw_demo[.]so.*|libjavajpeg[.]so.*|libjdwp[.]so.*|libjli[.]so.*|libjsdt[.]so.*|libjsoundalsa[.]so.*|libjsound[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libnpt[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsplashscreen[.]so.*|libsunec[.]so.*|libunpack[.]so.*|libzip[.]so.*|lib[.]so\\(SUNWprivate_.*


# In some cases, the arch used by the JDK does
# not match _arch.
# Also, in some cases, the machine name used by SystemTap
# does not match that given by _build_cpu
%ifarch x86_64
%global archinstall amd64
%global stapinstall x86_64
%endif
%ifarch ppc
%global archinstall ppc
%global stapinstall powerpc
%endif
%ifarch %{ppc64be}
%global archinstall ppc64
%global stapinstall powerpc
%endif
%ifarch %{ppc64le}
%global archinstall ppc64le
%global stapinstall powerpc
%endif
%ifarch %{ix86}
%global archinstall i386
%global stapinstall i386
%endif
%ifarch ia64
%global archinstall ia64
%global stapinstall ia64
%endif
%ifarch s390
%global archinstall s390
%global stapinstall s390
%endif
%ifarch s390x
%global archinstall s390x
%global stapinstall s390
%endif
%ifarch %{arm}
%global archinstall arm
%global stapinstall arm
%endif
%ifarch %{aarch64}
%global archinstall aarch64
%global stapinstall arm64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archinstall sparc
%global stapinstall %{_build_cpu}
%endif
# 64 bit sparc
%ifarch sparc64
%global archinstall sparcv9
%global stapinstall %{_build_cpu}
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
%global majorver 8

# Convert an absolute path to a relative path.  Each symbolic link is
# specified relative to the directory in which it is installed so that
# it will resolve properly within chrooted installations.
%global script 'use File::Spec; print File::Spec->abs2rel($ARGV[0], $ARGV[1])'
%global abs2rel %{__perl} -e %{script}


# Standard JPackage naming and versioning defines.
%global origin          openjdk
%global origin_nice     OpenJDK
%global top_level_dir_name   %{origin}
# note, following three variables are sedded from update_sources if used correctly. Hardcode them rather there.
%global shenandoah_project	aarch64-port
%global shenandoah_repo		jdk8u-shenandoah
%global shenandoah_revision    	aarch64-shenandoah-jdk8u212-b04
# Define old aarch64/jdk8u tree variables for compatibility
%global project         %{shenandoah_project}
%global repo            %{shenandoah_repo}
%global revision        %{shenandoah_revision}

# eg # jdk8u60-b27 -> jdk8u60 or # aarch64-jdk8u60-b27 -> aarch64-jdk8u60  (dont forget spec escape % by %%)
%global whole_update    %(VERSION=%{revision}; echo ${VERSION%%-*})
# eg  jdk8u60 -> 60 or aarch64-jdk8u60 -> 60
%global updatever       %(VERSION=%{whole_update}; echo ${VERSION##*u})
# eg jdk8u60-b27 -> b27
%global buildver        %(VERSION=%{revision}; echo ${VERSION##*-})
# priority must be 7 digits in total. The expression is workarounding tip
%global priority        %(TIP=1800%{updatever};  echo ${TIP/tip/999})

%global javaver         1.%{majorver}.0

# parametrized macros are order-sensitive
%global compatiblename  %{name}
%global fullversion     %{compatiblename}-%{version}-%{release}
# images stub
%global jdkimage       j2sdk-image
# output dir stub
%global buildoutputdir %{top_level_dir_name}/build/jdk8.build
#we can copy the javadoc to not arched dir, or make it not noarch
%global uniquejavadocdir %{fullversion}
#main id and dir of this jdk
%global uniquesuffix %{fullversion}.%{_arch}

# Standard JPackage directories and symbolic links.
%global sdkdir %{uniquesuffix}
%global jrelnk jre-%{javaver}-%{origin}-%{version}-%{release}.%{_arch}

%global jredir %{sdkdir}/jre
%global sdkbindir %{_jvmdir}/%{sdkdir}/bin
%global jrebindir %{_jvmdir}/%{jredir}/bin
%global jvmjardir %{_jvmjardir}/%{uniquesuffix}

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
%global tapsetdir %{tapsetroot}/tapset/%{stapinstall}
%endif

# not-duplicated scriptlets for normal/debug packages
%global update_desktop_icons /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

























# not-duplicated requires/provides/obsolate for normal/debug packages








# Prevent brp-java-repack-jars from being run
%global __jar_repack 0

Name:    java-%{javaver}-%{origin}
Version: %{javaver}.%{updatever}.%{buildver}
Release: alt2_0jpp8
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

# Shenandoah HotSpot
# aarch64-port/jdk8u-shenandoah contains an integration forest of
# OpenJDK 8u, the aarch64 port and Shenandoah
# To regenerate, use:
# VERSION=%%{shenandoah_revision}
# FILE_NAME_ROOT=%%{shenandoah_project}-%%{shenandoah_repo}-${VERSION}
# REPO_ROOT=<path to checked-out repository> generate_source_tarball.sh
# where the source is obtained from http://hg.openjdk.java.net/%%{project}/%%{repo}
Source0: %{shenandoah_project}-%{shenandoah_repo}-%{shenandoah_revision}.tar.xz

# Custom README for -src subpackage
Source2:  README.md

# Use 'generate_tarballs.sh' to generate the following tarballs
# They are based on code contained in the IcedTea project (3.x).

# Systemtap tapsets. Zipped up to keep it small.
Source8: systemtap-tapset-3.6.0pre02.tar.xz

# Desktop files. Adapted from IcedTea
Source9: jconsole.desktop.in
Source10: policytool.desktop.in

# nss configuration file
Source11: nss.cfg.in

# Removed libraries that we link instead
Source12: %{name}-remove-intree-libraries.sh

# Ensure we aren't using the limited crypto policy
Source13: TestCryptoLevel.java

# Ensure ECDSA is working
Source14: TestECDSA.java

Source20: repackReproduciblePolycies.sh

# New versions of config files with aarch64 support. This is not upstream yet.
Source100: config.guess
Source101: config.sub

############################################
#
# RPM/distribution specific patches
#
# This section includes patches specific to
# Fedora/RHEL which can not be upstreamed
# either in their current form or at all.
############################################

# Accessibility patches
# Ignore AWTError when assistive technologies are loaded 
Patch1:   rh1648242-accessible_toolkit_crash_do_not_break_jvm.patch
# Restrict access to java-atk-wrapper classes
Patch3:   rh1648644-java_access_bridge_privileged_security.patch
# PR1834, RH1022017: Reduce curves reported by SSL to those in NSS
# Not currently suitable to go upstream as it disables curves
# for all providers unconditionally
Patch525: pr1834-rh1022017-reduce_ellipticcurvesextension_to_provide_only_three_nss_supported_nist_curves_23_24_25.patch
# Turn on AssumeMP by default on RHEL systems
Patch534: rh1648246-always_instruct_vm_to_assume_multiple_processors_are_available.patch

#############################################
#
# Upstreamable patches
#
# This section includes patches which need to
# be reviewed & pushed to the current development
# tree of OpenJDK.
#############################################
# PR2737: Allow multiple initialization of PKCS11 libraries
Patch5: pr2737-allow_multiple_pkcs11_library_initialisation_to_be_a_non_critical_error.patch
# PR2095, RH1163501: 2048-bit DH upper bound too small for Fedora infrastructure (sync with IcedTea 2.x)
Patch504: rh1163501-increase_2048_bit_dh_upper_bound_fedora_infrastructure_in_dhparametergenerator.patch
# Turn off strict overflow on IndicRearrangementProcessor{,2}.cpp following 8140543: Arrange font actions
Patch512: rh1649664-awt2dlibraries_compiled_with_no_strict_overflow.patch
# RH1337583, PR2974: PKCS#10 certificate requests now use CRLF line endings rather than system line endings
Patch523: pr2974-rh1337583-add_systemlineendings_option_to_keytool_and_use_line_separator_instead_of_crlf_in_pkcs10.patch
# PR3083, RH1346460: Regression in SSL debug output without an ECC provider
Patch528: pr3083-rh1346460-for_ssl_debug_return_null_instead_of_exception_when_theres_no_ecc_provider.patch
# RH1566890: CVE-2018-3639
Patch529: rh1566890-CVE_2018_3639-speculative_store_bypass.patch
Patch531: rh1566890-CVE_2018_3639-speculative_store_bypass_toggle.patch
# PR3601: Fix additional -Wreturn-type issues introduced by 8061651
Patch530: pr3601-fix_additional_Wreturn_type_issues_introduced_by_8061651_for_prims_jvm_cpp.patch
# Support for building the SunEC provider with the system NSS installation
# PR1983: Support using the system installation of NSS with the SunEC provider
# PR2127: SunEC provider crashes when built using system NSS
# PR2815: Race condition in SunEC provider with system NSS
# PR2899: Don't use WithSeed versions of NSS functions as they don't fully process the seed
# PR2934: SunEC provider throwing KeyException with current NSS
# PR3479, RH1486025: ECC and NSS JVM crash
Patch513: pr1983-rh1565658-support_using_the_system_installation_of_nss_with_the_sunec_provider_jdk8.patch
Patch514: pr1983-rh1565658-support_using_the_system_installation_of_nss_with_the_sunec_provider_root8.patch
Patch515: pr2127-sunec_provider_crashes_when_built_using_system_nss_thus_use_of_nss_memory_management_functions.patch
Patch516: pr2815-race_condition_in_sunec_provider_with_system_nss_fix.patch
Patch517: pr2899-dont_use_withseed_versions_of_nss_functions_as_they_dont_fully_process_the_seed.patch
Patch518: pr2934-sunec_provider_throwing_keyexception_withine.separator_current_nss_thus_initialise_the_random_number_generator_and_feed_the_seed_to_it.patch
Patch519: pr3479-rh1486025-sunec_provider_can_have_multiple_instances_leading_to_premature_nss_shutdown.patch
# PR2888: OpenJDK should check for system cacerts database (e.g. /etc/pki/java/cacerts)
Patch539: pr2888-openjdk_should_check_for_system_cacerts_database_eg_etc_pki_java_cacerts.patch
# PR3575, RH1567204: System cacerts database handling should not affect jssecacerts
Patch540: pr3575-rh1567204-system_cacerts_database_handling_no_longer_affect_jssecacerts.patch
Patch541: rh1684077-openjdk_should_depend_on_pcsc-lite-libs_instead_of_pcsc-lite-devel.patch

#############################################
#
# Arch-specific upstreamable patches
#
# This section includes patches which need to
# be reviewed & pushed upstream and are specific
# to certain architectures. This usually means the
# current OpenJDK development branch, but may also
# include other trees e.g. for the AArch64 port for
# OpenJDK 8u.
#############################################
# s390: PR3593: Use "%z" for size_t on s390 as size_t != intptr_t
Patch103: pr3593-s390_use_z_format_specifier_for_size_t_arguments_as_size_t_not_equals_to_int.patch
# x86: S8199936, PR3533: HotSpot generates code with unaligned stack, crashes on SSE operations (-mstackrealign workaround)
Patch105: jdk8199936-pr3533-enable_mstackrealign_on_x86_linux_as_well_as_x86_mac_os_x.patch
# AArch64: PR3519: Fix further functions with a missing return value (AArch64)
Patch106: pr3519-fix_further_functions_with_a_missing_return_value.patch
# S390 ambiguous log2_intptr calls
Patch107: s390-8214206_fix.patch

#############################################
#
# Patches which need backporting to 8u
#
# This section includes patches which have
# been pushed upstream to the latest OpenJDK
# development tree, but need to be backported
# to OpenJDK 8u.
#############################################
# S8074839, PR2462: Resolve disabled warnings for libunpack and the unpack200 binary
# This fixes printf warnings that lead to build failure with -Werror=format-security from optflags
Patch502: pr2462-resolve_disabled_warnings_for_libunpack_and_the_unpack200_binary.patch
# S8154313: Generated javadoc scattered all over the place
Patch400: jdk8154313-generated_javadoc_scattered_all_over_the_place.patch
# 8171000, PR3542, RH1402819: Robot.createScreenCapture() crashes in wayland mode
Patch563: jdk8171000-pr3542-rh1402819-robot_createScreenCapture_crashes_in_wayland_mode.patch
# 8197546, PR3542, RH1402819: Fix for 8171000 breaks Solaris + Linux builds
Patch564: jdk8197546-pr3542-rh1402819-fix_for_8171000_breaks_solaris_linux_builds.patch
# PR3591: Fix for bug 3533 doesn't add -mstackrealign to JDK code
Patch571: jdk8199936-pr3591-enable_mstackrealign_on_x86_linux_as_well_as_x86_mac_os_x_jdk.patch
# 8141570, PR3548: Fix Zero interpreter build for --disable-precompiled-headers
Patch573: jdk8141570-pr3548-fix_zero_interpreter_build_for_disable_precompiled_headers.patch
# 8143245, PR3548: Zero build requires disabled warnings
Patch574: jdk8143245-pr3548-zero_build_requires_disabled_warnings.patch
# 8197981, PR3548: Missing return statement in __sync_val_compare_and_swap_8
Patch575: jdk8197981-pr3548-missing_return_statement_in_sync_val_compare_and_swap_8.patch
# 8064786, PR3599: Fix debug build after 8062808: Turn on the -Wreturn-type warning
Patch576: jdk8064786-pr3599-fix_debug_build_after_8062808_Turn_on_the_wreturn_type_warning.patch
# 8062808, PR3548: Turn on the -Wreturn-type warning
Patch577: jdk8062808-pr3548-turn_on_the_wreturn_type_warning.patch
# s390: JDK-8203030, Type fixing for s390
Patch102: jdk8203030-zero_s390_31_bit_size_t_type_conflicts_in_shared_code.patch
# 8035341: Allow using a system installed libpng
Patch202: jdk8035341-allow_using_system_installed_libpng.patch
# 8042159: Allow using a system-installed lcms2
Patch203: jdk8042159-allow_using_system_installed_lcms2.patch
# 8210761: libjsig is being compiled without optimization
Patch620: jdk8210761-rh1632174-libjsig_is_being_compiled_without_optimization.patch
# 8210416: [linux] Poor StrictMath performance due to non-optimized compilation
Patch622: jdk8210416-rh1632174-compile_fdlibm_with_o2_ffp_contract_off_on_gcc_clang_arches.patch
# 8210425: [x86] sharedRuntimeTrig/sharedRuntimeTrans compiled without optimization
#          Upstream 8u part.
Patch623: jdk8210425-rh1632174-01-compile_with_o2_and_ffp_contract_off_as_for_fdlibm.patch
# 8210425: [x86] sharedRuntimeTrig/sharedRuntimeTrans compiled without optimization
#          Aarch64-port 8u local part
Patch624: jdk8210425-rh1632174-02-compile_with_o2_and_ffp_contract_off_as_for_fdlibm_aarch64.patch
# 8210425: [x86] sharedRuntimeTrig/sharedRuntimeTrans compiled without optimization
#          Zero part of the fix for (arm/s390 arches)
Patch625: jdk8210425-rh1632174-03-compile_with_o2_and_ffp_contract_off_as_for_fdlibm_zero.patch

#############################################
#
# Patches appearing in 8u222
#
# This section includes patches which are present
# in the listed OpenJDK 8u release and should be
# able to be removed once that release is out
# and used by this RPM.
#############################################

#############################################
#
# Patches ineligible for 8u
#
# This section includes patches which are present
# upstream, but ineligible for upstream 8u backport.
#############################################
# 8043805: Allow using a system-installed libjpeg
Patch201: jdk8043805-allow_using_system_installed_libjpeg.patch

#############################################
#
# Shenandoah fixes
#
# This section includes patches which are
# specific to the Shenandoah garbage collector
# and should be upstreamed to the appropriate
# trees.
#############################################

# Shenandoah fixes
# PR3634: Shenandoah still broken on s390 with aarch64-shenandoah-jdk8u181-b16
Patch582: pr3634-fix_shenandoah_for_size_t_on_s390.patch

#############################################
#
# Non-OpenJDK fixes
#
# This section includes patches to code other
# that from OpenJDK.
#############################################

# Section currently empty

#############################################
#
# Dependencies
#
#############################################
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
BuildRequires: gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel
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
BuildRequires: unzip
# Use OpenJDK 7 where available (on RHEL) to avoid
# having to use the rhel-7.x-java-unsafe-candidate hack
%if ! 0%{?fedora} && 0%{?rhel} <= 7
# Require a boot JDK which doesn't fail due to RH1482244
BuildRequires: java-1.7.0-openjdk-devel >= 1.7.0.151
%else
BuildRequires: java-1.8.0-openjdk-devel
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
# Require libXcomposite explicitly since it's only dynamically loaded
# at runtime. Fixes screenshot issues. See JDK-8150954.
Requires: libXcomposite
# Requires rest of java
Requires: %{name}-headless = %{epoch}:%{version}-%{release}
# for java-X-openjdk package's desktop binding
Requires: libgail libgtk+2

Provides: java-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}

# Standard JPackage base provides.
Provides: jre = %{javaver}
Provides: jre-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver} = %{epoch}:%{version}-%{release}
Provides: java-%{origin} = %{epoch}:%{version}-%{release}
Provides: java = %{epoch}:%{javaver}
# Standard JPackage extensions provides.
Provides: java-fonts = %{epoch}:%{version}

#Obsoletes: java-1.7.0-openjdk
Obsoletes: java-1.5.0-gcj
Obsoletes: sinjdoc
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
Patch33: java-1.8.0-openjdk-alt-no-Werror.patch
Patch34: java-1.8.0-openjdk-alt-link.patch

%description
The %{origin_nice} runtime environment.

%if %{include_debug_build}
%package debug
Summary: %{origin_nice} Runtime Environment %{majorver} %{debug_on}
Group:   Development/Other

%description debug
The %{origin_nice} runtime environment.
%{debug_warning}
%endif

%if %{include_normal_build}
%package headless
Summary: %{origin_nice} Headless Runtime Environment %{majorver}
Group:   Development/Other

# Require /etc/pki/java/cacerts
Requires: ca-trust
# Require jpackage-utils for ownership of /usr/lib/jvm/
Requires: jpackage-utils
# Require zoneinfo data provided by tzdata-java subpackage.
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
Requires: liblksctp lksctp-tools libpcsclite libcups

# Standard JPackage base provides
Provides: jre-headless = %{epoch}:%{javaver}
Provides: jre-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-headless = %{epoch}:%{version}-%{release}
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

# https://bugzilla.redhat.com/show_bug.cgi?id=1312019
Provides: /usr/bin/jjs
Requires: java-common
Requires: /proc
Requires(post): /proc

#Obsoletes: java-1.7.0-openjdk-headless

%description headless
The %{origin_nice} runtime environment %{majorver} without audio and video support.
%endif

%if %{include_debug_build}
%package headless-debug
Summary: %{origin_nice} Runtime Environment %{debug_on}
Group:   Development/Other


%description headless-debug
The %{origin_nice} runtime environment %{majorver} without audio and video support.
%{debug_warning}
%endif

%if %{include_normal_build}
%package devel
Summary: %{origin_nice} Development Environment %{majorver}
Group:   Development/Java

# Require base package
Requires:         %{name} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install tool alternatives
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall tool alternatives
# in version 1.7 and higher for --family switch

# Standard JPackage devel provides.
Provides: java-sdk-%{javaver}-%{origin} = %{epoch}:%{version}
Provides: java-sdk-%{javaver} = %{epoch}:%{version}
Provides: java-sdk-%{origin} = %{epoch}:%{version}
Provides: java-sdk = %{epoch}:%{javaver}
Provides: java-%{javaver}-devel = %{epoch}:%{version}
Provides: java-%{javaver}-%{origin}-devel = %{epoch}:%{version}
Provides: java-devel-%{origin} = %{epoch}:%{version}
Provides: java-devel = %{epoch}:%{javaver}

#Obsoletes: java-1.7.0-openjdk-devel
#Obsoletes: java-1.5.0-gcj-devel

%description devel
The %{origin_nice} development tools %{majorver}.
%endif

%if %{include_debug_build}
%package devel-debug
Summary: %{origin_nice} Development Environment %{majorver} %{debug_on}
Group:   Development/Java


%description devel-debug
The %{origin_nice} development tools %{majorver}.
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

#Obsoletes: java-1.7.0-openjdk-demo

%description demo
The %{origin_nice} demos %{majorver}.
%endif

%if %{include_debug_build}
%package demo-debug
Summary: %{origin_nice} Demos %{majorver} %{debug_on}
Group:   Development/Other


%description demo-debug
The %{origin_nice} demos %{majorver}.
%{debug_warning}
%endif

%if %{include_normal_build}
%package src
Summary: %{origin_nice} Source Bundle %{majorver}
Group:   Development/Other

Requires: %{name}-headless = %{epoch}:%{version}-%{release}

# Standard JPackage javadoc provides
Provides: java-src = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-src = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-src = %{epoch}:%{version}-%{release}
#Obsoletes: java-1.7.0-openjdk-src

%description src
The java-%{origin}-src sub-package contains the complete %{origin_nice} %{majorver}
class library source code for use by IDE indexers and debuggers.
%endif

%if %{include_debug_build}
%package src-debug
Summary: %{origin_nice} Source Bundle %{majorver} %{for_debug}
Group:   Development/Other


%description src-debug
The java-%{origin}-src-slowdebug sub-package contains the complete %{origin_nice} %{majorver}
 class library source code for use by IDE indexers and debuggers. Debugging %{for_debug}.
%endif

%if %{include_normal_build}
%package javadoc
Summary: %{origin_nice} %{majorver} API documentation
Group:   Development/Java
Requires: jpackage-utils
BuildArch: noarch

# Post requires alternatives to install javadoc alternative.
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall javadoc alternative
# in version 1.7 and higher for --family switch

# Standard JPackage javadoc provides.
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc = %{epoch}:%{version}-%{release}
# hack till java 9+ will come
Provides: java-javadoc = 1:1.9.0

#Obsoletes: java-1.7.0-openjdk-javadoc


%description javadoc
The %{origin_nice} %{majorver} API documentation.
%endif

%if %{include_normal_build}
%package javadoc-zip
Summary: %{origin_nice} %{majorver} API documentation compressed in single archive
Group:   Development/Java
Requires: javapackages-tools
BuildArch: noarch

# Post requires alternatives to install javadoc alternative.
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall javadoc alternative
# in version 1.7 and higher for --family switch

# Standard JPackage javadoc provides.
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc = %{epoch}:%{version}-%{release}

#Obsoletes: java-1.7.0-openjdk-javadoc


%description javadoc-zip
The %{origin_nice} %{majorver} API documentation compressed in single archive.
%endif

%if %{include_debug_build}
%package javadoc-debug
Summary: %{origin_nice} %{majorver} API documentation %{for_debug}
Group:   Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc-debug
The %{origin_nice} %{majorver} API documentation %{for_debug}.
%endif

%if %{include_debug_build}
%package javadoc-zip-debug
Summary: %{origin_nice} %{majorver} API documentation compressed in single archive %{for_debug}
Group:   Development/Java
Requires: javapackages-tools
BuildArch: noarch


%description javadoc-zip-debug
The %{origin_nice} %{majorver} API documentation compressed in single archive %{for_debug}.
%endif


%if %{include_normal_build}
%package accessibility
Group: Development/Java
Summary: OpenJDK accessibility connector

Requires: java-atk-wrapper
Requires: %{name} = %{epoch}:%{version}-%{release}

Provides: java-accessibility = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-accessibility = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-accessibility = %{epoch}:%{version}-%{release}

#Obsoletes: java-1.7.0-openjdk-accessibility

%description accessibility
Enables accessibility support in %{origin_nice} %{majorver} by using java-atk-wrapper. This allows
compatible at-spi2 based accessibility programs to work for AWT and Swing-based
programs.

Please note, the java-atk-wrapper is still in beta, and %{origin_nice} %{majorver} itself is still
being tuned to be working with accessibility features. There are known issues
with accessibility on, so please do not install this package unless you really
need to.
%endif

%if %{include_debug_build}
%package accessibility-debug
Group: Development/Other
Summary: %{origin_nice} %{majorver} accessibility connector %{for_debug}


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
  echo "You have disabled both include_debug_build and include_normal_build. That is a no go."
  exit 13
fi
%setup -q -c -n %{uniquesuffix ""} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 7 ] ; then
 echo "priority must be 7 digits in total, violated"
 exit 14
fi
# For old patches
ln -s %{top_level_dir_name} jdk8

cp %{SOURCE2} .

# replace outdated configure guess script
#
# the configure macro will do this too, but it also passes a few flags not
# supported by openjdk configure script
cp %{SOURCE100} %{top_level_dir_name}/common/autoconf/build-aux/
cp %{SOURCE101} %{top_level_dir_name}/common/autoconf/build-aux/

# OpenJDK patches

# Remove libraries that are linked
sh %{SOURCE12}

# System library fixes
%patch201
%patch202
%patch203

%patch1
%patch3
%patch5

# s390 build fixes
%patch102
%patch103
%patch107

# AArch64 fixes
%patch106

# x86 fixes
%patch105

# Upstreamable fixes
%patch502
%patch504
%patch512
%patch513
%patch514
%patch515
%patch516
%patch517
%patch518
%patch519
%patch400
%patch523
%patch528
%patch529
%patch531
%patch530
%patch563
%patch564
%patch571
%patch573
%patch574
%patch575
%patch576
%patch577
%patch620
%patch622
%patch623
%patch624
%patch625
%patch541

# RPM-only fixes
%patch525
%patch539
%patch540

# RHEL-only patches
%if ! 0%{?fedora} && 0%{?rhel} <= 7
%patch534
%endif

# Shenandoah patches
%patch582

# Extract systemtap tapsets
%if_enabled systemtap
tar -x -I xz -f %{SOURCE8}
%if %{include_debug_build}
cp -r tapset tapset%{debug_suffix}
%endif


for suffix in %{build_loop} ; do
  for file in "tapset"$suffix/*.in; do
    OUTPUT_FILE=`echo $file | sed -e "s:%{javaver}\.stp\.in$:%{version}-%{release}.%{_arch}.stp:g"`
    sed -e "s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/server/libjvm.so:g" $file > $file.1
# TODO find out which architectures other than i686 have a client vm
%ifarch %{ix86}
    sed -e "s:@ABS_CLIENT_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/client/libjvm.so:g" $file.1 > $OUTPUT_FILE
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
for file in %{SOURCE9} %{SOURCE10} ; do
    FILE=`basename $file | sed -e s:\.in$::g`
    EXT="${FILE##*.}"
    NAME="${FILE%.*}"
    OUTPUT_FILE=$NAME$suffix.$EXT
    sed    -e  "s:@JAVA_HOME@:%{sdkbindir}:g" $file > $OUTPUT_FILE
    sed -i -e  "s:@JRE_HOME@:%{jrebindir}:g" $OUTPUT_FILE
    sed -i -e  "s:@ARCH@:%{version}-%{release}.%{_arch}$suffix:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_MAJOR_VERSION@:%{javaver}:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VENDOR@:%{origin}:g" $OUTPUT_FILE
done
done
sed -i -e 's, -m32, -m32 %optflags_shared -fpic -D_BLA_BLA_BLA1,' openjdk/hotspot/make/linux/makefiles/gcc.make
sed -i -e 's,DEF_OBJCOPY=/usr/bin/objcopy,DEF_OBJCOPY=/usr/bin/NO-objcopy,' openjdk/hotspot/make/linux/makefiles/defs.make
%patch33 -p1
%patch34 -p1

# Setup nss.cfg
#sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE11} > nss.cfg


%build
# How many CPU's do we have?
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

# We use ourcppflags because the OpenJDK build seems to
# pass EXTRA_CFLAGS to the HotSpot C++ compiler...
EXTRA_CFLAGS="%ourcppflags"
EXTRA_CPP_FLAGS="%ourcppflags"
%ifarch %{power64} ppc
# fix rpmlint warnings
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif
export EXTRA_CFLAGS

(cd %{top_level_dir_name}/common/autoconf
 bash ./autogen.sh
)

for suffix in %{build_loop} ; do
if [ "$suffix" = "%{debug_suffix}" ] ; then
debugbuild=%{debugbuild_parameter}
else
debugbuild=%{normalbuild_parameter}
fi

# Variable used in hs_err hook on build failures
top_dir_abs_path=$(pwd)/%{top_level_dir_name}

mkdir -p %{buildoutputdir}
pushd %{buildoutputdir}

NSS_LIBS="%{NSS_LIBS} -lfreebl" \
NSS_CFLAGS="%{NSS_CFLAGS}" \
bash ../../configure \
%ifnarch %{jit_arches}
    --with-jvm-variants=zero \
%endif
    --with-native-debug-symbols=internal \
    --with-milestone="fcs" \
    --with-update-version=%{updatever} \
    --with-build-number=%{buildver} \
    --with-boot-jdk=/usr/lib/jvm/java-openjdk \
    --with-debug-level=$debugbuild \
    --enable-unlimited-crypto \
    --disable-system-nss \
    --with-zlib=system \
    --with-libjpeg=system \
    --with-giflib=system \
    --with-libpng=system \
    --with-lcms=bundled \
    --with-stdc++lib=dynamic \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --with-extra-ldflags="%{ourldflags}" \
    --with-num-cores="$NUM_PROC"

cat spec.gmk
cat hotspot-spec.gmk

make \
    JAVAC_FLAGS=-g \
    LOG=trace \
    %{targets} || ( pwd; find $top_dir_abs_path -name "hs_err_pid*.log" | xargs cat && false )

make zip-docs

# the build (erroneously) removes read permissions from some jars
# this is a regression in OpenJDK 7 (our compiler):
# http://icedtea.classpath.org/bugzilla/show_bug.cgi?id=1437
find images/%{jdkimage} -iname '*.jar' -exec chmod ugo+r {} \;
chmod ugo+r images/%{jdkimage}/lib/ct.sym

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
#install -m 644 nss.cfg $JAVA_HOME/jre/lib/security/

# Use system-wide tzdata
rm $JAVA_HOME/jre/lib/tzdb.dat
ln -s %{_datadir}/javazi-1.8/tzdb.dat $JAVA_HOME/jre/lib/tzdb.dat

# build cycles
done

%check

# We test debug first as it will give better diagnostics on a crash
for suffix in %{rev_build_loop} ; do

export JAVA_HOME=$(pwd)/%{buildoutputdir}/images/%{jdkimage}

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE13}
$JAVA_HOME/bin/java TestCryptoLevel

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
jar -tf $JAVA_HOME/src.zip | grep 'sun.misc.Unsafe'

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
pushd %{buildoutputdir}/images/%{jdkimage}

# Install jsa directories so we can owe them
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{archinstall}/server/
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{archinstall}/client/

  # Install main files.
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  cp -a bin include lib src.zip $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
  cp -a jre/bin jre/lib $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}

%if_enabled systemtap
  # Install systemtap support files
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

  # Remove empty cacerts database
  rm -f $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/cacerts
  # Install cacerts symlink needed by some apps which hardcode the path
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

  # Install man pages
  install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
  for manpage in man/man1/*
  do
    # Convert man pages to UTF8 encoding
    iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
    mv -f $manpage.tmp $manpage
    install -m 644 -p $manpage $RPM_BUILD_ROOT%{_mandir}/man1/$(basename \
      $manpage .1)-%{uniquesuffix}.1
  done

  # Install demos and samples.
  cp -a demo $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  mkdir -p sample/rmi
  if [ ! -e sample/rmi/java-rmi.cgi ] ; then 
    # hack to allow --short-circuit on install
    mv bin/java-rmi.cgi sample/rmi
  fi
  cp -a sample $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}

popd


# Install Javadoc documentation
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
cp -a %{buildoutputdir}/docs $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}
cp -a %{buildoutputdir}/bundles/jdk-%{javaver}_%{updatever}$suffix-%{buildver}-docs.zip  $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}.zip

# Install icons and menu entries
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    %{top_level_dir_name}/jdk/src/solaris/classes/sun/awt/X11/java-icon${s}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-%{origin}.png
done

# Install desktop files
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole$suffix policytool$suffix ; do
    desktop-file-install --vendor=%{uniquesuffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

# Find JRE directories.
find $RPM_BUILD_ROOT%{_jvmdir}/%{jredir} -type d \
  | grep -v jre/lib/security \
  | sed 's|'$RPM_BUILD_ROOT'|%%dir |' \
  > %{name}.files-headless"$suffix"
# Find JRE files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{jredir} -type f -o -type l \
  | grep -v jre/lib/security \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  > %{name}.files.all"$suffix"
#split %%{name}.files to %%{name}.files-headless and %%{name}.files
#see https://bugzilla.redhat.com/show_bug.cgi?id=875408
NOT_HEADLESS=\
"%{_jvmdir}/%{uniquesuffix}/jre/lib/%{archinstall}/libjsoundalsa.so
%{_jvmdir}/%{uniquesuffix}/jre/lib/%{archinstall}/libpulse-java.so
%{_jvmdir}/%{uniquesuffix}/jre/lib/%{archinstall}/libsplashscreen.so
%{_jvmdir}/%{uniquesuffix}/jre/lib/%{archinstall}/libawt_xawt.so
%{_jvmdir}/%{uniquesuffix}/jre/lib/%{archinstall}/libjawt.so
%{_jvmdir}/%{uniquesuffix}/jre/bin/policytool"
#filter  %%{name}.files from  %%{name}.files.all to %%{name}.files-headless
ALL=`cat %{name}.files.all"$suffix"`
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
    echo "$file" >> %{name}.files-headless"$suffix"
else
    echo "$file" >> %{name}.files"$suffix"
fi
done
# Find demo directories.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample -type d \
  | sed 's|'$RPM_BUILD_ROOT'|%%dir |' \
  > %{name}-demo.files"$suffix"

# FIXME: remove SONAME entries from demo DSOs. See
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

# Create links which leads to separately installed java-atk-bridge and allow configuration
# links points to java-atk-wrapper - an dependence
  pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/lib/%{archinstall}
    ln -s %{_libdir}/java-atk-wrapper/libatk-wrapper.so.0 libatk-wrapper.so
  popd
  pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/lib/ext
     ln -s %{_libdir}/java-atk-wrapper/java-atk-wrapper.jar  java-atk-wrapper.jar
  popd
  pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/lib/
    echo "#Config file to  enable java-atk-wrapper" > accessibility.properties
    echo "" >> accessibility.properties
    echo "assistive_technologies=org.GNOME.Accessibility.AtkWrapper" >> accessibility.properties
    echo "" >> accessibility.properties
  popd

bash %{SOURCE20} $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir} %{javaver}
# https://bugzilla.redhat.com/show_bug.cgi?id=1183793
touch -t 201401010000 $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/lib/security/java.security

# stabilize permissions
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -name "*.so" -exec chmod 755 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -type d -exec chmod 755 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -name "ASSEMBLY_EXCEPTION" -exec chmod 644 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -name "LICENSE" -exec chmod 644 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -name "THIRD_PARTY_README" -exec chmod 644 {} \; ; 

# end, dual install
done
for rpm404_ghost in %{_jvmdir}/%{jredir}/lib/%{archinstall}/server/classes.jsa %{_jvmdir}/%{jredir}/lib/%{archinstall}/client/classes.jsa
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

%if %{include_normal_build}
%files -f %{name}.files
%_sysconfdir/buildreqs/packages/substitute.d/%name
# main package builds always
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}-%{origin}.png
%{_datadir}/applications/*policytool.desktop
%else
%files
# placeholder
%endif


%if %{include_normal_build}
%files headless  -f %{name}.files-headless
%_altdir/%altname-java-headless
%_sysconfdir/buildreqs/packages/substitute.d/%name-headless
# important note, see https://bugzilla.redhat.com/show_bug.cgi?id=1038092 for whole issue
# all config/noreplace files (and more) have to be declared in pretrans. See pretrans
%doc %{buildoutputdir}/images/%{jdkimage}/jre/ASSEMBLY_EXCEPTION
%doc %{buildoutputdir}/images/%{jdkimage}/jre/LICENSE
%doc %{buildoutputdir}/images/%{jdkimage}/jre/THIRD_PARTY_README
%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{jrelnk}
%{_jvmjardir}/%{jrelnk}
%{_jvmprivdir}/*
%{jvmjardir}
%dir %{_jvmdir}/%{jredir}/lib/security
%{_jvmdir}/%{jredir}/lib/security/cacerts
%dir %{_jvmdir}/%{jredir}/lib/security/policy/unlimited/
%dir %{_jvmdir}/%{jredir}/lib/security/policy/limited/
%dir %{_jvmdir}/%{jredir}/lib/security/policy/
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/policy/unlimited/US_export_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/policy/unlimited/local_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/policy/limited/US_export_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/policy/limited/local_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/blacklisted.certs
%config(noreplace) %{_jvmdir}/%{jredir}/lib/logging.properties
%{_mandir}/man1/java-%{uniquesuffix}.1*
%{_mandir}/man1/jjs-%{uniquesuffix}.1*
%{_mandir}/man1/keytool-%{uniquesuffix}.1*
%{_mandir}/man1/orbd-%{uniquesuffix}.1*
%{_mandir}/man1/pack200-%{uniquesuffix}.1*
%{_mandir}/man1/rmid-%{uniquesuffix}.1*
%{_mandir}/man1/rmiregistry-%{uniquesuffix}.1*
%{_mandir}/man1/servertool-%{uniquesuffix}.1*
%{_mandir}/man1/tnameserv-%{uniquesuffix}.1*
%{_mandir}/man1/unpack200-%{uniquesuffix}.1*
%{_mandir}/man1/policytool-%{uniquesuffix}.1*
#%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/nss.cfg
%ifarch %{jit_arches}
%ifnarch %{power64}
%attr(444, root, root) %ghost %{_jvmdir}/%{jredir}/lib/%{archinstall}/server/classes.jsa
%attr(444, root, root) %ghost %{_jvmdir}/%{jredir}/lib/%{archinstall}/client/classes.jsa
%endif
%endif
%{_jvmdir}/%{jredir}/lib/%{archinstall}/server/
%{_jvmdir}/%{jredir}/lib/%{archinstall}/client/
# sisyphus_check
%dir %{_jvmdir}/%{jredir}/lib/security/policy
%dir %{_jvmdir}/%{jredir}/lib/security/policy/limited
%dir %{_jvmdir}/%{jredir}/lib/security/policy/unlimited

%files devel
%_altdir/%altname-javac
%_altdir/%altname-javac-versioned
%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%doc %{buildoutputdir}/images/%{jdkimage}/ASSEMBLY_EXCEPTION
%doc %{buildoutputdir}/images/%{jdkimage}/LICENSE
%doc %{buildoutputdir}/images/%{jdkimage}/THIRD_PARTY_README
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/lib
%{_jvmdir}/%{sdkdir}/bin/*
%{_jvmdir}/%{sdkdir}/include/*
%{_jvmdir}/%{sdkdir}/lib/*
%{_jvmjardir}/%{sdkdir}
%{_datadir}/applications/*jconsole.desktop
%{_mandir}/man1/appletviewer-%{uniquesuffix}.1*
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
%{_mandir}/man1/jdeps-%{uniquesuffix}.1*
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
%{_mandir}/man1/rmic-%{uniquesuffix}.1*
%{_mandir}/man1/schemagen-%{uniquesuffix}.1*
%{_mandir}/man1/serialver-%{uniquesuffix}.1*
%{_mandir}/man1/wsgen-%{uniquesuffix}.1*
%{_mandir}/man1/wsimport-%{uniquesuffix}.1*
%{_mandir}/man1/xjc-%{uniquesuffix}.1*
%if_enabled systemtap
%dir %{tapsetroot}
%dir %{tapsetdir}
%{tapsetdir}/*%{version}-%{release}.%{_arch}.stp
%dir %{_jvmdir}/%{sdkdir}/tapset
%{_jvmdir}/%{sdkdir}/tapset/*.stp
%endif

%files demo -f %{name}-demo.files
%doc %{buildoutputdir}/images/%{jdkimage}/jre/LICENSE

%files src
%doc README.md
%{_jvmdir}/%{sdkdir}/src.zip

%files javadoc
%_altdir/%altname-javadoc
%_sysconfdir/buildreqs/packages/substitute.d/%name-javadoc
%doc %{_javadocdir}/%{uniquejavadocdir}
%doc %{buildoutputdir}/images/%{jdkimage}/jre/LICENSE

# this puts huge file to /usr/share
# unluckily ti is really a documentation file
# and unluckily it really is architecture-dependent, as eg. aot and grail are now x86_64 only
# same for debug variant
%files javadoc-zip
%doc %{_javadocdir}/%{uniquejavadocdir}.zip
%doc %{buildoutputdir}/images/%{jdkimage}/jre/LICENSE

%files accessibility
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libatk-wrapper.so
%{_jvmdir}/%{jredir}/lib/ext/java-atk-wrapper.jar
%{_jvmdir}/%{jredir}/lib/accessibility.properties
%endif

%if %{include_debug_build}
%files debug -f %{name}.files-debug

%files headless-debug  -f %{name}.files-headless-debug

%files devel-debug

%files demo-debug -f %{name}-demo.files-debug

%files src-debug

%files javadoc-debug

%files javadoc-zip-debug

%files accessibility-debug
%endif

%changelog
* Sun Jul 14 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.212.b04-alt2_0jpp8
- new alternatives layout

* Fri Jun 28 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.212.b04-alt1_0jpp8
- new version

* Tue Jun 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.171-alt2_8.b10jpp8
- added provides, cleaned up desktop files

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.171-alt1_8.b10jpp8
- new version

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.161-alt1_0.b14jpp8
- new version

* Wed Feb 13 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0:1.8.0.151-alt2_5.b12jpp8
- NMU: fixed build with gcc-8.

* Fri Jun 22 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.151-alt1_5.b12jpp8
- new version

* Mon May 14 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0:1.8.0.144-alt5_1.b01jpp8
- require java-1.8.0-openjdk for build on all platforms
- built for aarch64

* Thu May 03 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.144-alt4_1.b01jpp8
- merged e2k support

* Mon Nov 27 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.144-alt3_1.b01jpp8
- removed obsolete exports in jvmjardir
- removed obsolete security policy alternatives in _jvmprivdir
- added java-1.x.0-openjdk alternative in jvmdir

* Mon Nov 06 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.144-alt2_1.b01jpp8
- fixed /usr/bin/java provides (closes: #32531)

* Mon Oct 02 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0:1.8.0.144-alt1_1.b01jpp8
- new version

* Tue Jul 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0:1.8.0.71-alt7_1.b15jpp8
- Fixed build with gcc-6

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt6_1.b15jpp8
- dropped dependency on maven-local in javadoc

* Thu Oct 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt5_1.b15jpp8
- trimmed desktop names (closes: #32463)

* Fri Apr 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt4_1.b15jpp8
- hack around mkimage

* Thu Feb 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt3_1.b15jpp8
- cleaned parasyte dep on /usr/bin/java

* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt2_1.b15jpp8
- dropped dependency on maven-local

* Wed Jan 27 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt1_1.b15jpp8
- new version
- TODO: add java8 support to tzdata and use system-wide tzdata-java

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.45-alt1_40.b14jpp7
- new version

