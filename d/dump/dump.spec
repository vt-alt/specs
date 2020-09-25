Name: dump
Version: 0.4b44
Release: alt2

Summary: Programs for backing up and restoring ext2/ext3 filesystems
License: BSD
Group: Archiving/Backup

URL: http://dump.sourceforge.net/
Source: http://downloads.sourceforge.net/dump/dump-%version.tar.gz
Patch1: dump-0.4b28-alt-makefile.patch
Patch2: dump-0.4b40-include.patch
Patch3: dump-0.4b44-alt-DSO.patch

Requires: rmt = %version-%release

BuildPreReq: glibc-kernheaders

# Automatically added by buildreq on Fri Jun 26 2009
BuildRequires: bzlib-devel libdevmapper-devel libe2fs-devel libncurses-devel libreadline-devel libselinux-devel libsepol-devel zlib-devel

%package -n rmt
Summary: Provides certain programs with access to remote tape devices
Group: Archiving/Backup

%description
The %name package contains both dump and restore. Dump examines files in a
filesystem, determines which ones need to be backed up, and copies those files
to a specified disk, tape or other storage medium. The restore command performs
the inverse function of dump; it can restore a full backup of a filesystem.
Subsequent incremental backups can then be layered on top of the full backup.
Single files and directory subtrees may also be restored from full or partial
backups.

%description -n rmt
The rmt utility provides remote access to tape devices for programs like dump
(a filesystem backup program), restore (a program for restoring files from a
backup) and tar (an archiving program).

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p2

subst s,termcap,tinfo,g ./configure.in
sed -i '/^#include <sys.un.h>/ a#include <sys/sysmacros.h>' restore/tape.c

%build
#autoconf
%autoreconf
%configure \
	--with-manowner=root \
	--with-mangrp=root \
	--with-binmode=755 \
	--with-manmode=644 \
	--enable-rmt \
	--enable-readline \
	--enable-largefile
make OPT="%optflags -Wpointer-arith -Wstrict-prototypes -Wmissing-prototypes -Wno-char-subscripts"

%install
mkdir -p %buildroot{/sbin,%_man8dir}

make install SBINDIR=%buildroot/sbin BINDIR=%buildroot/sbin MANDIR=%buildroot%_man8dir

pushd %buildroot
	ln -s -nf dump ./sbin/rdump
	ln -s -nf restore ./sbin/rrestore
	ln -s -nf dump.8 .%_man8dir/rdump.8
	ln -s -nf restore.8 .%_man8dir/rrestore.8
	chmod a-s ./sbin/rmt
	mkdir -p .%_sysconfdir
	:> .%_sysconfdir/dumpdates
	ln -s -nf ../sbin/rmt .%_sysconfdir/rmt
popd

%files
/sbin/*dump
/sbin/*restore
%_man8dir/*dump.*
%_man8dir/*restore.*
%attr(664,root,disk) %config(noreplace) %_sysconfdir/dumpdates
%doc CHANGES COPYRIGHT KNOWNBUGS README THANKS MAINTAINERS

%files -n rmt
/sbin/rmt
%_sysconfdir/rmt
%_man8dir/rmt.*
%doc COPYRIGHT

%changelog
* Tue Apr 28 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4b44-alt2
- fixed build with glibc >=2.26

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4b44-alt1.1
- Fixed build

* Tue Jun 28 2011 Victor Forsiuk <force@altlinux.org> 0.4b44-alt1
- 0.4b44

* Fri Jun 11 2010 Victor Forsiuk <force@altlinux.org> 0.4b43-alt1
- 0.4b43

* Mon Jul 06 2009 Victor Forsyuk <force@altlinux.org> 0.4b42-alt1
- 0.4b42

* Wed Sep 12 2007 Victor Forsyuk <force@altlinux.org> 0.4b41-alt2
- Build with glibc-kernheaders instead of kernel-headers-std.

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.4b41-alt1.0
- Automated rebuild.

* Thu Jan 12 2006 Victor Forsyuk <force@altlinux.ru> 0.4b41-alt1
- 0.4b41
- Drop "fixacl" patch, now applied in upstream.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.4b40-alt1.1
- Rebuilt with libreadline.so.5.

* Thu May 26 2005 Victor Forsyuk <force@altlinux.ru> 0.4b40-alt1
- 0.4b40
- Note in the Summary that this tool only for ext2/ext3 filesystems.
- Patch to avoid "Invalid kernel header included in userspace" error
  in current Sisyphus.
- Fix restoration of ext3 ACL's.

* Wed Jan 28 2004 Stanislav Ievlev <inger@altlinux.org> 0.4b35-alt1
- 0.4b35
- use subst instead of tinfo patch
- now package use latest autoconf

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4b31-alt1
- Updated to 0.4b31.
- Explicitly use autoconf-2.13 for build.

* Sat Jun 29 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4b28-alt2
- Patched to link with libtinfo.

* Wed Jun 05 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4b28-alt1
- 0.4b28

* Wed Sep 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.4b24-alt1
- 0.4b24

* Thu Jul 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.4b23-alt1
- 0.4b23
- Corrected requires.
- Enabled LFS.

* Wed Jun 20 2001 Sergie Pugachev <fd_rag@altlinux.ru> 0.4b22-alt1
- new version

* Sat Feb 24 2001 Dmitry V. Levin <ldv@fandra.org> 0.4b21-ipl2mdk
- Fixed build with glibc-2.2.2

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 0.4b21-ipl1mdk
- RE adaptions.

* Sun Jan 14 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.4b21-1mdk
- new and shiny source.

* Sun Nov 12 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.4b20-1mdk
- new and shiny version to avoid potential security hole.

* Wed Nov 08 2000 Geoffrey Lee <snailtalk@mandrkaesoft.com> 0.4b19-3mdk
- don't pass suid permissions to %%configure.

* Tue Aug 22 2000 Vincent Saugey <vince@mandrakesoft.com> 0.4b19-2mdk
- Corrected licence
- Adding url

* Mon Aug 21 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.4b19-1mdk
- s|0.4b18|0.4b19|.

* Fri Jul 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.4b18-2mdk
- rebuild for the BM
- use more new macros (titiscks)

* Wed Jul 05 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4b18-1mdk
- new release (potential SECURITY FIX)
- use new macros

* Wed Apr 19 2000 Vincent Saugey <vince@mandrakesoft.com> 0.4b16-3mdk
- Remove the sgid (tty) on binaries files.

* Fri Mar 31 2000 Vincent Saugey <vince@mandrakesoft.com> 0.4b16-2mdk
- Update to 4b16

* Mon Mar 13 2000 David BAUDNS <baudens@mandrakesoft.com> - 0.4b10-2mdk
- Fix %%doc
- Use new Groups
- Use %%_tmppath for BuildRoot

* Mon Nov 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 0.4b10.

* Mon Nov  8 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 0.4b9.

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix danglings symlinks.

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge rh patchs.

* Mon Apr 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Add modification from RedHat 6.0.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man pages
- add de locale

* Fri Feb 19 1999 Preston Brown <pbrown@redhat.com>
- upgraded to dump 0.4b4, massaged patches.

* Tue Feb 02 1999 Ian A Cameron <I.A.Cameron@open.ac.uk>
- added patch from Derrick J Brashear for traverse.c to stop bread errors

* Wed Jan 20 1999 Jeff Johnson <jbj@redhat.com>
- restore original 6755 root.tty to dump/restore, defattr did tty->root (#684).
- mark /etc/dumpdates as noreplace.

* Tue Jul 14 1998 Jeff Johnson <jbj@redhat.com>
- add build root.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- added a patch for resolving linux/types.h and sys/types.h conflicts

* Wed Dec 31 1997 Erik Troan <ewt@redhat.com>
- added prototype of llseek() so dump would work on large partitions

* Thu Oct 30 1997 Donnie Barnes <djb@redhat.com>
- made all symlinks relative instead of absolute

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved rmt to its own package.

* Tue Feb 11 1997 Michael Fulbright <msf@redhat.com>
- Added endian cleanups for SPARC

* Fri Feb 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Made /etc/dumpdates writeable by group disk.

