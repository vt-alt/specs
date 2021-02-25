# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define xterm_stdflags \\\
	--with-app-defaults=%_sysconfdir/X11/app-defaults \\\
	--with-utempter \\\
	--enable-warnings \\\
	--enable-wide-chars \\\
	--enable-dec-locator \\\
	--enable-narrowproto \\\
	--disable-full-tgetent \\\
	--disable-echo \\\
	--enable-256-color \\\
	--enable-doublechars \\\
	--with-icondir=%_iconsdir

%define xterm_expflags \\\
  --with-neXtaw          \\\
  --enable-dabbrev       \\\
  --enable-double-buffer \\\
  --enable-exec-xterm    \\\
  --enable-load-vt-fonts \\\
  --enable-logfile-exec  \\\
  --enable-logging       \\\
  --enable-readline-mouse\\\
  --enable-regis-graphics\\\
  --enable-toolbar

Name: xterm
Version: 366
Release: alt1

Summary: A standard terminal emulator for the X Window System
Summary(ru_RU.UTF8): Стандартный эмулятор терминала для X Window System
Url: http://invisible-island.net/xterm/
License: MIT
Group: Terminals

Source0: ftp://invisible-island.net/%name/%name-%version.tgz
Source1: uxterm

Patch0001: 0001-xterm-alt-render.patch
Patch0002: 0002-xterm-alt-utempter.patch
Patch0003: 0003-xterm-alt-tinfo.patch
Patch0004: 0004-xterm-alt-perms.patch
Patch0005: 0005-xterm-alt-deffont.patch
Patch0006: 0006-xterm-alt-makefile-install.patch
Patch0007: 0007-xterm-alt-disable-report_win_label.patch
Patch0008: 0008-xterm-alt-i18n.patch
Patch0009: 0009-xterm-alt-colors.patch
Patch0010: 0010-xterm-alt-back_old_behavior_for_modifyFunctionKeys.patch
Patch0011: 0011-xterm-alt-appdef.patch
Patch0012: 0012-xterm-alt-man_suffix.patch
Patch0013: 0013-xterm-alt-translate-update-desktop.patch

Provides: xvt, %_bindir/xvt
Requires(pre): libutempter >= 1.0.7, alternatives >= 0.3.5-alt1
BuildRequires(pre): alternatives groff-base imake libXaw-devel libXft-devel libncurses-devel libutempter-devel libxkbfile-devel xorg-cf-files
# Automatically added by buildreq on Wed Nov 14 2012
# optimized out: alternatives fontconfig fontconfig-devel gnu-config libICE-devel libSM-devel libX11-devel libXmu-devel libXrender-devel libXt-devel libfreetype-devel libtinfo-devel pkg-config xorg-kbproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: ctags groff-base imake libXaw-devel libXext-devel libXft-devel libncurses-devel libneXtaw-devel libutempter-devel libxkbfile-devel xorg-cf-files

Requires: /etc/X11/app-defaults

%description
The XTerm program is the standard terminal emulator for the X Window System.
It provides DEC VT102/VT220 and Tektronix 4014 compatible terminals for
programs that can't use the window system directly.  If the underlying
operating system supports terminal resizing capabilities (for example,
the SIGWINCH signal in systems derived from 4.3bsd), xterm will use
the facilities to notify programs running in the window whenever it
is resized.

%package experimental
Group: Terminals
Summary: experimental version of xterm
%description experimental
XTerm build with some experimental/unsafe features:
%xterm_expflags

%prep
%setup

install -pm755 %_sourcedir/uxterm .

%patch0001 -p2
%patch0002 -p2
%patch0003 -p2
%patch0004 -p2
%patch0005 -p2
%patch0006 -p2
%patch0007 -p2
%patch0008 -p2
%patch0009 -p2
%patch0010 -p2
%patch0011 -p2
%patch0012 -p2
%patch0013 -p2

sed -i 's|^Exec=xterm|& -name XTerm|' %name.desktop
sed -i 's|_48x48||' *.desktop
sed -i '/^Comment=/s/$/ (UTF8 forced)/' uxterm.desktop

# Remove deprecated Encoding key
sed -i '/^Encoding=/d' *.desktop

%build
export ac_cv_path_XTERM_PATH=%_bindir/%name
# Rebuild this
touch ctlseqs.ms

%configure %xterm_stdflags
%make_build all ctlseqs.txt
cp xterm xterm.std
xz ctlseqs.txt

make distclean
%configure %xterm_stdflags %xterm_expflags
%make_build
cp xterm xterm.extd
cp xterm.std xterm

%install
%makeinstall_std
install xterm.extd %buildroot%_bindir/XTerm
install -D %name.desktop %buildroot/%_desktopdir/%name.desktop

for n in xterm xterm-color; do
  for s in 48 32; do
    install -D icons/${n}_${s}x${s}.xpm %buildroot%_iconsdir/hicolor/${s}x${s}/apps/$n.xpm
  done
  install -D icons/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
done

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt	%_bindir/xterm	40
EOF

%files
%doc README ctlseqs.txt.* %name.log.html tektests vttests
%attr(2711,root,utempter) %_bindir/%name
%_bindir/uxterm
%_bindir/koi8rxterm
%_bindir/resize
%_man1dir/resize.1.*
%_man1dir/%name.1.*
%_man1dir/uxterm.1.*
%_man1dir/koi8rxterm.1.*
%config(noreplace) %_sysconfdir/X11/app-defaults/*
%_altdir/%name
%_desktopdir/*.desktop
%_pixmapsdir/*.xpm
%_iconsdir/hicolor/*/apps/xterm*

%files experimental
%attr(2711,root,utempter) %_bindir/XTerm

%changelog
* Wed Feb 24 2021 Fr. Br. George <george@altlinux.ru> 366-alt1
- Autobuild version bump to 366
- CVE-2021-27135 (Closes: #39725)

* Thu Jan 28 2021 Fr. Br. George <george@altlinux.ru> 363-alt1
- Autobuild version bump to 363

* Thu Nov 26 2020 Fr. Br. George <george@altlinux.ru> 362-alt1
- Autobuild version bump to 362

* Wed Sep 30 2020 Fr. Br. George <george@altlinux.ru> 360-alt1
- Autobuild version bump to 360

* Wed Aug 26 2020 Fr. Br. George <george@altlinux.ru> 359-alt1
- Autobuild version bump to 359

* Sun May 31 2020 Fr. Br. George <george@altlinux.ru> 356-alt1
- Autobuild version bump to 356
- Update patches

* Thu Jan 23 2020 Fr. Br. George <george@altlinux.ru> 352-alt1
- Autobuild version bump to 352
- Patch to dump XHTML and SVG without "floats with comma" bug

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 350-alt1
- Autobuild version bump to 350

* Thu Oct 17 2019 Fr. Br. George <george@altlinux.ru> 349-alt1
- Autobuild version bump to 349
- Update patches

* Sun Apr 28 2019 Fr. Br. George <george@altlinux.ru> 344-alt1
- Autobuild version bump to 344

* Thu Feb 07 2019 Fr. Br. George <george@altlinux.ru> 343-alt1
- Autobuild version bump to 343

* Thu Nov 15 2018 Fr. Br. George <george@altlinux.ru> 337-alt1
- Autobuild version bump to 337

* Thu Nov 01 2018 Pavel Moseev <mars@altlinux.org> 333-alt2
- Updated translations in desktop file

* Wed May 23 2018 Fr. Br. George <george@altlinux.ru> 333-alt1
- Autobuild version bump to 333
- Cleanup buildreq

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 331-alt1
- Autobuild version bump to 331

* Fri Aug 04 2017 Fr. Br. George <george@altlinux.ru> 330-alt1
- Autobuild version bump to 330

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 327-alt1
- Autobuild version bump to 327

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 325-alt1
- Autobuild version bump to 325

* Wed Mar 09 2016 Fr. Br. George <george@altlinux.ru> 323-alt1
- Autobuild version bump to 323

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 320-alt1
- Autobuild version bump to 320

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 318-alt1
- Autobuild version bump to 318

* Tue Feb 03 2015 Fr. Br. George <george@altlinux.ru> 314-alt1
- Autobuild version bump to 314
- Drop obsoleted patch

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 312-alt1
- Autobuild version bump to 312

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 311-alt1
- Autobuild version bump to 311

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 310-alt1
- Autobuild version bump to 310

* Tue Jul 01 2014 Fr. Br. George <george@altlinux.ru> 308-alt1
- Autobuild version bump to 308
- Fix "-class ..." segfault by dropping UXTerm class enforce patch

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 306-alt1
- Autobuild version bump to 306

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 304-alt1
- Autobuild version bump to 304

* Thu Apr 10 2014 Fr. Br. George <george@altlinux.ru> 303-alt1
- Autobuild version bump to 303
- Fix patch

* Tue Jan 28 2014 Fr. Br. George <george@altlinux.ru> 301-alt1
- Autobuild version bump to 301

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 300-alt1
- Autobuild version bump to 300

* Wed Oct 09 2013 Fr. Br. George <george@altlinux.ru> 297-alt2
- Shorten passedPty to fit PTYCHARLEN (Closes: #29431)

* Mon Oct 07 2013 Fr. Br. George <george@altlinux.ru> 297-alt1
- Autobuild version bump to 297

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 296-alt1
- Autobuild version bump to 296

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 293-alt1
- Autobuild version bump to 293

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 292-alt1
- Autobuild version bump to 292

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 291-alt1
- Autobuild version bump to 291

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 290-alt1
- Autobuild version bump to 290

* Wed Jan 16 2013 Fr. Br. George <george@altlinux.ru> 288-alt1
- Autobuild version bump to 288
- Patches fixed

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 287-alt1
- Autobuild version bump to 287

* Mon Nov 12 2012 Fr. Br. George <george@altlinux.ru> 286-alt1
- Autobuild version bump to 286
- Patch fix
- Use gear-am/gear-format-patch
- Build XTerm, an exprerimental version of xterm

* Tue Oct 23 2012 Fr. Br. George <george@altlinux.ru> 284-alt1
- Autobuild version bump to 284
- Patches unified and adapted

* Thu Jul 26 2012 Fr. Br. George <george@altlinux.ru> 281-alt1
- Autobuild version bump to 281
- Native icons added

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 279-alt1
- Autobuild version bump to 279

* Sun Jan 22 2012 Fr. Br. George <george@altlinux.ru> 278-alt1
- Autobuild version bump to 278

* Fri Jan 13 2012 Fr. Br. George <george@altlinux.ru> 277-alt1
- Autobuild version bump to 277
- Fix patches

* Mon Sep 12 2011 Fr. Br. George <george@altlinux.ru> 275-alt1
- Autobuild version bump to 275
- Fix patch

* Thu Sep 01 2011 Fr. Br. George <george@altlinux.ru> 273-alt1
- Autobuild version bump to 273

* Wed Jul 20 2011 Fr. Br. George <george@altlinux.ru> 271-alt1
- Autobuild version bump to 271

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 270-alt1
- Autobuild version bump to 270

* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 269-alt1
- Autobuild version bump to 269

* Tue Feb 15 2011 Fr. Br. George <george@altlinux.ru> 268-alt1
- Autobuild version bump to 268

* Wed Dec 08 2010 Fr. Br. George <george@altlinux.ru> 267-alt1
- Autobuild version bump to 267

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 266-alt1
- Autobuild version bump to 266

* Thu Oct 21 2010 Fr. Br. George <george@altlinux.ru> 264-alt1
- Autobuild version bump to 264
- Backspace is sending "stty erase" by default (closes: #21731)

* Tue Sep 21 2010 Fr. Br. George <george@altlinux.ru> 262-alt1
- Version up

* Wed Aug 25 2010 Fr. Br. George <george@altlinux.ru> 261-alt1
- Version up

* Thu Apr 08 2010 Fr. Br. George <george@altlinux.ru> 256-alt1
- Version up

* Tue Feb 16 2010 Fr. Br. George <george@altlinux.ru> 255-alt1
- Version up

* Thu Jan 07 2010 Slava Semushin <php-coder@altlinux.ru> 254-alt1
- Updated to 254

* Thu Dec 10 2009 Slava Semushin <php-coder@altlinux.ru> 253-alt1
- Updated to 253

* Wed Nov 11 2009 Slava Semushin <php-coder@altlinux.ru> 251-alt1
- Updated to 251

* Wed Oct 14 2009 Slava Semushin <php-coder@altlinux.ru> 250-alt1
- Updated to 250

* Fri Oct 02 2009 Slava Semushin <php-coder@altlinux.ru> 249-alt1
- Updated to 249
  + Also fixed crash during scrolling (Closes: #21743)

* Sat Sep 12 2009 Slava Semushin <php-coder@altlinux.ru> 248-alt1
- Updated to 248

* Wed Sep 02 2009 Slava Semushin <php-coder@altlinux.ru> 247-alt1
- Updated to 247

* Mon Aug 17 2009 Slava Semushin <php-coder@altlinux.ru> 246-alt1
- Updated to 246
  + Also fixed ColorBDMode which was broken since 244 (Closes: #21056)

* Thu Aug 13 2009 Slava Semushin <php-coder@altlinux.ru> 245-alt1
- Updated to 245

* Mon Aug 10 2009 Slava Semushin <php-coder@altlinux.ru> 244-alt1
- Updated to 244
- Added requires to /etc/X11/app-defaults directory
  (Reported by Eugene Ostapets aka eostapets@)

* Thu Apr 02 2009 Slava Semushin <php-coder@altlinux.ru> 243-alt1
- Updated to 243

* Mon Feb 23 2009 Slava Semushin <php-coder@altlinux.ru> 242-alt1
- Updated to 242

* Sat Jan 31 2009 Slava Semushin <php-coder@altlinux.ru> 241-alt1
- Updated to 241

* Sun Jan 11 2009 Slava Semushin <php-coder@altlinux.ru> 239-alt1
- Updated to 239
- Fixed build in host system

* Wed Dec 31 2008 Slava Semushin <php-coder@altlinux.ru> 238-alt1
- Updated to 238
- Release fixes CVE-2008-2383 (see debian bug #510030 for details)

* Fri Dec 05 2008 Slava Semushin <php-coder@altlinux.ru> 237-alt3
- Removed obsolete %%register_alternatives/%%unregister_alternatives calls

* Tue Nov 18 2008 Slava Semushin <php-coder@altlinux.ru> 237-alt2
- Rebuild with libXaw.so.7
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)

* Mon Sep 15 2008 Slava Semushin <php-coder@altlinux.ru> 237-alt1
- Updated to 237

* Wed Aug 06 2008 Slava Semushin <php-coder@altlinux.ru> 236-alt1
- Updated to 236
- Removed Encoding key from desktop files (noted by repocop)

* Mon Apr 21 2008 Slava Semushin <php-coder@altlinux.ru> 235-alt1
- Updated to 235

* Sun Mar 16 2008 Slava Semushin <php-coder@altlinux.ru> 234-alt2
- Enable Utf8Title resource by default (#12776)

* Sat Mar 08 2008 Slava Semushin <php-coder@altlinux.ru> 234-alt1
- Updated to 234

* Mon Feb 25 2008 Slava Semushin <php-coder@altlinux.ru> 233-alt1
- Updated to 233

* Wed Feb 13 2008 Slava Semushin <php-coder@altlinux.ru> 232-alt1
- Updated to 232

* Tue Jan 08 2008 Slava Semushin <php-coder@altlinux.ru> 231-alt1
- Updated to 231

* Wed Jan 02 2008 Slava Semushin <php-coder@altlinux.ru> 230-alt1
- Updated to 230

* Mon Sep 10 2007 Slava Semushin <php-coder@altlinux.ru> 229-alt2
- Fixed build with desktop-file-utils-0.14 (correct desktop files)

* Mon Aug 13 2007 Slava Semushin <php-coder@altlinux.ru> 229-alt1
- Updated to 229
  (thanks to Michael Shigorin aka mike@ for notifying about new version)

* Mon Aug 06 2007 Slava Semushin <php-coder@altlinux.ru> 228-alt2
- Enable metaSendsEscape by default. It allows to work Alt-<key>
  combination (re-fixed #595)

* Mon Jul 23 2007 Slava Semushin <php-coder@altlinux.ru> 228-alt1
- Updated to 228

* Sun Jul 01 2007 Slava Semushin <php-coder@altlinux.ru> 227-alt1
- Updated to 227
- New maintainer
- Removed our icons and use icons from upstream
- Replaced menu file by desktop files from upstream
- Removed paste_in_koi8-r_fix patch (it was taken from upstream)
- Adapted patches
- Spec cleanup: use %%name macros in url in Source tag

* Thu Jun 21 2007 Slava Semushin <php-coder@altlinux.ru> 225-alt1.2
- NMU
- Fixed paste in koi8-r locale (#11725, deb #420974)

* Wed Apr 25 2007 Damir Shayhutdinov <damir@altlinux.ru> 225-alt1.1
- This release is based on Slava Semushin <php-coder> spec.

* Tue Apr 24 2007 Slava Semushin <php-coder@altlinux.ru> 225-alt1
- NMU
- Updated to 225 (which also fixes bug #11067)
- Adapted patches and modifying deffont patch
  (thnx vsu@ for detailed explanation how do this)

* Sat Mar 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 224-alt2.1
- NMU based on Slava Semushin <php-coder> spec.

* Tue Mar 13 2007 Slava Semushin <php-coder@altlinux.ru> 224-alt2
- NMU
- Back old behaviour for modifyFunctionKeys resource (#11002)
- Changed Packager to Damir Shayhutdinov aka damir@
- Minor rewording in %%changelog (thnx to ldv@)

* Sat Feb 24 2007 Damir Shayhutdinov <damir@altlinux.ru> 224-alt1.1
- NMU based on Slava Semushin <php-coder> spec.

* Tue Feb 20 2007 Slava Semushin <php-coder@altlinux.ru> 224-alt1
- NMU
- Updated to 224

* Sat Dec 02 2006 Slava Semushin <php-coder@altlinux.ru> 222-alt1
- NMU
- Updated to 222
- Removed metaaltfix patch (not needed anymore)
- Adapted all patches
- Enable _unpackaged_files_terminate_build
- Spec cleanup:
  + Renumber all patches
  + Replace all %%_x11* macroses to macroses without x11 prefixes
  + Do not try to remove files with ".orig" suffix: no longer needed
    after regnerating all patches for new upstream version
  + Removed chmod -R u+w: not needed too
  + Removed LDFLAGS from make: --as-needed now enabled by default
  + Running make with --no-print-directory and --silent options
  + Removed --enable-freetype flag for configure (enabled by default)
  + Added --disable-echo flag to configure
  + More strict names in %%files section
  + s/%%setup -q/%%setup/

* Thu Mar 23 2006 Dmitry V. Levin <ldv@altlinux.org> 211-alt1
- Updated to 211.
- Corrected typo in menu entry (#9299).

* Wed Mar 01 2006 Dmitry V. Levin <ldv@altlinux.org> 209-alt1
- Updated to 209.
- Relocated from /usr/X11R6 to /usr (#9101).

* Thu Jun 09 2005 Dmitry V. Levin <ldv@altlinux.org> 202-alt2
- Changed default UXTerm font to meet XTerm font defaults.

* Wed Jun 08 2005 Dmitry V. Levin <ldv@altlinux.org> 202-alt1
- Updated to 202.
- Updated patches.
- Set default class to UXTerm when run with utf8 codeset (#7026).
- Converted alternatives config files to new format (0.2.0).

* Tue Oct 05 2004 Dmitry V. Levin <ldv@altlinux.org> 196-alt1
- Updated to 196.
- Updated patches.

* Tue Jun 29 2004 Dmitry V. Levin <ldv@altlinux.org> 191-alt3
- Reverted color change in xterm-180, to fix (#4538):
  + use color resource setting from Debian package
    for xterm VT100 widget, since the choice of blues
    provides better contrast.

* Thu Jun 10 2004 Dmitry V. Levin <ldv@altlinux.org> 191-alt2
- Honor locale in default charClass (#1879).

* Thu Jun 10 2004 Dmitry V. Levin <ldv@altlinux.org> 191-alt1
- Updated to 191.
- Updated patches.

* Wed May 28 2003 Dmitry V. Levin <ldv@altlinux.org> 179-alt1
- Updated to 179.
- Fixed to build with new -lXft.

* Mon Apr 14 2003 Stanislav Ievlev <inger@altlinux.ru> 177-alt2.1
- move to new alternatives scheme

* Wed Mar 26 2003 Dmitry V. Levin <ldv@altlinux.org> 177-alt2
- Disabled report_win_label support (CAN-2003-0063).

* Mon Mar 24 2003 Dmitry V. Levin <ldv@altlinux.org> 177-alt1
- Updated to 177.

* Fri Feb 28 2003 Dmitry V. Levin <ldv@altlinux.org> 174-alt1
- Updated to 174.
- Enabled freetype support (#0002298).

* Tue Feb 18 2003 Dmitry V. Levin <ldv@altlinux.org> 173-alt1
- Updated to 173.
- Disabled logging support.

* Tue Dec 24 2002 Dmitry V. Levin <ldv@altlinux.org> 170-alt2
- Rebuilt with libutempter-1.1.0.

* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 170-alt1
- 170, updated patches.
- Fixed uxterm wrapper.

* Thu Sep 26 2002 Dmitry V. Levin <ldv@altlinux.org> 167-alt3
- Fixed logger.

* Tue Sep 24 2002 Dmitry V. Levin <ldv@altlinux.org> 167-alt2
- Drop effective group ID, too (but save it for utempter).

* Tue Sep 03 2002 Dmitry V. Levin <ldv@altlinux.org> 167-alt1
- 167, updated patches.
- Fixed metaalt fix (#0000595).
- Added ctlseqs.ms and %name.log* to documentation

* Sat Jun 29 2002 Dmitry V. Levin <ldv@altlinux.org> 166-alt2
- Patched to link with libtinfo.

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 166-alt1
- 166.
- Updated dependencies.

* Tue Jan 08 2002 Dmitry V. Levin <ldv@alt-linux.org> 165-alt1
- 165.
- Fixed tmp files handling.
- Fixed build to use ncurses instead of termcap.
- Fixed out libelf-devel requirement for build.
- Changed alternative for xvt (priority=20).
- Utempter support: use XDisplayString as remote hostname.
- Built with DECterm Locator support enabled.
- Cleanup for non-alt patches and docs.
- Added xvt to provides list.

* Tue Oct 16 2001 Dmitry V. Levin <ldv@alt-linux.org> 161-alt1
- 161.
- Specfile cleanup.
- Built with new utempter protocol support enabled.
- Built with logging support enabled (ok for sgid-utempter program).

* Tue Sep 11 2001 Konstantin Volckov <goldhead@altlinux.ru> 158-alt1
- Rebuilt with new XFree86
- New version 158
- Some spec cleanup

* Fri Jun 8 2001 AEN <aen@logic.ru> 156-alt4
- XFree requires removed

* Wed Jun 6 2001 AEN <aen@logic.ru> 156-alt3
- xft restored

* Wed Jun 6 2001 AEN <aen@logic.ru> 156-alt2
- xft patch temporary removed
- bidi patch temporary removed

* Tue Jun 5 2001 AEN <aen@logic.ru> 156-alt1
- build for Sisyphus

* Wed May 09 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 156-3mdk
- actually enabled support for use of locales and bidi

* Tue May 08 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 156-2mdk
- add bidirectional support (ie for semitic languages)

* Tue May 01 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 156-1mdk
- new release
- fix render test

* Mon Apr 23 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 155-1mdk
- newrelease

* Thu  Apr 12 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 154-1mdk
- New and shiny 154 bumped into cooker.

* Sat Mar 31 2001 Frederic Lepied <flepied@mandrakesoft.com> 152-3mdk
- enable unicode

* Thu Mar 29 2001 Frederic Lepied <flepied@mandrakesoft.com> 152-2mdk
- recompiled to activate the Render extension.

* Thu Mar 15 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 152-1mdk
- new release

* Mon Mar 12 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 151-1mdk
- new version

* Thu Feb  8 2001 Pixel <pixel@mandrakesoft.com> 150-2mdk
- add as alternative xvt

* Sun Dec 31 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 150-1mdk
- new and shiny source.

* Tue Dec 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 149-1mdk
- Fix compilation with last XFree.
- 149.

* Thu Nov 16 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 148-1mdk
- new release

* Fri Aug 25 2000 David BAUDENS <baudens@mandrakesoft.com> 144-2mdk
- Fix Menu entry (fix name, add longtitle and provide icons)
- Fix Sumary and Description
- Fix %%doc

* Thu Aug 24 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 144-1mdk
- s|143|144|.

* Mon Aug 21 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 143-1mdk
- new and shiny version.

* Sun Aug 20 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 142-1mdk
- even more use of the _menudir macro.
- a new and shiny version.

* Thu Aug 17 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 141-2mdk
- fix usage of macro before its definition: you don't get any chickens before
  they hatch.!

* Tue Aug 15 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 141-1mdk
- s|140|141|.

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 140-2mdk
- automatically added BuildRequires

* Mon Jul 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 140-1mdk
- more macros (_menudir and the like : geoffroy sucks:-) )
- new release

* Mon Jul 24 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 139-2mdk
- fix silly typo in summary

* Sat Jul 22 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 139-1mdk
- xterm source has moved
- new version
- some macro-ization

* Fri May  5 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 131-4mdk
- remove full path of icon in menu entry

* Tue Apr  4 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 131-3mdk
- Set menu in /Terminals.

* Sat Apr  1 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 131-2mdk
- Requires: XFree86 >= 3.3.6-13mdk to avoid conflicts.

* Fri Mar 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 131-1mdk
- Menu.
- First version.
- Fix meta-alt keys (Hey hey fred ;)).
