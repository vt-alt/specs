%define _unpackaged_files_terminate_build 1

%global __find_debuginfo_files %nil

%define sdkversion 2.1.813
%define coreversion 2.1.25

Name: dotnet-bootstrap-2.1
Version: 2.1.25
Release: alt1

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# To check we manually update download url
# FIXME: broken due sdk/core versions mismatch
#%define downloadversion 2.1.403
# from https://www.microsoft.com/net/download/dotnet-core/2.1

# Source-url: https://download.visualstudio.microsoft.com/download/pr/e1883c23-aad6-4658-a0bf-cdfb3d430d26/a2b8bdd775b9f5b1ff3424463955001c/dotnet-sdk-2.1.813-linux-x64.tar.gz
Source: %name-%version.tar

# Source2-url: https://download.visualstudio.microsoft.com/download/pr/0c96a1ac-ea01-42bf-b889-f07566ffe031/2b74d411c54506f9913ca21f5df5f9a8/dotnet-sdk-2.1.813-linux-arm64.tar.gz
Source2: %name-aarch64-%version.tar

ExclusiveArch: x86_64
#     aarch64: NEW bad_elf_symbols detected:
# dotnet-bootstrap-2.1-2.1.24-alt1.aarch64.rpm  /usr/lib64/dotnet-bootstrap-2.1/shared/Microsoft.NETCore.App/2.1.24/libmscordbi.so  U  FPFillR8
#ExclusiveArch: x86_64 aarch64

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

sed -E -i -e "s@CURL_OPENSSL_3@\x0URL_OPENSSL_3@" shared/Microsoft.NETCore.App/%coreversion/System.Net.Http.Native.so
%endif

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/

# due missed lldb (TODO)
rm -f %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/libsosplugin.so
%__subst "s|libsosplugin.so|libsos.so|g" %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/Microsoft.NETCore.App.deps.json

cd %buildroot%_libdir/%name

# See also https://bugzilla.altlinux.org/show_bug.cgi?id=37413
strip \
	shared/Microsoft.NETCore.App/%coreversion/libmscordbi.so \
	shared/Microsoft.NETCore.App/%coreversion/libmscordaccore.so \
	shared/Microsoft.NETCore.App/%coreversion/libhostpolicy.so \
	shared/Microsoft.NETCore.App/%coreversion/libdbgshim.so \
	shared/Microsoft.NETCore.App/%coreversion/libcoreclrtraceptprovider.so \
	shared/Microsoft.NETCore.App/%coreversion/libcoreclr.so \
	shared/Microsoft.NETCore.App/%coreversion/libclrjit.so \
	shared/Microsoft.NETCore.App/%coreversion/System.Security.Cryptography.Native.OpenSsl.so \
	shared/Microsoft.NETCore.App/%coreversion/System.Net.Security.Native.so \
	shared/Microsoft.NETCore.App/%coreversion/System.Net.Http.Native.so \
	shared/Microsoft.NETCore.App/%coreversion/System.Native.so \
	shared/Microsoft.NETCore.App/%coreversion/System.IO.Compression.Native.so \
	shared/Microsoft.NETCore.App/%coreversion/System.Globalization.Native.so \
	sdk/%sdkversion/AppHostTemplate/apphost \
	host/fxr/%coreversion/libhostfxr.so \
	dotnet \
	#

%files
%dir %_libdir/%name/
#_libdir/%name/additionalDeps/
%dir %_libdir/%name/host/
%dir %_libdir/%name/host/fxr/
%_libdir/%name/host/fxr/%coreversion/
%dir %_libdir/%name/sdk/
%_libdir/%name/sdk/%sdkversion/
%dir %_libdir/%name/shared/
%dir %_libdir/%name/shared/Microsoft.NETCore.App/
%_libdir/%name/shared/Microsoft.NETCore.App/%coreversion/
# TODO: drop from bootstrap
%ifarch x86_64
%dir %_libdir/%name/shared/Microsoft.AspNetCore.All/
%dir %_libdir/%name/shared/Microsoft.AspNetCore.App/
%_libdir/%name/shared/Microsoft.AspNetCore.All/%coreversion/
%_libdir/%name/shared/Microsoft.AspNetCore.App/%coreversion/
%endif
#_libdir/%name/store/
%_libdir/%name/LICENSE.txt
%_libdir/%name/ThirdPartyNotices.txt
%_libdir/%name/dotnet

%changelog
* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.25-alt1
- new version (2.1.25) with rpmgs script
- CVE-2021-1721: .NET Core Denial of Service Vulnerability
- CVE-2021-24112: .NET 5 and .NET Core Remote Code Execution Vulnerability

* Thu Jan 28 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.24-alt1
- new version (2.1.24) with rpmgs script
- CVE-2020-1045: Microsoft ASP.NET Core Security Feature Bypass Vulnerability
- CVE-2020-1597: NET Core Remote Code Execution Vulnerability
- CVE-2020-1147: NET Core Remote Code Execution Vulnerability
- CVE-2020-1108: .NET Core Denial of Service Vulnerability
- CVE-2020-0602: ASP.NET Core Denial of Service Vulnerability
- CVE-2019-1302: ASP.NET Core Elevation Of Privilege Vulnerability
- CVE-2019-1301: Denial of Service Vulnerability in .NET Core
- CVE-2018-8269: Denial of Service Vulnerability in OData
- CVE-2019-1075: ASP.NET Core Spoofing Vulnerability
- CVE-2019-0820: .NET Core Tampering Vulnerability
- CVE-2019-0980: ASP.NET Core Denial of Service Vulnerability
- CVE-2019-0981: ASP.NET Core Denial of Service Vulnerability
- CVE-2019-0982: ASP.NET Core Denial of Service Vulnerability
- CVE-2019-0815: ASP.NET Core denial of service vulnerability

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
