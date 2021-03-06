%define _unpackaged_files_terminate_build 1
%define oname pycmd

Name: python-module-%oname
Version: 1.2
Release: alt2

Summary: Command line tools for helping with Python development
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pycmd/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# pycmd was separated from pylib at that point
Conflicts: py < 1.4.0
BuildArch: noarch
%py_requires py

%description
Collection of command line tools for dealing with python files
(locating, counting LOCs, cleaning up pyc files ...)

%package -n python3-module-%oname
Summary: Command line tools for helping with Python development
Group: Development/Python3

%description -n python3-module-%oname
Collection of command line tools for dealing with python files
(locating, counting LOCs, cleaning up pyc files ...)

%prep
%setup

cp -fR . ../python3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	../python3/%oname/*.py

%build
%python_build

pushd ../python3
%python3_build
popd

%install

pushd ../python3
%python3_install
popd

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%python_install

%files
%doc CHANGELOG LICENSE *.txt
%_bindir/py.cleanup
%_bindir/py.convert_unittest
%_bindir/py.countloc
%_bindir/py.lookup
%_bindir/py.svnwcrevert
%_bindir/py.which
%python_sitelibdir/pycmd/
%python_sitelibdir/pycmd-*.egg-info/

%files -n python3-module-%oname
%doc CHANGELOG LICENSE *.txt
%_bindir/py.cleanup.py3
%_bindir/py.convert_unittest.py3
%_bindir/py.countloc.py3
%_bindir/py.lookup.py3
%_bindir/py.svnwcrevert.py3
%_bindir/py.which.py3
%python3_sitelibdir/pycmd/
%python3_sitelibdir/pycmd-*.egg-info/

%changelog
* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 1.2-alt2
- Add Requires on python py.

* Fri Apr 13 2018 Stanislav Levin <slev@altlinux.org> 1.2-alt1
- 1.1 -> 1.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.hg20140627.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt1.hg20140627.1
- NMU: Use buildreq for BR.

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20140627
- Version 1.1
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.a2dev1-alt1.hg20130918
- New snapshot

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.a2dev1-alt1.hg20121007
- Version 1.0.a2dev1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.hg20101129.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101129
- New snapshot

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101108.1
- Added explicit conflict with py

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101108
- Initial build for Sisyphus

