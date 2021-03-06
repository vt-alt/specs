%define modname pymeeus
%define _name PyMeeus
%def_enable python2
%def_enable check

Name: python-module-%modname
Version: 0.5.11
Release: alt1

Summary: Library of astronomical algorithms in Python
Group: Development/Python
License: GPL-3.0 and LGPL-3.0
Url: https://pypi.python.org/pypi/%_name

Source: https://pypi.io/packages/source/P/%_name/%_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%{?_enable_check:BuildRequires: python3-module-pytest}

%if_enabled python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
%{?_enable_check:BuildRequires: python-module-pytest}
%endif

%description
PyMeeus is a Python implementation of the astronomical algorithms described
in the classical book 
"Astronomical Algorithms, 2nd Edition, Willmann-Bell Inc. (1998)" by Jean Meeus.

%package -n python3-module-%modname
Summary: Library of astronomical algorithms in Python3
Group: Development/Python3

%description -n python3-module-%modname
PyMeeus is a Python implementation of the astronomical algorithms described
in the classical book 
"Astronomical Algorithms, 2nd Edition, Willmann-Bell Inc. (1998)" by Jean Meeus.

%prep
%setup -n %_name-%version %{?_enable_python2:-a0
mv %_name-%version py2build}

%build
%python3_build

%if_enabled python2
pushd py2build
%python_build
popd
%endif

%install
%python3_install

%if_enabled python2
pushd py2build
%python_install
popd
%endif

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir_noarch
py.test3 tests

%if_enabled python2
pushd py2build
export PYTHONPATH=%buildroot/%python_sitelibdir_noarch
py.test tests
popd
%endif


%if_enabled python2
%files
%python_sitelibdir_noarch/%modname/
%doc *.rst
%python_sitelibdir_noarch/*.egg-info
%endif

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%doc *.rst
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Wed Apr 14 2021 Yuri N. Sedunov <aris@altlinux.org> 0.5.11-alt1
- 0.5.11

* Sun Feb 21 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.13-alt1
- 0.3.13
- enabled %%check

* Thu Apr 02 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7
- fixed License tag

* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- first build for Sisyphus



