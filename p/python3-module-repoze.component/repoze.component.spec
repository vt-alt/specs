%define oname repoze.component

Name: python3-module-%oname
Version: 0.4
Release: alt3

Summary: A Python component system
License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.component

# https://github.com/repoze/repoze.component.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires repoze repoze.lru


%description
``repoze.component`` is a package that software developers can use to
provide configurability and pluggability to their applications.
``repoze.component`` provides a generalized indirection mechanism
which can be used to provide plugin points to integrators or other
developers who may wish to provide alternate implementations of
application logic or configuration values.

%package tests
Summary: Tests for repoze.component
Group: Development/Python3
Requires: %name = %version-%release

%description tests
``repoze.component`` is a package that software developers can use to
provide configurability and pluggability to their applications.
``repoze.component`` provides a generalized indirection mechanism
which can be used to provide plugin points to integrators or other
developers who may wish to provide alternate implementations of
application logic or configuration values.

This package contains tests for repoze.component.

%prep
%setup
%patch0 -p1

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
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests


%changelog
* Tue Feb 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt3
- Build for python2 disabled.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.4-alt2.git20121206.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt2.git20121206.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt2.git20121206.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2.git20121206
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20121206
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.git20110222.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110222.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110222
- Initial build for Sisyphus

