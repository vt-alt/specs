%define _unpackaged_files_terminate_build 1

%define _dotnet_major 5.0
%define _dotnet_corerelease 5.0.3

%define _dotnet_asppackrelease 5.0.0
%define _dotnet_aspnetcore_app %_dotnetdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/
%define _dotnet_aspnetcore_all %_dotnetdir/shared/Microsoft.AspNetCore.All/%_dotnet_corerelease/

# FIXME: build from sources
%def_with bootstrap
%define pre %nil

Name: dotnet-aspnetcore-%_dotnet_major
Version: 5.0.3
Release: alt2

Summary: ASP.NET is a cross-platform .NET framework for building modern cloud-based web application

License: MIT
Url: https://github.com/dotnet/aspnetcore
Group: Development/Other

Source: %name-%version.tar

ExclusiveArch: aarch64 x86_64

BuildRequires(pre): rpm-macros-dotnet
# TODO = %version

%if_with bootstrap
#BuildRequires: dotnet-bootstrap-runtime-%_dotnet_major
BuildRequires: dotnet-bootstrap-%_dotnet_major = %version
#= %version
%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major
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
ASP.NET is an open-source and cross-platform framework
for building modern cloud based internet connected applications,
such as web apps, IoT apps and mobile backends.

ASP.NET is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

Just copied managed binaries now.

%package -n dotnet-aspnetcore-runtime-%_dotnet_major
Version: %_dotnet_corerelease
Summary: ASP.NET 5 runtime
Group: Development/Other
#AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoReq: no
AutoProv: no

Requires: dotnet-runtime-%_dotnet_major = %_dotnet_corerelease

%description -n dotnet-aspnetcore-runtime-%_dotnet_major
The ASP.NET runtime contains everything needed to run .NET Core
web applications. It includes a high performance Virtual Machine as
well as the framework libraries used by .NET Core applications.

ASP.NET is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%package -n dotnet-aspnetcore-targeting-pack-%_dotnet_major
Version: %_dotnet_corerelease
Summary: ASP.NET 5 targeting pack
Group: Development/Other
#AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoReq: no
AutoProv: no

Requires: dotnet-targeting-pack-%_dotnet_major

%description -n dotnet-aspnetcore-targeting-pack-%_dotnet_major
The ASP.NET runtime contains everything needed to run .NET Core
web applications. It includes a high performance Virtual Machine as
well as the framework libraries used by .NET Core applications.

ASP.NET is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%prep
%setup

%install
mkdir -p %buildroot%_dotnet_aspnetcore_app
#%buildroot%_dotnet_aspnetcore_all
%if_with bootstrap
# managed
#cp -a %bootstrapdir/shared/Microsoft.AspNetCore.All/%_dotnet_corerelease/.version %buildroot%_dotnet_aspnetcore_all
#cp -a %bootstrapdir/shared/Microsoft.AspNetCore.All/%_dotnet_corerelease/*.dll %buildroot%_dotnet_aspnetcore_all
#cp -a %bootstrapdir/shared/Microsoft.AspNetCore.All/%_dotnet_corerelease/*.json %buildroot%_dotnet_aspnetcore_all

# TODO:
#ln -s %_libdir/libuv.so.1.0.0 %buildroot%_dotnet_aspnetcore_app/libuv.so

cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/.version %buildroot%_dotnet_aspnetcore_app
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/*.dll %buildroot%_dotnet_aspnetcore_app
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/*.json %buildroot%_dotnet_aspnetcore_app

# TODO: subpackage targeting-packs
mkdir -p %buildroot%_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/%_dotnet_asppackrelease/
cp -a %bootstrapdir/packs/Microsoft.AspNetCore.App.Ref/%_dotnet_asppackrelease/* %buildroot%_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/%_dotnet_asppackrelease/

%endif


%files -n dotnet-aspnetcore-runtime-%_dotnet_major
%dir %_dotnetdir/shared/Microsoft.AspNetCore.App/
%dir %_dotnet_aspnetcore_app/
%_dotnet_aspnetcore_app/.version
%_dotnet_aspnetcore_app/Microsoft.AspNetCore.App.deps.json
%_dotnet_aspnetcore_app/Microsoft.AspNetCore.App.runtimeconfig.json
# managed code
%_dotnet_aspnetcore_app/*.dll
# native code
#%_dotnet_aspnetcore_app/
#%dir %_dotnet_aspnetcore_all/
#%_dotnet_aspnetcore_all/.version
#%_dotnet_aspnetcore_all/Microsoft.AspNetCore.All.deps.json
#%_dotnet_aspnetcore_all/Microsoft.AspNetCore.All.runtimeconfig.json
#%_dotnet_aspnetcore_all/*.dll

%files -n dotnet-aspnetcore-targeting-pack-%_dotnet_major
%dir %_dotnetdir/packs/
%dir %_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/
%_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/%_dotnet_asppackrelease/

%changelog
* Fri Feb 19 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.3-alt2
- fix requires

* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.3-alt1
- ASP.NET 5.0.3
- CVE-2021-1721: .NET Core Denial of Service Vulnerability
- CVE-2021-24112: .NET 5 and .NET Core Remote Code Execution Vulnerability

* Tue Feb 16 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt1
- .NET 5

* Sat Aug 08 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt1
- ASP.NET Core 3.1.6

* Tue Dec 17 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- ASP.NET Core 3.1.0

* Wed May 22 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- initial release for ALT Sisyphus (just copy managed code)
