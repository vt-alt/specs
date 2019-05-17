Name: kernel-build-tools
Version: 0.109
Release: alt1

Summary: Utilities to build kernel packages for ALT Linux
License: GPL
Group: Development/Kernel
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Source: %name-%version.tar

Requires: rpm-build-kernel = %version-%release

# due to RPM macro expansion support
Requires: gear >= 1.3.1

# Automatically added by buildreq on Mon Apr 14 2008
BuildRequires: asciidoc help2man python-modules-encodings

%package -n rpm-build-kernel
Summary: RPM macros to build kernel packages
Group: Development/Kernel
Conflicts: rpm-build < 4.0.4-alt1

%ifnarch %ix86
Provides: kernel-headers-modules-std-pae
%endif
%ifnarch %ix86 x86_64
Provides: kernel-headers-modules-std-def
Provides: kernel-headers-modules-un-def
Provides: kernel-headers-modules-ovz-el
Provides: kernel-headers-modules-ovz-el7
%endif
%ifnarch aarch64
Provides: kernel-headers-modules-mp
%endif
%ifnarch %e2k
Provides: kernel-headers-modules-elbrus-def
%endif
%ifnarch e2k
Provides: kernel-headers-modules-elbrus-4c
%endif
%ifnarch e2kv4
Provides: kernel-headers-modules-elbrus-1cp
Provides: kernel-headers-modules-elbrus-8c
%endif

%description
Utilities to facilitate creation of kernel and additional module packages
according to ALT Linux kernel packaging conventions.

%description -n rpm-build-kernel
RPM macros used to build kernel packages according to ALT Linux
kernel packaging conventions.

%prep
%setup

%build
%make_build
asciidoc README.ru.koi8

%install
%makeinstall_std
install -Dpm644 kernel-macros \
	%buildroot%_rpmmacrosdir/kernel
install -Dpm0755 query-kEVR.sh \
	-t %buildroot%_rpmlibdir/

%files
%_bindir/*
%_mandir/man?/*
%doc README* config.sh.sample kernel-policy.txt kernel-spec-example.txt

%files -n rpm-build-kernel
%_rpmmacrosdir/kernel
%_rpmlibdir/query-kEVR.sh

%changelog
* Fri May 17 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.109-alt1
- Made the test in the packages produced by %%update_kernel_modules_checkinstall
  not ignore the exit status of update-kernel.

* Tue May 07 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.108-alt1
- kernel-macros: added powerpc support to %%base_arch macro.

* Thu Apr 04 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.107-alt1
- kernel-macros: made %%setup_kernel_module automatically add
  the usual {,Build}Requires for kernel-modules-*.
- kernel-macros: added for possible use in modules:
  + %%kimage & %%requires_kimage;
  + %%update_kernel_modules_checkinstall
    (to produce a specific kind of checkinstall subpkg);
  + %%setup_kernel_module_from_globals (split from %%setup_kernel_module) for
    those who want to set %%kversion and %%krelease manually, without rpmquery).

* Wed Jul 04 2018 Michael Shigorin <mike@altlinux.org> 0.106-alt1
- added %%e2k support

* Sat Jun 09 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.105-alt1
- km-create-tag: added --force and --arches options.
- kernel-macros:
  + added mips and riscv support to %%base_arch macro;
  + dropped buggy karch macro.
- rpm-build-kernel: added fake provides for existing kernel flavours.

* Tue Sep 29 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.104-alt1
- kernel-macros: added new arch translation aarch64 -> arm64.

* Tue Jul 16 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.103.1-alt1
- fix *_kernel_headers macros.

* Thu Jun 20 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.103-alt1
- kernel-macros:
  + deprecated %%post_kernel_headers and %%postun_kernel_headers.

* Mon Jun 03 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.102-alt2
- 4-component kernel versions in kcode calculation changed

* Fri May 31 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.102-alt1
- added support for 4-component kernel versions in kcode calculation

* Thu Jan 24 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.101-alt1
- Added km-create-tag script

* Fri Jan 18 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.100-alt4
- %%base_arch macro extended to arm

* Thu Dec 20 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.100-alt3
- Fixed last change.

* Thu Dec 20 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.100-alt2
- Added workaround for std-pae.

* Tue Dec 11 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.100-alt1
- Added %%setup_kernel_module.

* Fri Dec 07 2012 Dmitry V. Levin <ldv@altlinux.org> 0.99.5-alt1
- kernel-macros:
  deprecated %%post_kernel_modules and %%postun_kernel_modules.

* Fri Nov 02 2012 Dmitry V. Levin <ldv@altlinux.org> 0.99.4-alt1
- Relocated kernel macros to %_rpmmacrosdir.
- kernel-macros:
  + removed %%kgcc and %%kgcc_package;
  + made %%post_kernel_image and %%preun_kernel_image obsolete.

* Mon Sep 19 2011 Anton Protopopov <aspsk@altlinux.org> 0.99.3-alt1
- Add -d option (the same as in buildmodules)

* Sun Aug 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.99.2-alt2
- Fetching ftom /gears/k fixed.

* Fri Aug 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.99.2-alt1
- New option --pull for pull from gears/k/module_name

* Wed Jun 24 2009 Anton Protopopov <aspsk@altlinux.org> 0.99.1-alt1
- Run hasher by default in buildmodules
- Add new script for updating modules: updatemodules
- Save tag names into $TOP/out/taglist when --tag option is used
- Use - instead of / when signing modules
- Try to get a value of def_repo from hasher config
- Try to set hsh_workdir from hasher config first
- Fix hasher option parsing

* Thu Mar 26 2009 Anton Protopopov <aspsk@altlinux.org> 0.99.0-alt2
- integrate setarch
- Get right modules.build
- Fix buildmodules to work with new templates

* Tue Apr 22 2008 Sergey Vlasov <vsu@altlinux.ru> 0.99.0-alt1
- Add new scripts to the kernel-build-tools package:
  + buildkernel, buildmodules - scripts for build kernel and module packages
    from git repositories;
  + merge-all-branches - script for easier merging of multiple fix and feature
    branches into the release branch of a kernel package.
- Add documentation for new scripts (README.ru.koi8, README.ru.html) and a
  sample config file.
- Remove obsolete update_module_specs script.

* Sun Feb 03 2008 Sergey Vlasov <vsu@altlinux.ru> 0.11-alt1
- kernel-macros:
  + %%base_arch: Fix problem with athlon and athlon_xp architectures due to
    broken regexp (#14300).

* Wed Nov 07 2007 Sergey Vlasov <vsu@altlinux.ru> 0.10-alt1
- kernel-macros:
  %%base_arch: Add pentium2, pentium3, athlon_xp architectures.
- Split package into separate parts:
  + rpm-build-kernel - files actually required for building kernel-related
    packages (this package should replace kernel-build-tools in BuildRequires);
  + kernel-build-tools - scripts and documentation used by kernel package
    maintainers (should not be used in BuildRequires anymore).
- Updated kernel-policy and spec example for new package split.
- Fixed summary and description (#2730).

* Mon May 08 2006 Sergey Vlasov <vsu@altlinux.ru> 0.9-alt1
- kernel-macros:
  + %%get_patch_list: add package versions to the returned list (needed to get
    correct BuildRequires for kernel packages);
  + %%get_patch_list, %%format_patch_list: pass current %%_dbpath to rpmquery
    to get correct results when using build scripts from kernel CVS.

* Sat Dec 03 2005 Sergey Vlasov <vsu@altlinux.ru> 0.8-alt2
- kernel-macros: fix by Dmitry V. Levin <ldv@altlinux>:
  + %%_src_list: quote %% to avoid unneeded macro expansion

* Thu Jul 14 2005 Anton D. Kachalov <mouse@altlinux.org> 0.8-alt1
- kernel-macros: added macros for per-arch configuration:
  + %%set_kernel_arches
  + %%get_kernel_config

* Sat Jun 11 2005 Sergey Vlasov <vsu@altlinux.ru> 0.7-alt2
- kernel-macros: fix %%base_arch to support pentium4 and k6 targets (#7055).

* Tue Aug 03 2004 Sergey Vlasov <vsu@altlinux.ru> 0.7-alt1
- kernel-macros: added macros for installation scripts:
  + %%post_kernel_image
  + %%preun_kernel_image
  + %%post_kernel_headers
  + %%preun_kernel_headers
  + %%post_kernel_modules
  + %%postun_kernel_modules
- updated kernel-policy:
  + added description for new macros
- updated kernel spec example:
  + use new macros in scripts

* Mon Feb 02 2004 Sergey Vlasov <vsu@altlinux.ru> 0.6-alt6
- kernel-macros:
  - added not_PATCHSET support
- updated kernel-policy
- updated kernel spec example and separated it from policy text

* Sun Jan 18 2004 Sergey Vlasov <vsu@altlinux.ru> 0.6-alt5
- kernel-macros:
  - fixed apply_recursive fix
  - allow URLs in %%source
- updated kernel-policy

* Thu Jan 15 2004 Ed V. Bartosh <ed@altlinux.org> 0.6-alt4
- apply_recursive fix: check for return code in recursive calls

* Thu Dec 18 2003 Sergey Vlasov <vsu@altlinux.ru> 0.6-alt3
- kernel-macros:
  - enhanced %%source to take an optional subdirectory for patch file
    installation
  - dropped %%source_kver (now this is handled by %%source)

* Wed Dec 17 2003 Sergey Vlasov <vsu@altlinux.ru> 0.6-alt2
- kernel-macros:
  - %%apply_patches: cleanup; fixed bugs in recursive patch application; allow
    00_ prefixes for all special directories
  - %%install_patches, %%source: reworked kernel version specific patch
    installation

* Fri Dec  5 2003 Ed V. Bartosh <ed@altlinux.ru> 0.6-alt1
- kernel-policy: Sergey Vlasov added to the kernel committee
- kernel-macros: added ability to apply patches only to the specified kernel version

* Tue Nov 11 2003 Ed V. Bartosh <ed@altlinux.ru> 0.5-alt5
- fix: set right permissions to upgrade_module_specs

* Thu Oct 30 2003 Ed V. Bartosh <ed@altlinux.ru> 0.5-alt4
- Change packager to ed@altlinux.ru

* Wed Sep  3 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.5-alt3
- upgrade_module_spec: fixed bug with non-only-digit release increment
- upgrade_module_spec: save spec formatting during replace

* Thu Aug  7 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.5-alt2
- macro 'format_patch_list' corrected

* Tue Aug  5 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.5-alt1
- apply_patches macro: improve support of applying dependent patches
- upgrade_module_spec improved
- kgcc_package added to the kernel-macros

* Thu Jul 31 2003 Peter Novodvorsky <nidd@altlinux.com> 0.4-alt1
- added upgrade_module_specs script.

* Fri Jul  4 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.3-alt4
- spec typos fixed

* Tue Jul  1 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.3-alt3
- policy naming rules minor changes
- %%source and %%install_patches macroses added

* Fri Jun  6 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.3-alt2
- Sinchronized with Peter's work, added kernel-policy

* Mon May 26 2003 Peter Novodvorsky <nidd@altlinux.com> 0.3-alt1
- new version of kernel-macros from Ed.
- 1.0 version of kernel-policy.

* Wed Apr 30 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.1-alt5
- %%copy_sources macro added

* Tue Apr 22 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.1-alt4
- stop applying patches when  patch or apply script return error

* Tue Apr 22 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.1-alt3
- %%kernel_src and %%kernel_srcdir defines added

* Sat Apr 19 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.1-alt2
- %%apply_patches: add ability to don't apply patch for specific kernel version
- %%apply_patches: add ability to use 'NN_' prefix for directory patches 

* Tue Apr 15 2003 Ed V. Bartosh <ed@sam-solutions.net> 0.1-alt1
- Initial release
