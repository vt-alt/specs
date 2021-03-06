%define oname zc.i18n

Name: python3-module-%oname
Version: 0.7.0
Release: alt4

Summary: Additional I18n Support APIs
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zc.i18n/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires zope.i18n zope.i18nmessageid zope.interface


%description
This package provides additional I18n and L10n features. In particular
it provides an API to compute the time duratrions over various timezones.

%package tests
Summary: Tests for zc.i18n
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires zope.testing zope.publisher

%description tests
This package provides additional I18n and L10n features. In particular
it provides an API to compute the time duratrions over various timezones.

This package contains tests for zc.i18n.

%prep
%setup

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

%files tests
%python3_sitelibdir/*/*/tests.*


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt4
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

