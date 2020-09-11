%define oname bottleneck

%def_with python3

Name: python-module-%oname
Version: 1.2.1
Release: alt2

Summary: Fast NumPy array functions written in Cython
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Bottleneck/

%setup_python_module %oname

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: libnumpy-devel python-module-numpy-testing
BuildRequires: python-module-alabaster python-module-html5lib python-module-notebook python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libnumpy-py3-devel python3-module-numpy-testing
%endif

%description
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%package tests
Summary: Tests for Bottleneck
Group: Development/Python
Requires: %name = %EVR

%description tests
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains tests for Bottleneck.

%if_with python3
%package -n python3-module-%oname
Summary: Fast NumPy array functions written in Cython
Group: Development/Python3

%description -n python3-module-%oname
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%package -n python3-module-%oname-tests
Summary: Tests for Bottleneck
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains tests for Bottleneck.
%endif


%prep
%setup

for i in $(find %oname -type d); do
	touch $i/__init__.py
done

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
#find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags -fno-strict-aliasing

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

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.1-alt2
- Fixed build with numpy.

* Tue Apr 09 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Build new version for python3.7.
- Removed docs and pickles.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

