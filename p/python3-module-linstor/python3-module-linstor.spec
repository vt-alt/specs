%define modulename linstor

Name: python3-module-%modulename
Summary: Linstor Python API
Version: 1.1.2
Release: alt1
Group: Development/Python3
License: GPLv3
URL: https://github.com/LINBIT/linstor-api-py
Source: http://www.linbit.com/downloads/linstor/python-%modulename-%version.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%description
This library provides functions to access the Linstor controller
e.g.: add nodes, resources and query object status

%prep
%setup -n python-%modulename-%version
make -C linstor-common cleanpython
make -C linstor-common python

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Sat Jun 29 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt1
- Initial build for ALT
