%define _unpackaged_files_terminate_build 1

%define  modulename socks
%define  oname PySocks

Name:    python3-module-%modulename
Version: 1.7.1
Release: alt2

Summary: A SOCKS proxy client and wrapper for Python.
License: BSD
Group:   Development/Python
URL:     https://github.com/Anorov/PySocks

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
%summary

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/socks*
%python3_sitelibdir/__pycache__/socks*
%python3_sitelibdir/*.egg-info

%changelog
* Mon Dec 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.1-alt2
- Built version for python-3.

* Sat Oct 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- New version.

* Sun May 12 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- New version.

* Sun Dec 24 2017 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- New version.

* Thu Sep 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.6.7-alt1
- Initial build for Sisyphus
