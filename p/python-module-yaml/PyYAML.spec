%define project PyYAML

%def_with python3

Name: python-module-yaml
Version: 5.1.2
Release: alt1

Summary: PyYAML, a YAML parser and emitter for Python

License: MIT/X Consortium
Group: Development/Python
Url: https://github.com/yaml/pyyaml
#BuildArch: noarch

# Source-url: https://github.com/yaml/pyyaml/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.0.0

BuildRequires: python-devel libyaml-devel python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3 python3-module-Cython
BuildRequires: python3-devel
%endif

%description
YAML is a data serialization format designed for human readability
and interaction with scripting languages.

PyYAML is a YAML parser and emitter for the Python programming
language.  PyYAML features a complete YAML 1.1 parser, Unicode
support, and relatively sensible error messages.

%if_with python3
%package -n python3-module-yaml
Summary: PyYAML, a YAML parser and emitter for Python3
Group: Development/Python3

%description -n python3-module-yaml
YAML is a data serialization format designed for human readability
and interaction with scripting languages.

PyYAML is a YAML parser and emitter for the Python3 programming
language.  PyYAML features a complete YAML 1.1 parser, Unicode
support, and relatively sensible error messages.
%endif

%prep
%setup
%python3_dirsetup

%build
%add_optflags -fno-strict-aliasing

%python_build build_ext
%if_with python3
pushd ../python3
%python3_build build_ext
popd
%endif

%install
%python_install
%python3_dirinstall

%files
%doc CHANGES README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-yaml
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 05 2019 Grigory Ustinov <grenka@altlinux.org> 5.1.2-alt1
- Build new version.

* Wed Jul 10 2019 Grigory Ustinov <grenka@altlinux.org> 5.1.1-alt1
- Build new version.

* Tue Mar 19 2019 Grigory Ustinov <grenka@altlinux.org> 5.1-alt1
- Build new version.

* Tue Dec 25 2018 Grigory Ustinov <grenka@altlinux.org> 3.13-alt1
- Build new version.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.12-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Oct 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.12-alt1
- new version 3.12 (with rpmrb script) (ALT bug 34046)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.11-alt1.hg20141128.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11-alt1.hg20141128
- New snapshot

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11-alt1.hg20140326
- Version 3.11

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt2.hg20121224
- Snapshot from Mercurial

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.10-alt2.1
- Rebuild with Python-3.3

* Sat Apr 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt2
- Dont' rename _yaml.*.so -> _yaml.so

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt1
- Version 3.10
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.05-alt2.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.05-alt2.1
- Rebuilt with python 2.6

* Sun Jul 20 2008 Alexander Myltsev <avm@altlinux.ru> 3.05-alt2
- Fix #16285 (package lost directory).
- Pull a minor bugfix from SVN (a single dot is not a valid float).

* Fri Nov 16 2007 Alex V. Myltsev <avm@altlinux.ru> 3.05-alt1
- Initial build for Sisyphus.

