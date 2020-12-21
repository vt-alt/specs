%define oname bottle

Name: python3-module-%oname
Version: 0.12.18
Release: alt2
Epoch: 1

Summary: Fast and simple WSGI-framework for small web-applications

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/bottle/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

BuildRequires(pre): rpm-build-python3 rpm-build-intro
#BuildRequires: rpm-macros-sphinx3

%py3_provides %oname

%description
Bottle is a fast and simple micro-framework for small web applications.
It offers request dispatching (Routes) with url parameter support,
templates, a built-in HTTP Server and adapters for many third party
WSGI/HTTP-server and template engines - all in a single file and with no
dependencies other than the Python Standard Library.

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

#prepare_sphinx3 .
#ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.rst
%_bindir/bottle.py
%python3_sitelibdir/*


%changelog
* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1:0.12.18-alt2
- add conflicts/obsoletes against python-module-bottle (due bindir/bottle.py)

* Thu Feb 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1:0.12.18-alt1
- build python3 module from scratch repo
- revert to stable 0.12.x release

* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.13-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt1.dev.git20141002.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.13-alt1.dev.git20141002.1
- NMU: Use buildreq for BR.

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.dev.git20141002
- Initial build for Sisyphus

