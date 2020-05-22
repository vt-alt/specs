%define oname SleekXMPP

%def_with python3

Name: python-module-%oname
Version: 1.3.3
Release: alt3

Summary: Python 2.6+/3.1+ XMPP Library

License: MIT
Group: Development/Python
Url: http://sleekxmpp.com/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-git: https://github.com/fritzy/SleekXMPP.git
Source: %name-%version.tar
Patch1: python3-async.patch

BuildArch: noarch

#BuildPreReq: python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

%description
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Python 2.6+/3.1+ XMPP Library
Group: Development/Python3

%description -n python3-module-%oname
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

This package contains tests for %oname.

%prep
%setup
%patch1 -p1
%__subst "s|\(from sleekxmpp.thirdparty.suelta.util\)|#\1 (https://github.com/fritzy/SleekXMPP/issues/480)|" sleekxmpp/plugins/xep_0138.py

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

# Set correct python2 executable in shebang and scripts
find . -type f -print0 |
        xargs -r0 grep -lZ '^#![[:space:]]*%_bindir/.*python\>' -- |
        xargs -r0 sed -E -i '1 s@^(#![[:space:]]*)%_bindir/(env[[:space:]]+)?python\>@\1%__python@' --

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Thu May 14 2020 Pavel Vasenkov <pav@altlinux.org> 1.3.3-alt3
- Set correct python2 executable in shebang and scripts

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt2.1aeefd
- merge with 1aeefd88accf45947c6376e9fac3abae9cbba8aa

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- build 1.3.3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.git20140609.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1.git20140609.1
- NMU: Use buildreq for BR.

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140609
- Initial build for Sisyphus

