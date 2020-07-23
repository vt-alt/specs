%def_disable check
%def_without ksrc
%def_without xenserver
%def_with debugtools
# According to the "ExclusiveArch:" from the dpdk.
%ifarch x86_64 %ix86 aarch64 ppc64le
%def_with dpdk
%endif

Name: openvswitch
Version: 2.12.0
Release: alt4.M90P.1

Summary: An open source, production quality, multilayer virtual switch
License: ASL 2.0 and LGPLv2+ and SISSL
Group: Networking/Other

Url: http://openvswitch.org
Source0: %url/releases/%name-%version.tar
Source1: %name.init
Source12: %name.tmpfiles

Patch1: openvswitch-2.0_alt_fix_function.patch
Patch2: openvswitch-2.5.0-fix-link.patch
Patch3: openvswitch-2.12.0-alt-systemd-unit.patch
Patch4: python3-dict-change.patch

Patch101: python3.patch
Patch102: 0001-ovs-check-dead-ifs-unshadow-pid-variable.patch
Patch103: ovn-detrace-python3.patch

Obsoletes: %name-controller <= %name-%version
Obsoletes: %name-ovsdbmonitor <= %name-%version
Obsoletes: bash-completion-%name
# force apt to update openvswith with etcnet
Conflicts: etcnet <= 0.9.18

# util-linux-2.32-alt2
Requires: pam0(runuser)
%filter_from_requires /lsb-release/d

BuildRequires(pre): rpm-build-python3
BuildRequires: graphviz libssl-devel openssl groff
BuildRequires: libcap-ng-devel
BuildRequires: glibc-kernheaders
BuildRequires: python-devel python-module-setuptools python-module-six python-module-OpenSSL
BuildRequires: python3-devel python3-module-setuptools python3-module-six python3-module-OpenSSL

%{?_with_dpdk:BuildRequires: dpdk-devel >= 18.08 libpcap-devel libnuma-devel rdma-core-devel libmnl-devel}

%define ksrcdir %_usrsrc/kernel/sources

%description
Open vSwitch is a production quality, multilayer virtual switch
licensed under the open source Apache 2.0 license. It is designed
to enable massive network automation through programmatic
extension, while still supporting standard management interfaces
and protocols (e.g. NetFlow, sFlow, RSPAN, ERSPAN, CLI, LACP,
802.1ag). In addition, it is designed to support distribution
across multiple physical servers similar to VMware's vNetwork
distributed vswitch or Cisco's Nexus 1000V.

%package -n kernel-source-%name
Group: Development/Kernel
License: GPLv2+
Summary: Open vSwitch Linux kernel modules source
BuildArch: noarch

%description -n kernel-source-%name
Source for kernel modules supporting the openvswitch datapath

%package debugtools
Group: Networking/Other
License: ASL 2.0
Summary: Open vSwitch bug reporting tool
BuildArch: noarch
Requires: %name-common = %EVR

%description debugtools
This package contains ovs-bugtool to generate a debug bundle
with useful information about Open vSwitch on this system
and place it in %_logdir/ovs-bugtool, and ovs-test to check
Linux drivers for performance and vlan problems.

%package common
Group: Networking/Other
License: ASL 2.0 and LGPLv2+ and SISSL
Summary: Common Open vSwitch code

%description common
This package provides components required by both openvswitch
and openvswitch-controller.

%package vtep
Group: Networking/Other
License: ASL 2.0
Summary: Open vSwitch VTEP emulator
Requires: %name = %EVR

%description vtep
A VTEP emulator that uses Open vSwitch for forwarding.

%package devel
Summary: Open vSwitch Devel Libraries
License: ASL 2.0
Group: Development/C
Requires: %name = %EVR

%description devel
Devel files for Open vSwitch.

%package ipsec
Summary: Open vSwitch IPsec tunneling support
License: ASL 2.0
Group: Networking/Other
Requires: %name = %EVR
# libreswan
Requires: python3-module-%name = %EVR

%description ipsec
This package provides IPsec tunneling support for OVS tunnels.

%package ovn-central
Summary: Open vSwitch - Open Virtual Network support
License: ASL 2.0
Group: Networking/Other
Requires: %name = %EVR
Requires: %name-ovn-common = %EVR

%description ovn-central
OVN, the Open Virtual Network, is a system to support virtual network
abstraction.  OVN complements the existing capabilities of OVS to add
native support for virtual network abstractions, such as virtual L2 and L3
overlays and security groups.

%package ovn-host
Summary: Open vSwitch - Open Virtual Network support
License: ASL 2.0
Group: Networking/Other
Requires: %name = %EVR
Requires: %name-ovn-common = %EVR

%description ovn-host
OVN, the Open Virtual Network, is a system to support virtual network
abstraction.  OVN complements the existing capabilities of OVS to add
native support for virtual network abstractions, such as virtual L2 and L3
overlays and security groups.

%package ovn-vtep
Summary: Open vSwitch - Open Virtual Network support
License: ASL 2.0
Group: Networking/Other
Requires: %name = %EVR
Requires: %name-ovn-common = %EVR

%description ovn-vtep
OVN vtep controller

%package ovn-common
Summary: Open vSwitch - Open Virtual Network support
License: ASL 2.0
Group: Networking/Other
Requires: %name = %EVR

%description ovn-common
Utilities that are use to diagnose and manage the OVN components.

%package ovn-docker
Summary: Open vSwitch - Open Virtual Network support
License: ASL 2.0
Group: Networking/Other
Requires: %name = %EVR
Requires: %name-ovn-common = %EVR
Requires: python3-module-%name = %EVR

%description ovn-docker
Docker network plugins for OVN.

%package -n python-module-%name
Summary: Open vSwitch python bindings
Group: Development/Python
License: Python-2.0
%add_python_req_skip pywintypes win32con win32file msvcrt

%description -n python-module-%name
Python bindings for the Open vSwitch database

%package -n python3-module-%name
Summary: Open vSwitch python3 bindings
Group: Development/Python3
License: Python-2.0
%add_python3_req_skip pywintypes win32con win32file msvcrt

%description -n python3-module-%name
Python3 bindings for the Open vSwitch database

%prep
%setup
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

%patch101 -p1
%patch102 -p1
%patch103 -p1

%if_with ksrc
# it's not datapath/linux due to shared configure script; thx led@
pushd ..
mkdir kernel-source-%name-%version
cp -al  %name-%version/{config.h.in,configure,Makefile.in} \
	%name-%version/{build-aux,datapath,include,tests} \
	kernel-source-%name-%version/
tar cf kernel-source-%name-%version.tar kernel-source-%name-%version
rm -r kernel-source-%name-%version
popd
%endif

%build
export PYTHON=%__python3
#export PYTHON2=no
%autoreconf
%configure \
	--disable-static \
	--enable-shared \
	--enable-ssl \
%if_with dpdk
	--with-dpdk=$(dirname %_libdir/dpdk/*/.config) \
%endif
	--with-rundir=/run/%name \
	--with-logdir=%_logdir/%name \
	--with-dbdir=%_localstatedir/%name \
	--with-pkidir=%_localstatedir/%name/pki

%make_build
make rhel/usr_lib_systemd_system_ovs-vswitchd.service

# test 591 fails, reported upstream
%check
LC_CTYPE=en_US.UTF-8 LC_COLLATE=en_US.UTF-8 make check

%install
export PYTHON=%__python3
#export PYTHON2=no
%makeinstall_std

%if_with ksrc
mkdir -p %buildroot%ksrcdir
install -pm0644 ../kernel-source-%name-%version.tar %buildroot%ksrcdir/
%endif

install -dm0755 %buildroot%_sysconfdir/%name
install -pDm0755 %SOURCE1 %buildroot%_initdir/%name
install -dm0750 %buildroot%_logdir/%name
install -dm0755 %buildroot%_sysconfdir/%name

install -pDm0644 vswitchd/vswitch.ovsschema \
         %buildroot%_datadir/%name/vswitch.ovsschema
install -pDm0644 rhel/etc_logrotate.d_openvswitch \
         %buildroot%_sysconfdir/logrotate.d/%name
install -pDm0644 rhel/usr_share_openvswitch_scripts_sysconfig.template \
         %buildroot/%_sysconfdir/sysconfig/%name
install -pDm0644 rhel/etc_openvswitch_default.conf \
        %buildroot/%_sysconfdir/openvswitch/default.conf

for service in openvswitch ovsdb-server ovs-vswitchd ovs-delete-transient-ports \
                ovn-controller ovn-controller-vtep ovn-northd openvswitch-ipsec; do
    install -pDm0644 \
            rhel/usr_lib_systemd_system_${service}.service \
            %buildroot%_unitdir/${service}.service
done

install -p -D -m 0755 \
        rhel/usr_share_openvswitch_scripts_ovs-systemd-reload \
        %buildroot%_datadir/%name/scripts/ovs-systemd-reload

install -pDm644 %SOURCE12 %buildroot%_tmpfilesdir/%name.conf

# FIXME
%if_with xenserver
install -pDm755 xenserver/etc_init.d_openvswitch-xapi-update \
         %buildroot%_initdir/openvswitch-xapi-update
install -pDm755 xenserver/etc_xapi.d_plugins_openvswitch-cfg-update \
         %buildroot%_sysconfdir/xapi.d/plugins/openvswitch-cfg-update
install -pDm755 xenserver/opt_xensource_libexec_interface-reconfigure \
             %buildroot%_datadir/%name/scripts/interface-reconfigure
install -pDm644 xenserver/opt_xensource_libexec_InterfaceReconfigure.py \
             %buildroot%_datadir/%name/scripts/InterfaceReconfigure.py
install -pDm644 xenserver/opt_xensource_libexec_InterfaceReconfigureBridge.py \
             %buildroot%_datadir/%name/scripts/InterfaceReconfigureBridge.py
install -pDm644 xenserver/opt_xensource_libexec_InterfaceReconfigureVswitch.py \
             %buildroot%_datadir/%name/scripts/InterfaceReconfigureVswitch.py
install -pDm755 xenserver/etc_xensource_scripts_vif \
             %buildroot%_datadir/%name/scripts/vif
install -pDm644 xenserver/usr_share_openvswitch_scripts_sysconfig.template \
         %buildroot%_datadir/%name/scripts/sysconfig.template
install -pDm644 \
        xenserver/usr_lib_xsconsole_plugins-base_XSFeatureVSwitch.py \
               %buildroot%_libdir/xsconsole/plugins-base/XSFeatureVSwitch.py
%endif

install -d -m 0755 %buildroot%python3_sitelibdir_noarch
cp -a %buildroot%_datadir/%name/python/ovstest %buildroot%python3_sitelibdir_noarch

pushd python
export CPPFLAGS="-I ../include"
export LDFLAGS="-L %buildroot%_libdir"
%python_build
%python_install

%python3_build
%python3_install
popd

rm -rf %buildroot%_datadir/%name/python

touch %buildroot%_sysconfdir/%name/conf.db
touch %buildroot%_sysconfdir/%name/system-id.conf
mkdir -p %buildroot%_logdir/%name

# move completions to datadir
mkdir -p %buildroot%_datadir/bash-completion/completions
mv %buildroot%_sysconfdir/bash_completion.d/* %buildroot%_datadir/bash-completion/completions/

# remove unpackaged files
rm -f %buildroot%_bindir/ovs-benchmark \
    %buildroot%_bindir/ovs-parse-backtrace \
    %buildroot%_sbindir/ovs-vlan-bug-workaround \
    %buildroot%_man1dir/ovs-benchmark.1* \
    %buildroot%_man8dir/ovs-parse-backtrace.8* \
    %buildroot%_man8dir/ovs-vlan-bug-workaround.8*

%pre common
%_sbindir/groupadd -r -f %name
%_sbindir/useradd -r -n -g %name -d / -s /sbin/nologin -c 'openvswitch server daemon' %name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS.rst LICENSE NEWS NOTICE README.rst
%_bindir/ovs-dpctl
# exclude python2 script
%exclude %_bindir/ovs-dpctl-top
%_bindir/ovs-testcontroller
%_bindir/ovs-docker
%_bindir/ovs-vsctl
%_bindir/ovsdb-tool
%_sbindir/ovs-vswitchd
%_sbindir/ovsdb-server
%_initdir/%name
%_unitdir/%name.service
%_unitdir/ovs-vswitchd.service
%_unitdir/ovsdb-server.service
%_unitdir/ovs-delete-transient-ports.service
%_tmpfilesdir/%name.conf
%_man1dir/ovsdb-server.1*
%_man1dir/ovsdb-tool.1*
%_man5dir/ovs-vswitchd.conf.db.5*
%_man5dir/ovsdb-server.5*
%_man5dir/ovsdb.5*
%_man7dir/ovs-fields.7*
%_man7dir/ovsdb-server.7*
%_man7dir/ovsdb.7*
%_man7dir/ovs-actions.7*
%_man8dir/ovs-ctl.8*
%_man8dir/ovs-dpctl.8*
%_man8dir/ovs-dpctl-top.8*
%_man8dir/ovs-kmod-ctl.8*
%_man8dir/ovs-testcontroller.8*
%_man8dir/ovs-vsctl.8*
%_man8dir/ovs-vswitchd.8*

%_datadir/%name/vswitch.ovsschema
%_datadir/%name/scripts/ovs-check-dead-ifs
%_datadir/%name/scripts/ovs-lib
%_datadir/%name/scripts/ovs-save
%_datadir/%name/scripts/ovs-ctl
%_datadir/%name/scripts/ovs-kmod-ctl
%_datadir/%name/scripts/ovs-systemd-reload
%dir %_sysconfdir/openvswitch
%config(noreplace) %ghost %_sysconfdir/openvswitch/conf.db
%config(noreplace) %ghost %_sysconfdir/openvswitch/system-id.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/openvswitch/default.conf
%config(noreplace) %_sysconfdir/logrotate.d/openvswitch
%_datadir/bash-completion/completions/*

%if_with debugtools
%files debugtools
%_bindir/ovs-pcap
%_bindir/ovs-tcpdump
%_bindir/ovs-tcpundump
%_man1dir/ovs-pcap.1*
%_man8dir/ovs-tcpdump.8*
%_man1dir/ovs-tcpundump.1*
%python3_sitelibdir_noarch/ovstest
#python2 only tools
#%_sbindir/ovs-bugtool
#%_datadir/%name/bugtool-plugins/
#%_datadir/%name/scripts/ovs-bugtool*
%endif

%files common
%_logdir/%name
%_localstatedir/%name
%_libdir/*.so.*
%_bindir/ovs-appctl

%_bindir/ovs-ofctl
%_bindir/ovs-pki
%_bindir/ovsdb-client
%_man1dir/ovsdb-client.1*
%_man8dir/ovs-appctl.8*
%_man8dir/ovs-ofctl.8*
%_man8dir/ovs-pki.8*

# TODO
%files ipsec
#_initdir/openvswitch-ipsec
%_datadir/openvswitch/scripts/ovs-monitor-ipsec
%_unitdir/openvswitch-ipsec.service

%files vtep
%_bindir/vtep-ctl
%_man5dir/vtep.5.*
%_man8dir/vtep-ctl.8.*
%_datadir/%name/scripts/ovs-vtep
%_datadir/%name/vtep.ovsschema

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc


%files ovn-docker
%_bindir/ovn-docker-overlay-driver
%_bindir/ovn-docker-underlay-driver

%files ovn-common
%_bindir/ovn-nbctl
%_bindir/ovn-sbctl
%_bindir/ovn-trace
%_bindir/ovn-detrace
%_datadir/openvswitch/scripts/ovn-ctl
%_datadir/openvswitch/scripts/ovndb-servers.ocf
# python2 only tools
#%_datadir/openvswitch/scripts/ovn-bugtool-nbctl-show
#%_datadir/openvswitch/scripts/ovn-bugtool-sbctl-lflow-list
#%_datadir/openvswitch/scripts/ovn-bugtool-sbctl-show
%_man1dir/ovn-detrace.1*
%_man8dir/ovn-ctl.8*
%_man8dir/ovn-nbctl.8*
%_man8dir/ovn-trace.8*
%_man7dir/ovn-architecture.7*
%_man8dir/ovn-sbctl.8*
%_man5dir/ovn-nb.5*
%_man5dir/ovn-sb.5*

%files ovn-central
%_bindir/ovn-northd
%_mandir/man8/ovn-northd.8*
%_datadir/openvswitch/ovn-nb.ovsschema
%_datadir/openvswitch/ovn-sb.ovsschema
%_unitdir/ovn-northd.service

%files ovn-host
%_bindir/ovn-controller
%_man8dir/ovn-controller.8*
%_unitdir/ovn-controller.service

%files ovn-vtep
%_bindir/ovn-controller-vtep
%_man8dir/ovn-controller-vtep.8*
%_unitdir/ovn-controller-vtep.service

%files -n python-module-openvswitch
%python_sitelibdir/*

%files -n python3-module-openvswitch
%python3_sitelibdir/*

%if_with ksrc
%files -n kernel-source-%name
%ksrcdir/*
%endif

%changelog
* Fri Jul 10 2020 Anton Farygin <rider@altlinux.ru> 2.12.0-alt4.M90P.1
- openvswitch support for etcnet has been moved to etcnet package

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 2.12.0-alt3.M90P.1
- backport to p9
- revert python2 package

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 2.12.0-alt4
- Add support vlan for ovsport (ALT #38578)
- Add --may-exist option for ovsbond

* Sun Mar 08 2020 Alexey Shabalin <shaba@altlinux.org> 2.12.0-alt3
- Fixed build with python3.8.

* Sun Mar 08 2020 Alexey Shabalin <shaba@altlinux.org> 2.12.0-alt2
- fixed reload services with systemd

* Fri Nov 01 2019 Alexey Shabalin <shaba@altlinux.org> 2.12.0-alt1
- 2.12.0
- switch use from /var/run to /run
- drop python2 support
- move bash completions to main package
- Build openvswitch with dpdk only for list of supported architectures(arei@)

* Wed Jun 05 2019 Alexey Shabalin <shaba@altlinux.org> 2.11.1-alt1
- 2.11.1

* Tue Mar 12 2019 Alexey Shabalin <shaba@altlinux.org> 2.11.0-alt1
- 2.11.0

* Tue Oct 30 2018 Alexey Shabalin <shaba@altlinux.org> 2.10.1-alt1
- 2.10.1

* Thu Sep 13 2018 Anton Farygin <rider@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Fri Jun 01 2018 Anton Farygin <rider@altlinux.ru> 2.9.2-alt1
- 2.9.2
- removed selinux policy subpackage

* Thu Aug 03 2017 Anton Farygin <rider@altlinux.ru> 2.7.2-alt1
- 2.7.2

* Thu Jul 13 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1
- 2.7.1 with security fixes:
  + CVE-2017-9214 Buffer overrread in ofputil_pull_queue_get_config_reply10().
  + CVE-2017-9263 remote DoS attack by a malicious switch.
  + CVE-2017-9265 buffer over-read while parsing the group mod OpenFlow message sent from the controller

* Tue Apr 25 2017 Alexey Shabalin <shaba@altlinux.ru> 2.7.0-alt1
- 2.7.0
- build python3 package
- add ovn packages

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Thu Mar 03 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Fri Oct 02 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- build branch-2.4

* Tue Feb 03 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- build branch-2.3
- add systemd unit
- drop controller, ovsdbmonitor packages
- add vtep and devel packages
- build with --disable-static and --enable-shared
- fixed link shared libs
- backport upstream patches for devel package

* Fri Dec 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.1-alt2
- Add OVS_REMOVE and remove ports and bridges ony if set yes

* Wed Dec 25 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.1-alt1
- Fix runtimedir
- Add %_datadir/%name/scripts/ovs-check-dead-ifs
- Add etcnet support
- Fix initscript for etcnet support

* Sat Dec 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0-alt1
- 2.0
- Remove package brcompat (from upstream v1.10.0)
- Add packages ovsdbmonitor and python-module-openvswitch

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 1.4.1-alt1
- 1.4.1

* Wed Feb 22 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt2
- debugtools subpackage made noarch, optional, and off by default
  (until python part is there)

* Tue Feb 21 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- built for ALT Linux (based on openSUSE 1.2.1-1 spec)
- split into subpackages (largely inspired by debian 1.2.1-3 ones)
- neglected python-related parts for now
- *heavy* spec cleanup, buildreq
- NB: you will need kernel-modules-openvswitch (or linux-3.3+)
