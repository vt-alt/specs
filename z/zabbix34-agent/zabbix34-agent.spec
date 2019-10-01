%define zabbix_user	zabbix
%define zabbix_group	zabbix
%define zabbix_home	/dev/null
%define svnrev		86739

%def_with ssh2

%def_enable ipv6

%ifndef _unitdir
%define _unitdir %systemd_unitdir
%endif

Name: zabbix34-agent
Version: 3.4.15
Release: alt2

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv2
Group: Monitoring

Url: http://www.zabbix.com

Summary: %name
Group: Monitoring
Requires: %name-common
Conflicts: zabbix-agent


# http://heanet.dl.sourceforge.net/sourceforge/zabbix/zabbix-%version.tar.gz
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildPreReq: libelf-devel

# Automatically added by buildreq on Thu Nov 15 2018 (-bi)
# optimized out: elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libsasl2-3 perl pkg-config python-base python3 python3-base rpm-build-python3 sh3 xz
BuildRequires: libcurl-devel libelf-devel libldap-devel libpcre-devel libpython3 libssl-devel

BuildRequires: perl-Switch /proc

%package common
Summary: %name network monitor (common stuff)
Group: Monitoring
Provides: %_sysconfdir/zabbix
Provides: %_logdir/zabbix
BuildArch: noarch
Conflicts: zabbix-common

%package sudo
Summary: sudo entry for %name
Group: Monitoring
BuildArch: noarch
Requires: %name
Conflicts: zabbix-agent-sudo


%description
zabbix 3.4 network monitor agent.

ZABBIX is software for monitoring of your applications, network and servers.
ZABBIX supports both polling and trapping techniques to collect data from
monitored hosts. A flexible notification mechanism allows easy and quickly
configure different types of notifications for pre-defined events.

%description common
Common files and docs for zabbix network monitor

ZABBIX is software for monitoring of your applications, network and servers.
ZABBIX supports both polling and trapping techniques to collect data from
monitored hosts. A flexible notification mechanism allows easy and quickly
configure different types of notifications for pre-defined events.

%description sudo
Sudo entry for zabbix34-agent.

%prep
%setup
%patch0 -p1

%build
# fix ZABBIX_REVISION
sed -i -e "s,{ZABBIX_REVISION},%svnrev," include/version.h src/zabbix_java/src/com/zabbix/gateway/GeneralInformation.java

%autoreconf

%configure --with-sqlite3 \
	%{subst_enable ipv6} \
	--enable-agent \
	%{subst_enable java} \
	--with-libcurl \
	--with-libxml2 \
	--with-net-snmp \
	--with-ldap \
	--with-jabber \
	--with-openipmi \
	--with-openssl \
	%{subst_with ssh2} \
	%{subst_with unixodbc} \
	--with-libpcre-include=/usr/include/pcre \
	--sysconfdir=/etc/zabbix
%make

# adjust in several files /home/zabbix
find conf -type f -print0 | xargs -0 sed -i \
	-e "s,/home/zabbix/bin,/usr/sbin,g" \
	-e "s,PidFile=/tmp,PidFile=%_var/run/zabbix,g" \
	-e "s,LogFile=/tmp,LogFile=%_logdir/zabbix,g" \
	-e "s,/home/zabbix/lock,%_var/lock/subsys/zabbix,g" \
	-e "s,/tmp/mysql.sock,%_localstatedir/mysql/mysql.sock,g" \
	-e "s,Include=/usr/local/etc/zabbix_agentd.conf.d/,Include=%_sysconfdir/zabbix/zabbix_agentd.conf.d/,g" --

%install

%makeinstall

# create directory structure
install -dm1775 %buildroot%_logdir/zabbix
install -dm0755 %buildroot%_sbindir
install -dm0750 %buildroot%_sysconfdir/zabbix
install -dm0750 %buildroot%_sysconfdir/zabbix/zabbix_agentd.conf.d
install -dm0755 %buildroot%_unitdir

# binaries
install -m0755 src/zabbix_*/zabbix_agentd %buildroot%_sbindir

# conf files
install -m0640 conf/zabbix_agentd.conf %buildroot%_sysconfdir/zabbix
install -Dpm 644 sources/zabbix-tmpfiles.conf %buildroot/lib/tmpfiles.d/zabbix.conf

# start scripts
install -pDm0755 sources/zabbix_agentd.init %buildroot%_initdir/zabbix_agentd
install -pDm0644 sources/zabbix_agentd.service %buildroot%_unitdir/zabbix_agentd.service

# sudo entry
install -pDm0400 sources/zabbix.sudo %buildroot%_sysconfdir/sudoers.d/zabbix

# ChangeLog
bzip2 ChangeLog

%pre common
/usr/sbin/groupadd -r -f %zabbix_group ||:
/usr/sbin/useradd -g %zabbix_group -G proc -c 'Zabbix' \
	-d %zabbix_home -s /dev/null -r %zabbix_user >/dev/null 2>&1 ||:

%post
%post_service zabbix_agentd
if [ $1 -eq 1 ]; then
	sed -i -e "s,Hostname=Zabbix server,Hostname=$HOSTNAME,g" \
	%_sysconfdir/zabbix/zabbix_agentd.conf
fi

%post sudo
if [ $1 -eq 1 ]; then
	gpasswd -a %zabbix_user wheel
fi

%preun
%preun_service zabbix_agentd

%files common
%dir %attr(1775,root,%zabbix_group) %_logdir/zabbix
%dir %_sysconfdir/zabbix
/lib/tmpfiles.d/*

%files
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/zabbix/zabbix_agentd.conf
%dir %attr(0750,root,%zabbix_group) %_sysconfdir/zabbix/zabbix_agentd.conf.d
%_initdir/zabbix_agentd
%_unitdir/*agent*
%_sbindir/zabbix_agentd
%_bindir/zabbix_sender
%_man8dir/zabbix_agentd.*
%_man1dir/zabbix_sender.*

%files sudo
%config(noreplace) %attr(0400,root,root) %_sysconfdir/sudoers.d/zabbix

%changelog
* Thu Sep 26 2019 Alexei Takaseev <taf@altlinux.org> 3.4.15-alt2
- Add BR /proc (ALT #37264)

* Thu Nov 15 2018 Alexei Takaseev <taf@altlinux.org> 3.4.15-alt1
- Initial build for Sisyphus.
