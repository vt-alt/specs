%define  modulename CommonMark

Name:    python3-module-commonmark
Version: 0.9.1
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
rm -f %buildroot%_bindir/cmark

%files
%doc README.rst LICENSE spec.txt docs
%python3_sitelibdir/commonmark/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Feb 11 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- Initial version in Sisyphus.
