# TODO: --enable-bd-xlator

%define major 6.5
#define _localstatedir /var
%def_enable epoll
%def_enable fusermount
# disable NFS ganesha
%def_disable ganesha
%def_enable georeplication
# disable OCF resource agents
%def_without ocf
# rdma package
%def_enable ibverbs

Name: glusterfs6
Version: %major
Release: alt1

Summary: Cluster File System

License: GPLv2/LGPLv3+
Group: System/Base
Url: https://www.gluster.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/gluster/glusterfs/archive/v%version.tar.gz
Source: %name-%version.tar
Source2: glusterfs.watch
Source3: umount.glusterfs
Source4: glusterfs.logrotate
Source7: glusterd.init
Source8: glustereventsd.init
Patch0001: 0001-Increase-soname-version-of-libs-to-major-version-6.patch

# Stop unsupported i586 build
# Said all is ok: https://bugzilla.redhat.com/show_bug.cgi?id=1473968
#ExcludeArch: %ix86

%add_python3_path %_libexecdir/glusterfs/python

# fixme:
# glusterfs5
# add_python3_req_skip changelogdata libgfchangelog
# glusterfs5-georeplication
# add_python3_req_skip gsyncdstatus argsupgrade gsyncdconfig rconf repce subcmds syncdutils
# glusterfs5-gfevents
# add_python3_req_skip eventsapiconf eventtypes gfevents.eventsapiconf gfevents.eventtypes gfevents.utils handlers
%add_python3_path %_libexecdir/glusterfs/gfevents
%add_python3_path %_libexecdir/glusterfs/python/syncdaemon
%add_python3_path %_libexecdir/glusterfs/glusterfind
%add_python3_path %_libexecdir/glusterfs/gfind_missing_files
%allow_python3_import_path %_libexecdir/glusterfs/gfevents
%allow_python3_import_path %_libexecdir/glusterfs/python/syncdaemon
%allow_python3_import_path %_libexecdir/glusterfs/glusterfind
%allow_python3_import_path %_libexecdir/glusterfs/gfind_missing_files

# TODO: remove
%define _init_install() install -D -p -m 0755 %1 %buildroot%_initdir/%2 ;

%define glusterlibdir %_libdir/glusterfs/%version

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev

# liblvm2-devel: disable bd translator (uses obsoleted liblvm2app.so from liblvm2)

BuildRequires: flex libacl-devel libaio-devel libdb4-devel libreadline-devel libsqlite3-devel libuuid-devel libxml2-devel
BuildRequires: libssl-devel libcurl-devel zlib-devel libtirpc-devel
BuildRequires: libcmocka-devel
BuildRequires: systemd
BuildRequires: libuserspace-rcu-devel >= 0.9.1
%{?_enable_ibverbs:BuildRequires: rdma-core-devel}

Provides: glusterfs = %EVR
Conflicts: glusterfs3

%description
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package includes the glusterfs binary, the glusterfsd daemon and the
gluster command line, libglusterfs and glusterfs translator modules common to
both GlusterFS server and client framework.

%package rdma
Summary: GlusterFS rdma support for ib-verbs
Group: System/Base

Requires: %name = %EVR
Provides: glusterfs-rdma = %EVR
Conflicts: glusterfs3-rdma

%description rdma
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides support to ib-verbs library.

%package ganesha
Summary: NFS-Ganesha configuration
Group: System/Base
Requires: %name-server = %version-%release
Requires: nfs-ganesha
#Requires:         pcs
Provides: glusterfs-ganesha = %EVR
Conflicts: glusterfs3-ganesha
AutoReq: yes,noshell

%description ganesha
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the configuration and related files for using
NFS-Ganesha as the NFS server using GlusterFS.

%package georeplication
Summary: GlusterFS Geo-replication
Group: System/Base
Requires: %name = %EVR
Requires: rsync >= 3.0.0
Provides: glusterfs-georeplication = %EVR
Conflicts: glusterfs3-geo-replication

%description georeplication
GlusterFS is a clustered file-system capable of scaling to several
peta-bytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file system in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in userspace and easily manageable.

This package provides support to geo-replication.

%package thin-arbiter
Summary: GlusterFS thin-arbiter module
Group: System/Base
Requires: %name = %EVR
Requires: %name-server = %EVR
Provides: glusterfs-thin-arbiter = %EVR
Conflicts: glusterfs3-thin-arbiter

%description thin-arbiter
This package provides a tie-breaker functionality to GlusterFS
replicate volume. It includes translators required to provide the
functionality, and also few other scripts required for getting the setup done.

This package provides the glusterfs thin-arbiter translator.

%package client
Summary: GlusterFS client
Group: System/Base
BuildRequires: libfuse-devel

Requires: %name = %EVR
Provides: glusterfs-client = %EVR
Conflicts: glusterfs3-client

%description client
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides support to FUSE based clients.

%package -n lib%name-api
Summary: GlusterFS api library
Group: System/Libraries

%description -n lib%name-api
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the glusterfs libgfapi library.

%package -n lib%name-api-devel
Summary: Development libraries for GlusterFS api library
Group: Development/Other
Requires: lib%name-api = %EVR
Requires: lib%name-devel = %EVR
Provides: libglusterfs-api-devel = %EVR
Conflicts: libglusterfs3-api-devel

%description -n lib%name-api-devel
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the api include files.

%package server
Summary: Clustered file-system server
Group: System/Servers
Requires: %name = %EVR
Requires: %name-client = %EVR
Provides: glusterfs-server = %EVR
Conflicts: glusterfs3-server

%description server
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the glusterfs server daemon.

%package gfevents
Summary: GlusterFS Events
Group: System/Servers
BuildArch: noarch
Requires: %name-server = %EVR
Provides: %name-events = %EVR
Provides: glusterfs-gfevents = %EVR
Conflicts: glusterfs3-events

%description gfevents
GlusterFS Events

%package vim
Summary: Vim syntax file
Group: Editors
Requires: xxd
Requires: vim
BuildArch: noarch
Provides: glusterfs-vim = %EVR
Conflicts: glusterfs3-vim

%description vim
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

Vim syntax file for GlusterFS.

%package -n lib%name-devel
Summary: Development Libraries
Group: Development/Other
Requires: lib%name = %EVR
Requires: lib%name-api-devel = %EVR
Provides: libglusterfs-devel = %EVR
Conflicts: libglusterfs3-devel

%description -n lib%name-devel
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the development libraries.

%package -n python3-module-%name
Summary: Python module for %name
Group: Development/Python
BuildArch: noarch
Provides: python3-module-glusterfs = %EVR
Conflicts: python3-module-glusterfs3

%description -n python3-module-%name
This package provides Python API for %name

%package -n lib%name
Summary: GlusterFS common libraries
Group: System/Base

%description -n lib%name
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the base GlusterFS libraries.

%package resource-agents
Summary: OCF Resource Agents for GlusterFS
License: GPLv3+
Group: System/Base
BuildArch: noarch
Provides: glusterfs-resource-agents = %EVR
Requires: %name-server = %EVR

%description resource-agents
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the resource agents which plug glusterd into
Open Cluster Framework (OCF) compliant cluster resource managers,
like Pacemaker.

%prep
%setup
%patch0001 -p2

# due log2 in 6.0
%__subst "s|libgfrpc_la_LIBADD =|libgfrpc_la_LIBADD = -lm|" rpc/rpc-lib/src/Makefile.am

# due _libexecdir is /usr/lib
%__subst "s|/libexec/glusterfs|/lib/glusterfs|" ./configure.ac
%__subst "s|/usr/lib/systemd/system|%_unitdir|" ./configure.ac
# see build-aux/pkg-version
echo "v%version-%release" >VERSION

%build
export PYTHON=%__python3
# need from build from git repo (but incorporated in tarballs)
./autogen.sh
%configure \
  %{subst_enable ibverbs} \
  %{subst_enable epoll} \
  %{subst_enable fusermount} \
  %{subst_enable georeplication} \
  %{subst_with ocf} \
  --with-systemddir=%_unitdir \
  --localstatedir=/var/
  
# NOTE: --enable-asan makes all sizeof is 0, see broken-configure TESTS

# TODO: make check
#            --enable-cmocka

# Remove rpath
%__subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%__subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%makeinstall_std PYTHON=%__python3
# Install include directory
mkdir -p %buildroot%_includedir/glusterfs
install -p -m 0644 libglusterfs/src/*.h %buildroot%_includedir/glusterfs/
#install -p -m 0644 contrib/uuid/*.h %buildroot%_includedir/glusterfs/
# Following needed by hekafs multi-tenant translator
mkdir -p %buildroot%_includedir/glusterfs/rpc
install -p -m 0644 rpc/rpc-lib/src/*.h %buildroot%_includedir/glusterfs/rpc/
install -p -m 0644 rpc/xdr/src/*.h %buildroot%_includedir/glusterfs/rpc/
mkdir -p %buildroot%_includedir/glusterfs/server
install -p -m 0644 xlators/protocol/server/src/*.h %buildroot%_includedir/glusterfs/server/
# We'll use our init.d
rm -f %buildroot/etc/init.d/glusterd

# Create logging directory
mkdir -p %buildroot%_logdir/glusterfs/

# Remove unwanted files from all the shared libraries
find %buildroot%_libdir -name '*.a' -delete
find %buildroot%_libdir -name '*.la' -delete

# Remove installed docs, we include them ourselves as %%doc
rm -rf %buildroot%_docdir/glusterfs/
# move binary from datadir to bindir
mv %buildroot%_datadir/glusterfs/scripts/gsync-sync-gfid %buildroot%_bindir/

# Rename the samples, so we can include them as %%config
#for file in %buildroot%_sysconfdir/glusterfs/*.sample; do
#  mv ${file} `dirname ${file}`/`basename ${file} .sample`
#done

# Remove wrong placed confs
for file in glusterfs-georep-logrotate glusterfs-logrotate; do
  rm -v %buildroot%_sysconfdir/glusterfs/${file}
done

# Create working directory
mkdir -p %buildroot%_sharedstatedir/glusterd/

# Update configuration file to /var/lib working directory
%__subst 's|option working-directory %_sysconfdir/glusterd|option working-directory %_sharedstatedir/glusterd|g' \
%buildroot%_sysconfdir/glusterfs/glusterd.vol

install -D -m644 extras/systemd/glusterd.service %buildroot/%_unitdir/glusterd.service
install -D -m644 extras/systemd/glustereventsd.service %buildroot/%_unitdir/glustereventsd.service
install -D -m644 extras/systemd/gluster-ta-volume.service %buildroot/%_unitdir/gluster-ta-volume.service
install -D -m644 extras/systemd/glusterfssharedstorage.service %buildroot/%_unitdir/glusterfssharedstorage.service

# Install init script and sysconfig file
%_init_install %SOURCE7 glusterd
%_init_install %SOURCE8 glustereventsd
install -D -p -m 0644 extras/glusterd-sysconfig %buildroot%_sysconfdir/sysconfig/glusterd
# Install wrapper umount script
install -D -p -m 0755 %SOURCE3 %buildroot/sbin/umount.glusterfs

%if_enabled geo-replication
install -D -p -m 0644 extras/glusterfs-georep-logrotate %buildroot%_logrotatedir/glusterfs-georep
%endif
install -D -p -m 0644 %SOURCE4 %buildroot%_logrotatedir/glusterfs

install -D -p -m 644 extras/glusterfs.vim %buildroot%_datadir/vim/vimfiles/syntax/glusterfs.vim
%if_without ocf
rm -rf %buildroot%_libexecdir/ocf/
%endif
%if_disabled rdma
rm -rf %buildroot%glusterlibdir/rpc-transport/rdma*
%endif

rm -rf %buildroot%_sbindir/conf.py
# FIXME: uses python 2 syntax
# see also https://bugzilla.redhat.com/show_bug.cgi?id=1590193
rm -rf %buildroot%_sbindir/gcron.py
rm -rf %buildroot%_sbindir/snap_scheduler.py

# TODO: selinux
# rm HACK due S10selinux-label-brick.sh: line 46: syntax error near unexpected token `('
rm -fv %buildroot%_sharedstatedir/glusterd/hooks/1/create/post/S10selinux-label-brick.sh
# drop req on policycoreutils (semanage)
rm -fv %buildroot%_sharedstatedir/glusterd/hooks/1/delete/pre/S10selinux-del-fcontext.sh

# remove cloudsync-plugins
rm -fv %buildroot%glusterlibdir/cloudsync-plugins/cloudsyncs3.so

%post server
%post_service glusterd

%preun server
%preun_service glusterd

# TODO: move common part to -common?
%files
%doc ChangeLog INSTALL README.md THANKS COPYING-GPLV2 COPYING-LGPLV3
%_bindir/glusterfind

# cli
%_sbindir/gluster
%_sbindir/gluster-setgfid2path
%_man8dir/gluster.*
%_man8dir/gluster-setgfid2path.*

%dir %glusterlibdir/rpc-transport/
%glusterlibdir/rpc-transport/socket.so
%glusterlibdir/auth/
%glusterlibdir/xlator/
%exclude %glusterlibdir/xlator/mount/api.so
%exclude %glusterlibdir/xlator/mount/fuse*
%exclude %glusterlibdir/xlator/features/thin-arbiter.so
%_libexecdir/glusterfs/glusterfind/
%_sbindir/gfind_missing_files
%_libexecdir/glusterfs/gfind_missing_files/
%_libexecdir/glusterfs/mount-shared-storage.sh
# used in snap_scheduler.py
#_sbindir/gcron.py
#_sbindir/snap_scheduler.py
%_logdir/glusterfs/
%exclude %_man8dir/mount.glusterfs.8*
%dir %_datadir/glusterfs/scripts

%if_enabled ibverbs
%files rdma
%glusterlibdir/rpc-transport/rdma.so
%endif

%if_enabled georeplication
%files georeplication
%dir %_libexecdir/glusterfs/
%_libexecdir/glusterfs/gsyncd
%dir %_libexecdir/glusterfs/python/
%_libexecdir/glusterfs/gverify.sh
%_libexecdir/glusterfs/peer_add_secret_pub
%_libexecdir/glusterfs/peer_gsec_create
%_libexecdir/glusterfs/python/syncdaemon/
%_libexecdir/glusterfs/set_geo_rep_pem_keys.sh
%_datadir/glusterfs/scripts/get-gfid.sh
%_datadir/glusterfs/scripts/slave-upgrade.sh
%_datadir/glusterfs/scripts/gsync-upgrade.sh
%_datadir/glusterfs/scripts/generate-gfid-file.sh
%_datadir/glusterfs/scripts/schedule_georep.py
%_bindir/gsync-sync-gfid
%_libexecdir/glusterfs/peer_georep-sshkey.py
%_libexecdir/glusterfs/peer_mountbroker
%_libexecdir/glusterfs/peer_mountbroker.py
%_sbindir/gluster-georep-sshkey
%_sbindir/gluster-mountbroker
#config(noreplace) %_logrotatedir/glusterfs-georep
%endif

%files -n lib%name-api
# libgfapi files
%_libdir/libgfapi.so.*
%glusterlibdir/xlator/mount/api.so

%files -n lib%name-api-devel
%_pkgconfigdir/glusterfs-api.pc
%_libdir/libgfapi.so
%_includedir/glusterfs/api/

%files thin-arbiter
%glusterlibdir/xlator/features/thin-arbiter.so
%_datadir/glusterfs/scripts/setup-thin-arbiter.sh
#config %_sysconfdir/glusterfs/thin-arbiter.vol
%_unitdir/gluster-ta-volume.service

%files client
# CHECKME: glusterfs is a symlink to glusterfsd, -server depends on -client.
%_sbindir/glusterfs
%_sbindir/glusterfsd
%_man8dir/glusterfs.8*
%_man8dir/glusterfsd.8*
%config(noreplace) %_logrotatedir/glusterfs
%glusterlibdir/xlator/mount/fuse*
%_man8dir/mount.glusterfs.8*
/sbin/mount.glusterfs
/sbin/umount.glusterfs
%if_enabled fusermount
 %_bindir/fusermount-glusterfs
%endif

%files server
%_sbindir/glusterd
%_man8dir/glusterd.8*
%_initdir/glusterd
%_unitdir/glusterd.service
%_unitdir/glusterfssharedstorage.service
%config(noreplace) %_sysconfdir/sysconfig/glusterd
%dir %_sysconfdir/glusterfs/
%config(noreplace) %_sysconfdir/glusterfs/*
%exclude %_sysconfdir/glusterfs/eventsconfig.json

%_sharedstatedir/glusterd/
%exclude %_sharedstatedir/glusterd/events/

%_sbindir/glfsheal
%_sbindir/gf_attach
#%_libdir/libgfdb.so.*

%dir %_datadir/glusterfs/scripts/

%_datadir/glusterfs/scripts/post-upgrade-script-for-quota.sh
%_datadir/glusterfs/scripts/pre-upgrade-script-for-quota.sh
%_datadir/glusterfs/scripts/stop-all-gluster-processes.sh
%_datadir/glusterfs/scripts/control-cpu-load.sh
%_datadir/glusterfs/scripts/control-mem.sh

%if_with ocf
%dir %_libexecdir/ocf/resource.d/
%_libexecdir/ocf/resource.d/glusterfs/
%endif

%if_with ganesha
%files ganesha
%dir /etc/ganesha/
%config(noreplace) /etc/ganesha/ganesha-ha.conf.sample
%_libexecdir/ganesha/create-export-ganesha.sh
#%_libexecdir/ganesha/copy-export-ganesha.sh
%_libexecdir/ganesha/dbus-send.sh
%_libexecdir/ganesha/ganesha-ha.sh
%_libexecdir/ganesha/generate-epoch.py
%endif
# TODO: move inside of ganesha
%if_with ocf
 %_libexecdir/ocf/resource.d/heartbeat/
%endif

# Events
%files gfevents
%config(noreplace) %_sysconfdir/glusterfs/eventsconfig.json
%dir %attr(0755,-,-) %_sharedstatedir/glusterd/events/
%_libexecdir/glusterfs/gfevents/
%_libexecdir/glusterfs/peer_eventsapi.py*
%_sbindir/glustereventsd
%_sbindir/gluster-eventsapi
%_datadir/glusterfs/scripts/eventsdash.py*
%_unitdir/glustereventsd.service
%_initdir/glustereventsd

%files vim
%doc COPYING-GPLV2 COPYING-LGPLV3
%_datadir/vim/vimfiles/syntax/glusterfs.vim

%files -n lib%name-devel
%_includedir/glusterfs/
%exclude %_includedir/glusterfs/api/
%exclude %_includedir/glusterfs/y.tab.h
%_libdir/libgfchangelog.so
%_libdir/libgfrpc.so
%_libdir/libgfxdr.so
#%_libdir/libgfdb.so
%_libdir/libglusterfs.so
%_pkgconfigdir/libgfchangelog.pc
# pkgconfiglib.req: WARNING: /tmp/.private/lav/glusterfs3-buildroot/usr/lib64/pkgconfig/libgfdb.pc: cannot find -lgfchangedb library path (skip)
#_pkgconfigdir/libgfdb.pc

%files -n lib%name
# until we got -common subpackage
%dir %_libdir/glusterfs/
%dir %glusterlibdir/
%dir %_datadir/glusterfs/
%dir %_libexecdir/glusterfs/

%_libdir/libgfchangelog.so.*
%_libdir/libgfrpc.so.*
%_libdir/libgfxdr.so.*
%_libdir/libglusterfs.so.*

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%if_with ocf
%files resource-agents
%dir %_target_libdir_noarch/ocf
%dir %_target_libdir_noarch/ocf/resource.d/glusterfs
%_target_libdir_noarch/ocf/resource.d/glusterfs/glusterd
%endif

%changelog
* Tue Sep 17 2019 Vitaly Lipatov <lav@altlinux.ru> 6.5-alt1
- new version 6.5

* Tue Sep 17 2019 Vitaly Lipatov <lav@altlinux.ru> 6.3-alt6
- update sysv init-script and sysconfig config

* Fri Jul 12 2019 Andrew A. Vasilyev <andy@altlinux.org> 6.3-alt5
- clear python2 dependence
- spec cleanup
- remove Requires: from lib-api
- add Provides: to devel libs

* Wed Jun 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 6.3-alt4
- add Provides: glusterfs
- Increase soname version of libs to major version 6

* Fri Jun 14 2019 Andrew A. Vasilyev <andy@altlinux.org> 6.3-alt3
- add resource-agents
- fix georeplication option in configure
- minor spec cleanup

* Fri Jun 14 2019 Vitaly Lipatov <lav@altlinux.ru> 6.3-alt2
- enable build for ix86 (32bit)

* Fri Jun 14 2019 Vitaly Lipatov <lav@altlinux.ru> 6.3-alt1
- new version 6.3 (with rpmrb script)
- add conflicts to *gluster3 packages (ALT bug 36896)

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 6.2-alt1
- new version 6.2 (with rpmrb script)

* Wed Mar 20 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0-alt1
- new version (6.0) with rpmgs script

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 5.4-alt1
- new version
- rename events subpackage to gfevents

* Fri Dec 14 2018 Vitaly Lipatov <lav@altlinux.ru> 5.2-alt1
- initial build of the development release 5.2
