%define oname recommonmark

Name: python3-module-%oname
Version: 0.6.0
Release: alt1.2

Summary: A markdown parser for docutils
License: MIT
Group: Development/Python3
Url: https://github.com/rtfd/recommonmark
BuildArch: noarch

Packager: L.A. Kostis <lakostis@altlinux.ru>

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
Conflicts: python-module-recommonmark

%description
A docutils-compatibility bridge to CommonMark.
This allows you to write CommonMark inside of Docutils & Sphinx projects.

%prep
%setup

%build
%python3_build

%install
%python3_install --optimize=2

%files
%doc README.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue May 19 2020 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1.2
- NMU: conflicts with python-module-recommonmark due to executables.

* Tue Feb 11 2020 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1.1
- NMU: rebuild with python3-module-commonmark.

* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.0-alt1
- Version updated to 0.6.0
- porting on python3.

* Mon Feb 04 2019 L.A. Kostis <lakostis@altlinux.ru> 0.5.0-alt0.1
- Initial build for ALTLinux.

