%define oname flaky

%def_with python3

Name: python-module-%oname
Version: 3.6.0
Release: alt1
Summary: Plugin for nose or py.test that automatically reruns flaky tests
License: Apache-2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/flaky
BuildArch: noarch

# https://github.com/box/flaky.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools python-module-mock python-module-genty python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-mock python3-module-genty python3-module-nose
%endif

%description
Flaky is a plugin for nose or py.test that automatically reruns flaky tests.

Ideally, tests reliably pass or fail, but sometimes test fixtures must rely
on components that aren't 100%% reliable. With flaky, instead of removing
those tests or marking them to @skip, they can be automatically retried.

%package -n python3-module-%oname
Summary: Plugin for nose or py.test that automatically reruns flaky tests
Group: Development/Python3

%description -n python3-module-%oname
Flaky is a plugin for nose or py.test that automatically reruns flaky tests.

Ideally, tests reliably pass or fail, but sometimes test fixtures must rely
on components that aren't 100%% reliable. With flaky, instead of removing
those tests or marking them to @skip, they can be automatically retried.

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Jul 08 2019 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt1
- Build new version.

* Thu Jan 24 2019 Grigory Ustinov <grenka@altlinux.org> 3.5.3-alt1
- Build new version.

* Tue Jan 15 2019 Grigory Ustinov <grenka@altlinux.org> 3.5.2-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.0-alt1
- Initial build for ALT.
