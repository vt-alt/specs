Name: lockfile-progs
Version: 0.1.18
Release: alt1

Summary: Programs for locking and unlocking files and mailboxes
License: GPL-2.0
Group: File tools
URL: https://packages.debian.org/unstable/misc/lockfile-progs

Source: %name-%version.tar

BuildRequires: liblockfile-devel

%description
This package includes several programs to safely lock and unlock files
and mailboxes from the command line.

These include:
- lockfile-create
- lockfile-remove
- lockfile-touchlock
- mail-lock
- mail-unlock
- mail-touchlock.

These programs use liblockfile to perform the file locking and
unlocking.

%prep
%setup

%build
%make CC=gcc

%install
install -d %buildroot{%_bindir,%_man1dir}

cp -a bin/* %buildroot%_bindir
cp -a man/* %buildroot%_man1dir

echo '.so lockfile-progs.1' > lockfile-progs.1
install lockfile-progs.1 %buildroot%_man1dir/lockfile-create.1
install lockfile-progs.1 %buildroot%_man1dir/lockfile-remove.1
install lockfile-progs.1 %buildroot%_man1dir/lockfile-touch.1
install lockfile-progs.1 %buildroot%_man1dir/mail-lock.1
install lockfile-progs.1 %buildroot%_man1dir/mail-unlock.1
install lockfile-progs.1 %buildroot%_man1dir/mail-touchlock.1

%files
%doc TODO debian/changelog
%_bindir/lockfile-create
%_bindir/lockfile-remove
%_bindir/lockfile-touch
%_bindir/lockfile-check
%_bindir/mail-lock
%_bindir/mail-touchlock
%_bindir/mail-unlock
%_man1dir/lockfile-create.1*
%_man1dir/lockfile-progs.1*
%_man1dir/lockfile-remove.1*
%_man1dir/lockfile-touch.1*
%_man1dir/lockfile-check.1*
%_man1dir/mail-lock.1*
%_man1dir/mail-touchlock.1*
%_man1dir/mail-unlock.1*

%changelog
* Thu Jan 21 2021 Andrey Cherepanov <cas@altlinux.org> 0.1.18-alt1
- New version.
- Disable check.

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.17-alt1
- Version 0.1.17

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.11-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue May 19 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1.11-alt2
- Fix building with gcc4.4

* Wed Oct 29 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1.11-alt1
- Initial build for ALT Linux (spec from PLD)
