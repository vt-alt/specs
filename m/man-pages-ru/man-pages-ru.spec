Name: man-pages-ru
Version: 4.17
Release: alt1

# man-pages-ru_4.17-2385-2385-20181124.tar.bz2
%define lversion %version-2385-2385-20181124

Summary: Russian translations of OS GNU/*/Linux manpages
Summary(ru_RU.UTF-8): Русские переводы страниц руководства по ОС GNU/*/Linux
License: distributable
Group: Documentation
Url: https://sourceforge.net/projects/man-pages-ru/
BuildArch: noarch

Icon: books-ru.xpm

Source: man-pages-ru_%lversion.tar.bz2
Source1: man-pages-ru-4.08-alt-Makefile

Patch0: man-pages-ru-0.98-alt-combo.patch.bz2
Patch1: mat-functions-alt.patch.gz

Conflicts: man-pages-ru-extra < 0.1-alt3

Obsoletes: man-ru, manpages-ru, man-pages-ru-KOI8-R, man-pages-ru-CP1251
PreReq: man >= 1.6e-alt1

%description
A collection of man pages (documentation) from the Linux Documentation
Project (LDP) translated to russian.  The man pages are organized into the
following sections: Section 1, user commands; Section 2, system
calls; Section 3, libc calls; Section 4, devices (e.g., hd, sd); Section 5,
file formats and protocols (e.g., wtmp, /etc/passwd, nfs); Section 6, games
(intro only); Section 7, conventions, macro packages, etc. (e.g., nroff,
ascii); and Section 8, system administration.

%description -l ru_RU.UTF-8
Коллекция страниц руководства из Проекта Документации на Линукс, на
русском языке.  Страницы руководства организованы следующим образом:
секция 1, команды пользователя; секция 2, системные вызовы; секция 3,
функции библиотеки языка C; секция 4, устройства (например, hd, sd);
секция 5, форматы файлов и протоколы (например, wtmp, /etc/passwd, nfs);
секция 6, игры (только введение); секция 7, соглашения, макро-пакеты,
и т. п. (например, nroff, ascii); и секция 8, утилиты администратора.

%prep
%setup -q -n man-pages-ru_%lversion
#patch0 -p1
#patch1 -p0
sed "s/@VERSION@/%version/" < %SOURCE1 > %_builddir/man-pages-ru_%lversion/Makefile

#set_compress_method skip

%install
mkdir -p %buildroot%_mandir/ru/man{1,2,3,4,5,6,7,8,9,n}
mkdir -p %buildroot%_cachedir/man/ru/cat{1,2,3,4,5,6,7,8,9,n}

make install \
	INSTALL="install -p -m644" \
	INSTALLPATH=%buildroot%_mandir \
	LANG_SUBDIR=ru \
	COMPRESS=none \
	#


#echo KOI8-R >%buildroot%_mandir/ru/.charset
echo >%buildroot%_cachedir/man/ru/whatis

# pushd %buildroot%_mandir/ru/man2/
#  for F in \
#  munmap.2 \
#  mknodat.2 \
#  mlock2.2 \
#  ; do
#     rm -f $F
#  done
# popd

%postun
if [ "$1" = 0 -a ! -d %_mandir/ru ]; then
       rm -rf %_cachedir/man/ru
fi

%files
%doc License README
%_mandir/*

%attr(3775,root,man) %dir %_cachedir/man/ru
%attr(644,cacheman,man) %ghost %_cachedir/man/ru/whatis

%defattr(644,root,man,2775)
%_cachedir/man/ru/cat*

%changelog
* Thu May 30 2019 Sergey Y. Afonin <asy@altlinux.ru> 4.17-alt1
- 4.17-2385-2385-20181124

* Sat Aug 25 2018 Sergey Y. Afonin <asy@altlinux.ru> 4.16-alt1
- 4.16-2383-2383-20180422

* Mon Apr 24 2017 Sergey Y. Afonin <asy@altlinux.ru> 4.08-alt3
- 4.08-2329-2329-20170422 (all translated)
- added "Conflicts: man-pages-ru-extra < 0.1-alt3"

* Wed Mar 22 2017 Sergey Y. Afonin <asy@altlinux.ru> 4.08-alt2
- 4.08-2329-2272-20170321 (added malloc.3,math_error.7,mdoc.7)

* Wed Mar 08 2017 Sergey Y. Afonin <asy@altlinux.ru> 4.08-alt1
- 4.08-2329-2269-20170309 (Closes: #33166)
- removed all man pages except man-pages-ru
  removed pages will be packed separately (man-pages-ru-extra)
- disabled patches for man-pages-ru (old, needs revision)
- converted spec to UTF-8

* Sun May 08 2011 Slava Semushin <php-coder@altlinux.ru> 0.98-alt23
- NMU
- cp.1: fixed grammar error (Closes: #25170)
  (patch from Gleb F. Malinowski <glebfm@altlinux.org>)
- rename.1: include it to package
- rename.2: fixed name of header file (partially fix for #15372)
- index.3, strfry.3, strsignal.3, strlen.3: sync with man-pages-3.32

* Thu Dec 02 2010 Slava Semushin <php-coder@altlinux.ru> 0.98-alt22
- NMU
- install.1: fixed typo (Closes: #24676)
- man.1: fixed typo

* Tue Sep 14 2010 Slava Semushin <php-coder@altlinux.ru> 0.98-alt21
- NMU: changed group to Documentation (inspired by #24076)

* Fri Jul 16 2010 Slava Semushin <php-coder@altlinux.ru> 0.98-alt20
- NMU
- sshd_config.5: describe AllowAgentForwarding option (Closes: #23654)
  (contributed by nwtour@mail.ru)
- baby.1, sex.6: deleted (see also #13477)

* Mon Feb 01 2010 Slava Semushin <php-coder@altlinux.ru> 0.98-alt19
- NMU
- vsftpd.conf.5: updated (Closes: #22656)
  (contributed by Andrew Clark <andyc@altlinux.org>)

* Tue Jan 12 2010 Slava Semushin <php-coder@altlinux.ru> 0.98-alt18
- NMU
- Don't call makewhatis after installation (Closes: #21911)
- sort.1: describe -R option (Closes: #16905)
  (translated by Igor Chubin <igor@chub.in>)
- iconv.3: added (Closes: #22050)
  (contributed by Anatoly <vostok@etersoft.ru>)
- ldapdelete.1: added
  (translated by Igor Chubin <igor@chub.in>)
- drake.6: some improvements
- man.conf.5: fixed path to man.conf file
- whatis.1: fixed path to makewhatis
  (reported by Rinat Bikov <bikoz.r@gmail.com>)
- Package /usr/share/doc/security-ru directory

* Sun Oct 11 2009 Slava Semushin <php-coder@altlinux.ru> 0.98-alt17
- NMU
- ssh.1: describe -Y option, updated -X description (Closes: #15685)
  + Thanks to Vladimir Stupin <wheelof@gmail.com>

* Mon Oct 05 2009 Slava Semushin <php-coder@altlinux.ru> 0.98-alt16
- NMU
- head.1: corrected description for -n option (Closes: #17073)
- wget.1: fixed -nH option description (Closes: #17438)
- hosts.5: fixed typo and corrected translation (Closes: #18443)
- Spec cleanup

* Sun Jun 21 2009 Slava Semushin <php-coder@altlinux.ru> 0.98-alt15
- NMU
- at.1, atq.1, atrm.1, cron.8, crontab.1, crontab.5:
  fixed paths (Closes: #20517)
- bash.1: fixed typo and formatting (Closes: #19992)
- index.3, MB_LEN_MAX.3, MB_CUR_MAX.3, strfry.3, strsignal.3:
  sync with man-pages-3.21

* Sat Apr 11 2009 Slava Semushin <php-coder@altlinux.ru> 0.98-alt14
- NMU
- ln.1: fixed typo in parameter name (Closes: #16350)
- sudo.8: fixed typo (Closes: #18542)
- fcntl.2: fixed typos (Closes: #18624)
- accept.2: fixed typo and formatting (Closes: #18625)
- shutdown.2: updated (Closes: #18626)

* Thu Apr 03 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt13
- bug #15178

* Wed Feb 06 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt12
- Removed %_mandir/ru/.charset. Bug #9364.

* Thu Sep 27 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt11
- Package merged with man-pages-security-ru
- Fixed bugs: #9662, #10431, #11641, #12345, #12635
- Added new translations: osec.1, tr.1, tsort.1, vsftpd.conf.5, sconfig.8

* Thu Mar 15 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt10
- Added new translations: cat.1, fuser.1, uname.1, MB_CUR_MAX.3, MB_LEN_MAX.3, 
  psignal.3, strsignal.3, badblocks.8
- Updated: index.3, strcasecmp.3, strfry.3, strlen.3, strstr.3
- Fixed typos in: sudoers.5

* Sun Nov 05 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt9
- Added new translations: autofs.5, auto.master.5, autofs.8, automount.8,
  mkfs.8, rename.1, sort.1
- Updated: acos.3, asin.3, atan.3, atanh.3, atan2.3, cos.3, cosh.3, hypot.3, 
  sin.3, sinh.3, sqrt.3, tan.3
- Fixed typos in: wget.1, fdatasync.2, mmap2.2, stat.2, sync.2
- Renamed llab.3 to llabs.3

* Sat May 27 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt8
- Added new translations: 
  arch.1 from man-pages-ru by ASP Linux
  ethtool.8 by Aleksander N. Gorohovski <angel@feht.dgtu.donetsk.ua>
  hotplug.8 by Aleksandr Savvin <savvin@mail.ru>
- Updated links in sed.1

* Fri Mar 31 2006 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt7
- Added new translations: djview.1, last.1, lilo.8, logrotate.8
- Updated umount.8
- Dropped obsoleted translations: ldd.1, postfix manual pages.
- Removed vim.1

* Tue Nov 15 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt6
- Added: chroot.1, syslogd.1, which.1, fstab.5, setserial.8, sysctl.8, umount.8
- Updated: cut.1, bash.1
- Linked sh.1 to bash.1

* Thu Oct 13 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt5
- Added: cut.1, login.1, sleep.1, tty.1, who.1, dmesg.8, lspci.8
- Updated: man.1

* Fri Sep 16 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt4
- Added: baby.1, iconv.1, man.1, sex.6, fdformat.8
- Updated: access.2, muttrc.5, xinetd.conf.5
- Retranslated: install.1, ln.1

* Thu Jun 09 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt3
- Dropped obsoleted man pages: gpg.1, gpgv.1

* Mon May 09 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt2
- updated: chattr.1
- added: logname.1, lsattr.1, stat.1
- translations by Aleksander N.Gorohovski merged in one tar archive.

* Fri Apr 22 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.98-alt1
- 0.98
- added: eject.1, chattr.1, getcontext.2, getpagesize.2, getpriority.2, 
  koi8-r.7, ldp.7, x25.7
- updated: fcntl.2, muttrc.5

* Wed Mar 09 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.97-alt3
- added: id.1
- updated: mount.8

* Fri Dec 17 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.97-alt2
- added: tar.1, mount.8
- updated: scp.1, ssh.1, ssh-agent.1, ssh-keygen.1, sftp.1, ssh-add.1,
  ssh-copy-id.1, ssh-keyscan.1, sftp-server.8

* Tue Aug 03 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.97-alt1
- man-pages-ru-0.97: 
  added: clone.2, mmap2.2, personality.2, pread.2, pwrite.2, syscall.2, 
  sysinfo.2, umask.2
- updated: pipe.2, sync.2
  
* Wed Jul 07 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.96-alt2
- Updated gpg.1, gpgv.1

* Mon Jun 21 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.96-alt1
- man-pages-ru-0.96:
  added getdents.2, getitimer.2, getpeername.2, getresgid.2
  killpg.2, vm86.2, uname.2, uselib.2, ustat.2, vhangup.2, wait4.2
- updated mknod.2, unlink.2, write.2
- man-pages-ru-ALT: 
  added rsyncd.conf.5
  
* Thu May 27 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.95-alt2
- Added faq.6 and fstype.8

* Sat May 22 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.95-alt1
- man-pages-ru-0.95:
  added kill.2
  updated proc.5 and termcap.5.
- man-pages-ru-ALT:
  su.1 from coreutils replaced with new one from SimplePAMApps
  minor fixes in rpm.8, resolver.5

* Fri Apr 16 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.94-alt1
- man-pages-ru updated up to 0.94
- tcb translations updated up to 0.9.8.7
- added Makefile
- updated patches, removed obsoleted

* Fri Apr 09 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.7-alt31
- Added rsync.1 by Головин Сергей <svgol@mail.ru>

* Mon Mar 22 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.7-alt30
- Added bash.1 by "Russian Man Pages" project <http://ln.com.ua/~openxs/projects/man/>

* Fri Mar 12 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.7-alt29
- Added nice.1, master.8, qmgr.8 by Головин Сергей <svgol@mail.ru>
- Updated wget.1 by Н. Шафоростов <admin@program.net.ua>

* Tue Dec 16 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.7-alt28
- Updated gpg.1 and added gpgv.1

* Thu Jul 17 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.7-alt27
- Added: ar.1, gunzip.1, gzexe.1, gzip.1, zcat.1, zcmp.1, zdiff.1,
  zforce.1, zgrep.1, zmore.1, znew.1.

* Thu Jul 10 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.7-alt26
- Fixed typo's in procmail.1

* Wed Jul 09 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.7-alt25
- Added updated chgrp.1, fitchmail.1
- Updated man-pages-ru-1.41.patch.gz

* Sun Apr 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7-alt24
- Packaged %_cachedir/man/ru/whatis file.
- Changed %_cachedir/man/ru permissions
  from %attr(755,root,root) to %attr(3775,root,man).
- Changed %_cachedir/man/ru/cat* permissions
  from %%attr(775,root,man) to %%attr(2775,root,man).

* Fri Dec 20 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.7-alt23
- Added gendiff.1, lzop.1, autofs.8

* Tue Nov 26 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.7-alt22
- Updated man pages for postfix
- Added pppdump.8, pppstats.8, wget.1, procmail.1, sed.1
- Fixed Provides and russian description

* Mon Nov 04 2002 Dmitry V. Levin <ldv@altlinux.org> 0.7-alt21
- Merged subpackages back to single package;
  requires recent man.
- Rewritten %%install script.
- Updated summary and description.

* Wed Jul 17 2002 Sass <sass@altlinux.ru> 0.7-alt20
- fixed typo's in ssh.1

* Fri Jun 14 2002 Sass <sass@altlinux.ru> 0.7-alt19
- updated muttrc.5

* Mon Jun 03 2002 Sass <sass@altlinux.ru> 0.7-alt18
- corrected some mistakes

* Mon May 27 2002 Sass <sass@altlinux.ru> 0.7-alt17
- added translations apt.conf.5, sources.list.5, apt-cache.8,
  apt-cdrom.8, apt-config.8, apt-get.8, apt.8

* Tue May 14 2002 Sass <sass@altlinux.ru> 0.7-alt16
- added gpg.1, vim.1, xinetd.conf.5

* Wed Apr 10 2002 Sass <sass@altlinux.ru> 0.7-alt15
- updates in chgrp.1, chmod.1, chown.1, cp.1 to man-pages-1.41
- added nmap.1, ldif.5, apt.8, apt-cdrom.8
- fixed typo

* Mon Mar 18 2002 Sass <sass@altlinux.ru> 0.7-alt14
- updated update-alternatives.8

* Mon Mar 11 2002 Sass <sass@altlinux.ru> 0.7-alt13
- fixed typo

* Thu Mar 05 2002 Sass <sass@altlinux.ru> 0.7-alt12
- Bugfix release

* Mon Mar 04 2002 Sass <sass@altlinux.ru> 0.7-alt11
- Added man-tcb-ru.tar.bz2 from Dmitry V. Levin <ldv@altlinux.ru>
- Added initlog.1, xinetd.log.8 from Alex Savvin <savvin@mail.ru>
- Updated install.1

* Sun Feb 24 2002 Sass <sass@altlinux.ru> 0.7-alt10
- Added man-postfix.tar.bz2 by Alex Savvin <savvin@mail.ru>
- Added patch for man-postfix

* Thu Feb 21 2002 Sass <sass@altlinux.ru> 0.7-alt9
- Added w.1

* Sun Feb 03 2002 Sass <sass@altlinux.ru> 0.7-alt8
- Updated translations: sudoers.5, sudo.8, visudo.8

* Wed Jan 09 2002 Sass <sass@altlinux.ru> 0.7-alt7
- Added Summary & description in CP1251 encoding

* Tue Nov 27 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.7-alt6
- Updated package requires.
- Updated %post scripts.

* Mon Nov 26 2001 Sass <sass@altlinux.ru> 0.7-alt5
- Fixed access rights in man5
- Added new translations: xinetd.8, ftpd-BSD.8
- Removed makewhatis.ru script.
- Updated spec

* Fri Nov 23 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.7-alt3
- Fixed %%postun scripts.
- Updated makewhatis.ru script.
- Updated package requires.

* Thu Nov 22 2001 Sass <sass@altlinux.ru> 0.7-alt2
- added manpage ftpd-BSD.8

* Sat Nov 3 2001 Sass <sass@altlinux.ru> 0.7-alt1
- 0.7
- Updated spec
- Added scripts
- manpages-RE now known as manpages-ALT
- Updated manpages: make-ssh-known-hosts.1, scp.1, sftp.1,
  ssh-add.1, ssh-agent.1, ssh-copy-id.1, ssh-keygen.1,
  ssh-keyscan.1, ssh.1, sftp-server.8, sshd.8

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.6-ipl4mdk
- FHSification.
- Updated manpages.
- Kicked out obsoleted scripts.

* Wed Feb 14 2001 AEN <aen@logic.ru> 0.6-ipl3mdk
- adder rpm.8 & rpm2cpio.8 from Dmitry Levin

* Fri Jan 26 2001 AEN <aen@logic.ru> 0.6-ipl2mdk
- two packages
- 0.6
- rpm.8 added

* Tue Jul 18 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-12mdk
- BM

* Mon Jun 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-11mdk
- use mandir macro in order to be ok when switching to /usr/share/man as
  following FHS.

* Tue Apr 11 2000 Denis Havlik <denis@mandrakesoft.com> 0.1-10mdk
- Group: System/Internationalization
- added "Prereq: sed grep man"
- spechelper, dir permissions

* Wed Dec 22 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added 'man drake' from Aleksey Smirnov

* Fri Nov 19 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- moved makewhatis.ru from /usr/local/sbin to /usr/sbin

* Fri Oct 29 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- fixed the colours of the icon

* Fri Jul 23 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- adapted the rpm package to the Mandrake format (added icon, makewhatis
  scripts, %post script, improved %files etc)

* Tue May 20 1999 Alexei Mikhalev <leha@linuxfan.com>
- Initial version.
