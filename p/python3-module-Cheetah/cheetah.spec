%define origname Cheetah

Summary: Template engine and code-generator
Name: python3-module-%origname
Version: 3.2.3
Release: alt3
Source0: Cheetah-%version.tar
License: MIT
Group: Development/Python3
URL: http://cheetahtemplate.org/
# https://github.com/CheetahTemplate3/cheetah3
#BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: time
BuildPreReq: python3-module-distribute
BuildPreReq: python3-module-markdown
BuildPreReq: python3-module-sphinx

Conflicts: python-module-Cheetah < %EVR
Obsoletes: python-module-Cheetah < %EVR

%description
Cheetah is an open source template engine and code generation tool, written
in Python. It can be used standalone or combined with other tools and
frameworks. Web development is its principle use, but Cheetah is very
flexible and is also being used to generate C++ game code, Java, sql,
form emails and even Python code.

%package tests
Summary: Tests for Cheetah, template engine and code-generator
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Cheetah is an open source template engine and code generation tool, written
in Python. It can be used standalone or combined with other tools and
frameworks. Web development is its principle use, but Cheetah is very
flexible and is also being used to generate C++ game code, Java, sql,
form emails and even Python code.

This package contains tests for Cheetah.

%prep
%setup -n Cheetah-%version

%build
%python3_build

export PYTHONPATH=$PWD
%make SPHINXBUILD="sphinx-build-3" -C docs html
mkdir man
cp -fR docs/_build/html/* man/

%install
%python3_install

%files
%doc *.rst man/
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/Cheetah/Tests

%files tests
%python3_sitelibdir/Cheetah/Tests
%exclude %python3_sitelibdir/Cheetah/Tests/Performance.py*
%changelog
* Wed May 26 2021 Grigory Ustinov <grenka@altlinux.org> 3.2.3-alt3
- Drop python2 support.

* Tue Sep 3 2019 Vladimir Didenko <cow@altlinux.org> 3.2.3-alt2
- Don't use 2to3 conversion because it breaks python3 package

* Tue Sep 3 2019 Vladimir Didenko <cow@altlinux.org> 3.2.3-alt1
- Version 3.2.3

* Tue Mar 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.1.0-alt1
- Version 3.1.0-alt1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.4-alt2.git20121217.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.4-alt2.git20121217.1
- NMU: Use buildreq for BR.

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt2.git20121217
- Snapshot from git

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.4-alt1.1
- Rebuild with Python-3.3

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt1
- Version 2.4.4
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt2.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt2
- Rebuilt for debuginfo

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1
- Version 2.4.3
- Extracted tests into separate package

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.1
- Rebuilt with python 2.6

* Wed Jul 29 2009 Mikhail Pokidko <pma@altlinux.org> 2.2.1-alt1
- Version up

* Sat Apr 05 2008 Mikhail Pokidko <pma@altlinux.org> 2.0.1-alt1
- Initial ALT build
