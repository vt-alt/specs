%define brand alt
%define Brand ALT
%define theme education
%define Theme Education
%define codename FalcoRusticolus
%define status %nil
%define status_en %nil
%define distro_name ALT Education 9.0%status_en
%define flavour %brand-%theme

%define gtk_theme Breeze
%define kde_theme Breeze
%define icon_theme Papirus-Light
%define window_theme Smoothwall

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

Name: branding-%flavour
Version: 9.0
Release: alt1

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

%define distro_name_ru Альт Образование 9.0%status

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

Requires(post,preun): alternatives >= 0.2
%branding_add_conflicts %flavour graphics

%description graphics
This package contains some graphics for %distro_name design.

%description graphics -l ru_RU.UTF-8
В данном пакете находится необходимые графические элементы для дистрибутива 
%distro_name_ru.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release

%package release
BuildArch: noarch
Summary:  %distro_name release file
Summary(ru_RU.UTF-8): Описание дистрибутива %distro_name_ru
License:  GPL
Group:    System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list  branding-alt-%theme-release
%branding_add_conflicts %flavour release
Requires: pam-limits-desktop

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

%package kde-settings
BuildArch: noarch
Summary: KDE settings for %distro_name (for KDE4 and KF5)
License: Distributable
Group:   Graphical desktop/KDE
Requires(pre): %name-graphics
Requires: kde5-konsole-colorscheme-SolarizedPastel
Requires: plasma5-breeze
Requires: fonts-ttf-liberation
Requires: fonts-ttf-google-droid-sans-mono
Provides: branding-%flavour-kde4-settings = %version-%release
Obsoletes: branding-%flavour-kde4-settings < %version-%release
%branding_add_conflicts %flavour kde-settings
%branding_add_conflicts %flavour kde4-settings

%description kde-settings
KDE settings for %distro_name (for KDE4 and KF5)

%package xfce-settings
BuildArch: noarch
Summary: Default settings for XFCE for %distro_name
License: Distributable
Group: Graphical desktop/XFce
Requires: etcskel
Requires: fonts-ttf-liberation
Requires: fonts-ttf-google-droid-sans-mono
Requires: fonts-ttf-google-noto-sans
Requires: gnome-icon-theme
# Specified themes
Requires: icon-theme-ePapirus
Requires: icon-theme-Papirus
Requires: icon-theme-Papirus-Dark
Requires: icon-theme-Papirus-Light
Requires: gtk-theme-breeze
Requires(post): lightdm-gtk-greeter
# XFCE plugins
Requires: xfce4-whiskermenu-plugin
Requires: xfce4-pulseaudio-plugin
Requires: branding-%brand-%theme-graphics
%branding_add_conflicts %flavour xfce-settings

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
# Specified themes
Requires: icon-theme-ePapirus
Requires: icon-theme-Papirus
Requires: icon-theme-Papirus-Dark
Requires: icon-theme-Papirus-Light
Requires: gtk-theme-breeze
#
%branding_add_conflicts %flavour mate-settings
Requires(post): lightdm-gtk-greeter
Requires(post): libgio

%description mate-settings
MATE settings for %distro_name

%package slideshow
Summary: Slideshow for %distro_name installer
Summary(ru_RU.UTF-8): Изображения для организации "слайдшоу" в установщике дистрибутива %distro_name_ru
License: Distributable
Group: System/Configuration/Other 
BuildArch: noarch
%branding_add_conflicts %flavour slideshow

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
Requires: docs-alt-%theme
Requires: shared-desktop-icons
Requires(post): indexhtml-common

%description indexhtml
%distro_name welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
%distro_name_ru.

%package menu
BuildArch: noarch
Summary: Menu for %distro_name
License: Distributable
Group: Graphical desktop/Other
Requires(pre): altlinux-freedesktop-menu-common
Requires: altlinux-freedesktop-menu-common
%branding_add_conflicts %flavour menu

%description menu
Menu for %distro_name

%package system-settings
BuildArch: noarch
Summary: Some system settings for %distro_name
License: GPLv2+
Group: System/Base
# Really we need lightdm only, but it can pull another greeter.
Requires: lightdm-gtk-greeter
%branding_add_conflicts %flavour system-settings

%description system-settings
Some system settings for %distro_name.

%prep
%setup -n branding

%ifnarch %arm
%define x86 boot
%else
%define x86 %nil
%endif

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' CODENAME='%codename' X86='%x86' GTK_THEME='%gtk_theme' KDE_THEME='%kde_theme' ICON_THEME='%icon_theme' WINDOW_THEME='%window_theme' ./configure
make

%install
%makeinstall
find %buildroot -name \*.in -delete

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

%post system-settings
#chown _ldm:_ldm %_localstatedir/ldm/.pam_environment
sed -i '/pam_env\.so/ {
		/user_readenv/ b
		s/pam_env\.so/pam_env.so user_readenv=1/ }
' %_sysconfdir/pam.d/lightdm-greeter

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

%post mate-settings
subst 's/^#\?theme-name=.*/theme-name=%gtk_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?icon-theme-name=.*/icon-theme-name=%icon_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?indicators=.*/indicators=~clock;~spacer;~host;~spacer;~session;~layout;~a11y;~power/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?clock-format=.*/clock-format=%A, %x %H:%M/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas

%post xfce-settings
subst 's/^#\?theme-name=.*/theme-name=%gtk_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?icon-theme-name=.*/icon-theme-name=%icon_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?indicators=.*/indicators=~clock;~spacer;~host;~spacer;~session;~layout;~a11y;~power/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?clock-format=.*/clock-format=%A, %x %H:%M/' /etc/lightdm/lightdm-gtk-greeter.conf ||:

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
%_iconsdir/hicolor/*/apps/alt-%theme.png

%files bootsplash
%ifarch %ix86 x86_64
%_datadir/plymouth/themes/%theme/*
%endif

%files release
%_sysconfdir/*-release
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files kde-settings
%_datadir/kf5/konsole/%Theme.profile
/etc/skel/.config/autostart/nm-applet.desktop
/etc/skel/.config/kdeglobals
/etc/skel/.config/konsolerc

%files fvwm-settings
%_sysconfdir/skel/.fvwm2rc

%files mate-settings
%_datadir/glib-2.0/schemas/*.gschema.override

%files xfce-settings
%_sysconfdir/X11/profile.d/zdg-move-templates.sh
/etc/skel/XDG-Templates.skel/
/etc/skel/.wm-select
/etc/skel/.config
%exclude /etc/skel/.config/autostart/nm-applet.desktop
%exclude /etc/skel/.config/konsolerc
%exclude /etc/skel/.config/kdeglobals
/etc/skel/.face
/etc/skel/.gconf
/etc/skel/.gtkrc-2.0
/etc/skel/.local
/etc/skel/.vimrc
/etc/skel/.recoll

%files slideshow
/etc/alterator/slideshow.conf
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %_defaultdocdir/indexhtml/index.html
%_defaultdocdir/indexhtml/*
%_desktopdir/*
%_datadir/kf5/kio_desktop/DesktopLinks/indexhtml.desktop
%attr(0755,root,root) %_datadir/Desktop/indexhtml.desktop
%_iconsdir/hicolor/*/apps/alt-%theme-desktop.png

%files menu
/usr/share/slinux-style
/etc/xdg/menus/xfce-applications-merged/50-xfce-applications.menu
/usr/share/desktop-directories/altlinux-wine.directory

%files system-settings
%config %_sysconfdir/polkit-1/rules.d/*.rules
#config %_localstatedir/ldm/.pam_environment

%changelog
* Fri Aug 30 2019 Andrey Cherepanov <cas@altlinux.org> 9.0-alt1
- Release 9.0.

* Mon Aug 19 2019 Andrey Cherepanov <cas@altlinux.org> 8.93-alt1
- Beta2.
- Use icon theme Papirus-Light instead of Papirus for more contrast symbol icons.

* Fri Jul 19 2019 Andrey Cherepanov <cas@altlinux.org> 8.92-alt1
- Beta version of ALT Education 9.0.
- xfce-settings: use random screensaver by default.
- plasma: remove empty bookmarks tab in menu.

* Fri Jun 14 2019 Andrey Cherepanov <cas@altlinux.org> 8.91-alt2
- Make progressbar label brighter

* Tue Jun 11 2019 Andrey Cherepanov <cas@altlinux.org> 8.91-alt1
- Replace gnome-system-monitor for xfce4-taskmanager for Ctrl+Alt+Delete.
- Fix Plasma panel: change menu to Kickoff, set distro icon, remove lock and logout icons.

* Tue Apr 30 2019 Andrey Cherepanov <cas@altlinux.org> 8.90-alt1
- Alpha version of ALT Education 9.0.

* Thu Jan 31 2019 Andrey Cherepanov <cas@altlinux.org> 8.2-alt0.M80P.2
- Add Droid fonts used in XFCE.
- Remove overrided desktop file for system-config-printer.
- Fix menu on window key.
- Add xfce4-clipman.desktop.
- Replace standard XFCE menu by Whisker menu, mixer plugin by pulseaudio plugin.
- Simplify panel in XFCE.
- Remove Simply Linux logo and wallpapers.

* Fri May 12 2017 Andrey Cherepanov <cas@altlinux.org> 8.2-alt0.M80P.1
- New release
- Use pam-limits-desktop instead of own limits rules
- Remove altlinux.ru from files

* Fri Oct 21 2016 Andrey Cherepanov <cas@altlinux.org> 8.1-alt0.M80P.1
- Increase release number

* Thu Oct 20 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.5.M80P.1
- Complete Russian localization of menu
- Update indexhtml: fix URLs of official site sections URL and books location

* Mon Sep 05 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.4.M80P.1
- Use bright Education icon suitable both for light and dark backgrounds
- Rename kde4-settings to kde-settings, package Konsole profile and
  disable nm-applet.desktop autostart in KDE

* Tue Aug 30 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.3.M80P.1
- Set yellow labels for gfxboot
- Use predefined boot.png with logo for grub
- Set bright color for menubar in grub

* Fri Aug 26 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.2.M80P.1
- Do not require polkit-gnome
- Set SimpleSL icon theme in XFCE settings

* Fri Aug 26 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.1.M80P.2
- Rebuild with conflict with branding-xalt-kworkstation

* Fri Jul 22 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.1.M80P.1
- Initial build
