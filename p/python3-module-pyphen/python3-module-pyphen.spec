%define  modulename pyphen

Name:    python3-module-%modulename
Version: 0.9.5
Release: alt1

Summary: Hyphenation in pure Python
License: GPLv2+,LGPLv2+,MPL 1.1
Group:   Development/Python3
URL:     https://github.com/Kozea/Pyphen

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

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
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc README

%changelog
* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus
