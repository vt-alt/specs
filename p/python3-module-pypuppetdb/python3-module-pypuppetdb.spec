%define  modulename pypuppetdb

Name:    python3-module-%modulename
Version: 3.3.3
Release: alt1

Summary: Python library for working with the PuppetDB API
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/voxpupuli/pypuppetdb

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This library is a thin wrapper around the REST API providing some
convenience functions and objects to request and hold data from
PuppetDB.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Jun 27 2019 Andrey Cherepanov <cas@altlinux.org> 3.3.3-alt1
- Initial build for Sisyphus
