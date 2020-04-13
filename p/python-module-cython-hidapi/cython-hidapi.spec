%define version 0.9.0
%define release alt0.1
%def_with python3

%setup_python_module cython-hidapi

Name: %{packagename}
Version: %version
Release: %release
Summary: Python wrapper for the hidapi

Group: Development/Python
License: MIT
Url: https://github.com/trezor/cython-hidapi
Source0: %modulename-%{version}.tar
Patch: %modulename-%version-%release.patch

BuildRequires: python-module-Cython libhidapi-devel libusb-devel libudev-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:	python3-devel
BuildRequires:	python3-module-setuptools python3-module-Cython
%endif

Packager: L.A. Kostis <lakostis@altlinux.ru>

%description
Python wrapper for the hidapi

%package -n python3-module-%modulename
Summary: Python3 wrapper for the hidapi
Group: Development/Python3

%description -n python3-module-%modulename
Python wrapper for the hidapi

%prep
%setup -q -n %modulename-%{version}
%patch -p1

%if_with python3
cp -fR . ../python3
%endif

%build
export CFLAGS="%optflags"
%__python setup.py --with-system-hidapi build

%if_with python3
pushd ../python3
export CFLAGS="%optflags"
python3 setup.py --with-system-hidapi build
popd
%endif

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc README.rst LICENSE.*

%if_with python3
%files -n python3-module-%modulename
%doc README.rst LICENSE.*
%python3_sitelibdir/*
%endif

%changelog
* Fri Sep 13 2019 L.A. Kostis <lakostis@altlinux.ru> 0.9.0-alt0.1
- Initial build for ALTLinux.

