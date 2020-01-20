# TODO: fix nuget to operate offline
%def_with prebuild
%def_disable test

Name: powershell
Version: 6.0.0
Release: alt8

Summary: PowerShell for every system!

License: MIT
Url: https://github.com/PowerShell/PowerShell
Group: Development/Other

# Source-url: https://github.com/PowerShell/PowerShell/archive/v%version-beta.1.tar.gz
Source: %name-%version.tar

# built by maintainer (wait for fix nuget in hasher)
Source1: %name-prebuild-%version.tar

Source2: %name.1

ExclusiveArch: %_dotnet_archlist

BuildRequires(pre): rpm-macros-dotnet

AutoReq:yes,nonodejs,nonodejs_native,nomono,nomonolib,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

Requires: dotnet >= 2.0.0
# uses strict version in runtime config
#Requires: dotnet-coreclr = %_dotnet_corerelease

BuildRequires: cmake gcc-c++ dotnet >= 2.0.0 dotnet-sdk >= 2.0.0
%if_enabled test
# for libpsl-native build
BuildRequires: ctest libgtest-devel
%endif

# >= 1.2.100035
Requires: libomi >= 1.2.0
BuildRequires: libpsrp

%if_without prebuild
# local nuget cache
BuildRequires: nuget-packages >= 20170602
%endif

BuildRequires: /proc

%description
PowerShell is a cross-platform (Windows, Linux, and macOS) automation and configuration tool/framework
that works well with your existing tools and is optimized for dealing with structured data
(e.g. JSON, CSV, XML, etc.), REST APIs, and object models. It includes a command-line shell,
an associated scripting language and a framework for processing cmdlets.

%prep
%setup -a1
%__subst "s|.*-Werror.*||" src/libpsl-native/CMakeLists.txt

%__subst "s|\(add_subdirectory(googletest)\)|#\1|g" src/libpsl-native/test/CMakeLists.txt
%if_disabled test
%__subst "s|add_subdirectory(test)||" src/libpsl-native/CMakeLists.txt
%endif

%__subst "s|hash powershell|false|g" build.sh
#rm -f DELETE_ME_TO_DISABLE_CONSOLEHOST_TELEMETRY

%build
# make native library in any case
pushd src/libpsl-native
%cmake_insource -DCMAKE_BUILD_TYPE=Debug
%make_build
# need LANG due FAILED LocaleTest
# FIXME: commented out due hasher
#LANG=en_US.utf8 LD_LIBRARY_PATH=$(pwd)/../powershell-unix make test
popd

%if_without prebuild
#export NUGET_PACKAGES=$(pwd)/nuget
#export NUGET_FALLBACK_PACKAGES=$(pwd)/nuget-fallback
#export NUGET_FALLBACK_PACKAGES=%_libdir/nuget-packages/
#export http_proxy=http://localhost:8081
#mkdir -p $NUGET_PACKAGES
# will continue here after fail on git line
sh -x ./build.sh || :
# /usr/lib64/dotnet/sdk/2.0.0-preview1-005977/Microsoft.Common.CurrentVersion.targets(4326,5): error MSB3030: Could not copy the file "/tmp/.private/lav/RPM/BUILD/powershell-6.0.0/DELETE_ME_TO_DISABLE_CONSOLEHOST_TELEMETRY" because it was not found.
touch DELETE_ME_TO_DISABLE_CONSOLEHOST_TELEMETRY
echo "%version-%release" > powershell.version

#dotnet msbuild src/Microsoft.PowerShell.SDK/Microsoft.PowerShell.SDK.csproj /t:_GetDependencies "/property:DesignTimeBuild=true;_DependencyFile=$(pwd)/src/TypeCatalogGen/powershell.inc" /nologo

cd src/ResGen
#dotnet restore
dotnet run
cd -

cd src/TypeCatalogGen
#dotnet restore
dotnet run ../Microsoft.PowerShell.CoreCLR.AssemblyLoadContext/CorePsTypeCatalog.cs powershell.inc
cd -

cd src/powershell-unix
#dotnet restore
dotnet build --configuration Linux

# TODO: generate man from assets/powershell.1.ronn
%endif

%install
%if_with prebuild
mkdir -p %buildroot%_libdir/%name/
cp -a %name-prebuild/* %buildroot%_libdir/%name/
# hack to use latest runtime
%__subst "s|2.0.0-preview1-002111-00|%_dotnet_corerelease|g" %buildroot%_libdir/%name/powershell.runtimeconfig.json
cp -f src/powershell-unix/libpsl-native.so %buildroot%_libdir/%name/
%else
#dotnet publish --configuration Linux src/powershell-unix/ --output %buildroot%_libdir/%name/ --runtime linux-x64
dotnet publish --configuration Linux src/powershell-unix/ --output %buildroot%_libdir/%name/
rm -rf %buildroot%_libdir/%name/runtimes/{osx,win*}
rm -f %buildroot%_libdir/%name/DELETE_ME_TO_DISABLE_CONSOLEHOST_TELEMETRY
%endif

mkdir -p %buildroot%_bindir/
cat <<EOF >%buildroot%_bindir/%name
#!/bin/sh
exec dotnet %_libdir/%name/powershell.dll "$@"
EOF
chmod 0755 %buildroot%_bindir/%name

# replace downloaded libs with system versions
rm -rf %buildroot%_libdir/%name/runtimes/linux*
mkdir -p %buildroot%_libdir/%name/runtimes/%_dotnet_rid/native/
ln -sf %_libdir/libmi.so %buildroot%_libdir/%name/runtimes/%_dotnet_rid/native/libmi.so
ln -sf %_libdir/libpsrpclient.so %buildroot%_libdir/%name/runtimes/%_dotnet_rid/native/libpsrpclient.so

mkdir -p %buildroot%_man1dir/
cp %SOURCE2 %buildroot%_man1dir/

%if_enabled test
%check
cd src/libpsl-native
LD_LIBRARY_PATH=$(pwd)/../powershell-unix ctest --verbose
%endif

%files
%_bindir/%name
%_libdir/%name/
%_man1dir/%name.*
%doc docs/*

%changelog
* Sat Dec 28 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt8
- enable aarch64 build
- add disabled ctest for libpsl-native
- drop script coreclr version

* Tue Dec 17 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt7
- rebuild with .NET Core 3.1
- disable -Werror

* Wed Mar 20 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt6
- add require to the version from runtime config

* Thu Mar 07 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt5
- drop obsoleted libicu56 require (ALT bug 36210)
- add hack to use latest runtime (ALT bug 36198)

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt4
- always build libpsl-native.so

* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt3
- add dotnet requires

* Sun Jun 11 2017 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt2
- only pack prebuild binaries

* Wed May 31 2017 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt1
- initial release for ALT Sisyphus
