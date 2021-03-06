%define mname xstatic
%define oname %mname-html5shiv
%define pypi_name XStatic-html5shiv

Name: python-module-%oname
Version: 3.6.1
Release: alt4

Summary: html5shiv (XStatic packaging standard)
License: MIT & GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-%mname

%py_provides %mname.pkg.html5shiv
%py_requires %mname.pkg


%description
html5shiv packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these
files.

%prep
%setup -n %pypi_name-%version

%build
%python_build_debug

%install
%python_install

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%check
%__python setup.py test

%files
%doc *.txt
%python_sitelibdir/%mname/pkg/*
%python_sitelibdir/*.egg-info


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.6.1-alt4
- Rebuild with new setuptools
- removal build for python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.6.1-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 3.6.1-alt3
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.1-alt2.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.1-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.6.1-alt2.1
- NMU: Use buildreq for BR.

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Applied python-module-xstatic-html5shiv-3.6.1-alt1.diff

* Mon Nov 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

