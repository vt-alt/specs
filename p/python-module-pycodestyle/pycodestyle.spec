%define _unpackaged_files_terminate_build 1
%define oname pycodestyle

Name: python-module-%oname
Version: 2.5.0
Release: alt2

Summary: Python style guide checker
Group: Development/Python
License: Expat
BuildArch: noarch
Url: https://pypi.org/project/pycodestyle/

# https://github.com/PyCQA/pycodestyle.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python

%if_with check
BuildRequires: python2.7(json)
%endif


%description
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8.

%prep
%setup

%build
%python_build

%install
%python_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python}
# tox.py3 --sitepackages -p auto -o -v

%files
%doc README.rst LICENSE CONTRIBUTING.rst CHANGES.txt
%_bindir/pycodestyle
%python_sitelibdir/pycodestyle.py*
%python_sitelibdir/pycodestyle-%version-py%_python_version.egg-info/


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.5.0-alt2
- Rebuild with new setuptools
- removal build for python3.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Fri Oct 26 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt1
- Initial build for ALT.
