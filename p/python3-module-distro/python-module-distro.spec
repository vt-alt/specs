%define  modulename distro

Name:    python3-module-%modulename
Version: 1.5.0
Release: alt2

Summary: A much more elaborate, renewed alternative implementation for Python's platform.linux_distribution()
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/nir0s/distro

BuildArch: noarch

Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
%summary.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/%modulename
%python3_sitelibdir/*
%doc *.md

%changelog
* Mon Oct 05 2020 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt2
- rename src.rpm package to python3-module-distro

* Fri Jul 03 2020 Vladimir Didenko <cow@altlinux.org> 1.5.0-alt1
- New version

* Mon Apr 08 2019 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
