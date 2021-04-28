Name: bats
Version: 1.3.0
Release: alt1

Summary: Testing framework for Bash
Summary(ru_RU.UTF-8): Набор тестов на Bash

License: MIT
Group: Development/Other
Url: https://github.com/bats-core/bats-core

# Source-url: https://github.com/bats-core/bats-core/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

Requires: bash

%description
Bats is a testing framework for Bash.
It provides a simple way to verify that the UNIX programs you write behave as expected.

%description -l ru_RU.UTF-8
Bats - вспомогательный фреймворк для Bash'а.
Это простой способ убедиться, что программа, написанная под Unix, будет работать, как ожидается.

%prep
%setup
# use /usr/share instead of /usr/lib
find -type f -print0 | xargs -0 subst 's|lib/bats-core|share/bats-core|g'
mv -v lib share

%install
./install.sh %buildroot%prefix

%files
%doc LICENSE.md README.md AUTHORS
%_man1dir/*
%_man7dir/*
%_bindir/bats
%_datadir/bats-core/
%_prefix/libexec/bats-core/

%changelog
* Tue Apr 27 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script) (ALT bug 39998)
- switch to build from tarball

* Sun Nov 18 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version

* Fri Mar 11 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- cleanup spec

* Thu Sep 02 2015 Anton Agapov <anton@altlinux.org> 1.0-alt1
- iinitial build for ALT Linux Sisyphus
