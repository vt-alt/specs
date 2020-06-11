%define oname urllib3
%def_disable check

Name: python-module-%oname
Version: 1.25.6
Release: alt1

Epoch: 2

Summary: Library with thread-safe connection pooling, file post support, sanity friendly etc
License: MIT
Group: Development/Python

Url: https://github.com/shazow/urllib3/

# make all imports of things in packages try system copies first
Patch: %name-%version.patch

# https://github.com/shazow/urllib3.git
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-macros-sphinx

BuildRequires: python-module-six python-module-backports.ssl_match_hostname
BuildRequires: python-module-ndg-httpsclient
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-mock
BuildRequires: python-module-nose
BuildRequires: python-module-socks

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-six
BuildRequires: python3-module-mock
BuildRequires: python3-module-nose

%setup_python_module %oname

Requires: python-module-ndg-httpsclient
Requires: python-module-six python-module-backports.ssl_match_hostname ca-certificates
%py_requires ndg.httpsclient

%description
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

%package -n python3-module-%oname
Summary: Library with thread-safe connection pooling, file post support, sanity friendly etc
Group: Development/Python3
Requires: python3-module-ndg-httpsclient
Requires: python3-module-six ca-certificates

%description -n python3-module-%oname
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

%package -n python3-module-%oname-tests
Summary: Tests for urllib3
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains tests for urllib3.

%package tests
Summary: Tests for urllib3
Group: Development/Python
Requires: %name = %EVR

%description tests
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains tests for urllib3.

%package pickles
Summary: Pickles for urllib3
Group: Development/Python

%description pickles
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains pickles for urllib3.

%package docs
Summary: Documentation for urllib3
Group: Development/Documentation

%description docs
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains documentation for urllib3.

%prep
%setup -n %oname-%version
#rm -rf urllib3/packages/
%patch -p1

cp -fR . ../python3


%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
%make html
%make pickle
popd

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test

pushd ../python3
py.test-3
popd


%files
%doc *.txt *.rst
%python_sitelibdir/*
#exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/pickle

#files tests
#python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/test*

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/test*

%changelog
* Sat Oct 05 2019 Anton Farygin <rider@altlinux.ru> 2:1.25.6-alt1
- 1.24.3 -> 1.25.6

* Mon May 06 2019 Stanislav Levin <slev@altlinux.org> 2:1.24.3-alt1
- 1.24.2 -> 1.24.3 (fixes: CVE-2019-9740).

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 2:1.24.2-alt1
- 1.24.1 -> 1.24.2 (fixes: CVE-2019-11324).

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 2:1.24.1-alt2
- fixed import system six

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 2:1.24.1-alt1
- 1.24.1

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 2:1.21.1-alt1
- 1.21.1
- Add optional test check

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2:1.15.1-alt1
- 1.15.1

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:20150503-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:20150503-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:20150503-alt1.1
- NMU: Use buildreq for BR.

* Fri Sep 18 2015 Lenar Shakirov <snejok@altlinux.ru> 1:20150503-alt1
- Build old snapshot - 20150503 (1.10.4)
  * Problem between python-requests and urllib3
  * Epoch: 1

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150729-alt1
- New snapshot

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150222-alt1
- New snapshot

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150210-alt1
- New snapshot

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20141214-alt1
- New snapshot

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140810-alt2
- New snapshot

* Tue Jul 22 2014 Lenar Shakirov <snejok@altlinux.ru> 20140708-alt2
- Unbundle ssl_match_hostname, ordereddict and six package
- Use system python-module-{six,backports.ssl_match_hostname,ordereddict}

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140708-alt1
- New snapshot
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20131126-alt1
- New snapshot

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130915-alt1
- New snapshot

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130204-alt1
- Initial build for Sisyphus

