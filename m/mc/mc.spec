%def_without smb
%def_with    gpm
%define fullname MidnightCommander

Name: mc
Version: 4.8.25
Release: alt1

# '-gitYYYYMMDD' or ''
%define ver_date ''

License: GPL-3.0-or-later
Summary: An user-friendly file manager and visual shell
Group: File tools
Url: http://midnight-commander.org/

Source0: %name-%version.tar
Source1: synce-mcfs.tar
Source2: mc-dnlike.color
Source3: mc-dark.color
Source4: mc-16.png
Source5: mc-32.png
Source6: mc.zsh

%add_findreq_skiplist */lib/mc/ext.d/*
%add_findreq_skiplist */lib/mc/extfs.d/*

Patch0: %name-%version-%release.patch

Patch1: mc-4.8.24-alt-wrapper.patch
Patch2: mc-4.7.5.1-alt-defaults.patch
Patch3: mc-4.8.20-alt-menu.patch

# Misc

# a part of http://www.midnight-commander.org/ticket/1480
Patch101: mc-4.7.0.2-savannah-edit-homekey.patch

# http://www.midnight-commander.org/ticket/2496
Patch102: mc-4.8.20-alt-forceexec.patch

# http://www.midnight-commander.org/ticket/34
Patch103: mc-4.8.24-alt-extfs-udar.patch

Conflicts: %name-data
Conflicts: %name-locales
Conflicts: %name-doc

Obsoletes: %name-data
Obsoletes: %name-locales
Obsoletes: %name-doc

Requires: rpm >= 4.13

BuildPreReq: glib2-devel libe2fs-devel
BuildPreReq: groff-base cvs libX11-devel unzip
BuildPreReq: libslang2-devel libmount-devel
%if_with gpm
BuildPreReq: libgpm-devel
%endif

%add_findreq_skiplist %_sysconfdir/mc/edit.indent.rc
%add_findreq_skiplist %_sysconfdir/mc/edit.spell.rc
%add_findreq_skiplist %_libexecdir/mc/extfs.d/*

# Polish translations (*.pl) recognized as Perl code
%add_findreq_skiplist %_datadir/mc/mc.hlp*
%add_findreq_skiplist %_datadir/mc/mc.hint*

%description
Midnight Commander is a visual shell much like a file manager, only
with way more features. It is text mode, but also includes mouse
support if you are running GPM. Its coolest feature is the ability
to ftp or ssh files access, view various archive files (include cpio),
poke into RPMs and DEBs for specific files and more others.

%package full
Summary: Meta package for install Midnight Commander with packages which possible needed.
Group: File tools
BuildArch: noarch
Obsoletes: %name-complete
Requires: %name
Requires: cdrkit-utils sqlite3

%description full
This package pulls Midnight Commander with packages which can be
needed for working additional components (some vfs for example).

%prep
%setup -a1
%patch0 -p1

# ALT
%patch1 -p1
%patch2 -p1
%patch3 -p0

# Misc
#patch101 -p1
%patch102 -p1
%patch103 -p1

cat <<EOF > version.h
#ifndef MC_CURRENT_VERSION
#define MC_CURRENT_VERSION "@@VERSION@@"
#endif
EOF

sed 's|@@VERSION@@|%version-%release%ver_date|' -i version.h

#%%autoreconf
./autogen.sh

%build
%configure %{?_with_smb:--enable-vfs-smb --with-smb-configdir=%_sysconfdir/samba} \
	--enable-extcharset \
	--enable-vfs-undelfs

%make_build

%install
%makeinstall_std

install -d %buildroot%_sysconfdir/{profile.d,bashrc.d}
mv %buildroot%_libexecdir/mc/mc.csh %buildroot%_sysconfdir/profile.d/
mv %buildroot%_libexecdir/mc/mc.sh %buildroot%_sysconfdir/bashrc.d/
install -m755 %SOURCE6 %buildroot%_sysconfdir/profile.d/mc.sh
# Install DosNavigator color scheme
install -m644 %SOURCE2 .
# Install Dark color scheme
install -m644 %SOURCE3 .

# Install SynCE VFS ( http://www.midnight-commander.org/ticket/2905 )
install -m755 synce-mcfs/src/synce* %buildroot%_libexecdir/%name/extfs.d/

# http://www.midnight-commander.org/ticket/2314
# mc.desktop
cat <<__EOF__>%name.desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=Midnight Commander
Comment=Visual shell and file manager
Comment[ru]=Визуальная оболочка и диспетчер файлов 
Icon=%fullname
Exec=%name
Terminal=true
Categories=ConsoleOnly;System;FileTools;FileManager;
__EOF__
install -pD -m644 %name.desktop %buildroot%_desktopdir/%name.desktop
# mcedit.desktop
cat <<__EOF__>mcedit.desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=mcedit
GenericName=Text Editor
GenericName[ru]=Текстовый редактор
Comment=Internal file editor of GNU Midnight Commander
Comment[ru]=Встроенный текстовый редактор GNU Midnight Commander
Icon=%fullname
Exec=mcedit
Terminal=true
Categories=ConsoleOnly;Utility;TextEditor;
__EOF__
install -pD -m644 mcedit.desktop %buildroot%_desktopdir/mcedit.desktop

# icons
install -pD -m644 %SOURCE4 %buildroot%_miconsdir/%fullname.png
install -pD -m644 %SOURCE5 %buildroot%_niconsdir/%fullname.png

%find_lang --with-man %name

%files -f %name.lang
%_bindir/mc
%_bindir/mcedit
%_bindir/mcview
%_bindir/mcdiff
%_libexecdir/mc/
%config(noreplace) %_sysconfdir/bashrc.d/*
%config(noreplace) %_sysconfdir/profile.d/*
%dir %_sysconfdir/mc
%config(noreplace) %_sysconfdir/mc/*edit*
%config(noreplace) %_sysconfdir/mc/filehighlight.ini
%config(noreplace) %_sysconfdir/mc/mc.ext
%config(noreplace) %_sysconfdir/mc/mc.keymap
%config(noreplace) %_sysconfdir/mc/mc.default.keymap
%config(noreplace) %_sysconfdir/mc/mc.emacs.keymap
%config(noreplace) %_sysconfdir/mc/mc.menu
%config(noreplace) %_sysconfdir/mc/sfs.ini

%_man1dir/*

%_datadir/mc/
%_desktopdir/%name.desktop
%_desktopdir/mcedit.desktop
%_niconsdir/%fullname.png
%_miconsdir/%fullname.png

%doc AUTHORS doc/FAQ doc/HACKING doc/MAINTAINERS doc/NEWS doc/README
%doc doc/README.QNX doc/TODO doc/filehighlight.txt contrib/README.xterm
%doc mc-dnlike.color mc-dark.color

%files full

%changelog
* Tue Jul 28 2020 Sergey Y. Afonin <asy@altlinux.org> 4.8.25-alt1
- 4.8.25 (ALT #38737, ALT #38454)
- updated License tag to SPDX syntax

* Sat Feb 29 2020 Sergey Y. Afonin <asy@altlinux.org> 4.8.24-alt1
- 4.8.24 (updated to 20200215 git snapshot, ALT #37545)

* Thu Jul 04 2019 Sergey Y. Afonin <asy@altlinux.ru> 4.8.23-alt1
- 4.8.23

* Sun Jan 13 2019 Sergey Y. Afonin <asy@altlinux.ru> 4.8.22-alt1
- 4.8.22
- added mc-4.8.22-syntax.patch (ALT #35799)

* Tue Nov 13 2018 Ivan Razzhivin <underwit@altlinux.org> 4.8.21-alt4
- changed the name of the icons to avoid conflicts (ALT #34346)

* Thu Nov 01 2018 Pavel Moseev <mars@altlinux.org> 4.8.21-alt3
- Updated hint translation

* Mon Aug 20 2018 Sergey Y. Afonin <asy@altlinux.ru> 4.8.21-alt2
- updated to 20180819 git snapshot (ALT #35188)
- rebuilt with S-Lang 2.3.2 (ALT #34343)
- removed alt-rpm-select.patch, added "Requires: rpm >= 4.13"

* Wed Jun 20 2018 Sergey Y. Afonin <asy@altlinux.ru> 4.8.21-alt1
- 4.8.21 (updated to 20180620 git snapshot)

* Sun Mar 04 2018 Sergey Y. Afonin <asy@altlinux.ru> 4.8.20-alt2
- updated to 20180224 git snapshot (ALT #34573)

* Mon Dec 11 2017 Sergey Y. Afonin <asy@altlinux.ru> 4.8.20-alt1
- 4.8.20
- added mcedit.desktop (ALT #32528)
- updated patches:
  + alt-menu.patch
  + alt-forceexec.patch

* Thu Mar 09 2017 Sergey Y. Afonin <asy@altlinux.ru> 4.8.19-alt2
- added mc-4.8.19-alt-rpm-select.patch,
  removed "Requires: rpm >= 4.13"

* Tue Mar 07 2017 Sergey Y. Afonin <asy@altlinux.ru> 4.8.19-alt1
- 4.8.19 (updated to 20170306 git snapshot)
- added "Requires: rpm >= 4.13"

* Wed Nov 30 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.8.18-alt1
- 4.8.18 (updated to 20161130 git snapshot)

* Mon May 23 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.8.17-alt1
- 4.8.17 (with MC tickets #3643, #3637, #3648 of 4.8.18 roadmap)
- added sqlite3 to requires of mc-full
  (http://forum.altlinux.org/index.php?topic=34864.msg285786#msg285786)
- updated descriptions in spec

* Fri Mar 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.8.16-alt2
- merged with git://github.com/MidnightCommander/mc:
  + MC Ticket #3606 (fix segfault due to incorrect value of SHELL environment variable)
  + MC Ticket #3618 (update f90 syntax)
  + MC Ticket #3620 (patchfs: fix syntax error)
- added mc-4.8.16-3621_cpio_segfault.patch (MC Ticket #3621)

* Mon Mar 14 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.8.16-alt1
- 4.8.16
- droped fix for MC Ticket #3574 (fixed in upstream)
- added fix for fish ls helper (MC Ticket #3611)
- updated patches:
  + alt-wrapper.patch
  + alt-menu.patch
  + alt-forceexec.patch

* Mon Nov 30 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.8.15-alt2
- Fixed handling of MC_XDG_OPEN in ext.d/*.sh (MC Ticket #3574)

* Sun Nov 29 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.8.15-alt1
- 4.8.15
- replaced f90.syntax (ALT #31520)

* Thu Apr 02 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.8.14-alt2
- rebuilt without smb vfs (http://bugzilla.altlinux.org/30649#c10)
- fixed incorrect merge with tag '4.8.14'
- added libmount-devel to BuildPreReq

* Mon Mar 23 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.8.14-alt1
- 4.8.14
- built with enable-vfs-smb (ALT #30649)

* Sun Apr 06 2014 Sergey Y. Afonin <asy@altlinux.ru> 4.8.12-alt1
- 4.8.12

* Wed Dec 04 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.8.11-alt1
- 4.8.11
- diabled savannah-edit-homekey.patch (many changes in mcedit)

* Tue Apr 09 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.8.8-alt3
- applied patch for MC Ticket #3003 (ALT #28817)

* Mon Apr 08 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.8.8-alt2
- merged with git://github.com/MidnightCommander/mc.git
  (MC Ticket #2991 closed)

* Sun Apr 07 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.8.8-alt1
- 4.8.8

* Tue Jan 08 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.8.7-alt1
- 4.8.7
- removed xdg-open-quickdisable.patch (moved to upstream)

* Fri Dec 14 2012 Sergey Y. Afonin <asy@altlinux.ru> 4.8.6-alt7
- merged with git://github.com/MidnightCommander/mc.git
  (CVE-2012-4463)
- changed the metod of disabling xdg-open
  + you can use MC_XDG_OPEN="/bin/false" for disable xdg-open in
  + scripts in lib/mc/ext.d/*
  removed mc-4.8.6-alt-video.sh.patch
  added mc-4.8.6-alt-xdg-open-quickdisable.patch

* Tue Nov 20 2012 Sergey Y. Afonin <asy@altlinux.ru> 4.8.6-alt6
- added mc-4.8.6-alt-video.sh.patch
  (you can use MCVIDEOPLAYER="legacy" for disable xdg-open usage)

* Sun Nov 11 2012 Sergey Y. Afonin <asy@altlinux.ru> 4.8.6-alt5
- merged with git://github.com/MidnightCommander/mc.git

* Tue Oct 23 2012 Sergey Y. Afonin <asy@altlinux.ru> 4.8.6-alt4
- added lib/mc/ext.d and lib/mc/extfs.d to findreq_skiplist

* Mon Oct 22 2012 Sergey Y. Afonin <asy@altlinux.ru> 4.8.6-alt3
- merged with git://github.com/MidnightCommander/mc.git
- adapted alt-extfs-udar.patch for 4.8.6
- added alt-extfs-rpm.patch (ALT #27357)

* Sun Oct 14 2012 Sergey Y. Afonin <asy@altlinux.ru> 4.8.6-alt2
- merged with git://github.com/MidnightCommander/mc.git
  (MC Ticket #2897 closed)

* Sat Sep 22 2012 Sergey Y. Afonin <asy@altlinux.ru> 4.8.6-alt1
- 4.8.6 (License changed to GPLv3+)
- removed ALT patches which subject of metaticket
  http://www.midnight-commander.org/ticket/2897 (Milestone: 4.8.7)
  + mc-4.7.5-alt-filetypes.patch
  + mc-4.7.0-debian-mc.ext-use-arj.patch
- removed mc-4.7.5.3-alt-extf*s-udar.patch
  http://www.midnight-commander.org/ticket/34

* Sat Jan 07 2012 Sergey Y. Afonin <asy@altlinux.ru> 4.7.5.6-alt1
- 4.7.5.6

* Sat Oct 22 2011 Sergey Y. Afonin <asy@altlinux.ru> 4.7.5.5-alt3
- applied fix from MC Ticket #2635

* Thu Oct 20 2011 Sergey Y. Afonin <asy@altlinux.ru> 4.7.5.5-alt2
- fixed output of version string (typo in spec of 4.7.5.5-alt1)

* Wed Oct 19 2011 Sergey Y. Afonin <asy@altlinux.ru> 4.7.5.5-alt1
- 4.7.5.5
- disabled rollback for MC Ticket #81

* Tue Aug 23 2011 Sergey Y. Afonin <asy@altlinux.ru> 4.7.5.3-alt3
- moved mc.sh back to bashrc.d (ALT #25703/c#3)
- added alias definition for zsh in profile.d (ALT #25703)
- rollback fix for MC Ticket #81 (new problem described in MC Ticket #2594)

* Tue Aug 09 2011 Sergey Y. Afonin <asy@altlinux.ru> 4.7.5.3-alt2
- moved mc.sh from bashrc.d to profile.d (ALT #25703)

* Mon Aug 08 2011 Sergey Y. Afonin <asy@altlinux.ru> 4.7.5.3-alt1
- 4.7.5.3

* Sat Feb 12 2011 Sergey Y. Afonin <asy@altlinux.ru> 4.7.5.1-alt2
- adapted for 4.7.5.1 and reenabled patches:
  + mc-4.7.5.1-alt-forceexec.patch
  + mc-4.7.5.1-alt-defaults.patch
- added find_content_enable_by_default.patch from Andrew Borodin
- added "Obsoletes" for mc-data, mc-locales, mc-doc subpackages

* Mon Feb 07 2011 Sergey Y. Afonin <asy@altlinux.ru> 4.7.5.1-alt1
- 4.7.5.1
- removed iso9660-semicolon.patch (MC Ticket #2471)
- disabled patches:
  + mc-4.7.0.2-alt-forceexec.patch
  + mc-4.7.0-alt-po.patch
  + mc-4.7.0-alt-defaults.patch

* Tue Dec 21 2010 Sergey Y. Afonin <asy@altlinux.ru> 4.7.0.10-alt5
- fixed processing of ";1" in some ISO images (ALT #12299)

* Mon Dec 13 2010 Sergey Y. Afonin <asy@altlinux.ru> 4.7.0.10-alt4
- Merged branch '4.7.0-stable' of git://midnight-commander.org/git/mc
  + MC Ticket #2437: mcedit: selection length trouble
  + MC Ticket #1963: use grep instead of awk in iso9660 extfs plugin.
- updated mc-4.7.0-alt-filetypes.patch for libreoffice support
- rollback splitting of package
- renamed %name-complete to %name-full

* Mon Dec 06 2010 Sergey Y. Afonin <asy@altlinux.ru> 4.7.0.10-alt3
- Merged branch '4.7.0-stable' of git://midnight-commander.org/git/mc
  + MC Ticket #2415: keep active state of editor before final decision about quit.)

* Thu Dec 02 2010 Sergey Y. Afonin <asy@altlinux.ru> 4.7.0.10-alt2
- splitted package to %name, %name-data, %name-doc and %name-locales
- removed "Packager" field
- added meta package %name-complete

* Wed Dec 01 2010 Sergey Y. Afonin <asy@altlinux.ru> 4.7.0.10-alt1
- 4.7.0.10-165-gaf432f2
- removed mc-4.7.0.2-alt-extfs-urar-fix.patch (in upstream now)
- adapted mc-4.7.0.2-alt-extfs-udar.patch for 4.7.0.10 (and renamed)
- disabled mc-4.7.0.2-alt-esc.patch (not needed now)
- added cdrkit-utils to "Requires" (ALT #24662)

* Thu Feb 25 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0.2-alt2
- 4.7.0.2-37-ge0030fd (closes: #22979)

* Wed Feb 03 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0.2-alt1
- 4.7.0.2

* Wed Jan 20 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0.1-alt2
- 4.7.0.1-51-g79346ec

* Mon Jan 04 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0.1-alt1
- 4.7.0.1

* Sun Dec 27 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0-alt9
- 4.7.0 (closes: #892)

* Sat Dec 26 2009 Anton Farygin <rider@altlinux.ru> 4.7.0-alt8.pre4
- show dotfiles by default (closes: #22625)

* Sun Dec 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0-alt7.pre4
- 4.7.0-pre4-206-g8791773

* Thu Dec 10 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0-alt6.pre4
- 4.7.0-pre4-151-g3d8938a
- don't show dotfiles by default (closes: #22495)

* Sun Dec 06 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0-alt5.pre4
- 4.7.0-pre4-136-g2c7f684
- fix pixmap location

* Sun Nov 15 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0-alt4.pre4
- 4.7.0-pre4-42-gd36c635
- apply the rpm extfs fix to the srpm extfs too (closes: #22293)

* Wed Nov 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0-alt3.pre4
- 4.7.0-pre4-3-g299b04b
- Sisyphus build (closes: #6944, #10772, #13820, #21092)

* Tue Oct 13 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0-alt3.pre3
- 4.7.0-pre3-57-gc492abe

* Sun Oct 11 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0-alt2.pre3
- 4.7.0-pre3-50-ge2e549d
- remove obsolete iso9660 patch (see #13820)
- add unzip to buildreqs
- update Url:

* Fri Oct 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.7.0-alt1.pre3
- 4.7.0-pre3
- disable autoreq for the extfs modules
- change Esc timeout to 25ms, enable old_esc_mode by default (Patch451
  which adds a configuration dialog for that options no longer applies)

* Mon Jun 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt12.pre1
- extfs:
  + add udar extfs (closes: #11019)
  + don't set C locale in urar (closes: #18492, yurifil@etersoft.ru)
  + fix display of files in subdirs in ucab (closes: #18619, yurifil@etersoft.ru)

* Sun Nov 23 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt11.pre1
- remove obsolete macros
- replace menu file with .desktop
- try to load libX11.so.6 if libX11.so didn't load (SuSe)
- make whitespace highlighting configurable through menu (RH)

* Thu Aug 28 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt10.pre1
- add configuration dialog for Esc key timeout (Arch, upstream #13733)
- mcedit: second press of Home key jumps to first non-space character (upstream
  patch #4211)
- fix extension in mc-4.6.1-mdv-lzma.patch (RH)
- update mc-4.6.2-debian-recode.patch from 4.6.2~git20080311-3
- fix u7z list mode (RH; closes: #14099)
- mc.ext
  + use 7z instead of 7za
  + remove .fli patch (merged upstream)

* Sat Aug 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt9.pre1
- update to upstream 05069a72
- sync Debian patches with 4.6.2~git20080311-1
- mc.ext:
  + recognize .cl as Lisp source (damned@; closes: #15971)
  + use arj instead of unarj (Debian)
- syntax:
  + enhance: mail (Debian)
  + add: asm, procmail (Debian)
- extfs:
  + add .cab extfs (yurifil@etersoft.ru; closes: #16361)
- fix config file names in the manpage (Debian)
- correctly view tar files with colons in their names (Debian)
- fix smb.conf path (Debian)

* Sun May 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt8.pre1
- mc.ext:
  + recognize .3gp as video, not manpage (#14982, hiddenman@)
  + don't show exif(1) error if file doesn't contain EXIF data
  + recognize all mailboxes, not only ASCII ones
  + use fbv instead of zgv for viewing images without X
- syntax:
  + update ebuild.syntax
  + recognize .mak as Makefiles (#15589, led@)
- move global configs to /etc (RH)
- build with X events support
- 51 patch applied so far

* Wed Apr 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt7.pre1
- syntax:
  + recognize .hh and .hpp as c++ again (#15177, was lost during adaptation
    of Debian patches)
  + recognize man pages with additional suffixes other than 'x', such as
    write.3p (Debian)
- add recoding support to panels, FTP and copy/move operations (Debian)
- make visible_tabs and visible_tws mcedit options configurable through config
  file (Debian)
- (un)escape weird folder names in the command line (Debian)
- use more aggressive colors in warning boxes for superuser (UHU)

* Sat Mar 29 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt6.pre1
- build with slang2
- build with system libpopt
- fix mcview with slang2 in 8-bit locales (RH)
- fix segfault when no hint files available (RH)
- fix segfault when trying to display invalid timestamp (Gentoo)
- remove chkconfig from Requires
- convert all help files to UTF-8 to be viewable in all locales (Debian)
- fix displaying link count and mode columns in UTF-8 locale (Debian)
- fix bottom button widths in UTF-8 locale (UHU)
- fix selection width in the hotlist and quick search in UTF-8 locale (UHU)
- fix off-by-one misbehavior of Ctrl-Left and Alt-Backspace in line edit
  widget (UHU)
- fix line edit widget behavior with literal newline entered (UHU)
- syntax:
  + add ebuild (Gentoo)
- mc.ext:
  + use djview for .djvu files

* Tue Mar 18 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt5.pre1
- add option to build with libslang2 (#10591)
- mc.ext:
  + open chm files with kchmviewer || xchm
- disable mc-4.6.2-rh-delcheck.patch
- fix memleak in mc-4.6.1-alt-vfs.patch (#14849)
- fix unpacking of archives with spaces (#12626)

* Wed Mar 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt4.pre1
- build with slang2
- Daedalus build

* Wed Mar 05 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt3.pre1
- fix x86_64 build (damir@)
- mc.ext:
  + show EXIF for JPEG images (Debian)
  + use msgunfmt to view .mo message catalogs (Debian)
  + add .mkv and .rm to video file extensions (Mandriva)
  + add .asm to assembler file extensions (RH)
  + add JNG and MNG to image file types (RH)
  + add .flic to video file extensions (RH)
  + use mplayer -identify to 'view' video files (RH)
  + use OO.o for all MSO files (RH)

* Thu Feb 28 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt2.pre1
- enable lynx-style navigation by default (#8046)
- package /etc/profile.d/mc.csh
- compress ChangeLog
- Debian patches:
  + syntax enhance: c++, sh
  + syntax add: debian/{control,changelog,rules}, dsc, named,
    sources.list, strace
- RH patches:
  + update panels before showing copy/move dialog
  + allow exit command on non-local filesystems
  + disable support of dirs with embedded newline
  + fix 'Preserve attributes' copy/move option
  + handle resizing during file operation
  + show free space on the current device
  + add vertical scrollbars to panels and other widgets
- PLD patches:
  + syntax enhance: rpm spec
  + syntax add: vhdl
- Mandriva patches:
  + extfs: add lzma
- Misc patches:
  + extfs: 7z improvements

* Sun Feb 24 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.6.2-alt1.pre1
- 4.6.2-pre1
- spec cleanup
- take utf8 patch from Debian mc 1:4.6.2~pre1-3 (includes
  mc-4.6.1-alt-promptfix.patch)

* Fri Jan 05 2007 Igor Zubkov <icesik@altlinux.org> 4.6.1r-alt9
- fix not readable help when utf-8 locale is used (#9727)

* Mon Oct 23 2006 Igor Zubkov <icesik@altlinux.org> 4.6.1r-alt8
- use unrar instead rar in mc.ext (#8028)

* Mon Oct 16 2006 Igor Zubkov <icesik@altlinux.ru> 4.6.1r-alt7
- added mc-4.6.1-alt-menu.patch (fixed mc.menu scripts)

* Mon Oct 16 2006 Igor Zubkov <icesik@altlinux.ru> 4.6.1r-alt6
- revert mc-4.6.1a-rh-promptfix.patch (buggy)
- fix promt (mc-4.6.1-alt-promptfix.patch) (#8310)

* Mon Oct 16 2006 Igor Zubkov <icesik@altlinux.ru> 4.6.1r-alt5
- add catdoc as RTF viewer (#4443)

* Mon Oct 16 2006 Igor Zubkov <icesik@altlinux.ru> 4.6.1r-alt4
- add nemerle syntax (#10104)

* Thu Sep 15 2005 Kachalov Anton <mouse@altlinux.ru> 4.6.1r-alt3
- Updated file-type coloring (X-Stranger)
- Bugfixes:
    + Menu-file fix (#5007)
    + PO translation (#7582, patch from php-coder@)
    + 7zip extension support (#7962)

* Sat Aug 13 2005 Kachalov Anton <mouse@altlinux.ru> 4.6.1r-alt2
- Added file-type coloring (thanks to X-Stranger <x@interfax.by>)

* Mon Aug 01 2005 Kachalov Anton <mouse@altlinux.ru> 4.6.1r-alt1
- Release 4.6.1

* Mon Jul 11 2005 Kachalov Anton <mouse@altlinux.ru> 4.6.1a.20050606-alt1
- 4.6.1a
- New patches (RH):
    + updated UTF8
    + fish upload
    + command prompt fix

* Wed Jun 01 2005 Kachalov Anton <mouse@altlinux.ru> 4.6.1.20050601-alt1
- Bugfixes:
    + force subshell execution, forwardport (#6952)
    + question symbols in xterm title bar (#6945)
    + partially fixed codepage conversion (#6944)

* Thu May 19 2005 Kachalov Anton <mouse@altlinux.ru> 4.6.1.20050518-alt1
- 4.6.1 from CVS: 18 May 2005
- Bugfixes:
    + aterm generates symbols instead of cursor movement (#4548)
    + big files from zip archive doesn't show (#5428)
    + files copy failed via remote shell (#6806)
    + play video with mplayer or xine (#5052)
    + broken Grey Enter key (#1214)
    + missed menu entry (#5007)
- Added:
    + UTF-8 support
    + SynCE VFS

* Tue Jun 29 2004 Kachalov Anton <mouse@altlinux.ru> 4.6.0-alt9
- fix iso extension (#4366, #4536)
- additional file types handling (#3334, #4443)
- fix date parsing in vfs (#4545)

* Wed Apr 07 2004 Kachalov Anton <mouse@altlinux.ru> 4.6.0-alt8
- fix security bugs (buffer overflow) and backport from CVS version.

* Mon Jan 19 2004 Stanislav Ievlev <inger@altlinux.org> 4.6.0-alt7.1
- fix security bugs.

* Mon Nov 03 2003 Kachalov Anton <mouse@altlinux.ru> 4.6.0-alt7
- added .hh and .hpp files to Syntax highlight

* Wed Sep 03 2003 Kachalov Anton <mouse@altlinux.ru> 4.6.0-alt6
- removed requires for cdrecord, cdparanoia and wget

* Mon Jul 21 2003 Kachalov Anton <mouse@altlinux.ru> 4.6.0-alt5
- using links instead of lynx for viewing html
- added help file in cp1251 (#0002685)
- added DN-like coloration (thanks to Peter V. Chernikoff)

* Tue Apr 29 2003 Kachalov Anton <mouse@altlinux.ru> 4.6.0-alt4
- added ISO extfs

* Tue Feb 18 2003 Kachalov Anton <mouse@altlinux.ru> 4.6.0-alt3
- bugfix:
    + russian char in cp1251 locale not displayed (#000271)
    + problem with cp866 (#0002023)

* Mon Feb 10 2003 Kachalov Anton <mouse@altlinux.ru> 4.6.0-alt2
- bugfix: mc doesn't give hostname to the terminal
- proper recognition of man pages
- wrapper creation temp dir on first startup fix

* Thu Jan 06 2003 Kachalov Anton <mouse@altlinux.ru> 4.6.0-alt1
- new version
- remove mcserv
- remove smbfs
- bugfix:
    + Eterm is considered to be a dumb terminal (#0000851)
    + doen't look inside ~/.terminfo (#0000907)
    + mc crashes on linux console when gpm server closes connection (#0001123)
    + not copyied russian char to command line (#0001208)
    + locale error (#0001550)
    + hostname resolve (#0002010)

* Thu Dec 26 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.6.0-alt0.5.5
- Fixed wrapper

* Thu Nov 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.6.0-alt0.5
- Rebuilt with latest CVS changes

* Thu Oct 31 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.6.0-alt0.4
- Rebuilt back with slang library

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.6.0-alt0.3
- Fixed gpm bug
- Rebuilt with latest CVS changes
- Rebuilt with ncurses library
- Turn on smbfs support

* Tue Sep 03 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.6.0-alt0.2
- Rebuild with latest CVS changes
- Fixed restoring mouse events under xterm

* Wed Aug 27 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.6.0-alt0.1
- Rebuild with latest CVS changes
- Fixed some bugs
- Version now 4.6.0pre1a

* Thu Aug 15 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.5.99a-alt3
- Rebuild with latest CVS changes

* Wed Jul 17 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.5.99a-alt2
- Rebuild with fixed libgpm

* Tue Jul 16 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.5.99a-alt1
- Build from snapshot
- Package gmc now removed
- Some spec cleanup

* Tue Apr 16 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.5.55-alt7
- Added --enable-largefile, thnx to sav

* Mon Apr 15 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.5.55-alt6
- Removed umask patch

* Thu Feb 07 2002 AEN <aen@logic.ru> 4.5.55-alt5
- LANGUAGE variable not used anymore
- belarussian translation added
- build requires regenerated
- uk_UA.CP1251 tips added

* Tue Sep 24 2001 Kachalov Anton <mouse@altlinux.ru> 4.5.55-alt4
- Updated Russian translation - thanx to Andrew Borodin

* Tue Sep 11 2001 Konstantin Volckov <goldhead@altlinux.ru> 4.5.55-alt3
- Updated Russian translation - thanx to Andrew Borodin

* Sun Sep 09 2001 Konstantin Volckov <goldhead@altlinux.ru> 4.5.55-alt2
- Fix mc.hint for CP1251 locle
- Now we call links when view html's

* Tue Sep 04 2001 Konstantin Volckov <goldhead@altlinux.ru> 4.5.55-alt1
- 4.5.55
- Use recoding support fom mc
- Fixed Requires
- Show backup files by default now is on

* Thu Jun 21 2001 Konstantin Volckov <goldhead@linux.ru.net> 4.5.54-alt3.1
- Updated recode patch - added editor support & view search support

* Mon Jun 18 2001 Konstantin Volckov <goldhead@linux.ru.net> 4.5.54-alt3
- Fix Full 8 bit input to be on by default

* Thu Jun 14 2001 Konstantin Volckov <goldhead@linux.ru.net> 4.5.54-alt2
- Fixed cdparanoia requires
- Some spec cleanup

* Mon Jun 4 2001 Konstantin Volckov <goldhead@linux.ru.net> 4.5.54-alt1
- New mc version - 4.5.54
- Some new Cooker patches
- Fixed sources (bzip2 -> gz)
- Fixed recode patch
- Removed all entries in changelog before 01012001
- Added umask settings

* Thu Mar 15 2001 Konstantin Volckov <goldhead@linux.ru.net> 4.5.51-ipl11mdk
- Added recode patch
- Fix build with glibc-2.2.2 (time patch)
- Fixed name of po file
- Fixed build with new gtk
