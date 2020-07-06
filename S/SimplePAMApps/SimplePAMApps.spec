Name: SimplePAMApps
Version: 0.60
Release: alt36

%def_with login
%def_with su

Summary: Simple PAM-based Applications
License: BSD or GPL
Group: System/Base
Url: http://www.linux-pam.org/pre/applications/

# http://www.linux-pam.org/pre/applications/%name-%version.tar.bz2
Source0: %name-0.60.tar
Source1: login.pamd
Source2: su.pamd
Source3: su.control

Patch0: %name-0.60-alt-_BSD_SOURCE.patch
Patch1: %name-0.60-owl-alt-login.patch
Patch2: %name-0.60-owl-alt-su.patch
Patch3: %name-0.60-owl-alt-login-su-ut_id.patch
Patch4: %name-0.60-alt-login-su-ut_user.patch
Patch5: %name-0.60-alt-login-su-env.patch
Patch6: %name-0.60-alt-login-su-strip-argv0.patch
Patch7: %name-0.60-alt-owl-warnings.patch
Patch8: %name-0.60-owl-log.patch
Patch9: %name-0.60-owl-su-pam_acct_mgmt.patch
Patch10: %name-0.60-alt-makefile-passwd.patch
Patch11: %name-0.60-alt-openpam.patch
Patch12: %name-0.60-alt-audit.patch
Patch13: %name-0.60-alt-utmp_do_close_session.patch
Patch14: %name-0.60-alt-su-make_process_killable.patch
Patch15: %name-0.60-alt-login-do-not-set-PAM_RUSER-and-PAM_RHOST.patch

BuildPreReq: libpam-devel libaudit-devel

%description
These are applications for use with the Linux-PAM library.
This package may include "login" and "su".

%package -n login
Summary: Start an interactive session on the system
Group: System/Base
# pam_console fixed for login lives in 0.75-alt11.
#Requires: pam >= 0.75-alt11
# pam_lastlog fixed (nowtmp option added) in 0.75-alt12.
Requires: pam >= 0.75-alt12

%description -n login
The login application opens an interactive session with a Linux
workstation.  It is one of the first applications a user interacts with,
but is generally not invoked by a normal user.  Instead some program
like mingetty(8) will invoke login.

%package -n su
Summary: Assume a user's identity
Group: System/Base
PreReq: control

%description -n su
Su invokes the preferred shell of another user.  The identity of the new
user can be specified with the username argument.  The default username
is that of the local superuser (UID=0).

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p2
find -type f -print0 |
	xargs -r0 fgrep -lZ PAM_DATA_QUIET -- |
	xargs -r0 sed -i s/PAM_DATA_QUIET/PAM_DATA_SILENT/ --

%build
autoheader
autoconf
touch conf/.ignore_age

%if_enabled debug
%add_optflags -DDEBUG
%endif
%configure --without-pniam --without-pwdb --with-audit
make

%install
%if_with login
install -pD -m700 pamapps/login/login %buildroot/bin/login
install -pD -m644 pamapps/login/login.1 %buildroot%_man1dir/login.1
install -pD -m600 %_sourcedir/login.pamd %buildroot%_sysconfdir/pam.d/login
%endif #with login

%if_with su
install -pD -m700 pamapps/su/su %buildroot/bin/su
install -pD -m644 pamapps/su/su.1 %buildroot%_man1dir/su.1
install -pD -m600 %_sourcedir/su.pamd %buildroot%_sysconfdir/pam.d/su
install -pD -m755 %_sourcedir/su.control %buildroot%_controldir/su
%endif #with su

%pre -n su
%pre_control su

%post -n su
%post_control -s wheelonly su

%triggerpostun -n login -- util-linux < 2.11h-alt3
f=%_sysconfdir/pam.d/login
if [ ! -f "$f" ]; then
	if [ -f "$f".rpmsave ]; then
		cp -pf "$f".rpmsave "$f"
	elif [ -f "$f".rpmnew ]; then
		cp -pf "$f".rpmnew "$f"
	fi
fi

%triggerpostun -n su -- sh-utils < 2.0.11-alt2
f=%_sysconfdir/pam.d/su
if [ ! -f "$f" ]; then
	if [ -f "$f".rpmsave ]; then
		cp -pf "$f".rpmsave "$f"
	elif [ -f "$f".rpmnew ]; then
		cp -pf "$f".rpmnew "$f"
	fi
fi

%if_with login
%files -n login
/bin/login
%_man1dir/login.*
%config(noreplace) %_sysconfdir/pam.d/login
%doc Copyright Discussions
%endif #with login

%if_with su
%files -n su
%verify(not mode,group) /bin/su
%_man1dir/su.*
%config(noreplace) %verify(not size,md5,mtime) %_sysconfdir/pam.d/su
%config %_controldir/su
%doc Copyright Discussions
%endif #with su

%changelog
* Fri Jul 03 2020 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt36
- login: do not set PAM_RUSER and PAM_RHOST unnecessarily (closes: #38655).

* Mon Jan 16 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.60-alt35
- Fixed build with gcc 6 (dropped useless rcsid).

* Mon Dec 14 2015 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt34
- Fixed build with fresh glibc.

* Fri Aug 24 2012 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt33
- su: fixed build with fresh glibc.

* Mon Jul 16 2012 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt32
- login: reenabled GOODBYE_MESSAGE.

* Thu May 31 2012 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt31
- Made utmp_do_close_session() propagate write_wtmp() return value.
- Updated URL.

* Wed Dec 29 2010 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt30
- Fixed parameter passed to pam_end() call in the child process.

* Fri Jul 02 2010 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt29
- Rebuilt with libaudit.so.1.

* Wed Jun 23 2010 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt28
- /etc/pam.d/login: Changed to use common-login.

* Wed Dec 16 2009 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt27
- /etc/pam.d/login:
  Made pam_console.so fully optional.
  Added fully optional pam_ck_connector.so.

* Tue Apr 07 2009 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt26
- Acknowledged NMU.

* Thu Mar 12 2009 Anton Farygin <rider@altlinux.ru> 0.60-alt25.1
- NMU: added audit support to login
- NMU: added pam_loginuid to login.pam

* Wed Oct 18 2006 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt25
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Fri May 05 2006 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt24
- su: Do not ignore pam_acct_mgmt() return values except PAM_ACCT_EXPIRED
      and PAM_NEW_AUTHTOK_REQD even if executed by root.

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.60-alt23.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Tue Oct 04 2005 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt23
- Fixed build with new Linux-PAM.
- /etc/pam.d/login: moved pam_mail from auth to session control.

* Tue Jun 28 2005 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt22
- Enhanced build fix made in previous release.

* Sun Jan 16 2005 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt21
- Added help to control facility scripts.
- Removed verify checks for files controlled via control(8) facility.
- Fixed compilation issues detected by gcc-3.4.3.

* Sun Feb 08 2004 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt20
- In login and su, generate ut_id's consistently with
  libutempter and openssh (#3580).

* Sun Jan 18 2004 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt19
- Deal with compilation warnings generated by new gcc compiler.

* Tue Jun 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt18
- Fixed build with OpenPAM.
- Added Linux-PAM/OpenPAM multi-build support.

* Fri May 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt17
- PAM configuration policy enforcement.

* Thu Apr 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt16
- Do not compile passwd.
- Rearranged patches, to sync with 0.60-owl18.

* Sun Jan 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt15
- Removed build support for "passwd" from SimplePAMApps package.
- Replaced owl-su-no-tty and owl-alt-su-no-fail_delay with owl-su patch.
- Keep su at mode "restricted" in the package, but default it
  to "wheelonly" in %%post when the package is first installed.
  This avoids a race and fail-open behavior (Owl).

* Sun Oct 13 2002 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt14
- Added control support for su.

* Thu Jun 13 2002 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt13
- Setenv SHELL variable.

* Thu Mar 21 2002 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt12
- Fixed %triggerpostun scripts.

* Sun Mar 10 2002 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt11
- Pick the best match utmp entry to replace when ut_id's don't match (Owl).
- login: fixed pam_lastlog usage.

* Tue Dec 25 2001 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt10
- login:
  + changed pam_securetty control-flag from "requisite" to "required".
  + added pam_motd to the session stack.
  + fixed manpage.

* Fri Dec 14 2001 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt9
- Merged patches from Owl:
  * Mon Nov 19 2001 Solar Designer <solar@owl.openwall.com>
  - login: treat all PAM errors except PAM_NEW_AUTHTOK_REQD in the same way to
    reduce information leaks.
  - login: only chdir to the user's home directory after becoming the user.
  - su: don't set a fail delay (it made very little sense and may be enabled
    from within a PAM module anyway).

* Fri Oct 05 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.60-alt8
- login, su:
  + reset default PATH only for login sessions;
  + propagate DISPLAY environment variable for login sessions.

* Wed Sep 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.60-alt7
- login: requires latest pam_console for proper function.

* Tue Sep 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.60-alt6
- login, su: dropped ttyname patch (conflicts with utmp code).
- login, su: build_shell_args: strip argv[0] value (compatibility).

* Thu Sep 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.60-alt5
- set_user_credentials: add /usr/local/{s,}bin to PATH.

* Mon Sep 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.60-alt4
- login, su: set_user_credentials: set PATH variable depending on uid.

* Tue Sep 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.60-alt3
- su: added -s option for superuser (compatibility).
- su: -l option doesn't obsolete -c option.

* Mon Sep 10 2001 Dmitry V. Levin <ldv@fandra.org> 0.60-alt2
- login: disabled goodbye message and updated pam config to mimic
  traditional behaviour.
- Added %%post scripts to ease migration.

* Tue Aug 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.60-alt1
- ALT adaptions.
- Strip "/dev/" prefix from ttyname when pam_set_item( PAM_TTY ).
- Packaged login, passwd, su as separate independent subpackages.
- Enable build of login and su.

* Sun Apr 01 2001 Solar Designer <solar@owl.openwall.com>
- Use pam_limits with login and su.
- passwd: line-buffer stdout.
- passwd: don't require an utmp entry even when run on a tty.

* Mon Mar 19 2001 Solar Designer <solar@owl.openwall.com>
- passwd: don't require a tty.
- passwd.pam and su.pam: "nodelay" for pam_pwdb.

* Wed Dec 20 2000 Solar Designer <solar@owl.openwall.com>
- Use pam_mktemp.

* Sun Oct 29 2000 Solar Designer <solar@owl.openwall.com>
- su: don't require that the tty can be determined when started by root.
- su: don't require that getlogin() works to set PAM_RUSER.
- #include <stdarg.h> in su.c (was needed, but missing).

* Fri Sep 22 2000 Solar Designer <solar@owl.openwall.com>
- Make use of the new pam_passwdqc option: min=99,... -> min=disabled,...

* Sat Sep 16 2000 Solar Designer <solar@owl.openwall.com>
- Use RPM_OPT_FLAGS correctly.

* Wed Aug 23 2000 Solar Designer <solar@owl.openwall.com>
- %%config(noreplace) for /etc/pam.d files.

* Fri Aug 11 2000 Solar Designer <solar@owl.openwall.com>
- Added owl-control support for su and passwd.

* Sun Jul 09 2000 Solar Designer <solar@owl.openwall.com>
- Imported this spec file from SimplePAMApps-0.56-2.src.rpm and changed it
so heavily that there isn't much left.
- Added a bugfix patch for passwd and a bugfix and security patch for
login.  (In fact, login needs to be re-coded.)
- login can now obtain the username from LOGNAME when started as root (not
SUID), to be used by getty's.
