%define oname requests_toolbelt

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.9.1
Release: alt1
Summary: A toolbelt of useful classes and functions to be used with python-module-requests
License: Apache 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-toolbelt

# https://github.com/requests/toolbelt.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests
%endif

%py_provides %oname

%description
This is just a collection of utilities for python-requests,
but don't really belong in requests proper.
The minimum tested requests version is 2.1.0.
In reality, the toolbelt should work with 2.0.1 as well,
but some idiosyncracies prevent effective or sane testing on that version.

%package -n python3-module-%oname
Summary: A toolbelt of useful classes and functions to be used with python3-module-requests
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is just a collection of utilities for python-requests,
but don't really belong in requests proper.
The minimum tested requests version is 2.1.0.
In reality, the toolbelt should work with 2.0.1 as well,
but some idiosyncracies prevent effective or sane testing on that version.

%prep
%setup

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

%check
export PYTHONPATH=$PWD
python setup.py test
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
py.test3
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Sep 22 2019 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt1
- Initial build for ALT.
