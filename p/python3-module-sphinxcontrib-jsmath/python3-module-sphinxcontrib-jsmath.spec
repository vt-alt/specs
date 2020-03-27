%define _unpackaged_files_terminate_build 1

%define  oname sphinxcontrib-jsmath

Name:    python3-module-%oname
Version: 1.0.1
Release: alt1

Summary: A sphinx extension which renders display math in HTML via JavaScript
License: BSD
Group:   Development/Python3
URL:     https://github.com/sphinx-doc/sphinxcontrib-jsmath

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%doc README.rst CHANGES
%python3_sitelibdir/sphinxcontrib/*
%python3_sitelibdir/*.pth
%python3_sitelibdir/*.egg-info

%changelog
* Mon Sep 23 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
