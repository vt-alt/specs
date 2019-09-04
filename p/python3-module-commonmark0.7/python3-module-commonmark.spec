%define  modulename CommonMark

Name:    python3-module-commonmark0.7
Version: 0.7.2
Release: alt1

Summary: Python parser for the CommonMark Markdown spec
License: BSD
Group:   Development/Python3
URL:     https://github.com/rtfd/CommonMark-py

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

Conflicts: python3-module-commonmark

%description
Python parser for the CommonMark Markdown spec.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE spec.txt docs
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Wed Jun 26 2019 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus.
