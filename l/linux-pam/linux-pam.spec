Name: linux-pam
Version: 1.5.1
Release: alt1

Summary: Pluggable Authentication Modules
# The library is BSD-style *without* advertising clause, with option to relicense as GPLv2+.
License: BSD-3-Clause or GPLv2+
Group: System/Base
Url: https://github.com/linux-pam

%def_disable static
%def_enable nls
%def_enable audit
%def_enable selinux

# Linux-PAM name suffix
%define _pam_name_suffix	0

# Used for pam module package naming.
%define	make_pam_name()	pam%{_pam_name_suffix}_%{1}
%define	set_pam_name()	%global pam_name %(n='%{1}'; s="${n#pam_}"; [ "$n" = "$s" ] && echo -n "$n" || echo -n "pam%{_pam_name_suffix}_$s")

# Linux-PAM modules directory.
%define	_pam_modules_dir	/%_lib/security

# Linux-PAM library soname suffix.
%define _pam_so_suffix		%{nil}

# Linux-PAM library package name, used for tracking package dependencies.
%define	libpam			libpam%{_pam_name_suffix}

# git://git.altlinux.org/gears/l/linux-pam.git
Source: %name-%version-%release.tar

%define helperdir /sbin
%define _pamdir %_sysconfdir/pam.d
%define _secdir %_sysconfdir/security
%define docdir %_docdir/Linux-PAM-%version

BuildRequires: rpm-build >= 0:4.0.4-alt55

# Required for pam_conv1.
BuildRequires: flex

# Required for pam_userdb.
BuildRequires: libdb4-devel

# Required for docs.
BuildRequires: docbook-dtds docbook-style-xsl xsltproc w3m

# Required for audit support.
%{?_enable_audit:BuildRequires: libaudit-devel}

# Required for SELinux support.
%{?_enable_selinux:BuildRequires: libselinux-devel}

%package -n %libpam
Summary: Shared libraries for running PAM-based software
Group: System/Libraries
PreReq: pam-common
Provides: libpam(include), libpam(substack), libpam(optional_module)
Provides: libpam = %version-%release
Obsoletes: libpam

%package -n %libpam-devel
Summary: Libraries and header files for developing PAM-aware software
Group: Development/C
Requires: %libpam = %version-%release
Requires: rpm-macros-pam%{_pam_name_suffix} = %version-%release
Provides: libpam-devel = %version-%release, pam-devel = %version-%release
Obsoletes: libpam-devel, pam-devel
Conflicts: libpam2-devel

%package -n %libpam-devel-static
Summary: Static libraries for developing PAM-aware software
Group: Development/C
Requires: %libpam-devel = %version-%release
Provides: libpam-devel-static = %version-%release
Obsoletes: libpam-devel-static
Conflicts: libpam2-devel-static

%package -n pam
Summary: Pluggable Authentication Modules
Group: System/Base
Provides: %_secdir/limits.d
Requires: %libpam = %version-%release, pam-common >= 1.1
Obsoletes: pamconfig

%package -n pam-doc
Summary: Linux-PAM documentation
Group: Development/C
BuildArch: noarch
Requires: pam = %version-%release

%package -n %{make_pam_name timestamp}
Summary: Authenticate using cached successful authentication attempts
License: GPLv2+
Group: System/Base
Requires: pam = %version-%release
Provides: pam_timestamp = %version-%release

%package -n rpm-macros-pam%{_pam_name_suffix}
Summary: Set of RPM macros for packaging PAM modules
License: GPLv2+
Group: System/Base
BuildArch: noarch
Provides: rpm-macros-pam = %version-%release
Conflicts: rpm-macros-pam2
Obsoletes: pam_timestamp, pam_timestamp0

%description
Linux-PAM (Pluggable Authentication Modules) is a system security tool
that allows system administrators to set authentication policy without
having to recompile programs that handle authentication.

%description -n %libpam
Linux-PAM (Pluggable Authentication Modules) is a system security tool
that allows system administrators to set authentication policy without
having to recompile programs that handle authentication.

This package contains shared libraries required for running both
PAM-aware applications and modules for use with Linux-PAM.

%description -n %libpam-devel
Linux-PAM (Pluggable Authentication Modules) is a system security tool
that allows system administrators to set authentication policy without
having to recompile programs that handle authentication.

This package contains header files and development libraries used for
building both PAM-aware applications and modules for use with Linux-PAM.

%description -n %libpam-devel-static
Linux-PAM (Pluggable Authentication Modules) is a system security tool
that allows system administrators to set authentication policy without
having to recompile programs that handle authentication.

This package contains static libraries used for building statically
linked PAM-aware applications for use with Linux-PAM.

%description -n pam
Linux-PAM (Pluggable Authentication Modules) is a system security tool
that allows system administrators to set authentication policy without
having to recompile programs that handle authentication.

%description -n pam-doc
Linux-PAM (Pluggable Authentication Modules) is a system security tool
that allows system administrators to set authentication policy without
having to recompile programs that handle authentication.

This package contains detailed Linux-PAM documentation.

%description -n %{make_pam_name timestamp}
The pam_timestamp module implements sudo-style authentication
timestamps.

See pam_timestamp(8) for details.

%description -n rpm-macros-pam%{_pam_name_suffix}
This packages contains RPM macros for packaging PAM modules.

%prep
%setup -n %name-%version-%release
cp -p alt/pam_listfile.c modules/pam_listfile/

find -type f \( -name .cvsignore -o -name \*~ -o -name \*.orig \) -delete

%build
./autogen.sh
%configure \
	--libdir=/%_lib \
	--sbindir=/sbin \
	--includedir=%_includedir/security \
	--docdir=%docdir \
	--disable-prelude \
	--disable-unix \
	--enable-Werror \
	%{subst_enable selinux} \
	%{subst_enable audit} \
	%{subst_enable nls} \
	%{subst_enable static} \
	#
%make_build sepermitlockdir=%_lockdir/sepermit servicedir=%_unitdir

%install
%makeinstall_std sepermitlockdir=%_lockdir/sepermit servicedir=%_unitdir

# Relocate development libraries from /%_lib/ to %_libdir/.
mkdir -p %buildroot%_libdir
mv %buildroot/%_lib/*.*a %buildroot%_libdir/
/sbin/ldconfig -nv %buildroot/%_lib
for f in %buildroot/%_lib/*.so; do
	t=$(readlink -v "$f")
	ln -s ../../%_lib/"$t" "%buildroot%_libdir/${f##*/}"
	rm -f "$f"
done
rm -f %buildroot%_pam_modules_dir/*.la

# Make sure that no module exports symbols beyond standard set.
>check.log
for f in %buildroot%_pam_modules_dir/pam*.so; do
	readelf -Ws "$f" |
		grep -w GLOBAL |
		grep -Ewv 'UND|pam_sm_(acct_mgmt|authenticate|chauthtok|close_session|open_session|setcred)'  ||
			continue
	echo "ERROR: ${f##*/} exports symbol(s) beyond standard set." >&2
	echo "${f##*/}" >>check.log
done
! [ -s check.log ] || exit 1

# Make sure that no shared object has undefined symbols.
>check.log
for f in %buildroot/%_lib/lib*.so.0 %buildroot%_pam_modules_dir/pam*.so; do
	LD_LIBRARY_PATH="%buildroot/%_lib" ldd -r "$f" 2>&1 >/dev/null |
		tee -a check.log
done
! [ -s check.log ] || exit 1

# Make sure that none of the modules pull in threading libraries.
>check.log
for f in %buildroot%_pam_modules_dir/pam*.so; do
	# except pam_userdb
	[ "${f##*/}" != pam_userdb.so ] ||
		continue
	LD_LIBRARY_PATH="%buildroot/%_lib" ldd -r "$f" 2>&1 |
		fgrep -q libpthread ||
			continue
	echo "ERROR: ${f##*/} pulls in libpthread." >&2
	echo "${f##*/}" >>check.log
done
! [ -s check.log ] || exit 1

# pam_limits configuration
install -pm644 alt/50-defaults.conf \
	%buildroot%_secdir/limits.d/

# Linux-PAM-specific rpm macros.
install -pDm644 alt/linux-pam.macros \
	%buildroot%_rpmmacrosdir/pam

mkdir -p %buildroot%_tmpfilesdir
install -pm644 alt/faillock.conf %buildroot%_tmpfilesdir/
mkdir -p %buildroot/var/run/faillock

%if_enabled selinux
mkdir -p %buildroot%_lockdir/sepermit
install -pm644 alt/sepermit.conf %buildroot%_tmpfilesdir/
%endif # enabled selinux

# Documentation
mkdir -p %buildroot%docdir/modules
for f in modules/pam_*/README; do
	d="${f%%/*}"
	[ -s "$d/Makefile" ] || continue
	install -pm644 "$f" "%buildroot%docdir/modules/${d##*/}"
done
mkdir -p %buildroot%docdir/html
mv %buildroot%docdir/*.html %buildroot%docdir/html/
install -pm644 alt/PAM-Policy.ALT AUTHORS NEWS Copyright %buildroot%docdir/
find %buildroot%docdir/ -type f -size +4k \( -iname changelog -or -name \*.txt -or -name \*.ps \) -print0 |
	xargs -r0 bzip2 -9f --

# buildreq substitution rules
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
for n in libpam{,-devel%{?_enable_static:{,-static}}}; do
	echo $n >"%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%libpam${n#libpam}"
done

%find_lang Linux-PAM

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check VERBOSE=1

%files -n %libpam
%config %_sysconfdir/buildreqs/packages/substitute.d/%libpam
/%_lib/*.so.*
%_pam_modules_dir/pam_deny.so
%_pam_modules_dir/pam_permit.so
%dir %docdir
%docdir/AUTHORS*
%docdir/Copyright*
%docdir/NEWS*

%files -n %libpam-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/%libpam-devel
%_libdir/*.so
%_includedir/*
%_man3dir/*
%dir %docdir
%docdir/PAM*

%if_enabled static
%files -n %libpam-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/%libpam-devel-static
%_libdir/*.a
%endif # enabled static

%files -n rpm-macros-pam%{_pam_name_suffix}
%_rpmmacrosdir/pam

%files -n pam -f Linux-PAM.lang
%helperdir/faillock
%helperdir/mkhomedir_helper
%helperdir/pam_namespace_helper
%attr(700,root,root) %helperdir/pwhistory_helper
%_unitdir/pam_namespace.service
%config(noreplace) %_secdir/access.conf
%config(noreplace) %_secdir/faillock.conf
%config(noreplace) %_secdir/time.conf
%config(noreplace) %attr(640,root,wheel) %_secdir/group.conf
%config(noreplace) %_secdir/limits.conf
%config(noreplace) %_secdir/limits.d
%config(noreplace) %_secdir/namespace.*
%config(noreplace) %_secdir/pam_env.conf
%config(noreplace) %_sysconfdir/environment
%_tmpfilesdir/faillock.conf
%dir /var/run/faillock/
%if_enabled selinux
%config(noreplace) %_secdir/sepermit.conf
%dir %_lockdir/sepermit/
%_tmpfilesdir/sepermit.conf
%endif # enabled selinux
%_pam_modules_dir/*
%exclude %_pam_modules_dir/pam_deny.so
%exclude %_pam_modules_dir/pam_permit.so
%exclude %_pam_modules_dir/pam_timestamp.so
%_mandir/man[58]/*.*
%exclude %_mandir/man[58]/pam_timestamp*

%files -n %{make_pam_name timestamp}
%attr(700,root,root) %helperdir/pam_timestamp_check
%_pam_modules_dir/pam_timestamp.so
%_mandir/man[58]/pam_timestamp*

%files -n pam-doc
%dir %docdir
%docdir/[a-z]*
%docdir/Linux-PAM*

%changelog
* Tue Nov 24 2020 Dmitry V. Levin <ldv@altlinux.org> 1.5.1-alt1
- v1.5.0 -> v1.5.1.

* Thu Nov 05 2020 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt1
- v1.4.0-52-g650273e7 -> v1.5.0.
  Note that pam_tally and pam_tally2 were removed in favour of pam_faillock.
- Packaged pam_tty_audit module.

* Thu Aug 06 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4.0.0.52.6502-alt1
- v1.4.0 -> v1.4.0-52-g650273e7.

* Thu Jun 04 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt1
- v1.3.1-324-geec5fe0d -> v1.4.0.

* Fri May 22 2020 Dmitry V. Levin <ldv@altlinux.org> 1.3.1.0.324.eec5-alt1
- v1.3.1-223-gc2c0434b -> v1.3.1-324-geec5fe0d.
  New module: pam_faillock.
  Note that pam_tally and pam_tally2 are deprecated in favour of pam_faillock.

* Sun Apr 26 2020 Dmitry V. Levin <ldv@altlinux.org> 1.3.1.0.223.c2c0-alt1
- v1.3.1-212-g76916913 -> v1.3.1-223-gc2c0434b (closes: #38389).

* Fri Apr 24 2020 Dmitry V. Levin <ldv@altlinux.org> 1.3.1.0.212.76916-alt1
- v1.3.1-210-gf8fc7504 -> v1.3.1-212-g76916913.

* Fri Apr 24 2020 Dmitry V. Levin <ldv@altlinux.org> 1.3.1.0.210.f8fc-alt1
- v1.3.1-5-g955b3e2 -> v1.3.1-210-gf8fc7504.
  New modules: pam_setquota, pam_usertype.

* Thu Jul 05 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.1.0.5.955b-alt2
- Fixed Russian translation (closes: #35128).

* Fri Jun 22 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.1.0.5.955b-alt1
- v1.3.1 -> v1.3.1-5-g955b3e2 (fixes grammar of messages printed via pam_prompt).
- Updated Russian translation.

* Fri May 18 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt1
- v1.3.0-23-g94f529d4 -> v1.3.1.

* Thu Nov 09 2017 Dmitry V. Levin <ldv@altlinux.org> 1.3.0.0.23.94f5-alt2
- %helperdir/pam_tally2 --reset: avoid creating a missing tallylog file (closes: #34035).
- Packaged %%ghost %_logdir/tallylog file.

* Thu Oct 26 2017 Dmitry V. Levin <ldv@altlinux.org> 1.3.0.0.23.94f5-alt1
- v1.3.0-17-g7d0c508 -> v1.3.0-23-g94f529d4.
- pam_sepermit: changed sepermit lock directory to %_lockdir/sepermit.

* Tue Jun 20 2017 Dmitry V. Levin <ldv@altlinux.org> 1.3.0.0.17.7d0c-alt1
- v1.3.0-4-gdce30cd -> v1.3.0-17-g7d0c508.
- Enabled pam_keyinit module (closes: #33558).

* Tue Jun 14 2016 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt1
- v1.1.8-54-g5df44a3 -> v1.3.0-4-gdce30cd.

* Fri Nov 28 2014 Dmitry V. Levin <ldv@altlinux.org> 1.1.8-alt5
- Updated to v1.1.8-54-g5df44a3.

* Mon Mar 31 2014 Dmitry V. Levin <ldv@altlinux.org> 1.1.8-alt4
- Updated to v1.1.8-32-g9dcead8.

* Tue Jan 28 2014 Dmitry V. Levin <ldv@altlinux.org> 1.1.8-alt3
- Updated to v1.1.8-29-g316e993.

* Fri Jan 10 2014 Dmitry V. Levin <ldv@altlinux.org> 1.1.8-alt2
- Updated to v1.1.8-15-g24f3a88.

* Mon Nov 18 2013 Dmitry V. Levin <ldv@altlinux.org> 1.1.8-alt1
- Updated to v1.1.8-6-g5865f52.

* Mon Oct 15 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1.6-alt2
- Updated to v1.1.6-5-g0603b28.

* Fri Aug 24 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1.6-alt1
- Updated to 1.1.6.

* Mon Feb 13 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1.5-alt2
- Updated to Linux-PAM-1_1_5-26-g3c69856.

* Tue Oct 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.1.5-alt1
- Updated to 1.1.5.

* Fri Mar 18 2011 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt3
- pam_mkhomedir: changed default umask from 0022 to 0077 (closes: #25247).

* Sat Feb 26 2011 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt2
- Backported pam_selinux fixes from HEAD.
- Rebuilt for debuginfo.

* Thu Oct 28 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt1
- Updated to Linux-PAM-1_1_3 (fixes CVE-2010-3853).

* Tue Oct 19 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt4
- Updated to Linux-PAM-1_1_2-13-g4d9616d.
- pam_selinux: Refactored, implemented "restore" option.
- macros.d/pam: Removed %%config flag.

* Mon Oct 04 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt3
- Updated to Linux-PAM-1_1_2-6-g843807a
  (fixes CVE-2010-3430 and CVE-2010-3431).

* Fri Sep 03 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt2
- Made rpm-macros-pam* noarch.

* Thu Sep 02 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt1
- Updated to Linux-PAM-1_1_2 (fixes CVE-2010-3316).

* Fri Jul 02 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt2
- Updated to Linux-PAM-1_1_1-16-ge305200.

* Wed Mar 10 2010 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1.1
- Enabled build with SELinux.

* Wed Dec 16 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt1
- Updated Linux-PAM to Linux-PAM-1_1_1.
- Moved pam-redhat to separate package.
- Moved rpm macros to separate subpackage rpm-macros-pam.

* Fri Nov 13 2009 Anton Farygin <rider@altlinux.ru> 1.1.0-alt3.1
- NMU: removed v4l and dvb permissions control from pam0_console

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt3
- Moved "make check" to %%check section.

* Fri Jun 26 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt2
- libpam: Added libpam(optional_module) to provides list.
- pam_console: Create system group "scanner" and
  use it in rules (closes: #20477).

* Fri Jun 19 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt1
- Updated Linux-PAM to Linux-PAM-1_1_0.
- Updated pam-redhat to 0.99.10-1.

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt5
- pam_console %%post: Create xgrp system group.

* Wed Apr 08 2009 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt4
- libpam/pam_audit.c (_pam_audit_writelog): Removed unreliable getuid() check.

* Fri Apr 03 2009 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt3
- Replaced all calls to exit(3) in child processes
  with calls to _exit(2).

* Mon Mar 30 2009 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt2
- Enabled audit support by default.

* Tue Mar 03 2009 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt1
- Updated Linux-PAM to Linux-PAM-1_0_4.

* Wed Dec 10 2008 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt1
- Updated Linux-PAM to Linux-PAM-1_0_3.
- Packaged -doc subpackage as noarch.
- Removed obsolete %%post_ldconfig_sys/%%postun_ldconfig calls.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt1
- Updated Linux-PAM to Linux-PAM-1_0_2.
- Fixed build with fresh autoconf.

* Wed Apr 16 2008 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- Updated Linux-PAM to Linux-PAM-1_0_1.

* Fri Apr 04 2008 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1
- Updated Linux-PAM to Linux-PAM-1_0_0 (bugfix only).
- Enabled nls support by default.

* Wed Feb 20 2008 Dmitry V. Levin <ldv@altlinux.org> 0.99.10.0-alt1
- Updated Linux-PAM to 0.99.10.0-4-gb453d28; most essential changes:
  + New substack directive in config file syntax.
  + New PAM items: PAM_XDISPLAY and PAM_XAUTHDATA.
  + Finaly removed deprecated pam_rhosts_auth module.
  + misc_conv no longer blocks SIGINT.
  + pam_limits: Added support for limits.d directory.
- Updated pam-redhat to 0.99.8-1.
- Enabled new modules: pam_faildelay, pam_namespace.
- pam_limits:
  + Moved default limits from limits.conf to limits.d/50-defaults.conf
  + Raised nproc limit from 256/512 to 512/1024.
- pam_console:
  + Moved default permission definitions from console.perms
    to console.perms.d/50-default.perms
- pam_console_apply: Fixed garbage output on error path (#4634).
- 50-default.perms: Changed <dri> permissions (#6831).
- 50-default.perms (joystick): Added /dev/input/js[0-9]* (#7669).
- pam_console no longer needs glib (#8791).

* Wed Apr 11 2007 Dmitry V. Levin <ldv@altlinux.org> 0.99.6.3-alt2
- Backported several fixes from Linux-PAM 0.99.7.1.

* Sun Sep 10 2006 Dmitry V. Levin <ldv@altlinux.org> 0.99.6.3-alt1
- Updated Linux-PAM to 0.99.6.3.
- Packaged %_sysconfdir/environment file.

* Sun Aug 27 2006 Dmitry V. Levin <ldv@altlinux.org> 0.99.6.2-alt1
- Updated Linux-PAM to 0.99.6.2:
- pam_umask: Enabled packaging.
- pam_rhosts: New module which replaces pam_rhosts_auth.
- Enhanced documentation for PAM functions and modules.

* Tue Jun 06 2006 Dmitry V. Levin <ldv@altlinux.org> 0.99.4.0-alt2
- Updated Linux-PAM to cvs snapshot 20060523.

* Fri May 05 2006 Dmitry V. Levin <ldv@altlinux.org> 0.99.4.0-alt1
- Updated Linux-PAM to 0.99.4.0.

* Mon Mar 20 2006 Dmitry V. Levin <ldv@altlinux.org> 0.99.3.0-alt2
- Backported a few fixes from cvs.

* Mon Jan 16 2006 Dmitry V. Levin <ldv@altlinux.org> 0.99.3.0-alt1
- Updated Linux-PAM to 0.99.3.0.

* Thu Jan 12 2006 Dmitry V. Levin <ldv@altlinux.org> 0.99.2.1-alt2
- Updated Linux-PAM to cvs snapshot 20060111.
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Tue Dec 13 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.2.1-alt1
- Updated Linux-PAM to 0.99.2.1.
- Updated %%_pam_modules_dir (fixes #8630).

* Thu Nov 24 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.2.0-alt1
- Updated Linux-PAM to cvs snapshot 20051124.

* Fri Nov 18 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.1.0-alt4
- Updated Linux-PAM to cvs snapshot 20051118.

* Mon Oct 03 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.1.0-alt3
- Updated Linux-PAM to cvs snapshot 20051004.
- Merged upstream patches:
  owl-strdup-cleanup

* Fri Sep 30 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.1.0-alt2
- Updated Linux-PAM to cvs snapshot 20050930.
- Fixed several memory leaks in few modules.

* Mon Sep 26 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.1.0-alt1
- Updated Linux-PAM to 0.99.1.0.
- Merged upstream patches:
  owl-pam_mail
  owl-pam_nologin
  owl-pam_xauth

* Wed Sep 21 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.0.3-alt6
- Updated Linux-PAM to cvs snapshot 20050921.
- Merged upstream patches:
  owl-attribute
  owl-pam_issue
  owl-pam_lastlog-fixes
  owl-pam_limits
  owl-pam_userdb
  owl-sprintf
- Fixed pam_xauth.

* Mon Sep 19 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.0.3-alt5
- Updated Linux-PAM to cvs snapshot 20050918.
- Merged upstream patches:
  owl-pam_access
  owl-pammodutil-makefile
- Fixed pam_mail and pam_nologin.

* Sun Sep 18 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.0.3-alt4
- Updated Linux-PAM to cvs snapshot 20050917.
- Merged upstream patches:
  owl-conv-warning
  owl-pam_deny
  owl-pam_env
  owl-pam_motd
  owl-pam_permit
  owl-pam_start
  owl-pam_warn
- Fixed pam_issue.

* Fri Sep 16 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.0.3-alt3
- Updated Linux-PAM to cvs snapshot 20050915.
- Merged upstream patches:
  owl-pam_ext
  owl-libpam_misc-makefile
  owl-pam_filter-upperLOWER
  owl-pam_ftp
  owl-pam_lastlog
  owl-pam_tally
  owl-pam_time
  owl-pam_userdb
- Enhanced errors diagnostics.
- Fixed compilation warnings.

* Sat Sep 10 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.0.3-alt2
- Added more const and attribute tags to function prototypes.
- Fixed pam_lastlog.

* Wed Sep 07 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.0.3-alt1
- Updated Linux-PAM to cvs snapshot 20050906.
- Merged upstream patches:
  owl-tmp,
  owl-pam_get_user-cache-failures,
  owl-man,
  owl-pam_securetty,
  owl-pam_limits,
  owl-pam_motd,
  owl-configure,
  owl-pam_filter,
  owl-pammodutil-attribute.
- Updated patches.
- Disabled packaging of the static library.
- Finished Linux-PAM migration to pam_syslog/pam_prompt.

* Fri Aug 26 2005 Dmitry V. Levin <ldv@altlinux.org> 0.80-alt2
- pam0_console: fixed console.handlers (#7752).

* Wed Aug 17 2005 Dmitry V. Levin <ldv@altlinux.org> 0.80-alt1
- Restricted list of global symbols exported by libraries.

* Fri Aug 12 2005 Dmitry V. Levin <ldv@altlinux.org> 0.80-alt0.3
- Cleaned up conversation wrappers.
- Raised nprocs limits in limits.conf (#5636).
- Added pam_sm_acct_mgmt for pam_mkhomedir module (#6989).

* Thu Aug 11 2005 Dmitry V. Levin <ldv@altlinux.org> 0.80-alt0.2
- Changed modules logging to eliminate disunion in behaviour and
  avoid openlog/closelog calls for each logging function invocation.
- Restricted list of global symbols exported by PAM modules to
  standard set of six pam_sm_* functions.

* Mon Jul 18 2005 Dmitry V. Levin <ldv@altlinux.org> 0.80-alt0.1
- Updated Linux-PAM to 0.80.
- Updated pam-redhat to 0.80-1.
- Disabled build and packaging of the pam_stack module.
- Reviewed patches, removed obsolete ones, updated all the rest.

* Thu Feb 10 2005 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt28
- Fixed multilib (closes #5091).

* Tue Aug 03 2004 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt27
- pam_console: Fixed /dev/sg* permissions (#4742).
- Added multilib support (#4891).

* Wed May 05 2004 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt26
- console.perms: added /dev/dri/* to <dri> (#2507).
- console.perms: fixed typo in <console> (#3343).
- pam_userdb: build with libdb4 (#4080).

* Thu Nov 06 2003 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt25
- Build with %%optflags_shared.

* Sat Sep 27 2003 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt24
- /etc/rpm/macros.d/pam: reverted previous change.

* Fri Sep 26 2003 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt23
- pam_limits: don't invoke setrlimit(2) on limits which are not
  set explicitly as simply resetting RLIMIT_FSIZE to what
  appears to be its current value may decrease the actual
  limit with LFS (Owl).
- Added buildreq substitution rules.
- /etc/rpm/macros.d/pam: updated (#3050).

* Wed Jul 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt22
- pam_wheel: patched to never rely on getlogin(3).
- pam_console: added "/dev/snd/*" to console.perms <sound> list.
- Renamed:
  pam_console0 -> pam0_console
  pam_stack0 -> pam0_stack
  pam_timestamp0 -> pam0_timestamp
- Updated PAM Policy file.
- Updated rpm macros file.

* Thu May 29 2003 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt21
- Renamed:
  libpam -> libpam0
  libpam-devel -> libpam0-devel
  libpam-devel-static -> libpam0-devel-static
  pam_console -> pam_console0
  pam_stack -> pam_stack0
  pam_timestamp -> pam_timestamp0
- Relocated /etc/pam.d/other from this package to pam-common.
- Relocated pam_{deny,permit}.so modules to libpam0 subpackage.
- Added Linux-PAM-specific rpm macros file.
- Updated PAM Policy file.

* Fri May 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt20
- Implemented pam include config support.
- Moved pam_stack to separate subpackage.

* Fri May 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt19
- Cleaned up build a bit.
- Build with --disable-read-both-confs
 (when /etc/pam.d/ exists, don't look at /etc/pam.conf).
- Moved pam_timestamp to separate subpackage.
- Relocated Linux-PAM documentation to %docdir.

* Thu Feb 13 2003 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt18
- Updated pam_xauth to pam-redhat-0.75-48.
- pam_xauth: removed wildcards support introduced in pam-redhat-0.75-48.

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt17
- Patched pam_motd to behave on errors (Owl).
- Updated pam_timestamp* to pam-redhat-0.75-40.
- Fixed library symlinks generation.
- Use subst instead of perl for build.
- Updated devel-static requirements.

* Wed Jul 31 2002 Dmitry V. Levin <ldv@altlinux.org> 0.75-alt16
- Simplified read_string patch.
- Readded documentation in PostScript format.
- Dropped buildrequires on libcrypt.so.1(GLIBC_2.2.2), no longer needed
  since we don't build pam_unix/pam_pwdb.
- Added patches from Owl:
  + Moved pam.d and pam.conf man pages to section 5 where they belong.
  + pam_limits: support stacking for account management (as well as for
    session setup), be fail-close on configuration file reads, report the
    "too many logins" via PAM conversation rather than direct printf(3).
- Updated pam-redhat to -38:
  + pam_xauth: fix cases where DISPLAY is "localhost:screen" and
    the xauth key is actually stored using the system's hostname;
  + pam_timestamp fixes;
  + added pam_timestamp_check.

* Thu Mar 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.75-alt15
- Updated console.perms <dri> rules.
- Relaxed %_secdir/console.apps permissions a bit.

* Wed Mar 20 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.75-alt14
- Fixed pam_console %%triggerpostun script.
- Fixed %_secdir/console.* permissions.

* Fri Mar 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.75-alt13
- Updated pam-redhat to -27 (added pam_timestamp).
- Relocated helpers back to /sbin/.
- Updated console.perms to new scheme.
- Moved pam_console stuff to separate subpackage.
- Run %helperdir/pam_console_apply in pam_console %%post.

* Thu Dec 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.75-alt12
- Merged RH patches (rh release 20).
- Merged Owl patches (owl release 14).
- Dropped: pam_unix, pam_pwdb, pam_cracklib.

* Wed Sep 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt11
- Merged RH patches (rh release 12, pam_stack still from 5).
- console.perms: corrected console class description.
- Moved cracklib module to separate subpackage.
- fixed and relocated docs.

* Thu Sep 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt10
- pam_stack: revert to old version (from rh release 5) for now.

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt9
- Moved changable system-auth config to pam-config package.

* Fri Sep 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt8
- Relocated helper programs to %helperdir.
- Rebuilt to get more dependencies.

* Wed Aug 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt7
- Moved %_lockdir/console /var/run/console.
- Merged RH patches (rh release 10).
- Removed versioned dependence on glibc package.
- Added requires on libcrypt.so.1(GLIBC_2.2.1).

* Mon Jun 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt6
- More sanity checks in pam_unix_passwd.c

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt5
- Fixed more errors in pam_console/chmod.c

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt4
- Fixed recent typo in pam_unix/support.h

* Tue May 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt3
- 0.75 (rh release 2).
- Attempt to fix loop in pam_console.

* Thu May 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt2
- Fixed pam_unix-chkpwd helper.

* Tue May 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.75-alt1
- 0.75 (rh release 1).
- Moved static libraries to devel-static subpackage.

* Thu Mar 01 2001 Dmitry V. Levin <ldv@fandra.org> 0.74-ipl5mdk
- Merged RH patches (rh release 12).
- Libification.

* Sat Feb 24 2001 Dmitry V. Levin <ldv@fandra.org> 0.74-ipl4mdk
- Merged RH patches (rh release 10).

* Fri Feb 23 2001 Dmitry V. Levin <ldv@fandra.org> 0.74-ipl3mdk
- changed console.perms:
  <console> 0600 <burner> 0600 root.cdwriter

* Sun Feb 11 2001 Dmitry V. Levin <ldv@fandra.org> 0.74-ipl2mdk
- Enhanced unix_chkpwd to support LOGNAME environment variable.
- Merged RH patches (rh release 5).

* Wed Jan 31 2001 Dmitry V. Levin <ldv@fandra.org> 0.74-ipl1mdk
- 0.74 (sync with Linux-PAM and pam-redhat).
- Moved development libraries from /lib to %_libdir.

* Fri Jan 12 2001 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl16mdk
- Use libc_crypt as crypt function (glibc >= 2.2.1-ipl0.3mdk).

* Wed Jan 10 2001 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl15mdk
- Integrated new feaures of glibc >= 2.2.1-ipl0.2mdk:
  + added blowfish crypt support for pam_unix (libcrypt);
  + dropped BSDIcrypt support for pam_unix (it was never used);
  + set default crypt to blowfish in system-auth.

* Fri Jan 05 2001 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl14mdk
- Updated console.perms patch.
- Built with db2.

* Wed Dec 06 2000 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl13mdk
- Merge RH changes (26-->37).

* Tue Oct 17 2000 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl12mdk
- Added pam_sameuid module.

* Fri Oct 06 2000 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl11mdk
- Merge last RH changes (by Nalin Dahyabhai <nalin@redhat.com>):
  + clean up logging in pam_xauth;
  + mova README.* files in txt subdirectory;
  + add pam_tally's application to allow counts to be reset;
  + move pam_filter modules to /lib/security/pam_filter;
  + add DRI and nvidia devices to console.perms.
- Fixed:
  + pam_stack now passes delay back.

* Wed Sep 27 2000 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl10mdk
- Added:
  + BSDIcrypt support for pam_unix;
  + pam_limits in system-auth.

* Tue Sep 26 2000 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl9mdk
- Merge last RH changes (by Nalin Dahyabhai <nalin@redhat.com>):
  + add a broken_shadow option to pam_unix;
  + add all module README files to the documentation list;
  + fix pam_stack debug and losing-track-of-the-result bug;
  + rework pam_console's usage of syslog to actually be sane (#14646);
  + take the LOG_ERR flag off of some of pam_console's new messages.
- Merge last MDK changes:
  + set all sound stuff to audio group;
  + add cdburner permissions;
  + add %_pamdir/system-auth;
  + noreplace configs.

* Mon Sep 04 2000 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl8mdk
- Merge with last MDK changes.

* Fri Jul 21 2000 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl7mdk
- Merge with last RH changes.
- Added: BSDIcrypt support.

* Wed May 31 2000 Dmitry V. Levin <ldv@fandra.org> 0.72-ipl6mdk
- Package split into pam, pam-devel and pam-doc packages
- RE adaptions.

* Tue Feb 22 2000 Dmitry V. Levin <ldv@fandra.org>
- Fixes:
  + read_string bugfix
  + real buildroot packaging
- more documentation included
- Fandra adaptions.

* Sat Feb 05 2000 Nalin Dahyabhai <nalin@redhat.com>
- Fix pam_xauth bug #6191.

* Thu Feb 03 2000 Elliot Lee <sopwith@redhat.com>
- Add a patch to accept 'pts/N' in /etc/securetty as a match for tty '5'
  (which is what other pieces of the system think it is). Fixes bug #7641.

* Mon Jan 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- argh, turn off gratuitous debugging

* Wed Jan 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 0.72
- fix pam_unix password-changing bug
- fix pam_unix's cracklib support
- change package URL

* Mon Jan 03 2000 Cristian Gafton <gafton@redhat.com>
- don't allow '/' on service_name

* Thu Oct 21 1999 Cristian Gafton <gafton@redhat.com>
- enhance the pam_userdb module some more

* Fri Sep 24 1999 Cristian Gafton <gafton@redhat.com>
- add documenatation

* Tue Sep 21 1999 Michael K. Johnson <johnsonm@redhat.com>
- a tiny change to pam_console to make it not loose track of console users

* Mon Sep 20 1999 Michael K. Johnson <johnsonm@redhat.com>
- a few fixes to pam_xauth to make it more robust

* Wed Jul 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- pam_console: added <xconsole> to manage /dev/console

* Thu Jul 01 1999 Michael K. Johnson <johnsonm@redhat.com>
- pam_xauth: New refcounting implementation based on idea from Stephen Tweedie

* Sat Apr 17 1999 Michael K. Johnson <johnsonm@redhat.com>
- added video4linux devices to /etc/security/console.perms

* Fri Apr 16 1999 Michael K. Johnson <johnsonm@redhat.com>
- added joystick lines to /etc/security/console.perms

* Thu Apr 15 1999 Michael K. Johnson <johnsonm@redhat.com>
- fixed a couple segfaults in pam_xauth uncovered by yesterday's fix...

* Wed Apr 14 1999 Cristian Gafton <gafton@redhat.com>
- use gcc -shared to link the shared libs

* Wed Apr 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- many bug fixes in pam_xauth
- pam_console can now handle broken applications that do not set
  the PAM_TTY item.

* Tue Apr 13 1999 Michael K. Johnson <johnsonm@redhat.com>
- fixed glob/regexp confusion in pam_console, added kbd and fixed fb devices
- added pam_xauth module

* Sat Apr 10 1999 Cristian Gafton <gafton@redhat.com>
- pam_lastlog does wtmp handling now

* Thu Apr 08 1999 Michael K. Johnson <johnsonm@redhat.com>
- added option parsing to pam_console
- added framebuffer devices to default console.perms settings

* Wed Apr 07 1999 Cristian Gafton <gafton@redhat.com>
- fixed empty passwd handling in pam_pwdb

* Mon Mar 29 1999 Michael K. Johnson <johnsonm@redhat.com>
- changed /dev/cdrom default user permissions back to 0600 in console.perms
  because some cdrom players open O_RDWR.

* Fri Mar 26 1999 Michael K. Johnson <johnsonm@redhat.com>
- added /dev/jaz and /dev/zip to console.perms

* Thu Mar 25 1999 Michael K. Johnson <johnsonm@redhat.com>
- changed the default user permissions for /dev/cdrom to 0400 in console.perms

* Fri Mar 19 1999 Michael K. Johnson <johnsonm@redhat.com>
- fixed a few bugs in pam_console

* Thu Mar 18 1999 Michael K. Johnson <johnsonm@redhat.com>
- pam_console authentication working
- added /etc/security/console.apps directory

* Mon Mar 15 1999 Michael K. Johnson <johnsonm@redhat.com>
- added pam_console files to filelist

* Fri Feb 12 1999 Cristian Gafton <gafton@redhat.com>
- upgraded to 0.66, some source cleanups

* Mon Dec 28 1998 Cristian Gafton <gafton@redhat.com>
- add patch from Savochkin Andrey Vladimirovich <saw@msu.ru> for umask
  security risk

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- upgrade to ver 0.65
- build the package out of internal CVS server
