%define _pseudouser_user     _pcp
%define _pseudouser_group    _pcp
%define _pseudouser_home     %_sharedstatedir/pcp
%define _unpackaged_files_terminate_build 1


%define _localstatedir /var
%define _libexecdir /usr/libexec
%define _confdir  %_sysconfdir/pcp
%define _logsdir  %_localstatedir/log/pcp
%define _pmnsdir  %_sharedstatedir/pcp/pmns
%define _tempsdir %_sharedstatedir/pcp/tmp
%define _pmdasdir %_sharedstatedir/pcp/pmdas
%define _logconfdir %_sharedstatedir/pcp/config/pmlogconf

Name: pcp
Version: 5.0.2
Release: alt1
Summary: System-level performance monitoring and performance management
License: GPLv2+ and LGPLv2+ and CC-BY-SA-3.0
Group: Monitoring
URL: https://pcp.io

Source0: %name-%version.tar.gz
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: flex
BuildRequires: gcc-c++

BuildRequires: libavahi-devel
BuildRequires: liblzma-devel
BuildRequires: libnss-devel
BuildRequires: libreadline-devel
BuildRequires: librpm-devel
BuildRequires: libsasl2-devel
BuildRequires: libssl-devel
BuildRequires: libsystemd-devel

BuildRequires: perl-devel
BuildRequires: python3-devel

BuildRequires: perl-autodie
BuildRequires: perl-Class-DBI
BuildRequires: perl-DateTime
BuildRequires: perl-File-Slurp
BuildRequires: perl-JSON
BuildRequires: perl-LWP-UserAgent-Determined
BuildRequires: perl-List-MoreUtils
BuildRequires: perl-RRD
BuildRequires: perl-TimeDate
BuildRequires: perl-Spreadsheet-WriteExcel
BuildRequires: perl-XML-LibXML
BuildRequires: perl-XML-TokeParser

BuildRequires: chrpath
BuildRequires: postfix
BuildRequires: man-db

Requires: libpcopilot = %EVR

%description
Performance Co-Pilot (PCP) provides a framework and services to support
system-level performance monitoring and performance management.

The PCP open source release provides a unifying abstraction for all of
the interesting performance data in a system, and allows client
applications to easily retrieve and process any subset of that data.

# pcp-conf
%package conf
License: LGPLv2+
Group: Monitoring
Summary: Performance Co-Pilot run-time configuration

%description conf
Performance Co-Pilot (PCP) run-time configuration

# libpcp
%package -n libpcopilot
License: LGPLv2+
Group: Monitoring
Summary: Performance Co-Pilot run-time libraries
Requires: pcp-conf = %EVR

%description -n libpcopilot
Performance Co-Pilot (PCP) run-time libraries

# libpcp-devel
%package -n libpcopilot-devel
License: GPLv2+ and LGPLv2+
Group: Development/Other
Summary: Performance Co-Pilot (PCP) development headers
Requires: libpcopilot = %EVR

%description -n libpcopilot-devel
Performance Co-Pilot (PCP) headers for development.

# pcp-devel
%package devel
License: GPLv2+ and LGPLv2+
Group: Development/Other
Summary: Performance Co-Pilot (PCP) development tools and documentation
Requires: pcp = %EVR
Requires: libpcopilot-devel = %EVR

%description devel
Performance Co-Pilot (PCP) documentation and tools for development.

# pcp-manager
%package manager
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) manager daemon
Requires: pcp = %EVR

%description manager
An optional daemon (pmmgr) that manages a collection of pmlogger and
pmie daemons, for a set of discovered local and remote hosts running
the performance metrics collection daemon (pmcd).  It ensures these
daemons are running when appropriate, and manages their log rotation
needs.  It is an alternative to the cron-based pmlogger/pmie service
scripts.

# perl-PCP-common.
%package -n perl-PCP-common
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Perl common

%description -n perl-PCP-common
Performance Co-Pilot (PCP) Perl common

# perl-PCP-PMDA. This is the PCP agent perl binding.
%package -n perl-PCP-PMDA
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Perl bindings and documentation
Requires: perl-PCP-common

%description -n perl-PCP-PMDA
The PCP::PMDA Perl module contains the language bindings for
building Performance Metric Domain Agents (PMDAs) using Perl.
Each PMDA exports performance data for one specific domain, for
example the operating system kernel, Cisco routers, a database,
an application, etc.

# perl-PCP-MMV
%package -n perl-PCP-MMV
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Perl bindings for PCP Memory Mapped Values
Requires: perl-PCP-common

%description -n perl-PCP-MMV
The PCP::MMV module contains the Perl language bindings for
building scripts instrumented with the Performance Co-Pilot
(PCP) Memory Mapped Value (MMV) mechanism.
This mechanism allows arbitrary values to be exported from an
instrumented script into the PCP infrastructure for monitoring
and analysis with pmchart, pmie, pmlogger and other PCP tools.

# perl-PCP-LogImport
%package -n perl-PCP-LogImport
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Perl bindings for importing external data into PCP archives
Requires: perl-PCP-common

%description -n perl-PCP-LogImport
The PCP::LogImport module contains the Perl language bindings for
importing data in various 3rd party formats into PCP archives so
they can be replayed with standard PCP monitoring tools.

# perl-PCP-LogSummary
%package -n perl-PCP-LogSummary
BuildArch: noarch
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Perl bindings for post-processing output of pmlogsummary
Requires: perl-PCP-common

%description -n perl-PCP-LogSummary
The PCP::LogSummary module provides a Perl module for using the
statistical summary data produced by the Performance Co-Pilot
pmlogsummary utility.  This utility produces various averages,
minima, maxima, and other calculations based on the performance
data stored in a PCP archive.  The Perl interface is ideal for
exporting this data into third-party tools (e.g. spreadsheets).

# pcp-import-tools
%package import-tools
License: LGPLv2+
Group: Monitoring
Summary: Performance Co-Pilot tools for importing various format into PCP archive logs

%description import-tools
Performance Co-Pilot (PCP) front-end tools for importing various format
into standard PCP archive logs for replay with any PCP monitoring tool.

# pcp-export-tools
%package export-tools
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot tools for exporting PCP metrics to various format
Requires: python3-module-pcp = %EVR

%description export-tools
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in various format.

# pcp-pmdas
%package pmdas
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) metrics for various services
Requires: perl-PCP-PMDA = %EVR
Requires: python3-module-pcp = %EVR
Requires: python3-module-psycopg2
Requires: python3-module-libvirt
Requires: python3-module-lxml
Requires: python3-module-rtslib
Requires: python3-module-requests

%description pmdas
This package contains the PCP performance metrics domain agent (PMDA)
to collect metrics from various services

%package zeroconf
BuildArch: noarch
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Zeroconf Package

%description zeroconf
This package contains configuration tweaks and files to increase metrics
gathering frequency, several extended pmlogger configurations, as well as
automated pmie diagnosis, alerting and self-healing for the localhost.
A cron script also writes daily performance summary reports similar to
those written by sysstat.

# python3-module-pcp. This is the PCP library bindings for python3.
%package -n python3-module-pcp
License: GPLv2+
Group: Development/Python3
Summary: Performance Co-Pilot (PCP) Python3 bindings and documentation

%description -n python3-module-pcp
This python PCP module contains the language bindings for
Performance Metric API (PMAPI) monitor tools and Performance
Metric Domain Agent (PMDA) collector tools written in Python3.

# pcp-doc package
%package doc
BuildArch: noarch
License: GPLv2+ and CC-BY-SA-3.0
Group: Monitoring
Summary: Documentation and tutorial for the Performance Co-Pilot

%description doc
Documentation and tutorial for the Performance Co-Pilot
Performance Co-Pilot (PCP) provides a framework and services to support
system-level performance monitoring and performance management.

The pcp-doc package provides useful information on using and
configuring the Performance Co-Pilot (PCP) toolkit for system
level performance management.  It includes tutorials, HOWTOs,
and other detailed documentation about the internals of core
PCP utilities and daemons, and the PCP graphical tools.

%prep
%setup -q
%patch0 -p1

%build

# Rename the libpcp library to libpcopilot in all files, 
# because the pcp library is already in the pgpool-II package
grep -rl '\(libpcp.*\|lpcp.*\|Extension\)' | xargs sed -i \
-e 's/libpcp/libpcopilot/g' \
-e 's/lpcp/lpcopilot/g' \
-e '/libraries/s/pcp/pcopilot/g'

# Rename file and folder names from libpcp to libpcopilot
find -type f,d -name 'libpcp*' | sort -r | sed 'p;s:\(.*\)libpcp:\1libpcopilot:' | xargs -n2 mv

mv src/include/pcp src/include/pcopilot
sed -i -e 's:include/pcp/:include/pcopilot/:g' configure.ac 
sed -i -e 's:SUBDIRS = pcp:SUBDIRS = pcopilot:' src/include/GNUmakefile
grep -rl '/include/pcp' | xargs sed -i \
-e '/PCP_INC_DIR/s:/include/pcp:/include/pcopilot:g' \
-e 's:/include/pcp/:/include/pcopilot/:g' \
-e '/-I/s:/include/pcp:/include/pcopilot:g' \
-e '/-I/s:$(TOPDIR)/src/include/pcp:$(TOPDIR)/src/include/pcopilot:g' \
-e 's:$(TOPDIR)/src/include/pcp/:$(TOPDIR)/src/include/pcopilot/:g' 

grep -rl '\($INCDIR/pcp/\|$includedir/pcp\)' | xargs sed -i \
-e 's:$INCDIR/pcp/:$INCDIR/pcopilot/:g' \
-e 's:$includedir/pcp:$includedir/pcopilot:g'

grep -rl '\(<pcp/\|"pcp/\|find_library\)' | xargs sed -i \
-e '/include/s/pcp/pcopilot/g' \
-e 's:@<pcp/pmapi.h>@:@<pcopilot/pmapi.h>@:g' \
-e '/find_library/s/pcp/pcopilot/g'

# Change path for ALTLinux
sed -i \
-e 's_/etc/apache2:/etc/httpd_/etc/httpd2_' \
-e 's_log/apache2_log/httpd2_' \
-e 's/FTPPATH:-$_logdir/FTPPATH:-\/var\/ftp/' src/pmdas/weblog/server.sh

%autoreconf

# due to @b78cbe17d and @8ab231919
sed -i \
-e '/undef HAVE_32BIT_LONG/d' \
-e '/undef HAVE_32BIT_PTR/d' \
-e '/undef HAVE_64BIT_LONG/d' \
-e '/undef HAVE_64BIT_PTR/d' \
-e '/undef PM_SIZEOF_SUSECONDS_T/d' \
-e '/undef PM_SIZEOF_TIME_T/d' \
src/include/pcopilot/config.h.in

%configure \
	--with-rcdir=%_initddir \
	--with-rundir=/run/pcp \
	--with-python3=yes \
	--with-selinux=no \
	--with-pmdapodman=no \
	--with-perfevent=no \
	--with-pmdabcc=no \
	--with-infiniband=no \
	--with-dstat-symlink=no \
	--with-pmdanutcracker=no \
	--with-pmdajson=no \
	--with-python=no \
	--with-webapps=no \
	--with-pmdasnmp=no \
	--with-user=%_pseudouser_user \
	--with-group=%_pseudouser_group 

%make_build default_pcp

%install
export NO_CHOWN=true DIST_ROOT=%buildroot
%make install_pcp
# strange source place(tests' dir) for runtime Perl module
install -D ./qa/slurm/Slurm/Hostlist.pm \
    %buildroot%perl_vendorarch/Slurm/Hostlist.pm
install ./qa/slurm/Slurm.pm %buildroot%perl_vendorarch/

chrpath -d \
    %buildroot%perl_vendor_autolib/PCP/LogImport/LogImport.so \
    %buildroot%perl_vendor_autolib/PCP/MMV/MMV.so \
    %buildroot%perl_vendor_autolib/PCP/PMDA/PMDA.so

mv %buildroot%_sharedstatedir/pcp/pmdas/activemq/*.pm \
    %buildroot%perl_vendorarch/PCP/
PCP_GUI='pmchart|pmconfirm|pmdumptext|pmmessage|pmquery|pmsnap|pmtime'

# Fix stuff we do/don't want to ship
rm %buildroot%_libdir/*.a

rm %buildroot%_bindir/sheet2pcp

# remove {config,platform}sz.h as these are not multilib friendly.
rm %buildroot%_includedir/pcopilot/configsz.h
rm %buildroot%_includedir/pcopilot/platformsz.h

rm -r %buildroot%_sharedstatedir/pcp/config/pmchart/
rm -r %buildroot%_datadir/pcp-gui/pixmaps/

touch %buildroot/%_pmnsdir/root \
        %buildroot/%_pmnsdir/root.prev \
        %buildroot/%_pmnsdir/stdpmid
chmod 644 %buildroot/%_pmnsdir/root \
        %buildroot/%_pmnsdir/root.prev \
        %buildroot/%_pmnsdir/stdpmid

%pre
getent group %_pseudouser_group >/dev/null || groupadd -r %_pseudouser_group
getent passwd %_pseudouser_user >/dev/null || \
  useradd -c "Performance Co-Pilot" -g %_pseudouser_group -d %_pseudouser_home -M -r -s /sbin/nologin %_pseudouser_user

%post manager
%post_service pmmgr

%post zeroconf
# increase default pmlogger recording frequency
sed -i 's/^\#\ PMLOGGER_INTERVAL.*/PMLOGGER_INTERVAL=10/g' \
    "%_sysconfdir/sysconfig/pmlogger"

%post_service pmcd
%post_service pmlogger
%post_service pmie

%post
PCP_LOG_DIR=%_logsdir
PCP_PMNS_DIR=%_pmnsdir
# restore saved configs, if any
test -s "$PCP_LOG_DIR/configs.sh" && source "$PCP_LOG_DIR/configs.sh"
rm -f $PCP_LOG_DIR/configs.sh

touch "$PCP_PMNS_DIR/.NeedRebuild"
chmod 644 "$PCP_PMNS_DIR/.NeedRebuild"
%post_service pmproxy

cd $PCP_PMNS_DIR && ./Rebuild -s && rm -f .NeedRebuild

%files
%doc CHANGELOG COPYING INSTALL.md README.md

%_pmdasdir/jbd2/
%_pmdasdir/kvm/
%_pmdasdir/linux/
%_pmdasdir/mmv/
%_pmdasdir/pipe/
%_pmdasdir/pmcd/
%_pmdasdir/proc/
%_pmdasdir/root/
%_pmdasdir/xfs/
%_bindir/dbpmda
%_bindir/pcp
%_bindir/pcp2csv
%_bindir/pmafm
%_bindir/pmdate
%_bindir/pmdiff
%_bindir/pmdumplog
%_bindir/pmevent
%_bindir/pmfind
%_bindir/pmgenmap
%_bindir/pmie
%_bindir/pmie2col
%_bindir/pmieconf
%_bindir/pminfo
%_bindir/pmjson
%_bindir/pmlc
%_bindir/pmlogcheck
%_bindir/pmlogconf
%_bindir/pmlogextract
%_bindir/pmlogger
%_bindir/pmloglabel
%_bindir/pmlogmv
%_bindir/pmlogsize
%_bindir/pmlogsummary
%_bindir/pmprobe
%_bindir/pmpython
%_bindir/pmsocks
%_bindir/pmstat
%_bindir/pmstore
%_bindir/pmtrace
%_bindir/pmval
%dir %_libexecdir/pcp
%dir %_libexecdir/pcp/bin
%_libexecdir/pcp/bin/chkhelp
%_libexecdir/pcp/bin/discover
%_libexecdir/pcp/bin/install-sh
%_libexecdir/pcp/bin/mkaf
%_libexecdir/pcp/bin/newhelp
%_libexecdir/pcp/bin/pcp-python
%_libexecdir/pcp/bin/pcp-summary
%_libexecdir/pcp/bin/pcp-vmstat
%_libexecdir/pcp/bin/pmcd
%_libexecdir/pcp/bin/pmcd_wait
%_libexecdir/pcp/bin/pmconfig
%_libexecdir/pcp/bin/pmcpp
%_libexecdir/pcp/bin/pmgetopt
%_libexecdir/pcp/bin/pmhostname
%_libexecdir/pcp/bin/pmie_check
%_libexecdir/pcp/bin/pmie_daily
%_libexecdir/pcp/bin/pmie_email
%_libexecdir/pcp/bin/pmiestatus
%_libexecdir/pcp/bin/pmlock
%_libexecdir/pcp/bin/pmlogconf
%_libexecdir/pcp/bin/pmlogconf-setup
%_libexecdir/pcp/bin/pmlogextract
%_libexecdir/pcp/bin/pmlogger
%_libexecdir/pcp/bin/pmlogger_check
%_libexecdir/pcp/bin/pmlogger_daily
%_libexecdir/pcp/bin/pmlogger_merge
%_libexecdir/pcp/bin/pmlogger_rewrite
%_libexecdir/pcp/bin/pmlogreduce
%_libexecdir/pcp/bin/pmlogrewrite
%_libexecdir/pcp/bin/pmnewlog
%_libexecdir/pcp/bin/pmnsadd
%_libexecdir/pcp/bin/pmnsdel
%_libexecdir/pcp/bin/pmnsmerge
%_libexecdir/pcp/bin/pmpause
%_libexecdir/pcp/bin/pmpost
%_libexecdir/pcp/bin/pmproxy
%_libexecdir/pcp/bin/pmsignal
%_libexecdir/pcp/bin/pmsleep
%_libexecdir/pcp/bin/pmwtf
%_libexecdir/pcp/bin/telnet-probe
%_logconfdir/statsd
%_logconfdir/apache
%_logconfdir/cpu
%_logconfdir/disk
%_logconfdir/elasticsearch
%_logconfdir/filesystem
%_logconfdir/gfs2
%_logconfdir/kernel
%_logconfdir/kvm
%_logconfdir/libvirt
%_logconfdir/mailq
%_logconfdir/memcache
%_logconfdir/memory
%_logconfdir/mmv
%_logconfdir/netfilter
%_logconfdir/networking
%_logconfdir/nginx
%_logconfdir/oracle
%_logconfdir/platform
%_logconfdir/sgi
%_logconfdir/shping
%_logconfdir/sqlserver
%_logconfdir/storage
%_logconfdir/tools
%_logconfdir/v1.0
%_logconfdir/zimbra

%dir %_confdir
%dir %_pmdasdir
%dir %_logconfdir
%dir %_datadir/pcp
%dir %_sharedstatedir/pcp
%dir %_sharedstatedir/pcp/config
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_tempsdir
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_tempsdir/pmie
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_tempsdir/pmlogger
%dir %attr(0700,root,root) %_tempsdir/pmcd

%dir %_datadir/pcp/lib
%_datadir/pcp/lib/ReplacePmnsSubtree
%_datadir/pcp/lib/bashproc.sh
%_datadir/pcp/lib/lockpmns
%_datadir/pcp/lib/pmdaproc.sh
%_datadir/pcp/lib/utilproc.sh
%_datadir/pcp/lib/rc-proc.sh
%_datadir/pcp/lib/rc-proc.sh.minimal
%_datadir/pcp/lib/unlockpmns

%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir
%attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir/pmcd
%attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir/pmlogger
%attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir/pmie
%attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir/pmproxy
%_sharedstatedir/pcp/pmns
%_initddir/pcp
%_initddir/pmcd
%_initddir/pmlogger
%_initddir/pmie
%_initddir/pmproxy
%_unitdir/pmcd.service
%_unitdir/pmlogger.service
%_unitdir/pmie.service
%_unitdir/pmproxy.service
%_unitdir/pmlogger_check.service
%_unitdir/pmlogger_check.timer
%_unitdir/pmlogger_daily.service
%_unitdir/pmlogger_daily.timer
%_unitdir/pmlogger_daily-poll.service
%_unitdir/pmlogger_daily-poll.timer
%_unitdir/pmie_check.service
%_unitdir/pmie_check.timer
%_unitdir/pmie_daily.service
%_unitdir/pmie_daily.timer
%config(noreplace) %_sysconfdir/sysconfig/pmie_timers
%config(noreplace) %_sysconfdir/sysconfig/pmlogger_timers
%config(noreplace) %_sysconfdir/sasl2/pmcd.conf
%config(noreplace) %_sysconfdir/sysconfig/pmlogger
%config(noreplace) %_sysconfdir/sysconfig/pmproxy
%config(noreplace) %_sysconfdir/sysconfig/pmcd
%config %_sysconfdir/pcp.env
%dir %_confdir/labels
%dir %_confdir/pmcd
%config(noreplace) %_confdir/pmcd/pmcd.conf
%config(noreplace) %_confdir/pmcd/pmcd.options
%config(noreplace) %_confdir/pmcd/rc.local
%dir %_confdir/pmproxy
%config(noreplace) %_confdir/pmproxy/pmproxy.options
%config(noreplace) %_confdir/pmproxy/pmproxy.conf
%dir %_confdir/pmie
%dir %_confdir/pmie/control.d
%config(noreplace) %_confdir/pmie/control
%config(noreplace) %_confdir/pmie/control.d/local
%dir %_confdir/pmlogger
%dir %_confdir/pmlogger/control.d
%config(noreplace) %_confdir/pmlogger/control
%config(noreplace) %_confdir/pmlogger/control.d/local
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_confdir/nssdb
%dir %_confdir/discover
%config(noreplace) %_confdir/discover/pcp-kube-pods.conf

%ghost %dir %attr(0775,%_pseudouser_user,%_pseudouser_group) /run/pcp
%_sharedstatedir/pcp/config/pmafm
%exclude %_sharedstatedir/pcp/config/pmafm/pcp-gui
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_sharedstatedir/pcp/config/pmie
%_sharedstatedir/pcp/config/pmie/*
%_sharedstatedir/pcp/config/pmieconf
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_sharedstatedir/pcp/config/pmlogger
%_sharedstatedir/pcp/config/pmlogger/*
%_sharedstatedir/pcp/config/pmlogrewrite
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_sharedstatedir/pcp/config/pmda

%dir %_datadir/bash-completion/
%dir %_datadir/bash-completion/completions
%_datadir/bash-completion/completions/*
%dir %_datadir/zsh/
%dir %_datadir/zsh/site-functions/
%_datadir/zsh/site-functions/_pcp

%_bindir/pmiostat
%_bindir/pmrep
%_libexecdir/pcp/bin/pcp-atop
%_libexecdir/pcp/bin/pcp-atopsar
%_libexecdir/pcp/bin/pcp-dmcache
%_libexecdir/pcp/bin/pcp-dstat
%_libexecdir/pcp/bin/pcp-free
%_libexecdir/pcp/bin/pcp-iostat
%_libexecdir/pcp/bin/pcp-ipcs
%_libexecdir/pcp/bin/pcp-lvmcache
%_libexecdir/pcp/bin/pcp-mpstat
%_libexecdir/pcp/bin/pcp-numastat
%_libexecdir/pcp/bin/pcp-pidstat
%_libexecdir/pcp/bin/pcp-shping
%_libexecdir/pcp/bin/pcp-tapestat
%_libexecdir/pcp/bin/pcp-uptime
%_libexecdir/pcp/bin/pcp-verify
%dir %_confdir/dstat
%dir %_confdir/pmrep
%config(noreplace) %_confdir/dstat/*
%config(noreplace) %_confdir/pmrep/*

%files zeroconf
%_libexecdir/pcp/bin/pmlogger_daily_report
%_unitdir/pmlogger_daily_report.service
%_unitdir/pmlogger_daily_report.timer
%_unitdir/pmlogger_daily_report-poll.service
%_unitdir/pmlogger_daily_report-poll.timer
%_sharedstatedir/pcp/config/pmlogconf/zeroconf

%files conf
%dir %_includedir/pcopilot
%dir %_localstatedir/lib/pcp
%dir %_localstatedir/lib/pcp/config
%_includedir/pcopilot/builddefs
%_includedir/pcopilot/buildrules
%config %_sysconfdir/pcp.conf
%dir %_sharedstatedir/pcp/config/derived
%config %_sharedstatedir/pcp/config/derived/*

%files -n libpcopilot
%_libdir/libpcopilot.so.3
%_libdir/libpcopilot_gui.so.2
%_libdir/libpcopilot_mmv.so.1
%_libdir/libpcopilot_pmda.so.3
%_libdir/libpcopilot_trace.so.2
%_libdir/libpcopilot_import.so.1
%_libdir/libpcopilot_web.so.1

%files -n libpcopilot-devel
%_libdir/libpcopilot.so
%_libdir/libpcopilot_gui.so
%_libdir/libpcopilot_mmv.so
%_libdir/libpcopilot_pmda.so
%_libdir/libpcopilot_trace.so
%_libdir/libpcopilot_import.so
%_libdir/libpcopilot_web.so
%_libdir/pkgconfig/libpcopilot.pc
%_libdir/pkgconfig/libpcopilot_pmda.pc
%_libdir/pkgconfig/libpcopilot_import.pc
%_includedir/pcopilot/*.h

%files devel
%_bindir/genpmda
%_bindir/pmclient
%_bindir/pmclient_fg
%_bindir/pmdbg
%_bindir/pmerr
%_datadir/pcp/examples
# PMDAs that ship src and are not for production use
# straight out-of-the-box, for devel or QA use only.
%_pmdasdir/simple
%_pmdasdir/sample
%_pmdasdir/trivial
%_pmdasdir/txmon

%files manager
%_initddir/pmmgr
%_unitdir/pmmgr.service
%_libexecdir/pcp/bin/pmmgr
%attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir/pmmgr
%config(missingok,noreplace) %_confdir/pmmgr

%files import-tools
%_bindir/sar2pcp
%_bindir/iostat2pcp
%_bindir/mrtg2pcp
%_bindir/ganglia2pcp
%_bindir/collectl2pcp

%files pmdas
%_pmdasdir/activemq
%dir %perl_vendorarch/PCP
%dir %perl_vendor_autolib/PCP
%dir %perl_vendorarch/Slurm
%perl_vendor_archlib/PCP/*
%exclude %perl_vendorarch/PCP/PMDA.pm
%exclude %perl_vendorarch/PCP/MMV.pm
%exclude %perl_vendorarch/PCP/server.pl
%exclude %perl_vendorarch/PCP/LogImport.pm
%perl_vendorarch/Slurm/*
%perl_vendorarch/Slurm.pm
%_pmdasdir/mssql
%_pmdasdir/netcheck
%_pmdasdir/bonding
%_pmdasdir/bind2
%_pmdasdir/dbping
%_pmdasdir/ds389log
%_pmdasdir/ds389
%_pmdasdir/elasticsearch
%_pmdasdir/gpfs
%_pmdasdir/gpsd
%_pmdasdir/docker
%_pmdasdir/lustre
%_pmdasdir/lustrecomm
%_pmdasdir/memcache
%_pmdasdir/named
%_pmdasdir/netfilter
%_pmdasdir/news
%_pmdasdir/nginx
%_pmdasdir/nfsclient
%_pmdasdir/oracle
%_pmdasdir/pdns
%_pmdasdir/postfix
%_pmdasdir/redis
%_pmdasdir/rsyslog
%_pmdasdir/samba
%_pmdasdir/slurm
%_pmdasdir/zimbra
%_pmdasdir/dm
%_pmdasdir/gluster
%_pmdasdir/zswap
%_pmdasdir/unbound
%_pmdasdir/mic
%_pmdasdir/haproxy
%_pmdasdir/lmsensors
%_pmdasdir/apache
%_pmdasdir/bash
%_pmdasdir/cifs
%_pmdasdir/cisco
%_pmdasdir/gfs2
%_pmdasdir/logger
%_pmdasdir/mailq
%_pmdasdir/mounts
%_pmdasdir/nvidia
%_pmdasdir/roomtemp
%_pmdasdir/rpm
%_pmdasdir/sendmail
%_pmdasdir/shping
%_pmdasdir/smart
%_pmdasdir/summary
%_pmdasdir/systemd
%_pmdasdir/trace
%_pmdasdir/weblog

%files export-tools
%_bindir/pcp2graphite
%_bindir/pcp2json
%_bindir/pcp2spark
%_bindir/pcp2xml
%_bindir/pcp2zabbix
%_libdir/zabbix
%dir %_sysconfdir/zabbix
%dir %_sysconfdir/zabbix/zabbix_agentd.d/
%_sysconfdir/zabbix/zabbix_agentd.d/zbxpcp.conf

%files -n perl-PCP-common
%dir %perl_vendorlib/PCP
%dir %perl_vendorarch/PCP
%dir %perl_vendor_autolib/PCP

%files -n perl-PCP-PMDA
%dir %perl_vendor_autolib/PCP/PMDA
%perl_vendorarch/PCP/PMDA.pm
%perl_vendor_autolib/PCP/PMDA/PMDA.so

%files -n perl-PCP-MMV
%dir %perl_vendor_autolib/PCP/MMV
%perl_vendorarch/PCP/MMV.pm
%perl_vendorarch/PCP/server.pl
%perl_vendor_autolib/PCP/MMV/MMV.so

%files -n perl-PCP-LogImport
%dir %perl_vendor_autolib/PCP/LogImport
%perl_vendorarch/PCP/LogImport.pm
%perl_vendor_autolib/PCP/LogImport/LogImport.so

%files -n perl-PCP-LogSummary
%perl_vendorlib/PCP/LogSummary.pm
%perl_vendorlib/PCP/exceldemo.pl
%perl_vendorlib/PCP/extract.pl

%files -n python3-module-pcp
%python3_sitelibdir/*

%files doc
%_man1dir/*
%_man3dir/*
%_man5dir/*
%_defaultdocdir/pcp-doc/
%dir %_datadir/pcp/
%dir %_datadir/pcp/demos/
%dir %_datadir/pcp/demos/tutorials
%_datadir/pcp/demos/mmv
%_datadir/pcp/demos/pmclient
%_datadir/pcp/demos/procmemstat
%_datadir/pcp/demos/trace
%_datadir/pcp/demos/tutorials/*.tar.gz

%changelog
* Wed Sep 18 2019 Mikhail Chernonog <snowmix@altlinux.org> 5.0.2-alt1
- Initial build for Sisyphus
