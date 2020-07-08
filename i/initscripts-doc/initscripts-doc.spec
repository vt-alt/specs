Name: initscripts-doc
Version: 5.49.1
Release: alt3
Serial: 1

Summary: The initscripts documentation
License: GPLv2+
Group: System/Base

Url: http://altlinux.org/sysvinit
Source1: sysvinitfiles
Source2: sysconfig.txt

BuildArch: noarch
AutoReqProv: no
Obsoletes: initscripts

%description
This package contains documentation for initscripts:
- guidelines for writing those;
- /etc/sysconfdir/ use.

%prep
%setup -qcT
install -pm644 %SOURCE1 %SOURCE2 .

%files
%doc sysconfig.txt sysvinitfiles

%changelog
* Wed Jun 24 2020 Michael Shigorin <mike@altlinux.org> 1:5.49.1-alt3
- renamed into initscripts-doc.

* Wed Nov 17 2004 Dmitry V. Levin <ldv@altlinux.org> 1:5.49.1-alt2
- s/net-scripts/network-config-subsystem/ (#5489).

* Tue Apr 22 2003 Dmitry V. Levin <ldv@altlinux.org> 1:5.49.1-alt1
- Removed all but compatibility dependencies and old documentation.
  All the rest is packaged separately.

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 5.49-ipl54mdk
- %_initdir/sound: don't sort aliases in LoadModule (#0001802).
- %_initdir/clock: test $HWCLOCK_ADJUST also for "true" value (#0002351).
- %_initdir/functions:
  + fixed check logic in daemon() a bit (#0002407).
  + fixed return code in killproc() (#0002412).
- %_initdir/outformat: check argumnets being passed to tput (#0002450).
- /etc/sysctl.conf:
  + set "net.ipv4.icmp_echo_ignore_broadcasts = 1" by default (#0002472);
  + added comments from Owl's sysctl.conf file.
- usernetctl: support variable definitions quoted with single quotes.
