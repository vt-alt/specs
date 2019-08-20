%define  modulename cheroot
%def_with python3

Name:    python-module-%modulename
Version: 6.5.6
Release: alt1

Summary: Cheroot is the high-performance, pure-Python HTTP server used by CherryPy
License: BSD
Group:   Development/Python
URL:     https://github.com/cherrypy/cheroot

Source:  %modulename-%version.tar
Patch:   alt-fix-requires.patch

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-setuptools_scm
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools_scm
%endif

BuildArch: noarch

%py_requires backports.functools_lru_cache

%description
Cheroot is the high-performance, pure-Python HTTP server used by CherryPy.

%if_with python3
%package -n python3-module-%modulename
Summary: Cheroot is the high-performance, pure-Python HTTP server used by CherryPy
Group: Development/Python3

%description -n python3-module-%modulename
Cheroot is the high-performance, pure-Python HTTP server used by CherryPy.
%endif

%prep
%setup -n %modulename-%version
%patch -p1
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%_bindir/cheroot
%python3_sitelibdir/%{modulename}*
%endif

%changelog
* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 6.5.6-alt1
- New version.

* Tue Apr 30 2019 Andrey Cherepanov <cas@altlinux.org> 6.5.5-alt1
- New version.

* Thu Jan 03 2019 Andrey Cherepanov <cas@altlinux.org> 6.5.4-alt1
- New version.

* Fri Dec 28 2018 Andrey Cherepanov <cas@altlinux.org> 6.5.3-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 6.5.2-alt1
- New version.

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 6.4.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 6.3.3-alt1
- New version.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 6.3.2-alt1
- New version.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 6.3.1-alt2
- Require module instead of package.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 6.3.1-alt1
- Initial build for Sisyphus
