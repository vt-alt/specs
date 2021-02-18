# TODO: build from sources
%define _unpackaged_files_terminate_build 1

%define _dotnet_major 5.0
# CHECKME
%define _dotnet_templatesrelease 5.0.3
%define _dotnet_apprefrelease 5.0.0
%define _dotnet_corerelease 5.0.3
%define _dotnet_sdkrelease 5.0.103
%define _dotnet_netstandartrelease 2.1.0

%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major

Name: dotnet-sdk-%_dotnet_major
Version: 5.0.103
Release: alt1

Summary: SDK for the .NET

License: MIT
Group: Development/Other

Source: %name-%version.tar

%define _dotnet_sdkrelease %version

ExclusiveArch: aarch64 x86_64

BuildRequires: rpm-build-intro

# TODO
BuildRequires(pre): rpm-macros-dotnet

#BuildRequires: dotnet-bootstrap-sdk-%_dotnet_major = %_dotnet_sdkrelease
BuildRequires: dotnet-bootstrap-%_dotnet_major = %_dotnet_corerelease
BuildRequires: dotnet-host >= %_dotnet_corerelease

BuildRequires: dotnet-apphost-pack-%_dotnet_major = %_dotnet_corerelease

# SDK unusable without dotnet CLI
#Requires: dotnet-host-%_dotnet_major = %_dotnet_corerelease

Requires: dotnet-common
# = %_dotnet_corerelease

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

Provides: netstandard-targeting-pack-2.1 = %_dotnet_netstandartrelease
Provides: dotnet-targeting-pack-%_dotnet_major = %_dotnet_apprefrelease


%description
SDK for the .NET runtime and libraries.

Just copying managed code now.

%prep
%setup

%install
mkdir -p %buildroot%_dotnet_sdk/
cp -a %bootstrapdir/sdk/%_dotnet_sdkrelease/* %buildroot%_dotnet_sdk/

# dotnet --info get RID string from this .version, line 3
cp -a %bootstrapdir/sdk/%_dotnet_sdkrelease/.version %buildroot%_dotnet_sdk/
cp -a %bootstrapdir/sdk/%_dotnet_sdkrelease/.toolsetversion %buildroot%_dotnet_sdk/

# TODO: standalone package
mkdir -p %buildroot%_dotnetdir/packs/
cp -a %bootstrapdir/packs/NETStandard.Library.Ref/ %buildroot%_dotnetdir/packs/
cp -a %bootstrapdir/packs/Microsoft.NETCore.App.Ref/ %buildroot%_dotnetdir/packs/

mkdir -p %buildroot%_dotnetdir/templates/%_dotnet_templatesrelease/
cp -a %bootstrapdir/templates/%_dotnet_templatesrelease/* %buildroot%_dotnetdir/templates/%_dotnet_templatesrelease/

# apphost used as executable, f.i. dotnet tool install --global paket will install it in $HOME/.dotnet/tools as paket
rm -f %buildroot%_dotnet_sdk/AppHostTemplate/apphost

# link deps workaround
#ln -sr %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/apphost %buildroot%_dotnet_sdk/AppHostTemplate/apphost
cp %_dotnet_apphostdir/runtimes/%_dotnet_rid/native/apphost %buildroot%_dotnet_sdk/AppHostTemplate/apphost

mkdir -p %buildroot%_cachedir/dotnet/NuGetFallbackFolder/
ln -sr %buildroot%_cachedir/dotnet/NuGetFallbackFolder %buildroot%_libdir/dotnet/sdk/NuGetFallbackFolder

%pre
%groupadd dotnet || :

%files
%dir %_dotnetdir/sdk/
%_dotnet_sdk/

# TODO: standalone package netstandard-targeting-pack-2.1.0
%_dotnetdir/packs/NETStandard.Library.Ref/
# TODO: dotnet-targeting-pack
%_dotnetdir/packs/Microsoft.NETCore.App.Ref/

# TODO: standalone package
%dir %_dotnetdir/templates/
%dir %_dotnetdir/templates/%_dotnet_templatesrelease/
%_dotnetdir/templates/%_dotnet_templatesrelease/*.nupkg

%_libdir/dotnet/sdk/NuGetFallbackFolder/
%dir %_cachedir/dotnet/
%attr(2775,root,dotnet) %dir %_cachedir/dotnet/NuGetFallbackFolder/

%changelog
* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.103-alt1
- .NET SDK 5.0.103
- CVE-2021-1721: .NET Core Denial of Service Vulnerability
- CVE-2021-24112: .NET 5 and .NET Core Remote Code Execution Vulnerability

* Tue Feb 16 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.102-alt1
- .NET 5 SDK

* Wed Aug 05 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.106-alt1
- .NET Core SDK 3.1.106 Release

* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.100-alt5
- revert apphost copying

* Fri Feb 14 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.100-alt4
- add strict dotnet cli requires (SDK unusable without it)
- replace copy of apphost with link to the original

* Sat Dec 28 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.100-alt3
- build on aarch64

* Wed Dec 18 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.100-alt2
- add NETStandard.Library.Ref and Microsoft.NETCore.App.Ref targeting packs

* Tue Dec 17 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.100-alt1
- .NET Core SDK 3.1.100 Release

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt2
- override apphost binary from our build

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- .NET Core SDK 2.1.505 Release

* Wed Dec 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- .NET Core SDK 2.1.500 Release

* Fri Oct 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- NMU: .NET Core SDK 2.1.5 Release

* Thu Feb 08 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- .NET Core SDK 2.0.5 Release
- CVE-2018-0764, CVE-2018-0786

* Sun Nov 26 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- .NET Core SDK 2.0.3 Release

* Mon Aug 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt4
- .NET Core SDK 2.0.0 Release
- add /var/cache/dotnet/NuGetFallbackFolder for packages common cache

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview2
- use dotnet-bootstrap-sdk buildreq

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- .NET Core SDK 2.0.0 Preview 2 build 006497

* Wed May 31 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview1
- fix requires, provides
- add missed .version

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packing

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
