%define oname saharaclient

Name: python3-module-%oname
Version: 3.1.0
Release: alt2

Summary: Python API and CLI for OpenStack  Sahara

Group: Development/Python3
License: Apache-2.0
Url: http://docs.openstack.org/developer/python-%oname

Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-osc-lib >= 2.0.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-openstackclient >= 3.12.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

%description
This is a client for the OpenStack Sahara API. There's a Python API (the
saharaclient module), and a command-line script (sahara). Each implements
100 percent of the OpenStack Sahara API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Sahara API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Sahara API. There's a Python API (the
saharaclient module), and a command-line script (sahara). Each implements
100 percent of the OpenStack Sahara API.

This package contains documentation for %oname.

%prep
%setup -n python-%oname-%version

rm -rf *.egg-info

# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -rf {,test-}requirements.txt

%build
%python3_build

export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

# install man page
install -p -D -m 644 man/saharaclient.1 %buildroot%_man1dir/saharaclient.1

%files
%doc *.rst LICENSE
%_man1dir/saharaclient*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1
- Automatically updated to 2.3.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1
- Automatically updated to 2.2.1

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt1
- 2.0.0

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.11.1-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Mon Mar 16 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- Initial release for Sisyphus

