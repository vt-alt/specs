%define oname pytest-repeat
%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-%oname
Version: 0.9.1
Release: alt1
Summary: pytest plugin for repeating tests
License: MPL-2.0 
Group: Development/Python3
Url: https://pypi.org/project/pytest-repeat/
Source: %name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)
%py3_provides %oname

%if_with check
BuildRequires: python3(tox)
%endif

%description 
pytest-repeat is a plugin for py.test that makes it easy
to repeat a single test, or multiple tests, a specific number of times.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
sed -i '/isolated_build/s/true/false/' tox.ini
sed -i '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
export PIP_NO_INDEX=YES
export PIP_NO_BUILD_ISOLATION=no
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files 
%doc CHANGES.rst  LICENSE README.rst
%python3_sitelibdir/pytest_repeat.py*
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/pytest_repeat-%version-py%_python3_version.egg-info/

%changelog
* Wed Mar 31 2021 Mikhail Chernonog <snowmix@altlinux.org> 0.9.1-alt1
- 0.8.0 -> 0.9.1
- Fixed testing

* Thu Mar 07 2019 Mikhail Chernonog <snowmix@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus
