Name: service
Version: 0.5.31
Release: alt1

Summary: The service start/stop scripts
License: GPLv2+
Group: System/Base
Url: http://git.altlinux.org/people/ldv/packages/service.git

Source: %name-%version.tar
Source1: list.functions-compat

Requires: /bin/tput
# due to start-stop-daemon (Conflicts: SysVinit < 0:2.85-alt5)
Requires: sysvinit-utils
Conflicts: initscripts < 1:5.49.1-alt1
# due to RPM_INSTALL_ARG1 support:
Conflicts: rpm < 0:4.0.4-alt0.7
# due to %_sysconfdir/rc?.d and %_sysconfdir/rc.d/rc?.d
Conflicts: startup < 0.0.2-alt1
# due to run-parts
Conflicts: crontabs < 0:1.8-alt1
# due to start-stop-daemon.8
Conflicts: dpkg <= 0:1.6.15-alt3

%global __find_provides_filter fgrep -x -v -e "$(/usr/lib/rpm/shell.prov %buildroot%_initdir/.provides.sh.compat)"

# This is required for shell function provides autogeneration.
BuildPreReq: rpm-build >= 4.0.4-alt16

BuildRequires: help2man, libpopt-devel, libshell

%description
This package contains the basic system scripts used to
start and stop services.

%prep
%setup

%build
make -C src VERSION=%version

%install
%makeinstall_std -C src
install -p -m755 service %buildroot/sbin/
install -p -m644 service.8 %buildroot%_man8dir/
mkdir -p %buildroot{/bin,%_sbindir}
install -p -m755 run-parts %buildroot/bin/
install -p -m755 post_service preun_service %buildroot%_sbindir/
install -p -m755 rc.d/init.d/* %buildroot%_initdir/
chmod a-x %buildroot%_initdir/template

# This is a LSB compatibility symlink.  We hope that some day
# the actual files will be here instead of symlinks.
ln -s rc.d/init.d %buildroot%_sysconfdir/

# This is a LSB compatibility symlink.  We hope that some day
# the actual files will be here instead of symlinks.
for i in `seq 0 6`; do
        ln -s rc.d/rc$i.d %buildroot%_sysconfdir/rc$i.d
done

mkdir -p %buildroot%_sysconfdir/rc.d/rc{0,1,2,3,4,5,6}.d
mkdir -p %buildroot%_sysconfdir/sysconfig/limits.d
mkdir -p %buildroot/usr/libexec/service/legacy-actions

# Generate shell functions provides list.
export LC_COLLATE=C

print_function_names()
{
        sed -ne 's/^\([A-Za-z][A-Za-z_0-9]*[[:space:]]*\)()$/\1/pg' "$1"
}

for f in %buildroot%_initdir/*; do
        [ -x "$f" ] || continue
        print_function_names "$f"
done | sort -u \
>%buildroot%_initdir/.list.functions

(
        echo '# shell functions provides list'
        comm -1 -3 \
        %buildroot%_initdir/.list.functions \
        %SOURCE1
) >%buildroot%_initdir/.provides.sh.compat

(
        echo '# shell functions provides list'
        sort -u \
        %buildroot%_initdir/.list.functions \
        %SOURCE1
) >%buildroot%_initdir/.provides.sh
# In other pkgs, Requires will be generated for all functions listed here.

%triggerpostun -- initscripts < 1:5.49.1-alt1
f=%_sysconfdir/initlog.conf
if [ ! -f "$f" ]; then
        if [ -f "$f".rpmsave ]; then
                cp -pf "$f".rpmsave "$f"
        elif [ -f "$f".rpmnew ]; then
                cp -pf "$f".rpmnew "$f"
        fi
fi

%files
%exclude %_initdir/.provides.sh.compat
/sbin/*
/bin/*
%_sbindir/*
%_mandir/man?/*
%_sysconfdir/init.d
%_sysconfdir/rc?.d
%defattr(644,root,root,755)
%_sysconfdir/sysconfig/limits.d
/usr/libexec/service/
%config %_sysconfdir/rc.d
%config(noreplace) %_sysconfdir/initlog.conf
%config(noreplace) %_sysconfdir/sysconfig/limits

%changelog
* Thu Dec 26 2019 Dmitry V. Levin <ldv@altlinux.org> 0.5.31-alt1
- {post,preun}_service: added support of non-service systemd units (closes: #35388).

* Thu Dec 26 2019 Dmitry V. Levin <ldv@altlinux.org> 0.5.30-alt1
- service: added support of non-service systemd units (closes: #35388).

* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.29-alt1.1
- NMU: added URL

* Thu Mar 01 2018 Ivan Zakharyaschev <imz@altlinux.org> 0.5.29-alt1
- Fixed the typo in su invocation introduced in 0.5.28-alt1 (ALT#34500).

* Wed Dec 27 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.5.28-alt1
- use "start-stop-daemon --chuid USER" instead of "su"
  if WITHOUT_RC_COMPAT >= 2 or --make-pidfile is used, which
  is better because the saved PID belongs to the started program then
  (rather than "su"), but worse -- because PAM limits are not set.

* Thu Jul 27 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.5.27-alt1
- functions: new *warning() funcs (as in Fedora).
- Drop functions-compat from our pkg; it'll be external.
- The list of functions-compat saved from initscripts-compat-fedora-9.72-alt1.

* Tue Jul 25 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.5.26-alt2
- Unprovide functions defined only in functions-compat, but still
  make the corresponding Requires be generated in other pkgs.
- functions: innocent checkpid() copied from functions-compat,
  because there are some scripts in Sisyphus which use it.

* Tue Sep 09 2014 Dmitry V. Levin <ldv@altlinux.org> 0.5.26-alt1
- preun_service: added chkconfig call in systemd case (closes: #30165).
- service: added legacy-actions support (closes: #29925).
- sd_booted: synced systemd check with libsystemd.

* Mon May 12 2014 Dmitry V. Levin <ldv@altlinux.org> 0.5.25-alt1
- service: use is-active as a closer systemd equivalent of
  sysvinit status (closes: #30034).

* Thu Feb 28 2013 Dmitry V. Levin <ldv@altlinux.org> 0.5.24-alt1
- Implemented systemd-only service support in {post,preun}_service
  (closes: #27390) and native support of systemd services.
  Due to systemctl limitations, when systemd is active,
  post_service will no longer be able to enable sysv-only services.
- Added /sbin/sd_booted utility.

* Tue Jul 24 2012 Dmitry V. Levin <ldv@altlinux.org> 0.5.23-alt1
- Fixed build with new gcc.

* Thu Jan 26 2012 Dmitry V. Levin <ldv@altlinux.org> 0.5.22-alt1
- start-stop-daemon: implemented support of /proc/pid/exe pointing
  to names with " (deleted)" prefix.
- minilogd: changed to create /dev/log socket world writable
  (closes: #12564).
- init.d/functions (UnmountFilesystems): implemented mountpoints
  decoding to match getmntent(3) behaviour (closes: #17118).
- init.d/functions (start_daemon):
  + added --background option (closes: #26529);
  + added --check option.
- service.8: imported from Fedora (closes: #22166).

* Thu Mar 17 2011 Dmitry V. Levin <ldv@altlinux.org> 0.5.21-alt1
- service: added systemd support (closes: #24989).

* Fri Dec 03 2010 Dmitry V. Levin <ldv@altlinux.org> 0.5.20-alt1
- getkey: Fixed signal handling.
- init.d/{functions,outformat}: Made it usable with sh -eu
  (by Alexey Froloff; closes: #22159).
- start-stop-daemon: Backported some options from Debian
  (by Vitaly Kuznetsov; closes: #24683).

* Fri Mar 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.5.19-alt2
- move run-parts to /bin

* Thu Jan 29 2009 Dmitry V. Levin <ldv@altlinux.org> 0.5.19-alt1
- limited: Set limits in proper order (legion@; closes: #18436).

* Sun Nov 16 2008 Dmitry V. Levin <ldv@altlinux.org> 0.5.18-alt1
- functions-compat: Fixed regression (legion@; closes: #17900).

* Wed Nov 12 2008 Dmitry V. Levin <ldv@altlinux.org> 0.5.17-alt1
- Added new utility, /sbin/limited, for running programs with limited
  resources, and use it in functions/start_daemon (legion@, me).

* Tue Oct 28 2008 Dmitry V. Levin <ldv@altlinux.org> 0.5.16-alt1
- init.d/functions (start_daemon): Added --retry option (closes: #15044).

* Fri Apr 25 2008 Dmitry V. Levin <ldv@altlinux.org> 0.5.15-alt1
- Dropped explicit pathname provides.
- Require sysvinit-utils instead of versioned conflict with old SysVinit.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 0.5.14-alt1
- init.d/template: Disabled service by default (#11202).

* Tue Feb 20 2007 Dmitry V. Levin <ldv@altlinux.org> 0.5.13-alt1
- minilogd: Do not check atime of /dev/log to detect syslogd
  startup (vsu@, patch from Mandriva).

* Sun Oct 15 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.12-alt1
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.
- post_service: Call chkconfig resetpriorities on upgrade (#9588).

* Sat Sep 23 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.11-alt1
- start-stop-daemon --exec:
  Handle /proc/%%d/exe names with "(deleted) " prefix.

* Mon May 15 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.10-alt1
- Fixed build with gcc-4.1.0.

* Mon Sep 05 2005 Dmitry V. Levin <ldv@altlinux.org> 0.5.9-alt1
- functions/start_daemon:
  + fixed --make-pidfile option (#7725).
- functions/{start_daemon,stop_daemon,status}:
  + added --displayname option (#5743,#7743).

* Mon Mar 21 2005 Dmitry V. Levin <ldv@altlinux.org> 0.5.8-alt1
- functions/{splash_init,splash_update}: new functions (#6275).

* Wed Mar 09 2005 Dmitry V. Levin <ldv@altlinux.org> 0.5.7-alt1
- service: pass all parameters to services (#5080).
- functions/{start_daemon,stop_daemon,status}:
  + honor --name during BASENAME calculation (#5743).
- functions/UnmountFilesystems:
  + if BOOTUP=verbose, display all processes
    which use busy mointpoints (#6068);
  + pass -l option to umount (#6230).

* Sat Sep 04 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.6-alt1
- functions/status: implemented --lockfile option (#5086).

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.5-alt1
- functions/confirm: handle default value (#3085).

* Sun Jun 27 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.4-alt1
- functions/stop_daemon:
  + when sending HUP, do not remove lockfile to workaround
    bugs in third party rc scripts.
- functions/start_daemon:
  + implemented --make-pidfile option (#4231).

* Wed Jan 21 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.3-alt1
- service: removed support for dangerous --status-all option.
- functions-compat: hide pidof to avoid sysvinit dependency.

* Tue Aug 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.2-alt1
- functions:
  + start_daemon/stop_daemon: fixed output appearance (#0002860).

* Thu Aug 07 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- functions:
  + failure: fixed typo (#0002815).

* Tue Jun 03 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5-alt1
- functions:
  + start_daemon: fixed --name option processing;
  + echo_*,action: fixed echoing.

* Tue May 27 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- functions:
  + added --name support;
  + better error diagnostics;
  + command substitution cleanup.
- functions, start-stop-daemon:
  + added --user-fallback-to-name support,
    should cover most of #0002615.

* Thu May 22 2003 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- initlog:
  + fixed arg check (#0002417);
  + fixed get_facility/get_priority (#0002418).
- initlog.conf:
  commented out facility/priority settings.
- All this initlog stuff is far from clean.
  Please anybody rewrite it someday.

* Wed May 21 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- functions: fixed options parsing in stop_daemon().

* Mon May 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Imported new start-stop-daemon from dpkg-1.10.9/utils/,
  with our fixes merged from SysVinit-2.85-alt4's version.
- functions: fix action() return code.
- functions-compat: more RH compatibility.
- Added template rc script.

* Fri Apr 25 2003 Dmitry V. Levin <ldv@altlinux.org> 0.0.3-alt1
- functions:
  + added start_daemon and stop_daemon from Owl;
  + added msg_* functions from PLD for convenience;
  + moved daemon/killproc/... stuff to functions-compat.
- Added %_initdir/.provides.sh file.
- run-parts: moved from crontabs to this package.

* Wed Apr 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.0.2-alt1
- Relocated %_sysconfdir/rc?.d and %_sysconfdir/rc.d/rc?.d
  from startup package to this package.

* Mon Apr 21 2003 Dmitry V. Levin <ldv@altlinux.org> 0.0.1-alt1
- Removed all but service start/stop scripts and packaged them separately.
- New programs: post_service and preun_service.
- functions: replaced status() implementation with ssd-based one
  from owl-startup.

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 5.49-ipl54mdk
- %_initdir/sound: don't sort aliases in LoadModule (#0001802).
- %_initdir/clock: test $HWCLOCK_ADJUST also for "true" value (#0002351).
- %_initdir/functions:
  + fixed check logic in daemon() a bit (#0002407).
  + fixed return code in killproc() (#0002412).
- %_initdir/outformat: check argumnets being passed to tput (#0002450).
- /etc/sysctl.conf:
  + set "net.ipv4.icmp_echo_ignore_broadcasts = 1" by default (#0002472);
  + added comments from Owl's sysctl.conf file.
- usernetctl: support variable definitions quoted with single quotes.
