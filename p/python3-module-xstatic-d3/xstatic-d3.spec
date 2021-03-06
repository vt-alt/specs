%define mname xstatic
%define oname %mname-d3
%define pypi_name XStatic-D3

Name: python3-module-%oname
Version: 3.5.17.0
Release: alt2

Summary: D3 (XStatic packaging standard)
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/%pypi_name/
BuildArch: noarch

Source: %pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-%mname

%py3_provides %mname.pkg.d3
%py3_requires %mname.pkg


%description
D3 JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these
files.

%prep
%setup -n %pypi_name-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/pkg/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*.pth


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.5.17.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.17.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 3.5.17.0-alt1
- 3.5.17.0
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.6.2-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.6.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.1.6.2-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.6.2-alt1
- Initial build for Sisyphus

