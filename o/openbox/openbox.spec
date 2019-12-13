%def_without kde
%def_without gnome

Name: openbox
Version: 3.6.1
Release: alt5

Summary: Openbox is a standards compliant, fast, light-weight, extensible window manager
Summary(ru_RU.UTF-8): Openbox это следующий стандартам, быстрый, лёгкий, расширяемый оконный менеджер
License: GPLv2+
Group: Graphical desktop/Other
Url: http://openbox.org/

Source0: %name-%version.tar
Source2: %name-icons.tar.bz2
Source3: %name.menu
Source4: %name.menu-method
Source5: %name.wmsession
Source6: %name-kde.wmsession
Source7: %name-gnome.wmsession

# Debian
Source12: gnome-panel-control.pod
Source13: menu.xml

# ALT Linux
Patch2: openbox-alt-menu-rc.xml.in.patch

# Fedora patch
Patch10: openbox-python3.patch

Requires: lib%name = %version-%release
# for menu "Run" item
Requires: Xdialog

Requires: %_bindir/openbox-session
Requires: %name-themes
Requires: %_libexecdir/openbox-autostart

Conflicts: openbox-extras

BuildPreReq: gettext >= 0.15

# Automatically added by buildreq on Fri Sep 11 2015 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel libICE-devel libX11-devel libXau-devel libXext-devel libXft-devel libXrender-devel libfreetype-devel libstartup-notification libxcb-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage pkg-config python-base rpm-build-gir xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel xz
BuildRequires: imake libSM-devel libXcursor-devel libXinerama-devel libXrandr-devel libpango-devel libstartup-notification-devel libxml2-devel perl-podlators xorg-cf-files
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(imlib2)

BuildRequires: perl-podlators
BuildRequires(pre): rpm-build-python3

%description
Openbox is a standards compliant, fast, light-weight, extensible window manager.
Openbox works with your applications, and makes your desktop easier to manage.
This is because the approach to its development was the opposite of what seems
to be the general case for window managers. Openbox was written first to comply
with standards and to work properly. Only when that was in place did the team
turn to the visual interface.
Openbox is fully functional as a stand-alone working environment, or can be
usedas a drop-in replacement for the default window manager in the GNOME or KDE
desktop environments.

%package -n lib%name
Summary: Openbox libraries
Group: System/Libraries
Requires: %_datadir/themes/Clearlooks/openbox-3/themerc
Conflicts: openbox-base <= 3.5.0-alt5

%description -n lib%name
This package contains libraries for Openbox window manager:
libobparser - Openbox config file parsing library,
libobrender - Openbox Render Library.

%package -n lib%name-devel
Summary: Development files for Openbox
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files and libraries for
developing with Openbox window manager.

%package -n lib%name-devel-static
Summary: Development static library for Openbox
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static libraries for developing with
Openbox window manager.

%package base
Summary: Openbox pure WM
Group: Graphical desktop/Other

%description base
Openbox pure WM.

%if_with kde
%package kde
Summary: Run KDE with Openbox as the WM
Group: Graphical desktop/Other
BuildArch: noarch
Requires: %_bindir/openbox

%description kde
Run KDE with Openbox as the WM.
%endif

%if_with gnome
%package gnome
Summary: Run GNOME with Openbox as the WM
Group: Graphical desktop/Other
Requires: %_bindir/openbox

%description gnome
Run GNOME with Openbox as the WM.
%endif

%package autostart
Summary: XDG support for Openbox
Group: Graphical desktop/Other
BuildArch: noarch
%py3_requires xdg

%description autostart
XDG support for Openbox.

%package themes
Summary: A Openbox themes engine
Group: System/Libraries
BuildArch: noarch
Requires: %_datadir/themes/Artwiz-boxed/openbox-3/themerc
Requires: %_datadir/themes/Bear2/openbox-3/themerc
Requires: %_datadir/themes/Clearlooks/openbox-3/themerc
Requires: %_datadir/themes/Clearlooks-3.4/openbox-3/themerc
Requires: %_datadir/themes/Clearlooks-Olive/openbox-3/themerc
Requires: %_datadir/themes/Mikachu/openbox-3/themerc
Requires: %_datadir/themes/Natura/openbox-3/themerc
Requires: %_datadir/themes/Onyx/openbox-3/themerc
Requires: %_datadir/themes/Onyx-Citrus/openbox-3/themerc
Requires: %_datadir/themes/Orang/openbox-3/themerc
Requires: %_datadir/themes/Syscrash/openbox-3/themerc
Conflicts: openbox-base <= 3.5.0-alt5

%description themes
This is a virtual package requires all themes engine
distributed with Openbox.

%package theme-Artwiz-boxed
Summary: A Openbox theme engine - Artwiz-boxed
Summary(ru_RU.UTF-8): Тема для Openbox - Artwiz-boxed
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Artwiz-boxed
This package contains the Openbox theme engine named Artwiz-boxed.
This theme distributed with Openbox.

%package theme-Bear2
Summary: A Openbox theme engine - Bear2
Summary(ru_RU.UTF-8): Тема для Openbox - Bear2
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Bear2
This package contains the Openbox theme engine named Bear2.
This theme distributed with Openbox.

%package theme-Clearlooks
Summary: A Openbox theme engine - Clearlooks
Summary(ru_RU.UTF-8): Тема для Openbox - Clearlooks
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Clearlooks
This package contains the Openbox theme engine named Clearlooks.
This theme distributed with Openbox.

%package theme-Clearlooks-3.4
Summary: A Openbox theme engine - Clearlooks-3.4
Summary(ru_RU.UTF-8): Тема для Openbox - Clearlooks-3.4
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Clearlooks-3.4
This package contains the Openbox theme engine named Clearlooks-3.4.
This theme distributed with Openbox.

%package theme-Clearlooks-Olive
Summary: A Openbox theme engine - Clearlooks-Olive
Summary(ru_RU.UTF-8): Тема для Openbox - Clearlooks-Olive
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Clearlooks-Olive
This package contains the Openbox theme engine named Clearlooks-Olive.
This theme distributed with Openbox.

%package theme-Mikachu
Summary: A Openbox theme engine - Mikachu
Summary(ru_RU.UTF-8): Тема для Openbox - Mikachu
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Mikachu
This package contains the Openbox theme engine named Mikachu.
This theme distributed with Openbox.

%package theme-Natura
Summary: A Openbox theme engine - Natura
Summary(ru_RU.UTF-8): Тема для Openbox - Natura
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Natura
This package contains the Openbox theme engine named Natura.
This theme distributed with Openbox.

%package theme-Onyx
Summary: A Openbox theme engine - Onyx
Summary(ru_RU.UTF-8): Тема для Openbox - Onyx
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Onyx
This package contains the Openbox theme engine named Onyx.
This theme distributed with Openbox.

%package theme-Onyx-Citrus
Summary: A Openbox theme engine - Onyx-Citrus
Summary(ru_RU.UTF-8): Тема для Openbox - Onyx-Citrus
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Onyx-Citrus
This package contains the Openbox theme engine named Onyx-Citrus.
This theme distributed with Openbox.

%package theme-Orang
Summary: A Openbox theme engine - Orang
Summary(ru_RU.UTF-8): Тема для Openbox - Orang
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Orang
This package contains the Openbox theme engine named Orang.
This theme distributed with Openbox.

%package theme-Syscrash
Summary: A Openbox theme engine - Syscrash
Summary(ru_RU.UTF-8): Тема для Openbox - Syscrash
Group: Graphical desktop/Other
BuildArch: noarch
Conflicts: openbox-base <= 3.5.0-alt5

%description theme-Syscrash
This package contains the Openbox theme engine named Syscrash.
This theme distributed with Openbox.

%prep
%setup -q -a2
%patch2 -p1
%patch10 -p1
sed -i '/^obrender_libobrender_la_LIBADD/ a\\tobt/libobt.la \\' Makefile.am

%build
%autoreconf
%configure \
	--disable-rpath \
	--disable-static
%make_build

cp %SOURCE12 .

pod2man --section=1 --release=%version --center "Openbox documentation" gnome-panel-control.pod > gnome-panel-control.1

%install
%make_install DESTDIR=%buildroot install

rm -rf %buildroot%_datadir/doc/

# manual pages
mkdir -p %buildroot%_man1dir/
install -pD -m 644 gnome-panel-control.1 %buildroot%_man1dir/

# icons
install -pD -m 644 %name-64.xpm %buildroot%_iconsdir/hicolor/64x64/apps/OpenBox.xpm
install -pD -m 644 %name-48.xpm %buildroot%_liconsdir/%name.xpm
install -pD -m 644 %name-32.xpm %buildroot%_niconsdir/%name.xpm
install -pD -m 644 %name-16.xpm %buildroot%_miconsdir/%name.xpm

# Menu isn't cooked yet, because it's hard to implement menu-method
# for Openbox XML based menu
install -pD -m 755 %SOURCE4 %buildroot%_sysconfdir/menu-methods/%name
install -pD -m 644 %SOURCE5 %buildroot%_sysconfdir/X11/wmsession.d/09%name
%if_with kde
install -pD -m 644 %SOURCE6 %buildroot%_sysconfdir/X11/wmsession.d/10%name-kde
%endif
install -pD -m 644 %SOURCE7 %buildroot%_sysconfdir/X11/wmsession.d/11%name-gnome

mkdir -p %buildroot%_sysconfdir/xdg/openbox/

install -pD -m 644 %SOURCE13 %buildroot%_sysconfdir/xdg/openbox/

%find_lang --output=%name.lang %name

%files
%config %_sysconfdir/X11/wmsession.d/09openbox
%_datadir/xsessions/openbox.desktop

%files base -f %name.lang
%doc AUTHORS CHANGELOG COMPLIANCE README
%doc data/menu.xsd doc/rc-mouse-focus.xml data/rc.xsd data/xbm
%_sysconfdir/xdg/openbox/*
%config(noreplace) %_sysconfdir/menu-methods/*
%_bindir/*
%exclude %_bindir/openbox-kde-session
%exclude %_bindir/openbox-gnome-session
%exclude %_bindir/gdm-control
%exclude %_bindir/gnome-panel-control
%_man1dir/*
%exclude %_man1dir/openbox-kde-session.*
%exclude %_man1dir/openbox-gnome-session.*
%exclude %_man1dir/gnome-panel-control.*
%_datadir/gnome/wm-properties/*
%_datadir/pixmaps/*
%_liconsdir/%name.xpm
%_niconsdir/%name.xpm
%_iconsdir/hicolor/64x64/apps/OpenBox.xpm
%_miconsdir/%name.xpm
%_datadir/applications/openbox.desktop

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_pkgconfigdir/*
%_libdir/*.so
%_includedir/*

%if_with kde
%files kde
%config %_sysconfdir/X11/wmsession.d/10openbox-kde
%_bindir/openbox-kde-session
%_datadir/xsessions/openbox-kde.desktop
%_man1dir/openbox-kde-session.*
%endif

%if_with gnome
%files gnome
%config %_sysconfdir/X11/wmsession.d/11openbox-gnome
%_bindir/openbox-gnome-session
%_bindir/gdm-control
%_bindir/gnome-panel-control
%_datadir/gnome-session/sessions/openbox-gnome*.session
%_datadir/xsessions/openbox-gnome.desktop
%_man1dir/openbox-gnome-session.*
%_man1dir/gnome-panel-control.*
%endif

%files autostart
%_libexecdir/openbox-xdg-autostart
%_libexecdir/openbox-autostart

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files themes

%files theme-Artwiz-boxed
%_datadir/themes/Artwiz-boxed

%files theme-Bear2
%_datadir/themes/Bear2

%files theme-Clearlooks
%_datadir/themes/Clearlooks

%files theme-Clearlooks-3.4
%_datadir/themes/Clearlooks-3.4

%files theme-Clearlooks-Olive
%_datadir/themes/Clearlooks-Olive

%files theme-Mikachu
%_datadir/themes/Mikachu

%files theme-Natura
%_datadir/themes/Natura

%files theme-Onyx
%_datadir/themes/Onyx

%files theme-Onyx-Citrus
%_datadir/themes/Onyx-Citrus

%files theme-Orang
%_datadir/themes/Orang

%files theme-Syscrash
%_datadir/themes/Syscrash

%changelog
* Thu Nov 28 2019 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt5
- add Buildrequires: imlib2 librsvg (Closes: 37547)

* Thu Nov 07 2019 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt4.1
- fix reguires

* Wed Nov 06 2019 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt4
- switch to python3
- Rebuilt without gnome subpackage.

* Thu Sep 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.1-alt3
- Rebuilt without kde subpackage.

* Wed Sep 16 2015 Aleksey Avdeev <solo@altlinux.org> 3.6.1-alt2
- Remove kdetrayproxy.1: kdetrayproxy removed in openbox-3.5.0

* Mon Sep 14 2015 Aleksey Avdeev <solo@altlinux.org> 3.6.1-alt1
- 3.5.0 -> 3.6.1
- Fix requires for openbox package: add %%_libexecdir/openbox-autostart
- Remove TheBear theme (move to package openbox-theme-TheBear)
- All themes engine highlighted in the sub-packages:
  + openbox-themes (virtual)
  + openbox-theme-Artwiz-boxed
  + openbox-theme-Bear2
  + openbox-theme-Clearlooks
  + openbox-theme-Clearlooks-3.4
  + openbox-theme-Clearlooks-Olive
  + openbox-theme-Mikachu
  + openbox-theme-Natura
  + openbox-theme-Onyx
  + openbox-theme-Onyx-Citrus
  + openbox-theme-Orang
  + openbox-theme-Syscrash

* Fri Oct 03 2014 Lenar Shakirov <snejok@altlinux.ru> 3.5.0-alt5
- make autostart and kde packages noarch

* Fri Oct 03 2014 Lenar Shakirov <snejok@altlinux.ru> 3.5.0-alt4
- finally fix wmsession file (ALT #28627)

* Tue Mar 05 2013 Mykola Grechukh <gns@altlinux.ru> 3.5.0-alt3
- execute autostart and environment when run standalone from DM

* Thu Feb 14 2013 Mykola Grechukh <gns@altlinux.ru> 3.5.0-alt2
- revisited subpackages layout

* Thu Feb 14 2013 Mykola Grechukh <gns@altlinux.ru> 3.5.0-alt1.3
- wmsession splitted to subpackage

* Thu Feb 14 2013 Mykola Grechukh <gns@altlinux.ru> 3.5.0-alt1.2
- s/O/o/, closes #28524

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt1.1
- Rebuild with Python-2.7

* Fri Aug 05 2011 Mykola Grechukh <gns@altlinux.ru> 3.5.0-alt1
3.4.11.1 -> 3.5.0

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 3.4.11.1-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Nov 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.11.1-alt1.1
- Rebuilt for soname set-versions

* Tue Apr 20 2010 Mykola Grechukh <gns@altlinux.ru> 3.4.11.1-alt1
- new version

* Sat Jan 23 2010 Igor Zubkov <icesik@altlinux.org> 3.4.10-alt2
- update Url:

* Tue Jan 12 2010 Igor Zubkov <icesik@altlinux.org> 3.4.10-alt1
- 3.4.9 -> 3.4.10

* Thu Dec 24 2009 Igor Zubkov <icesik@altlinux.org> 3.4.9-alt2
- fix desktop file

* Sat Dec 19 2009 Igor Zubkov <icesik@altlinux.org> 3.4.9-alt1
- 3.4.7.2 -> 3.4.9

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.7.2-alt5.qa1.1
- Rebuilt with python 2.6

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 3.4.7.2-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for openbox
  * postclean-05-filetriggers for spec file

* Thu Mar 26 2009 Igor Zubkov <icesik@altlinux.org> 3.4.7.2-alt5
- add Conflicts with openbox-extras

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7.2-alt4
- apply patch from repocop
- buildreq

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.4.7.2-alt3.1
- NMU:
  * updated build dependencies

* Sat Jun 21 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7.2-alt3
- move kde and gnome parts to subpackages (closes #15771)

* Fri May 23 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7.2-alt2
- add BuildRequires: gettext >= 0.15 (closes #15762)

* Thu Apr 24 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7.2-alt1
- 3.4.7.1 -> 3.4.7.2

* Thu Apr 17 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7.1-alt1
- 3.4.7 -> 3.4.7.1

* Wed Apr 16 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7-alt1
- 3.4.6.1 -> 3.4.7
- buildreq

* Thu Feb 21 2008 Igor Zubkov <icesik@altlinux.org> 3.4.6.1-alt1
- 3.4.5 -> 3.4.6.1

* Tue Jan 08 2008 Igor Zubkov <icesik@altlinux.org> 3.4.5-alt1
- 3.4.4 -> 3.4.5

* Wed Nov 14 2007 Igor Zubkov <icesik@altlinux.org> 3.4.4-alt2
- bump release

* Tue Nov 13 2007 Igor Zubkov <icesik@altlinux.org> 3.4.4-alt1
- 3.3.1 -> 3.4.4
- "Run" and "Terminal" menu items (bga@)
- buildreq

* Tue Nov 13 2007 Igor Zubkov <icesik@altlinux.org> 3.3.1-alt6
- clean up spec file

* Wed May 23 2007 Igor Zubkov <icesik@altlinux.org> 3.3.1-alt5
- buildreq to fix rebuild

* Tue Apr 10 2007 Igor Zubkov <icesik@altlinux.org> 3.3.1-alt4
- add TheBear theme from old openbox source package (closes #11379)

* Thu Nov 02 2006 Igor Zubkov <icesik@altlinux.org> 3.3.1-alt3
- add menu method from debian (closes #10332)

* Sat Oct 28 2006 Igor Zubkov <icesik@altlinux.org> 3.3.1-alt2
- sync with debian openbox_3.3-2
  + add manual pages (closes #10333)

* Fri Sep 08 2006 Igor Zubkov <icesik@altlinux.ru> 3.3.1-alt1
- 3.3 -> 3.3.1
- buildreq

* Wed Sep 06 2006 Igor Zubkov <icesik@altlinux.ru> 3.3-alt4
- s/ru_RU.KOI8-R/ru_RU.UTF-8/
- buildreq

* Tue Aug 29 2006 Igor Zubkov <icesik@altlinux.ru> 3.3-alt3
- 3.3rc2 -> 3.3
- convert spec to utf-8

* Fri May 26 2006 Igor Zubkov <icesik@altlinux.ru> 3.3-alt2.rc2
- x86_64 fix

* Fri Mar 17 2006 Igor Zubkov <icesik@altlinux.ru> 3.3-alt1.rc2
- 3.3rc2
- move binary from /usr/X11R6/bin/ to /usr/bin/
- update url
- buildreq
- fix build with new ld / -Wl,--as-needed

* Thu Jan 22 2004 Anton V. Denisov <avd@altlinux.org> 3.1-alt1.1
- BuildRequires tuned by hands in hope what
  /usr/lib/pkgconfig/xft.pc is in XFree86-devel package in
  current Sisyphus (I have ALT Linux Sisyphus (20030704)).

* Tue Jan 20 2004 Anton V. Denisov <avd@altlinux.org> 3.1-alt1
- Initial release for ALT Linux Sisyphus.
- TODO:
  + Menu system (it's hard because Openbox use XML based menu);
  + Russian translation for %%description.
