%define oname pycurl
%define oversion %(echo %version | sed -e "s|\\.|_|g")

Name: python3-module-pycurl
Version: 7.43.0.6
Release: alt2

Summary: Python bindings to libcurl
License: LGPL
Group: Development/Python3
Url: http://pycurl.io/
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/pycurl/pycurl/archive/REL_%oversion.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libcurl-devel libssl-devel

Requires: python3 >= 3.5

BuildRequires(pre): libcurl
%define libcurlver %(rpm -q --qf '%%{VERSION}' libcurl)
Requires: libcurl >= %libcurlver

%description
This module provides the Python bindings to libcurl.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing

%__python3 setup.py docstrings
%python3_build_debug

%install
%python3_install

%files
%_docdir/%oname/
%python3_sitelibdir/*


%changelog
* Tue Oct 06 2020 Vitaly Lipatov <lav@altlinux.ru> 7.43.0.6-alt2
- the package needs python 3.5 or above

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 7.43.0.6-alt1
- new version 7.43.0.6 (with rpmrb script)
- require libcurl not older than was at building time (ALT bug 25431)

* Wed Mar 18 2020 Pavel Skrylev <majioa@altlinux.org> 7.43.0.2-alt3
- fixed (!) inconsistency error to in libcurl versions 7.65.0 and 7.68.0 (fixes #38235)

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 7.43.0.2-alt2
- Build for python2 disabled.

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 7.43.0.2-alt1
- new version 7.43.0.2 (with rpmrb script)

* Thu Sep 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.43.0.1-alt2
- NMU: rebuilt with openssl 1.1.

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 7.43.0.1-alt1
- new version 7.43.0.1 (with rpmrb script)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.43.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sat Apr 23 2016 Vitaly Lipatov <lav@altlinux.ru> 7.43.0-alt1
- new version (7.43.0) with rpmgs script

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 7.19.5.3-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 7.19.5.3-alt1.1
- NMU: Use buildreq for BR.

* Sun Jan 03 2016 Vitaly Lipatov <lav@altlinux.ru> 7.19.5.3-alt1
- new version 7.19.5.3 (with rpmrb script)

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.5-alt1
- Version 7.19.5
- Added module for Python 3

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 7.19.3.1-alt1
- new version 7.19.3.1 (with rpmrb script)

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.0.3-alt1
- Version 7.19.0.3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 7.19.0-alt1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 7.19.0-alt1.2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.0-alt1.2
- Rebuilt for debuginfo

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.0-alt1.1
- Fixed build

* Thu Dec 02 2010 Ivan Fedorov <ns@altlinux.org> 7.19.0-alt1
- 7.19.0

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.16.4-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 7.16.4-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 7.16.4-alt1
- new version 7.16.4 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 7.16.1-alt1
- new version 7.16.1 (with rpmrb script)

* Sun Feb 04 2007 Vitaly Lipatov <lav@altlinux.ru> 7.16-alt0.1cvs
- build from CVS 20070204

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 7.15.5.1-alt0.1
- initial build for ALT Linux Sisyphus
