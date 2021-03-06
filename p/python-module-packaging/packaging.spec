%define _unpackaged_files_terminate_build 1
%define oname packaging

%def_with docs
%def_without check

Name: python-module-%oname
Version: 19.0
Release: alt3
Summary: Core utilities for Python packages
License: ASLv2.0 or BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/packaging
BuildArch: noarch

# https://github.com/pypa/packaging.git
Source: %name-%version.tar
Patch0: packaging-19.0-Fix-testsuite-for-pytest-5.x.patch

%if_with docs
BuildRequires: python-module-sphinx-devel
%endif

%if_with check
BuildRequires: python2.7(coverage)
BuildRequires: python2.7(pretend)
BuildRequires: python2.7(pyparsing)
BuildRequires: python2.7(pytest)
%endif

%description
Core utilities for Python packages.

%if_with docs
%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
%summary
This package contains documentation for %oname

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Core utilities for Python packages.

This package contains pickles for %oname.
%endif

%prep
%setup
%patch0 -p1

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%python_build_debug

%install
%python_install

%if_with docs
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python}
tox.py --sitepackages -p auto -o -v

%files
%doc *.rst LICENSE*
%python_sitelibdir/%oname/
%python_sitelibdir/%oname-%version-py%_python_version.egg-info/
%if_with docs
%exclude %python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/* tasks

%files pickles
%python_sitelibdir/*/pickle
%endif

%changelog
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 19.0-alt3
- build python2 only (specially for pytest)

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 19.0-alt2
- Fixed testing against Pytest 5.

* Thu Jun 06 2019 Stanislav Levin <slev@altlinux.org> 19.0-alt1
- 16.8 -> 19.0.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 16.8-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 16.8-alt1
- Updated to upstream version 16.8.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 15.4-alt2.dev0.git20150801.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 15.4-alt2.dev0.git20150801
- rebuild with clean buildreq
- disable tests 

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.4-alt1.dev0.git20150801
- Initial build for Sisyphus

