Name: gyp
Version: 0.1.h.e87d37d6
Release: alt1

Summary: Generate Your Projects
License: BSD
Group: Development/Tools

Url: http://code.google.com/p/gyp/

BuildArch: noarch

# Source-git: https://chromium.googlesource.com/external/gyp
Source: %name-%version.tar

Patch: gyp-precompiled.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools python3-devel

%description
GYP is a tool to generates native Visual Studio, Xcode and SCons and/or
make build files from a platform-independent input format. Its syntax
is a universal cross-platform build representation that still allows
sufficient per-platform flexibility to accommodate irreconcilable
differences.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install
rm -fv %buildroot/%python3_sitelibdir/%name/generator/*_test.py

%files
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-0.1-*
%doc AUTHORS LICENSE

%changelog
* Thu Jan 16 2020 Vitaly Lipatov <lav@altlinux.ru> 0.1.h.e87d37d6-alt1
- new version (0.1.h.e87d37d6) with rpmgs script
- switch to python3

* Sun Dec 11 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.g940a15e-alt2
- add cmake_precompiled_header support from tdesktop project patch

* Sun Dec 11 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.g940a15e-alt1
- build lastest commit from git

* Sat Jun 16 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.1-alt1.r1415
- Update to SVN r1415

* Tue Mar 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1.r1241
- initial build for Sisyphus

