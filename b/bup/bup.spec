Name:     bup
Version:  0.32
Release:  alt1

Summary:  Very efficient backup system based on the git packfile format
# all of the code is licensed as GNU Lesser General Public License v2, except:
# - lib/bup/bupsplit.c: BSD License (two clause),
# - lib/bup/bupsplit.h: BSD License (two clause),
# - lib/bup/options.py: BSD License (two clause),
# - definition of relpath() function in wvtest.py: Python License
License:  LGPL-2.0 and BSD-2-Clause and Python
Group:    Archiving/Backup
URL:      https://bup.github.io/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
# VCS:    https://github.com/bup/bup
Source1:  bup-web.service

Patch1:   bup-disable-test_from_path_error.patch
Patch2:   bup-python.patch
Patch3:   bup-fix_uint32.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: git-core
BuildRequires: pandoc
BuildRequires: python3-module-fuse
BuildRequires: python3-module-pyxattr
BuildRequires: python3-module-libacl
BuildRequires: python3-module-tornado

%add_findreq_skiplist %_libexecdir/%name/cmd/bup*
%add_python3_path %_libexecdir/%name/
%py3_requires xattr posix1e fuse

Requires: git-core

%description
Very efficient backup system based on the git packfile format, providing fast
incremental saves and global deduplication (among and within files, including
virtual machine images). Some of its features are:
* It uses a rolling checksum algorithm and hence it can backup huge files
  incrementally.
* It uses packfile format from git, so one can access the stored data even if
  he doesn't like bup's user interface.
* It writes packfiles directly so it is fast even with huge amounts of data:
  it can track millions of files and keep track of hundreds or thousands of
  gigabytes of objects.
* Data is "automagically" shared between incremental backups without having to
  know which backup is based on which other one.
* One can make a backup directly to a remote bup server, without needing tons
  of temporary disk space on the computer being backed up. If the backup is
  interrupted halfway through, the next run will pick up where the previous
  backup left off.
* It can use "par2" redundancy to recover corrupted backups even if the disk
  has undetected bad sectors.
* Each incremental backup acts as if it's a full backup, it just takes less
  disk space.
* One can mount a bup repository as a FUSE filesystem and access the contents
  that way, or even export it over Samba.

%package web
License: LGPL-2.0
Summary: Web server for browsing through bup repositories
Group:   Archiving/Backup
Requires: %name = %version-%release
Requires: python3-module-tornado

%description web
Provides the "bup web" command which runs a web server for browsing through
bup repositories.

%prep
%setup -q
#patch1 -p1
#patch2 -p1
%patch3 -p1

%build
pushd config
./configure \
       --prefix=%{_prefix} \
       --execdir=%{_bindir} \
       --sbindir=%{_sbindir} \
       --confdir=%{_sysconfdir} \
       --libdir=%{_libdir} \
       --libexecdir=%{_libexecdir} \
       --mandir=%{_mandir}
popd
%make_build PREFIX=%_prefix PYTHON=%__python3

%install
%makeinstall_std PREFIX=%_prefix PYTHON=%__python3
rm -f %buildroot%_bindir/%name
ln -s ../lib/bup/cmd/bup %buildroot%_bindir/%name
install -Dm0644 %SOURCE1 %buildroot%_unitdir/bup-web.service
rm -f %buildroot%_libexecdir/%name/bup/py2raise.py

%check
#make test

%post web
%post_service bup-web

%preun web
%preun_service bup-web

%files
%doc README README.md DESIGN
%doc %_defaultdocdir/%name/
%_bindir/%name
%_libexecdir/%name/
%_man1dir/%{name}*
%exclude %_libexecdir/%name/cmd/bup-web
%exclude %_libexecdir/%name/web/
%exclude %_man1dir/bup-web.1*

%files web
%_libexecdir/%name/cmd/bup-web
%_libexecdir/%name/web/
%_unitdir/bup-web.service
%_man1dir/bup-web.1*

%changelog
* Sun Jan 10 2021 Andrey Cherepanov <cas@altlinux.org> 0.32-alt1
- New version.

* Sat Nov 14 2020 Grigory Ustinov <grenka@altlinux.org> 0.31-alt2
- Transfer on python3.

* Sun Aug 23 2020 Andrey Cherepanov <cas@altlinux.org> 0.31-alt1
- New version.

* Mon May 25 2020 Andrey Cherepanov <cas@altlinux.org> 0.30.1-alt1
- New version.

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1
- New version.

* Mon Aug 26 2019 Andrey Cherepanov <cas@altlinux.org> 0.29.3-alt1
- New version.

* Mon Oct 22 2018 Andrey Cherepanov <cas@altlinux.org> 0.29.2-alt1
- New version.
- Do not build for aarch64 because pandoc is missing.

* Sat Apr 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.29.1-alt1
- New version

* Fri Dec 30 2016 Andrey Cherepanov <cas@altlinux.org> 0.29-alt1
- new version 0.29

* Sun Dec 20 2015 Andrey Cherepanov <cas@altlinux.org> 0.27-alt1
- New version
- Fix project URL and License
- New package bup-web (now only with systemd service)

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.25-alt1.rc1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Jan 30 2012 Andrey Cherepanov <cas@altlinux.org> 0.25-alt1.rc1
- New version 0.25_rc1 (needed for kde4-kup)
- Fix package version to LGPLv2+

* Thu Jan 26 2012 Andrey Cherepanov <cas@altlinux.org> 0.24-alt1
- Initial build in Sisyphus

