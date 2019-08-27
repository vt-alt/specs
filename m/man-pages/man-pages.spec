Name: man-pages
Version: 5.2
Release: alt1

Summary: Man (manual) pages from the Linux Documentation Project
Summary(ru_RU.UTF8): Руководства пользователя Linux Documentation Project
License: distributable
Group: Documentation
Url: http://www.kernel.org/doc/man-pages/

# http://www.kernel.org/pub/linux/docs/man-pages/%name-%version.tar.xz
Source: %name-%version.tar
Source1: %name-extra.tar

Requires: man >= 1.5i2-alt4
BuildArch: noarch
Obsoletes: gnumaniak

# due to major.3/minor.3 (see #19717)
Conflicts: libSDL_sound-devel <= 1.0.3-alt1

# due to resolver.5 (see #19784)
Conflicts: bind-utils <= 9.3.6-alt3

# due to security.2
Conflicts: libcint-devel <= 7.3.00-alt1.svn20090707

# due to attr.5
Conflicts: attr < 2.4.47.0.35.dce9
# due to *attr.2
Conflicts: libattr-devel < 2.4.47.0.35.dce9

# due to fd.4
Conflicts: fdutils < 5.5.20081027-alt2

# due to keyrings.7 and *-keyring.7 (see #33254)
Conflicts: keyutils < 1.5.10

%description
A large collection of man pages (reference material) from the Linux
Documentation Project (LDP).  The man pages are organized into the
following sections:
	1:  User commands (intro and pages not maintained by FSF)
	2:  System calls
	3:  Libc calls
	4:  Devices (e.g. hd, sd)
	5:  File formats and protocols (e.g. wtmp, /etc/passwd, nfs)
	6:  Games (intro only)
	7:  Conventions, macro packages, etc.
	8:  System administration (intro only)

%description -l ru_RU.UTF8
Большая коллекция справочного материала разработанного в рамках Linux
Documentation Project (LDP). Материалы сгруппированы по секциям:
	1:  Команды пользователя (введение)
	2:  Системные вызовы
	3:  Вызовы libc
	4:  Устройства (например, hd, sd)
	5:  Форматы файлов и протоколов (например, wtmp, /etc/passwd, nfs)
	6:  Игры (только введение)
	7:  Соглагшения, макропакеты, и т.д.
	8:  Системное администрирование (только введение)

%package utils
Summary: The scripts for man-pages maintenance tasks
Summary(ru_RU.UTF8): The scripts for man-pages maintenance tasks.
Group: System/Internationalization

%description utils
The scripts for man-pages maintenance tasks.
They may be useful for downstream man-pages package maintainers or for
man-pages translators.

%description -l ru_RU.UTF8
The scripts for man-pages maintenance tasks.
They may be useful for downstream man-pages package maintainers or for
man-pages translators.

%prep
%setup -b1

%build
rm man3/crypt{,_r}.3

%install
mkdir -p %buildroot%_datadir/%name
%makeinstall_std
install -pm644 scripts/* %buildroot%_datadir/%name/

# strip COLOPHON section
find %buildroot%_mandir -type f -print0 |
	xargs -r0 sh scripts/remove_COLOPHON.sh

%files
%doc README* *.Announce *.lsm
%_mandir/man?/*

%files utils
%_datadir/%name/

%changelog
* Fri Aug 02 2019 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt1
- 5.1 -> 5.2.

* Thu May 09 2019 Dmitry V. Levin <ldv@altlinux.org> 5.1-alt1
- 5.0 -> 5.1.

* Wed Mar 06 2019 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt1
- 4.16 -> 5.0.

* Mon Jun 25 2018 Dmitry V. Levin <ldv@altlinux.org> 4.16-alt1
- 4.15 -> 4.16.
- Moved Owl crypt*(3) manual pages to libcrypt-devel.

* Tue Feb 20 2018 Dmitry V. Levin <ldv@altlinux.org> 4.15-alt1
- 4.14 -> 4.15.

* Sun Nov 26 2017 Dmitry V. Levin <ldv@altlinux.org> 4.14-alt1
- 4.13 -> 4.14.

* Fri Sep 15 2017 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt1
- 4.12 -> 4.13.

* Fri Jul 21 2017 Dmitry V. Levin <ldv@altlinux.org> 4.12-alt1
- 4.11 -> 4.12.

* Thu May 25 2017 Dmitry V. Levin <ldv@altlinux.org> 4.11-alt1
- 4.10 -> 4.11.

* Mon Mar 20 2017 Dmitry V. Levin <ldv@altlinux.org> 4.10-alt2
- Conflicts: keyutils < 1.5.10 (closes: #33254).

* Tue Mar 14 2017 Dmitry V. Levin <ldv@altlinux.org> 4.10-alt1
- 4.09 -> 4.10.

* Mon Dec 12 2016 Dmitry V. Levin <ldv@altlinux.org> 4.09-alt1
- 4.08 -> 4.09.

* Sat Oct 08 2016 Dmitry V. Levin <ldv@altlinux.org> 4.08-alt1
- 4.07 -> 4.08.

* Tue Jul 26 2016 Dmitry V. Levin <ldv@altlinux.org> 4.07-alt1
- 4.06 -> 4.07.

* Tue May 10 2016 Dmitry V. Levin <ldv@altlinux.org> 4.06-alt1
- 4.04 -> 4.06.

* Tue Dec 29 2015 Dmitry V. Levin <ldv@altlinux.org> 4.04-alt1
- 4.03 -> 4.04.

* Sat Dec 05 2015 Dmitry V. Levin <ldv@altlinux.org> 4.03-alt1
- 4.02 -> 4.03.
- Packaged fd(4), iconv(1), locale(1), localedef(1), quotactl(2),
  and sprof(1) from the Linux man-pages project.
- Stopped erroneous editing of man3 pages.

* Tue Sep 15 2015 Dmitry V. Levin <ldv@altlinux.org> 4.02-alt2
- Packaged *attr(2).

* Mon Sep 14 2015 Fr. Br. George <george@altlinux.ru> 4.02-alt1
- Autobuild version bump to 4.02

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 4.00-alt1
- Autobuild version bump to 4.00

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 3.83-alt1
- Autobuild version bump to 3.83

* Wed Apr 01 2015 Fr. Br. George <george@altlinux.ru> 3.82-alt1
- Autobuild version bump to 3.82

* Wed Feb 11 2015 Fr. Br. George <george@altlinux.ru> 3.79-alt1
- Autobuild version bump to 3.79

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 3.78-alt1
- Autobuild version bump to 3.78

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 3.75-alt1
- Autobuild version bump to 3.75

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 3.73-alt1
- Autobuild version bump to 3.73

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 3.70-alt1
- Autobuild version bump to 3.70

* Tue Jun 03 2014 Fr. Br. George <george@altlinux.ru> 3.68-alt1
- Autobuild version bump to 3.68

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 3.66-alt1
- Autobuild version bump to 3.66

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 3.64-alt1
- Autobuild version bump to 3.64

* Wed Mar 05 2014 Fr. Br. George <george@altlinux.ru> 3.61-alt1
- Autobuild version bump to 3.61

* Wed Mar 05 2014 Fr. Br. George <george@altlinux.ru> 3.60-alt1
- Long delayed update to 3.60.
- Remove some pages now provided by upstream.
- Refer to original crypt.3 probably containing more recent information.

* Fri Aug 12 2011 Dmitry V. Levin <ldv@altlinux.org> 3.32-alt3
- Updated crypt.3 from crypt_blowfish-1.2.

* Sat Apr 23 2011 Slava Semushin <php-coder@altlinux.ru> 3.32-alt2
- Exclude rpcinfo.8 from package to resolve conflict with rpcbind

* Sat Dec 04 2010 Slava Semushin <php-coder@altlinux.ru> 3.32-alt1
- 3.32

* Fri Nov 12 2010 Slava Semushin <php-coder@altlinux.ru> 3.31-alt1
- 3.31

* Sat Nov 06 2010 Slava Semushin <php-coder@altlinux.ru> 3.30-alt1
- 3.30

* Wed Oct 27 2010 Slava Semushin <php-coder@altlinux.ru> 3.29-alt1
- 3.29
- New maintainer

* Mon Oct 04 2010 Slava Semushin <php-coder@altlinux.ru> 3.28-alt1
- 3.28

* Thu Sep 23 2010 Slava Semushin <php-coder@altlinux.ru> 3.27-alt1
- 3.27

* Tue Sep 14 2010 Slava Semushin <php-coder@altlinux.ru> 3.26-alt1
- 3.26
- Changed group to Documentation (Closes: #24076)

* Sun Jun 20 2010 Slava Semushin <php-coder@altlinux.ru> 3.25-alt1
- 3.25

* Sun Feb 28 2010 Slava Semushin <php-coder@altlinux.ru> 3.24-alt1
- 3.24

* Sun Nov 01 2009 Slava Semushin <php-coder@altlinux.ru> 3.23-alt3
- Strip COLOPHON section in all manual pages
- Made Conflicts with libcint-devel versioned

* Fri Oct 16 2009 Slava Semushin <php-coder@altlinux.ru> 3.23-alt2
- Don't call makewhatis after installation (Closes: #21796)
- Added explicit Conflicts with libcint-devel (noted by repocop)

* Wed Sep 30 2009 Slava Semushin <php-coder@altlinux.ru> 3.23-alt1
- 3.23

* Sun Aug 23 2009 Slava Semushin <php-coder@altlinux.ru> 3.22-alt1
- 3.22

* Tue Apr 21 2009 Slava Semushin <php-coder@altlinux.ru> 3.21-alt1
- NMU
- 3.21
- Changed home page
- Dropped glibcbug.1
- Provide resolver.5 and resolv.conf.5 (see #19784)
- Added versioned Conflicts for libSDL_sound-devel (see #19717)

* Tue Apr 21 2009 Slava Semushin <php-coder@altlinux.ru> 3.18-alt1
- NMU
- 3.18

* Wed Nov 12 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.13-alt1
- 3.13

* Sat Sep 13 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.09-alt1
- 3.09

* Wed Jun 25 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.01-alt1
- 3.01

* Thu Jun 19 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.00-alt1
- 3.00
- dropped obsoleted man-pages-2.65-alt-Makefile.patch

* Sun Jun 08 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.80-alt1
- 2.80
- Updated spec

* Tue Feb 26 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.78-alt1
- 2.78

* Thu Dec 20 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.74-alt1
- 2.74

* Mon Dec 03 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.68-alt1
- 2.68
- Dropped man-pages-goodies

* Thu Oct 11 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.66-alt1
- New pages fallocate.2
- Updated pages: close.2, execve.2, open.2, recv.2, sysctl.2, rpc.3

* Mon Sep 24 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.65-alt1
- 2.65

* Tue Jun 26 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.60-alt1
- 2.60

* Wed May 23 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.50-alt1
- Dropped obsoleted manuals from section 1

* Sat May 19 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.48-alt1
- 2.48

* Tue Dec 12 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.43-alt1
- 2.43
- New and updated pages:
  brk.2, futex.2, ioperm.2, open.2, ptrace.2
  getaddrinfo.3, getnameinfo.3, strerror.3, syslog.3, wcwidth.3
  rtc.4
  core.5, proc.5
  feature_test_macros.7, raw.7, udp.7

* Sun Nov 05 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.41-alt1
- 2.41
- New and updated pages: ldd.1
  execve.2, fork.2, getdtablesize.2, getpagesize.2, madvise.2, mount.2, mmap.2, mremap.2,
  msync.2, prctl.2, posix_fadvise.2, qsort.2, remap_file_pages.2, sendfile.2, sync_file_range.2,
  splice.2, tee.2, vmsplice.2, vfork.2, wait4.2
  clog2.3, clog10.3, mq_receive.3, termios.3, tzset.3
  proc.5
  ip.7, pthreads.7, socket.7

* Sun Nov 05 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.40-alt1
- 2.40
- New and updated pages: clone.2, execve.2, faccessat.2, fchmodat.2, fchownat.2, fork.2,
  fstatat.2, futimesat.2, linkat.2, mkdirat.2, mknodat.2, openat.2, readlinkat.2, renameat.2,
  symlinkat.2, set_mempolicy.2, write.2
  getcwd.3
  proc.5
  capabilities.7, regex.7

* Fri Aug 11 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.39-alt1
- 2.39
- New and updated pages: ldd.1, intro.1
  bind.2, chdir.2, chroot.2, epoll_ctl.2, exevce.2, fdatasync.2, fsync.2, getitimer.2,
  getrlimit.2, getpriority.2, inotify_add_watch.2, intro.2, mmap.2, openat.2, nanosleep.2,
  nice.2, poll.2, readlink.2, readlinkat.2, sched_setscheduler.2, sendfile.2, setpgid.2,
  setsid.2, sync_file_range.2, umask.2
  adjtime.3, atexit.3, ferror.3, intro.3, makecontext.3
  intro.4, wavelan.4
  intro.5, nscd.conf.5, passwd.5
  capabilities.7, feature_test_macros.7, intro.7, standards.7, standards.7, tcp.7

* Thu Jun 22 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.34-alt1
- 2.34
- New pages: ioprio_get.2, ioprio_set.2, mq_getsetattr.2
  CPU_ISSET.3, CPU_CLR.3, CPU_SET.3, CPU_ZERO.3, FD_CLR.3, FD_ISSET.3, FD_SET.3,
  FD_ZERO.3, mq_setattr.3, mq_timedreceive.3, mq_timedsend.3, offsetof.3, rpmatch.3,
  sigandset.3, sigisemptyset.3, sigorset.3, strchrnul.3
- Updated: _exit.2, acct.2, chmod.2, fcntl.2, inotify_add_watch.2, inotify_init.2,
  inotify_rm_watch.2, mmap.2, mount.2, mremap.2, msync.2, open.2, pipe.2, posix_fadvise.2,
  read.2, readahead.2, sched_setaffinity.2, select.2, select_tut.2, send.2, setsid.2,
  shmctl.2, stat.2, statfs.2, umask.2, write.2
- __setfpucw.3, assert_perror.3, bindresvport.3, difftime.3, fts.3, ftw.3, getline.3,
  getrpcent.3, getrpcport.3, inet.3, isalpha.3, mktemp.3, mkstemp.3, mq_open.3,
  mq_notify.3, printf.3, readdir.3, re_comp.3, rpc.3, scandir.3, setlocale.3, stdio.3,
  strchr.3, strtoul.3, tmpnam.3, tmpfile.3, undocumented.3, unlocked_stdio.3, xdr.3
- null.4, console_codes.4
- rpc.5
- epoll.7, feature_test_macros.7, futex.7, inotify.7, ip.7, man.7, mq_overview.7
- tzselect.8, zdump.8, zic.8
- ftm.7 renamed to the more suggestive feature_test_macros.7

* Sat May 20 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.32-alt1
- 2.32
- New pages: faccessat.2, fchmodat.2, fchownat.2, futimesat.2
- Updated: access.2, capget.2, chmod.2, chown.2, mmap.2, openat.2, shmget.2,
  truncate.2, utime.2
  fopen.3, futimes.3, qsort.3, termios.3
  capabilities.7

* Fri May 12 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.31-alt1
- 2.31
- New pages:
  fstatat.2
  adjtime.3, error.3, error_at_line.3, error_message_count.3, error_on_per_line.3,
  error_print_progname.3, program_invocation_name.3, program_invocation_short_name.3,
  sockatmark.3
  ftm.7, time.7
- Updated:
  accept.2, adjtimex.2, chown.2, chdir.2, fsync.2, getgroups.2, getitimer.2,
  gettimeofday.2, mount.2, nanosleep.2, openat.2, recv.2, rmdir.2, select.2,
  semget.2, shmget.2, sigwaitinfo.2, stat.2, syscall.2, time.2, times.2, utime.2,
  wait4.2
  confstr.3, ctanh.3, ctime.3, dirfd.3, err.3, errno.3, fmemopen.3, getdate.3,
  getline.3, initgroups.3, perror.3, printf.3, scanf.3, strerror.3, strtod.3,
  strtoul.3, strtol.3, tmpfile.3,
  rtc.4
  ip.7, signal.7
  ld.so.8

* Mon May 01 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.30-alt1
- 2.30
- New pages: linkat.2, renameat.2, symlinkat.2, unlinkat.2
- Updated:
  link.2, openat.2, rename.2, rmdir.2, symlink.2, unlink.2
  termios.3
  full.4
  core.5

* Sun Apr 09 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.29-alt1
- 2.29
- Added ldd.1 patch by php-coder
- New pages: mkdirat.2, mkfifoat.3, mknodat.2, core.5
- Updated:
  accept.2, fcntl.2, getpeername.2, getrlimit.2, getsockname.2, mkdir.2, mknod.2,
  open.2, openat.2, prctl.2, recv.2, shmop.2, sigaction.2, unshare.2
  mkfifo.3
  elf.5, proc.5
  ip.7, sem_overview.7, signal.7

* Sat Apr 01 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.28-alt1
- 2.28

* Sun Mar 26 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.27-alt1
- 2.27

* Tue Mar 07 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.25-alt1
- 2.25

* Sun Feb 19 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.23-alt1
- 2.23
- Dropped obsoleted manuals from man-pages-2.05-deb.patch
- Added strlcat.3

* Wed Jan 11 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.20-alt1
- 2.20
- Dropped obsoleted manuals from man-pages-2.05-deb.patch

* Mon Dec 19 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.18-alt1
- 2.18
- Dropped obsoleted manuals from man-pages-2.05-deb.patch and netman-cvs.

* Wed Dec 14 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.17-alt1
- 2.17

* Mon Nov 21 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.14-alt1
- 2.14

* Fri Nov 04 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.13-alt1
- 2.13

* Thu Oct 27 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.11-alt1
- 2.11
- Added scripts for man-pages maintenance tasks.

* Tue Oct 18 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.09-alt1
- 2.09

* Thu Sep 29 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.08-alt1
- 2.08
- Dropped obsoleted manuals from man-pages-extra.

* Wed Jul 27 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.07-alt1
- 2.07
- Updated iconv.1 by 'php-coder' <php-coder@altlinux.ru>
- Updated man-pages-deb.patch

* Tue Jun 28 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.05-alt2
  Changes from 2.03:
- New pages: pthreads.7
- Updated pages: _exit.2, epoll_ctl.2 close.2 dup.2 fcntl.2 flock.2 fpclassify.3
  getgid.2 getuid.2 getitimer.2 getpriority.2 getrlimit.2 getrusage.2 nice.2
  open.2 atexit.3 exit.3 getloadavg.3 getopt.3 hsearch.3 log1p.3 log2.3 makecontext.3
  on_exit.3 rand.3 readdir.3 realpath.3 rcmd.3 scanf.3 stdin.3 strerror.3 strtod.3
  sysconf.3 tdestroy.3 tsearch.3 mem.4 null.4 vcs.4 proc.5 ip.7 tcp.7 signal.7 urn.7
- Updated man-pages-deb.patch

* Thu Jun 09 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.03-alt2
- Updated man-pages-1.69-deb.patch

* Mon Jun 06 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.03-alt1
- 2.03

* Thu Apr 14 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.02-alt1
- 2.02

* Tue Dec 21 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.01-alt1
- 2.01

* Mon Dec 20 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.00-alt1
- 2.00
- Many minor content and formatting bug fixes were made to the math pages.
- Minor changes in spec.

* Mon Nov 15 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.70-alt1
- 1.70.
- Differences from version 1.69:
  the man pages are new or have been updated:

  ls.1

  chroot.2 exit_group.2 mmap.2 nanosleep.2 remap_file_pages.2
  undocumented.2 wait.2

  HUGE_VAL.3 HUGE_VALF.3 HUGE_VALL.3 INFINITY.3 NAN.3
  dl_iterate_phdr.3 drand48_r.3 endnetgrent.3 erand48_r.3
  finite.3 finitef.3 finitel.3 fpclassify.3 gethostent.3
  gethostent_r.3 getnetgrent.3 getnetgrent_r.3 grantpt.3
  ilogb.3 ilogbf.3 ilogbl.3 innetgr.3 isalpha.3 isinf.3
  isinff.3 isinfl.3 jrand48_r.3 lcong48_r.3 ldexp.3
  logb.3 logbf.3 logbl.3 lrand48_r.3 mrand48_r.3 nrand48_r.3
  openpty.3 ptsname.3 remquo.3 remquof.3 remquol.3 resolver.3
  scalb.3 scalbf.3 scalbl.3 scalbln.3 scalblnf.3 scalblnl.3
  scalbn.3 scalbnf.3 scalbnl.3 seed48_r.3 setnetgrent.3
  significand.3 significandf.3 significandl.3 srand48_r.3
  termios.3 undocumented.3 unlockpt.3

  resolv.conf.5 utmp.5

  ip.7

  ld-linux.8 ld-linux.so.8

* Wed Oct 27 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.69-alt1
- Updated man-pages-deb.patch
- Dropped obsoleted man-pages-owl-uselib.patch
- Differences from version 1.67:
  the man pages are new or have been updated:

  accept.2 acct.2 adjtimex.2 bdflush.2 bind.2 capget.2 chdir.2
  chmod.2 chown.2 chroot.2 clone.2 connect.2 epoll_create.2
  execve.2 fcntl.2 fork.2 futex.2 getdomainname.2
  getgroups.2 gethostname.2 getpriority.2 getrlimit.2
  gettimeofday.2 getuid.2 ioperm.2 iopl.2 kill.2 killpg.2
  link.2 lookup_dcookie.2 mkdir.2 mknod.2 mlock.2 mlockall.2
  mmap.2 mprotect.2 msgctl.2 msgget.2 msgop.2 munlockall.2
  nice.2 open.2 path_resolution.2 pipe.2 pivot_root.2 poll.2
  ptrace.2 readahead.2 reboot.2 sched_setparam.2
  sched_setscheduler.2 select.2 semctl.2 semget.2 semop.2
  send.2 seteuid.2 setfsgid.2 setfsuid.2 setreuid.2
  set_tid_address.2 setuid.2 shmctl.2 shmget.2
  shmop.2 socket.2 stime.2 tgkill.2 tkill.2 vhangup.2

  cabs.3 cacosf.3 cacosl.3 cerf.3 cexp2.3 clock_getres.3
  clog10.3 clog2.3 cproj.3 creal.3 ecvt_r.3 exec.3 exp10.3
  gethostbyname.3 getmntent.3 getopt.3 log2.3 malloc.3 pow10.3
  remainder.3 setenv.3 sincos.3 strcat.3 termios.3

  resolv.conf.5

  capabilities.7 mailaddr.7 man.7 socket.7 udp.7 unix.7

  nscd.8

  ksoftirqd.9

* Sun May 23 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.67-alt1
- Differences from version 1.66:
  the man pages are new or have been updated:

  capget.2 epoll_ctl.2 execve.2 fcntl.2 getrlimit.2 ioctl.2
  mincore.2 mmap.2 mremap.2 open.2 sched_setaffinity.2
  setresuid.2 sigpause.2 utime.2

  getmntent.3 gets.3 hsearch.3 login.3 scandir.3

  epoll.4

  proc.5

  ascii.7 LDP.7 packet.7 socket.7 unix.7

* Mon Feb 23 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.66-alt2
- POSIX manual pages moved into separate package due to licensing problem.

* Tue Feb 10 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.66-alt1
- 1.66
- Fixed errors in spec.
- Fixed few buggy links in man3p.
- Differences from version 1.65:
  the man pages are new or have been updated:

  sys_ipc.h.0p sys_mman.h.0p sys_msg.h.0p sys_resource.h.0p
  sys_select.h.0p sys_sem.h.0p sys_shm.h.0p sys_socket.h.0p
  sys_stat.h.0p sys_statvfs.h.0p sys_time.h.0p sys_timeb.h.0p
  sys_times.h.0p sys_types.h.0p sys_uio.h.0p sys_un.h.0p
  sys_utsname.h.0p sys_wait.h.0p

* Tue Jan 27 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.65-alt1
- 1.65
- POSIX pages were added
- Differences from version 1.64:
  the man pages are new or have been updated:

  chroot.2 clone.2 intro.2 mkdir.2 remap_file_pages.2

  errno.3

  sk98lin.4

  elf.5 protocols.5 raw.7

* Wed Dec 03 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.64-alt1
- 1.64
- Differences from version 1.63:
  the man pages are new or have been updated:

  getrlimit.2 intro.2 posix_fadvise.2 signal.2

  asinh.3 cfree.3 des_crypt.3 dladdr.3 dlopen.3 dlvsym.3 drem.3
  dremf.3 dreml.3 encrypt.3 fmodf.3 fmodl.3 frexp.3 gamma.3
  getaddrinfo.3 getgrouplist.3 getipnodebyname.3 getmntent_r.3
  getutent.3 getutent_r.3 getutid_r.3 getutline_r.3 hsearch.3
  ldexp.3 ldexpf.3 ldexpl.3 lgamma.3 malloc.3 perror.3
  remainder.3 remainderf.3 remainderl.3 sincosf.3 sincosl.3
  stdio.3 strtoimax.3 syslog.3 tgamma.3

  hosts.equiv.5

  packet.7

* Mon Nov 17 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.63-alt1
- 1.63
- Differences from version 1.60:
  the man pages are new or have been updated:

  sstk.2

  endspent.3 fgetgrent_r.3 fgetpwent_r.3 fgetspent.3 fgetspent_r.3
  getgrent.3 getgrent_r.3 getgrgid_r.3 getgrnam.3 getgrnam_r.3
  getmntent.3 getmntent_r.3 getpwent_r.3 getpwnam.3 getpwnam_r.3
  getpwuid_r.3 getspent.3 getspent_r.3 getspnam.3 getspnam_r.3
  lckpwdf.3 putgrent.3 putspent.3 qsort.3 rand.3 rand_r.3
  setspent.3 sgetspent.3 sgetspent_r.3 tmpnam.3 tmpnam_r.3
  ulckpwdf.3 undocumented.3

  addseverity.3 aio_cancel.3 aio_error.3 aio_fsync.3 aio_read.3
  aio_return.3 aio_suspend.3 aio_write.3

  brk.2 fcntl.2 mlock.2 munlock.2 recv.2 send.2

  atexit.3 basename.3 bsearch.3 cosf.3 coshf.3 coshl.3 cosl.3
  ctime.3 div.3 endaliasent.3 fmtmsg.3 getaliasbyname.3
  getaliasbyname_r.3 getaliasent.3 getaliasent_r.3
  gethostbyname.3 imaxdiv.3 log10.3 mempcpy.3 on_exit.3 printf.3
  setaliasent.3 sinhf.3 sinhl.3 strtoimax.3 strtoumax.3
  tanhf.3 tanhl.3 wcstoimax.3 wcstoumax.3 wmempcpy.3
  wordexp.3 wordfree.3

  random.4

* Thu Aug 28 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.60-alt1
- 1.60
- Differences from version 1.59:

  fdatasync.2 fstatvfs.2 get_thread_area.2 getdents.2 mlockall.2
  mmap.2 mprotect.2 msync.2 sched_setscheduler.2 select_tut.2
  statfs.2 statvfs.2

  asctime_r.3 clock_getres.3 clock_gettime.3 clock_settime.3
  ctime_r.3 getlogin.3 getlogin_r.3 gmtime_r.3 localtime_r.3
  posix_memalign.3 sysconf.3

  host.conf.5

  glob.7 iso-8859-16.7 iso_8859_16.7 latin10.7 latin5.7 latin9.7
  operator.7 posixoptions.7

* Fri Aug 22 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.59-alt1
- 1.59
- updated man-pages-1.39-deb.patch
- Differences from version 1.58:

  dup.2 getsockopt.2 gettimeofday.2 ioperm.2 iopl.2 lseek.2
  msync.2 munlock.2 open.2 pciconfig_iobase.2 pciconfig_read.2
  pciconfig_write.2 poll.2 ptrace.2 reboot.2 recv.2 rmdir.2
  sched_rr_get_interval.2 select.2 send.2 sendfile.2 setresuid.2
  setuid.2 sigaction.2 statfs.2 ustat.2 wait4.2

  bstring.3 dirfd.3 ffs.3 ffsl.3 ffsll.3 inet_ntop.3 insque.3
  stdio.3 va_copy.3

  ip.7

* Mon Aug 11 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.58-alt1
- 1.58
- Fixed few buggy links in man3.
- differences from 1.57:

  fcntl.2 mlock.2

  acos.3 acosf.3 acosh.3 acoshf.3 acoshl.3 acosl.3 asin.3 asinf.3
  asinh.3 asinhf.3 asinhl.3 asinl.3 atan.3 atan2.3 atan2f.3 atan2l.3
  atanf.3 atanh.3 atanhf.3 atanhl.3 atanl.3 cbc_crypt.3 cos.3 cosh.3
  des_crypt.3 des_setparity.3 ecb_crypt.3 erf.3 erfcf.3 erfcl.3
  erff.3 erfl.3 exp.3 exp10.3 exp10f.3 exp10l.3 exp2.3 exp2f.3
  exp2l.3 expf.3 expl.3 expm1.3 expm1f.3 expm1l.3 fdim.3 fdimf.3
  fdiml.3 fma.3 fmaf.3 fmal.3 fmax.3 fmaxf.3 fmaxl.3 fmin.3 fminf.3
  fminl.3 fmod.3 fpclassify.3 frexp.3 getgrnam.3 getpwnam.3 hypot.3
  hypotf.3 hypotl.3 isfinite.3 isgreater.3 isgreaterequal.3 isinf.3
  isless.3 islessequal.3 islessgreater.3 isnan.3 isnormal.3 isunordered.3
  log.3 log10.3 log10f.3 log10l.3 log1p.3 log1pf.3 log1pl.3 log2.3
  log2f.3 log2l.3 logf.3 login.3 logl.3 logout.3 modf.3 modff.3
  modfl.3 openpty.3 passwd2des.3 pow10.3 pow10f.3 pow10l.3 pow.3
  powf.3 powl.3 sin.3 sincos.3 sinf.3 sinh.3 sinl.3 sqrt.3 sqrtf.3
  sqrtl.3 tan.3 tanf.3 tanh.3 tanl.3 termios.3 ualarm.3 undocumented.3
  updwtmp.3 usleep.3 xcrypt.3 xdecrypt.3 xencrypt.3

- differences from 1.56:

  epoll_create.2 epoll_ctl.2 epoll_wait.2 getresuid.2 ioctl_list.2
  lookup_dcookie.2 mmap.2 open.2 poll.2 semop.2 semtimedop.2

  cabs.3 cabsf.3 cabsl.3 cacos.3 cacosh.3 cacoshf.3 cacoshl.3 carg.3
  cargf.3 cargl.3 casin.3 casinf.3 casinh.3 casinhf.3 casinhl.3
  casinl.3 catan.3 catanf.3 catanh.3 catanhf.3 catanhl.3 catanl.3
  cbrt.3 cbrtf.3 cbrtl.3 ccos.3 ccosf.3 ccosh.3 ccoshf.3 ccoshl.3
  ccosl.3 cerf.3 cerfc.3 cerfcf.3 cerfcl.3 cerff.3 cerfl.3 cexp2.3
  cexp2f.3 cexp2l.3 cexp.3 cexpf.3 cexpl.3 cimag.3 cimagf.3 cimagl.3
  clog10.3 clog10f.3 clog10l.3 clog2.3 clog2f.3 clog2l.3 clog.3
  clogf.3 clogl.3 conj.3 conjf.3 conjl.3 cpow.3 cpowf.3 cpowl.3
  cproj.3 cprojf.3 cprojl.3 creal.3 crealf.3 creall.3 csin.3 csinf.3
  csinh.3 csinhf.3 csinhl.3 csinl.3 csqrt.3 csqrtf.3 csqrtl.3 ctan.3
  ctanf.3 ctanh.3 ctanhf.3 ctanhl.3 ctanl.3 dlopen.3 encrypt.3 lockf.3
  mtrace.3 rtime.3

  epoll.4
  complex.5 proc.5
  iso_8859-16.7 ip.7

* Tue Mar 11 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.56-alt2
- removed duplicates

* Fri Mar 07 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.56-alt1
- 1.56
- Added new and updated manuals:
  fgetxattr.2 flistxattr.2 fremovexattr.2 fsetxattr.2 getpmsg.2
  getxattr.2 get_thread_area.2 io_cancel.2 io_destroy.2
  io_getevents.2 io_setup.2 io_submit.2 lgetxattr.2 listxattr.2
  llistxattr.2 lookup_dcookie.2 lremovexattr.2 lsetxattr.2
  posix_fadvise.2 putpmsg.2 readahead.2 removexattr.2 security.2
  setxattr.2 set_thread_area.2

  ftw.3 openpty.3

* Mon Feb 10 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.55-alt1
- 1.55
- Added new and updated manuals:
  alloc_hugepages.2 arch_prctl.2 clone.2 free_hugepages.2
  futex.2 gettid.2 mmap.2 msgget.2 personality.2 recv.2
  select.2 send.2 setpgid.2 shmget.2 syslog.2 tkill.2
  undocumented.2

  bcmp.3 bcopy.3 bzero.3 getpt.3 grantpt.3 ptsname.3 remove.3
  scanf.3 shm_open.3 string.3 tcgetpgrp.3 tcgetsid.3 unlockpt.3

  futex.4 ptmx.4 pts.4

  proc.5

  signal.7

* Fri Jan 03 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.54-alt1
- 1.54

* Wed Sep 03 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.53-alt2
- 1.53

* Wed Aug 07 2002 Stanislav Ievlev <inger@altlinux.ru> 1.52-alt2
- removed gnumaniak man-pages. This pages now provided by
  appropriate packages. libtool and libtoolize man pages still live
  in this package.
- ressurected dlopen
- removed fileutils related man pages

* Mon Jul 29 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.52-alt1
- 1.52

* Wed Jun 20 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.51-alt1
- 1.51

* Fri Jun 14 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.48-alt2
- addition in man-pages-extra: catchsegv.1, getconf.1, glibcbug.1
- updates in man-pages-extra: getent.1, iconv.1, locale.1,
  localedef.1, sprof.1, ld-linux.so.8, rpcinfo.8

* Fri Mar 01 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.48-alt1
- 1.48
- updated man-pages-extra (man3/crypt*)
- updated deb patch.

* Wed Jan 09 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.47-alt1
- 1.47
- updated deb patch.
- added Summary & description in CP1251 encoding

* Sun Dec 23 2001 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.45-alt1
- 1.45
- updated deb patch.

* Thu Dec 06 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.44-alt1
- 1.44, updated patches.
- Moved all extra man pages into man-pages-extra traball.
- Added strlcpy(3) from OpenBSD.
- Added %post (run daily makewhatis script).

* Sun Oct 28 2001 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.43-alt1
- 1.43
- Updated deb patch.
- Updated spec.

* Tue Oct 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.40-alt1
- 1.40
- Updated deb patch.

* Wed Sep 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.39-alt2
- su.1: moved to su package based on SimplePamApps.

* Thu Jul 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.39-alt1
- 1.39

* Mon Jun 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.38-alt1
- 1.38

* Mon Jun 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.37-alt1
- 1.37
- Updated crypt.3 page from crypt_blowfish-0.4.1

* Mon May 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.36-alt2
- Updated crypt.3 page from crypt_blowfish-0.4

* Fri May 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.36-alt1
- 1.36

* Tue May 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.35-ipl2mdk
- More manpages from RH, Debian, Owl.

* Tue Mar 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.35-ipl1mdk
- 1.35

* Mon Jan 29 2001 Dmitry V. Levin <ldv@fandra.org> 1.34-ipl2mdk
- Fixed few buggy links in man9.

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.33-ipl1mdk
- 1.33

* Tue Dec 12 2000 Dmitry V. Levin <ldv@fandra.org> 1.32-ipl1mdk
- 1.32

* Thu Nov 30 2000 Dmitry V. Levin <ldv@fandra.org> 1.31-ipl1mdk
- 1.31

* Thu Jul 27 2000 Dmitry V. Levin <ldv@fandra.org> 1.30-ipl2mdk
- Added: manpages from gnumaniak project.
- RE and Fandra adaptions.

* Tue Jun 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.30-2mdk
- Add URL
- Use mandir macros for FHS compatibilty

* Mon Jun 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.30-1mdk
- new release (1.30 : various fixes & a few more pages)
- suppress the tzet path which is now useless

* Wed Apr  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.29-4mdk
- Rebuild with the good spec-helper to remove orphan link to orphan
  man-page.

* Thu Mar 23 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- new group scheme
- spechelper

* Fri Mar 17 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.29-2mdk
- removed various pages that conflict with pages included in new
  rpm packages (ld.so and bind-utils)

* Wed Mar 08 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.29-1mdk
- 1.29 is out
- moved man1/{COPYING,README} to /usr/doc

* Fri Feb 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.28-3mdk
- Remove dir and vdir.1 (conflicts with last fileutils).

* Wed Jan 26 2000 Pablo Saratxaga <pablo@mandrakesoft.com>
- added humoristic man pages sex(6), baby(1) and guru(n).

* Mon Nov 29 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- 1.28

* Fri Nov 19 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added requires locales-en (english man pages require english lang. support)
- added nice icon similar to other man-pages-* packages
- added obsoletes man9 (as we now include the man9 pages)

* Wed Aug 25 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.26
- add man9

* Thu Jul 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.25.

* Mon Jun 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.24 version.
- Removed some obsolete patchs.

* Mon May 24 1999 Bernhard RosenkrДnzer <bero@mandrakesoft.com>
- remove fd.4 - we get a far more recent version from fdutils
