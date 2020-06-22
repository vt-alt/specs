%define oname WSGIProxy2

%def_without test
%def_with python3

Name:    python-module-%oname
Version: 0.4.6
Release: alt1
Summary: WSGI Proxy that supports several HTTP backends

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/WSGIProxy2/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gawel/WSGIProxy2.git
Source: %name-%version.tar

BuildArch:      noarch

Group: Development/Python
Summary:        WSGI Proxy that supports several HTTP backends

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-nose
BuildRequires: python-module-pytest
BuildRequires: python-module-requests python-module-restkit
%if_with test
BuildRequires: python-module-webtest
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-webob python3-module-six
BuildRequires: python3-module-restkit python3-module-http-parser
BuildRequires: python3-module-urllib3 python3-module-requests
BuildRequires: python3-module-nose
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
%if_with test
BuildRequires: python3-module-webtest
BuildRequires: python3-module-coverage
%endif
%endif

%py_provides wsgiproxy
Conflicts: python-module-wsgiproxy

%description
A WSGI Proxy with various http client backends.

%if_with test
%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A WSGI Proxy with various http client backends.

This package contains tests for %oname.
%endif

%package -n python3-module-%oname
Summary: A WSGI Proxy with various http client backends
Group: Development/Python3
%py3_provides wsgiproxy
Conflicts: python3-module-wsgiproxy

%description -n python3-module-%oname
A WSGI Proxy with various http client backends.

%if_with test
%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A WSGI Proxy with various http client backends.

This package contains tests for %oname.
%endif

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

%if_with test
%check
nosetests -vv
#if_with python3
%if 0
pushd ../python3
nosetests3 -vv
popd
%endif
%endif

%files
%doc README_fixt.py README.rst
%python_sitelibdir/*
%if_with test
%exclude %python_sitelibdir/*/test_*
%endif

%if_with test
%files -n python-module-%oname-tests
%python_sitelibdir/*/test_*
%endif

%if_with python3
%files -n python3-module-%oname
%doc README_fixt.py README.rst
%python3_sitelibdir/*
%if_with test
%exclude %python3_sitelibdir/*/test_*
%endif

%if_with test
%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test_*
%endif
%endif

%changelog
* Thu Jun 04 2020 Pavel Vasenkov <pav@altlinux.org> 0.4.6-alt1
- Version 0.4.6

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.3-alt1.dev0.git20141227.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.3-alt1.dev0.git20141227.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1.dev0.git20141227.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.dev0.git20141227
- Version 0.4.3.dev0

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.dev0.git20131221
- Initial build for Sisyphus
