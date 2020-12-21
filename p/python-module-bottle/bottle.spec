%define oname bottle

%def_without python3

Name: python-module-%oname
Version: 0.13
Release: alt4
Summary: Fast and simple WSGI-framework for small web-applications
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bottle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/defnull/bottle.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

%description
Bottle is a fast and simple micro-framework for small web applications.
It offers request dispatching (Routes) with url parameter support,
templates, a built-in HTTP Server and adapters for many third party
WSGI/HTTP-server and template engines - all in a single file and with no
dependencies other than the Python Standard Library.

%package -n python3-module-%oname
Summary: Fast and simple WSGI-framework for small web-applications
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Bottle is a fast and simple micro-framework for small web applications.
It offers request dispatching (Routes) with url parameter support,
templates, a built-in HTTP Server and adapters for many third party
WSGI/HTTP-server and template engines - all in a single file and with no
dependencies other than the Python Standard Library.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Bottle is a fast and simple micro-framework for small web applications.
It offers request dispatching (Routes) with url parameter support,
templates, a built-in HTTP Server and adapters for many third party
WSGI/HTTP-server and template engines - all in a single file and with no
dependencies other than the Python Standard Library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Bottle is a fast and simple micro-framework for small web applications.
It offers request dispatching (Routes) with url parameter support,
templates, a built-in HTTP Server and adapters for many third party
WSGI/HTTP-server and template engines - all in a single file and with no
dependencies other than the Python Standard Library.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make docs
sphinx-build -b pickle -d build/docs/doctrees docs build/docs/pickle

install -d %buildroot%python_sitelibdir/%oname
cp -fR build/docs/pickle %buildroot%python_sitelibdir/%oname/

rm -fv %buildroot%_bindir/bottle.py

%files
%doc AUTHORS *.rst
#_bindir/bottle.py
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc build/docs/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt4
- drop /usr/bin/dir/bootle.py (ALT bug 38057)

* Fri Feb 07 2020 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt3
- build python2 only

* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.13-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt1.dev.git20141002.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.13-alt1.dev.git20141002.1
- NMU: Use buildreq for BR.

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.dev.git20141002
- Initial build for Sisyphus

