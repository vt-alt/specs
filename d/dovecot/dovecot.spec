%define _libexecdir /usr/libexec
%define _ssldir %(openssl-config --openssldir)
%define _unpackaged_files_terminate_build 1

%def_disable debug

Name: dovecot
Version: 2.3.10.1
Release: alt1

Summary: Dovecot secure IMAP/POP3 server
License: MIT
Group: System/Servers

Url: http://www.dovecot.org/

# Repacked https://dovecot.org/releases/2.3/dovecot-%version.tar.gz
Source0: %name-%version.tar
Source1: dovecot.pam
Source2: dovecot.init
# XXX doesn't work for now
Source3: dovecot-auth.control
Source4: http://www.unicode.org/Public/UNIDATA/UnicodeData.txt

Patch1: fix-mail_plugin_dir-default.patch
Patch2: dovecot-2.0-defaultconfig.patch
#Patch3: dovecot-2.1-privatetmp.patch
Patch4: dovecot-2.1.4-postreleasefix.patch
Patch5: dovecot-2.3-systemd_firsttime.patch

PreReq: mailboxes-control

# TODO remove this when splitting into modules
%add_findreq_skiplist %_libexecdir/dovecot/decode2text.sh

# Automatically added by buildreq on Tue Apr 24 2012
# optimized out: libcom_err-devel libkrb5-devel libpq-devel libstdc++-devel pkg-config
BuildRequires: bzlib-devel gcc-c++ libldap-devel libmysqlclient-devel libpam-devel libsasl2-devel libsqlite3-devel libssl-devel openssl postgresql-devel zlib-devel
BuildRequires: libkrb5-devel

Obsoletes: dovecot1.0
Obsoletes: dovecot1.2

%description
Dovecot is an IMAP/POP3 server for Linux/UNIX-like systems, written with
security primarily in mind. Although it's written with C, it uses
several coding techniques to avoid most of the common pitfalls.

Dovecot can work with standard mbox and maildir formats and it's fully
compatible with UW-IMAP and Courier IMAP servers as well as mail clients
accessing the mailboxes directly.

%package -n %name-devel
Summary: Libraries and headers for Dovecot
Group: Development/Other

Requires: %name = %version-%release
Obsoletes: dovecot1.0-devel
Obsoletes: dovecot1.2-devel

%description -n %name-devel
Libraries and headers for Dovecot

%prep
%setup

%patch1 -p1
%patch2 -p1
#patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i 's@/usr/local@/usr@g' src/plugins/fts/decode2text.sh
sed -i 's@/usr/local@/usr@g' doc/example-config/conf.d/90-quota.conf

%ifarch %e2k
# lcc 1.23.12 won't do that
sed -i 's, ATTR_RETURNS_NONNULL,,' src/lib/mempool.h
%endif

xz -9 ChangeLog

%build
%add_optflags -D_DEFAULT_SOURCE=1
export ACLOCAL='aclocal -I .'
%autoreconf
%configure \
	    --localstatedir=%_var                   \
	    --with-moduledir=%_libdir/%name/modules \
	    --with-systemdsystemunitdir=%_unitdir   \
	    --disable-static                        \
	    --with-ssl=openssl                      \
	    --with-ssldir=%_ssldir                  \
	    --with-pgsql                            \
	    --with-mysql                            \
	    --with-sqlite                           \
	    --with-ldap                             \
	    --with-gssapi                           \
	    #

# setup right ssl directory
sed -i 's|/etc/ssl|%_ssldir|' doc/mkcert.sh doc/example-config/conf.d/10-ssl.conf

cp -a %SOURCE4 src/lib
%make_build

%install
%makeinstall_std

install -Dp -m 0600 %SOURCE1 %buildroot%_sysconfdir/pam.d/dovecot
install -Dp -m 0755 %SOURCE2 %buildroot%_initdir/%name

# generate ghost .pem files
touch empty
install -Dp -m600 empty %buildroot%_ssldir/certs/dovecot.pem
install -Dp -m600 empty %buildroot%_ssldir/private/dovecot.pem

mkdir -p %buildroot/run/dovecot/{login,empty}
chmod 755 %buildroot/run/dovecot
chmod 700 %buildroot/run/dovecot/login
mkdir -p %buildroot/var/cache/dovecot/indexes

# Install dovecot configuration and dovecot-openssl.cnf
mkdir -p %buildroot%_sysconfdir/dovecot/conf.d
install -Dp -m 644 doc/example-config/dovecot.conf %buildroot%_sysconfdir/dovecot
install -p -m 644 doc/example-config/conf.d/*.conf %buildroot%_sysconfdir/dovecot/conf.d
install -p -m 644 doc/example-config/conf.d/*.conf.ext %buildroot%_sysconfdir/dovecot/conf.d
install -Dp -m 644 doc/dovecot-openssl.cnf %buildroot%_ssldir/dovecot-openssl.cnf

install -Dp -m755 doc/mkcert.sh %buildroot%_libexecdir/%name/mkcert.sh

mkdir -p %buildroot%_localstatedir/%name

# remove the libtool archives
find %buildroot%_libdir/%name/ -name '*.la' | xargs rm -f

# remove what we don't want
rm -f %buildroot%_sysconfdir/dovecot/README
rm -f %buildroot%_bindir/dovecot-sysreport
rm -f %buildroot%_man1dir/dovecot-sysreport.1*

# hi buildreq!
( cd %buildroot%_libdir; ln -s %name/lib*.so.* . )

# create tmpfiles.conf
mkdir -p %buildroot%_tmpfilesdir
cat >%buildroot%_tmpfilesdir/%name.conf<<END
d /run/dovecot 0755 root root -
d /run/dovecot/empty 0750 root root -
d /run/dovecot/login 0700 root root -
END

%pre
%pre_control mailboxes
groupadd -r -f dovecot 2>/dev/null ||:
useradd -r -n -g dovecot -c 'Dovecot internal processes' \
		-d %_var/run/%name -s /dev/null dovecot 2>/dev/null ||:
groupadd -r -f dovenull 2>/dev/null ||:
useradd -r -n -g dovenull -c 'Dovecot untrusted login processes' \
		-d %_var/run/%name -s /dev/null dovenull 2>/dev/null ||:
%post
%post_control -s private mailboxes
%post_service %name

# TODO postun old mailboxes access?

%files
%doc AUTHORS ChangeLog* COPYING NEWS README
%_bindir/doveconf
%_bindir/doveadm
%_bindir/dsync
%_sbindir/dovecot
%dir %_datadir/dovecot
%_datadir/dovecot/*
%_unitdir/*

%dir %_cachedir/dovecot
%dir %_cachedir/dovecot/indexes
%dir %_localstatedir/dovecot

%_tmpfilesdir/%name.conf

%_initdir/dovecot

%dir %_sysconfdir/dovecot
%dir %_sysconfdir/dovecot/conf.d
%config(noreplace) %_sysconfdir/dovecot/dovecot.conf
%config(noreplace) %_sysconfdir/dovecot/conf.d/*
%config(noreplace) %_sysconfdir/pam.d/dovecot
%config(noreplace) %_ssldir/dovecot-openssl.cnf
%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_ssldir/certs/dovecot.pem
%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_ssldir/private/dovecot.pem

%_libexecdir/dovecot

%_docdir/dovecot

%_man1dir/*
%_man7dir/doveadm-search-query.*

# hi buildreq
%_libdir/lib*.so.*
%_libdir/dovecot
%exclude %_libdir/dovecot/libdovecot*.so
%exclude %_libdir/dovecot/dovecot-config

%files -n %name-devel
%_includedir/dovecot
%_datadir/aclocal/dovecot.m4
%_libdir/dovecot/libdovecot*.so
%_libdir/dovecot/dovecot-config

%changelog
* Wed May 20 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.3.10.1-alt1
- Updated to 2.3.10.1 (fixes CVE-2020-10957, CVE-2020-10958, CVE-2020-10967).

* Thu Jan 23 2020 Fr. Br. George <george@altlinux.ru> 2.3.9.2-alt1
- Autobuild version bump to 2.3.9.2

* Wed Dec 25 2019 Anton Midyukov <antohami@altlinux.org> 2.3.7.2-alt3.1
- not packaged /run/dovecot

* Sat Nov 30 2019 Anton Midyukov <antohami@altlinux.org> 2.3.7.2-alt3
- Create _tmpfilesdir/dovecot.conf (Closes: 37554)
- Replace /var/run -> /run, /var/lock -> /run/lock

* Tue Sep 03 2019 Michael Shigorin <mike@altlinux.org> 2.3.7.2-alt2
- E2K: fixed build with sed equivalent of george@'s patch.
- Care a bit more about timestamps et al.

* Wed Aug 28 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.3.7.2-alt1
- Updated to 2.3.7.2 (fixes CVE-2019-11500).

* Fri Aug 23 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.3.7.1-alt1
- Updated to 2.3.7.1 (ALT#36351, #37111).

* Mon Mar 25 2019 Fr. Br. George <george@altlinux.ru> 2.3.5-alt1
- Autobuild version bump to 2.3.5

* Tue Nov 27 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.2.1-alt2
- Packaged AUTHORS, ChangeLog, COPYING, NEWS and README.

* Tue Sep 11 2018 Grigory Ustinov <grenka@altlinux.org> 2.3.2.1-alt1.1
 - Rebuilt with openssl 1.1.
 - Added BR: libkrb5-devel.

* Mon Jul 23 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3.2.1-alt1
- Update version to 2.3.2.1 from src

* Sat Jul 21 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.2.36-alt3
- More correct fix (thnx ldv@)

* Sat Jul 21 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.2.36-alt2
- Fixed auth crash

* Fri Jul 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.36-alt1
- Update version to 2.2.36 from src

* Thu Jan 18 2018 Fr. Br. George <george@altlinux.ru> 2.2.33.2-alt1
- Manual vwersion bump to 2.2.33.2

* Wed Jun 07 2017 Fr. Br. George <george@altlinux.ru> 2.2.30.2-alt1
- Autobuild version bump to 2.2.30.2

* Wed Apr 26 2017 Fr. Br. George <george@altlinux.ru> 2.2.29.1-alt1
- Autobuild version bump to 2.2.29.1

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 2.2.28-alt1
- Autobuild version bump to 2.2.28

* Tue Dec 27 2016 Fr. Br. George <george@altlinux.ru> 2.2.27-alt1
- Autobuild version bump to 2.2.27 (closes: #32946)

* Mon Jan 25 2016 Fr. Br. George <george@altlinux.ru> 2.2.21-alt1
- Autobuild version bump to 2.2.21

* Wed Oct 14 2015 Fr. Br. George <george@altlinux.ru> 2.2.19-alt1
- Autobuild version bump to 2.2.19
- Fix systemd service patch

* Thu Sep 10 2015 Fr. Br. George <george@altlinux.ru> 2.2.18-alt1
- Autobuild version bump to 2.2.18

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 2.2.16-alt1
- Autobuild version bump to 2.2.16

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 2.2.15-alt1
- Autobuild version bump to 2.2.15

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 2.2.14-alt1
- Autobuild version bump to 2.2.14

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 2.2.13-alt1
- Autobuild version bump to 2.2.13

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 2.2.12-alt1
- Autobuild version bump to 2.2.12

* Sun Jan 12 2014 Fr. Br. George <george@altlinux.ru> 2.2.10-alt1
- Autobuild version bump to 2.2.10

* Thu Nov 28 2013 Fr. Br. George <george@altlinux.ru> 2.2.9-alt1
- Autobuild version bump to 2.2.9

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 2.2.6-alt1
- Autobuild version bump to 2.2.6

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 2.2.5-alt1
- Autobuild version bump to 2.2.5

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 2.2.2-alt1
- Autobuild version bump to 2.2.2

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 2.1.15-alt1
- Autobuild version bump to 2.1.15
- 2.1.11+ cache file trouble bugfix releases 2.1.13-2.2.15

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 2.1.12-alt1
- Autobuild version bump to 2.1.12
- Bugfix 2.1.11 and bugfix fix 2.1.12 releases

* Tue Nov 13 2012 Fr. Br. George <george@altlinux.ru> 2.1.10-alt3
- Add systemd first run service

* Tue Nov 13 2012 Fr. Br. George <george@altlinux.ru> 2.1.10-alt2
- Fix post_control

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 2.1.10-alt1
- Autobuild version bump to 2.1.10 (bugfixes + doveadm improvement)

* Tue Aug 21 2012 Fr. Br. George <george@altlinux.ru> 2.1.9-alt1
- Autobuild version bump to 2.1.9

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 2.1.8-alt1
- Autobuild version bump to 2.1.8

* Mon Jun 04 2012 Fr. Br. George <george@altlinux.ru> 2.1.7-alt1
- Autobuild version bump to 2.1.7

* Mon May 14 2012 Fr. Br. George <george@altlinux.ru> 2.1.6-alt1
- Autobuild version bump to 2.1.6
- Unhide new fedora patch
- Add mailboxes control to prevent http://wiki2.dovecot.org/Errors/ChgrpNoPerm

* Thu Apr 26 2012 Fr. Br. George <george@altlinux.ru> 2.1.5-alt1
- Brand new version
- Control removed
- Run-out-of-the-box patches
- FC patches
- Systemd services

* Thu Apr 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.12-alt1
- 2.0.12

* Thu Apr 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.5-alt3
- Repair build

* Wed Oct 27 2010 Anton Protopopov <aspsk@altlinux.org> 2.0.5-alt2
- Restore old changelog
- Merge (by ours) with gears/d/dovecot.git

* Tue Sep 28 2010 Anton Protopopov <aspsk@altlinux.org> 2.0.5-alt1
- Build dovecot 2.0.5 for Sisyphus

* Thu Sep 03 2009 Maxim Ivanov <redbaron at altlinux.org> 1.2.4-alt5
- Fixed bug with multiple sieve-before scripts

* Wed Sep 02 2009 Maxim Ivanov <redbaron at altlinux.org> 1.2.4-alt4
- Added option to compile debug version
- sievec is now part of dovecot package

* Tue Sep 01 2009 Maxim Ivanov <redbaron at altlinux.org> 1.2.4-alt3
- conflicts and obsoletes are corrected

* Sat Aug 29 2009 Maxim Ivanov <redbaron at altlinux.org> 1.2.4-alt2
- Added GSSAPI auth fix

* Sat Aug 29 2009 Maxim Ivanov <redbaron at altlinux.org> 1.2.4-alt1
- dovecot 1.2.4, managesieve 0.11.9, sieve 0.1.12
- added dist-upgrade and upgrade notifications

* Mon May 18 2009 Ivanov Maxim <redbaron@altlinux.org> 1.2-alt2.rc3
- Use separate libexecdir to remove conflict to other dovecot version.
  BEWARE! Update your MTA config, /usr/libexec/dovecot/deliver if you
  are upgrading from obsolete dovecot1.2 package
- Spec cleanup.
- make various bundled files more universal to handle multiple versions

* Tue May 05 2009 Ivanov Maxim <redbaron@altlinux.org> v1.2-alt1.rc3
- Updated to 1.2.rc3
- Fixed macros warnings in spec

* Tue Nov 18 2008 Sergey Ivanov <seriv@altlinux.ru> v1.2-alt3_alpha3
- fix: in v1.2-alt2_alpha3 managesieve was lost due to my mistake.

* Mon Nov 17 2008 Sergey Ivanov <seriv@altlinux.ru> v1.2-alt2_alpha3
- upstream fixes ManageSieve SECURITY hole: virtual users can edit scripts of other virtual users

* Mon Oct 27 2008 Sergey Ivanov <seriv@altlinux.ru> v1.2-alt1_alpha3
- dovecot-1.2 (alpha3) for Sisyphus

* Sun Jul 06 2008 Sergey Ivanov <seriv@altlinux.ru> 1.2.rc8-alt1
- dovecot-1.2 (rc8) for Sisyphus

* Thu Jun 26 2008 Sergey Ivanov <seriv@altlinux.ru> 1.0.15-alt2
- Renamed to dovecot1.0 and set conflicts against dovecot

* Sun Jun 22 2008 Sergey Ivanov <seriv@altlinux.ru> 1.0.15-alt1
- Release v1.0.15 (see Changelog) and fix check-subdirs

* Thu Mar 13 2008 Sergey Ivanov <seriv@altlinux.ru> 1.0.13-alt1
- Release v1.0.13, see Changelog

* Thu Mar 13 2008 Sergey Ivanov <seriv@altlinux.ru> 1.0.10-alt2
- fix #14287: use cert-sh-functions instead of custom mkcert.sh

* Sat Dec 29 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.10-alt1
- Released v1.0.10, see Changelog

* Fri Dec 28 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.9.hg20071228-alt1
- applied patch http://hg.dovecot.org/dovecot-1.0/rev/0a4f86976f50 to fix
  mailbox problem of v. 1.0.9 (got too little data).

* Thu Dec 27 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.9.hg20071225-alt3
- added symlink for better backward compatibility,
  see http://lists.altlinux.org/pipermail/sisyphus/2007-December/210648.html

* Wed Dec 26 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.9.hg20071225-alt2
- fix bugs #13807 #12532

* Tue Dec 25 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.9.hg20071225-alt1
- 1.0.9 with many changes, see Changelog

* Wed Oct 31 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.6.hg20071030-alt1
- 1.0.6 with many changes, among them compressed with zlib mailboxes support,
  see Changelog

* Wed Aug 01 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.3.hg20070801-alt1
- updated to 1.0.3, with security fix: If user was given i (insert) right
  for a mailbox, but not all s/t/w (seen, deleted, other flags) rights,
  COPY and APPEND commands weren't supposed to allow saving those flags.
  This is technically a security fix, but it's unlikely this caused problems
  for anyone.

* Tue Jul 17 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.2.hg20070717-alt1
- updated to 1.0.2, with better sieve handling errors (bounce
  only if message couldn't be saved anywhere); fixes for UILDLIST plugins handling
  and others, see ChangeLog

* Thu Jul 05 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.1.5-alt1
- new upstream changes, including:
    crashfix if PAM returns a reply but the process doesn't die,
    Update tmp/ directory's atime+mtime with utime(NULL) so it works
    even if we're not the directory owner.

* Mon Jul 02 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.1.4-alt1
- recent upstream fixes:
  2007-07-02  Timo Sirainen  <tss@iki.fi>

	* src/auth/passdb-ldap.c, src/auth/userdb-ldap.c:
	Memory leak fix

  2007-06-28  Timo Sirainen  <tss@iki.fi>

	* dovecot-example.conf:
	Mention that flock doesn't work with NFS.

  2007-06-27  Timo Sirainen  <tss@iki.fi>

	* src/auth/passdb-pam.c:
	FIXME comment update

	* src/lib/lib-signals.c:
	Allow registering signal handlers even before lib_signals_init() is
	called. The signals won't be effective until then though, unless
	they're ignored.

	* src/lib/ioloop-notify-inotify.c:
	If inotify_init() fails with EMFILE, give an understandable error
	message.

	* src/imap/client.c, src/imap/client.h, src/imap/cmd-idle.c:
	Changes sent by IDLE shouldn't affect the client's inactivity
	timeout checking.

  2007-06-26  Timo Sirainen  <tss@iki.fi>

	* src/imap/cmd-append.c:
	APPEND {0+} didn't eat the finishing CRLF.

  2007-06-25  Timo Sirainen  <tss@iki.fi>

	* src/imap/cmd-list.c:
	LIST "" %% with INBOX. namespace returned INBOX with \HasNoChildren.

* Wed Jun 20 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.1.3-alt1
- two more 1.0.1+ fixes:
  2007-06-20  Timo Sirainen  <tss@iki.fi>

	* src/lib-index/mail-transaction-log-view.c:
	Map the log files only after they've all been found. Otherwise we
	could have skipped some transactions from the end of non-head logs.

	* src/lib-index/mail-transaction-log.c:
	mmap_disable=yes: Fixed invalid "hdr.size too large" transaction log
	corruption errors.

* Tue Jun 19 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.1.2-alt13
- two more 1.0.1+ fixes:
 2007-06-19  Timo Sirainen  <tss@iki.fi>
        * src/plugins/quota/quota-maildir.c:
        If maildirsize file is being rewritten while we're trying to do
        that, recalculate it later instead of failing with "Unknown quota
        error".

        * src/plugins/quota/quota.c:
        Changed "Unknown error" to "Unknown quota error".

* Mon Jun 18 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.1.1-alt13
- added last after-1.0.1 fixes:
  2007-06-17  Timo Sirainen  <tss@iki.fi>
	* src/pop3/client.c:
	Even if mailbox sync fails, commit the transaction so that cache
	file gets updated.
	* src/imap/imap-fetch.c:
	Always commit FETCH transaction to make sure cached data is
	committed.
	* src/imap/imap-fetch.c:
	We didn't update last_output timestamp with long fetches, causing
	Dovecot to idle-disconnect the client.
  2007-06-16  Timo Sirainen  <tss@iki.fi>
	* src/lib-storage/mail-copy.c:
	Added missing error logging for i_stream_read()

* Fri Jun 15 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.1-alt13
- directory structure returned to dovecot's original, thangs
  to ldv (http://lists.altlinux.org/pipermail/devel/2007-June/047071.html).
  Dovecot-wikies dropped from this package to be a separate package with own *.src.rpm
  Update to 1.0.1 release, among the changes:
  2007-06-14  Timo Sirainen  <tss@iki.fi>
	* src/lib-storage/index/index-storage.c:
	Treat unknown errors as temporary errors.
	* src/lib-storage/index/maildir/maildir-uidlist.c:
	When saving a message to maildir without dovecot-uidlist file, give
	the newly created uidlist file a non-zero uidvalidity.
	* src/lib-storage/index/mbox/mbox-storage.c:
	When trying to use mbox file as the root directory, give a nice
	error.
  2007-06-13  Timo Sirainen  <tss@iki.fi>
	* src/deliver/deliver.c:
	If input mail gets lost somehow, log a real error instead of
	"Unknown error".
	* dovecot-example.conf:
	Updated passwd/shadow comments.
  2007-06-12  Timo Sirainen  <tss@iki.fi>
	* src/deliver/deliver.c:
	If save failed, log also the reason for it.
	* src/deliver/deliver.c:
	Added -e parameter to write rejection error to stderr and exit with
	EX_NOPERM instead of sending the rejection by executing sendmail.
	* src/master/mail-process.c:
	nfs check: If namespaces are defined, use the first one's location
	instead of mail_location.
	* src/lib-storage/index/index-storage.c, src/lib-storage/index/index-
	storage.h, src/lib-storage/index/maildir/maildir-sync.c:
	If new/ directory is lost when syncing, assume the mailbox was
	deleted and make the mailbox inconsistent (which disconnects the
	client).

* Tue Jun 12 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.1-alt12.hg20070612
- releasing 1.0.1rc3

* Sun May 27 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt12.hg20070527
- fixes from hg http://hg.dovecot.org/dovecot_1_0
  2007-05-24  Timo Sirainen  <tss@iki.fi>
	* src/lib-mail/istream-header-filter.c:
	If there's no message body, the final read() should return -1, not
	-2
  2007-05-23  Timo Sirainen  <tss@iki.fi>
	* src/master/master-settings.c:
	If Dovecot is already running, complain about it instead of wiping
	out login_dir and causing the already running Dovecot to break.
  2007-05-22  Timo Sirainen  <tss@iki.fi>
	* src/lib-index/mail-cache-compress.c:
	Cache compression actually lost the cache with non-x86 CPU and 64bit
	file offsets.
	* src/master/main.c:
	If startup fails because of configuration problems, print "Invalid
	configuration in <path>"
	* src/master/master-settings.c:
	Complain about missing pop3_uidl_format if pop3 is enabled.
	* src/pop3/main.c:
	Changed pop3_uidl_format error message once again.
	* src/lib/ioloop.c:
	Added wiki link to "time moved backwards" error.
  2007-05-19  Timo Sirainen  <tss@iki.fi>
	We no longer need .cvsignore files
	Mercurify the repository
  2007-05-16  Timo Sirainen  <tss@iki.fi>
	* src/lib-storage/index/index-mail-headers.c:
	Assert-crashfix in some conditions.
	* src/lib-storage/index/maildir/maildir-uidlist.c:
	When recreating dovecot-uidlist file based on dovecot.index, we set
	next_uid value wrong if new messages had been added.
* Tue May 15 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt12.cvs20070515
- fixes from cvs branch_1_0:
  * If Return-Path doesn't contain user and domain, treat it as missing
    Return-Path.
  * Handle symlinks pointing to nonexisting files better.
  * Log an error if pwrite_full() fails while overwriting index mapping.
  * If ssl-parameters.dat has been updated externally, copy it to our base_dir.
  * When running multiple Dovecot instances, only one of them needs to
    regenerate ssl-parameters.dat.
  * We sent "Hang in there.." too early sometimes and checked it too often.
  * Give a better error message if dotlock is deleted immediately under us (or
    more likely an OS bug).
  * Print also Dovecot version with dovecot -n.
  * Keyword characters weren't sorted in the maildir filename.
  * If we don't have write access to cur/ directory, treat the mailbox as
    read-only.
  * Changed auth_request->created to last_access and update it a bit more often.
    If there are slow authentications this could help avoid removing timeouted
    auth requests too early.
  * %%c wasn't exported to auth worker processes. Patch by Andrey Panin
  * Make sure uid_validity and next_uid aren't 0 in the uidlist header.
  * Updated error message.
  * If we synced the mbox while saving the message (happens only with quota
    plugin loaded), we could have used a wrong append offset (calculated before
    sync) which caused "Unexpectedly lost From-line" errors, and depending on
    the sync either extra NUL lines or Content-Length header written over
    existing mails (quite unlikely).
  * If pop3_uidl_format=%%m, it wasn't cached correctly when saving new messages
    (eg. with deliver). X-Delivery-ID wasn't used in the MD5 sum, causing
    duplicates when POP3 recalculated the MD5 sum later.
  And others.

* Mon Apr 16 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt12
- clean-up (mostly rm .cvsignore files); update wikies.

* Sat Apr 14 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt11
- fix errors in -alt10 release of dovecot: by my mistake there were not applied recent patches.

* Fri Apr 13 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt10
- release 1.0.rc32 renamed to be 1.0; updated wiki to current state

* Thu Apr 12 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt9.rc32
- updated to rc32

* Sun Apr 08 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt9.rc31
- updated to rc31

* Fri Apr 06 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt9.rc30
- updated to rc30

* Fri Mar 30 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt9.rc29
- added doc/wiki/*txt files to dovecot-doc.rpm

* Fri Mar 30 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc29
- rc29: security fix: If zlib plugin was loaded, it was possible to open
  gzipped mbox files outside the user's mail directory.
  Other fixes and cleanups.

* Thu Mar 29 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc28.cvs20070329
- fix Bug #11255: generate certificates if needed at start, not at install;
  strip unneeded details in output;
  patches from cvs up to 2007-03-29.

* Sun Mar 25 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc28.cvs20070325
- upstream --enable-header-install obsoletes half hacks for dovecot-devel;
  patches from cvs up to 2007-03-25.

* Sat Mar 24 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc28.cvs20070324
- update to rc28 + patches from cvs up to 2007-03-24.

* Wed Mar 21 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc27.cvs20070321
- update to rc27 + patches from cvs up to 2007-03-21.

* Fri Mar 02 2007 Stanislav Ievlev <inger@altlinux.org> 1.0-alt8.rc24.1
- uncomment socket section in default config
- add dovecot-auth control

* Thu Feb 22 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc24
- upgrade to rc24

* Wed Feb 21 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc23
- upgrade to rc23

* Tue Feb 06 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc22
- upgrade to rc22

* Sat Feb 03 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc21
- upgrade to rc21

* Tue Jan 23 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc19
- upgrade to rc19: ACL plugin wasn't working in rc18

* Mon Jan 22 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc18
- upgrade to rc18.

* Sun Jan 07 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc17
- upgrade to rc17: fixed MySQL authentication broken in rc16.

* Sat Jan 06 2007 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc16
- upgrade to rc16; fixed section Files which was broken in alt8.rc15

* Sat Nov 18 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc15
- upgrade to rc15

* Mon Nov 13 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt8.rc14
- Split to dovecot, dovecot-devel, dovecot-sieve removed to a separate
  package. Refix #9634 (previous fix was lost during upgrades).

* Sun Nov 12 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt7.rc14
- upgrade to rc14

* Fri Nov 10 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt7.rc13
- sieve plugin update to 1.0

* Wed Nov 08 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt6.rc13
- update to rc13

* Sun Nov 05 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt6.rc12
- update to rc12

* Sat Nov 04 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt6.rc11
- update to rc11

* Mon Oct 16 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt6.cvs20061016
- Update to recent dovecot rc10 and dovecot-sieve;
  now dovecot.index.cache files have the same format for 32- and 64-bit machines.

* Fri Oct 13 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt6.cvs20060926
- Restore dovecot's deliver agent building

* Thu Sep 28 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt5.cvs20060926
- Fix #10045 & update to cvs20060926 (rc7+)

* Sun Sep 17 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt5.cvs20060812
- Fix #9915

* Fri Sep 15 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt4.cvs20060812.1
- Rebuilt with MySQL-5.0.24-alt2.

* Wed Aug 16 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt4.cvs20060812
- fix bug #9836; update to cvs version of Aug/16/2006 (rc6+)

* Wed Jul 05 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt3.rc2
- updated to rc2

* Mon Jul 03 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt3.rc1
- fix #9634 by defaulting pop3_uidl_format = %%08Xu%%08Xv

* Wed Jun 28 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt2.rc1
- updated to rc1.

* Mon Jun 26 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt2.cvs20060626
- Bug 9719 fixed in upstream, dovecot updated to CVS snapshot

* Fri Jun 23 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt2.cvs20060619
- Reverted to CVS version of 2006.06.19: recent changes with strict UID policy
  don't work on my mailboxes.

* Thu Jun 22 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt1.cvs20060622
- updated to beta9, see Changelog. Sieve delivery agent now renamed to sievec.
  Also closes bug #9634.

* Wed Apr 12 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt1.cvs20060412
- updated to beta7, see Changelog; now with working sieve-like delivery

* Fri Mar 03 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt1.cvs20060303
- s/%_libexecdir\/%name/%_libdir\/%name/ in %files section

* Mon Feb 27 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt0.cvs20060227
- updated to beta3 from cvs, with memory leak and other fixes;
  disabled sieve-like local delivery agent for now.

* Wed Feb 15 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt0.cvs20060215
- updated to beta3 from cvs, with security fixes

* Mon Jan 30 2006 Sergey Ivanov <seriv@altlinux.org> 1.0-alt0.cvs20060130
- built from dovecot cvs 2006-01-30 and with sieve local delivery agent

* Sun Dec 04 2005 Sergey Ivanov <seriv@altlinux.ru> 1.0-alt0.cvs20051204
- 1.0-alpha4 of nightly cvs builds at 12/04/2005

* Mon Nov 21 2005 Sergey Ivanov <seriv@altlinux.ru> 0.99.14-alt5
- Fix postgresql-devel dependency, removed version number binding;
  fix %_libexecdir - %_libdir confusion;
  fix documentation installation.

* Tue Oct 11 2005 Sergey Ivanov <seriv@altlinux.ru> 0.99.14-alt4
- removed undefined macro from commented-out text;
  removed conflicting relation to other POP3/IMAP servers

* Fri Aug 05 2005 Sergey Ivanov <seriv@altlinux.ru> 0.99.14-alt3
- Fix #7479

* Sun May 22 2005 Sergey Ivanov <seriv@altlinux.ru> 0.99.14-alt2
- Buildreq fix: removed version binding for libpq-devel

* Fri Feb 18 2005 Sergey Ivanov <seriv@altlinux.ru> 0.99.14-alt1
-  Message address fields are now parsed differently, fixing some
  issues with spaces. Affects only clients which use FETCH ENVELOPE
  command.
- Message MIME parser was somewhat broken with missing MIME boundaries
- mbox: Don't allow X-UID headers in mails to override the UIDs we
  would otherwise set. Too large values can break some clients and
  cause other trouble.
- passwd-file userdb wasn't working
- PAM crashed with 64bit systems
- non-SSL inetd startup wasn't working
- If UID FETCH notices and skips an expunged message, don't return
  a NO reply. It's not needed and only makes clients give error
  messages.

* Thu Jan 06 2005 Sergey Ivanov <seriv@altlinux.ru> 0.99.13-alt1
- Update to new version. From it's changelog:
  * GNUTLS support hasn't been working for a while, so it's not even
    tried to be used anymore unless explicitly wanted.
  + Added CRAM-MD5 authentication mechanism. Patch by Joshua Goodall
  + Added SMD5 and LDAP-MD5 password schemes and changed MD5 scheme to
    use LDAP-MD5 if the password isn't in MD5crypt format. Patch by
    Joshua Goodall
  + Workaround for some POP3 client bugs: if message doesn't contain the
    "end of headers" empty line, add it automatically.
  + vpopmail supports now all password schemes, most importantly
    MD5crypt works now without support from libc's crypt()
  - SQL and LDAP authentication was broken
  - SEARCH UNKEYWORD wasn't working

* Sun Dec 05 2004 Sergey Ivanov <seriv@altlinux.ru> 0.99.12-alt1
- Updated to new version. From changelog of 0.99.12:
    - Fix memory leaks in LDAP, MySQL and PGSQL userdb/passdb
    - Fix hanging when parsing mails that have over 4096 bytes in one
      line (SMTP servers normally don't allow over 1000 bytes so it
      shouldn't be much of a problem)
    - FETCH BODYSTRUCTURE sometimes gave a wrong reply
      (eg. with FETCH (BODYSTRUCTURE RFC822.SIZE) if it wasn't cached)
    - Never return more than one INBOX in LIST even if there are such
      files. They don't work anyway and it just confuses clients.
    - mbox: Don't allow creating INBOX directory by creating/renaming
      mailboxes under it. They just wouldn't work.
    - POP3: Don't return PLAIN in SASL list. We don't support initial SASL
      responses, so it only breaks with most clients that try to use it.
    - IMAP and POP3 login processes may have sent each line in two IP
      packets, one with the data and another with CR+LF. Some clients
      didn't work because of this.

* Thu Sep 23 2004 Sergey Ivanov <seriv@altlinux.ru> 0.99.11-alt1
- Updated to 0.99.11

* Mon Aug 02 2004 Sergey Ivanov <seriv@altlinux.ru> 0.99.10.9-alt1
- Update to 0.99.10.9

* Fri Jul 30 2004 Sergey Ivanov <seriv@altlinux.ru> 0.99.10.8-alt1
- Updated to 0.99.10.8

* Sat Jan 10 2004 Anton V. Denisov <avd@altlinux.org> 0.99.10.4-alt1.1
- Explicitly use automake-1.4 for build and run %%__automake before
  %%configure (hope this fix build with new autotools and GCC).

* Mon Dec 15 2003 Anton V. Denisov <avd@altlinux.org> 0.99.10.4-alt1
- Updated to 0.99.10.4 (bugfix release).

* Tue Dec 09 2003 Anton V. Denisov <avd@altlinux.org> 0.99.10.2-alt1
- Initial release for ALT Linux Sisyphus.

* Mon Dec 08 2003 Anton V. Denisov <avd@altlinux.org> 0.99.10.2-alt0.2
- Built with pop3 daemon and enable it in config.
- Add into %%summary and %%descrition info about POP3 protocol.
- Minor improvements in %%files section.
- PreReq tuned.

* Tue Nov 11 2003 Anton V. Denisov <avd@altlinux.org> 0.99.10.2-alt0.1
- Updated to 0.99.10.2 (bugfix release).
- Removed auth-no-homedir.patch (no longer need).
- Updated our patches for new version.
- Add Packager tag.
- added %postun for user removal and commented it out.
- TODO is still todo.

* Mon Nov 10 2003 Anton V. Denisov <avd@altlinux.org> 0.99.10-alt0.1
- New version 0.99.10.
- Applied upstream bugfix patch.
- Added alt-conf-paths.patch
- Updated alt-mkcert.patch
- Updated %%description.
- Updated buildrequires.
- PAM config renamed: imap->%name
- SSL/TLS certs renamed.
- Additional flags for %%configure.
- Temporary build with --without-pop3d (should we?)
- Use default config instead of our.
- Mark %_initdir/%name as %%config(noreplace) (should we?).
- Init script updated.
- Corrected permissions for %_var/run/%name and %_var/run/%name/login.
- Other minor updates in spec file.
- TODO:
  + build and split modules (like postfix2 package).
  + other.

* Sun Nov 09 2003 Anton V. Denisov <avd@altlinux.org> 0.99.4-alt0.2
- Initial build for ALT Linux.
- Spec file cleaned up and improved (courier-imap.spec as example).
- Automatically added BuildRequires.
- %%confugure with additional keys.
- PAM configs added.
- Create user for imap-login process.
- added sample default config
- SSL/TLS certs generation during package install (need more working)
- TODO:
  + check FHS and ALT policy compliance
  + with/without logic of build (do we need shadow-auth support?)

* Sun Dec  1 2002 Seth Vidal <skvidal@phy.duke.edu>
- 0.99.4 and fix startup so it starts imap-master not vsftpd :)

* Tue Nov 26 2002 Seth Vidal <skvidal@phy.duke.edu>
- first build
