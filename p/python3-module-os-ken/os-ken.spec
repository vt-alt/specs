%define  oname os-ken

Name:    python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: A component-based software defined networking framework for OpenStack

License: ASLv2
Group:   Development/Python3
URL:     https://pypi.org/project/os-ken/

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0

BuildArch: noarch

Source:  %oname-%version.tar

%description
%summary

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/osken
%_bindir/osken-manager
%python3_sitelibdir/os_ken
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Automatically updated to 1.0.0.

* Thu Sep 26 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus.
