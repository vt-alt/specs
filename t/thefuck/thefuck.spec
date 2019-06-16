Name:    thefuck
Version: 3.29
Release: alt1

Summary: Magnificent app which corrects your previous console command

License: MIT
Group:   Other
URL:     https://github.com/nvbn/thefuck

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup
rm -v thefuck/system/win32.py

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/%name
%python3_sitelibdir/*.egg-info

%changelog
* Tue May 28 2019 Grigory Ustinov <grenka@altlinux.org> 3.29-alt1
- Build new version.

* Mon Dec 03 2018 Grigory Ustinov <grenka@altlinux.org> 3.28-alt1
- Build new version.

* Tue May 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.27-alt1
- Build new version.

* Tue May 15 2018 Grigory Ustinov <grenka@altlinux.org> 3.26-alt1
- Build new version.

* Mon Feb 12 2018 Grigory Ustinov <grenka@altlinux.org> 3.25-alt2
- Change package group.

* Thu Feb 08 2018 Grigory Ustinov <grenka@altlinux.org> 3.25-alt1
- Initial build for Sisyphus.
