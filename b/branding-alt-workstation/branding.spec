%define brand alt
%define Brand ALT
%define theme workstation
%define Theme Workstation
%define codename Laertes
%define status %nil
%define status_en %nil
%define flavour %brand-%theme

%define gtk_theme BlueMenta
%define icon_theme Papirus

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

%define data_cur_dir %_datadir/branding-data-current

%define _unpackaged_files_terminate_build 1

Name: branding-%flavour
Version: 9.1
Release: alt1
Url: https://basealt.ru

%ifarch %ix86 x86_64
BuildRequires: gfxboot >= 4
BuildRequires: cpio fonts-ttf-dejavu fonts-ttf-google-droid-sans
BuildRequires: design-bootloader-source >= 5.0-alt2 fribidi
%endif

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPLv2+

%define distro_name ALT Workstation %version%status_en
%define distro_name_ru Альт Рабочая станция %version%status

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
BuildArch: noarch
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

%package mate-settings
BuildArch: noarch
Summary: MATE settings for %distro_name
License: Distributable
Group:   Graphical desktop/GNOME
Requires: dconf
# Specified themes
Requires: icon-theme-ePapirus
Requires: icon-theme-Papirus
Requires: icon-theme-Papirus-Dark
Requires: icon-theme-Papirus-Light
Requires: mate-themes
Requires: theme-mate-windows
Requires: x-cursor-theme-jimmac
#
%branding_add_conflicts %flavour mate-settings
%branding_add_conflicts %flavour graphics
Requires(post): lightdm-gtk-greeter
Requires(post): libgio
# To avoid install check conflicts
Requires: %name-graphics = %EVR
Conflicts: installer-feature-lightdm-stage3 < 0.1.0-alt1

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
Requires: menu-icons-default
Requires(post): indexhtml-common

%description indexhtml
%distro_name welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
%distro_name_ru.

%prep
%setup -n branding

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' CODENAME='%codename' GTK_THEME='%gtk_theme' ICON_THEME='%icon_theme' ./configure
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
[ "$1" -eq 1 ] || exit 0
%ifarch %ix86 x86_64
ln -snf %theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message
%endif
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
#shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high

%ifarch %ix86 x86_64
%preun bootloader
[ "$1" -eq 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    rm -f /boot/splash/message
%endif

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
%ifarch %ix86 x86_64
%_datadir/gfxboot/%theme
/boot/splash/%theme
%endif
/boot/grub/themes/%theme

#bootsplash
%post bootsplash
[ "$1" -eq 1 ] || exit 0
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf
[ -f /etc/sysconfig/grub2 ] && \
      subst "s|GRUB_WALLPAPER=.*|GRUB_WALLPAPER=/usr/share/plymouth/themes/%theme/grub.jpg|" \
             /etc/sysconfig/grub2 ||:

%post mate-settings
[ "$1" -eq 1 ] || exit 0
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas

#release
%post release
if ! [ -e %_sysconfdir/altlinux-release ] && \
   ! [ -e %_sysconfdir/os-release ]; then
	cp -a %data_cur_dir/release/*-release %_sysconfdir/
fi

#notes
%post notes
if ! [ -e %_datadir/alt-notes/license.all.html ]; then
	cp -a %data_cur_dir/alt-notes/license.*.html %_datadir/alt-notes/
fi

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
#_iconsdir/hicolor/*/apps/alt-%theme.png

%files bootsplash
%_datadir/plymouth/themes/%theme/*

%files release
%dir %data_cur_dir
%data_cur_dir/release/
%_sysconfdir/buildreqs/packages/ignore.d/*
%ghost %config(noreplace) %_sysconfdir/*-release

%files notes
%dir %data_cur_dir
%data_cur_dir/alt-notes
%_datadir/alt-notes/livecd-*
%_datadir/alt-notes/release-notes.*
%ghost %config(noreplace) %_datadir/alt-notes/license.*.html

%files mate-settings
%_sysconfdir/skel/.config/
%_sysconfdir/skel/.gtkrc-2.0
%_datadir/glib-2.0/schemas/*.gschema.override
%_datadir/install3/*

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
#_iconsdir/hicolor/*/apps/alt-%theme-desktop.png

%changelog
* Fri Jul 17 2020 Mikhail Efremov <sem@altlinux.org> 9.1-alt1
- Bump version.

* Thu Jul 02 2020 Mikhail Efremov <sem@altlinux.org> 9.0.990-alt1
- Bump version.

* Wed Jun 10 2020 Mikhail Efremov <sem@altlinux.org> 9.0.920-alt1
- Use getalt.org as download link.

* Thu Jun 04 2020 Mikhail Efremov <sem@altlinux.org> 9.0.910-alt1
- Bump version.

* Wed Apr 29 2020 Mikhail Efremov <sem@altlinux.org> 9.0.900-alt1
- mate-settings: Drop gksu.

* Fri Oct 18 2019 Mikhail Efremov <sem@altlinux.org> 9.0-alt1
- Drop redundant empty %%description section.
- bootloader: Fix %%preun script.
- mate-settings: Add keyboard layout and full date to LightDM.
- mate-settings: Don't touch lightdm-gtk-greeter.conf at all.
- mate-settings: Get rid of gnome-settings.
- cleanup: Don't use internal rpm macros.
- all: Don't touch config files during package update.
- BR: Drop libGConf-devel.
- BR: Require fribidi on x86 only.
- bootsplash,bootloader: Package grub and plymouth themes on
  all arches.
- build: Install grub and plymouth themes on all arches.
- mate-settings: Use BlueMenta theme.
- Use design-bootloader-source on x86 only.

* Wed Oct 02 2019 Mikhail Efremov <sem@altlinux.org> 8.991-alt1
- Bump version.

* Mon Sep 16 2019 Mikhail Efremov <sem@altlinux.org> 8.990-alt2
- Rename slides/ -> Slides/.

* Fri Sep 13 2019 Mikhail Efremov <sem@altlinux.org> 8.990-alt1
- Add English slides for ALT Workstation 9.
- Add Russian slides for ALT Workstation 9.

* Fri Aug 09 2019 Mikhail Efremov <sem@altlinux.org> 8.940-alt1
- Bump version.

* Fri Jul 26 2019 Andrey Cherepanov <cas@altlinux.org> 8.920-alt2
- Set for installer widescreen background.
- Use common icon with BaseALT logo for indexhtml.
- Make progressbar label brighter.

* Thu Jul 11 2019 Mikhail Efremov <sem@altlinux.org> 8.920-alt1
- Set codename Laertes.
- mate-settings: Use theme-mate-windows.

* Thu Jul 04 2019 Mikhail Efremov <sem@altlinux.org> 8.910-alt1
- mate-settings: Use TraditionalOk theme.
- mate-setting: Don't use non-existent window theme.
- notes: Replace license.all.html.in with English page.

* Tue Jun 18 2019 Mikhail Efremov <sem@altlinux.org> 8.900-alt2
- mate-settings: Require graphics subpackage.
- mate-settings: Add conflicts with *-graphics subpackages.

* Wed Jun 05 2019 Mikhail Efremov <sem@altlinux.org> 8.900-alt1
- mate-settings: Package all files in /etc/skel/.
- Don't try to install non-existent icons.
- Drop alt-education-*.png icons.
- Use BaseALT logo in the alterator web interface.
- mate-settings: Package Trolltech.conf.
- Drop menu subpackage.
- Drop system-settings subpackage.
- Drop {kde4,xfce,fvwm}-settings.
- Use _unpackaged_files_terminate_build.
- Don't change license and *-release files during update.
- Change spec for ALT Workstation.
- Update images for Workstation.

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
