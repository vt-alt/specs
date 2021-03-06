%define oname xstatic
%define pypi_name XStatic

Name: python-module-%oname
Version: 1.0.1
Release: alt3

Summary: XStatic base package with minimal support code
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

%py_provides %oname


%description
The goal of XStatic family of packages is to provide static file
packages with minimal overhead - without selling you some dependencies
you don't want.

XStatic has some minimal support code for working with the XStatic-*
packages.

%prep
%setup -n %pypi_name-%version

%build
%python_build

%install
%python_install
install -p -m644 %oname/__init__.py %buildroot%python_sitelibdir/%oname/
cp -fR %oname/pkg %buildroot%python_sitelibdir/%oname/

%check
%__python setup.py test

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt3
- Rebuild with new setuptools
- removal build for python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt2
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

