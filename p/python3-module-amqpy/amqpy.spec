%define oname amqpy

%def_with check

Name: python3-module-%oname
Version: 0.12.4
Release: alt2.git20160226
Summary: Pure-Python 3 AMQP client library
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/amqpy/

# https://github.com/veegee/amqpy.git
Source: %name-%version.tar
Patch: 0.12.4-amqpy-Add-rabbitmq-pytest-mark.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildPreReq: python3-module-sphinx

%if_with check
BuildRequires: python3(tox)
%endif

%py3_provides %oname

%description
amqpy is a pure-Python AMQP 0.9.1 client library for Python >= 3.2.0
(including PyPy3) with a focus on:

* stability and reliability
* well-tested and thoroughly documented code
* clean, correct design
* 100%% compliance with the AMQP 0.9.1 protocol specification

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
amqpy is a pure-Python AMQP 0.9.1 client library for Python >= 3.2.0
(including PyPy3) with a focus on:

* stability and reliability
* well-tested and thoroughly documented code
* clean, correct design
* 100%% compliance with the AMQP 0.9.1 protocol specification

This package contains tests for %oname.

%prep
%setup
%patch -p1

%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/

%build
%python3_build_debug

%install
%python3_install

%make SPHINXBUILD="sphinx-build-3" -C docs html
mv docs/build/html docs_html

%check
cat > tox.ini <<EOF
[testenv]
deps =
    pytest
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v -- amqpy/ -m 'not rabbitmq' -vra

%files
%doc AUTHORS *.rst docs_html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 0.12.4-alt2.git20160226
- Transfer building docs on sphinx3.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 0.12.4-alt1.git20160226.1.1.1
- Added missing dep on Pytest.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.12.4-alt1.git20160226.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12.4-alt1.git20160226.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 26 2016 Denis Medvedev <nbr@altlinux.org> 0.12.4-alt1.git20160226
- New version.

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.git20150215
- Version 0.9.4

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20150113
- Initial build for Sisyphus

