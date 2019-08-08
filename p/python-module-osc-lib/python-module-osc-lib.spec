%define oname osc-lib

Name: python-module-%oname
Version: 1.11.1
Release: alt2
Summary: OpenStackClient (aka OSC) is a command-line client for OpenStack
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

Patch1: fix-error-with-3.7-python.patch

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-cliff >= 2.8.0
BuildRequires: python-module-keystoneauth1 >= 3.7.0
BuildRequires: python-module-openstacksdk >= 0.15.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-simplejson >= 3.5.0
BuildRequires: python-module-stevedore >= 1.20.0

# doc
BuildRequires: python-module-sphinx
BuildRequires: python-module-sphinxcontrib-apidoc
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-keystoneauth1 >= 3.7.0
BuildRequires: python3-module-openstacksdk >= 0.15.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-simplejson >= 3.5.0
BuildRequires: python3-module-stevedore >= 1.20.0

# doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinxcontrib-apidoc
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0

%description
OpenStackClient (aka OSC) is a command-line client for OpenStack.
osc-lib is a package of common support modules for writing OSC plugins.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack %oname library
Group: Development/Documentation

%description doc
Documentation for OpenStack %oname library

%package -n python3-module-%oname
Summary: OpenStackClient (aka OSC) is a command-line client for OpenStack
Group: Development/Python3

%description -n python3-module-%oname
OpenStackClient (aka OSC) is a command-line client for OpenStack.
osc-lib is a package of common support modules for writing OSC plugins.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.


%prep
%setup -n %oname-%version
%patch1 -p1
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr build/sphinx/html/.buildinfo

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files doc
%doc README.rst build/sphinx/html

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Mon Aug 05 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.1-alt2
- Fix work with python 3.7

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.1-alt1
- 1.11.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial packaging
