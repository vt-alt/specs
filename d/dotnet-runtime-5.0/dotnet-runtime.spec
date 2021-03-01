%define _unpackaged_files_terminate_build 1

%define _dotnet_major 5.0
%define _dotnet_corerelease 5.0.3
%define _dotnet_sdkrelease 5.0.103
%define commithash %version-%release

%def_with bootstrap
# TODO:
%def_with skipmanaged
%def_with libunwind

Name: dotnet-runtime-%_dotnet_major
Version: 5.0.3
Release: alt2

Summary: Microsoft .NET Runtime and Microsoft.NETCore.App

License: MIT
Url: https://github.com/dotnet/runtime
Group: Development/Other

# Source-url: https://github.com/dotnet/runtime/archive/v%version.tar.gz
Source: %name-%version.tar

ExclusiveArch: aarch64 x86_64

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

# TODO:
BuildRequires(pre): rpm-macros-dotnet

BuildRequires: /proc

BuildRequires: clang llvm
BuildRequires: python3 >= 3.7.1

# cmake_minimum_required for Native and mono
BuildRequires: cmake >= 3.14.5

BuildRequires: libstdc++-devel
%if_with libunwind
BuildRequires: libunwind-devel
%endif
BuildRequires: liblttng-ust-devel liblwp-devel

#BuildRequires: lldb-devel
BuildRequires: libicu-devel libuuid-devel zlib-devel libcurl-devel libkrb5-devel libssl-devel

# it is not linked directly (the same like in libicu-devel)
# there are icu detection in a version range
Requires: libicu
Requires: libssl >= 1.1

%if_with bootstrap
BuildRequires: dotnet-bootstrap-%_dotnet_major = %version
%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major
%else
BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif

# TODO
Requires: dotnet-common
# = %version

Requires: dotnet-hostfxr-%_dotnet_major = %EVR


%description
This package contains the .NET Core runtime, called CoreCLR,
and the base library, called mscorlib.

.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).

# common for current version
%package -n dotnet-%_dotnet_major
Version: %_dotnet_corerelease
Group: Development/Other
Summary: .NET %_dotnet_major full installation

Requires: dotnet-host
Requires: dotnet-runtime-%_dotnet_major = %EVR
Requires: dotnet-hostfxr-%_dotnet_major = %EVR
#Requires: dotnet-apphost-pack-%_dotnet_major = %EVR

%description -n dotnet-%_dotnet_major
The .NET %_dotnet_major.

This is a virtual package to provide full installation of .NET %_dotnet_major.

.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).

# Note: one for all versions
%package -n dotnet-host
Version: %_dotnet_corerelease
Group: Development/Other
Summary: .NET command line launcher

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

Conflicts: dotnet <= 3.1.6-alt1
Requires: dotnet-common

%description -n dotnet-host
The .NET host is a command line program that runs a standalone
.NET core application or launches the SDK.

.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).


%package -n dotnet-hostfxr-%_dotnet_major
Version: %_dotnet_corerelease
Group: Development/Other
Summary: Microsoft .NET Host FX Resolver
AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

Requires: dotnet-host

%description -n dotnet-hostfxr-%_dotnet_major
The .NET host resolver contains the logic to resolve and select
the right version of the .NET Core SDK or runtime to use.

.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).

%package -n dotnet-apphost-pack-%_dotnet_major
Version: %_dotnet_corerelease
Group: Development/Other
Summary: Microsoft.NETCore.App.Host
AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

%description -n dotnet-apphost-pack-%_dotnet_major
.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).


%prep
%setup

# set global runtime location
%__subst "s|/usr/share/dotnet|%_dotnetdir|" src/installer/corehost/cli/hostmisc/pal.unix.cpp

# replace obsoleted FindPythonInterp with FindPython3
sed -i -e 's|FindPythonInterp|FindPython3|' -e 's|PYTHON_EXECUTABLE|Python3_EXECUTABLE|' \
    src/coreclr/src/pal/src/eventprovider/*/CMakeLists.txt src/coreclr/src/vm/eventing/CMakeLists.txt src/coreclr/src/vm/eventing/*/CMakeLists.txt

%if_with libunwind
rm -rfv src/coreclr/src/pal/src/libunwind/
%endif

# be equal to our bootstrap version
%__subst "s|5.0.100|%_dotnet_sdkrelease|" global.json

%build
#export DotNetRunningInDocker=1
export DotNetCoreSdkDir=%bootstrapdir
export DotNetBuildToolsDir=%bootstrapdir

# Note: version-release instead of git commit
cat <<EOF >.version
%commithash
%_dotnet_corerelease
EOF

# build CLR
cd src/coreclr/
bash -x ./build-runtime.sh -release -verbose -skipmanaged -ignorewarnings -skiprestoreoptdata -nopgooptimize -portablebuild 0\
    -cmakeargs -DENABLE_LLDBPLUGIN=0 -cmakeargs -DFEATURE_SINGLE_FILE_DIAGNOSTICS=0 \
%if_with libunwind
    -cmakeargs -DCLR_CMAKE_USE_SYSTEM_LIBUNWIND=1 \
%endif
    %nil
cd -

# build Native libraries
cd src/libraries/Native/
bash -x ./build-native.sh -release -skipgenerateversion
cd -

# build host commands
export artifacts=$(pwd)/artifacts
cd src/installer/corehost/
sh -x ./build.sh \
    -release \
    -hostver %_dotnet_corerelease \
    -apphostver %_dotnet_corerelease \
    -fxrver %_dotnet_corerelease \
    -policyver %_dotnet_corerelease \
    -skipgenerateversion \
    -portablebuild 0 \
    -coreclrartifacts $artifacts/bin/coreclr/Linux.%_dotnet_arch.Release \
    -nativelibsartifacts  $artifacts/bin/native/Linux-%_dotnet_arch-Release \
    -commithash %commithash \
%if_with libunwind
    -cmakeargs -DCLR_CMAKE_USE_SYSTEM_LIBUNWIND=1 \
%endif
    %nil
cd -

# TODO: run via common build.sh file
#echo ""> artifacts/toolset/%version.txt
# TODO: --build
#sh -x ./build.sh clr+libs --configuration Checked --clang --verbosity normal --cmakeargs -DFEATURE_SINGLE_FILE_DIAGNOSTICS=0 --cmakeargs -DENABLE_LLDBPLUGIN=0
#%if_with libunwind
#    --cmakeargs -DCLR_CMAKE_USE_SYSTEM_LIBUNWIND=1 \
#%endif
#%if_with skipmanaged
#    -skipmanaged \
#%endif
#    %nil


%install
mkdir -p %buildroot%_dotnet_shared/
# TODO: some publish use?
# TODO: drop SOS_README.md?
cp -a artifacts/bin/coreclr/Linux.%_dotnet_arch.Release/{lib*.so,createdump} %buildroot%_dotnet_shared/
cp -a artifacts/bin/native/Linux-%_dotnet_arch-Release/{libSystem.*Native*.so,libSystem.*Native*.a} %buildroot%_dotnet_shared/

mkdir -p %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
cp -a artifacts/bin/linux-%_dotnet_arch.Release/corehost/{apphost,coreclr_delegates.h,hostfxr.h,libnethost.so,libnethost.a,nethost.h,singlefilehost} %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
cp -a artifacts/bin/linux-%_dotnet_arch.Release/corehost/{nethost.h,libhostpolicy.so,libnethost.a,coreclr_delegates.h,hostfxr.h} %buildroot%_dotnet_shared/
mkdir -p %buildroot%_dotnet_hostfxr/
cp -a artifacts/bin/linux-%_dotnet_arch.Release/corehost/libhostfxr.so %buildroot%_dotnet_hostfxr/
mkdir -p %buildroot%_dotnetdir/
install -m755 artifacts/bin/linux-%_dotnet_arch.Release/corehost/dotnet %buildroot%_dotnetdir/

mkdir -p %buildroot%_bindir/
ln -sr %buildroot%_dotnetdir/dotnet %buildroot%_bindir/dotnet

install -D -m644 .version %buildroot%_dotnet_shared/.version

# copy managed libraries as is
%if_with bootstrap
# managed
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/*.dll %buildroot%_dotnet_shared/

# FIXME: possible hack
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/Microsoft.NETCore.App.deps.json %buildroot%_dotnet_shared/

# read during dotnet --version
#cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/System.Native.a %buildroot%_dotnet_shared/
%endif

# missed in the official package
rm -f %buildroot%_dotnet_shared/libsuperpmi-shim-*.so
rm -f %buildroot%_dotnet_shared/libprotononjit.so


%files
%doc LICENSE.TXT PATENTS.TXT THIRD-PARTY-NOTICES.TXT README.md CONTRIBUTING.md
%dir %_dotnet_shared/

%_dotnet_shared/.version
%_dotnet_shared/Microsoft.NETCore.App.deps.json

# managed code
%_dotnet_shared/Microsoft.CSharp.dll
%_dotnet_shared/Microsoft.VisualBasic.Core.dll
%_dotnet_shared/Microsoft.VisualBasic.dll
%_dotnet_shared/Microsoft.Win32.Primitives.dll
%_dotnet_shared/Microsoft.Win32.Registry.dll
%_dotnet_shared/System.*.dll
%_dotnet_shared/System.dll
%_dotnet_shared/WindowsBase.dll
%_dotnet_shared/mscorlib.dll
%_dotnet_shared/netstandard.dll

# native code
%_dotnet_shared/libSystem.IO.Compression.Native.a
%_dotnet_shared/libSystem.IO.Compression.Native.so
%_dotnet_shared/libSystem.IO.Ports.Native.a
%_dotnet_shared/libSystem.IO.Ports.Native.so
%_dotnet_shared/libSystem.Native.a
%_dotnet_shared/libSystem.Native.so
%_dotnet_shared/libSystem.Net.Security.Native.a
%_dotnet_shared/libSystem.Net.Security.Native.so
# search for openssl dinamically
%_dotnet_shared/libSystem.Security.Cryptography.Native.OpenSsl.a
%_dotnet_shared/libSystem.Security.Cryptography.Native.OpenSsl.so

# not in bootstrap
%_dotnet_shared/libclrgc.so
%_dotnet_shared/libdbgshim.so
%_dotnet_shared/libjitinterface.so

%_dotnet_shared/libclrjit.so
%_dotnet_shared/libcoreclr.so
%_dotnet_shared/libcoreclrtraceptprovider.so
%_dotnet_shared/libmscordaccore.so
%_dotnet_shared/libmscordbi.so

%_dotnet_shared/libhostpolicy.so
%_dotnet_shared/libnethost.a

%_dotnet_shared/coreclr_delegates.h
%_dotnet_shared/hostfxr.h
%_dotnet_shared/nethost.h

%_dotnet_shared/createdump

%files -n dotnet-%_dotnet_major
%doc README.md

%files -n dotnet-host
%doc LICENSE.TXT
%dir %_dotnetdir/
%_dotnetdir/dotnet
%_bindir/dotnet
%dir %_dotnetdir/host/
%dir %_dotnetdir/host/fxr/

%files -n dotnet-hostfxr-%_dotnet_major
%dir %_dotnet_hostfxr/
%_dotnet_hostfxr/libhostfxr.so

%files -n dotnet-apphost-pack-%_dotnet_major
%dir %_dotnetdir/
%dir %_dotnetdir/packs/
%dir %_dotnetdir/packs/Microsoft.NETCore.App.Host.%_dotnet_rid/
%dir %_dotnet_apphostdir/
%dir %_dotnet_apphostdir/runtimes/
%dir %_dotnet_apphostdir/runtimes/%_dotnet_rid/
%dir %_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/apphost
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/coreclr_delegates.h
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/hostfxr.h
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/libnethost.a
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/libnethost.so
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/nethost.h
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/singlefilehost

%changelog
* Fri Feb 19 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.3-alt2
- pack dotnet-5.0 full installation package, fix requires

* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.3-alt1
- new version (5.0.3) with rpmgs script
- .NET 5.0.3
- CVE-2021-1721: .NET Core Denial of Service Vulnerability
- CVE-2021-24112: .NET 5 and .NET Core Remote Code Execution Vulnerability

* Tue Feb 16 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt1
- .NET 5 Runtime
