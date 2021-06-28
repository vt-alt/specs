%define  modulename pypi-search

Name:    python3-module-%modulename
Version: 1.2.0
Release: alt1

Summary: Get Information on Python Packages From PyPI
License: MIT
Group:   Development/Python3
URL:     https://github.com/asadmoosvi/pypi-search

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
pypi-search allows you to quickly query packages on PyPI. It fetches the
following information:
* Version Information
* Project Links
* Github Stats if any
* Meta Information (author, maintainer)
* Description

It quickly allows you to know what a package is all about without having to
open up the PyPI website.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%_bindir/pypisearch
%python3_sitelibdir/pypi_search
%python3_sitelibdir/*.egg-info

%changelog
* Thu Jun 10 2021 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
