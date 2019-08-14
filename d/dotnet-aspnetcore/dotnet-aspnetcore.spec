%define _unpackaged_files_terminate_build 1

%define _dotnet_aspnetcore_app %_dotnetdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/
%define _dotnet_aspnetcore_all %_dotnetdir/shared/Microsoft.AspNetCore.All/%_dotnet_corerelease/

# FIXME: build from sources
%def_with bootstrap
%define pre %nil

Name: dotnet-aspnetcore
Version: 2.1.9
Release: alt1

Summary: ASP.NET Core is a cross-platform .NET framework for building modern cloud-based web application

License: MIT
Url: https://github.com/aspnet/AspNetCore
Group: Development/Other

Source: %name-%version.tar

ExclusiveArch: x86_64

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

BuildRequires(pre): rpm-macros-dotnet

%if_with bootstrap
BuildRequires: dotnet-bootstrap-runtime
#= %version
%define bootstrapdir %_libdir/dotnet-bootstrap
%else
BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif

Requires: dotnet-common = %version

# BuildRequires: libuv

#%remove_optflags -frecord-gcc-switches
#BuildRequires: clang llvm cmake libstdc++-devel

#BuildRequires: libcurl-devel libssl-devel zlib-devel libkrb5-devel

%description
ASP.NET Core is an open-source and cross-platform framework
for building modern cloud based internet connected applications,
such as web apps, IoT apps and mobile backends.

ASP.NET Core apps can run on .NET Core or on the full .NET Framework.
It was architected to provide an optimized development framework
for apps that are deployed to the cloud or run on-premises.
It consists of modular components with minimal overhead,
so you retain flexibility while constructing your solutions.

Just copied managed binaries now.

%prep
%setup

%install
mkdir -p %buildroot%_dotnet_aspnetcore_app %buildroot%_dotnet_aspnetcore_all
%if_with bootstrap
# managed
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.All/%_dotnet_corerelease/.version %buildroot%_dotnet_aspnetcore_all
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.All/%_dotnet_corerelease/*.dll %buildroot%_dotnet_aspnetcore_all
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.All/%_dotnet_corerelease/*.json %buildroot%_dotnet_aspnetcore_all

# TODO:
#ln -s %_libdir/libuv.so.1.0.0 %buildroot%_dotnet_aspnetcore_app/libuv.so

cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/.version %buildroot%_dotnet_aspnetcore_app
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/*.dll %buildroot%_dotnet_aspnetcore_app
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/*.json %buildroot%_dotnet_aspnetcore_app
%endif

%files
%dir %_dotnet_aspnetcore_app/
%_dotnet_aspnetcore_app/.version
%_dotnet_aspnetcore_app/Microsoft.AspNetCore.App.deps.json
%_dotnet_aspnetcore_app/Microsoft.AspNetCore.App.runtimeconfig.json
# managed code
%_dotnet_aspnetcore_app/*.dll
# native code
#%_dotnet_aspnetcore_app/
%dir %_dotnet_aspnetcore_all/
%_dotnet_aspnetcore_all/.version
%_dotnet_aspnetcore_all/Microsoft.AspNetCore.All.deps.json
%_dotnet_aspnetcore_all/Microsoft.AspNetCore.All.runtimeconfig.json
%_dotnet_aspnetcore_all/*.dll

%changelog
* Wed May 22 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- initial release for ALT Sisyphus (just copy managed code)
