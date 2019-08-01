Name: systemd-settings
Version: 2
Release: alt1
Summary: Settings for systemd
Url: https://packages.altlinux.org/en/Sisyphus/srpms/%name
Group: System/Configuration/Boot and Init
License: GPLv2+
BuildArch: noarch

Source: %name-%version.tar

%description
This package contains drop-in settings for systemd.

%package disable-user-systemd-for-selinux
Summary: Disable user systemd --user  for ALT selinux systems
Group: System/Configuration/Boot and Init

%description disable-user-systemd-for-selinux
Disabling user@.service, which attempts to start
systemd for user sessions, not needed or allowed
in ALT selinux systems.

%package disable-kill-user-processes
Summary: Set global KillUserProcesses=no
Group: System/Configuration/Boot and Init
Requires: /lib/systemd/systemd-logind
Conflicts: %name-enable-kill-user-processes

%description disable-kill-user-processes
%summary

%package enable-kill-user-processes
Summary: Set global KillUserProcesses=yes
Group: System/Configuration/Boot and Init
Requires: /lib/systemd/systemd-logind
Conflicts: %name-disable-kill-user-processes

%description enable-kill-user-processes
%summary

%package enable-showstatus
Summary: Set global ShowStatus=yes
Group: System/Configuration/Boot and Init

%description enable-showstatus
%summary

%package disable-dumpcore
Summary: Set global DumpCore=no
Group: System/Configuration/Boot and Init

%description disable-dumpcore
%summary

%package enable-log-to-tty12
Summary: Set global TTYPath=/dev/tty12 for forward logs
Group: System/Configuration/Boot and Init

%description enable-log-to-tty12
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot/lib/systemd/{logind.conf.d,system.conf.d,journald.conf.d,system/user@.service.d}

install -p -m644 disable-kill-user-processes.conf \
    %buildroot/lib/systemd/logind.conf.d/disable-kill-user-processes.conf
install -p -m644 enable-kill-user-processes.conf \
    %buildroot/lib/systemd/logind.conf.d/enable-kill-user-processes.conf
install -p -m644 enable-showstatus.conf \
    %buildroot/lib/systemd/system.conf.d/enable-showstatus.conf
install -p -m644 disable-dumpcore.conf \
    %buildroot/lib/systemd/system.conf.d/disable-dumpcore.conf
install -p -m644 enable-log-to-tty12.conf \
    %buildroot/lib/systemd/journald.conf.d/enable-log-to-tty12.conf

install -p -m644 disable-user-systemd-for-selinux.conf \
    %buildroot/lib/systemd/system/user@.service.d/disable-user-systemd-for-selinux.conf

%files disable-kill-user-processes
/lib/systemd/logind.conf.d/disable-kill-user-processes.conf

%files enable-kill-user-processes
/lib/systemd/logind.conf.d/enable-kill-user-processes.conf

%files disable-user-systemd-for-selinux
/lib/systemd/system/user@.service.d/disable-user-systemd-for-selinux.conf

%files enable-showstatus
/lib/systemd/system.conf.d/enable-showstatus.conf

%files disable-dumpcore
/lib/systemd/system.conf.d/disable-dumpcore.conf

%files enable-log-to-tty12
/lib/systemd/journald.conf.d/enable-log-to-tty12.conf

%changelog
* Thu Jul 25 2019 Alexey Shabalin <shaba@altlinux.org> 2-alt1
- Added packages:
  + enable-showstatus
  + disable-dumpcore
  + enable-log-to-tty12

* Thu Apr 05 2018 Denis Medvedev <nbr@altlinux.org> 1-alt2
- Added ALT selinux settings as additional packages. Changed
package group.

* Sat Mar 31 2018 Alexey Shabalin <shaba@altlinux.ru> 1-alt1
- Initial build

