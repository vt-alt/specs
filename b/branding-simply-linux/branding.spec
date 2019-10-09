%define theme slinux
%define Name Simply Linux
%define codename Destiny
%define status %nil

%define brand simply

%define _unpackaged_files_terminate_build 1

Name: branding-simply-linux
Version: 8.900
Release: alt2

%ifarch %ix86 x86_64
BuildRequires: cpio fonts-ttf-dejavu fonts-ttf-google-droid-serif fonts-ttf-google-droid-sans fonts-ttf-google-droid-sans-mono
BuildRequires: design-bootloader-source >= 5.0-alt2 fribidi
BuildRequires: gfxboot >= 4
%endif

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc

Source: %name-%version.tar

Group: Graphics
Summary: System/Base
License: GPLv2+

%description
Distro-specific packages with design and texts for Simply Linux distribution.

%description -l ru_RU.UTF-8
Пакеты, для дистрибутива "Просто Линукс" (Simply Linux)

%package bootloader
Group: System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
Summary(ru_RU.UTF-8): Тема для экрана выбора вариантов загрузки (lilo и syslinux) 
License: GPLv2+

Requires: coreutils
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
%branding_add_conflicts simply-linux bootloader

%define grub_normal white/dark-gray
%define grub_high black/white

%description bootloader
Here you find the graphical boot logo for Simply Linux distribution.
Suitable for both lilo and syslinux.

%description bootloader -l ru_RU.UTF-8
В данном пакете находится тема для экрана выбора вариантов загрузки (lilo и syslinux) 
для дистрибутива "Просто Линукс" (Simply Linux).

%package bootsplash
Summary: Theme for splash animations during bootup
Summary(ru_RU.UTF-8): Тема для экрана загрузки для дистрибутива "Просто Линукс"
License: Distributable
Group:  System/Configuration/Boot and Init
%ifarch %ix86 x86_64
Provides: plymouth-theme-%theme
Requires: plymouth-plugin-script
Requires: plymouth
%endif

%branding_add_conflicts simply-linux bootsplash

%description bootsplash
This package contains graphics for boot process for Simply Linux
(needs console splash screen enabled).

%description bootsplash -l ru_RU.UTF-8
В данном пакете находится тема для экрана загрузки для дистрибутива
"Просто Линукс" (Simply Linux).

%package alterator
Summary: Design for alterator for Simply Linux 
Summary(ru_RU.UTF-8): Тема для "Центра управления системой" и QT для дистрибутива "Просто Линукс"
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes:  branding-alt-%theme-browser-qt  branding-altlinux-%theme-browser-qt 

# lexicographically first of the village
Conflicts: branding-sisyphus-server-light-alterator

%branding_add_conflicts simply-linux alterator
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server branding-altlinux-backup-server-alterator
Requires(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for Simply Linux.

%description alterator -l ru_RU.UTF-8
В данном пакете находится тема для "Центра управления системой" (Alterator)
и модулей библиотеки QT для дистрибутива "Просто Линукс" (Simply Linux).

%package graphics
Summary: Design for Simply Linux
Summary(ru_RU.UTF-8): Тема для дистрибутива "Просто Линукс"
License: Different licenses
Group: Graphics
BuildArch: noarch

Provides: design-graphics-%theme  branding-alt-%theme-graphics
Obsoletes:  branding-alt-%theme-graphics design-graphics-%theme
Provides: design-graphics = 12.0.0

Requires(post,preun): alternatives >= 0.2
%branding_add_conflicts simply-linux graphics

%description graphics
This package contains some graphics for Simply Linux design.

%description graphics -l ru_RU.UTF-8
В данном пакете находится необходимые графические элементы для дистрибутива 
"Просто Линукс" (Simply Linux).


%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-5.0 altlinux-release-5.1 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business

%package release
Summary: Simply Linux release file
Summary(ru_RU.UTF-8): Описание дистрибутива "Просто Линукс"
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list  branding-alt-%theme-release
Conflicts: %conflicts_list
%branding_add_conflicts simply-linux release

%description release
Simply Linux %version release file.

%description release -l ru_RU.UTF-8
В данном пакете находится описание версии %version дистрибутива
"Просто Линукс" (Simply Linux).

%package notes
Provides: alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme 
Summary: Distribution license and release notes
Summary(ru_RU.UTF-8): Лицензия и дополнительные сведения для дистрибутива "Просто Линукс"
License: Distributable
Group: Documentation
BuildArch: noarch
Conflicts: alt-notes-children alt-notes-hpc alt-notes-junior alt-notes-junior-sj alt-notes-junior-sm alt-notes-school-server alt-notes-server-lite alt-notes-skif alt-notes-terminal alt-notes-desktop
%branding_add_conflicts simply-linux notes

%description notes
Distribution license and release notes

%description notes -l ru_RU.UTF-8
В данном пакете находится лицензия и дополнительные сведения для версии %version
дистрибутива "Просто Линукс" (Simply Linux).

%package xfce-settings

Summary: default settings for Xfce for Simply linux distribution
License: GPLv2+
Group: Graphical desktop/XFce
BuildArch: noarch
Requires: PolicyKit-gnome
Requires: etcskel
Requires: gtk-theme-classiclooks
Requires: gnome-themes-standard
Requires: gnome-icon-theme icon-theme-simple-sl >= 2.7-alt3
Requires: branding-simply-linux-graphics
Requires: branding-simply-linux-backgrounds8
# plugins added on panel by default
Requires: xfce4-places-plugin
Requires: xfce4-pulseaudio-plugin
Requires: xfce4-whiskermenu-plugin
Requires: xfce4-xkb-plugin

Obsoletes: xfce-settings-lite xfce-settings-school-lite
%branding_add_conflicts simply-linux xfce-settings
Conflicts: xfce-settings-simply-linux

# NOTE: Drop this requires when SL-9 will be released:
# at that point these packages will be installed already.
Requires: branding-simply-linux-backgrounds-legacy branding-simply-linux-backgrounds-vladstudio

%description xfce-settings
This package contains default settings for Xfce for Simply linux distribution.

%package backgrounds8
Group: Graphics
Summary: Backgrounds for SL-8
License: CC-BY-NC-SA-3.0+
BuildArch: noarch
%branding_add_conflicts simply-linux backgrounds8

%description backgrounds8
This package contains backgrounds for Simply Linux 8.

%package slideshow
Summary: Slideshow for Simply Linux %version installer.
Summary(ru_RU.UTF-8): Изображения для организации "слайдшоу" в установщике дистрибутива "Просто Линукс"
License: CC-BY-NC-SA-3.0+
Group: System/Configuration/Other 
BuildArch: noarch
%branding_add_conflicts simply-linux slideshow

%description slideshow
Slideshow for Simply Linux %version installer.

%description slideshow -l ru_RU.UTF-8
В данном пакете находятся изображения для организации "слайдшоу" в установщике 
дистрибутива "Просто Линукс" (Simply Linux).

%package indexhtml
Summary: Simply Linux html welcome page
Summary(ru_RU.UTF-8): Стартовая страница для дистрибутива "Просто Линукс"
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
Conflicts: branding-altlinux-backup-server-indexhtml

Requires: xdg-utils 
Requires: docs-simply-linux
Requires(post): indexhtml-common

%description indexhtml
Simply Linux index.html welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
"Просто Линукс" (Simply Linux).

%package menu
Summary: menu for Simply Linux
License: Distributable
Group: Graphical desktop/Other
BuildArch: noarch
Requires(pre): altlinux-freedesktop-menu-common
Requires: altlinux-freedesktop-menu-common

%description menu
Menu for Simply Linux

%package system-settings
Summary: Some system settings for Simply Linux
License: GPLv2+
Group: System/Base
BuildArch: noarch

%description system-settings
Some system settings for Simply Linux.

%prep
%setup -q


%build
autoconf
THEME=%theme NAME='%Name' STATUS=%status VERSION=%version CODENAME=%codename ./configure
make

%install
%makeinstall
make x86 DESTDIR=%buildroot datadir=%buildroot%_datadir sysconfdir=%buildroot%_sysconfdir

%define data_cur_dir %_datadir/branding-data-current
mkdir -p %buildroot%data_cur_dir

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


install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/artworks	%_datadir/design/%theme 10	
%_datadir/design-current	%_datadir/design/%theme	10
%_datadir/design/current	%_datadir/design/%theme	10
__EOF__

#release
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
install -pD -m644 components/systemd/os-release %buildroot%data_cur_dir/release/os-release
echo "%Name %version %status (%codename)" >%buildroot%data_cur_dir/release/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%data_cur_dir/release/$n-release
done
for r in %buildroot%data_cur_dir/release/*-release; do
  touch %buildroot%_sysconfdir/"${r##*/}"
done

#notes
pushd notes
%makeinstall
popd
ln -s license.ru.html %buildroot%data_cur_dir/alt-notes/license.uk.html
for r in %buildroot%data_cur_dir/alt-notes/license.*.html; do
  touch %buildroot%_datadir/alt-notes/"${r##*/}"
done

mkdir -p %buildroot/etc/skel/XDG-Templates.skel/

cp -r xfce-settings/etcskel/* %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.config %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.local %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.vimrc %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.gtkrc-2.0 %buildroot/etc/skel/

install -m 644 xfce-settings/etcskel/.wm-select %buildroot/etc/skel/

# backgrounds
mkdir -p %buildroot%_datadir/backgrounds/xfce/
install -m 644 xfce-settings/backgrounds/slinux*.jpg %buildroot%_datadir/backgrounds/xfce/

install -pDm0755 xfce-settings/scripts/zdg-move-templates.sh %buildroot%_sysconfdir/X11/profile.d/zdg-move-templates.sh

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
mkdir -p %buildroot/etc/alterator
cp -a slideshow/slides*/  %buildroot/usr/share/install2/slideshow/
# Set English slideshow as default
#ln -s slides-en %buildroot/usr/share/install2/slideshow/slides
install slideshow/slideshow.conf %buildroot/etc/alterator/

#indexhtml
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

%ifarch %ix86 x86_64
#bootloader
%pre bootloader
[ -s /usr/share/gfxboot/%theme ] && rm -fr  /usr/share/gfxboot/%theme ||:
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:
%endif

%post bootloader
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
[ $1 = 0 ] || exit 0
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
%ifarch %ix86 x86_64
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf
%endif
[ -f /etc/sysconfig/grub2 ] && \
      subst "s|GRUB_WALLPAPER=.*|GRUB_WALLPAPER=/usr/share/plymouth/themes/%theme/grub.jpg|" \
             /etc/sysconfig/grub2 ||:

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
%_niconsdir/slinux.png
%_iconsdir/altlinux.png

%files bootsplash
%ifarch %ix86 x86_64
%_datadir/plymouth/themes/%theme/*
%exclude %_datadir/plymouth/themes/%theme/*.in
%endif

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

%files xfce-settings
%_sysconfdir/X11/profile.d/zdg-move-templates.sh
/etc/skel/XDG-Templates.skel/
/etc/skel/.wm-select
/etc/skel/.config
/etc/skel/.local
/etc/skel/.vimrc
/etc/skel/.gtkrc-2.0

%files backgrounds8
/usr/share/backgrounds/xfce/*

%files slideshow
/etc/alterator/slideshow.conf
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %indexhtmldir/index.html
%indexhtmldir/index-*.html
%indexhtmldir/index.css
%indexhtmldir/images
%_desktopdir/indexhtml.desktop

%files menu
/usr/share/slinux-style
/etc/xdg/menus/xfce-applications-merged/50-xfce-applications.menu
/usr/share/desktop-directories/altlinux-wine.directory

%files system-settings
%config %_sysconfdir/polkit-1/rules.d/*.rules

%changelog
* Wed Oct 09 2019 Mikhail Efremov <sem@altlinux.org> 8.900-alt2
- Fix BR: Add fribidi on x86.
- Fix build on aarch64.

* Tue Oct 08 2019 Mikhail Efremov <sem@altlinux.org> 8.900-alt1
- Don't use deprecated PreReq.
- Drop gnome-chess.desktop.
- Change GTK theme to gtk-theme-classiclooks.
- Set codename for SL-9.
- xfce-settings: Drop Russian words.
- slideshow: Russian slides for SL9.
- xfce-settings: Replace gnome-system-monitor with xfce4-taskmanager.
- Use Qt5 to generate theme.
- Drop splash theme.
- Drop libGConf-devel from BR.
- xfce-settings: Update xfwm4 settings.
- xfce-settings: Drop xfce4-volumed-pulse settings.
- xfce-settings: Update xfce4-panel settings.
- xfce-settings: Update xfce4-desktop settings.
- xfce-settings: Drop xfce4-mixer settings.
- xfce-settings: Requre plugins added on panel by default.

* Thu Jul 06 2017 Mikhail Efremov <sem@altlinux.org> 8.2.0-alt1
- Bump version to 8.2.
- xfce-settings: Fix menu on window key.

* Fri Jun 30 2017 Mikhail Efremov <sem@altlinux.org> 7.99.0-alt1
- menu: Add xfce4-clipman.desktop.
- indexhtml.desktop: Split part of Name to Comment.
- xfce-settings: Enlarge whiskermenu height.
- release-notes.ru: Fix style (thanks mike@).

* Thu Jun 22 2017 Mikhail Efremov <sem@altlinux.org> 7.98.1-alt3
- menu: Don't show java-*-policytool menu entry.

* Wed Jun 21 2017 Mikhail Efremov <sem@altlinux.org> 7.98.1-alt2
- menu: Add wesnoth.desktop.
- xfce-settings: Force DPI 96.

* Mon Jun 19 2017 Mikhail Efremov <sem@altlinux.org> 7.98.1-alt1
- slideshow: Change License to CC-BY-NC-SA-3.0+.
- xfce-settings: Require backgrounds8 subpackage.
- Drop legacy backgrounds.
- menu: Add ppracer.desktop.
- menu: Add freeciv-*.desktop files.
- menu: Add Russian Comment.
- menu: Add Russian comment for Ri-li.
- menu: Add openttd.desktop.
- menu: Fix fusion-icon.desktop.
- menu: Add blender-win.desktop.
- menu: Drop synfigstudio.desktop.
- New slideshow.
- xfce-settings: Use 1920x1080 backgrounds as default.
- xfce4-settings: Change style for background.
- steps: Add luks step icon.
- xfce-settings: Set slinux_june_2017 background as default.
- xfce-settings: Add slinux_june_2017* backgrounds.

* Thu May 18 2017 Mikhail Efremov <sem@altlinux.org> 7.98.0-alt1
- menu: Add gnome-chess.desktop.
- menu: Add Russian comment to dropbox.desktop.
- menu: Add shotwell*.desktop.
- xfce-settings: Add balou splash theme.
- Change home page link.
- menu: Add sound-juicer.desktop.
- gfxboot: Make menu bar transparent.
- plymouth: Use 16x9 and 4x3 backgrounds.
- New images for bootloader, splash and lightdm.

* Mon Apr 24 2017 Mikhail Efremov <sem@altlinux.org> 7.97.0-alt1
- xfce-settings: Use chromium instead of firefox.
- menu: Don't expose cheese if not installed.

* Fri Mar 31 2017 Mikhail Efremov <sem@altlinux.org> 7.96.0-alt1
- indexhtml: Add Telegram button.
- indexhtml.desktop: Use slinux icon.
- indexhtml: Drop twitter button.
- indexhtml: Fix and update links.
- xfce-settings: Use Oxygen icon theme in LibreOffice.
- menu: Drop alt-alt_linux.desktop.
- indexhtml: Update logo and links.
- Drop graphics/kde.
- Prepare SL 8: Set codename.
- vimrc: Disable bell.
- Change license text.
- xfce-settings: Drop icons.screen0.rc.
- xfce-settings: Use dm-tool to switch users.
- menu: Update/drop *.desktop files.
- xfce-settings: Move terminalrc to new place.
- xfce-settings: Update for xfce-4.12.
- xfce-settings: Drop gconf settings from etcskel.

* Fri Mar 10 2017 Mikhail Efremov <sem@altlinux.org> 7.95.0-alt6
- Spec cleanup.
- Don't change license and *-release files during update.
- Use rpm-macros-branding.
- Use Clearlooks-Phenix theme again.

* Tue Feb 07 2017 Artem Zolochevskiy <azol@altlinux.org> 7.95.0-alt5
- indexhtml: Drop reference to alt-docs/modules

* Fri Apr 29 2016 Mikhail Efremov <sem@altlinux.org> 7.95.0-alt4
- Replace GTK theme Clearlooks-Phenix with Adwaita.

* Fri Dec 25 2015 Mikhail Kolchin <mvk@altlinux.org> 7.95.0-alt3
- xfce-settings: Add .gtkrc-2.0 for canberra support (closes: #30264).

* Tue Apr 14 2015 Mikhail Efremov <sem@altlinux.org> 7.95.0-alt2
- menu: Hide gmplayer in the SL menu.
- xfce-settings: Cleanup gconf settings.

* Tue Apr 14 2015 Mikhail Efremov <sem@altlinux.org> 7.95.0-alt1
- system-settings: Drop lightdm hack (closes: #30901).
- index.html: Use https for facebook and twitter.
- index.html: Update "VKontakte" URL.
- index.html: Update company address and copyright year.
- xfce-settings: Replace clock plugin with xfce4-orageclock-plugin.
- Fix font for background text.
- Update BR for Droid fonts.
- menu: Drop celestia.desktop.
- menu: Fix dropbox.desktop.

* Wed Mar 05 2014 Mikhail Efremov <sem@altlinux.org> 7.0.4-alt1
- Bump version to 7.0.4.

* Fri Feb 21 2014 Mikhail Efremov <sem@altlinux.org> 7.0.3-alt2
- menu: Add cheese.desktop.
- index.html: Drop reference to planet.altlinux.org.

* Wed Feb 12 2014 Mikhail Efremov <sem@altlinux.org> 7.0.3-alt1
- Update license texts.
- theme.plymouth: Fix descriptions.
- xfce-settings: Drop gnome-mplayer from gconf.

* Tue Dec 24 2013 Mikhail Efremov <sem@altlinux.org> 7.0.2-alt3
- xfce settings: Increase the default double-click time.
- xfce settings: Disable mousewheel-rollup feature in the xfwm4.

* Mon Dec 16 2013 Mikhail Efremov <sem@altlinux.org> 7.0.2-alt2
- xfce-settings: Fix summary and description.
- Package old SL New Year wallpapers.

* Fri Nov 29 2013 Mikhail Efremov <sem@altlinux.org> 7.0.2-alt1
- Bump version to 7.0.2.
- indexhtml.desktop: Drop unneeded space.

* Fri Jul 19 2013 Mikhail Efremov <sem@altlinux.org> 7.0.1-alt1
- xfce settings: Set ristretto as default images viewer.
- Replace gnome-mplayer with smplayer.
- system-settings: Add comment about requires.
- menu: Use 'xfce-applications-merged' directory only.
- system-settings Add workaround for 'lightdm cursor' bug.
- indexhtml: Fix title in the Russian index.html.
- documentation: Drop space between VERSION and STATUS.
- Add system-settings subpackage.
- Allow 'wheel' group memebers to modify NM's systemwide connections.
- Fix license tag.

* Thu Jul 04 2013 Mikhail Efremov <sem@altlinux.org> 7.0.0-alt6
- menu: Fix GenericName of winefile.

* Tue Jun 25 2013 Mikhail Efremov <sem@altlinux.org> 7.0.0-alt5
- xfce settings: Disable GNOME compatibility mode.

* Mon Jun 24 2013 Mikhail Efremov <sem@altlinux.org> 7.0.0-alt4
- Fix user's fonts.conf location.
- Fix license.ru.html.

* Fri Jun 21 2013 Mikhail Efremov <sem@altlinux.org> 7.0.0-alt3
- xfce settings: Autophoto disabled.
- xfce settings: Drop unneded files.

* Tue Jun 11 2013 Mikhail Efremov <sem@altlinux.org> 7.0.0-alt2
- license.ru.html: Add SL version.
- xfce settings: Set gnome-mplayer as default for video/*.

* Mon Jun 10 2013 Mikhail Efremov <sem@altlinux.org> 7.0.0-alt1
- Drop 'beta' status.

* Fri Jun 07 2013 Mikhail Efremov <sem@altlinux.org> 6.996.0-alt1
- menu: Add remmina.desktop.
- Updated slideshow.
- Add Ukrainian start/release-notes pages.
- Really use russian license text for Ukrainian.
- menu: Hide xfce4-mixer.
- xfce settings: Use pavucontrol instead of xfce4-mixer.
- Add Ukrainian slideshow.
- Add English slideshow.
- Support localized slideshow.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 6.995.0-alt1
- Drop autostart/polkit-gnome-authentication-agent-1.desktop.
- Update index.html.
- menu:Add virtualbox.desktop.
- Add TryExec to the recently added desktop files.
- menu: Add Ri-li.desktop.
- gfxboot: Move menu to the left a bit.

* Tue Apr 16 2013 Mikhail Efremov <sem@altlinux.org> 6.994.0-alt1
- xfce settings: Change icon theme Simple -> SimpleSL.
- slideshow: Update Slide_Simply7_spring_2013.png.
- Replace stardict-gtk.desktop with stardict.desktop.
- menu: Add glchess.desktop.
- grub and gfxboot: Change seleted menuitems colour.
- grub: Update menu position.
- menu: Fix GenericNames.
- menu: Hide X-XFCE-SettingsDialog category.
- menu: Show Generic names by default.
- plymouth theme: Update scale factor for new logo.
- Update boot images.
- menu: Drop not needed desktop files.
- plymouth theme: Use scaling for logo.
- Update groups/firewall.png for alterator (tnx cas@).

* Wed Mar 27 2013 Mikhail Efremov <sem@altlinux.org> 6.993.0-alt1
- Set status 'beta'.
- Fix perms for acc group icons.
- Add groups/firewall.png from Centaurus.
- Update backgrounds.
- Don't package theme.plymouth.in file.
- plymouth: Replace progress bar with appearing logo.
- Fix grub text colour.
- Install *.png backgrounds too.
- gfxboot: Fix font color.
- Update wallpaper.png.
- Set new default background.
- Add new wallpapers.
- New slideshow.
- Replace gtk2-theme-simplicity with gtk3-theme-clearlooks-phenix.
- Update boot images.
- Drop parts of old Centaurus branding.
- Change theme to Clearlooks-Phenix.
- xfce settings: Suspend on lid close in case of AC too.
- Fix grub fonts and colours.
- Fix sysconfig-base installer step icon.
- xfce settings: Lock screen when going for sleep.

* Thu Feb 28 2013 Mikhail Efremov <sem@altlinux.org> 6.992.0-alt1
- Added os-release file.
- Fix design.qss.
- browser-qt design: Fix password characters.
- Set all existing brandings in variant.
- Set codename for SL-7.0.
- xfce settings: Fix mixer plugin configuration.
- livecd-start.ru.html: Fix align.

* Tue Feb 12 2013 Mikhail Efremov <sem@altlinux.org> 6.991.0-alt2
- Added gnome-authentication-agent autostart desktop-file.
- release-notes: Fix align (thx cas@).

* Fri Feb 08 2013 Mikhail Efremov <sem@altlinux.org> 6.991.0-alt1
- xfce-settings: Drop obsoleted autostart *.desktop files.
- Don't disable tracker by default.
- Set status 'alpha' and codename 'UNKNOWN'.

* Fri Jun 22 2012 Mikhail Efremov <sem@altlinux.org> 6.990.0-alt1
- menu: Updated for Xfce 4.10.
- Update backgrounds location for Xfce 4.10.
- Drop gfxboot menu.
- Updated xfce panel configuration.

* Fri May 04 2012 Michael Shigorin <mike@altlinux.org> 6.0.1-alt9
- Added sisyphus-server-light to conflicting list.
- Fixed alterator subpackage Conflicts: list generation.

* Fri Dec 23 2011 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt8
- Install /etc/skel/.vimrc.

* Fri Dec 23 2011 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt7
- Package /etc/skel/.vimrc.
- Disable tracker.

* Fri Dec 09 2011 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt6
- menu: Added gsynaptics.desktop.

* Thu Dec 08 2011 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt5
- Fix Win keys binding.

* Thu Nov 24 2011 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt4
- Bind Win key to Xfce menu (closes: #17314).
- Rename Templates dir from /etc/skel to XDG_TEMPLATES_DIR.
- Don't use Russian name for 'Templates'.

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

* Wed Jun 30 2011 Alexandra Panyukova <mex3@altlinux.ru> 6.0.0-alt15
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

