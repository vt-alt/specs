%define oname yajl

Name: python-module-%oname
Version: 0.3.6
Release: alt2

Summary: A CPython module for Yet-Another-Json-Library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yajl/

# https://github.com/rtyler/py-yajl.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python

%py_provides %oname
%py_requires cjson

BuildRequires: libyajl1-devel python-module-cjson python-module-setuptools


%description
The yajl module provides a Python binding to the Yajl library originally
written by Lloyd Hilaiel.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%check
%__python setup.py test
%__python setup.py build_ext -i
export PYTHONPATH=$PWD
%__python tests/unit.py

%files
%doc README.markdown compare.py
%python_sitelibdir/*


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.6-alt2
- Rebuild with new setuptools
- removal build for python3.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.6-alt1.git20140530.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.6-alt1.git20140530.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt1.git20140530.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt1.git20140530.1
- NMU: Use buildreq for BR.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20140530
- Initial build for Sisyphus

