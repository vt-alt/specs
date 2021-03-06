%define oname clyde

%def_without docs

Name: python3-module-%oname
Version: 0.8.0
Release: alt2
Summary: Command line interface designer
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/clyde/

# https://github.com/clyde-hub/clyde.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-coverage python3-module-jinja2 python3-module-nose
BuildRequires: python3(sugarbowl)
%if_with docs
BuildRequires: python3-module-html5lib python3-module-sphinx-settings python3(sphinx_rtd_theme)
%endif

%py3_provides %oname
%py3_requires sugarbowl jinja2

%description
Clyde is a command line interface designer.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=$PWD
pushd docs
py3_sphinx-build -b html -d _build/doctrees . _build/html
popd
%endif

%check
python3 setup.py test

%files
%doc *.rst demo
%if_with docs
%doc docs/_build/html
%endif
%python3_sitelibdir/*

%changelog
* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.0-alt2
- drop excessive python3-module-jinja2-tests BR

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1.git20141130.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Nov 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt1.git20141130.2
- Rebuilt without docs since doc generation config is incompatible with python-module-sphinx-1.6.5.

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.git20141130.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.git20141130.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20141130.1
- NMU: Use buildreq for BR.

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20141130
- Initial build for Sisyphus
