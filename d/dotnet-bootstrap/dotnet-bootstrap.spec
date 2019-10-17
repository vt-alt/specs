%define _unpackaged_files_terminate_build 1

%define sdkversion 3.0.100
%define coreversion 3.0.0

Name: dotnet-bootstrap
Version: 3.0.0
Release: alt1

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# To check we manually update download url
# FIXME: broken due sdk/core versions mismatch
#%define downloadversion 2.1.403
# from https://www.microsoft.com/net/download/dotnet-core/2.1

# Source-url: https://download.visualstudio.microsoft.com/download/pr/886b4a4c-30af-454b-8bec-81c72b7b4e1f/d1a0c8de9abb36d8535363ede4a15de6/dotnet-sdk-3.0.100-linux-x64.tar.gz
Source: %name-%version.tar
# Source2-url: https://download.visualstudio.microsoft.com/download/pr/cbc83a0e-895c-4959-99d9-21cd11596e64/b0e59c2ba2bd3ef0f592acbeae7ab27d/dotnet-sdk-3.0.100-linux-arm64.tar.gz
Source2: %name-aarch64-%version.tar

ExclusiveArch: x86_64 aarch64

#Requires: /proc
#BuildPreReq: /proc

%set_verify_elf_method textrel=relaxed
AutoReq: no,lib,shell
AutoProv: no

BuildRequires: libunwind >= 1.1
BuildRequires: liblttng-ust >= 2.8.0
BuildRequires: libcurl
BuildRequires: libkrb5

# for System.Security.Cryptography.Native.OpenSsl.so
# but already required by libkrb5
#Requires: libcrypto10 libssl10

# it is not linked directly (need the same version like in libicu-devel)
# there are icu detection in a version range
Requires: libicu

Provides: dotnet-bootstrap-runtime = %coreversion
Provides: dotnet-bootstrap-sdk = %sdkversion

%description
This package contains full .NET Core SDK binaries, needed for bootstrap build.

https://github.com/dotnet/core/blob/master/release-notes/download-archives/%version-download.md

%prep
%setup
%ifarch aarch64
rm -rf packs/ host/ shared/
tar xfv %SOURCE2
# hack: we have lib64/ld-linux-aarch64.so.1
sed -E -i -e "s@/lib/ld-linux-aarch64.so.1@/lib64/ld-2.27.so\x0________@" \
    dotnet \
    shared/Microsoft.NETCore.App/%coreversion/{*.so,createdump} \
    host/fxr/%coreversion/libhostfxr.so \
    sdk/%sdkversion/AppHostTemplate/apphost \
    packs/Microsoft.NETCore.App.Host.linux-arm64/%coreversion/runtimes/linux-arm64/native/*
sed -E -i -e "s@CURL_OPENSSL_3@\x0URL_OPENSSL_3@" shared/Microsoft.NETCore.App/3.0.0/System.Net.Http.Native.so
%endif

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/

# due missed lldb (TODO)
rm -f %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/libsosplugin.so
%__subst "s|libsosplugin.so|libsos.so|g" %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/Microsoft.NETCore.App.deps.json

%files
%dir %_libdir/%name/
%dir %_libdir/%name/templates/
%_libdir/%name/templates/%coreversion/
%dir %_libdir/%name/packs/
%dir %_libdir/%name/packs/Microsoft.AspNetCore.App.Ref
%_libdir/%name/packs/Microsoft.AspNetCore.App.Ref/%coreversion/
%ifarch aarch64
%dir %_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-arm64/
%_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-arm64/%coreversion/
%else
%dir %_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-x64/
%_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-x64/%coreversion/
%endif
%dir %_libdir/%name/packs/Microsoft.NETCore.App.Ref/
%_libdir/%name/packs/Microsoft.NETCore.App.Ref/%coreversion/
%dir %_libdir/%name/packs/NETStandard.Library.Ref/
%_libdir/%name/packs/NETStandard.Library.Ref/2.1.0/
%dir %_libdir/%name/host/
%dir %_libdir/%name/host/fxr/
%_libdir/%name/host/fxr/%coreversion/
%dir %_libdir/%name/sdk/
%_libdir/%name/sdk/%sdkversion/
%dir %_libdir/%name/shared/
%dir %_libdir/%name/shared/Microsoft.NETCore.App/
%_libdir/%name/shared/Microsoft.NETCore.App/%coreversion/
# TODO: drop from bootstrap
#dir %_libdir/%name/shared/Microsoft.AspNetCore.All/
%dir %_libdir/%name/shared/Microsoft.AspNetCore.App/
#_libdir/%name/shared/Microsoft.AspNetCore.All/%coreversion/
%_libdir/%name/shared/Microsoft.AspNetCore.App/%coreversion/
#_libdir/%name/store/
%_libdir/%name/LICENSE.txt
%_libdir/%name/ThirdPartyNotices.txt
%_libdir/%name/dotnet

%changelog
* Sat Oct 05 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version (3.0.0) with rpmgs script
- .NET Core 3.0.0 - September 23, 2019

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- new version 2.1.9 (with rpmrb script)
- includes .NET Core 2.1.9, ASP.NET Core 2.1.9 and .NET Core SDK 2.1.505
- CVE-2019-0657: .NET Core NuGet Tampering Vulnerability

* Tue Dec 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)
- includes .NET Core 2.1.6, ASP.NET Core 2.1.6 and .NET Core SDK 2.1.500

* Fri Oct 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- NMU: new version (2.1.5) (based on changes by lav@)
- includes .NET Core 2.1.5, ASP.NET Core 2.1.5 and .NET Core SDK 2.1.403

* Sat Sep 15 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- new version (2.1.4) with rpmgs script
- includes .NET Core 2.1.4, ASP.NET Core 2.1.4 and .NET Core SDK 2.1.402

* Mon Sep 03 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version (2.1.3) with rpmgs script
- includes .NET Core 2.1.3, ASP.NET Core 2.1.3 and .NET Core SDK 2.1.401

* Mon Feb 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version (2.0.5) with rpmgs script
- CVE-2018-0764, CVE-2018-0786

* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version (2.0.3) with rpmgs script

* Sun Aug 27 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3
- new version (2.0.0) with rpmgs script

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- enable autoreq for libs, shell
- fix buildreqs to correct generated requires

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview2
- add provides with .NET Core runtime/SDK versions

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview2
- .NET Core Runtime 2.0.0 Preview 2 build 25407-01
- .NET Core SDK 2.0.0 Preview 2 build 006497

* Thu May 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1.005977
- .NET Core Runtime 2.0.0 Preview 1 build 002111
- .NET Core SDK 2.0.0 Preview 1 build 005977

* Fri Apr 28 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version (1.1.1) with rpmgs script (SDK 1.0.3)

* Fri Apr 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial release for ALT Sisyphus
