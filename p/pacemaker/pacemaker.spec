%define _rundir /run
%define gname haclient
%define uname hacluster
%define _libexecdir /usr/libexec

%add_findreq_skiplist */ocf/resource.d/.isolation/*
%add_findreq_skiplist */ocf/resource.d/pacemaker/*

%def_disable doc

Name:    pacemaker
Summary: Scalable High-Availability cluster resource manager
Version: 2.0.3
Release: alt2
License: GPLv2+ and LGPLv2+
Url:     http://www.clusterlabs.org
# VCS:   https://github.com/ClusterLabs/pacemaker.git
Group:   System/Servers
Source:  %name-%version.tar
Patch:   %name-%version-alt.patch

Provides: pcmk-cluster-manager
Requires: corosync
Requires: resource-agents
Requires: lib%name = %version-%release
Requires(pre): %name-cli = %version-%release

BuildRequires(pre): rpm-build-python3
BuildRequires: /proc
BuildRequires: glib2-devel libxml2-devel libxslt-devel libuuid-devel systemd-devel libdbus-devel  perl(Pod/Text.pm)
BuildRequires: python3-devel gcc-c++ bzlib-devel libpam-devel
BuildRequires: libqb-devel > 0.11.0 libgnutls-devel libltdl-devel libgio-devel
BuildRequires: libncurses-devel libssl-devel libselinux-devel docbook-style-xsl
BuildRequires: help2man xsltproc
BuildRequires: libesmtp-devel libsensors3-devel libnet-snmp-devel libopenipmi-devel libservicelog-devel
BuildRequires: libcorosync-devel
%{?_enable_doc:BuildRequires: publican inkscape asciidoc}

%description
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

It supports "n-node" clusters with significant capabilities for
managing resources and dependencies.

It will run scripts at initialization, when machines go up or down,
when related resources fail and can be configured to periodically check
resource health.

Available rpmbuild rebuild options:
  --with(out) : heartbeat cman corosync doc publican snmp esmtp pre_release

%package cli
License: GPLv2+ and LGPLv2+
Summary: Command line tools for controlling Pacemaker clusters
Group: System/Servers
Requires: perl-DateTime-Format-DateParse
Requires: procps-ng
Requires: psmisc

%description cli
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

The %name-cli package contains command line tools that can be used
to query and control the cluster from machines that may, or may not,
be part of the cluster.

%package -n lib%name
License: GPLv2+ and LGPLv2+
Summary: Core Pacemaker libraries
Group: System/Servers
Requires: %name-schemas = %version-%release

%description -n lib%name
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

The lib%name package contains shared libraries needed for cluster
nodes and those just running the CLI tools.

%package remote
License: GPLv2+ and LGPLv2+
Summary: Pacemaker remote daemon for non-cluster nodes
Group: System/Servers

Provides: pcmk-cluster-manager
Requires: resource-agents
Requires: lib%name = %version-%release
Requires: %name-cli = %version-%release

%description remote
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

The %name-remote package contains the Pacemaker Remote daemon
which is capable of extending pacemaker functionality to remote
nodes not running the full corosync/cluster stack.

%package -n lib%name-devel
License: GPLv2+ and LGPLv2+
Summary: Pacemaker development package
Group: Development/C
Requires: lib%name = %version-%release
Requires: libqb-devel libuuid-devel
Requires: libxml2-devel libxslt-devel bzlib-devel glib2-devel
Requires: libcorosync-devel

%description -n lib%name-devel
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

The lib%name-devel package contains headers and shared libraries
for developing tools for Pacemaker.

%package cts
License: GPLv2+ and LGPLv2+
Summary: Test framework for cluster-related technologies like Pacemaker
Group: System/Servers
Requires: resource-agents
Requires: procps-ng
Requires: %name-cli = %version-%release
Requires: psmisc
BuildArch: noarch

%description cts
Test framework for cluster-related technologies like Pacemaker

%package doc
License: GPLv2+ and LGPLv2+
Summary: Documentation for Pacemaker
Group: System/Servers
BuildArch: noarch

%description doc
Documentation for Pacemaker.

Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Linux-HA (Heartbeat) and/or Corosync.

%package schemas
License: GPLv2+
Summary: Schemas and upgrade stylesheets for Pacemaker
Group: System/Servers
BuildArch: noarch

%description   schemas
Schemas and upgrade stylesheets for Pacemaker

Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	PYTHON=/usr/bin/python3 \
	--disable-fatal-warnings	\
	--disable-static	\
	--with-profiling	\
	--with-gcov		\
	--with-acl		\
	--with-ais		\
	--with-corosync		\
	--with-cs-quorum	\
	--with-stonithd		\
	--enable-thread-safe	\
	--with-initdir=%_initdir	\
	--enable-systemd	\
	--disable-upstart	\
	--with-systemdsystemunitdir=%_unitdir	\
	--with-runstatedir=%_rundir	\
	--localstatedir=%_var	\
    --with-nagios-plugin-dir=%_prefix/lib/nagios/plugins \
	--with-daemon-user=%uname	\
	--with-daemon-group=%gname	\
	--with-version=%version-%release

subst 's|/usr/bin/help2man|/usr/bin/help2man --no-discard-stderr|g' tools/Makefile

%make_build V=1

%install
%makeinstall_std

mkdir -p %buildroot%_var/lib/pacemaker/cores
install -D -m 644 daemons/pacemakerd/pacemaker.sysconfig %buildroot%_sysconfdir/sysconfig/pacemaker
install -D -m 755 pacemaker.init %buildroot%_initdir/pacemaker

# Copy configuration for pacemaker_remote and use it in init script
install -D -m 644 daemons/pacemakerd/pacemaker.sysconfig %buildroot%_sysconfdir/sysconfig/pacemaker_remote
subst 's|/etc/sysconfig/pacemaker|/etc/sysconfig/pacemaker_remote|' %buildroot%_initdir/pacemaker_remote
install -D -m 755 pacemaker_remote.init %buildroot%_initdir/pacemaker_remote

# These are not actually scripts
find %buildroot -name '*.xml' -type f -print0 | xargs -0 chmod a-x
find %buildroot -name '*.xsl' -type f -print0 | xargs -0 chmod a-x
find %buildroot -name '*.rng' -type f -print0 | xargs -0 chmod a-x

# Don't package static libs
find %buildroot -name '*.a' -type f -print0 | xargs -0 rm -f
find %buildroot -name '*.la' -type f -print0 | xargs -0 rm -f

# Do not package this either
rm -rf %buildroot%_datadir/pacemaker/tests/cts

GCOV_BASE=%buildroot/%_var/lib/pacemaker/gcov
mkdir -p $GCOV_BASE
find . -name '*.gcno' -type f | while read F ; do
        D=`dirname $F`
        mkdir -p ${GCOV_BASE}/$D
        cp $F ${GCOV_BASE}/$D
done


%pre cli
groupadd -f -r %gname ||:
getent passwd %uname >/dev/null || useradd -r -g %gname -s /sbin/nologin -c "cluster user" %uname ||:

%post cli
%post_service crm_mon

%preun cli
%preun_service crm_mon

%post
%post_service %name

%preun
%preun_service %name

%post -n %name-remote
%post_service pacemaker_remote

%preun -n %name-remote
%preun_service pacemaker_remote

%files
%doc COPYING ChangeLog README.markdown
%doc %_datadir/pacemaker/alerts
%exclude %_libexecdir/pacemaker/cts-log-watcher
%exclude %_libexecdir/pacemaker/cts-support
%exclude %_sbindir/pacemaker-remoted
%exclude %_sbindir/pacemaker_remoted
%config(noreplace) %_sysconfdir/sysconfig/pacemaker
%_sbindir/pacemakerd
%_initdir/pacemaker
%_unitdir/pacemaker.service
%_logrotatedir/%name
%_libexecdir/pacemaker/*
%_sbindir/fence_legacy
%_sbindir/notifyServicelogEvent
%_sbindir/ipmiservicelogd
%_man7dir/*.7*
%_man8dir/pacemakerd.*
%dir %attr (750, %uname, %gname) %_var/lib/pacemaker/cib
%dir %attr (750, %uname, %gname) %_var/lib/pacemaker/pengine
/usr/lib/ocf/resource.d/pacemaker/controld
/usr/lib/ocf/resource.d/pacemaker/remote

%files cli
%_sbindir/attrd_updater
%_sbindir/cibadmin
%_sbindir/crm_attribute
%_sbindir/crm_diff
%_sbindir/crm_error
%_sbindir/crm_failcount
%_sbindir/crm_master
%_sbindir/crm_mon
%_unitdir/crm_mon.service
%_sbindir/crm_node
%_sbindir/crm_standby
%_sbindir/crmadmin
%_sbindir/iso8601
%_sbindir/crm_shadow
%_sbindir/crm_simulate
%_sbindir/crm_report
%_sbindir/crm_resource
%_sbindir/crm_rule
%_sbindir/crm_ticket
%_sbindir/crm_verify
%_sbindir/stonith_admin
%_man8dir/*.8*
%exclude %_man8dir/pacemakerd.*
%exclude %_man8dir/pacemaker-remoted.*

%_datadir/pacemaker/report.collector
%_datadir/pacemaker/report.common
%_datadir/snmp/mibs/PCMK-MIB.txt

%dir /usr/lib/ocf
%dir /usr/lib/ocf/resource.d
/usr/lib/ocf/resource.d/pacemaker
%exclude /usr/lib/ocf/resource.d/pacemaker/controld
%exclude /usr/lib/ocf/resource.d/pacemaker/remote

%dir %attr (750, %uname, %gname) %_var/lib/pacemaker
%dir %attr (750, %uname, %gname) %_var/lib/pacemaker/cores
%dir %attr (750, %uname, %gname) %_var/lib/pacemaker/blackbox
%dir %attr (770, %uname, %gname) %_var/log/pacemaker
%dir %attr (770, %uname, %gname) %_var/log/pacemaker/bundles

%files -n lib%name
%_libdir/*.so.*

%files remote
%config(noreplace) %_sysconfdir/sysconfig/pacemaker_remote
%_initdir/pacemaker_remote
%_unitdir/pacemaker_remote.service
%_sbindir/pacemaker-remoted
%_sbindir/pacemaker_remoted
%_man8dir/pacemaker-remoted.*

%files doc
%doc %_docdir/%name

%files cts
%python3_sitelibdir_noarch/cts
%_datadir/pacemaker/tests
%_libexecdir/pacemaker/cts-log-watcher
%_libexecdir/pacemaker/cts-support

%files -n lib%name-devel
%_includedir/pacemaker
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/pkgconfig/*.pc

%files schemas
%dir %_datadir/pacemaker
%_datadir/pacemaker/*.rng
%_datadir/pacemaker/*.xsl
%_datadir/pacemaker/api

%changelog
* Sat Apr 04 2020 Alexey Shabalin <shaba@altlinux.org> 2.0.3-alt2
- define %%_libexecdir as /usr/libexec
- move attrd_updater, crm_attribute, crm_master to pacemaker-cli

* Wed Dec 18 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.3-alt1
- New version.
- disable build doc (error build publican on i586)

* Sun Jun 16 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.2-alt1
- New version.

* Wed Mar 06 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.1-alt1
- New version.
- build with python3
- move schemas to sepatated package

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.18-alt1
- New version.

* Tue Oct 03 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.17-alt2
- Build without cluster-glue (ALT #33944)

* Thu Jul 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.17-alt1
- New version

* Thu Jun 29 2017 Denis Medvedev <nbr@altlinux.org> 1.1.16-alt3
- Fix initscript,(ALT #33598).

* Wed Apr 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.1.16-alt2
- enabled stonithd

* Sat Dec 24 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.16-alt1
- New version

* Fri Sep 23 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.15-alt3
- do not package fence files
- add_findreq_skiplist for resource files

* Wed Sep 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.15-alt2
- build with systemd support
- update sysv init script

* Mon Jun 27 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.15-alt1
- New version

* Fri Jan 22 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.14-alt2
- Fix initscripts and paths

* Thu Jan 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.14-alt1
- New version

* Sat Oct 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.13-alt1
- New version

* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt4
- NMU: added missing Pod dependencies

* Thu Aug 15 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.10-alt3
- Fix initscript

* Mon Aug 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.10-alt2
- New version

* Mon May 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.10-alt1.rc3
- New RC

* Sat Apr 06 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.9-alt2.git.132019bd
- New version

* Thu Mar 21 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.9-alt1
- Build for ALT
