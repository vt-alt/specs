%def_enable check
Name: python-module-xmlsec
Version: 1.3.6
Release: alt1
Source: %version.tar.gz
Summary: Python bindings for the XML Security Library
License: MIT
Group: Development/Python
Url: https://github.com/mehcode/python-xmlsec
Obsoletes: python-module-mehcode-xmlsec

BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python3-devel python3-module-setuptools

%if_with check
BuildRequires: python-module-pytest python-module-setuptools-tests
BuildRequires: python3-module-pytest python3-module-setuptools-tests
%endif

# Automatically added by buildreq on Wed Jul 27 2016
# optimized out: libltdl7-devel libssl-devel libxml2-devel libxmlsec1-devel libxmlsec1-openssl libxslt-devel pkg-config python-base python-devel python-module-Cython python-module-cssselect python-module-lxml python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-xml python3 python3-base python3-module-Cython python3-module-cssselect python3-module-lxml python3-module-setuptools
BuildRequires: libxmlsec1-openssl-devel

BuildRequires: python-module-Cython python-module-lxml python-module-pkgconfig
BuildRequires: python3-module-Cython python3-module-lxml python3-module-pkgconfig
BuildRequires: python-module-sphinx
BuildRequires: python3-module-sphinx

%description
Python bindings for the XML Security Library.

%package -n python3-module-xmlsec
Group: Development/Python
Summary: Python3 bindings for the XML Security Library
Obsoletes: python3-module-mehcode-xmlsec
%description -n python3-module-xmlsec
Python3 bindings for the XML Security Library

%prep
%setup -n python-xmlsec-%version

%build
%python_build_debug -b build2
PYTHONPATH=`realpath build2/lib.linux*` make -C doc html BUILDDIR=build2

%python3_build_debug -b build3
PYTHONPATH=`realpath build3/lib.linux*` make -C doc html SPHINXBUILD=py3_sphinx-build BUILDDIR=build3

%install
rm -f build && ln -s build2 build && %python_install
rm -f build && ln -s build3 build && %python3_install

%if_with check
%check
python setup.py test build_ext -i
py.test -vv
python3 setup.py test build_ext -i
py.test-%_python3_version -vv
%endif

%files
%doc README* doc/build2/html
%python_sitelibdir/*

%files -n python3-module-xmlsec
%doc README* doc/build2/html
%python3_sitelibdir/*

%changelog
* Sun Jan 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt1
- Build new version.

* Tue May 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt2
- NMU: Add URL (Closes: #34693).

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 1.3.3-alt1
- Autobuild version bump to 1.3.3
- Introduce documentation

* Wed Jul 27 2016 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Fresh build from Pypi
- Thanks real@ for old python-module-mehcode-xmlsec

