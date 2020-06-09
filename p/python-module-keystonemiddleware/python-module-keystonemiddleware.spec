%define oname keystonemiddleware

%def_with docs

Name: python-module-%oname
Version: 6.0.0
Release: alt0.1.p9
Summary: Middleware for OpenStack Identity
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-oslo.cache >= 1.26.0
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.context >= 2.19.2
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-pycadf >= 1.1.0
BuildRequires: python-module-keystoneclient >= 3.8.0
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-webob >= 1.7.1

BuildRequires: python-module-doc8 >= 0.6.0
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-sphinx >= 1.6.2
BuildRequires: python-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python-module-oslo.messaging >= 5.29.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-oslo.cache >= 1.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-pycadf >= 1.1.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-webob >= 1.7.1

BuildRequires: python3-module-doc8 >= 0.6.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python3-module-oslo.messaging >= 5.29.0

%description
This package contains middleware modules designed to provide authentication
and authorization features to web services other than OpenStack Keystone.
The most prominent module is keystonemiddleware.auth_token.
This package does not expose any CLI or Python API features.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack Oslo Utility library
Group: Development/Python3

%description -n python3-module-%oname
The OpenStack Oslo Utility library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for the Middleware for OpenStack Identity
Group: Development/Documentation

%description doc
Documentation for the Middleware for OpenStack Identity
%endif

%prep
%setup -n %oname-%version
rm -f requirements.txt
# Remove bundled egg-info
rm -rf %oname.egg-info

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%if_with docs
# generate html docs
#python3 setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf build/sphinx/html/.{doctrees,buildinfo}
%endif

%install
%python_install

pushd ../python3
%python3_install
popd


%files
%doc README.rst LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%if_with docs
%files doc
%doc LICENSE
#build/sphinx/html
%endif

%changelog
* Mon Jun 01 2020 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt0.1.p9
- FTBFS: backport new version to p9 branch.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 6.0.0-alt1
- Automatically updated to 6.0.0

* Tue Dec 18 2018 Alexey Shabalin <shaba@altlinux.org> 5.2.0-alt1
- 5.2.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.14.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 4.14.0-alt1
- 4.14.0
- add test packages

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.9.1-alt1
- 4.9.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 4.9.0-alt1
- 4.9.0

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial package.
