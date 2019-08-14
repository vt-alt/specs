%define _cyrususer cyrus
%define _cyrusgroup cyrus
%define _vardata %_var/lib/imap
%define _spooldata %_var/spool/imap
%define _cyrexecdir %_libexecdir/cyrus
%define _contribdir %_datadir/%name/contrib

# http://bugzilla.altlinux.org/31381
%def_without unit_tests

# 3.0.8 with python-module-sphinx-1.4 (p8):
# File "./docsrc/exts/sphinxlocal/builders/manpage.py", line 78, in write
#     darkgreen, [docname])
# TypeError: inline_all_toctrees() takes exactly 5 arguments (6 given)
%def_with sphinx

%def_with snmp

Name: cyrus-imapd
Version: 3.0.11
Release: alt1

Summary: A high-performance email, contacts and calendar server
License: CMU License
Group: System/Servers

# fresh sources available at https://github.com/cyrusimap/cyrus-imapd
Url: http://www.cyrusimap.org/

Source0: %name-%version.tar
Source1: cyrus-procmailrc
Source2: cyrus-user-procmailrc.template
Source3: %name.logrotate
Source4: %name.imapd-conf
Source5: README.ALT.rus
Source6: %name.control
Source7: %name.pam-config
Source8: %name-procmail+cyrus.mc
Source10: %name.sysconfig
Source11: %name.cvt_cyrusdb_all
Source12: %name.magic
Source13: %name.sasl-conf
Source14: %name.cron-daily
Source16: folderxfer
Source17: imapcreate.pl
Source18: inboxfer
Source19: %name-README.HOWTO-recover-mailboxes.db
Source20: %name-sendmail-8.12.9-cyrusv2.m4
Source21: %name.init
Source22: %name.cyrus-conf

#Patch7: http://servercc.oakton.edu/~jwade/cyrus/cyrus-imapd-2.1.3/cyrus-imapd-2.1.3-flock.patch

PreReq: e2fsprogs /sbin/chkconfig /sbin/service cert-sh-functions
Requires: su, tzdata
Provides: MDA imap IMAPD POP3D

%if_with unit_tests
BuildRequires: CUnit-devel
BuildRequires: valgrind-devel
%endif

BuildRequires: control flex gcc-c++ transfig libdb4-devel zlib-devel libldap-devel libuuid-devel
BuildRequires: libsasl2-devel libssl-devel libnl-devel libsensors3-devel libpcre-devel libkrb5-devel

%if_with snmp
BuildRequires: libnet-snmp-devel
%endif

# http (CalDAV, CardDAV e.t.c.)
BuildRequires: libjansson-devel libical-devel libxml2-devel libsqlite3-devel

BuildRequires: perl-devel perl-Pod-Parser perl-Term-ReadLine-Gnu perl-Net-Server perl-Unix-Syslog

# 2.5.11
# BuildRequires: python-module-sphinx
# BuildRequires: perl-Pod-POM-View-Restructured

# 3.0.8
BuildRequires: perl-JSON xxd
%if_with sphinx
BuildRequires: perl-Pod-POM-View-Restructured
BuildRequires: python-module-GitPython
BuildRequires: python-module-sphinx >= 1.6
%endif

%description
The Cyrus IMAP (Internet Message Access Protocol) server provides
access to personal mail, system-wide bulletin boards, news-feeds,
calendar and contacts through the IMAP, NNTP, CalDAV and CardDAV
protocols. The Cyrus IMAP server is a scalable enterprise groupware
system designed for use from small to large enterprise environments
using technologies based on well-established Open Standards.

A full Cyrus IMAP implementation allows a seamless mail and bulletin
board environment to be set up across one or more nodes. It differs
from other IMAP server implementations in that it is run on "sealed
nodes", where users are not normally permitted to log in. The mailbox
database is stored in parts of the filesystem that are private to the
Cyrus IMAP system. All user access to mail is through software using
the IMAP, IMAPS, POP3, POP3S, KPOP, CalDAV and/or CardDAV protocols.

%package murder
Group: System/Servers
Summary: Cyrus IMAP server murder aggregator system files
Requires: %name = %version-%release

%description murder
The %name-murder package contains the Cyrus murder aggregator system,
i.e. IMAP, POP3 and LMTP proxies, and the mupdate mailbox master daemon.
It allows for cluster setups where there are many backend Cyrus spools
and frontend proxy servers.

%package ldap
Group: System/Servers
Summary: Cyrus IMAP server ldap auth system
Requires: %name = %version-%release

%description ldap
The %name-ldap package contains the Cyrus ldap auth system.

%package devel
Group: Development/C
Summary: Cyrus IMAP server development files

%description devel
The %name-devel package contains header files and libraries
necessary for developing applications which use the imclient library.

%package -n perl-Cyrus
Group: Development/Perl
Summary: Cyrus IMAP server utility Perl modules
Provides: perl(Cyrus/IMAP.pm) perl(Cyrus/IMAP/Admin.pm)

%description -n perl-Cyrus
The perl-Cyrus package contains Perl modules necessary to use the
Cyrus IMAP server administration utilities.

%package utils
Group: System/Servers
Summary: Cyrus IMAP server administration utilities
Requires: perl-Cyrus = %version-%release perl(Term/ReadLine.pm)

%description utils
The %name-utils package contains administrative tools for the
Cyrus IMAP server. It can be installed on systems other than the
one running the server.

%package doc
Group: System/Servers
Summary: Cyrus IMAP server documentation
BuildArch: noarch

%description doc
The %name-doc package contains Here the documentation about
Cyrus IMAP server.

%if_with sphinx
%package doc-full
Group: System/Servers
Summary: Cyrus documentation
BuildArch: noarch

%description doc-full
The %name-doc-full package contains complete Cyrus documentation
for IMAP server and SASL library
%endif

%prep
%setup
echo %version > VERSION

# hack for really enable pcre
sed "s|pcreposix\.h|pcre/pcreposix.h|g" -i configure.ac
sed 's|if test "$ac_cv_header_pcreposix_h" = "yes"|ac_cv_header_pcreposix_h="yes"; if test "$ac_cv_header_pcreposix_h" = "yes"|' -i configure.ac
%add_optflags -I%_includedir/pcre
sed "s|pcre\.h|pcre/pcre.h|" -i  lib/util.h		#  include <pcre.h>
sed "s|pcreposix\.h|pcre/pcreposix.h|" -i  lib/util.h	#  include <pcreposix.h>
sed "s|@ZLIB@|@ZLIB@ -lpcreposix|" -i perl/imap/Makefile.PL.in
sed "s|@ZLIB@|@ZLIB@ -lpcreposix|" -i perl/sieve/managesieve/Makefile.PL.in

%if_with unit_tests
# Suite: command
#   Test: run ...FAILED
#     1. cunit/unit.c:115  - CU_FAIL_FATAL("Code under test exited")
sed "s|/usr/bin/touch|/bin/touch|" -i cunit/command.testc
%endif

autoreconf -v -i

%add_optflags -lcrypto -lsasl2 -lssl

%configure \
  --with-extraident="%release" \
  \
  --sbindir=%_cyrexecdir \
  --libexecdir=%_cyrexecdir \
  \
  --enable-autocreate \
  --enable-idled \
  --enable-nntp \
  --enable-murder \
  --enable-http \
  --enable-calalarmd \
  --enable-replication \
  --enable-backup \
  \
  %{?_with_unit_tests: --enable-unit-tests} \
  \
  --enable-pcre \
  \
  %{?_with_snmp: --with-snmp} \
  %{?_without_snmp: --with-snmp=no} \
  --with-perl=perl \
  --with-ldap \
  --with-cyrus-user=%_cyrususer \
  --with-bdb-incdir=%_includedir/db4 \
  %{?_without_sphinx: --with-sphinx-build=no} \
  #

%build
%make

# Modify docs master --> cyrus-master
pushd man
  sed -i 's/master(8)/cyrus-master(8)/' *5 *8
popd
pushd doc/legacy
  sed -i 's/master/cyrus-master/g' man.html

  fig2dev -L png murder.fig murder.png
  fig2dev -L png netnews.fig netnews.png
popd

# Modify path in perl scripts
find . -type f -name \*.pl -print0 |
    xargs -r0 perl -pi -e 's@\/usr\/local\/bin\/perl@perl@' --

%if_with unit_tests
%check
make check
%endif

%install

# libcyrus*.so.* contains big count undefined symbols. Is it plugins possible ?
# So, libcyrus*.so.* in main package while question in resolving statuis:
# http://lists.andrew.cmu.edu/pipermail/info-cyrus/2015-October/038550.html
%set_verify_elf_method unresolved=relaxed

# Do what the regular make install does
make install DESTDIR=%buildroot PREFIX=%prefix mandir=%_mandir \
	INSTALLDIRS=vendor

install -m 755 imtest/imtest		%buildroot%_cyrexecdir/
install -m 755 perl/imap/cyradm		%buildroot%_cyrexecdir/

# Install tools
#rm -f tools/git-version.sh tools/jenkins-build.sh tools/build-with-cyruslibs.sh
pushd tools
for tool in * ; do
  case "$tool" in
    git-version.sh|jenkins-build.sh|build-with-cyruslibs.sh)
	continue
	;;
    *)
	test -f ${tool} && install -m 755 ${tool} %buildroot%_cyrexecdir/
	;;
  esac
done
popd

install -d \
  %buildroot%_sysconfdir/{rc.d/init.d,logrotate.d,pam.d,sysconfig,cron.daily} \
  %buildroot%_libdir/sasl2 \
  %buildroot%_bindir \
  %buildroot%_spooldata/stage. \
  %buildroot%_vardata/{user,quota,proc,log,msg,socket,db,sieve,rpm,backup} \
  %buildroot%_contribdir \
  %buildroot%_datadir/%name/rpm

install -m 755 %SOURCE11   %buildroot%_cyrexecdir/cvt_cyrusdb_all
install -m 755 %SOURCE12   %buildroot%_datadir/%name/rpm/magic

install -m 644 %SOURCE22   %buildroot%_sysconfdir/cyrus.conf
install -m 644 %SOURCE4    %buildroot%_sysconfdir/imapd.conf
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/pop
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/imap
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/sieve
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/mupdate
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/lmtp
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/http
install -m 644 %SOURCE10   %buildroot%_sysconfdir/sysconfig/%name

install -m 755 %SOURCE21    %buildroot%_initdir/%name
install -m 644 %SOURCE3    %buildroot%_sysconfdir/logrotate.d/%name
install -m 755 %SOURCE14   %buildroot%_sysconfdir/cron.daily/%name
install -pDm600 %SOURCE13 %buildroot%_sysconfdir/sasl2/Cyrus.conf

install -m 755 -d doc/conf
install -pD -m 755 %SOURCE6 %buildroot%_controldir/%name

install -m 755 %SOURCE16 %SOURCE17 %SOURCE18  %buildroot%_contribdir
install -m 644 %SOURCE19 %SOURCE20 %SOURCE5 doc/

# Rename 'master' binary and manpage to avoid crash with postfix
mv -f %buildroot%_cyrexecdir/master	%buildroot%_cyrexecdir/cyrus-master
mv -f %buildroot%_mandir/man8/master.8 %buildroot%_mandir/man8/cyrus-master.8

# http://bugzilla.altlinux.org/33788
mv -f %buildroot%_man8dir/httpd.8 %buildroot%_man8dir/cyrus-httpd.8

# Move utilites from /usr/libexec/cyrus to /usr/bin
# mupdate-loadgen.pl convert-sieve.pl
for i in arbitronsort.pl cyradm imtest  \
	 mknewsgroups config2header config2man masssievec
do
    mv %buildroot%_cyrexecdir/$i %buildroot/%_bindir/
done

# Create filelist for perl package, compress manpages before
[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress
find %buildroot%perl_vendor_autolib/Cyrus %buildroot%perl_vendor_archlib/Cyrus -type f -print |
  sed "s@^%buildroot@@g" |
  grep -v perllocal.pod |
  grep -v "\.bs" |
  grep -v "\.packlist" > perl-Cyrus-%version-filelist
if [ "$(cat perl-Cyrus-%version-filelist)X" = "X" ] ; then
  echo "ERROR: EMPTY FILE LIST"
  exit -1
fi

# Remove installed but not packaged files
rm -f %buildroot%_cyrexecdir/not-mkdep
find %buildroot -name "perllocal.pod" -exec rm -f {} \;
find %buildroot -name ".packlist" -exec rm -f {} \;

# Create file wich contains information about compiled db backends
for conf in DUPLICATE MBOX SEEN SUBS TLS
do
  echo CONFIG_DB_${conf}=$(grep "CONFIG_DB_${conf}" config.h | sed -e 's/)//' -e 's/_/-/g' | cut -d" " -f3 | cut -d"-" -f2) >> %buildroot%_datadir/%name/rpm/db.cfg
done

# directory for ssl-certs
install -dm750 %buildroot%_vardata/ssl

# imap sessions logs
mkdir -p %buildroot%_vardata/log/cyrus

# needed for %%ghost
touch %buildroot%_vardata/ssl/cyrus.cert
touch %buildroot%_vardata/ssl/cyrus.key

%add_findreq_skiplist /usr/bin/cyradm

# big doc section
%add_findreq_skiplist %_cyrexecdir/perl2rst
%if_with sphinx
pushd docsrc
    DOCSRC=./docsrc make html
    mkdir -p %buildroot%_defaultdocdir/%name-doc-full-%version
    cp -r build/html/* %buildroot%_defaultdocdir/%name-doc-full-%version
popd
%endif

%pre
/usr/sbin/groupadd -r -f %_cyrusgroup ||:
/usr/sbin/useradd -g %_cyrusgroup -G sasl -c "Cyrus IMAP Server" -d %_vardata \
  -s /dev/null -r %_cyrususer 2> /dev/null ||:

%post
%post_service %name
# Force synchronous updates, usually only on ext2 filesystems
for i in %_vardata/{user,quota} %_spooldata
do
	fstype=`find $i -maxdepth 0 -printf %%F`
	[ x"$fstype" = x"ext2" ] && chattr -R +S $i 2>/dev/null ||:
done

%preun
%preun_service %name

%files
# initscript
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name

# other stuff
%config %_controldir/*
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/cron.daily/%name

# cyrus configs
%config(noreplace) %_sysconfdir/cyrus.conf
%config(noreplace) %_sysconfdir/imapd.conf
%config(noreplace) %_sysconfdir/pam.d/imap
%config(noreplace) %_sysconfdir/pam.d/lmtp
%config(noreplace) %_sysconfdir/pam.d/http
%config(noreplace) %_sysconfdir/pam.d/pop
%config(noreplace) %_sysconfdir/pam.d/sieve
%config(noreplace) %attr(640,root,%_cyrusgroup) %_sysconfdir/sasl2/Cyrus.conf

# suid deliver
%attr(4710,%_cyrususer,%_cyrusgroup) %_cyrexecdir/deliver

# data dirs
%dir %attr(1770,root,%_cyrusgroup) %_vardata
%dir %attr(1770,root,%_cyrusgroup) %_vardata/*
%dir %attr(1770,root,%_cyrusgroup) %_vardata/log/*
%dir %attr(1770,root,%_cyrusgroup) %_spooldata
%dir %attr(1770,root,%_cyrusgroup) %_spooldata/*

%_datadir/%name
%if_with sphinx
%_man5dir/*
%_man8dir/*
%endif

# ssl-related
%dir %attr(0750,root,%_cyrusgroup) %_vardata/ssl
%ghost %attr(0640,root,%_cyrusgroup) %verify(not md5 mtime size) %_vardata/ssl/cyrus.cert
%ghost %attr(0640,root,%_cyrusgroup) %verify(not md5 mtime size) %_vardata/ssl/cyrus.key

%_cyrexecdir
%exclude %_cyrexecdir/lmtpproxyd
%exclude %_cyrexecdir/mupdate
%exclude %_cyrexecdir/pop3proxyd
%exclude %_cyrexecdir/proxyd
%exclude %_cyrexecdir/ptdump
%exclude %_cyrexecdir/ptexpire
%exclude %_cyrexecdir/ptloader
%exclude %_contribdir

%_libdir/libcyrus*.so.*

%files doc
%doc COPYING README.md
%doc $RPM_SOURCE_DIR/cyrus-procmailrc
%doc $RPM_SOURCE_DIR/cyrus-user-procmailrc.template
%doc $RPM_SOURCE_DIR/%name-procmail+cyrus.mc
%doc doc/*

%if_with sphinx
%files doc-full
%_defaultdocdir/%name-doc-full-%version
%endif

%files murder
%config(noreplace) %_sysconfdir/pam.d/mupdate
%_cyrexecdir/lmtpproxyd
%_cyrexecdir/mupdate
%_cyrexecdir/pop3proxyd
%_cyrexecdir/proxyd

%files ldap
%_cyrexecdir/ptdump
%_cyrexecdir/ptexpire
%_cyrexecdir/ptloader

%files devel
%_includedir/cyrus
%_libdir/*.so
#_libdir/lib*.a
%if_with sphinx
%_man3dir/*
%endif
%_libdir/pkgconfig/*

%files -n perl-Cyrus
%perl_vendor_autolib/Cyrus*
%perl_vendor_archlib/Cyrus*
%perl_vendor_privlib/Cyrus*
%doc perl/imap/README
%doc perl/imap/Changes
%doc perl/imap/examples

%files utils
%_contribdir
%_bindir/*
%_man1dir/*
%dir %_datadir/%name

%changelog
* Tue Aug 13 2019 Sergey Y. Afonin <asy@altlinux.org> 3.0.11-alt1
- 3.0.11 (CVE-2019-11356 fixed in 3.0.10)
- updated README.ALT.rus

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.8-alt3.1
- rebuild with new perl 5.28.1

* Thu Sep 13 2018 Sergey Y. Afonin <asy@altlinux.ru> 3.0.8-alt3
- updated README.ALT.rus
- do not installed build scripts from "tools" directory (dropped
  auto dependency by git)
- removed "--enable-netscapehack" (absent in configure in 3.0)
- added "--enable-calalarmd"
- added "--enable-backup"
  (warning: backup and replication features remains experimental)
- added libkrb5-devel to BuildRequires

* Thu Aug 30 2018 Sergey Y. Afonin <asy@altlinux.ru> 3.0.8-alt2
- disabled tcpwrappers support
- rebuilt with openssl 1.1
- some cleanups of spec

* Fri Aug 24 2018 Sergey Y. Afonin <asy@altlinux.ru> 3.0.8-alt1
- 3.0.8
- disabled altnamespace in imapd.conf (restored behaviour of Cyrus IMAP 2.5)
- reverted patches:
  patches/alt/004-configs (examples no modified now)

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.11-alt3.1
- rebuild with new perl 5.26.1

* Wed Aug 23 2017 Sergey Y. Afonin <asy@altlinux.ru> 2.5.11-alt3
- renamed httpd.8 to cyrus-httpd.8 (Closes: #33788)

* Fri May 12 2017 Sergey Y. Afonin <asy@altlinux.ru> 2.5.11-alt2
- removed forgotten files from /var/lib/imap/socket/
  in stop() function in init script

* Fri May 12 2017 Sergey Y. Afonin <asy@altlinux.ru> 2.5.11-alt1
- 2.5.11

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.9-alt2.1
- rebuild with new perl 5.24.1

* Tue Aug 30 2016 Sergey Y. Afonin <asy@altlinux.ru> 2.5.9-alt2
- rebuilt with libical-devel (v2.0.1)

* Mon Aug 29 2016 Sergey Y. Afonin <asy@altlinux.ru> 2.5.9-alt1
- 2.5.9

* Tue Jun 14 2016 Sergey Y. Afonin <asy@altlinux.ru> 2.5.8-alt1
- 2.5.8

* Fri Feb 05 2016 Sergey Y. Afonin <asy@altlinux.ru> 2.5.7-alt2
- rebuilt with libical1-devel

* Fri Dec 11 2015 Sergey Y. Afonin <asy@altlinux.ru> 2.5.7-alt1
- 2.5.7 (CVE-2015-8077, CVE-2015-8078; Closes: #31611)
- added tzdata to "Requires" (Closes: #31612)

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.5.6-alt1.1
- rebuild with new perl 5.22.0

* Fri Oct 23 2015 Sergey Y. Afonin <asy@altlinux.ru> 2.5.6-alt1
- 2.5.6 (git 20151016 of "cyrus-imapd-2.5" branch)
- renamed README.ALT to README.ALT.rus; updated README.ALT.rus

* Tue Oct 20 2015 Sergey Y. Afonin <asy@altlinux.ru> 2.5.5-alt1
- 2.5.5 (git 20150831 of "cyrus-imapd-2.5" branch)
- reverted patches:
  branch 005-autocreate (merged with upstream)
  branch 012-getline (not needed more)

* Fri Jul 10 2015 Sergey Y. Afonin <asy@altlinux.ru> 2.4.18-alt1
- 2.4.18
- added lsb init header
- added ability to disable copying of certificates in init script
  (Closes: #29984)

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.17-alt1.1
- rebuild with new perl 5.20.1

* Thu Sep 12 2013 Sergey Y. Afonin <asy@altlinux.ru> 2.4.17-alt1
- 2.4.17 (git 20130904 of "cyrus-imapd-2.4" branch )

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 2.4.12-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.4.12-alt2
- rebuilt for perl-5.16

* Sat Oct 15 2011 Alexey Tourbin <at@altlinux.ru> 2.4.12-alt1.1
- Rebuilt for perl-5.14.

* Thu Oct 06 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.12-alt1
- 2.4.12 fixes CVE-2011-3372, authentication bypass in the nntpd daemon.

* Fri Sep 09 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.11-alt1
- 2.4.11 fixes CVE-2011-3208, a remotely exploitable buffer overflow in
  the nntpd daemon.

* Wed Jun 22 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.9-alt1
- 2.4.9.

* Thu May 12 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.8-alt2
- Add libsensors-devel and libnl-devel to buildreqs for fix building.

* Thu Apr 14 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.8-alt1
- 2.4.8.

* Fri Apr 01 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.7-alt1
- 2.4.7.

* Thu Mar 24 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.6-alt3
- Enable libwrap and snmp support.

* Thu Mar 24 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.6-alt2
- Fix build by updating build requires.

* Thu Jan 13 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.6-alt1
- 2.4.6.
- Apply autocreate and autosieve patches for Cyrus IMAP Server 2.4.x by
  Martin Matuska <mm@freebsd.org>.
- Drop 002-fdatasync patch (unneeded).
- Drop Cyradm_Annotations.patch (merged upstream).

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.3.16-alt4.1
- Rebuilt with perl 5.12.

* Mon Oct 04 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.16-alt4
- Rebuild with libssl.so.10 and libcrypto.so.10.

* Tue Jun 08 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.16-alt3
- Build with --enable-replication.

* Mon Mar 01 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.16-alt2
- Add ldap auth support (Closes: #23002).

* Thu Dec 24 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.16-alt1
- 2.3.16
- Drop TV-annotation-definitions.diff patch (merged upstream).

* Thu Oct 22 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.15-alt2
- Move ssl cert generation code from spec to initscript.

* Thu Sep 10 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.15-alt1
- 2.3.15
- Update sieve to cyrus-imapd-2.3.15 release
- Security fix: Cyrus IMAP Server Sieve Buffer Overflow Vulnerability,
  see http://secunia.com/advisories/36629/

* Wed May 13 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.14-alt2
- Fix building with gcc4.4

* Mon Apr 20 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.14-alt1
- 2.3.14
- Drop 10-fix_potential_overflows.dpatch (merged by upstream)

* Tue Nov 25 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.13-alt3
- Updated buildreqs for fix building

* Sat Nov 01 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.13-alt2
- Fixed bug with pseudouser creation (introduced in 2.2.3-alt4)
- Add cyrus pseudouser to 'sasl' group by default

* Wed Oct 22 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.13-alt1
- 2.3.13 release

* Mon Aug 25 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3.12p2-alt3
- More carefully handle find(1) errors in %%post (Closes: #16857)

* Tue Jun 17 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3.12p2-alt2
- Fixed linking with libdb4.7

* Tue May 27 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3.12p2-alt1
- 2.3.12p2
- Fixed directory permissions according to ALT Security Policy
- Implemented automatic ssl-certificates generation using cert-sh-functions
  (Closes: #14304)
- Relocate client config for libsasl2 from %%_libdir/sasl2 to
  %%_sysconfdir/sasl2
- Do not package contrib both in cyrus-imapd and cyrus-imapd-utils
- README.ALT: add notice about sasl_mech_list
- Add sasl_mech_list option to default config

* Mon Jan 14 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3.11-alt1
- 2.3.11 release
- Disable cyrus-imapd service autostart by default
- Apply some Kolab patches:
  + cyrus-imap-admin-2.3.8-cyradm.patch
  + TV-annotation-definitions.diff from http://vman.de/cyrus/
  http://wiki.kolab.org/index.php/Kolab-major-app-patches#Cyrus_IMAPD
- Apply some Debian patches:
  + 03-fix_docs
  + 08-clean_socket_closes
  + 10-fix_potential_overflows
  + 30-update_perlcalling.sh
  + 40-rehash_fix_pathes.dpatch, change paths to alt-style
- Update autocreate patch http://email.uoa.gr/projects/cyrus/autocreate/
- README.ALT: recode to utf8, fix typo

* Tue Oct 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.2.13-alt2
- Add dependency on su(1) (Closes: #9971).
- Fix segfault when use lmtp socket for delivery (Closes: #10094)
- Use "skiplist" as default cyrusdb backend to use for the duplicate delivery
  suppression (Closes: #10476)

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.13-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon May 15 2006 Alexei Takaseev <taf@altlinux.ru> 2.2.13-alt1
- 2.2.13
- add Requires "perl(Term/ReadLine.pm)" for cyrus-imapd-utils
- Add LDFLAGS and CPPFLAGS for Sysiphus correct Kerberos detection

* Fri May 20 2005 Alexei Takaseev <taf@altlinux.ru> 2.2.12-alt3
- Fix #6902, #6903
- Remove unneeded requires to libsasl2-plugin-gssapi (#6859)

* Fri Apr 22 2005 Alexei Takaseev <taf@altlinux.ru> 2.2.12-alt2
- Fix (not created /var/spool/imap)

* Sat Feb 26 2005 Alexei Takaseev <taf@altlinux.ru> 2.2.12-alt1
- 2.2.12

* Fri Feb 11 2005 Alexei Takaseev <taf@altlinux.ru> 2.2.10-alt3
- Update autocreate patch to cyrus-imapd-2.2.10-autocreate-0.9.1.diff
- Add cyrus-imapd control facilities (for local delivery)
- Update README.ALT

* Wed Dec 08 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.10-alt2
- Update autocreate patch to cyrus-imapd-2.2.10-autocreate-0.1.diff

* Wed Nov 24 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.10-alt1
- 2.2.10
- CAN-2004-1015

* Tue Nov 23 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.9-alt1
- 2.2.9
- This release implements several bugfixes, notably one where lmtpproxyd
  could reuse a freed connection, another involving a pre-authentication
  buffer overrun in "imap magic plus" support (CAN-2004-1011) and lack
  of bounds checking in PARTIAL and FETCH. (CAN-2004-1012, CAN-2004-1013)

* Sat Jul 31 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.8-alt1
- 2.2.8

* Tue Jul 27 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.7-alt1
- 2.2.7
- add README.ALT
- remove cyrus-imapd-2.0.12-deliverman.patch,
  cyrus-imapd-2.0.12-~adm_man_sec.patch, cyrus-imapd-2.1.11-snmpargs.patch

* Wed Jun 23 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.6-alt2
- Update autocreate patch to cyrus-imapd-2.2.6-autocreate-0.2.diff

* Sat Jun 19 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.6-alt1
- 2.2.6

* Fri Jun 11 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.5-alt2
- Update autocreate patch to cyrus-imapd-2.2.5-autocreate-0.2.diff

* Sat May 29 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.5-alt1
- 2.2.5
- remove cyrus-imapd-2.0.9-cflags.patch (fixed in mainstream)

* Tue May 25 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.4-alt1
- 2.2.4
- remove cyrus-imapd-2.0.5-mandir.patch (fixed in mainstream)
- update autocreate patch to 2.2.4-autocreate-0.1

* Mon May 17 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.3-alt4
- cleanup spec-file 

* Thu May 13 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.3-alt2
- cleanup spec-file
- Add MDA, IMAPD and POP3D provides

* Tue Feb 24 2004 Alexander Bokovoy <ab@altlinux.ru> 2.2.3-alt1.2
- Rebuild against libkrb5-1.3.1-alt3

* Sun Jan 25 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.3-alt1.1
- build with db-4.2

* Sun Jan 25 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.3-alt1
- 2.2.3
- Drop cyrus-imapd-2.2.2-idled.patch (fix in upstream)
- Update autocreate patch
- Update imapd.conf (add all options)

* Mon Jan 05 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.2-alt4
- fix imapd.conf - tls_* undefine by default
- fix cyrus.conf - all services is offline by default, path for LMTP
  defined for postfix

* Fri Nov 28 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.2-alt3
- Enable `idle' daemon
- Update autocreate patch to 0.8.3
+ Add cyrus-imapd-2.2.2-idled.patch (fix idled compile)

* Mon Nov 03 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.2-alt2
- fix cyrus-imapd-alt-cyradm.patch (error:
  /usr/bin/cyradm: line 46: `exec perl -MCyrus::IMAP::Shell -e shell -- "$@" ;;')

* Wed Oct 29 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.2-alt1
- 2.2.2
- Disable `idle' daemon

* Sat Sep 13 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt6
- implemented autodetected / manual distro setting to package initscripts
  for both ALM2.2 (maintenance builds) and Sisyphus (implementation based
  somewhat on aureal-std-up.spec by Alexey Morozov <morozov novosoft ru>)

* Sun Aug 24 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt5
- removed creation of spool/config dirs, not needed anymore
- add sendmail m4 macro
- just one source for pam default configuration (they were all the same)
- added /etc/pam.d/lmtp
- added murder support

* Tue Aug 05 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt4
- Fixed definitions of files in perl-Cyrus

* Mon Aug 04 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt3
- fixed pam0(system-auth) requires

* Mon Aug 04 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt2
- by ivv:
    + changed main group to System/Servers
    + changed group of perl-Cyrus to Development/Perl
    + changed group of cyrus-imap-utils to System/Servers
    + changed file permissions on /usr/lib/cyrus/deliver to 4710
    + added patch for autocreate mailbox on post or login (see
      email.uoa.gr/autocreate)
    + added some contrib utils - folderxfer,imapcreate.pl,inboxfer

* Fri Jul 25 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt1
- first build for ALT
