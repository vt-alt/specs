%define _unpackaged_files_terminate_build 1

%def_with check

Name: yamllint
Version: 1.24.2
Release: alt1
Summary: A linter for YAML files
Group: Development/Python
License: GPLv3
Url: https://github.com/adrienverge/yamllint
Source0: https://pypi.python.org/packages/source/y/%name/%name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx-sphinx-build-symlink

%if_with check
BuildRequires: /dev/pts
BuildRequires: python3(pathspec)
BuildRequires: python3(tox)
BuildRequires: python3(yaml)
%endif

%description
A linter for YAML files.

yamllint does not only check for syntax validity, but for weirdnesses like key
repetition and cosmetic problems such as lines length, trailing spaces,
indentation, etc.

%prep
%setup

%build
%python3_build
pushd docs
make man
popd

%install
%python3_install
install -D -m0644 docs/_build/man/%name.1 %buildroot/%_man1dir/%name.1

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m unittest discover -vv tests {posargs}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
export TOX_TESTENV_PASSENV='HOME'
tox.py3 --sitepackages -vvr

%files
%doc README.rst CHANGELOG.rst
%_man1dir/%name.1.*

%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-*

%changelog
* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 1.24.2-alt1
- 1.17.0 -> 1.24.2.

* Fri Sep 20 2019 Terechkov Evgenii <evg@altlinux.org> 1.17.0-alt1
- Initial build for ALT Linux Sisyphus
