Name: hddtemp
Version: 0.4.3
Release: alt1
Epoch: 20110629

Summary: Hard Drive Temperature Monitoring

License: GPLv2+
Group: Monitoring
Url: https://github.com/vitlav/hddtemp

# Source-url: https://github.com/vitlav/hddtemp/archive/v%version.tar.gz
Source: %name-%version.tar

Source2: hddtemp.control
Source3: hddtemp.init
Source4: hddtemp.sysconfig
Source6: hddtemp.service

%description
hddtemp is a tool that gives you the temperature of your IDE, NVME,
SATA or SCSI hard drive by reading S.M.A.R.T. information.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
install -pDm644 data/hddtemp.db %buildroot%_datadir/misc/hddtemp.db
install -pDm755 %SOURCE2 %buildroot%_controldir/hddtemp
install -pDm755 %SOURCE3 %buildroot%_initdir/hddtemp
install -pDm755 %SOURCE4 %buildroot%_sysconfdir/sysconfig/hddtemp
install -pDm644 %SOURCE6 %buildroot%_unitdir/hddtemp.service
install -d %buildroot%_man8dir

%makeinstall_std

%find_lang %name

%pre
%pre_control %name

%post
%post_service %name
%post_control -s wheelonly %name

%preun
%preun_service %name

%files -f %name.lang
%doc README TODO contribs
%_sbindir/hddtemp
%_initdir/hddtemp
%_unitdir/hddtemp.service
%_man8dir/*
%_datadir/misc/hddtemp.db
%config(noreplace) %_sysconfdir/control.d/facilities/hddtemp
%config(noreplace) %_sysconfdir/sysconfig/hddtemp

# TODO:
# - find someone to do privsep/chroot on hddtemp?

%changelog
* Sun Mar 21 2021 Vitaly Lipatov <lav@altlinux.ru> 20110629:0.4.3-alt1
- new version 0.4.3 (with rpmrb script)
 + fix segfault if there is no bus

* Sun Feb 28 2021 Vitaly Lipatov <lav@altlinux.ru> 20110629:0.4.2-alt1
- new version 0.4.2 (with rpmrb script)

* Sun Feb 28 2021 Vitaly Lipatov <lav@altlinux.ru> 20110629:0.4.1-alt1
- new version 0.4.1 (with rpmrb script)

* Sun Feb 28 2021 Vitaly Lipatov <lav@altlinux.ru> 20110629:0.4-alt1
- cleanup spec, build 0.4 from the new upstream (closes: #28054)
 + use minimal database for drives not covered by defaults
 + first try S.M.A.R.T. attribute 194, otherwise try attribute 190
 + add support for NVME bus
 + allow binding to a listen address that doesn't exist yet
 + implement drives auto-detection

* Tue Jun 16 2020 Vitaly Chikunov <vt@altlinux.org> 20110629:0.3-alt15.beta15
- fix crash on numeric output if disk is not in db (closes: #38616)

* Mon Sep 16 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 20110629:0.3-alt14.beta15
- systemd service file added

* Tue Feb 19 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20110629:0.3-alt13.beta15
- NMU: fixed build on i586.

* Sun Feb 10 2013 Sergey Kurakin <kurakin@altlinux.org> 20110629:0.3-alt12.beta15
- i586 build fixed

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 20110629:0.3-alt11.beta15
- added several WD/Hitachi drives (closes: #27586, #27587, #27588)

* Mon Apr 09 2012 Michael Shigorin <mike@altlinux.org> 20110629:0.3-alt10.beta15
- added WDC WD1003FBYX-01Y7B0 (closes: #27186)
  and KINGSTON SNVP325S2128GB (just in case)

* Wed Jun 29 2011 Michael Shigorin <mike@altlinux.org> 20110629:0.3-alt9.beta15
- added Samsung HD204UI (closes: #25832)

* Tue Jul 13 2010 Victor Forsiuk <force@altlinux.org> 20100712:0.3-alt8.beta15
- Use guessed value (i.e. read from the de-facto standard temperature field)
  by default. This allows us to automatically support all modern drives without
  need to add them to database first. Suggestion and patch by Vitaly Lipatov
  (lav@altlinux).

* Mon Jun 15 2009 Michael Shigorin <mike@altlinux.org> 20090615:0.3-alt7.15
- merged hddtemp.db additions (closes: #14864, #14924, #15077, #16198, #20444)
- moved in-spec here document content into a separate source
- moved in-spec subst into another addition

* Tue Mar 11 2008 Victor Forsyuk <force@altlinux.org> 20080311:0.3-alt6.15
- Build with updated hddtemp.db (from 2007-09-14).
- Added new disks suggested in ALT bugzilla.

* Wed Apr 18 2007 Victor Forsyuk <force@altlinux.org> 20070418:0.3-alt5.15
- Added drives from ALT#11037.

* Tue Dec 26 2006 Victor Forsyuk <force@altlinux.org> 20061226:0.3-alt4.15
- Do not start service by default (closes bug#6097).
- Added bunch of drives (closes bugs#9355,9690,10515).

* Wed Jun 07 2006 Victor Forsyuk <force@altlinux.ru> 20060607:0.3-alt3.15
- 0.3.beta15 + fresh hddtemp.db.

* Wed Jan 18 2006 Victor Forsyuk <force@altlinux.ru> 20060118:0.3-alt2.14
- Update with fresh hddtemp.db.

* Thu Sep 29 2005 Victor Forsyuk <force@altlinux.ru> 20050929:0.3-alt1.14
- 0.3.beta14
- Updated hddtemp.db.

* Fri Aug 26 2005 Victor Forsyuk <force@altlinux.ru> 20050826:0.3-alt2.13
- Updated hddtemp.db.

* Fri Apr 22 2005 Victor Forsyuk <force@altlinux.ru> 20050422:0.3-alt1.13
- beta13, updated hddtemp.db.
- Fix URL.

* Sun Jan 04 2004 Michael Shigorin <mike@altlinux.ru> 20040104:0.3-alt1.11
- beta11
- moved to control(8) rpm macros
- removed superfluous groupadd netadmin %%)
- implemented initscript (based on debian's) (127.0.0.1:7634)
- spec cleanup

* Sun Nov 02 2003 Michael Shigorin <mike@altlinux.ru> 20031102:0.3-alt0.84
- added WD1600JB-00DUA3 info (thanks vvzhy@ again)

* Tue Oct 28 2003 Michael Shigorin <mike@altlinux.ru> 20031028:0.3-alt0.83
- *do* apply patch for WD1600JB-00EVA0 support;
  thanks Vadim V. Zhytnikov (vvzhy@)

* Sat Oct 25 2003 Michael Shigorin <mike@altlinux.ru> 0.3-alt0.82
- added WD1600JB-00EVA0; thanks to Mikhail Yakshin (greycat@)

* Mon Sep 22 2003 Michael Shigorin <mike@altlinux.ru> 0.3-alt0.81
- added ST3120026A to hddtemp.db; thanks to Vitaly Lipatov (lav@)

* Wed Aug 13 2003 Michael Shigorin <mike@altlinux.ru> 0.3-alt0.8
- 0.3beta8
- po files included as i18n support got fixed
- tiny spec cleanup

* Thu Jul 03 2003 Michael Shigorin <mike@altlinux.ru> 0.3-alt0.7
- 0.3beta7
- updated %%url
- patches merged into upstream
- spec change due to upstream autoconf'izing (+cleanup)

* Thu Apr 17 2003 Michael Shigorin <mike@altlinux.ru> 0.3-alt0.6
- 0.3beta6

* Fri Mar 14 2003 Michael Shigorin <mike@altlinux.ru> 0.3-alt0.31
- hddtemp.db entry for "Maxtor DiamondMax 16" from Andrey Brindeew <abr>

* Sat Mar 08 2003 Michael Shigorin <mike@altlinux.ru> 0.3-alt0.3
- built for ALT Linux (0.3-beta3)
- moved hddtemp.db to %_datadir/misc
- control support instead of plain suid binary

* Fri Jan 24 2003 Vincent Danen <vdanen@mandrakesoft.com> 0.3-0.beta3.1mdk
- initial contrib from Ben Reser

* Fri Jan 24 2003 Ben Reser <ben@reser.org> 0.3-0.beta3.1brs
- 0.3-beta3
