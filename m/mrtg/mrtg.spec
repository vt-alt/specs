Name: mrtg
Version: 2.17.7
Release: alt1

Summary: Multi Router Traffic Grapher
Group: Monitoring
License: GPL-2.0+
Url: http://oss.oetiker.ch/mrtg/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: http://oss.oetiker.ch/mrtg/pub/%name-%version.tar.gz
Source1: mrtg.cfg
Source4: mrtg.cron.d
Source5: mrtg.iptables
Source6: mrtg-lo0.cfg
Source7: mrtg.cpuinfo
Source8: README.ALT-ru_RU.KOI8-R
PreReq: sysstat

BuildRequires: fontconfig freetype2-devel groff-base libgd2-devel libjpeg-devel libpng-devel perl-Math-BigInt perl-Net-SNMP zlib-devel
BuildRequires: perl-Pod-Parser

%description
The Multi Router Traffic Grapher (MRTG) is a tool to monitor the traffic
load on network-links. MRTG generates HTML pages containing GIF or PNG
images which provide a LIVE visual representation of this traffic.

%package contrib
Summary: Multi Router Traffic Grapher - contribs
Group: Monitoring
AutoReq: no
Requires: %name = %version-%release

%description contrib
Scripts in contrib/ directory of MRTG source distribution

%define _contentdir /var/www/html/%name
%define _libmrtg /usr/lib/%{name}2

%define _perl_lib_path %_libmrtg
%add_findprov_skiplist */contrib/*
%add_findprov_skiplist */helpers/*

%prep
%setup -q
echo "Removing .orig's..."
find . -name "*.orig" -print0 -exec rm -f \{\} \; \
 > /dev/null

%__cp -p %SOURCE8 .

%__mv -f COPYING COPYING.orig
%__ln_s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%configure
%make_build

find contrib -type f -print0 -exec %__perl -pi \
 -e 's;^#!/.*/perl.*;#!/usr/bin/perl;gi' \{\} \; \
 > /dev/null

find contrib -type f -print0 -exec %__perl -pi \
 -e 's;/usr/local/bin/;/usr/bin/;gi' \{\} \; \
 > /dev/null

find contrib -type f -print0 -exec %__perl -pi \
 -e 's;/usr/local/mrtg/(bin/)?mrtg;/usr/bin/mrtg;gi' \{\} \; \
 > /dev/null

find . -name "*.pl" -print0 -exec %__perl -pi -e 's;\015;;gi' \{\} \; \
 > /dev/null

#tar -cf - contrib | gzip -9nf > contrib.tar.gz

%install
%make_install DESTDIR=%buildroot install
%__rm -rf %buildroot{%_docdir,%_datadir}/mrtg2

# another try to work around x86_64
if [ "%_libdir" == "/usr/lib64" ]; then
	%__mkdir -p %buildroot/usr/lib
	%__mv %buildroot%_libdir/mrtg2 %buildroot/usr/lib
	%__rm -rf %buildroot%_libdir
fi

# get rid of a copy of standard Pod perl modules
%__rm -rf %buildroot%_libmrtg/Pod

%__mkdir -p %buildroot{%_sysconfdir/%name,%_sysconfdir/cron.d,%_contentdir/images,%_libmrtg/helpers,%_localstatedir/%name}

%__install -m 644 images/* %buildroot%_contentdir/images
%__install -m 644 %SOURCE1 %buildroot%_sysconfdir/%name
%__install -m 640 %SOURCE4 %buildroot%_sysconfdir/cron.d/%name

%__install -m 755 %SOURCE5 %buildroot/%_libmrtg/helpers/iptables-accounting.pl
%__install -m 644 %SOURCE6 %buildroot%_sysconfdir/%name
%__install -m 755 %SOURCE7 %buildroot/%_libmrtg/helpers/cpuinfo.pl

%__cp -r contrib %buildroot%_libmrtg/

%pre
/usr/sbin/groupadd -r -f %name &> /dev/null ||:
/usr/sbin/useradd -r -g %name -d /dev/null -s /dev/null -n %name &> /dev/null ||:

%files
%doc CHANGES COPYRIGHT MANIFEST README README.ALT-ru_RU.KOI8-R THANKS
%doc --no-dereference COPYING

%config(noreplace) %_sysconfdir/%name/mrtg*.cfg
%config(noreplace) %attr(640,root,root) %_sysconfdir/cron.d/%name
%dir %attr(3770,root,mrtg) %_sysconfdir/%name
%dir %attr(3775,root,mrtg) %_contentdir
%dir %attr(3775,root,mrtg) %_localstatedir/%name
%dir %_libmrtg
%dir %_libmrtg/helpers

%dir %_contentdir/images
%_contentdir/images/*
%_man1dir/indexmaker*.1*
%_man1dir/cfgmaker*.1*
%_man1dir/mrtg*.1*
%_bindir/*
%_libmrtg/*.pm
%_libmrtg/helpers/*

%files contrib
%dir %_libmrtg/contrib
%_libmrtg/contrib/*

%changelog
* Fri Jul 24 2020 Andrey Cherepanov <cas@altlinux.org> 2.17.7-alt1
- NMU: 2.17.7 (ALT #38128)
- Fix changelog dates and remove descriptions in KOI8.
- Fix License tag according to SPDX.

* Sun Dec 18 2011 Ilya Mashkin <oddity@altlinux.ru> 2.17.3-alt1
- 2.17.3

* Tue Mar 01 2011 Ilya Mashkin <oddity@altlinux.ru> 2.17.2-alt1
- 2.17.2

* Thu Jan 20 2011 Ilya Mashkin <oddity@altlinux.ru> 2.17.0-alt1
- 2.17.0

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 2.16.4-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Aug 23 2010 Ilya Mashkin <oddity@altlinux.ru> 2.16.4-alt1
- 2.16.4

* Mon Feb 15 2010 Ilya Mashkin <oddity@altlinux.ru> 2.16.3-alt1
- 2.16.3

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 2.16.2-alt1
- 2.16.2

* Mon Oct 09 2006 Andrei Bulava <abulava@altlinux.ru> 2.14.7-alt1
- 2.14.7
- fixed URL of a source archive file
- changed ownership and access rights of directories which were
  previously owned by user 'mrtg'
- removed ugly hacks regarding update from 2.9.29-alt1 (hacks
  were introduced by 2.10.12-alt1)

* Mon Aug 07 2006 Andrei Bulava <abulava@altlinux.ru> 2.14.5-alt1.1
- rebuilt

* Mon Jul 24 2006 Andrei Bulava <abulava@altlinux.ru> 2.14.5-alt1
- 2.14.5

* Tue Jul 11 2006 Andrei Bulava <abulava@altlinux.ru> 2.14.4-alt1
- 2.14.4

* Fri May 19 2006 Andrei Bulava <abulava@altlinux.ru> 2.14.3-alt1
- 2.14.3

* Wed May 03 2006 Andrei Bulava <abulava@altlinux.ru> 2.14.1-alt1
- 2.14.1
- updated Url following upstream

* Mon Feb 27 2006 Andrei Bulava <abulava@altlinux.ru> 2.13.2-alt2
- removed the lame hack (blame on me) around %%_libdir which was
  introduced in the previous build
- worked around x86_64 issues in a plain and dirty way
- got rid of a copy of standard Pod perl modules

* Mon Feb 13 2006 Andrei Bulava <abulava@altlinux.ru> 2.13.2-alt1
- 2.13.2
- hardcoded %%_libdir for non-x86 archs as /usr/lib (look at the beginning
  of the spec file for grounds)
- made the packaged cfg files to be independent on LANG environment
  variable (#7353)

* Sun Feb 05 2006 Andrei Bulava <abulava@altlinux.ru> 2.13.1-alt1
- 2.13.1
- didn't package html documentation (following upstream)
- didn't package 14all.cgi (anyone is encouraged to package it -
  see http://my14all.sourceforge.net/ and decide yourself, because
  previously packaged 14all.cgi was outdated anyway)
- minor spec cleanups: license, %%make_install, an orphaned directory

* Sat Jun 25 2005 Andrei Bulava <abulava@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Mon Jun 06 2005 Andrei Bulava <abulava@altlinux.ru> 2.12.1-alt1
- 2.12.1
- removed deletion of mrtg pseudouser from postuninstall scriptlet (#6973)
- updated configuration examples to produce proper xhtml output conforming
  with changes in mrtg-2.12.0

* Wed Jan 12 2005 Andrei Bulava <abulava@altlinux.ru> 2.11.1-alt1
- 2.11.1

* Mon Dec 27 2004 Andrei Bulava <abulava@altlinux.ru> 2.11.0-alt1
- 2.11.0
- added README.ALT-ru_RU.KOI8-R
- changed /etc/cron.d/mrtg permissions from 750 to 640
- /etc/cron.d/mrtg has example cron jobs commented by default from now
- updated BuildRequires

* Thu Jun 10 2004 Andrei Bulava <abulava@altlinux.ru> 2.10.14-alt1
- 2.10.14

* Tue Feb 17 2004 Andrei Bulava <abulava@altlinux.ru> 2.10.13-alt2
- minor spec fixes:
  + nullified garbage output
  + used macros where possible

* Fri Jan 30 2004 Andrei Bulava <abulava@altlinux.ru> 2.10.13-alt1
- 2.10.13

* Fri Jan 16 2004 Andrei Bulava <abulava@altlinux.ru> 2.10.12-alt1
- 2.10.12
- package split (contrib directory from mrtg tarball to %name-contrib)
- spec fixes:
  + corrected dependencies
  + fixed problem with unconditional 'userdel mrtg' in POSTUN
  + minor changes to conform with Secure Packaging Policy

* Tue May 06 2003 Nikita Gergel <fc@altlinux.ru> 2.9.29-alt1
- 2.9.29

* Wed Apr 09 2003 Nikita Gergel <fc@altlinux.ru> 2.9.28-alt1
- 2.9.28
- specfile fixes

* Wed Mar 26 2003 Nikita Gergel <fc@altlinux.ru> 2.9.27-alt1
- 2.9.27

* Thu Oct 31 2002 Nikita Gergel <fc@altlinux.ru> 2.9.25-alt1
- 2.9.25

* Mon Oct 21 2002 Michael Shigorin <mike@altlinux.ru> 2.9.22-alt1
- 2.9.22 (minor bugfixes)
- built with gcc3.2
- spec cleanup
- proper Group
- docs images symlinked around
- "no-one's" files in mrtg dirs are searched and overtaken after install

* Fri Jul 05 2002 Michael Shigorin <mike@altlinux.ru> 2.9.18-alt2
- spec cleanup
- package split (most scripts to mrtg-contrib)
- put two "must have" scripts to %_libmrtg/helpers (cpu, iptables)
- purified helpers/iptables-accounting.pl
- fixed helpers/cpuinfo.pl regarding low uptimes
- sample config is now more consistent with package
- pre-ALT changelog chopped off

* Sat Jun 1 2002 Nikita Gergel <fc@altlinux.ru> 2.9.18-alt1
- New version

* Tue Mar 12 2002 Nikita Gergel <fc@altlinux.ru> 2.9.17-alt8
- bugfix in cpuinfo.pl contrib

* Mon Nov 19 2001 Stanislav Ievlev <inger@altlinux.ru> 2.9.17-alt7
- bugfix in cgi script

* Thu Nov 15 2001 Nikita Gergel <fc@altlinux.ru>
 [2.9.17-alt6]
 - Involved %_contentdir as /var/www/html/%name
 - Some fixes in mrtg.cfg

* Wed Nov 14 2001 Stanislav Ievlev <inger@altlinux.ru>
 [2.9.17-alt5]
- small cleanups. build fixes

* Mon Nov 12 2001 Nikita Gergel <fc@altlinux.ru>
 [2.9.17-alt4]
 - Fixed crontab rules
 - Returned 14all.cgi to package

* Sat Nov 10 2001 Nikita Gergel <fc@altlinux.ru>
 [2.9.17-alt3]
 - Fixed bug in sample mrtg.cfg in machine target
 - Changes in crontab rules

* Sat Oct 20 2001 Nikita Gergel <fc@altlinux.ru>
 [2.9.17-alt2]
 - More merge with ALTLinux(tm) RPM packets making rules

* Sun Oct 14 2001 Nikita Gergel <fc@altlinux.ru>
 [2.9.17-alt1]
 - RPM to Sisyphus released
