%define _unpackaged_files_terminate_build 1

%define oname sphinx
%define sphinx_dir %python_sitelibdir_noarch/%oname

Name: python-module-%oname
Epoch: 1
Version: 1.6.5
Release: alt8

Summary: Tool for producing documentation for Python projects
License: BSD
Group: Development/Python
Url: http://sphinx-doc.org

BuildArch: noarch

%py_requires simplejson
%py_requires alabaster
%py_requires requests
%py_requires typing
%py_requires sphinxcontrib.websupport
%py_requires docutils

Provides: python-module-objects.inv
Obsoletes: python-module-objects.inv

# https://github.com/sphinx-doc/sphinx.git
Source0: %name-%version.tar
Source1: conf.py.template
Source2: macro
Source4: refcounting.py

Patch0: sphinx-1.4b1-alt-avoid-download-objects.inv.patch 
# deprecate formatargspec() and format_annotation()
Patch1: 464f94c2380b4cb2600735c0c0085e771da2bce4.patch
Patch2: sphinx-1.6.5-Fix-sphinx.testing-uses-deprecated-pytest-API-Node.patch
Patch3: sphinx-1.6.4-alt-disable-remote-tests.patch

BuildRequires(pre): rpm-build-python
BuildRequires: python-sphinx-objects.inv
BuildRequires: python-module-docutils
BuildRequires: python-module-html5lib
BuildRequires: python-module-nose
BuildRequires: python-module-alabaster
BuildRequires: python2.7(typing)
BuildRequires: python2.7(sphinxcontrib.websupport)
BuildRequires: /usr/bin/convert
BuildRequires: python2.7(sphinxcontrib)
BuildRequires: %py_dependencies imagesize
# For %%check:
BuildRequires: %py_dependencies mock
BuildRequires: python2.7(pytest)
# minimal deps on the built-in sqlite driver have been fixed in 1.0.8-alt2:
BuildRequires: python-module-SQLAlchemy >= 1.0.8-alt2
# These 2 must be recent to pass the tests:
BuildRequires: python-module-Pygments >= 2.1.3
BuildRequires: python-module-alabaster >= 0.7.6-alt2.git20150703

%description
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

%package devel
Summary: Development package for Sphinx
Group: Development/Python
Requires: %name = %EVR
Requires: %name-pickles = %EVR
Requires: rpm-macros-sphinx = %EVR

%description devel
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This package destinated for development of Python modules.

%package -n rpm-macros-sphinx
Summary: RPM macros for build with Sphinx
Group: Development/Python

# W.r.t. to the content of the macros (see the substitution in %%install):
#Requires: %sphinx_dir
# ...but we do not add such a formal dependency,
# because it is not needed at all
# given the intended usage of rpm-macros-* packages.
# The guarantee that a macro doesn't refer to a path other
# than the current valid %%sphinx_dir
# is given by the strict dep of the main pkg (on EVR of the macros pkg).

%description -n rpm-macros-sphinx
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains RPM macros for build with Sphinx.

%package tests
Summary: Tests for Sphinx
Group: Development/Python
Requires: %name = %EVR
%py_requires nose
%add_python_req_skip compiler
%add_python_req_skip missing_module missing_package1 missing_package2
%add_python_req_skip dummy missing_package3
%add_findreq_skiplist %sphinx_dir/tests/typing_test_data.py

%description tests
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains tests for Sphinx.

%package doc
Summary: Documentation for Sphinx
Group: Development/Python
%add_findreq_skiplist %sphinx_dir/pickle/_downloads/example_google.py
%add_findreq_skiplist %sphinx_dir/pickle/_downloads/example_numpy.py

%description doc
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This package contains documentation for Sphinx itself.

%package pickles
Summary: Pickles for Sphinx
Group: Development/Python

%description pickles
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains pickles for Sphinx.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
install -pm644 %SOURCE1 .

ln -s %_datadir/python-sphinx/objects.inv doc/
ln -s %_datadir/python-sphinx/objects.inv tests/

cp %SOURCE4 sphinx/ext/

install -pm644 %SOURCE2 .
# Invalid Python2:
rm tests/py35/test_autodoc_py35.py

%build
%python_build

# docs
%make_build -C doc html
%make_build -C doc man

%install
%python_install

ln -rs %buildroot%_datadir/python-sphinx/objects.inv \
	%buildroot%sphinx_dir/

# docs
install -d %buildroot%_docdir/%name
install -d %buildroot%_man1dir
cp -R doc/_build/html %buildroot%_docdir/%name/
install -p -m644 AUTHORS CHANGES* EXAMPLES LICENSE README.rst \
	%buildroot%_docdir/%name

# macros
install -d %buildroot%_rpmmacrosdir
sed -e 's:@SPHINX_DIR@:%sphinx_dir:g' < macro > %buildroot%_rpmmacrosdir/sphinx

# add pickle files
%make_build -C doc pickle

install -d %buildroot%sphinx_dir/doctrees
install -p -m644 doc/_build/doctrees/*.pickle \
	%buildroot%sphinx_dir/doctrees/
cp -R doc/_build/pickle %buildroot%sphinx_dir/
install -p -m644 conf.py.template \
	%buildroot%sphinx_dir/

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%name-files.req.list
%sphinx_dir	%name
EOF

%check
# Tried to export NOSE_PROCESSES=%%__nprocs, but it makes a lot tests fail.
export LC_ALL=en_US.utf8 # some tests fail otherwise, because they use paths with Unicode

rm -f tests/test_build_linkcheck.py
PYTHONPATH=$(pwd) %make_build test

%files
%_bindir/*
%sphinx_dir/
%exclude %sphinx_dir/testing
%exclude %sphinx_dir/pickle
%exclude %sphinx_dir/doctrees
%python_sitelibdir/*.egg-info

%files devel

%files pickles
%sphinx_dir/pickle
%sphinx_dir/doctrees

%files tests
%sphinx_dir/testing

%files doc
%doc %_docdir/%name

%files -n rpm-macros-sphinx
%_rpmmacrosdir/sphinx
%_rpmlibdir/%name-files.req.list

%changelog
* Wed Apr 29 2020 Grigory Ustinov <grenka@altlinux.org> 1:1.6.5-alt8
- Fixed FTBFS (Removed copying tests).

* Mon Sep 23 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.6.5-alt7
- Rebuilt without support for python-3.

* Sun Jun 09 2019 Stanislav Levin <slev@altlinux.org> 1:1.6.5-alt6
- Moved tests out to their own package.

* Sat Jun 01 2019 Stanislav Levin <slev@altlinux.org> 1:1.6.5-alt5
- Fixed Pytest4.x compatibility errors.

* Fri Apr 26 2019 Grigory Ustinov <grenka@altlinux.org> 1:1.6.5-alt4
- Fixed FTBFS (Closes: #36648).

* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.6.5-alt3
- added sphinx-build-3 for compatibility with fedora

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.6.5-alt2
- rebuild with python3.6

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.6.5-alt1
- Updated to upstream version 1.6.5.

* Thu Oct 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.6.4-alt1
- Updated to upstream version 1.6.4.

* Sat Apr 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.1-alt2
- %%py_requires alabaster (in the new source code, alabaster looks
  like a conditional import--i.e., not top-level and hence not
  autodetected--but this doesn't make much sense since setuptools
  check the declared reqs when running the entry_point
  %_bindir/sphinx-build...)

* Thu Apr 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.1-alt1
- 1.4.1 released

* Thu Apr 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4-alt8.a0.git20150813
- 2to3 not used, because sphinx is known to support Python3 natively.
  (This fixed one test that used to fail before.)
- Enabled %%check (for Python{2,3}).

* Thu Apr 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4-alt6.a0.git20150813
- (.spec) clarify: use the pure upstream sources & explicitly expose
  a single useful patch (sphinx-1.4b1-alt-avoid-download-objects.inv.patch).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4-alt5.a0.git20150813.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Mar  5 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4-alt5.a0.git20150813
- rpm-macros-* shouldn't have a formal dep on the main pkg (via %%sphinx_dir);
  the guarantee of compatibility is given by other formal deps
  (of the main pkgs on EVR of the macros pkg; see RPM Macros Packaging Policy
  and https://lists.altlinux.org/pipermail/devel/2016-March/201042.html).
- Declare with a *-files.req.list that we own %%sphinx{,3}_dir
  (just in case other pkgs happen to need to do something inside it).
- (.spec) When the various subpkgs owned %%sphinx_dir, too,
  this caused unwanted installation of them by APT/hsh for %%sphinx_dir.

* Thu Mar 03 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4-alt4.a0.git20150813
- rpm-macros-sphinx{,3}: save the real path %%__sphinx{,3}_dir
  (when built) and require it (when used).

* Wed Mar 02 2016 Dmitry V. Levin <ldv@altlinux.org> 1:1.4-alt3.a0.git20150813
- Added Provides/Obsoletes for python*-module-objects.inv.
- Cleaned up %%sphinx* macros.

* Tue Mar 01 2016 Dmitry V. Levin <ldv@altlinux.org> 1:1.4-alt2.a0.git20150813.2
- NMU: replaced python*-module-objects.inv with python-sphinx-objects.inv.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:1.4-alt2.a0.git20150813.1
- NMU: Use buildreq for BR.

* Wed Jan 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt2.a0.git20150813
- spec cleanup: *PreReq -> Requires, dropped rpm-macros-* deps.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4-alt1.a0.git20150813
- New snapshot

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4-alt1.a0.git20150727
- Version 1.4a0

* Thu Jun 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt7.a0
- Avoid download objects.inv

* Tue Jun 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt6.a0
- Restored %python3_sitelibdir/%oname/conf.py.template

* Tue Jun 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt5.a0
- New snapshot

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt4.a0
- Restored original sphinx/highlighting.py

* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt3.a0
- Removed sphinx.ext from sys.path

* Wed Jan 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt2.a0
- Enabled devel subpackage

* Wed Jan 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt1.a0
- Version 1.3a0

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2-alt2
- Added sphinx/ext/refcounting.py from old source

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2-alt1
- Version 1.2

* Thu Oct 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.3-alt6
- Fixed build manpages (ALT #29450)

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.3-alt5
- Use 'find... -exec...' instead of 'for ... $(find...'

* Thu Mar 21 2013 Aleksey Avdeev <solo@altlinux.ru> 1:1.1.3-alt4.1
- Rebuild with Python-3.3

* Sun Jan 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.3-alt4
- Disabled generating of man pages (broken)

* Mon Sep 10 2012 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.3-alt3
- Fixed rpm-macros-sphinx* interpackage requirements.

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.3-alt2
- Added python3-module-jinja2-tests in requirements for
  python3-module-sphinx-devel

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.3-alt1
- Version 1.1.3
- Added module for Python 3

* Thu Feb 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.2-alt4
- Added necessary requirements for rpm-macros-sphinx (ALT #26915)

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.2-alt3
- Fixed intersphinx.py

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.2-alt2
- Fixed doctest.py

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.2-alt1
- Version 1.1.2

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.7-alt3
- Built with docs (except pdf)

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.0.7-alt2.1
- Rebuild with Python-2.7 (bootstrap without docs)

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.7-alt2
- Find objects.inv into local machine

* Sat Apr 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.7-alt1
- Version 1.0.7

* Thu Mar 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.5-alt2
- Moved development requirements devel subpackage (inspired by damir@)
- Fixed requirements with %%epoch

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.5-alt1
- Version 1.0.5

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.1-alt2
- Restored sphinx.directives.desc
- Added requirement on simplejson

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.1-alt1
- Version 1.0.1

* Wed Jun 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt2
- Version 0.6.7 (version down from 1.0b2)

* Sat Feb 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt11
- Avoided rewrite conf.py

* Sat Feb 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt10
- Use objects.inv instead of Grammar file for build docs
- Macro %%prepare_sphinx need directory for copying files as parameter

* Tue Feb 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt9
- Added runtime requirement on %name-pickles

* Tue Feb 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt8
- Fixed syntax error in %%generate_pickles

* Tue Feb 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt7
- Macros: %%generate_pickles: added 3rd parameter for module name

* Mon Feb 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt6
- Macros %%generate_pickles: extended set of 1st parameter

* Wed Feb 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt5
- Added macros %%generate_pickles() for generating pickles in packages,
  that haven't this functions
- Add conf.py.template for work of Sphinx, when it copy into current
  docs directory (macros %%generate_pickles())

* Mon Feb 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt4
- Added macros %%sphinx_Grammar_file

* Mon Feb 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt3
- Added build time pickle files. E.g., files environment.pickle,
  searchindex.pickle and globalcontext.pickle may using as sources pickle
  files when build documentation

* Sun Jan 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt2
- Added:
  + pickles file (need by documentation process for some packages)
  + docs in PDF
  + manpages
  + tests package (fixed error in tests)
  + package with macros, need by build with python-module-%oname
- Enabled `make test' when build packages

* Thu Jan 21 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.4-alt1
- 0.6.4 (closes: #22808)

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1.1
- Rebuilt with python 2.6

* Thu Sep 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.1-alt2
- build HTML docs and package them as -doc subpackage

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.1-alt1
- initial build
