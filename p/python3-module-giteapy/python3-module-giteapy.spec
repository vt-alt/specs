%define _unpackaged_files_terminate_build 1
%define mname giteapy

Name: python3-module-%mname
Version: 1.0.8
Release: alt1
Summary: Python SDK for Gitea
License: Unlicense
Group: Development/Python3
Url: https://github.com/dblueai/giteapy
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

%description
Python SDK for Gitea - A painless, self-hosted Git service.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/test
%doc README.md

%changelog
* Sun Aug 30 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.0.8-alt1
- Initial build for ALT
