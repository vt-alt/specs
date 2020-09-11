%define mname scikits
%define oname %mname.bootstrap

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.1.1
Summary: Bootstrap confidence interval estimation routines for SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.bootstrap/

# https://github.com/cgevans/scikits-bootstrap.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-numpy python-module-scipy
BuildRequires: python-module-numpy-testing
BuildRequires: python-module-nose python-module-pandas
BuildRequires: python-modules-multiprocessing
BuildRequires: python2.7(pyerf)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-numpy python3-module-scipy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-nose python3-module-pandas
BuildRequires: python3(pyerf)
%endif

%py_provides %oname
%py_requires %mname numpy scipy

%description
Scikits.bootstrap provides bootstrap confidence interval algorithms for
scipy.

At present, it is rather feature-incomplete and in flux. However, the
functions that have been written should be relatively stable as far as
results.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pandas

%description tests
Scikits.bootstrap provides bootstrap confidence interval algorithms for
scipy.

At present, it is rather feature-incomplete and in flux. However, the
functions that have been written should be relatively stable as far as
results.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Bootstrap confidence interval estimation routines for SciPy
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy scipy

%description -n python3-module-%oname
Scikits.bootstrap provides bootstrap confidence interval algorithms for
scipy.

At present, it is rather feature-incomplete and in flux. However, the
functions that have been written should be relatively stable as far as
results.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pandas

%description -n python3-module-%oname-tests
Scikits.bootstrap provides bootstrap confidence interval algorithms for
scipy.

At present, it is rather feature-incomplete and in flux. However, the
functions that have been written should be relatively stable as far as
results.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%python_sitelibdir/*-nspkg.pth
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%exclude %python3_sitelibdir/%mname/*/test*
%exclude %python3_sitelibdir/%mname/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/*/test*
%python3_sitelibdir/%mname/*/*/test*
%endif

%changelog
* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1.1
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20150327.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20150327.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20150327
- New snapshot

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20140521
- Initial build for Sisyphus

