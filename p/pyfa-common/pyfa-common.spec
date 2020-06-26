Name: pyfa-common
Version: 0.8.0
Release: alt4.2

Summary: Common files for Python fitting assistant

Packager: Alexey Borovskoy <alb@altlinux.org>

License: %gpl3plus
Group: Games/Other 
BuildArch: noarch
Url: http://pyfa.sourceforge.net/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: python-module-setuptools
#BuildRequires: python-module-pygtk-libglade
BuildRequires: python-modules-sqlite3

Provides: pyfa = 0.4.2
Obsoletes: pyfa <= 0.4.2

%add_python_compile_include %_datadir/pyfa/model

#Костыль. Need fix.
%add_python_req_skip launch

%description
pyfa is the Python Fitting Assistant, a standalone application to create
fittings for the EVE-Online SciFi MMORPG.
The layout of pyfa heavily based on EFT, the EVE fitting tool. Although
it is a complete rewrite and replacement for EFT, the fittings are still
compatible with EFT

This package contains common files and libraries for pyfa-gtk and pyfa-web.

%prep
%setup -q

%build

%install

mkdir -p %buildroot%_datadir/pyfa/model
cp -r {effects,overrides,util,fitting,updater} %buildroot%_datadir/pyfa/model
cp *.py %buildroot%_datadir/pyfa/model

%files
%dir %_datadir/pyfa
%_datadir/pyfa/model

%changelog
* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt4.2
- NMU: fix provides

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt4.1
- Rebuild with Python-2.7

* Tue Mar 16 2010 Alexey Borovskoy <alb@altlinux.ru> 0.8.0-alt4
- Git version, commit 1f24113d0843286f4f2c360e99739cd6fc98f5ca

* Sun Mar 07 2010 Alexey Borovskoy <alb@altlinux.ru> 0.8.0-alt3
- Git version, commit f3a81f15c529287b37bd983a533d4ea1943b96eb

* Sun Feb 21 2010 Alexey Borovskoy <alb@altlinux.ru> 0.8.0-alt2
- Git version, commit 5f0738c83b904d21a92ad145745f9b5104da441b

* Thu Feb 04 2010 Alexey Borovskoy <alb@altlinux.ru> 0.8.0-alt1
- 0.8.0
- Git version, commit ad24a046fda9a749f5b6cfded5e8a511549a44f1

* Sat Jan 16 2010 Alexey Borovskoy <alb@altlinux.ru> 0.7.0-alt2
- Git version, commit 70f6f5b084032ddda15c7a99289e2cf91738ed49

* Thu Dec 31 2009 Alexey Borovskoy <alb@altlinux.ru> 0.7.0-alt1
- 0.7.0
- Git version, commit 2fcbc90c5abb31552aa9b183c2ee713d5325a742

* Mon Dec 21 2009 Alexey Borovskoy <alb@altlinux.ru> 0.6.1-alt1
- 0.6.1
- Git version, commit b51371caeb303cf13f5ad18ac86acc00eb62b22b

* Tue Dec 01 2009 Alexey Borovskoy <alb@altlinux.ru> 0.6.0-alt1
- 0.6.0
- Dominion support
- Git version, commit e3b8671cefcbbd027a89752b638e8fcf26eed116

* Mon Nov 30 2009 Alexey Borovskoy <alb@altlinux.ru> 0.5.1-alt2
- Git version, commit dd5acf6b2fd8ac9d54612c9c1e27b4dc9f48853d

* Tue Nov 24 2009 Alexey Borovskoy <alb@altlinux.ru> 0.5.1-alt1
- New version 0.5.1

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.1
- Rebuilt with python 2.6

* Tue Nov 17 2009 Alexey Borovskoy <alb@altlinux.ru> 0.5.0-alt2
- Git version, commit 7afb6defbb695dd64e5343f3250e78109cc43e82

* Mon Nov 16 2009 Alexey Borovskoy <alb@altlinux.ru> 0.5.0-alt1
- Git version, commit 17ac33ed51ceb1267a08ed74dbcb0711a887fedf

* Sun Nov 15 2009 Alexey Borovskoy <alb@altlinux.ru> 0.4.2-alt2
- Git version, commit 5ba9cb58f1e4b03243643f7af80d88b11b0ecc24

* Sat Nov 14 2009 Alexey Borovskoy <alb@altlinux.ru> 0.4.2-alt1
- Pyfa was splitted into three subprojects.
