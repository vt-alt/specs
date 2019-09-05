%define ver 1.3.6

Name: proftpd
Version: %ver
Release: alt0.1.ga73dbfe3b

%define _libexecdir %{expand:%_libdir}
%def_disable tests

%define def_shared() %{expand:%{?1:%%global mod_shared_list %{?mod_shared_list:%mod_shared_list:}%*}}%{expand:%%global _shared_%1 1}%{expand:%%global _with_%1 1}
%define def_static() %{expand:%{?1:%%global mod_static_list %{?mod_static_list:%mod_static_list:}%*}}%{expand:%%global _static_%1 1}%{expand:%%global _with_%1 1}

%def_static mod_auth_pam
%def_static mod_readme

%def_shared mod_ctrls_admin
%def_shared mod_ifsession
%def_shared mod_ldap
%def_shared mod_quotatab
%def_shared mod_quotatab_file
%def_shared mod_quotatab_ldap
%def_shared mod_quotatab_sql
%def_shared mod_radius
%def_shared mod_ratio
%def_shared mod_rewrite
%def_shared mod_site_misc
%def_shared mod_sql
%def_shared mod_sql_mysql
#def_shared mod_sql_odbc
%def_shared mod_sql_passwd
%def_shared mod_sql_postgres
%def_shared mod_sql_sqlite
%def_shared mod_tls
%def_shared mod_tls_shmcache
%def_shared mod_tls_memcache
%def_shared mod_facl
%def_shared mod_load
%def_shared mod_sftp
%def_shared mod_sftp_pam
%def_shared mod_sftp_sql
%def_shared mod_ban
%def_shared mod_dynmasq
%def_shared mod_exec
%def_shared mod_shaper
%def_shared mod_unique_id
#def_shared mod_wrap2
#def_shared mod_wrap2_file
#def_shared mod_wrap2_sql

Summary: ProFTPd -- Professional FTP Server
License: GPL
Group: System/Servers
Url: http://www.%name.org/

Source: %name-%ver.tar
Source1: %name.logrotate
Source2: %name.xinetd
Source3: %name.init
Source4: %name.pamd
Source5: %name-control
Source6: %name.conf

Patch1: %name-man.patch
Patch2: %name-1.3.3rc1-alt-pkgconfig-prefix.patch
Patch4: %name-ldap-config.patch
Patch5: %name-1.2.10-iconv.patch
Patch6: %name-1.3.2rc1-mod_sql_mysql.patch
Patch7: %name-1.3.6-mod_sql_postgres.patch
Patch9: %name-1.3.0-alt-ltdl.patch
Patch10: %name-1.3.6-inc-pcre.patch
Patch11: %name-1.3.5-alt-mysql8-transition.patch

# Debian patches
Patch50: %name-deb-change_pam_name.patch
Patch51: %name-deb-core_create-home.patch

Provides: ftpserver
Requires: locale-en
PreReq: anonftp
AutoReq: yes, noshell, noperl

Packager: Afanasov Dmitry <ender@altlinux.org>

BuildRequires: gcc-c++ libncurses-devel libtinfo-devel zlib-devel libltdl-devel libpcre-devel
# ftpmail findreq
BuildRequires: perl-Mail-Sendmail

%{?_with_mod_auth_pam:BuildRequires: pam-devel}

%{?_with_mod_sql_mysql:BuildRequires: libMySQL-devel}
%{?_with_mod_ldap:BuildRequires: libldap-devel}
%{?_with_mod_sql_postgres:BuildRequires: libpq-devel postgresql-devel}
%{?_with_mod_tls:BuildRequires: libssl-devel}
%{?_with_mod_tls_memcache:BuildRequires: libmemcached-devel}
%{?_with_mod_facl:BuildRequires: libacl-devel}
%{?_with_mod_sql_sqlite:BuildRequires: libsqlite3-devel}
%{?_with_mod_facl:BuildRequires: libacl-devel}

%description
ProFTPd is an enhanced FTP server with a focus toward simplicity, security,
and ease of configuration.  It features a very Apache-like configuration
syntax, and a highly customizable server infrastructure, including support for
multiple 'virtual' FTP servers, anonymous FTP, and permission-based directory
visibility.

This package will setup ProFTPd for both inetd and standalone operations.

%package -n %name-mod_ctrls_admin
Summary: Module implementing admin control handlers
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_ifsession
Summary: Module supporting conditional per-user/group/class configuration contexts
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_ldap
Summary: LDAP password lookup module for ProFTPD
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_quotatab
Summary: Module for managing FTP byte/file quotas via centralized tables
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_quotatab_file
Summary: Sub-module for managing quota data via file-based tables
Group: System/Servers
Requires: %name-mod_quotatab = %version-%release

%package -n %name-mod_quotatab_ldap
Summary: Sub-module for obtaining quota information from an LDAP directory
Group: System/Servers
Requires: %name-mod_quotatab = %version-%release

%package -n %name-mod_quotatab_sql
Summary: Sub-module for managing quota data via SQL-based tables
Group: System/Servers
Requires: %name-mod_quotatab = %version-%release

%package -n %name-mod_radius
Summary: Module for RADIUS authentication and accounting
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_ratio
Summary: Support upload/download ratios
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_rewrite
Summary: Module for rewriting FTP commands
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_site_misc
Summary: Module implementing miscellaneous SITE commands
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_sql
Summary: SQL frontend
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_sql_passwd
Summary: Enables support for some of OpenSSL password formats
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_sql_mysql
Summary: Support for connecting to MySQL databases
Group: System/Servers
Requires: %name-mod_sql = %version-%release

%package -n %name-mod_sql_postgres
Summary: Support for connecting to Postgres databases
Group: System/Servers
Requires: %name-mod_sql = %version-%release

%package -n %name-mod_tls
Summary: An RFC2228 SSL/TLS module for ProFTPD
Group: System/Servers
Requires: %name = %version-%release


%package -n %name-mod_facl
Summary: POSIX ACL checking code (aka POSIX.1e hell)
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_ban
Summary: A ProFTPD module implementing ban lists using the Controls API
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_dynmasq
Summary: A ProFTPD module for DynDNS configurations
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_load
Summary: System load handling module for ProFTPD
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_sftp
Summary: A ProFTPD module implementing sftp server
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_sftp_pam
Summary: PAM authorization for mod_sftp ProFTPD sub-module
Group: System/Servers
Requires: %name-mod_sftp = %version-%release

%package -n %name-mod_sftp_sql
Summary: SQL authorization for mod_sftp ProFTPD sub-module
Group: System/Servers
Requires: %name-mod_sftp = %version-%release

%package -n %name-mod_sql_sqlite
Summary: Support for using SQLite databases
Group: System/Servers
Requires: %name-mod_sql = %version-%release

%package -n %name-mod_tls_shmcache
Summary: Implements shared SSL session cache
Group: System/Servers
Requires: %name-mod_tls = %version-%release

%package -n %name-mod_tls_memcache
Summary: Implements shared SSL/TLS session cache in memcache
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_exec
Summary: Executes external scripts
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_shaper
Summary: Implements rate throttling
Group: System/Servers
Requires: %name = %version-%release

%package -n %name-mod_unique_id
Summary: Generates unique ids
Group: System/Servers
Requires: %name = %version-%release


%package -n %name-control
Summary: ProFTPD control facility
Group: System/Servers
Requires: %name = %version-%release
Buildarch: noarch

%package -n %name-devel
Summary: ProFTPD development header files
Group: System/Servers
Requires: %name = %version-%release

%description -n %name-mod_ctrls_admin
This module implements administrative control actions for the ftpdctl program.

%description -n %name-mod_ifsession
Module supporting conditional per-user/group/class configuration contexts

%description -n %name-mod_ldap
LDAP password lookup module for ProFTPD

%description -n %name-mod_quotatab
Module for managing FTP byte/file quotas via centralized tables

%description -n %name-mod_quotatab_file
Sub-module for managing quota data via file-based tables

%description -n %name-mod_quotatab_ldap
Sub-module for obtaining quota information from an LDAP directory

%description -n %name-mod_quotatab_sql
Sub-module for managing quota data via SQL-based tables

%description -n %name-mod_radius
Module for RADIUS authentication and accounting

%description -n %name-mod_ratio
Support upload/download ratios

%description -n %name-mod_rewrite
Module for rewriting FTP commands

%description -n %name-mod_site_misc
Module implementing miscellaneous SITE commands

%description -n %name-mod_sql
SQL frontend

%description -n %name-mod_sql_passwd
The mod_sql_passwd module provides support for some password formats, which are
not supported by mod_sql. Such as MD5 or SHA1 passwords, base64-encoded or
hex-encoded, without the prefix which is required by mod_sql's "OpenSSL" SQLAuthType. 
   
When the mod_sql_passwd module is enabled, you can configure SQLAuthTypes of
"MD5", "SHA1", "SHA256", or "SHA512", as well as the existing types supported
by mod_sql. 

%description -n %name-mod_sql_mysql
Support for connecting to MySQL databases

%description -n %name-mod_sql_postgres
Support for connecting to Postgres databases

%description -n %name-mod_tls
An RFC2228 SSL/TLS module for ProFTPD

%description -n %name-mod_facl
POSIX ACL checking code (aka POSIX.1e hell)

%description -n %name-mod_ban
Module implementing ban lists using the Controls API

%description -n %name-mod_dynmasq
Module for dynamically updating MasqueradeAddress configurations, as when
DynDNS names are used

%description -n %name-mod_load
Module for refusing connections based on system load

%description -n %name-mod_sftp
SFTP server implementation

%description -n %name-mod_sftp_pam
SFTP PAM authentication.

%description -n %name-mod_sftp_sql
SFTP SQL authentication.

%description -n %name-mod_sql_sqlite
SQLite backend.

%description -n %name-mod_tls_shmcache
Module which provides a shared SSL session cache using SysV shared memory

%description -n %name-mod_tls_memcache
Module which provides a shared SSL session cache in a memcached server

%description -n %name-mod_exec
Module for executing external scripts

%description -n %name-mod_shaper
Module implementing daemon-wide rate throttling via IPC

%description -n %name-mod_unique_id
Module for generating a unique ID for each FTP session.

%description -n %name-devel
ProFTPD development header files

%description -n %name-control
This package contains control rules for proftpd - Professional FTP Daemon

See control(8) for details.

%prep
%setup -q -n %name-%ver
%patch1 -p2
%patch2 -p1
%patch4 -p1
#patch5 -p1
%patch6 -p1
%patch7 -p2
#%%patch9 -p1
%patch10 -p2
%patch11 -p0

# debian patches
%patch50 -p1
%patch51 -p1

%build
#__libtoolize --ltdl
%__autoconf
%configure \
        %{?_enable_debug:--enable-devel} \
        %{?_enable_tests:--enable-tests} \
        --libexecdir=%_libexecdir/%name \
        --with-pkgconfig=%_pkgconfigdir \
        --localstatedir=/var/run/proftpd \
        --enable-auth-pam \
        --enable-ctrls \
        --enable-largefile \
        --disable-rpath \
        --enable-autoshadow --enable-sendfile --enable-dso \
        --with-lastlog=/var/log/lastlog \
        --enable-openssl \
        --enable-nls \
        --enable-facl \
        --enable-memcache \
        --enable-pcre \
        --with-modules=%mod_static_list \
        --with-shared=%mod_shared_list

subst 's|^\(/var/tmp/proftpd-buildroot\)=.*$|\1=no|' libtool

%make

%install
myname=`id -un`
mygroup=`id -gn`

%make_install install DESTDIR=%buildroot INSTALL_USER=$myname INSTALL_GROUP=$mygroup

install -pD -m640 %SOURCE4 %buildroot%_sysconfdir/pam.d/%name
install -p -m644 -D %SOURCE6 %buildroot%_sysconfdir/%name.conf
install -p -m644 -D %SOURCE1 %buildroot%_sysconfdir/logrotate.d/%name
install -p -m644 -D %SOURCE2 %buildroot%_sysconfdir/xinetd.d/%name
install -p -m755 -D %SOURCE3 %buildroot%_initdir/%name
install -m755 contrib/xferstats.holger-preiss %buildroot%_sbindir

chmod 711 %buildroot%_sbindir/%name

ln -s -f %name %buildroot%_sbindir/in.%name
ln -s -f %name %buildroot%_sbindir/in.ftpd

install -pD -m755 %SOURCE5 %buildroot%_controldir/%name

echo >>%buildroot%_sysconfdir/ftpusers <<EOF
root
bin
daemon
adm
lp
sync
shutdown
halt
mail
news
uucp
operator
games
nobody
EOF

mkdir -p %buildroot/var/log/%name
rm -f %buildroot%_libexecdir/%name/*.a

%find_lang %name

%pre
if [ -e "%_controldir/%name" ]; then
    %pre_control %name
fi

%post
if grep -qe '^[[:blank:]]*CharsetLocal' %_sysconfdir/%name.conf; then
   echo "WARNING: iconv patch is disabled, do not use CharsetLocal/CharsetRemote" >&2
   echo "WARNING: see doc/modules/mod_lang.html for details" >&2
   echo "WARNING: autocommenting corresponding Options, please check" >&2
   subst 's/^\([[:blank:]]*CharsetLocal .*\)/# \1/' %_sysconfdir/%name.conf
   subst 's/^\([[:blank:]]*CharsetRemote .*\)/# \1/' %_sysconfdir/%name.conf
fi
if [ -e "%_controldir/%name" ]; then
    %post_control -s standalone %name
fi
%post_service %name

%preun
%preun_service %name

%files -f %name.lang
%doc README* ChangeLog INSTALL NEWS CREDITS doc/* contrib/README.*
%doc sample-configurations/* contrib/ftpasswd contrib/ftpquota
%attr(600,root,root) %config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/ftpusers
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_initdir/%name
%config(noreplace) %_sysconfdir/xinetd.d/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_sbindir/*
%_bindir/ftp*
%_man1dir/ftpasswd.*
%_man1dir/ftpmail.*
%_man1dir/ftpquota.*
%_man1dir/ftpwho.*
%_man1dir/ftpcount.*
%_man1dir/ftptop.*
%_man5dir/*
%_man8dir/%name.*
%_man8dir/ftpshut.*
%_man8dir/ftpdctl.*
%_man8dir/ftpscrub.*
%dir /var/run/%name
%dir /var/log/%name
%dir %_libexecdir/%name

%ifdef _shared_mod_ctrls_admin
%files -n %name-mod_ctrls_admin
%_libexecdir/%name/mod_ctrls_admin.*
%endif

%ifdef _shared_mod_ifsession
%files -n %name-mod_ifsession
%_libexecdir/%name/mod_ifsession.*
%endif

%ifdef _shared_mod_ldap
%files -n %name-mod_ldap
%_libexecdir/%name/mod_ldap.*
%endif

%ifdef _shared_mod_quotatab
%files -n %name-mod_quotatab
%_libexecdir/%name/mod_quotatab.*
%endif

%ifdef _shared_mod_quotatab_file
%files -n %name-mod_quotatab_file
%_libexecdir/%name/mod_quotatab_file.*
%endif

%ifdef _shared_mod_quotatab_ldap
%files -n %name-mod_quotatab_ldap
%_libexecdir/%name/mod_quotatab_ldap.*
%endif

%ifdef _shared_mod_quotatab_sql
%files -n %name-mod_quotatab_sql
%_libexecdir/%name/mod_quotatab_sql.*
%endif

%ifdef _shared_mod_radius
%files -n %name-mod_radius
%_libexecdir/%name/mod_radius.*
%endif

%ifdef _shared_mod_ratio
%files -n %name-mod_ratio
%_libexecdir/%name/mod_ratio.*
%endif

%ifdef _shared_mod_rewrite
%files -n %name-mod_rewrite
%_libexecdir/%name/mod_rewrite.*
%endif

%ifdef _shared_mod_site_misc
%files -n %name-mod_site_misc
%_libexecdir/%name/mod_site_misc.*
%endif

%ifdef _shared_mod_sql
%files -n %name-mod_sql
%_libexecdir/%name/mod_sql.*
%endif

%ifdef _shared_mod_sql_passwd
%files -n %name-mod_sql_passwd
%_libexecdir/%name/mod_sql_passwd.*
%endif

%ifdef _shared_mod_sql_mysql
%files -n %name-mod_sql_mysql
%_libexecdir/%name/mod_sql_mysql.*
%endif

%ifdef _shared_mod_sql_postgres
%files -n %name-mod_sql_postgres
%_libexecdir/%name/mod_sql_postgres.*
%endif

%ifdef _shared_mod_tls
%files -n %name-mod_tls
%_libexecdir/%name/mod_tls.*
%endif

%ifdef _shared_mod_facl
%files -n %name-mod_facl
%_libexecdir/%name/mod_facl.*
%endif

%ifdef _shared_mod_ban
%files -n %name-mod_ban
%_libexecdir/%name/mod_ban.*
%endif

%ifdef _shared_mod_dynmasq
%files -n %name-mod_dynmasq
%_libexecdir/%name/mod_dynmasq.*
%endif

%ifdef _shared_mod_load
%files -n %name-mod_load
%_libexecdir/%name/mod_load.*
%endif

%ifdef _shared_mod_sftp
%files -n %name-mod_sftp
%_libexecdir/%name/mod_sftp.*
%_sysconfdir/blacklist.dat
%_sysconfdir/dhparams.pem
%endif

%ifdef _shared_mod_sftp_pam
%files -n %name-mod_sftp_pam
%_libexecdir/%name/mod_sftp_pam.*
%endif

%ifdef _shared_mod_sftp_sql
%files -n %name-mod_sftp_sql
%_libexecdir/%name/mod_sftp_sql.*
%endif

%ifdef _shared_mod_sql_sqlite
%files -n %name-mod_sql_sqlite
%_libexecdir/%name/mod_sql_sqlite.*
%endif

%ifdef _shared_mod_tls_shmcache
%files -n %name-mod_tls_shmcache
%_libexecdir/%name/mod_tls_shmcache.*
%endif

%ifdef _shared_mod_tls_memcache
%files -n %name-mod_tls_memcache
%_libexecdir/%name/mod_tls_memcache.*
%endif

%ifdef _shared_devel
%files -n %name-devel
%_libexecdir/%name/devel.*
%endif

%ifdef _shared_control
%files -n %name-control
%_libexecdir/%name/control.*
%endif

%ifdef _shared_mod_exec
%files -n %name-mod_exec
%_libexecdir/%name/mod_exec.*
%endif

%ifdef _shared_mod_shaper
%files -n %name-mod_shaper
%_libexecdir/%name/mod_shaper.*
%endif

%ifdef _shared_mod_unique_id
%files -n %name-mod_unique_id
%_libexecdir/%name/mod_unique_id.*
%endif


%files -n %name-devel
%_bindir/prxs
%_includedir/%name
%_pkgconfigdir/*

%files -n %name-control
%_controldir/%name

%changelog
* Tue Jul 23 2019 L.A. Kostis <lakostis@altlinux.ru> 1.3.6-alt0.1.ga73dbfe3b
- Updated to 1.3.6-ga73dbfe3b.
- Fix mod_copy bug #4372 (Ensure that mod_copy checks for <Limits> for its SITE
  CPFR) (CVE-2019-12815) (closes #37056).
- Updated mod_sql_postgres patch.
- Updated -pcre patch.

* Wed Mar 06 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.3.5-alt6.rel.e
- Fix FTBFS against libmysqlclient21

* Wed Oct 10 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.5-alt5.rel.e
- Rebuild without libwrap.

* Tue Jan 02 2018 L.A. Kostis <lakostis@altlinux.ru> 1.3.5-alt4.rel.e
- 1.3.5e release:
  + Backported fix for "AllowChrootSymlinks off" checking each component
      for symlinks (CVE-2017-7418).
- minor .spec cleanup.

* Wed Dec 02 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.5-alt3.rel.a.1
- Rebuild with new libmemcached 1.0.18

* Fri May 29 2015 L.A. Kostis <lakostis@altlinux.ru> 1.3.5-alt3.rel.a
- 1.3.5a release.
- Increased rlimit to 64M for xinetd.

* Thu May 21 2015 Konstantin A. Lepikhov <lakostis@altlinux.ru> 1.3.5-alt2.gita31d0ab
- .spec fixes.

* Wed May 20 2015 Konstantin A. Lepikhov <lakostis@altlinux.ru> 1.3.5-alt1.gita31d0ab
- Updated to 1.3.5-a31d0ab GIT fixing following CVEs:
  + CVE-2013-4359.
- Include the fix for Bug 4169 (Unauthenticated copying of files
  via SITE CPFR/CPTO allowed by mod_copy).
- Configuration changes:
  + enabled pcre support;
  + enabled memcache support (mod_tls_memcache is using it).

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.3rel-alt2.qa1
- NMU: rebuilt with libmysqlclient.so.18.

* Fri Aug 19 2011 Afanasov Dmitry <ender@altlinux.org> 1.3.4rc2-alt1
- 1.3.4rc2

* Thu Nov 04 2010 Afanasov Dmitry <ender@altlinux.org> 1.3.3rel-alt2
- 1.3.3c stable release (closes: #24471)

* Tue Mar 23 2010 Afanasov Dmitry <ender@altlinux.org> 1.3.3rel-alt1
- 1.3.3 stable release
- add mod_sql_passwd

* Tue Mar 23 2010 Afanasov Dmitry <ender@altlinux.org> 1.3.3rc3-alt2
- raise rlimit_as (closes: #23208)

* Sat Dec 19 2009 Afanasov Dmitry <ender@altlinux.org> 1.3.3rc3-alt1
- 1.3.3rc3

* Tue Nov 17 2009 Afanasov Dmitry <ender@altlinux.org> 1.3.3rc2-alt1
- 1.3.3rc2

* Mon Oct 12 2009 Afanasov Dmitry <ender@altlinux.org> 1.3.3rc1-alt3
- fix initscript with new pidfile location (Closes: #21910)

* Thu Sep 03 2009 Afanasov Dmitry <ender@altlinux.org> 1.3.3rc1-alt2
- rebuild mod_ldap with libldap v2.4

* Mon Jul 20 2009 Afanasov Dmitry <ender@altlinux.org> 1.3.3rc1-alt1
- 1.3.3rc1
- build shared modules: mod_sftp, mod_sql_sqlite, mod_load, mod_ban,
  mod_dynmasq and others
- enable LangEngine in default config
- add patch alt-pkgconfig-prefix that prevents unnesessary prefix adding to
  pkgconfigdir.
- remove patches:
  + proftpd-typo-prxs (applied in upstream)

* Fri Feb 06 2009 Afanasov Dmitry <ender@altlinux.org> 1.3.2rel-alt1
- stable release
  + fixed encoding-dependent SQL injection vulnerability

* Tue Jan 27 2009 Afanasov Dmitry <ender@altlinux.org> 1.3.2rc4-alt1
- 1.3.2rc4
- remove O_CREATE patch (applied in upstream)

* Fri Nov 21 2008 Afanasov Dmitry <ender@altlinux.org> 1.3.2rc3-alt1
- build new version.

* Mon Nov 17 2008 Afanasov Dmitry <ender@altlinux.org> 1.3.2rc2-alt4
- fix build (open with O_CREAT)
- change packager

* Sun Nov 02 2008 Afanasov Dmitry <ender@altlinux.org> 1.3.2rc2-alt3
- package locale files for mod_lang.c

* Wed Sep 24 2008 Afanasov Dmitry <ender@altlinux.org> 1.3.2rc2-alt2
- comment AuthPAMConfig in default config
- change AuthPAMConfig value to 'proftpd'
- change session string to pam_tcb.so in pam config

* Tue Sep 23 2008 Afanasov Dmitry <ender@altlinux.org> 1.3.2rc2-alt1
- 1.3.2rc2

* Sun Sep 21 2008 Afanasov Dmitry <ender@altlinux.org> 1.3.2rc1-alt2
- merged lakostis@ changes

* Sat Sep 20 2008 L.A. Kostis <lakostis@altlinux.ru> 1.3.2rc1-alt1.1
- rollback -ltdl patch (again).

* Wed Sep 10 2008 Afanasov Dmitry <ender@altlinux.org> 1.3.2rc1-alt1
- build new version
- removed patches (merged upstream):
    - ctrls-restart
    - deb-SA23141
    - deb-CORE-2006-1127
    - deb-auth_fix
    - deb-auth_loop
    - deb-auth_cache (http://secunia.com/advisories/24867)
- removed HAVE_OPENSSL flag (pass --enable-openssl to configure script)
- built with --enable-nls (mod_lang)
- introduced devel subpackage (pkgconfig file included)
- use system libltdl from now on
- disabled iconv patch due to mod_lang features (doc/modules/mod_lang.html)
- added control facility (not depend from main package and requires
  independent install)

* Wed May 16 2007 L.A. Kostis <lakostis@altlinux.ru> 1.3.0rel-alt2
- 1.3.0a stable release.
- rollback alt-ltdl patch (use alternate variant).
- don't delete *.la files (due lt_dlopenext breakage in this case).
- remove previous CVE-2006-5815 fixes, use variant from Debian.
- change packager.
- cleanup obsoleted Conflicts.
- change pam service name to more appropriate.
- Add a bunch of Debian patches:
   - proftpd-deb-core_create-home.patch: to support script exec on home creation.
   - proftpd-1.3.0-deb-cve_2006_5815.patch: See
     http://bugs.proftpd.org/show_bug.cgi?id=2858 for details.
   - proftpd-1.3.0-deb-SA22803.patch: security bug Secunia SA22803 advisory
     (sreplace() abuse).
   - proftpd-1.3.0-deb-SA23141.patch: Secunia SA23141 advisory (mod_tls abuse).
   - proftpd-1.3.0-deb-CORE-2006-1127.patch: ProFTPD Controls Buffer Overflow,
     locally exploitable. This is fixed in 1.3.1.
   - proftpd-1.3.0-deb-auth-fix.patch: auth_fix (fixes taken from 1.3.1rc1).
     (cfr http://bugs.proftpd.org/show_bug.cgi?id=2721)
   - proftpd-1.3.0-deb-auth-loop.patch: avoid endless loop in auth modules.
   - proftpd-1.3.0-deb-auth-cache.patch: See
     http://bugs.proftpd.org/show_bug.cgi?id=2922 (ALT #11558).

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.0rel-alt1.3.1.0
- Fixed postgresql build dependencies.
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.0rel-alt1.3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Tue Nov 14 2006 L.A. Kostis <lakostis@altlinux.org> 1.3.0rel-alt1.3
- fix null reference in CVE-2006-5815 patch made by upstream.

* Mon Nov 13 2006 L.A. Kostis <lakostis@altlinux.org> 1.3.0rel-alt1.2
- Security fix for CVE-2006-5815 ("CommandBufferSize" Directive Remote Code
  Execution Vulnerability).

* Tue Aug 29 2006 LAKostis <lakostis at altlinux.org> 1.3.0rel-alt1.1
- fix %%setup.

* Mon Aug 28 2006 LAKostis <lakostis at altlinux.org> 1.3.0rel-alt1
- NMU;
- Change versioning due rpmvercmp complaints.

* Sun Aug 27 2006 LAKostis <lakostis at altlinux.org> 1.3.0-alt1
- NMU;
- 1.3.0;
- use system libltdl;
- update -conf patch for DSO changes (fixes #9825);
- add ctrls-restart.patch;
- use autoconf due changed configure.in.

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.0rc3-alt1.1.1
- Rebuilt with libldap-2.3.so.0.

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.0rc3-alt1.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Thu Dec 08 2005 Konstantin Timoshenko <kt@altlinux.ru> 1.3.0rc3-alt1
- 1.3.0rc3

* Mon Oct 17 2005 Konstantin Timoshenko <kt@altlinux.ru> 1.3.0rc2-alt1
- 1.3.0rc2

* Mon May 30 2005 Konstantin Timoshenko <kt@altlinux.ru> 1.3.0rc1-alt2
- rebuild with libpq4-devel

* Mon Apr 18 2005 Konstantin Timoshenko <kt@altlinux.ru> 1.3.0rc1-alt1
- 1.3.10rc1
- add local <-> remote charset conversion patch
- Multi package creation.

* Thu May 06 2004 Konstantin Timoshenko <kt@altlinux.ru> 1.2.10rc1-alt2
- rebuild with glibc-2.3

* Fri Apr 30 2004 Konstantin Timoshenko <kt@altlinux.ru> 1.2.10rc1-alt1
- 1.2.10rc1

* Fri Oct 31 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.2.9release-alt1
- 1.2.9 release

* Mon Oct 21 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.2.9rc3-alt1
- 1.2.9rc3

* Wed Sep 24 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.2.9rc2-alt3
- security fix

* Fri Sep 19 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.2.9rc2-alt2
- fix wrong prereq.

* Mon Sep 15 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.2.9rc2-alt1
- 1.2.9rc2

* Tue Jul 29 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.2.9rc1-alt1
- 1.2.9rc1
- Rewritten start/stop script to new rc scheme.

* Wed Mar 12 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.2.8release-alt1
- 1.2.8 release

* Fri Feb 07 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.2.8-alt2.rc1
- fix logrotate config.

* Mon Jan 20 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.2.8-alt1.rc1
- 1.2.8rc1

* Mon Nov 11 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.2.7-alt2.rc2
- rebuild with libwrap

* Thu Oct 24 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.2.7-alt1.rc2
- 1.2.7rc2

* Tue Oct 22 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.2.7-alt1.rc1
- 1.2.7rc1

* Mon Sep 16 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.2.6release-alt1
- 1.2.6 release

* Mon Aug 19 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.2.6rc2-alt1
- 1.2.6rc2

* Fri May 31 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.2.5rc3-alt1
- 1.2.5rc3

* Tue May 14 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.2.5rc2-alt1
- 1.2.5rc2
- Re-enable sendfile.

* Mon May 13 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.2.5rc1-alt2
- apply patch from CVS to fix bug with users being unable to overwrite files
  they have permission to (patch #7)
- remove --enable-sendfile from configure

* Thu Dec 20 2001 Konstantin Timoshenko <kt@altlinux.ru> 1.2.5rc1-alt1
- 1.2.5rc1.
- mod_wrap 1.2.3.
- fix pam configuration.

* Wed Dec 19 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.2.4-alt2
- Fixed glob problem.
- Updated pam configuration (needs checking).

* Mon Oct 22 2001 Konstantin Timoshenko <kt@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Fri Oct 19 2001 Konstantin Timoshenko <kt@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Wed Oct  3 2001 Kostya Timoshenko <kt@altlinux.ru> 1.2.2-alt3
- Enable AllowStoreRestart so FTP resume works.

* Fri Aug 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2.2-alt2
- Added "rlimit_as = 16M" to xinetd config.
- Fixed %%post/%%preun scripts.

* Tue Aug 21 2001 Kostya Timoshenko <kt@altlinux.ru> 1.2.2-alt1
- 1.2.2.
- added LDAP support v2.7.6
- added LDAP configuration directives to proftpd.conf
- patched makefile to compile mod_ldap

* Tue Apr 24 2001 Kostya Timoshenko <kt@altlinux.ru> 1.2.2rc2-alt1
- 1.2.2rc2

* Sun Mar 25 2001 Kostya Timoshenko <kt@petr.kz> 1.2.2rc1-ipl1mdk
- 1.2.2rc1
- fix configs to use nobody.nobody not nobody.nogroup to run as nogroup
  seems to no longer exist

* Fri Mar 16 2001 Kostya Timoshenko <kt@petr.kz> 1.2.1-ipl3mdk
- fix workaround for ls bug

* Sun Mar 11 2001 Kostya Timoshenko <kt@petr.kz> 1.2.1-ipl2mdk
- Don't enable Anonymous login by default.
- URL change from .net -> .org
- remove chkconfig entry

* Mon Mar  5 2001 Kostya Timoshenko <kt@petr.kz> 1.2.1-ipl1mdk
- 1.2.1
- fix xinetd config

* Wed Feb 28 2001 Kostya Timoshenko <kt@petr.kz> 1.2.0-ipl1mdk
- 1.2.0 final version

* Mon Feb 12 2001 Kostya Timoshenko <kt@petr.kz> 1.2.0rc3-ipl1mdk
- 1.2.0rc3: security update

* Wed Jan 24 2001 Kostya Timoshenko <kt@petr.kz>
- fix PASV mode bug

* Tue Jan 23 2001 Kostya Timoshenko <kt@petr.kz>
- fix proftpd.init
- rebuild for RE

* Wed Nov 01 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.0rc2-9mdk
- fix the anonymous login in proftpd configuration files.

* Wed Sep 27 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.0rc2-7mdk
- really fix inetd problem. We remnove it from /etc/inetd.conf, and let it
  run instandalone mode which seems to work quite fine ...

* Fri Sep 22 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.0rc2-6mdk
- really add the xinetd entry.

* Thu Sep 21 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.0rc2-5mdk
- include the chkconfig entry, but don't run chkconfig by default.
- add an xinetd entry.
- re-add the inetd.conf entry ...

* Fri Sep 15 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.0rc2-4mdk
- rebuild for the Big Move (tm) and hope that I don't break anything.
- remove inetd.conf entry (again, hoping that I don't break anything.)

* Tue Aug 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.0rc2-3mdk
- use of _initrddir.

* Wed Aug 23 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.0rc2-2mdk
- quick and ugly hack to fix wu-ftpd breakage when proftpd is uninstalled.
- change the description as the AUTH patch is no longer here.

* Sat Jul 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.0rc2-1mdk
- new version
- remove the packager tag (vincentscks)

* Wed Jul 19 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.2.0rc1-3mdk
- rebuild for directory changes

* Tue Jul 18 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.2.0rc1-2mdk
- add directory /var/log/proftpd
- add home directory /home/ftp
- add conflicts with anonftp
- fix so can install as nonroot
- add --enable-autoshadow to configure

* Wed Jul 12 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.2.0rc1-1mdk
- 1.2.0rc1
- macroization
- remove directory /home/ftp since we don't need it

* Fri Jun 30 2000 Vincent Danen <vdanen@linux-mandrake.com> 1.2.0pre10-2mdk
- merge with .spec file from Geoffrey Lee <snailtalk@linux-mandrake.com>:
- add logrotate entry
- add symlinks to in.proftpd and in.ftpd
- on uninstall, run /etc/rc.d/init.d/proftpd stop prior to uninstall
- compile with mod_pam support
- add Conflicts: wu-ftpd, ncftpd, beroftpd

* Fri May  5 2000 Vincent Danen <vdanen@linux-mandrake.com> 1.2.0pre10-1mdk
- build for Mandrake
- bzip sources
- bzip manpages
- remove multi-package creation.  one package does all... updates
  /etc/inetd.conf but defaults to standalone server type

* Thu Oct 3 1999 O.Elliyasa <osman@Cable.EU.org>
- Multi package creation.
  Created core, standalone, inetd (&doc) package creations.
  Added startup script for init.d
  Need to make the "standalone & inetd" packages being created as "noarch"
- Added URL.
- Added prefix to make the package relocatable.

* Wed Sep 8 1999 O.Elliyasa <osman@Cable.EU.org>
- Corrected inetd.conf line addition/change logic.

* Sat Jul 24 1999 MacGyver <macgyver@tos.net>
- Initial import of spec.
