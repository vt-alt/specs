%define oname jsonpickle

%def_with python3

Name: python-module-%oname
Version: 0.9.5
Release: alt2
Summary: Python library for serializing any arbitrary object graph into JSON
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/jsonpickle/

# git://github.com/jsonpickle/jsonpickle.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-feedparser
BuildRequires: python-module-demjson python-module-jsonlib
BuildRequires: python-module-yajl python-module-ujson
BuildRequires: python-module-nose python-module-coverage
BuildRequires: python-module-pytest
BuildRequires: python-module-sphinxtogithub
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
BuildRequires: python-module-numpy
BuildRequires: python-module-numpy-testing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-demjson python3-module-jsonlib
BuildRequires: python3-module-yajl python3-module-ujson
BuildRequires: python3-module-nose python3-module-coverage
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
%py_requires json demjson jsonlib yajl ujson

%description
jsonpickle converts complex Python objects to and from JSON.

%if_with python3
%package -n python3-module-%oname
Summary: Python library for serializing any arbitrary object graph into JSON
Group: Development/Python3
%py3_provides %oname
%py3_requires demjson jsonlib yajl ujson

%description -n python3-module-%oname
jsonpickle converts complex Python objects to and from JSON.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
jsonpickle converts complex Python objects to and from JSON.

This package contains pickles for %oname.

%package docs
Summary: documentaiton for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
jsonpickle converts complex Python objects to and from JSON.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
sed -i 's|feedparser|speedparser|g' ../python3/tests/*.py
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test3
popd
%endif

%files
%doc *.rst contrib
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst contrib
%python3_sitelibdir/*
%endif

%changelog
* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 0.9.5-alt2
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.5-alt1
- Updated to upstream version 0.9.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.git20150116.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150116.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150116
- Version 0.9.0

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20141022
- Initial build for Sisyphus

