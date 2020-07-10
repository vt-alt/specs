Name: exim
Version: 4.94
Release: alt2
Summary: Exim MTA
Group: Networking/Mail
License: GPLv2+
Source: %name-%version.tar.xz
URL: https://exim.org
Conflicts: postfix, sendmail
BuildRoot: %_tmppath/%name-%version-root

Requires: %name-config
Provides: smtpdaemon smtpd MTA MailTransferAgent
Provides: %name-light
Provides: %name-bin

BuildRequires: pkg-config perl libdb4-devel libpcre-devel libssl-devel
BuildRequires: libsqlite3-devel postgresql-devel libmariadb-devel
# for exigrep
BuildRequires: perl-Pod-Usage

%description
Exim is a highly flexible and feature-rich mail transfer agent
(MTA) with extensive facilities for processing incoming mail.

This package contains %name built with out-of-box virtual mail
domains support (that means, mail domain users are not related
to system users from /etc/passwd) - just install vmail-tools

If you need SQL-based accounts, look at %name-*sql* packages.


%package config
Summary: Configuration data for %name
Group: Networking/Mail
BuildArch: noarch
Requires: %name-bin
Requires: openssl
%description config
%summary

%package doc
Summary: Optional documentation for %name
Group: Documentation
BuildArch: noarch
%description doc
%summary

%package mysql
Summary: %name MTA with MySQL support
Group: Networking/Mail
Requires: %name-config
Provides: %name-bin
Provides: smtpdaemon, smtpd, MTA, MailTransferAgent
%description mysql
%summary

%package pgsql
Summary: %name MTA with PostgreSQL support
Group: Networking/Mail
Requires: %name-config
Provides: %name-bin
Provides: smtpdaemon, smtpd, MTA, MailTransferAgent
%description pgsql
%summary

%package sqlite
Summary: %name MTA with SQLite support
Group: Networking/Mail
Requires: %name-config
Provides: %name-bin
Provides: smtpdaemon, smtpd, MTA, MailTransferAgent
%description sqlite
%summary

%package tools
Summary: Postmaster tools for %name
Group: Networking/Mail
# for exigrep
Requires: perl-Pod-Usage
%description tools
%summary


%prep
%setup

%build
# build binaries for all known configurations
allconfigs=`echo Local-Makefile.* | sed -re 's,L[^.]+\.,,g'`
mkdir -p src/Local
sed -i -re 's/ -lnsl//g' src/OS/Makefile-Linux
cd src
for buildtype in $allconfigs
do
  rm -rf build-Linux-*
  cat ../Local-Makefile.$buildtype > Local/Makefile
  echo '' > src/version.sh
  echo EXIM_RELEASE_VERSION=%version >> src/version.sh
  echo EXIM_VARIANT_VERSION=%release >> src/version.sh
  echo EXIM_COMPILE_NUMBER=1 >> src/version.sh
  export CFLAGS="-I%_includedir/openssl -I%_includedir/pgsql"
  export LDFLAGS="-s -lpq"
  %make_build
  cp -a build-Linux-*/%name ./%name.$buildtype
done


%install
umask 022
cd src
make DESTDIR=%buildroot INSTALL_ARG=-no_chown install
rm -f %buildroot%_sbindir/%name %buildroot%_sbindir/%name-*

# now install real binaries
install -m 755 %name.* %buildroot%_sbindir/
# ghost symlink
ln -s exim.vmail %buildroot%_sbindir/%name

cd ..
rm -f %buildroot%_sysconfdir/%name/%name.conf
install -m 600 %name.conf \
	%buildroot%_sysconfdir/%name/%name.conf
cp -a %buildroot%_sysconfdir/%name/%name.conf{,.sample}

mv %buildroot/etc/aliases %buildroot/etc/aliases.sample
touch %buildroot%_sysconfdir/aliases
touch %buildroot%_sysconfdir/%name/mail-server.{crt,key}

mkdir -pm755 %buildroot%_initdir
install -m 755 %name.rc \
	%buildroot%_initdir/%name

mkdir -pm700 %buildroot%_sysconfdir/logrotate.d
install -m 600 %name.logrotate \
	%buildroot%_sysconfdir/logrotate.d/%name

install -m 755 mkcert %buildroot%_sbindir/%name-mkcert

mkdir -pm750 %buildroot%_logdir/%name
touch %buildroot%_logdir/%name/{main,panic,reject}.log


%clean
rm -rf %buildroot %_builddir/%name-%version


%post
ln -sf exim.vmail %_sbindir/exim

%post mysql
ln -sf exim.mysql %_sbindir/exim

%post pgsql
ln -sf exim.pgsql %_sbindir/exim

%post sqlite
ln -sf exim.sqlite %_sbindir/exim

%post config
test -s %_sysconfdir/aliases || cp -a %_sysconfdir/aliases{.sample,}
cd %_sysconfdir/%name
test -s mail-server.key || exim-mkcert


%files
%defattr(-,root,root)
%_sbindir/exim.vmail

%files mysql
%defattr(-,root,root)
%_sbindir/exim.mysql

%files pgsql
%defattr(-,root,root)
%_sbindir/exim.pgsql

%files sqlite
%defattr(-,root,root)
%_sbindir/exim.sqlite

%files config
%dir %_sysconfdir/%name
%dir %_logdir/%name
%config %_initdir/%name
%config %_sysconfdir/logrotate.d/%name
%attr(0640,root,mail) %config %_sysconfdir/aliases.sample
%attr(0640,root,mail) %ghost %config (noreplace) %_sysconfdir/aliases
%attr(0640,root,mail) %config %_sysconfdir/%name/*.conf.sample
%attr(0640,root,mail) %ghost %config (noreplace) %_sysconfdir/%name/mail-server.key
%attr(0640,root,mail) %ghost %config (noreplace) %_sysconfdir/%name/mail-server.crt
%attr(0640,root,mail) %config (noreplace) %_sysconfdir/%name/*.conf
%_sbindir/%name-mkcert
# symlink to actual binary
%ghost %_sbindir/%name
%ghost %_logdir/%name/*

%files tools
%_sbindir/exicyclog
%_sbindir/exigrep
%_sbindir/exim_checkaccess
%_sbindir/exim_dbmbuild
%_sbindir/exim_dumpdb
%_sbindir/exim_fixdb
%_sbindir/exim_lock
%_sbindir/eximstats
%_sbindir/exim_tidydb
%_sbindir/exinext
%_sbindir/exipick
%_sbindir/exiqgrep
%_sbindir/exiqsumm
%_sbindir/exiwhat

%files doc
%doc Readme.pod vmail-dovecot.txt

%changelog
* Tue Jul 07 2020 Gremlin from Kremlin <gremlin@altlinux.org> 4.94-alt2
- fix config permissions

* Tue Jul 07 2020 Gremlin from Kremlin <gremlin@altlinux.org> 4.94-alt1
- update to 4.94

* Tue Jul 07 2020 Gremlin from Kremlin <gremlin@altlinux.org> 4.92.3-alt2
- quick fix for the startup script (#38633)

* Mon Sep 30 2019 Gremlin from Kremlin <gremlin@altlinux.org> 4.92.3-alt1
- update to 4.92.3 (fix CVE-2019-16928)

* Thu Jun 20 2019 Gremlin from Kremlin <gremlin@altlinux.org> 4.92.1.0.1-alt1
- update to post-4.92.1 snapshot

* Thu Jun 20 2019 Gremlin from Kremlin <gremlin@altlinux.org> 4.92.0.1-alt1
- re-import from upstream and rebuild from scratch
