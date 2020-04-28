%def_with python3

Name: python-module-pykcs11
Version: 1.4.3
Release: alt2
Summary: A complete PKCS#11 wrapper for Python
Group: Development/Python
License: GPLv2
URL: https://github.com/LudovicRousseau/PyKCS11

Source: %name-%version.tar

BuildRequires: rpm-build-python python-module-setuptools
BuildRequires: gcc-c++

%if_with python3
BuildRequires: rpm-build-python3 python3-module-setuptools python3-devel
%endif

%description
A complete PKCS#11 wrapper for Python. You can use any PKCS#11 (aka CryptoKi)
module such as the PSM which comes as part of mozilla or the various modules
supplied by vendors of hardware crypto tokens, and almost all PKCS#11 functions
and data types. The wrapper has been generated with the help of the SWIG
compiler.

%package docs
Summary: A complete PKCS#11 wrapper for Python
Group: Development/Documentation

%description docs
A complete PKCS#11 wrapper for Python. You can use any PKCS#11 (aka CryptoKi)
module such as the PSM which comes as part of mozilla or the various modules
supplied by vendors of hardware crypto tokens, and almost all PKCS#11 functions
and data types. The wrapper has been generated with the help of the SWIG
compiler.

This package contains documentation.

%package -n python3-module-pykcs11
Summary: A complete PKCS#11 wrapper for Python
Group: Development/Python3

%description -n python3-module-pykcs11
A complete PKCS#11 wrapper for Python. You can use any PKCS#11 (aka CryptoKi)
module such as the PSM which comes as part of mozilla or the various modules
supplied by vendors of hardware crypto tokens, and almost all PKCS#11 functions
and data types. The wrapper has been generated with the help of the SWIG
compiler.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
cd ../python3
%python3_install
%endif

%files
%python_sitelibdir/*

%files docs
%doc README.md samples/

%if_with python3
%files -n python3-module-pykcs11
%python3_sitelibdir/*
%endif

%changelog
* Wed Apr 22 2020 Lenar Shakirov <snejok@altlinux.org> 1.4.3-alt2
- Fix python3 build

* Fri Jul 14 2017 Lenar Shakirov <snejok@altlinux.ru> 1.4.3-alt1
- Initial build for ALT
