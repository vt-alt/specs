Name: pve-manager
Summary: The Proxmox Virtual Environment
Version: 6.0.6
Release: alt1
License: GPLv3
Group: System/Servers
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64 aarch64
Requires: cstream lzop pve-vncterm pve-novnc pve-spiceterm pve-xtermjs pve-docs
Requires: perl-LWP-Protocol-https pve-cluster

Source0: pve-manager.tar.xz
Source1: pve-container.tar.xz
Source2: pve-firewall.tar.xz
Source3: pve-ha-manager.tar.xz
Source4: qemu-server.tar.xz

Source10: pve-guest-common.tar.xz
Source11: pve-http-server.tar.xz
Source12: extjs.tar.xz
Source13: pve-widget-toolkit.tar.xz
Source14: pve-i18n.tar.xz
Source15: pve-mini-journalreader.tar.xz
Source16: jquery-3.3.1.min.js
Source17: bootstrap-3.4.1-dist.zip

Source5: pve-manager-ru.po
Source6: basealt_logo.png
Source70: basealt_bootsplash.svg
Source71: basealt_bootsplash_yellow.jpg
Source72: basealt_bootsplash_blue.jpg
Source8: basealt_favicon.ico
Source9: basealt_logo-128.png

Patch0: pve-manager-www.patch
Patch1: pve-manager-alt.patch
Patch2: pve-firewall-alt.patch
Patch3: pve-ha-manager-alt.patch
Patch4: pve-container-alt.patch
Patch5: qemu-server-alt.patch
Patch6: pve-manager-alt-bps-to-bit.patch
Patch7: pve-container-altlinux-lxc.patch
Patch9: pve-manager-alt-pve.patch
Patch10: pve-manager-help.patch
Patch11: pve-manager-install_vzdump_cron_config.patch
Patch12: qemu-server-lsi.patch
Patch13: pve-manager-lsi.patch
Patch14: pve-container-lxc.patch
Patch15: pve-manager-sgdisk.patch
Patch16: pve-manager-logrotate.patch
Patch18: pve-container-lxcnetdelbr.patch
Patch19: pve-manager-snapshot-resize.patch
Patch20: pve-manager-rem-package-ver-btn.patch
Patch21: pve-http-server-alt.patch
Patch22: extjs-alt.patch
Patch23: qemu-server-migrate-local-devices.patch
Patch24: pve-manager-postfix-ntpd.patch
Patch25: pve-manager-gettext.patch
Patch26: pve-ha-manager-watchdog.patch
Patch27: pve-widget-toolkit-alt.patch
Patch28: pve-widget-toolkit-alt-utils.patch
Patch29: pve-manager-widgettoolkit.patch
Patch30: pve-manager-perl-T.patch
Patch31: qemu-server-qemu-3-0-0-alt.patch
Patch32: pve-manager-alt-rm-pve-version.patch
Patch33: qemu-server-vga-map.patch
Patch34: qemu-server-alt-bootsplash.patch
Patch35: pve-manager-dc-summary.patch
Patch36: qemu-server-vmgenid-aarch64.patch
Patch37: pve-mini-journalreader-alt.patch
Patch38: pve-http-server-glyphicons.patch
Patch39: qemu-server-aarch64-spice.patch

BuildRequires: glib2-devel libnetfilter_log-devel pve-doc-generator pve-storage librados2-perl libsystemd-daemon-devel
BuildRequires: perl-AnyEvent-AIO perl-AnyEvent-HTTP perl-AptPkg perl-Crypt-SSLeay perl-File-ReadBackwards
BuildRequires: perl-IO-Multiplex perl-Locale-PO perl-UUID unzip xmlto pve-lxc libnetfilter_conntrack-devel
BuildRequires: perl(File/Sync.pm) perl(Net/DNS/Resolver.pm) perl(Pod/Select.pm) perl(Crypt/Eksblowfish/Bcrypt.pm)
BuildRequires: perl(Template.pm) perl(IPC/Run.pm) perl(Term/ReadLine.pm) libjson-c-devel libsystemd-devel

%description
This package contains the PVE management tools

%package -n pve-container
Summary: PVE Container management tool
Version: 3.0.5
Group: Development/Perl
PreReq: shadow-submap
Requires: pve-lxc >= 2.1.0 dtach perl-Crypt-Eksblowfish >= 0.009-alt5_15

%description -n pve-container
Tool to manage Linux Containers on PVE

%package -n pve-firewall
Summary: PVE Firewall
Version: 4.0.7
Group: System/Servers
Requires: ebtables ipset iptables iptables-ipv6 shorewall shorewall6 iproute2 >= 4.10.0

%description -n pve-firewall
This package contains the PVE Firewall

%package -n pve-ha-manager
Summary: PVE HA Manager
Version: 3.0.2
Group: System/Servers

%description -n pve-ha-manager
HA Manager PVE

%package -n pve-qemu-server
Summary: Qemu Server Tools
Version: 6.0.7
Group: System/Servers
Requires: socat genisoimage pve-qemu-system >= 2.6.1-alt4
Provides: qemu-server = %version-%release
Obsoletes: qemu-server < %version-%release

%description -n pve-qemu-server
This package contains the Qemu Server tools used by PVE

%package -n pve-guest-common
Summary: PVE common guest-related modules
Version: 3.0.1
Group: System/Servers

%description -n pve-guest-common
This package contains a common code base used by pve-container and qemu-server

%package -n pve-http-server
Summary: PVE Asynchrounous HTTP Server Implementation
Version: 3.0.2
Group: System/Servers
Requires: fonts-font-awesome

%description -n pve-http-server
This is used to implement the PVE REST API

%add_findreq_skiplist %perl_vendor_privlib/PVE/HA/Env/PVE2.pm

%prep
%setup -q -c -n pve -a1 -a2 -a3 -a4 -a10 -a11 -a12 -a13 -a14 -a15
%patch0 -p0 -b .altwww
%patch1 -p0 -b .alt
%patch2 -p0 -b .alt
%patch3 -p0 -b .alt
%patch4 -p0 -b .alt
%patch5 -p0 -b .alt
%patch6 -p0 -b .alt-bps-to-bit
%patch7 -p0 -b .altlinux-lxc
%patch9 -p0 -b .alt-pve
%patch10 -p0 -b .alt-help
%patch11 -p0 -b .vzdump
%patch12 -p0 -b .megasas-gen2-1
%patch13 -p0 -b .megasas-gen2-2
%patch14 -p0 -b .lxc
%patch15 -p0 -b .sgdisk
%patch16 -p0 -b .logrotate
%patch18 -p0 -b .lxcnetdelbr
%patch19 -p0 -b .resize
%patch20 -p0 -b .rembtn
%patch21 -p0 -b .alt
%patch22 -p0 -b .alt
%patch23 -p0 -b .local-devices
%patch24 -p0 -b .postfix-3
%patch25 -p0 -b .gettext
%patch26 -p0 -b .watchdog
%patch27 -p0 -b .alt
%patch28 -p0 -b .alt
%patch29 -p0 -b .widgettoolkit
%patch30 -p0 -b .T
%patch31 -p0 -b .qemu-3-0-0
%patch32 -p0 -b .rm-version
%patch33 -p0 -b .vga-map
%patch34 -p0 -b .bootsplash
%patch35 -p0 -b .nosubscription
%patch36 -p0 -b .vmgenid
%patch37 -p0 -b .type-limits
%patch38 -p0 -b .glyphicons
%patch39 -p0 -b .aarch64-spice

find -name Makefile | while read m; do
	sed -i '/^.*\/usr\/share\/dpkg.*/d' $m;
done

grep '/var/run' * -rl | while read f; do
    sed -i 's|/var/run|/run|' $f
done

install -m0644 %SOURCE5 pve-i18n/ru.po

%build
for d in pve-manager pve-firewall/src pve-ha-manager/src pve-widget-toolkit pve-mini-journalreader/src; do
    pushd $d
    %make
    popd
done

%install
for d in pve-manager pve-firewall/src pve-ha-manager/src pve-container/src qemu-server pve-guest-common pve-http-server extjs pve-widget-toolkit pve-i18n pve-mini-journalreader/src; do
    pushd $d
    %make DESTDIR=%buildroot install
    popd
done

install -pD -m0644 %SOURCE16 %buildroot%_datadir/javascript/jquery/jquery.min.js
unzip %SOURCE17 -d %buildroot%_datadir/javascript/
mv %buildroot%_datadir/javascript/bootstrap-*-dist %buildroot%_datadir/javascript/bootstrap
ln -s ../fonts-font-awesome %buildroot%_datadir/javascript/font-awesome

install -m0644 %SOURCE6 %buildroot%_datadir/pve-manager/images/basealt_logo.png
install -m0644 %SOURCE8 %buildroot%_datadir/pve-manager/images/favicon.ico
install -m0644 %SOURCE9 %buildroot%_datadir/pve-manager/images/logo-128.png

install -m0644 %SOURCE71 %buildroot%_datadir/qemu-server/bootsplash.jpg
install -m0644 %SOURCE72 %buildroot%_datadir/qemu-server/bootsplash_invert.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-cirrus.jpg
ln -s bootsplash_invert.jpg %buildroot%_datadir/qemu-server/bootsplash-std.jpg
ln -s bootsplash_invert.jpg %buildroot%_datadir/qemu-server/bootsplash-vmware.jpg
ln -s bootsplash_invert.jpg %buildroot%_datadir/qemu-server/bootsplash-qxl.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-serial0.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-serial1.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-serial2.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-serial3.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-virtio.jpg

install -m0644 pve-firewall/debian/*.service %buildroot%systemd_unitdir/
install -m0644 pve-firewall/debian/pve-firewall.logrotate %buildroot%_sysconfdir/logrotate.d/pve-firewall
mkdir -p %buildroot%_localstatedir/pve-firewall

install -m0644 pve-ha-manager/debian/*.service %buildroot%systemd_unitdir/
install -pD -m0644 pve-ha-manager/debian/pve-ha-manager.default %buildroot%_sysconfdir/sysconfig/pve-ha-manager

mkdir -p %buildroot/lib/tmpfiles.d
cat << __EOF__ > %buildroot/lib/tmpfiles.d/%name.conf
d /run/pveproxy 0700 www-data www-data -
f /var/lock/pveproxy.lck 0644 www-data www-data
f /var/lock/spiceproxy.lck 0644 www-data www-data
__EOF__

mkdir -p %buildroot%_sysconfdir/modules-load.d
cat << __EOF__ > %buildroot%_sysconfdir/modules-load.d/pve-firewall.conf
br_netfilter
__EOF__

%post
%post_service pvedaemon
%post_service pveproxy
%post_service pvestatd
%post_service spiceproxy

%preun
%preun_service pvedaemon
%preun_service pveproxy
%preun_service pvestatd
%preun_service spiceproxy

%post -n pve-container
%_sbindir/usermod --add-subgids 100000-165535 root ||:
%_sbindir/usermod --add-subuids 100000-165535 root ||:

%post -n pve-firewall
%post_service pve-firewall
%post_service pvefw-logger

%preun -n pve-firewall
%preun_service pve-firewall
%preun_service pvefw-logger

%files
%dir %_datadir/doc/pve-manager
%_datadir/doc/pve-manager/examples
%_datadir/bash-completion/completions/pveam
%_datadir/bash-completion/completions/pvesr
%_datadir/bash-completion/completions/pveceph
%_datadir/bash-completion/completions/pvedaemon
%_datadir/bash-completion/completions/pvenode
%_datadir/bash-completion/completions/pveproxy
%_datadir/bash-completion/completions/pvestatd
%_datadir/bash-completion/completions/pvesubscription
%_datadir/bash-completion/completions/spiceproxy
%_datadir/bash-completion/completions/vzdump
%_datadir/bash-completion/completions/pvesh
%_datadir/bash-completion/completions/pve5to6
%_datadir/zsh/vendor-completions/_pveam
%_datadir/zsh/vendor-completions/_pvesr
%_datadir/zsh/vendor-completions/_pveceph
%_datadir/zsh/vendor-completions/_pvedaemon
%_datadir/zsh/vendor-completions/_pvenode
%_datadir/zsh/vendor-completions/_pveproxy
%_datadir/zsh/vendor-completions/_pvestatd
%_datadir/zsh/vendor-completions/_pvesubscription
%_datadir/zsh/vendor-completions/_spiceproxy
%_datadir/zsh/vendor-completions/_vzdump
%_datadir/zsh/vendor-completions/_pvesh
%_datadir/zsh/vendor-completions/_pve5to6
%_sysconfdir/logrotate.d/pve
%config(noreplace) %_sysconfdir/vzdump.conf
#systemd_unitdir/pvebanner.service
#systemd_unitdir/pvenetcommit.service
%systemd_unitdir/pvedaemon.service
%systemd_unitdir/pve-guests.service
%systemd_unitdir/pveproxy.service
%systemd_unitdir/pvestatd.service
%systemd_unitdir/spiceproxy.service
%systemd_unitdir/pve-storage.target
%systemd_unitdir/pvesr.*
%systemd_unitdir/ceph-*.service.d
/lib/tmpfiles.d/%name.conf
%_bindir/pveam
%_bindir/pvesr
#_bindir/pvebanner
%_bindir/pveceph
%_bindir/pvedaemon
%_bindir/pvemailforward
%_bindir/pvemailforward.pl
%_bindir/pvenode
%_bindir/pveperf
%_bindir/pveproxy
%_bindir/pvereport
%_bindir/pvesh
%_bindir/pvestatd
#_bindir/pvesubscription
%_bindir/pveupdate
#_bindir/pveupgrade
%_bindir/pveversion
%_bindir/spiceproxy
%_bindir/vzdump
%_bindir/mini-journalreader
%_bindir/pve5to6
%_datadir/pve-i18n
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/API2
%dir %perl_vendor_privlib/PVE/CLI
%dir %perl_vendor_privlib/PVE/Service
%dir %perl_vendor_privlib/PVE/Status
%dir %perl_vendor_privlib/PVE/VZDump
%dir %perl_vendor_privlib/PVE/Ceph
%perl_vendor_privlib/PVE/API2.pm
%perl_vendor_privlib/PVE/API2Tools.pm
%perl_vendor_privlib/PVE/APLInfo.pm
%perl_vendor_privlib/PVE/AutoBalloon.pm
%perl_vendor_privlib/PVE/CertHelpers.pm
%perl_vendor_privlib/PVE/HTTPServer.pm
%perl_vendor_privlib/PVE/NodeConfig.pm
%perl_vendor_privlib/PVE/pvecfg.pm
%perl_vendor_privlib/PVE/Report.pm
%perl_vendor_privlib/PVE/VZDump.pm
%perl_vendor_privlib/PVE/API2/ACME.pm
%perl_vendor_privlib/PVE/API2/ACMEAccount.pm
%perl_vendor_privlib/PVE/API2/APT.pm
%perl_vendor_privlib/PVE/API2/Backup.pm
%perl_vendor_privlib/PVE/API2/Ceph.pm
%perl_vendor_privlib/PVE/API2/Certificates.pm
%perl_vendor_privlib/PVE/API2/Cluster.pm
%perl_vendor_privlib/PVE/API2/HAConfig.pm
%perl_vendor_privlib/PVE/API2/Network.pm
%perl_vendor_privlib/PVE/API2/NodeConfig.pm
%perl_vendor_privlib/PVE/API2/Nodes.pm
%perl_vendor_privlib/PVE/API2/Pool.pm
%perl_vendor_privlib/PVE/API2/Services.pm
%perl_vendor_privlib/PVE/API2/Subscription.pm
%perl_vendor_privlib/PVE/API2/Tasks.pm
%perl_vendor_privlib/PVE/API2/VZDump.pm
%perl_vendor_privlib/PVE/API2/Replication.pm
%perl_vendor_privlib/PVE/API2/ReplicationConfig.pm
%perl_vendor_privlib/PVE/API2/Hardware.pm
%perl_vendor_privlib/PVE/API2/Scan.pm
%dir %perl_vendor_privlib/PVE/API2/Hardware
%dir %perl_vendor_privlib/PVE/API2/Ceph
%perl_vendor_privlib/PVE/API2/Hardware/PCI.pm
%perl_vendor_privlib/PVE/API2/Ceph/FS.pm
%perl_vendor_privlib/PVE/API2/Ceph/MDS.pm
%perl_vendor_privlib/PVE/API2/Ceph/MGR.pm
%perl_vendor_privlib/PVE/API2/Ceph/MON.pm
%perl_vendor_privlib/PVE/API2/Ceph/OSD.pm
%dir %perl_vendor_privlib/PVE/API2/Cluster
%perl_vendor_privlib/PVE/API2/Cluster/Ceph.pm
%perl_vendor_privlib/PVE/CLI/pveceph.pm
%perl_vendor_privlib/PVE/CLI/pvenode.pm
%perl_vendor_privlib/PVE/CLI/pvesr.pm
%perl_vendor_privlib/PVE/CLI/pvesubscription.pm
%perl_vendor_privlib/PVE/CLI/vzdump.pm
%perl_vendor_privlib/PVE/CLI/pvesh.pm
%perl_vendor_privlib/PVE/CLI/pve5to6.pm
%perl_vendor_privlib/PVE/Ceph/Services.pm
%perl_vendor_privlib/PVE/Ceph/Tools.pm
%perl_vendor_privlib/PVE/Service/pvedaemon.pm
%perl_vendor_privlib/PVE/Service/pveproxy.pm
%perl_vendor_privlib/PVE/Service/pvestatd.pm
%perl_vendor_privlib/PVE/Service/spiceproxy.pm
%perl_vendor_privlib/PVE/Status/Graphite.pm
%perl_vendor_privlib/PVE/Status/InfluxDB.pm
%perl_vendor_privlib/PVE/Status/Plugin.pm
%perl_vendor_privlib/PVE/CLI/pveam.pm
%_datadir/pve-manager
%_localstatedir/pve-manager
%dir %_localstatedir/vz/images
%dir %_localstatedir/vz/template/iso
%dir %_localstatedir/vz/template/qemu
%attr(0770,root,www-data) %_logdir/pveproxy
%_man1dir/pveceph.1*
%_man1dir/pvenode.1*
%_man1dir/pveperf.1*
%_man1dir/pvereport.1*
%_man1dir/pvesh.1*
%_man1dir/pvesr.1*
%_man1dir/pve5to6.1*
#_man1dir/pvesubscription.1*
#_man1dir/pveupgrade.1*
%_man1dir/pveversion.1*
%_man1dir/vzdump.1*
%_man1dir/pveam.1.xz
%_man8dir/pvedaemon.8*
%_man8dir/pveproxy.8*
%_man8dir/pvestatd.8*
%_man8dir/spiceproxy.8*
%dir %_datadir/doc/%name

%files -n pve-container
%_sysconfdir/sysctl.d/10-pve-ct-inotify-limits.conf
%_datadir/bash-completion/completions/pct
%_datadir/zsh/vendor-completions/_pct
%systemd_unitdir/pve-container*.service
%systemd_unitdir/system-pve*container.slice
%_sbindir/pct
%_datadir/lxc
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/API2
%dir %perl_vendor_privlib/PVE/CLI
%dir %perl_vendor_privlib/PVE/VZDump
%perl_vendor_privlib/PVE/LXC
%perl_vendor_privlib/PVE/LXC.pm
%perl_vendor_privlib/PVE/API2/LXC
%perl_vendor_privlib/PVE/API2/LXC.pm
%perl_vendor_privlib/PVE/CLI/pct.pm
%perl_vendor_privlib/PVE/VZDump/ConvertOVZ.pm
%perl_vendor_privlib/PVE/VZDump/LXC.pm
%_man1dir/pct.1*
%_man5dir/*ct.conf.5*

%files -n pve-firewall
%_datadir/bash-completion/completions/pve-firewall
%_datadir/zsh/vendor-completions/_pve-firewall
%_sysconfdir/logrotate.d/pve-firewall
%config(noreplace) %_sysconfdir/sysctl.d/pve-firewall.conf
%config(noreplace) %_sysconfdir/modules-load.d/pve-firewall.conf
%systemd_unitdir/pve-firewall.service
%systemd_unitdir/pvefw-logger.service
%_sbindir/pve-firewall
%_sbindir/pvefw-logger
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/API2
%dir %perl_vendor_privlib/PVE/Service
%perl_vendor_privlib/PVE/Firewall.pm
%perl_vendor_privlib/PVE/FirewallSimulator.pm
%perl_vendor_privlib/PVE/API2/Firewall
%perl_vendor_privlib/PVE/Service/pve_firewall.pm
%_localstatedir/pve-firewall
%_man8dir/pve-firewall.8*

%files -n pve-ha-manager
%config(noreplace) %_sysconfdir/sysconfig/pve-ha-manager
%_datadir/bash-completion/completions/ha-manager
%_datadir/bash-completion/completions/pve-ha-crm
%_datadir/bash-completion/completions/pve-ha-lrm
%_datadir/zsh/vendor-completions/_ha-manager
%_datadir/zsh/vendor-completions/_pve-ha-crm
%_datadir/zsh/vendor-completions/_pve-ha-lrm
%systemd_unitdir/pve-ha-crm.service
%systemd_unitdir/pve-ha-lrm.service
%systemd_unitdir/watchdog-mux.service
%_sbindir/ha-manager
%_sbindir/pve-ha-crm
%_sbindir/pve-ha-lrm
%_sbindir/watchdog-mux
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/API2
%dir %perl_vendor_privlib/PVE/CLI
%dir %perl_vendor_privlib/PVE/HA
%dir %perl_vendor_privlib/PVE/Service
%dir %perl_vendor_privlib/PVE/HA/Resources
%perl_vendor_privlib/PVE/API2/HA
%perl_vendor_privlib/PVE/CLI/ha_manager.pm
%perl_vendor_privlib/PVE/HA/Env
%perl_vendor_privlib/PVE/HA/Config.pm
%perl_vendor_privlib/PVE/HA/CRM.pm
%perl_vendor_privlib/PVE/HA/Env.pm
%perl_vendor_privlib/PVE/HA/Groups.pm
%perl_vendor_privlib/PVE/HA/LRM.pm
%perl_vendor_privlib/PVE/HA/Manager.pm
%perl_vendor_privlib/PVE/HA/NodeStatus.pm
%perl_vendor_privlib/PVE/HA/Resources.pm
%perl_vendor_privlib/PVE/HA/Tools.pm
%perl_vendor_privlib/PVE/HA/Fence.pm
%perl_vendor_privlib/PVE/HA/FenceConfig.pm
%perl_vendor_privlib/PVE/Service/pve_ha_crm.pm
%perl_vendor_privlib/PVE/Service/pve_ha_lrm.pm
%perl_vendor_privlib/PVE/HA/Resources/PVEVM.pm
%perl_vendor_privlib/PVE/HA/Resources/PVECT.pm
%_man1dir/ha-manager.1*
%_man8dir/pve-ha-crm.8*
%_man8dir/pve-ha-lrm.8*

%files -n pve-qemu-server
%_datadir/bash-completion/completions/qm
%_datadir/bash-completion/completions/qmrestore
%_datadir/zsh/vendor-completions/_qm
%_datadir/zsh/vendor-completions/_qmrestore
%config(noreplace) %_sysconfdir/modules-load.d/qemu-server.conf
%systemd_unitdir/qmeventd.service
%_prefix/lib/qemu-server
%_sbindir/qm
%_sbindir/qmrestore
%_sbindir/qmeventd
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/API2
%dir %perl_vendor_privlib/PVE/API2/Qemu
%dir %perl_vendor_privlib/PVE/CLI
%dir %perl_vendor_privlib/PVE/VZDump
%dir %perl_vendor_privlib/PVE/QemuServer
%perl_vendor_privlib/PVE/QemuMigrate.pm
%perl_vendor_privlib/PVE/QemuServer.pm
%perl_vendor_privlib/PVE/QemuConfig.pm
%perl_vendor_privlib/PVE/QMPClient.pm
%perl_vendor_privlib/PVE/API2/Qemu/Agent.pm
%perl_vendor_privlib/PVE/API2/Qemu.pm
%perl_vendor_privlib/PVE/CLI/qm.pm
%perl_vendor_privlib/PVE/CLI/qmrestore.pm
%perl_vendor_privlib/PVE/VZDump/QemuServer.pm
%perl_vendor_privlib/PVE/QemuServer/Memory.pm
%perl_vendor_privlib/PVE/QemuServer/PCI.pm
%perl_vendor_privlib/PVE/QemuServer/USB.pm
%perl_vendor_privlib/PVE/QemuServer/ImportDisk.pm
%perl_vendor_privlib/PVE/QemuServer/OVF.pm
%perl_vendor_privlib/PVE/QemuServer/Cloudinit.pm
%perl_vendor_privlib/PVE/QemuServer/Agent.pm
%_datadir/qemu-server
%_localstatedir/qemu-server
%_man1dir/qm.1*
%_man1dir/qmrestore.1*
%_man5dir/*m.conf.5*
%_man8dir/qmeventd.8*

%files -n pve-guest-common
%dir %perl_vendor_privlib/PVE/VZDump
%perl_vendor_privlib/PVE/VZDump/Plugin.pm
%perl_vendor_privlib/PVE/ReplicationState.pm
%perl_vendor_privlib/PVE/ReplicationConfig.pm
%perl_vendor_privlib/PVE/Replication.pm
%perl_vendor_privlib/PVE/GuestHelpers.pm
%perl_vendor_privlib/PVE/AbstractMigrate.pm
%perl_vendor_privlib/PVE/AbstractConfig.pm

%files -n pve-http-server
%_datadir/javascript
%perl_vendor_privlib/PVE/APIServer

%changelog
* Mon Aug 26 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.6-alt1
- pve-manager 6.0-6
- pve-widget-toolkit 2.0-7

* Tue Aug 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.5-alt1
- pve-manager 6.0-5
- pve-container 3.0-5
- pve-firewall 4.0-7
- qemu-server 6.0-7
- pve-ha-manager 3.0-2
- pve-guest-common 3.0-1
- pve-http-server 3.0-2
- pve-widget-toolkit 2.0-5
- pve-i18n 2.0-2

* Tue Jun 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.4.6-alt3
- fixed aarch64 VM parameters

* Fri May 24 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.4.6-alt2
- pve-mini-journalreader 1.1-1

* Mon May 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.4.6-alt1
- pve-manager 5.4-6
- pve-container 2.0-39
- pve-firewall 3.0-21
- qemu-server 5.0-51
- pve-ha-manager 2.0-9
- pve-guest-common 2.0-20
- pve-http-server 2.0-13
- pve-widget-toolkit 1.0-28
- pve-i18n 1.1-4

* Fri Feb 01 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.3.8-alt11
- pve-manager 5.3-8
- pve-container 2.0-33
- pve-firewall 3.0-17
- qemu-server 5.0-45
- pve-ha-manager 2.0-6
- pve-guest-common 2.0-19

* Wed Dec 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.3.5-alt10
- pve-manager 5.3-5
- pve-container 2.0-31
- pve-firewall 3.0-16
- qemu-server 5.0-43
- pve-widget-toolkit 1.0-22
- extjs 6.0.1-2
- pve-i18n 1.0-9

* Mon Nov 26 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.3.3-alt9
- pve-manager 5.3-3
- pve-container 2.0-30
- pve-firewall 3.0-15
- qemu-server 5.0-42
- pve-guest-common 2.0-18

* Wed Oct 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt8
- pve-http-server 2.0-11

* Thu Oct 04 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt7
- updated russian translation

* Tue Oct 02 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt6
- pve-firewall 3.0-12

* Fri Sep 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt5
- removed ubt

* Wed Sep 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt4.S1
- fixed version check qemu 3.0.0

* Tue Sep 04 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt3.S1
- pve-manager 5.2-3
- qemu-server 5.0-27

* Thu Aug 09 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.2-alt2.S1
- updated russian translation

* Wed Jul 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.2-alt1.S1
- pve-manager 5.2-2
- pve-container 2.0-24
- pve-firewall 3.0-10
- pve-ha-manager 2.0-5
- qemu-server 5.0-26
- pve-guest-common 2.0-17
- pve-http-server 2.0-9

* Wed Jan 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.1.39-alt3.S1
- merged patches PCID flags from upstream

* Thu Dec 14 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.1.39-alt1.M80P.3
- backport to p8 branch

* Tue Dec 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.1.39-alt3
- pve-manager 5.1-39
- pve-firewall 3.0-5
- pve-ha-manager 2.0-4
- pve-http-server 2.0-8

* Tue Nov 28 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.1.35-alt1.M80P.1
- backport to p8 branch

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.1.35-alt2
- pve-manager 5.1-35

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.34-alt1
- pve-manager 5.0-34
- pve-container 2.0-17
- pve-firewall 3.0-3
- pve-ha-manager 2.0-3
- qemu-server 5.0-17
- pve-guest-common 2.0-13
- pve-http-server 2.0-6

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt5.M80C.8
- backport to c8 branch

* Thu Sep 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt5.M80P.8
- fixed creation osd in ceph 10

* Tue Sep 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt4.M80P.8
- backport to p8 branch

* Tue Sep 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt8
- pve-container 2.0-16

* Wed Aug 09 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt4.M80P.1
- backport to p8 branch

* Wed Aug 09 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt7
- don't uses ssh if install vzdump.cron to localhost (closes: #33746)
- qemu-server 5.0-15

* Fri Aug 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt3.M80P.1
- backport to p8 branch

* Fri Aug 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt6
- updates services list

* Thu Aug 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt2.M80P.1
- backport to p8 branch

* Thu Aug 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt5
- do not use force when migrating vm uses local device

* Tue Aug 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt1.M80P.1
- backport to p8 branch

* Tue Aug 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt4
- fixed FontAwesome path

* Tue Jul 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt3
- pve-container 2.0-15
- qemu-server 5.0-14

* Thu Jul 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt2
- pve-manager 5.0-24
- pve-firewall 3.0-2

* Thu Jul 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.23-alt0.M80P.1
- backport to p8 branch

* Mon Jul 17 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.23-alt1
- pve-manager 5.0-23
- pve-container 2.0-14
- qemu-server 5.0-13
- pve-ha-manager 2.0-2
- pve-guest-common 2.0-11
- pve-http-server 2.0-5

* Wed Jul 05 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt15
- removed "Package version" button (closes: #33615)

* Tue Jun 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt14
- firewall now works

* Wed Jun 14 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt13
- fixed date/time column resize in snapshots (closes: #33528)

* Mon May 15 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt12
- pve-container: added lxcnetdelbr script

* Thu May 11 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt11
- various fixes

* Thu Apr 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt10
- fixed create/start unprivileged container

* Tue Apr 18 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt9
- fixed creation of containers by the user

* Mon Mar 27 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt8
- added LSI Logic SAS 1068 support

* Sat Mar 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt7
- corrected the names of MegaRAID SAS controllers

* Sat Mar 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt6
- added LSI MegaRAID SAS 2108 support

* Mon Feb 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt5
- fixed node network status

* Mon Dec 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt4
- 4.4-1
- pve-container 1.0-88

* Thu Dec 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.14-alt3
- install regular file to cron.d (closes: #32835)

* Wed Dec 07 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.14-alt2
- 4.3-14
- qemu-server 4.0-101

* Mon Dec 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.13-alt1
- 4.3-13
- pve-container 1.0-87
- pve-firewall 2.0-33
- pve-ha-manager 1.0-38
- qemu-server 4.0-100

* Mon Nov 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.12-alt10
- 4.3-12

* Thu Nov 24 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.11-alt9
- pve-container 1.0-84

* Wed Nov 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.11-alt8
- 4.3-11
- pve-container 1.0-83
- pve-ha-manager 1.0-37
- qemu-server 4.0-96

* Fri Oct 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.6-alt7
- 4.3-6
- qemu-server 4.0-92

* Sun Oct 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.3-alt6
- 4.3-3
- qemu-server 4.0-91
- pve-firewall 2.0-31

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.23-alt5
- qemu-server 4.0-89
- pve-container 1.0-78

* Mon Sep 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.23-alt4
- requires pve-docs

* Thu Sep 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.23-alt3
- 4.2-23
- pve-container 1.0-75

* Wed Sep 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.21-alt2
- added support altlinux container

* Mon Sep 19 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.21-alt1
- 4.2-21
- pve-container 1.0-74
- pve-firewall 2.0-30
- pve-ha-manager 1.0-35
- qemu-server 4.0-88

* Mon Sep 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.18-alt9
- Network Device: replace rate limit MB/s to MBit/s

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.18-alt8
- 4.2-18
- pve-container 1.0-73
- pve-ha-manager 1.0-33
- qemu-server 4.0-85

* Fri Jul 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.16-alt7
- 4.2-16
- pve-ha-manager 1.0-32

* Tue Jun 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.15-alt6
- pve-container 1.0-70

* Sun Jun 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.15-alt5
- pve-container: requires pve-lxc

* Tue Jun 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.15-alt4
- pve-manager 4.2-15
- qemu-server 4.0-83

* Wed Jun 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.14-alt3
- 4.2-14

* Tue Jun 07 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.11-alt2
- rebuild

* Mon Jun 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.11-alt1
- 4.2-11

* Mon Feb 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.1.10-alt1
- update version

* Thu Dec 10 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.64-alt1
- initial release

