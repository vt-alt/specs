Name:     bup
Version:  0.29.3
Release:  alt1

Summary:  Very efficient backup system based on the git packfile format
# all of the code is licensed as GNU Lesser General Public License v2, except:
# - lib/bup/bupsplit.c: BSD License (two clause),
# - lib/bup/bupsplit.h: BSD License (two clause),
# - lib/bup/options.py: BSD License (two clause),
# - definition of relpath() function in wvtest.py: Python License
License:  LGPLv2 and BSD and Python
Group:    Archiving/Backup
URL:      https://bup.github.io/

Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: %ix86 x86_64

Source:   %name-%version.tar
# VCS:    https://github.com/bup/bup
Source1:  bup-web.service

Patch1:   bup-disable-test_from_path_error.patch

BuildPreReq:   python-devel 
BuildRequires: git-core
BuildRequires: pandoc
BuildRequires: python-module-fuse
BuildRequires: python-module-pyxattr
BuildRequires: python-module-libacl
BuildRequires: python-module-tornado

Requires: git-core python-module-pyxattr python-module-libacl python-module-fuse

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
License: LGPLv2
Summary: Web server for browsing through bup repositories
Group:   Archiving/Backup
Requires: %name = %version-%release
Requires: python-module-tornado

%description web
Provides the "bup web" command which runs a web server for browsing through
bup repositories.

%prep
%setup -q
#patch1 -p1

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
%make_build PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix
mkdir -p %buildroot%python_sitelibdir
mv %buildroot%_libexecdir/bup/bup %buildroot%python_sitelibdir

install -Dm0644 %SOURCE1 %buildroot%_unitdir/bup-web.service

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
%python_sitelibdir/bup
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

