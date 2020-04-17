%define oname psutil

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 5.7.0
Release: alt1

Summary: A process utilities module for Python

License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/psutil/

# Source-url: https://pypi.io/packages/source/p/%oname/%oname-%version.tar.gz
Source: %oname-%version.tar

%add_python_req_skip _psutil_bsd _psutil_mswindows _psutil_osx pywintypes win32com
%add_python_req_skip _psutil_sunos _psutil_windows

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools-tests /proc
#BuildPreReq: python-module-mock
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-mock
%endif

%setup_python_module %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-pbr python-module-pytest python-module-unittest2 python3-devel python3-module-html5lib python3-module-pbr python3-module-pytest python3-module-unittest2 rpm-build-python3

%description
psutil is a module providing an interface for retrieving information on running
processes and system utilization (CPU, memory) in a portable way by using
Python, implementing many functionalities offered by tools like ps, top and
Windows task manager.

%package -n python3-module-%oname
Summary: A process utilities module for Python
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip _psutil_bsd _psutil_mswindows _psutil_osx pywintypes win32com
%add_python3_req_skip _psutil_sunos _psutil_windows

%description -n python3-module-%oname
psutil is a module providing an interface for retrieving information on running
processes and system utilization (CPU, memory) in a portable way by using
Python, implementing many functionalities offered by tools like ps, top and
Windows task manager.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py build_ext -i
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc CREDITS *.rst LICENSE docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CREDITS *.rst LICENSE docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Apr 12 2020 Vitaly Lipatov <lav@altlinux.ru> 5.7.0-alt1
- new version 5.7.0 (with rpmrb script) (ALT bug 38347)
- CVE-2019-18874

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 5.6.3-alt1
- new version 5.6.3 (with rpmrb script)

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 5.6.1-alt1
- new version 5.6.1 (with rpmrb script)

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 5.5.1-alt1
- new version 5.5.1 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 5.4.7-alt1
- new version 5.4.7 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 5.4.3-alt1
- new version 5.4.3 (with rpmrb script)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 5.3.1-alt1
- new version 5.3.1 (with rpmrb script)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.1-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.1.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1
- Version 3.1.1

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt1
- Version 2.1.3
- Added module for Python 3

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)

* Sat Feb 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Version 0.6.1 (ALT #28561)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Jan 23 2012 Alexey Morsov <swi@altlinux.ru> 0.4.1-alt1
- new version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.3-alt1.1
- Rebuild with Python-2.7

* Wed Sep 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- initial build for ALT Linux Sisyphus
