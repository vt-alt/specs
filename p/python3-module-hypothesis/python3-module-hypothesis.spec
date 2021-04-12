%define _unpackaged_files_terminate_build 1

%define oname hypothesis

%def_disable check

Name: python3-module-%oname
Version: 5.7.0
Release: alt2

Summary: A library for property based testing

License: MPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/hypothesis

BuildArch: noarch

# Source-url: %__pypi_url hypothesis
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-numpy python3-module-flaky python3-module-pytz python3-module-django
BuildRequires: python3-module-fake-factory python3-modules-sqlite3
BuildRequires: python3(mock) python3(coverage) python3(pandas) python3(dateutil)

%py3_requires coverage

%description
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
rm -rf tests/py2 tests/django/toystore
PYTHONPATH=%buildroot%python3_sitelibdir py.test3

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/*

%changelog
* Fri Apr 09 2021 Alexey Shabalin <shaba@altlinux.org> 5.7.0-alt2
- backport to p9

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 5.7.0-alt1
- new version 5.7.0 (with rpmrb script)
- separated build python3 module

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.66.30-alt1
- Updated to upstream version 3.66.30.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.18.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.18.1-alt1
- Updated to upstream version 3.18.1.

* Thu Jan 19 2017 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt1
- Initial build for ALT Linux Sisyphus.
