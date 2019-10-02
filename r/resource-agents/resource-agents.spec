%define _unpackaged_files_terminate_build 1
%define _localstatedir %_var
%def_without cluster_glue

Name: resource-agents
Summary: Open Source HA Reusable Cluster Resource Scripts
Version: 4.3.0
Release: alt1
License: GPLv2+ and LGPLv2+
Url: https://github.com/ClusterLabs/resource-agents
Group: System/Base
Source: %name-%version.tar

Provides: heartbeat = %version
Obsoletes: heartbeat < 2.1.4
Conflicts: heartbeat < 2.1.4

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel xsltproc libxslt-devel glib2-devel which docbook-style-xsl docbook-dtds libnet2-devel 
%{?_with_cluster_glue:BuildRequires: libcluster-glue-devel}
BuildRequires: perl-podlators perl-Socket6 perl-libwww perl-IO-Socket-INET6 perl-Net-Ping perl-MailTools
BuildRequires: systemd-devel
BuildRequires: python3-module-jsonlib

Requires: linux-ha-common

%add_findreq_skiplist */ocf/lib/heartbeat/*
%add_findreq_skiplist */ocf/resource.d/heartbeat/*
%add_findreq_skiplist */ocf/resource.d/redhat/*
%add_findreq_skiplist %_datadir/cluster/*
%add_findreq_skiplist %_datadir/cluster/utils/*

%description
A set of scripts to interface with several services to operate in a
High Availability environment for both Pacemaker and rgmanager
service managers.

%package CTDB
Group: System/Base
Requires: %name = %version-%release
Summary: resource agent manages CTDB
BuildArch: noarch

%description CTDB
This resource agent manages CTDB, allowing one to use Clustered Samba in a
Linux-HA/Pacemaker cluster.  You need a shared filesystem (e.g. OCFS2) on
which the CTDB lock will be stored.  Create /etc/ctdb/nodes containing a list
of private IP addresses of each node in the cluster, then configure this RA
as a clone.  To have CTDB manage Samba, set ctdb_manages_samba="yes".
Note that this option will be deprecated in future, in favour of configuring
a separate Samba resource.

%package iSCSI
Group: System/Base
Requires: %name = %version-%release
Summary: resource agent manages iSCSI
BuildArch: noarch

%description iSCSI
Manages iSCSI targets. An iSCSI target is a collection of SCSI Logical
Units (LUs) exported via a daemon that speaks the iSCSI protocol.

%package tomcat
Group: System/Base
Requires: %name = %version-%release
Summary: resource agent manages Tomcat
BuildArch: noarch

%description tomcat
Manages Tomcat

%package fio
Group: System/Base
Requires: %name = %version-%release
Summary: resource agent manages fio
BuildArch: noarch

%description fio
fio is a generic I/O load generator. This RA allows start/stop of fio
instances to simulate load on a cluster without configuring complex
services.

%package libvirt
Group: System/Base
Requires: %name = %version-%release
Summary: resource agent manages libvirtd
BuildArch: noarch

%description libvirt
Resource agent for a virtual domain (a.k.a. domU, virtual machine,
virtual environment etc., depending on context) managed by libvirtd.

%package lxc
Group: System/Base
Requires: %name = %version-%release
Requires: lxc
Summary: resource agent manages lxc
BuildArch: noarch

%description lxc
Allows LXC containers to be managed by the cluster.
If the container is running "init" it will also perform an orderly shutdown.
It is 'assumed' that the 'init' system will do an orderly shudown if presented with a 'kill -PWR' signal.
On a 'sysvinit' this would require the container to have an inittab file containing "p0::powerfail:/sbin/init 0"
I have absolutly no idea how this is done with 'upstart' or 'systemd', YMMV if your container is using one of them.

%package nfs
Group: System/Base
Requires: %name = %version-%release
Summary: resource agent manage NFS
BuildArch: noarch

%description nfs
Nfs-server helps to manage the Linux nfs server as a failover-able resource in Linux-HA.

%package xen
Group: System/Base
Requires: %name = %version-%release
Summary: resource agent manage Xen Hypervisor
BuildArch: noarch

%description xen
Manages Xen virtual machine instances by mapping cluster resource
start and stop,  to Xen create and shutdown, respectively.

%package drbd
Group: System/Base
Requires: %name = %version-%release
Summary: resource agent manage DRBD
BuildArch: noarch

%description drbd
This resource agent manages a Distributed
Replicated Block Device (DRBD) object as a master/slave
resource. DRBD is a mechanism for replicating storage.

Deprecation warning: This agent is deprecated and may be removed from
a future release. See the ocf:linbit:drbd resource agent for a
supported alternative.

%package lvm
Group: System/Base
Requires: %name = %version-%release
Summary: resource agent manage LVM
BuildArch: noarch

%description lvm
It manages an  Linux Volume Manager volume (LVM) as an HA resource.

%package WinPopup
Group: System/Base
Requires: %name = %version-%release
Summary: Resource script for WinPopup
BuildArch: noarch

%description WinPopup
It sends WinPopups message to a sysadmin's workstation whenever a takeover occurs.

%package -n ldirectord
License: GPLv2+
Summary: A Monitoring Daemon for Maintaining High Availability Resources
Group: System/Base
Provides: heartbeat-ldirectord = %version
Requires: ipvsadm logrotate linux-ha-common resource-agents
BuildArch: noarch

%description -n ldirectord
The Linux Director Daemon (ldirectord) was written by Jacob Rief.
<jacob.rief@tiscover.com>

ldirectord is a stand alone daemon for monitoring the services on real
servers. Currently, HTTP, HTTPS, and FTP services are supported.
lditrecord is simple to install and works with the heartbeat code
(http://www.linux-ha.org/).

See 'ldirectord -h' and linux-ha/doc/ldirectord for more information.

%prep
%setup
echo %version > .version
cp .version .tarball-version
mkdir -p m4

%build
export PYTHON=%__python3
%autoreconf
%configure	\
		--with-version=%version \
		--with-systemdsystemunitdir=%_unitdir \
		--with-initdir=%_initdir

%make_build

%install
%makeinstall_std

## tree fixup
# remove docs (there is only one and they should come from doc sections in files)
rm -rf %buildroot/usr/share/doc/resource-agents

mkdir -p %buildroot%_var/run/resource-agents

%preun -n ldirectord
%preun_service ldirectord

%post -n ldirectord
%post_service ldirectord

%files
%doc AUTHORS COPYING COPYING.GPLv3 COPYING.LGPL ChangeLog doc/README.webapps
%_datadir/%name/ra-api-1.dtd

%_unitdir/*.target
%_tmpfilesdir/*.conf
%_datadir/%name/metadata.rng

%_sbindir/*
%dir %_datadir/%name
%dir %_datadir/%name/ocft
%_datadir/%name/ocft/configs
%_datadir/%name/ocft/caselib
%_datadir/%name/ocft/README*
%_datadir/%name/ocft/helpers.sh
%exclude %_datadir/%name/ocft/runocft
%exclude %_datadir/%name/ocft/runocft.prereq

%_datadir/cluster

%dir %_libexecdir/ocf
%dir %_libexecdir/ocf/resource.d
%dir %_libexecdir/ocf/lib

%_libexecdir/ocf/lib/heartbeat
%_libexecdir/ocf/resource.d/redhat
%_libexecdir/ocf/resource.d/heartbeat

%_includedir/heartbeat

%_libexecdir/heartbeat
%_man7dir/*
%_man8dir/ocf-tester.8*
%if_with cluster_glue
%_man8dir/sfex_init.8*
%endif
%dir %attr (1755, root, root)	%_runtimedir/resource-agents

# For compatability with pre-existing agents
%dir %_sysconfdir/ha.d
%config(noreplace) %_sysconfdir/ha.d/shellfuncs

%exclude %_sysconfdir/ha.d/resource.d/ldirectord
%exclude %_sbindir/ldirectord
%exclude %_libexecdir/ocf/resource.d/heartbeat/ldirectord

%exclude %_libexecdir/ocf/resource.d/heartbeat/CTDB
%exclude %_man7dir/*_CTDB.*

%exclude %_libexecdir/ocf/resource.d/heartbeat/iSCSI*
%exclude %_man7dir/*_iSCSI*
%exclude %_libexecdir/ocf/resource.d/heartbeat/iscsi
%exclude %_man7dir/*_iscsi*
%exclude %_datadir/%name/ocft/configs/iscsi

%exclude %_libexecdir/ocf/resource.d/heartbeat/tomcat
%exclude %_datadir/cluster/tomcat*
%exclude %_datadir/cluster/utils/tomcat*
%exclude %_man7dir/*_tomcat.*

%exclude %_libexecdir/ocf/resource.d/heartbeat/fio
%exclude %_man7dir/*_fio.*

%exclude %_libexecdir/ocf/resource.d/heartbeat/VirtualDomain
%exclude %_man7dir/*_VirtualDomain.*

%exclude %_libexecdir/ocf/resource.d/heartbeat/lxc

%exclude %_datadir/cluster/nfsclient.sh
%exclude %_datadir/cluster/nfsexport.sh
%exclude %_datadir/cluster/nfsserver.sh
%exclude %_datadir/cluster/svclib_nfslock
%exclude %_libexecdir/ocf/resource.d/heartbeat/exportfs
%exclude %_libexecdir/ocf/resource.d/heartbeat/nfsserver
%exclude %_man7dir/*_exportfs.*
%exclude %_man7dir/*_nfsserver.*

%exclude %_libexecdir/ocf/resource.d/heartbeat/Xen
%exclude %_man7dir/*_Xen.*

#exclude %_libexecdir/ocf/resource.d/heartbeat/drbd
%exclude %_datadir/cluster/drbd*
#exclude %_man7dir/*_drbd.*

%exclude %_libexecdir/ocf/resource.d/heartbeat/LVM
%exclude %_datadir/cluster/lvm*
%exclude %_datadir/%name/ocft/configs/LVM
%exclude %_man7dir/*_LVM.*

%exclude %_libexecdir/ocf/resource.d/heartbeat/WinPopup
%exclude %_man7dir/*_WinPopup.*

%files CTDB
%_libexecdir/ocf/resource.d/heartbeat/CTDB
%_man7dir/*_CTDB.*

%files iSCSI
%_libexecdir/ocf/resource.d/heartbeat/iSCSI*
%_man7dir/*_iSCSI*
%_libexecdir/ocf/resource.d/heartbeat/iscsi
%_man7dir/*_iscsi*
%_datadir/%name/ocft/configs/iscsi

%files tomcat
%_libexecdir/ocf/resource.d/heartbeat/tomcat
%_datadir/cluster/tomcat*
%_datadir/cluster/utils/tomcat*
%_man7dir/*_tomcat.*

%files fio
%_libexecdir/ocf/resource.d/heartbeat/fio
%_man7dir/*_fio.*

%files libvirt
%_libexecdir/ocf/resource.d/heartbeat/VirtualDomain
%_man7dir/*_VirtualDomain.*

%files lxc
%_libexecdir/ocf/resource.d/heartbeat/lxc

%files nfs
%_datadir/cluster/nfsclient.sh
%_datadir/cluster/nfsexport.sh
%_datadir/cluster/nfsserver.sh
%_datadir/cluster/svclib_nfslock
%_libexecdir/ocf/resource.d/heartbeat/exportfs
%_libexecdir/ocf/resource.d/heartbeat/nfsserver
%_man7dir/*_exportfs.*
%_man7dir/*_nfsserver.*

%files xen
%_libexecdir/ocf/resource.d/heartbeat/Xen
%_man7dir/*_Xen.*

#files drbd
#_libexecdir/ocf/resource.d/heartbeat/drbd
#_datadir/cluster/drbd*
#_man7dir/*_drbd.*

%files lvm
%_libexecdir/ocf/resource.d/heartbeat/LVM
%_datadir/cluster/lvm*
%_datadir/%name/ocft/configs/LVM
%_man7dir/*_LVM.*

%files WinPopup
%_libexecdir/ocf/resource.d/heartbeat/WinPopup
%_man7dir/*_WinPopup.*

%files -n ldirectord
%doc ldirectord/ldirectord.cf COPYING
%config(noreplace) %_sysconfdir/logrotate.d/ldirectord
%config(noreplace) %_sysconfdir/ha.d/resource.d/ldirectord
%_initdir/ldirectord
%_unitdir/ldirectord.service
%_sbindir/ldirectord
%_libexecdir/ocf/resource.d/heartbeat/ldirectord
%_mandir/man8/ldirectord.8*

%changelog
* Wed Jul 03 2019 Andrew A. Vasilyev <andy@altlinux.org> 4.3.0-alt1
- 4.3.0

* Tue Apr 23 2019 Andrew A. Vasilyev <andy@altlinux.org> 4.2.0-alt1
- 4.2.0

* Wed Aug 02 2017 Anton Farygin <rider@altlinux.ru> 4.0.1-alt1
- new version

* Thu Apr 20 2017 Sergey Novikov <sotor@altlinux.org> 3.9.7-alt3
- fix CTDB start function, add ubt tag (closes: #33353)

* Fri Sep 23 2016 Alexey Shabalin <shaba@altlinux.ru> 3.9.7-alt2
- update add_findreq_skiplist

* Wed Sep 14 2016 Alexey Shabalin <shaba@altlinux.ru> 3.9.7-alt1
- 3.9.7

* Mon Nov 18 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 3.9.5-alt3.git.7fac8c7e
- Rebuild from git

* Wed Aug 14 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 3.9.5-alt2
- Set correct /var

* Tue Mar 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 3.9.5-alt1
- Build for ALT
