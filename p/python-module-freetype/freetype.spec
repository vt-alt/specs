%define oname freetype

%def_with python3

Name: python-module-%oname
Version: 2.1.0.post1
Release: alt1
Summary: Freetype python bindings
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/freetype-py/

# https://github.com/rougier/freetype-py.git
Source: %name-%version.tar
Patch1: %oname-1.1-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-numpy python-module-numpy-testing python-module-matplotlib
BuildRequires: python-module-OpenGL python-module-pygobject3
BuildRequires: python-module-Pillow python-module-pycairo
BuildRequires: python2.7(sphinx_rtd_theme)
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
BuildRequires: python-module-setuptools_scm
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-OpenGL python3-module-pygobject3
BuildRequires: python3-module-Pillow python3-module-pycairo
BuildRequires: python3-module-cffi
BuildRequires: python3-module-setuptools_scm
%endif

%py_provides %oname
Requires: lib%oname
%py_requires ctypes

%description
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

%if_with python3
%package -n python3-module-%oname
Summary: Freetype python bindings
Group: Development/Python3
%py3_provides %oname
Requires: lib%oname
%py3_requires ctypes

%description -n python3-module-%oname
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples doc/_build/html

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.txt
%python3_sitelibdir/*
%endif

%changelog
* Wed May 15 2019 Grigory Ustinov <grenka@altlinux.org> 2.1.0.post1-alt1
- Build new version (Closes: #36320).

* Thu Jan 24 2019 Grigory Ustinov <grenka@altlinux.org> 2.0-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1-alt1
- Updated to upstream version 1.1.

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.git20150409.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.git20150409.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.git20150409.1
- NMU: Use buildreq for BR.

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20150409
- Initial build for Sisyphus

