%define _unpackaged_files_terminate_build 1

%define oname wavelets

Name: python3-module-%oname
Version: 1.0.2
Release: alt3
Summary: Wavelet Transforms in Python
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/PyWavelets/

# https://github.com/PyWavelets/pywt.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Cython
BuildRequires: python3-module-nose
BuildRequires: python3-module-numpy-testing
BuildRequires: libnumpy-py3-devel

# circumvent build failures due to relying on headers from libnumpy-devel
BuildRequires: libnumpy-devel

%description
PyWavelets is a free Open Source library for wavelet transforms in Python.
Wavelets are mathematical basis functions that are localized in both time
and frequency.
Wavelet transforms are time-frequency transforms employing wavelets.
They are similar to Fourier transforms, the difference being that
Fourier transforms are localized only in frequency instead of in time
and frequency.

The main features of PyWavelets are:
- 1D, 2D and nD Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
- 1D, 2D and nD Multilevel DWT and IDWT
- 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
- 1D and 2D Wavelet Packet decomposition and reconstruction
- 1D Continuous Wavelet Tranfsorm
- Computing Approximations of wavelet and scaling functions
- Over 100 built-in wavelet filters and support for custom wavelets
- Single and double precision calculations
- Real and complex calculations
- Results compatible with Matlab Wavelet Toolbox (TM)

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
PyWavelets is a free Open Source library for wavelet transforms in Python.
Wavelets are mathematical basis functions that are localized in both time
and frequency.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
cd ..
PYTHONPATH=%buildroot%python3_sitelibdir nosetests3 --tests %name-%version/pywt/tests

%files
%doc LICENSE
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt3
- Added missing dep on `numpy.testing`.

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt2
- Rebuild for python3.7.

* Tue Apr 09 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Initial build for ALT.
