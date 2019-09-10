Name: blackbox
Version: 0.74
Release: alt1

Summary: A Window Manager for the X Window System
License: BSD-style
Group:   Graphical desktop/Other
URL:     https://github.com/bbidulock/blackboxwm
Source0: https://github.com/bbidulock/blackboxwm/releases/download/%version/%name-%version.tar.xz
Source1: %name.menu-method
Source2: %name.menu
Source3: %name-16.png
Source4: %name-32.png
Source5: %name-48.png
Source6: %name-64.png
Source7: %name.wmsession
Source8: %name.alternatives
Source9: %name-gencat-wrapper
Source10: blackbox.desktop
Source11: ru.po.fixed

Patch0: blackbox-0.74-alt-link.patch
Patch10: blackbox-0.70.1-alt-style.patch

# Automatically added by buildreq on Tue Mar 12 2013
# optimized out: alternatives fontconfig fontconfig-devel gnu-config libX11-devel libXrender-devel libfreetype-devel libstdc++-devel pkg-config xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ imake libXext-devel libXft-devel xorg-cf-files

%description
This is a window manager for X.  It is similar in many respects to
such popular packages as Window Maker, Enlightenment, and FVWM2.  You
might be interested in this package if you are tired of window managers
that are a heavy drain on your system resources, but you still want
an attractive and modern-looking interface.

The best part of all is that this program is coded in C++, so it
is even more attractive "under the hood" than it is in service -- no
small feat.

If none of this sounds familiar to you, or you want your computer to
look like Windows 98, you probably don't want this package.

%package devel
Summary: Blackbox Toolbox library for writing small applications
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains the Blackbox Toolbox files, headers and static library
of the utility class library for writing small applications.

%prep
%setup -q
%patch0 -p1
#patch10 -p0

# %%{__global_ldflags} wrongly passed to pkgconfig file
sed -i 's|@LDFLAGS@||g' lib/libbt.pc.in

#iconv -f utf-8 -t koi8-r ./po/ru.po | iconv -t iso-8859-5 -f koi8-r | iconv -f koi8-r -t utf-8 > ./po/ru.po.fixed && edit manually
install -p %SOURCE11 ./po/ru.po
rm -f ./po/ru.gmo

install -p %SOURCE9 ./gencat-wrapper

%build
export gencat_cmd="`pwd`/gencat-wrapper"
autoreconf -fisv
%configure \
    --enable-shared \
    --disable-static \
    --sysconfdir=%_sysconfdir/X11/%name \
    --enable-nls

%make_build DEFAULT_MENU=%_sysconfdir/X11/%name/%name-menu

%install
%make_install DESTDIR=%buildroot install

mv %buildroot%_bindir/bsetbg   %buildroot%_bindir/bsetbg-%name
mv %buildroot%_bindir/bsetroot %buildroot%_bindir/bsetroot-%name
mv %buildroot%_man1dir/bsetbg.1 %buildroot%_man1dir/bsetbg-%name.1
mv %buildroot%_man1dir/bsetroot.1 %buildroot%_man1dir/bsetroot-%name.1

install -pD -m755 %SOURCE1 %buildroot%_sysconfdir/menu-methods/%name
install -pD -m644 %SOURCE2 %buildroot%_menudir/%name
install -pD -m644 %SOURCE3 %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE4 %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE5 %buildroot%_liconsdir/%name.png
install -pD -m644 %SOURCE6 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -pD -m644 %SOURCE7 %buildroot%_sysconfdir/X11/wmsession.d/07%name
install -pD -m644 %SOURCE8 %buildroot%_altdir/%name

install -pD -m644 /dev/null %buildroot%_sysconfdir/X11/%name/%name-menu

# Install the desktop entry
install -pD -m644 %SOURCE10 %buildroot%_datadir/xsessions/blackbox.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COMPLIANCE ChangeLog* COPYING README* TODO
%_bindir/blackbox
%_bindir/bsetbg*
%_bindir/bsetroot*
%_bindir/bstyleconvert
%_man1dir/*
%dir %_datadir/%name
%_datadir/%name/
%_libdir/libbt.so.*
%_datadir/xsessions/blackbox.desktop
%lang(fr) %_mandir/fr/man?/*
%lang(ja) %_mandir/ja/man?/*
%lang(nl) %_mandir/nl/man?/*
%lang(sl) %_mandir/sl/man?/*
# alt specific
%_menudir/*
%config(noreplace) %_sysconfdir/menu-methods/*
%config %_sysconfdir/X11/wmsession.d/*
%dir %_sysconfdir/X11/%name
%ghost %_sysconfdir/X11/%name/%name-menu
%_altdir/%name
%_iconsdir/hicolor/??x??/apps/*.png

%files devel
%_libdir/libbt.so
%dir %_includedir/bt
%_includedir/bt/*.hh
%_pkgconfigdir/libbt.pc

%changelog
* Wed Sep 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1
- new version

* Wed Sep 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.70.1-alt4
- fixed man alternatives

* Tue Mar 12 2013 Igor Zubkov <icesik@altlinux.org> 0.70.1-alt3
- buildreq

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.70.1-alt2
- resurrected from orphaned
- added devel subpackage

* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 0.70.1-alt1.1
- fix build

* Mon Mar 31 2008 Sergey Balbeko <balbeko@altlinux.org> 0.70.1-alt1
- new version.
- nls & def.theme patched

* Wed Mar 08 2006 Igor Zubkov <icesik@altlinux.ru> 0.65.0-alt6
- fix build
- buildreq

* Wed Nov 23 2005 Igor Zubkov <icesik@altlinux.ru> 0.65.0-alt5
- change %%_libdir/menu/ to %%_menudir/ (possible should fix build for x86_86)
- reallocate binary files from %%_x11bindir/ to %%_bindir/
- likewise for manual pages
- likewise for data files

* Tue Jul 05 2005 Igor Zubkov <icesik@altlinux.ru> 0.65.0-alt4
- clean up spec file -> RPM_BUILD_ROOT to buildroot
- fixed build with gcc-3.4

* Fri Apr 30 2004 Sergey Vlasov <vsu@altlinux.ru> 0.65.0-alt3
- Fixed build breakage on ja_JP and ko_KR translations.
- Include %_sysconfdir/X11/%name directory and the menu file into the package.
- Spec file cleanup.

* Mon Mar 01 2004 Sergey Vlasov <vsu@altlinux.ru> 0.65.0-alt2
- Fixed build with gcc-3.3.
- Fixed BuildRequires.

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 0.65.0-alt1.2
- new alternatives config format

* Tue Mar 25 2003 Stanislav Ievlev <inger@altlinux.ru> 0.65.0-alt1.1
- move to new alternatives scheme

* Mon Oct 21 2002 Sergey Vlasov <vsu@altlinux.ru> 0.65.0-alt1
- Version 0.65.0.
- Dropped obsolete patches.
- Updated exitbutton, fonts, localename patches.
- Build extra encodings for ru_RU.* locales on the fly.
- Added the gencat-wrapper hack to set LC_CTYPE for gencat.
- Patch to treat all locales except C as multibyte (fixes problem with font
  encoding not matching the current charset).
- Updated URLs.
- Fixed license specification (BSD-style, not GPL).

* Thu May 09 2002 Anton Denisov <antden@mail.ru> 0.62.0-alt7
- bset{bg,root} moved to bset{bg,root}-%name and update-alternative'ed
  (to syns with fluxbox package).
  TODO (AEN or I ?):
  - Patch{0,2} remove (out of date);
  - Source{3,4,5} modify and put into tar.bz2;
  - Patch5 fix (add more locales);
  - %%doc add.

* Mon Apr 22 2002 AEN <aen@logic.ru> 0.62.0-alt6
- menu fixed

* Wed Jan 29 2002 AEN <aen@logic.ru> 0.62.0-alt5
- locale name fixed

* Mon Jan 28 2002 AEN <aen@logic.ru> 0.62.0-alt4
- nls patch 

* Thu Jan 24 2002 AEN <aen@logic.ru> 0.62.0-alt3
- Styles menu fixed

* Mon Jan 21 2002 AEN <aen@logic.ru> 0.62.0-alt2
- patch 2 regenerated

* Mon Jan 21 2002 AEN <aen@logic.ru> 0.62.0-alt1
- patches 0,1,2  removed

* Fri Jan 11 2002 AEN <aen@logic.ru> 0.61.1-ipl5mdk
- s/Mandrake/ALTLinux/ in menu method

* Wed Jan 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.61.1-ipl4mdk
- Updated wmsession.d and startup scripts.
- Relocated %_x11dir
- Minor specfile cleanup.

* Tue Dec 05 2000 AEN <aen@logic.ru>
- fonts patch

* Tue Nov 14 2000 David BAUDENS <baudens@mandrakesoft.com> 0.61.1-2mdk
- Fix some macros

* Tue Oct 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.61.1-1mdk
- Arrange menus entry to add Setting box.
- Set default style to Artwiz.
- Make blackbox like the old name blackbox and not BlackBox.
- Add debian translations.
- 0.61.1 (fix gcc2.96).

* Wed Sep 27 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.51.3.1-25mdk
- entry in /etc/X11/wmsession.d
- noreplace

* Mon Sep 25 2000 Daouda Lo <daouda@mandrakesoft.com> 0.51.3.1-24mdk
- add icons for menu system.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.51.3.1-23mdk
- automatically added BuildRequires

* Sun Jul 09 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 0.51.3.1-22mdk
- makeinstall macro
- macroszifications

* Sun May 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.51.3.1-21mdk
- Fix descriptions (RPM & menu)

* Fri Apr 28 2000 dam's <damien@mandrakesoft.com> 0.51.3.1-20mdk
- Added fndSession call.

* Wed Apr  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.51.3.1-19mdk
- Add an exit button just after mandrake menu.

* Tue Apr  4 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.51.3.1-18mdk
- i18n menu support.

* Mon Apr  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.51.3.1-17mdk
- Remove bbdrake stuff (dadou i have pity for you).
- Don't chmod 666 files.
- Add man pages from debian.
- Add i18n patch from debian (hint hint, traductors)
- Adjust groups.

* Mon Jan 03 2000 - David BAUDENS <baudens@mandrakesoft.com>
- 0.51.3.1-16mdk
- Fix typos

* Sat Jan 01 2000 - David BAUDENS <baudens@mandrakesoft.com>
- 0.51.3.1-15mdk
- Add kvideogen in BBDrake

* Tue Dec 28 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Add kdmconfig and kcontrol in BBDrake (thanks Arnold)

* Mon Dec 27 1999 - David BAUDENS <baudens@mandrakesoft.com>
- 0.51.3.1-13mdk
- Fix some typos
- Fix display version

* Mon Dec 20 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix display version

* Sun Dec 19 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix call at bbdrake_kde
- Add AnotherLevel in BBDrake

* Sat Dec 18 1999 - David BAUDENS <baudens@mandrakesoft.com>
- 0.51.3.1-10mdk
  - Replace "drakXconf" by "DrakConf"
- 0.51.3.1-9mdk
  - Cleanup BBDrake
  - Add a blank before "Exit"
  - Add "BlackBox/KDE" in "Desktop/Window Managers"
- 0.51.3.1-8mdk
  - Remove "Sutdown or restart"
  - Add BBDrake_KDE

* Fri Dec 17 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Add DrakXconf in BBDrake, remove XFDrake (call by DrakXcon)
- Change default theme

* Thu Dec 16 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Add a lot of apps in BBDrake
- Fix some typos in BBDrake
- Fix some problems when run as user

* Thu Dec 10 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix Group

* Wed Dec 09 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Build release

* Tue Dec 08 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Add some apps in bbdrake

* Fri Dec 04 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Initial bbdrake

* Fri Nov 20 1999 - David BAUDENS <baudens@mandrakesoft.com>
- First spec
