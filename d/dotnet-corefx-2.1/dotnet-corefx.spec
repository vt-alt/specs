%define _unpackaged_files_terminate_build 1

# FIXME: build from sources
%def_with bootstrap
%define pre %nil

%define _dotnet_major 2.1
%define _dotnet_corerelease 2.1.25
#define _dotnet_sdkrelease 5.0.103

Name: dotnet-corefx-%_dotnet_major
Version: 2.1.25
Release: alt1

Summary: .NET Core foundational libraries, called CoreFX

License: MIT
Url: https://github.com/dotnet/corefx
Group: Development/Other

# Source-url: https://github.com/dotnet/corefx/archive/v%{version}%pre.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

BuildRequires(pre): rpm-macros-cmake

BuildRequires(pre): rpm-macros-dotnet

%if_with bootstrap
BuildRequires: dotnet-bootstrap-%_dotnet_major = %_dotnet_corerelease
#= %version
%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major
# currently binary version supports only OpenSSL-1.0 library
# System.Security.Cryptography.Native.OpenSsl.so
#Requires: libssl10
%else
BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif

Requires: dotnet-common >= %version
Requires: dotnet-coreclr-%_dotnet_major = %version

%remove_optflags -frecord-gcc-switches
BuildRequires: clang llvm cmake libstdc++-devel

BuildRequires: libcurl-devel libssl-devel zlib-devel libkrb5-devel

%description
This package contains the the .NET Core foundational libraries, called CoreFX.
It includes classes for collections, file systems, console, XML, async and many others.

Just copied managed binaries now.

%prep
%setup

%__subst "s|.*-Werror.*||" src/Native/Unix/CMakeLists.txt
#find -type f -name "*.sh" | xargs subst "s|/etc/os-release|%_libdir/dotnet/fake-os-release|g"
cat <<EOF >src/version.c
static char sccsid[] __attribute__((used)) = "@(#)Version %version-%release @BuiltBy: %vendor";
EOF

%build
export CC=clang
export CXX=clang++
export __CMakeBinDir=%buildroot%_dotnet_shared/
cd src/Native/Unix
%cmake_insource -DCMAKE_BUILD_TYPE=RELEASE -DFEATURE_DISTRO_AGNOSTIC_SSL=0 -DCMAKE_STATIC_LIB_LINK=0
# TODO
%__subst "s|HAVE_IN_PKTINFO 0|HAVE_IN_PKTINFO 1|" Common/pal_config.h
%make_build
%if_with bootstrap
#DOTNET_TOOL_DIR=%bootstrapdir
# original process:
#./build-native.sh -release -SkipManagedPackageBuild

#dotnet run config.json -release -SkipManagedPackageBuild
%else
#DOTNET_TOOL_DIR=%bootstrapdir ./build.sh x64 release managed verbose
%endif

%install
mkdir -p %buildroot%_dotnet_shared/
%if_with bootstrap
# managed
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/*.dll %buildroot%_dotnet_shared/

# FIXME: possible hack
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/Microsoft.NETCore.App.deps.json %buildroot%_dotnet_shared/

# read during dotnet --version
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/System.Native.a %buildroot%_dotnet_shared/

# native
#cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/System*.so %buildroot%_dotnet_shared/
# FIXME: needed due to new Microsoft.NETCore.App.deps.json
#cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/System.IO.Compression.Native.a                %buildroot%_dotnet_shared/
#cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/System.Net.Http.Native.a                      %buildroot%_dotnet_shared/
#cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/System.Net.Security.Native.a                  %buildroot%_dotnet_shared/
#cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/System.Security.Cryptography.Native.OpenSsl.a %buildroot%_dotnet_shared/

# already in coreclr
rm -fv %buildroot%_dotnet_shared/System.Globalization.Native.so
%endif

cd src/Native/Unix
make install


mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/%name.filetrigger << EOF
#!/bin/sh
# remove obsoleted empty dirs (see discussion at https://github.com/dotnet/sdk/issues/2772)
rmdir %_dotnetdir/shared/Microsoft.NETCore.App/* 2>/dev/null || :
EOF
chmod 0755 %buildroot%_rpmlibdir/%name.filetrigger


%files
%_rpmlibdir/%name.filetrigger
#dir %_dotnet_shared/
%_dotnet_shared/Microsoft.NETCore.App.deps.json
# managed code
%_dotnet_shared/*.dll
# native code
%_dotnet_shared/System.IO.Compression.Native.so
#_dotnet_shared/System.IO.Ports.Native.so
%_dotnet_shared/System.Native.so
%_dotnet_shared/System.Net.Http.Native.so
%_dotnet_shared/System.Net.Security.Native.so
# search for openssl dinamically
%_dotnet_shared/System.Security.Cryptography.Native.OpenSsl.so
%_dotnet_shared/System.IO.Compression.Native.a
#_dotnet_shared/System.IO.Ports.Native.a
%_dotnet_shared/System.Native.a
%_dotnet_shared/System.Net.Http.Native.a
%_dotnet_shared/System.Net.Security.Native.a
%_dotnet_shared/System.Security.Cryptography.Native.OpenSsl.a

%changelog
* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.25-alt1
- new version (2.1.25) with rpmgs script

* Tue Mar 19 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt2
- rebuild with dotnet-common 2.1.9

* Tue Mar 12 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- new version (2.1.9) with rpmgs script
- build native, linking with openssl

* Sat Dec 29 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt4
- drop obsoleted empty dir within filetrigger

* Mon Dec 24 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt3
- drop obsoleted empty dir from shared/Microsoft.NETCore.App/

* Wed Dec 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt2
- move versioned dirs to the appropriate packages

* Wed Dec 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)

* Thu Oct 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt2
- NMU: packaged additional required libraries.

* Fri Oct 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- NMU: new version (2.1.5)

* Mon Feb 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version (2.0.5) with rpmgs script
- CVE-2018-0764, CVE-2018-0786

* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version (2.0.3) with rpmgs script

* Mon Aug 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt4
- .NET Core 2.0.0 Release

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview2
- build with strict dotnet-bootstrap require

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- .NET Core Runtime 2.0.0 Preview 2 build 25407-01

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview1
- rebuild without bootstrap with RID linux.x64

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packing

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1

* Wed Apr 19 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial release for ALT Sisyphus
