
%def_with rdma
%def_with glfs
%ifarch %ix86 %arm %mips32 ppc
%def_without rbd
%else
%def_with rbd
%endif

Name: scsitarget-utils
Version: 1.0.78
Release: alt1

Summary: The SCSI target daemon and utility programs

Group: System/Configuration/Hardware
License: GPLv2
URL: http://stgt.sourceforge.net/

Source0: %name-%version.tar
Source1: tgt.service
Source2: sysconfig.tgtd
Source3: targets.conf
Source4: sample.conf
Source5: tgtd.conf
Source6: tgt.init

# Patch10: %name-snapshot.patch
# Patch2: %name-alt-patches.patch

# fedora patches
Patch1: 0002-remove-check-for-xsltproc.patch
Patch2: 0003-default-config.patch

BuildRequires: libxslt docbook-style-xsl xsltproc
BuildRequires: glibc-devel
BuildRequires: libaio-devel
BuildRequires: glibc-kernheaders
BuildRequires: systemd-devel
BuildRequires: perl-Config-General
%{?_with_rdma:BuildRequires: libibverbs-devel librdmacm-devel}
%{?_with_rbd:BuildRequires: ceph-devel}
%{?_with_glfs:BuildRequires: glusterfs3-devel}

Requires: lsof
Requires: sg3_utils

Provides: scsi-target-utils = %version-%release
Provides: tgt = %version-%release
Obsoletes: tgt < %version-%release
Provides: iscsitarget = 1.4.20.2-alt2.1
Obsoletes: iscsitarget < 1.4.20.2-alt2.1

%description
The SCSI target package contains the daemon and tools to setup a SCSI
targets. Currently, software iSCSI targets are supported.

%package rbd
Summary: Support for the Ceph rbd backstore to scsi-target-utils
Group: System/Configuration/Hardware
Requires: %name = %version-%release

%description rbd
Adds support for the Ceph rbd backstore to scsi-target-utils.

%package gluster
Summary:        Support for the Gluster backstore to scsi-target-utils
Group: System/Configuration/Hardware
Requires: %name = %version-%release

%description gluster
Adds support for the Gluster glfs backstore to scsi-target-utils.

%prep
%setup
# %%patch10 -p1
%patch1 -p1
%patch2 -p1

%build
%__subst 's|-g -O2 -Wall|%optflags|' Makefile
%make_build \
	%{?_with_rdma:ISCSI_RDMA=1} \
	%{?_with_rbd:CEPH_RBD=1} \
	%{?_with_glfs:GLFS_BD=1} \
	SD_NOTIFY=1 \
	libdir=%_libdir/tgt

%install
mkdir -p %buildroot{%_sbindir,%_initdir,%_unitdir,%_sysconfdir/tgt/conf.d,%_sysconfdir/sysconfig,%_man5dir,%_man8dir}

install -p -m 0755 scripts/tgt-setup-lun %buildroot%_sbindir
install -p -m 0644 %SOURCE1 %buildroot%_unitdir
install -p -m 0755 scripts/tgt-admin %buildroot/%_sbindir/tgt-admin
install -p -m 0644 doc/manpages/targets.conf.5 %buildroot/%_man5dir
install -p -m 0644 doc/manpages/tgtadm.8 %buildroot/%_man8dir
install -p -m 0644 doc/manpages/tgt-admin.8 %buildroot/%_man8dir
install -p -m 0644 doc/manpages/tgt-setup-lun.8 %buildroot/%_man8dir
install -p -m 0600 %SOURCE2 %buildroot%_sysconfdir/sysconfig/tgtd
install -p -m 0600 %SOURCE3 %buildroot%_sysconfdir/tgt
install -p -m 0600 %SOURCE4 %buildroot%_sysconfdir/tgt/conf.d
install -p -m 0600 %SOURCE5 %buildroot%_sysconfdir/tgt
install -p -m 0755 %SOURCE6 %buildroot%_initdir/tgt

pushd usr
%makeinstall_std \
	%{?_with_rdma:ISCSI_RDMA=1} \
	%{?_with_rbd:CEPH_RBD=1} \
	%{?_with_glfs:GLFS_BD=1} \
	SD_NOTIFY=1 \
	sbindir=%_sbindir \
	libdir=%_libdir/tgt

%post
%post_service tgt

%preun
%preun_service tgt

%files
%doc README doc/README.iscsi doc/README.iser doc/README.lu_configuration doc/README.mmc doc/README.ssc
%_sbindir/tgtd
%_sbindir/tgtadm
%_sbindir/tgt-setup-lun
%_sbindir/tgt-admin
%_sbindir/tgtimg
%_man5dir/*
%_man8dir/*
%_unitdir/tgt.service
%_initdir/tgt
%dir %_libdir/tgt/backing-store
%dir %_sysconfdir/tgt
%dir %_sysconfdir/tgt/conf.d
%attr(0600,root,root) %config(noreplace) %_sysconfdir/sysconfig/tgtd
%attr(0600,root,root) %config(noreplace) %_sysconfdir/tgt/targets.conf
%attr(0600,root,root) %config(noreplace) %_sysconfdir/tgt/tgtd.conf
%attr(0600,root,root) %config(noreplace) %_sysconfdir/tgt/conf.d/sample.conf

%if_with rbd
%files rbd
%_libdir/tgt/backing-store/bs_rbd.so
%doc doc/README.rbd
%endif

%if glfs
%files gluster
%_libdir/tgt/backing-store/bs_glfs.so
%doc doc/README.glfs
%endif

%changelog
* Tue Jun 04 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.78-alt1
- 1.0.78
- obsoletes for iscsitarget

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.74-alt1
- new version 1.0.74
- disable support ceph on 32-bit arch

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.62-alt1
- 1.0.62

* Fri Mar 20 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.55-alt3
- Obsoletes tgt

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.55-alt2
- fix unit perm

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.55-alt1
- 1.0.55

* Tue Sep 03 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt6
- Rename tgtd.{init,service} files to tgt.{init,service}

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.30-alt5
- cleanup spec

* Sat Mar 30 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt4.1
- Add SysVinit support

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt4
- Fix unowned files

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt3
- Use post/preun_service scripts in spec

* Tue Jan 29 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt2
- Fix build with new docbook-style-xsl

* Wed Oct 03 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt1
- Initial release for Sisyphus
