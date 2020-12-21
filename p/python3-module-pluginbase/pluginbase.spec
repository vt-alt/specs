%define oname pluginbase

Name: python3-module-%oname
Summary: A simple but flexible plugin system for Python. 
Version: 0.7
Release: alt1

Group: Development/Python3
License: MIT
Url: https://github.com/mitsuhiko/pluginbase
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
PluginBase is a module for Python that enables the development of flexible
plugin systems in Python.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.md LICENSE
%python3_sitelibdir/%{oname}*
%python3_sitelibdir/__pycache__/*


%changelog
* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt1
- Initial build

