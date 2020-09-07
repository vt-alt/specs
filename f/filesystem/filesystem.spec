Name: filesystem
Version: 2.3.18
Release: alt1

Summary: The basic directory layout for a GNU/Linux system
License: Public Domain
Group: System/Base

Source0: %name-dir.list
Source1: %name-link.list
Source2: %name-dir64.list
source3: %name-dir-x32.list
# Traditional MCST paths:
Source4: %name-dir-e2k32.list

PreReq: setup

Provides: /var/empty /var/lock/serial
Provides: /media /proc /run /selinux /srv /sys
Provides: /usr/share/wallpapers
Provides: /usr/share/icons/hicolor
# http://bugzilla.altlinux.org/12020
Provides: /dev/pts
Provides: /dev/shm

Conflicts: shadow-utils < 4.4

%description
This package is one of the basic packages that is installed on a
%distribution system.  Filesystem contains the basic directory layout
for a FHS-compatible GNU/Linux operating system, including the correct
permissions for the directories.

%prep
%setup -cT

%build
{
	cat %_sourcedir/%name-dir.list
%if "%_lib" == "lib64"
	cat %_sourcedir/%name-dir64.list
%endif
%ifarch x32
	cat %_sourcedir/%name-dir64.list
%endif
%ifarch x86_64 x32
	cat %_sourcedir/%name-dir-x32.list
%endif
%ifarch %e2k
	cat %_sourcedir/%name-dir-e2k32.list
%endif
} > dir.list

{
	cat dir.list
	echo '%%defattr(-,root,root,-)'
	cut -d' ' -f1 < %_sourcedir/%name-link.list
} > list

%install
mkdir %buildroot

while read attr dir name extra; do
	mkdir "%buildroot$name"
done < dir.list

while read source target; do
	ln -s "$target" "%buildroot$source"
done < %_sourcedir/%name-link.list

%files -f list

%changelog
* Fri Sep 04 2020 Alexey Shabalin <shaba@altlinux.org> 2.3.18-alt1
- Added /etc/keys directory (by Mikhail Efremov).

* Tue Aug 28 2018 Dmitry V. Levin <ldv@altlinux.org> 2.3.17-alt1
- Moved /etc/syslog.d from syslog-common to filesystem.
- Made /lib/modules readable and executable by everybody (closes: #5969).
- Added libx32 directories on x86_64 and x32 systems (by Ivan Zakharyaschev).
- Added lib32 directories on %%e2k (thx Ivan Zakharyaschev).
- Added %%ghost /run/lock/, marked /var/lock/ and /var/lock/* as %%ghost (by Alexey Shabalin).

* Fri Dec 29 2017 Dmitry V. Levin <ldv@altlinux.org> 2.3.16-alt1
- Added /etc/pki and /usr/share/pki directories.

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 2.3.15-alt1
- Added provides for /dev/shm.

* Tue Mar 07 2017 Mikhail Efremov <sem@altlinux.org> 2.3.14-alt1
- Added /etc/default.

* Wed Feb 10 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.13-alt1
- Added /usr/share/appdata directory.

* Thu Oct 01 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.3.12-alt1
- Made lib64 conditions same for %%build and %%install stages.

* Thu May 17 2012 Dmitry V. Levin <ldv@altlinux.org> 2.3.11-alt1
- Added /run directory.

* Tue Dec 13 2011 Dmitry V. Levin <ldv@altlinux.org> 2.3.10-alt1
- Added 8 new directories:
  /etc/binfmt.d
  /etc/modules-load.d
  /etc/sysctl.d
  /etc/tmpfiles.d
  /lib/binfmt.d
  /lib/modules-load.d
  /lib/sysctl.d
  /lib/tmpfiles.d

* Thu Sep 15 2011 Dmitry V. Levin <ldv@altlinux.org> 2.3.9-alt1
- Removed /cgroup.
- Removed obsolete /usr/X11R6 (closes: #11699).
- Added /dev/pts to Provides (closes: #12020).

* Mon Jan 31 2011 Alexey Tourbin <at@altlinux.ru> 2.3.8-alt1
- Added /usr/src/debug.
- Populated /usr/lib/debug.

* Thu Jul 08 2010 Dmitry V. Levin <ldv@altlinux.org> 2.3.7-alt1
- Added /cgroup and /selinux.

* Wed Jun 23 2010 Dmitry V. Levin <ldv@altlinux.org> 2.3.6-alt1
- Added /lib*/security from pam-config.

* Tue Oct 06 2009 Dmitry V. Levin <ldv@altlinux.org> 2.3.5-alt1
- Added /etc/xdg/autostart/ (closes: #19647).
- Added /etc/hooks/resolv.conf.d/.

* Wed Feb 25 2009 Stanislav Ievlev <inger@altlinux.org> 2.3.4-alt1
- Added /etc/hooks and /etc/hooks/hostname.d directories.

* Thu Oct 18 2007 Dmitry V. Levin <ldv@altlinux.org> 2.3.3-alt1
- Added /usr/share/icons/hicolor directory hierarchy (#11302).
- Added /usr/share/wallpapers directory.

* Fri Jan 13 2006 Dmitry V. Levin <ldv@altlinux.org> 2.3.2-alt1
- Removed symlinks: /usr/bin/X11, /usr/lib/X11.
- Added /usr/share/games directory (#8730).

* Wed Jan 05 2005 Dmitry V. Levin <ldv@altlinux.org> 2.3.1-alt1
- Removed unused 64bit directories and symlinks:
  /lib64/modules, /usr/X11R6/lib64/X11, /usr/lib64/X11.
- Added more XDG directories:
  /etc/xdg, /etc/xdg/menus, /usr/share/applications,
  /usr/share/desktop-directories, /usr/share/mime (#5936).
- Made this package arch-specific.
- Package multilib-specific directories only for multilib
  architectures.

* Sat Oct 02 2004 Dmitry V. Levin <ldv@altlinux.org> 2.3.0-alt1
- Added directories:
  /media, /srv, /lib/tls,
  /lib/i686/tls, /usr/lib/tls, /usr/X11R6/lib/tls.
- Added 64bit directories and symlinks (#4880):
  /lib64, /lib64/modules, /usr/lib64, /usr/lib64/debug,
  /usr/lib64/games, /usr/local/lib64, /usr/X11R6/lib64,
  /usr/X11R6/lib64/X11, /usr/lib64/X11.
- Marked /mnt/* directories as %%ghost, to fix (#4826).
- Added %%ghost directories:
  /initrd, /media/{cdrom,floppy},
  /tmp/.{ICE-unix,X11-unix,esd}.

* Sun Jul 11 2004 Dmitry V. Levin <ldv@altlinux.org> 2.1.7-alt2
- Provides: /proc, /sys.

* Mon Jan 19 2004 Dmitry V. Levin <ldv@altlinux.org> 2.1.7-alt1
- Added directories:
  /sys

* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 2.1.6-alt9
- Removed directories:
  /usr/local/src
  /usr/local/share/man/*
- Added directories:
  /usr/local/man

* Thu Jun 20 2002 Dmitry V. Levin <ldv@altlinux.org> 2.1.6-alt8
- Removed directories:
  /etc/pam.d (pam),
  /etc/profile.d. (setup).
- Added directories:
    /lib/i686, /usr/lib/debug.

* Fri May 24 2002 Dmitry V. Levin <ldv@altlinux.org> 2.1.6-alt7
- Repackaged.
- Changed permissions:
    /boot: 755 -> 700;
    /lib/modules: 755 -> 700;
    /root: 750 ->700.
- Added directories:
    /usr/libexec, /usr/X11R6/lib/X11.

* Mon Jan 28 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.1.6-alt6
- Dropped:
  + %_sysconfdir/chroot.d (chrooted);
  + %_sysconfdir/cron.d (vixie-cron);
  + %_sysconfdir/logrotate.d (chrooted);
  + %_sysconfdir/skel (etcskel);
  + %_sysconfdir/sudo.d (sudo);
  + %_sysconfdir/xinetd.d (xinetd);
  + %_libdir/gcc-lib (gcc-common).

* Sat Nov 17 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.1.6-alt5
- Added directories: /etc/{cron,logrotate,pam,profile}.d.
- Removed directories: /var/lib/rpm.

* Thu Nov 08 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.1.6-alt4
- Changed /var/spool/mail permissions to 3771.
- Added /var/empty provides.

* Mon Oct 22 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.1.6-alt3
- Added /var/lock/serial with %%attr(770,root,uucp) permissions.
- Dropped uucp permissions from /var/lock.
- Removed /initrd.

* Sat Sep 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.6-alt2
- Sync with Owl:
  + Added:
    /var/empty (to be used instead of %_datadir/empty);
    /var/lock/uucp (to be used instead of current /var/lock).
  + Changed permissions:
    /var/spool/mail: 1775 -> 1771;
    /var/lock/subsys: 755 -> 700.

* Fri Sep 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.6-alt1
- 2.1.6: added /usr/X11R6/share, /var/yp, /usr/share/pixmaps,
  /etc/X11/*, /usr/local/*, /initrd
- Added: %_miconsdir, %_liconsdir, %_menudir, %_libdir/helper,
  %_datadir/sounds, %_docdir/HTML/en

* Sun Apr 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.0.7-ipl3mdk
- Fixed perms for /etc/sudo.d

* Sat Mar 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.0.7-ipl2mdk
- Added: /etc/sudo.d, /var/nobody, /usr/share/icons.

* Mon Dec 18 2000 Dmitry V. Levin <ldv@fandra.org> 2.0.7-ipl1mdk
- RE adaptions.
- Added %_sysconfdir/{chroot.d,sysconfig}.
- Really moved /usr/dict to /usr/share/dict.

* Mon Oct  2 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.0.6-2mdk
- Move /usr/dict to /usr/share/dict (thnks: flepied).

* Tue Jul 18 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0.6-1mdk
- merge in RH patches
- For FHS compliance, make the BM (Big Move) (hide children & women :-) ) :
 add /usr/share/{info,man,doc}, remove /usr/{doc,man,info}
- rename /etc/xinet.d to /etc/xinetd.d

* Fri Jul 14 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.5-3mdk
- Add /etc/xinetd.d/

* Wed Mar 29 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.5-2mdk
- Add /mnt/disk.
- Upgrade groups.

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add /opt, /var/state, /var/cache for FHS lords.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- add de locale

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- don't carry X11R6.1 as directory on sparc.
- /var/tmp/build root (#811)

* Wed Jan 13 1999 Preston Brown <pbrown@redhat.com>
- font directory didn't belong, which I previously misunderstood.  removed.

* Fri Nov 13 1998 Preston Brown <pbrown@redhat.com>
- /usr/share/fonts/default added.

* Fri Oct  9 1998 Bill Nottingham <notting@redhat.com>
- put /mnt/cdrom back in

* Wed Oct  7 1998 Bill Nottingham <notting@redhat.com>
- Changed /root to 0750

* Wed Aug 05 1998 Erik Troan <ewt@redhat.com>
- added /var/db
- set attributes in the spec file; don't depend on the ones in the cpio
  archive
- use a tarball instead of a cpioball

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Sep 09 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Wed Jul 09 1997 Erik Troan <ewt@redhat.com>
- added /

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- Changed /proc to 555
- Removed /var/spool/mqueue (which is owned by sendmail)
