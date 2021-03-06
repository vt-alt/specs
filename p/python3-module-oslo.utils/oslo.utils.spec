%define oname oslo.utils

Name: python3-module-%oname
Version: 4.1.1
Release: alt1

Summary: OpenStack Oslo Utility library

Group: Development/Python3
License: Apache-2.0
Url: http://docs.openstack.org/developer/oslo.utils

Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Provides: python3-module-oslo-utils = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-netifaces >= 0.10.4
BuildRequires: python3-module-monotonic >= 0.6
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-pyparsing >= 2.1.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-reno

%description
The OpenStack Oslo Utility library.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo Utility library
Group: Development/Documentation
Provides: python-module-oslo-utils-doc = %EVR

%description doc
Documentation for the Oslo Utility library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info
# Let RPM handle the dependencies
rm -f requirements.txt

%build
%python3_build

export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc *.rst LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.1.1-alt1
- Automatically updated to 4.1.1.
- Unify documentation building.
- Fix license.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 3.42.1-alt1
- Automatically updated to 3.42.1.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.41.2-alt1
- Automatically updated to 3.41.2.
- Build without python2.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.40.3-alt1
- Automatically updated to 3.40.3

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 3.36.4-alt1
- 3.36.4

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.22.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.1-alt1
- 3.22.1

* Tue May 02 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.0-alt1
- 3.22.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.16.0-alt1
- 3.16.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.5.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial package.
