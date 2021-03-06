%define oname pycountry

Name: python-module-%oname
Version: 1.10
Release: alt2

Summary: ISO country, subdivision, language, currency and script definitions
License: LGPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/pycountry

# hg clone https://bitbucket.org/gocept/pycountry
Source: %name-%version.tar
Patch10: %name-%version-alt-python3.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose


%description
ISO country, subdivision, language, currency and script definitions and
their translations.

%package tests
Summary: Tests ISO country, subdivision, language, currency and script definitions
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR

%description tests
Tests for ISO country, subdivision, language, currency and script
definitions and their translations.

%prep
%setup
%patch10 -p1

%build
%python_build_debug

%install
%python_install

%check
%__python setup.py test
nosetests

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests.*

%files tests
%python_sitelibdir/%oname/tests.*


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.10-alt2
- Rebuild with new setuptools
- removal build for python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt1
- Version 1.10

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1
- Version 1.8

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.dev0
- Version 1.3.dev0

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.8-alt1.1
- Fixed build

* Fri Mar 15 2013 Aleksey Avdeev <solo@altlinux.ru> 0.14.8-alt1
- Version 0.14.8
- Add %%name-tests subpackage
- Added module for Python 3

* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.5-alt1
- Initial build for Sisyphus
