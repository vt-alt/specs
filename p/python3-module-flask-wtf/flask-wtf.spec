%define oname flask-wtf

Name: python3-module-%oname
Version: 0.14.2
Release: alt2

Summary: Simple integration of Flask and WTForms
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-WTF/
BuildArch: noarch

# https://github.com/lepture/flask-wtf.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch
Patch2: %oname-%version-upstream-sphinx.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-flask
BuildRequires: python3-module-werkzeug python3-module-wtforms
BuildRequires: python3-module-flask-babel python3-module-speaklater
BuildRequires: flask-sphinx-themes python3-module-sphinx

%py3_provides flask_wtf


%description
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

This package comtains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

This package comtains documentation for %oname.

%prep
%setup
%patch1 -p1
%patch2 -p1

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

PYTHONPATH=$(pwd) %make -C docs pickle
PYTHONPATH=$(pwd) %make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
py.test3 ||:

%files
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.14.2-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.14.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.2-alt1
- Updated to upstream version 0.14.2.

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20141005
- Initial build for Sisyphus

