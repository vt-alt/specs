Name: procps
Version: 3.3.15
Release: alt4.git4c4d8b24640612

Summary: System and process monitoring utilities
License: GPLv2+, LGPLv2+
Group: Monitoring
URL: https://sourceforge.net/projects/procps-ng/

# git://git.altlinux.org/gears/p/procps.git
Source: %name-%version-%release.tar

# it is actually procps-ng
Provides: procps-ng = %version-%release

%ifarch x86_64
# hack around arepo, remove this as soon as possible
Provides: i586-procps = %version-%release
%endif

Requires: lib%name = %version-%release

# Due to kill(1) relocation to coreutils.
Requires: coreutils >= 0:5.2.1-alt2

BuildRequires: libncursesw-devel
BuildRequires: libsystemd-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: dejagnu}}

%define _unpackaged_files_terminate_build 1

%description
This package contains a set of system utilities which provide system
information.  procps includes: free, pgrep, pkill, pmap, ps, pwdx,
skill, slabtop, snice, sysctl, tload, top, uptime, vmstat, w, watch.

%package -n lib%name
Summary: %name shared library
License: LGPLv2+
Group: System/Libraries

%package -n lib%name-devel
Summary: Development files for building %name-aware applications
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name
This package contains lib%name runtime library.

%description -n lib%name-devel
This package contains development files for building %name-aware
applications.

%prep
%setup -n %name-%version-%release

# build scripts expect to find package version in this file
echo -n %version-%release > .tarball-version

%build
%add_optflags "-Werror"
./autogen.sh
%configure \
	--exec-prefix=/ \
	--sbindir=/sbin \
	--enable-watch8bit \
	--disable-static \
	--disable-kill \
	--enable-skill \
	--disable-nls \
	--disable-modern-top \
	--with-systemd \
	#
%make_build

%install
%makeinstall_std
rm -r %buildroot%_docdir/procps-ng

# move ps to /bin
mkdir -p %buildroot/bin
mv %buildroot%_bindir/ps %buildroot/bin/

# reduce redundancy
ln -snf pgrep %buildroot%_bindir/pkill
ln -snf skill %buildroot%_bindir/snice

# relocate shared libraries from %_libdir/ to /%_lib/
for f in %buildroot%_libdir/*.so; do
	t=$(readlink -v "$f")
	ln -snf ../../%_lib/"$t" "$f"
done
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%check
make check

%files
/bin/*
/sbin/*
%_bindir/*
%_mandir/man?/*
%doc AUTHORS Documentation/bugs.md Documentation/FAQ NEWS README.md top/README.top Documentation/TODO

%files -n lib%name
/%_lib/*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%changelog
* Wed Aug 28 2019 Mikhail Efremov <sem@altlinux.org> 3.3.15-alt4.git4c4d8b24640612
- ps: Initialize variable.
- procio: Make bit field unsigned.
- Updated to v3.3.15-76-g4c4d8b2.

* Wed May 22 2019 Mikhail Efremov <sem@altlinux.org> 3.3.15-alt3.git2f79ff3bc6a7ad
- Don't link with libsystemd directly.

* Mon May 13 2019 Mikhail Efremov <sem@altlinux.org> 3.3.15-alt2.git2f79ff3bc6a7ad
- Enable systemd support.
- Drop obsoleted configure option.
- Return to original top defaults.

* Fri Apr 26 2019 Mikhail Efremov <sem@altlinux.org> 3.3.15-alt1.git2f79ff3bc6a7ad
- pmap: Fix build on i586.
- top: Update "Protect scat() from buffer overflows" patch.
- Re-applied Qualys patches:
  + top: Protect scat() from buffer overflows.
  + top: Prevent integer overflows in procs_refresh().
- top: Fix warnings.
- proc: Fix strings truncation warnings.
- proc/sysinfo.c: Check return values.
- watch: Initialize variable.
- watch: Drop unused variable.
- tests: Disable ps_sched_batch.
- pwdx: Link against libprocps.
- Updated to v3.3.15-88-g2f79ff3.

* Thu Jan 29 2015 Mikhail Efremov <sem@altlinux.org> 3.3.7-alt2
- Fix ps_sched_batch test.
- Disable 'pmap with unreachable process' tests.
- Disable faulty tests.

* Thu Apr 25 2013 Dmitry V. Levin <ldv@altlinux.org> 3.3.7-alt1
- Updated to v3.3.7-15-g53fd7dd.

* Wed Jan 16 2013 Dmitry V. Levin <ldv@altlinux.org> 3.3.6-alt1
- Updated to procps-ng 3.3.6 (closes: #18136, #27296).

* Fri Sep 24 2010 Dmitry V. Levin <ldv@altlinux.org> 3.2.8-alt1
- Updated to 3.2.8.
- Updated patches from Debian procps-3.2.8-9, Fedora procps-3.2.8-10
  and openSUSE procps-3.2.8-19.8.
- Reviewed patches (closes: #20805); thanks to almost dead upstream,
  the amount of patches we have to maintain grows with time.
  In this release, the number of patches raised to 85.
- Fixed SELinux support.

* Thu Aug 26 2010 Dmitry V. Levin <ldv@altlinux.org> 3.2.7-alt3
- Enabled SELinux support (by Mikhail Efremov).

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 3.2.7-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Thu Oct 02 2008 Dmitry V. Levin <ldv@altlinux.org> 3.2.7-alt1
- Updated to 3.2.7.
- Updated patches, imported assorted patches from various vendors,
  see git changelog for details.

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 3.2.5-alt7
- Uncompressed tarball.

* Tue Mar 07 2006 Dmitry V. Levin <ldv@altlinux.org> 3.2.5-alt6
- Fixed build with --as-needed.

* Mon Dec 05 2005 Dmitry V. Levin <ldv@altlinux.org> 3.2.5-alt5
- Updated Owl patch for top.

* Mon Oct 24 2005 Dmitry V. Levin <ldv@altlinux.org> 3.2.5-alt4
- Applied Owl patch for top.

* Wed Sep 14 2005 Dmitry V. Levin <ldv@altlinux.org> 3.2.5-alt3
- Handle processes with unreadable /proc/#/stat files.

* Tue Aug 30 2005 Dmitry V. Levin <ldv@altlinux.org> 3.2.5-alt2
- Corrected ps(1) manpage formatting (closes #7759).

* Wed Aug 24 2005 Dmitry V. Levin <ldv@altlinux.org> 3.2.5-alt1
- Updated to 3.2.5.
- Reviewed patches, removed obsolete ones, updated all the rest.
- Imported a bunch of patches from RH and SuSE procps packages.
- Dropped unneeded -devel subpackage.
- Cleaned up the spec.
- Fixed build.

* Thu Jul 21 2005 Stanislav Ievlev <inger@altlinux.org> 3.2.4-alt2
- Added patch from SuSE for "-n" option.

* Thu Dec 23 2004 Stanislav Ievlev <inger@altlinux.org> 3.2.4-alt1
- 3.2.4

* Mon Aug 23 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.10-alt5
- Fix potential division by zero bug, reported by Alexey M. Tourbin.

* Wed Aug 11 2004 Stanislav Ievlev <inger@altlinux.org> 2.0.10-alt4.1
- setlocale in watch to see output with national symbols (e.g. russian)

* Wed Mar 31 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.10-alt4
- Do not package kill and its manpage, since
  coreutils >= 5.2.1-alt2 provides them.

* Mon Nov 03 2003 Stanislav Ievlev <inger@altlinux.org> 2.0.10-alt3.2
- fix bug reported by Yury A. Zotov (#3226)

* Thu Oct 23 2003 Stanislav Ievlev <inger@altlinux.org> 2.0.10-alt3
- fix building in hasher

* Mon Nov 18 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.10-alt2
- ressurected shutup patch

* Thu Nov 14 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.10-alt1
- 2.0.10

* Thu Jan 10 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-ipl6mdk
- fix locale patch

* Tue May 08 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-ipl5mdk
- Add RH, MDK and Openwall patches

* Sat Dec 02 2000 Dmitry V. Levin <ldv@fandra.org> 2.0.7-ipl4mdk
- PreReq: fileutils.

* Fri Sep 08 2000 Dmitry V. Levin <ldv@fandra.org> 2.0.7-ipl3mdk
- Fixed top: set LC_NUMERIC to C to make it work.

* Thu Jul 27 2000 Dmitry V. Levin <ldv@fandra.org> 2.0.7-ipl2mdk
- RE and Fandra adaptions.

* Fri Jul 21 2000 David BAUDENS <baudens@mandrakesoft.com> 2.0.7-2mdk
- Human readble description
- Use %%_tmppath for BuildRoot

* Fri Jul 21 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 2.0.7-1mdk
- updated.
- removed not needed anymore patch :
	- procps-proto-fix.patch.bz2
	- procps-2.0.6-sysmap.patch.bz2
	- procps-2.0.6-include.patch.bz2
	- procps-2.0.6-Makefile.patch.bz2
- added patch procps-2.0.7-makefile.patch
- install new manpages / binary.
- create man5 directory.
- pass mandir as a make argument.

* Wed May 17 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0.6-13mdk
- added devel package.

* Wed May 17 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0.6-13mdk
- added

* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 2.0.6-12mdk
- fix postin / postun.
- .so in devel package

* Tue Mar 28 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 2.0.6-11mdk
- Added a patch to fix an include compile time problem with new glibc.
- Fix group.
- Url wasn't pointing to the main procps site.

* Mon Mar 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.0.6-9mdk
- Fix sysctly_shut_your_mouth patch.

* Sun Mar 12 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.0.6-8mdk
- By default shut up the mouth of sysctl (and add the -v option to verbose it).

* Sat Mar 11 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.0.6-7mdk
- Add /sbin/sysctl in %%files.

* Tue Jan 18 2000 Francis Galiegue <francis@mandrakesoft.com>
- Fixed a wrong function prototype which made sparc's ps try to divide by zero

* Mon Jan 3 2000 Florent Villard <warly@mandrakesoft.com> 2.0.6-5mdk
- fix libproc.so problem

* Fri Dec 31 1999 Florent Villard <warly@mandrakesoft.com> 2.0.6-4mdk
- add link /lib/libproc.so to /lib/libproc.so.2.0.6

* Thu Dec 30 1999 Florent Villard <warly@mandrakesoft.com> 2.0.6-3mdk
- correct path permissions

* Sun Nov 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Provides: libproc.so.2.0

* Thu Nov  4 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.0.6.

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.0.5.
- include more manpages.

* Fri Aug 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix bogus permissions on doc (it was only availlable to root)

* Tue Jul  6 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Rebuild w/ prereq dev

* Tue Apr 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- FIx small bug with the /usr/X11R6/bin/

* Sun Apr 11 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- bzip2 man pages
- update to 2.0.2
- add de locale
- Mandrake adaptions
