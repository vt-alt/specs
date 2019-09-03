Name: pve-storage
Summary: PVE storage management library
Version: 6.0.7
Release: alt1
License: GPLv3
Group: Development/Perl
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64 aarch64

Requires: open-iscsi smartmontools gdisk parted hdparm
Requires: multipath-tools ceph >= 12.2.1 zfs-utils

Source: pve-storage.tar.xz
Patch: pve-storage-alt.patch

BuildRequires: librados2-perl pve-common pve-cluster pve-doc-generator pve-access-control xmlto
BuildRequires: perl(File/chdir.pm) perl(Net/DBus.pm)

%description
This package contains the storage management library used by PVE

%prep
%setup -q -n %name
%patch -p1

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_sysconfdir/modules-load.d
cat << __EOF__ > %buildroot%_sysconfdir/modules-load.d/pve-storage.conf
rbd
__EOF__

%files
%_sysconfdir/modules-load.d/pve-storage.conf
%_sbindir/pvesm
%perl_vendor_privlib/PVE
%_datadir/bash-completion/completions/*
%_datadir/zsh/vendor-completions/*
%_man1dir/pvesm.1*

%changelog
* Mon Aug 26 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt1
- 6.0-7

* Tue Jul 30 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.6-alt1
- 6.0-6

* Mon May 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.43-alt1
- 5.0-43

* Wed Jan 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.36-alt1
- 5.0-36

* Thu Dec 06 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.33-alt1
- 5.0-33

* Mon Nov 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.31-alt1
- 5.0-31

* Thu Sep 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.23-alt2
- fixed parse RBD size format

* Wed Jul 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.23-alt1
- 5.0-23

* Tue Dec 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.17-alt1
- 5.0-17

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.16-alt1
- 5.0-16

* Tue Oct 10 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.15-alt1
- 5.0-15

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.14-alt0.M80C.1
- backport to c8 branch

* Wed Sep 06 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.14-alt1
- 5.0-14

* Thu Jul 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt1
- 5.0-12

* Wed Jul 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.70-alt2
- update requires

* Mon Dec 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.70-alt1
- 4.0-70

* Wed Nov 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.68-alt1
- 4.0-68

* Fri Oct 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.67-alt1
- 4.0-67

* Thu Oct 13 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.66-alt2
- added requires zfs-utils

* Sun Oct 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.66-alt1
- 4.0-66

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.63-alt1
- 4.0-63

* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.61-alt1
- 4.0-61

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.57-alt1
- 4.0-57

* Sun Jun 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.55-alt1
- 4.0-55

* Wed Jun 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.54-alt1
- 4.0-54

* Wed Jun 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.52-alt1
- 4.0-52

* Wed Jun 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.50-alt1
- 4.0-50

* Mon Feb 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt1
- 4.0-40

* Thu Dec 03 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.35-alt1
- initial release

