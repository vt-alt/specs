%define _unpackaged_files_terminate_build 1
%define oname entrypoints

Name: python-module-%oname
Version: 0.3
Release: alt2
Summary: Discover and load entry points from installed packages
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/entrypoints

# https://github.com/takluyver/entrypoints.git
Source: %name-%version.tar

%py_requires configparser

%description
Discover and load entry points from installed packages.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check

%files
%python_sitelibdir/entrypoints.py*
%python_sitelibdir/entrypoints-%version-py%_python_version.egg-info/

%changelog
* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 0.3-alt2
- Built Python3 package from its ows src.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 0.3-alt1
- 0.2.3 -> 0.3.

* Wed Dec 19 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.2.3-alt2
- Added egg-info

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.3-alt1
- Initial build for ALT.
