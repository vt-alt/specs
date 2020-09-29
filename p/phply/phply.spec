Name: phply
Version: 1.2.5
Release: alt2

Summary: Lexer and parser for PHP source implemented using PLY

License: BSD
Group: Development/Python
Url: https://github.com/viraptor/phply

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools python-module-ply
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-ply

Requires: python3-module-%name = %version-%release

%setup_python_module %name

%description
phply is a parser for the PHP programming language written using PLY, a Lex/YACC-style parser generator toolkit for Python.

%package -n python-module-%name
Summary: Lexer and parser for PHP source implemented using PLY
Group: Development/Python
# Module uses *-nspkg.pth to add module available for import
# but rpm doesn't detect it.
Provides: python2.7(phply)

%description -n python-module-%name
Python 2 module for phply. phply is a parser for the PHP programming language written using PLY, a Lex/YACC-style parser generator toolkit for Python.

%package -n python3-module-%name
Summary: Lexer and parser for PHP source implemented using PLY
Group: Development/Python3
%py3_provides phply.phpast
%py3_provides phply.phplex
%py3_provides phply.phpparse

%description -n python3-module-%name
Python 3 module for phply. phply is a parser for the PHP programming language written using PLY, a Lex/YACC-style parser generator toolkit for Python.


%prep
%setup -n %name-%version

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.md
%_bindir/phplex
%_bindir/phpparse

%files -n python-module-%name
%exclude %python_sitelibdir/tests
%python_sitelibdir/*-nspkg.pth
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info

%files -n python3-module-%name
%exclude %python3_sitelibdir/tests
%python3_sitelibdir/*-nspkg.pth
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-*

%changelog
* Mon Sep 23 2019 Anton Farygin <rider@altlinux.ru> 1.2.5-alt2
- added missing python3 provides for modules

* Tue Mar 19 2019 Vladimir Didenko <cow@altlinux.ru> 1.2.5-alt1
- new version

* Tue Jul 17 2018 Vladimir Didenko <cow@altlinux.ru> 1.2.4-alt1
- initial build for Sisyphus
