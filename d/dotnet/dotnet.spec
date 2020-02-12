%define _unpackaged_files_terminate_build 1


%def_without bootstrap
%define pre %nil

Name: dotnet
Version: 3.1.0
Release: alt2

Summary: Installer packages for the .NET Core runtime and libraries

License: MIT
Url: https://github.com/dotnet/core-setup
Group: Development/Other

# Source-url: %url/archive/v%version%pre.tar.gz
Source: %name-%version.tar

ExclusiveArch: aarch64 x86_64

BuildRequires: clang llvm

BuildRequires: cmake libstdc++-devel

BuildRequires(pre): rpm-macros-dotnet = %version

BuildRequires: dotnet-common = %version

# FIXME
#Requires: dotnet-common >= %_dotnet_major
Requires: dotnet-common >= 3.1
# FIXME: warning: Macro %_dotnet_corerelease not found
# FIXME: error: line 32: Dependency tokens must not contain '%<=>' symbols: Requires: dotnet-coreclr = %_dotnet_corerelease
#Requires: dotnet-coreclr = %_dotnet_corerelease
#Requires: dotnet-corefx = %_dotnet_corerelease
Requires: dotnet-coreclr = %version
Requires: dotnet-corefx = %version
#Requires: dotnet-sdk >= %version

%if_with bootstrap
BuildRequires: dotnet-bootstrap
%define bootstrapdir %_libdir/dotnet-bootstrap
%else
#BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif

%define exedir artifacts/bin/%_dotnet_rid.Debug/corehost

%description
This repo contains the code to build the .NET Core runtime,
libraries and shared host (dotnet) installers for all supported platforms.
It does not contain the actual sources to .NET Core runtime;
this source is split across the dotnet/coreclr repo (runtime)
and dotnet/corefx repo (libraries).

%prep
%setup
# since glibc 2.26 xlocale.h is removed
%__subst "s|xlocale.h|locale.h|" src/corehost/cli/json/casablanca/include/cpprest/asyncrt_utils.h

# set global runtime location
%__subst "s|/usr/share/dotnet|%_dotnetdir|" src/corehost/common/pal.unix.cpp

find -type f -name "*.sh" | xargs subst "s|/etc/os-release|%_dotnetdir/fake-os-release|g"

%build
#DOTNET_TOOL_DIR=%_libdir/dotnet-bootstrap ./build.sh x64 release verbose
cd src/corehost
#DOTNET_TOOL_DIR=%bootstrapdir
sh -x ./build.sh \
    --arch %_dotnet_arch \
    --hostver %_dotnet_corerelease \
    --apphostver %_dotnet_corerelease \
    --fxrver %_dotnet_corerelease \
    --policyver %_dotnet_corerelease \
    -portable \
    --commithash 0

%install
mkdir -p %buildroot%_dotnetdir/
install -m755 %exedir/dotnet %buildroot%_dotnetdir/

mkdir -p %buildroot%_dotnet_shared/
install -m755 %exedir/libhostpolicy.so %buildroot%_dotnet_shared/

mkdir -p %buildroot%_dotnet_hostfxr/
install -m755 %exedir/libhostfxr.so %buildroot%_dotnet_hostfxr/

mkdir -p %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
install -m755 %exedir/apphost %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
install -m644 %exedir/libnethost.so %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
install -m644 %exedir/nethost.h %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
install -m644 %exedir/nethost.h %buildroot%_dotnet_shared/

mkdir -p %buildroot%_bindir/
ln -sr %buildroot%_dotnetdir/dotnet %buildroot%_bindir/dotnet

%files
%doc THIRD-PARTY-NOTICES.TXT README.md CONTRIBUTING.md LICENSE.TXT
%_bindir/dotnet
%_dotnetdir/dotnet

%dir %_dotnet_hostfxr/
%_dotnet_hostfxr/libhostfxr.so
%_dotnet_shared/libhostpolicy.so

# some doubles
%_dotnet_shared/nethost.h


%dir %_dotnetdir/packs/Microsoft.NETCore.App.Host.%_dotnet_rid/
%dir %_dotnet_apphostdir/
%dir %_dotnet_apphostdir/runtimes/
%dir %_dotnet_apphostdir/runtimes/%_dotnet_rid/
%dir %_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/apphost
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/libnethost.so
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/nethost.h

%changelog
* Wed Jan 15 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt2
- fix global runtime location for framework-depended applications

* Tue Dec 17 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

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
