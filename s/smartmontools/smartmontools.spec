%global _unpackaged_files_terminate_build 1

Name: smartmontools
Version: 7.2
Release: alt1

Summary: Control and monitor storage systems using S.M.A.R.T.
License: GPLv2+
Group: Monitoring

Url: http://smartmontools.sourceforge.net

# http://download.sourceforge.net/smartmontools/smartmontools-%version.tar.gz
Source0: smartmontools-%version.tar
Source1: smartd.init
Source2: smartd.sysconfig
Source3: smartmontools-update-drivedb

Patch1: smartmontools-alt-conf.patch
Patch2: smartmontools-alt-service.patch

Obsoletes: smartctl
Obsoletes: smartd
Obsoletes: ucsc-smartsuite
Obsoletes: smartsuite

# Automatically added by buildreq on Thu Mar 13 2008
BuildRequires: gcc-c++
BuildRequires: libsystemd-devel

%description
This package contains two utility programs (smartctl and smartd) to
control and monitor storage systems using the Self-Monitoring, Analysis
and Reporting Technology System (S.M.A.R.T.) built into most modern
ATA and SCSI hard disks.  It is derived from the smartsuite package,
and includes support for ATA/ATAPI-5 disks.

%package update-drivedb
Summary: Install drivedb update script and cron task
Group: Monitoring
Requires: %name
Requires: gnupg curl crontabs

%description update-drivedb
This package contains script to update drive database and verify it
using GnuPG. Monthly cronjob is also provided.

Use this package when your smart output contains Unknown_Attribute
records: the drive database is updated much faster than
smartmontools themselves.

%prep
%setup
%patch1 -p1
%patch2 -p1
fgrep -lZ /usr/local/bin/mail *.in |
	xargs -r0 sed -i 's,/usr/local/bin/mail,/bin/mail,g' --
fgrep -lZ /usr/local/etc/sysconfig *.am *.in |
	xargs -r0 sed -i 's,/usr/local/etc/sysconfig,/etc/sysconfig,g' --

%build
%define docdir %_docdir/%name-%version
%configure --docdir=%docdir \
	--with-libsystemd \
	--with-systemdsystemunitdir=%systemd_unitdir
%make_build \
	BUILD_INFO='"(%distribution %version-%release)"'

%install
%makeinstall_std

chmod 600 %buildroot%_sysconfdir/smartd.conf

install -pD -m755 %_sourcedir/smartd.init \
	%buildroot%_initdir/smartd
install -pD -m644 %_sourcedir/smartd.sysconfig \
	%buildroot%_sysconfdir/sysconfig/smartd

rm %buildroot%docdir/{ChangeLog,COPYING,INSTALL}

install -pD -m755 %_sourcedir/smartmontools-update-drivedb \
	%buildroot%_sysconfdir/cron.monthly/smartmontools-update-drivedb

%post
%post_service smartd

%preun
%preun_service smartd

%files
%_sbindir/smartd
%_sbindir/smartctl
%_initdir/smartd
%systemd_unitdir/smartd.service
%_man8dir/smartctl.*
%_man8dir/smartd.*
%_man5dir/smartd.conf.*
%config(noreplace) %_sysconfdir/smartd.conf
%config(noreplace) %_sysconfdir/sysconfig/smartd
%config(noreplace) %_sysconfdir/smartd_warning.sh
%docdir

%files update-drivedb
%_sbindir/update-smart-drivedb
%_datadir/%name
%_man8dir/update-smart-drivedb.*
%_sysconfdir/cron.monthly/smartmontools-update-drivedb

%changelog
* Fri Jan 01 2021 Michael Shigorin <mike@altlinux.org> 7.2-alt1
- Updated to 7.2.

* Fri Jul 03 2020 Andrew Savchenko <bircoph@altlinux.org> 7.1-alt2
- Add package for drivedb update script, data and cronjob.

* Tue Dec 31 2019 Michael Shigorin <mike@altlinux.org> 7.1-alt1
- Updated to 7.1.

* Mon Dec 31 2018 Michael Shigorin <mike@altlinux.org> 7.0-alt1
- Updated to 7.0.

* Mon Nov 06 2017 Michael Shigorin <mike@altlinux.org> 6.6-alt1
- Updated to 6.6.

* Tue May 10 2016 Michael Shigorin <mike@altlinux.org> 6.5-alt1
- Updated to 6.5.

* Fri Jun 05 2015 Michael Shigorin <mike@altlinux.org> 6.4-alt1
- Updated to 6.4.

* Mon Jul 28 2014 Michael Shigorin <mike@altlinux.org> 6.3-alt1
- Updated to 6.3.

* Sun Jul 28 2013 Michael Shigorin <mike@altlinux.org> 6.2-alt1
- Updated to 6.2.

* Wed Mar 20 2013 Michael Shigorin <mike@altlinux.org> 6.1-alt2
- Packaged %_sysconfdir/smartd_warning.sh.

* Tue Mar 19 2013 Michael Shigorin <mike@altlinux.org> 6.1-alt1
- Updated to 6.1.

* Mon Oct 15 2012 Dmitry V. Levin <ldv@altlinux.org> 6.0-alt1
- Updated to 6.0.

* Fri Sep 28 2012 Dmitry V. Levin <ldv@altlinux.org> 5.43-alt1
- Updated to 5.43.

* Wed May 09 2012 Dmitry V. Levin <ldv@altlinux.org> 5.42-alt4
- Fixed smartd.service.

* Sat May 05 2012 Dmitry V. Levin <ldv@altlinux.org> 5.42-alt3
- Fixed smartd.service.

* Fri May 04 2012 Dmitry V. Levin <ldv@altlinux.org> 5.42-alt2
- smartd.conf: Added some options to DEVICESCAN directive.
- Packaged systemd unit file.

* Fri Nov 25 2011 Dmitry V. Levin <ldv@altlinux.org> 5.42-alt1
- Updated to 5.42.

* Tue Sep 27 2011 Dmitry V. Levin <ldv@altlinux.org> 5.41-alt1
- Updated to 5.41 (closes: #26355).

* Sun Jan 31 2010 Sergey Vlasov <vsu@altlinux.ru> 5.39.1-alt1
- Version 5.39.1.
- Dropped alt-cciss-warnings patch (fixed upstream).
- Dropped rh-cloexec patch (fixed upstream for Linux).

* Sat Mar 15 2008 Sergey Vlasov <vsu@altlinux.ru> 5.38-alt1
- Version 5.38.
- Dropped obsolete cvs-* patches.
- Dropped deb-cciss patch (already upstream).
- Updated FC cloexec patch from smartmontools-5.38-1.fc9.
- Updated BuildRequires.
- Add alt-cciss-warnings patch: remove unused variable and fix 64bit printf
  format mismatch in cciss support code.

* Mon Apr 16 2007 Dmitry V. Levin <ldv@altlinux.org> 5.36-alt3
- Imported FC cloexec patch.

* Sun Jun 11 2006 Sergey Vlasov <vsu@altlinux.ru> 5.36-alt2
- Added patches from smartmontools CVS:
  + cvs-wd-attr-190: identify Attribute 190 for Western Digital disks
    (temperature in Celsius, like Attribute 190, but with failure threshold set
    to maximum design operating temperature of the disk)
  + cvs-vpd-page-0x83-size: increase VPD page 0x83 request size from 96 to 252
    bytes for Linux
  + cvs-libata-2.6.17-id: change libata detection by VPD page 0x83 to accept
    the new variant used by kernels >= 2.6.17
  + cvs-seagate-momentus: add more Seagate Momentus 5400.2 drives to database

* Sat Jun 10 2006 Dmitry V. Levin <ldv@altlinux.org> 5.36-alt1
- Updated to 5.36.
- Dropped ALM22 startup script.
- Dropped old patch from Debian package.
- Applied patch with support for CCISS controllers.

* Mon Apr 11 2005 Dmitry V. Levin <ldv@altlinux.org> 5.32-alt1
- Updated to 5.32.
- Applied patch from Debian package (smartmontools-5.32-3).
- startup script: added recheck, reload and condreload targets.

* Tue Apr 20 2004 Sergey Vlasov <vsu@altlinux.ru> 5.30-alt1
- Version 5.30.

* Tue Dec 02 2003 Sergey Vlasov <vsu@altlinux.ru> 5.26-alt1
- Version 5.26.
- Added backward-compatible initscript (use --with m22 to build package
  compatible with Master 2.2).

* Tue Jun 17 2003 Sergey Vlasov <vsu@altlinux.ru> 5.1.14-alt1
- Version 5.1-14.
- Init script completely rewritten for new conventions.

* Wed Apr 30 2003 Sergey Vlasov <vsu@altlinux.ru> 5.1.10-alt1
- First build for ALT Linux.
- Removed pre-ALT %%changelog (it was just a duplicate of CHANGELOG
  inside the package and described main code changes, not packaging changes).
- Added ALT-specific init script.
