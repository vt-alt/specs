%define _unpackaged_files_terminate_build 1
%define oname descartes

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.1.p9.1
Summary: Use geometric objects as matplotlib paths and patches
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/descartes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/1d/6f/81735a30432b74f41db6754dd13869021ccfed3088d1cf7a6cfc0af9ac49/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: libnumpy-devel python-module-shapely python-module-nose
#BuildPreReq: python-module-matplotlib
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: libnumpy-py3-devel python3-module-shapely
#BuildPreReq: python3-module-nose python3-module-matplotlib
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-cycler python-module-dateutil python-module-genshi python-module-jinja2 python-module-numpy python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cycler python3-module-dateutil python3-module-numpy python3-module-pyparsing python3-module-pytest python3-module-setuptools python3-module-six xz
BuildRequires: python-module-docutils python-module-html5lib python-module-matplotlib python-module-nose python-module-numpy-testing python-module-setuptools python-module-shapely python3-module-matplotlib python3-module-nose python3-module-numpy-testing python3-module-setuptools python3-module-shapely rpm-build-python3 time

%description
Use Shapely or GeoJSON-like geometric objects as matplotlib paths and
patches.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Use Shapely or GeoJSON-like geometric objects as matplotlib paths and
patches.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Use geometric objects as matplotlib paths and patches
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Use Shapely or GeoJSON-like geometric objects as matplotlib paths and
patches.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Use Shapely or GeoJSON-like geometric objects as matplotlib paths and
patches.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

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

%check
#python setup.py test
#nosetests
#if_with python3
#pushd ../python3
#python3 setup.py test
#nosetests3
#popd
#endif
#
%files
%doc *.txt PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Apr 22 2021 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.1.p9.1
- Disable tests.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt3.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt3.1
- NMU: Use buildreq for BR.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt3
- Fixed build

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added requirement on shapely for Python 3 (for tests)
- Enabled testing with nose

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

