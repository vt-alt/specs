%define _unpackaged_files_terminate_build 1

%define oname setuptools_scm

Name: python-module-%oname
Version: 3.3.3
Release: alt3
Summary: The blessed package to manage your versions by scm tags
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/setuptools_scm/
Packager: Python Development Team <python at packages.altlinux.org>

# https://github.com/pypa/setuptools_scm.git
Source: %name-%version.tar
Patch1: %oname-2.1.0-alt-tests.patch

%py_provides setuptools-scm
Requires: git-core mercurial
%py_requires setuptools

%description
setuptools_scm is a simple utility for the setup_requires feature of
setuptools for use in Mercurial and Git based projects.

It uses metadata from the SCM to generate the version of a project and
is able to list the files belonging to that project (which makes the
MANIFEST.in file unnecessary in many cases).

It falls back to PKG-INFO/.hg_archival.txt when necessary.

%prep
%setup
%patch1 -p1

rm ./src/setuptools_scm/win_py31_compat.py

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python_build_debug

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python_install

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Fri Apr 24 2020 Stanislav Levin <slev@altlinux.org> 3.3.3-alt3
- Moved Python3 subpackage out to its own package.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 3.3.3-alt2
- Fixed testing against Pytest 5.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 3.3.3-alt1
- 2.1.0 -> 3.3.3.

* Fri Jun 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Updated to upstream version 2.1.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.15.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 01 2017 Michael Shigorin <mike@altlinux.org> 1.15.0-alt1.1
- R: git-core instead of full-blown git metapackage
- fix build --with python3 (actually the test)

* Mon Jan 02 2017 Anton Midyukov <antohami@altlinux.org> 1.15.0-alt1
- Version 1.15.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.0-alt1.git20150812.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt1.git20150812.1
- NMU: Use buildreq for BR.

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20150812
- Version 1.7.0

* Sun Jul 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20150723
- Version 1.6.0

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

