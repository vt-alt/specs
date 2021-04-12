%define branch 1.11
%define version %branch.29
%define release alt2
%define origname Django
%define oname django

%def_disable check

%setup_python_module django
%add_python_req_skip cx_Oracle
%add_findreq_skiplist %python_sitelibdir/%modulename/contrib/gis/db/backends/*/*

Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Name: python-module-%oname
Version: %version
Release: %release
Source0: %origname-%version.tar
License: BSD
Group: Development/Python
BuildArch: noarch
URL: http://www.djangoproject.com/
Provides: Django = %EVR
Provides: %name%branch = %EVR
Obsoletes: python-module-django2.2 < %EVR
Obsoletes: python-module-django1.5 < %EVR
Conflicts: python-module-django1.0 python-module-django1.1
Conflicts: python-module-django1.2
Provides: %name-tests = %EVR
Provides: %name%branch-tests = %EVR
Obsoletes: %name%branch-tests < %EVR
Obsoletes: python-module-django1.5-tests < %EVR
Conflicts: python-module-django1.0-tests
Conflicts: python-module-django1.1-tests
Conflicts: python-module-django1.2-tests


BuildRequires(pre): rpm-build-python
BuildRequires: python-module-six

%if_enabled check
BuildRequires: python-module-sqlparse
BuildRequires: python-module-pytz
BuildRequires: python-modules-sqlite3
BuildRequires: python-module-jinja2
BuildRequires: python-module-numpy
BuildRequires: python-module-pylibmc
BuildRequires: python-module-memcached
BuildRequires: python-module-yaml
BuildRequires: python-module-enum34
BuildRequires: python-module-selenium
BuildRequires: python-module-mock
BuildRequires: python-modules-wsgiref
%endif

%description
%summary

%package dbbackend-mysql
Summary: MySQLSQL support for Django.
Group: Development/Python
Requires: %name = %EVR
%py_requires MySQLdb
Provides: %name%branch-tests-mysql = %EVR
Obsoletes: %name%branch-tests-mysql < %EVR
Obsoletes: python-module-django1.5-dbbackend-mysql <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-mysql
Conflicts: python-module-django1.1-dbbackend-mysql
Conflicts: python-module-django1.2-dbbackend-mysql

%description dbbackend-mysql
%summary

%package dbbackend-psycopg
Summary: PostgreSQL support for Django. (via psycopg)
Group: Development/Python
Requires: %name = %EVR
%py_requires psycopg
Provides: %name%branch-psycopg = %EVR
Obsoletes: %name%branch-psycopg < %EVR
Obsoletes: python-module-django1.5-dbbackend-psycopg <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-psycopg
Conflicts: python-module-django1.1-dbbackend-psycopg
Conflicts: python-module-django1.2-dbbackend-psycopg

%description dbbackend-psycopg
%summary

%package dbbackend-psycopg2
Summary: PostgreSQL support for Django. (via psycopg2)
Group: Development/Python
Requires: %name = %EVR
%py_requires psycopg2
Provides: %name%branch-psycopg2 = %EVR
Obsoletes: %name%branch-psycopg2 < %EVR
Obsoletes: python-module-django1.5-dbbackend-psycopg2 <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-psycopg2
Conflicts: python-module-django1.1-dbbackend-psycopg2
Conflicts: python-module-django1.2-dbbackend-psycopg2

%description dbbackend-psycopg2
%summary

%package dbbackend-sqlite3
Summary: SQLite3 support for Django.
Group: Development/Python
Requires: %name = %EVR
%py_requires sqlite3
Provides: %name%branch-sqlite3 = %EVR
Obsoletes: %name%branch-sqlite3 < %EVR
Obsoletes: python-module-django1.5-dbbackend-sqlite3 <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-sqlite3
Conflicts: python-module-django1.1-dbbackend-sqlite3
Conflicts: python-module-django1.2-dbbackend-sqlite3

%description dbbackend-sqlite3
%summary

%package doc
Summary: Django documentation
Group: Development/Documentation
Provides: %name%branch-doc = %EVR
Obsoletes: %name%branch-doc < %EVR
Obsoletes: python-module-django1.5-doc <= 1.5.0-alt3
Obsoletes: python3-module-django-doc <= 1.5.0-alt1.alpha
Conflicts: python-module-django1.0-doc
Conflicts: python-module-django1.1-doc
Conflicts: python-module-django1.2-doc

%description doc
%summary

%prep
%setup -n %origname-%version

# Use system six instead of bundled
find -type f -name '*.py*' -exec sed -i 's|django.utils.six|six|'  -- '{}' +

find -type f -name '*.py*' -exec sed -i 's|%_bindir/env python|%_bindir/python2|' -- '{}' +
find -type f -name '*.py' -exec sed -i 's|.*from future_builtins import zip.*||' -- '{}' +

%build
%python_build

%install
export LC_ALL=en_US.UTF-8
%python_install
mv %buildroot%_bindir/django-admin.py %buildroot%_bindir/django-admin.py2

# remove .po files
find %buildroot -name "*.po" | xargs rm -f


%check
export PYTHONPATH=$(pwd)
cd tests
LANG="en_US.UTF-8" python runtests.py --settings=test_sqlite --verbosity=2 --parallel 1

%files
%_bindir/django-admin.py2
%python_sitelibdir/*

%exclude %python_sitelibdir/%modulename/db/backends/mysql/
#exclude %python_sitelibdir/%modulename/db/backends/postgresql/
%exclude %python_sitelibdir/%modulename/db/backends/postgresql_psycopg2/
%exclude %python_sitelibdir/%modulename/db/backends/sqlite3/

%files doc
%doc docs

%files dbbackend-mysql
%python_sitelibdir/%modulename/db/backends/mysql/

#files dbbackend-psycopg
#python_sitelibdir/%modulename/db/backends/postgresql/

%files dbbackend-psycopg2
%python_sitelibdir/%modulename/db/backends/postgresql_psycopg2/

%files dbbackend-sqlite3
%python_sitelibdir/%modulename/db/backends/sqlite3/

%changelog
* Wed Feb 24 2021 Alexey Shabalin <shaba@altlinux.org> 1.11.29-alt2
- rename package to python-module-django back

* Sun Apr 12 2020 Alexey Shabalin <shaba@altlinux.org> 1.11.29-alt1
- 1.11.29
- build only for python2
- merge tests package to main
- enable tests
- Fixes for the following security vulnerabilities:
  + CVE-2019-19844: Potential account hijack via password reset form
  + CVE-2020-7471: Potential SQL injection via StringAgg(delimiter)
  + CVE-2020-9402: Potential SQL injection via tolerance parameter in GIS functions and aggregates on Oracle

* Mon Aug 05 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.23-alt1
- 1.11.23
- Fixes for the following security vulnerabilities:
  + CVE-2019-14232 Adjusted regex to avoid backtracking issues when truncating HTML
  + CVE-2019-14233 Prevented excessive HTMLParser recursion in strip_tags() when handling incomplete HTML entities
  + CVE-2019-14234 Protected JSONField/HStoreField key and index lookups against SQL injection
  + CVE-2019-14235 Fixed potential memory exhaustion in django.utils.encoding.uri_to_iri()

* Tue Jul 16 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.22-alt2
- revert rename package to python-module-django1.11

* Mon Jul 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.22-alt1
- 1.11.22
- rename package to python-module-django1.11
- Fixes for the following security vulnerabilities:
  + CVE-2019-12781 Incorrect HTTP detection with reverse-proxy connecting via HTTPS
  + CVE-2019-12308 AdminURLFieldWidget XSS
  + CVE-2019-6975 Memory exhaustion in django.utils.numberformat.format()
  + CVE-2019-3498 Content spoofing possibility in the default 404 page

* Mon Dec 17 2018 Grigory Ustinov <grenka@altlinux.org> 1.11.17-alt1
- Build new version (Closes: #35861).
- Transfer to python3.
- Temporary disabled check.

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1.8.18-alt1
- 1.8.18
- fixed CVE-2017-7233,CVE-2017-7234

* Thu Feb 02 2017 Alexey Shabalin <shaba@altlinux.ru> 1.8.17-alt1
- 1.8.17
- fixed CVE-2016-9013,CVE-2016-9014 

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.15-alt1
- 1.8.15
- fixed CVE-2016-2512,CVE-2016-2513,CVE-2016-6186,CVE-2016-7401

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.7-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.7-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.8.7-alt1.1
- NMU: Use buildreq for BR.

* Fri Nov 27 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.7-alt1
- 1.8.7
- fixed CVE-2015-8213

* Tue Oct 13 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.5-alt1
- 1.8.5
- fixed CVE-2015-5143, CVE-2015-5144, CVE-2015-5145, CVE-2015-5964, CVE-2015-5963

* Thu Apr 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8-alt2
- Version 1.8

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8-alt1.c1
- Version 1.8c1

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.b1
- Version 1.8b1

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1
- Version 1.7

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt1
- Version 1.6.6

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt1
- Version 1.6.5

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.1
- Use 'find... -exec...' instead of 'for ... $(find...'

* Wed Apr 03 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.1-alt1
- Version 1.5.1
- Fix python3-module-django

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt4.1
- Rebuild with Python-3.3

* Wed Feb 27 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt4
- Rename package to python-module-django

* Wed Feb 27 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt3
- Version 1.5.0

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt2.rc2
- Version 1.5.0-rc2
- Rename package to python-module-django1.5
- Remove %%name-mod_python subpackage

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.alpha
- Version 1.5.0-alpha

* Thu May 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4 (ALT #27288)

* Thu Dec 15 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.1-alt1
- Version 1.3.1. Security fixes:
  https://www.djangoproject.com/weblog/2011/sep/09/security-releases-issued/

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Version 1.3

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1
- Version 1.2.5

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1
- Version 1.2.3

* Thu Aug 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.2.1-alt2
- do not search for dependencies in django/contrib/gis/db/backends (closes: #23924)

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1
- Added tests (ALT #22479)

* Sun Mar 21 2010 Denis Klimov <zver@altlinux.org> 1.2-alt3.svn12825
- fix inherit with alt gear

* Sun Mar 21 2010 Denis Klimov <zver@altlinux.org> 1.2-alt2.svn12825
- new version
- remove examples subpackage. It was removed from Django.

* Tue Feb 09 2010 Denis Klimov <zver@altlinux.org> 1.2-alt2.svn12398
- new version

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.svn11756.1
- Rebuilt with python 2.6

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 1.2-alt2.svn11756
- add conflicts

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 1.2-alt1.svn11756
- new version
- use python macros
- add doc and examples subpackages
- remove test files

* Sat Sep 19 2009 Denis Klimov <zver@altlinux.org> 1.1-alt2.svn11581
- change depend for sqlite python module (Closes: #18957)

* Fri Sep 18 2009 Denis Klimov <zver@altlinux.org> 1.1-alt1.svn11581
- new version (Closes: #21617)

* Thu Jun 04 2009 Denis Klimov <zver@altlinux.org> 1.1-alt1.svn10914
- new version (Closes: #20300)

* Thu May 07 2009 Denis Klimov <zver@altlinux.org> 1.1-alt1.svn10702
- new version from trunk
- remove needless -q option from setup macros
- remove commented lines
- turn off test section

* Fri Mar 20 2009 Denis Klimov <zver@altlinux.org> 1.0-alt5.svn10105
- new version from trunk

* Sun Feb 15 2009 Denis Klimov <zver@altlinux.org> 1.0-alt5.svn9832
- new version from trunk

* Thu Sep 04 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt5
- 1.0 release

* Mon Sep 01 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt4.beta_2
- 1.0 beta 2

* Sun Aug 17 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt3.beta_1
- 1.0 beta 1

* Thu Aug 14 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt2.alpha_2
- 1.0 alpha 2
- BuildReq updates

* Fri Jul 25 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt1.alpha
- First 1.0 alpha
- Spec updates
- Removed ChangeLog.bz2
- Use Django unit tests

* Tue May 20 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7540
- Latest SVN trunk sources (Closes: #15646)
- Security fixes (http://groups.google.com/group/django-developers/browse_thread/thread/903d7c2af239ec42)
- Spec updates (pack subdirs)

* Fri Apr 11 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7412
- Latest SVN trunk sources
- Fixed packages description

* Thu Mar 20 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7152
- SVN trunk

* Sat Feb 09 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7103
- Latest svn trunk sources

* Mon Dec 10 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.2.svn6903
- Latest svn trunk sources

* Sat Dec 08 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.2.svn6898
- Latest svn trunk sources

* Mon Sep 24 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.1.svn6410
- Latest svn trunk sources
- Temporarily removed cx_Oracle requirement
- ChangeLog added to the docs
- Removed core/handler.py because it's deprecated

* Mon Jul 02 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.1.svn5583
- Near the 0.97 release

* Sat May 26 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.96-alt1
- New version
- Spec cleanups (package names)

* Thu Mar 08 2007 Ivan Fedorov <ns@altlinux.ru> 0.95.1-alt1
- Initial build for ALT Linux Sisyphus.
