%define oname fiona

%def_disable check

Name: python3-module-%oname
Version: 1.8.17
Release: alt2
Summary: Fiona reads and writes spatial data files
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Fiona/

# https://github.com/Toblerity/Fiona.git
Source: %name-%version.tar

Patch: use_sphinx-apidoc-3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: libgdal-devel gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-module-Cython python3-module-pytest
BuildRequires: python3-module-sphinx

Conflicts: fio
Conflicts: python-module-fiona < %EVR
Obsoletes: python-module-fiona < %EVR
%py3_provides %oname
%py3_requires logging json cligj six click click_plugins

%description
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

This package contains documentation for %oname.

%prep
%setup
%patch -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

python3 setup.py build_ext -i
export PYTHONPATH=$PWD
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
python3 setup.py test

%files
%doc CHANGES.txt CREDITS.txt *.rst examples
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html docs/*.txt

%changelog
* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.17-alt2
- fix build

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 1.8.17-alt1
- Automatically updated to 1.8.17.

* Thu Mar 19 2020 Grigory Ustinov <grenka@altlinux.org> 1.8.13-alt1
- Build new version.
- Add conflict on python-module-fiona (Closes: #37383).

* Thu Oct 24 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.9-alt1
- Build new version.

* Mon Sep 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.8-alt1
- Build new version.

* Tue Mar 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.6-alt1
- Build new version.

* Tue Jan 15 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.4-alt1
- Build new version.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.9-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.9-alt1
- Updated to upstream version 1.7.9.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.0-alt1.git20150810.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1.git20150810.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20150810
- Version 1.6.0

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20150301
- New snapshot

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20150204
- Initial build for Sisyphus

