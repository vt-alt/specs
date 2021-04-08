%define _unpackaged_files_terminate_build 1

Name: suspend-psmouse-workaround
Version: 1.0
Release: alt2

Summary: Workaround to fix pointing devices after suspend
License: none
Group: Other

Source0: 50-psmouse
Source1: lidopen-psmouse
Source2: lidopen-psmouse.sh
Source3: psmouse.sh

Requires: pm-utils, acpid

BuildArch: noarch

%description
Hooks for pm-utils, acpid and systemd-sleep to reload psmouse
module after hibernation in order to fix some pointing devices,
including Lenovo ThinkPad L13, Lenovo ThinkPad E15.

%install
mkdir -p %buildroot%_sysconfdir/pm/sleep.d/
mkdir -p %buildroot%_sysconfdir/acpi/{events,actions}/
mkdir -p %buildroot%systemd_unitdir-sleep/
install -pD -m755 %SOURCE0 %buildroot%_sysconfdir/pm/sleep.d/
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/acpi/events/
install -pD -m755 %SOURCE2 %buildroot%_sysconfdir/acpi/actions/
install -pD -m755 %SOURCE3 %buildroot%systemd_unitdir-sleep/

%post
printf "Reloading acpid configuration: "
if kill -1 `pidof acpid` &>/dev/null; then
	echo OK
else
	echo FAILED
fi

%files
%_sysconfdir/pm/sleep.d/*
%_sysconfdir/acpi/events/*
%_sysconfdir/acpi/actions/*
%systemd_unitdir-sleep/*

%changelog
* Wed Apr 07 2021 Egor Ignatov <egori@altlinux.org> 1.0-alt2
- Add hook for systemd-sleep

* Wed Mar 24 2021 Egor Ignatov <egori@altlinux.org> 1.0-alt1
- First build for ALT
