Name:           python3-module-xlrd
Version:        2.0.1
Release:        alt2.1
Summary:        Library to extract data from Microsoft Excel (TM) spreadsheet files

Group:          Development/Python3
License:        BSD
URL:            http://www.python-excel.org/
Source0:        xlrd-%version.tar
# VCS:		https://github.com/python-excel/xlrd

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

Provides:	python3-xlrd = %version-%release
# Conflict over /usr/bin/runxlrd
Provides: 	python-module-xlrd = %EVR
Obsoletes: 	python-module-xlrd < %EVR

%description
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0
onwards) on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strong
support for Excel dates.  Unicode-aware.

%prep
%setup -q -n xlrd-%{version}

%build
export PYTHONPATH=`pwd`:$PYTHONPATH
make SPHINXBUILD="sphinx-build-3" -C docs man
%python3_build

%install
%python3_install
install -Dm0644 docs/_build/man/xlrd.1 %buildroot%_man1dir/xlrd.1

# add shebang and remove .py extension
subst 's|^#!.*|#!%__python3|' %buildroot%_bindir/runxlrd.py
mv %buildroot%_bindir/runxlrd{.py,}

%files
%doc README.rst
%_bindir/runxlrd
%python3_sitelibdir/xlrd/*
%python3_sitelibdir/*egg-info
%_man1dir/xlrd.1*

%changelog
* Thu Jun 10 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt2.1
- Conflict over /usr/bin/runxlrd.

* Wed Jun 02 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt2
- Drop python2 support.

* Fri Dec 11 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version.

* Sun Dec 16 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.
- Do not generate html documentation.

* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version
- Generate and package documentation amn man page

* Tue Jun 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Mon Mar 31 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt2
- Increase release to prevent Fedoraimport/Sisyphus warning

* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- Import package to ALT Linux from Fedora

