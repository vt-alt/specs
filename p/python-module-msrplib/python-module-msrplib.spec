%define  modulename msrplib

Name:    python-module-%modulename
Version: 0.20.0
Release: alt1

Summary: MSRP (RFC4975) client library
License: LGPLv2+
Group:   Development/Python
URL:     https://github.com/AGProjects/python-msrplib

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  python-%modulename-%version.tar

%description
This library implements Message Session Relay Protocol (MSRP). MSRP is
defined in RFC 4975.  The relay extension that can be used for NAT
traversal purposes is defined in RFC 4976.

%prep
%setup -n python-%modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.2-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.1-alt1
- Initial build for Sisyphus
