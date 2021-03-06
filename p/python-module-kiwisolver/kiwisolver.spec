%define oname kiwisolver

Name: python-module-%oname
Version: 0.1.3
Release: alt2

Summary: A fast implementation of the Cassowary constraint solver
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/kiwisolver/

# https://github.com/nucleic/kiwi.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++


%description
Kiwi is an efficient C++ implementation of the Cassowary constraint
solving algorithm. Kiwi is an implementation of the algorithm based on
the seminal Cassowary paper. It is not a refactoring of the original C++
solver. Kiwi has been designed from the ground up to be lightweight and
fast. Kiwi ranges from 10x to 500x faster than the original Cassowary
solver with typical use cases gaining a 40x improvement. Memory savings
are consistently > 5x.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
%__python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.3-alt2
- Rebuild with new setuptools.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt1.git20140712.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20140712
- Initial build for Sisyphus

