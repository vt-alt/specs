%define oname aiokafka

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.5.1
Release: alt1

Summary: asyncio client for kafka

License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiokafka/

# https://github.com/aio-libs/aiokafka.git
# Source-url: https://pypi.io/packages/source/a/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

# due _crecords
#BuildArch: noarch
BuildRequires: zlib-devel

%if_with python2
BuildRequires: python-dev python-module-setuptools
BuildRequires: python2.7(asyncio) python2.7(kafka)
BuildRequires: python2.7(snappy) python2.7(flake8)
BuildRequires: python2.7(nose)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(asyncio) python3(kafka)
BuildRequires: python3(snappy) python3(flake8)
BuildRequires: python3(nose)
%endif

%py_provides %oname
%py_requires asyncio kafka snappy

%description
Kafka integration with asyncio.

%package -n python3-module-%oname
Summary: asyncio client for kafka
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio kafka snappy

%description -n python3-module-%oname
Kafka integration with asyncio.

%prep
%setup
subst "s|kafka-python==|kafka-python>=|" setup.py

%if_with python3
cp -fR . ../python3
#sed -i 's|flake8|python3-flake8|' ../python3/Makefile
#sed -i 's|nosetests|nosetests3|' ../python3/Makefile
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
#nosetests -s -v ./tests/
%endif
%if_with python3
pushd ../python3
python3 setup.py test
#nosetests3 -s -v ./tests/
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
#exclude %python_sitelibdir/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
#exclude %python3_sitelibdir/tests
%endif

%changelog
* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- new version 0.5.1 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt2
- Fixed build.

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.git20150207.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20150207.1
- NMU: Use buildreq for BR.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150207
- New snapshot

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141230
- Initial build for Sisyphus

