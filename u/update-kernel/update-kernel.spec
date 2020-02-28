Name: update-kernel
Version: 0.9.18
Release: alt1

Summary: Update kernel and modules
License: GPL-2.0+
Group: System/Kernel and hardware

Source: %name-%version.tar
BuildArch: noarch

Requires: apt
Requires: /usr/bin/rpmevrcmp
# May use rpm -q with an Epoch in the pkg argument (as well as Buildtime and
# Disttag -- but these are dependent on the output from APT, and APT cares
# about the correct dependencies on such features).
Requires: RPMQ(EPOCH)

%description
This package contains a script to conveniently update
kernel and modules.

It works by installing a new package set along with existing kernel
so that you don't end up without a kernel guaranteed to boot (your
good old one); by default, it will look for the most recent package
of the same flavour (e.g. "std-def") and try to install all the same
modules as already installed for that.

See also:
http://lists.altlinux.org/pipermail/community/2005-November/366618.html
http://lists.altlinux.org/pipermail/sisyphus/2006-November/192226.html

%prep
%setup

%install
install -pDm755 update_kernel_modules_cetus.sh %buildroot%_sbindir/%name
install -pm755 remove-old-kernels %buildroot%_sbindir/

%files
%_sbindir/update-kernel
%_sbindir/remove-old-kernels

%changelog
* Wed Feb 12 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.18-alt1
- Support for single word kernel flavours (closes: #36835).
- Update license tag to be more specific.

* Mon Dec 30 2019 Sergey Novikov <sotor@altlinux.org> 0.9.17-alt1
- update-kernel: remove duplicates modules entries (Closes: #37690)

* Fri Dec 20 2019 Oleg Solovyov <mcpain@altlinux.org> 0.9.16-alt1
- NMU: do not call apt when there are no kernels to remove

* Thu Dec 19 2019 Oleg Solovyov <mcpain@altlinux.org> 0.9.15-alt1
- NMU: protect latest kernel from removing (Closes: #34314)
- NMU: add "-a|--all" option to remove kernels with all flavours
  (Closes: #34141)

* Wed Jun 05 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9.14-alt1
- update-kernel: fixed in the presence of disttags in package IDs
  printed by APT (apt-cache pkgnames).

* Tue May 28 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9.13-alt1
- remove-old-kernels: APT invocation (to remove installed pkgs) rewritten in
  a more portable way. (A preparation for APT with support for disttags.)

* Wed May 15 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9.12-alt1
- APT invocation (to install the modules) rewritten in a more robust way.
  (A preparation for APT with support for disttags.)

* Mon Apr 01 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9.11-alt2
- Rewritten with another bashism that doesn't require /proc/.
- Requires: apt (important not for real systems, but for testing in hasher).

* Wed Aug 22 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.11-alt1
- add -y option as alias for -f (force operation) (ALT bug 35283)

* Fri Aug 04 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- force select newest kernel module package (ALT bug 22572)

* Sun Apr 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt1
- remove-old-kernels: check only current flavour (or used with -t) (ALT bug #30717)
- remove-old-kernels: do not delete current or newest kernel(s)

* Sat Jan 23 2016 Terechkov Evgenii <evg@altlinux.org> 0.9.8-alt1
- Add help/force/dry-run options to remove-old-kernels

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- check if we already have lastest kernel package (alt bug #26715)

* Thu Jul 11 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- skip install if the latest kernel is already installed (ALT bug #26715)

* Tue Dec 25 2012 Terechkov Evgenii <evg@altlinux.org> 0.9.5-alt1
- Add --download-only (--dry-run/-n) support (ALT#25300)

* Thu Dec 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.4-alt2
- don't try to install unexistent modules

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 0.9.4-alt1
- Install kernel and modules together

* Tue Sep 28 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9.3-alt1
[Dmitriy Kulik]
- Add interactive mode (-i)
- Add option -a|--all for installing all modules (Closes: #22271)

* Sat Oct 17 2009 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- removed warning on x11setupdrv absence due to its obsolescence
  (closes: #21872)

* Mon Aug 31 2009 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1
- added one-liner to fix path to x11presetdrv (closes: #21301)

* Thu Mar 05 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9-alt1
- Add x11presetdrv calling (mike)
- Add ldconfig call after x11setupdrv (mike)
- Remove message about updating kernel-headers and kernel-headers-modules

* Thu Feb 26 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.1-alt1
- update_kernel: run x11setupdrv only if Xorg present

* Sun Dec 28 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8-alt1
- update_kernel: update kernel-headers and kernel-headers-modules also
  (me, kipruss) (Closes: #18259)
- Add new script remove-old-kernels. It removes all kernels except current
  (Closes: #14764)

* Mon Nov 24 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.7-alt1
- Use rpmevrcmp instead of rpmvercmp
- Use only serial/epoch+version+release when comparing versions

* Mon Sep 22 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.6-alt1
- Run x11setupdrv if needed (mike)
- Spelling fixes (mike)

* Mon Sep 01 2008 Vladimir V Kamarzin <vvk@altlinux.org> 0.5-alt1
- Fix module-names calculation (Closes: #16946)

* Tue Apr 22 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.4-alt1
- Rewrite modules upgrading procedure (Closes: #15380)

* Tue Apr 15 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3-alt4
- update_kernel: bugfix in options parser

* Fri Apr 11 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3-alt3
- Set dependency on /usr/bin/rpmvercmp instead of rpm-utils

* Thu Mar 13 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3-alt2
- Add dependency on rpm-utils

* Wed Mar 12 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3-alt1
- update-kernel:
  + use rpmvercmp(1) for getting newest kernel package name
  + old code for manual choosing of kernel flavour/release replaced with
  options -t/-r

* Mon Mar 03 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2-alt1
- update-kernel:
  + implemented "force" mode
  + recode script to utf8
  + update copyright header

* Mon Feb 18 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- clarified License: (with lav@)
- noarch

* Sun Feb 17 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial package
- many thanks to Vitaly Lipatov (lav@) and Anatoly Kitouwaykin (cetus)
  for writing and improving the script -- I just had to package it

