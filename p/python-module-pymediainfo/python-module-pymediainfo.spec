%define modname pymediainfo
%def_without python2

Name: python-module-%modname
Version: 4.1
Release: alt1

Summary: A Python wrapper for the mediainfo library
Group: Development/Python
License: MIT
Url: https://pypi.python.org/pypi/%modname
Source: https://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildArch: noarch

Requires: libmediainfo

%{?_with_python2:
BuildRequires: python-devel
BuildRequires: python-module-setuptools_scm}

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-setuptools_scm

%description
This Python module provides a wrapper around the MediaInfo library.

%package -n python3-module-%modname
Summary: A Python3 wrapper for the mediainfo library
Group: Development/Python3
Requires: libmediainfo

%description -n python3-module-%modname
This Python3 module provides a wrapper around the MediaInfo library.

%prep
%setup -n %modname-%version -a0
%{?_with_python2:cp -a %modname-%version py2build}

%build
%python3_build

%if_with python2
pushd py2bbuild
%python_build
popd
%endif

%install
%python3_install

%if_with python2
pushd py2build
%python_install
popd
%endif

%if_with python2
%files
%python_sitelibdir_noarch/%modname/
%doc README.rst
%python_sitelibdir_noarch/*.egg-info
%endif

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%doc README.rst
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt1
- 4.1
- disabled python2 module

* Sat Apr 06 2019 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- 4.0

* Wed Mar 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1

* Sat Nov 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0

* Wed May 16 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Mar 03 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Wed Nov 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt1
- first build for Sisyphus


