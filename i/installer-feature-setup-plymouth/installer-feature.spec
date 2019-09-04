Name: installer-feature-setup-plymouth
Version: 0.5.4
Release: alt1

Summary: Set up plymouth
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Set up environment plymouth

%prep
%setup

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Sep 04 2019 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1
- Handle empty uuid (closes: #37191).

* Mon Aug 05 2019 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- do not fail without grub

* Sat Nov 16 2013 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- do use plymouth with sysvinit at least for m-p
  (partially reverts 0.5-alt1)

* Thu Apr 18 2013 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Disable plymouth if root on luks only.

* Thu Mar 21 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- don't use plymouth with sysvinit

* Thu Feb 07 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- don't setup plymouth if LUKS exists

* Wed Jun 13 2012 Michael Shigorin <mike@altlinux.org> 0.3.3-alt1
- add "quiet" option too

* Wed Jun 13 2012 Michael Shigorin <mike@altlinux.org> 0.3.2-alt1
- don't uncomment plymouth theme if that results in a duplicate

* Fri Jun 01 2012 Michael Shigorin <mike@altlinux.org> 0.3.1-alt1
- dropped an extra space in regexp causing it not to match

* Mon Nov 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- setup initrd.mk resurrected

* Fri Nov 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- setup initrd.mk removed: plymouth installs inintrd.mk.d/plymouth.mk

* Tue Nov 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- furst build


