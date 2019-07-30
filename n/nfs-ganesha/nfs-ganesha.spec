%def_with nfsidmap
%def_with systemd

# TODO: rewrite these crazy global macros

# Conditionally enable some FSALs, disable others.
#
# 1. rpmbuild accepts these options (gpfs as example):
#    --with gpfs
#    --without gpfs

%define on_off_switch() %%{?_with_%1:ON}%%{?!_with_%1:OFF}

# A few explanation about %%bcond_with and %%bcond_without
# /!\ be careful: this syntax can be quite messy
# %%bcond_with means you add a "--with" option, default = without this feature
# %%bcond_without adds a"--without" so the feature is enabled by default

%def_without nullfs
%global use_fsal_null %{on_off_switch nullfs}

%def_without gpfs
%global use_fsal_gpfs %{on_off_switch gpfs}

%def_without xfs
%global use_fsal_xfs %{on_off_switch xfs}

%def_without ceph
%global use_fsal_ceph %{on_off_switch ceph}

%def_without lustre
%global use_fsal_lustre %{on_off_switch lustre}

%def_without mem
%global use_fsal_mem %{on_off_switch mem}

%def_without shook
%global use_fsal_shook %{on_off_switch shook}

%def_without gluster
%global use_fsal_gluster %{on_off_switch gluster}

%def_without hpss
%global use_fsal_hpss %{on_off_switch hpss}

%def_without panfs
%global use_fsal_panfs %{on_off_switch panfs}

%def_without pt
%global use_fsal_pt %{on_off_switch pt}

%def_without rdma
%global use_rdma %{on_off_switch rdma}

%def_with jemalloc

%def_without lustre_up
%global use_lustre_up %{on_off_switch lustre_up}

%def_without lttng
%global use_lttng %{on_off_switch lttng}

%def_without utils
%global use_utils %{on_off_switch utils}

%def_without gui_utils
%global use_gui_utils %{on_off_switch gui_utils}

%def_with system_ntirpc
%global use_system_ntirpc %{on_off_switch system_ntirpc}

Name: nfs-ganesha
Version: 2.7.3
Release: alt1

Summary: NFS-Ganesha is a NFS Server running in user space

Group: System/Servers
License: LGPLv3+
Url: https://github.com/nfs-ganesha/nfs-ganesha/wiki

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/nfs-ganesha/nfs-ganesha/archive/V%version.tar.gz
Source: %name-%version.tar

BuildRequires: rpm-macros-intro-conflicts

BuildRequires: cmake gcc-c++
BuildRequires: bison
BuildRequires: flex
BuildRequires: pkg-config
BuildRequires: libkrb5-devel
BuildRequires: libdbus-devel
BuildRequires: libcap-devel
BuildRequires: libblkid-devel
BuildRequires: libuuid-devel
%if_with ceph
BuildRequires: librados2-devel
%endif
%if_with system_ntirpc
BuildRequires: libntirpc-devel >= 1.7.0
%endif
Requires: dbus
Requires: nfs-utils
%if_with nfsidmap
BuildRequires: libnfsidmap-devel
%else
BuildRequires: nfs-utils-lib-devel
%endif
%if_with rdma
BuildRequires: libmooshika-devel >= 0.6-0
%endif
%if_with jemalloc
BuildRequires: libjemalloc-devel
%endif
%if_with lustre_up
BuildRequires: lcap-devel >= 0.1-0
%endif
%if_with systemd
BuildRequires: udev-rules
Requires(post): udev-rules
Requires(preun): udev-rules
Requires(postun): udev-rules
%else
BuildRequires: initscripts
%endif

# Use CMake variables

%description
nfs-ganesha : NFS-GANESHA is a NFS Server running in user space.
It comes with various back-end modules (called FSALs) provided as
shared objects to support different file systems and name-spaces.

%package mount-9P
Summary: a 9p mount helper
Group: System/Servers

%description mount-9P
This package contains the mount.9P script that clients can use
to simplify mounting to NFS-GANESHA. This is a 9p mount helper.

%package vfs
Summary: The NFS-GANESHA's VFS FSAL
Group: System/Servers
BuildRequires: libattr-devel
Requires: nfs-ganesha = %version-%release

%description vfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support VFS based filesystems

%package proxy
Summary: The NFS-GANESHA's PROXY FSAL
Group: System/Servers
BuildRequires: libattr-devel
Requires: nfs-ganesha = %version-%release

%description proxy
This package contains a FSAL shared object to
be used with NFS-Ganesha to support PROXY based filesystems

%if_with utils
%package utils
Summary: The NFS-GANESHA's util scripts
Group: System/Servers
Requires: dbus-python, pygobject2
#if_with gui_utils
#BuildRequires: PyQt4-devel
#Requires: PyQt4
#endif
Requires: nfs-ganesha = %version-%release, python

%description utils
This package contains utility scripts for managing the NFS-GANESHA server
%endif

%if_with lttng
%package lttng
Summary: The NFS-GANESHA's library for use with LTTng
Group: System/Servers
BuildRequires: lttng-ust-devel >= 2.3
Requires: nfs-ganesha = %version-%release, lttng-tools >= 2.3,  lttng-ust >= 2.3

%description lttng
This package contains the libganesha_trace.so library. When preloaded
to the ganesha.nfsd server, it makes it possible to trace using LTTng.
%endif

# Option packages start here. use "rpmbuild --with lustre" (or equivalent)
# for activating this part of the spec file

# NULL
%if_with nullfs
%package nullfs
Summary: The NFS-GANESHA's NULLFS Stackable FSAL
Group: System/Servers
Requires: nfs-ganesha = %version-%release

%description nullfs
This package contains a Stackable FSAL shared object to
be used with NFS-Ganesha. This is mostly a template for future (more sophisticated) stackable FSALs
%endif

# GPFS
%if_with gpfs
%package gpfs
Summary: The NFS-GANESHA's GPFS FSAL
Group: System/Servers
Requires: nfs-ganesha = %version-%release

%description gpfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support GPFS backend
%endif

# CEPH
%if_with ceph
%package ceph
Summary: The NFS-GANESHA's CEPH FSAL
Group: System/Servers
Requires: nfs-ganesha = %version-%release
Requires: ceph >= 0.78
BuildRequires: ceph-devel >= 0.78

%description ceph
This package contains a FSAL shared object to
be used with NFS-Ganesha to support CEPH
%endif

# LUSTRE
%if_with lustre
%package lustre
Summary: The NFS-GANESHA's LUSTRE FSAL
Group: System/Servers
Requires: nfs-ganesha = %version-%release
Requires: lustre
BuildRequires: libattr-devel lustre

%description lustre
This package contains a FSAL shared object to
be used with NFS-Ganesha to support LUSTRE
%endif

# SHOOK
%if_with shook
%package shook
Summary: The NFS-GANESHA's LUSTRE/SHOOK FSAL
Group: System/Servers
Requires: nfs-ganesha = %version-%release
Requires: lustre shook-client
BuildRequires: libattr-devel lustre shook-devel

%description shook
This package contains a FSAL shared object to
be used with NFS-Ganesha to support LUSTRE via SHOOK
%endif

# XFS
%if_with xfs
%package xfs
Summary: The NFS-GANESHA's XFS FSAL
Group: System/Servers
Requires: nfs-ganesha = %version-%release
BuildRequires: libattr-devel xfsprogs-devel

%description xfs
This package contains a shared object to be used with FSAL_VFS
to support XFS correctly
%endif

# HPSS
%if_with hpss
%package hpss
Summary: The NFS-GANESHA's HPSS FSAL
Group: System/Servers
Requires: nfs-ganesha = %version-%release
#BuildRequires:	hpssfs

%description hpss
This package contains a FSAL shared object to
be used with NFS-Ganesha to support HPSS
%endif

# PANFS
%if_with panfs
%package panfs
Summary: The NFS-GANESHA's PANFS FSAL
Group: System/Servers
Requires: nfs-ganesha = %version-%release

%description panfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support PANFS
%endif

# PT
%if_with pt
%package pt
Summary: The NFS-GANESHA's PT FSAL
Group: System/Servers
Requires: nfs-ganesha = %version-%release

%description pt
This package contains a FSAL shared object to
be used with NFS-Ganesha to support PT
%endif

# GLUSTER
%if_with gluster
%package gluster
Summary: The NFS-GANESHA's GLUSTER FSAL
Group: System/Servers
Requires: nfs-ganesha = %version-%release
BuildRequires: glusterfs-api-devel >= 3.7.4
BuildRequires: libattr-devel, libacl-devel

%description gluster
This package contains a FSAL shared object to
be used with NFS-Ganesha to support Gluster
%endif

%prep
%setup
rm -rf contrib/libzfswrapper
%__subst "s|-Werror||g" src/cmake/maintainer_mode.cmake

%build
cd src && %cmake_insource -DCMAKE_BUILD_TYPE=Debug		\
	-DBUILD_CONFIG=rpmbuild				\
	-DUSE_FSAL_NULL=%use_fsal_null		\
	-DUSE_FSAL_ZFS=NO				\
	-DUSE_FSAL_XFS=%use_fsal_xfs			\
	-DUSE_FSAL_CEPH=%use_fsal_ceph		\
	-DUSE_FSAL_LUSTRE=%use_fsal_lustre		\
	-DUSE_FSAL_MEM=%use_fsal_mem			\
	-DUSE_FSAL_SHOOK=%use_fsal_shook		\
	-DUSE_FSAL_GPFS=%use_fsal_gpfs		\
	-DUSE_FSAL_HPSS=%use_fsal_hpss		\
	-DUSE_FSAL_PANFS=%use_fsal_panfs		\
	-DUSE_FSAL_PT=%use_fsal_pt			\
	-DUSE_FSAL_GLUSTER=%use_fsal_gluster		\
	-DUSE_SYSTEM_NTIRPC=%use_system_ntirpc	\
	-DUSE_9P_RDMA=%use_rdma			\
	-DUSE_FSAL_LUSTRE_UP=%use_lustre_up		\
	-DUSE_LTTNG=%use_lttng			\
	-DUSE_ADMIN_TOOLS=%use_utils			\
	-DUSE_GUI_ADMIN_TOOLS=%use_gui_utils		\
	-DUSE_FSAL_VFS=ON				\
	-DUSE_FSAL_PROXY=ON				\
	-DUSE_DBUS=ON					\
	-DUSE_9P=ON					\
	-DDISTNAME_HAS_GIT_DATA=OFF			\
%if_with jemalloc
	-DALLOCATOR=jemalloc
%endif

%make_build

%install
mkdir -p %buildroot%_sysconfdir/ganesha/
mkdir -p %buildroot%_sysconfdir/dbus-1/system.d
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_sysconfdir/logrotate.d
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_libdir/ganesha
mkdir -p %buildroot%_runtimedir/ganesha

cd src
install -m 644 config_samples/logrotate_ganesha	%buildroot%_sysconfdir/logrotate.d/ganesha
install -m 644 scripts/ganeshactl/org.ganesha.nfsd.conf	%buildroot%_sysconfdir/dbus-1/system.d
install -m 755 tools/mount.9P	%buildroot%_sbindir/mount.9P

install -m 644 config_samples/vfs.conf %buildroot%_sysconfdir/ganesha

%if_with systemd
mkdir -p %buildroot%_unitdir
install -m 644 scripts/systemd/nfs-ganesha.service.el7	%buildroot%_unitdir/nfs-ganesha.service
%__subst "s|/run/sysconfig|/etc/sysconfig|g" %buildroot%_unitdir/nfs-ganesha.service
install -m 644 scripts/systemd/nfs-ganesha-lock.service.el7	%buildroot%_unitdir/nfs-ganesha-lock.service
%__subst "s|/run/sysconfig|/etc/sysconfig|g" %buildroot%_unitdir/nfs-ganesha-lock.service
install -m 644 scripts/systemd/sysconfig/nfs-ganesha	%buildroot%_sysconfdir/sysconfig/ganesha
%else
mkdir -p %buildroot%_sysconfdir/init.d
install -m 755 scripts/init.d/nfs-ganesha.el6		%buildroot%_sysconfdir/init.d/nfs-ganesha
install -m 644 scripts/init.d/sysconfig/ganesha		%buildroot%_sysconfdir/sysconfig/ganesha
%endif

%if_with pt
install -m 644 config_samples/pt.conf %buildroot%_sysconfdir/ganesha
%endif

%if_with xfs
install -m 644 config_samples/xfs.conf %buildroot%_sysconfdir/ganesha
%endif

%if_with ceph
install -m 644 config_samples/ceph.conf %buildroot%_sysconfdir/ganesha
%endif

%if_with lustre
install -m 755 config_samples/lustre.conf %buildroot%_sysconfdir/ganesha
%endif

%if_with gpfs
install -m 644 config_samples/gpfs.conf	%buildroot%_sysconfdir/ganesha
install -m 644 config_samples/gpfs.ganesha.nfsd.conf %buildroot%_sysconfdir/ganesha
install -m 644 config_samples/gpfs.ganesha.main.conf %buildroot%_sysconfdir/ganesha
install -m 644 config_samples/gpfs.ganesha.log.conf %buildroot%_sysconfdir/ganesha
install -m 644 config_samples/gpfs.ganesha.exports.conf	%buildroot%_sysconfdir/ganesha
#if_without systemd
#mkdir -p %buildroot%_sysconfdir/init.d
#install -m 755 scripts/init.d/nfs-ganesha.gpfs		%buildroot%_sysconfdir/init.d/nfs-ganesha-gpfs
#endif
%endif

%makeinstall_std
install -m 644 ChangeLog	%buildroot%_docdir/ganesha

# ganesha-rados-grace tool for interacting with the database used by the rados_cluster recovery backend.
rm -f %buildroot%_bindir/ganesha-rados-grace

%files
%doc src/LICENSE.txt
%_bindir/ganesha.nfsd
%if_without system_ntirpc
%_libdir/libntirpc.so.1.3.0
%_libdir/libntirpc.so.1.3
%_libdir/libntirpc.so
%_pkgconfigdir/libntirpc.pc
%_includedir/ntirpc/
%endif
%config %_sysconfdir/dbus-1/system.d/org.ganesha.nfsd.conf
%config(noreplace) %_sysconfdir/sysconfig/ganesha
%config(noreplace) %_sysconfdir/logrotate.d/ganesha
%dir %_sysconfdir/ganesha/
%config(noreplace) %_sysconfdir/ganesha/ganesha.conf
%dir %_docdir/ganesha/
%_docdir/ganesha/*
%doc %_docdir/ganesha/ChangeLog
%dir %_runtimedir/ganesha

%if_with systemd
%_unitdir/nfs-ganesha.service
%_unitdir/nfs-ganesha-lock.service
%else
%_sysconfdir/init.d/nfs-ganesha
%endif

%files mount-9P
%_sbindir/mount.9P

%files vfs
%_libdir/ganesha/libfsalvfs*
%config(noreplace) %_sysconfdir/ganesha/vfs.conf

%files proxy
%_libdir/ganesha/libfsalproxy*

# Optional packages
%if_with nullfs
%files nullfs
%_libdir/ganesha/libfsalnull*
%endif

%if_with gpfs
%files gpfs
%_libdir/ganesha/libfsalgpfs*
%config(noreplace) %_sysconfdir/ganesha/gpfs.conf
%config(noreplace) %_sysconfdir/ganesha/gpfs.ganesha.nfsd.conf
%config(noreplace) %_sysconfdir/ganesha/gpfs.ganesha.main.conf
%config(noreplace) %_sysconfdir/ganesha/gpfs.ganesha.log.conf
%config(noreplace) %_sysconfdir/ganesha/gpfs.ganesha.exports.conf
#if_without systemd
#%_sysconfdir/init.d/nfs-ganesha-gpfs
#endif
%endif

%if_with xfs
%files xfs
%_libdir/ganesha/libfsalxfs*
%config(noreplace) %_sysconfdir/ganesha/xfs.conf
%endif

%if_with ceph
%files ceph
%_libdir/ganesha/libfsalceph*
%config(noreplace) %_sysconfdir/ganesha/ceph.conf
%endif

%if_with lustre
%files lustre
%config(noreplace) %_sysconfdir/ganesha/lustre.conf
%_libdir/ganesha/libfsallustre*
%endif

%if_with shook
%files shook
%_libdir/ganesha/libfsalshook*
%endif

%if_with gluster
%files gluster
%_libdir/ganesha/libfsalgluster*
%endif

%if_with hpss
%files hpss
%_libdir/ganesha/libfsalhpss*
%endif

%if_with panfs
%files panfs
%_libdir/ganesha/libfsalpanfs*
%endif

%if_with pt
%files pt
%_libdir/ganesha/libfsalpt*
%config(noreplace) %_sysconfdir/ganesha/pt.conf
%endif

%if_with lttng
%files lttng
%_libdir/ganesha/libganesha_trace*
%endif

%if_with utils
%files utils
%python_sitelibdir/Ganesha/*
%python_sitelibdir/ganeshactl-*-info
#%if_with gui_utils
#%_bindir/ganesha-admin
#%_bindir/manage_clients
#%_bindir/manage_exports
#%_bindir/manage_logger
#%_bindir/ganeshactl
#%_bindir/client_stats_9pOps
#%_bindir/export_stats_9pOps
#%endif
%_bindir/fake_recall
%_bindir/get_clientids
%_bindir/grace_period
%_bindir/purge_gids
%_bindir/ganesha_stats
%_bindir/sm_notify.ganesha
%_bindir/ganesha_mgr
%endif

%changelog
* Thu May 30 2019 Vitaly Lipatov <lav@altlinux.ru> 2.7.3-alt1
- new version 2.7.3 (with rpmrb script)

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 2.7.2-alt1
- new version 2.7.2 (with rpmrb script)

* Fri Jan 11 2019 Michael Shigorin <mike@altlinux.org> 2.7.1-alt2
- extended ceph knob (BR: librados2-devel might be a problem)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.7.1-alt1
- new version 2.7.1 (with rpmrb script)

* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 2.7.0-alt1
- new version 2.7.0 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2.6.2-alt1
- new version 2.6.2 (with rpmrb script)

* Tue Mar 27 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.4-alt2
- libnfsidmap soname bump

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.4-alt1
- new version 2.5.4 (with rpmrb script)

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.3-alt1
- new version 2.5.3 (with rpmrb script)

* Wed Oct 18 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt3
- add rpm-build-intro buildreq (fix /var/lib/run)

* Tue Aug 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt2
- build with new libntirpc 1.5.3

* Sun Jun 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0

* Mon Dec 05 2016 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 2.4.0.1-alt1
- new version 2.4.0.1 (with rpmrb script)

* Sun Jul 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt0.dev26
- new version (2.4.0-dev26) with rpmgs script

* Fri Jul 22 2016 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- new version 2.3.2 (with rpmrb script)

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- initial build for ALT Linux Sisyphus

* Wed Oct 28 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-1
- 2.3.0 GA

* Tue Oct 27 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.15rc8
- 2.3.0 RC8, rebuild with libntirpc-1.3.1, again

* Mon Oct 26 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.14rc8
- 2.3.0 RC8, rebuild with libntirpc-1.3.1

* Sun Oct 25 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.13rc8
- 2.3.0 RC8

* Thu Oct 22 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.12rc7
- 2.3.0 RC7 (N.B. 2.3.0-0.11rc6 was really rc7)

* Mon Oct 19 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.11rc7
- 2.3.0 RC7

* Mon Oct 12 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.10rc6
- 2.3.0 RC6

* Thu Oct 8 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.9rc5
- 2.3.0 RC5 w/ CMakeLists.txt.patch and config-h.in.cmake.patch

* Wed Oct 7 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.8rc5
- 2.3.0 RC5 mount-9p w/o Requires: nfs-ganesha

* Tue Oct 6 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.7rc5
- 2.3.0 RC5 revised scripts/ganeshactl/CMakeLists.txt.patch

* Mon Oct 5 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.6rc5
- 2.3.0 RC5

* Mon Sep 28 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.5rc4
- 2.3.0 RC4

* Fri Sep 18 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.4rc3
- 2.3.0 RC3

* Fri Sep 11 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.3rc2
- 2.3.0 RC2

* Fri Sep 11 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.2rc1
- 2.3.0 RC1, revised .../SAL/nfs4_state_id.c.patch

* Wed Sep 9 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.3.0-0.1rc1
- 2.3.0 RC1

* Sat Aug 29 2015 Niels de Vos <ndevos@redhat.com> 2.2.0-6
- Rebuilt for jemalloc SONAME bump

* Fri Jul 17 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-5
- BuildRequires: libntirprc on base

* Fri Jul 17 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-4
- link with unbundled, shared libntirpc

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Niels de Vos <ndevos@redhat.com>
- improve readability and allow "rpmbuild --with .." options again

* Fri May 15 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-2
- %%license, build with glusterfs-3.7.0 GA

* Tue Apr 21 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-1
- 2.2.0 GA

* Mon Apr 20 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.13rc-final
- 2.2.0-0.13rc-final

* Mon Apr 13 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.12rc8
- 2.2.0-0.12rc8

* Mon Apr 6 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.11rc7
- 2.2.0-0.11rc7

* Thu Apr 2 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.10rc6
- 2.2.0-0.10rc6, with unbundled libntirpc

* Mon Mar 30 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.9rc6
- 2.2.0-0.9rc6

* Sun Mar 22 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.8rc5
- 2.2.0-0.8rc5

* Tue Mar 17 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.7rc4
- ntirpc-1.2.1.tar.gz

* Tue Mar 17 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.6rc4
- updated ntirpc-1.2.0.tar.gz

* Sun Mar 15 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.5rc4
- 2.2.0-0.5rc4

* Mon Feb 23 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.4rc3
- 2.2.0-0.4rc3

* Mon Feb 16 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.3rc2
- subpackage Requires: nfs-ganesha = %%{version}-%%{release}

* Mon Feb 16 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.2rc2
- 2.2.0-0.2rc2

* Fri Feb 13 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.2.0-0.1rc1
- 2.2.0-0.1rc1
- nfs-ganesha.spec based on upstream

* Thu Feb 12 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-14
- Fedora 23/rawhide build fixes
- Ceph restored in EPEL

* Mon Jan 19 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-13
- Ceph retired from EPEL 7

* Thu Nov 6 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-12
- rebuild after libnfsidmap symbol version revert

* Wed Oct 29 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-11
- PyQt -> PyQt4 typo

* Mon Oct 27 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-10
- use upstream init.d script

* Thu Oct 2 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-9
- restore exclusion of gluster gfapi on rhel

* Thu Oct 2 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-8
- install /etc/dbus-1/system.d/org.ganesha.nfsd.conf
- build and install admin tools

* Mon Sep 29 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-7
- install /etc/sysconfig/nfs-ganesha file

* Fri Aug 29 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- Ceph FSAL typo, #1135437

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 24 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-5
- use upstream nfs-ganesha.service

* Fri Jul 11 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-4
- keep fsal .so files, implementation now uses them

* Tue Jul 1 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-3
- static libuid2grp

* Tue Jul 1 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-2
- add libuid2grp.so

* Mon Jun 30 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.1.0-1
- nfs-ganesha-2.1.0 GA

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 2 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.0.0-9
- Ceph FSAL enabled with ceph-0.80

* Wed May 21 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.0.0-8
- getdents()->getdents64(), struct dirent -> struct dirent64

* Sat May 10 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- and exclude libfsalceph

* Sat May 10 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- exclude libfsalgluster correctly

* Fri May 9 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.0.0-7
- Ceph FSAL, in a subpackage, (but requires ceph >= 0.78)

* Mon Mar 31 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- GlusterFS FSAL in a subpackage
- EPEL7 has jemalloc as of 2014-02-25

* Tue Jan 21 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- sussed out github archive so as to allow correct Source0

* Fri Jan 17 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.0.0-6
- EPEL7 and xfsprogs

* Fri Jan 17 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.0.0-5
- EPEL7

* Mon Jan 6 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.0.0-4
- with glusterfs-api(-devel) >= 3.4.2

* Sat Jan 4 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.0.0-3
- with glusterfs-api

* Thu Jan 2 2014 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.0.0-2
- Build on RHEL6. Add sample init.d script

* Wed Dec 11 2013 Jim Lieb <lieb@sea-troll.net> - 2.0.0-1
- Update to V2.0.0 release

* Mon Nov 25 2013 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.0.0-0.2.rcfinal
- update to RC-final

* Fri Nov 22 2013 Kaleb S. KEITHLEY <kkeithle at redhat.com> 2.0.0-0.1.rc5
- Initial commit
