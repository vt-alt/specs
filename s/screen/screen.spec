Name: screen
Version: 4.6.2
Release: alt3.p9.1

Summary: A screen manager that supports multiple sessions on one terminal
License: GPLv2+
Group: Terminals
Url: http://www.gnu.org/software/screen/

# git://git.savannah.gnu.org/screen.git
# git://git.altlinux.org/gears/s/screen.git
Source: screen-%version-%release.tar

Requires(post): libutempter >= 1.0.6, pam_tcb >= 0.9.7.1, coreutils

BuildPreReq: libutempter-devel >= 1.0.6

# Automatically added by buildreq on Mon Jan 25 2016
# optimized out: libpam-devel libtinfo-devel pam0_userpass perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-unicore xz
BuildRequires: libncurses-devel libutempter-devel makeinfo pam_userpass-devel

%description
The screen utility allows you to run interactive text-mode programs
(such as login shells) even if it is not possible to control them
interactively all the time (for example, because you are limited by
the way of access to a remote machine.)

For instance, you can do several interactive tasks on the same
physical terminal (a remote shell session) by switching from one virtual
terminal to another with the help of screen utility installed on the
remote machine. Another option would be running a program that needs a
terminal without attaching it to any physical terminal at all
(its start may be scheduled in crontab, or you may want to detach it
when you break the connection to the remote machine).

Install the screen package if you may need to use virtual terminals
managed by the screen utility.

%prep
%setup -q -n screen-%version-%release

%build
pushd src
%autoreconf
%add_optflags -D_GNU_SOURCE
%if_enabled debug
%add_optflags -DDEBUG
%endif
%configure \
	--with-sys-screenrc=/etc/screenrc \
	--with-socket-dir=/var/run/screen \
	--enable-pam \
	--enable-telnet \
	--enable-colors256 \
	--enable-rxvt_osc \
	#

popd

%make_build -C src CFLAGS="%optflags"
%make_build -C src/doc screen.info
xz -kf src/doc/*.ps

%install
%makeinstall_std -C src

pushd %buildroot%_bindir
	rm -f screen.old screen
	mv screen-%version screen
popd

install -pD -m644 alt/screenrc %buildroot/etc/screenrc
install -pD -m644 alt/screencap %buildroot/etc/screencap

install -pD -m644 alt/screen.pamd %buildroot/etc/pam.d/screen

mkdir -p %buildroot{/var/run/screen,%_tmpfilesdir}
echo 'd /var/run/screen 0775 root screen' > %buildroot%_tmpfilesdir/screen.conf

mkdir -p %buildroot%_libexecdir/screen
touch %buildroot%_libexecdir/screen/{tcb_chkpwd,utempter}

%pre
/usr/sbin/groupadd -r -f screen

%post
ln -f %_libexecdir/chkpwd/tcb_chkpwd %_libexecdir/screen/
ln -f %_libexecdir/utempter/utempter %_libexecdir/screen/

%preun
if [ $1 -eq 0 ]; then
	rm -f %_libexecdir/screen/{tcb_chkpwd,utempter}
fi

%triggerin -- pam_tcb >= 0.9.7.1
ln -f %_libexecdir/chkpwd/tcb_chkpwd %_libexecdir/screen/

%triggerin -- libutempter >= 1.0.6
ln -f %_libexecdir/utempter/utempter %_libexecdir/screen/

%files
%attr(2711,root,screen) %_bindir/screen
%attr(710,root,screen) %dir %_libexecdir/screen
%attr(2711,root,shadow) %ghost %_libexecdir/screen/tcb_chkpwd
%attr(2711,root,utmp) %ghost %_libexecdir/screen/utempter
%attr(775,root,screen) %dir /var/run/screen/

%_datadir/screen
%_man1dir/screen.*
%_infodir/*.info*
%config(noreplace) /etc/screenrc
%config(noreplace) /etc/screencap
%config(noreplace) /etc/pam.d/screen
%_tmpfilesdir/screen.conf

%doc src/etc/*screenrc
%doc src/NEWS src/README src/FAQ src/doc/README.DOTSCREEN src/doc/*.ps.*

%changelog
* Wed Jan 20 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.6.2-alt3.p9.1
- Backported upstream commits (fixes CVE-2020-9366).

* Fri Jun 28 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.6.2-alt2
- Moved tmpfiles.d(5) config file to %%_tmpfilesdir.

* Tue Apr 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.6.2-alt1
- Updated to v.4.6.2 (ALT#36357).

* Tue Jul 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.6.1-alt1
- Updated to v.4.6.1.

* Thu Mar 09 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.5.1-alt1
- Updated to v.4.5.1.

* Mon Jan 25 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.3-alt12
- Added BR: makeinfo.

* Thu Sep 03 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.3-alt11
- Fixed CVE-2015-6806.

* Wed Feb 27 2013 Fr. Br. George <george@altlinux.ru> 4.0.3-alt10.1
- Rebuild with -Werror removed

* Mon Jul 16 2012 Dmitry V. Levin <ldv@altlinux.org> 4.0.3-alt10
- Fixed build with gcc 4.6.

* Thu Dec 01 2011 Dmitry V. Levin <ldv@altlinux.org> 4.0.3-alt9
- Added a %%preun script removing hardlinks created in %%post script.
- Moved screen sockets to /var/run/screen/ (closes: #25106).

* Mon Nov 08 2010 Dmitry V. Levin <ldv@altlinux.org> 4.0.3-alt8
- Fixed a bug uncovered by gcc 4.5.

* Fri Sep 17 2010 Dmitry V. Levin <ldv@altlinux.org> 4.0.3-alt7
- Enlarged internal $TERM string buffers (closes: #23972).

* Mon Jan 11 2010 Dmitry V. Levin <ldv@altlinux.org> 4.0.3-alt6
- Fixed build with glibc >= 2.11 that provides execvpe(3).

* Sun Aug 02 2009 Dmitry V. Levin <ldv@altlinux.org> 4.0.3-alt5
- Removed obsolete %%install_info/%%uninstall_info calls.
- Fixed build with fresh toolchain.

* Tue Dec 02 2008 Dmitry V. Levin <ldv@altlinux.org> 4.0.3-alt4
- Fixed build without sys/stropts.h file.
- Removed obsolete requirements.

* Thu Jul 19 2007 Alexey Tourbin <at@altlinux.ru> 4.0.3-alt3
- reverted cp866.patch (#5440) to resolve UTF-8 locale problems
  (#8817, Alexey Morozov)
- fixed compiler warnings with -DDEBUG
- changed src.rpm packaging to keep pristine tarball

* Wed Apr 18 2007 Alexey Tourbin <at@altlinux.ru> 4.0.3-alt2
- loadav.c: fixed possible /proc/loadavg fd leak introduced in
  previous release (Dmitry V. Levin)
- layer.c, screen.c: fixed vsnprintf() return value check introduced
  in previous release
- socket.c: added errno to panic() message

* Wed Oct 25 2006 Alexey Tourbin <at@altlinux.ru> 4.0.3-alt1
- 4.0.2 -> 4.0.3 (fixes two bug in combining characters handling)
- imported sources into git, applied all changes to the sources tree,
  and built with gear
- fixed warnings emitted by new gcc compiler (-Werror build mode on),
  resulting in better error checking; some changes are not purely
  cosmetic, notably dup2() usage for oldish close()+dup() technique

* Mon May 15 2006 Alexey Tourbin <at@altlinux.ru> 4.0.2-alt4
- urgency=medium: applied alarm/lonjmp fix for "Reproducible key sequence
  causes hard lock" (debian #157873, savannah #11610)
- fixed build with -Wl,--as-needed (by using -ltinfo, not -lcurses)
- fixed -Werror mode (by using NULL sentinel for execl() in fileio.c)

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 4.0.2-alt3.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Fri Aug 26 2005 Dmitry V. Levin <ldv@altlinux.org> 4.0.2-alt3
- Added system logger initialization in the screen builtin locker.
- Allowed users with empty passwords to use builtin locker.

* Sun Apr 17 2005 Alexey Tourbin <at@altlinux.ru> 4.0.2-alt2
- added support for cp866 (Kachalov Anton, #5440)
- fixed invalid type casts (Kachalov Anton)

* Thu Jan 15 2004 Alexey Tourbin <at@altlinux.ru> 4.0.2-alt1
- 4.0.2 (new screenrc parser, see NEWS)
- configuration file reworked
  + moved terminal settings to /etc/screencap (sourced from screenrc)
- rh-delete-hack.patch (treat backspaces '^?' as deletes in sample screenrc)
- owl-pam.patch and owl-no-fault-handler.patch updated
- owl-warnings patch applied, -Werror mode enabled
- support for rxvt OSC codes enabled
- removed "merge status" from specfile as it is completely outdated
- added Debian FAQ

* Fri Nov 28 2003 Alexey Tourbin <at@altlinux.ru> 3.9.15-alt2
- security update (buffer overflow fixed, Timo Sirainen)

* Fri Sep 05 2003 Alexey Tourbin <at@altlinux.ru> 3.9.15-alt1.1
- alt-owl-config.patch updated (eliminates glibc-devel-static from BuildRequires)
- support for 256 colors enabled

* Sun Aug 03 2003 Alexey Tourbin <at@altlinux.ru> 3.9.15-alt1
- 3.9.15; patches updated: alt-texinfo, alt-owl-config,
  deb-owl-alt-home-screen-exchange, alt-msgfix, alt-owl-pam,
  owl-alt-no-fault-handler, mdk-alt-max-window-size

* Sat Apr 12 2003 Dmitry V. Levin <ldv@altlinux.org> 3.9.11-alt4
- Rebuilt with libpam_userpass.so.1.

* Tue Dec 24 2002 Dmitry V. Levin <ldv@altlinux.org> 3.9.11-alt3
- Rebuilt with libutempter-1.1.0.

* Tue Nov 05 2002 Dmitry V. Levin <ldv@altlinux.org> 3.9.11-alt2
- Use subst instead of perl in %%build.

* Sun May 26 2002 Dmitry V. Levin <ldv@altlinux.org> 3.9.11-alt1
- 3.9.11, updated patches.
- Dropped screen terminfo entries (can be found in terminfo package).
- Grant screen access to both chkpwd and utempter helpers via a group
  screen restricted directory and hard links (Owl).
- Switch egid for the PAM authentication making use of POSIX saved ID's (Owl).
- Don't compile in the SIGSEGV/SIGBUS fault handler; previously it was
  only used for SUID installation, not SGID, and would claim to dump core
  which it indeed can't do (Owl).
- Updated dependencies.

* Mon Dec 17 2001 Dmitry V. Levin <ldv@altlinux.org> 3.9.10-alt4
- Reordered patches.
- Fixed message typo in FindSocket().
- More tmp fixes in configure.in (Owl).
- Added pam_userpass support (derived from Owl's patch).
- Link without libelf and libshadow.

* Mon Oct 15 2001 Dmitry V. Levin <ldv@altlinux.org> 3.9.10-alt3
- Patched and built with new utempter.

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.9.10-alt2
- Made %_bindir/screen sgid to utempter.

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.9.10-alt1
- 3.9.10

* Sat Jul  7 2001 Ivan Zakharyaschev <imz@altlinux.ru> 3.9.9-alt3
- the default place for user's sockets is now ~/tmp/screen/
- Files:
  + /etc/profile.d/screen.sh thrown away (it made using screen almost
    impossible)
  + added ALT-PACKAGING-INFO.en
- Documentation: a useful addition about the resurrecting effect of
  SIGCHLD.
- spec-file:
  + the args for %%make_build became shorter (no need to define
    ETCSCREENRC -- it is passed in ./configure options)
  + generating and installing terminfo entries made optional

* Thu Jun 28 2001 Ivan Zakharyaschev <imz@altlinux.ru> 3.9.9-alt2
- Files:
    + the sample user's .screenrc moved from /etc/skel/ to doc
    + terminfo files included (the same files provided by ncurses
      package are just counterparts of these ones).
- Documentation fixes from RedHat.
- Changes in the spec-file (all of them don't affect the content of the
resulting binary package):
  + made the Description a bit less lamer-ish
  + other minor enhancements
  + some substitution commands thrown away from %%build section because
    the same corrections are done in the Owl's patches
  + shortened a bit Owl's config patch -- the same configuration is done
    by adding ./configure options.

* Mon May 28 2001 Stanislav Ievlev <inger@altlinux.ru> 3.9.9-alt1
- 3.9.9

* Thu May 17 2001 Stanislav Ievlev <inger@altlinux.ru> 3.9.8-ipl2mdk
- Add patches from Owl.

* Wed Nov 15 2000 Dmitry V. Levin <ldv@fandra.org> 3.9.8-ipl1mdk
- 3.9.8
- Patched to build with glibc-2.2.

* Wed Sep 20 2000 Dmitry V. Levin <ldv@fandra.org> 3.9.5-ipl9mdk
- RE adaptions.
- Automatically added BuildRequires.

* Mon Sep 18 2000 Francis Galiegue <fg@mandrakesoft.com> 3.9.5-9mdk
- Fix info file

* Fri Sep 15 2000 Francis Galiegue <fg@mandrakesoft.com> 3.9.5-8mdk
- Security fix, adapted patch from RH

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.9.5-7mdk
- automatically added BuildRequires

* Fri Jul 28 2000 Francis Galiegue <fg@mandrakesoft.com> 3.9.5-6mdk
- Oops... Fixed *info macros...

* Fri Jul 28 2000 Francis Galiegue <fg@mandrakesoft.com> 3.9.5-5mdk
- BMacros
- Some spec file changes

* Mon Jun 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.9.5-4mdk
- fix wrong URL
- use %%_mandir & %%_infodir to prepare FHS compliancy
- merge in RH patches

* Sun Jun 04 2000 David BAUDENS <baudens@mandrakesoft.com> 3.9.5-3mdk
- Fix build

* Fri Mar 17 2000 Francis Galiegue <francis@mandrakesoft.com>
- Let spec helper handle stripping and compressed manpages
- Changed group to match 7.1 specs

* Tue Dec 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 3.9.5 (fix a lot of know bugs).

* Wed Nov 10 1999 Francis Galiegue <francis@mandrakesoft.com>
- Really fixed /etc/skel/.screenrc permissions
- Fixed /etc/screenrc permissions
- spawn ptys are no more world writable

* Tue Nov 09 1999 John Buswell <johnb@mandrakesoft.com>
- Fixed /etc/skel/.screenrc permissions
- Enabled Unix98 ptys

* Tue Nov 02 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Thu Oct 21 1999 Francis Galiegue <francis@mandrakesoft.com>
- Merged patch from RedHat: screen now uses /dev/pts/*
- made /etc/profile.d/screen.sh sh-compatible (use test -z $SCREENDIR)

* Tue Sep 21 1999 Francis Galiegue <francis@mandrakesoft.com>
- fixed bug in /etc/profile.d/screen.sh (credits go to Axalon for this one)

* Mon Aug 23 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 3.9.4

* Sun Jul 25 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- set SCREENDIR=$HOME/tmp

* Tue May 11 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Wed Apr 07 1999 Bill Nottingham <notting@redhat.com>
- take out warning of directory ownership so root can still use screen

* Wed Apr 07 1999 Erik Troan <ewt@redhat.com>
- patched in utempter support, turned off setuid bit

* Fri Mar 26 1999 Erik Troan <ewt@redhat.com>
- fixed unix98 pty support

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Thu Mar 11 1999 Bill Nottingham <notting@redhat.com>
- add patch for Unix98 pty support

* Mon Dec 28 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.7.6.

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- upgraded to 3.7.4

* Wed Oct 08 1997 Erik Troan <ewt@redhat.com>
- removed glibc 1.99 specific patch

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- added install-info support

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
