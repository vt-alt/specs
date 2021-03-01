%define _unpackaged_files_terminate_build 1

# CHECKME
%define _dotnet_templatesrelease 3.1.7

# TODO: build from sources
%define _dotnet_major 2.1

# FIXME
%define _dotnet_corerelease 2.1.25
%define _dotnet_sdkrelease 2.1.813

Name: dotnet-sdk-%_dotnet_major
Version: 2.1.813
Release: alt1

Summary: SDK for the .NET Core runtime and libraries

License: MIT
Group: Development/Other

Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires: rpm-build-intro


BuildRequires(pre): rpm-macros-dotnet

BuildRequires: dotnet-bootstrap-%_dotnet_major = %_dotnet_corerelease

Requires: dotnet-common >= %_dotnet_corerelease

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

%description
SDK for the .NET Core runtime and libraries.

Just copying managed code now.

%prep
%setup

%install
mkdir -p %buildroot%_dotnet_sdk/
cp -a %_libdir/dotnet-bootstrap-%_dotnet_major/sdk/%_dotnet_sdkrelease/* %buildroot%_dotnet_sdk/

# dotnet --info get RID string from this .version, line 3
cp -a %_libdir/dotnet-bootstrap-%_dotnet_major/sdk/%_dotnet_sdkrelease/.version %buildroot%_dotnet_sdk/
#cp -a %_libdir/dotnet-bootstrap-%_dotnet_major/sdk/%_dotnet_sdkrelease/.toolsetversion %buildroot%_dotnet_sdk/

# TODO: standalone package
#mkdir -p %buildroot%_dotnetdir/packs/
#cp -a %_libdir/dotnet-bootstrap/packs/NETStandard.Library.Ref/ %buildroot%_dotnetdir/packs/
#cp -a %_libdir/dotnet-bootstrap/packs/Microsoft.NETCore.App.Ref/ %buildroot%_dotnetdir/packs/

#mkdir -p %buildroot%_dotnetdir/templates/%_dotnet_templatesrelease/
#cp -a %_libdir/dotnet-bootstrap/templates/%_dotnet_templatesrelease/* %buildroot%_dotnetdir/templates/%_dotnet_templatesrelease/

# apphost used as executable, f.i. dotnet tool install --global paket will install it in $HOME/.dotnet/tools as paket
rm -f %buildroot%_dotnet_sdk/AppHostTemplate/apphost

# link deps workaround
#ln -sr %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/apphost %buildroot%_dotnet_sdk/AppHostTemplate/apphost
# we have no apphost in 2.1
#cp %_dotnet_apphostdir/runtimes/%_dotnet_rid/native/apphost %buildroot%_dotnet_sdk/AppHostTemplate/apphost

mkdir -p %buildroot%_cachedir/dotnet/NuGetFallbackFolder/
ln -sr %buildroot%_cachedir/dotnet/NuGetFallbackFolder %buildroot%_libdir/dotnet/sdk/NuGetFallbackFolder

%pre
%groupadd dotnet || :

%files
%dir %_dotnetdir/sdk/
%_dotnet_sdk/

# TODO: standalone package
#%_dotnetdir/packs/NETStandard.Library.Ref/
#%_dotnetdir/packs/Microsoft.NETCore.App.Ref/

# TODO: standalone package
#%dir %_dotnetdir/templates/
#%dir %_dotnetdir/templates/%_dotnet_templatesrelease/
#%_dotnetdir/templates/%_dotnet_templatesrelease/*.nupkg

%_libdir/dotnet/sdk/NuGetFallbackFolder/
%dir %_cachedir/dotnet/
%attr(2775,root,dotnet) %dir %_cachedir/dotnet/NuGetFallbackFolder/

%changelog
* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.813-alt1
- .NET Core SDK 2.1

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
