%define oname filterpy

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt2
Summary: Kalman filtering and optimal estimation library
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/filterpy/

# https://github.com/rlabbe/filterpy.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-scipy python-module-matplotlib
BuildRequires: python-module-mock
BuildRequires: python-module-nose
BuildRequires: python-module-pygobject3
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python2.7(numpydoc) xvfb-run
BuildRequires: python-module-numpy-testing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-scipy python3-module-matplotlib
BuildRequires: python3-module-mock
BuildRequires: python3-module-nose python3-module-pytz
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-pygobject3 python3-module-pycairo
BuildRequires: python3-module-html5lib python3-module-pbr python3-module-unittest2
%endif

%py_provides %oname

%description
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

%if_with python3
%package -n python3-module-%oname
Summary: Kalman filtering and optimal estimation library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

rm -f requirements.txt

%check
rm -f filterpy/kalman/tests/test_fls.py
rm -f filterpy/kalman/tests/test_kf.py
rm -f filterpy/common/tests/test_discretization.py
python setup.py build_ext -i
PYTHONPATH=%buildroot%python_sitelibdir xvfb-run py.test -vv

%if_with python3
pushd ../python3
rm -f filterpy/common/tests/test_discretization.py
python3 setup.py build_ext -i
PYTHONPATH=%buildroot%python3_sitelibdir xvfb-run py.test3 -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.1.0-alt2
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Updated to upstream version 1.1.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.16-alt1.git20150217.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.16-alt1.git20150217.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20150217
- Version 0.0.16

* Mon Dec 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20141130
- Version 0.0.7

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt2.git20141122
- Moved examples into tests subpackage

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141122
- Initial build for Sisyphus

