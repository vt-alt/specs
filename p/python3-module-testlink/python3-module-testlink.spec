%define _unpackaged_files_terminate_build 1
%define oname testlink

Name: python3-module-%oname
Version: 0.8.1
Release: alt2
Summary: A Python client to use the TestLink API
License: Apache 2.0
Group: Development/Python3
Url: https://github.com/lczub/TestLink-API-Python-client
Source: %name-%version.tar
Patch1: add-inactive-active-testplan-feature.patch
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
TestLink-API-Python-client is a Python XML-RPC client for TestLink.

%prep
%setup
%patch1 -p1

%build
%python3_build

%install
%python3_install
cp -r example test %buildroot%python3_sitelibdir/%oname

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/TestLink_API_Python_client-%version-py%_python3_version.egg-info
%doc LICENSE-2.0.txt doc/{install.rst,usage.rst}

%changelog
* Thu Oct 31 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt2
- Add inactive and active feature for testplan

* Tue Oct 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt1
- New version

* Thu Oct 17 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.4-alt1
- Initial build for ALT
