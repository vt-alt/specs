%define oname html2text
Name: python3-module-html2text
Version: 2020.1.16
Release: alt1

Summary: Converts a page of HTML into clean, easy-to-read plain ASCII text

Group: Development/Python
License: GPLv3+
Url: http://www.aaronsw.com/2002/html2text/

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires: python3-module-pytest
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro

#Conflicts: python-module-html2text

%description
html2text is a Python script that convers a page of HTML into clean,
easy-to-read plain ASCII text.  Better yet, that ASCII also happens to
be valid Markdown (a text-to-HTML format).

%prep
%setup

%build
%python3_build

%install
%python3_install

mv %buildroot%_bindir/html2text %buildroot%_bindir/html2text.py3

%check
#export PYTHONPATH=%buildroot%python3_sitelibdir
#python3_test
# TODO:
#tox.py3

%files
%_bindir/html2text.py3
%python3_sitelibdir/*

%changelog
* Sat Mar 21 2020 Vitaly Lipatov <lav@altlinux.ru> 2020.1.16-alt1
- new version 2020.1.16 (with rpmrb script) (ALT bug 37305)

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 2016.9.19-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2014.4.5-alt1.git20140524.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 2014.4.5-alt1.git20140524.1
- NMU: Use buildreq for BR.

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.4.5-alt1.git20140524
- Add initial build for Sisyphus

