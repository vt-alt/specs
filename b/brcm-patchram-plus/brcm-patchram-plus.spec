Name: brcm-patchram-plus
Version: 0.1.1
Release: alt1

Summary: Tool to patch Broadcom Bluetooth chips.
License: Apache-2.0
Group: System/Base
URL: https://github.com/fredldotme/brcm-patchram-plus
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Source: %name-%version.tar
BuildRequires: gcc

%description
This program downloads a patchram files in the HCD format
to Broadcom Bluetooth based silicon and combo chips
and other utility functions.

%prep
%setup

%build
gcc -o brcm_patchram_plus brcm_patchram_plus.c

%install
install -D brcm_patchram_plus %buildroot/usr/bin/brcm_patchram_plus
install -D -m 644 attach-bluetooth.service %buildroot/lib/systemd/system/attach-bluetooth.service

%files
/usr/bin/brcm_patchram_plus
/lib/systemd/system/attach-bluetooth.service

%changelog
* Fri Mar 27 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.1.1-alt1
- Initial build
