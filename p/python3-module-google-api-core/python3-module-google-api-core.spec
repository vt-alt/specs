Name:    python3-module-google-api-core
Version: 1.31.0
Release: alt1

Summary: Core Library for Google Client Libraries
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/googleapis/python-api-core

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  python-api-core-%version.tar

%description
%summary

This library is not meant to stand-alone. Instead it defines common
helpers used by all Google API clients. For more information, see the
documentation at https://googleapis.dev/python/google-api-core/latest.

%prep
%setup -n python-api-core-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/google/api_core
%python3_sitelibdir/*-nspkg.pth
%python3_sitelibdir/*.egg-info

%changelog
* Sat Jul 10 2021 Andrey Cherepanov <cas@altlinux.org> 1.31.0-alt1
- New version.

* Wed Jun 09 2021 Andrey Cherepanov <cas@altlinux.org> 1.30.0-alt1
- New version.

* Thu Jun 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.29.0-alt1
- New version.

* Fri May 21 2021 Andrey Cherepanov <cas@altlinux.org> 1.28.0-alt1
- New version.

* Tue May 18 2021 Andrey Cherepanov <cas@altlinux.org> 1.27.0-alt1
- New version.

* Tue Mar 30 2021 Andrey Cherepanov <cas@altlinux.org> 1.26.3-alt1
- New version.

* Wed Mar 24 2021 Andrey Cherepanov <cas@altlinux.org> 1.26.2-alt1
- New version.

* Mon Mar 08 2021 Andrey Cherepanov <cas@altlinux.org> 1.26.1-alt1
- New version.

* Thu Feb 11 2021 Andrey Cherepanov <cas@altlinux.org> 1.26.0-alt1
- New version.

* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- Initial build for Sisyphus
