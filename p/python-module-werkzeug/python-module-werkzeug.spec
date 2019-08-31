%define oname werkzeug

%def_with python3
%def_disable check

Summary: Werkzeug is one of the most advanced WSGI utility modules
Name: python-module-%oname
Version: 0.15.5
Release: alt1
License: BSD
Group: Development/Python
BuildArch: noarch
URL: http://werkzeug.pocoo.org/

# http://github.com/mitsuhiko/werkzeug.git
Source: %name-%version.tar

BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
%endif

%description
Werkzeug started as a simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules. It includes a powerful debugger, fully featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

It does Unicode and doesn't enforce a specific template engine, database
adapter or anything else. It doesn't even enforce a specific way of
handling requests and leaves all that up to the developer.

%if_with python3
%package -n python3-module-%oname
Summary: Werkzeug is one of the most advanced WSGI utility modules
Group: Development/Python3

%description -n python3-module-%oname
Werkzeug started as a simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules. It includes a powerful debugger, fully featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

It does Unicode and doesn't enforce a specific template engine, database
adapter or anything else. It doesn't even enforce a specific way of
handling requests and leaves all that up to the developer.
%endif

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
pushd ../python3
%python3_install
popd
%endif

%check
python ./setup.py test

%if_with python3
pushd ../python3
python3 ./setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Aug 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.15.5-alt1
- Version updated to 0.15.5

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.1-alt1
- Updated to upstream version 0.14.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.10.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Version 0.10.1

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1
- Version 0.9.6
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.1
- Fixed build

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.8.3-alt1
- 0.8.3 (ALT #28297);
- minor packaging improvements.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Sergey Alembekov <rt@altlinux.ru> 0.6.2-alt1
- Initial release for ALTLinux
