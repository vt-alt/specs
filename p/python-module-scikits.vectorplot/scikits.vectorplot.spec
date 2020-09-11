%define mname scikits
%define oname %mname.vectorplot

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.2
Release: alt2.git20150130.1.1.1.1
Summary: Vector fields plotting algorithms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.vectorplot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aarchiba/scikits-vectorplot.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-numpy-testing
BuildPreReq: python-module-matplotlib python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-numpy-testing
BuildPreReq: python3-module-matplotlib python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires numpy

%description
Line integral convolution for visualizing vector fields.

%package -n python3-module-%oname
Summary: Vector fields plotting algorithms
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy

%description -n python3-module-%oname
Line integral convolution for visualizing vector fields.

%prep
%setup

echo "__version__ = '%version'" >vectorplot/version.py

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

%check
python setup.py test
python vectorplot/kernels.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 vectorplot/kernels.py
popd
%endif

%files
%doc *.rst vectorplot/doc/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst vectorplot/doc/*
%python3_sitelibdir/*
%endif

%changelog
* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1:0.2-alt2.git20150130.1.1.1.1
- Added missing dep on `numpy.testing`.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.2-alt2.git20150130.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.2-alt2.git20150130.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.2-alt2.git20150130.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2-alt2.git20150130
- Rebuilt with updated NumPy

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2-alt1.git20150130
- Initial build for Sisyphus

