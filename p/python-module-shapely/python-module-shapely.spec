%define _unpackaged_files_terminate_build 1

%define oname shapely

Name: python-module-%oname
Version: 1.7
Release: alt1.b1

Summary: Planar geometries, predicates, and operations

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/Shapely

# https://github.com/Toblerity/Shapely.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libgeos-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-Cython libnumpy-devel
BuildRequires: python-module-descartes python-module-sphinx-devel
BuildRequires: python-module-matplotlib-sphinxext
BuildRequires: python-module-packaging
BuildRequires: python-module-pytest
BuildRequires: python-module-numpy-testing
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Cython libnumpy-py3-devel
BuildRequires: python3-module-descartes
BuildRequires: python3-module-packaging
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy-testing
BuildRequires: xvfb-run

%description
Planar geometries, predicates, and operations.

%package examples
Summary: Examples for %oname
Group: Development/Python
Requires: %name = %EVR

%description examples
Planar geometries, predicates, and operations.

This package contains examples for %oname.

%package -n python3-module-%oname
Summary: Planar geometries, predicates, and operations
Group: Development/Python3

%description -n python3-module-%oname
Planar geometries, predicates, and operations.

%package -n python3-module-%oname-examples
Summary: Examples for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-examples
Planar geometries, predicates, and operations.

This package contains examples for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python
%add_python_req_skip figures

%description pickles
Planar geometries, predicates, and operations.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Planar geometries, predicates, and operations.

This package contains documentation for %oname.

%prep
%setup
cp -fR . ../python3

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export LC_ALL=en_US.UTF-8
%add_optflags -fno-strict-aliasing

%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
export LC_ALL=en_US.UTF-8

%python_install

pushd ../python3
%python3_install
popd

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

# Tests fail on i586 due to fp math precision
%ifnarch %ix86
%check
export LC_ALL=en_US.UTF-8

python setup.py test
python setup.py build_ext -i
py.test -vv

pushd ../python3
xvfb-run python3 setup.py test
python3 setup.py build_ext -i
py.test3 -vv
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/examples

%files examples
%python_sitelibdir/*/examples

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/examples

%changelog
* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7-alt1.b1
- Updated to upstream version 1.7b1 (Closes: #37910)

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.5.17-alt1.post1.1.1.1.1
- Added missing dep on `numpy.testing`.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.17-alt1.post1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.17-alt1.post1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 1.5.17-alt1.post1.1
- Build without geos support

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.17-alt1.post1
- Updated to upstream version 1.5.17.post1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.10-alt1.git20150820.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.10-alt1.git20150820
- Version 1.5.10

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20150202
- New snapshot

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20150104
- Version 1.5.2

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.git20141102
- Version 1.4.4

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1.git20141031
- Version 1.4.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2b6-alt2.1
- Rebuild with Python-2.7

* Tue Apr 13 2010 Denis Klimov <zver@altlinux.org> 1.2b6-alt2
- add build require to python-module-setuptools

* Tue Apr 13 2010 Denis Klimov <zver@altlinux.org> 1.2b6-alt1
- Initial build for ALT Linux

