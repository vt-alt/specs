# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define theme starterkit
%define Theme starter kit
%define codename Hypericum
%define brand alt
%define Brand ALT
%define distro_name ALT Starterkit

Name: branding-%brand-%theme
Version: p9
Release: alt5

Url: http://en.altlinux.org/starterkits

BuildRequires: cpio fonts-ttf-dejavu fonts-ttf-google-droid-sans

BuildRequires: qt5-base-devel
BuildRequires: libalternatives-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel
BuildRequires: fribidi

%define status %nil
%define status_en %nil
%define variants altlinux-office-desktop altlinux-office-server altlinux-lite altlinux-workbench school-master school-junior school-lite school-server altlinux-gnome-desktop altlinux-kdesktop ivk-chainmail simply-linux sisyphus-server-light altlinux-sisyphus altlinux-p7 altlinux-starterkit basealt-starterkit informika-schoolmaster

# argh
%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL

%description
Distro-specific packages with design and texts

%package bootloader
Group: System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
License: GPL

%ifarch %ix86 x86_64
BuildRequires: gfxboot >= 4
%endif #ifarch
BuildRequires: design-bootloader-source >= 5.0-alt2
Requires: coreutils
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootloader ";done )

%define grub_normal white/blue
%define grub_high black/white

%description bootloader
Here you find the graphical boot logo.
Suitable for grub2, lilo and syslinux.

%package bootsplash
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
BuildArch: noarch
Provides: plymouth-theme-%theme plymouth(system-theme)
Requires: plymouth-plugin-script
Requires: plymouth

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootsplash ";done )
%description bootsplash
This package contains graphics for boot process, displayed via Plymouth

%package alterator
Summary: Design for alterator for %Brand %Theme
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Provides: design-alterator-browser-%theme branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes: branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-alterator ";done )
Obsoletes: design-alterator-server design-alterator-desktop design-alterator-browser-desktop design-alterator-browser-server
Requires: alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for %Brand %Theme

%package graphics
Summary: design for ALT
License: Different licenses
Group: Graphics
BuildArch: noarch

# FIXME: have a closer look at kdesktop flavour's spec
Provides: design-graphics = 12.0.0
Provides: design-graphics-%theme branding-alt-%theme-graphics
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix
Obsoletes: branding-alt-%theme-graphics design-graphics-%theme
Requires: alternatives >= 0.2
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-graphics ";done )
Conflicts: design-graphics-default

%description graphics
This package contains some graphics for ALT design.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business

%package release
Summary: %distribution %Theme release file
Group: System/Configuration/Other
BuildArch: noarch
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme branding-alt-%theme-release
Obsoletes: %obsolete_list branding-alt-%theme-release
Conflicts: %conflicts_list
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-release ";done )

%description release
%distribution %version %Theme release file.

%package notes
Provides: alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary: Distribution license and release notes
License: Distributable
Group: Documentation
BuildArch: noarch
Conflicts: alt-notes-children alt-notes-hpc alt-notes-junior alt-notes-junior-sj alt-notes-junior-sm alt-notes-school-server alt-notes-server-lite alt-notes-skif alt-notes-terminal
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-notes ";done )

%description notes
Distribution license and release notes

%package slideshow

Summary: Slideshow for %Brand %version %Theme installer
License: Distributable
Group: System/Configuration/Other
BuildArch: noarch
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-slideshow ";done )

%description slideshow
Slideshow for %Brand %version %Theme installer

%package indexhtml

Summary: ALT Linux welcome page
License: distributable
Group: System/Base
BuildArch: noarch
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop

Conflicts: indexhtml-sisyphus
Conflicts: indexhtml-school_junior
Conflicts: indexhtml-school_lite
Conflicts: indexhtml-school_master
Conflicts: indexhtml-school_terminal
Conflicts: indexhtml-small_business
Conflicts: indexhtml-school-server
Conflicts: branding-sisyphus-server-light-indexhtml

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-indexhtml";done )

Requires: xdg-utils
Requires(post): indexhtml-common

%description indexhtml
ALT Linux index.html welcome page.

%package xfce-settings

Summary: XFCE settings for %Brand %version %Theme
License: Distributable
Group: Graphical desktop/XFce
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-xfce-settings ";done )

%description xfce-settings
XFCE settings for %Brand %version %Theme

%prep
%setup -n branding

%build
autoconf
THEME=%theme NAME='%Theme' BRAND_FNAME='%Brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME='%distro_name' CODENAME=%codename URL='%url' ./configure
LC_ALL=en_US.UTF-8 make

%install
%makeinstall

#graphics
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
cp -ar graphics/* %buildroot/%_datadir/design/%theme

pushd %buildroot/%_datadir/design/%theme
    pushd backgrounds
	ln -sf ../../../wallpapers more
    popd
popd

install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/artworks	%_datadir/design/%theme 10	
%_datadir/design-current	%_datadir/design/%theme	10
%_datadir/design/current	%_datadir/design/%theme	10
__EOF__

# bootsplash
mkdir -p %buildroot%_pixmapsdir
cp -a images/system-logo.png %buildroot%_pixmapsdir/

#release
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
{
	echo -n "%distribution"
	[ -n "%Theme" ] && echo -n " %Theme"
	[ -n "%status_en" ] && {
		[ "%status_en" = "unstable" ] \
		&& echo -n " (unstable)" \
		|| echo -n " %status_en"
	}
	[ -n "%codename" ] && echo -n " (%codename)"
	echo
} >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system alt; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done
install -pD -m644 components/systemd/os-release %buildroot%_sysconfdir/os-release

#notes
pushd notes
%makeinstall
popd

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
install slideshow/* %buildroot/usr/share/install2/slideshow/

#xfce-settings
pushd xfce-settings
mkdir -p %buildroot/etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml
mkdir -p %buildroot/etc/skel/.config/xfce4/panel
mkdir -p %buildroot/etc/skel/.config/autostart
cp -r etcskel/.config/xfce4/xfconf/xfce-perchannel-xml/* %buildroot/etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml
cp -r etcskel/.config/xfce4/panel/* %buildroot/etc/skel/.config/xfce4/panel
cp -r etcskel/.config/autostart/* %buildroot/etc/skel/.config/autostart
popd

#bootloader
%pre bootloader
[ -s /usr/share/gfxboot/%theme ] && rm -fr /usr/share/gfxboot/%theme ||:
[ -s /boot/splash/%theme ] && rm -fr /boot/splash/%theme ||:

%post bootloader
%ifarch %ix86 x86_64
ln -snf %theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message
%endif #ifarch
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high
shell_config_set /etc/sysconfig/grub2 GRUB_WALLPAPER /boot/grub/themes/%theme/boot.png

%ifarch %ix86 x86_64
%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    rm -f /boot/splash/message
%endif #ifarch

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
%ifarch %ix86 x86_64
%_datadir/gfxboot/%theme
/boot/splash/%theme
%endif #ifarch
/boot/grub/themes/%theme

#bootsplash
%post bootsplash
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design

%files bootsplash
%_datadir/plymouth/themes/%theme/*
%_pixmapsdir/system-logo.png

%files release
%_sysconfdir/*-release
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files slideshow
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %indexhtmldir/index.html
%indexhtmldir/index-*.html
%indexhtmldir/index.css
%indexhtmldir/img
%_desktopdir/indexhtml.desktop

%files xfce-settings
%_sysconfdir/skel/.config/xfce4
%_sysconfdir/skel/.config/autostart/*

%changelog
* Sat Oct 26 2019 Anton Midyukov <antohami@altlinux.org> p9-alt5
- bootsplash: add system-logo

* Mon Jun 24 2019 Anton Midyukov <antohami@altlinux.org> p9-alt4.2
- xfce-settings: replaced clipman and power-manager applets on tray
applications

* Mon Jun 17 2019 Anton Midyukov <antohami@altlinux.org> p9-alt4.1
- xfce-settings: revert launchers on panel

* Sun Jun 16 2019 Anton Midyukov <antohami@altlinux.org> p9-alt4
- xfce-settings: xfce panel settings only

* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> p9-alt3
- xfce-settings back in minimal

* Mon May 27 2019 Anton Midyukov <antohami@altlinux.org> p9-alt2
- setup GRUB_WALLPAPER when installing bootloader

* Fri May 17 2019 Anton Midyukov <antohami@altlinux.org> p9-alt1.1
- build bootloader and bootsplash for all ARCH

* Sun Mar 17 2019 Anton Midyukov <antohami@altlinux.org> p9-alt1
- updated for basealt-p9-starterkits
- drop kde3-settings
- drop kde4-settings
- drop gnome-settings and gnome-themes
- fix build for non-x86
- added grub theme

* Mon Feb 25 2019 Anton Midyukov <antohami@altlinux.org> p8-alt0.M80P.5
- Cleanup plymouth theme

* Wed Dec 19 2018 Anton Midyukov <antohami@altlinux.org> p8-alt0.M80P.4.1
- Fix the installer background defect

* Fri Dec 07 2018 Anton Midyukov <antohami@altlinux.org> p8-alt0.M80P.4
- Use resources generator from Qt5
- Use _unpackaged_files_terminate_build
- Update background for installer
- Fix build

* Mon Dec 05 2016 Michael Shigorin <mike@altlinux.org> p8-alt0.M80P.3
- added /etc/os-release
- fixed progressbar position
- tweaked release notes
- replaced licene step icon
- rebuilt in current environment

* Mon Aug 15 2016 Michael Shigorin <mike@altlinux.org> p8-alt0.M80P.2
- updated again for alt-p8-starterkits

* Sat Apr 23 2016 Michael Shigorin <mike@altlinux.org> p8-alt0.M80P.1
- updated for basealt-p8-starterkits

* Fri Mar 11 2016 Michael Shigorin <mike@altlinux.org> p7-alt7.M70P.2
- tweaked license a bit more

* Fri Mar 11 2016 Michael Shigorin <mike@altlinux.org> p7-alt7.M70P.1
- fixed license (closes: #31748)
- tweaked bootloader help cursor background colour

* Thu Sep 10 2015 Michael Shigorin <mike@altlinux.org> p7-alt6.M70P.1
- updated company address

* Tue Sep 02 2014 Michael Shigorin <mike@altlinux.org> p7-alt5.M70P.1
- updated company address

* Tue Apr 01 2014 Michael Shigorin <mike@altlinux.org> p7-alt4.M70P.1
- enabled mediachk by default

* Mon Mar 10 2014 Michael Shigorin <mike@altlinux.org> p7-alt3.M70P.1
- replaced images (qtbrowser background and slideshow)

* Tue Feb 11 2014 Michael Shigorin <mike@altlinux.org> p7-alt2.M70P.1
- updated license agreement

* Wed Nov 27 2013 Michael Shigorin <mike@altlinux.org> p7-alt1.M70P.1
- fixed graphics subpackage provides (altlinux-sisyphus-20130322-alt2)
- added informika-schoolmaster to known variants

* Tue Sep 24 2013 Michael Shigorin <mike@altlinux.org> p7-alt0.M70P.1
- version changed to reflect branch and not build date

* Tue Sep 24 2013 Michael Shigorin <mike@altlinux.org> 20130924-alt0.M70P.1
- tweaked notes (thx zerg@)

* Mon Jun 10 2013 Michael Shigorin <mike@altlinux.org> 20130610-alt0.M70P.1
- starter kit branding

* Sun Apr 28 2013 Michael Shigorin <mike@altlinux.org> 20130427-alt1.M70P.4
- fixed bootloader config for p7/branch

* Sun Apr 28 2013 Michael Shigorin <mike@altlinux.org> 20130427-alt1.M70P.3
- stuck design-graphics versioning in (for kde4)

* Sat Apr 27 2013 Michael Shigorin <mike@altlinux.org> 20130427-alt1.M70P.2
- added missing Conflicts:

* Sat Apr 27 2013 Michael Shigorin <mike@altlinux.org> 20130427-alt1.M70P.1
- fixed Release: (thx aen@)

* Sat Apr 27 2013 Michael Shigorin <mike@altlinux.org> 20130427-alt2
- added codename ;-)

* Sat Apr 27 2013 Michael Shigorin <mike@altlinux.org> 20130427-alt1
- adapted for p7/branch

* Fri Mar 22 2013 Michael Shigorin <mike@altlinux.org> 20130322-alt1
- rebuilt upon d-b-s with Kazakh translation

* Tue Mar 12 2013 Michael Shigorin <mike@altlinux.org> 20130312-alt1
- tweaked wallpaper to avoid kde4/gnome3/mate/wmaker collisions

* Thu Mar 07 2013 Michael Shigorin <mike@altlinux.org> 20130307-alt1
- fixed broken image resolution/directory name match for kde4 splash
  (thanks zerg@)

* Mon Dec 31 2012 Michael Shigorin <mike@altlinux.org> 20121231-alt1
- fixed module link text colour in acc
- tweaked acc background color (was too white)

* Wed Dec 26 2012 Michael Shigorin <mike@altlinux.org> 20121226-alt1
- fixed background image position

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 20110706-alt3
- *dropped* R: altlinux-menus (closes: #27585)

* Fri Jun 01 2012 Michael Shigorin <mike@altlinux.org> 20110706-alt2
- bootsplash subpackage provides plymouth(system-theme)

* Wed Jul 06 2011 Michael Shigorin <mike@altlinux.org> 20110706-alt1
- rebuilt against current design-bootloader-source
  (syslinux-3.86 support)

* Thu May 12 2011 Michael Shigorin <mike@altlinux.org> 20101228-alt2
- dropped R: altlinux-menus (closes: #25565)

* Tue Dec 28 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101228-alt1
- bootsplash->plymouth
- OO.o->libreoffice

* Thu Dec 09 2010 Michael Shigorin <mike@altlinux.org> 20101209-alt1
- initial Sisyphus-specific adaptation,
  including custom texts, background and colour scheme
- fixed alterator subpackage obsoletes (a typo) and conflicts (stale)
- minor spec cleanup

* Thu Jun 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt17
- ksplashrc added for kde4
- kde3-settings and splash for kde3 added (mex@)
- gnome-settngs added (mex@)

* Wed May 13 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt16
- %%setup fixed from boyarsh@
- remove package name from .gear-rules from boyarsh@

* Fri Apr 24 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt15
- minor fixes of strange merge
- changes in alterator.css.in from inger@

* Fri Apr 17 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt14
- better quality background image for installer

* Thu Apr 16 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt13
- alterator.css = alterator.css+menu.css
- some strange results of merge fixed

* Fri Apr 10 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt12
- gear-rules fixed

* Fri Apr 10 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt11
- web logo - white and smaller;
  labels on buttons - darker;
  disabled elements - lighter;

* Fri Apr 10 2009 Alxandra Panyukova <mex3@altlinux.ru> 5.0.0-alt10
- some misspells fixed

* Thu Apr 09 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt9
- darker text and new logo for web

* Thu Apr 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt8
- gradients and some colors in css fixed by mex3@

* Tue Apr 07 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt7
- fixes for installer design from mex3@ 

* Fri Apr 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt6
- default gray design from mex3@
- \%status_en intorduces for release file 

* Wed Apr 01 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt5
- logo in www design fixed 

* Tue Mar 31 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt4
- www design fixed 

* Tue Mar 31 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt3
- conflicts for -alterator subpackages added
- design for web alterator changed

* Mon Mar 30 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt2
- -browser-qt subpackage remaned to -alterator as it really is

* Fri Mar 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt1
- addes \%status to altlinux-release
- images for verbose bootsplash mode from one source

* Wed Mar 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt24
- added versioned provides for indexhtml 

* Tue Mar 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt23
- indexhtml subpackage added 

* Mon Mar 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt22
- nepomukserverrc added into kde4 

* Wed Mar 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt21
- other images for browser-qt added
- gtkrcs added into kde4-settings
- plasma-applet-networkmanagenemt removed from kde4 by default
- conflicts bitween different brandings added

* Thu Mar 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt20
- steps icons added 

* Fri Feb 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt19
- sample slideshow added

* Wed Feb 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt18
- 1024x768 removed :D
- more transparent menu selection bar

* Tue Feb 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt17
- 1024x768 added 
- fonts changed

* Thu Feb 19 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt16
- not setup language in bootloader during install (when it is 'C') 

* Wed Feb 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt15
- rebuild with new bootloader-source with support of real language change 

* Tue Feb 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt14
- auto set default language for bootloader from /etc/sysconfig/i18n 

* Mon Feb 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt13
- rebuild for fix oversized /boot/splash/message 

* Fri Feb 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt12
- default language set to ru_RU for system boot 

* Wed Feb 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt11
- fixed conflict of notes subpackage with itself 

* Tue Feb 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt10
- more kde4 settings from zerg@ 
- alternative and obsoletes for graphics added

* Thu Feb 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt9
- rebuild with new translations 

* Thu Feb 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt8
- added kde4-settings subpackage 

* Wed Feb 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt7
- added conflicts for notes 

* Mon Jan 26 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt6
- xdm background fixed 

* Fri Jan 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt5
- added 'notes' subpackage 

* Thu Jan 15 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt4
- fixed problem with owerwritten alternative 

* Wed Jan 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt3
- release subpackage added 

* Fri Dec 26 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- colors integration
- graphics package added

* Thu Dec 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- initial sceleton 

