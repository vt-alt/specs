%define rname reportlab
%define oname Reportlab

Name: python3-module-%oname
Version: 3.5.66
Release: alt1

Summary: The Reportlab Toolkit

License: BSD license (see LICENSE.txt for details)
Group: Development/Python3
Url: http://www.reportlab.org

# Source-url: %__pypi_url %rname
Source: reportlab-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-sphinx

%description
The ReportLab Toolkit.
An Open Source Python library for generating PDFs and graphics.

%package docs
Summary: Documentation for Reportlab Toolkit
Group: Development/Documentation
BuildArch: noarch

%description docs
The ReportLab Toolkit.
An Open Source Python library for generating PDFs and graphics.

This package contains documentation for Reportlab Toolkit.

%prep
%setup -n reportlab-%version

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%make -C docs html SPHINXBUILD=sphinx-build-3

%install
%python3_install
%python3_prune

%files
%doc *.txt
%python3_sitelibdir/%rname/
%python3_sitelibdir/%rname-*.egg-info/

%files docs
%doc docs/build/html docs/userguide demos

%changelog
* Wed Apr 07 2021 Vitaly Lipatov <lav@altlinux.ru> 3.5.66-alt1
- build python3 separately
- new version 3.5.66 (with rpmrb script) (ALT bug 39865)

* Sun Apr 07 2019 Michael Shigorin <mike@altlinux.org> 3.4.0-alt3
- added explicit BR: python-dev to ease e2k python upgrade

* Thu Apr 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.0-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 29 2018 Vitaly Lipatov <lav@altlinux.ru> 3.4.0-alt2
- add provides: python-reportlab (ALT bug 34732)

* Mon Mar 12 2018 Vitaly Lipatov <lav@altlinux.ru> 3.4.0-alt1
- new version (3.4.0) with rpmgs script

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 3.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Added module for Python 3

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1
- Version 2.7

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt3.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt3
- Rebuilt with python-module-sphinx-devel

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt2
- Rebuilt for debuginfo

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Version 2.5
- Added tests

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-Reportlab
  * postclean-05-filetriggers for spec file

* Sat Jan 23 2010 Alexey Morsov <swi@altlinux.ru> 2.4-alt1
- new version

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.1
- Rebuilt with python 2.6

* Wed Feb 25 2009 Alexey Morsov <swi@altlinux.ru> 2.3-alt1
- new version
- clean spec

* Wed Nov 26 2008 Alexey Morsov <swi@altlinux.ru> 2.2-alt1
- new version

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 2.1-alt2.1
- Rebuilt with python-2.5.

* Tue Jan 22 2008 Grigory Batalov <bga@altlinux.ru> 2.1-alt2
- Remove python version from BuildRequires and Requires.

* Fri Jun 15 2007 Alexey Morsov <swi@altlinux.ru> 2.1-alt1
- version 2.1
- add python_sitelibdir  to files

* Thu Jan 18 2007 Alexey Morsov <swi@altlinux.ru> 2.0-alt1
- New version: full support for unicode, python 2.4 or higher
is required.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.20-alt2.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Sat Apr 09 2005 Andrey Orlov <cray@altlinux.ru> 1.20-alt2
- Font rina.ttf excluded due to  license restrictions
- Documentation files added
- License text added

* Wed Jan 12 2005 Andrey Orlov <cray@altlinux.ru> 1.20-alt1
- New Version

* Mon May 17 2004 Andrey Orlov <cray@altlinux.ru> 1.19-alt5
- Changed for sisyphus

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 1.19-alt4.d
- Rebuild

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 1.19-alt3.d
- Rebuild with new rpm/python macros

* Tue Apr 13 2004 Andrey Orlov <cray@altlinux.ru> 1.19-alt2.d
- Rebuild with new rpm/python macros

* Thu Mar 25 2004 Andrey Orlov <cray@altlinux.ru> 1.19-alt1.d
- Initial release

