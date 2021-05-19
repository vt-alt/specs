# SPEC file for dirtree package

%define real_name tree

Name:    dirtree
Version: 1.8.0
Release: alt1

Summary: a recursive directory listing command
Summary(ru_RU.UTF-8): консольная утилита для рекурсивного отображения каталогов

License: %gpl2only
Group:   File tools

# Note: access to the project home page may be blocked from Russia,
# try to use any of foreign proxies if needed.
URL:     http://mama.indstate.edu/users/ice/tree/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %real_name-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed Jan 25 2017
# optimized out: python-base python-modules python3
BuildRequires: gcc-common

%description
Tree is a recursive directory listing command that produces
a depth indented listing of files, which is colorized ala
dircolors if the LS_COLORS environment variable is set and
output is to tty.

This variant of 'tree' utility (renamed to 'dirtree') have a much
more features comparing to the default ALT Linux 'tree', but
with incompatible options syntax.

%description -l ru_RU.UTF-8
Tree - команда для рекурсивного отображения содержимого каталогов,


%prep
%setup -q -n %real_name-%version

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENSE) LICENSE

%build
%make_build

%install
# Makefile doesn't support DESTDIR...
install -D -m 755 %real_name %buildroot%_bindir/%name
install -D -m 644 doc/%{real_name}.1  %buildroot%_man1dir/%{name}.1

%files
%doc CHANGES TODO README
%doc --no-dereference LICENSE

%_bindir/%name
%_man1dir/%{name}.*

%changelog
* Sat Jun 27 2020 Nikolay A. Fetisov <naf@altlinux.org> 1.8.0-alt1
- New version

* Wed Jan 25 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.7.0-alt1
- Initial build for ALT Linux Sisyphus
