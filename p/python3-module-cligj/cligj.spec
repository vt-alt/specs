%define _unpackaged_files_terminate_build 1
%define oname cligj

%def_without check

Name: python3-module-%oname
Version: 0.7.0
Release: alt1

Summary: Click params for GeoJSON CLI

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/cligj/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
BuildPreReq: python3-module-click

%description
Common arguments and options for GeoJSON processing commands, using
Click.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test3 -vv

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt2
- build python3 package separately

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)
- switch to build from tarball
- disable check (old code? NameError: name '__nonzero__' is not defined)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150528.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150528
- Version 0.2.0

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141227
- Initial build for Sisyphus

