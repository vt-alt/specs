Name: postfix
Version: 2.11.11
Release: alt3
Epoch: 1

Summary: Postfix Mail Transport Agent
License: IBM Public License
Group: System/Servers
Url: http://www.postfix.org/

# ftp://ftp.porcupine.org/mirrors/postfix-release/official/postfix-%version.tar.gz
Source: %name-%version.tar.gz

Patch: postfix-%version-%release.patch

%def_with cdb
%def_with ldap
%def_with mysql
%def_with pcre
%def_with pgsql
%def_with sasl
%def_with cyrus
%def_with tls

# Chrooted environment
%define ROOT /var/spool/%name

# Configuration definitions below are here for both customization
# and to simplify building list of files for a package (converting
# postfix-files list to rpm's filelist).

%define _libexecdir /usr/libexec

%define queue_directory %_var/spool/%name
%define config_directory %_sysconfdir/%name

%define plugin_directory %_libdir/%name
%define daemon_directory %_libexecdir/%name
%define data_directory %_localstatedir/%name
%define program_directory %daemon_directory
%define command_directory %_sbindir

%define newaliases_path %_bindir/newaliases
%define mailq_path %_bindir/mailq
%define sendmail_path %_sbindir/sendmail

%define docdir %_docdir/%name-%version
%define manpage_directory %_mandir
%define html_directory %docdir/html
%define readme_directory %config_directory/README_FILES

%define mail_admin mailadm
%define mail_owner postfix
%define setgid_group postdrop
%define default_privs postman

%define restart_flag /var/run/%name.restart
%define libpostfix lib%name-%version.so
%define libpostfix_dict lib%{name}_dict-%version.so

%define _buildaltdir %_builddir/%name-%version/extra

Provides: MTA, MailTransportAgent
Provides: smtpd, smtpdaemon, %name-smtpd
Conflicts: sendmail, masqmail, exim
Obsoletes: %name-beta, %name-smtpd
Requires(pre): sendmail-common >= 1.3, chrooted >= 0.3, %name-control >= 1.6

# This is used to be MDA, but default postfix main.cf uses procmail.
Requires: procmail

BuildPreReq: rpm-build >= 4.0.4-alt0.3, sendmail-common >= 1.3, chrooted >= 0.3
%{?_with_cdb:BuildPreReq: libcdb-devel}
%{?_with_pcre:BuildPreReq: libpcre-devel}
%{?_with_ldap:BuildPreReq: libldap-devel}
%{?_with_mysql:BuildPreReq: libMySQL-devel}
%{?_with_pgsql:BuildPreReq: postgresql-devel}
%{?_with_cyrus:BuildPreReq: libsasl2-devel}
%{?_with_tls:BuildPreReq: libssl-devel}

# Automatically added by buildreq on Fri Oct 31 2003
BuildRequires: groff-base html2text libdb4-devel

%description
Postfix is Wietse Venema's attempt to provide an alternative to the
widely-used Sendmail program.  Postfix attempts to be fast, easy to
administer, and hopefully secure, while at the same time being sendmail
compatible enough to not upset your users.

%package ldap
Summary: LDAP map support for Postfix
Group: System/Servers
Requires: %name = %EVR

%description ldap
This package provides support for LDAP maps in Postfix.

%package mysql
Summary: MySQL map support for Postfix
Group: System/Servers
Requires: %name = %EVR

%description mysql
This package provides support for MySQL maps in Postfix.

%package pcre
Summary: PCRE map support for Postfix
Group: System/Servers
Requires: %name = %EVR

%description pcre
This package provides support for PCRE maps in Postfix.

%package pgsql
Summary: PostgreSQL map support for Postfix
Group: System/Servers
Requires: %name = %EVR

%description pgsql
This package provides support for PostgreSQL maps in Postfix.

%package cyrus
Summary: Cyrus SASL plugin for Postfix
Group: System/Servers
Requires: %name = %EVR

%description cyrus
This package provides Cyrus SASL support for Postfix.

%package dovecot
Summary: Dovecot SASL plugin for Postfix
Group: System/Servers
Requires: %name = %EVR

%description dovecot
This package provides Dovecot SASL support for Postfix.

%package tls
Summary: SSL/TLS support for Postfix
Group: System/Servers
Requires: %name = %EVR

%description tls
This package provides support for SSL/TLS in Postfix.

%package html
Summary: html documentation for Postfix
Group: System/Servers
BuildArch: noarch
Requires: %name = %EVR

%description html
This package provides documentation for Postfix in html format.

%package test-tools
Summary: Postfix testing tools
Group: System/Servers

%description test-tools
Various postfix testing tools

%prep
%setup
%patch -p1

find -type f -print0 |
	xargs -r0 grep -FZl @libdir@ -- |
	xargs -r0 sed -i 's,@libdir@,%_libdir,g' --

%if_with tls
rm -rf src/*-tls
for i in smtp smtpd; do
	cp -a src/$i src/$i-tls
done
%endif #with tls

# Add some makefile targets where appropriate.
sed -i 's/^update /&objs dicts xsasls /' Makefile.in
sed -i 's/^# do not edit below this line/objs: $(OBJS)\n\nobjs-print: objs\n\tls $(OBJS)\n\n&/' \
	src/*/Makefile.in

# Change program names for smtp and smtpd.
sed -i 's/^PROG[[:space:]]*=.*/&-std/' src/{smtp,smtpd}/Makefile.in
%if_with tls
sed -i 's/^PROG[[:space:]]*=.*/&-tls/' src/{smtp,smtpd}-tls/Makefile.in
%endif #with tls

# Remove license, makedefs.out, html documentation, man pages, readme files and sample files from master list.
sed -i '/\(LICENSE\|makedefs\.out\|\(html\|manpage\|readme\|sample\)_directory\)/ d' conf/%name-files
rm -f conf/LICENSE

# Adjust arch-dependent paths.
sed -i s,@LIB@,%_lib, conf/%name-files

# Fix build with util-linux-ng.
sed -i 's/col -bx |/LANG=en_US &/' proto/Makefile.in

# More std/tls tweaks for filelist.
sed -i 's,^.*/\(smtp\|smtpd\),&-std,' conf/%name-files
# comment out tls.*
sed -i 's/[^#]*tls/#&/' conf/%name-files

if [ "%_libexecdir" != "/usr/libexec" ]; then
	find -type f -print0 |
		xargs -r0 grep -FZl /usr/libexec -- |
		xargs -r0 sed -i 's,/usr/libexec,%_libexecdir,g' --
fi

# Create mynetworks and mydestination.
install -pm644 %_buildaltdir/mynetworks conf/
touch conf/mydestination

# Set executable bit on scripts we are going to execute later.
chmod a+x postfix-install %_buildaltdir/*.sh

# Force documentation re-generation
touch -t 01010000 man/*/* html/*

### BUILD ###
%build
OPT="%optflags -fno-strict-aliasing -Wno-comment -Wno-missing-braces"
CCARGS="\
 -DNO_NIS \
 -DDEF_COMMAND_DIR=\\\"%command_directory\\\" \
 -DDEF_CONFIG_DIR=\\\"%config_directory\\\" \
 -DDEF_DAEMON_DIR=\\\"%daemon_directory\\\" \
 -DDEF_DATA_DIR=\\\"%data_directory\\\" \
 -DDEF_PLUGIN_DIR=\\\"%plugin_directory\\\" \
 -DDEF_HTML_DIR=\\\"%html_directory\\\" \
 -DDEF_MAILQ_PATH=\\\"%mailq_path\\\" \
 -DDEF_MANPAGE_DIR=\\\"%manpage_directory\\\" \
 -DDEF_NEWALIAS_PATH=\\\"%newaliases_path\\\" \
 -DDEF_PROGRAM_DIR=\\\"%program_directory\\\" \
 -DDEF_QUEUE_DIR=\\\"%queue_directory\\\" \
 -DDEF_README_DIR=\\\"%readme_directory\\\" \
 -DDEF_SAMPLE_DIR=\\\"%readme_directory\\\" \
 -DDEF_SENDMAIL_PATH=\\\"%sendmail_path\\\" \
"
DICTS=
DICT_LIBS="-ldb"
DICT_ARGS=
SYSLIBS="-lresolv -ldl"
AUXLIBS=

%if_with sasl
# USE_SASL_AUTH is used by smtp, smtpd and xsasl
CCARGS="$CCARGS -DUSE_SASL_AUTH"
%endif #with sasl

%if_with cdb
DICT_ARGS="$DICT_ARGS -DHAS_CDB"
DICT_LIBS="$DICT_LIBS -lcdb"
%endif #with cdb

%if_with ldap
DICT_ARGS="$DICT_ARGS -DHAS_LDAP"
DICTS="$DICTS \$(DICT_LDAP)"
%endif #with ldap

%if_with mysql
DICT_ARGS="$DICT_ARGS -DHAS_MYSQL -I%_includedir/mysql"
DICTS="$DICTS \$(DICT_MYSQL)"
%endif #with mysql

%if_with pcre
DICT_ARGS="$DICT_ARGS -DHAS_PCRE `pcre-config --cflags`"
DICTS="$DICTS \$(DICT_PCRE)"
%endif #with pcre

%if_with pgsql
DICT_ARGS="$DICT_ARGS -DHAS_PGSQL -I%_includedir/pgsql"
DICTS="$DICTS \$(DICT_PGSQL)"
%endif #with pgsql

%if_with tls
# USE_TLS is used by smtp, smtpd, tls and tlsmgr
TLS_ARGS="-DUSE_TLS $(pkg-config libssl --cflags)"
TLS_LIBS='-lssl -lcrypto'
TLS_DIRS='src/tls src/tlsmgr src/tlsproxy src/smtp-tls src/smtpd-tls'
%endif #with tls

## Shared build model; suggested by mjt.
pushd src

# 0. Prepare.
make	-C .. \
	tidy makefiles \
	SYSLIBS="$SYSLIBS" \
	AUXLIBS="$AUXLIBS" \
	CCARGS="$CCARGS $DICT_ARGS -UUSE_TLS" \
	OPT="$OPT" \
	DEBUG=

# 1. build all static libs objects with %optflags_shared.
%make_build -C .. \
	update \
	DEBUG='%optflags_shared' PROG= \
	DIRS='$(LIB_DIRS)'

# 2. separate libs objects into dict-dependent and others.
for a in */*.a; do
	ar t "$a" |
		sed -ne "s,.*,${a%%/*}/&,p"
done | sort -u >postfix_all_obj.list
%_buildaltdir/lorder.sh `cat postfix_all_obj.list` |
	sort -u |
	sort -k2,2 >postfix_lorder.list
printf '%%s\n%%s\n' util/dict_{c,}db.o |
	%_buildaltdir/oclosure.sh postfix_lorder.list >postfix_dict_obj.list
join -v1 postfix_all_obj.list postfix_dict_obj.list >postfix_common_obj.list

# 3. build %libpostfix shared library.
gcc -shared -o ../lib/%libpostfix \
	-Wl,-O1 -Wl,-soname,%libpostfix \
	`cat postfix_common_obj.list` \
	$SYSLIBS
ln -s %libpostfix ../lib/libpostfix.so

# 4. build %libpostfix_dict shared library.
gcc -shared -o ../lib/%libpostfix_dict \
	-Wl,-O1 -Wl,-soname,%libpostfix_dict \
	`cat postfix_dict_obj.list` \
	../lib/libpostfix.so $DICT_LIBS
ln -s %libpostfix_dict ../lib/libpostfix_dict.so

# 5.1 build libtls.a.
%make_build -C .. DIRS=src/tls update

# 5.2 build applications objects.
%make_build -C .. objs

# 6. build dict-dependent applications with %libpostfix and %libpostfix_dict.
dict_build_dirs=
for d in *; do
	[ -f "$d/Makefile" ] || continue
	%_buildaltdir/lorder.sh `cat postfix_dict_obj.list` \
	             `MAKEFLAGS= make -C "$d" -s objs-print |sed -e "s,^,$d/,"` |
		sort -u |
		sort -k2,2 |
		join -1 1 -2 2 -o 2.1 postfix_dict_obj.list - |
		sort -u |join -v1 - postfix_dict_obj.list |
		fgrep -qs "$d"/ || continue
	dict_build_dirs="$dict_build_dirs src/$d"
done
%make_build -C .. \
	LIBS='../../lib/libpostfix_dict.so ../../lib/libpostfix.so ../../lib/libtls.a' \
	DIRS="$dict_build_dirs" \
	SYSLIBS= \
	AUXLIBS= \
	#

# 7. build other applications with %libpostfix only.
%make_build -C .. \
	LIBS=../../lib/libpostfix.so \
	SYSLIBS= \
	AUXLIBS= \
	#

# 8. build dicts.
%make_build -C .. dicts \
	DIRS="src/util src/global" \
	DEBUG='%optflags_shared' \
	LIBS='../../lib/libpostfix_dict.so ../../lib/libpostfix.so' \
	SYSLIBS= \
	AUXLIBS= \
	DICTS="$DICTS" \
	#

# 9. build xsasl plugins.
%if_with sasl
%make_build -C .. xsasls \
	DIRS='src/xsasl' \
	DEBUG='%optflags_shared' \
	LIBS='../../lib/libpostfix.so' \
	SYSLIBS= \
	AUXLIBS= \
	XSASLS='$(XSASL_DOVECOT)%{?_with_cyrus: $(XSASL_CYRUS)}' \
	#
%endif #with sasl

popd # src

# SMP build seems to be broken here.
for d in proto man html; do
	make -C $d -f Makefile.in clobber
done
make manpages

%if_with tls
make	makefiles \
	DIRS="$TLS_DIRS" \
	SYSLIBS= \
	AUXLIBS= \
	CCARGS="$CCARGS $TLS_ARGS" \
	OPT="$OPT" \
	DEBUG=

%make_build \
	DIRS="$TLS_DIRS" \
	LIBS='../../lib/libpostfix_dict.so ../../lib/libpostfix.so ../../lib/libtls.a' \
	SYSLIBS="$TLS_LIBS $DICT_LIBS $SYSLIBS" \
	AUXLIBS= \
	#
%endif #with tls

install -pm644 /usr/share/sendmail-common/aliases conf/
mkdir -p libexec/postqueue
mv bin/postqueue libexec/postqueue/

### INSTALL ###
%install
mkdir -p %buildroot{%ROOT,%_bindir,%_sbindir,%_libdir,%daemon_directory/postqueue,%plugin_directory,%_mandir}

# Install shared libraries and dictionaries.
install -p -m644 lib/%libpostfix lib/%libpostfix_dict %buildroot%_libdir/
install -p -m644 src/*/dict_*.so src/xsasl/xsasl_*.so \
	%buildroot%plugin_directory/ ||:

:>%name.files
# Postfix's postfix-install script accept various parameters both in
# command line and as environment variables.  Better to reset environment
# here, so no locally-set variable will give any surprise.
env -i "LD_LIBRARY_PATH=%buildroot%_libdir" \
	./postfix-install -non-interactive \
		install_root=%buildroot \
		tempdir=%_tmppath

# install testing tools
install bin/*-* %buildroot%_bindir/

# install minimal main.cf
mv %buildroot%config_directory/main.cf{,.dist}
install -pm644 %_buildaltdir/main.cf %buildroot%config_directory/

# prepare for std
for i in smtp smtpd; do
	ln -snf $i-std %buildroot%daemon_directory/$i
done
ln -snf smtp %buildroot%daemon_directory/lmtp

%if_with tls
install -pm755 libexec/{*-tls,tlsmgr,tlsproxy} %buildroot%daemon_directory/
install -pm755 bin/posttls* %buildroot%_bindir/
%endif #with tls

# Finish postqueue install.
chmod 700 %buildroot%daemon_directory/postqueue
ln -rsnf %buildroot%daemon_directory/postqueue/postqueue \
	%buildroot%command_directory/

install -pD -m755 %_buildaltdir/init \
	%buildroot%_initdir/%name
install -pD -m644 %_buildaltdir/%name.service \
	%buildroot%_unitdir/%name.service
install -pD -m755 %_buildaltdir/cron.daily \
	%buildroot%_sysconfdir/cron.daily/%name
install -pD -m750 %_buildaltdir/chroot.lib \
	%buildroot%_sysconfdir/chroot.d/%name.lib
install -pD -m750 %_buildaltdir/chroot.conf \
	%buildroot%_sysconfdir/chroot.d/%name.conf
install -pD -m750 %_buildaltdir/chroot.all \
	%buildroot%_sysconfdir/chroot.d/%name.all
%if_with tls
install -pm755 %_buildaltdir/postfix-generate-ssl-certificate \
	%buildroot%_sbindir/
%endif #with tls

# Install filetrigger.
mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/%name.filetrigger <<'EOF'
#!/bin/sh
LC_ALL=C grep -Fqs %_sbindir/postfix &&
	[ -f %restart_flag ] ||
	exit 0
rm -f %restart_flag
service %name start
exit 0
EOF
chmod 0755 %buildroot%_rpmlibdir/%name.filetrigger

# Install /etc/aliases.
ln -rsnf %buildroot%config_directory/aliases %buildroot%_sysconfdir/

# Install manpages
cp -a man/man{1,5,8} %buildroot%manpage_directory/

# Install qshape and rmail.
install -p -m755 auxiliary/qshape/qshape.pl %buildroot%_bindir/qshape
install -p -m755 auxiliary/rmail/rmail %buildroot%_bindir/

rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir

cp -a html examples *README* COMPATIBILITY HISTORY LICENSE PORTING RELEASE_NOTES \
	%buildroot%docdir/
xz -9 %buildroot%docdir/HISTORY
%if_with tls
mkdir -p %buildroot%docdir/tls
cp -a TLS_* %buildroot%docdir/
xz -9 %buildroot%docdir/TLS_CHANGES
%endif #with tls

install -pm644 IPv6-ChangeLog %buildroot%docdir/
xz -9 %buildroot%docdir/IPv6-ChangeLog

# Install README_FILES.
rm -rf %buildroot%config_directory/README_FILES
mkdir -p %buildroot%docdir/README_FILES
ln -rsnf %buildroot%docdir/README_FILES %buildroot%config_directory/

# Install README.ALT
install -pm644 %_buildaltdir/README.ALT-ru_RU.utf8 %buildroot%docdir/

touch %buildroot%config_directory/{access,aliases,canonical,relocated,transport,virtual}.{cdb,db}

# syslog.d
mkdir -pm700 %buildroot%_sysconfdir/syslog.d
ln -s %ROOT/dev/log %buildroot%_sysconfdir/syslog.d/%name

# Chrooted environment
touch %buildroot%ROOT%_sysconfdir/{localtime,hosts,services,{host,nsswitch,resolv}.conf}
mksock %buildroot%ROOT/dev/log

# Remove sendmail-common files
rm %buildroot%_bindir/{mailq,newaliases}

### RUNTIME SCRIPTS ###

%pre
/usr/sbin/groupadd -r -f %setgid_group
/usr/sbin/groupadd -r -f %mail_owner
/usr/sbin/groupadd -r -f %default_privs
/usr/sbin/groupadd -r -f %mail_admin
/usr/sbin/useradd -r -n -g %name -d %ROOT -s /dev/null -c %name %name >/dev/null 2>&1 ||:
/usr/sbin/useradd -r -n -g %default_privs -d /dev/null -s /dev/null -c %default_privs %default_privs >/dev/null 2>&1 ||:

rm -f %restart_flag
if [ $1 -ge 2 ]; then
	SYSTEMCTL=systemctl
	if sd_booted && $SYSTEMCTL --version >/dev/null 2>&1; then
		$SYSTEMCTL is-active %name.service >/dev/null 2>&1 &&
		$SYSTEMCTL stop %name.service &&
		touch %restart_flag ||:
	else
		%_initdir/%name status >/dev/null 2>&1 &&
		%_initdir/%name stop &&
		touch %restart_flag ||:
	fi
	if [ ! -f %daemon_directory/postqueue/postqueue -a \
	       -f %command_directory/postqueue -a \
	     ! -L %command_directory/postqueue ]; then
		mkdir -pm755 %daemon_directory/postqueue &&
		cp -pf %command_directory/postqueue %daemon_directory/postqueue/
	fi
	/usr/sbin/control-dump %name postqueue
fi

oua=/usr/sbin/update-alternatives
if [ -x "$oua" ]; then
	"$oua" --remove aliases %config_directory/aliases >/dev/null 2>&1 ||:
fi

%post
if [ $1 -eq 1 ]; then
	chkconfig --add %name
else
	chkconfig %name resetpriorities
	SYSTEMCTL=systemctl
	sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1 &&
		"$SYSTEMCTL" daemon-reload ||:
fi
rm -f %config_directory/{access,aliases,canonical,relocated,transport,virtual}.{,c}db
%_libexecdir/postfix/post-install \
	config_directory=%config_directory \
	daemon_directory=%daemon_directory \
	upgrade-package
if [ $1 -ge 2 ]; then
	ALIASES=%config_directory/aliases /usr/share/sendmail-common/rebuild_aliases
	%_sysconfdir/chroot.d/%name.all --force
	/usr/sbin/control-restore %name postqueue
else
	/usr/sbin/control %name local
	/usr/sbin/control postqueue public
fi

%preun
if [ $1 = 0 ]; then
	service %name condstop
	chkconfig --del %name
	rm -f %ROOT/lib/* %ROOT%_sysconfdir/* %ROOT/var/yp/binding/* \
		%ROOT/var/nis/NIS_COLD_START
fi

%if_with tls
%post tls
for n in smtp smtpd; do
      ln -snf "$n"-tls %daemon_directory/"$n"
done
sed -i 's/^#\(.*tls\)/\1/' %daemon_directory/%name-files
%_libexecdir/postfix/post-install upgrade-package

%preun tls
if [ $1 = 0 ]; then
	for n in smtp smtpd; do
	      ln -snf "$n"-std %daemon_directory/"$n"
	done
	sed -i 's/[^#]*tls/#&/' %daemon_directory/%name-files
fi
%endif #with tls

%triggerpostun -- sendmail, exim, %name <= 0:20010228
[ $1 = 0 ] || exit 0
ln -snf %name/aliases %_sysconfdir/aliases
%_sysconfdir/chroot.d/%name.all

%files -f %name.files
%config %config_directory/main.cf.dist
%config %_initdir/%name
%config(noreplace) %_sysconfdir/cron.daily/%name
%config %_sysconfdir/chroot.d/*
%_sysconfdir/aliases
%ghost %attr(644,root,root) %config(missingok) %verify(not md5 mtime size) %config_directory/*.db
%ghost %attr(644,root,root) %config(missingok) %verify(not md5 mtime size) %config_directory/*.cdb
%attr(-,root,root) %daemon_directory/lmtp
%attr(-,root,root) %daemon_directory/smtp
%attr(-,root,root) %daemon_directory/smtpd
%_unitdir/%name.service
%_rpmlibdir/%name.filetrigger
%_sysconfdir/syslog.d/%name
%_libdir/%libpostfix
%_libdir/%libpostfix_dict
%attr(700,root,root) %verify(not mode,group) %dir %daemon_directory/postqueue
%command_directory/postqueue
%dir %plugin_directory
%_bindir/qshape
%_bindir/rmail
%_mandir/man?/*
%exclude %_mandir/man1/*-*
%if_with tls
%exclude %_mandir/man?/*tls*
%endif #with tls

%doc %config_directory/README_FILES
%dir %docdir
%docdir/examples
%docdir/[A-Z]*
%if_with tls
%exclude %docdir/TLS_*
%endif # with tls

# Chrooted environment
%attr(644,root,root) %verify(not md5 mtime size) %ghost %ROOT%_sysconfdir/*
%attr(666,root,root) %ghost %ROOT/dev/log

%files test-tools
%_bindir/*-*
%_mandir/man1/*-*

%files html
%dir %docdir
%docdir/html

%if_with ldap
%files ldap
%dir %plugin_directory
%plugin_directory/dict_ldap.so
%endif #with ldap

%if_with mysql
%files mysql
%dir %plugin_directory
%plugin_directory/dict_mysql.so
%endif #with mysql

%if_with pcre
%files pcre
%dir %plugin_directory
%plugin_directory/dict_pcre.so
%endif #with pcre

%if_with pgsql
%files pgsql
%dir %plugin_directory
%plugin_directory/dict_pgsql.so
%endif #with pgsql

%if_with sasl
%if_with cyrus
%files cyrus
%dir %plugin_directory
%plugin_directory/xsasl_cyrus.so
%endif #with cyrus

%files dovecot
%dir %plugin_directory
%plugin_directory/xsasl_dovecot.so
%endif #with sasl

%if_with tls
%files tls
%_sbindir/postfix-generate-ssl-certificate
%_mandir/man8/*tls*
%dir %daemon_directory
%daemon_directory/*-tls
%daemon_directory/tlsmgr
%daemon_directory/tlsproxy
%dir %docdir
%docdir/TLS_*
%endif #with tls

%changelog
* Sun Jul 05 2020 Dmitry V. Levin <ldv@altlinux.org> 1:2.11.11-alt3
- Fixed build on linux 5.x.

* Thu Apr 11 2019 Dmitry V. Levin <ldv@altlinux.org> 1:2.11.11-alt2
- chroot.conf: do not apply alias_maps update rules to alias_database files.
- dict_mysql: backported MySQL 8.x support.
- tls: backported assorted upstream (by vt@).

* Sun Jan 28 2018 Dmitry V. Levin <ldv@altlinux.org> 1:2.11.11-alt1
- 2.11.7 -> 2.11.11.
- Disabled NIS/NIS+ support as it was disabled in glibc-2.26.0.124.98f244e-alt1.
- Restart postfix from filetrigger (closes: #21620).
- Save a copy of %config_directory/aliases before rewriting it (closes: #25238).
- Fixed "postconf -a" and "postconf -A" (closes: #28372).
- Fixed Cyrus SASL support (by asy@; closes: #30270).
- Fixed update procedure when systemd is active (closes: #31363).
- Recoded README.ALT-ru_RU from koi8r to utf8 (closes: #32038).
- Cleared executable bit from postfix.service (closes: #34567).

* Wed Mar 02 2016 Fr. Br. George <george@altlinux.ru> 1:2.11.7-alt2
- Making /etc/sysconfig/network optional (closes: #31827)
- Extra/chroot.conf: added support for alias_maps (closes: #31822)
- Disable TLS micro version check (closes: #31752)

* Wed Oct 14 2015 Fr. Br. George <george@altlinux.ru> 1:2.11.7-alt1
- Version upgrade (still on legacy branch)
- Test tools package addded (closes: #28476)

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 1:2.11.3-alt1
- Autobuild version bump to 2.11.3

* Wed May 14 2014 Fr. Br. George <george@altlinux.ru> 1:2.11.1-alt1
- Autobuild version bump to 2.11.1
- Patch fixed

* Wed Feb 05 2014 Fr. Br. George <george@altlinux.ru> 1:2.10.3-alt1
- Autobuild version bump to 2.10.3

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 1:2.10.2-alt1
- Autobuild version bump to 2.10.2
- Next bugfix release

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 1:2.10.1-alt1
- Autobuild version bump to 2.10.1
- Bugfix release

* Mon Apr 22 2013 Fr. Br. George <george@altlinux.ru> 1:2.10.0-alt1
- Version up
- Use upstream "postconf -x" instead of "postconf -E"

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 1:2.9.5-alt1
- Autobuild version bump to 2.9.5
- Bugfix release

* Mon Nov 26 2012 Fr. Br. George <george@altlinux.ru> 1:2.9.4-alt3
- Reimplement 2.5-style postconf -E (still no default values evaluation)

* Mon Nov 19 2012 Fr. Br. George <george@altlinux.ru> 1:2.9.4-alt2
- Fix ill-applied ignore-system-user patch
- Add systemd service

* Mon Oct 29 2012 Fr. Br. George <george@altlinux.ru> 1:2.9.4-alt1
- Autobuild version bump to 2.9.4
- Bugfix release

* Tue Aug 14 2012 Fr. Br. George <george@altlinux.ru> 1:2.9.3-alt3
- Remove obsoleted MAKEFLAGS from spec
- Implement and settle "inet_protocols = any" configuration option

* Tue Jul 31 2012 Fr. Br. George <george@altlinux.ru> 1:2.9.3-alt2
- Fix postscreen open after close + chroot misfeature

* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 1:2.9.3-alt1
- Version up to 2.9.3 (4 middle-version jumps!)
- Reverting generated files patches
- Settle tlsproxy on postfix-tls
- Heavy merge of old ALT patches

* Thu Jul 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.14-alt1
- Updated to 2.5.14.

* Mon May 09 2011 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.13-alt1
- Updated to 2.5.13 (fixes CVE-2011-1720 in SMTP server Cyrus SASL support).

* Tue Mar 08 2011 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.12-alt1
- Updated to 2.5.12.

* Sat Dec 04 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.11-alt1
- Updated to 2.5.11.

* Wed Nov 03 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.9-alt4
- Fixed a namespace conflict (closes: #24496).

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.9-alt3
- Rebuilt with libssl.so.10 and libmysqlclient.so.16.

* Tue Sep 01 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.9-alt2
- Fixed SSL certificate generation conditions check (closes: #21164).

* Mon Aug 31 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.9-alt1
- Updated to 2.5.9.

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.7-alt3
- Changed startup script to generate SSL certificate
  if %name-tls is installed (closes: #21164).

* Mon Jun 08 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.7-alt2
- Fixed main.cf.params generation to make it always sorted.

* Tue May 12 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.7-alt1
- Updated to 2.5.7.

* Tue Mar 03 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.6-alt1
- Updated to 2.5.6.

* Thu Dec 04 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.5.5-alt1
- Updated to 2.5.5.

* Sun Nov 30 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.9-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Packaged html subpackage as noarch.
- Do not package MEMCACHE_README* unless memcache support is enabled (closes: #18046).

* Sun Aug 31 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.9-alt1
- Updated to 2.4.9 (fixes potential epoll file descriptor leak).

* Sat Aug 09 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.8-alt2
- Fixed build with kerberized openssl.

* Tue Aug 05 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.8-alt1
- Updated to 2.4.8 (fixes CVE-2008-2936).

* Mon Feb 25 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.7-alt1
- Updated to 2.4.7.

* Sun Dec 23 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.6-alt3
- Fixed build of documentation.

* Sun Dec 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.6-alt2
- main.cf: Removed unneeded unknown_local_recipient_reject_code.
- post-install: Fixed adding missing entry for retry service.

* Tue Dec 04 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.6-alt1
- Updated to 2.4.6.
- postconf: Enabled "-E" option support.
- /etc/chroot.d/postfix.conf: Use "postconf -E" (fixes #12282).

* Tue Oct 23 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.13-alt1
- Updated to 2.3.13.

* Tue Aug 07 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.12-alt1
- Updated to 2.3.12.

* Thu May 31 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.11-alt1
- Updated to 2.3.11.

* Wed May 02 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.9-alt1
- Updated to 2.3.9.

* Fri Mar 30 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.8-alt1.1
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Thu Mar 08 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.8-alt1
- Updated to 2.3.8.

* Fri Mar 02 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.7-alt4
- Fixed postfix-cyrus configuration on x86-64,
  reported by Vladimir V. Kamarzin.

* Tue Feb 27 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.7-alt3
- Fixed postfix-tls, reported by Vladimir V. Kamarzin.

* Mon Feb 26 2007 Stanislav Ievlev <inger@altlinux.org> 1:2.3.7-alt2.1
- master.cf: add content filter

* Fri Feb 16 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.7-alt2
- Enabled build of Dovecot SASL plugin by default.
- main.cf.dist:
  Added comments about message_size_limit and mailbox_size_limit (#7923).

* Sun Feb 11 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.7-alt1
- Updated to 2.3.7.
- Enabled SASL support by default.
- Disabled memcache by default.
- Minimized default main.cf file.
- Stripped postfix version from plugin file names.
- Implemented dynamic loading of xsasl plugins.
- Build Cyrus SASL plugin by default.
- Changed daemon_directory to /usr/libexec/%name.
- Changed plugin_directory to %%_libdir/%name.
- Changed default parameters:
  biff = no
  mydestination = $myhostname, localhost.$mydomain, localhost, $config_directory/mydestination
  smtpd_data_restrictions = reject_unauth_pipelining
  smtpd_etrn_restrictions = permit_mynetworks, reject
  smtpd_helo_required = yes

* Sat Sep 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.11-alt2
- Fixed default path to sasl plugins on multilib arches (closes #9975).

* Sun Jul 30 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.11-alt1
- Updated to 2.2.11.
- Changed postfix-install script to avoid adding default installation
  parameters to main.cf and therefore avoid potential upgrade problems
  (closes #9747).

* Thu May 25 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.10-alt2
- print_unknown_params: Fixed typo.

* Fri Apr 07 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.10-alt1
- Updated to 2.2.10.

* Fri Mar 24 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.9-alt3
- Reverted version change introduced by 2.2.10-RC1 patch (#9314).

* Fri Mar 17 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.9-alt2
- Updated to 2.2.10-RC1.
- postfix-script(check-warn):
  + If main.cf contains unknown parameters, print them.
- postconf(5): Document this change.
- init.d/postfix(check):
  + Disabled "postfix check" output redirection.
- Added dict_memcache, patch from ns@ and lakostis@.

* Mon Mar 06 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.9-alt1
- Updated to 2.2.9.

* Thu Jan 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.8-alt1
- Updated to 2.2.8.

* Tue Dec 13 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.7-alt1
- Updated to 2.2.7.

* Fri Dec 02 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.6-alt1
- Updated to 2.2.6.

* Sun Nov 06 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.5-alt2
- Added x86_64 support (fixes #8111).
- Enhanced mailbox_unpriv_delivery patch.

* Tue Aug 09 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.5-alt1
- Updated to 2.2.5.
- Updated deb-man patch.

* Wed Jun 29 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.4-alt3
- Changed default database type:
  alias_database = cdb:/etc/postfix/aliases
  alias_maps = cdb:/etc/postfix/aliases
  default_database_type = cdb
- Hardened $queue_directory/maildrop directory permissions.
- Enhanced documentation of ALT-specific changes of defaults.

* Sat Jun 25 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.4-alt2
- Packaged qshape.

* Thu Jun 23 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.4-alt1
- Updated to 2.2.4.
- Rediffed patches.

* Mon Jun 13 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.2.3-alt1
- Removed no longer needed deb-tls-master.cf patch.
- Updated alt-post-install patch to handle new services properly.
- Updated awk build scripts to handle new master.cf properly.
- Minor README.ALT tweaks.

* Thu Jun 12 2005 LAKostis <lakostis at altlinux.org> 1:2.2.3-alt0.5
- Returned back to old build model, with tls and sasl enabled together.
- Removed sed from build dependencies.
- Updated sasl_config patch for 2.2.3.
- Added README.ALT.

* Thu Jun 02 2005 LAKostis <lakostis at altlinux.org> 1:2.2.3-alt0.4
- s,alt,deb, in sasl_config patch as more correct.
- Define SASL vars in all build stages.
- Build with TLS and SASL by default.

* Sun May 29 2005 LAKostis <lakostis at altlinux.org> 1:2.2.3-alt0.3
- Updated to 2.2.3.
- Merged debian patches (for man pages and /etc/postfix/sasl/smtpd.conf).
- Updated alt patches.
- Build with new postgresql.
- 0.1 and 0.2 - internal releases.

* Wed May 11 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.1.6-alt1
- Updated to 2.1.6.

* Thu Apr 21 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.1.5-alt3
- Build fix: updated %name-lorder.sh to use join(1) in more portable way.

* Thu Mar 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.1.5-alt2
- Reverted change to default queue_minfree value
  which was introduced in 2.1.5-alt1.
- Fixed postfix-tls (closes #6214).
- Enabled ipv6 for postfix-tls by default (closes #6216).

* Fri Feb 25 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.1.5-alt1
- Cleaned up shlib model.
- Reviewed and rediffed patches.
- Disabled oqmgr packaging.
- Relocated documentation.
- Merged -readme subpackage back to main package.
- Updated TLS patch to deb-2.1.5-8.
- Changed daemon suffixes.
- Disabled %%verify check for files which are ususally changed after
  package installation, and for directory controlled via control(8) facility.
- Marked rare %%ghost files with %%config(missingok) attribute.
- Documented ALT-specific changes of defaults:
  default_privs = postman (introduced in 2.0.16-alt1);
  disable_vrfy_command = yes (introduced in 2.0.16-alt1);
  mynetworks_style = host (introduced in 2.0.16-alt1);
  mailbox_unpriv_delivery = yes (introduced in 2.0.16-alt3);
  virtual_minimum_uid = 500 (introduced in 2.0.16-alt3).
- Changed packager tag to reflect reality.

* Wed Feb 23 2005 LAKostis <lakostis at altlinux.ru> 1:2.1.5-alt0.5
- handle post/preun for -tls more correctly.
- remove bogus obsoletes tags.

* Tue Feb 22 2005 LAKostis <lakostis at altlinux.ru> 1:2.1.5-alt0.4
- relocate -virgin back to main postfix.
- disable ipv6 support.

* Mon Feb 21 2005 LAKostis <lakostis at altlinux.ru> 1:2.1.5-alt0.3
- rebuild with libdb4.3.
- check for proper dist-upgrade.
- TODO:
  - IPV6 patch update or IPV6 removal? :)

* Sat Jan 22 2005 LAKostis <lakostis at altlinux.ru> 1:2.1.5-alt0.2
- Move SASL2 and TLS to separate package (tnx to debian and ns@ for idea).
- Make postfix-virgin package with old functionality.
- Use tls+ipv6 patch from debian.
- TODO:
  + html-docs
  ? make cdb default

* Sat Jan 15 2005 LAKostis <lakostis at altlinux.ru> 1:2.1.5-alt0.1
- 2.1.5.
- update patches & spec.
- remove obsolete patches.

* Thu Oct 28 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.20-alt2
- init.d/postfix(reload): check postfix configuration.

* Fri Apr 23 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.20-alt1
- Updated to 2.0.20.

* Mon Apr 19 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.19-alt3
- dict_cdb: updated to libcdb.so.1.
- postfix.chroot.conf: fixed tab spaces handling.

* Mon Apr 19 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.19-alt2
- Changed shlib model to reduce shlib dependencies.  It should
  fix potential upgrade problems caused by shlib soname changes.
- chroot.d/postfix.conf: honor --verbose option.

* Tue Mar 16 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.19-alt1
- Updated to 2.0.19.

* Tue Mar 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.18-alt4
- postfix.chroot.conf: fail when postconf(1) fails (#3789).
- regexp_table(5): fixed regex syntax reference (#3766).

* Mon Feb 16 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.18-alt3
- Updated for chrooted-0.3.
- Rebuilt with libdb-4.2.so.

* Wed Feb 11 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.18-alt2
- postconf: show virtual_maps legacy parameter.
- main.cf.default: fixed (was empty).
- postfix.chroot.conf: implemented smart aliases and maps update.

* Fri Jan 23 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.18-alt1
- Updated to 2.0.18.

* Wed Jan 21 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.17-alt1
- Updated to 2.0.17.
- Fixed %%pre script to avoid unwanted postfix start on upgrade.

* Sat Nov 08 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.16-alt5
- Ensure that all shared libraries are built with %%optflags_shared.

* Sat Nov 01 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.16-alt4
- Fixed dynamic map loading support (broken in -alt3).

* Thu Oct 30 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.16-alt3
- Documented cdb hashing method everywhere.
- Implemented change to local(8) service and unix:passwd.byname map,
  to skip system users by default.
  Tunable by local_minimum_uid parameter, default is 500.
- Implemented change to local(8) deliver_mailbox_file to perform
  all operations as recipient user by default.
  Tunable by mailbox_unpriv_delivery parameter, default is true.
- Changed hardcoded default for virtual_minimum_uid parameter,
  from 100 to 500.
- Relocated shared library.
- Enable manpage regeneration.

* Wed Oct 29 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.16-alt2
- Provide smoother migration from %name-smtpd.
- Fixed build without optional modules (reported by Anton V. Denisov).

* Sun Oct 19 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.16-alt1
- Updated to 2.0.16.
- Dropped update-alternatives support for %_sysconfdir/aliases.
- Updated startup script.
- Updated patches:
  owl-sparse-hack, alt-install, alt-main.cf.
- New patches:
  ns-mx-acl-patch (unofficial from upstream),
  pg.postfix-2.0.0.2 (pgsql support),
  mjt-sharedlib-cmdmaxtime, pld-doc-cdb, deb-alt-doc, deb-ldap,
  alt-check, alt-defaults, alt-filelist, alt-post-install, alt-dynamicmaps.
- Removed patches:
  alt-script (obsoleted by alt-install)
  alt-def_mailbox_lock (obsoleted by alt-defaults)
- Hardcoded most essential changes in config defaults:
  alias_database = hash:/etc/postfix/aliases
  alias_maps = hash:/etc/postfix/aliases
  daemon_directory = /usr/lib/postfix
  default_privs = postman
  disable_vrfy_command = yes
  mailbox_delivery_lock = fcntl
  mynetworks_style = host
- Build postfix shared library.
- Added CDB support.
  See http://www.corpit.ru/mjt/tinycdb.html for details.
- Enabled ldap support (in -ldap subpackage).
- Enabled mysql support (in -mysql subpackage).
- Enabled pcre support (in -pcre subpackage).
- Added pgsql support (in -pgsql subpackage).
- Implemented dynamic map loading support.
- Implemented control(8) support for postfix server and postqueue.
- Dropped smtpd subpackage.
- Disabled nis:mail.aliases lookup by default.
- Disabled sasl support for a while.

* Mon Jul 28 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.13-alt1
- Updated to 1.1.13 (bugfix release).
- Updated start/stop script to new rc scheme.
- Updated build dependencies.

* Wed Jan 29 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.12-alt2
- Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature (#0002062).

* Mon Nov 25 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.12-alt1
- 1.1.12 release.
- chrooted.d/postfix.conf:
  + purge all chroot jail configs in force mode;
  + be more verbose on errors.
- chrooted.d/postfix.lib:
  + purge all chroot jail libs in force mode;
  + don't put unneeded libraries into chroot jail.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.11-alt2
- Use subst instead of perl for build and %%post* scripts.

* Thu May 30 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.11-alt1
- 1.1.11 release.

* Tue May 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.10-alt2
- Fixed typo in startup script made in previous release.

* Mon May 20 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.10-alt1
- 1.1.10 release.
- Moved /usr/share/postfix/* to sendmail-common package.

* Sat May 18 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.9-alt2
- Smtp/inet service now turned off by default unless postfix-smtpd is installed.
- Added SASL support for lmtp/unix, smtp/unix and smtp/inet services:
  it is turned off by default unless corresponding -sasl subpackages are installed.
- Startup script: added "condreload" option.

* Tue May 14 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.9-alt1
- 1.1.9 release.

* Tue May 07 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.1.8-alt1
- 1.1.8 release.
- Set default mailbox_lock style to "fcntl".

* Tue Apr 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.1.7-alt2
- Updated chroot (added NIS/NIS+ support).

* Mon Apr 01 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.1.7-alt1
- 1.1.7 release.
- Updated --with/--without specfile logic.

* Wed Mar 27 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.1.6-alt1
- 1.1.6 release.

* Mon Mar 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.1.5-alt2
- Updated --with/--without specfile logic.
- Build with libdb4.

* Fri Mar 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.1.5-alt1
- 1.1.5 release.

* Mon Feb 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.1.3-alt1
- 1.1.3 release.

* Mon Jan 28 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.1.2-alt1
- 1.1.2 release.

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.1.1-alt1
- 1.1.1 release.

* Sun Jan 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020112-alt1
- 20020112.

* Sun Jan 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020110-alt1
- 20020110.
- Changed postdrop command sgid named to postdrop.
- Changed local delivery agent default_privs to postman.
- Updated description (owl).
- Added %_sysconfdir/%name/{pcre,regexp}_table files.
- Rewritten %%install script.

* Fri Jan 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 20011226-alt2
- Updated make_aliases script to work with tcb.

* Fri Dec 28 2001 Dmitry V. Levin <ldv@alt-linux.org> 20011226-alt1
- 20011226 (safety, see RELEASE_NOTES and HISTORY files).

* Wed Dec 19 2001 Dmitry V. Levin <ldv@alt-linux.org> 20011217-alt1
- 20011217 (security, see RELEASE_NOTES and HISTORY files).

* Thu Nov 29 2001 Dmitry V. Levin <ldv@alt-linux.org> 20011127-alt1
- 20011127:
  + New parameter smtpd_noop_commands;
  + New header/body_check.

* Tue Nov 27 2001 Dmitry V. Levin <ldv@alt-linux.org> 20011125-alt1
- 20011125:
  + New parameter smtpd_sender_login_maps;
  + New sender anti-spoofing restriction reject_sender_login_mismatch.

* Thu Nov 22 2001 Dmitry V. Levin <ldv@alt-linux.org> 20011121-alt1
- 20011121.

* Mon Nov 19 2001 Dmitry V. Levin <ldv@alt-linux.org> 20011115-alt2
- Correct build with new pcre.

* Fri Nov 16 2001 Dmitry V. Levin <ldv@alt-linux.org> 20011115-alt1
- 20011115 (session log memory exhaustion bugfix).

* Tue Oct 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 20011008-alt1
- 20011008.

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010808-alt2
- Fixed %%post script: do not chkconfig if upgrading.

* Sun Sep 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010808-alt1
- 20010808.
- Build with ldap support.

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010714-alt1
- 20010714.

* Wed Jul 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010709-alt1
- 20010709.

* Mon Jun 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010610-alt1
- 20010610.

* Thu Jun 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010525-alt3
- Fixed directory permissions in %ROOT (was undefined before).

* Mon Jun 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010525-alt2
- Fixed startup and check scripts.

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010525-alt1
- 20010525.

* Tue May 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010502-alt1
- 20010502.

* Mon Apr 02 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010329-alt1
- 20010329.

* Wed Mar 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010228-ipl3mdk
- Fixed %%triggerpostun script.

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 20010228-ipl2mdk
- Updated aliases template.

* Fri Mar 02 2001 Dmitry V. Levin <ldv@fandra.org> 20010228-ipl1mdk
- Snapshot 20010228.

* Mon Feb 26 2001 Dmitry V. Levin <ldv@fandra.org> 20010225-ipl1mdk
- Snapshot 20010225.
- Updated aliases template.

* Thu Feb 22 2001 Dmitry V. Levin <ldv@fandra.org> 19991231pl13-ipl6mdk
- Moved common sendmail links to sendmail-common package.
- Fixed Requires.

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 19991231pl13-ipl5mdk
- Fixed startup script (abort startup if failed to setup chroot).

* Fri Feb 02 2001 Dmitry V. Levin <ldv@fandra.org> 19991231pl13-ipl4mdk
- Rebuilt with db3-3.2.9.

* Wed Jan 31 2001 Dmitry V. Levin <ldv@fandra.org> 19991231pl13-ipl3mdk
- Added smtpd_size patch.
- Ported to new chrooted scheme.

* Sat Jan 06 2001 Dmitry V. Levin <ldv@fandra.org> 19991231pl13-ipl2mdk
- Rebuilt with db3-3.2.3e.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 19991231pl13-ipl1mdk
- Fixed %_datadir/%name/make_aliases script (installation problem).
- Fixed groupadd/useradd/chkconfig calls.

* Tue Dec 12 2000 Dmitry V. Levin <ldv@fandra.org>
- 19991231-pl13.
- Patched to work with LFS and pthread-aware db3.
- RE adaptions.
- FHSification.

* Fri Jun  2 2000 Dmitry V. Levin <ldv@fandra.org>
- 19991231-pl08

* Mon May 15 2000 Dmitry V. Levin <ldv@fandra.org>
- 19991231-pl07

* Tue Apr  4 2000 Dmitry V. Levin <ldv@fandra.org>
- 19991231-pl06

* Tue Mar 28 2000 Dmitry V. Levin <ldv@fandra.org>
- dependency fix with resolv.conf and chroot setup

* Mon Mar 13 2000 Dmitry V. Levin <ldv@fandra.org>
- 19991231-pl05

* Wed Mar 08 2000 Dmitry V. Levin <ldv@fandra.org>
- updated to rpm-3.0.4

* Thu Feb 10 2000 Dmitry V. Levin <ldv@fandra.org>
- 19991231-pl03

* Mon Jan  3 2000 Dmitry V. Levin <ldv@fandra.org>
- fixed chrooted libraries

* Sun Dec 26 1999 Dmitry V. Levin <ldv@fandra.org>
- 19990906-pl09
- fixed chrooted environment

* Wed Dec  1 1999 Dmitry V. Levin <ldv@fandra.org>
- 19990906-pl07
- fixed permissions

* Wed Sep  7 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Sat Jun  5 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- install bins from libexec/

* Sat Jun  5 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 19990601
- .spec cleanup for easier updates

* Wed May 26 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- created link from /usr/sbin/sendmail to /usr/lib/sendmail
  so it doesn't bug out when i rpm -e sendmail
- Now removes /var/lock/subsys/postfix like a good little prog
  upon rpm -e

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adptations.

* Tue Apr 13 1999 Arne Coucheron <arneco@online.no>
  [19990317-pl04-1]

* Tue Mar 30 1999 Arne Coucheron <arneco@online.no>
  [19990317-pl03-2]
- Castro, Castro, pay attention my friend. You're making it very hard
  maintaining the package if you don't follow the flow of the releases

* Thu Mar 25 1999 Arne Coucheron <arneco@online.no>
  [19990317-pl02-1]

* Tue Mar 23 1999 Arne Coucheron <arneco@online.no>
  [19990317-3]
- added bugfix patch01

* Sat Mar 20 1999 Arne Coucheron <arneco@online.no>
  [19990317-2]
- removed the mynetworks line in main.cf, let postfix figure it out
- striping of the files in /usr/sbin
- alias database moved to /etc/postfix and made a symlink to it in /etc
- enabled procmail support in main.cf and added it to Requires:
- check status on master instead of postfix in the init script
- obsoletes postfix-beta
- had to move some of my latest changelog entries up here since Edgard Castro
  didn't follow my releases

* Thu Mar 18 1999 Edgard Castro <castro@usmatrix.net>
  [19990317]

* Tue Mar 16 1999 Edgard Castro <castro@usmatrix.net>
  [alpha-19990315]

* Tue Mar  9 1999 Edgard Castro <castro@usmatrix.net>
  [19990122-pl01-2]
- shell and gecho information changed to complie with Red Hat stardand
- changed the name of the rpm package to postfix, instead of postfix-beta

* Tue Feb 16 1999 Edgard Castro <castro@usmatrix.net>
  [19990122-pl01-1]

* Sun Jan 24 1999 Arne Coucheron <arneco@online.no>
  [19990122-1]
- shell for postfix user changed to /bin/true to avoid logins to the account
- files in /usr/libexec/postfix moved to /usr/lib/postfix since this complies
  more with the Red Hat standard

* Wed Jan 06 1999 Arne Coucheron <arneco@online.no>
  [19981230-2]
- added URL for the source
- added a cron job for daily check of errors
- sample config files moved from /etc/postfix/sample to the docdir
- dropped making of symlinks in /usr/sbin and instead installing the real
  files there
- because of the previous they're not needed anymore in /usr/libexec/postfix,
  so they are removed from that place

* Fri Jan 01 1999 Arne Coucheron <arneco@online.no>
  [19981230-1]

* Tue Dec 29 1998 Arne Coucheron <arneco@online.no>
  [19981222-1]
- first build of rpm version
