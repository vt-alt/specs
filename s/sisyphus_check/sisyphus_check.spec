Name: sisyphus_check
Version: 0.8.52
Release: alt1

Summary: package checker for Sisyphus
License: GPLv2+
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

Requires: file, getopt, mktemp >= 1:1.3.1, rpm
Conflicts: sisyphus < 0.7.2

%description
This package contains sisyphus_check utility.

%prep
%setup

%install
install -pD -m644 fhs %buildroot%_sysconfdir/%name/fhs
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m644 sisyphus-check-functions \
	%buildroot%_bindir/sisyphus-check-functions

mkdir -p -- %buildroot%_sysconfdir/
cp -a -- sisyphus_check.d %buildroot%_sysconfdir/%name/check.d

%files
%config %_sysconfdir/%name
%_bindir/*

%changelog
* Wed Sep 25 2019 Dmitry V. Levin <ldv@altlinux.org> 0.8.52-alt1
- 130-check-fhs: allow hasher-provides-dev-kvm package to provide /dev/kvm.

* Thu Jun 27 2019 Dmitry V. Levin <ldv@altlinux.org> 0.8.51-alt1
- 130-check-fhs (check_fhs): disallow invalid path names
  starting with /usr/lib/tmpfiles.d/.

* Fri Apr 26 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.8.50-alt1
- 210-check-kernel: more info in a message
  (about multiple kernel-image Requires).

* Tue Apr 16 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.8.49-alt1
- 210-check-kernel:
  + fixed splitting of $kernel_require in the presence of disttag;
  + for standalone kmodules, accept Requires on kernel-image with disttags;
  + added warning to advise to use %%requires_kimage.

* Fri Apr 05 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.48-alt1
- 130-check-fhs: allow /run as defined in FHS-3.0

* Tue Jan 15 2019 Dmitry V. Levin <ldv@altlinux.org> 0.8.47-alt1
- 090-check-nvr: check disttag.
- 210-check-kernel (check_kmodule): strip disttag from kernel_release.

* Mon Dec 31 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.46-alt1
- 090-check-nvr: make version and release check more strict

* Fri May 18 2018 Ivan Zakharyaschev <imz@altlinux.org> 0.8.45-alt1
- check-fhs: allow libdirs compatible with the processor arch
  determined by rpm_arch. For e2k*, the peculiar lib32 has been
  added to the list of allowed libdirs.
- check-fhs: added an exception for lcc (the proprietary compiler
  for e2k provided as binary blobs).

* Tue Oct 31 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.8.44-alt1
- 220-check-python: prohibit modules with version files containing
  unknown version. (Thanks Aleksei Nikiforov darktemplar@)

* Wed Oct 25 2017 Dmitry V. Levin <ldv@altlinux.org> 0.8.43-alt1
- 130-check-fhs (check_fhs): disallow invalid path names (closes: #34024).

* Mon Feb 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.42-alt1
- check-python: minor version is not allowed in
  /usr/lib(64)?/python3[.][0-9]/site-packages/.
- check-python: adapted to the possibility of having modules in
  /usr/lib(64)?/python[23]/ without the minor version.

* Fri Feb 26 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.41-alt1
- 220-check-python: disallow having files in tools/ and lib-dynload/
  subdirs of %%python_libdir (for all except pythonN.src.rpm's
  subpkgs).

* Fri Nov 13 2015 Dmitry V. Levin <ldv@altlinux.org> 0.8.40-alt1
- 090-check-nvr (check_nvr):
  + allowed single symbol package names (closes: #28834, #31481).

* Mon Jun 03 2013 Dmitry V. Levin <ldv@altlinux.org> 0.8.39-alt1
- 210-check-kernel (kernel_version_code):
  + changed algorithm for 4-component kernel versions support.

* Fri May 31 2013 Dmitry V. Levin <ldv@altlinux.org> 0.8.38-alt1
- 100-check-deps: allowed kernel deps in packages built from kernel-image-*.
- 210-check-kernel:
  + added support for 4-component kernel versions;
  + relaxed kernel module version check (by led@; closes: #28908).

* Thu Jan 24 2013 Dmitry V. Levin <ldv@altlinux.org> 0.8.37-alt1
- 211-check-firmware: added exception for firmware-tools and
  firmware-tools-* (closes: #28284).
- fhs: added exception for msp430* packages (closes: #28286).

* Wed Dec 05 2012 Dmitry V. Levin <ldv@altlinux.org> 0.8.36-alt1
- 090-check-nvr: added a check for package name validity.

* Wed Sep 12 2012 Dmitry V. Levin <ldv@altlinux.org> 0.8.35-alt1
- 211-check-firmware: removed "noarch" check (closes: #27709).

* Fri Apr 13 2012 Dmitry V. Levin <ldv@altlinux.org> 0.8.34-alt1
- 220-check-python: implemented additional restrictions on
  requirements between python2 and python3 modules (closes: #27194).

* Tue Apr 10 2012 Dmitry V. Levin <ldv@altlinux.org> 0.8.33-alt1
- 220-check-python:
  + reverted the change made in 0.8.32-alt1;
  + disallowed python3 requirements in python2 modules and vice versa (closes: #27194).

* Thu Apr 05 2012 Dmitry V. Levin <ldv@altlinux.org> 0.8.32-alt1
- 220-check-python: ignore "i586-" arepo prefix in package names.

* Wed Feb 08 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.31-alt1
- 220-check-python: add special python3-module-* packages handling.

* Mon Jan 16 2012 Alexey Gladkov <legion@altlinux.ru> 0.8.30-alt1
- 240-check-browser: allow /usr/lib*/mozilla/* (closes: #26808).

* Tue Dec 20 2011 Dmitry V. Levin <ldv@altlinux.org> 0.8.29-alt1
- 220-check-python: allow packaging of *.py* files in the
  arch-independent site-packages directory on x86-64 (closes: #26728).

* Thu Dec 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.28-alt1
- 220-check-python: add exception for python3 source package as well.

* Wed Sep 21 2011 Dmitry V. Levin <ldv@altlinux.org> 0.8.27-alt1
- 140-check-perms: added check that accessible directories have
  appropriate executable bits set.

* Thu Sep 15 2011 Dmitry V. Levin <ldv@altlinux.org> 0.8.26-alt1
- Removed /usr/X11R6 (see ALT#11699).

* Wed May 04 2011 Dmitry V. Levin <ldv@altlinux.org> 0.8.25-alt1
- 210-check-kernel (check_kmodule): strip epoch number from kernel_version.

* Tue Apr 26 2011 Dmitry V. Levin <ldv@altlinux.org> 0.8.24-alt1
- fhs: changed exception for mingw64-* packages (closes: #25453).

* Sun Apr 17 2011 Dmitry V. Levin <ldv@altlinux.org> 0.8.23-alt1
- fhs: added exception for mingw64-* packages (closes: #25453).

* Tue Apr 05 2011 Dmitry V. Levin <ldv@altlinux.org> 0.8.22-alt1
- fhs: renamed SysVinit to sysvinit.

* Mon Mar 28 2011 Dmitry V. Levin <ldv@altlinux.org> 0.8.21-alt1
- 100-check-deps (bad_deps): Removed xorg-x11-*, added xorg-x11-devel.

* Wed Mar 23 2011 Alexey Tourbin <at@altlinux.ru> 0.8.20-alt1
- 100-check-deps (bad_deps): Added xorg-x11-* xorg-devel libmesa-devel.
- 210-check-kernel: Exempted kernel-*-debuginfo from this check.

* Fri Sep 24 2010 Dmitry V. Levin <ldv@altlinux.org> 0.8.19-alt1
- 100-check-deps: Added /lib64/udev, /lib64/udev/rules.d
  and '(GLIBC_PRIVATE)' to the list of forbidden requirements.

* Wed Mar 31 2010 Dmitry V. Levin <ldv@altlinux.org> 0.8.18-alt1
- 210-check-kernel: Enhanced error reporting.

* Sun Mar 21 2010 Dmitry V. Levin <ldv@altlinux.org> 0.8.17-alt1
- 220-check-python: Updated source rpm name check for base python
  packages (closes: #23199).

* Sun Nov 08 2009 Dmitry V. Levin <ldv@altlinux.org> 0.8.16-alt1
- 210-check-kernel: Fixed regression introduced by previous release.

* Fri Nov 06 2009 Dmitry V. Levin <ldv@altlinux.org> 0.8.15-alt1
- 100-check-deps:
  + Updated list of forbidden requirements.
  + Added check for forbidden prerequirements.

* Wed Oct 07 2009 Dmitry V. Levin <ldv@altlinux.org> 0.8.14-alt1
- 140-check-perms:
  + Introduced /etc/sudo.d/* permissions check
    (by Michael Shigorin; closes: #21864).
  + Improved error messages (by Michael Shigorin).
- 240-check-browser: New check for invalid browser paths.

* Thu Jul 23 2009 Dmitry V. Levin <ldv@altlinux.org> 0.8.13-alt1
- fhs: Added exception for mingw32-* packages (closes: #20845).
- 211-check-firmware: Marked udev package as exception.

* Wed Jul 15 2009 Alexey Tourbin <at@altlinux.ru> 0.8.12-alt1
- 230-check-bindir: New check for invalid PATH files (e.g. /usr/bin/*/*).

* Tue May 05 2009 Alexey Tourbin <at@altlinux.ru> 0.8.11-alt1
- 130-check-fhs: Check provided paths as well (suggested by Dmitry V. Levin
  after we discovered "Provides: /usr/config.h" in opencascade.spec).

* Fri Feb 20 2009 Dmitry V. Levin <ldv@altlinux.org> 0.8.10-alt1
- 220-check-python: New check for python policy compliance.

* Fri Feb 13 2009 Dmitry V. Levin <ldv@altlinux.org> 0.8.9-alt1
- 211-check-firmware: Marked kernel-image-* packages as exception.

* Fri Feb 13 2009 Dmitry V. Levin <ldv@altlinux.org> 0.8.8-alt1
- Merged 160-check-locales into 110-check-content (Alexey Gladkov).
- 211-check-firmware: New check for firmware policy compliance (Alexey Gladkov),
  see http://www.altlinux.org/FirmwarePolicy for details.

* Thu Feb 12 2009 Dmitry V. Levin <ldv@altlinux.org> 0.8.7-alt1
- sisyphus-check-functions (init_check):
  Updated packager_pattern to allow more spaces and disallow null elements.
- 190-check-dirlist:
  Fixed typo in error message (Slava Semushin; closes: #17001).

* Wed Oct 01 2008 Dmitry V. Levin <ldv@altlinux.org> 0.8.6-alt1
- 210-check-kernel: Special exception for kernel modules
  built within a kernel image (Alexey Gladkov).

* Fri Sep 26 2008 Dmitry V. Levin <ldv@altlinux.org> 0.8.5-alt1
- 210-check-kernel: New check for kernel policy compliance (Alexey Gladkov).
- 010-check-gpg, 060-check-summary, 070-check-description:
  Hide SIGPIPE (Alexey Gladkov).
- 100-check-deps: Userspace packages should not depend
  from kernelspace (Alexey Gladkov).

* Tue Sep 16 2008 Alexey Tourbin <at@altlinux.ru> 0.8.4-alt1
- check-noarch: New check for soname dependencies and lib64 paths in noarch packages.

* Fri Aug 29 2008 Dmitry V. Levin <ldv@altlinux.org> 0.8.3-alt1
- sisyphus_check: Added -[-no]-check=ALL special value (Alexey Gladkov; closes: #16662).

* Sat Aug 09 2008 Alexey Tourbin <at@altlinux.ru> 0.8.2-alt1
- check-dirlist: Prune stderr when *-files.req.list are missing (#16631).

* Tue Jun 24 2008 Alexey Tourbin <at@altlinux.ru> 0.8.1-alt1
- check-dirlist: New check for directory ownership with respect
  to /usr/lib/rpm/*-files.req.list files.

* Sun May 11 2008 Dmitry V. Levin <ldv@altlinux.org> 0.8.0-alt1
- Factored out tests to %_sysconfdir/%name/check.d directory (legion).
- Added options descriptions (legion).
- check-deps: Added more forbidden patterns (at).
- check-subdirs: New check for unpackaged subdirectories (at).
- check-pkgconfig: New check for invalid pkg-config pathnames (at).
- Optimized rpmquery invocations (at).
- Enhanced error summaries.
- Fixed signal handler.

* Thu Mar 20 2008 Dmitry V. Levin <ldv@altlinux.org> 0.7.22-alt1
- fhs: Added dev-minimal (mike, #14889).

* Fri Feb 08 2008 Dmitry V. Levin <ldv@altlinux.org> 0.7.21-alt1
- check_nvr: Disallowed ipl* and alt0 release numbers.
- check_perms: Added check for world writable directories.
- Disabled gpg check exception for kernel@packages.altlinux.

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 0.7.20-alt1
- fhs: Added webserver-common (#11784).

* Sat Aug 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.19-alt1
- fhs: /var/avahi, /var/resolv/var/avahi

* Mon Jan 22 2007 Dmitry V. Levin <ldv@altlinux.org> 0.7.18-alt1
- check_files:
  Check file type manually, do not rely on file(1) utility.
  Perform quick sanity check prior to other checks.

* Mon Apr 10 2006 Dmitry V. Levin <ldv@altlinux.org> 0.7.17-alt1
- check_fhs: Added /var/games (FHS-2.3, 5.7.1).

* Thu Dec 22 2005 Dmitry V. Levin <ldv@altlinux.org> 0.7.16-alt1
- check_printable: Added check for changelogs (#7626).
- Moved libtool la-files check to separate check_libtool() function
  and disabled new "libtool" check by default.
- Split Usage() into show_help() and show_usage().
- Introduced --check* options.

* Sun Oct 02 2005 Dmitry V. Levin <ldv@altlinux.org> 0.7.15-alt1
- check_locales: Fix bugs introduced in previous release.

* Wed Sep 28 2005 Dmitry V. Levin <ldv@altlinux.org> 0.7.14-alt1
- check_locales: New check (legion).

* Mon May 16 2005 Dmitry V. Levin <ldv@altlinux.org> 0.7.13-alt1
- fhs: added arm-palmos-* and prc-tools-common (raorn).

* Thu May 12 2005 Dmitry V. Levin <ldv@altlinux.org> 0.7.12-alt1
- check_nvr: Add check for filename.
- check_content: Adjust .la-files check for 64bit platforms.
- New options:
  --files: Consider arguments as file names (closes #5652).
  --directories: Consider arguments as directory names;
  this is default mode, for compatibility with previous releases.

* Wed Dec 29 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.11-alt1
- check_fhs: allow /usr/libexec/.
- check_changelog, check_buildtime: enhanced wording.

* Fri Nov 19 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.10-alt1
- check_content: added few checks for intersections
  with known packages.
- fhs: added rule for udev.

* Thu Nov 11 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.9-alt2
- Check for file type before rpmquery.
- New option: --recursive.
- Updated package dependencies.

* Fri Oct 22 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.8-alt1
- Implemented support for check_gpgname() exceptions (legion).

* Wed Sep 01 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.7-alt1
- check_content, check_fhs: enhanced error diagnostics.

* Tue Aug 31 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt1
- check_gpgname: made the check case-insensitive.
- check_fhs: added /lib64 and /usr/lib64 to builtin list.

* Fri Aug 13 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.5-alt1
- New option: --trust-gpg-names.

* Wed Aug 11 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.4.1-alt1
- check_gpgname: enhanced error diagnostics.

* Tue Aug 10 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.4-alt1
- check_gpgname: new check.

* Wed Jul 07 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.3-alt1
- check_fhs,check_intersects: do not use command substitutions.
- Enhanced error diagnostics a bit.

* Thu Jun 24 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.2-alt1
- Moved sisyphus_check to separate subpackage.

* Mon Jun 07 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.1-alt1
- functions: fixed quiet mode.
- sisyphus_check: added new option: verbose.
- sisyphus_add_new: enabled quiet mode by default.

* Sat Jun 05 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.0-alt1
- functions: optimized, thanks to legion@.
- functions/check_buildtime: new check.
- functions/check: use it.
- sisyphus_check: added new options:
  quiet, fast-check, show-bad-files.

* Thu May 13 2004 Dmitry V. Levin <ldv@altlinux.org> 0.6.0-alt1
- sisyphus_relink: added support for new style lists.
- functions/{check_summary,check_description}: new checks.
- functions/check: use them.

* Thu Feb 19 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.6-alt1
- functions/check_changelog: added check for empty changelog text.

* Mon Feb 09 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.5-alt1
- functions/check_deps:
  + added initscripts to the list of forbidden dependencies.
- functions/check_nvr:
  + new check (for invalid name-version-release).
- functions/check:
  + use it.

* Wed Nov 26 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.4-alt1
- functions/check_content: new check (forbidden .la files).
- config:
  + define VERSION;
  + added --no-oldhashfile to GENBASEDIR_OPT_ARGS.
- sisyphus_genhash: pass architecture and version to genbasedir.

* Sun Nov 02 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.3-alt1
- sisyphus_check:
  + new option: --no-check=LIST;
  + better error diagnostics.

* Tue Oct 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.2-alt1
- sisyphus/fhs: new file.
- functions: use it.
- sisyphus_check,sisyphus_add_new: turn into bash script.
- functions/check_gpg: ignore default keyring.
- functions/check*: better error checking.

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- functions/check_changelog: added check for packager format.
- functions,sisyphus_check: added support to skip some checks.
- functions/check*: better error checking.

* Tue Sep 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.10-alt1
- functions/check_deps: added check for invalid dependencies.

* Thu Sep 18 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.9-alt1
- functions/check_printable: new check.
- functions/check: use it (#932).
- functions/upload_{src,bin}: remove unused functions.
- functions/check*: better error checking.

* Tue Sep 09 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.8-alt1
- functions/check_buildhost: new check.
- functions/check: use it.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.7-alt1
- sisyphus_gen_contents: new script.
- functions/check_fhs: fixed possible false alarms on empty list.
- functions/check_deps: added to forbidden requires:
  fileutils, sh-utils, textutils.

* Thu Jun 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.6-alt1.1
- sync

* Wed May 14 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.6-alt1
- sisyphus_check: check deps.

* Tue Apr 29 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.5-alt1
- sisyphus_check: check permisions in source archive.

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.4-alt1
- Updated.

* Wed Feb 19 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.3-alt1
- sync. new checks (FHS)

* Tue Dec 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt1
- sync. new relink algo by ldv. unset LC_*

* Mon Oct 21 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt5
- sync

* Fri Sep 27 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt4
- sync

* Tue Sep 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt3
- sync with latest changes:
- new utils:
	sisyphus_relink
	sisyphus_add_new

* Tue Aug 13 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt2
- rebuild to fix deps

* Mon Aug 12 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt1
- sync last changes
- added changelog checking

* Thu Aug 08 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt1
- sync last changes
- added symlink incoming_cleanup to sisyphus_cleanup_incoming
- added automatic package group check, suid/sgid check
- added sisyphus_check utility
- check() moved to functions
- /etc/sisyphus/functions no config(noreplace) now

* Thu Jun 20 2002 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- More code cleanup.

* Thu Jun 20 2002 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Specfile and code cleanup.

* Mon Jun 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2-alt1
- added master repository
- added cleanup dups script

* Wed Jun 05 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt1
- Inital release for Sisyphus
