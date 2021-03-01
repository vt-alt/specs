# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: systemd-boot-trigger
Version: 1.0
Release: alt5

Summary: Filetrigger for systemd-boot
License: GPL-2.0-only
Group: System/Base
Url: http://git.altlinux.org/
BuildArch: noarch

Source: %name-%version.tar

%description
Automatically install kernel into EFI partition to boot with systemd-boot.

%prep
%setup

%build

%install
install -p -m755 -D filetrigger %buildroot%_rpmlibdir/systemd-boot.filetrigger

%files
%_rpmlibdir/systemd-boot.filetrigger

%changelog
* Wed Sep 30 2020 Alexey Shabalin <shaba@altlinux.org> 1.0-alt5
- Fixed path to kernel-install (changed in systemd-246.6-alt2).

* Tue Sep 22 2020 Vitaly Chikunov <vt@altlinux.org> 1.0-alt4
- Optimize installation process more.

* Tue Sep 22 2020 Vitaly Chikunov <vt@altlinux.org> 1.0-alt3
- Optimize installation process.

* Mon Sep 21 2020 Vitaly Chikunov <vt@altlinux.org> 1.0-alt2
- Autocreate esp/machine_id dir.

* Sat Sep 19 2020 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- Initial version.
