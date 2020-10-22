%define oname jinja2

%def_without doc
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.11.2
Release: alt1

Summary: The new and improved version of a small but fast template engine
License: BSD
Group: Development/Python
BuildArch: noarch
Url: http://jinja.pocoo.org/2/

# https://github.com/mitsuhiko/jinja2.git
Source: %name-%version.tar

BuildRequires: python-module-pytest
%if_with doc
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
%endif

%add_findprov_skiplist %python_sitelibdir_noarch/jinja2/asyncfilters.py* %python_sitelibdir_noarch/jinja2/asyncsupport.py*
%add_findreq_skiplist  %python_sitelibdir_noarch/jinja2/asyncfilters.py* %python_sitelibdir_noarch/jinja2/asyncsupport.py*

Provides: python-module-%oname-tests = %EVR
Obsoletes: python-module-%oname-tests

%description
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%if_with python3
%package -n python3-module-%oname
Summary: The new and improved version of a small but fast template engine (Python 3)
Group: Development/Python3
Provides: python3-module-%oname-tests = %EVR
Obsoletes: python3-module-%oname-tests

%description -n python3-module-%oname
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.
%endif

%package doc
Summary: Documentation for Jinja2
Group: Development/Documentation

%description doc
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

This package contains HTML documentation for Jinja2.

%package pickles
Summary: Pickles for Jinja2
Group: Development/Python

%description pickles
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

This package contains pickles for Jinja2.

%prep
%setup
%if_with python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%if_with doc
%make_build -C docs html
%make_build -C docs pickle
%endif

%install
%python_install
# IronPython support
rm -f %buildroot%python_sitelibdir_noarch/jinja2/_ipysupport.py

%if_with python3
pushd ../python3
%python3_install
popd
rm -f %buildroot%python3_sitelibdir_noarch/jinja2/_ipysupport.py
%endif

%if_with doc
cp -fR docs/_build/pickle %buildroot%python_sitelibdir_noarch/jinja2/
%endif

%check
make test

%files
%doc CHANGES.rst
%python_sitelibdir_noarch/jinja2/
%python_sitelibdir_noarch/*.egg-info
%if_with doc
%exclude %python_sitelibdir_noarch/jinja2/pickle
%doc ext/
%endif

%if_with doc
%files doc
%doc docs/_build/html/*

%files pickles
%dir %python_sitelibdir_noarch/jinja2
%python_sitelibdir_noarch/jinja2/pickle
%endif

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.rst
%python3_sitelibdir_noarch/jinja2/
%python3_sitelibdir_noarch/*.egg-info
%endif

%changelog
* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.11.2-alt1
- 2.11.2 released

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.10.3-alt1
- 2.10.3 released

* Mon Sep 09 2019 Anton Farygin <rider@altlinux.ru> 2.10.1-alt1
- 2.10.1 (Fixes: CVE-2019-10906)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10-alt1
- Updated to upstream version 2.10.

* Sat Jan 14 2017 Michael Shigorin <mike@altlinux.org> 2.9-alt1.dev.git20150726.1.1.1.1
- BOOTSTRAP: introduced doc knob (avoid sphinx)

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.9-alt1.dev.git20150726.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.9-alt1.dev.git20150726.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.9-alt1.dev.git20150726.1
- NMU: Use buildreq for BR.

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1.dev.git20150726
- Version 2.9.dev

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt2.git20140610
- New snapshot

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt2.git20140110
- New snapshot

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt2.git20130807
- Added requirement on tests for python3-module-%oname

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt1.git20130807
- Version 2.8

* Wed Mar 27 2013 Aleksey Avdeev <solo@altlinux.ru> 2.7-alt1.git20120916
- New snapshot

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.git20120313
- New snapshot
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.git20111215
- Version 2.7

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.5-alt2
- Enabled docs

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.5-alt1.1
- Rebuild with Python-2.7 (bootstraping without docs)

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.5-alt1
- Version 2.5.5

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt2
- Added requirement on tests package

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Version 2.5
- Extracted tests into separate package
- Added pickles

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.2
- Enable building of documentation

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.1
- Rebuilt with python 2.6 (bootstrap)

* Thu Sep 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.2.1-alt1
- 2.2.1
- enable building of documentation
- build as noarch

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.1.1-alt1
- initial build
