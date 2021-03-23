%define _groupname	mfs
%define _username	mfs
%define _localstatedir	/var/lib
%define liz_datadir	%_localstatedir/mfs
%define liz_confdir	%_sysconfdir/mfs
%define liz_limits_conf %_sysconfdir/security/limits.d/10-lizardfs.conf
%define liz_pam_d %_sysconfdir/pam.d/lizardfs
%define __nprocs 4

%def_without docs
%def_without ganesha

Summary: LizardFS - distributed, fault tolerant file system
Name: lizardfs
Version: 3.13.0
Release: alt0.rc3.2
License: GPLv3
Group: System/Servers
Url: https://www.lizardfs.org/
# git-vcs: https://github.com/lizardfs/lizardfs.git
Source: %name-%version.tar
Source1: pam-lizardfs
Source2: 10-lizardfs.conf
#Source3: spdlog-0.14.0.zip
%if_with ganesha
Source4: nfs-ganesha-2.5-stable.zip
Source5: ntirpc-1.5.zip
%endif
# Patch: %name-%version.patch

Conflicts: moosefs

ExcludeArch: armh

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): unzip
%if_with docs
BuildRequires: asciidoc-a2x
%endif
BuildRequires: boost-devel
BuildRequires: boost-asio-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libfuse-devel
BuildRequires: libjudy-devel
BuildRequires: libpam-devel
BuildRequires: libdb4-devel
BuildRequires: libsystemd-devel
# BuildRequires: thrift
BuildRequires: zlib-devel
BuildRequires: libspdlog-devel

%description
LizardFS is an Open Source, easy to deploy and maintain, distributed,
fault tolerant file system for POSIX compliant OSes.
LizardFS is a fork of MooseFS. For more information please visit
http://lizardfs.com

%package master
Summary: LizardFS master server
Group: System/Servers
Conflicts: moosefs-common
Conflicts: moosefs-master
#Requires: pam

%description master
LizardFS master (metadata) server together with metadata restore utility.
%summary.

%package metalogger
Summary: LizardFS metalogger server
Group: System/Servers
Conflicts: moosefs-common
Conflicts: moosefs-metalogger

%description metalogger
LizardFS metalogger (metadata replication) server.

%package chunkserver
Summary: LizardFS data server
Group: System/Servers
Conflicts: moosefs-common
Conflicts: moosefs-chunkserver

%description chunkserver
LizardFS data server.

%package client
Summary: LizardFS client
Group: System/Servers
Requires: fuse
Requires: libfuse
Requires: bash-completion
Conflicts: moosefs-common
Conflicts: moosefs-client

%description client
LizardFS client: mfsmount and lizardfs.

%package -n lib%name-client
Summary: LizardFS client C/C++ library
Group: System/Libraries
Provides: %name-lib-client = %EVR
Obsoletes: %name-lib-client < %EVR

%description -n lib%name-client
LizardFS client library for C/C++ bindings.

%package -n lib%name-client-devel
Summary: LizardFS client C/C++ library
Group: Development/C++

%description -n lib%name-client-devel
LizardFS client library for C/C++ bindings.

%package nfs-ganesha
Summary: LizardFS plugin for nfs-ganesha
Group: System/Servers
Requires: lib%name-client = %EVR

%description nfs-ganesha
LizardFS fsal plugin for nfs-ganesha.

%package cgi
Summary: LizardFS CGI Monitor
Group: System/Servers
Conflicts: moosefs-cgi

%description cgi
LizardFS CGI Monitor.

%package cgiserv
Summary: Simple CGI-capable HTTP server to run LizardFS CGI Monitor
Group: System/Servers
Requires: %name-cgi = %EVR
Conflicts: moosefs-cgiserv

%description cgiserv
Simple CGI-capable HTTP server to run LizardFS CGI Monitor.

%package adm
Summary: LizardFS administration utility
Group: System/Servers

%description adm
LizardFS command line administration utility.

%package uraft
Summary: LizardFS cluster management tool
Group: System/Servers
Requires: %name-master
Requires: %name-adm

%description uraft
LizardFS cluster management tool.

%prep
%setup

#unzip -q -d external SOURCE3
%if_with ganesha
unzip -q -d external %SOURCE4
unzip -q -d external %SOURCE5
%endif

# Remove /usr/bin/env from bash scripts
for i in src/tools/mfstools.sh src/master/mfsrestoremaster.in \
	 src/common/serialization_macros_generate.sh src/data/postinst.in \
	 utils/coverage.sh utils/cpp-interpreter.sh utils/wireshark/plugins/lizardfs/generate.sh; do
	sed -i 's@#!/usr/bin/env bash@#!/bin/bash@' $i
done
# Remove /usr/bin/env from python2/python3 scripts
for i in src/cgi/cgiserv.py.in; do
	sed -i "s@#!/usr/bin/env python2@#!/usr/bin/python2@" $i
done
for i in src/cgi/chart.cgi.in src/cgi/lizardfs-cgiserver.py.in src/cgi/mfs.cgi.in utils/wireshark/plugins/lizardfs/make_dissector.py; do
	sed -i "s@#!/usr/bin/env python3@#!/usr/bin/python3@" $i
done

%build
%cmake  \
%ifnarch i586
        -DLIB64=YES \
%endif
	-DCMAKE_BUILD_TYPE=Release \
	-DENABLE_TESTS=NO \
	-DENABLE_DEBIAN_PATHS=YES \
	-DCMAKE_INSTALL_PREFIX=/ \
	-DENABLE_CLIENT_LIB=YES \
%if_with ganesha
	-DENABLE_NFS_GANESHA=YES \
%endif
	-DENABLE_URAFT=YES \
%if_with docs
	-DENABLE_DOCS=YES \
%else
	-DENABLE_DOCS=OFF \
%endif
	-DENABLE_POLONAISE=OFF

%cmake_build

%install
%cmakeinstall_std

# configs
for configs in %buildroot%liz_confdir/*.cfg.dist; do
    mv -n -v "$configs" "${configs%%.dist}"
done
mv -n -v \
    %buildroot%_localstatedir/mfs/metadata.mfs.empty \
    %buildroot%_localstatedir/mfs/metadata.mfs

install -d -m755 %buildroot%_unitdir
for f in rpm/service-files/*.service ; do
	install -m644 "$f" %buildroot%_unitdir/$(basename "$f")
done

install -D -p -m644 %SOURCE1 %buildroot%liz_pam_d
install -D -p -m644 %SOURCE2 %buildroot%liz_limits_conf

pushd alt
# udev rules
mkdir -p %buildroot%_udevrulesdir
install -p -m644 lizardfs-chunkserver.udev %buildroot%_udevrulesdir/80-lizardfs-chunkserver.rules

# sysv init scripts
mkdir -p %buildroot%_sysconfdir/sysconfig
install -p -m644 lizardfs-cgiserv.sysconfig %buildroot%_sysconfdir/sysconfig/lizardfs-cgiserv
mkdir -p %buildroot%_initdir

for f in *.init ; do
    install -p -m755 $f %buildroot%_initdir/${f%%.init}
done
popd

%pre master
%_sbindir/groupadd -r -f %_groupname 2>/dev/null ||:
%_sbindir/useradd -M -r -d %_localstatedir/mfs -s /bin/null -c "LizardFS" -g %_groupname %_username 2>/dev/null ||:

%post master
%post_service %name-master
%preun master
%preun_service %name-master

%pre metalogger
%_sbindir/groupadd -r -f %_groupname 2>/dev/null ||:
%_sbindir/useradd -M -r -d %_localstatedir/mfs -s /bin/null -c "LizardFS" -g %_groupname %_username 2>/dev/null ||:

%post metalogger
%post_service %name-metalogger
%preun metalogger
%preun_service %name-metalogger

%pre chunkserver
%_sbindir/groupadd -r -f %_groupname 2>/dev/null ||:
%_sbindir/useradd -M -r -d %_localstatedir/mfs -s /bin/null -c "LizardFS" -g %_groupname %_username 2>/dev/null ||:
%post chunkserver
%post_service %name-chunkserver
%preun chunkserver
%preun_service %name-chunkserver

%post cgiserv
%post_service %name-cgiserv
%preun cgiserv
%preun_service %name-cgiserv

%files master
%doc NEWS README.md UPGRADE INSTALL COPYING
%_sbindir/mfsmaster
%_sbindir/mfsrestoremaster
%_sbindir/mfsmetadump
%_sbindir/mfsmetarestore
%if_with docs
%_man5dir/mfsexports.cfg.5*
%_man5dir/mfstopology.cfg.5*
%_man5dir/mfsgoals.cfg.5*
%_man5dir/mfsmaster.cfg.5*
%_man5dir/globaliolimits.cfg.5*
%_man7dir/mfs.7*
%_man7dir/moosefs.7*
%_man7dir/lizardfs.7*
%_man8dir/mfsmaster.8*
%_man8dir/mfsmetadump.8*
%_man8dir/mfsmetarestore.8*
%_man8dir/mfsrestoremaster.8*
%endif
%_unitdir/lizardfs-master.service
%_initdir/lizardfs-master

%attr(0755,%_username,%_groupname) %dir %liz_datadir
%config(noreplace) %attr(644,%_username,%_groupname) %liz_datadir/metadata.mfs
# Upstream documentation expects default config files to be stored in /etc/mfs
%dir %liz_confdir
%config(noreplace) %liz_confdir/mfsexports.cfg
%config(noreplace) %liz_confdir/mfstopology.cfg
%config(noreplace) %liz_confdir/mfsgoals.cfg
%config(noreplace) %liz_confdir/mfsmaster.cfg
%config(noreplace) %liz_confdir/globaliolimits.cfg
%config(noreplace) %liz_pam_d
%config(noreplace) %liz_limits_conf

%files metalogger
%doc NEWS README.md UPGRADE
%_sbindir/mfsmetalogger
%if_with docs
%_man5dir/mfsmetalogger.cfg.5*
%_man8dir/mfsmetalogger.8*
%endif
%_unitdir/lizardfs-metalogger.service
%_initdir/lizardfs-metalogger
%attr(0755,%_username,%_groupname) %dir %liz_datadir
%dir %liz_confdir
%config(noreplace) %liz_confdir/mfsmetalogger.cfg

%files chunkserver
%doc NEWS README.md UPGRADE
%_sbindir/mfschunkserver
%if_with docs
%_man5dir/mfschunkserver.cfg.5*
%_man5dir/mfshdd.cfg.5*
%_man8dir/mfschunkserver.8*
%endif
%_udevrulesdir/80-lizardfs-chunkserver.rules
%_unitdir/lizardfs-chunkserver.service
%_initdir/lizardfs-chunkserver
%attr(0755,%_username,%_groupname) %dir %liz_datadir
%dir %liz_confdir
%config(noreplace) %liz_confdir/mfschunkserver.cfg
%config(noreplace) %liz_confdir/mfshdd.cfg
%config(noreplace) %liz_pam_d
%config(noreplace) %liz_limits_conf

%files client
%doc NEWS README.md UPGRADE
%_bindir/*
%exclude %_bindir/lizardfs-admin
%exclude %_bindir/lizardfs-probe
%if_with docs
%_man1dir/*
%_man5dir/iolimits.cfg.5*
%_man5dir/mfsmount.cfg.5*
%_man7dir/mfs.7*
%_man7dir/moosefs.7*
%_man7dir/lizardfs.7*
%endif
%_sysconfdir/bash_completion.d/lizardfs
%dir %liz_confdir
%config(noreplace) %liz_confdir/mfsmount.cfg
%config(noreplace) %liz_confdir/iolimits.cfg

%files -n lib%name-client
%_libdir/liblizardfsmount_shared.so
%_libdir/liblizardfs-client.so

%files -n lib%name-client-devel
%_libdir/liblizardfs-client-cpp.a
%_libdir/liblizardfs-client-cpp_pic.a
%_libdir/liblizardfs-client.a
%_libdir/liblizardfs-client_pic.a
%_includedir/lizardfs

%if_with ganesha
%files nfs-ganesha
%_libdir/ganesha/libfsallizardfs.so
#%_libdir/ganesha/libfsallizardfs.so.4
#%_libdir/ganesha/libfsallizardfs.so.4.2.0
%endif

%files cgi
%doc NEWS README.md UPGRADE
%_datadir/mfscgi

%files cgiserv
%doc NEWS README.md UPGRADE
%_sbindir/lizardfs-cgiserver
%_sbindir/mfscgiserv
%if_with docs
%_man8dir/lizardfs-cgiserver.8*
%_man8dir/mfscgiserv.8*
%endif
%_unitdir/lizardfs-cgiserv.service
%_initdir/lizardfs-cgiserv
%_sysconfdir/sysconfig/lizardfs-cgiserv

%files adm
%doc NEWS README.md UPGRADE
%_bindir/lizardfs-admin
%_bindir/lizardfs-probe
%if_with docs
%_man8dir/lizardfs-admin.8*
%_man8dir/lizardfs-probe.8*
%endif

%files uraft
%_sbindir/lizardfs-uraft
%_sbindir/lizardfs-uraft-helper
%doc NEWS README.md UPGRADE
%if_with docs
%_man8dir/lizardfs-uraft.8*
%_man8dir/lizardfs-uraft-helper.8*
%_man5dir/lizardfs-uraft.cfg.5*
%endif
%config(noreplace) %liz_confdir/lizardfs-uraft.cfg
%_initdir/lizardfs-uraft
%_unitdir/lizardfs-uraft.service
%_unitdir/lizardfs-ha-master.service
%_unitdir/lizardfs-uraft.lizardfs-ha-master.service

%changelog
* Thu Dec 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.13.0-alt0.rc3.2
- update to aa878d3977a1fd25c4a63c9bdce5d5f59b3db784 from upstream

* Sat Nov 07 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.13.0-alt0.rc3.1
- build without Thrift

* Wed Sep 16 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.13.0-alt0.rc3
- 3.13.0-rc3

* Wed Apr 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.13.0-alt0.rc2.8.c27fe12f
- update to c27fe12fd0ec2dc5613d98cdc78423a6b788973e from upstream
- changed python2 to python3
- fix missing libfmt

* Mon Feb 03 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.13.0-alt0.rc1.16.g9c119b5c.3
- build without docs

* Fri Nov 22 2019 Andrew A. Vasilyev <andy@altlinux.org> 3.13.0-alt0.rc1.16.g9c119b5c.2
- fix python-base dependency

* Wed Jul 10 2019 Andrew A. Vasilyev <andy@altlinux.org> 3.13.0-alt0.rc1.16.g9c119b5c.1
- add conflicts with moosefs-*

* Mon Jul 08 2019 Alexey Shabalin <shaba@altlinux.org> 3.13.0-alt0.rc1.16.g9c119b5c
- upstream snapshot (fixed build on 32-bit arch)

* Tue May 28 2019 Andrew A. Vasilyev <andy@altlinux.org> 3.13.0-alt0.rc1
- Import from upstream 3.13.0-rc1

