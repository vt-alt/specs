%define mname dm.xmlsec
%define oname %mname.binding

%def_disable check

Name: python-module-%oname
Version: 2.0
Release: alt1

Summary: Cython/lxml based binding for the XML security library -- for lxml 3.x
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dm.xmlsec.binding/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: libxml2-devel
BuildRequires: libxmlsec1-devel
BuildRequires: libxmlsec1-openssl-devel
BuildRequires: python-module-Cython
BuildRequires: python-module-lxml

Requires: python-module-%mname = %EVR
%py_requires lxml

%py_provides %oname


%description
This package contains a Cython based bindung to Aleksey Sanin's XML
security library to be used together with lxml, the most popular Python
binding to the Gnome XML library libxml2.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains a Cython based bindung to Aleksey Sanin's XML
security library to be used together with lxml, the most popular Python
binding to the Gnome XML library libxml2.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
Requires: python-module-dm = %EVR

%description -n python-module-%mname
Core files of %mname.

%package -n python-module-dm
Summary: Core files of dm
Group: Development/Python
%py_provides dm

%description -n python-module-dm
Core files of dm.

%prep
%setup

sed -i '/transformByHref/s/^/#/' dm/xmlsec/binding/__init__.py

rm -f src/*.c

%build
%python_build_debug

%install
%python_install

install -p -m644 dm/__init__.py \
	%buildroot%python_sitelibdir/dm/
install -p -m644 dm/xmlsec/__init__.py \
	%buildroot%python_sitelibdir/dm/xmlsec/

%check
%__python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/dm/xmlsec/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/dm/xmlsec/*/tests.*
%exclude %python_sitelibdir/dm/xmlsec/__init__.py*

%files tests
%python_sitelibdir/dm/xmlsec/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/dm/xmlsec
%python_sitelibdir/dm/xmlsec/__init__.py*

%files -n python-module-dm
%dir %python_sitelibdir/dm
%python_sitelibdir/dm/__init__.py*


%changelog
* Thu Feb 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0-alt1
- Version updated to 2.0
- fixed segfault xmlsec.binding upon import.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

