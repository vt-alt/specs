%define oname aioamqp

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.13.0
Release: alt1

Summary: AMQP implementation using asyncio

License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aioamqp/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Polyconseil/aioamqp.git
# Source-url: https://pypi.io/packages/source/a/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-asyncio python-module-nose
#BuildPreReq: python-module-coverage pylint
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pamqp
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-asyncio python3-module-nose
#BuildPreReq: python3-module-coverage pylint-py3
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-logilab-common python3-module-pytest python3-module-setuptools
BuildRequires: pylint-py3 python3-module-coverage python3-module-nose python3-module-setuptools rpm-build-python3

%description
aioamqp library is a pure-Python implementation of the AMQP 0.9.1
protocol.

Built on top on Python's asynchronous I/O support introduced in PEP
3156, it provides an API based on coroutines, making it easy to write
highly concurrent applications.

%package -n python3-module-%oname
Summary: AMQP implementation using asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
aioamqp library is a pure-Python implementation of the AMQP 0.9.1
protocol.

Built on top on Python's asynchronous I/O support introduced in PEP
3156, it provides an API based on coroutines, making it easy to write
highly concurrent applications.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst docs/*.rst examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20141217.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1.git20141217.1
- NMU: Use buildreq for BR.

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141217
- Initial build for Sisyphus

