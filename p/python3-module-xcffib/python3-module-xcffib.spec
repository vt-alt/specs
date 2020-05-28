%define  modulename xcffib

Name:    python3-module-%modulename
Version: 0.8.1
Release: alt1

Summary: A drop-in replacement for xpyb based on cffi
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/tych0/xcffib

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-six python3-module-cffi

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
%doc *.md

%changelog
* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus
