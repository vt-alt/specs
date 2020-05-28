%define  modulename cairocffi

Name:    python3-module-%modulename
Version: 1.0.2
Release: alt1

Summary: CFFI-based cairo bindings for Python.
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/Kozea/cairocffi

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-cffi
BuildRequires: python3-module-pytest-runner

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
