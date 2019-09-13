##########################################################################
# Package Definitions #
##########################################################################
# SELinux support
%def_disable			selinux

# Use /dev/shm as client's tmp directory
%def_enable			clientshmtmp

# Use alternate exec shell
%def_disable			altshell
%{?_enable_altshell:%global	shell	/bin/dash}

# Compile xymon-client with dietlibc ?
%def_disable			dietlibc

# Build trunk version
%def_disable			trunk

# Experimental native snmp support
%def_disable			snmp

# Build orcamon and reduced-functionality client RPMs
%def_disable			extraclients

##########################################################################
##########################################################################
%define _libexecdir %_prefix/libexec

%define serverName	xymon
%define clientName	xymon-client
%define xymonRoot	%{_datadir}/xymon
%define xymonServerRoot	%{_datadir}/%{serverName}
%define xymonClientRoot	%{_datadir}/%{clientName}

# Common directories used on both servers and clients
%define	logDirectory	%{_var}/log/%{name}
%define runDirectory	%{_var}/run/%{name}
%define localClientDirectory %{_prefix}/local/share/%{clientName}

# long-term data for the server, generated html, and templates
%define libDirectory	%{_var}/lib/%{name}
%define wwwDirectory	%{_var}/www/%{name}
%define wwwCacheDirectory	%{_var}/cache/%{serverName}
%define wwwStaticDirectory	%{xymonServerRoot}/static
%define webDirectory	%{_sysconfdir}/%{serverName}/web

# temp directories. if clientshmtmp is specified, the client
# tries to use /dev/shm instead
%define tmpDirectorySrv	%{_var}/lib/%{name}/tmp
%define tmpDirectoryCli	/dev/shm

##########################################################################
# Headers #
##########################################################################

Name:		xymon
Summary:	A system for monitoring servers and networks
Group:		Monitoring
License:	%gpl2only
URL:		http://xymon.sourceforge.net/

%if_disabled trunk
Version:	4.3.29
Release:	alt1
Source0:	http://prdownloads.sourceforge.net/xymon/Xymon/%{version}/%{name}-%{version}.tar.gz
%else
%define		trunkVersion	%(svn info ~/svn/xymon/trunk/ | grep ^Revision | awk '{print $2}')
Version:	0.%{trunkVersion}
Release:	alt1_alt1_1.1
Source0:	xymon-trunk-%{trunkVersion}.tgz
%endif


# Updated init scripts
Source1:	xymon.server-init
Source2:	xymon.client-init
Source3:	xymon.README.terabithia
Source4:	xymon430.README.core
Source5:	xymon-server.sysconfig
Source6:	xymon-client.sysconfig

# xymonlaunch task files for periodic report generation
Source31:	xymonreports.daily.task
Source32:	xymonreports.weekly.task
Source33:	xymonreports.monthly.task
Source34:	xymongen.task

# SELinux policy sources
Source41:	xymon.te
Source42:	xymon-client.te

Source21:	xymon.sections.mounts

Requires:	xymon-common = %{version}-%{release}

BuildRequires:	rpm-build-licenses

BuildRequires:	libssl-devel pcre-devel rrdtool-devel openldap-devel
%if_enabled trunk
BuildRequires:	libsqlite3-devel >= 3 zlib-devel
%if_enabled dietlibc
BuildRequires:	zlib-devel-static
#BuildRequires:	openssl-static
%endif # dietlibc
%endif # trunk

%add_findreq_skiplist */share/xymon/server/*
%add_findreq_skiplist *xymon/critical.cfg*

Provides:	xymon-client = %{version}-%{release} xymon-client-passive = %{version}-%{release} xymon-client-core = %{version}-%{release}

%if_enabled selinux
# Very ugly, but the preferred hack from http://fedoraproject.org/wiki/SELinux_Policy_Modules_Packaging_Draft
%global		selinux_policyver %(%{__sed} -e 's,.*selinux-policy-\\([^/]*\\)/.*,\\1,' /usr/share/selinux/devel/policyhelp || echo 0.0.0)
%global		selinux_variants mls targeted
BuildRequires:	checkpolicy selinux-policy-devel /usr/share/selinux/devel/policyhelp
Requires:	selinux-policy >= %{selinux_policyver}
Requires(post):		/usr/sbin/semodule /usr/sbin/semanage /sbin/restorecon
Requires(postun):	/usr/sbin/semodule /usr/sbin/semanage
%endif # selinux

# since 4.3.29
BuildRequires: libcares-devel libtirpc-devel

#%{?_disable_trunk:Requires:	ntpdate ntp-utils}
%{?_enable_altshell:Requires:	%shell}
%{?_enable_snmp:BuildRequires:	libnet-snmp-devel}
%{?_enable_dietlibc:BuildRequires:	/usr/bin/diet}

#################
# Patches	#
#################

# move static www files from HOME/www to HOME/static
Patch1: xymon_4317.installstaticwww.patch

# specify location of help files instead of assuming
Patch2: xymon.helpdir.patch

# create missing www/rep www/snap www/html www/notes directories if needed
# (for tmps wwwdir)
Patch45: xymon.mkdir.patch

# Move /periodic (xymonreports output) and /notes from the web tree
# to /var/lib/xymon/
Patch46: xymon.varlibwww.patch

# move pid files to rundir
# see: https://sourceforge.net/tracker/?func=detail&aid=3170854&group_id=128058&atid=710490
Patch303: xymon_trunk.rundir.patch
Patch3: xymon.rundir.patch

# add a "sections" directory, for scripts whose output will automatically be included in the Xymon client data
# based on trunk: http://xymon.svn.sourceforge.net/viewvc/xymon?view=revision&sortby=rev&sortdir=down&revision=6800
# but w/o "local:" header
Patch4: xymon.sections.patch

# insert /etc/xymon/*.d/ references in config files
Patch5: xymon.breakout-directories.patch

# include init scripts in the regexes performed during 'make'
Patch6: xymon437.initdvars.patch

# remove auto-updating of scripts and binaries from xymonclient.sh
# since there's no good way to make this work on an RPM system
Patch8: xymon.noclientupdate.patch


# We don't package anything in /usr/local, but check there for
# local xymon-client script add-ins
Patch13: xymon.usrlocallocaldir.patch

# don't sleep after running xymonclient
Patch15: xymon.nosleep.patch

# create xymonlaunch var in sysconfig
Patch16: xymon437.launchopts.patch

# xymond not following {net,disp}include lines properly
# see https://sourceforge.net/mailarchive/message.php?msg_id=28657398
Patch18: xymon.nullfollowsincl.patch


# XYMONCLIENTHOME was not being set on clients running xymoncmd
# see: https://sourceforge.net/tracker/?func=detail&aid=3170916&group_id=128058&atid=710490
Patch36: xymon.xymonclienthome.patch


# use environment variables if no args given to xymon client
Patch41: xymon.xymonmsg.patch

# prevent refresh loop when loading "trends" page when locator is enabled
Patch44: xymon.trendsloop.patch

# Try harder to send a xymon message when segfaulting
Patch48: xymon.sigbetter.patch

# Silence an rpmlint warning about packaging an empty file
Patch49: xymon.confreport_back.patch


# point apache-writable /rep and /snap to /var/cache/xymon
Patch51: xymon.wwwcachedir.patch


# respect /etc/sysconfig/xymon-client as source of truth for 
# destination of local client reports (even on servers)
Patch52: xymon.alwaysmultiservers.patch
Patch53: xymon.usesysconfig.patch
Patch54: xymon.serverclient.patch


# config files can also use "source" and ". " as aliases for include
# this allows us to pre-stage some configs with shell interpreters instead
# of after the fact (preparing for systemd unit files)
Patch59: xymon.shellinclude.patch


# fork the vmstat collector on clients by piping to a shell instead
# of putting it all on a single command line
Patch103: xymon.pipevmstatfork.patch


# Search /usr for libs too
Patch203: xymon.usrlibs.patch

# BACKPORTED TO CURRENT RELEASE ONLY


# DIFFERING VERSIONS ONLY
# allow custom http headers to be specified for http tests for a given host
Patch326: xymon_trunk.httpheaders.patch

# TRUNK ONLY
# use distribution fping instead of building included one
Patch401: xymon_trunk.nofping.patch

# add zliblibs
Patch402: xymon_trunk.zlibfix.patch

# wrap ssl in HAVE_OPENSSL
Patch403: xymon_trunk.nossl.patch

# typo
Patch404: xymon_trunk.ackinfo.patch

# let trunk build with <= 3.3.6 sqlite, eg RHEL 5
Patch405: xymon_trunk.old_sqlite.patch


# configure.client more like configure.server
Patch406: xymon_trunk.configureclient.patch
Source44: import.info

# removed not needed version's check
Patch500: xymonclient-linux.sh-altlinux.patch

# removed xymongen task from tasks.cfg
Patch501: xymongen.tasks.cfg.DIST.patch

# added control for using "ifconfig" and "netstat -rn" in xymonclient-linux.sh
Patch502: xymonclient-linux.sh-ifconfig-route.patch

# configurable top and ps (allow to use vzprocps)
Patch503: xymonclient-linux.sh-various-procps.patch

# rollback of changes for cgiwrap introduced in 4.3.20
Patch504: xymon-4.3.21-FollowSymLinks.patch

##########################################################################
##########################################################################

%description
Xymon monitors your hosts, your network services, and anything else you
configure it to do via extensions. Xymon will periodically generate
requests to network services - HTTP, FTP, SMTP and so on - and record if
the service is responding as expected. Through the use of agents
installed on the servers (the xymon-client package), you can also
monitor local disk utilization, log files and processes.

Xymon is the successor to the BBGEN toolkit, which has been available as
an add-on to Big Brother since late 2002. It was also previously known
as Hobbit. If you have used BBGEN before, Xymon will seem quite
familiar.

You should install this package if you want this machine to monitor 
services running on other machines.


###########################################################################
%package common
Summary:	Common files for Xymon server and Xymon client
Group:		File tools

%description common
Common files for Xymon server and Xymon client

%package web
Summary: web-server part of Xymon server
Group: Networking/WWW
Requires: %name = %version-%release, webserver-common

%description web
web-server part of Xymon server

%package apache2
Summary: Apache 2.x web-server configuration for Xymon server
Group: Networking/WWW
Requires: %name-web = %version-%release, apache2
BuildArch: noarch

%description apache2
Apache 2.x web-server configuration for Xymon server

%package man
Summary: Xymon man pages
Group: Development/Documentation
BuildArch: noarch

%description man
Xymon man pages

%package client
Summary:	The reporting client service for the Xymon monitoring system
Group:		Monitoring
BuildArch:	noarch
Conflicts:	xymon
Provides:	xymon-client-core = %{version}-%{release} xymon-client-passive = %{version}-%{release}
Requires:	xymon-common = %{version}-%{release}
%if_enabled selinux
Requires:		selinux-policy >= %{selinux_policyver}
Requires(post):		/usr/sbin/semodule
Requires(postun):	/usr/sbin/semodule
%endif # selinux
%{?_enable_altshell:Requires:	%shell}

%description client
This package contains a client/agent for the Xymon monitor. Clients
report data about the local system to the monitor, allowing it to check
on the status of the system load, file system utilization, processes that
must be running, and so forth.

This package does not need to be installed on a system that is 
already running as a Xymon server (indeed, it conflicts with it).
The Xymon server already contains the files necessary to run its
built-in monitor.

%package bb-compatibility
Summary:	Some Big Brother compatibility symlinks for Xymon
Group:		Monitoring
Requires:	xymon-common
BuildArch:	noarch
Conflicts:	bb

%description bb-compatibility
Some Big Brother compatibility symlinks for Xymon. The package contains
/usr/bin/bb and /usr/bin/bbcmd. All other symlinks placed to /usr/lib/xymon
or /usr/lib/xymon-client and it is not interfere with other packages.

/usr/bin/bb has conflict with BB - the portable AAlib demo

###########################################################################
%if_enabled extraclients
%package client-passive
Summary:	Run-time utilities and a client for the Xymon monitoring system
Group:		Monitoring
Conflicts:	xymon xymon-client
Provides:	xymon-client = %{version}-%{release} xymon-client-core = %{version}-%{release}
%if_enabled selinux
Requires:		selinux-policy >= %{selinux_policyver}
Requires(post):		/usr/sbin/semodule
Requires(postun):	/usr/sbin/semodule
%endif
%{?_enable_altshell:Requires:	%shell}

%description client-passive
This package contains run-time utilities and a manual client for
communicating with the Xymon monitor. It does not set up a user account
and does not contain init scripts for the client agent.

You should install this package if you want to retrieve data 
about a machine on a manual basis or automated outside the bailiwick 
of the xymonlaunch process.

Note that this software may leave temp files around that are owned
by whichever user last ran the client script. You should try to run
the client consistently by the same method.


%package client-core
Summary:	Utilities for communicating with the Xymon monitoring system
Group:		File tools

%description client-core
This package contains run-time utilities for communicating with the Xymon
monitor: the xymon and xymoncmd commands and associated configuration files.

It does not contain the local client daemon which regularly reports 
system status back. You should install xymon-client for that instead.

Install this package if you have scripts which may need to report back a
result, but you cannot or don't want to install the local xymon-client
daemon or scripts.  If you later decide to install the full client, you
can upgrade to either the active or passive client directly over this
one.


%package client-orca
Summary:	Orca collector client for the Xymon monitoring system
Group:		Monitoring

%description client-orca
orcaxymon is an add-on tool for the Xymon client. It is used to grab data 
collected by the ORCA data collection tool (orcallator.se), and send it to 
the Xymon server in NCV format. 

%endif # extraclients

%prep
%if_disabled trunk
%setup -q
%else
%setup -q -n trunk
%endif # trunk


%patch1 -b .installstaticwww
%patch2 -p1
%patch45 -p1
%patch46 -p1
%patch4 -b .sections
%patch5 -b .breakout
%patch6 -b .initdvars
%patch8 -b .noclientupdate


%patch13 -b .usrlocallocaldir
%patch15 -b .nosleep
%patch16 -b .launchopts
%patch18 -b .nullfollowsincl

%patch36 -b .clienthomecheck

%patch41 -b .xymonmsg
%patch44 -b .trendsloop
%patch48 -p1
# confreport_back.patch
%patch49

%patch51 -b .wwwcachedir
%patch52 -b .alwaysmultiservers
%patch53 -b .usesysconfig
%patch54 -b .serverclient
%patch59 -b .shellinclude

%patch103 -b .pipevmstatfork

%patch203 -b .usrlibs

%if_disabled trunk
%patch3 -p1
%else # trunk
%patch326 -b .httpheaders
%patch303 -b .rundir
%patch401 -b .nofping
%patch402 -b .zlibfix
%patch403 -b .nossl
%patch404 -b .ackinfo
%patch405 -b .old_sqlite
%patch406 -b .configureclient
%endif # trunk

%patch500 -p2
%patch501 -p0
%patch502 -p2
%patch503 -p1
%patch504 -p1

sed "s/define MAXCHECK   102400/define MAXCHECK   4194303/" -i client/logfetch.c

%if_disabled trunk
  PROTOFILE="xymond/etcfiles/protocols.cfg.DIST"
%else
  PROTOFILE="xymond/etcfiles/protocols2.cfg.DIST"
%endif
  echo "
# include additional sections
directory @XYMONHOME@/etc/protocols.d" >> $PROTOFILE


# fix perms on patch4
  chmod 644 client/README-sections*

# Ensure that any utf8 data perl scans will read OK on RH8
  export LANG=C


# Updated init scripts
  rm -f rpm/xymon-init.d rpm/xymon-client.init
  install -m 644 %{SOURCE1} rpm/xymon-init.d.DIST
  install -m 644 %{SOURCE2} rpm/xymon-client.init.DIST
  %{__perl} -p -e 's#PROGRAMS = xymon.sh#PROGRAMS = ../rpm/xymon-init.d ../rpm/xymon-client.init xymon.sh#' -i xymond/Makefile
  %{__perl} -p -e 's#PROGRAMS=xymonlaunch#PROGRAMS=../rpm/xymon-client.init xymonlaunch#' -i client/Makefile


%if_enabled selinux
  mkdir SELinux
  install -m 644 %{SOURCE41} SELinux/%{serverName}.te
  install -m 644 %{SOURCE42} SELinux/%{clientName}.te
  %{__perl} -p -e 's/VERSION/%{version}.%{release}/' -i SELinux/*.te
%endif # selinux



# Search and replace our shells?
%if_enabled altshell
# Init script launching
  %{__perl} -p -e 's#-s /bin/sh#-s %{shell}#' -i rpm/xymon-init.d* rpm/xymon-client.init*

# Generic forking
  %{__perl} -p -e 's#/bin/sh#%{shell}#' -i lib/misc.c

# Client-side (on Linux, for the client RPM) forking
  %{__perl} -p -e 's#nohup sh #nohup %{shell} #' -i ./client/xymonclient-linux.sh

# Script shebangs generally
  find -type f | grep -e .sh$ -e .sh.DIST$ | grep -v /build/ | \
	xargs -r %{__perl} -p -e 's|^#!/bin/sh|#!%{shell}|' -i
%endif # altshell


# Convert remaining configure-time tweaked paths to their fixed equivalents.
# eg, /usr/share/xymon/server/etc/tasks.cfg is now:
#     /etc/xymon/tasks.cfg

find -type f > tmp.flist
find xymond/ xymongen/ xymonnet/ xymonproxy/ rpm/xymon-init.d.DIST -type f > tmp.slist

xargs -r %{__perl} -p \
	-e 's#\@XYMONTOPDIR\@/server/bin#%{_libexecdir}/%{serverName}#g;'	\
	-e 's#\@XYMONTOPDIR\@/server/etc#%{_sysconfdir}/%{serverName}#g;'	\
	-e 's#\@XYMONTOPDIR\@/server/ext#%{_sysconfdir}/%{serverName}/ext#g;' \
	-e 's#\@XYMONTOPDIR\@/client/bin#%{_libexecdir}/%{clientName}#g;'	\
	-e 's#\@XYMONTOPDIR\@/client/etc#%{_sysconfdir}/%{clientName}#g;'	\
	-e 's#\@XYMONTOPDIR\@/client/ext#%{xymonClientRoot}/ext#g;'	\
	-e 's#\@XYMONTOPDIR\@/client"#%{xymonClientRoot}"#g;'		\
		-i < tmp.flist
xargs -r %{__perl} -p \
	-e 's#\@XYMONHOME\@/bin#%{_libexecdir}/%{serverName}#g;' \
	-e 's#\@XYMONHOME\@/etc#%{_sysconfdir}/%{serverName}#g;' \
	-e 's#\@XYMONHOME\@/ext#%{_sysconfdir}/%{serverName}/ext#g;' \
		-i < tmp.slist

rm -f tmp.flist tmp.slist


##########################################################################
##########################################################################

%build

# Remove hard-coded compiler options so we can use our own
%{__perl} -p -e 's/^CC/#CC/g;' -e 's/^CFLAGS/#CFLAGS/g;' -i build/Makefile.Linux

%if_enabled dietlibc
  # Include strings.h in code that has a strcasecmp function, which may not always be in "string.h"
  # This kind of stuff gets caught with automake, but we're not using that here
    find -type f | grep \.c$ | xargs -r grep -l strcasecmp | xargs -r \
	%{__perl} -p -e 's|#include <string.h>|#include <string.h>\n#include <strings.h>|' -i

  # Build static dietlibc client before the regular server
    export ENABLESSL=n SSLOK=NO \
	XYMONUSER=xymon \
	XYMONTOPDIR=%{xymonRoot} \
	XYMONHOSTIP=127.0.0.1 \
	CONFTYPE=server \
	CC="diet gcc" \
	CFLAGS="%{optflags} -DREALLY_SMALL -finline-functions -Os"

    ./configure.client
    make PKGBUILD=1 client
    cp -fpR client client-diet
    make distclean
%endif # dietlibc


export	CC="gcc" \
	CFLAGS="%{optflags} -pthread"
export	USEXYMONPING=n \
	USERFPING=%{_sbindir}/fping \
	ENABLESSL=y SSLOK=YES \
	ENABLELDAP=y \
	ENABLELDAPSSL=y \
	CONFTYPE=server \
	XYMONUSER=xymon \
	XYMONTOPDIR=%{xymonRoot} \
	XYMONVAR=%{libDirectory} \
	XYMONHOSTURL=/xymon \
	CGIDIR=%{xymonServerRoot}/cgi-bin \
	XYMONCGIURL=/xymon-cgi \
	SECURECGIDIR=%{xymonServerRoot}/cgi-secure \
	SECUREXYMONCGIURL=/xymon-seccgi \
	HTTPDGID=apache \
	XYMONLOGDIR=%{logDirectory} \
	XYMONRUNDIR=%{runDirectory}	\
	XYMONHOSTNAME=localhost \
	XYMONHOSTIP=127.0.0.1 \
	MANROOT=%{_mandir} \
	INSTALLBINDIR=%{_libexecdir}/%{serverName} \
	INSTALLETCDIR=%{_sysconfdir}/%{serverName} \
	INSTALLEXTDIR=%{_sysconfdir}/%{serverName}/ext \
	INSTALLWEBDIR=%{webDirectory} \
	INSTALLTMPDIR=%{tmpDirectorySrv} \
	INSTALLWWWDIR=%{wwwDirectory} \
	INSTALLSTATICWWWDIR=%{wwwStaticDirectory}

%{?_enable_snmp:export SNMP=1}


# this is not gnu autoconf -- can't use macro
./configure

# Make
# %{__perl} -p -e 's/^# XYMONLIBRARY=libxymon.so/XYMONLIBRARY=libxymon.so/' -i build/Makefile.Linux
make PKGBUILD=1


%if_enabled selinux
pushd SELinux
for selinuxvariant in %{selinux_variants} ; do
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
    mv %{serverName}.pp %{serverName}.pp.${selinuxvariant}
    mv %{clientName}.pp %{clientName}.pp.${selinuxvariant}
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
popd
%endif # selinux


##########################################################################
##########################################################################

%install

# rollback of changes for cgiwrap introduced in 4.3.20
%{__perl} -p -e 's/ln -f \$\(INSTALLROOT\)/ln -sf /g;' -i %{_builddir}/%{name}-%{version}/web/Makefile

install -d %{buildroot}%{wwwCacheDirectory}
install -d %{buildroot}%{runDirectory}
install -d %{buildroot}%{_bindir}
make PKGBUILD=1 INSTALLROOT=%{buildroot} install

install -m 644 %{SOURCE3} README.redhat

%if_enabled dietlibc
   # Copy the smaller, static client binaries back into the client section
   for bin in xymon xymoncmd xymondigest xymonlaunch logfetch msgcache; do
	install -m 755 client-diet/$bin %{buildroot}%{xymonRoot}/client/bin/
   done
%endif # dietlibc


# Fix a utf8 warning from rpmlint
  iconv --from=ISO-8859-1 --to=UTF-8 CREDITS > CREDITS.utf8 && \
	touch -r CREDITS CREDITS.utf8 && mv CREDITS.utf8 CREDITS

# Move client home directory to /usr/share/xymon-client
  mv %{buildroot}%{xymonRoot}/client %{buildroot}%{xymonClientRoot}
  ln -s %{xymonClientRoot} %{buildroot}%{xymonRoot}/client

# Handled below
  rm -f %{buildroot}%{xymonClientRoot}/{local,sections}/README

# Install init scripts
  install -d %{buildroot}%{_initrddir}
  mv %{buildroot}%{_libexecdir}/%{serverName}/xymon-init.d %{buildroot}%{_initrddir}/%{serverName}
  mv %{buildroot}%{xymonClientRoot}/bin/xymon-client.init %{buildroot}%{_initrddir}/%{clientName}
  rm -f %{buildroot}%{_libexecdir}/%{serverName}/xymon-client.init
  rm -f %{buildroot}%{_libexecdir}/%{serverName}/xymon.sh
  rm -f %{buildroot}%{xymonClientRoot}/runclient.sh
  rm -f %{buildroot}%{xymonRoot}/server/xymon.sh 


# Install the apache config and touch htpasswd files
  touch %{buildroot}%{_sysconfdir}/%{serverName}/xymonpasswd
  touch %{buildroot}%{_sysconfdir}/%{serverName}/xymongroups

  install -d %{buildroot}%{_sysconfdir}/httpd2/conf/addon.d
  mv -f %{buildroot}%{_sysconfdir}/%{name}/xymon-apache.conf \
	%{buildroot}%{_sysconfdir}/httpd2/conf/addon.d/A.%{serverName}.conf

  ### add /hobbit -> /xymon compatibility line for previous package versions
  echo "RewriteRule ^/hobbit(.*) /xymon\$1 [R=permanent,L]" >> \
	%{buildroot}%{_sysconfdir}/httpd2/conf/addon.d/A.%{serverName}.conf


# Certs = config files
  install -d %{buildroot}%{_sysconfdir}/%{serverName}/certs
  ln -s %{_sysconfdir}/%{serverName}/certs %{buildroot}%{xymonRoot}/server/certs


# Dynamically create these directories if/when needed
  rmdir %{buildroot}%{wwwDirectory}/{html,notes,rep,snap,wml} 
  rmdir %{buildroot}%{libDirectory}/logs		# this is for [storestatus], not /var/log/xymon

# we've moved the positions of some of these directories
  %{__perl} -p	-e 's#\$XYMONWWWDIR/rep#%{wwwCacheDirectory}/rep#g;'	\
	-e 's#\$XYMONWWWDIR/snap#%{wwwCacheDirectory}/snap#g;'	\
	-e 's#\$XYMONHOME/static#%{wwwStaticDirectory}#g;'	\
	-e 's#\$XYMONHOME/www#%{wwwDirectory}#g;'			\
		-i %{buildroot}%{_sysconfdir}/%{serverName}/xymonserver.cfg


# logrotate scripts for servers and clients
  install -d %{buildroot}%{_sysconfdir}/logrotate.d
  %{__perl} -p -e 's#/var/log/xymon/\*.log#%{logDirectory}/*.log#' -i rpm/xymon.logrotate
  %{__perl} -p -e 's#/etc/init.d/xymon rotate#/sbin/service %{serverName} rotate >/dev/null 2>/dev/null#'  rpm/xymon.logrotate	> %{buildroot}%{_sysconfdir}/logrotate.d/%{serverName}
  %{__perl} -p -e 's#/etc/init.d/xymon rotate#/sbin/service %{clientName} rotate >/dev/null 2>/dev/null#'  rpm/xymon.logrotate	> %{buildroot}%{_sysconfdir}/logrotate.d/%{clientName}
  chmod 644 %{buildroot}%{_sysconfdir}/logrotate.d/*


# sysconfig files for servers and clients
  install -d %{buildroot}%{_sysconfdir}/sysconfig
  install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/sysconfig/%{clientName}
  install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/%{serverName}
  %{__perl} -p -e 's#/etc/default/#%{_sysconfdir}/sysconfig/#' -i %{buildroot}%{_initrddir}/*

# fix permissions
  find %{buildroot}%{wwwStaticDirectory} -type f | xargs -r chmod 644


# disable "clientupdate", which won't work on RPM systems
  rmdir %{buildroot}%{xymonRoot}/server/download/
  rm -f %{buildroot}%{xymonClientRoot}/bin/clientupdate
  rm -f %{buildroot}%{_mandir}/*/clientupdate.*

# disable localclient.cfg, which also won't work
  rm -f %{buildroot}%{xymonClientRoot}/etc/localclient.cfg
  rm -f %{buildroot}%{xymonClientRoot}/bin/{xymoncfg,xymongrep}


# remove unneeded HOME variables
  %{__perl} -p -e 's#\$XYMONHOME/bin#%{_libexecdir}/%{clientName}#g;' -e 's#\$XYMONHOME/#%{xymonClientRoot}/#g;' \
	-i %{buildroot}%{xymonClientRoot}/etc/xymonclient.cfg %{buildroot}%{xymonClientRoot}/bin/xymonclient.sh

  %{__perl} -p -e 's#\$XYMONHOME/bin#%{_libexecdir}/%{serverName}#g;' -e 's#\$XYMONHOME/etc#%{_sysconfdir}/%{serverName}#g;'	\
	-i %{buildroot}%{_sysconfdir}/%{serverName}/xymonserver.cfg


# For server tests, increase the frequency of all 5m testing up to 1m; xymonnet-again to 30s
  %{__perl} -p -e 's/INTERVAL 5m/INTERVAL 1m/g;'	-i %{buildroot}%{_sysconfdir}/%{serverName}/tasks.cfg
  %{__perl} -0pe 's/xymonnetagain.log\n\tINTERVAL \d+\w?/xymonnetagain.log\n\tINTERVAL 30s/s' -i %{buildroot}%{_sysconfdir}/%{serverName}/tasks.cfg

# For client reports, increase the frequency from 5m to 100s
  %{__perl} -p -e 's/INTERVAL 5m/INTERVAL 100s/g;' -i %{buildroot}%{xymonClientRoot}/etc/clientlaunch.cfg
  %{__perl} -0pe 's/xymonclient.log\n\tINTERVAL \d+\w?/xymonclient.log\n\tINTERVAL 100s/s' -i %{buildroot}%{_sysconfdir}/%{serverName}/tasks.cfg

# Save a fork and hard-code our version into xymonclient.sh
  %{__perl} -p -e 's/`\$XYMON --version`/Xymon version %{version}-%{release}/' -i %{buildroot}%{xymonClientRoot}/bin/xymonclient.sh


# Since environment is always set, full pathnames aren't needed
  %{__perl} -p	-e 's#CMD \$XYMONCLIENTHOME/bin/#CMD #g;'	-e 's#CMD %{_libexecdir}/%{clientName}/#CMD #g;' \
	-e 's#CMD \$XYMONHOME/ext/#CMD %{_sysconfdir}/%{serverName}/ext/#g;' \
	-e 's#CMD \$XYMONHOME/bin/#CMD #g;' \
	-e 's#\$XYMONHOME/logs#%{logDirectory}#g;' \
	-i %{buildroot}%{_sysconfdir}/%{serverName}/tasks.cfg

  %{__perl} -p	-e 's#CMD \$XYMONCLIENTHOME/bin/#CMD #g;'				\
	-e 's#CMD \$XYMONCLIENTHOME/ext/#CMD %{_sysconfdir}/%{clientName}/ext/#g;' \
	-e 's#\$XYMONCLIENTHOME/etc#%{_sysconfdir}/%{clientName}#g;'	\
	-e 's#CMD %{xymonRoot}/client/bin/#CMD #g;'			\
	-i %{buildroot}%{xymonClientRoot}/etc/clientlaunch.cfg

  %{__perl} -p	-e 's#\$XYMONHOME/bin#%{_libexecdir}/%{serverName}#g;' -i %{buildroot}%{_libexecdir}/%{serverName}/*.sh

   if [ -f %{buildroot}%{_sysconfdir}/%{serverName}/ext/xymonnet-again.sh ] ; then
	%{__perl} -p -e 's#\$XYMONHOME/bin#%{_libexecdir}/%{serverName}#g;' -i %{buildroot}%{_sysconfdir}/%{serverName}/ext/xymonnet-again.sh 
   fi

# Move client binaries to /usr/bin
  pushd %{buildroot}%{xymonClientRoot}
    for this in xymon xymoncmd xymondigest logfetch msgcache xymonlaunch; do
       mv -f bin/$this %{buildroot}%{_bindir}/$this
       ln -s %{_bindir}/$this bin/$this
    done

# Put the rest of the home directory in their proper places
    mv -f bin %{buildroot}%{_libexecdir}/%{clientName}
    mv -f etc %{buildroot}%{_sysconfdir}/%{clientName}
    ln -s %{_libexecdir}/%{clientName}	bin
    ln -s %{_sysconfdir}/%{clientName}	etc
    rmdir local logs
    ln -s %{logDirectory} logs
  popd


# Make sure XYMONTMP and PATH are always set properly
  %{__perl} -p -e 's#XYMONTMP=".*"#XYMONTMP="%{tmpDirectorySrv}"#g;' -i %{buildroot}%{_sysconfdir}/%{serverName}/xymonserver.cfg
  %{__perl} -p -e 's#XYMONTMP=".*"#XYMONTMP="%{tmpDirectoryCli}"#g;' -i %{buildroot}%{_sysconfdir}/%{clientName}/xymonclient.cfg
  %{__perl} -p -e 's#PATH="#PATH="%{_libexecdir}/%{serverName}:#' -i %{buildroot}%{_sysconfdir}/%{serverName}/xymonserver.cfg
  %{__perl} -p -e 's#PATH="#PATH="%{_libexecdir}/%{clientName}:#' -i %{buildroot}%{_sysconfdir}/%{clientName}/xymonclient.cfg

# Now that XYMOMTMP is hard-coded to where we need it; remove extraneous symlinks
  rmdir %{buildroot}%{xymonClientRoot}/tmp
  rm -f %{buildroot}%{xymonServerRoot}/tmp


# Big Brother compatibility symlinks
  ln -s xymon %{buildroot}%{_bindir}/bb
  ln -s xymoncmd %{buildroot}%{_bindir}/bbcmd
  ln -s %{_bindir}/xymon %{buildroot}%{_libexecdir}/%{clientName}/bb
  ln -s %{_bindir}/xymoncmd %{buildroot}%{_libexecdir}/%{clientName}/bbcmd
  ln -s xymon.1 %{buildroot}%{_mandir}/man1/bb.1
  ln -s xymoncmd.1 %{buildroot}%{_mandir}/man1/bbcmd.1


# Since it's writable by apache, move critical.cfg out of /etc/xymon
  install -d %{buildroot}%{libDirectory}/configs/
  mv %{buildroot}%{_sysconfdir}/%{serverName}/critical.cfg %{buildroot}%{libDirectory}/configs/critical.cfg
  rm -f %{buildroot}%{_sysconfdir}/%{serverName}/critical.cfg.bak

  ln -s %{libDirectory}/configs/critical.cfg %{buildroot}%{_sysconfdir}/%{serverName}/critical.cfg
  ln -s %{xymonClientRoot}/ext %{buildroot}%{_sysconfdir}/%{clientName}/ext


%if_enabled extraclients
  install -m 644 %{SOURCE4} README.core
%else
  ## remove orcaxymon from tree
  rm -f %{buildroot}%{_libexecdir}/%{clientName}/orcaxymon
  rm -f %{buildroot}%{_mandir}/*/orcaxymon.*
%endif # extraclients


# Create /etc/xymon*/*.d/ configuration directories
# For the server
  for THIS in alerts analysis graphs combo protocols tasks; do
      install -d %{buildroot}%{_sysconfdir}/%{serverName}/${THIS}.d
  done
# For the client
  install -d %{buildroot}%{_sysconfdir}/%{clientName}/client.d
  echo "
# Include add-on modules -- do not confuse with /local/ scripts, which are tests inserted directly into the client report
directory %{_sysconfdir}/%{clientName}/client.d" >> %{buildroot}%{_sysconfdir}/%{clientName}/clientlaunch.cfg


# Add [mounts] to client
  install -m 755 %{SOURCE21} %{buildroot}%{xymonClientRoot}/sections/mounts

# Automatic periodic SLA reports (daily/weekly/monthly)
  install -m 644 %{SOURCE31} %{buildroot}%{_sysconfdir}/%{serverName}/tasks.d/dailyreport
  install -m 644 %{SOURCE32} %{buildroot}%{_sysconfdir}/%{serverName}/tasks.d/weeklyreport
  install -m 644 %{SOURCE33} %{buildroot}%{_sysconfdir}/%{serverName}/tasks.d/monthlyreport

# xymongen task should be in web package
  install -m 644 %{SOURCE34} %{buildroot}%{_sysconfdir}/%{serverName}/tasks.d/xymongen

# deal with alternative shells
%if_enabled altshell
	%{__perl} -p -e 's#/bin/sh#%{shell}#' -i %{buildroot}%{xymonClientRoot}/sections/*
%endif


%if_enabled selinux
  # SELinux policy
  for selinuxvariant in %{selinux_variants}; do
    install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
    for policyname in %{serverName} %{clientName}; do
	install -p -m 644 SELinux/${policyname}.pp.${selinuxvariant} %{buildroot}%{_datadir}/selinux/${selinuxvariant}/${policyname}.pp
    done
  done
%endif

# removing client's scripts for non linux
# (buildreq should not parse it)
for FNAME in `ls -1 %buildroot%_libexecdir/xymon-client/xymonclient-*|grep -v linux`; do
    rm -f $FNAME
done

ln -s %_libexecdir/xymon/xymond_client %buildroot%_libexecdir/xymon-client/xymond_client

# add content-type to all html headers
%{__perl} -p -e 's#<HEAD>|<head>#<HEAD>\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">#;' -i %{buildroot}%{_sysconfdir}/%{serverName}/web/*_header

##########################################################################
##########################################################################

%pre
getent passwd xymon >/dev/null && \
	usermod -d "%{xymonRoot}" -c "xymon Monitor" xymon 2>/dev/null || :

###################################################################
%pre client
getent passwd xymon >/dev/null && \
	usermod -d "%{xymonClientRoot}" -c "xymon Monitor (client)" xymon 2>/dev/null || :

###################################################################
%pre common
getent passwd xymon >/dev/null || \
	useradd -r -d "/tmp" -s /sbin/nologin xymon 2>/dev/null || :

%post
if [ "$1" -eq 1 ]; then
  # Replace default 'localhost' entries (from install) with our real hostname
  # so we provide useful local info even when not using --local
  HOSTNAME="`uname -n`"
  %{__perl} -p -e "s/ localhost\b/ $HOSTNAME/g;" -e "s/^127.0.0.1/0.0.0.0/g;" -i %{_sysconfdir}/%{serverName}/hosts.cfg
  %{__perl} -p -e "s/^XYMONSERVERS=\"\"\$/XYMONSERVERS=\"127.0.0.1\"/g;" -i %{_sysconfdir}/sysconfig/%{clientName}
fi

# Fix duplicate localhost bug
  %{__perl} -p -e "s/\blocalhost\b/$HOSTNAME/g;" -i %{_sysconfdir}/%{serverName}/xymonserver.cfg*
  XYMDAT="`xymoncmd env | grep -e XYMONSERVERIP= -e XYMONSERVERS= -e XYMSERVERS=`"
  SIP=`echo "$XYMDAT" | grep ^XYMONSERVERIP= | %{__perl} -p -e 's/^.*=//'`
  SRV=`echo "$XYMDAT" | grep ^XYMONSERVERS= | %{__perl} -p -e 's/^.*=//'`
  XYM=`echo "$XYMDAT" | grep ^XYMSERVERS= | %{__perl} -p -e 's/^.*=//'`
  if [ x"$SIP" = x"$SRV" -a "$XYM" = "$SIP $SRV" ] ; then
	%{__perl} -p -e 's/^XYMSERVERS=\"\$XYMONSERVERIP \$XYMONSERVERS\"/XYMSERVERS=\"\$XYMONSERVERIP\"	/g;' -i %{_sysconfdir}/%{serverName}/xymonserver.cfg*
  fi
# XXX: Future use, when working with systemd unit files >.<
## Convert file 'include' lines to file 'source' lines for systemd compat
#  sed -e "s/^include /source /" -i %{_sysconfdir}/%{serverName}/xymonserver.cfg*  %{_sysconfdir}/%{clientName}/xymonclient.cfg*

%if_enabled selinux
/usr/sbin/semanage fcontext -a -t initrc_var_run_t		'%{runDirectory}(/.*)?'			|| :
/usr/sbin/semanage fcontext -a -t httpd_cache_t			'%{wwwCacheDirectory}(/.*)?'		|| :
/usr/sbin/semanage fcontext -a -t httpd_sys_script_exec_t	'%{xymonServerRoot}/cgi-bin(/.*)?'	|| :
/usr/sbin/semanage fcontext -a -t httpd_sys_script_exec_t	'%{xymonServerRoot}/cgi-secure(/.*)?'	|| :
/usr/sbin/semanage fcontext -a -t httpd_sys_content_t		'%{libDirectory}(/.*)?'			|| :
/usr/sbin/semanage fcontext -a -t tmp_t				'%{tmpDirectorySrv}(/.*)?'		|| :
/sbin/restorecon -R %{xymonServerRoot}/cgi-* %{wwwCacheDirectory} %{runDirectory} %{libDirectory} %{tmpDirectorySrv} || :

for selinuxvariant in %{selinux_variants}; do
    /usr/sbin/semodule -s ${selinuxvariant} -i %{_datadir}/selinux/${selinuxvariant}/%{serverName}.pp &> /dev/null || :
    /usr/sbin/semodule -s ${selinuxvariant} -i %{_datadir}/selinux/${selinuxvariant}/%{clientName}.pp &> /dev/null || :
done
if [ "$1" -eq 1 ]; then
    /usr/sbin/setsebool -P httpd_can_network_connect on 2>/dev/null || :
fi
%endif # selinux

%post_service %{serverName}

###################################################################
%post client
%post_service %{clientName}

HOSTNAME="`uname -n`"
%{__perl} -p -e "s/^# MACHINEDOTS=\"localhost\"$/MACHINEDOTS=\"${HOSTNAME}\"/g;" -i %{_sysconfdir}/sysconfig/%{clientName}

%if_enabled selinux
for selinuxvariant in %{selinux_variants}; do
    /usr/sbin/semodule -s ${selinuxvariant} -i %{_datadir}/selinux/${selinuxvariant}/%{clientName}.pp &> /dev/null || :
done
%endif

# XXX: Future use, when working with systemd unit files >.<
## Convert file 'include' lines to file 'source' lines for systemd compat
#  sed -e "s/^include /source /" -i %{_sysconfdir}/%{clientName}/xymonclient.cfg*

%post apache2
for A2MODULE in authn_file authz_groupfile rewrite userdir cgi; do
    a2enmod $A2MODULE &>/dev/null || :
done

%preun
%preun_service  %{serverName}

%postun
%if_enabled selinux
if [ "$1" -eq 0 ]; then
   /usr/sbin/semanage fcontext -d -t tmp_t			'%{tmpDirectorySrv}(/.*)?' 2>/dev/null || :
   /usr/sbin/semanage fcontext -d -t httpd_cache_t		'%{wwwCacheDirectory}(/.*)?' 2>/dev/null || :
   /usr/sbin/semanage fcontext -d -t initrc_var_run_t		'%{runDirectory}(/.*)?' 2>/dev/null || :
   /usr/sbin/semanage fcontext -d -t httpd_sys_script_exec_t	'%{xymonServerRoot}/cgi-bin(/.*)?' 2>/dev/null || :
   /usr/sbin/semanage fcontext -d -t httpd_sys_script_exec_t	'%{xymonServerRoot}/cgi-secure(/.*)?' 2>/dev/null || :
   /usr/sbin/semanage fcontext -d -t httpd_sys_content_t	'%{libDirectory}(/.*)?' 2>/dev/null || :
   for selinuxvariant in %{selinux_variants}; do
     /usr/sbin/semodule -s ${selinuxvariant} -r %{clientName} &> /dev/null || :
     /usr/sbin/semodule -s ${selinuxvariant} -r %{serverName} &> /dev/null || :
   done
   /bin/true
fi
%endif # selinux


%preun client
%preun_service %{clientName}

%postun client
%if_enabled selinux
if [ "$1" -eq 0 ]; then
   for selinuxvariant in %{selinux_variants}; do
     /usr/sbin/semodule -s ${selinuxvariant} -r %{clientName} &> /dev/null || :
   done
   /bin/true
fi
%endif


###################################################################
%if_enabled extraclients
###################################################################
#######################################
%pre client-passive
if [ -r "%{_sysconfdir}/sysconfig/%{clientName}" ] ; then
   if [ "`grep -c ^HOBBITSERVERS= %{_sysconfdir}/sysconfig/%{clientName} 2>/dev/null`" -gt 0 -a \
	"`grep -c ^XYMONSERVERS= %{_sysconfdir}/sysconfig/%{clientName} 2>/dev/null`" -eq 0 ]
   then
	sed -e 's/^HOBBITSERVERS=\(.*\)$/XYMONSERVERS=\1\nHOBBITSERVERS=\1/' -i %{_sysconfdir}/sysconfig/%{clientName} 2>/dev/null
   fi
fi
%if_enabled selinux
for selinuxvariant in %{selinux_variants}; do
  /usr/sbin/semodule -s ${selinuxvariant} -i %{_datadir}/selinux/${selinuxvariant}/%{clientName}.pp &> /dev/null || :
done
%endif


#######################################
%pre client-core
if [ -r "%{_sysconfdir}/sysconfig/%{clientName}" ] ; then
   if [ "`grep -c ^HOBBITSERVERS= %{_sysconfdir}/sysconfig/%{clientName} 2>/dev/null`" -gt 0 -a \
	"`grep -c ^XYMONSERVERS= %{_sysconfdir}/sysconfig/%{clientName} 2>/dev/null`" -eq 0 ]
   then
	sed -e 's/^HOBBITSERVERS=\(.*\)$/XYMONSERVERS=\1\nHOBBITSERVERS=\1/' -i %{_sysconfdir}/sysconfig/%{clientName} 2>/dev/null
   fi
fi


#######################################
%postun client-passive
%if_enabled selinux
for selinuxvariant in %{selinux_variants}; do
  /usr/sbin/semodule -s ${selinuxvariant} -r %{clientName} &> /dev/null || :
done
/bin/true
%endif

#######################################################################
%endif # extraclients
#######################################################################

%files
%doc README README.CLIENT README.redhat Changes* COPYING CREDITS RELEASENOTES
%doc client/README-local client/README-sections

%if_enabled selinux
%doc SELinux/%{serverName}.te
%doc SELinux/%{clientName}.te
%{_datadir}/selinux/*/%{serverName}.pp
%{_datadir}/selinux/*/%{clientName}.pp
%endif

%{_initdir}/%{serverName}

%exclude %{_libexecdir}/%{serverName}/xymond_client
%exclude %{_libexecdir}/%{serverName}/*.cgi
%{_libexecdir}/%{serverName}/*

%exclude		%{_sysconfdir}/%{serverName}/tasks.d/xymongen
%dir			%{_sysconfdir}/%{serverName}
%dir			%{_sysconfdir}/%{serverName}/ext
%dir			%{_sysconfdir}/%{serverName}/certs
%dir			%{_sysconfdir}/%{serverName}/*.d
%config(noreplace)	%{_sysconfdir}/%{serverName}/*.d/*
%config(noreplace)	%{_sysconfdir}/%{serverName}/*.cfg
%config(noreplace)	%{_sysconfdir}/%{serverName}/columndoc.csv
%config(noreplace)	%ghost	%attr(644,root,root)	%{_sysconfdir}/%{serverName}/xymonpasswd
%config(noreplace)	%ghost	%attr(644,root,root)	%{_sysconfdir}/%{serverName}/xymongroups

%exclude %{libDirectory}/configs/critical.cfg*
%dir	%{libDirectory}
%attr(755,xymon,xymon) %dir	%{libDirectory}/acks
%attr(755,xymon,xymon) %dir	%{libDirectory}/configs
%attr(755,xymon,xymon) %dir	%{libDirectory}/data
%attr(755,xymon,xymon) %dir	%{libDirectory}/disabled
%attr(755,xymon,xymon) %dir	%{libDirectory}/hist
%attr(755,xymon,xymon) %dir	%{libDirectory}/histlogs
%attr(755,xymon,xymon) %dir	%{libDirectory}/hostdata
%attr(755,xymon,xymon) %dir	%{libDirectory}/rrd
%attr(755,xymon,xymon) %dir	%{libDirectory}/tmp

%exclude %{xymonServerRoot}/server/static
%exclude %{xymonServerRoot}/server/web
%exclude %{xymonServerRoot}/server/www
%dir	%{xymonServerRoot}
%dir	%{xymonServerRoot}/server
%{xymonServerRoot}/server/*
%{xymonServerRoot}/client

%if_disabled trunk
%attr(755,root,root)	%{_sysconfdir}/%{serverName}/ext/xymonnet-again.sh
%endif

%attr(644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{serverName}
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{serverName}

%files web
%attr(755,xymon,xymon)	%{wwwDirectory}
%attr(755,xymon,_webserver) %dir %{wwwCacheDirectory}
%attr(755,xymon,xymon) %dir %{libDirectory}/configs
%attr(755,xymon,xymon) %ghost %{libDirectory}/configs/critical.cfg*

%config(noreplace)	%{_sysconfdir}/%{serverName}/tasks.d/xymongen

%{_libexecdir}/%{serverName}/*.cgi

%dir %{webDirectory}
%config(noreplace) %{webDirectory}/*

%dir %{wwwStaticDirectory}
%{wwwStaticDirectory}/*

%{xymonServerRoot}/cgi-bin
%{xymonServerRoot}/cgi-secure
%{xymonServerRoot}/server/static
%{xymonServerRoot}/server/web
%{xymonServerRoot}/server/www

%files apache2
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/httpd2/conf/addon.d/A.%{serverName}.conf

%files common
%dir	%{_sysconfdir}/%{clientName}
%dir	%{_sysconfdir}/%{clientName}/client.d
	%{_sysconfdir}/%{clientName}/ext

%attr(644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{clientName}
%attr(644,root,root) %config(noreplace)	%{_sysconfdir}/%{clientName}/xymonclient.cfg
%attr(644,root,root) %config(noreplace)	%{_sysconfdir}/%{clientName}/clientlaunch.cfg

%{_bindir}/xymon*
%{_bindir}/logfetch
%{_bindir}/msgcache

%dir	%{_libexecdir}/%{serverName}
%{_libexecdir}/%{serverName}/xymond_client

### client stuff ###

%{xymonClientRoot}
%dir	%{_libexecdir}/%{clientName}
%{_libexecdir}/%{clientName}/bb*
%{_libexecdir}/%{clientName}/logfetch
%{_libexecdir}/%{clientName}/msgcache
%{_libexecdir}/%{clientName}/xymon
%{_libexecdir}/%{clientName}/xymoncmd
%{_libexecdir}/%{clientName}/xymondigest
%{_libexecdir}/%{clientName}/xymonlaunch
%{_libexecdir}/%{clientName}/xymonclient.sh
%{_libexecdir}/%{clientName}/xymonclient-linux.sh
%{_libexecdir}/%{clientName}/xymond_client

### end client stuff ###

%attr(1770,root,xymon)	%{logDirectory}
%attr(1770,root,xymon)	%{runDirectory}

%files man
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*

%files client
%doc README README.CLIENT README.redhat Changes* COPYING CREDITS RELEASENOTES
%doc client/README-local client/README-sections
%if_enabled selinux
%doc SELinux/%{clientName}.te
%{_datadir}/selinux/*/%{clientName}.pp
%endif

%attr(755,root,root) %{_initrddir}/%{clientName}
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{clientName}

%files bb-compatibility
%{_bindir}/bb*

################ start extra clients ################
%if_enabled extraclients
%files client-passive
%doc README README.CLIENT README.redhat Changes* COPYING CREDITS RELEASENOTES
%doc client/README-local client/README-sections
%if_enabled selinux
%doc SELinux/%{clientName}.te
%{_datadir}/selinux/*/%{clientName}.pp
%endif

%{_mandir}/man1/bb.1.*
%{_mandir}/man1/bbcmd.1.*
%{_mandir}/man1/xymon.1.*
%{_mandir}/man1/xymoncmd.1.*
%{_mandir}/man1/xymondigest.1.*
%{_mandir}/man1/logfetch.1.*
%{_mandir}/man5/xymonclient.cfg.5.*

%{_bindir}/bb*
%{_bindir}/xymon*
%attr(755,root,root) %dir	%{_libexecdir}/%{clientName}
%{_libexecdir}/%{clientName}/bb*
%{_libexecdir}/%{clientName}/xymon
%{_libexecdir}/%{clientName}/xymoncmd
%{_libexecdir}/%{clientName}/xymondigest
%{_libexecdir}/%{clientName}/xymonclient.sh
%{_libexecdir}/%{clientName}/xymonclient-linux.sh

%{xymonClientRoot}
%exclude %{xymonClientRoot}/logs

%dir		   %{_sysconfdir}/%{clientName}
%config(noreplace) %{_sysconfdir}/%{clientName}/xymonclient.cfg
%config(noreplace) %{_sysconfdir}/sysconfig/%{clientName}

%{_bindir}/logfetch
%{_libexecdir}/%{clientName}/logfetch

%files client-core
%doc README README.redhat README.core Changes* COPYING CREDITS RELEASENOTES

%{_mandir}/man1/bb.1.*
%{_mandir}/man1/bbcmd.1.*
%{_mandir}/man1/xymon.1.*
%{_mandir}/man1/xymoncmd.1.*
%{_mandir}/man1/xymondigest.1.*

%{_bindir}/bb
%{_bindir}/bbcmd
%{_bindir}/xymon
%{_bindir}/xymoncmd
%{_bindir}/xymondigest
%{_libexecdir}/%{clientName}/bb
%{_libexecdir}/%{clientName}/bbcmd
%{_libexecdir}/%{clientName}/xymon
%{_libexecdir}/%{clientName}/xymoncmd
%{_libexecdir}/%{clientName}/xymondigest
%dir %{_libexecdir}/%{clientName}

# Still need to know where to send data
%dir		   %{_sysconfdir}/%{clientName}
%config(noreplace) %{_sysconfdir}/%{clientName}/xymonclient.cfg
%config(noreplace) %{_sysconfdir}/sysconfig/%{clientName}

# $XYMONCLIENTHOME
%dir %{xymonClientRoot}
     %{xymonClientRoot}/bin
     %{xymonClientRoot}/etc

%files client-orca
%doc README Changes* COPYING CREDITS RELEASENOTES
%{_libexecdir}/%{clientName}/orcaxymon
%{_mandir}/*/orcaxymon.*
%endif

################ end extra clients ################

%changelog
* Thu Sep 12 2019 Sergey Y. Afonin <asy@altlinux.org> 4.3.29-alt1
- new version  (fixes: CVE-2019-13451, CVE-2019-13452, CVE-2019-13455,
  CVE-2019-13473, CVE-2019-13474, CVE-2019-13484, CVE-2019-13485,
  CVE-2019-13486)
- fixed handling /var/run on tmpfs

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.3.28-alt2.2
- NMU: Rebuild with new openssl 1.1.0.

* Mon Mar 12 2018 Grigory Ustinov <grenka@altlinux.org> 4.3.28-alt2.1
- NMU: Add patch for fix rebuild in Sisyphus.

* Tue Oct 31 2017 Sergey Y. Afonin <asy@altlinux.ru> 4.3.28-alt2
- rebuilt with librrd8

* Tue May 23 2017 Sergey Y. Afonin <asy@altlinux.ru> 4.3.28-alt1
- new version
- increased logfetch's buffer size from 2048000 to 4194303

* Fri Apr 22 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.3.27-alt2
- dropped patch for config of logrotate, changed permissions for
  %{logDirectory} instead; permissions for %{runDirectory} changed
  similarly

* Thu Apr 21 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.3.27-alt1
- new version
- fixed config for logrotate
- increased logfetch's buffer size from 102400 to 2048000

* Fri Feb 26 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.3.26-alt1
- new version (CVE-2016-2054, CVE-2016-2055, CVE-2016-2056,
  CVE-2016-2057, CVE-2016-2058 was fixed in previous 4.3.25)

* Fri Jul 17 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.3.21-alt1
- new version (CVE-2015-1430 was fixed in previous 4.3.18)
- moved binaries from /usr/lib to /usr/libexec
  (xymonserver.cfg of earlier installed package should be updated manualy)
- removed "Requires: ntp" (but ntpdate and ntpq may be needed
  in some installations)

* Wed Feb 12 2014 Sergey Y. Afonin <asy@altlinux.ru> 4.3.16-alt1
- new version
- added xymonclient-linux.sh-various-procps.patch

* Wed Jan 22 2014 Sergey Y. Afonin <asy@altlinux.ru> 4.3.13-alt1
- new version (CVE-2013-4173 was fixed in previous 4.3.12)
- some patches synced with terabithia's xymon-4.3.13-1.fc20.src.rpm

* Thu May 16 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.3.11-alt1
- new version
- added xymongen-4311.patch and
  updated xymon.sections.patch and xymon_trunk.installstaticwww.patch from
  http://terabithia.org/rpms/xymon/testing/f18/xymon-4.3.11-5.fc18.src.rpm

* Sun Apr 07 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.3.10-alt4
- moved /usr/bin/bb* to bb-compatibility package
  (resolved conflict with BB - the portable AAlib demo)

* Sat Apr 06 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.3.10-alt3
- added charset=utf-8 to web/*_header

* Sun Mar 31 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.3.10-alt2
- added control for using "ifconfig" and "netstat -rn" in
  xymonclient-linux.sh

* Thu Mar 28 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.3.10-alt1
- initial build for ALT Linux

* Thu Oct 04 2012 Igor Vlasenko <viy@altlinux.ru> 4.3.10-alt0.1
- converted by srpmconvert script from
  http://terabithia.org/rpms/xymon/fc17/xymon-4.3.10-1.fc17.src.rpm
