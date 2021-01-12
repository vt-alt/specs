Name: hw-probe
Version: 1.5
Release: alt1
Summary: A tool to check operability of computer hardware
License: LGPLv2.1+
Group: Development/Other
Url: https://github.com/linuxhw/hw-probe
Source: %name-%version.tar

%define _unpackaged_files_terminate_build 1

Requires: perl
Requires: perl-Digest-SHA
Requires: perl-Data-Dumper-Concise
Requires: perl-libwww
Requires: curl
Requires: hwinfo
Requires: dmidecode
Requires: edid-decode
Requires: pciutils
Requires: usbutils
Requires: smartmontools
Requires: hdparm
Requires: sysstat
Requires: util-linux
Requires: lm_sensors3
Requires: lsb-release
Requires: acpica
%ifarch x86_64 %ix86
Requires: mcelog
%endif

%description
A tool to check operability of computer hardware and upload result
to the Linux hardware database.

Probe - is a snapshot of your computer's hardware state and system
logs. The tool returns a permanent URL to view the probe of the
computer.

The tool is intended to simplify collecting of logs necessary for
investigating hardware related problems. Just ask user to run one
simple command to collect all the system logs at once:

 sudo hw-probe -all -upload

By creating probes you contribute to the HDD/SSD Real-Life
Reliability Test study: https://github.com/linuxhw/SMART


%prep
%setup

%install
%makeinstall_std

%files
%doc README.md
%_bindir/%name

%changelog
* Thu Jan 07 2021 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- New version.

* Mon Oct 08 2018 Egor Zotov <egorz@altlinux.org> 1.4-alt1
- Initial build for ALT.

