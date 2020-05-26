Name: urbackup-server
Version: 2.3.8
Release: alt1.M90P.1
Summary: Efficient Client-Server backup system for Linux and Windows
Group: Archiving/Backup
License: AGPL-3.0+
Url: http://www.urbackup.org/
Source: %name-%version.tar.gz
Patch1: urbackup-server-fix-link-sqlite3.patch

BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libfuse-devel
BuildRequires: zlib-devel
BuildRequires: libcryptopp-devel
BuildRequires: liblmdb-devel
BuildRequires: libsqlite3-devel
BuildRequires: liblua5.3-devel
Requires: urbackup-common = %version-%release

%description
Efficient Client-Server Backup system for Linux and Windows
with GPT and UEFI partition. A client for Windows lets you
backup open files and complete partition images. Backups
are stored to disks in a efficient way (deduplication)
on either Windows or Linux servers.

%package -n urbackup-common
Summary: Common directories and user for urbackup server and client
Group: Archiving/Backup

%description -n urbackup-common
Common directories and user for urbackup server and client

%prep
%setup -n %name-%version
%patch1 -p1

%build
export SUID_CFLAGS=-fPIE
export SUID_LDFLAGS=-fpie
%ifarch %ix86
export CXXFLAGS="-msse2 -O2 -g"
%endif
%autoreconf
%configure \
    --enable-packaging \
    --with-mountvhd \
    --without-embedded-sqlite3 \
    --without-embedded-lua \
    --without-embedded-lmdb

%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_unitdir,%_man1dir,%_logrotatedir,%_logdir,%_localstatedir/urbackup}
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%prefix/lib/firewalld/services

sed -i "s@/etc/default/urbackupsrv@%_sysconfdir/sysconfig/%name@g" %name.service

install -m 644 defaults_server %buildroot%_sysconfdir/sysconfig/%name
install -m 640 urbackup-server-firewalld.xml %buildroot%prefix/lib/firewalld/services/%name.xml
install -m 644 urbackup-server.service %buildroot%_unitdir/%name.service
install -m 644 docs/urbackupsrv.1 %buildroot%_man1dir/%name.1
install -m 644 logrotate_urbackupsrv  %buildroot%_sysconfdir/logrotate.d/%name
touch %buildroot%_logdir/urbackup.log

%pre -n urbackup-common
groupadd -r -f urbackup >/dev/null 2>&1 ||:
useradd -g urbackup -c 'UrBackup pseudo user' \
    -d %_localstatedir/urbackup -s /dev/null -r -l -M urbackup >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING ChangeLog README
%attr(4710,root,urbackup) %_bindir/urbackup_snapshot_helper
%attr(4710,root,urbackup) %_bindir/urbackup_mount_helper
%attr(-,urbackup,urbackup) %_datadir/urbackup/*
%_bindir/urbackupsrv
%_man1dir/*
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%prefix/lib/firewalld/services/%name.xml
%ghost %_logdir/urbackup.log
%attr(-,urbackup,urbackup) %_localstatedir/urbackup/dataplan_db.txt
%attr(0644,root,root) %_unitdir/%name.service

%files -n urbackup-common
%dir %attr(0755,urbackup,urbackup) %_datadir/urbackup
%dir %attr(0755,urbackup,urbackup) %_localstatedir/urbackup

%changelog
* Mon May 25 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.3.8-alt1.M90P.1
- urbackup-common package introduced

* Sun Jul 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.3.8-alt1
- Initial build
