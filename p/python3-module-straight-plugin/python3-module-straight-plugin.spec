%define  modulename straight-plugin

Name:    python3-module-%modulename
Version: 1.5.0
Release: alt1

Summary: A simple plugin loading facility
License: MIT
Group:   Development/Python3
URL:     https://github.com/ironfroggy/straight.plugin

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Straight Plugin provides a type of plugin you can create from almost any
existing Python modules, and an easy way for outside developers to add
functionality and customization to your projects with their own plugins.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS README.rst
%python3_sitelibdir/straight
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*.pth

%changelog
* Fri Sep 04 2020 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- New version (ALT #38870).

* Thu Jul 09 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
