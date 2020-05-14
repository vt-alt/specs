%define oname setproctitle

Name: python3-module-%oname
Version: 1.1.10
Release: alt3

Summary: A library to allow customization of the process title
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/setproctitle/

# https://github.com/dvarrazzo/py-setproctitle.git
Source: %name-%version.tar
Patch0: fix-deprecation-warning.patch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3 python3-module-Cython-tests

%py3_provides %oname

%description
The library allows a process to change its title (as displayed by system
tools such as ps and top).

%prep
%setup
%patch0 -p1

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Tue May 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.10-alt3
- Deprecation warning fixed (Closes #38459).

* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.10-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.10-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 03 2017 Anton Midyukov <antohami@altlinux.org> 1.1.10-alt1
- New version 1.1.10
- Disable check

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.9-alt1.dev0.git20140903.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.dev0.git20140903
- Initial build for Sisyphus

