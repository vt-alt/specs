%add_python3_req_skip XenAPI
%add_python3_req_skip __main__
%add_python3_path %_datadir/fence
%allow_python3_import_path %_datadir/fence

Name: fence-agents
Summary: Fence Agents
Version: 4.3.3
Release: alt1
License: GPLv2+ and LGPLv2+
Group: System/Base
Url: http://sourceware.org/cluster/wiki/

Source0: %name-%version.tar.xz

BuildRequires(pre): rpm-build-python3
BuildRequires: autoconf-archive python3-module-pexpect python3-module-pycurl python3-module-requests python3-module-suds sudo xml-utils xsltproc
BuildRequires: python3-module-boto3

%description
Fence Agents is a collection of scripts to handle remote
power management for several devices.

%package common
BuildArch: noarch
Group: System/Base
Summary: Common utilities for fence agents

%description common
Fence Agents is a collection of scripts and libraries to handle remote power management for various devices.

%package alom
BuildArch: noarch
Group: System/Base
Summary: Fence agent for SUN ALOM
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description alom
The fence-agents-apc package contains a fence agent for SUN ALOM

%package apc
BuildArch: noarch
Group: System/Base
Summary: Fence agent for APC devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description apc
The fence-agents-apc package contains a fence agent for APC devices that are accessed via telnet or SSH.

%package apc-snmp
BuildArch: noarch
Group: System/Base
Summary: Fence agent for APC devices (SNMP)
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description apc-snmp
The fence-agents-apc-snmp package contains a fence agent for APC devices that are accessed via the SNMP protocol.

%package amt
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Intel AMT devices
Requires: amtterm
Requires: fence-agents-common = %version-%release

%description amt
The fence-agents-amt package contains a fence agent for AMT compatibile devices that are accessed via 3rd party software.

#%package amt-ws
#BuildArch: noarch
#License: ASL 2.0
#Group: System/Base
#Summary: Fence agent for Intel AMT (WS-Man) devices
#Requires: fence-agents-common >= %version-%release
#Requires: openwsman-python3

#%description amt-ws
#The fence-agents-amt-ws package contains a fence agent for AMT (WS-Man) devices.

%package aws
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Amazon AWS
Requires: fence-agents-common = %version-%release
BuildArch: noarch
Group: System/Base
Obsoletes: fence-agents

%description aws
Fence agent for Amazon AWS instances.

%package azure-arm
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Azure Resource Manager
Requires: fence-agents-common = %version-%release
Requires: python3-module-libcloud
BuildArch: noarch
Group: System/Base
Obsoletes: fence-agents

%description azure-arm
Fence agent for Azure Resource Manager instances.

%package bladecenter
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM BladeCenter
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description bladecenter
The fence-agents-bladecenter package contains a fence agent for IBM BladeCenter devices that are accessed via telnet or SSH.

%package brocade
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Brocade switches
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description brocade
The fence-agents-bladecenter package contains a fence agent for Brocade devices that are accessed via telnet or SSH.

%package cisco-mds
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Cisco MDS 9000 series
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description cisco-mds
The fence-agents-cisco-mds package contains a fence agent for Cisco MDS 9000 series devices that are accessed via the SNMP protocol.

%package cisco-ucs
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Cisco UCS series
Requires: fence-agents-common = %version-%release

%description cisco-ucs
The fence-agents-cisco-ucs package contains a fence agent for Cisco UCS series devices that are accessed via the SNMP protocol.

%package compute
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Nova compute nodes
Requires: fence-agents-common = %version-%release

%description compute
The fence-agents-compute package contains a fence agent for Nova compute nodes.

%package docker
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Docker
Requires: fence-agents-common = %version-%release

%description docker
The fence-agents-docker package contains a fence agent for Docker images that are accessed over HTTP.

%package drac
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Dell DRAC
Requires: telnet
Requires: fence-agents-common = %version-%release

%description drac
The fence-agents-drac package contains a fence agent for Dell DRAC IV series devices that are accessed via telnet.

%package drac5
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Dell DRAC 5
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description drac5
The fence-agents-drac5 package contains a fence agent for Dell DRAC 5 series devices that are accessed via telnet or SSH.

%package eaton-snmp
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Eaton network power switches
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description eaton-snmp
The fence-agents-eaton-snmp package contains a fence agent for Eaton network power switches that are accessed via the SNMP protocol.

%package emerson
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Emerson devices (SNMP)
Requires: fence-agents-common = %version-%release

%description emerson
The fence-agents-emerson package contains a fence agent for Emerson devices that are accessed via the SNMP protocol.

%package eps
BuildArch: noarch
Group: System/Base
Summary: Fence agent for ePowerSwitch 8M+ power switches
Requires: fence-agents-common = %version-%release

%description eps
The fence-agents-eps package contains a fence agent for ePowerSwitch 8M+ power switches that are accessed via the HTTP(s) protocol.

#%package gce
#License: GPLv2+ and LGPLv2+
#Summary: Fence agent for GCE (Google Cloud Engine)
#Requires: fence-agents-common = %version-%release
#Requires: python3-google-api-client
#BuildArch: noarch
#Group: System/Base
#Obsoletes: fence-agents

#%description gce
#Fence agent for GCE (Google Cloud Engine) instances.

%package heuristics-ping
License: GPLv2+ and LGPLv2+
Summary: Pseudo fence agent to affect other agents based on ping-heuristics
Requires: fence-agents-common = %version-%release
BuildArch: noarch
Group: System/Base
Obsoletes: fence-agents

%description heuristics-ping
Fence pseudo agent used to affect other agents based on
ping-heuristics.

%package hpblade
BuildArch: noarch
Group: System/Base
Summary: Fence agent for HP BladeSystem devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description hpblade
The fence-agents-hpblade package contains a fence agent for HP BladeSystem devices that are accessed via telnet or SSH.

%package hds-cb
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Hitachi Compute Blade systems
Requires: telnet
Requires: fence-agents-common = %version-%release

%description hds-cb
The fence-agents-hds-cb package contains a fence agent for Hitachi Compute Blades that are accessed via telnet.

%package ibmblade
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM BladeCenter
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description ibmblade
The fence-agents-ibmblade package contains a fence agent for IBM BladeCenter devices that are accessed via the SNMP protocol.

%package ifmib
BuildArch: noarch
Group: System/Base
Summary: Fence agent for devices with IF-MIB interfaces
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description ifmib
The fence-agents-ifmib package contains a fence agent for IF-MIB interfaces that are accessed via the SNMP protocol.

%package ilo2
BuildArch: noarch
Group: System/Base
Summary: Fence agent for HP iLO2 devices
Requires: gnutls-utils
Requires: fence-agents-common = %version-%release

%description ilo2
The fence-agents-ilo2 package contains a fence agent for HP iLO2 devices that are accessed via the HTTP(s) protocol.

%package ilo-mp
BuildArch: noarch
Group: System/Base
Summary: Fence agent for HP iLO MP devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description ilo-mp
The fence-agents-ilo-mp package contains a fence agent for HP iLO MP devices that are accessed via telnet or SSH.

%package ilo-moonshot
BuildArch: noarch
Group: System/Base
Summary: Fence agent for HP iLO Moonshot devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description ilo-moonshot
The fence-agents-ilo-moonshot package contains a fence agent for HP iLO Moonshot devices that are accessed via telnet or SSH.

%package ilo-ssh
BuildArch: noarch
Group: System/Base
Summary: Fence agent for HP iLO devices over SSH
Requires: openssh-clients
Requires: fence-agents-common = %version-%release

%description ilo-ssh
The fence-agents-ilo-ssh package contains a fence agent for HP iLO devices that are accessed via telnet or SSH.

%package intelmodular
BuildArch: noarch
Group: System/Base
Summary: Fence agent for devices with Intel Modular interfaces
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description intelmodular
The fence-agents-intelmodular package contains a fence agent for Intel Modular interfaces that are accessed via the SNMP protocol.

%package ipdu
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM iPDU network power switches
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description ipdu
The fence-agents-ipdu package contains a fence agent for IBM iPDU network power switches that are accessed via the SNMP protocol.

%package ipmilan
BuildArch: noarch
Group: System/Base
Summary: Fence agent for devices with IPMI interface
Requires: ipmitool
Requires: fence-agents-common = %version-%release

%description ipmilan
The fence-agents-ipmilan package contains a fence agent for devices with IPMI interface.

%package ironic
License: GPLv2+ and LGPLv2+
Summary: Fence agent for OpenStack's Ironic (Bare Metal as a service)
Requires: /usr/bin/openstack
Requires: fence-agents-common = %version-%release
BuildArch: noarch
Group: System/Base

%description ironic
Fence agent for OpenStack's Ironic (Bare Metal as a service) service.

%package kdump
Group: System/Base
Summary: Fence agent for use with kdump crash recovery service
Requires: fence-agents-common = %version-%release

%description kdump
The fence-agents-kdump package contains a fence agent for use with kdump crash recovery service.

%package ldom
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Sun LDom virtual machines
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description ldom
The fence-agents-ldom package contains a fence agent for APC devices that are accessed via telnet or SSH.

%package lpar
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM LPAR
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description lpar
The fence-agents-lpar package contains a fence agent for IBM LPAR devices that are accessed via telnet or SSH.

%package mpath
BuildArch: noarch
Group: System/Base
Summary: Fence agent for reservations over Device Mapper Multipath
Requires: multipath-tools
Requires: fence-agents-common = %version-%release

%description mpath
The fence-agents-mpath package contains fence agent for SCSI persisent reservation over Device Mapper Multipath.

%package netio
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Koukaam NETIO devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description netio
The fence-agents-netio package contains a fence agent for Koukaam NETIO devices that are accessed via telnet or SSH.

%package ovh
BuildArch: noarch
Group: System/Base
Summary: Fence agent for OVH provider
Requires: fence-agents-common = %version-%release

%description ovh
The fence-agents-apc package contains a fence agent for OVH hosting provider.

%package powerman
BuildArch: noarch
Group: System/Base
Summary: Fence agent for APC devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description powerman
The fence-agents-powerman package contains a fence agent for Powerman devices that are accessed via telnet or SSH.

%package pve
BuildArch: noarch
Group: System/Base
Summary: Fence agent for PVE
Requires: fence-agents-common = %version-%release

%description pve
The fence-agents-apc package contains a fence agent for PVE.

%package raritan
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Raritan Dominion PX
Requires: fence-agents-common = %version-%release

%description raritan
The fence-agents-apc package contains a fence agent for Raritan Dominion PX.

%package rcd-serial
BuildArch: noarch
Group: System/Base
Summary: Fence agent for RCD serial
Requires: fence-agents-common = %version-%release

%description rcd-serial
The fence-agents-apc package contains a fence agent for RCD serial.

%package rhevm
BuildArch: noarch
Group: System/Base
Summary: Fence agent for RHEV-M
Requires: fence-agents-common = %version-%release

%description rhevm
The fence-agents-rhevm package contains a fence agent for RHEV-M via REST API.

%package rsa
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM RSA II
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description rsa
The fence-agents-rsa package contains a fence agent for IBM RSA II devices that are accessed via telnet or SSH.

%package rsb
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Fujitsu RSB
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description rsb
The fence-agents-rsb package contains a fence agent for Fujitsu RSB devices that are accessed via telnet or SSH.

%package sanbox2
BuildArch: noarch
Group: System/Base
Summary: Fence agent for QLogic SANBox2 FC switches
Requires: telnet
Requires: fence-agents-common = %version-%release

%description sanbox2
The fence-agents-sanbox2 package contains a fence agent for QLogic SANBox2 switches that are accessed via telnet.

%package sbd
License: GPLv2+ and LGPLv2+
Summary: Fence agent for SBD (storage-based death)
#Requires: sbd
Requires: fence-agents-common = %version-%release
BuildArch: noarch
Group: System/Base

%description sbd
Fence agent for SBD (storage-based death).

%package scsi
BuildArch: noarch
Group: System/Base
Summary: Fence agent for SCSI persisent reservations
Requires: sg3_utils
Requires: fence-agents-common = %version-%release

%description scsi
The fence-agents-scsi package contains fence agent for SCSI persisent reservations.

%package vbox
BuildArch: noarch
Group: System/Base
Summary: Fence agent for VirtualBox
Requires: openssh-clients
Requires: fence-agents-common = %version-%release

%description vbox
The fence-agents-vbox package contains a fence agent for VirtualBox dom0 accessed via SSH.

%package virsh
BuildArch: noarch
Group: System/Base
Summary: Fence agent for virtual machines based on libvirt
Requires: openssh-clients libvirt-client
Requires: fence-agents-common = %version-%release

%description virsh
The fence-agents-virsh package contains a fence agent for virtual machines that are accessed via SSH.

%package vmware
BuildArch: noarch
Group: System/Base
Summary: Fence agent for VMWare with VI Perl Toolkit or vmrun
Requires: fence-agents-common = %version-%release

%description vmware
The fence-agents-vmware package contains a fence agent for VMWare accessed with VI Perl Toolkit or vmrun.

%package vmware-rest
License: GPLv2+ and LGPLv2+
Summary: Fence agent for VMWare with REST API
Requires: fence-agents-common = %version-%release
BuildArch: noarch
Group: System/Base
Obsoletes: fence-agents

%description vmware-rest
Fence agent for VMWare with REST API.

%package vmware-soap
BuildArch: noarch
Group: System/Base
Summary: Fence agent for VMWare with SOAP API v4.1+
Requires: fence-agents-common = %version-%release

%description vmware-soap
The fence-agents-vmware-soap package contains a fence agent for VMWare with SOAP API v4.1+

%package vmware-vcloud
License: GPLv2+ and LGPLv2+
Summary: Fence agent for VMWare vCloud Director
Requires: fence-agents-common = %version-%release
BuildArch: noarch
Group: System/Base
Obsoletes: fence-agents

%description vmware-vcloud
Fence agent for VMWare vCloud Director.

%package wti
BuildArch: noarch
Group: System/Base
Summary: Fence agent for WTI Network power switches
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description wti
The fence-agents-wti package contains a fence agent for WTI network power switches that are accessed via telnet or SSH.

%package xenapi
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Citrix XenServer over XenAPI
Requires: fence-agents-common = %version-%release

%description xenapi
The fence-agents-xenapi package contains a fence agent for Citrix XenServer accessed over XenAPI.

%package zvm
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM z/VM over IP
Requires: fence-agents-common = %version-%release

%description zvm
The fence-agents-zvm package contains a fence agent for IBM z/VM over IP.

%prep
%setup

sed -i '/^.*pywsman.*/d' configure.ac

%build
%autoreconf
export PYTHON="/usr/bin/python3"
%configure --localstatedir=%_var
%make_build

%install
%make DESTDIR=%buildroot install

rm  %buildroot%_sbindir/fence_aliyun
rm  %buildroot%_man8dir/fence_aliyun.8*
ln -sf ../../sbin/fence_scsi %buildroot%_datadir/cluster/fence_scsi_check
ln -sf ../../sbin/fence_scsi %buildroot%_datadir/cluster/fence_scsi_check_hardreboot

%files common
%_defaultdocdir/%name
%_datadir/fence
%_datadir/cluster
%exclude %_datadir/fence/azure_fence.*
%exclude %_datadir/cluster/fence_scsi_check*
%exclude %_sbindir/fence_ack_manual
%exclude %_man8dir/fence_ack_manual.8*
%exclude %_sbindir/fence_dummy
%exclude %_man8dir/fence_dummy.8*
%exclude %_sbindir/fence_zvm
%exclude %_man8dir/fence_zvm.8*

%files alom
%_sbindir/fence_alom
%_man8dir/fence_alom.8*

%files apc
%_sbindir/fence_apc
%_man8dir/fence_apc.8*

%files apc-snmp
%_sbindir/fence_apc_snmp
%_man8dir/fence_apc_snmp.8*
%_sbindir/fence_tripplite_snmp
%_man8dir/fence_tripplite_snmp.8*

%files amt
%_sbindir/fence_amt
%_man8dir/fence_amt.8*

#%files amt-ws
#%_sbindir/fence_amt_ws
#%_man8dir/fence_amt_ws.8*

%files aws
%_sbindir/fence_aws
%_man8dir/fence_aws.8*

%files azure-arm
%_sbindir/fence_azure_arm
%_datadir/fence/azure_fence.py*
%_man8dir/fence_azure_arm.8*

%files bladecenter
%_sbindir/fence_bladecenter
%_man8dir/fence_bladecenter.8*

%files brocade
%_sbindir/fence_brocade
%_man8dir/fence_brocade.8*

%files cisco-mds
%_sbindir/fence_cisco_mds
%_man8dir/fence_cisco_mds.8*

%files cisco-ucs
%_sbindir/fence_cisco_ucs
%_man8dir/fence_cisco_ucs.8*

%files compute
%_sbindir/fence_compute
%_man8dir/fence_compute.8*
%_sbindir/fence_evacuate
%_man8dir/fence_evacuate.8*

%files docker
%_sbindir/fence_docker
%_man8dir/fence_docker.8*

%files drac
%_sbindir/fence_drac
%_man8dir/fence_drac.8*

%files drac5
%_sbindir/fence_drac5
%_man8dir/fence_drac5.8*

%files eaton-snmp
%_sbindir/fence_eaton_snmp
%_man8dir/fence_eaton_snmp.8*

%files emerson
%_sbindir/fence_emerson
%_man8dir/fence_emerson.8*

%files eps
%_sbindir/fence_eps
%_man8dir/fence_eps.8*

#%files gce
#%_sbindir/fence_gce
#%_man8dir/fence_gce.8*

%files heuristics-ping
%_sbindir/fence_heuristics_ping
%_man8dir/fence_heuristics_ping.8*

%files hpblade
%_sbindir/fence_hpblade
%_man8dir/fence_hpblade.8*

%files hds-cb
%_sbindir/fence_hds_cb
%_man8dir/fence_hds_cb.8*

%files ibmblade
%_sbindir/fence_ibmblade
%_man8dir/fence_ibmblade.8*

%files ifmib
%_sbindir/fence_ifmib
%_man8dir/fence_ifmib.8*

%files ilo2
%_sbindir/fence_ilo
%_sbindir/fence_ilo2
%_man8dir/fence_ilo.8*
%_man8dir/fence_ilo2.8*

%files ilo-mp
%_sbindir/fence_ilo_mp
%_man8dir/fence_ilo_mp.8*

%files ilo-moonshot
%_sbindir/fence_ilo_moonshot
%_man8dir/fence_ilo_moonshot.8*

%files ilo-ssh
%_sbindir/fence_ilo_ssh
%_man8dir/fence_ilo_ssh.8*
%_sbindir/fence_ilo3_ssh
%_man8dir/fence_ilo3_ssh.8*
%_sbindir/fence_ilo4_ssh
%_man8dir/fence_ilo4_ssh.8*
%_sbindir/fence_ilo5_ssh
%_man8dir/fence_ilo5_ssh.8*

%files intelmodular
%_sbindir/fence_intelmodular
%_man8dir/fence_intelmodular.8*

%files ipdu
%_sbindir/fence_ipdu
%_man8dir/fence_ipdu.8*

%files ipmilan
%_sbindir/fence_ipmilan
%_man8dir/fence_ipmilan.8*
%_sbindir/fence_idrac
%_man8dir/fence_idrac.8*
%_sbindir/fence_ilo3
%_man8dir/fence_ilo3.8*
%_sbindir/fence_ilo4
%_man8dir/fence_ilo4.8*
%_sbindir/fence_ilo5
%_man8dir/fence_ilo5.8*
%_sbindir/fence_imm
%_man8dir/fence_imm.8*

%files ironic
%_sbindir/fence_ironic
%_man8dir/fence_ironic.8*

%files kdump
%_sbindir/fence_kdump
%_libexecdir/fence_kdump_send
%_man8dir/fence_kdump.8*
%_man8dir/fence_kdump_send.8*

%files ldom
%_sbindir/fence_ldom
%_man8dir/fence_ldom.8*

%files lpar
%_sbindir/fence_lpar
%_man8dir/fence_lpar.8*

%files mpath
%_sbindir/fence_mpath
%_man8dir/fence_mpath.8*

%files netio
%_sbindir/fence_netio
%_man8dir/fence_netio.8*

%files ovh
%_sbindir/fence_ovh
%_man8dir/fence_ovh.8*

%files powerman
%_sbindir/fence_powerman
%_man8dir/fence_powerman.8*

%files pve
%_sbindir/fence_pve
%_man8dir/fence_pve.8*

%files raritan
%_sbindir/fence_raritan
%_man8dir/fence_raritan.8*

%files rcd-serial
%_sbindir/fence_rcd_serial
%_man8dir/fence_rcd_serial.8*

%files rhevm
%_sbindir/fence_rhevm
%_man8dir/fence_rhevm.8*

%files rsa
%_sbindir/fence_rsa
%_man8dir/fence_rsa.8*

%files rsb
%_sbindir/fence_rsb
%_man8dir/fence_rsb.8*

%files sanbox2
%_sbindir/fence_sanbox2
%_man8dir/fence_sanbox2.8*

%files sbd
%_sbindir/fence_sbd
%_man8dir/fence_sbd.8*

%files scsi
%_sbindir/fence_scsi
%_datadir/cluster/fence_scsi_check*
%_man8dir/fence_scsi.8*

%files vbox
%_sbindir/fence_vbox
%_man8dir/fence_vbox.8*

%files virsh
%_sbindir/fence_virsh
%_man8dir/fence_virsh.8*

%files vmware
%_sbindir/fence_vmware
%_man8dir/fence_vmware.8*

%files vmware-rest
%_sbindir/fence_vmware_rest
%_man8dir/fence_vmware_rest.8*

%files vmware-soap
%_sbindir/fence_vmware_soap
%_man8dir/fence_vmware_soap.8*

%files vmware-vcloud
%_sbindir/fence_vmware_vcloud
%_man8dir/fence_vmware_vcloud.8*

%files wti
%_sbindir/fence_wti
%_man8dir/fence_wti.8*

%files xenapi
%_sbindir/fence_xenapi
%_man8dir/fence_xenapi.8*

%files zvm
%_sbindir/fence_zvmip
%_man8dir/fence_zvmip.8*

%changelog
* Wed May 08 2019 Andrew A. Vasilyev <andy@altlinux.org> 4.3.3-alt1
- 4.3.3
- Add gce, ironic, openstack, powerman, vmware-vcloud modules.

* Fri Jan 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.24-alt3
- Fixed localstatedir location.

* Wed Apr 19 2017 Sergey Novikov <sotor@altlinux.org> 4.0.24-alt2
- fix fence-pve

* Thu Apr 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.24-alt1
- initial release

