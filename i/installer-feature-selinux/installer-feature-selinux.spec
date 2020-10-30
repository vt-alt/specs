Name: installer-feature-selinux
Version: 0.12
Release: alt12

Summary: Installer selinux hooks
License: GPL
Group: System/Configuration/Other

Url: http://altlinux.org/sl
Source: %name-%version.tar

BuildArch: noarch
Provides: %name-stage2

BuildRequires(pre): rpm-macros-alterator

%description
This package contains selinux hooks for installer.

%prep
%setup

%install
%define hookdir %_datadir/install2
mkdir -p %buildroot%hookdir/{initinstall,preinstall,postinstall}.d
mkdir -p %buildroot%_alterator_libdir/hooks/setup-postinstall.d
install -pm755 preinstall.sh %buildroot%hookdir/preinstall.d/90-selinux.sh
install -pm755 postinstall.sh %buildroot%hookdir/postinstall.d/90-selinux.sh
install -pm755 preinstall.sh %buildroot%_alterator_libdir/hooks/setup-postinstall.d/80-selinux.sh

%files
%hookdir/preinstall.d/*
%hookdir/postinstall.d/*
%_alterator_libdir/hooks/setup-postinstall.d/*

%changelog
* Thu Oct 15 2020 Anton Midyukov <antohami@altlinux.org> 0.12-alt12
- Added support extlinux.conf, bootconf (Tavolga)
- Added support alterator-setup
- preinstall.sh: Not enable enforcing mode

* Mon May 25 2020 Denis Medvedev <nbr@altlinux.org> 0.12-alt11
- different format of inline doc. Small fix.

* Fri May 22 2020 Denis Medvedev <nbr@altlinux.org> 0.12-alt10
- proper escaping in inline documents for scripts that fix working
of level showing applet.

* Thu May 21 2020 Denis Medvedev <nbr@altlinux.org> 0.12-alt9
- fix typos in scripts.

* Fri Apr 24 2020 Denis Medvedev <nbr@altlinux.org> 0.12-alt8
- prepared scripts for safe values for seapplet. Seapplet doesn't work
with DRI3 and MITSHM in QT.

* Wed Oct 09 2019 Denis Medvedev <nbr@altlinux.org> 0.12-alt7
- setting shell for officer if selinux

* Fri Jun 28 2019 Denis Medvedev <nbr@altlinux.org> 0.12-alt6
- also removed extra smem - already added by installer.

* Tue Jun 25 2019 Michael Shigorin <mike@altlinux.org> 0.12-alt5
- fix e2k session setup under systemd 239
- harden/denoise scripts regarding absent files

* Thu May 23 2019 Denis Medvedev <nbr@altlinux.org> 0.12-alt4
- small fix in regexp

* Thu May 23 2019 Denis Medvedev <nbr@altlinux.org> 0.12-alt3
- Integrated root login disabling features.

* Wed May 22 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.12-alt2
- fixed work without dovecot installed

* Tue May 21 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.12-alt1
- disable ipv6 in dovecot.conf

* Mon Apr 15 2019 Denis Medvedev <nbr@altlinux.org> 0.11-alt1
- added officer group wheel for him personally and setup
smem and disable ipv6.

* Tue Apr 09 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.10-alt1
- merge c8.1 and sisyphus versions
- disable pam_mktemp

* Mon Jan 21 2019 Denis Medvedev <nbr@altlinux.org> 0.9-alt1.M80C.3
- e2k support

* Fri Oct 05 2018 Denis Medvedev <nbr@altlinux.org> 0.9-alt1.M80C.2
- added officer to users that are being allowed login to console

* Tue May 22 2018 Michael Shigorin <mike@altlinux.org> 0.9-alt3
- e2k support
- missing grub is not a problem (at least not this package's problem)

* Wed Mar 28 2018 Denis Medvedev <nbr@altlinux.org> 0.9-alt1.M80C.1
- to c8

* Wed Mar 28 2018 Denis Medvedev <nbr@altlinux.org> 0.9-alt2
- fixed wrong string characters when adding string in common_login

* Thu Mar 15 2018 Denis Medvedev <nbr@altlinux.org> 0.9-alt1
- fixed wrong pam_selinux placement not in end of file of common_login

* Tue Feb 14 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.8-alt1
- disable users listing in lightdm

* Mon Feb 13 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.7-alt1
- disable non-root logins in console

* Fri Feb 06 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt2
- typo fixed

* Mon Apr 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- adding pam_permit into pam.d/newrole added

* Thu Apr 03 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- make stage indifferent

* Wed Apr 02 2014 Timur Aitov <timonbl4@altlinux.org> 0.4-alt1
- [0.4]

* Wed Dec 11 2013 Timur Aitov <timonbl4@altlinux.org> 0.3-alt1
- [0.3]

* Tue Aug 06 2013 Timur Aitov <timonbl4@altlinux.org> 0.2-alt1
- [0.2]

* Tue Jun 25 2013 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- first build

