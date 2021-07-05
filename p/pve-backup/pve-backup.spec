
%define _libexecdir /usr/libexec
%define proxy_user backup

Name: pve-backup
Version: 1.0.5
Release: alt1
Summary: PVE Backup Server
License: GPL-1 and LGPLv2 and BSD
Group: Archiving/Backup
URL: https://www.proxmox.com/en/proxmox-backup-server

Source0: proxmox.tar
Source1: cargo.tar

ExclusiveArch: x86_64 aarch64

BuildRequires: /proc clang-devel rust-cargo libudev-devel libssl-devel libacl-devel libsystemd-devel libpam-devel libfuse3-devel libuuid-devel
BuildRequires: python3-module-sphinx

%description
PVE Backup Server daemon with tools and GUI
This package contains the Proxmox Backup Server daemons and related
tools. This includes a web-based graphical user interface.

%package server
Summary: PVE backup server
Group: Archiving/Backup
Requires(pre): shadow-utils
Requires: javascript-common
Provides: proxmox-backup-server = %EVR

%description server
This package provides PVE Backup Server.

%package client
Summary: PVE backup client
Group: Archiving/Backup
Provides: proxmox-backup-client = %EVR

%description client
This package provides PVE Backup client.

%package -n libpve-backup-qemu
Summary: PVE Backup Server client library for QEMU
Group: System/Libraries
Provides: libproxmox-backup-qemu0 = %EVR

%description -n libpve-backup-qemu
PVE Backup Server client library for QEMU
This library contains the library to access the Proxmox Backup server from
within QEMU.

%package -n libpve-backup-qemu-devel
Summary: PVE Backup Server development environment
Group: Development/Other
Requires: libpve-backup-qemu = %EVR

%description -n libpve-backup-qemu-devel
PVE Backup Server development environment.

%prep
tar -xf %SOURCE0 -C %_builddir
tar -xf %SOURCE1 -C %_builddir

%build
for c in proxmox-backup proxmox-backup-qemu; do
	pushd $c
	CARGO_HOME=%_builddir/cargo cargo build --release --offline
	popd
done

%install
install -pD -m644 proxmox-backup-qemu/proxmox-backup-qemu.h %buildroot%_includedir/proxmox-backup-qemu.h
install -pD -m644 proxmox-backup-qemu/target/release/libproxmox_backup_qemu.so %buildroot%_libdir/libproxmox_backup_qemu.so.0
ln -s libproxmox_backup_qemu.so.0 %buildroot%_libdir/libproxmox_backup_qemu.so

install -dm755 %buildroot%_bindir
install -m755 proxmox-backup/target/release/pxar %buildroot%_bindir/
install -m755 proxmox-backup/target/release/proxmox-backup-client %buildroot%_bindir/

install -dm755 %buildroot%_sbindir
install -m755 proxmox-backup/target/release/proxmox-backup-manager %buildroot%_sbindir/
install -dm755 %buildroot%_libexecdir/proxmox-backup
install -m755 proxmox-backup/target/release/proxmox-backup-api %buildroot%_libexecdir/proxmox-backup/
install -m755 proxmox-backup/target/release/proxmox-backup-banner %buildroot%_libexecdir/proxmox-backup/
install -m755 proxmox-backup/target/release/proxmox-backup-proxy %buildroot%_libexecdir/proxmox-backup/
install -m755 proxmox-backup/target/release/proxmox-daily-update %buildroot%_libexecdir/proxmox-backup/

pushd proxmox-backup
make -C etc PROXY_USER=%proxy_user LIBEXECDIR=%_libexecdir
install -dm755 %buildroot%_unitdir
for u in proxmox-backup-banner.service proxmox-backup-daily-update.service \
        proxmox-backup.service proxmox-backup-proxy.service proxmox-backup-daily-update.timer ; do
    install -m644 etc/$u %buildroot%_unitdir/
done

sed -i 's/eslint/# eslint/g' www/Makefile
sed -i 's/sphinx-build/sphinx-build-3/' docs/Makefile
make -C www
popd
pushd proxmox-backup/www
%define jsdir %buildroot%_datadir/javascript/proxmox-backup
        install -dm755 %jsdir
        install -m644 index.hbs %jsdir
        install -dm755 %jsdir/js
        install -m644 js/proxmox-backup-gui.js %jsdir/js/
        install -dm755 %jsdir/css
        install -m644 css/ext6-pbs.css %jsdir/css/
        install -dm755 %jsdir/images
        install -m644 images/*.png %jsdir/images/
popd

%pre server
grep -q "^%proxy_user:" %_sysconfdir/group \
|| %_sbindir/groupadd -r -f %proxy_user ||:
grep -q "^%proxy_user:" %_sysconfdir/passwd \
|| %_sbindir/useradd -g %proxy_user -c 'PBS proxy user' \
        -d /tmp -s /dev/null -r %proxy_user ||:

%files server
%_sbindir/*
%_libexecdir/proxmox-backup
%_datadir/javascript/proxmox-backup
%_unitdir/*

%files client
%_bindir/pxar
%_bindir/proxmox-backup-client

%files -n libpve-backup-qemu
%_libdir/libproxmox_backup_qemu.so.0

%files -n libpve-backup-qemu-devel
%_includedir/*
%_libdir/libproxmox_backup_qemu.so

%changelog
* Tue Feb 16 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.5-alt1
- initial build for ALT

