%define _unpackaged_files_terminate_build 1
%define oname pytest

%def_without check

Name: python-module-%oname
Version: 4.6.6
Release: alt2

Summary: Python test framework
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pytest.git
Url: https://pypi.python.org/pypi/pytest

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: python2.7(setuptools_scm)

%if_with check
BuildRequires: /dev/pts
BuildRequires: python2.7(tox)

BuildRequires: python2.7(argcomplete)
BuildRequires: python2.7(atomicwrites)
BuildRequires: python2.7(attr)
BuildRequires: python2.7(decorator)
BuildRequires: python2.7(funcsigs)
BuildRequires: python2.7(hypothesis)
BuildRequires: python2.7(mock)
BuildRequires: python2.7(more_itertools)
BuildRequires: python2.7(nose)
BuildRequires: python2.7(numpy)
BuildRequires: python2.7(py)
BuildRequires: python2.7(packaging)
BuildRequires: python2.7(pathlib2)
BuildRequires: python2.7(pexpect)
BuildRequires: python2.7(pluggy)
BuildRequires: python2.7(requests)
BuildRequires: python2.7(six)
BuildRequires: python2.7(wcwidth)

%endif

%py_requires funcsigs
%py_requires pathlib2
%py_requires py
%py_requires wcwidth

BuildArch: noarch

%description
The pytest framework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.

%package -n pytest
Summary: Additional executable for pytest
Group: Development/Python
Requires: python-module-%oname = %EVR
# It simply has executables with the same filename:
Conflicts: python-module-logilab-common < 1.0.2-alt2.hg20150708

%description -n pytest
The pytest framework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.

%prep
%setup
%patch -p1

%if_with check
# adjust timeouts for testing on aarch64/beehive
grep -qs 'child\.expect(.*)' \
testing/{test_pdb.py,test_terminal.py,test_unittest.py} || exit 1
grep -qs 'child\.expect_exact([[:space:]]*$' \
testing/{test_pdb.py,test_terminal.py,test_unittest.py} || exit 1
grep -qs 'testdir\.spawn_pytest([[:space:]]*$' \
testing/{test_pdb.py,test_terminal.py,test_unittest.py} || exit 1

sed -i -e '/child\.expect(.*)/s/)[[:space:]]*$/, timeout=60)/g;' \
-e '/child\.expect_exact([[:space:]]*$/{$!N;s/\n\([[:space:]]*\)\(.*\)/\n\1\2,\n\1timeout=60,/g}' \
-e '/testdir\.spawn_pytest(.*)/s/)[[:space:]]*$/, expect_timeout=30)/g;' \
-e '/testdir\.spawn_pytest([[:space:]]*$/{$!N;s/\n\([[:space:]]*\)\(.*\)/\n\1\2,\n\1expect_timeout=30,/g}' \
-e 's/\([[:space:]]*\)child\.sendline(\x22p .*)$/&\n\1import time; time.sleep(child.delaybeforesend)/g' \
testing/{test_pdb.py,test_terminal.py,test_unittest.py}
%endif

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
%define python2_nodots py%{python_version_nodots python}
export TOXENV=%python2_nodots,%python2_nodots-pexpect
tox --sitepackages -p auto -o -v

%files
%doc AUTHORS LICENSE *.rst
%_bindir/py.test
%python_sitelibdir/pytest.py*
%python_sitelibdir/_pytest/
%python_sitelibdir/pytest-*.egg-info/

%files -n pytest
%_bindir/pytest

%changelog
* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 4.6.6-alt2
- Disabled testing.

* Fri Nov 15 2019 Stanislav Levin <slev@altlinux.org> 4.6.6-alt1
- 4.6.5 -> 4.6.6.

* Thu Aug 22 2019 Stanislav Levin <slev@altlinux.org> 4.6.5-alt1
- 4.6.4 -> 4.6.5.

* Mon Aug 05 2019 Stanislav Levin <slev@altlinux.org> 4.6.4-alt1
- 4.6.2 -> 4.6.4.
- Moved Python3 package out to its own one.

* Wed Jun 05 2019 Stanislav Levin <slev@altlinux.org> 4.6.2-alt1
- 4.5.0 -> 4.6.2
  ~ The 4.6.X series will be the last series to support Python 2
  ~ https://docs.pytest.org/en/latest/py27-py34-deprecation.html

* Mon May 27 2019 Stanislav Levin <slev@altlinux.org> 4.5.0-alt1
- 3.10.1 -> 4.5.0.

* Sun Mar 31 2019 Stanislav Levin <slev@altlinux.org> 3.10.1-alt5
- Fixed testing against py 1.8.0.

* Thu Feb 07 2019 Stanislav Levin <slev@altlinux.org> 3.10.1-alt4
- Fixed "test_pdb_unittest_postmortem" test.

* Wed Jan 23 2019 Stanislav Levin <slev@altlinux.org> 3.10.1-alt3
- Fixed "test_raises_exception_looks_iterable" test.

* Sun Jan 13 2019 Stanislav Levin <slev@altlinux.org> 3.10.1-alt2
- Added workaround for request_garbage test.

* Mon Dec 17 2018 Stanislav Levin <slev@altlinux.org> 3.10.1-alt1
- 3.9.3 -> 3.10.1.

* Sun Oct 28 2018 Stanislav Levin <slev@altlinux.org> 3.9.3-alt1
- 3.9.1 -> 3.9.3.

* Sun Oct 21 2018 Stanislav Levin <slev@altlinux.org> 3.9.1-alt1
- 3.8.2 -> 3.9.1.

* Thu Oct 04 2018 Stanislav Levin <slev@altlinux.org> 3.8.2-alt1
- 3.7.3 -> 3.8.2.

* Wed Aug 29 2018 Stanislav Levin <slev@altlinux.org> 3.7.3-alt1
- 3.7.2 -> 3.7.3.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 3.7.2-alt1
- 3.4.2 -> 3.7.2.

* Tue Mar 20 2018 Stanislav Levin <slev@altlinux.org> 3.4.2-alt1
- 3.2.1 -> 3.4.2

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.1-alt1
- Updated to upstream version 3.2.1.

* Thu Jan 26 2017 Ivan Zakharyaschev <imz@altlinux.org> 3.0.5-alt3
- %%check: enabled Python3 tests.

* Thu Jan 26 2017 Ivan Zakharyaschev <imz@altlinux.org> 3.0.5-alt2
- Separate packages for the extra /usr/bin/pytest* to track their
  users (ALT#33028).
- /usr/bin/py.test3 - Avoid dep on minor version of python3 in the filename:
  + no need to rebuild with the change of python3's minor version;
  + no need for python3 to preprocess the .spec.
- (.spec) BuildPreReq for manually written build deps.
- (.spec) put Requires before any specs how to build (they are
  externally visible).
- (.spec) A bit safer scripting.
- (.spec) more %%if_with python3 (to avoid unwanted calls to python3;
  just in case).

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 3.0.5-alt1
- New version 3.0.5
- srpm build

* Sat Mar 19 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.0-alt1.dev4.git20150807.2.workaround
- Rebuild with python3-3.5 to update the executable name (this is a
  workaround; this should be fixed not to depend on the minor version).
- This rebuild (with rpm-build-python3-0.1.10) will also switch to the
  new python3(*) reqs.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.0-alt1.dev4.git20150807.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.8.0-alt1.dev4.git20150807.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.dev4.git20150807
- New snapshot

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.dev4.git20150726
- Version 2.8.0.dev4

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.dev1.hg20141030
- Version 2.7.0.dev1

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt2.dev1.hg20141025
- New snapshot

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt2.dev1.hg20141009
- Added requirement on py

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.dev1.hg20141009
- Version 2.6.4.dev1

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.dev1.hg20140109
- Version 2.5.2.dev1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.dev2.hg20131122
- Version 2.4.3.dev2

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.dev12.hg20130909
- Version 2.4.0.dev12

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.5.dev8-alt1.hg20130328
- Version 2.3.5.dev8

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.3.0.dev10-alt1.hg20120813.1
- Rebuild with Python-3.3

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0.dev10-alt1.hg20120813
- Version 2.3.0.dev10

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.4.dev2-alt1.hg20120331
- Version 2.2.4.dev2
- Added module for Python 3

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2.dev6-alt1.hg20110120
- Version 2.2.2.dev6

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.hg20111119
- Fixed buildreq

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.hg20111119
- Version 2.2.0
- Disabled conflict with py

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.3-alt1.hg20110501.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.hg20110501
- Version 2.0.3

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.hg20101120.2
- Rebuilt with python-module-sphinx-devel

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.hg20101120.1
- Added explicit conflict with py

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.hg20101120
- Initial build for Sisyphus

