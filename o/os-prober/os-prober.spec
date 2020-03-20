%filter_from_requires s,python-module-zope\.app\.appsetup,,

Name: os-prober
Version: 1.77
Release: alt3

Summary: Operating systems detector
License: GPLv2+
Group: System/Configuration/Boot and Init
Url: https://salsa.debian.org/installer-team/os-prober
#Git: https://salsa.debian.org/installer-team/os-prober.git

Source0: %name-%version.tar

Patch: %name-1.42-UUID-rootdev-alt.patch
Patch1: %name-1.77-alt-grub2-detect-auto-reference.patch
Patch2: %name-1.77-alt-grub2-skip-30_os-prober-parsing.patch

%description
This is a small package that may be depended on by any bootloader
installer package to detect other filesystems with operating systems on
them, and work out how to boot other linux installs.

%prep
%setup
%patch -p1
%patch1 -p1 
%patch2 -p1

%build
%make_build

%install
mkdir -p %buildroot/%_bindir/
cp -a os-prober %buildroot/%_bindir/
cp -a linux-boot-prober %buildroot/%_bindir/
mkdir -p %buildroot/usr/lib/
mkdir -p %buildroot/usr/lib/%name
cp -a newns %buildroot/usr/lib/%name

mkdir -p %buildroot/usr/lib/os-probes/init
cp -a os-probes/init/common/* %buildroot/usr/lib/os-probes/init
mkdir -p %buildroot/usr/lib/os-probes/mounted
cp -a os-probes/mounted/x86/* %buildroot/usr/lib/os-probes/mounted/
cp -a os-probes/mounted/common/* %buildroot/usr/lib/os-probes/mounted/
cp -a os-probes/common/* %buildroot/usr/lib/os-probes/

mkdir -p %buildroot/usr/lib/linux-boot-probes/mounted
cp -a linux-boot-probes/common/* %buildroot/usr/lib/linux-boot-probes
cp -a linux-boot-probes/mounted/x86/* %buildroot/usr/lib/linux-boot-probes/mounted/
cp -a linux-boot-probes/mounted/common/* %buildroot/usr/lib/linux-boot-probes/mounted/

mkdir -p %buildroot%_datadir/%name
cp -a common.sh %buildroot%_datadir/%name/
mkdir -p %buildroot%_localstatedir/%name

%files
%doc README
%_bindir/*
/usr/lib/linux-boot-probes
/usr/lib/os-probes
/usr/lib/%name
%_datadir/%name/
%_localstatedir/%name

%changelog
* Fri Mar 20 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.77-alt3
- fix grub2-skip-30_os-prober-parsing patch

* Wed Mar 11 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.77-alt2
- add grub2-detect-auto-reference patch
- add grub2-skip-30_os-prober-parsing patch

* Tue Apr 30 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.77-alt1
- 1.77 (closes: #37224)
  + relies on grub-mount

* Fri Mar 03 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1.74-alt1
- 1.74

* Mon Nov 02 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.70-alt1
- 1.70
- Fix (ALT #31347)

* Thu May 23 2013 Mikhail Efremov <sem@altlinux.org> 1.61-alt1
- 1.61

* Thu May 23 2013 Michael Shigorin <mike@altlinux.org> 1.52-alt2
- dropped evms related hack that is long irrelevant (see #28181)

* Fri May 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.52-alt1
- 1.52

* Tue Aug 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.48-alt1
- 1.48

* Mon Jul 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.47-alt1
- 1.47

* Mon Apr 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.44-alt1
- 1.44

* Tue Mar 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.42-alt2
- add suport for UUID= root devices in lilo.conf (ALT #25168)

* Tue Feb 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.42-alt1
- 1.42

* Fri Nov 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.41-alt1
- 1.41

* Mon Oct 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.39-alt2
- hackaround evms

* Sun Jul 11 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.39-alt1
- 1.39

* Mon Jun 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.38-alt1
- 1.38

* Mon Apr 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.36-alt1
- initial
