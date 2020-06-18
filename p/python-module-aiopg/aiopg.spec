# BEGIN SourceDeps(oneline):
BuildRequires: python3(sqlalchemy)
# END SourceDeps(oneline)
%define oname aiopg

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.16.0
Release: alt1.1
Summary: aiopg is a library for accessing a PostgreSQL database from the asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiopg/

BuildArch: noarch

# https://github.com/aio-libs/aiopg.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-psycopg2
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-psycopg2
%endif

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx-devel python3-module-sphinxcontrib-asyncio

%py_provides %oname
%py_requires asyncio psycopg2 sqlalchemy

%description
aiopg is a library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the
Psycopg database driver.

%if_with python3
%package -n python3-module-%oname
Summary: aiopg is a library for accessing a PostgreSQL database from the asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio psycopg2 sqlalchemy

%description -n python3-module-%oname
aiopg is a library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the
Psycopg database driver.
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx3 .
ln -s ../objects.inv docs/

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

%make -C docs html SPHINXBUILD=py3_sphinx-build

rm -f requirements.txt

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
%doc *.txt *.rst examples docs/_build/html
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Fri Apr 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1.1
- NMU: applied logoved fixes

* Sat Apr 20 2019 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1
- New version 0.16.0

* Fri Mar 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.13.2-alt1
- Updated to upstream version 0.13.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.git20150203.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1.git20150203.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150203
- Version 0.6.1

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20150102
- Initial build for Sisyphus

