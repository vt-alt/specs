%define _unpackaged_files_terminate_build 1
%define oname certifi

%def_with python3

Name: python-module-%oname
Version: 2020.12.5
Release: alt1
Summary: Python package for providing Mozilla's CA Bundle
License: MPL-2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/certifi/

Source0: https://files.pythonhosted.org/packages/06/a9/cd1fd8ee13f73a4d4f491ee219deeeae20afefa914dfb4c130cfc9dc397a/certifi-2020.12.5.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
This installable Python package contains a CA Bundle that you can
reference in your Python code. This is useful for verifying HTTP
requests, for example.

This is the same CA Bundle which ships with the Requests codebase, and
is derived from Mozilla Firefox's canonical set.

%package -n python3-module-%oname
Summary: Python package for providing Mozilla's CA Bundle
Group: Development/Python3

%description -n python3-module-%oname
This installable Python package contains a CA Bundle that you can
reference in your Python code. This is useful for verifying HTTP
requests, for example.

This is the same CA Bundle which ships with the Requests codebase, and
is derived from Mozilla Firefox's canonical set.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%doc LICENSE *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.12.5-alt1
- 2020.12.5 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.6.20-alt1
- 2020.6.20 released

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.11.28-alt1
- 2019.11.28 released

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2016.9.26-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2015.04.28-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2015.04.28-alt1
- Version 2015.04.28

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.05.14-alt1
- Initial build for Sisyphus

