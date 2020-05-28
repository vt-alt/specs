%define  modulename humblewx

Name:    python3-module-%modulename
Version: 0.2.1
Release: alt1

Summary: Library that simplifies creating user interfaces with wxPython.
License: GPL-3.0
Group:   Development/Python3
URL:     https://github.com/thetimelineproj/humblewx

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

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
%doc AUTHORS README.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Fri May 22 2020 Andrey Cherepanov <cas@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus.
