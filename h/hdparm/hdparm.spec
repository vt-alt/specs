Name: hdparm
Version: 9.58
Release: alt1

Summary: An utility for displaying and/or setting hard disk parameters
License: BSD-style
Group: System/Kernel and hardware
Url: https://sourceforge.net/projects/hdparm/

# https://download.sourceforge.net/%name/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
hdparm utility provides a command line interface to various hard disk
ioctls supported by the Linux SATA/PATA/SAS "libata" subsystem and the
older IDE driver subsystem.

%prep
%setup
%patch -p1
rm contrib/fix_standby

%build
export CFLAGS='%optflags'
%make_build CC=gcc LDFLAGS= STRIP=:

%install
install -pD -m755 hdparm %buildroot/sbin/hdparm
install -pD -m644 hdparm.8 %buildroot%_man8dir/hdparm.8
install -pD -m644 sysconfig %buildroot%_sysconfdir/sysconfig/harddisks
mkdir -p %buildroot%_sysconfdir/sysconfig/harddisk

%files
%dir %_sysconfdir/sysconfig/harddisk
%config(noreplace) %_sysconfdir/sysconfig/harddisks
/sbin/*
%_mandir/man?/*
%doc *.lsm Changelog LICENSE.TXT README* contrib wiper

%changelog
* Fri Oct 26 2018 Dmitry V. Levin <ldv@altlinux.org> 9.58-alt1
- 9.56 -> 9.58.

* Thu Jun 07 2018 Dmitry V. Levin <ldv@altlinux.org> 9.56-alt1
- 9.52 -> 9.56.

* Sun Dec 10 2017 Dmitry V. Levin <ldv@altlinux.org> 9.52-alt1
- 9.48 -> 9.52.

* Mon Jan 18 2016 Dmitry V. Levin <ldv@altlinux.org> 9.48-alt1
- 9.45 -> 9.48.

* Sat Nov 15 2014 Dmitry V. Levin <ldv@altlinux.org> 9.45-alt1
- Updated to 9.45.

* Fri Apr 26 2013 Dmitry V. Levin <ldv@altlinux.org> 9.43-alt1
- Updated to 9.43.

* Mon Oct 08 2012 Dmitry V. Levin <ldv@altlinux.org> 9.42-alt1
- Updated to 9.42.

* Mon Apr 02 2012 Dmitry V. Levin <ldv@altlinux.org> 9.39-alt1
- Updated to 9.39.

* Mon Jan 24 2011 Dmitry V. Levin <ldv@altlinux.org> 9.37-alt1
- Updated to 9.37.

* Sat Nov 06 2010 Dmitry V. Levin <ldv@altlinux.org> 9.35-alt1
- Updated to 9.35.

* Tue Oct 05 2010 Dmitry V. Levin <ldv@altlinux.org> 9.33-alt1
- Updated to 9.33.

* Fri Sep 24 2010 Dmitry V. Levin <ldv@altlinux.org> 9.32-alt1
- Updated to 9.32.

* Fri Sep 03 2010 Dmitry V. Levin <ldv@altlinux.org> 9.30-alt1
- Updated to 9.30.

* Mon Mar 22 2010 Dmitry V. Levin <ldv@altlinux.org> 9.28-alt1
- Updated to 9.28 (closes: #23020).

* Fri Jun 20 2008 Dmitry V. Levin <ldv@altlinux.org> 8.9-alt1
- Updated to 8.9.

* Thu Jun 12 2008 Dmitry V. Levin <ldv@altlinux.org> 8.8-alt1
- Updated to 8.8.

* Thu Jun 05 2008 Dmitry V. Levin <ldv@altlinux.org> 8.7-alt1
- Updated to 8.7.

* Tue Dec 04 2007 Dmitry V. Levin <ldv@altlinux.org> 7.7-alt1
- Updated to 7.7.

* Thu Nov 02 2006 Dmitry V. Levin <ldv@altlinux.org> 6.9-alt1
- Updated to 6.9.

* Thu Nov 02 2006 Dmitry V. Levin <ldv@altlinux.org> 6.8-alt1
- Updated to 6.8.

* Fri Oct 06 2006 Dmitry V. Levin <ldv@altlinux.org> 6.7-alt1
- Updated to 6.7.

* Mon Jun 12 2006 Dmitry V. Levin <ldv@altlinux.org> 6.6-alt1
- Updated to 6.6.

* Fri Nov 04 2005 Dmitry V. Levin <ldv@altlinux.org> 6.3-alt1
- Updated to 6.3.

* Wed Dec 01 2004 Dmitry V. Levin <ldv@altlinux.org> 5.8-alt1
- Updated to 5.8.

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 5.7-alt1
- Updated to 5.7.
- Removed patches:
  alt-ataraid (no longer needed),
  rh-readahead (merged upstream).
- Rediffed patches.

* Tue Apr 27 2004 Dmitry V. Levin <ldv@altlinux.org> 5.5-alt1
- Updated to 5.5.
- Fixed build with fresh glibc headers.

* Wed Jan 08 2003 Dmitry V. Levin <ldv@altlinux.org> 5.3-alt1
- Updated to 5.3.
- Minor compilation fixes.

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 5.2-alt2
- Rebuilt in new environment

* Fri Aug 02 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt1
- 5.2
- Moved %_sysconfdir/sysconfig/harddisk* here from initscripts package.

* Tue Jan 08 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.6-alt2
- Added ATARAID functionality
- Fixed optflags

* Sat Jan 05 2002 Rider <rider@altlinux.ru> 4.6-alt1
- 4.6
- russian summary and description

* Wed Mar 07 2001 Dmitry V. Levin <ldv@fandra.org> 4.1-ipl1mdk
- 4.1

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 3.9-ipl1mdk
- RE adaptions.
- FHSification.

* Fri Feb 18 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Sun Feb 06 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 3.9-1mdk
- 3.9

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix building as non-root.
- Fix wrong patch.

* Mon May 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 3.5 (UltraDMA at last...)

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- handle RPM_OPT_FLAGS

* Tue Dec 29 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 3.3
- build rooted

* Fri Oct 31 1997 Donnie Barnes <djb@redhat.com>
- fixed spelling error in summary

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
