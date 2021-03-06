%define oname appdirs

Name: python-module-%oname
Version: 1.4.3
Release: alt2

Summary: Determining appropriate platform-specific dirs, e.g. a "user data dir"
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/appdirs/

# https://github.com/ActiveState/appdirs.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

%py_provides %oname


%description
A small Python module for determining appropriate platform-specific
dirs, e.g. a "user data dir".

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
%__python setup.py test

%files
%doc *.rst *.md
%python_sitelibdir/*


%changelog
* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.4.3-alt2
- Rebuild with new setuptools
- remove python3 support (built separately).

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.3-alt1
- Updated to upstream version 1.4.3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.1-alt1.git20150722.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.git20150722
- New snapshot

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.git20140820
- Initial build for Sisyphus

