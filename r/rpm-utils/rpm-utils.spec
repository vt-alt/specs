Name: rpm-utils
Version: 0.10.3
Release: alt1

Summary: Utilities every rpm packager must have
License: GPLv2+
Group: Development/Other

Source: %name-%version.tar

Requires: getopt, time
Requires: rpm-build > 0:4.0.4-alt96.8, mktemp >= 1:1.3.1
# due to strace --seccomp-bpf
Requires: strace >= 5.3

# due to rpmEVRDTCompare() in rpmrdups:
BuildPreReq: librpm-devel >= 4.13.0.1-alt9

# Automatically added by buildreq on Wed Sep 25 2019
BuildRequires: gcc-c++ librpm-devel

%description
This package contains following utilities:
+ filereq - generates list of file requires while running the program;
+ packageof - generates list of packages owning specified files;
+ packagereq - generates list of package requires while running the program;
+ buildreq - generates and adds/updates BuildRequires tag in specfiles;
+ rpmdups,rpmrdups - generates list of duplicated packages;
+ paste_changelog - pastes a whole ready piece to the top of a changelog;
+ stamp_spec - generates timestamp for rpm specfile changelog entry;
+ add_changelog - generates and adds changelog entry to rpm specfile;
+ compare_packages - generates lists of package sets and compares them;
+ cleanup_spec - attempts to cleanup rpm specfile;
+ rebuild_package - rebuilds source package keeping packager info unchanged;
+ rebuild_packages - rebuilds source packages using rebuild_package.

%prep
%setup

%build
%def_enable Werror
%make_build

%install
%makeinstall_std

%check
rpmquery -a --qf='%%{name}\n' |
	%buildroot%_datadir/buildreqs/optimize_package_list > out
grep -qs 'rpm-build' out
grep -qs 'librpm-devel' out
grep -qs 'gcc.*-c++' out

rm -f FAIL
rpmquery -a --qf '%%{name}\n' |while read n; do
	echo "$n" |
		%buildroot%_datadir/buildreqs/optimize_package_list > out
	[ "$n" = "$(cat out)" ] ||
		echo "$n -> $(cat out)" >> FAIL
done
if [ -s FAIL ]; then
	echo FAILED:
	cat FAIL
	exit 1
fi >&2

%files
%dir %_sysconfdir/buildreqs
%dir %_sysconfdir/buildreqs/*
%dir %_sysconfdir/buildreqs/files/*.d
%dir %_sysconfdir/buildreqs/packages/*.d
%config %_sysconfdir/buildreqs/files/*/*
%config %_sysconfdir/buildreqs/packages/essential*
%_bindir/*
%_datadir/buildreqs

%changelog
* Wed Sep 25 2019 Dmitry V. Levin <ldv@altlinux.org> 0.10.3-alt1
- strace_files: speedup by enabling latest strace features.

* Thu Jun 20 2019 Dmitry V. Levin <ldv@altlinux.org> 0.10.2-alt1
- filter_spec: fixed regular expressions for modern gawk.

* Wed Jun 19 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt1
- rpmrdups: honor disttag, buildtime.

* Wed Aug 17 2016 Alexey Gladkov <legion@altlinux.ru> 0.10-alt1
- port to rpm-4.13.

* Mon May 09 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.21-alt1
- paste_changelog: a trivial ed wrapper extracted from add_changelog.
  (It can be useful in combination with, e.g., gear-changelog.)

* Wed Mar 23 2016 Dmitry V. Levin <ldv@altlinux.org> 0.9.20-alt1
- filereq: add faccessat, lstat/lstat64, and fstatat64/newfstatat
  to the list of weak syscalls.

* Tue Mar 22 2016 Dmitry V. Levin <ldv@altlinux.org> 0.9.19-alt1
- filereq: take openat, execveat, faccessat, lstat/lstat64, and
  fstatat64/newfstatat syscalls into account.

* Fri Jan 17 2014 Dmitry V. Levin <ldv@altlinux.org> 0.9.18-alt1
- optimize_package_list: fixed misoptimization (closes: #26320).

* Fri Aug 24 2012 Dmitry V. Levin <ldv@altlinux.org> 0.9.17-alt1
- Fixed build with fresh glibc.

* Mon May 21 2012 Dmitry V. Levin <ldv@altlinux.org> 0.9.16-alt1
- Fixed build with ld --no-copy-dt-needed-entries.

* Wed Aug 10 2011 Dmitry V. Levin <ldv@altlinux.org> 0.9.15-alt1
- optimize_package_list: robustified by ignoring file names containing spaces.

* Tue Aug 09 2011 Dmitry V. Levin <ldv@altlinux.org> 0.9.14-alt1
- optimize_package_list: fixed optimization by taking into account
  all indirect requirements and their providers.

* Fri Apr 01 2011 Dmitry V. Levin <ldv@altlinux.org> 0.9.13-alt1
- cleanup_spec: strip -q from %%setup (closes: #25011).
- add_changelog: pass --args to all "rpm -q --qf" invocations (closes: #22346).
- buildreq: added --no-pruned option, enabled --pruned y default.
- stamp_spec, add_changelog, packagereq, buildreq: fixed quoting
  using shell-quote.

* Tue Apr 06 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.12-alt1
- Added support for fixating pruned BRs (by Michael Shigorin; closes: #22709).
- Fixed signal handling in shell scripts.
- Removed obsolete strace options.
- Moved test to %%check section.

* Tue Oct 28 2008 Dmitry V. Levin <ldv@altlinux.org> 0.9.11-alt1
- Moved rpmevrcmp/rpmvercmp to rpm package (closes: #13627).
- Fixed build with fresh g++.

* Fri Aug 29 2008 Dmitry V. Levin <ldv@altlinux.org> 0.9.10-alt1
- compare_packages: Apply sed(1) pattern before sort(1).
- add_changelog --help: Fixed expansion of $STAMPER (Mikhail Gusarov; closes: #16800).

* Wed Mar 26 2008 Alexey Tourbin <at@altlinux.ru> 0.9.9-alt1
- improved optimize_package_list:
  + check for ambiguous virtual dependencies
  + break simple RV-loops (select the package with non-virtual dependency)
  + show the list of optimized out packages

* Fri Mar 21 2008 Alexey Tourbin <at@altlinux.ru> 0.9.8-alt1
- filereq: do not finally overwrite driven command's output
- optimize_package_list: join on filenames as well as provides
- compare_packages: fixed sort(1) old-style options (Dmitry V. Levin)

* Thu Dec 27 2007 Alexey Tourbin <at@altlinux.ru> 0.9.7-alt1
- added more /usr/share/fonts/*/fonts.* patterns to ignore list
- add_changelog: fixed typo in --help text (Dmitry V. Levin, #12584)

* Mon Aug 13 2007 Alexey Tourbin <at@altlinux.ru> 0.9.6-alt1
- filereq: implemented strong (open, execve) and weak (access, stat)
  file access logic; strong access via symbolic link now also implies
  the requirement of symlink target file
- strace post-processor: implemented canonicalization of filenames,
  which makes it impossible to circumvent files/ignore.d/* patterns
- packagereq: factored new program: /usr/share/buildreqs/optimize_package_list
- buildreq: implemented --trace-file=FILE and --trace-package=PKG options,
  which can help to explain unexpected build dependencies

* Fri Oct 27 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.5-alt1
- rpmrdups: New option "-" to read file names from standart input (ldv, legion).

* Sun Oct 15 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.4-alt1
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Mon Sep 11 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt1
- buildreq:
  --define: New option, for compatibility with rpmbuild (legion).

* Sun Sep 03 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.2-alt1
- packagereq:
  Replaced unfair deps optimizer with correct one,
  based on idea and code from Alexey Tourbin.
- ignore.d/0filesystem:
  Ignore /usr/share/fonts/*/fonts.cache*.

* Mon May 15 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.1-alt1
- Fixed build with gcc-4.1.0.

* Fri Mar 10 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.0-alt1
- packagereq: Implemented dependencies optimization.

* Tue Mar 07 2006 Dmitry V. Levin <ldv@altlinux.org> 0.8.4-alt1
- Fixed build with --as-needed.
- /etc/buildreqs/files/ignore.d/0filesystem:
  Ignore /etc/ld.so.conf.d/*.

* Tue Apr 19 2005 Dmitry V. Levin <ldv@altlinux.org> 0.8.3-alt1
- add_changelog,buildreq,compare_packages,lastchange_spec,
  packagereq,query_spec,stamp_spec: redirect --help output
  to stdout, and error diagnostics to stderr.
- add_changelog,buildreq,cleanup_spec,compare_packages,filereq,
  filter_strace,packagereq,rebuild_package,stamp_spec: use
  trap in more portable way.
- essential:
  + removed: net-tools;
  + added: hostinfo;
  + added libs:
    aalib,clanlib,dclib,fnlib,ghostscript-lib,glib,glib2,
    id3lib,imlib,imlib2,jamlib,libgiblib,libglibmm,
    plib,sendmail-libs,t1lib,xorg-x11-libs,zziplib.

* Thu Mar 17 2005 Dmitry V. Levin <ldv@altlinux.org> 0.8.2-alt1
- essential:
  + added: rpm-build-python, rpm-build-tcl.

* Thu May 06 2004 Dmitry V. Levin <ldv@altlinux.org> 0.8.1-alt1
- rpmrdups: fixed epoch handling.

* Tue May 04 2004 Dmitry V. Levin <ldv@altlinux.org> 0.8.0-alt1
- rpmevrcmp: new program.
- rpmdups, rpmrdups: rewritten in C++.

* Mon Mar 01 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt1
- rpmdups, rpmrdups: adopted for coreutils-5.2.

* Tue Dec 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.5-alt1
- essential:
  + added: gcc-[^-]+-common.
- packageof:
  + fixed syntax to comply with g++-3.3 requirements.

* Wed Dec 10 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.4-alt1
- compare_packages:
  + better support for packages with devices.
- essential:
  + removed: all lib* records;
  + added: lib[^-]+ record.

* Fri Sep 26 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.3-alt1
- buildreq:
  + implemented build stage change using -bi,
    (#3034, at);
  + changed --args behaviour, added --reset-args option.
- Updated build dependencies.

* Mon Sep 22 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.2-alt1
- essential:
  + readded: bash, libreadline.

* Mon Sep 22 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.1-alt1
- essential:
  + added: rpm-build-perl.
  + removed: bash, console-tools, fileutils, less, libreadline,
             mawk, perl, sh-utils, textutils.
- packagereq:
  + removed -r option.
- buildreq:
  + do not use "packagereq -r";
  + set TERM=dumb by default (#3016);
    use --term option to redefine.
- rebuild_packages:
  + changed subdir names.

* Fri Sep 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.0-alt1
- spp: new strace postprocessor, to fix race condition
  in filereq (#2888); requires strace >= 4.4-alt6.
- rpmvercmp: new program (#2882).
- essential: added libtcb.
- Build with -Werror.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.13-alt1
- Corrected error handling.
- essential:
  + added: gettext-runtime, glibc-kernheaders, libtool-common,
    nss_db, nss_ldap, nss_tcb.
  + removed: ncurses.

* Tue Apr 22 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.12-alt1
- essential:
  + added: service, startup.
  + removed: initscripts.

* Thu Apr 03 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.11-alt1
- buildreq: timestamp no longer depends on current locale (#0002445);
  this fix is required due to better i18n support in gawk-3.1.2.

* Mon Mar 10 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.10-alt1
- compare_packages: use subst instead of perl.
- essential: added added libdb4.[0-9] pattern.

* Mon Feb 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.9-alt1
- rpmdups, rpmrdups: patched to work with new coreutils.
- add_changelog: skip missing files.

* Tue Nov 05 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6.8-alt1
- Enhanced error handling.

* Wed Oct 30 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6.7-alt1
- packageof: ignore non-regular files.

* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6.6-alt1
- essential:
  + added: autoconf-common, automake-common.

* Wed Oct 23 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6.5-alt1
- essential:
  + added: gettext-tools
  + removed *2.96
- rebuild_package: fixed typo.

* Sat Oct 05 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6.4-alt1
- essential:
  + added rpm-build-topdir
  + s/glibc-core/glibc-core.*/

* Wed Sep 18 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6.3-alt1
- essential: added coreutils.
- buildreq: added --nodeps to default arguments for rpm.

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6.2-alt1
- essential:
  + added libpcre (required by grep);
  + updated glibc subpackages list.
- packageof: fixed gcc-3.2 build.

* Thu Aug 15 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6.1-alt1
- packageof: extended ignore.d support.

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6.0-alt1
- /etc/buildreqs/packages/ignore: removed.
- /etc/buildreqs/packages/ignore.d: added.
- buildreq, packagereq, packageof: added packages/ignore.d support.

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.2-alt1
- packagereq: changed SIGQUIT handling (#0001006).

* Mon Aug 05 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- packageof: fixed dereferencing symlinks bug (#0001174).

* Wed Jul 10 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.0-alt1
- added: packageof utility.
- removed: check_importance helper script.
- packagereq:
  + updated to use packageof (and significantly speed up
    dependencies calculation);
  + enhanced requires cleaning rule.
- filereq, filter_strace:
  + relocated sort from filter_strace to filereq,
    changed SIGQUIT atexit action (imz).
- 0filesystem: added /home.

* Thu Jul 04 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4.4-alt1
- essential:
  + added: terminfo, libtinfo;
  + removed: termcap, libtermcap.
- added: rpmrdups.

* Thu May 30 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4.3-alt1
- cleanup_spec: dont't replace %make with %make_build.
- stamp_spec: added new option: --format.
- add_changelog: check for version changes by default.
- add_changelog: added new option: --nocheck.

* Fri Mar 29 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.4.2-alt1
- essential:
  + added: libbeecrypt, libdb4;
  + removed: libdb3.

* Thu Mar 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.4.1-alt1
- packagereq: fixed substitute logic:
  do not forget to ignore essential substitution.
- add_changelog: fixed $RPMARG parse typo.
- rebuild_packages: redirect stdin to /dev/null.
- essential:
  + added: sh

* Wed Jan 30 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.4.0-alt1
- Added substitute.d support.

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.3.0-alt1
- filter_strace:
  + Added ignore.d support;
  + Added $verbose support.
- Added rebuild_packages utility.
- Updated requires list.

* Mon Dec 10 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.2.4-alt1
- files/ignore: added to ignore list: /etc/emacs/site-start.d/*.el (imz).

* Wed Dec 05 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.2.3-alt1
- compare_packages: shutup diff errors, do not requires less.
- essential:
  + added: libgcc, cpp2.96, gcc2.96, libstdc++2.96;
  + removed: libjpeg.

* Fri Nov 16 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.2.2-alt1
- Added SIGPIPE handling.

* Mon Nov 12 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.2.1-alt1
- rebuild_package: fixed typo.

* Fri Nov 09 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.2.0-alt1
- Enabled rpm4 support.

* Fri Oct 26 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.1.1-alt1
- cleanup_spec: fixed nasty bugs introduced in previous version.

* Mon Oct 22 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.1-alt1
- buildreq: fixed shell quoting pattern.
- Added new utilities: stamp_spec, add_changelog, compare_packages, cleanup_spec, rebuild_package.
- Renamed to rpm-utils.

* Wed Oct 17 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.9.9.1-alt1
- essential: take into account glibc split.
- filereq,packagereq,buildreq: use features of mktemp >= 1:1.3.1

* Wed Oct 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.9-alt1
- Make use of "mktemp -t" (requires mktemp >= 1.6).
- buildreq: quote packagereq and some of its arguments.
- buildreq: added define of __nprocs=1 to avoid strace bugs.
- filter_strace: ignore files from $TMPDIR, %%_builddir and %%_tmppath.

* Fri Sep 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.8-alt1
- packagereq: optimized by checking file existance before executing rpm query.
- buildreq: set default arguments list to "-bc --define '__buildreqs 1'".
- filter_strace: ignore files from $TMPDIR.
- essential: added getopt.

* Wed Aug 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.7-alt1
- Updated %_sysconfdir/%name/packages/essential config.

* Thu Jul 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.6-alt1
- Added files/ignore config for filter_strace helper script.
- Added check_importance helper script.
- Changed logic of checking package importance.
- Moved config files to %_sysconfdir/%name.

* Sun May 06 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.5-alt1
- Updates ignore and essential lists.

* Fri Apr 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.4-alt1
- Fixed and enhanced packagereq utility.
- Updated %_datadir/%name/essential list.

* Fri Jan 26 2001 Dmitry V. Levin <ldv@fandra.org> 0.9.3-ipl1
- Fixed typo in packagereq.

* Tue Jan 23 2001 Dmitry V. Levin <ldv@fandra.org> 0.9.2-ipl1
- Added %_bindir/rpmdups.
- Added %_datadir/%name/ignore support.
- Updated %_datadir/%name/essential list.
- Marked %_datadir/%name/{essential,ignore} as config files.

* Sun Dec 24 2000 Dmitry V. Levin <ldv@fandra.org> 0.9.1-ipl1
- Minor fixes.

* Mon Oct 16 2000 Dmitry V. Levin <ldv@fandra.org> 0.9-ipl1
- 0.9:
  + reduced size of temporary files to minimum (list of files);
  + filter_spec now inserts BuildRequires line in proper place,
    not in the first line as before;
  + added packages, required by rpm-build, to essential list.

* Sun Oct 15 2000 Dmitry V. Levin <ldv@fandra.org> 0.8-ipl1
- 0.8 (optimized strace output, usage typo fixes).
- BuildArchitectures: noarch.

* Mon Oct 09 2000 Dmitry V. Levin <ldv@fandra.org> 0.7-ipl1
- 0.7 (rewritten completely, now using strace).

* Mon Oct 09 2000 Dmitry V. Levin <ldv@fandra.org> 0.6-ipl1
- 0.6 (added essential packages).

* Mon Oct 02 2000 Dmitry V. Levin <ldv@fandra.org> 0.5-ipl1
- 0.5 (rewritten error reporting).

* Thu Sep 21 2000 Dmitry V. Levin <ldv@fandra.org> 0.3-ipl1
- 0.3 (minor fixes).

* Tue Sep 19 2000 Dmitry V. Levin <ldv@fandra.org> 0.2-ipl1
- Initial revision
