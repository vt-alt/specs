# SPEC file for password-store package

Name:    password-store
Version: 1.7.4
Release: alt1

Summary: a simple password manager using standard Unix tools
Summary(ru_RU.UTF-8): простой и использующий стандартные средства менеджер паролей

License: %gpl2plus
Group:   Text tools
URL:     https://www.passwordstore.org/
#URL:    http://zx2c4.com/projects/password-store/
#URL:    http://git.zx2c4.com/password-store/

BuildArch: noarch

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-alt-1.6.5-shebang.patch
Patch2:  %name-alt-1.7-dirtree.patch
Patch3:  %name-alt-1.7.1-completion.patch

BuildRequires(pre): rpm-build-licenses rpm-build-vim

# Automatically added by buildreq on Wed Jan 25 2017
# optimized out: libgpg-error python-base python-modules python3 tzdata
BuildRequires: dirtree git-core gnupg gnupg2 pwgen

# Skip extra requires:
%add_findreq_skiplist %_bindir/pass

# Requires for pass:
Requires: /bin/bash
Requires: gnupg2 dirtree coreutils diffutils findutils git-core procps sed which


%description
A simple console password manager that follows Unix philosophy.
With pass, each password lives inside of a GnuPG encrypted text
file whose filename is the title of the website or resource
that requires the password. These encrypted files may be
organized into meaningful folder hierarchies, copied from
computer to computer, and, in general, manipulated using
standard command line file management utilities.

Multiple GPG keys can be specified, for using pass in a team
setting, and different folders can have different GPG keys.
Password changes can be tracked using git.


%description -l ru_RU.UTF-8
Простой консольный менеджер паролей, следующий философии Unix.
Пароли сохраняются внутри защищенных с использованием GnuPG
текстовых файлов с именами, соответствующими названиям
веб-сайтов или ресурсов. Файлы с паролями могут быть
организованы в произвольной иерархии каталогов, копироваться
с компьютера на компютер, и, в общем случае, обрабатываться
стандартными утилитами.

Поддерживается использование нескольких ключей GPG для
случая использования pass в совместной работе, разные
каталоги могут иметь разные наборы ключей GPG.
Все изменения паролей могут отслеживаться в репозитории Git.


%package gui
Summary: GUI support for password-store
Summary(ru_RU.UTF-8): графический интерфейс к password-store
Group: Text tools
Requires: %name = %version-%release

Requires: qt5-dbus xclip
Requires: xdotool dmenu
Requires: qrencode feh

%description gui
Password-store (pass) is a simple console password manager that
follows Unix philosophy.

This package contains passmenu utility - a simple GUI interface
to pass, and installs X11 utilities to work with clipboard and
display passwords as QR codes.

%description gui -l ru_RU.UTF-8
Password-store (pass) - простой консольный менеджер паролей,
следующий философии Unix.

Данный пакет содержит утилиту passmenu - простой графический
интерфейс к pass, и зависимости на утилиты X11 для работы
с буфером обмена и выводом паролей как QR-кодов.


%prep
%setup -q
%patch0 -p1

%patch1
%patch2
%patch3

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
# This can't be run inside hasher - some problems with /dev/urandom (?)
%ifdef __BTE
   rm -f tests/t0010-generate-tests.sh
   rm -f tests/t0020-show-tests.sh
   rm -f tests/t0300-reencryption.sh
   rm -f tests/t0400-grep.sh
   rm -f tests/t0060-rm-tests.sh
   rm -f tests/t0200-edit-tests.sh
   rm -f tests/t0500-find.sh
%endif
LC_ALL=C %make test

%install
%make_install DESTDIR=%buildroot FORCE_ALL=1 WITH_ALLCOMP=yes install

install -dp %buildroot%_sysconfdir/bash_completion.d/
mv -f -- %buildroot%_datadir/bash-completion/completions/pass %buildroot%_sysconfdir/bash_completion.d/pass

chmod 644 -- contrib/importers/*

install -dp %buildroot%vim_plugin_dir
mv -f -- contrib/vim/*  %buildroot%vim_plugin_dir/
rmdir -- contrib/vim/

# passmenu
install -m 755 contrib/dmenu/passmenu %buildroot%_bindir/passmenu

%files
%doc README contrib
%doc --no-dereference COPYING

%_bindir/pass
%_man1dir/pass.*

%_sysconfdir/bash_completion.d/pass
%vim_plugin_dir/*

%_datadir/fish/vendor_completions.d/pass.fish
%_datadir/zsh/site-functions/_pass

%files gui
%doc contrib/dmenu/README.md
%_bindir/passmenu


%changelog
* Fri Jul 02 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.7.4-alt1
- New version (Closes: 36738)
- Pack fish and zsh completions (Closes: 34654)
- Add subpackage -gui with GUI-related dependencies

* Tue Jun 19 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.7.2-alt1
- New version
  * Ensure signature regexes are anchored, fix for CVE-2018-12356
  * Allow grep options and arguments for 'search' command
  * Other changes and bug fixes

* Mon Sep 25 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.7.1-alt2
- Fix Bash completion code

* Sat Jul 15 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.7.1-alt1
- New version

* Thu Jan 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.6.5-alt1
- Initial build for ALT Linux Sisyphus
