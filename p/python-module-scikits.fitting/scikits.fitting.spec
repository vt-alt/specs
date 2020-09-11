%define mname scikits
%define oname %mname.fitting

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.7
Release: alt3
Summary: Framework for fitting functions to data with SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.fitting/

# https://github.com/ludwigschwardt/scikits.fitting.git
# Source-url: https://pypi.io/packages/source/s/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-scipy libnumpy-devel
BuildRequires: python-module-numpy-testing
BuildRequires: python-module-matplotlib python-module-nose

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-scipy libnumpy-py3-devel
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-matplotlib python3-module-nose
%endif

%py_provides %oname
%py_requires %mname numpy scipy matplotlib

%description
A framework for fitting functions to data with SciPy which unifies the
various available interpolation methods and provides a common interface
to them.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires nose

%description tests
A framework for fitting functions to data with SciPy which unifies the
various available interpolation methods and provides a common interface
to them.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Add-on packages for SciPy
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
SciKits (short for SciPy Toolkits), are add-on packages for SciPy,
hosted and developed separately from the main SciPy distribution. All
SciKits are available under the 'scikits' namespace and are licensed
under OSI-approved licenses.

%if_with python3
%package -n python3-module-%oname
Summary: Framework for fitting functions to data with SciPy
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy scipy matplotlib

%description -n python3-module-%oname
A framework for fitting functions to data with SciPy which unifies the
various available interpolation methods and provides a common interface
to them.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires nose

%description -n python3-module-%oname-tests
A framework for fitting functions to data with SciPy which unifies the
various available interpolation methods and provides a common interface
to them.

This package contains tests for %oname.

%package -n python3-module-%mname
Summary: Add-on packages for SciPy
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
SciKits (short for SciPy Toolkits), are add-on packages for SciPy,
hosted and developed separately from the main SciPy distribution. All
SciKits are available under the 'scikits' namespace and are licensed
under OSI-approved licenses.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc *.txt
%python_sitelibdir/%mname/fitting
%python_sitelibdir/*.egg-info
%python_sitelibdir/*-nspkg.pth
%exclude %python_sitelibdir/%mname/fitting/tests

%files tests
%python_sitelibdir/%mname/fitting/tests

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/fitting
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%exclude %python3_sitelibdir/%mname/fitting/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/fitting/tests

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Thu Apr 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 1:0.7-alt3
- Requires fixed.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1:0.7-alt2
- Added missing dep on `numpy.testing`.

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1:0.7-alt1
- new version 0.7 (with rpmrb script)
- switch to build from tarball

* Wed Mar 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.6-alt2
- Reintroduced common packages python-module-scikits and python3-module-scikits.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6-alt1
- Updated to upstream version 0.6.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt2.git20121029.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt2.git20121029.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2.git20121029
- Rebuilt with updated NumPy

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20121029
- Initial build for Sisyphus

