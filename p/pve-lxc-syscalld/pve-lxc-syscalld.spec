%define _libexecdir %_prefix/libexec

Name: pve-lxc-syscalld
Summary: PVE LXC syscall daemon
Version: 0.9.1
Release: alt1
License: GPL
Group: System/Servers
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: %name.tar.xz
Source1: %name-cargo.tar
Patch0: pve-lxc-syscalld-aarch64-u8.patch

ExclusiveArch: x86_64 aarch64
BuildRequires: /proc rust-cargo libsystemd-devel

%description
A daemon which handles a selected subset of syscalls for unprivileged
containers.

%prep
%setup -q -n %name

%ifarch aarch64
%patch -p0 -b .u8
%endif

rm -fr .cargo
tar -xf %SOURCE1 -C %_builddir
sed -i 's|roxmox ||' etc/pve-lxc-syscalld.service.in

%build
CARGO_HOME=%_builddir/cargo cargo build --release --offline

%install
install -pD -m755 target/release/%name %buildroot%_libexecdir/pve-lxc-syscalld/pve-lxc-syscalld
mkdir -p %buildroot%systemd_unitdir
sed "s|%LIBEXECDIR%|%_libexecdir|" etc/pve-lxc-syscalld.service.in > %buildroot%systemd_unitdir/pve-lxc-syscalld.service

%files
%systemd_unitdir/pve-lxc-syscalld.service
%_libexecdir/pve-lxc-syscalld/pve-lxc-syscalld

%changelog
* Thu Dec 10 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1
- initial release

