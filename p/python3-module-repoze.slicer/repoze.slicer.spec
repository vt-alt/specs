%define oname repoze.slicer

Name: python3-module-%oname
Version: 1.0a2
Release: alt3

Summary: WSGI middleware to filter HTML responses
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.slicer/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires repoze wsgifilter lxml


%description
repoze.slicer is a simple piece of WSGI middleware that can extract part
of a HTML response. This can be used to reduce the amount of parsing and
manipulation of DOM trees in browsers, which is especially expensive
with older versions of IE.

%package tests
Summary: Tests for repoze.slicer
Group: Development/Python3
Requires: %name = %version-%release

%description tests
repoze.slicer is a simple piece of WSGI middleware that can extract part
of a HTML response. This can be used to reduce the amount of parsing and
manipulation of DOM trees in browsers, which is especially expensive
with older versions of IE.

This package contains tests for repoze.slicer.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0a2-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0a2-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0a2-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0a2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0a2-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a2-alt1
- Initial build for Sisyphus

