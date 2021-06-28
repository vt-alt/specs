%def_without python3

%define oname BeautifulSoup4
Name: python-module-%oname
Version: 4.9.0
Release: alt2

Summary: HTML/XML parser for quick-turnaround applications like screen-scraping

License: PSF
Group: Development/Python
Url: http://www.crummy.com/software/BeautifulSoup/

BuildArch: noarch

%setup_python_module %oname

Source0: https://pypi.python.org/packages/9b/a5/c6fa2d08e6c671103f9508816588e0fb9cec40444e8e72993f3d4c325936/beautifulsoup4-%{version}.tar.gz

BuildRequires(pre): rpm-build-python
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest

#BuildPreReq: python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
#BuildRequires: python3-devel python-tools-2to3
#BuildPreReq: python3-module-setuptools-tests
%endif

%description
Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.

%package tests
Summary: Tests for BeautifulSoup4
Group: Development/Python
Requires: %name = %version-%release

%description tests
Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.

This package contains tests for BeautifulSoup4.

%if_with python3
%package -n python3-module-%oname
Summary: HTML/XML parser for quick-turnaround applications like screen-scraping (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.

%package -n python3-module-%oname-tests
Summary: Tests for BeautifulSoup4 (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.

This package contains tests for BeautifulSoup4.
%endif

%prep
%setup -q -n beautifulsoup4-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
python -m unittest discover -s bs4
%if_with python3
pushd ../python3
python3 -m unittest discover -s bs4
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/bs4/test*

%files tests
%python_sitelibdir/bs4/test*

%if_with python3
%doc *.txt
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/bs4/test*
%exclude %python3_sitelibdir/bs4/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/bs4/test*
%python3_sitelibdir/bs4/*/test*
%endif

%changelog
* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 4.9.0-alt2
- build python2 only

* Fri Sep 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.6.3-alt1
- update version to 4.6.3 from src

* Mon Jul 02 2018 Ivan Zakharyaschev <imz@altlinux.org> 4.5.3-alt2
- (.spec) use standard Python build/install macros
- (.spec) re-arrange Python/Python3 BuildRequires

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.5.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 4.4.0-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1
- Version 4.4.0

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1
- Version 4.3.2

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.1-alt1
- Version 4.3.1

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Wed Mar 06 2013 Aleksey Avdeev <solo@altlinux.ru> 4.1.3-alt1.1
- Added module for Python 3

* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Extracted tests into separate package

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.8.1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8.1-alt1
- Version 3.0.8.1

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.6-alt1.1
- Rebuilt with python 2.6

* Mon Jun 09 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.6-alt1
- new version 3.0.6 (with rpmrb script) - fix bug #14975

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt1
- change buildarch to noarch

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt0.1
- initial build for ALT Linux Sisyphus

