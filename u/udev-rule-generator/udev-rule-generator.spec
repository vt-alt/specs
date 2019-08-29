Name: udev-rule-generator
Epoch: 2
Version: 1.2
Release: alt1
Summary: Common package for udev rule generator
Url: https://packages.altlinux.org/en/Sisyphus/srpms/%name
Group: System/Configuration/Hardware
License: GPLv2+
PreReq: udev >= 1:238-alt4
BuildArch: noarch

Provides: udevd-final

Source: %name-%version.tar

%description
This package contains common files for udev-rule-generator:
 - udev-final SysV init script
 - udev-final.service systemd unit
 - rule_generator.functions

%package cdrom
Summary: CD rule generator for udev
Group: System/Configuration/Hardware
License: GPLv2+
BuildArch: noarch
PreReq: udev-rules
PreReq: %name = %EVR

%description cdrom
This package contains CD rule generator for udev

%package net
Summary: Net rule generator for udev
Group: System/Configuration/Hardware
License: GPLv2+
BuildArch: noarch
PreReq: udev-rules
PreReq: %name = %EVR

%description net
This package contains Net rule generator for udev

%prep
%setup

%build

%install
mkdir -p %buildroot{%_initdir,%_unitdir,{%_sysconfdir,/lib}/udev/rules.d,%_sysconfdir/sysconfig}
install -p -m755 udevd-final.init %buildroot%_initdir/udevd-final
install -p -m644 udevd-final.service %buildroot%_unitdir/udevd-final.service

# Create ghost files
touch %buildroot%_sysconfdir/udev/rules.d/70-persistent-net.rules
touch %buildroot%_sysconfdir/udev/rules.d/70-persistent-cd.rules

# udev rule generator
install -p -m644 rule_generator.functions %buildroot/lib/udev/
install -p -m755 write_net_rules %buildroot/lib/udev/
install -p -m644 write_net_rules.sysconfig %buildroot%_sysconfdir/sysconfig/write_net_rules
install -p -m644 75-persistent-net-generator.rules %buildroot/lib/udev/rules.d/
install -p -m755 write_cd_rules %buildroot/lib/udev/
install -p -m644 75-cd-aliases-generator.rules %buildroot/lib/udev/rules.d/
ln -s /dev/null %buildroot%_sysconfdir/udev/rules.d/80-net-setup-link.rules

%preun
%preun_service udevd-final

%post cdrom
%post_service udevd-final

%post net
%post_service udevd-final

%files
/lib/udev/rule_generator.functions
%_initdir/udevd-final
%_unitdir/udevd-final.service

%files cdrom
%config(noreplace,missingok) %verify(not md5 size mtime) %ghost %_sysconfdir/udev/rules.d/70-persistent-cd.rules
/lib/udev/rules.d/75-cd-aliases-generator.rules
/lib/udev/write_cd_rules

%files net
%config(noreplace,missingok) %verify(not md5 size mtime) %ghost %_sysconfdir/udev/rules.d/70-persistent-net.rules
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/sysconfig/write_net_rules
%_sysconfdir/udev/rules.d/80-net-setup-link.rules
/lib/udev/rules.d/75-persistent-net-generator.rules
/lib/udev/write_net_rules


%changelog
* Thu Aug 29 2019 Sergey Y. Afonin <asy@altlinux.org> 2:1.2-alt1
- returned "eth" by default in write_net_rules (problems with
  the "ether" name detected in some applications)
- added sysconfig/write_net_rules

* Tue Aug 20 2019 Sergey Y. Afonin <asy@altlinux.org> 2:1.1-alt1
- changed /var/lock to /run/lock (antohami@altlinux, ALT #35889)
- changed "eth" to "ether" in generated rules (ALT #32167)

* Fri Apr 06 2018 Alexey Shabalin <shaba@altlinux.ru> 2:1-alt2
- update post and preun scripts

* Sat Mar 31 2018 Alexey Shabalin <shaba@altlinux.ru> 2:1-alt1
- Initial build

