%define mname xstatic
%define oname %mname-jquery
%define pypi_name XStatic-jQuery

Name: python-module-%oname
Version: 1.10.2.1
Release: alt3

Summary: jQuery (XStatic packaging standard)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-%mname

%py_provides %mname.pkg.jquery
%py_requires %mname.pkg


%description
jQuery javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these
files.

%prep
%setup -n %pypi_name-%version

%build
%python_build_debug

%install
%python_install

%check
%__python setup.py test

%files
%doc *.txt
%python_sitelibdir/%mname/pkg/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*.pth


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.10.2.1-alt3
- Rebuild with new setuptools
- removal build for python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10.2.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.2.1-alt2
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.2.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.2.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.10.2.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2.1-alt1
- Initial build for Sisyphus

