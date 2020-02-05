Name: libisc-export-dhcp
Version: 9.11.15
Release: alt1

Summary: ISC BIND 9.9.x exportable libraries to build ISC DHCP
License: MPL-2.0
Group: System/Libraries
Url: http://www.isc.org/products/BIND/

%define vsuffix -P5
# NOTE: vsuffix removed from Source0
# ftp://ftp.isc.org/isc/bind9/%version%vsuffix/bind-%version%vsuffix.tar.gz
Source0: bind-%version.tar

# NB: there must be at least one patch :)
Patch0001: 0001-owl-warnings.patch
Patch0002: 0002-alt-owl-chroot.patch
Patch0003: 0003-alt-nofile.patch
Patch0004: 0004-Link-libirs-with-libdns-libisc-and-libisccfg.patch

Obsoletes: libisc-export <= 9.9.9

%def_disable static
%def_enable ipv6
%def_with openssl

# due to broken configure script
BuildPreReq: gcc-c++

%{?_with_openssl:BuildPreReq: libssl-devel}

%define bind_export_libs isc dns isccfg irs

%package devel
Summary: ISC 9.9.x BIND development files for exportable libraries
Group: Development/C
Requires: %name = %version-%release
Obsoletes: libisc-export-devel <= 9.9.9

%description
This package contains shared libraries used to build ISC DHCP

%description devel
This package contains develompent files for ISC 9.9.x BIND libraries
used to build ISC DHCP.

%prep
%setup -n bind-%version

# NB: there must be at least one patch :)
%patch0001 -p2
%patch0002 -p2
%patch0003 -p2
%patch0004 -p2

sed -i '/# Large File/iAC_SYS_LARGEFILE' configure.ac

%build
%autoreconf
%configure \
	--localstatedir=/var \
	--with-randomdev=/dev/random \
	--disable-threads \
	--disable-linux-caps \
	 %{subst_with openssl} \
	 %{subst_enable ipv6} \
	 %{subst_enable static} \
	--enable-rrl \
	--enable-fetchlimit \
	--enable-exportlib \
	--with-export-libdir=%{_libdir} \
	--with-export-includedir=%{_includedir} \
	--includedir=%{_includedir}/bind9 \
	--disable-openssl-version-check \
	--with-libtool \
	--with-gssapi=no \
	--disable-isc-spnego \
	--without-python \
	#

sed -i \
	-e '/^SUBDIRS =/s/.*/SUBDIRS = make lib/i' \
	Makefile

sed -i -e \
	"/^SUBDIRS =/s/.*/SUBDIRS = %bind_export_libs/i" \
	lib/Makefile

for lib in %bind_export_libs
do
	find .  -name Makefile -exec sed  "s/lib${lib}\./lib${lib}-export\./g" -i {} \;
done;

%make_build

%install
%makeinstall_std

%define _unpackaged_files_terminate_build 1

%files
%_libdir/lib*-export.so.*
%exclude %_bindir/*
%exclude %_mandir/*/*
%exclude %_sysconfdir/*

%files devel
%_includedir/*
%_libdir/lib*-export.so

%changelog
* Fri Jan 24 2020 Mikhail Efremov <sem@altlinux.org> 9.11.15-alt1
- Build without python.
- Fixed build without gssapi.
- Updated patches.
- Updated license.
- Updated to 9.11.15.

* Wed Dec 05 2018 Mikhail Efremov <sem@altlinux.org> 9.11.5-alt1
- Updated to 9.11.5.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 9.9.11-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Aug 30 2017 Mikhail Efremov <sem@altlinux.org> 9.9.11-alt1
- Updated to 9.9.11.

* Fri Feb 03 2017 Mikhail Efremov <sem@altlinux.org> 9.9.9-alt3
- Obsolete libisc-export.

* Wed Feb 01 2017 Mikhail Efremov <sem@altlinux.org> 9.9.9-alt2
- Fix failover initialization in dhcpd (closes: #31158).
- Drop unneeded files.
- Rename to libisc-export-dhcp.
- Build export libraries only.

* Sat Jan 07 2017 Dmitry V. Levin <ldv@altlinux.org> 9.9.9-alt1
- 9.9.8-P4 -> 9.9.9-P5.
- Implemented early drop of linux capabilities.

* Wed Nov 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 9.9.8-alt5
- Applied upstream fix for CVE-2016-8864.

* Tue Sep 27 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 9.9.8-alt4
- Applied upstream fix for CVE-2016-2776.

* Thu Mar 10 2016 Fr. Br. George <george@altlinux.ru> 9.9.8-alt3
- Update to ftp://ftp.isc.org/isc/bind9/9.9.8-P2/bind-9.9.8-P4.tar.gz
- Build with --enable-fetchlimit (Closes: #31701)

* Wed Jan 20 2016 Fr. Br. George <george@altlinux.ru> 9.9.8-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.8-P2/bind-9.9.8-P3.tar.gz

* Thu Dec 17 2015 Fr. Br. George <george@altlinux.ru> 9.9.8-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.8-P2/bind-9.9.8-P2.tar.gz

* Thu Sep 03 2015 Fr. Br. George <george@altlinux.ru> 9.9.7-alt3
- Update to ftp://ftp.isc.org/isc/bind9/9.9.7-P3/bind-9.9.7-P3.tar.gz

* Wed Jul 29 2015 Fr. Br. George <george@altlinux.ru> 9.9.7-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.7-P2/bind-9.9.7-P2.tar.gz

* Tue Jul 28 2015 Fr. Br. George <george@altlinux.ru> 9.9.7-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.7-P1/bind-9.9.7-P1.tar.gz
- CVE-2015-5477 fix

* Thu Dec 11 2014 Fr. Br. George <george@altlinux.ru> 9.9.6-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.6-P1/bind-9.9.6-P1.tar.gz

* Tue Nov 18 2014 Fr. Br. George <george@altlinux.ru> 9.9.6-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.6/bind-9.9.6.tar.gz
- Fix old style autoheader AC_DEFINE
- Enable ratelimits (Closes: #30398)
- Provide initial rndc_keygen (Closes: #28034)

* Mon Oct 06 2014 Fr. Br. George <george@altlinux.ru> 9.9.5-alt3
- Build with GSSAPI

* Tue Jun 17 2014 Fr. Br. George <george@altlinux.ru> 9.9.5-alt2
- Updated to ftp://ftp.isc.org/isc/bind9/9.9.5-P1/bind-9.9.5-P1.tar.gz

* Mon Feb 03 2014 Fr. Br. George <george@altlinux.ru> 9.9.5-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.5/bind-9.9.5.tar.gz
- Don't package bind9-config (in favour of lib*-export)

* Thu Nov 28 2013 Fr. Br. George <george@altlinux.ru> 9.9.4-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.4-P1/bind-9.9.4-P1.tar.gz
- (CVE-2013-6230 is fixed in this version)

* Tue Oct 01 2013 Fr. Br. George <george@altlinux.ru> 9.9.4-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.4/bind-9.9.4.tar.gz

* Sun Jul 28 2013 Fr. Br. George <george@altlinux.ru> 9.9.3-alt3
- Update to ftp://ftp.isc.org/isc/bind/9.9.3-P2/bind-9.9.3-P2.tar.gz

* Tue Jun 11 2013 Fr. Br. George <george@altlinux.ru> 9.9.3-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.3-P1/bind-9.9.3-P1.tar.gz

* Thu Jun 06 2013 Fr. Br. George <george@altlinux.ru> 9.9.3-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.3/bind-9.9.3.tar.gz
- Drop alt-isc-config.patch

* Thu Mar 28 2013 Fr. Br. George <george@altlinux.ru> 9.9.2-alt5
- Update to ftp://ftp.isc.org/isc/bind9/9.9.2-P2/bind-9.9.2-P2.tar.gz
- Turn regex support off

* Fri Dec 28 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt4
- Service file fixup

* Tue Dec 11 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt3
- Update to 9.9.2-P1 (CVE-2012-5688 and bugfixes)
- Add systemd service file (from FC)

* Wed Nov 07 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt2
- Fix pidfile recreation try on reload
- Replace index IDs in patches to dummy ones

* Wed Oct 17 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt1
- Version up to 9.9.2 (CVE 5166 included)

* Wed Oct 15 2012 Fr. Br. George <george@altlinux.ru> 9.9.1-alt1
- Version up to 9.9.1-P3 (6 middle versions jump!)
- Drop outdated patches (including CVE 5166, this is insecure build)
- Adapt actual patches

* Wed Oct 10 2012 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt8
- Imported fixes for several vulnerabilities from RH bind-9.3.6-20.P1.5
  (CVE-2012-{1033,1667,4244,5166}).

* Fri Dec 16 2011 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt7
- Imported fixes for several DNSSEC vulnerabilities from RH bind
  (CVE-2009-4022, CVE-2010-0097, CVE-2010-3762, CVE-2011-4313);
  note that DNSSEC is not enabled by default.
- Enabled IPv6 support.
- Fixed RPATH issue.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt6
- Rebuilt with libcrypto.so.10.

* Tue Jul 28 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt5
- Backported upstream fix for a remote DoS bug (CVE-2009-0696).

* Thu Apr 30 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt4
- Removed resolver(5) manual page (closes: #19784).

* Fri Mar 06 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt3
- options.conf:
  + Removed root-delegation-only directive.
  + Added interface-interval directive example.
- Made "max open files" limit by default as large as default "max sockets" limit.

* Wed Jan 07 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt2
- Updated to 9.3.6-P1 release.

* Mon Nov 24 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt1
- Updated to 9.3.6 release.

* Sun Aug 10 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt4
- Implemented automatic fdsets expansion to overcome FD_SETSIZE limit.

* Thu Aug 07 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt3
- Updated to 9.3.5-P2 release.

* Fri Jun 06 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt2
- Updated to 9.3.5-P1 release (fixes VU#800113/CVE-2008-1447).

* Wed Apr 16 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt1
- Updated to 9.3.5 release.

* Mon Nov 05 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt5
- options.conf: Added recursing-file directive.
- Updated L.ROOT-SERVERS.NET: 198.32.64.12 -> 199.7.83.42.

* Tue Jul 24 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt4
- Updated to 9.3.4-P1 release (fixes CVE-2007-2926).

* Fri Apr 06 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt3
- rndc-confgen: Revert previous change.
- Changed startup script to use /dev/urandom as a source
  of randomness during rndc key generation.

* Wed Apr 04 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt2
- rndc-confgen: Restore default key size (#11321).

* Thu Jan 25 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt1
- Updated to 9.3.4 release.

* Fri Dec 29 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt2
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Dec 09 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt1
- Updated to 9.3.3 release.

* Fri Nov 03 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt0.2
- Updated to 9.3.3 RC3.

* Sat Sep 23 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt0.1
- Updated to 9.3.3 RC2.

* Wed Sep 06 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.2-alt2
- Updated to 9.3.2 P1.

* Thu Mar 30 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.2-alt1
- Updated to 9.3.2 release.

* Tue Sep 27 2005 Dmitry V. Levin <ldv@altlinux.org> 9.3.1-alt2
- Fixed /etc/syslog.d/bind bug introduced in previous release:
  /etc/syslog.d/* must be absolute symlinks.

* Wed Sep 21 2005 Dmitry V. Levin <ldv@altlinux.org> 9.3.1-alt1
- Updated to 9.3.1 release.
- Synced with Owl's bind-9.3.1-owl1 package.
- Applied few fixes from RH and SuSE bind packages.
- Merged all shared libraries into single package, libbind.
- Replaced -debug and -slave subpackages with control facilities.
- Converted absolute symlinks into relative.

* Sat Feb 12 2005 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rel-alt2
- Fixed build of queryperf utility on x86_64 platform (closes #6083).

* Fri Sep 24 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rel-alt1
- Updated to 9.2.4 release (== 9.2.4rc8).

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rc8-alt1
- Updated to 9.2.4rc8.
- Renamed subpackage according to soname change:
  libdns11 -> libdns16.
- Updated startup script to make use of new "status --lockfile" option.

* Wed Jun 30 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rc5-alt1
- Updated to 9.2.4rc5.
- Updated patches.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 9.2.3.rel-alt2.1
- Rebuilt with openssl-0.9.7d.

* Wed Mar 10 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rel-alt2
- Updated build dependencies.
- Do not build static library by default.

* Mon Nov 24 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rel-alt1
- Updated to 9.2.3 release.
- Rediffed patches.
- Do not package .la files.
- named.8: fixed reference to the BIND 9 Administrator Reference Manual.

* Mon Sep 22 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc4-alt1
- Updated to 9.2.3rc4.
- Renamed subpackage according to soname change:
  libdns10 -> libdns11.
- Replaced "delegation-only" defaults implemented in previous release
  with new option, root-delegation-only, and enabled it by default.

* Thu Sep 18 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc2-alt1
- Updated to 9.2.3rc2.
- Renamed subpackage according to soname change:
  libdns9 -> libdns10.
- Marked all known gTLDs and ccTLDs as delegation-only by default.

* Thu Sep 11 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc1-alt2
- Merged patches from OpenBSD, thanks to Jarno Huuskonen:
  + write pidfile before chroot (#2866);
  + use chroot jailing by default, no -u/-t options are necessary;
- Make named-checkconf use chroot jail by default (Jarno Huuskonen).
- options.conf: added few samples (#2968).

* Tue Aug 26 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc1-alt1
- Updated to 9.2.3rc1.
- Removed alt-lib_dns_rootns patch (merged upstream).
- Explicitly disable use of linux capabilities.
- Renamed subpackages according to soname changes:
  libdns8 -> libdns9, libisc4 -> libisc7.

* Tue Jul 29 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rel-alt2
- Fixed message from 'service bind reload' (#0002411).
- Moved 'include "/etc/rfc1912.conf";' directive
  from bind.conf to local.conf (#0002791).
- Rewritten start/stop script to new rc scheme.

* Tue Mar 04 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rel-alt1
- Updated to 9.2.2 release.

* Wed Feb 12 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rc1-alt2
- Relocated initial rndc key generation from %%post to startup script.
- Added some information about ALT specific to named(8) and rndc(8).
- Added README.ALT.

* Thu Feb 06 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rc1-alt1
- Migrated to 9.2.2rc1.
- Build --with-libtool --with-openssl --disable-ipv6 --disable-threads.
- Do not package contrib.
- Package queryperf utility.
- Package each shared library separately:
  libdns8 libisc4 libisccc0 libisccfg0 liblwres1.
- Package lwresd separately (chrooted to /var/resolv).
- Moved %_chrootdir/zone/slave to separate subpackage, %name-slave.
- Moved %_chrootdir/var/run to separate subpackage, %name-debug.
- Added nslookup(1) and resolver(5) manpages from bind8.
- Minor manpage corrections.
- isc-config.sh: fixed --cflags.
- libdns: updated root_ns list to 2002110501.
- rndc-confgen: added "-A" option support.
- Implemented default rndc settings.
- named: patched to get correct chroot jailing support.
- Updated chroot jail and relocated it to /var/lib/bind:
  default CE is now readonly.
- Renamed %_initdir/named to %_initdir/bind.
- Merged caching-nameserver into bind package.
- Split named.conf into several configurations files.
- Added more rfc1912 zones by default.
- Added rfc1918 zones (not enabled by default).

* Wed Nov 13 2002 Dmitry V. Levin <ldv@altlinux.org> 8.3.3-alt2
- Security fixes from ISC:
  + 1469. buffer length calculation for PX was wrong.
  + 1468. ns_name_ntol() could overwite a zero length buffer.
  + 1467. off by one bug in ns_makecannon().
  + 1466. large ENDS UDP buffer size could trigger a assertion.
  + 1465. possible NULL pointer dereference in db_sec.c
  + 1464. the buffer used to construct the -ve record was not
    	  big enough for all possible SOA records.  use pointer
    	  arithmetic to calculate the remaining size in this
    	  buffer.
  + 1463. use serial space arithmetic to determine if a SIG is
    	  too old, in the future or has internally constistant
    	  times.
  + 1462. write buffer overflow in make_rr().
- Changed named.init:
  + added condreload();
  + fixed argument for "-c" option.
- Changed bind chroot jail:
  + removed /var/lib;
  + removed /etc/{host,nsswitch}.conf;
  + added /etc/{protocols,services}.
- Use subst instead of perl in %%post script.
- Dont't calc perl dependencies for -contrib.

* Mon Jul 01 2002 Dmitry V. Levin <ldv@altlinux.org> 8.3.3-alt1
- Updated code to 8.3.3 release.
- Explicitly use mksock from fileutils.
- Fixed build when glibc-core-archopt is installed.
- Updated packager information.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 8.3.1-alt1
- Updated code to 8.3.1 release.
- Fixed bind to use /dev/null from core system.
- Make use of syslogd-1.4.1-alt9 /etc/syslog.d/ feature.
- Renamed /etc/chroot.d/named.* to /etc/chroot.d/bind.*
- Relaxed dependencies (conflicts instead of requires).

* Wed Oct 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.5-alt1
- 8.2.5

* Tue Sep 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt3
- Corrected manpages according to chrooted scheme.
- More manpages moved to man-pages package.

* Tue Jul 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt2
- Moved chroot from /var/named to %_localstatedir/named (according to FHS).
- Merged bind-chroot into main package.
- Updated scripts to handle new syslogd.
- Removed restart support from named.

* Thu May 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt1
- 8.2.4

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.3-ipl4mdk
- Updated PreReqs.

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl3mdk
- Fixed %%devel subpackage.

* Wed Jan 31 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl2mdk
- Pacthed db_defs.h to ease finding errors.
- Added %%triggerpostun.
- Added call for chrooted environment adjustment before server start.

* Sun Jan 28 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl1mdk
- 8.2.3
- Ported to new chrooted scheme.

* Thu Nov 16 2000 Dmitry V. Levin <ldv@fandra.org> 8.2.2_P7-ipl1mdk
- 8.2.2_P7
- Moved chrooted environment to separate subpackage.
- Removed few manpages, obsoleted by new man-pages package.

* Sat May 13 2000 Dmitry V. Levin <ldv@fandra.org>
- xfer tmpdir patch
- chrooted environment fix

* Fri Mar 10 2000 Dmitry V. Levin <ldv@fandra.org>
- fixed startup script to exit with error if no configuration available
- updated to rpm-3.0.4

* Thu Nov 11 1999 Dmitry V. Levin <ldv@fandra.org>
- 8.2.2-P3

* Sun Oct 31 1999 Dmitry V. Levin <ldv@fandra.org>
- chrooted environment
- doc and contrib packages
- optimal manpage compression
- Fandra adaptions

* Sat Oct 09 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Add lame server patch

* Fri Jul 16 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 8.2.1

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Wed Mar 31 1999 Bill Nottingham <notting@redhat.com>
- add ISC patch
- add quick hack to make host not crash
- add more docs

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add probing information in the init file to keep linuxconf happy
- dont strip libbind

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- removed 'done' output at named shutdown.

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- version 8.2

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- patch to use the __FDS_BITS macro
- build for glibc 2.1

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- change named.restart to /usr/sbin/ndc restart

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- install man pages correctly.
- change K10named to K45named.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- don't start if /etc/named.conf doesn't exist.

* Sat Aug  8 1998 Jeff Johnson <jbj@redhat.com>
- autmagically create /etc/named.conf from /etc/named.boot in %post
- remove echo in %post

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- merge in 5.1 mods

* Sun Apr 12 1998 Manuel J. Galan <manolow@step.es>
- Several essential modifications to build and install correctly.
- Modified 'ndc' to avoid deprecated use of '-'

* Mon Dec 22 1997 Scott Lampert <fortunato@heavymetal.org>
- Used buildroot
- patched bin/named/ns_udp.c to use <libelf/nlist.h> for include
  on Redhat 5.0 instead of <nlist.h>
