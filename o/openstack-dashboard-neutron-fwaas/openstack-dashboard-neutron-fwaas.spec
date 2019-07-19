
%define oname neutron-fwaas-dashboard

Name: openstack-dashboard-neutron-fwaas
Version: 1.5.0
Release: alt1
Summary: Horizon UI support for Neutron FWaaS
Group: System/Servers

License: ASL 2.0
Url: http://docs.openstack.org/developer/neutron-fwaas-dashboard/
Source:  %oname-%version.tar.gz

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-paste
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: openstack-dashboard >= 13.0.0
BuildRequires: python-module-neutronclient >= 6.7.0

# doc
BuildRequires: python-module-sphinx >= 1.6.2
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-oslotest >= 3.2.0
BuildRequires: python-module-reno >= 2.5.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-paste
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: openstack-dashboard >= 13.0.0
BuildRequires: python3-module-neutronclient >= 6.7.0


Requires: openstack-dashboard >= 13.0.0
Requires: python-module-neutronclient >= 6.7.0
Requires: python3-module-%oname = %EVR

Provides: neutron-fwaas-dashboard

%description
Horizon panels for Neutron FWaaS

%package doc
Summary: Documentation for Neutron LBaaS dashboard
Group: Development/Documentation

%description doc
Documentation for Neutron FWaaS dashboard

%package -n python-module-%oname
Summary: Horizon UI support for Neutron FWaaS
Group: Development/Python

%description -n python-module-%oname
Horizon UI support for Neutron FWaaS

%package -n python-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python
Requires: python-module-%oname = %EVR

%description -n python-module-%oname-tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Horizon UI support for Neutron FWaaS
Group: Development/Python3
%add_python3_req_skip openstack_dashboard.contrib.developer.profiler
%add_python3_req_skip openstack_dashboard.dashboards.project.networks.ports

%description -n python3-module-%oname
Horizon UI support for Neutron FWaaS

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip openstack_dashboard.api
%add_python3_req_skip openstack_dashboard.enabled
%add_python3_req_skip openstack_dashboard.test
%add_python3_req_skip openstack_dashboard.test.settings
%add_python3_req_skip openstack_dashboard.test.test_data

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
pushd ../python3
%python3_install
popd

mkdir -p %buildroot%_datadir/openstack-dashboard/openstack_dashboard/local/enabled/
install -p -D -m 640 neutron_fwaas_dashboard/enabled/_701[01]_project* %buildroot%_datadir/openstack-dashboard/openstack_dashboard/local/enabled/


%files
%doc README.rst LICENSE
%_datadir/openstack-dashboard/openstack_dashboard/local/enabled/_701[01]*

%files -n python-module-%oname
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files -n python-module-%oname-tests
%python_sitelibdir/*/test*

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*

%changelog
* Fri Jul 19 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt1
- initial build
