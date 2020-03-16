Name: ansible-lint
Version: 4.1.0
Release: alt1

Summary: Best practices checker for Ansible

Group: System/Libraries
License: MIT
Url: https://github.com/willthames/ansible-lint

Source: %name-%version.tar
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm_git_archive

%description
ansible-lint checks playbooks for practices and behaviour that could potentially be improved

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc CONTRIBUTING.md README.rst examples
%_bindir/*
%python3_sitelibdir/ansiblelint
%python3_sitelibdir/*.egg-info/

%changelog
* Thu Sep 12 2019 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Build new version with python3.

* Mon May 25 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux Sisyphus
