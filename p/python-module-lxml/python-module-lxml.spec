%def_without bootstrap

%define modulename lxml

%def_with python3

Name: python-module-lxml
Version: 4.4.2
Release: alt1

Summary: Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.

# Source-git: https://github.com/lxml/lxml.git
Source: %name-%version.tar

License: BSD-3-Clause AND GPL-2.0-or-later
Group: Development/Python
URL: http://codespeak.net/lxml

BuildPreReq: libxslt-devel zlib-devel
# see doc/build.txt
BuildPreReq: python-module-Cython >= 0.18
BuildPreReq: python-modules-wsgiref
#BuildPreReq: python-module-distribute
%if_without bootstrap
# Used for tests only, but depends on lxml itself,
# which is not yet built in a bootstrap environment.
BuildPreReq: python-module-cssselect
%endif

%setup_python_module lxml
%py_requires cssselect

BuildPreReq: python-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
# see doc/build.txt
BuildPreReq: python3-module-Cython >= 0.18
BuildPreReq: python3-devel
#BuildPreReq: python3-module-distribute
%if_without bootstrap
# Used for tests only, but depends on lxml itself,
# which is not yet built in a bootstrap environment.
BuildPreReq: python3-module-cssselect
%endif

%add_python3_req_skip etree
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 libgpg-error libxml2-devel python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-lxml python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-lxml python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface xml-common
#BuildRequires: libxslt-devel python-module-Cython python-module-html5lib python-module-notebook python3-module-Cython python3-module-html5lib python3-module-notebook rpm-build-python3 zlib-devel

%description
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

%if_with python3
%package -n python3-module-%modulename
Summary: XML processing library combining libxml2/libxslt with the ElementTree API (Python 3)
Group: Development/Python3
%py3_requires cssselect
# Prepare for the future default method (to test the result earlier):
%python3_req_hier

%description -n python3-module-%modulename
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

This is module for use with Python 3.
%endif


%package doc
Summary: Documentation for lxml
Group: Development/Documentation
BuildArch: noarch

%description doc
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

This package contains documentation for lxml.

%prep
%setup
%if_with python3
cp -a . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
# see Makefile
%python_build_debug --with-cython
%if_with python3
pushd ../python3
sed -i 's|/usr/bin/env python.*|/usr/bin/env python3|' \
	update-error-constants.py test.py
sed -i 's|/usr/bin/python|/usr/bin/python3|' \
	doc/rest2latex.py doc/rest2html.py
%python3_build --with-cython
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

# see Makefile
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ;
cp -l build/lib.linux-*/lxml/*.so src/lxml/
python test.py -p -v
PYTHONPATH=src python src/lxml/tests/selftest.py
PYTHONPATH=src python src/lxml/tests/selftest2.py
%if_with python3
pushd ../python3
cp -l build/lib.linux-*/lxml/*.so src/lxml/
python3 test.py -p -v
PYTHONPATH=src python3 src/lxml/tests/selftest.py
PYTHONPATH=src python3 src/lxml/tests/selftest2.py
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%endif

%files doc
%doc doc samples

%changelog
* Mon Dec 09 2019 Grigory Ustinov <grenka@altlinux.org> 4.4.2-alt1
- Build new version
- Fix license

* Fri Aug 23 2019 Grigory Ustinov <grenka@altlinux.org> 4.4.1-alt1
- Build new version
- Disable bootstrap knob.

* Wed Apr 03 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.3-alt1.1
- Bootstrap for python3.7.

* Wed Mar 27 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.3-alt1
- Build new version

* Mon Mar 04 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.2-alt1
- Build new version

* Mon Feb 11 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.1-alt1
- Build new version

* Sun Jan 06 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.0-alt1
- Build new version

* Tue Dec 25 2018 Grigory Ustinov <grenka@altlinux.org> 4.2.5-alt1
- Build new version

* Tue Mar 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.1-alt1
- Updated to upstream version 4.2.1.

* Sun Oct 01 2017 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- build new version

* Sun Oct 01 2017 Vitaly Lipatov <lav@altlinux.ru> 3.8.0-alt1
- build new version

* Fri Apr 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt2.beta1.git20150727
- (.spec) Described the actually necessary simplification for %%if_with bootstrap
  (namely: make it skip some tests employing cssselect which depends on lxml itself).

* Tue Apr 12 2016 Denis Medvedev <nbr@altlinux.org> 3.5.0-alt1.beta1.git20150727.3
- NMU: added documentation back.

* Wed Mar 23 2016 Denis Medvedev <nbr@altlinux.org> 3.5.0-alt1.beta1.git20150727.2
- NMU: temporarily removed documentation for python3.5 cycle removal.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.5.0-alt1.beta1.git20150727.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.beta1.git20150727
- Version 3.5.0.beta1

* Mon Apr 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.dev.git20150417
- Version 3.5.dev

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.git20141226
- New snapshot

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.git20141120
- Version 3.4.1

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.5-alt1.git20140418
- Version 3.3.5

* Sat Mar 30 2013 Aleksey Avdeev <solo@altlinux.ru> 3.1.1-alt1.git20130330
- Version 3.1.1 (d7ea8fd4bb60e8e0799b1cb4a3ef0f79da8f3530)

* Thu Mar 28 2013 Aleksey Avdeev <solo@altlinux.ru> 3.1.0-alt1
- Version 3.1.0

* Sun Mar 17 2013 Aleksey Avdeev <solo@altlinux.ru> 2.3.6-alt1
- Version 2.3.6

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt2
- Added module for Python 3

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt1
- Version 2.3.4

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.8-alt2.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.8-alt2
- Added zlib-devel into BuildPreReq
- Rebuilt for debuginfo

* Tue Nov 30 2010 Ivan Fedorov <ns@altlinux.org> 2.2.8-alt1
- Version 2.2.8

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.7-alt1
- Version 2.2.7
- Added docs

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt1
- cleanup spec
- new version 2.2.4 (with rpmrb script)

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.1.1-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-lxml
  * postclean-05-filetriggers for spec file

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.1
- Rebuilt with python 2.6

* Wed Jul 30 2008 Ivan Fedorov <ns@altlinux.org> 2.1.1-alt1
- 2.1.1

* Wed May 28 2008 Ivan Fedorov <ns@altlinux.org> 2.0.5-alt1
- 2.0.5

* Wed Apr 09 2008 Ivan Fedorov <ns@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Jan 28 2008 Grigory Batalov <bga@altlinux.ru> 1.3.6-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt1
- initial build for ALT Linux Sisyphus
