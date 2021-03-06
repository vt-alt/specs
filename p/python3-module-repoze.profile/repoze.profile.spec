%define _unpackaged_files_terminate_build 1

%define oname repoze.profile

Name: python3-module-%oname
Version: 2.2
Release: alt2

Summary: WSGI middleware: aggreggate profile data across requests
License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.profile

# https://github.com/repoze/repoze.profile.git
Source0: https://pypi.python.org/packages/e2/a1/fa5cb1fbbf7cb3439755a9484e27a79a7b7f18fe725990756d091e101b12/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
%py3_requires repoze meld3 paste pyprof2calltree


%description
This package provides a WSGI middleware component which aggregates
profiling data across *all* requests to the WSGI application.  It
provides a web GUI for viewing profiling data.

%package tests
Summary: Tests for repoze.profile
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This package provides a WSGI middleware component which aggregates
profiling data across *all* requests to the WSGI application.  It
provides a web GUI for viewing profiling data.

This package contains tests for repoze.profile.

%prep
%setup -q -n %{oname}-%{version}

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
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2-alt2
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.b1.git20130408.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.b1.git20130408.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.b1.git20130408
- Added module for Python 3

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1.git20130408
- New snapshot

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1.git20130130
- Version 2.0b1

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20110930
- Version 1.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.git20110512.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20110512.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20110512
- Initial build for Sisyphus

