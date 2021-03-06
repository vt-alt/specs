%define _unpackaged_files_terminate_build 1
%define oname iniconfig

Name: python-module-%oname
Version: 1.0.0
Release: alt3

Summary: A small and simple INI-file parser
License: MIT
Group: Development/Tools
# Source-git: https://github.com/RonnyPfannschmidt/iniconfig.git
Url: https://pypi.org/project/iniconfig/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: python2.7(setuptools_scm)

BuildArch: noarch

%description
%summary

%prep
%setup
%patch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install

%check

%files
%doc CHANGELOG LICENSE README.txt
%python_sitelibdir/iniconfig.py*
%python_sitelibdir/iniconfig-%version-py%_python_version.egg-info/

%changelog
* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.0.0-alt3
- Built Python3 package from its ows src.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- Fixed testing against Pytest 5.

* Sat Mar 16 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build.

