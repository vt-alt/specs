%define original_kernel_version	5.3
%define kernel_version		5.3
%define patch_level		%nil

%define kernel_fullversion	%kernel_version%patch_level

# Numeric extra version scheme developed by Alexander Bokovoy:
# 0.0.X -- preX
# 0.X.0 -- rcX, testX
# 1.0.0 -- release
%define patch_level_numeric     1.0.0

Name: kernel-source-%kernel_version
Version: %patch_level_numeric
Release: alt1

Summary: Linux kernel %kernel_fullversion sources
License: GPL-2.0-only
Group: Development/Kernel
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Source: linux-%kernel_fullversion.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-kernel
AutoReq: no

%description
Kernel sources for Linux kernel %kernel_fullversion.

%prep
%setup -c
mv linux-%kernel_fullversion kernel-source-%kernel_version
cd kernel-source-%kernel_version

%install
mkdir -p %kernel_srcdir
tar --owner=root --group=root --mode=u+w,go-w,go+rX -cf \
	%kernel_srcdir/kernel-source-%kernel_version.tar \
	kernel-source-%kernel_version

%files
%kernel_src/kernel-source-%kernel_version.tar

%changelog
* Mon Sep 16 2019 Kernel Bot <kernelbot@altlinux.org> 1.0.0-alt1
- v5.2 -> v5.3.

* Sun Jul 07 2019 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1
- v5.1 -> v5.2.

* Mon May 06 2019 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1
- v5.0 -> v5.1.

* Sun Mar 03 2019 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1
- v4.20 -> v5.0.

* Mon Dec 24 2018 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1
- v4.19 -> v4.20.

* Mon Oct 22 2018 Kernel Bot <kernelbot@altlinux.org> 1.0.0-alt1
- v4.18-> v4.19

* Mon Aug 13 2018 Kernel Bot <kernelbot@altlinux.org> 1.0.0-alt1
- v4.17-> v4.18

* Mon Jun 04 2018 Kernel Bot <kernelbot@altlinux.org> 1.0.0-alt1
- v4.16 -> v4.17.

* Mon Apr 02 2018 Kernel Bot <kernelbot@altlinux.org> 1.0.0-alt1
- v4.15 -> v4.16.

* Mon Jan 29 2018 Kernel Bot <kernelbot@altlinux.org> 1.0.0-alt1
- v4.14 -> v4.15.

* Sun Nov 12 2017 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1
- v4.13 -> v4.14.

* Sun Sep 03 2017 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1
- v4.12 -> v4.13.

* Mon Jul 03 2017 Kernel Bot <kernelbot@altlinux.org> 1.0.0-alt1
- v4.12

* Wed May 17 2017 Kernel Bot <kernelbot@altlinux.org> 1.0.0-alt1
- v4.11

* Sun Apr 16 2017 Dmitry V. Levin <ldv@altlinux.org> 0.7.0-alt1
- v4.10 -> v4.11-rc7.

* Sun Feb 19 2017 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1
- v4.10-rc8 -> v4.10.

* Mon Feb 13 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.0-alt1
- Updated to 4.10-rc8.
- Cleaned up specfile.

* Mon Dec 12 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0.0-alt1
- 4.9

* Mon Oct 03 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0.0-alt1
- 4.8

* Mon Jul 25 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0.0-alt1
- 4.7

* Tue May 17 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0.0-alt1
- 4.6

* Mon Mar 14 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0.0-alt1
- 4.5

* Mon Jan 11 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0.0-alt1
- 4.4

* Mon Nov 02 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 4.3

* Wed Sep 02 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 4.2

* Thu Jun 25 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 4.1

* Tue Apr 14 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 4.0

* Mon Feb 09 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.19

* Mon Dec 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.18

* Wed Oct 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.17

* Tue Jun 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.15

* Mon Apr 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.14

* Wed Jan 22 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.13

* Tue Nov 05 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.12

* Wed Sep 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.11

* Tue Jul  2 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.10

* Mon Apr 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.9

* Tue Feb 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.8

* Tue Dec 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.7 release

* Tue Dec 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt1
- 3.7-rc8

* Tue Nov 27 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1
- 3.7-rc7

* Mon Oct 01 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.6 release

* Sat Sep 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1
- 3.6-rc7

* Fri Aug 17 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2.0-alt1
- 3.6-rc2

* Wed Aug 01 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt2
- right version in gear/rules

* Wed Jul 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.0-alt1
- 3.5 release

* Sun Jul 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1
- 3.5-rc7

* Thu Jul 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.0-alt1
- 3.5-rc6

* Sun Jul 01 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5.0-alt1
- 3.5-rc5

* Mon Jun 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.0-alt1
- 3.5-rc4

* Fri Jun 22 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.0-alt1
- 3.5-rc3

* Thu Dec 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.32

* Thu Sep 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.31

* Mon Sep 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt1
- 2.6.31-rc9

* Wed Jun 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.30

* Wed Jun 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.0-alt1
- 2.6.30-rc8

* Mon May 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.0-alt1
- 2.6.30-rc7

* Sat May 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 2.6.30-rc6

* Tue Mar 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.29

* Fri Mar 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.0-alt1
- 2.6.29-rc8

* Wed Mar 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.0-alt1
- 2.6.29-rc7

* Wed Feb 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 2.6.29-rc6

* Thu Dec 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.28

* Fri Oct 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.27

* Mon Jul 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 2.6.26

* Sun Apr 20 2008 Michail Yakushin <silicium@altlinux.ru> 1.0.0-alt1
- 2.6.25

* Fri Jan 25 2008 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.24

* Sun Oct 29 2006 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.18

* Sun Jun 18 2006 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.17

* Sun Apr 23 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt2
- Specfile cleanup.

* Mon Mar 20 2006 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.16

* Fri Oct 28 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.14

* Sat Jun 18 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.12
- Removed kernel-doc package (documentation generation is performed when
  building kernel-image-%%flavour packages).

* Thu Mar 03 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.11

* Mon Dec 27 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.0-alt1
- 2.6.10

* Wed Oct 20 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- 2.6.9
