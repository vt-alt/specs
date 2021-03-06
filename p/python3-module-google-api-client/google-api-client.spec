%define oname google-api-client

%def_with python3

Name: python3-module-%oname
Version: 2.12.0
Release: alt1
Summary: Google API Client Library for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/google-api-python-client/
Packager: Andrey Cherepanov <cas@altlinux.org>

# https://github.com/google/google-api-python-client.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-httplib2 >= 0.8
BuildRequires: python3-module-oauth2client >= 1.4.6
BuildRequires: python3-module-six >= 1.6.1
BuildRequires: python3-module-uritemplate >= 0.6

%add_python3_req_skip google.appengine.api

%description
The Google API Client for Python is a client library for accessing the
Plus, Moderator, and many other Google APIs.

%package docs
Summary: Documentation for Google API Client Library for Python
Group: Development/Documentation

%description docs
The Google API Client for Python is a client library for accessing the
Plus, Moderator, and many other Google APIs.

This package contains documentation for Google API Client Library for
Python.

%prep
%setup

%build
%python3_build

%install
%python3_install
rm -f docs/build

%files
%doc CHANGELOG.md README.md
%python3_sitelibdir/*

%files docs
%doc docs/*

%changelog
* Thu Jul 08 2021 Andrey Cherepanov <cas@altlinux.org> 2.12.0-alt1
- New version.

* Wed Jun 30 2021 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt1
- New version.

* Wed Jun 23 2021 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- New version.

* Tue Jun 15 2021 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version.

* Tue Jun 08 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- New version.

* Wed Jun 02 2021 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version.

* Wed May 26 2021 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version.

* Thu May 20 2021 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- New version.
- Build only module for python3.

* Thu May 13 2021 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Thu Apr 29 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Fri Apr 16 2021 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.

* Thu Apr 01 2021 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Mon Mar 08 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version.

* Thu Nov 19 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.8-alt1
- New version.

* Fri Oct 23 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.5-alt1
- New version.

* Wed Oct 21 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.4-alt1
- New version.

* Wed Sep 30 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.3-alt1
- New version.

* Fri Sep 25 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.2-alt1
- New version.

* Fri Sep 18 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.1-alt1
- New version.

* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 1.9.1-alt1
- New version.
- Fix License tag according to SPDX.

* Thu May 07 2020 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1
- New version.

* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version.

* Thu Mar 12 2020 Andrey Cherepanov <cas@altlinux.org> 1.7.12-alt1
- New version.

* Tue Aug 13 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.11-alt1
- New version.

* Sat Jul 27 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.10-alt1
- New version.

* Thu May 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.9-alt1
- New version.

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.8-alt1
- New version.

* Fri Dec 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.7-alt1
- New version.

* Sun Dec 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.6-alt1
- New version.

* Tue Dec 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1
- New version.

* Fri Jul 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt1
- New version.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.3-alt1
- New version.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- New version.

* Sun Apr 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.7-alt1
- New version.

* Thu Mar 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.6-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.5-alt1
- New version.

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt1.git20140913.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20140913
- Initial build for Sisyphus

