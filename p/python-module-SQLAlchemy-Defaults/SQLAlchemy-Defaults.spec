%define oname SQLAlchemy-Defaults

%def_with python3

Name: python-module-%oname
Version: 0.4.4
Release: alt3.git20141230
Summary: Smart SQLAlchemy defaults for lazy guys, like me
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLAlchemy-Defaults/
Packager: Python Development Team <python@packages.altlinux.org>

# https://github.com/kvesteri/sqlalchemy-defaults.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-six python-module-SQLAlchemy
#BuildPreReq: python-module-Pygments python-module-jinja2
#BuildPreReq: python-module-docutils python-module-flexmock
#BuildPreReq: python-module-psycopg2 python-module-pymysql
#BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-six python3-module-SQLAlchemy
#BuildPreReq: python3-module-Pygments python3-module-jinja2
#BuildPreReq: python3-module-docutils python3-module-flexmock
#BuildPreReq: python3-module-psycopg2 python3-module-pymysql
#BuildPreReq: python3-modules-sqlite3
%endif

%py_provides sqlalchemy_defaults

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python3 python3-base python3-module-Pygments python3-module-SQLAlchemy python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pluggy python3-module-py python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer xz
BuildRequires: python-module-SQLAlchemy python-module-docutils python-module-html5lib python-module-psycopg2 python-module-setuptools python-modules-sqlite3 python3-module-html5lib python3-module-psycopg2 python3-module-setuptools python3-module-sphinx python3-modules-sqlite3 rpm-build-python3 time
BuildRequires: python-module-pytest
BuildRequires: python3-module-pytest
BuildPreReq: python3-module-SQLAlchemy

%description
Smart SQLAlchemy defaults for lazy guys, like me.

%package -n python3-module-%oname
Summary: Smart SQLAlchemy defaults for lazy guys, like me
Group: Development/Python3
%py3_provides sqlalchemy_defaults

%description -n python3-module-%oname
Smart SQLAlchemy defaults for lazy guys, like me.

%prep
%setup

%if_with python3
rm -rf ../python3
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test3
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed May 13 2020 Pavel Vasenkov <pav@altlinux.org> 0.4.4-alt3.git20141230
- (NMU) Fix build with python3-modile-SQLAlchemy
        Fix Requires to python-module-flexmock

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.4-alt2.git20141230.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.4-alt2.git20141230.2
- Fix build with new python3-module-pytest

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.4-alt2.git20141230.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.4-alt2.git20141230
- NMU: added python-module-SQLAlchemy to BRs.

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1.git20141230.1
- NMU: Use buildreq for BR.

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20141230
- Initial build for Sisyphus

