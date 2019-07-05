%define _unpackaged_files_terminate_build 1

Name: powerpc-utils
Version: 1.3.7
Release: alt1
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
Summary: Utilities for PowerPC platforms

ExclusiveArch: ppc ppc64 ppc64le

Source: %name-%version.tar
Patch0: powerpc-utils-1.3.6-alt-fix-systemd-unit-install.patch
Patch1: powerpc-utils-1.3.6-alt-remove-absolute-paths.patch

BuildRequires: zlib-devel librtas-devel

AutoReq: noshell
# shell.req generates these requires:
# /sbin/reboot coreutils getopt grep ipmitool kmod kpartx sed systemd-utils which
# most of them are optional.
Requires: coreutils getopt grep sed which

%description
Utilities for maintaining and servicing PowerPC systems.

%prep
%setup
%patch0 -p1
%patch1 -p1
sed -e 's/^Before=libvirt-bin.service$/Before=libvirtd.service/' -i \
	systemd/smt_off.service.in

%build
%autoreconf
%configure \
	--with-systemd=%_unitdir \
#
%make_build

%install
%makeinstall_std

rm -r %buildroot/usr/share/doc

%files
%_bindir/amsstat
%_sbindir/*
%_man1dir/*
%_man5dir/*
%_man8dir/*
%_unitdir/smt_off.service
%doc COPYING README

%changelog
* Fri Jul 05 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.7-alt1
- Initial build.
