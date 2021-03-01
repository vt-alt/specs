%define _unpackaged_files_terminate_build 1

%define pre %nil
%define _dotnet_major 2.1
%define _dotnet_corerelease 2.1.25
#define _dotnet_sdkrelease 5.0.103

Name: dotnet-hostfxr-%_dotnet_major
Version: 2.1.25
Release: alt2

Summary: Installer packages for the .NET Core runtime and libraries

License: MIT
Url: https://github.com/dotnet/core-setup
Group: Development/Other

# Source-url: %url/archive/v%version%pre.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires: clang llvm

BuildRequires: cmake libstdc++-devel

BuildRequires(pre): rpm-macros-dotnet

Requires: dotnet-common

%description
This repo contains the code to build the .NET Core runtime,
libraries and shared host (dotnet) installers for all supported platforms.
It does not contain the actual sources to .NET Core runtime;
this source is split across the dotnet/coreclr repo (runtime)
and dotnet/corefx repo (libraries).

# common for current version
%package -n dotnet-%_dotnet_major
Version: %_dotnet_corerelease
Group: Development/Other
Summary: .NET %_dotnet_major full installation

Requires: dotnet-host
Requires: dotnet-coreclr-%_dotnet_major = %_dotnet_corerelease
Requires: dotnet-corefx-%_dotnet_major = %_dotnet_corerelease
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


%prep
%setup
# since glibc 2.26 xlocale.h is removed
#__subst "s|xlocale.h|locale.h|" src/corehost/cli/json/casablanca/include/cpprest/asyncrt_utils.h

# set global runtime location
%__subst "s|/usr/share/dotnet|%_dotnetdir|" src/corehost/common/pal.unix.cpp

%build
cd src/corehost
sh -x ./build.sh \
    --arch %_dotnet_arch \
    --hostver %_dotnet_corerelease \
    --apphostver %_dotnet_corerelease \
    --fxrver %_dotnet_corerelease \
    --policyver %_dotnet_corerelease \
    -portable \
    --commithash 0 || make -C bin/obj/Linux.x64.Release
# (parallel generation fail workaround)

%install
#mkdir -p %buildroot%_dotnetdir/
#install -m755 src/corehost/cli/exe/apphost/apphost %buildroot%_dotnetdir/

mkdir -p %buildroot%_dotnet_shared/
install -m755 src/corehost/cli/dll/libhostpolicy.so %buildroot%_dotnet_shared/
mkdir -p %buildroot%_dotnet_hostfxr/
install -m755 src/corehost/cli/fxr/libhostfxr.so %buildroot%_dotnet_hostfxr/

%files
%doc THIRD-PARTY-NOTICES.TXT README.md CONTRIBUTING.md LICENSE.TXT
%dir %_dotnet_hostfxr/
%_dotnet_hostfxr/libhostfxr.so
%dir %_dotnet_shared/
%_dotnet_shared/libhostpolicy.so

%files -n dotnet-%_dotnet_major


%changelog
* Fri Feb 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.25-alt2
- add dotnet-2.1 virtual package, cleanup spec

* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.25-alt1
- .NET Core 2.1

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt2
- install apphost

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- new version (2.1.9) with rpmgs script

* Wed Dec 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt2
- move versioned dirs to the appropriate packages

* Wed Dec 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)

* Fri Oct 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- NMU: new version 2.1.5.

* Sun May 20 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt2
- rebuild with lvvm6.0

* Thu Feb 22 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version 2.0.5 (with rpmrb script)

* Sat Nov 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script)

* Mon Aug 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3
- .NET Core Runtime 2.0.0 Release

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- .NET Core Runtime 2.0.0 Preview 2 build 25407-01

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview1
- rebuild without bootstrap with RID linux.x64

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packaging

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
