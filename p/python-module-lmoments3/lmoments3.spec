%define oname lmoments3
Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20140925.2
Summary: Estimate linear moments for statistical distribution functions
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/lmoments3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/OpenHydrology/lmoments3.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-numpy python-module-scipy
BuildPreReq: python-module-numpy-testing
BuildPreReq: python-module-nose

%py_provides %oname
%py_requires numpy scipy

%description
This library was designed to use L-moments to calculate optimal
parameters for a number of distributions. This library extends a number
of scipy distributions and provides some additional distributions
frequently used in Extreme Value Analyses.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
nosetests -v

%files
%doc CHANGES.txt *.rst docs/source/*.rst
%python_sitelibdir/*

%changelog
* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1.git20140925.2
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1.git20140925.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20140925
- Initial build for Sisyphus

