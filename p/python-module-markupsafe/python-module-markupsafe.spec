%define oname markupsafe

%def_with python3

Name: python-module-%oname
Version: 1.1.1
Release: alt1
Summary: implements a XML/HTML/XHTML Markup safe string for Python

Group: Development/Python
License: BSD-3-Clause
Url: http://pypi.python.org/pypi/MarkupSafe

Source: %oname-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are
replaced so that they display as the actual characters. This mitigates
injection attacks, meaning untrusted user input can safely be displayed
on a page.

%if_with python3
%package -n python3-module-%oname
Summary: implements a XML/HTML/XHTML Markup safe string for Python 3
Group: Development/Python3

%description -n python3-module-%oname
MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are
replaced so that they display as the actual characters. This mitigates
injection attacks, meaning untrusted user input can safely be displayed
on a page.
%endif

%package tests
Summary: Tests for MarkupSafe
Group: Development/Python
Requires: %name = %version-%release

%description tests
%summary

This package contains tests for MarkupSafe.

%prep
%setup -q -n %oname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
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

%files
%doc README.rst
%python_sitelibdir/markupsafe
%python_sitelibdir/MarkupSafe-%version-py?.?.egg-info

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Mar 24 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.
- Fix License tag according upstream and SPDX.
- Build from upstream tag.
- Do not package tests.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.23-alt1.2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.23-alt1.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Feb 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.23-alt1.2
- rebuild with rpm-build-python3-0.1.9
  (to conform to the new Python3 deps and location "policy")

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.23-alt1.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23-alt1
- Version 0.23

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.15-alt1.1
- Rebuild with Python-3.3

* Mon May 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt1
- Version 0.15
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt1.1
- Rebuild with Python-2.7

* Tue Mar 01 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- New version 0.12

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- New version 0.11

* Tue Aug 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.3-alt1
- New version 0.9.3

* Tue Jul 27 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.2-alt1
- initial build

