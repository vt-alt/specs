%define oname lark-parser

Name: python3-module-%oname
Version: 0.9.0
Release: alt1

Summary: A modern parsing library for Python, implementing Earley & LALR(1) and an easy interface

License: MIT
Group: Development/Python3
Url: https://github.com/lark-parser/lark

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-numpy python3-module-flaky python3-module-pytz python3-module-django
#BuildRequires: python3-module-django-tests python3-module-fake-factory python3-modules-sqlite3
#BuildRequires: python3(mock) python3(coverage) python3(pandas) python3(dateutil)

#py3_requires coverage

%description
Parse any context-free grammar, FAST and EASY!

Beginners: Lark is not just another parser.
It can parse any grammar you throw at it,
no matter how complicated or ambiguous, and do so efficiently.
It also constructs a parse-tree for you, without additional code on your part.

Experts: Lark implements both Earley(SPPF) and LALR(1),
and several different lexers, so you can trade-off power and speed,
according to your requirements.
It also provides a variety of sophisticated features and utilities.

Lark can:
Parse all context-free grammars, and handle any ambiguity
Build a parse-tree automagically, no construction code required
Outperform all other Python libraries when using LALR(1) (Yes, including PLY)
Run on every Python interpreter (it's pure-python)
Generate a stand-alone parser (for LALR(1) grammars)

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune
rm -rfv %buildroot%python3_sitelibdir/lark/__pyinstaller

%check
#PYTHONPATH=%buildroot%python3_sitelibdir py.test3

%files
%doc LICENSE README.md
%python3_sitelibdir/*

%changelog
* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version 0.9.0 (with rpmrb script)

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- initial build for ALT Sisyphus
