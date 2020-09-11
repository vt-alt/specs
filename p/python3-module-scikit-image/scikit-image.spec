%define _unpackaged_files_terminate_build 1

%define oname scikit-image

%def_disable docs

# some issue similar to https://github.com/cython/cython/issues/1953
%def_disable check

Name: python3-module-%oname
Version: 0.15.0
Release: alt3

Summary: Image processing routines for SciPy
License: BSD
Group: Development/Python3

Url: https://pypi.org/project/scikit-image/
# https://github.com/scikit-image/scikit-image.git
Source: %name-%version.tar
Patch1: %oname-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Cython python3-module-matplotlib
BuildRequires: python3-module-scipy libnumpy-py3-devel
BuildRequires: python3-module-six python3-module-networkx
BuildRequires: python3-module-Pillow
# for tests
BuildRequires: xvfb-run
BuildRequires: python3-module-wavelets python3-module-imageio
# for docs
BuildRequires: python3-module-sphinx

%py3_provides skimage
%py3_requires numpy scipy networkx matplotlib

%description
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%prepare_sphinx3 doc
ln -s ../objects.inv doc/source/

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%if_enabled docs
export PYTHONPATH=%buildroot%python3_sitelibdir
xvfb-run make -C doc pickle
xvfb-run make -C doc html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR doc/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%if_disabled check
rm -f requirements.txt
%endif

%check
python3 setup.py test
rm -f requirements.txt

%files
%doc *.txt *.md
%_bindir/*
%python3_sitelibdir/*
%if_enabled docs
%exclude %python3_sitelibdir/*/pickle
%endif
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*

%if_enabled docs
%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc doc/build/html doc/examples viewer_examples
%else
%files docs
%doc doc/examples viewer_examples
%endif

%changelog
* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.0-alt3
- Fixed build with numpy.

* Sat Mar 14 2020 Michael Shigorin <mike@altlinux.org> 0.15.0-alt2
- Explicit BR: python3-module-sphinx

* Mon Apr 08 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.0-alt1
- Updated to latest upstream release.
- Disabled build for python-2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12-alt1.dev.git20150413.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.12-alt1.dev.git20150413.1
- NMU: Use buildreq for BR.

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1.dev.git20150413
- Version 0.12dev

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev.git20141124
- New snapshot
- Moved all tests into tests subpackage

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev.git20141123
- Initial build for Sisyphus

