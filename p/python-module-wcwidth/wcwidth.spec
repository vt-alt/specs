%define _unpackaged_files_terminate_build 1
%define oname wcwidth

Name: python-module-%oname
Version: 0.1.9
Release: alt2
Summary: Measures number of Terminal column cells of wide-character codes
License: MIT
Group: Development/Python
Url: https://pypi.org/project/wcwidth/

# https://github.com/jquast/wcwidth.git
Source: %name-%version.tar
BuildArch: noarch

%description
This API is mainly for Terminal Emulator implementors - any python
program that attempts to determine the printable width of a string on a
Terminal. It is implemented in python (no C library calls) and has no
3rd-party dependencies.

%prep
%setup

%build
%python_build_debug

%install
%python_install
rm -r %buildroot%python_sitelibdir/%oname/tests

%check

%files
%doc README.rst LICENSE.txt
%python_sitelibdir/%oname-%version-py%_python_version.egg-info/
%python_sitelibdir/%oname/

%changelog
* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 0.1.9-alt2
- Built Python3 package from its ows src.

* Thu May 07 2020 Stanislav Levin <slev@altlinux.org> 0.1.9-alt1
- 0.1.7 -> 0.1.9.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.7-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt2
- Fixed tests.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt1
- Updated to upstream version 0.1.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150413.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150413
- New snapshot

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150125
- Initial build for Sisyphus

