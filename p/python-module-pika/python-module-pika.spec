%define modulename pika

%def_with python3

Name: python-module-%modulename
Version: 1.1.0
Release: alt1

%setup_python_module %modulename

Summary: Pika is a pure-Python implementation of the AMQP 0-9-1 protocol.

License: MPLv2.0
Group: Development/Python
Url: http://github.com/pika/pika

BuildArch: noarch

# Source-git: https://github.com/pika/pika.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx-devel python-module-twisted-core
BuildRequires: python-module-tornado

%add_python_req_skip asyncio

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires twisted.internet tornado

%description
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library.

%package docs
Summary: Documentation for %modulename
Group: Development/Documentation

%description docs
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library.

This package contains documentation for %modulename.

%package -n python3-module-%modulename
Summary: Pika is a pure-Python implementation of the AMQP 0-9-1 protoco
Group: Development/Python3
%py3_requires twisted.internet tornado

%description -n python3-module-%modulename
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

# generate html docs
python setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf build/sphinx/html/.{doctrees,buildinfo}

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


%files
%doc *.rst
%python_sitelibdir/*

%files docs
%doc build/sphinx/html/*

%if_with python3
%files -n python3-module-%modulename
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat May 02 2020 Pavel Vasenkov <pav@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.14-alt1.git20141201.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.14-alt1.git20141201.1
- NMU: Use buildreq for BR.

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.14-alt1.git20141201
- New snapshot

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.14-alt1.git20140711
- Version 0.9.14
- Added module for Python 3

* Tue Jan 17 2012 Alexey Morsov <swi@altlinux.ru> 0.9.5-alt1.git20120106
- initial build

