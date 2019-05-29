%define _groupname	mfs
%define _username	mfs
%define _localstatedir	/var/lib
%define mfsconfdir	%_sysconfdir/mfs

Summary: MooseFS - distributed, fault tolerant file system
Name: moosefs
Version: 3.0.105
Release: alt1
License: GPLv2
Group: System/Servers
Url: http://www.moosefs.com/
# git-vcs: https://github.com/moosefs/moosefs.git
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libfuse-devel
BuildRequires: zlib-devel
BuildRequires: libpcap-devel
BuildRequires: pkgconfig(systemd)

%description
MooseFS is an Open Source, easy to deploy and maintain, distributed,
fault tolerant file system for POSIX compliant OSes.

%package -n libmfsio
Summary: MooseFS IO library
Group: System/Libraries
%description -n libmfsio
%summary.

%package -n libmfsio-devel
Summary: Development files for MooseFS IO library
Group: Development/C
Requires: libmfsio = %EVR
%description -n libmfsio-devel
%summary.

%package common
Summary: MooseFS - common files
Group: System/Servers
BuildArch: noarch

%description common
MooseFS - distributed, fault tolerant file system

%package master
Summary: MooseFS master server
Group: System/Servers
Requires: %name-common = %EVR

%description master
MooseFS master (metadata) server together with mfssupervisor utility.

%package metalogger
Summary: MooseFS metalogger server
Group: System/Servers
Requires: %name-common = %EVR

%description metalogger
MooseFS metalogger (metadata replication) server.

%package chunkserver
Summary: MooseFS data server
Group: System/Servers
Requires: %name-common = %EVR

%description chunkserver
MooseFS data server.

%package client
Summary: MooseFS client
Group: File tools

%description client
MooseFS client: mfsmount and mfstools.

%package cli
Summary: MooseFS CLI Utility
Group: File tools
BuildArch: noarch

%description cli
MooseFS CLI utilities.

%package cgi
Summary: MooseFS CGI Monitor
Group: System/Servers
BuildArch: noarch

%description cgi
MooseFS CGI monitor.

%package cgiserv
Summary: Simple CGI-capable HTTP server to run MooseFS CGI Monitor
Group: System/Servers
BuildArch: noarch
Requires: %name-cgi = %EVR
Requires: %name-common = %EVR

%description cgiserv
Simple CGI-capable HTTP server to run MooseFS CGI monitor.

%package netdump
Summary: MooseFS network packet dump utility
Group: System/Servers

%description netdump
MooseFS network packet dump utility

%prep
%setup
%patch -p1

%build
export PYTHON=/usr/bin/python3
%autoreconf
%configure \
	--with-default-user=%_username \
	--with-default-group=%_groupname \
	--with-systemdsystemunitdir=%_unitdir

%make_build

%install
%makeinstall_std
# configs
for configs in %buildroot%mfsconfdir/*.cfg.sample; do
    mv -n -v "$configs" "${configs%%.sample}"
done
mv -n -v \
    %buildroot%_localstatedir/mfs/metadata.mfs.empty \
    %buildroot%_localstatedir/mfs/metadata.mfs

pushd alt
# udev rules
mkdir -p %buildroot%_udevrulesdir
install -p -m644 moosefs-chunkserver.udev %buildroot%_udevrulesdir/80-moosefs-chunkserver.rules

# sysv init scripts
mkdir -p %buildroot%_sysconfdir/sysconfig
install -p -m644 moosefs-cgiserv.sysconfig %buildroot%_sysconfdir/sysconfig/moosefs-cgiserv
mkdir -p %buildroot%_initdir

for f in *.init ; do
    install -p -m755 $f %buildroot%_initdir/${f%%.init}
done
popd

%pre common
%_sbindir/groupadd -r -f %_groupname 2>/dev/null ||:
%_sbindir/useradd -M -r -d %_localstatedir/mfs -s /bin/null -c "MooseFS" -g %_groupname %_username 2>/dev/null ||:

%post master
%post_service %name-master
%preun master
%preun_service %name-master

%post metalogger
%post_service %name-metalogger
%preun metalogger
%preun_service %name-metalogger

%post chunkserver
%post_service %name-chunkserver
%preun chunkserver
%preun_service %name-chunkserver

%post cgiserv
%post_service %name-cgiserv
%preun cgiserv
%preun_service %name-cgiserv

%files -n libmfsio
%_libdir/libmfsio.so.*

%files -n libmfsio-devel
%_includedir/mfsio.h
%_libdir/libmfsio.so

%files common
%doc NEWS README
%dir %attr(770,root,%_groupname) %_localstatedir/mfs
%dir %attr(770,root,%_groupname) %mfsconfdir

%files master
%_sbindir/mfsmaster
%_sbindir/mfsmetadump
%_sbindir/mfsmetadirinfo
%_sbindir/mfsmetarestore
%_sbindir/mfsstatsdump
%_man5dir/mfsexports.cfg.5*
%_man5dir/mfstopology.cfg.5*
%_man5dir/mfsmaster.cfg.5*
%_man8dir/mfsmaster.8*
%_man8dir/mfsmetarestore.8*
%_man8dir/mfsmetadump.8*
%_man8dir/mfsmetadirinfo.8*
%_man8dir/mfsstatsdump.8*
%config(noreplace) %mfsconfdir/mfsexports.cfg
%config(noreplace) %mfsconfdir/mfstopology.cfg
%config(noreplace) %mfsconfdir/mfsmaster.cfg
%config(noreplace) %attr(640,%_username,%_groupname) %_localstatedir/mfs/metadata.mfs
%_initdir/moosefs-master
%_unitdir/moosefs-master.service
%_unitdir/moosefs-master@.service

%files metalogger
%_sbindir/mfsmetalogger
%_man5dir/mfsmetalogger.cfg.5*
%_man8dir/mfsmetalogger.8*
%config(noreplace) %mfsconfdir/mfsmetalogger.cfg
%_initdir/moosefs-metalogger
%_unitdir/moosefs-metalogger.service
%_unitdir/moosefs-metalogger@.service

%files chunkserver
%_sbindir/mfschunkserver
%_sbindir/mfschunktool
%_sbindir/mfscsstatsdump
%_man5dir/mfschunkserver.cfg.5*
%_man5dir/mfshdd.cfg.5*
%_man8dir/mfschunkserver.8*
%_man8dir/mfschunktool.8*
%_man8dir/mfscsstatsdump.8*
%config(noreplace) %mfsconfdir/mfschunkserver.cfg
%config(noreplace) %mfsconfdir/mfshdd.cfg
%_udevrulesdir/80-moosefs-chunkserver.rules
%_initdir/moosefs-chunkserver
%_unitdir/moosefs-chunkserver.service
%_unitdir/moosefs-chunkserver@.service

%files client
%_bindir/mfsappendchunks
%_bindir/mfscheckfile
%_bindir/mfsdirinfo
%_bindir/mfsfileinfo
%_bindir/mfsfilerepair
%_bindir/mfsmakesnapshot
%_bindir/mfsrmsnapshot
%_bindir/mfsgetgoal
%_bindir/mfssetgoal
%_bindir/mfscopygoal
%_bindir/mfsrgetgoal
%_bindir/mfsrsetgoal
%_bindir/mfsgetsclass
%_bindir/mfssetsclass
%_bindir/mfscopysclass
%_bindir/mfsxchgsclass
%_bindir/mfslistsclass
%_bindir/mfsgettrashtime
%_bindir/mfssettrashtime
%_bindir/mfscopytrashtime
%_bindir/mfsrgettrashtime
%_bindir/mfsrsettrashtime
%_bindir/mfsgeteattr
%_bindir/mfsseteattr
%_bindir/mfsdeleattr
%_bindir/mfscopyeattr
%_bindir/mfsgetquota
%_bindir/mfssetquota
%_bindir/mfsdelquota
%_bindir/mfscopyquota
%_bindir/mfschkarchive
%_bindir/mfsclrarchive
%_bindir/mfssetarchive
%_bindir/mfsfilepaths
%_bindir/mfsscadmin
%_bindir/mfstools
%_bindir/mfsmount
%_sbindir/mfsbdev
/sbin/mount.moosefs
%_man1dir/*
%exclude %_man1dir/mfscli.1*
%_man8dir/mfsmount.8*
%_man8dir/mount.moosefs.8*
%_man8dir/mfsbdev.8*
%config(noreplace) %mfsconfdir/mfsmount.cfg

%files cli
%_bindir/mfscli
%_man1dir/mfscli.1*

%files cgi
%dir %_datadir/mfscgi
%attr(755,root,root) %_datadir/mfscgi/*.cgi
%_datadir/mfscgi/*.css
%_datadir/mfscgi/*.gif
%_datadir/mfscgi/*.html
%_datadir/mfscgi/*.ico
%_datadir/mfscgi/*.js
%_datadir/mfscgi/*.png

%files cgiserv
%config(noreplace) %_sysconfdir/sysconfig/moosefs-cgiserv
%_sbindir/mfscgiserv
%_man8dir/mfscgiserv.8*
%_initdir/moosefs-cgiserv
%_unitdir/moosefs-cgiserv.service

%files netdump
%_sbindir/mfsnetdump
%_man8dir/mfsnetdump.8*

%changelog
* Wed May 29 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.105-alt1
- 3.0.105

* Wed May 08 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.104-alt1
- 3.0.104

* Sun Mar 03 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.103-alt1
- inital build for ALT (based on upstream spec)
