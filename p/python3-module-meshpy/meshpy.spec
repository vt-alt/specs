%define oname meshpy

%def_with python3
%def_without docs

Name: python3-module-%oname
Version: 2018.2.1
Release: alt2
Summary: Triangular and Tetrahedral Mesh Generator in Python
License: MIT
Group: Development/Python3
Url: http://mathema.tician.de/software/meshpy
Packager: Python Development Team <python@packages.altlinux.org>

# http://git.tiker.net/trees/meshpy.git
Source: %oname-%version.tar
# git://github.com/inducer/bpl-subset
Source1: bpl-subset.tar

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: boost-python3-devel
BuildRequires: python3-module-pybind11

%if_with docs
BuildRequires: python-module-epydoc python-module-html5lib
%endif

%description
MeshPy offers quality triangular and tetrahedral mesh generation for
Python. Meshes of this type are chiefly used in finite-element
simulation codes, but also have many other applications ranging from
computer graphics to robotics.

%package tests
Summary: Tests for MeshPy
Group: Development/Python3
Requires: %name = %EVR

%description tests
MeshPy offers quality triangular and tetrahedral mesh generation for
Python. Meshes of this type are chiefly used in finite-element
simulation codes, but also have many other applications ranging from
computer graphics to robotics.

This package contains tests for MeshPy.

%package -n python-module-meshpy-docs
Summary: Documentation for MeshPy
Group: Development/Documentation
BuildArch: noarch

%description -n python-module-meshpy-docs
MeshPy offers quality triangular and tetrahedral mesh generation for
Python. Meshes of this type are chiefly used in finite-element
simulation codes, but also have many other applications ranging from
computer graphics to robotics.

This package contains documentation for MeshPy.

%prep
%setup

sed -i 's/python/python3/g' configure.py

rm -fR bpl-subset
tar -xf %SOURCE1

%build
./configure.py
%python3_build_debug

%if_with docs
export PYTHONPATH=$PWD
%make doc
%endif

%install
%python3_install
touch test/__init__.py
rm -f test/clean.sh
cp -fR test %buildroot%python3_sitelibdir/%oname/

%files
%doc LICENSE README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test

%files tests
%python3_sitelibdir/%oname/test

%if_with docs
%files -n python-module-meshpy-docs
%doc doc/*.rst
%endif

%changelog
* Mon Dec 23 2019 Anton Midyukov <antohami@altlinux.org> 2018.2.1-alt2
- build python 3 module only
- disable build docs (needed python 2)

* Mon Feb 11 2019 Anton Midyukov <antohami@altlinux.org> 2018.2.1-alt1
- Version 2018.2.1

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2014.1-alt3.git20140706.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2014.1-alt3.git20140706.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2014.1-alt3.git20140706
- NMU: added python-module-setuptools to BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2014.1-alt2.git20140706.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.1-alt2.git20140706
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.1-alt1.git20140706
- Version 2014.1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1.2-alt1.git20131122
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1.2-alt1.git20130916
- Version 2013.1.2

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20130121
- New snapshot

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20121113
- New snapshot

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20120902
- New snapshot

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20111128
- Rebuilt with Boost 1.49.0

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20111128
- Version 2011.1

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt2.git20101129
- Rebuilt with Boost 1.48.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.91.2-alt1.git20101129.2.1
- Rebuild with Python-2.7

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.git20101129.2
- Rebuilt with Boost 1.47.0

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.git20101129.1
- Rebuilt for debuginfo

* Tue Dec 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.git20101129
- Initial build for Sisyphus

