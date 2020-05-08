%define oname evelink

%def_with python3

Name: python-module-%oname
Version: 0.7.5
Release: alt1.2
Summary: Python Bindings for the EVE Online API
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/EVELink/

# https://github.com/eve-val/evelink.git
Source: %name-%version.tar
Patch0: evelink-async-fix.patch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-z4r-coveralls python-module-mock
BuildRequires: python-module-nose
BuildRequires: python-modules-wsgiref python-modules-sqlite3
BuildRequires: python3-module-html5lib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-z4r-coveralls python3-module-mock
BuildRequires: python3-module-nose
BuildRequires: python3-modules-sqlite3
%endif

%py_provides %oname

%add_findreq_skiplist %python_sitelibdir/%oname/appengine/*
%add_findprov_skiplist %python_sitelibdir/%oname/appengine/*
%if_with python3
%add_findreq_skiplist %python3_sitelibdir/%oname/appengine/*
%add_findprov_skiplist %python3_sitelibdir/%oname/appengine/*
%endif

%description
EVELink provides a means to access the EVE XML API from Python.

%if_with python3
%package -n python3-module-%oname
Summary: Python Bindings for the EVE Online API
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip evelink.thirdparty.six.moves six.moves.configparser

%description -n python3-module-%oname
EVELink provides a means to access the EVE XML API from Python.
%endif

%prep
%setup
%patch0 -p1

# Set correct python2 executable in shebang and scripts
subst 's|#!.*python$|#!%__python|' $(grep -Rl '#!.*python$' *) \
    $(find ./ -name '*.py')

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py build_ext -i
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
nosetests3 -v
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Apr 30 2020 Pavel Vasenkov <pav@altlinux.org> 0.7.5-alt1.2
- (NMU) fixed:
  * rename variable with reserved name
  * set correct python2 executable in shebang and scripts

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.5-alt1
- Updated to upstream version 0.7.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.p2.git20141130.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.p2.git20141130.1
- NMU: Use buildreq for BR.

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.p2.git20141130
- Initial build for Sisyphus

