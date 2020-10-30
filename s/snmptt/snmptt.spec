%filter_from_requires /perl.DB[DI]/d
%filter_from_requires /perl.SNMP.pm/d

Name: snmptt
Version: 1.4.2
Release: alt1
Summary: An SNMP trap handler written in Perl

Group: System/Servers
License: GPLv2+
Url: http://www.snmptt.org/

Source0: http://downloads.sourceforge.net/snmptt/%{name}-%{version}.tar

#TODO: Upstream
Source1: %name.service
Source2: %name.init

BuildArch: noarch

BuildRequires: perl-Text-Balanced perl-Config-IniFiles

# Needed for precreated users/group "snmp":
Requires: net-snmp-common

%description
SNMPTT (SNMP Trap Translator) is an SNMP trap handler written in Perl
for use with the Net-SNMP / UCD-SNMP snmptrapd program.  It can be
used to translate trap output from snmptrapd to more descriptive and
human friendly form, supports logging, invoking external programs, and
has the ability to accept or reject traps based on a number of
parameters.

%package mysql
Summary: MySQL support for %name
Group: System/Servers
Requires: perl(DBD/mysql.pm)
Requires: %name = %EVR

%description mysql
MySQL support for %name

(virtual package)

%package postgresql
Summary: PostgreSQL support for %name
Group: System/Servers
Requires: perl(DBD/Pg.pm)
Requires: %name = %EVR

%description postgresql
PostgreSQL support for %name

(virtual package)

%package odbc
Summary: ODBC support for %name
Group: System/Servers
Requires: perl(DBD/ODBC.pm)
Requires: %name = %EVR

%description odbc
ODBC support for %name

(virtual package)

%package net-snmp
Summary: NET-SNMP support for %name
Group: System/Servers
Requires: perl(SNMP.pm)
Requires: %name = %EVR

%description net-snmp
NET-SNMP support for %name

(virtual package)

%prep
%setup

mv sample-*trap* examples/
mv examples/snmptt.conf.generic snmptt.conf

# convert ChangeLog to UTF-8
iconv -f ISO-8859-1 -t UTF-8 ChangeLog > ChangeLog.utf8 && \
touch -r ChangeLog ChangeLog.utf8 && \
mv -f ChangeLog{.utf8,}

sed -i -e 's/NETSNMPTRAPD_HANDLER_OK/1/g' snmptthandler-embedded

%build
%install
install -D -p -m 0755 snmptt %buildroot%_sbindir/snmptt
install -D -p -m 0755 snmptthandler %buildroot%_sbindir/snmptthandler
install -D -p -m 0644 snmptthandler-embedded %buildroot%_datadir/snmptt/snmptthandler-embedded
install -D -p -m 0755 snmpttconvert %buildroot%_bindir/snmpttconvert
install -D -p -m 0755 snmpttconvertmib %buildroot%_bindir/snmpttconvertmib
install -D -p -m 0644 snmptt.conf %buildroot%_sysconfdir/snmp/snmptt.conf
install -D -p -m 0644 snmptt.ini %buildroot%_sysconfdir/snmp/snmptt.ini
install -D -p -m 0644 -p %SOURCE1 %buildroot%_unitdir/%name.service
install -D -p -m 0755 -p %SOURCE2 %buildroot%_initdir/snmptt
install -D -p -m 0644 snmptt.logrotate %buildroot%_logrotatedir/snmptt
install -d %buildroot%_var/spool/snmptt
install -d %buildroot%_logdir/snmptt

%pre
/usr/sbin/groupadd -r -f snmptt ||:
/usr/sbin/useradd -r -g snmptt -d %_var/spool/snmptt -s /sbin/nologin -n -c "SNMP Trap Translate" snmptt ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name
%config(noreplace) %_sysconfdir/snmp/%name.conf
%config(noreplace) %_sysconfdir/snmp/%name.ini
%config(noreplace) %_logrotatedir/%name
%_bindir/snmpttconvert
%_bindir/snmpttconvertmib
%_sbindir/%name
%_sbindir/snmptthandler
%_datadir/%name
%_unitdir/%name.service
%attr(775,%name,snmp) %dir %_var/spool/%name/
%attr(1770,root,%name) %dir %_logdir/%name/

%doc ChangeLog COPYING README
%doc contrib/ docs/ examples/

%files mysql
%files postgresql
%files odbc
%files net-snmp

%changelog
* Tue Oct 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.2-alt1
- Updated to upstream version 1.4.2 (Fixes: CVE-2020-24361).

* Fri Jan 29 2016 Terechkov Evgenii <evg@altlinux.org> 1.4-alt5
- Fix service stopping with systemd

* Mon Jan 18 2016 Terechkov Evgenii <evg@altlinux.org> 1.4-alt4
- Rebuild for work with net-snmp-5.7.3 and up

* Wed Jan  6 2016 Terechkov Evgenii <evg@altlinux.org> 1.4-alt3
- Change mode/owner of /var/log/snmptt to 1770/root:snmptt according to ALT Secure Packaging Policy

* Wed Apr  8 2015 Evgenii Terechkov <evg@altlinux.org> 1.4-alt2
- Change /var/spool/snmptt/ ownership to snmptt:root to work with buggy snmptrapd (ALT #30926)
- Missed Requires: added to subpackages
- Fix initscript's condrestart

* Thu Apr  2 2015 Terechkov Evgenii <evg@altlinux.org> 1.4-alt1
- Initial build for ALT Linux Sisyphus
