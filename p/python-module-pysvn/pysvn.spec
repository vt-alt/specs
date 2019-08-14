%define oname pysvn

%def_with python3

Name: python-module-%oname
Version: 1.9.10
Release: alt1
Summary: Subversion support for python
License: Apache License
Group: Development/Python
Url: http://pysvn.tigris.org/

Source0: pysvn-%version.tar

BuildRequires: gcc-c++ libcom_err-devel libexpat-devel libkrb5-devel libsubversion-devel python-devel python-modules-compiler python-modules-xml subversion
BuildRequires: libaprutil1-devel
BuildRequires: subversion-server-common
BuildRequires: python-module-pycxx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pyutilib-svn
BuildRequires: python3-module-pycxx-devel
BuildPreReq: python3-devel python-tools-2to3
%endif

%description
The pysvn project's goal is to enable Tools to be written in Python that
use Subversion.

%package -n python3-module-%oname
Summary: Subversion support for python
Group: Development/Python3

%description -n python3-module-%oname
The pysvn project's goal is to enable Tools to be written in Python that
use Subversion.

%prep
%setup -n pysvn-%version

%if_with python3
cp -fR . ../python3
%endif

%build
pushd Source
python setup.py configure \
    --apr-inc-dir=/usr/include/apr-1 \
    --apu-inc-dir=/usr/include/apu-1 \
    --norpath

%make_build
popd

%if_with python3
pushd ../python3
pushd Source
python3 setup.py configure \
    --apr-inc-dir=/usr/include/apr-1 \
    --apu-inc-dir=/usr/include/apu-1 \
    --norpath

%make_build
popd
%endif

%install
mkdir -p %buildroot%python_sitelibdir 
cp -r Source/pysvn %buildroot%python_sitelibdir

%if_with python3
pushd ../python3
mkdir -p %buildroot%python3_sitelibdir 
cp -r Source/pysvn %buildroot%python3_sitelibdir
popd
%endif

%files
%dir %python_sitelibdir/pysvn
%python_sitelibdir/pysvn/*

%if_with python3
%files -n python3-module-%oname
%dir %python_sitelibdir/pysvn
%python3_sitelibdir/pysvn/*
%endif

%changelog
* Thu Aug 01 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.10-alt1
- Build new version.

* Wed Apr 17 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.9-alt1
- Build new version for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Feb 10 2016 Denis Medvedev <nbr@altlinux.org> 1.8.0-alt1
- up version

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.8-alt1
- Version 1.7.8
- Added module for Python 3

* Wed Mar 06 2013 Andrey Cherepanov <cas@altlinux.org> 1.7.6-alt1
- New version 1.7.6
- Remove obsoleted patches

* Wed Mar 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt3.3
- Fixed build with subversion 1.7.8

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt3.2
- Removed RPATH

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.2-alt3.1
- Rebuild with Python-2.7

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt3
- Rebuilt for debuginfo

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt2
- Rebuilt with python 2.6

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.5.2-alt1.1
- Rebuilt with python-2.5.

* Tue Jan 02 2008 Gennady Kovalev <gik@altlinux.ru> 1.5.2-alt1
- Initial build

