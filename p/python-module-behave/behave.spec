%define _unpackaged_files_terminate_build 1
%define oname behave

%def_with check
%def_with docs

Name: python-module-%oname
Version: 1.2.6
Release: alt2
Summary: behave is behaviour-driven development, Python style
License: BSD
Group: Development/Python
Url: https://pypi.org/project/behave/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/behave/behave.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python2.7(parse)
BuildRequires: python2.7(parse_type)
BuildRequires: python2.7(sphinx_bootstrap_theme)
BuildRequires: python2.7(traceback2)
%endif

%if_with check
BuildRequires: python2.7(hamcrest)
BuildRequires: python2.7(mock)
BuildRequires: python2.7(nose)
BuildRequires: python2.7(path.py)
BuildRequires: python2.7(pytest)
BuildRequires: python3(hamcrest)
BuildRequires: python3(mock)
BuildRequires: python3(nose)
BuildRequires: python3(parse)
BuildRequires: python3(parse_type)
BuildRequires: python3(path.py)
BuildRequires: python3(tox)
%endif

Requires: %oname-common = %EVR
%py_requires traceback2
%add_python_req_skip gherkin

%description
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

%package -n %oname-common
Summary: Common files for Python 2 & 3 modules
Group: Development/Python

%description -n %oname-common
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

This package contains common files for Python 2 & 3 modules.

%package -n python3-module-%oname
Summary: behave is behaviour-driven development, Python style
Group: Development/Python3
Requires: %oname-common = %EVR
%add_python3_req_skip gherkin
%add_python3_req_skip gherkin.formatter
%add_python3_req_skip gherkin.tag_expression

%description -n python3-module-%oname
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

This package contains documentation for %oname.
%endif

%prep
%setup
%patch -p1

rm -rf ../python3
cp -fR . ../python3

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build

%if_with docs
%make -C docs pickle
%make -C docs html
%endif

%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%python_install

install -d %buildroot%_sysconfdir
cp -fR etc/* %buildroot%_sysconfdir/

%if_with docs
cp -fR build/docs/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
sed -i -e '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/py.test\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' \
-e '/behave --format=/d' \
tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
%_bindir/tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst *features
%_bindir/behave
%python_sitelibdir/behave/
%python_sitelibdir/setuptools_behave.py*
%python_sitelibdir/behave-%version-py%_python_version.egg-info/
%if_with docs
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc build/docs/html/*
%endif

%files -n %oname-common
%dir %_sysconfdir/json
%_sysconfdir/json/behave.json-schema
%dir %_sysconfdir/junit.xml
%_sysconfdir/junit.xml/behave_junit.xsd
%_sysconfdir/junit.xml/junit-4.xsd

%files -n python3-module-%oname
%doc *.rst *features
%_bindir/behave.py3
%python3_sitelibdir/behave/
%python3_sitelibdir/setuptools_behave.py
%python3_sitelibdir/__pycache__/setuptools_behave.cpython-*.py*
%python3_sitelibdir/behave-%version-py%_python3_version.egg-info/

%changelog
* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.2.6-alt2
- Added missing dep on Pytest.

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 1.2.6-alt1
- 1.2.5 -> 1.2.6.
- Dropped BR on python argparse.

* Sat Feb 03 2018 Stanislav Levin <slev@altlinux.org> 1.2.5-alt1.a1.git20141018.1.1.1
- (NMU) Fix Requires to gherkin

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.5-alt1.a1.git20141018.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.5-alt1.a1.git20141018.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1.a1.git20141018
- Initial build for Sisyphus

