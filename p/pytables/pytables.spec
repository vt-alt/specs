%define descr PyTables is a package for managing hierarchical datasets and designed \
to efficiently and easily cope with extremely large amounts of data. \
\
PyTables is built on top of the HDF5 library, using the Python language \
and the NumPy package (it also supports numarray and Numeric right \
out-of-the-box). It features an object-oriented interface that, combined \
with C extensions for the performance-critical parts of the code \
(generated using Pyrex), makes it a fast, yet extremely easy to use tool \
for interactively dealing with, processing and searching very large \
amounts of data. One important feature of PyTables is that it optimizes \
memory and disk resources so that data takes much less space (specially \
if on-flight compression is used) than other solutions such as \
relational or object oriented databases.

%define hdf5dir %_libdir/hdf5-seq
%define oname tables

%def_with python3
%def_enable check

Name: py%oname
Version: 3.5.2
Release: alt1
Epoch: 1
Summary: Managing hierarchical datasets
License: MIT
Group: Development/Python
Url: http://www.pytables.org/

# https://github.com/PyTables/PyTables.git
Source: %name-%version.tar.gz

%add_findreq_skiplist %python_sitelibdir/%oname/contrib/nctoh5.py
%add_findreq_skiplist %python3_sitelibdir/%oname/contrib/nctoh5.py

Requires: python-module-%oname = %EVR

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-numpydoc python-module-numpy-addons
BuildPreReq: python-module-lxml python-module-numpy
BuildPreReq: python-module-docutils python-module-matplotlib
BuildPreReq: python-module-sphinx
BuildPreReq: python-module-numexpr-tests
BuildPreReq: python-devel python-module-Pyrex libnumpy-devel
BuildPreReq: libhdf5-devel liblzo2-devel bzlib-devel
BuildPreReq: xsltproc inkscape fop
BuildPreReq: java-devel-default docbook-tldp-xsl docbook-dtds
BuildPreReq: python-module-Cython
BuildPreReq: python-module-numexpr python-module-setuptools
#BuildPreReq: texlive-latex-recommended libblosc-devel
BuildPreReq: libblosc-devel
BuildRequires: python-module-sphinx_rtd_theme ipython python-module-pathlib2
BuildRequires: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel python-tools-2to3
BuildPreReq: python3-module-distribute python3-module-Cython
BuildPreReq: python3-module-numexpr-tests
BuildRequires: python3-module-mock
%endif

%description
%descr

%if_with python3
%package py3
Summary: Managing hierarchical datasets (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description py3
%descr

%package -n python3-module-%oname
Summary: Managing hierarchical datasets (Python 3)
Group: Development/Python3
%add_python3_req_skip numarray Scientific

%description -n python3-module-%oname
%descr

This package contains python module of PyTables.

%package -n python3-module-%oname-tests
Summary: Tests and examples for PyTables (Python 3)
Group: Development/Python3
%add_python3_req_skip numarray
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
%descr

This package contains tests and examples for PyTables.

%package -n python3-module-%oname-bench
Summary: Benchmarks for PyTables (Python 3)
Group: Development/Python3
%add_python3_req_skip numarray chararray recarray recarray2 Numeric psyco
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-bench
%descr

This package contains benchmarks for PyTables.
%endif

%package doc
Summary: Documentation for PyTables
Group: Development/Documentation
BuildArch: noarch

%description doc
%descr

This package contains documentation for PyTables.

%package -n python-module-%oname
Summary: Managing hierarchical datasets
Group: Development/Python
%setup_python_module %oname
%add_python_req_skip numarray

%description -n python-module-%oname
%descr

This package contains python module of PyTables.

%package -n python-module-%oname-tests
Summary: Tests and examples for PyTables
Group: Development/Python
%add_python_req_skip numarray queue
Requires: python-module-%oname = %EVR

%description -n python-module-%oname-tests
%descr

This package contains tests and examples for PyTables.

%package -n python-module-%oname-bench
Summary: Benchmarks for PyTables
Group: Development/Python
%add_python_req_skip numarray chararray recarray recarray2 Numeric psyco
Requires: python-module-%oname = %EVR

%description -n python-module-%oname-bench
%descr

This package contains benchmarks for PyTables.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
find ../python3 -type f -name '*.py' -exec \
    sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
find ../python3 -type f -name '*.py' -exec \
    sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' '{}' +
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%add_optflags -fno-strict-aliasing
export NPY_NUM_BUILD_JOBS=%__nprocs
%python_build_debug --hdf5=%hdf5dir
%if_with python3
pushd ../python3
%python3_build_debug --hdf5=%hdf5dir
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install --hdf5=%hdf5dir --root=%buildroot

cp -fR examples %buildroot%python3_sitelibdir/%oname/
cp -fR bench contrib %buildroot%python3_sitelibdir/%oname/
popd
pushd %buildroot%_bindir
for i in $(ls); do
    mv $i $i.py3
done
popd
%endif

%python_install --hdf5=%hdf5dir --root=%buildroot

export PYTHONPATH=%buildroot%python_sitelibdir
%make_build -C doc pickle
%make_build -C doc html

install -d %buildroot%_docdir/%name/pdf
install -p -m644 LICENSE.txt README.rst RELEASE_NOTES.txt THANKS \
    %buildroot%_docdir/%name
cp -fR LICENSES %buildroot%_docdir/%name
#install -p -m644 doc/build/latex/*.pdf %buildroot%_docdir/%name/pdf
cp -fR doc/build/html %buildroot%_docdir/%name/

cp -fR examples %buildroot%python_sitelibdir/%oname/

cp -fR bench contrib %buildroot%python_sitelibdir/%oname/

%check
%make check
%if_with python3
pushd ../python3
%make check PYTHON=python3
popd
%endif

%files
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif

%files -n python-module-%oname
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/examples
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/*/tests
%exclude %python_sitelibdir/%oname/bench

%files -n python-module-%oname-tests
%python_sitelibdir/%oname/examples
%python_sitelibdir/%oname/tests
%python_sitelibdir/%oname/*/tests

%files -n python-module-%oname-bench
%python_sitelibdir/%oname/bench

%if_with python3
%files py3
%_bindir/*.py3

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/examples
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests
%exclude %python3_sitelibdir/%oname/bench

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/examples
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/*/tests

#files -n python3-module-%oname-bench
#python3_sitelibdir/%oname/bench
%endif

%files doc
%_docdir/%name

%changelog
* Fri Jul 19 2019 Grigory Ustinov <grenka@altlinux.org> 1:3.5.2-alt1
- Build new version.

* Tue Apr 09 2019 Grigory Ustinov <grenka@altlinux.org> 1:3.5.1-alt1
- Build new version for python3.7.

* Fri Mar 22 2019 Anton Farygin <rider@altlinux.ru> 1:3.4.2-alt2
- removed w3c-markup-validator-libs build dependency

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Aug 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.2-alt1
- Updated to upstream release version 3.4.2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:3.2.2-alt1.dev0.git20150828.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2.2-alt1.dev0.git20150828
- New snapshot

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2.2-alt1.dev0.git20150817
- Version 3.2.2.dev0

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.1.2-alt1.dev.git20150418
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.1.2-alt1.dev.git20141012
- Version 3.1.2dev

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.1.1-alt3.git20140325
- Added module for Python 3

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.1.1-alt2.git20140325
- NMU: corrected java deps

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.1.1-alt1.git20140325
- Version 3.1.1

* Thu Oct 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.0-alt3.git20130601
- Rebuilt with updated NumPy

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.0-alt2.git20130601
- Rebuilt with new libhdf5

* Sun Jun 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.0-alt1.git20130601
- Version 3.0.0

* Tue Oct 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.4.0-alt2.git20120720
- Rebuilt with updated NumPy

* Thu Sep 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.4.0-alt1.git20120720
- Version 2.4.0

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3.1-alt1.git20120613
- New snapshot
- Applied repocop patch

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3.1-alt1.git20120318
- New snapshot

* Sat Dec 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3.1-alt1.git20111114
- Version 2.3.1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3b1-alt1.svn20110408.1.1
- Rebuild with Python-2.7

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20110408.1
- Rebuilt with libhdf5-7

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20110408
- New snapshot

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20101118.1
- Rebuilt for debuginfo

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20101118
- New snapshot

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20100707.3
- Rebuilt for soname set-versions

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20100707.2
- Fixed underlinking

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20100707.1
- Avoid requirement on RandomArray

* Mon Jul 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20100707
- Version 2.3b1
- Rebuilt with docbook-style-xsl 1.75.2

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b3-alt1.svn20100203
- Version 2.2b3

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b2-alt1.svn20090911.4
- Fixed creating some extensions
- Added docs, benchmarks and tests/examples

* Wed Feb 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b2-alt1.svn20090911.3
- Rebuilt with reformed NumPy

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b2-alt1.svn20090911.2
- Rebuilt without python-module-Numeric

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b2-alt1.svn20090911.1
- Rebuilt with python 2.6

* Fri Sep 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b2-alt1.svn20090911
- Initial build for Sisyphus

