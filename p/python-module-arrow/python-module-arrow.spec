%define modname arrow

%def_with python2
%def_disable python2_tests

Name: python-module-%modname
Version: 0.14.7
Release: alt1
Summary: Better dates & times for Python
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/arrow/

# https://github.com/crsmithdev/arrow.git
Source: https://pypi.io/packages/source/a/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-dateutil python3-module-nose
BuildPreReq: python3-module-nose-cov python3-module-chai
BuildPreReq: python3-module-sphinx
BuildPreReq: python3-module-simplejson
BuildRequires: python3-module-mock

%if_with python2
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-dateutil python-module-nose
BuildPreReq: python-module-nose-cov python-module-chai
BuildPreReq: python-module-sphinx
BuildRequires: python-module-mock
%py_provides %modname
%endif

%description
Arrow is a Python library that offers a sensible, human-friendly
approach to creating, manipulating, formatting and converting dates,
times, and timestamps. It implements and updates the datetime type,
plugging gaps in functionality, and provides an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%package -n python3-module-%modname
Summary: Better dates & times for Python
Group: Development/Python3
%py3_provides %modname

%description -n python3-module-%modname
Arrow is a Python library that offers a sensible, human-friendly
approach to creating, manipulating, formatting and converting dates,
times, and timestamps. It implements and updates the datetime type,
plugging gaps in functionality, and provides an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%prep
%setup -n %modname-%version %{?_with_python2:-a0}
%{?_with_python2:mv %modname-%version python2}

%build
%python3_build_debug

%if_with python2
pushd python2
%python_build_debug
popd
%endif

%install
%python3_install

%if_with python2
pushd python2
%python_install
popd
%endif

export PYTHONPATH=%buildroot%python3_sitelibdir
SPHINXBUILD=sphinx-build-3 %make -C docs html
mkdir man
cp -fR docs/_build/html/* man/

%check
python3 setup.py test

%if_with python2
%if_enabled python2_tests
pushd python2
python2 setup.py test
popd
%endif
%endif

%if_with python2
%files
%doc *.md *.rst LICENSE man/
%python_sitelibdir/*
%endif

%files -n python3-module-%modname
%doc *.md *.rst LICENSE man/
%python3_sitelibdir/*

%changelog
* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.14.7-alt1
- 0.14.7

* Fri Aug 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.14.6-alt1
- 0.14.6

* Wed Aug 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.14.5-alt1
- 0.14.5
- made python2 build optional

* Mon Mar 26 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt1
- Version 0.10.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.4-alt1.git20140812.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.4-alt1.git20140812.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20140812
- Initial build for Sisyphus

