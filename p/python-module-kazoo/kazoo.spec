%define oname kazoo

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.6.1
Release: alt1

Summary: Higher Level Zookeeper Client

License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/kazoo/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/python-zk/kazoo.git
# Source-url: https://pypi.io/packages/source/k/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-dns python-module-enum34 python-module-genshi python-module-greenlet python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-psycopg2 python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-mccabe python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-pyflakes python3-tools-pep8
BuildRequires: python-module-sphinx python-module-alabaster python-module-coverage python-module-docutils python-module-eventlet python-module-flake8 python-module-gevent python-module-html5lib python-module-nose python-module-objects.inv python-module-pbr python-module-pytest python-module-unittest2 python3-module-coverage python3-module-dns python3-module-flake8 python3-module-greenlet python3-module-html5lib python3-module-nose python3-module-pbr python3-module-psycopg2 python3-module-sphinx python3-module-unittest2

#BuildRequires: python-devel python-module-setuptools-tests
#BuildRequires: python-module-coverage python-module-mock
#BuildRequires: python-module-nose python-module-gevent
#BuildRequires: python-module-greenlet python-module-jinja2
#BuildRequires: python-module-Pygments python-module-docutils
#BuildRequires: python-module-sphinx-devel
#BuildRequires: python-module-flake8
#BuildRequires: python-module-eventlet python-module-gevent

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildRequires: python3-module-coverage python3-module-mock
#BuildRequires: python3-module-nose python3-module-gevent
#BuildRequires: python3-module-greenlet python3-module-jinja2
#BuildRequires: python3-module-Pygments python3-module-docutils
#BuildRequires: python3-module-flake8
#BuildRequires: python3-module-eventlet python3-module-gevent
%endif

%py_provides %oname

%description
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Higher Level Zookeeper Client
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

This packag contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

This packag contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle SPHINXBUILD=sphinx-build
%make -C docs html SPHINXBUILD=sphinx-build

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%endif

%changelog
* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version 2.6.1 (with rpmrb script)
- switch to build from tarball

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.2.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20141002
- Initial build for Sisyphus

