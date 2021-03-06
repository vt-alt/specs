%define _unpackaged_files_terminate_build 1

%define oname z3c.batching

Name: python3-module-%oname
Version: 2.1.0
Release: alt2

Summary: This package provides simple sequence batching
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/z3c.batching/

Source0: https://pypi.python.org/packages/a7/98/26875d5a32b153e39dd480fb2a204f0cd9f7746ed57905f7ed76d9b7bf21/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
%py3_requires zope.interface zope.schema


%description
This module implements a simple batching mechanism that allows you to
split a large sequence into smaller batches.

%package tests
Summary: Tests for z3c.batching
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This module implements a simple batching mechanism that allows you to
split a large sequence into smaller batches.

This package contains tests for z3c.batching.

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
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1.0-alt2
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

