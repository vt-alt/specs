%define brand alt
%define Brand ALT
%define theme tonk
%define Theme TONK
%define codename %nil
%define status %nil
%define status_en %nil
%define distro_name ALT TONK%status_en
%define flavour %brand-%theme

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

Name: branding-%flavour
Version: 9.0
Release: alt1

ExclusiveArch: %ix86 x86_64

%ifarch %ix86 x86_64
BuildRequires: gfxboot >= 4
%endif
BuildRequires: cpio fonts-ttf-dejavu fonts-ttf-google-droid-sans
BuildRequires: design-bootloader-source >= 5.0-alt2

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel fribidi

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPLv2+

%define distro_name_ru Альт ТОНК%status

%description
Distro-specific packages with design and texts for %distro_name.

%description -l ru_RU.UTF-8
Пакеты оформления для дистрибутива %distro_name_ru.

%package bootloader
Group:   System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
Summary(ru_RU.UTF-8): Тема для экрана выбора вариантов загрузки (lilo и syslinux) 
License: GPLv2+

Requires(pre):    coreutils
Provides:  design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
%branding_add_conflicts %flavour bootloader

%define grub_normal white/light-blue
%define grub_high black/light-gray

%description bootloader
Here you find the graphical boot logo for %distro_name.
Suitable for both lilo and syslinux.

%description bootloader -l ru_RU.UTF-8
В данном пакете находится тема для экрана выбора вариантов загрузки (lilo и syslinux)
для дистрибутива %distro_name_ru.

%package bootsplash
Summary:  Theme for splash animations during bootup
Summary(ru_RU.UTF-8): Тема для экрана загрузки для дистрибутива %distro_name_ru
License:  Distributable
Group:    System/Configuration/Boot and Init
Provides: plymouth-theme-%theme
Requires: plymouth-plugin-script
Requires(pre):   plymouth

%branding_add_conflicts %flavour bootsplash

%description bootsplash
This package contains graphics for boot process for %distro_name
(needs console splash screen enabled).

%description bootsplash -l ru_RU.UTF-8
В данном пакете находится тема для экрана загрузки для дистрибутива
%distro_name_ru.

%package alterator
Summary: Design for alterator for %distro_name
Summary(ru_RU.UTF-8): Тема для "Центра управления системой" и QT для дистрибутива %distro_name_ru
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes:  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt 

# lexicographically first of the village
Conflicts: branding-sisyphus-server-light-alterator

%branding_add_conflicts %flavour alterator
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server branding-altlinux-backup-server-alterator
Requires(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for %distro_name.

%description alterator -l ru_RU.UTF-8
В данном пакете находится тема для "Центра управления системой" (Alterator)
и модулей библиотеки QT для дистрибутива %distro_name_ru.

%package graphics
Summary: Design for %distro_name
Summary(ru_RU.UTF-8): Тема для дистрибутива %distro_name_ru
License: Different licenses
Group: Graphics
BuildArch: noarch

Provides: design-graphics-%theme  branding-alt-%theme-graphics
Obsoletes:  branding-alt-%theme-graphics design-graphics-%theme
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix

PreReq(post,preun): alternatives >= 0.2
%branding_add_conflicts %flavour graphics

%description graphics
This package contains some graphics for %distro_name design.

%description graphics -l ru_RU.UTF-8
В данном пакете находится необходимые графические элементы для дистрибутива 
%distro_name_ru.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-5.0 altlinux-release-5.1 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business
%package release

Summary:  %distro_name release file
Summary(ru_RU.UTF-8): Описание дистрибутива %distro_name_ru
License:  GPL
Group:    System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list  branding-alt-%theme-release
%branding_add_conflicts %flavour release

%description release
%distro_name release file.

%description release -l ru_RU.UTF-8
В данном пакете находится описание дистрибутива %distro_name_ru.

%package notes
BuildArch: noarch
Provides:  alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary:   Distribution license and release notes
Summary(ru_RU.UTF-8): Лицензия и дополнительные сведения для дистрибутива %distro_name_ru
License:   Distributable
Group:     Documentation
%branding_add_conflicts %flavour notes

%description notes
Distribution license and release notes

%description notes -l ru_RU.UTF-8
В данном пакете находится лицензия и дополнительные сведения
для дистрибутива %distro_name_ru.

%package kde4-settings
BuildArch: noarch
Summary: KDE4 settings for %distro_name
License: Distributable
Group:   Graphical desktop/KDE
Provides: branding-%flavour-kde4-settings = %version-%release
Obsoletes: branding-%flavour-kde4-settings < %version-%release
%branding_add_conflicts %flavour kde-settings
%branding_add_conflicts %flavour kde4-settings
PreReq: %name-graphics

%description kde4-settings
KDE4 settings for %distro_name

%package xfce-settings
Summary: default settings for Xfce 4.6 for %distro_name
License: Distributable
Group: Graphical desktop/XFce
Requires: PolicyKit-gnome
Requires: etcskel gtk3-theme-clearlooks-phenix
Requires: gnome-icon-theme icon-theme-simple-school
Requires: branding-%brand-%theme-graphics
Obsoletes: xfce-settings-lite xfce-settings-school-lite
%branding_add_conflicts %flavour xfce-settings
Conflicts: xfce-settings-simply-linux

%description xfce-settings
XFCE settings for %distro_name

%package fvwm-settings
BuildArch: noarch
Summary: FVWM2 settings for %distro_name
License: Distributable
Group:   Graphical desktop/FVWM based
Requires: altlinux-freedesktop-menu-gnomish-menu
%branding_add_conflicts %flavour fvwm-settings

%description fvwm-settings
FVWM2 settings for %distro_name

%package mate-settings
BuildArch: noarch
Summary: MATE settings for %distro_name
License: Distributable
Group:   Graphical desktop/GNOME
Requires: gksu
Requires: dconf
Requires: theme-mate-windows
%branding_add_conflicts %flavour mate-settings
PreReq(post): lightdm-gtk-greeter
PreReq(post): libgio
PreReq(post): mate-backgrounds

%description mate-settings
MATE settings for %distro_name

%package slideshow
Summary: Slideshow for %distro_name installer
Summary(ru_RU.UTF-8): Изображения для организации "слайдшоу" в установщике дистрибутива %distro_name_ru
License: Distributable
Group: System/Configuration/Other
%branding_add_conflicts %flavour slideshow

BuildArch: noarch

%description slideshow
Slideshow for %distro_name installer.

%description slideshow -l ru_RU.UTF-8
В данном пакете находятся изображения для организации "слайдшоу" в установщике
дистрибутива %distro_name_ru.

%package indexhtml
BuildArch: noarch
Summary:  HTML welcome page for %distro_name
Summary(ru_RU.UTF-8): Стартовая страница для дистрибутива %distro_name_ru
License:  distributable
Group:    System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop
%branding_add_conflicts %flavour indexhtml

Requires: xdg-utils 
Requires(post): indexhtml-common

%description indexhtml
%distro_name welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
%distro_name_ru.

%package menu
Summary: Menu for %distro_name
License: Distributable
Group: Graphical desktop/Other
Requires(pre): altlinux-freedesktop-menu-common
Requires: altlinux-freedesktop-menu-common
%branding_add_conflicts %flavour menu

%description menu
Menu for %distro_name

%package system-settings
Summary: Some system settings for Simply Linux
License: GPLv2+
Group: System/Base
# Really we need lightdm only, but it can pull another greeter.
Requires: lightdm-gtk-greeter
Requires: /proc
%branding_add_conflicts %flavour system-settings

%description system-settings
Some system settings for Simply Linux.

%prep
%setup -n branding

%ifnarch %arm
%define x86 boot
%else
%define x86 %nil
%endif

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' CODENAME='%codename' X86='%x86' ./configure
make

%install
%makeinstall

#graphics
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
mkdir -p %buildroot/%_niconsdir
install graphics/icons/slinux.png %buildroot/%_niconsdir/slinux.png
install graphics/icons/mini/slinux.png %buildroot/%_iconsdir/altlinux.png
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
echo "%distro_name" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done
install -pD -m644 components/systemd/os-release %buildroot%_sysconfdir/os-release

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

ln -s license.ru.html %buildroot%_datadir/alt-notes/license.uk.html

#fwvm-settings
mkdir -p %buildroot/etc/skel
install -m 644 fvwm-settings/.fvwm2rc %buildroot/etc/skel/

install -Dm0644 mate-settings/%theme-default.xml %buildroot%_datadir/mate-background-properties/%theme-default.xml
# Put Skype icon to menu
install -Dm0644 menu/applications/skype.desktop %buildroot%_desktopdir/skype.desktop
install -Dm0644 menu/pixmaps/skype.png %buildroot%_pixmapsdir/skype.png

mkdir -p %buildroot/etc/skel/XDG-Templates.skel/

cp -r xfce-settings/etcskel/* %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.config %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.local %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.gconf %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.vimrc %buildroot/etc/skel/

install -m 644 xfce-settings/etcskel/.wm-select %buildroot/etc/skel/

mkdir -p %buildroot/usr/share/backgrounds/xfce/
cp -P xfce-settings/backgrounds/*.{jpg,png} %buildroot/usr/share/backgrounds/xfce/

install -pDm0755 xfce-settings/scripts/zdg-move-templates.sh %buildroot%_sysconfdir/X11/profile.d/zdg-move-templates.sh

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
mkdir -p %buildroot/etc/alterator
cp -a slideshow/*  %buildroot/usr/share/install2/slideshow/
install slideshow/slideshow.conf %buildroot/etc/alterator/
# Set English slideshow as default
#ln -s slides-en %buildroot/usr/share/install2/slideshow/slides

#indexhtml
%define _altdocsdir %_defaultdocdir/alt-docs
%define _indexhtmldir %_defaultdocdir/indexhtml
install components/indexhtml/*.html %buildroot%_defaultdocdir/indexhtml/
mkdir -p %buildroot%_defaultdocdir/indexhtml/images
install components/indexhtml/images/* %buildroot%_defaultdocdir/indexhtml/images/
#install -m644 components/indexhtml.desktop %buildroot%_desktopdir/

#menu
mkdir -p %buildroot/usr/share/slinux-style/applications
install menu/applications/* %buildroot/usr/share/slinux-style/applications/
mkdir -p %buildroot/etc/xdg/menus/xfce-applications-merged
cp menu/50-xfce-applications.menu %buildroot/etc/xdg/menus/xfce-applications-merged/
mkdir -p %buildroot/usr/share/desktop-directories
cp menu/altlinux-wine.directory %buildroot/usr/share/desktop-directories/

# system-settings
mkdir -p %buildroot/%_sysconfdir/polkit-1/rules.d/
cp -a system-settings/polkit-rules/*.rules %buildroot/%_sysconfdir/polkit-1/rules.d/

#bootloader
%ifarch %ix86 x86_64
%pre bootloader
[ -s /usr/share/gfxboot/%theme ] && rm -fr  /usr/share/gfxboot/%theme ||:
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:
%endif

%post bootloader
%ifarch %ix86 x86_64
%__ln_s -nf %theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
#shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high
%endif

%ifarch %ix86 x86_64
%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message
%endif

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
%ifarch %ix86 x86_64
%_datadir/gfxboot/%theme
/boot/splash/%theme
/boot/grub/themes/%theme
%endif

#bootsplash
%post bootsplash
%ifarch %ix86 x86_64
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf
[ -f /etc/sysconfig/grub2 ] && \
      subst "s|GRUB_WALLPAPER=.*|GRUB_WALLPAPER=/usr/share/plymouth/themes/%theme/grub.jpg|" \
             /etc/sysconfig/grub2 ||:
%endif

#mate-settings
%preun mate-settings
if [ -d /usr/share/mate-background-properties ]; then
	sed -i 's| deleted="true">| deleted="false">|g' /usr/share/mate-background-properties/mate-*.xml
fi

%post mate-settings
subst 's,^background=.*,background=/usr/share/design/current/backgrounds/login-screen.jpg,' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/#theme-name=/theme-name=Clearlooks-Phenix/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas
if [ -d /usr/share/mate-background-properties ]; then
	sed -i 's| deleted="false">| deleted="true">|g' /usr/share/mate-background-properties/mate-*.xml
fi

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
%_niconsdir/slinux.png
%_iconsdir/altlinux.png

%files bootsplash
%ifarch %ix86 x86_64
%_datadir/plymouth/themes/%theme/*
%exclude %_datadir/plymouth/themes/%theme/*.in
%endif

%files release
%_sysconfdir/*-release
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files kde4-settings
%_sysconfdir/kde4/xdg/menus/applications-merged/*.menu
%_sysconfdir/skel/.kde4

%files fvwm-settings
%_sysconfdir/skel/.fvwm2rc

%files mate-settings
%_datadir/mate-background-properties/%theme-default.xml
%_pixmapsdir/skype.png

%files xfce-settings
%_sysconfdir/X11/profile.d/zdg-move-templates.sh
/etc/skel/XDG-Templates.skel/
/etc/skel/.wm-select
/etc/skel/.config
/etc/skel/.local
/etc/skel/.gconf
/etc/skel/.vimrc
/usr/share/backgrounds/xfce/*

%files slideshow
/etc/alterator/slideshow.conf
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %_indexhtmldir/index.html
%_indexhtmldir/*
%_desktopdir/*
%_datadir/kde4/apps/kio_desktop/DesktopLinks/indexhtml.desktop

%files menu
/usr/share/slinux-style
/etc/xdg/menus/xfce-applications-merged/50-xfce-applications.menu
/usr/share/desktop-directories/altlinux-wine.directory

%files system-settings
%config %_sysconfdir/polkit-1/rules.d/*.rules

%changelog
* Mon Sep 23 2019 Andrey Cherepanov <cas@altlinux.org> 9.0-alt1
- Build on p9.

* Tue Mar 05 2019 Andrey Cherepanov <cas@altlinux.org> 8.3-alt0.M80P.3
- Use package theme-mate-windows.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 8.3-alt0.M80P.2
- Remove Skype icon from desktop.

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 8.3-alt0.M80P.1
- Add new boot logo, wallpapers for login screen and desktop.
- Use branding macros for simplify spec file.
- Make login screen and desktop wallpaper different.
- TONK default wallpapers XML-description for MATE desktop added. (thanks klark@)
- Turn ON/OFF default MATE wallpapers in graphics pre/post-sections added. (thanks klark@)

* Tue Jun 06 2017 Michael Shigorin <mike@altlinux.org> 8.2-alt1
- Renamed to ALT TONK

* Tue Dec 27 2016 Michael Shigorin <mike@altlinux.org> 7.9.3-alt2
- Conflict with xalt-kworkstation odour^Wflavour

* Mon Nov 30 2015 Michael Shigorin <mike@altlinux.org> 7.9.3-alt1
- Updated schemes (xkb flags, -progressbar, vino settings by erik@)

* Fri Nov 06 2015 Michael Shigorin <mike@altlinux.org> 7.9.2-alt1
- Updated schemes with tonk layout (thx cas@)

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 7.9.1-alt1
- Updated schemes (thx cas@)

* Fri Sep 25 2015 Michael Shigorin <mike@altlinux.org> 7.9-alt1
- New flavour: altlinux-tonk (MATE based)

* Mon Apr 13 2015 Andrey Cherepanov <cas@altlinux.org> 7.0.5-alt0.M70P.2
- Update copyright years, fix VK group URL and update company address
- Fix button gluing in web interface
- Fix package name with Droid fonts
- Generate image for selection bar in GRUB menu from specified color

* Wed Jun 11 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.5-alt0.M70P.1
- Backport to p7 branch

* Wed Jun 11 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.5-alt1
- New release

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.4-alt1
- New release

* Fri Feb 14 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.3-alt3
- Set light blue background in rEFIt by set correct pixel color in top
  left corner of background image
- Remove abandoned web resource planet.altlinux.org from indexhtml

* Thu Feb 13 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.3-alt2
- Rebuild with updated gfxboot

* Wed Feb 05 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.3-alt1
- Fix license

* Tue Dec 24 2013 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt1
- Release 7.0.2

* Tue Dec 17 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.9-alt3
- indexhtml requires docs-school-teacher
- beta version

* Thu Dec 05 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.9-alt2
- Pack wide wallpaper and product logo
- Fix favicon and logo width in Alterator web-interface
- Fix bootloader colors
- Hide section border, simplify tooltips, turn off checkbox and
  radiobutton highlight in installer
- Replace Simply Linux logo by Platform Seven logo
- Simplify GRUB config
- Use icon-theme-simple-school

* Thu Nov 21 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.9-alt1
- Update branding for Seven platform

* Wed Aug 29 2012 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt5
- Set correct distribution name

* Mon Aug 20 2012 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt4
- Fix indexhtml menu and distro name

* Mon Aug 20 2012 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt3
- Fix attribute name for meta http-equiv
- Fix grub background color and font

* Fri Jul 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt2
- autoboot from usb

* Tue Nov 22 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt1
- school variant

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt3
- Set elflord as colorscheme for vim.
- Add apps/%%gconf.xml for gconf.

* Tue Oct 25 2011 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt2
- Fix grub2 font.
- Update xfce4-power-manager's settings.

* Fri Oct 14 2011 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt1
- Fix indexhtml.desktop.
- menu: Add pavucontrol.desktop.
- Drop not needed audacious2.desktop.
- blueman settings: Set Thunar as browser for obex protocol.
- xkb-plugin settings: Don't hardcode layout, model, etc.
- Fix keyboard default settings.

* Thu Sep 22 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt29
- Use preferences-system icon for wine-regedit.
- Add TryExec to desktop files.
- Fix desktop file for celestia.
- Fix wine menu.
- gfxboot: Change menu position.
- new desktop files (by Alexandra Panyukova).
- Wine moved in subdirectory in menu (by Alexandra Panyukova).

* Mon Sep 19 2011 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt28
- Fix indexhtml translation on English

* Fri Sep 16 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt27
- wine menu section became below other sections (by Alexandra Panyukova).
- Add TryExec into the wine's desktop files.
- wine desktop files added; wine settings in settings menu grouped
  together; (by Alexandra Panyukova).

* Fri Sep 16 2011 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt26
- Add requires for documentation

* Thu Sep 15 2011 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt25
- Use russian license text for Ukrainian
- Fix English text in indexhtml

* Tue Sep 13 2011 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt24
- Add project web-site
- Fix ALT Linux web-site in English version

* Tue Sep 13 2011 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt23
- Fix build

* Tue Sep 13 2011 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt22
- New indexhtml design with more links

* Thu Aug 25 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt21
- menu: Change 'Xfce about' icon.
- desktop: Fix trash icon position.
- Fix web browser's and mail client's icons.

* Mon Aug 22 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt20
- grub: Change letters colour to dark-gray (closes: #25889).
- xfdesktop: Set image-style to 'auto'.

* Fri Aug 19 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt19
- slideshow: timeout 30sec, repeat slideshow.
- Drop xfce4-popup-menu shortcut.
- Set panel opacity to 100 by default.
- index.html: Fix FAQ link.

* Wed Aug 10 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt18
- New slides.
- Drop mpd stuff.
- xfce4-mixer: Set pulseaudio as default device.
- text for first installer step on livecd added (by Alexandra Panyukova).
- white color for installer titles (by Alexandra Panyukova).

* Fri Jul 29 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt17
- removing thunderbird and Terminal from panel (by Alexandra Panyukova).
- codename Flounder (by Alexandra Panyukova).
- wide wallpaper became default (by Alexandra Panyukova).
- s/slinux/simplylinux/ (by Alexandra Panyukova).
- new color for alterator background (by Alexandra Panyukova).
- New slinux logo.
- New slides.
- Add TryExec into menu desktop files (closes: #25859).
- Add slideshow.
- Drop slinux-thunar icon.
- Drop Thunar launcher from panel.
- Change theme to Clearlooks.
- Fix steps icons location.
- Don't show frame around clock.
- Revert "panel became gray".

* Fri Jul 01 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt16
- Drop altlinux-menus requires.
- Rename and fix fusion-icon.desktop for autostart.
- backgrounds: Replace slinux_spring_*.png with slinux_spring_*.jpg.

* Thu Jun 30 2011 Alexandra Panyukova <mex3@altlinux.ru> 6.0.0-alt15
- wallpapers path fixed
- more sizes of thunar icons
- greeting, installer, lilo and finish step icons added

* Tue Jun 28 2011 Alexandra Panyukova <mex3@altlinux.ru> 6.0.0-alt14
- new wallpapers
- new thunar icon
- adding symlink for final step in installer

* Fri Jun 17 2011 Alexandra Panyukova <mex3@altlinux.ru> 6.0.0-alt13
- translation of desktop-files for libreoffice, xkill and eiskaltdcpp-gt
- web-browser icon on xfce panel changed on firefox icon
- new icons on livecd installer steps

* Thu Jun 16 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt12
- indexhtml: change link to user manual (by Artem Zolochevskiy).
- menu: Drop unneeded desktop files.
- etcscel: Changed display type of xkb plugin.

* Tue Jun 14 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt11
- new desktop files for libreoffice and xkill (by Alexandra Panyukova).
- new images for installer steps (by Alexandra Panyukova).
- menu subpackage added (by Alexandra Panyukova).
- trying to replace some elements in bootloader (by Alexandra Panyukova).
- style changes in grub theme (by Alexandra Panyukova).
- trying to read images less times in bootloader (by Alexandra Panyukova).
- new menu items (by Alexandra Panyukova).
- new grub theme (by Alexandra Panyukova).
- etcskel: Drop xfce4-terminal.desktop.
- etcskel: Drop ristretto.desktop.
- Show gnome-screensever preferences in xfce4 settings.
- etcskel: Drop nm-applet.desktop.
- making grey points in menu from the beginning (by Alexandra Panyukova).
- testing default version of menu.inc (by Alexandra Panyukova).

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt10
- Tune desktop: show trash, don't show removable disks.
- etcskel: Move Russian Music to Documents.
- etcskel: Move Russian Templates to Documents.
- etcskel: Drop sonata config.

* Thu May 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt9
- gfxboot design

* Mon May 23 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt8
- Font: Droid Sans.
- Cursor theme: jimmac.

* Fri May 20 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt7
- helpers.rc: Add more defaults.

* Fri May 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt6
- gfxboot colors changed

* Tue May 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt5
- bootsplash changed from centaurus to simply

* Mon May 16 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt4
- fix automatic boot from usb disk

* Sat May 14 2011 Mikhail Efremov <sem@altlinux.org> 6.0.0-alt3
- Minor spec cleanup.
- Add compiz configs to /etc/skel.
- Fix fusion-icon config: newline at the end.

* Fri May 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt2
- gear repo structure changed to comply other brandings
- gfxboot colors changed

* Wed Apr 13 2011 Alexandra Panyukova <mex3@altlinux.ru> 6.0.0-alt1
- new version

* Fri Dec 17 2010 Alexandra Panyukova <mex3@altlinux.ru> 5.0.2-alt1
- version for 5.0.2:
-- new wallpapers
-- some new xfce default settings

* Fri Apr 30 2010 Alexandra Panyukova <mex3@altlinux.ru> 5.0.1-alt3
- test user bindings removed (Closes: 23327)
- returning icon for alterator (Closes: 23316)
- removing local *.desktop files for often deleted packages

* Mon Apr 05 2010 Alexandra Panyukova <mex3@altlinux.ru> 5.0.1-alt2
- xfce-settings for simply linux 5.0.1

* Thu Mar 04 2010 Alexandra Panyukova <mex3@altlinux.ru> 5.0.1-alt1
- merged with xfce-settings-simply-linux

* Tue Nov 24 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt12
- Some repocop warnings is taken into account.

* Tue Nov 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt11
- Some repocop warnings is taken into account.

* Tue Nov 03 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt9.M51.1
- Backport to 5.1.

* Tue Nov 03 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt10
- Version update for easy backport to 5.1.

* Mon Nov 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt9
- Indexhtml page changed.

* Sun Oct 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt8
- Changed colors for bootsplash.
- Changed license page fonts.
- Changed logo for slideshow.

* Sat Oct 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt7
- Simply Linux 5.0 RC3 release.

* Wed Oct 14 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt6
- Added new bootloader theme.

* Sun Oct 04 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt5
- Simply Linux RC2.

* Tue Sep 08 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt4
- Removed misspellings in bootsplash text for 640x480 and 800x600 modes

* Wed Aug 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt3
- Added brand icon an Russian description for package.

* Thu Aug 13 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt2
- Update for bootsplash.

* Sat Jun 13 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt1
- Fork from branding-altlinux-lite

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
- Lite version

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

