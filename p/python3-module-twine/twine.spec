%define oname twine

%def_disable check

Name: python3-module-%oname
Version: 1.9.1
Release: alt2

Summary: Collection of utilities for interacting with PyPI
License: ASL
Group: Development/Python3
Url: https://pypi.python.org/pypi/twine/
BuildArch: noarch

# https://github.com/pypa/twine.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-chardet python3-module-nose
BuildRequires: python3-module-pkginfo python3-module-pytest
BuildRequires: python3-module-urllib3

%py3_provides %oname


%description
Twine is a utility for interacting with PyPI.

Currently it only supports uploading distributions.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

find . -name '*.py' -type f -print0 | xargs -0 sed -i \
    -e 's:from requests\.packages\.:from :g'

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
%__python3 setup.py test
py.test3

%files
%doc AUTHORS *.rst docs/*.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Wed Dec 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9.1-alt2
- build for python2 disabled

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.1-alt1
- Updated to upstream releases 1.9.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt2.git20140815.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 1.3.1-alt2.git20140815
- cleanup buildreqs
- disable check

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140815
- Initial build for Sisyphus

