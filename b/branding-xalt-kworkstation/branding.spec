%ifarch %ix86 x86_64
%def_enable gfxboot
%else
%def_disable gfxboot
%endif

%define Theme Workstation K
%define smalltheme kworkstation
%define codename Centaurea Ruthenica
%define brand alt
%define Brand ALT
%define fakebrand xalt

%define major 9
%define minor 0
%define bugfix 0
%define altversion %major.%minor
Name: branding-%fakebrand-%smalltheme
Version: %major.%minor.%bugfix
Release: alt0.3

%define theme %name
%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

BuildRequires: fonts-ttf-dejavu fonts-ttf-google-droid-sans
BuildRequires: design-bootloader-source >= 5.0-alt2
BuildRequires: cpio %{?_enable_gfxboot:gfxboot >= 4}

BuildRequires(pre): rpm-build-ubt
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel

%define Theme_ru Рабочая станция К
%define Brand_ru Альт
%define status BETA
%define status_ru БЕТА
%define ProductName %Brand %Theme %altversion
%define ProductName_ru %Brand_ru %Theme_ru %altversion

%define variants alt-kdesktop alt-server alt-starterkit alt-workstation altlinux-kdesktop altlinux-desktop altlinux-office-desktop altlinux-office-server altlinux-lite altlinux-workbench altlinux-sisyphus sisyphus-server school-master school-server school-teacher school-lite school-junior altlinux-gnome-desktop sisyphus-server-light

Source: %name.tar

Group: Graphics
Summary: System/Base
License: GPL
Url: http://www.basealt.ru

%description
Distro-specific packages with design and texts


%package bootloader
Group: System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
License: GPL
PreReq: coreutils
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
%define grub_normal white/black
%define grub_high black/white
%description bootloader
Here you find the graphical boot logo. Suitable for both lilo and syslinux.

%package bootsplash
BuildArch: noarch
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: plymouth-theme-%theme plymouth(system-theme)
Requires: plymouth-plugin-script
PreReq: plymouth
%description bootsplash
This package contains graphics for boot process, displayed via Plymouth


%package alterator
BuildArch: noarch
Summary: Design for alterator for %Brand %Theme 
License: GPL
Group: System/Configuration/Other
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes:  branding-alt-%theme-browser-qt  branding-altlinux-%theme-browser-qt 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-alterator ";done )
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server 
PreReq(post,preun): alternatives >= 0.2 alterator
%description alterator
Design for QT and web alterator for %Brand %Theme

%package graphics
BuildArch: noarch
Summary: design for ALT
License: Different licenses
Group: Graphics
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix
Provides: design-graphics-%theme  branding-alt-%theme-graphics design-graphics-kdesktop
Obsoletes:  branding-alt-%theme-graphics design-graphics-%theme design-graphics-kdesktop
Provides: gnome-session-splash = %version-%release
PreReq(post,preun): alternatives >= 0.2
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-graphics ";done )
%description graphics
This package contains some graphics for ALT design.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business

%package release
BuildArch: noarch
Summary: %ProductName release file
License: GPL
Group: System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list  branding-alt-%theme-release
Conflicts: %conflicts_list
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-release ";done )
%description release
%ProductName release file.

%package notes
BuildArch: noarch
Provides: alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary: Distribution license and release notes
License: Distributable
Group: Documentation
Conflicts: alt-notes-children alt-notes-hpc alt-notes-junior alt-notes-junior-sj alt-notes-junior-sm alt-notes-school-server alt-notes-server-lite alt-notes-skif alt-notes-terminal 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-notes ";done )
%description notes
Distribution license and release notes

%package kde4-settings
BuildArch: noarch
Summary: KDE4 settings for %ProductName
License: Distributable
Group: Graphical desktop/KDE
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-kde4-settings ";done )
PreReq: %name-graphics
%description kde4-settings
KDE4 settings for %ProductName

%package fvwm-settings
BuildArch: noarch
Summary: FVWM2 settings for %ProductName
License: Distributable
Group: Graphical desktop/FVWM based
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-fvwm-settings ";done )
%description fvwm-settings
FVWM2 settings for %ProductName

%package mate-settings
BuildArch: noarch
Summary: MATE settings for %ProductName
License: Distributable
Group:   Graphical desktop/GNOME
Requires: gksu
Requires: dconf
%description mate-settings
MATE settings for %ProductName

%package gnome-settings
BuildArch: noarch
Summary: GNOME settings for %ProductName
License: Distributable
Group: Graphical desktop/GNOME
Requires: gtk2-theme-mist
#PreReq: gnome-panel
Provides: gnome-theme-%brand-%theme = %version-%release
Provides: metacity-theme-%brand-%theme = %version-%release
Provides: metacity-theme
Provides: gnome-menus = 2.30.4
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-gnome-settings ";done )
%description gnome-settings
GNOME settings for %ProductName

%package slideshow
BuildArch: noarch
Summary: Slideshow for %ProductName installer
License: Distributable
Group: System/Configuration/Other 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-slideshow ";done )
%description slideshow
Slideshow for %ProductName installer

%package indexhtml
BuildArch: noarch
Summary: %name -- ALT html welcome page
License: distributable
Group: System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-indexhtml ";done )
Requires: xdg-utils
Requires(post): indexhtml-common
%description indexhtml
ALT index.html welcome page.

%prep
%setup -n %name

%if_enabled gfxboot
%define x86 boot
%else
%define x86 %nil
%endif

mkdir design-bootloader-source-copy
cp -ar /usr/src/design-bootloader-source ./design-bootloader-source-copy/
sed -i 's|/usr/share/fonts/ttf/droid/|/usr/share/fonts/ttf/google-droid/|' design-bootloader-source-copy/design-bootloader-source/fonts/Makefile
sed -i 's|/usr/src/design-bootloader-source|design-bootloader-source-copy/design-bootloader-source|' components.mk

%build
autoconf
THEME=%theme \
NAME='%Theme' \
NAME_RU='%Theme_ru' \
BRAND_FNAME='%Brand' \
BRAND_FNAME_RU='%Brand_ru' \
BRAND='%brand' \
PRODUCT_NAME='%ProductName' \
PRODUCT_NAME_RU='%ProductName_ru' \
STATUS=%status \
STATUS_RU=%status_ru \
VERSION=%altversion \
X86='%x86' \
    ./configure
make

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

GRAPHICS_ALTPRIO=`printf '%%.3d%%.3d%%.3d%%.3d\n' %design_graphics_abi_epoch %design_graphics_abi_major %design_graphics_abi_minor %design_graphics_abi_bugfix`
install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/design-current	%_datadir/design/%theme	$GRAPHICS_ALTPRIO
%_datadir/design/current	%_datadir/design/%theme	$GRAPHICS_ALTPRIO
__EOF__


#release
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/ignore.d/
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
echo "%ProductName %status (%codename)" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done
# os-release
mkdir -p %buildroot/%_datadir/%name
cat >>%buildroot/%_sysconfdir/os-release <<__EOF__
NAME="%Brand"
VERSION="%altversion %status"
ID=altlinux
VERSION_ID=%altversion
PRETTY_NAME="%ProductName %status (%codename)"
ANSI_COLOR="1;33"
CPE_NAME="cpe:/o:%brand:%smalltheme:%altversion"
HOME_URL="%url"
BUG_REPORT_URL="https://bugs.altlinux.org/"
__EOF__

#notes
pushd notes
%makeinstall
popd

#kde4-settings
pushd kde4-settings
mkdir -p %buildroot%_sysconfdir/skel/.kde4
cp -a kde4/* %buildroot%_sysconfdir/skel/.kde4/
mkdir -p %buildroot%_sysconfdir/kde4/xdg/menus/applications-merged/
install -m 0644 menu/*.menu %buildroot%_sysconfdir/kde4/xdg/menus/applications-merged/
popd
# disable annoing autostart
mkdir -p %buildroot/%_sysconfdir/skel/.config/autostart/
for n in tracker-extract tracker-miner-apps tracker-miner-fs tracker-miner-user-guides tracker-store ; do
    echo -e "[Desktop Entry]\nHidden=true" > %buildroot%_sysconfdir/skel/.config/autostart/$n.desktop
done
# disable annoing menus
mkdir -p %buildroot/%_sysconfdir/skel/.local/share/applications/
for n in gnome-mplayer mplayer gmplayer ; do
    echo -e "[Desktop Entry]\nHidden=true" > %buildroot/%_sysconfdir/skel/.local/share/applications/$n.desktop
done

#fwvm-settings
mkdir -p %buildroot/etc/skel
install -m 644 fvwm-settings/.fvwm2rc %buildroot/etc/skel/

#mate-settings
pushd mate-settings
install -m 644 -D mate-background.gschema.override %buildroot/%_datadir/glib-2.0/schemas/50_mate-%name-background.gschema.override
popd

#gnome-settings
%define XdgThemeName %Brand %Theme
pushd gnome-settings
mkdir -p '%buildroot/%_datadir/themes/%XdgThemeName'
install -m 644  panel-default-setup.entries '%buildroot/%_datadir/themes/%XdgThemeName/'
mkdir -p '%buildroot/%_datadir/themes/%XdgThemeName/gtk-2.0'
install -m 644 gtkrc '%buildroot/%_datadir/themes/%XdgThemeName/gtk-2.0'
mkdir -p '%buildroot/%_datadir/themes/%XdgThemeName/metacity-1'
install -m 644 metacity-theme-1.xml '%buildroot/%_datadir/themes/%XdgThemeName/metacity-1/'
install -m 644 index.theme '%buildroot/%_datadir/themes/%XdgThemeName/'
mkdir -p '%buildroot/etc/gnome/xdg/menus/'
install -m 644 gnome-applications.menu '%buildroot/etc/gnome/xdg/menus/'
install -m 644 settings.menu '%buildroot/etc/gnome/xdg/menus/'
install -m 644 gtkrc-2 %buildroot/etc/skel/.gtkrc-2.0
mkdir -p %buildroot/etc/skel/.config/gtk-3.0/
install -m 644 gtk3-settings.ini %buildroot/etc/skel/.config/gtk-3.0/settings.ini
popd

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
install -m 0644 slideshow/*  %buildroot/usr/share/install2/slideshow/

#bootloader
%pre bootloader
[ -s /usr/share/gfxboot/%theme ] && rm -fr  /usr/share/gfxboot/%theme ||:
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:

%post bootloader
%__ln_s -nf %theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high


%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message

%post indexhtml
%_sbindir/indexhtml-update

%if_enabled gfxboot
%files bootloader
%_datadir/gfxboot/%theme
/boot/splash/%theme
/boot/grub/themes/%theme
%endif

#bootsplash
%post bootsplash
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf
[ -f /etc/sysconfig/grub2 ] && \
      subst "s|GRUB_WALLPAPER=.*|GRUB_WALLPAPER=/usr/share/plymouth/themes/%theme/grub.jpg|" \
             /etc/sysconfig/grub2 ||:

%post gnome-settings
%gconf2_set string /desktop/gnome/interface/font_name Sans 11
%gconf2_set string /desktop/gnome/interface/monospace_font_name Monospace 10
cat '/%_datadir/themes/%XdgThemeName/panel-default-setup.entries' > \
/etc/gconf/schemas/panel-default-setup.entries
/usr/bin/gconftool-2 --direct --config-source=$(/usr/bin/gconftool-2 --get-default-source) \
--load='/%_datadir/themes/%XdgThemeName/panel-default-setup.entries'
/usr/bin/gconftool-2 --direct --config-source=$(/usr/bin/gconftool-2 --get-default-source) \
--load='/%_datadir/themes/%XdgThemeName/panel-default-setup.entries' /apps/panel



%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
%_sysconfdir/skel/.config/gtk-3.0
%_sysconfdir/skel/.gtkrc-2.0
%_sysconfdir/skel/.config/autostart
%_sysconfdir/skel/.local/share/applications

%files bootsplash
%_datadir/plymouth/themes/%theme/*

%files release
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*
%dir %_datadir/%name/


%files notes
%_datadir/alt-notes/*

%files kde4-settings
%_sysconfdir/kde4/xdg/menus/applications-merged/*.menu
%_sysconfdir/skel/.kde4

%files fvwm-settings
%_sysconfdir/skel/.fvwm2rc

%files mate-settings
%_datadir/glib-2.0/schemas/*mate*

%files gnome-settings
%_datadir/themes/*
/etc/gnome/xdg/menus/*

%files slideshow
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %indexhtmldir/index.html
%indexhtmldir/index-*.html
%indexhtmldir/index.css
%indexhtmldir/images
%_desktopdir/indexhtml.desktop
%_datadir/kde4/apps/kio_desktop/DesktopLinks/indexhtml.desktop
%_datadir/kf5/kio_desktop/DesktopLinks/indexhtml.desktop

%changelog
* Mon Aug 12 2019 Sergey V Turchin <zerg at altlinux dot org> 9.0.0-alt0.3
- update plymouth theme (ALT#37097)

* Mon Aug 05 2019 Sergey V Turchin <zerg at altlinux dot org> 9.0.0-alt0.2
- mark as beta-version

* Tue Jul 02 2019 Sergey V Turchin <zerg at altlinux dot org> 9.0.0-alt0.1
- mark as alpha-version

* Mon Feb 25 2019 Sergey V Turchin <zerg at altlinux dot org> 8.3.0-alt4
- cleanup plymouth theme

* Mon Feb 11 2019 Sergey V Turchin <zerg at altlinux dot org> 8.3.0-alt3
- remove requires to pam-limits-desktop (ALT#36064)

* Tue Nov 20 2018 Sergey V Turchin <zerg at altlinux dot org> 8.3.0-alt2
- don't package kde3-settings

* Mon Sep 17 2018 Sergey V Turchin <zerg at altlinux dot org> 8.3.0-alt1%ubt
- new version

* Fri Dec 01 2017 Sergey V Turchin <zerg at altlinux dot org> 8.2.0-alt3%ubt
- update indexhtml

* Tue Jul 25 2017 Sergey V Turchin <zerg at altlinux dot org> 8.2.0-alt2%ubt
- update steps/sysconfig-base.png

* Thu Jul 20 2017 Sergey V Turchin <zerg at altlinux dot org> 8.2.0-alt1%ubt
- new version

* Tue Mar 07 2017 Sergey V Turchin <zerg at altlinux dot org> 8.1.0-alt4%ubt
- require pam-limits-desktop; don't use own limits

* Wed Nov 16 2016 Sergey V Turchin <zerg at altlinux dot org> 8.1.0-alt3
- fix version
- update backgrounds

* Thu Nov 03 2016 Sergey V Turchin <zerg at altlinux dot org> 8.1.0-alt2
- clean titles

* Tue Nov 01 2016 Sergey V Turchin <zerg at altlinux dot org> 8.1.0-alt1
- bump version

* Thu Oct 06 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt9
- set Breeze GTK2/3 theme by default

* Thu Sep 29 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt8
- fix default gtk2 tooltip colors

* Tue Sep 27 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt7
- update slideshow
- set release status

* Fri Sep 02 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt6
- update conflicts for indexhtml

* Thu Sep 01 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt5
- update conflicts

* Tue Aug 30 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt4
- add conflicts for graphics subpackages (ALT#32452)

* Wed Aug 24 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt3
- update conflicts

* Wed Aug 24 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt2
- rebuild

* Tue Aug 23 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt1
- update wallpapers

* Wed Jul 13 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt0.1
- import from kdesktop branding

* Mon Jul 11 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt0.4
- add system limits defaults

* Tue May 10 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt0.3
- rebuild with new gfxboot
- add GTK2 defaults

* Thu Apr 21 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt0.2
- set breeze gtk3 icon theme by default

* Tue Apr 19 2016 Sergey V Turchin <zerg at altlinux dot org> 8.0.0-alt0.1
- add common KDE5 support

* Fri Feb 26 2016 Sergey V Turchin <zerg at altlinux dot org> 7.0.5-alt4
- return default gtk3 icon theme to oxygen

* Fri Feb 26 2016 Sergey V Turchin <zerg at altlinux dot org> 7.0.5-alt3
- update GTK3 defaults

* Tue Jan 20 2015 Sergey V Turchin <zerg at altlinux dot org> 7.0.5-alt2
- fix build with new fonts

* Wed Jan 14 2015 Sergey V Turchin <zerg at altlinux dot org> 7.0.5-alt1
- bump version

* Thu Mar 13 2014 Sergey V Turchin <zerg at altlinux dot org> 7.0.3-alt5
- package static os-release

* Wed Feb 19 2014 Sergey V Turchin <zerg at altlinux dot org> 7.0.3-alt4
- remove planet.altlinux.org URL from indexhtml

* Wed Feb 12 2014 Sergey V Turchin <zerg at altlinux dot org> 7.0.3-alt3
- rebuilt with new design-bootloader-source

* Sat Feb 01 2014 Sergey V Turchin <zerg at altlinux dot org> 7.0.3-alt2
- fix license.all.html

* Wed Jan 22 2014 Sergey V Turchin <zerg at altlinux dot org> 7.0.3-alt1
- licence fixed

* Thu Dec 26 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.2-alt2
- disable tracker autostart (ALT#26549)

* Mon Dec 16 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.2-alt1
- 7.0.2 release

* Fri Dec 06 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.2-alt0.1
- bump version

* Fri Oct 18 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt14
- add conflict with sisyphus-server-light

* Fri Jul 19 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt13
- fix gfxboot background gamma
- decrease plymouth backgrounds size

* Fri Jul 05 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt12
- clear status

* Thu Jun 20 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt11
- change status to RC

* Tue Apr 30 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt10
- fix setup /etc/os-release

* Fri Apr 19 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt9
- fix grub terminal box background color

* Mon Apr 08 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt8
- fix requires

* Thu Apr 04 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt7
- set GTK3 defaults

* Wed Apr 03 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt6
- change status to beta

* Tue Apr 02 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt5
- remove KDE3 splash doublet

* Tue Mar 26 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt4
- add missing grub font

* Fri Mar 22 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt3
- add mate-settings package

* Wed Mar 20 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt2
- update graphics
- add /etc/os-release

* Wed Mar 13 2013 Sergey V Turchin <zerg at altlinux dot org> 7.0.0-alt1
- update background images

* Mon Mar 11 2013 Sergey V Turchin <zerg@altlinux.org> 7.0.0-alt0.1
- bump version

* Mon Sep 03 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt8.M60P.1
- built for M60P

* Mon Sep 03 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt9
- fix KDE3 splash and color defaults

* Mon Aug 27 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt7.M60P.1
- built for M60P

* Mon Aug 27 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt8
- don't remove background image from livecd alterator-browser-qt branding (ALT#27647)

* Tue Aug 21 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt6.M60P.1
- built for M60P

* Tue Aug 21 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt7
- update indexhtml css

* Fri Aug 17 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt5.M60P.1
- built for M60P

* Fri Aug 17 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt6
- fix grub terminal box background color

* Fri Aug 17 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt4.M60P.1
- built for M60P

* Thu Aug 16 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt5
- make grub terminal box background flat

* Fri Aug 10 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt3.M60P.1
- built for M60P

* Fri Aug 10 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt4
- gix license content-type

* Wed Jul 18 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt2.M60P.1
- built for M60P

* Wed Jul 18 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt3
- cleanup browser-qt colors

* Tue Jul 17 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt1.M60P.1
- built for M60P

* Tue Jul 17 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt2
- make installer background black

* Mon Jul 02 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt1
- bump version

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.1-alt5
- provide plymouth(system-theme)

* Wed Mar 07 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.1-alt4
- use bold font for grub menu items

* Mon Mar 05 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.1-alt2.M60P.1
- built for M60P

* Mon Mar 05 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.1-alt3
- fix grub font (ATL#27038)

* Wed Feb 29 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.1-alt1.M60P.1
- built for M60P

* Wed Feb 29 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.1-alt2
- hide gnome-mplayer from menu

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.1-alt1
- bump version
- merge centaurus changes

* Mon Sep 19 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt35
- add Yo to notes

* Mon Aug 22 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt34
- update slideshow

* Tue Aug 16 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt33
- remove "beta"
- fix FAQ URL for uk,en languages

* Wed Aug 03 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt32
- add KDesktop slideshow

* Tue Jul 05 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt31
- don't require altlinux-freedesktop-menu-gnomish-menu

* Mon Jul 04 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt30
- fix indexhtml.desktop permissions

* Fri Jul 01 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt29
- add grub.png symlink to steps
- rebuilt with new design-bootloader-source

* Fri Jun 24 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt28
- hide cups in KDE4 menu

* Fri Jun 24 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt27
- install indexhtml.desktop to KDE4 desktop

* Fri Jun 17 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt26
- fix indexhtml look

* Thu Jun 16 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt25
- update boot images

* Thu Jun 16 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt24
- fix boot progress images

* Thu Jun 16 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt23
- update boot backgrounds

* Tue Jun 14 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt22
- update bootsplash images

* Fri Jun 10 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt21
- update boot backgrounds

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt11
- images with p6 logo

* Wed Jun 08 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt20
- fix grub2 theme colors

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt19
- fix bootloader colors
- fetch colors from KDE4

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt18
- fix installer scroll area border color
- merge last changes from centaurus branding

* Mon Jun 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt10
- automatic 800x600 for virtualbox

* Fri Jun 03 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt17
- add logos
- update kdm colors

* Thu Jun 02 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt16
- update basic colors

* Wed Jun 01 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt15
- update basic backgrounds and colors

* Thu May 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt9
- setup default gnome panel
- .gconf deleted from etcskel

* Tue May 24 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt14
- change title label to KDesktop

* Mon May 23 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt8
- dependence on altlinux-menus dropped

* Sat May 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt7
- beta status deleted
- rebuild with design-bootloader-source 5.9-alt4

* Thu Apr 28 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt13
- fix default background color

* Thu Apr 28 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt12
- fix requires

* Thu Apr 28 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt11
- remove old unused backgrounds
- fix gnome settings placement
- import last changes from centaurus branding

* Wed Apr 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt6
- settings menu translation fixed

* Tue Apr 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt5
- arm buildabulity
- gnome menus customization

* Tue Apr 12 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt10
- update groups and steps icons

* Thu Mar 24 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt9
- return kde3 startup splash

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt8
- import last changes from centaurus branding

* Mon Feb 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt4
- indexhtml colors changed (mex3)

* Fri Feb 11 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt7
- import last changes from centaurus branding

* Thu Feb 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt3
- fixed logo in web interface
- boot colors changed

* Mon Feb 07 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt6
- update kdm4 color scheme
- import last changes from centaurus branding

* Thu Feb 03 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt2
- install menu position changed
- web design from mex3@

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt5
- import last changes from centaurus branding

* Fri Jan 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt1
- production slideshow
- installer wallpaper changed
- grub theme

* Wed Dec 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt11
- fvwm settings added

* Fri Nov 19 2010 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt4
- import last changes from centaurus:
  - gfxboot colors changed

* Tue Nov 16 2010 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt3
- import last changes from centaurus:
  - plymouth: scaling for non 4:3 or 16:9 resolutions fixed
  - non 4:3 or 16:9 resolutions support
  - typo in plymouth script fixed

* Fri Nov 12 2010 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt2
- update last changes from centaurus

* Thu Oct 28 2010 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt1
- update fixes from centaurus

* Thu Sep 30 2010 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt0.3
- update graphics from centaurus

* Tue Sep 14 2010 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt0.2
- update design, codename

* Thu Sep 09 2010 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt0.1
- update kdesktop design to 6.0.0 beta

* Tue Aug 31 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt4
- status changed to beta
- background changed

* Mon Aug 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt3
- fonts changed

* Tue May 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt2.2
- rebuld with design-bootloader-source 5.9

* Fri May 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt2.1
- rebuild with gfxboot.git-4.1.47

* Tue Apr 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt2
- product-logo.png changed

* Thu Mar 04 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt1
- Centaurus branding

* Wed Mar 03 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.1-alt1
- OO.o desktop files names changed

* Wed Dec 23 2009 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt28.M51.1
- built for M51

* Wed Dec 23 2009 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt29
- add icon for Firewall group
- remove "beta"

* Fri Nov 27 2009 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt26.M51.3
- built for M51

* Fri Nov 27 2009 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt28
- update steps and groups icons

* Mon Nov 23 2009 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt26.M51.2
- built for M51

* Mon Nov 23 2009 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt27
- update sysconfig-base icon

* Mon Nov 23 2009 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt26
- udpate graphics
- update alterator-browser-qt style
- remove bootsplash and graphics conflicts
- move status word to SouthEast

* Fri Oct 30 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0.0-alt25
- indexhtml:
  + change default indexhtml dir
  + use unified local documentation link

* Mon Oct 26 2009 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt22
- provide design-graphics and gnome-session-splash to avoid wrong 
  graphics package installation

* Thu Oct 22 2009 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt21
- fix Russian name and copyright years
- fix images
- remove beta status

* Tue Sep 24 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt24
- new pictures

* Mon Sep 07 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt20
- beep on boot disabled

* Thu Aug 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt19
- production images, slides (and colors?)

* Sun Jul 12 2009 Alexey Rusakov <ktirf@altlinux.org> 5.0.0-alt18.1.1
- fix unexpanded autoconf substitute (closes bug 20757)
- beautify theme names in -gnome-settings

* Thu Jun 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt18.1
- titles removed from wallpater and installer 

* Wed Jun 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt18
- sources restructure 

* Thu Jun 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt17
- ksplashrc added for kde4
- kde3-settings and splash for kde3 added (mex@)
- gnome-settngs added (mex@)

* Wed May 13 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt16
- \%setup fixed from boyarsh@
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
- status_en intorduces for release file 

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

