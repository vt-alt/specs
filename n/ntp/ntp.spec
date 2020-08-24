%define _unpackaged_files_terminate_build 1

Name: ntp
Version: 4.2.8p15
Release: alt1
%define srcname %name-%version%{?patchlevel:%patchlevel}

Summary: The Network Time Protocol (NTP)
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: http://www.ntp.org/

Source0: http://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/%srcname.tar.gz
Source1: ntpd.init
Source2: ntpd.sysconfig
Source3: %name.conf
Source4: %name.keys

Source11: ntp.1
Source12: ntpd.8
Source13: ntpdate.8
Source14: ntpsweep.8

Source21: chrooted-ntpd.all
Source22: chrooted-ntpd.conf
Source23: chrooted-ntpd.lib

Patch1: %name-4.2.6p5-alt-compile-dirty-hack-NANO.patch
Patch2: %name-4.2.8p14-MD5-to-SHA1-default.patch

Requires: ntp-doc = %version-%release
Requires: ntp-utils = %version-%release
Requires: ntpdate = %version-%release
Requires: ntpd = %version-%release

# ntpq subpackage should not have dependency to ntp-utils subpackage:
# man8/ntpq.8 is a symlink to man1/ntp.1 which in ntp-utils
%add_findreq_skiplist %_man8dir/ntpq.*

BuildRequires: zlib-devel

# due to readline library linked with tinfo.
BuildPreReq: libreadline-devel >= 4.3-alt5

# due to ntp_drop_priv.
BuildRequires: libcap-devel

# ntp_crypto_rnd.c:93: undefined reference to `arc4random_buf'
BuildRequires: libssl-devel
# https://bugzilla.altlinux.org/38287
%(rpmquery --qf 'Requires: libcrypto = %%{VERSION}' libssl-devel)

# for sbin/update-leap
BuildRequires: perl-File-Fetch perl-Digest-SHA perl-HTTP-Tiny perl-Net-SSLeay perl-IO-Socket-SSL

# Root directory for chrooted environment, must not be same as real system root.
%define ROOT /var/lib/ntpd

%define common_description The Network Time Protocol (NTP) is used to synchronize the time\
of a computer client or server to another server or reference time\
source, such as a radio or satellite receiver or modem. It provides\
client accuracies typically within a millisecond on LANs and up to\
a few tens of milliseconds on WANs.\
\
Binaries was built with a source code under various free licenses.

%package aux
Summary: The Network Time Protocol (NTP) auxiliary package
Group: System/Configuration/Other
Conflicts: ntp < 4.1.1b
BuildArch: noarch

%package doc
Summary: The Network Time Protocol (NTP) documentation
Group: Development/Other
Requires: ntp-aux = %version-%release
BuildArch: noarch

%package -n perl-NTP-Util
Summary: Perl NTP module
Group: Development/Perl
BuildArch: noarch

%package utils
Summary: The Network Time Protocol (NTP) utilities
Group: System/Base
Requires: ntpdate = %version-%release
Requires: ntpq = %version-%release

%package -n ntpdate
Summary: Set the date and time via NTP
Group: System/Base
Requires: ntp-aux = %version-%release
Requires(pre): shadow-utils
Requires: /var/empty

%package -n ntpq
Summary: The standard NTP query program
Group: System/Base

%package -n ntpd
Summary: The Network Time Protocol daemon
Group: System/Servers
Obsoletes: xntp3
Requires(pre): shadow-utils
Requires(pre): service, coreutils
# due to ntp_intres.
Requires: /var/resolv
Provides: ntp-server

%description
%common_description

%description aux
%common_description

This is an auxiliary package.

%description doc
%common_description

This package contains NTP documentation.

%description -n perl-NTP-Util
Perl NTP module

%description utils
%common_description

This package contains various NTP utilities.

%description -n ntpdate
%common_description

This package contains ntpdate program for retrieving the date and time
from remote machines via a network.

%description -n ntpq
%common_description

This package contains standard NTP query program

%description -n ntpd
%common_description

This package contains Network Time Protocol daemon.

%prep
%setup -n %srcname
%ifarch %e2k
sed -i 's,-Wnormalized=id,,' sntp/libevent/configure*
%endif

#patch1 -p1
%patch2 -p2

# Fix progname initialization when argc==0.
fgrep -rl --include='*.c' 'progname = argv[0];' . |
	xargs grep -l 'main *(' |
	while read f; do
		n="${f##*/}"
		n="${n%%.c}"
		subst 's/progname = argv\[0\];/progname = argc ? argv[0] : "PROGNAME";/' "$f"
		subst "s/PROGNAME/$n/" "$f"
	done

%__install -p -m644 %SOURCE2 ntpd.sysconfig
%__install -p -m644 $RPM_SOURCE_DIR/{ntp.1,{ntpd,ntpdate,ntpsweep}.8} .

find -type f -print0 |
	xargs -r0 %__grep -FZl '@ROOT@' -- |
	xargs -r0 %__subst -p 's,@ROOT@,%ROOT,g' --

%build
%add_optflags -D_GNU_SOURCE
%define _bindir %_sbindir

%autoreconf
%configure \
	--enable-ntp-signd \
	--enable-linuxcaps \
	--without-readline
echo '#define HAVE_LIBREADLINE 1' >>config.h

%make_build

%check
# https://lists.altlinux.org/pipermail/devel/2020-March/210366.html
%ifnarch ppc64le
make check
%endif

%install
make DESTDIR=$RPM_BUILD_ROOT perllibdir=%perl_vendor_privlib install

%__install -p -m755 scripts/ntpsweep/ntpsweep $RPM_BUILD_ROOT%_sbindir/

# Manpages.
%set_compress_method skip
%__mkdir_p $RPM_BUILD_ROOT{%_man1dir,%_man8dir}
#__install -p -m644 ntp.1 $RPM_BUILD_ROOT%_man1dir/
sed "s|@VERSION@|%version|" < ntp.1 > $RPM_BUILD_ROOT%_man1dir/ntp.1
%__install -p -m644 {ntpd,ntpdate,ntpsweep}.8 $RPM_BUILD_ROOT%_man8dir/
find $RPM_BUILD_ROOT%_mandir -type f -regex '.*\.[1-8]$' -print0 | xargs -r0 bzip2 -9
for f in $RPM_BUILD_ROOT%_sbindir/*; do
	t="$RPM_BUILD_ROOT%_man8dir/${f##*/}.8.bz2"
	[ -f "$t" ] || %__ln_s ../man1/ntp.1.bz2 "$t"
done

# Docs.
%define docdir %_docdir/%name-%version
%__mkdir_p $RPM_BUILD_ROOT%docdir
mv $RPM_BUILD_ROOT%_docdir/ntp  $RPM_BUILD_ROOT%docdir
mv $RPM_BUILD_ROOT%_docdir/sntp $RPM_BUILD_ROOT%docdir
%__cp -a COPYRIGHT NEWS TODO WHERE-TO-START README.bk README.hackers README.refclocks README.versions \
	$RPM_BUILD_ROOT%docdir/

%__install -pD -m755 %SOURCE1 $RPM_BUILD_ROOT%_initdir/ntpd
%__install -pD -m644 ntpd.sysconfig $RPM_BUILD_ROOT%_sysconfdir/sysconfig/ntpd
%__install -pD -m600 %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/%name.conf

# Prepare for chroot
%__mkdir_p $RPM_BUILD_ROOT%ROOT/tmp
%__mkdir_p $RPM_BUILD_ROOT%ROOT/%_lib
%__install -pD -m600 %SOURCE4 $RPM_BUILD_ROOT%ROOT%_sysconfdir/%name/keys
touch $RPM_BUILD_ROOT%ROOT%_sysconfdir/%name/{drift,step-tickers}
%__ln_s ..%ROOT%_sysconfdir/%name $RPM_BUILD_ROOT%_sysconfdir/
# scripts for update_chrooted
%__mkdir_p $RPM_BUILD_ROOT%_sysconfdir/chroot.d
%__install -pD -m700 %SOURCE21 $RPM_BUILD_ROOT%_sysconfdir/chroot.d/ntpd.all
%__install -pD -m700 %SOURCE22 $RPM_BUILD_ROOT%_sysconfdir/chroot.d/ntpd.conf
%__install -pD -m700 %SOURCE23 $RPM_BUILD_ROOT%_sysconfdir/chroot.d/ntpd.lib
# ghost files from update_chrooted
touch $RPM_BUILD_ROOT%ROOT%_sysconfdir/host.conf
touch $RPM_BUILD_ROOT%ROOT%_sysconfdir/hosts
touch $RPM_BUILD_ROOT%ROOT%_sysconfdir/localtime
touch $RPM_BUILD_ROOT%ROOT%_sysconfdir/nsswitch.conf
touch $RPM_BUILD_ROOT%ROOT%_sysconfdir/resolv.conf
touch $RPM_BUILD_ROOT%ROOT%_sysconfdir/services
touch $RPM_BUILD_ROOT%ROOT/%_lib/libnsl.so.1
touch $RPM_BUILD_ROOT%ROOT/%_lib/libnss_dns.so.2
touch $RPM_BUILD_ROOT%ROOT/%_lib/libnss_files.so.2
touch $RPM_BUILD_ROOT%ROOT/%_lib/libresolv.so.2

%define r_dir %ROOT%_sysconfdir/%name
%define r_link %_sysconfdir/%name

%pre -n ntpdate
/usr/sbin/groupadd -r -f ntpd
/usr/sbin/useradd -r -g ntpd -d /dev/null -s /dev/null -n ntpd >/dev/null 2>&1 ||:

%pre -n ntpd
/usr/sbin/groupadd -r -f ntpd
/usr/sbin/useradd -r -g ntpd -d /dev/null -s /dev/null -n ntpd >/dev/null 2>&1 ||:
f=%r_link
if [ -d "$f" -a ! -L "$f" ]; then
	%__rm -rf "$f"
	/bin/touch "$f.RPMLOCK"
fi

%post -n ntpd
%_sysconfdir/chroot.d/ntpd.all
if [ $1 = 1 ]; then
        /sbin/chkconfig --add ntpd
fi
d=%r_dir
f=%r_link
if [ -f "$f.RPMLOCK" -a -d "$f" -a ! -d "$d.RPMSAVE" ]; then
	%__mv "$d" "$d.RPMSAVE"
	%__rm -f "$f.RPMLOCK"
else
	/sbin/service ntpd condrestart ||:
fi

%preun -n ntpd
%preun_service ntpd

%triggerpostun -n ntpd -- %name < 4.1.1b
d=%r_dir
if [ -d "$d.RPMSAVE" -a ! -d "$d" ]; then
	%__mv "$d.RPMSAVE" "$d"
	/sbin/service ntpd condrestart ||:
fi

%files

%files aux

%files doc
%dir %docdir
%docdir/ntp
%docdir/sntp
%docdir/[A-Z]*

%files -n perl-NTP-Util
%dir %perl_vendor_privlib/NTP
%perl_vendor_privlib/NTP/Util.pm

%files utils
%_sbindir/*
%_mandir/man?/*
%exclude %_sbindir/ntpd
%exclude %_sbindir/ntpq
%exclude %_sbindir/ntpdate
%exclude %_man1dir/ntpd.*
%exclude %_man1dir/ntpq.*
%exclude %_man8dir/ntpd.*
%exclude %_man8dir/ntpq.*
%exclude %_man8dir/ntpdate.*

%files -n ntpdate
%_sbindir/ntpdate
%_man8dir/ntpdate.*

%files -n ntpq
%_sbindir/ntpq
%_man1dir/ntpq.*
%_man8dir/ntpq.*

%files -n ntpd
%config %_initdir/ntpd
%config(noreplace) %_sysconfdir/sysconfig/ntpd
%config(noreplace) %_sysconfdir/%name.conf
%_sysconfdir/%name
%_sysconfdir/chroot.d/ntpd.*
%_sbindir/ntpd
%_man1dir/ntpd.*
%_man8dir/ntpd.*

%defattr(640,root,ntpd,710)
%dir %ROOT
%dir %ROOT%_sysconfdir
%dir %ROOT/%_lib
%attr(1770,root,ntpd) %dir %ROOT/tmp
%attr(1770,root,ntpd) %dir %ROOT%_sysconfdir/%name
%config(noreplace) %ROOT%_sysconfdir/%name/keys
%config(noreplace) %verify(not md5 size mtime) %ROOT%_sysconfdir/%name/step-tickers
%attr(640,ntpd,ntpd) %ghost %ROOT%_sysconfdir/%name/drift

# ghost files from update_chrooted
%ghost %ROOT%_sysconfdir/host.conf
%ghost %ROOT%_sysconfdir/hosts
%ghost %ROOT%_sysconfdir/localtime
%ghost %ROOT%_sysconfdir/nsswitch.conf
%ghost %ROOT%_sysconfdir/resolv.conf
%ghost %ROOT%_sysconfdir/services
%ghost %ROOT/%_lib/libnsl.so.1
%ghost %ROOT/%_lib/libnss_dns.so.2
%ghost %ROOT/%_lib/libnss_files.so.2
%ghost %ROOT/%_lib/libresolv.so.2

%changelog
* Wed Aug 19 2020 Sergey Y. Afonin <asy@altlinux.org> 4.2.8p15-alt1
- 4.2.8p15

* Sat Apr 04 2020 Sergey Y. Afonin <asy@altlinux.org> 4.2.8p14-alt2
- updated License tag to SPDX syntax, changed to GPL-3.0-or-later
- added ntp-4.2.8p14-MD5-to-SHA1-default.patch (ALT #38300)
- added libcrypto with build version to Requires (ALT #38287)

* Mon Mar 23 2020 Sergey Y. Afonin <asy@altlinux.org> 4.2.8p14-alt1
- 4.2.8p14 (medium security update, look to "NEWS" file)
- disabled alt-compile-dirty-hack-NANO.patch
- disabled "make check" for ppc64le due to --gc-sections problem

* Tue Mar 12 2019 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8p13-alt1
- 4.2.8p13

* Tue Aug 28 2018 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8p12-alt1
- 4.2.8p12 (CVE-2018-12327)

* Tue Aug 14 2018 Michael Shigorin <mike@altlinux.org> 4.2.8p11-alt2
- E2K: avoid lcc-unsupported option
- autoreconf

* Sun Mar 04 2018 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8p11-alt1
- 4.2.8p11 (CVE-2018-7185, CVE-2018-7184, CVE-2018-7170, CVE-2018-7183,
  CVE-2018-7182, CVE-2016-1549)
- updated vniiftri ntp servers in ntp.conf
- added perl-HTTP-Tiny, perl-Net-SSLeay, perl-IO-Socket-SSL to BuildRequires

* Wed Sep 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 4.2.8p10-alt1
- updated to 4.2.8p10 (Fixes: CVE-2017-6451, CVE-2017-6452, CVE-2017-6455,
  CVE-2017-6458, CVE-2017-6459, CVE-2017-6460, CVE-2017-6462, 
  CVE-2017-6463, CVE-2017-6464)
- patch level moved to version to pleasure CVE checkoing tools

* Sun Dec 04 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8-alt8
- fixed version in changelog in 4.2.8-alt7

* Sun Dec 04 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8-alt7
- 4.2.8p9
- built with --enable-ntp-signd (ALT #32313)

* Tue Jul 05 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8-alt6
- 4.2.8p8 (CVE-2016-4957 and other CVEs)

* Mon Mar 21 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8-alt5
- 4.2.8p6
- removed "Packager" from spec
- splitted ntpq to separate subpackage

* Tue Dec 15 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8-alt4
- added files produced by update_chrooted as ghost
- added check section

* Mon Dec 14 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8-alt3
- 4.2.8p4 (multiple CVEs; see "NEWS" file)
- ntpdate is not used in init script (obsoleted by --panicgate),
  removed ntpdate from "Requires" in the ntpd subpackage
- updated chrooted environment (update_chrooted is used now)
- added IPv6 localhost as trusted source
- compressed manual pages

* Tue Jul 07 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8-alt2
- 4.2.8p3
- used chroot by default
- used --panicgate by default

* Mon Dec 22 2014 Sergey Y. Afonin <asy@altlinux.ru> 4.2.8-alt1
- 4.2.8 (ALT #30591, CVEs 2014 9293-9296)
- refactored ntp.conf (ALT #19494#c7)

* Tue Feb 18 2014 Sergey Y. Afonin <asy@altlinux.ru> 4.2.6-alt2
- refactored ntp.conf (temporary solution for ALT #19494)

* Fri Feb 14 2014 Sergey Y. Afonin <asy@altlinux.ru> 4.2.6-alt1
- NMU
- 4.2.6p5 (closes: #27162)
- removed unsupported option from ntp.conf (closes: #27162)
- added "disable monitor" to ntp.conf (CVE-2013-5211)
- moved man1/ntpd.1.gz to ntpd package (closes: #27948)
- added "BuildArch: noarch" for ntp-aux and ntp-doc

* Wed May 20 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt5.p7
- 4.2.4p7
- fix for CVE-2009-1252 (closes: #20099)
- fix for CVE-2009-0159 (closes: #19779)

* Sun Apr 05 2009 Stanislav Ievlev <inger@altlinux.org> 4.2.4-alt4.p6.1
- Provides ntp-server

* Sat Jan 10 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt4.p6
- 4.2.4p6 ( fix for http://www.ocert.org/advisories/ocert-2008-016.html )
- LSB header for init-script

* Sat Apr 05 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt3.p4
- add NTPD_GROUP to /etc/sysconfig/ntpd and init-script

* Tue Apr 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt2.p4
- add ntptrace output to service ntp status (#8411)
  + fix from Denis Smirnov <mithraen@altlinux.ru> in 4.2.2-alt2.p4.3
- add pid-file creation to init-script (#3825)

* Sun Mar 30 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt1.p4
- 4.2.4p4
- fix for #11139 and #13233

* Mon Mar 12 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt1.p0
- 4.2.4p0

* Fri Nov 24 2006 Denis Smirnov <mithraen@altlinux.ru> 4.2.2-alt1.p4.3
- fix buffer overflow in WWV Audio driver (#216309 from fedora)

* Sun Nov 19 2006 Denis Smirnov <mithraen@altlinux.ru> 4.2.2-alt1.p4.2
- Chroot and change user to ntpd by default
- Ignore -T in ntpdate (for compatibility with old /etc/sysconfig/ntp)

* Fri Nov 17 2006 Denis Smirnov <mithraen@altlinux.ru> 4.2.2-alt1.p4.1
- Version update

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 4.1.2-alt3.1
- Rebuilt with libreadline.so.5.

* Tue Apr 20 2004 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt3
- ntpd, ntpdate:
  Do not try to drop privileges when run by unprivileged user.
- ntpd: Create pid file by default.
- Fix progname initialization when argc==0.
- Updated alt-tinfo patch (now called alt-readline patch).

* Sun Feb 15 2004 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt2
- Fixed chroot jailing and droppriv code (#3461).
- Changed default settings:
  ntpd: switch to ntpd:ntpd, chroot to %ROOT;
  ntp_intres: switch to ntpd:ntpd, chroot to /var/resolv;
  ntpdate: switch to ntpd:ntpd, chroot to /var/empty.
- Added auxiliary subpackage for better interpackage dependencies.

* Sun Aug 17 2003 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt1
- Updated to 4.1.2.
- Rewritten start/stop script to new rc scheme.

* Tue Feb 25 2003 Dmitry V. Levin <ldv@altlinux.org> 4.1.1c-alt1.rc1
- Updated to 4.1.1c-rc1.
- More new RH patches to be considered:
  4.1.73-limit, 4.1.1c-loopfilter.

* Tue Nov 19 2002 Dmitry V. Levin <ldv@altlinux.org> 4.1.1b-alt1
- Updated to 4.1.1b.
- Merged in RH patches:
  + ntp-4.1.0b-rc1-genkey
  + ntp-4.1.1a-genkey2
  - ntp-4.1.1a-mfp (not needed in 4.1.1b)
- Updated droproot patch.
- Removed ntp-4.0.99j-rh-vsnprintf patch (merged upstream).
- Enabled (fixed) readline support.
- Packaged ntpsweep.
- Added manpages from Debian
  (and mentioned our chroot support options there).
- Split into several subpackages.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt3
- Updated startup script.
- Updated dependencies.

* Mon Apr 01 2002 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt2
- 4.1.1
- Chrooted by default to %ROOT.
- Updated default config (cornet).

* Wed Oct 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.1.0-alt1
- 4.1.0 (not chrooted yet).

* Thu May 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.0.99k-ipl4mdk
- Conflicts: xntp3
- Use service macros.

* Mon Apr 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.0.99k-ipl3mdk
- Fixed buffer overrun.
- Fixed glibc-2.2.2 compilation.

* Sat Jan 20 2001 Dmitry V. Levin <ldv@fandra.org> 4.0.99k-ipl2mdk
- RE adaptions.

* Thu Aug 31 2000 Warly <warly@mandrakesoft.com> 4.0.99k-2mdk
- add condrestart

* Mon Jul 24 2000 Warly <warly@mandrakesoft.com> 4.0.99k-1mdk
- new release
- BM

* Wed Apr 05 2000 Daouda Lo <daouda@mandrakesoft.com> 4.0.99g-3mdk
- fix the conf files permissions
- bunzip'ed conf files

* Fri Mar 31 2000 Warly <warly@mandrakesoft.com> 4.0.99g-2mdk
- New group: System/Configuration/Other

* Tue Mar 07 2000 Daouda LO <daouda@mandrakesoft.com>
- Mandrakised (relocatable + %%define )

* Sun May 23 1999 David E. Myers <dem@skyline.rtp.nc.us>
- Changes for submission to Red Hat Contrib|Net.

* Wed Apr 14 1999 Cristian Gafton <gafton@redhat.com>
- disallow remote updates by default in ntp.conf (#2170)

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- use %configure
- fix initscript not to sit out the output of ntpdate (use syslog instead)
- eliminate subshell from the install stage

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 9)

* Sun Nov 22 1998 Jeff Johnson <jbj@redhat.com>
- ntp.conf: default local clock stratum to 10.

* Wed Oct 21 1998 Jeff Johnson <jbj@redhat.com>
- update to 5.93e.

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries

* Thu Aug  6 1998 Jeff Johnson <jbj@redhat.com>
- update to 5.93c.
- implement suggestions from James Youngman <JYoungman@vggas.com>:
-   correct default /etc/ntp/keys
-   use /etc/ntp/step-tickers for ntpdate hosts

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- start it after named

* Mon May 04 1998 Jeff Johnson <jbj@redhat.com>
- Update to 5.93.

* Mon Feb  2 1998 Jeff Johnson <jbj@jbj.org>
- Fiddles for RH-5.0. Update to xntp3-5.92.

* Mon Feb  2 1998 Jeff Johnson <jbj@jbj.org>
- Fiddles for RH-5.0. Update to xntp3-5.92.

* Sat Oct 18 1997 Manoj Kasichainula <manojk@io.com>
- Initial release for 5.91
