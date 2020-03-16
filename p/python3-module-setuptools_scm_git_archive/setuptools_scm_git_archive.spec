%define  oname setuptools_scm_git_archive

Name:    python3-module-%oname
Version: 1.1
Release: alt1

Summary: This is a setuptools_scm plugin that adds support for git archives

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/setuptools-scm-git-archive

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

BuildArch: noarch

Source:  %oname-%version.tar

%description
%summary.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info/

%changelog
* Thu Sep 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.1-alt1
- Initial build for Sisyphus.
