%define oname tinycss2

%def_without check

Name: python3-module-%oname
Version: 1.0.2
Release: alt1

Summary: Modern CSS parser for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/tinycss2/

BuildArch: noarch

# https://github.com/Kozea/tinycss2.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-webencodings
BuildRequires: python3-module-pytest-isort
BuildRequires: python3-module-pytest-flake8
BuildRequires: python3-module-pytest-cov

%description
tinycss2 is a rewrite of tinycss with a simpler API, based on the more
recent CSS Syntax Level 3 specification.

%prep
%setup

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc CHANGES TODO LICENSE *.rst docs/*.rst docs/css_diagram_role.py
%python3_sitelibdir/*

%changelog
* Mon Jun 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt1
- Version updated to 1.0.2.

* Thu Apr 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1
- Updated to upstream version 0.6.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20140819.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20140819.1
- NMU: Use buildreq for BR.

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20140819
- Initial build for Sisyphus

