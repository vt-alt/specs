Name: sudo
Version: 1.8.28
Release: alt1
Epoch: 1

Summary: Allows command execution as another user
License: BSD-style
Group: System/Base
Url: http://www.courtesan.com/sudo/

# ftp://ftp.courtesan.com/pub/sudo/sudo-%version.tar.gz
Source: sudo-%version.tar

Patch: sudo-%version-alt.patch

PreReq: control
Requires: vitmp
Provides: %_sysconfdir/sudoers.d

# Automatically added by buildreq on Wed Apr 09 2003
BuildRequires: flex libpam-devel perl-podlators
# Due check of man pages type
BuildRequires: /usr/bin/nroff

%define _libexecdir %_prefix/libexec/sudo

Summary(ru_RU.UTF-8): Запускает команды в контексте другого пользователя

%description
Sudo is a program designed to allow a sysadmin to give limited root
privileges to users and log root activity.  The basic philosophy is
to give as few privileges as possible but still allow people to get
their work done.

%description -l ru_RU.UTF-8
Sudo - программа, разработанная в помощь системному администратору
делегировать те или иные привилегированные ресурсы пользователям,
с ведением протокола их деятельности.  Основная идея - делегировать
как можно меньше прав, но ровно столько, сколько необходимо для
решения поставленных задач.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %epoch:%version-%release
BuildArch: noarch

%description devel
The %name-devel package contains header files developing sudo
plugins that use %name.

%description devel -l ru_RU.UTF-8
Пакет %name-devel содержит заголовочные файлы для разработки расширений
для програмы %name.

%prep
%setup
%patch -p1

%build
./autogen.sh
export ac_cv_prog_NROFFPROG=nroff
configure_options='
--with-logging=syslog
--with-logfac=authpriv
--enable-shell-sets-home
--enable-log-host
--disable-rpath
--with-pam
--with-ignore-dot
--with-env-editor
--with-tty-tickets
--with-sudoers-mode=0400
--with-editor=/bin/vitmp
--with-sendmail=/usr/sbin/sendmail
--with-sssd
--docdir=%_datadir/doc/%name-%version
--with-plugindir=%_libdir/sudo
--libexecdir=%_libdir
--with-secure-path=/sbin:/usr/sbin:/usr/local/sbin:/bin:/usr/bin:/usr/local/bin'

%configure $configure_options --with-passprompt='[sudo] password for %%u:'
%make_build

%install
%makeinstall_std INSTALL_OWNER=
install -pD -m600 examples/pam.conf %buildroot%_sysconfdir/pam.d/sudo
mkdir -p %buildroot%_sysconfdir/sudoers.d
chmod u+rwx %buildroot%prefix/*bin/*
install -pD -m755 sudo.control %buildroot/etc/control.d/facilities/sudo
install -pD -m755 sudoers.control %buildroot/etc/control.d/facilities/sudoers
install -pD -m755 sudoreplay.control %buildroot/etc/control.d/facilities/sudoreplay
install -pD -m755 sudowheel.control %buildroot/etc/control.d/facilities/sudowheel
bzip2 -9 %buildroot%_datadir/doc/%name-%version/ChangeLog

%find_lang sudo
%find_lang sudoers

cat sudo.lang sudoers.lang > sudo_all.lang
rm sudo.lang sudoers.lang
rm -f %buildroot%_libdir/sudo/*.la %buildroot%_libdir/*.so

mv %buildroot%_sysconfdir/sudoers.dist %buildroot%_datadir/doc/%name-%version/

%pre
%pre_control sudo
%pre_control sudoers
if [ -f "%_controldir/sudoreplay" ]; then
    %pre_control sudoreplay
fi
if [ -f "%_controldir/sudowheel" ]; then
    %pre_control sudowheel
fi

%post
%post_control -s wheelonly sudo
%post_control -s strict sudoers
if [ ! -f "/var/run/control/sudoreplay" ]; then
    echo wheelonly > "/var/run/control/sudoreplay"
fi
%post_control -s wheelonly sudoreplay
if [ ! -f "/var/run/control/sudowheel" ]; then
    if [ "$1" -gt 1 ]; then
        %pre_control sudowheel
    else
        echo disabled > "/var/run/control/sudowheel"
    fi
fi
%post_control -s disabled sudowheel

%triggerpostun -- %name < 1:1.8.0
cp -a %_sysconfdir/sudoers %_sysconfdir/sudoers.rpmsave
if ! grep -q '^#includedir %_sysconfdir/sudoers.d$' %_sysconfdir/sudoers; then
    if [ -d %_sysconfdir/sudoers.d ]; then
        echo "WARNING: %_sysconfdir/sudoers.d directory no longer supported indirectly"
        echo "Update %_sysconfdir/sudoers with next line:"
        echo "#includedir %_sysconfdir/sudoers.d"
        echo

        echo >>%_sysconfdir/sudoers
        echo "# Automatically updates by rpm:" >>%_sysconfdir/sudoers
        echo "#includedir %_sysconfdir/sudoers.d" >>%_sysconfdir/sudoers
    fi
fi
if ! grep -q '^#includedir %_sysconfdir/sudo.d$' %_sysconfdir/sudoers; then
    if [ -d %_sysconfdir/sudo.d ]; then
        echo "WARNING: %_sysconfdir/sudo.d compat directory no longer supported indirectly"

        if [ "$(ls -A %_sysconfdir/sudo.d)" ]; then
            echo "Update %_sysconfdir/sudoers with next line:"
            echo "#includedir %_sysconfdir/sudo.d"

            echo >>%_sysconfdir/sudoers
            echo "# Automatically updates by rpm:" >>%_sysconfdir/sudoers
            echo "#includedir %_sysconfdir/sudo.d" >>%_sysconfdir/sudoers
        fi

        echo
    fi
fi

%files -f sudo_all.lang
%config %_controldir/sudo*
%attr(400,root,root) %config(noreplace) %_sysconfdir/sudoers
%attr(600,root,root) %config(noreplace) %_sysconfdir/pam.d/sudo
%_bindir/sudoedit
%dir %_libdir/sudo
%_libdir/*.so.*
%_libdir/sudo/*.so*
%attr(700,root,root) %_bindir/sudo
%attr(700,root,root) %_bindir/sudoreplay
%attr(755,root,root) %_sbindir/visudo
%attr(700,root,root) %_sysconfdir/sudoers.d
%_bindir/cvtsudoers
%_mandir/man?/*
%exclude %_man8dir/sudo_plugin.8*
%_datadir/doc/%name-%version/

%files devel
%doc plugins/sample/sample_plugin.c
%_includedir/sudo_plugin.h
%_man8dir/sudo_plugin.8*

%changelog
* Tue Oct 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 1:1.8.28-alt1
- Update to autumn security release (closes: 37334)
- Code execution with euid==0 in rare box configurations (fixes: CVE-2019-14287)
- Fix post script for sudowheel control in case of upgrade in not default state

* Thu Apr 11 2019 Evgeny Sinelnikov <sin@altlinux.org> 1:1.8.27-alt1
- Update to last winter release

* Fri Dec 07 2018 Evgeny Sinelnikov <sin@altlinux.org> 1:1.8.26-alt1
- Update to last autumn release
- Fix post script for sudowheel control (closes: 35611)

* Thu Nov 08 2018 Evgeny Sinelnikov <sin@altlinux.org> 1:1.8.25p1-alt2
- Reapply replace libsudo_util.so to libexecdir (avoid rpath in binaries)
- Set sudowheel control with rule "ALL=(ALL) ALL" for wheel users disabled
  by default (closes: 18344)

* Tue Nov 06 2018 Evgeny Sinelnikov <sin@altlinux.org> 1:1.8.25p1-alt1
- Update to latest release
- Disable ubt macros due binary package identity change
- Replace libsudo_util.so to libexecdir
- Add new cvtsudoers utility

* Fri Apr 27 2018 Evgeny Sinelnikov <sin@altlinux.org> 1:1.8.22-alt1%ubt
- Update to latest winter release
- Add sudowheel control with rule "ALL=(ALL) ALL" for wheel users enabled
  by default (closes: 18344)

* Thu Nov 23 2017 Evgeny Sinelnikov <sin@altlinux.org> 1:1.8.21p2-alt1%ubt
- Update to latest autumn release

* Fri Jun 02 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.20p2-alt1%ubt
- Update to first summer security release

* Wed May 31 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.20p1-alt1%ubt
- Update to spring security release ((Fixes: CVE-2017-1000367)

* Mon May 29 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.20-alt1%ubt
- Update to latest spring release

* Tue Jan 10 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.19p1-alt6%ubt
- Add compatibility trigger for /etc/sudoers.d and /etc/sudo.d
- Avoid sudoreplay pre and post control warnings

* Mon Jan 02 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.19p1-alt5%ubt
- Add warning if /etc/sudo.d directory exixsts

* Wed Dec 28 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.19p1-alt4%ubt
- Disable sudo rule for root by default

* Tue Dec 27 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.19p1-alt3%ubt
- Fixed relaxed control rule for sudoers

* Mon Dec 26 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.19p1-alt2%ubt
- Build without *.la files in modules directory

* Wed Dec 21 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.19p1-alt1%ubt
- Updated to last stable release 1.8.19p1 with sssd features

* Thu Aug 04 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.17p1-alt2
- Fixed new sudoers template with sudoers.control settings

* Thu Jul 28 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.17p1-alt1
- Updated to last stable release 1.8.17p1

* Tue Jun 30 2015 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.13-alt1
- Updated to last stable release 1.8.13

* Mon Jan 27 2014 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.9p4-alt1
- Updated to last stable release 1.8.9p4

* Mon Oct 07 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.8-alt1
- Updated to new relrease 1.8.8

* Fri Oct 04 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.6p8-alt1
- Updated to 1.8.6p8

* Tue Feb 12 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.6p6-alt1
- Updated to 1.8.6p6

* Wed Jan 16 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.6p4-alt1
- Updated to 1.8.6p4

* Wed Dec 19 2012 Evgeny Sinelnikov <sin@altlinux.ru> 1:1.8.6p3-alt1
- Updated to 1.8.6p3
- Enabled /etc/sudoers.d by default (for new installations)
- Added sudo-devel package for plugin development

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.6.8p12-alt12
- Dropped /etc/sudo.d from package and Provides, handling left for
  compatibility.

* Thu Jul 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.6.8p12-alt11
- Implemented /etc/sudoers.d support to provide upstream-compatibility
  /etc/sudo.d support left for backward compatibility.

* Thu Jul 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt10
- Fixed generation of man pages (by george@; closes: #27479).

* Thu May 24 2012 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt9
- Relocated sudo timestamp directory: /var/run/sudo -> /var/lib/sudo.

* Tue Jun 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt8
- Backported upstream fix for CVE-2010-1163 (env_reset, ignore_dot and
  secure_path sudoers options all had to be explicitly disabled
  to make an attack possible).
- Backported upstream fix for CVE-2010-1646 (env_reset sudoers option
  had to be explicitly disabled to make an attack possible).

* Tue Feb 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt7
- Backported upstream fix for CVE-2010-0426 (a flaw in sudoedit could
  give a user with permission to run sudoedit the ability to run
  arbitrary commands; env_reset sudoers option had to be
  explicitly disabled to make an attack possible).

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt6
- Fixed build with fresh libtool.

* Mon Jan 21 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt5
- Documented that set_home is on by default due to --enable-shell-sets-home.
- Configured less confusing default password prompt (#13719).
- Fixed build with autoconf-2.61.

* Sat Aug 04 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt4
- Fixed typo in configure check (george, #12449, #12462).
- sudoers (#11753):
  + Added DISPLAY and XAUTHORITY to env_keep for "xgrp" group members.
  + Added "!env_reset" example.
  + Added sudoers environment control.

* Tue May 22 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt3
- Forced manpage generation from .pod files.
- sudoers: Added "DISPLAY" to env_keep.

* Sat May 05 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt2
- Reverted change to requiretty default value.
- Resurrected tgetpass fix from 1.6.6-alt3.

* Tue Apr 17 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt1
- Updated to 1.6.8p12 with backports from HEAD.
- Enabled env_reset, requiretty and tty_tickets options by default.

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1:1.6.7p5-alt6.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Fri Aug 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt6
- Added system logger initialization, removed closelog() calls.

* Tue Jun 21 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt5
- Backported upstream fix so a sudoers entry with sudo ALL no longer
  overwrites the value of safe_cmnd (CAN-2005-1993).

* Fri Nov 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt4
- Backported upstream fix that restricts exporting of shell functions
  and CDPATH shell variable (CAN-2004-1051).
- Added help to control.

* Thu Mar 11 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt3
- Changed "listpw" default value from "any" to "all".

* Wed Mar 10 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt2
- Fixed build with fresh autotools.

* Tue Jul 29 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt1
- Updated to 1.6.7p5.

* Sat May 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p2-alt2
- PAM configuration policy enforcement.

* Tue Apr 08 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p2-alt1
- Updated to 1.6.7p2, updated patches.
- Enable setting $HOME to target user in shell mode.
- Keep sudo at mode "restricted" in the package, but default it
  to "wheelonly" in %post when the package is first installed.
  This avoids a race and fail-open behavior (like in su package).

* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.6-alt4
- Added control support for sudo.

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.6-alt3
- tgetpass: The /dev/tty _must_ be opened for reading/writing unless
  requested to use stdin/stderr.

* Fri May 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.6-alt2
- Set default visudo(8) editor to vitmp(1).

* Mon May 13 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.6-alt1
- 1.6.6

* Fri Apr 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5p2-alt3
- Applied patch from Tom Parker.

* Mon Jan 28 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5p2-alt2
- Added %_sysconfdir/sudo.d

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5p2-alt1
- 1.6.5p2.
- Built with --disable-saved-ids.

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5p1-alt2
- Rebuilt with bison-1.31-alt2.

* Mon Jan 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5p1-alt1
- 1.6.5p1.

* Thu Jan 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5-alt1
- 1.6.5 final.

* Tue Jan 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.4-alt2
- Fixed nasty typo in description.

* Mon Jan 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.4-alt1
- 1.6.4 final.

* Sun Jan 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.4-alt0.1rc4
- 1.6.4rc4, which fixes set_perms_posix problem.

* Sat Jan 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.4-alt0.1rc3
- 1.6.4rc3, updated patches.
- Explicitly set sudoers mode to 0400.
- Disabled broken set_perms_posix introduced in new version.
- Cleaned up list of linked libraries.

* Sun Apr 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.6.3p7-ipl3mdk
- Fixed progname usage.
- Fixed SECURE_PATH.
- Enabled: --with-secure-path --with-env-editor --with-editor=/bin/vi.
- Implemented optional sudoers file for visudo.
- implemented sudoers lookup in %_sysconfdir/sudo.d directory.

* Mon Mar 05 2001 Dmitry V. Levin <ldv@fandra.org> 1.6.3p7-ipl2mdk
- Corrected license information.

* Sat Mar 03 2001 Dmitry V. Levin <ldv@fandra.org> 1.6.3p7-ipl1mdk
- 1.6.3p7

* Tue Feb 20 2001 Dmitry V. Levin <ldv@fandra.org> 1.6.3p6-ipl1mdk
- 1.6.3p6

* Wed Feb 14 2001 Dmitry V. Levin <ldv@fandra.org> 1.6.3p5-ipl5mdk
- Added set of PAM_TTY.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p5-ipl4mdk
- Commented out translations in specfile for a while.

* Fri Oct 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p5-ipl3mdk
- Updated pam configuration.
- Changed syslog facility to log with from local2 to authpriv.

* Fri Sep 01 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p5-ipl2mdk
- Russian translations.

* Mon Aug 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p5-ipl1mdk
- 1.6.3p5

* Wed Jun 07 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p4-ipl1mdk
- 1.6.3p4

* Mon May 15 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p3-ipl1mdk
- 1.6.3p3

* Thu May 04 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Fri Apr 07 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.6.2p2-3mdk
- Set /etc/sudoers as 0440.

* Fri Apr 7 2000 Denis Havlik <denis@mandrakesoft.com> 1.6.2p2-2mdk
- Group: System/Base
- fixed config files

* Mon Feb 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.6.2p2-1mdk
- 1.62p2.

* Wed Feb  9 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.6.2p1-1mdk
- 1.6.2p1.
- specs teak.

* Thu Jul 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Fri Jun  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [sudo-1.5.9p3-1]
- Updated to version 1.5.9p3
- Changed RPM name from cu-sudo tp sudo.

* Fri Jun  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [cu-sudo-1.5.9p2-1]
- Added dir /var/run/sudo to file list.
- Added --enable-log-host --disable-log-wrap to configure.
- Added --with-logging=file to configure.
- Added logrotate.d file to rotate /var/log/sudo.log monthly.

* Fri Jun  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [cu-sudo-1.5.9p2-1]
- Initial RPM build.
- Installing sample pam file.
