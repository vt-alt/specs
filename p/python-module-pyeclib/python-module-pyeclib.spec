%define oname pyeclib

Name:           python-module-%oname
Version:        1.6.0
Release:        alt1
Summary:        Python interface to erasure codes
Group:          Development/Python

License:        BSD
URL:            https://pypi.org/project/pyeclib
Source0:        %oname-%version.tar

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  liberasurecode-devel >= 1.0.7

%if ""=="3"
BuildRequires:  chrpath
%endif

Requires:       liberasurecode >= 1.0.7

%description
This library provides a simple Python interface for implementing erasure
codes. A number of back-end implementations is supported either directly
or through the C interface liberasurecode.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%if ""=="3"
chrpath -d "%buildroot%python_sitelibdir/pyeclib_c.cpython-37m.so"
%endif

%files
%doc README.rst
%python_sitelibdir/*

%changelog
* Fri May 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Build new version.

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 1.0.8-alt1
- First build for ALT
