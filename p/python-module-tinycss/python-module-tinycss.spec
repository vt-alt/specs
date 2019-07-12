%define oname tinycss
%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1

Summary: Simple CSS parser for Python
License: BSD
Group: Development/Python
Url: https://github.com/Kozea/tinycss

Source: %oname-%version.tar

BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%if_with python3
BuildRequires(pre): rpm-build-python3
%endif

%setup_python_module %oname

%description
tinycss is a complete yet simple CSS parser for Python. It supports the full
syntax and error handling for CSS 2.1 as well as some CSS 3 modules.

%if_with python3
%package -n python3-module-%oname
Summary: Simple CSS parser for Python
Group: Development/Python3

%description -n python3-module-%oname
tinycss is a complete yet simple CSS parser for Python. It supports the full
syntax and error handling for CSS 2.1 as well as some CSS 3 modules.
%endif


%prep
%setup -n %oname-%version

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
%doc README.rst
%python_sitelibdir/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 0.4.0-alt1
- initial build for Sisyphus
