%define oname mysqlclient
%define fname python-module-%oname
%define descr \
mysqlclient is a fork of MySQL-python. It adds Python 3.3 support and \
merges some pull requests.

%def_enable check

Name: %fname
Version: 1.4.4
Release: alt1

%if ""==""
Summary: Python interface to MySQL
Group: Development/Python
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: GPL
Url: https://pypi.python.org/pypi/mysqlclient/
# https://github.com/PyMySQL/mysqlclient-python.git
Source: %name-%version.tar

%if ""!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
BuildArch: noarch
%else
Conflicts: python-module-MySQLdb
Conflicts: python-module-MySQLdb2
Provides: python-module-MySQLdb
%py_provides MySQLdb
%endif

BuildRequires(pre): rpm-macros-sphinx rpm-build-python
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: libmysqlclient-devel python-module-alabaster python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pytest python3-devel python3-module-nose python3-module-pytest rpm-build-python3 time
BuildRequires: python-devel

%description
%descr

%if ""!=""
This package contains documentation for %oname.

%package -n %fname-pickles
Summary: Pickles for %oname
Group: Development/Python

%description -n %fname-pickles
%descr

This package contains pickles for %oname.
%endif

%prep
%setup
%if ""!=""
%prepare_sphinx .
ln -s ../objects.inv doc/
%endif

%build
%if ""==""
%python_build
%else
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html
%endif


%install
%if ""==""
%python_install
%else
install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%if ""==""
%check
python setup.py test

%files
%doc HISTORY* *.md
%python_sitelibdir/*

%else

%files
%doc doc/_build/html/*

%files -n %fname-pickles
%python_sitelibdir/*/pickle
%endif

%changelog
* Mon Aug 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.4-alt1
- Build new version.

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.2.post1-alt3
- Rebuild for python3.7.

* Tue Apr 09 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.2.post1-alt2
- Added explicit BR: python-devel. (thx to mike@)

* Thu Mar 07 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.2.post1-alt1
- Upstream changed version without changes.
- Add provides of python-module-MySQLdb (Closes: #36247).

* Sat Feb 09 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Build new version.

* Sun Jan 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Build new version.

* Fri Dec 21 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.14-alt1
- Build new version.

* Mon Jul 16 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.13-alt1
- Build new version.

* Wed May 30 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.12-alt1
- Build new version.

* Fri May 11 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt2
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.6-alt1.git20150225.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.6-alt1.git20150225.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.6-alt1.git20150225.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20150225
- Version 1.3.6

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20150105
- New snapshot

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20141102
- Initial build for Sisyphus

