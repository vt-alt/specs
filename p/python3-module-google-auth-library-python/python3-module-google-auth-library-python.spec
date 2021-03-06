%define  modulename google-auth-library-python

Name:    python3-module-%modulename
Version: 1.32.1
Release: alt1

Summary: Google Auth Python Library
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/googleapis/google-auth-library-python

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%add_python3_req_skip requests.packages.urllib3.util.ssl_

%description
This library simplifies using Google's various server-to-server authentication
mechanisms to access Google APIs.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%doc *.md

%changelog
* Thu Jul 01 2021 Andrey Cherepanov <cas@altlinux.org> 1.32.1-alt1
- New version.

* Tue Jun 22 2021 Andrey Cherepanov <cas@altlinux.org> 1.32.0-alt1
- New version.

* Fri Jun 11 2021 Andrey Cherepanov <cas@altlinux.org> 1.31.0-alt1
- New version.

* Wed Jun 09 2021 Andrey Cherepanov <cas@altlinux.org> 1.30.2-alt1
- New version.

* Thu May 27 2021 Andrey Cherepanov <cas@altlinux.org> 1.30.1-alt1
- New version.

* Sat Apr 27 2019 Anton Midyukov <antohami@altlinux.org> 1.6.3-alt1
- Initial build for Sisyphus
