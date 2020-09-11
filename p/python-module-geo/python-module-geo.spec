%define oname geo
Name: python-module-%oname
Version: 1.0.0
Release: alt1.svn20080909.6
Summary: Enthought Geophysics Tool Suite

Group: Development/Python
License: BSD
URL: http://code.enthought.com
# https://svn.enthought.com/svn/enthought/Geo
Source: Geo-%version.tar.gz

BuildRequires: python-devel, python-module-setuptools
BuildRequires: python-module-scipy gcc-c++ libnumpy-devel
BuildRequires: python-module-sphinx python-module-Pygments
BuildRequires: python-module-weave
BuildRequires: python-module-numpy-testing


%description
Enthought Geophysics Tool Suite.

%package doc
Summary: Documentation for Enthought Geophysics Tool Suite
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for Enthought Geophysics Tool Suite.

%prep
%setup

# fix dependencies
find . -name '*.py' -type f -print0 | xargs -0 sed -i \
	-e 's:scipy\.weave:weave:g'

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%files doc
%doc doc/*

%changelog
* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.svn20080909.6
- Added missing dep on `numpy.testing`.

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1.svn20080909.5
- Fixed build.

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.svn20080909.4.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.svn20080909.4
- Rebuild with Python-2.7

* Fri Oct 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20080909.3
- Rebuilt with updated NumPy

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20080909.2
- Rebuilt for debuginfo

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20080909.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20080909
- Initial build for Sisyphus

