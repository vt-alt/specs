%define oname pam
%def_with python3

Summary:	PAM bindings for Python
Name:		python-module-PAM
Version:	1.8.4
Release:	alt1
License:	%mit
Group:		Development/Python

Source0:	%{name}-%{version}.tar
Url:		https://github.com/FirefighterBlu3/python-pam

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-distribute python-module-pip

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute python3-module-pip
%endif

%setup_python_module %oname

%description
PAM (Pluggable Authentication Module) bindings for Python.

%if_with python3
%package -n python3-module-PAM
Summary: PAM bindings for Python (Python 3)
Group: Development/Python3

%description -n python3-module-PAM
PAM (Pluggable Authentication Module) bindings for Python 3.
%endif


%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc LICENSE README.md
%python_sitelibdir/%{oname}*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-PAM
%python3_sitelibdir/%{oname}*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Thu Jul 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.4-alt1
- Build new version.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.3-alt2
- NMU: Rebuild with python3.7.

* Fri May 04 2018 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- New version (switch to fork from David Ford)
- Add Python 3 package
- Make package noarch

* Fri Mar 01 2013 Pavel Shilovsky <piastry@altlinux.org> 0.5.0-alt2
- Rename package to python-module-PAM

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.5.0-alt1
- Initial release for Sisyphus (based on Fedora)
