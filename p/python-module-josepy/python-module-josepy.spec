%define oname josepy

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt2

Summary: JOSE protocol implementation in Python using cryptography

License: Apache-2.0
Group: Development/Python
Url: https://github.com/certbot/josepy

# Source-url: %__pypi_url %oname
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-intro >= 2.1.3

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

Conflicts: python-module-acme < 0.21.0

%description
JOSE protocol implementation in Python using cryptography.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
JOSE protocol implementation in Python using cryptography

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: JOSE protocol implementation in Python using cryptography
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
JOSE protocol implementation in Python using cryptography

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
JOSE protocol implementation in Python using cryptography

This package contains tests for %oname.
%endif

%prep
%setup

%python3_dirsetup

%build
%python_build_debug
%python3_dirbuild

%install
%python_install
%python3_dirinstall

rm -rf %buildroot%_bindir/

%check
%python_check
%python3_dircheck
# Make sure the script uses the expected python version
#grep -q python3 %buildroot%_bindir/jws


%files
%doc README*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
#%_bindir/jws

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc README*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*test*
%exclude %python3_sitelibdir/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*test*
%python3_sitelibdir/*/*/*test*
%endif

%changelog
* Thu Jul 23 2020 Anton Farygin <rider@altlinux.ru> 1.1.0-alt2
- moved tests from python3-module-%oname package
- fix for License tag according to SPDX

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Sisyphus

