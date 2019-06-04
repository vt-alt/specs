%define _unpackaged_files_terminate_build 1
Name: sysstat
Version: 12.0.5
Release: alt1

Summary: The sar and iostat system monitoring commands
License: GPLv2+
Group: System/Base

URL: http://sebastien.godard.pagesperso-orange.fr/
Source: %name-%version.tar
Source1: sysstat.init

# Automatically added by buildreq on Wed Aug 04 2010
BuildRequires: libsensors3-devel

%description
This package provides the sar and iostat commands for the Linux operating
system, similar to their traditional UNIX counterparts. They enable system
monitoring of disk, network, and other IO activity.

%package isag
Summary: Interactive System Activity Graph
License: GPLv2+
Group: System/Base
Requires: gnuplot, sysstat = %version

BuildArch: noarch

%description isag
isag is a command that enables you to plot data stored in a daily data file
by a previous sar run.

%prep
%setup

%build
export CFLAGS="%optflags"
export sa_lib_dir=%_libdir/sa
# we build script for daily summary that takes yesterday's data and will
# run it by cron after midnight
%configure \
	--enable-yesterday \
	--enable-sensors \
	--disable-file-attr \
	--disable-compress-manpg 

sed -i 's/SADC_OPTIONS=""/SADC_OPTIONS="-S DISK"/' sysstat.sysconfig

%make_build SA_LIB_DIR="%_libdir/sa" LFLAGS="-lsensors"

%install
%makeinstall_std IGNORE_MAN_GROUP=y

install -p -m644 -D sysstat.ioconf %buildroot%_sysconfdir/sysconfig/
install -p -m644 -D sysstat.sysconfig %buildroot/etc/sysconfig/sysstat
install ./contrib/isag/isag %buildroot%_bindir
install ./contrib/isag/isag.1  %buildroot%_man1dir

install -d %buildroot%_sysconfdir/cron.d/
# Create cronjob file inline. We can easily use here rpm macros for libdir and
# thus allows for multiarch build.
cat > %buildroot%_sysconfdir/cron.d/%name <<EOF
# run system activity accounting tool every 10 minutes
*/10 * * * * root %_libdir/sa/sa1 -S DISK 1 1
# generate a daily summary of process accounting
0 2 * * * root %_libdir/sa/sa2 -A
EOF

install -pD -m755 %_sourcedir/sysstat.init %buildroot%_initrddir/sysstat
subst 's@LIBDIR@%_libdir@' %buildroot%_initrddir/sysstat

# Install service file
mkdir -p %buildroot%_unitdir
install -m 0644 sysstat.service %buildroot%_unitdir/

# Install timer units
install -m 0644 cron/sysstat-{collect,summary}.{service,timer} %buildroot%_unitdir/

# sysstat makefiles install the docs, blow them away
rm -rf %buildroot/usr/doc

%find_lang %name

%post
%post_service sysstat

%preun
%preun_service sysstat
if [[ $1 -eq 0 ]]; then
  # Remove sa logs if removing sysstat completely
  rm -f %_logdir/sa/*
fi

%files -f %name.lang
%config(noreplace) %attr(644,root,root) %_sysconfdir/cron.d/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config %_sysconfdir/sysconfig/sysstat.ioconf
%_bindir/*
%exclude %_bindir/isag
%_libdir/sa
%_initrddir/*
%_unitdir/*
%_man1dir/*
%exclude %_man1dir/isag.*
%_man5dir/*
%_man8dir/*
%attr(750,root,adm) %_logdir/sa
%doc CHANGES CREDITS FAQ.md

%files isag
%_bindir/isag
%_man1dir/isag.*

%changelog
* Mon Jun 03 2019 Alexey Melyashinsky <bip@altlinux.org> 12.0.5-alt1
- Update to upstraem version 12.0.5.

* Wed Dec 26 2018 Alexey Melyashinsky <bip@altlinux.org> 12.0.3-alt1
- Update to upstream version 12.0.3.

* Sat Jun 28 2014 Alexey Shabalin <shaba@altlinux.ru> 11.0.0-alt1
- 11.0.0

* Fri Mar 09 2012 Victor Forsiuk <force@altlinux.org> 10.0.4-alt1
- 10.0.4

* Sat Dec 10 2011 Victor Forsiuk <force@altlinux.org> 10.0.3-alt1
- 10.0.3

* Wed Aug 31 2011 Victor Forsiuk <force@altlinux.org> 10.0.2-alt1
- 10.0.2

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 10.0.1-alt1
- 10.0.1
- Fix sar -u overflow problem (patch from Fedora).

* Wed Mar 16 2011 Victor Forsiuk <force@altlinux.org> 10.0.0-alt1
- 10.0.0

* Thu Dec 30 2010 Victor Forsiuk <force@altlinux.org> 9.1.7-alt1
- 9.1.7

* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 9.1.6-alt1
- 9.1.6

* Tue Sep 28 2010 Victor Forsiuk <force@altlinux.org> 9.1.5-alt1
- 9.1.5

* Wed Aug 04 2010 Victor Forsiuk <force@altlinux.org> 9.1.4-alt1
- 9.1.4
- sysstat-isag should be noarch.

* Mon Jul 12 2010 Victor Forsiuk <force@altlinux.org> 9.1.3-alt1
- 9.1.3

* Fri Jun 18 2010 Victor Forsiuk <force@altlinux.org> 9.1.2-alt1
- 9.1.2

* Mon Mar 01 2010 Victor Forsiuk <force@altlinux.org> 9.1.1-alt1
- 9.1.1

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 9.0.6-alt1
- 9.0.6

* Mon Aug 31 2009 Victor Forsyuk <force@altlinux.org> 9.0.4-alt1
- 9.0.4
- No more automatic sa logs deleting when user remove sysstat package.

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 8.1.6-alt1
- 8.1.6

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 8.1.5-alt1
- 8.1.5

* Mon Jun 23 2008 Victor Forsyuk <force@altlinux.org> 8.1.4-alt1
- 8.1.4

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 8.1.3-alt2
- Fix #15849.

* Mon May 26 2008 Victor Forsyuk <force@altlinux.org> 8.1.3-alt1
- 8.1.3

* Thu Mar 27 2008 Victor Forsyuk <force@altlinux.org> 8.1.2-alt1
- 8.1.2

* Wed Nov 14 2007 Victor Forsyuk <force@altlinux.org> 8.0.2-alt1
- 8.0.2
- Modify cron.d job: tell sadc to report statistics for disks.

* Wed May 02 2007 Victor Forsyuk <force@altlinux.org> 7.1.4-alt1
- 7.1.4
- Fix ALT#11673.

* Fri Mar 30 2007 Victor Forsyuk <force@altlinux.org> 7.1.3-alt1
- 7.1.3

* Thu Dec 07 2006 Victor Forsyuk <force@altlinux.org> 7.0.3-alt1
- 7.0.3
- Install initscript to reset system activity logs at system startup.
- Package isag (interactive stats grapher).

* Mon Apr 10 2006 Victor Forsyuk <force@altlinux.ru> 6.1.1-alt1
- 6.1.1

* Wed Nov 30 2005 Victor Forsyuk <force@altlinux.ru> 6.0.2-alt1
- 6.0.2
- Set values in `make' command invocation arguments instead of patching
  build configuration file.
- Fix for #6209 (see also RH #37733).
- Fix for correct multiarch build.

* Mon May 16 2005 Victor Forsyuk <force@altlinux.ru> 6.0.0-alt1
- 6.0.0

* Tue Mar 01 2005 Victor Forsyuk <force@altlinux.ru> 5.1.5-alt1
- Build latest development version.

* Fri Nov 05 2004 Victor Forsyuk <force@altlinux.ru> 5.0.6-alt1
- 5.0.6

* Wed May 19 2004 Victor Forsyuk <force@altlinux.ru> 5.0.3-alt1
- 5.0.3

* Sat Aug 30 2003 Victor Forsyuk <force@altlinux.ru> 4.0.7-alt2
- Fixed NLS initialization (patch adding LC_CTYPE setlocale setting).
- Summarize previous day's activity with sa2, not current.
- Fixed permissions of cron scripts (added exec bit).

* Mon Jun 09 2003 Victor Forsyuk <force@altlinux.ru> 4.0.7-alt1
- Added URL.
- Added FAQ to package docs.
- nls patch from PLD.
- Proper configuration before build.

* Wed Sep 25 2002 Stanislav Ievlev <inger@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Mon Oct 15 2001 Stanislav Ievlev <inger@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Sat Feb 24 2001 Dmitry V. Levin <ldv@fandra.org> 3.3.5-ipl1
- 3.3.5

* Sun Feb 04 2001 Dmitry V. Levin <ldv@fandra.org> 3.3.4-ipl1
- 3.3.4

* Sat Jan 27 2001 Dmitry V. Levin <ldv@fandra.org> 3.3.3-ipl1
- RE adaptions.

* Tue Jan 17 2001 Preston Brown <pbrown@redhat.com>
- iostat man page fixes

* Fri Jan 05 2001 Preston Brown <pbrown@redhat.com>
- 3.3.3, crontab fixes

* Fri Dec 29 2000 Bill Nottingham <notting@redhat.com>
- fix prereqs

* Fri Oct 13 2000 Preston Brown <pbrown@redhat.com>
- crontab entry was still incorrect.  Fixed.

* Mon Oct 09 2000 Preston Brown <pbrown@redhat.com>
- make sure disk accounting is enabled to fix iostat -l, -p (#16268)
- crontab entries were missing the user (root) to run as (#18212)

* Tue Aug 22 2000 Preston Brown <pbrown@redhat.com>
- enable IO accounting now that kernel supports it

* Wed Aug 16 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix buildrooting (#16271)

* Tue Aug 08 2000 Preston Brown <pbrown@redhat.com>
- bugfixes in 3.2.4 cause our inclusion. :)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 29 2000 Preston Brown <pbrown@redhat.com>
- 3.2.3 fixes SMP race condition

* Tue Jun 20 2000 Preston Brown <pbrown@redhat.com>
- FHS macros
- 3.2.2

* Fri May 26 2000 Preston Brown <pbrown@redhat.com>
- packaged for Winston
- change va patch to indicate kernel is not patched for iostat accounting.
  re-enable if our stock kernel gets this patch.
- upgrade to 3.2.
- install crontab entry.

* Sun Dec 12 1999  Ian Macdonald <ian@caliban.org>
- upgraded to 2.2

* Fri Oct 29 1999  Ian Macdonald <ian@caliban.org>
- first RPM release (2.1)
