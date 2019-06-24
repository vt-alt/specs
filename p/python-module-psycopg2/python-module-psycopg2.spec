%define oname psycopg2
%def_with python3

Version: 2.8.3
Release: alt1
%setup_python_module %oname

Summary: psycopg2 is a PostgreSQL database adapter for Python
Name: %packagename
# https://github.com/psycopg/psycopg2.git
Source0: psycopg2.tar
License: GPL
Group: Development/Python
URL: http://www.psycopg.org/psycopg/
# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: elfutils libpq-devel libsasl2-3 python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: postgresql-devel python-devel python3-devel rpm-build-python3

#BuildRequires: postgresql-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python-tools-2to3
%endif

Requires: python-modules-json

%description
psycopg is a PostgreSQL database adapter for the Python programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.

%if_with python3
%package -n python3-module-%oname
Summary: psycopg2 is a PostgreSQL database adapter for Python 3
Group: Development/Python3

%description -n python3-module-%oname
psycopg is a PostgreSQL database adapter for the Python 3 programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.
%endif

%package doc
Summary: Documentation for psycopg2 python PostgreSQL database adapter
Group: Development/Python
BuildArch: noarch

%description doc
Documenation and example files for the psycopg2 python PostgreSQL
database adapter.

%prep
%setup

echo "include_dirs=.:/usr/include/pgsql" >> setup.cfg

%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
%python3_build
%endif

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%if_with python3
%python3_install
%endif

%files -f INSTALLED_FILES
%dir %python_sitelibdir/psycopg2

%files doc
%doc AUTHORS INSTALL README* doc

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Mon Jun 17 2019 Grigory Ustinov <grenka@altlinux.org> 2.8.3-alt1
- Build new version.

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 2.8.2-alt1
- Build new version.
- Clean up changelog.

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 2.8.1-alt1
- Build new version for python3.7.
- Removed tests packages, because they doesn't supported now.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.3.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.3.1-alt1
- Updated to upstream version 2.7.3.1.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7-alt1.dev0.git20150602.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 2.7-alt1.dev0.git20150602.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.dev0.git20150602
- Version 2.7.dev0

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.git20150209
- Version 2.6

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.dev0.git20141225
- New snapshot

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.dev0.git20140731
- Version 2.6.dev0

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2
- Changed URL (ALT #29766)
- Added Requires: python-modules-json (ALT #29767)

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 2.5.1-alt1
- 2.5.1
- Dropped Zope adapter from source repository. ZPsycopgDA now has its own
  project at <http://github.com/psycopg/ZPsycopgDA>.

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt2.git20120328
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.5-alt1.git20120328.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt1.git20120328
- Version 2.4.5
- Added module for Python 3

* Mon Jan 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt1.git20111219
- Version 2.4.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.1-alt2.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt2
- Rebuilt for debuginfo

* Wed Dec 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1
- Version 2.3.1 (ALT #24712)
- Extracted tests into separate package

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt3
- Fixed underlinking

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt2
- Set docs package as noarch

* Fri Jul 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1
- Version 2.2.2

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.8-alt1.1
- Rebuilt with python 2.6

* Sat Nov 01 2008 Ivan Fedorov <ns@altlinux.org> 2.0.8-alt1
- new version

* Thu Jan 03 2008 Ivan Fedorov <ns@altlinux.org> 2.0.6-alt3
- fix building

* Sun Jul 15 2007 Ivan Fedorov <ns@altlinux.org> 2.0.6-alt2
- 2.0.6
- fixed bug in type casting. (uninitialized pointer)

* Wed Mar 21 2007 Ivan Fedorov <ns@altlinux.ru> 2.0.6-alt1.svn876
- rebuild with libpq5 from postgresql8.2
- update to svn

* Sat Mar 03 2007 Ivan Fedorov <ns@altlinux.ru> 2.0.6-alt1.b1
- 2.0.6b1

* Sun Feb 18 2007 Ivan Fedorov <ns@altlinux.ru> 2.0.5.1-alt1
- 2.0.5.1

* Sat Jul 01 2006 Ivan Fedorov <ns@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Sun Feb 12 2006 Ivan Fedorov <ns@altlinux.ru> 2.0-alt0.b8
- 2.0b8

* Wed Feb 01 2006 Ivan Fedorov <ns@altlinux.ru> 2.0-alt0.b6
- 2.0b6

* Thu Nov 10 2005 Ivan Fedorov <ns@altlinux.ru> 2.0-alt0.b5
- 2.0b5

* Mon Oct 03 2005 Ivan Fedorov <ns@altlinux.ru> 2.0-alt0.b4
- switch to 2.0 branch
- 2.0b4

* Tue Jan 11 2005 Andrey Orlov <cray@altlinux.ru> 1.1.18-alt1
- New Version

* Fri Jul 02 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt9
- Requires for egenix-mx-base added;

* Wed May 19 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt8
- Obsoleting of previous packages added

* Tue May 18 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt7
- Conditional operators excluded from spec

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt6.d
- Fix egenix-mx-base dependence

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt5.d
- Remove BuildArchitecture: noarch clause

* Tue Apr 13 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt4.d
- Rebuild with new rpm/python macros
- Insert BuildArchitecture: noarch clause

* Fri Mar 26 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt3.d
- New version
- Fix new python policy compatibility

* Wed Dec 10 2003 Andrey Orlov <cray@altlinux.ru> 1.1.9-alt4
- Fix permissions
- Try eliminate libpq2
- Try to use with py23

* Sun Sep 14 2003 Andrey Orlov <cray@altlinux.ru> 1.1.9-alt1
- New release

* Sat Dec 14 2002 Andrey Orlov <cray@altlinux.ru> 1.0.12-alt3
- Declaration of requirements are enhanced

* Mon Dec 02 2002 Andrey Orlov <cray@altlinux.ru> 1.0.12-alt2
- Logging of all queries in debug mode (STUPID_LOG_SEVERITY=DEBUG) was added

* Tue Oct 29 2002 Andrey Orlov <cray@altlinux.ru> 1.0.12-alt1
- Recompile with gcc 3.2.1
