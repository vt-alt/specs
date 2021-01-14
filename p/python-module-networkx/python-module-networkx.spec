%define oname networkx

%def_disable docs

Name:           python-module-%oname
Version:        2.2
Release:        alt3
Epoch:          2
Summary:        Creates and Manipulates Graphs and Networks
Group:          Development/Python
License:        LGPLv2+
URL:            http://networkx.github.io
# https://github.com/networkx/networkx.git
Source:         %oname-%version.tar

BuildArch:      noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-decorator >= 4.3.0
BuildRequires: python-module-numpy >= 1.15.0
BuildRequires: python-module-scipy >= 1.1.0
#BuildRequires: python-module-pandas >= 0.23.3
BuildRequires: python-module-matplotlib >= 2.2.2
BuildRequires: python-module-pygraphviz >= 1.5
BuildRequires: python-module-pydot >= 1.2.4
BuildRequires: python-module-yaml >= 3.13
BuildRequires: python-module-lxml >= 4.2.3
BuildRequires: python-module-gdal >= 1.10.0

%if_enabled docs
BuildRequires: python-module-sphinx >= 1.7.6
BuildRequires: python-module-sphinx_rtd_theme >= 0.4.1
BuildRequires: python-module-sphinx-gallery >= 0.2.0
BuildRequires: python-module-Pillow >= 5.2.0
BuildRequires: python-module-nb2plots >= 0.6
BuildRequires: python-module-texext >= 0.6
%endif

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-decorator >= 4.3.0
BuildRequires: python3-module-numpy >= 1.15.0
BuildRequires: python3-module-scipy >= 1.1.0
#BuildRequires: python3-module-pandas >= 0.23.3
BuildRequires: python3-module-matplotlib >= 2.2.2
BuildRequires: python3-module-pygraphviz >= 1.5
BuildRequires: python3-module-pydot >= 1.2.4
BuildRequires: python3-module-yaml >= 3.13
BuildRequires: python3-module-lxml >= 4.2.3
BuildRequires: python3-module-gdal >= 1.10.0

%if_enabled docs
BuildRequires: python3-module-sphinx >= 1.7.6
BuildRequires: python3-module-sphinx_rtd_theme >= 0.4.1
BuildRequires: python3-module-sphinx-gallery >= 0.2.0
BuildRequires: python3-module-Pillow >= 5.2.0
BuildRequires: python3-module-nb2plots >= 0.6
BuildRequires: python3-module-texext >= 0.6
%endif

Requires: %name-drawing = %EVR

%description
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package core
Summary: Creates and Manipulates Graphs and Networks
Group: Development/Python
Requires: python-module-decorator
Requires: python-module-yaml
Requires: python-module-numpy
Requires: python-module-scipy
%add_python_req_skip tests
%add_python_req_skip networkx.tests.test

%description core
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package drawing
Summary: Creates and Manipulates Graphs and Networks
Group: Development/Python
Requires: %name-core = %EVR
Requires: python-module-pygraphviz
Requires: python-module-pydot
Requires: python-module-matplotlib

%description drawing
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package provides support for graph visualizations.

%package -n python3-module-%oname-core
Summary: Creates and Manipulates Graphs and Networks (Python 3)
Group: Development/Python3
Requires: python3-module-decorator
Requires: python3-module-yaml
Requires: python3-module-numpy
Requires: python3-module-scipy
%add_python3_req_skip tests
%add_python3_req_skip networkx.tests.test

%description -n python3-module-%oname-core
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package -n python3-module-%oname-drawing
Summary: Creates and Manipulates Graphs and Networks (Python 3)
Group: Development/Python3
Requires: python3-module-%oname-core = %EVR
Requires: python3-module-pygraphviz
Requires: python3-module-pydot
Requires: python3-module-matplotlib

%description -n python3-module-%oname-drawing
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package provides support for graph visualizations.

%package -n python3-module-%oname
Summary: Creates and Manipulates Graphs and Networks (Python 3)
Group: Development/Python3
Requires: python3-module-%oname-drawing = %EVR

%description -n python3-module-%oname
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package -n python3-module-%oname-tests
Summary: Tests for NetworkX (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package contains tests for NetworkX.

%package docs
Summary: Documentation for NetworkX
Group: Development/Documentation

%description docs
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package contains development documentation for NetworkX.

%package pickles
Summary: Pickles for NetworkX
Group: Development/Python

%description pickles
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package contains pickles for NetworkX.

%package tests
Summary: Tests for NetworkX
Group: Development/Python
Requires: %name = %EVR

%description tests
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package contains tests for NetworkX.

%prep
%setup
chmod -x examples/*/*.py
chmod -x examples/*/*.bz2
sed -i '1,1d' networkx/tests/test.py

rm -rf ../python3
cp -a . ../python3

%if_enabled docs
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
%prepare_sphinx .
%endif

%build
%python_build

pushd ../python3
find -type f -name '*.py' -exec sed -i \
	's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
%python3_build
popd

%install
%python_install -O1
#pushd nose_plugin
#python_install -O1
#popd

pushd ../python3
%python3_install
popd

%if_enabled docs
export PYTHONPATH=$PYTHONPATH:%buildroot%python_sitelibdir
#make -C doc latex ||:
#cp doc/build/doctrees/reference/credits.doctree \
#	doc/build/doctrees/
%make -C doc html

mkdir installed-docs
mv %buildroot%_docdir/%oname-%{version}* ./installed-docs

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%files core
%python_sitelibdir/*
#exclude %python_sitelibdir/networkxdoctest.py*
%if_enabled docs
%exclude %python_sitelibdir/%oname/pickle
%endif
%exclude %python_sitelibdir/%oname/drawing
%exclude %python_sitelibdir/%oname/readwrite/nx_shp.py*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/testing
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files drawing
%python_sitelibdir/%oname/drawing
%python_sitelibdir/%oname/readwrite/nx_shp.py*
%exclude %python_sitelibdir/%oname/drawing/tests

%files tests
#python_sitelibdir/networkxdoctest.py*
%python_sitelibdir/*/tests
%python_sitelibdir/*/testing
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_enabled docs

%files docs
%doc installed-docs/*
%doc doc/build/html

%files pickles
%python_sitelibdir/%oname/pickle

%endif

%files -n python3-module-%oname

%files -n python3-module-%oname-core
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/drawing
%exclude %python3_sitelibdir/%oname/readwrite/nx_shp.py*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/testing
%exclude %python3_sitelibdir/*/*/tests
%exclude  %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-drawing
%python3_sitelibdir/%oname/drawing
%python3_sitelibdir/%oname/readwrite/nx_shp.py*
%exclude %python3_sitelibdir/%oname/drawing/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/testing
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests

%changelog
* Thu Jun 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2:2.2-alt3
- Fixed dependencies of core modules.

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2:2.2-alt2
- drop panda buildrequire

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 2:2.2-alt1
- 2.2

* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 2:1.11-alt2
- update recuires pydot -> pydotplus

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1:1.11-alt1
- 1.11

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.10-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:1.10-alt2.1
- NMU: Use buildreq for BR.

* Wed Nov 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.10-alt2
- fixed import optional modules

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.10-alt1
- 1.10

* Mon Oct 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.9.1-alt1
- downgrade to 1.9.1 release

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20150205
- New snapshot

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20140713
- Version 2.0

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1.git20131127
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1.git20130915
- Version 1.9

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt3.git20130303
- Use 'find... -exec...' instead of 'for ... $(find...'

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt2.git20130303
- New snapshot

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.8-alt1.hg20120708.1
- Rebuild with Python-3.3

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.hg20120708
- Version 1.8
- Added module for Python 3
- Disabled docs

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.hg20111126
- Version 1.7

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2.svn20100829
- Enabled docs (except pdf)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.svn20100829.2.1
- Rebuild with Python-2.7

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100829.2
- Fixed build

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100829.1
- Rebuilt with python-module-sphinx-devel

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100829
- Version 1.4

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20100505
- Version 1.2

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20100306.1
- Added docs and pickles packages

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20100306
- Version 1.1
- Exatracted tests into separate package

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20091004.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20091004
- Initial build for Sisyphus

* Tue Mar 24 2009 Conrad Meyer <konrad@tylerc.org> - 0.99-3
- Replace __python macros with direct python invocations.
- Disable checks for now.
- Replace a define with global.

* Thu Mar 12 2009 Conrad Meyer <konrad@tylerc.org> - 0.99-2
- License is really LGPLv2+.
- Include license as documentation.
- Add a check section to run tests.

* Sat Dec 13 2008 Conrad Meyer <konrad@tylerc.org> - 0.99-1
- Initial package.
