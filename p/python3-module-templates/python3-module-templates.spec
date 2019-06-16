%define  oname templates

Name:    python3-module-%oname
Version: 0.0.5
Release: alt1

Summary: Python templating library with templates included.

License: ASL 2.0
Group:   Development/Python3
URL:     https://github.com/grantjenks/python-templates

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

Requires: python3-module-bottle

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Tue May 21 2019 Grigory Ustinov <grenka@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus (Closes: #36765).
