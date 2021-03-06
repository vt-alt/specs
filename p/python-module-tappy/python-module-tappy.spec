%define modname tap.py

Name: python-module-tappy
Version: 2.6.2
Release: alt2

Summary: Test Anything Protocol (TAP) tools
Group: Development/Python
License: BSD-2-Clause
Url: http://pypi.python.org/pypi/%modname

# VCS: https://github.com/python-tap/tappy
Source: http://pypi.io/packages/source/t/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools python-module-babel

%description
tappy python module provides a set of tools for working with the Test
Anything Protocol (TAP), a line based test protocol for recording test
data in a standard way.

%prep
%setup -n %modname-%version

%build
%python_build

%install
%python_install
for f in %buildroot%_bindir/*; do mv "$f" "$f"-2; done

%files
%_bindir/tap-2
%_bindir/tappy-2
%python_sitelibdir_noarch/tap/
%python_sitelibdir_noarch/*.egg-info
%doc README.md


%changelog
* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt2
- removed python3 support (the last version supporting Python 2.7 is 2.6.x)
- fixed License tag

* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2
- made python2 build optional

* Mon Oct 01 2018 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- 2.5

* Wed Jun 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4-alt1
- 2.4

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- first build for Sisyphus



