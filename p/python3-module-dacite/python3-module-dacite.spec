%define  modulename dacite

Name:    python3-module-%modulename
Version: 1.4.0
Release: alt1

Summary: Simple creation of data classes from dictionaries
License: MIT
Group:   Development/Python3
URL:     https://github.com/konradhalas/dacite

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This module simplifies creation of data classes (PEP 557) from dictionaries.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Apr 12 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Wed Mar 18 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus.
