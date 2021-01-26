%define _unpackaged_files_terminate_build 1

%def_without bootstrap
# TODO:
%def_with skipmanaged
%def_with libunwind

%define pre %nil

Name: dotnet-coreclr
Version: 3.1.6
Release: alt2

Summary: .NET Core runtime, called CoreCLR, and the base library, called mscorlib

License: MIT
Url: https://github.com/dotnet/coreclr
Group: Development/Other

# Source-url: https://github.com/dotnet/coreclr/archive/v%version%pre.tar.gz
Source: %name-%version.tar
Patch1: 0001-Add-support-for-building-under-glibc-2.26-13785.patch
Patch2: 0001-fix-build-with-clang6.0.patch
Patch3: dotnet-coreclr-alt-not-supported.patch

ExclusiveArch: aarch64 x86_64

#add_verify_elf_skiplist *.dbg

BuildRequires(pre): rpm-macros-dotnet = %version

BuildRequires: /proc

BuildRequires: clang llvm python3

BuildRequires: cmake libstdc++-devel
%if_with libunwind
BuildRequires: libunwind-devel
%endif
BuildRequires: liblttng-ust-devel liblwp-devel
#BuildRequires: lldb-devel
BuildRequires: libicu-devel libuuid-devel zlib-devel libcurl-devel libkrb5-devel libssl-devel
BuildRequires: python-modules-xml

# it is not linked directly (the same like in libicu-devel)
# there are icu detection in a version range
Requires: libicu

%if_with bootstrap
BuildRequires: dotnet-bootstrap = %version
%define bootstrapdir %_libdir/dotnet-bootstrap
%else
BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif

Requires: dotnet-common = %version

%description
This package contains the .NET Core runtime, called CoreCLR,
and the base library, called mscorlib.

It includes the garbage collector, JIT compiler,
base .NET data types and many low-level classes.

.NET Core is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

%prep
%setup
#patch1 -p1
#patch2 -p1
#patch3 -p2

# make strange error if uncomment due isMSBuildOnNETCoreSupported initialized
#find -type f -name "*.sh" | xargs subst "s|/etc/os-release|%_libdir/dotnet/fake-os-release|g"

# TODO: CMake Error: CMake can not determine linker language for target: System.Globalization.Native
#__subst "s|__isMSBuildOnNETCoreSupported=0|__isMSBuildOnNETCoreSupported=1|" build.sh

%if_with libunwind
rm -rfv src/pal/src/libunwind/
%endif

# c8 hack
%__subst "s|VERSION 3....|VERSION 3.4.3|" CMakeLists.txt tests/CMakeLists.txt

%build
export DotNetCoreSdkDir=%bootstrapdir
export DotNetBuildToolsDir=%bootstrapdir
bash -x ./build.sh -release -verbose -skipnuget -ignorewarnings -skiprestoreoptdata -cmakeargs -DENABLE_LLDBPLUGIN=0 \
%if_with libunwind
    -cmakeargs -DCLR_CMAKE_USE_SYSTEM_LIBUNWIND=1 \
%endif
%if_with skipmanaged
    -skipmanaged \
%endif
    %nil

# FIXME: possible hack
cat <<EOF >.version
%version-%release
%_dotnet_corerelease
EOF

%install
mkdir -p %buildroot%_dotnet_shared/
# TODO: some publish use?
cp -a bin/Product/Linux.%_dotnet_arch.Release/{System.Globalization.Native.so,lib*.so,createdump,SOS_README.md} %buildroot%_dotnet_shared/

install -D -m644 .version %buildroot%_dotnet_shared/.version

# superpmi mcs
# https://github.com/dotnet/coreclr/tree/master/src/ToolBox/superpmi

# createdump
# verify-elf: ERROR: ./usr/lib64/dotnet/shared/Microsoft.NETCore.App/2.0.0/createdump: RPATH contains illegal entry "/tmp/.private/lav/RPM/BUILD": /tmp/.private/lav/RPM/BUILD/dotnet-coreclr-2.0.0/bin/obj/Linux.x64.Release/src/dlls/mscordac
# ldd: libmscordaccore.so => /tmp/.private/lav/RPM/BUILD/dotnet-coreclr-2.0.0/bin/obj/Linux.x64.Release/src/dlls/mscordac/libmscordaccore.so
#rm -f %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%_dotnet_corerelease/createdump

# TODO
rm -f %buildroot%_dotnet_shared/libsuperpmi-shim-*.so

rm -f %buildroot%_dotnet_shared/libprotononjit.so

mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/%name.filetrigger << EOF
#!/bin/sh
# remove obsoleted empty dirs (see discussion at https://github.com/dotnet/sdk/issues/2772)
rmdir %_dotnetdir/shared/Microsoft.NETCore.App/* 2>/dev/null || :
EOF
chmod 0755 %buildroot%_rpmlibdir/%name.filetrigger


%files
%doc CODE_OWNERS.TXT LICENSE.TXT PATENTS.TXT THIRD-PARTY-NOTICES.TXT README.md CONTRIBUTING.md
%dir %_dotnet_shared/
%_dotnet_shared/.version
%_dotnet_shared/System.Globalization.Native.so

%_dotnet_shared/libclrgc.so
%_dotnet_shared/libclrjit.so
%_dotnet_shared/libcoreclr.so
%_dotnet_shared/libcoreclrtraceptprovider.so
%_dotnet_shared/libdbgshim.so
%_dotnet_shared/libmscordaccore.so
%_dotnet_shared/libmscordbi.so
#ifarch x86_64
#_dotnet_shared/libprotononjit.so
#endif
# moved to dotnet/diagnostics repo
%_dotnet_shared/SOS_README.md
#_dotnet_shared/libsos.so
#_dotnet_shared/libsuperpmi-shim-collector.so
#_dotnet_shared/libsuperpmi-shim-counter.so
#_dotnet_shared/libsuperpmi-shim-simple.so

#_dotnet_shared/corerun
%_dotnet_shared/createdump
#_dotnet_shared/coreconsole
%_rpmlibdir/%name.filetrigger

%changelog
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt2
- build with external libunwind

* Mon Aug 03 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt1
- new version 3.1.6 (with rpmrb script) (ALT bug 38744)
- .NET Core 3.1.6 - July 14, 2020
- CVE-2020-1108: .NET Core Denial of Service Vulnerability
- CVE-2020-1147: NET Core Remote Code Execution Vulnerability

* Sun Feb 16 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt2
- downgrade required cmake version to 3.4.3

* Mon Dec 16 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version (3.1.0) with rpmgs script

* Sat Oct 05 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version (3.0.0) with rpmgs script
- .NET Core 3.0.0

* Fri May 17 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt2
- more strict libs packing

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- new version 2.1.9 (with rpmrb script)

* Sat Dec 29 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt4
- drop obsoleted empty dir within filetrigger

* Wed Dec 26 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt3
- drop obsoleted empty dir from shared/Microsoft.NETCore.App/

* Wed Dec 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt2
- move versioned dirs to the appropriate packages

* Tue Dec 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)

* Fri Oct 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- NMU: new version (2.1.5) (based on changes by lav@)

* Sat Sep 15 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- new version (2.1.4) with rpmgs script

* Mon Sep 03 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- .NET Core 2.1.3 LTS

* Sun May 20 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt2
- rebuild with llvm 6.0
- set libicu60 require

* Thu Feb 22 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version (2.0.5) with rpmgs script
- CVE-2018-0764, CVE-2018-0786
- backport patch: Add support for building under glibc 2.26

* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version (2.0.3) with rpmgs script

* Mon Aug 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt4
- .NET Core 2.0.0 Release

* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview2
- .NET Core 2.0.0 Preview 2 (2.0.0-preview2-25407-01)
- pack missed createdump

* Wed May 31 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview1
- strict packing

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview1
- rebuild without bootstrap with RID linux.x64

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packing

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1

* Mon Apr 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial release for ALT Sisyphus
