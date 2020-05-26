
Name: urbackup-client
Version: 2.3.4
Release: alt1.M90P.2
Summary: Efficient Client-Server backup system for Linux and Windows
Group: Archiving/Backup
License: AGPL-3.0+
Url: http://www.urbackup.org/
Source: %name-%version.tar.gz
Patch1: urbackup-client-fix-link-sqlite3.patch
Patch2: urbackup-client-scripts.patch

BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libcryptopp-devel
BuildRequires: libsqlite3-devel

Requires: urbackup-common

%description
Efficient Client-Server Backup system for Linux and Windows
with GPT and UEFI partition. A client for Windows lets you
backup open files and complete partition images. Backups
are stored to disks in a efficient way (deduplication)
on either Windows or Linux servers.

%prep
%setup -n %name-%version.0
%patch1 -p1
%patch2 -p1

%build
export SUID_CFLAGS=-fPIE
export SUID_LDFLAGS=-fpie
%ifarch %ix86
export CXXFLAGS="-msse2 -O2 -g"
%endif
%autoreconf
%configure \
    --without-embedded-sqlite3 \
    --enable-headless

%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_unitdir,%_man1dir,%_logdir,%_localstatedir/urbackup}
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_initdir

sed -i "s@/usr/local/sbin/urbackupclientbackend@%_sbindir/urbackupclientbackend@g" urbackupclientbackend-redhat.service

install -m 644 defaults_client %buildroot%_sysconfdir/sysconfig/urbackupclient
install -m 644 urbackupclientbackend-redhat.service %buildroot%_unitdir/%name.service
install -m 644 docs/urbackupclientbackend.1 %buildroot%_man1dir/urbackupclientbackend.1
touch %buildroot%_logdir/urbackupclient.log

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING ChangeLog README
%config(noreplace) %_sysconfdir/sysconfig/urbackupclient
%dir %_sysconfdir/urbackup
%config(noreplace) %_sysconfdir/urbackup/*.conf
%_bindir/urbackupclientctl
%_sbindir/urbackupclientbackend
%_unitdir/%name.service
%_man1dir/*
%dir %attr(0755,urbackup,urbackup) %_datadir/urbackup
%attr(-,urbackup,urbackup) %_datadir/urbackup/*
%dir %attr(0755,urbackup,urbackup) %_localstatedir/urbackup
%attr(-,urbackup,urbackup) %_localstatedir/urbackup/*
%ghost %_logdir/urbackupclient.log

%changelog
* Mon May 25 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.3.4-alt1.M90P.2
- dep on urbackup-common added

* Fri May 15 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.3.4-alt1.M90P.1
- file conflict with urbackup-server fixed

* Sun Jul 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.3.4-alt1
- Initial build
