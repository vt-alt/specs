%define _unpackaged_files_terminate_build 1
%define oname pylbfgs

%def_with python3

Name: python-module-%oname
Version: 0.2.0.12
Release: alt2
Summary: LBFGS and OWL-QN optimization algorithms
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/PyLBFGS

Source0: https://pypi.python.org/packages/ff/82/5bd1a652ee8d061593f07ba54eb62e72a6a04f60e9fc4273033f5a021d0c/PyLBFGS-%{version}.tar.gz

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose libnumpy-devel
BuildRequires: python-module-numpy-testing python-module-html5lib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose libnumpy-py3-devel
BuildRequires: python3-module-numpy-testing
%endif

%py_provides %oname lbfgs
%py_requires numpy

%description
This is a Python wrapper around Naoaki Okazaki (chokkan)'s liblbfgs
library of quasi-Newton optimization routines (limited memory BFGS and
OWL-QN).

This package aims to provide a cleaner interface to the LBFGS algorithm
than is currently available in SciPy, and to provide the OWL-QN
algorithm to Python users.

%if_with python3
%package -n python3-module-%oname
Summary: LBFGS and OWL-QN optimization algorithms
Group: Development/Python3
%py3_provides %oname lbfgs
%py3_requires numpy

%description -n python3-module-%oname
This is a Python wrapper around Naoaki Okazaki (chokkan)'s liblbfgs
library of quasi-Newton optimization routines (limited memory BFGS and
OWL-QN).

This package aims to provide a cleaner interface to the LBFGS algorithm
than is currently available in SciPy, and to provide the OWL-QN
algorithm to Python users.
%endif

%prep
%setup -q -n PyLBFGS-%{version}

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

cp liblbfgs/README README.libLBFGS

%check
python setup.py test -v
python setup.py build_ext -i
nosetests -vv lbfgs
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 setup.py build_ext -i
nosetests3 -vv lbfgs
popd
%endif

%files
%doc *.rst README.libLBFGS
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst README.libLBFGS
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0.12-alt2
- Fixed build with numpy.

* Thu Apr 04 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.0.12-alt1
- Build new version with python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0.3-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0.3-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0.2-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0.2-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0.2-alt1
- Initial build for Sisyphus

