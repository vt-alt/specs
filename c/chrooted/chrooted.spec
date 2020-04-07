Name: chrooted
Version: 0.3.11
Release: alt1

Summary: The chrooted environment helper
License: GPLv2+
Group: File tools
BuildArch: noarch

%define _chrootdir %_sysconfdir/chroot.d

Source: %name-%version.tar

Provides: %_chrootdir
Requires: coreutils, getopt, glibc-utils, grep, sed

BuildPreReq: help2man

%description
This package is required for chroot-aware packages.

%prep
%setup

%build
sed -i 's/@VERSION@/%version/g' -- update_chrooted
help2man -N -s8 -i update_chrooted.8.inc ./update_chrooted >update_chrooted.8

%install
mkdir -p %buildroot{/sbin,%_sbindir,%_man8dir,%_chrootdir}
install -pm755 update_chrooted %buildroot/sbin/
ln -s ../../sbin/update_chrooted %buildroot%_sbindir/
install -pm755 functions %buildroot%_chrootdir/
install -pm644 update_chrooted.8 %buildroot%_man8dir/

install -Dpm755 resolvconf %buildroot%_sysconfdir/hooks/resolv.conf.d/update_chrooted

# Generate shell functions provides list.
(
	echo '# shell functions provides list'
	for f in %buildroot%_chrootdir/*; do
		[ -x "$f" ] || continue
		sed -ne 's/^\([A-Za-z][A-Za-z_0-9]*[[:space:]]*\)()$/\1/pg' "$f"
	done |LC_COLLATE=C sort -u
) >%buildroot%_chrootdir/.provides.sh

%post
/sbin/update_chrooted -f all

%files
%_sysconfdir/hooks/resolv.conf.d/*
/sbin/*
%_sbindir/*
%_man8dir/*
%config %_chrootdir

%changelog
* Fri Apr 03 2020 Dmitry V. Levin <ldv@altlinux.org> 0.3.11-alt1
- Copy: always dereference symbolic links in SOURCE
  (by Alexey Shabalin; closes: #33591).

* Wed Mar 11 2020 Ivan Zakharyaschev <imz@altlinux.org> 0.3.10-alt1
- Fixes:
  + OVE-20200311-0001 Normal update operations by root can corrupt/crash running processes through modifying libraries

    (Normally, the processes that can be affected are only the services
    already running in the chrooted environment being updated, if it is on
    a different filesystem than the system libraries, and hence they
    can't be hardlinked. Extraordinarily, if a file in a chrooted
    environment has been a hardlink to a system library, but ln hasn't
    succeeded this time for some reason, the affected processes are any
    already running processes system-wide.

    This could happen only as a result of actions initiated by root:
    for example, a package upgrade which included the old version of
    chrooted, or a package upgrade which included libraries in a system
    with the old version of chrooted, or an invocation of
    /sbin/update_chrooted.)

* Tue Apr 10 2018 Maxim Voronov <mvoronov@altlinux.org> 0.3.9-alt1
- copy_resolv_conf: added support for symlinked /etc/localtime (see #32346).

* Fri Aug 24 2012 Dmitry V. Levin <ldv@altlinux.org> 0.3.8-alt1
- copy_resolv_conf: forcibly remove stale optional config files.

* Fri Aug 24 2012 Dmitry V. Levin <ldv@altlinux.org> 0.3.7-alt1
- copy_resolv_conf: treat /etc/localtime as an optional config file.

* Mon Mar 16 2009 Stanislav Ievlev <inger@altlinux.org> 0.3.6-alt2
- added a hook for openresolv

* Thu Nov 27 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3.6-alt1
- functions (copy_resolv_lib): Copy required NSS libraries only.
- %%post: Force full update.

* Fri Aug 24 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.5-alt1
- updated to play well with nss_mdns

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 0.3.4-alt2
- Reduced macro abuse in specfile.

* Mon Sep 05 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.4-alt1
- chroot.d/functions (copy_resolv_conf): added multilib support.
- Updated FSF postal address.

* Sat Jun 18 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt1
- chroot.d/functions (CopyLibs): enhanced new ldd(1) output handling.

* Tue Mar 01 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.2-alt1
- chroot.d/functions (is_yes): new function.
- chroot.d/functions:
  + added options: --no-force/--no-verbose;
  + changed force default value to be $FORCE-dependent;
  + changed verbose default value to be $VERBOSE-dependent.

* Wed Mar 31 2004 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- chroot.d/functions (CopyLibs):
  + fix readlink usage for coreutils >= 5.2.1-alt3.
- chroot.d/functions (copy_resolv_conf):
  + attempt to copy /var/nis/NIS_COLD_START file only if it exists.
- update_chrooted: added --list option.

* Sun Feb 15 2004 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- update_chrooted: added more options and document them.
- chroot.d/functions:
  + parse common options;
  + optimized getopt handling code;
  + added functions: Info, Verbose;
  + added functions: copy_resolv_conf, copy_resolv_lib.
- Added %_chrootdir/.provides.sh file.
- Added update_chrooted(8) manpage.

* Mon Nov 25 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.1-alt1
- update_chrooted: propagate --force option to scripts.
- chroot.d/functions:
  + added comments (#0001443);
  + added Fatal() function;
  + Copy(): use cp(1) for simple cases, install(1) for others.

* Wed Sep 25 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt4
- Provides: %_sysconfdir/chroot.d

* Tue Apr 16 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt3
- update_chrooted: exit during install.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt2
- update_chrooted: relocated from %_sbindir/ to /sbin/
  (compatibility symlink created).

* Sat Apr 13 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- chroot.d/functions (CopyLibs): when in Copy mode,
  call Copy (by default) in "-m 755" mode.
- Updated package requires.

* Thu Feb 22 2001 Dmitry V. Levin <ldv@fandra.org> 0.1-ipl5
- chroot.d/functions (Copy): really skip missing source files.

* Fri Feb 16 2001 Dmitry V. Levin <ldv@fandra.org> 0.1-ipl4
- chroot.d/functions (Copy): allow empty exe list, be less verbose.

* Wed Feb 14 2001 Dmitry V. Levin <ldv@fandra.org> 0.1-ipl3
- chroot.d/functions (Copy): skip missing source files.

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 0.1-ipl2
- chroot.d/functions (CopyLibs): skip missing libraries.

* Mon Jan 29 2001 Dmitry V. Levin <ldv@fandra.org> 0.1-ipl1
- Initial revision.
