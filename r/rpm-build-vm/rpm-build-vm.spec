# SPDX-License-Identifier: GPL-2.0-only
# Copyright (C) 2019 Vitaly Chikunov <vt@altlinux.org>
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: rpm-build-vm
Version: 1.18
Release: alt2

Summary: RPM helper to run tests in virtualised environment
License: GPL-2.0-only
Group: Development/Other

Source: %name-%version.tar

%define supported_arches %ix86 x86_64 ppc64le aarch64 armh

%ifarch %supported_arches
# We need static libs to build initramfs /init binary:
#   klibc-devel        - cannot call arbitrary syscall.
#   musl-devel         - does not cover all arches.
#   glibc-devel-static - binaries are bigger.
BuildRequires: klibc-devel

# Try to load un-def kernel this way to avoid "forbidden dependencies"
# from sisyphus_check.
Requires(pre): kernel >= 5.7

Requires(pre): %name-run = %EVR
%endif

%ifarch %supported_arches
%description
RPM helper to run QEMU inside hasher. This is mainly intended
for %%check section to test software under better emulated root
than fakeroot.

This is similar to multiple vm scripts, virtme, vido, and eudyptula-boot.
%else
%description
This package is a stub instead of RPM helper to run QEMU inside hasher
on supported architectures (this one (%_arch) is unsupported).
%endif

%package run
Summary: vm-run virtualized runner
Group: Development/Other

# Other arches will get a stub which will always return success
%ifarch %supported_arches
Requires: mount

# /proc is required for qemu 9p to work, otherwise you'll get
# confusing ENOENT when creating a file. This is because
# `qemu/hw/9pfs/9p-local.c:fchmodat_nofollow' is doing chmod
# over `/proc/self/fd/%%d'.
Requires: /proc
Requires: /dev/kvm

%ifarch %ix86 x86_64
Requires: qemu-system-x86-core
%endif
%ifarch ppc64le
Requires: qemu-system-ppc-core
%endif
%ifarch aarch64
Requires: qemu-system-aarch64-core
%endif
%ifarch armh
# No KVM support in the kernel for this arch.
Requires: qemu-system-arm-core
%endif

%endif

%ifarch %supported_arches
%description run
RPM helper to run QEMU inside hasher. This is mainly intended
for %%check section to test software under better emulated root
than fakeroot.

This is similar to multiple vm scripts, virtme, vido, and eudyptula-boot.

This package is vm-run scripts only (without requirement on the kernel).
%else
%description run
This package is a stub instead of RPM helper to run QEMU inside hasher
on supported architectures (this one (%_arch) is unsupported).
%endif

%package checkinstall
Summary: Checkinstall for vm-run
Group: Development/Other
BuildArch: noarch
Requires(pre): %name = %EVR

%description checkinstall
Run checkinstall tests for vm-run.

%prep
%setup

%ifarch %supported_arches
%build
[ -x /usr/bin/musl-gcc ] && export CC=musl-gcc
[ -x /usr/bin/klcc     ] && export CC=klcc
CFLAGS="%optflags" make
%endif

%install
%ifnarch %supported_arches
install -D -p -m 0755 vm-run-stub %buildroot%_bindir/vm-run
%else
install -D -p -m 0755 vm-run      %buildroot%_bindir/vm-run
install -D -p -m 0755 vm-init     %buildroot%_libexecdir/vm-run/vm-init
install -D -p -m 0755 initrd-init %buildroot%_libexecdir/vm-run/initrd-init
install -D -p -m 0755 filetrigger %buildroot%_rpmlibdir/vm-run.filetrigger
%endif

%pre run
# Only allow to install inside of hasher.
[ -d /.host -a -d /.in -a -d /.out ] || {
        echo >&2 'rpm-build-vm-run is not allowed outside hasher environments'
        exit 1
}

%files

%files checkinstall

%files run
%_bindir/vm-run

%ifarch %supported_arches
%_libexecdir/vm-run
%_rpmlibdir/vm-run.filetrigger

%post
# Fix permissions to boot the installed kernel
find /boot /lib/modules -type f,d \! -perm -444 -print0 | xargs -0r chmod a+rX

%post run
# Required in case of --udevd option to vm-run
mkdir -p /run/udev
chmod a+twx /run/udev

# Just in case
mkdir -p /run/dbus
chmod a+twx /run/dbus

# u&mount should to be readable to use inside vm
control mount unprivileged

# For --overlay=
chmod a+twx /mnt

# Allow user creation (for openssh)
chmod a+r /etc/login.defs

%ifarch armh
# Workaround to KVM not working on armh: signal to scripts that we don't have
# kvm. This will work on normal build, but will be cleared on hsh-shell, that
# will not produce failure though, just more warnings from qemu.
chmod go-rwx /dev/kvm
%endif
%endif

%pre checkinstall
set -ex
vm-run --verbose uname -a
vm-run --verbose --overlay=ext4 uname -a

%changelog
* Fri Dec 04 2020 Vitaly Chikunov <vt@altlinux.org> 1.18-alt2
- Warning if there is attempt to install rpm-build-vm-run outside of hasher.

* Sat Nov 14 2020 Vitaly Chikunov <vt@altlinux.org> 1.18-alt1
- Support to find and run uncompressed vmlinux kernels.

* Fri Sep 25 2020 Vitaly Chikunov <vt@altlinux.org> 1.17-alt1
- Skip copying non-existent modules into initramfs.

* Tue Sep 08 2020 Vitaly Chikunov <vt@altlinux.org> 1.16-alt1
- Fix checkinstall.

* Sat Sep 05 2020 Vitaly Chikunov <vt@altlinux.org> 1.15-alt1
- Split into two packages, with kernel dependence and without it.
- Remove dependence on make-initrd by generating own initramfs.

* Mon Aug 17 2020 Vitaly Chikunov <vt@altlinux.org> 1.14-alt1
- armh: Enable tcg support.

* Wed Aug 12 2020 Vitaly Chikunov <vt@altlinux.org> 1.13-alt1
- Make kernel shutdown quicker.

* Mon Aug 10 2020 Vitaly Chikunov <vt@altlinux.org> 1.12-alt1
- Make console output non-truncated on shutdown.
- Fix tty support for console.

* Sat Aug 08 2020 Vitaly Chikunov <vt@altlinux.org> 1.11-alt1
- x86_64,i586: Try to make kernel more robust with 'no_timer_check'.
- spec: Move checkinstall %%pre outside of %%ifarch to fix noarch check.

* Thu Jul 02 2020 Vitaly Chikunov <vt@altlinux.org> 1.10-alt1
- ppc: Use cap-ccf-assist=off for kvm-type=HV.

* Tue Jun 30 2020 Vitaly Chikunov <vt@altlinux.org> 1.9-alt1
- Propagate exported functions into vm subshell.

* Sat Jun 20 2020 Vitaly Chikunov <vt@altlinux.org> 1.8-alt1
- aarch64: Fix `.gic_version not found' (qemu).
- spec: Fix `different set of noarch packages' (girar).

* Mon Feb 24 2020 Vitaly Chikunov <vt@altlinux.org> 1.7-alt2
- Require /dev/kvm.

* Fri Jan 24 2020 Vitaly Chikunov <vt@altlinux.org> 1.7-alt1
- ppc: Make use of KVM.

* Thu Jan 23 2020 Vitaly Chikunov <vt@altlinux.org> 1.6-alt1
- Fix `Multiple devices detected in same VirtFS export' warning.

* Thu Jan 23 2020 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- aarch64: Make use of KVM.

* Mon Dec 30 2019 Ivan A. Melnikov <iv@altlinux.org> 1.4.1-alt3
- Fix build on qemu-less architectures (closes: #37629).

* Sat Dec 28 2019 Vitaly Chikunov <vt@altlinux.org> 1.4.1-alt2
- Fix build on unsupported arches.

* Mon Dec 16 2019 Vitaly Chikunov <vt@altlinux.org> 1.4.1-alt1
- Quickfix of 1.4 (MAXMEM handling).

* Mon Dec 16 2019 Vitaly Chikunov <vt@altlinux.org> 1.4-alt2
- Optimize spec.
- Add checkinstall package.

* Mon Dec 16 2019 Vitaly Chikunov <vt@altlinux.org> 1.4-alt1
- Limit 32-bit system memory.

* Thu Dec 12 2019 Vitaly Chikunov <vt@altlinux.org> 1.3-alt1
- Initialize cpu and mem to the max, support share_network=1,
  handle multiple kernels using --kernel= option.

* Sat Aug 31 2019 Vitaly Chikunov <vt@altlinux.org> 1.2-alt1
- Improvements corresponding to v1.2.

* Mon Aug 19 2019 Vitaly Chikunov <vt@altlinux.org> 1.1-alt1
- Do not use `qemu' binary on x86 due to qemu repackage.

* Mon Aug 19 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt5
- Make stub vm-run output a warning message

* Sun Aug 18 2019 Michael Shigorin <mike@altlinux.org> 1.0-alt4
- Rework to provide a stub package on qemu-unsupported arches
  (that can be added into BuildRequires: unconditionally).

* Thu Aug 15 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt3
- Add ExclusiveArch for only supported arches.

* Mon Aug 12 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt2
- Improvements for ppc64le.

* Mon Aug 05 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- Initial version.

