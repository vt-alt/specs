%define modname mallard-ducktype

Name: python3-module-%modname
Version: 1.0.2
Release: alt1

Summary: Parse Ducktype files and convert them to Mallard
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Source: https://github.com/projectmallard/%modname/archive/%version/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%description
Parse Ducktype files and convert them to Mallard.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%_bindir/ducktype
%python3_sitelibdir_noarch/*
%doc AUTHORS README.md COPYING


%changelog
* Tue Jul 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Apr 30 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Apr 10 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Thu Feb 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- first build for Sisyphus

