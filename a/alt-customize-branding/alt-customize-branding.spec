%define rname alt-customize-branding

Name: %rname
Version: 1.0.9
Release: alt1
%K5init altplace

#Group: Graphics
Group: Graphical desktop/KDE
Summary: Customize branding tool
License: GPL-3.0-or-later
Url: https://www.basealt.ru/
Source: %rname-%version.tar

ExcludeArch: armh

BuildRequires(pre): rpm-build-kf5

BuildRequires: extra-cmake-modules 
BuildRequires: qt5-base-devel
BuildRequires: libImageMagick-devel
BuildRequires: kf5-kcmutils-devel 
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kio-devel
BuildRequires: qt5-tools
BuildRequires: kf5-kwindowsystem-devel
Requires: qt5-translations convert
Requires: %rname-backend

%description
The ALT tool for KDE to customize branding

%package backend
Summary: Customize branding tool backend
License: GPL-3.0-or-later
Group: System/Configuration/Boot and Init
%description backend
The ALT tool backend for KDE to customize branding

%prep
%setup -n %rname-%version

%build
%K5build
lrelease-qt5 translations/alt-customize-branding_ru_RU.ts

%install
%K5install

# translations
mkdir -p %buildroot/%_qt5_translationdir/
install -m 0644 translations/*.qm %buildroot/%_qt5_translationdir/

# branding_helper script
install -m 0755 altcusbranding_helper_script %buildroot/%_K5libexecdir/kauth/

# alt-customize-branding-settings.ini
mkdir -p %buildroot%_localstatedir/%rname
#install -m 0644 %%rname-settings.ini %%buildroot%%_localstatedir/%%rname/

# alternatives
mkdir -p %buildroot%_altdir
install -m 0644 %rname %buildroot%_altdir/

# branding directories
mkdir -p %buildroot/boot/grub/themes/%rname
mkdir -p %buildroot%_datadir/design/%rname
mkdir -p %buildroot%_datadir/plymouth/themes/%rname

%find_lang --with-qt --all-name %rname

%postun backend
if [ $1 -eq 0 ] ; then
    %define configFile alt-customize-branding-settings.ini
    %define configDir /var/lib
    if [ -f %configDir/%rname/%configFile ] ; then
        previousThemeName=$(awk -F "=" '/ThemeName/ {print $2}' %configDir/%rname/%configFile)
        echo Previous theme name: $previousThemeName
# Change /etc/sysconfig/grub2 and run
        . shell-config
        shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/$previousThemeName/theme.txt
        shell_config_set /etc/sysconfig/grub2 GRUB_BACKGROUND /boot/grub/themes/$previousThemeName/grub.png
        shell_config_set /etc/sysconfig/grub2 GRUB_WALLPAPER /boot/grub/themes/$previousThemeName/grub.png
# generate file "/boot/grub/grub.cfg"
        /usr/sbin/grub-mkconfig -o /boot/grub/grub.cfg
# Change theme name in file 'plymouthd.conf':
        sed -i "s/Theme=.*/Theme=$previousThemeName/" /etc/plymouth/plymouthd.conf
    fi
# Remove directories
#rm -R %%_localstatedir/%%rname
    if [ -d "/usr/share/design/%rname" ]; then
        rm -R /usr/share/design/%rname
    fi
    if [ -d "/boot/grub/themes/%rname" ]; then
        rm -R /boot/grub/themes/%rname
    fi
    if [ -d "/usr/share/plymouth/themes/%rname" ]; then
        rm -R /usr/share/plymouth/themes/%rname
    fi
    if [ -d "/tmp/%rname" ]; then
        rm -R /tmp/%rname
    fi
# Toggle/repair alternatives
    alternatives-update
    make-initrd
fi

%files -f %rname.lang
%_K5bin/*
%_K5xdgapp/%rname.desktop
%_K5libexecdir/kauth/altcusbranding_helper
%_K5dbus/system.d/org.kde.altcusbranding.conf
%_K5dbus_sys_srv/org.kde.altcusbranding.service
%_datadir/polkit-1/actions/org.kde.altcusbranding.policy
%doc COPYING

%files backend
%_K5libexecdir/kauth/altcusbranding_helper_script
%_altdir/%rname
%_localstatedir/%rname
%_datadir/design/%rname
%_datadir/plymouth/themes/%rname
/boot/grub/themes/%rname

#%%_qt5_translationdir/alt-customize-branding_ru_RU.qm
#%%doc README

%changelog
* Fri Jun 26 2020 Pavel Moseev <mars@altlinux.org>  1.0.9-alt1
- fix logo duplication (closes: #38585)

* Thu Jun 04 2020 Pavel Moseev <mars@altlinux.org>  1.0.8-alt1
- fix form cleaning

* Mon Jun 01 2020 Pavel Moseev <mars@altlinux.org>  1.0.7-alt1
- fix return settings after package removal

* Mon Jun 01 2020 Pavel Moseev <mars@altlinux.org>  1.0.6-alt1
- clean code

* Fri May 29 2020 Pavel Moseev <mars@altlinux.org>  1.0.5-alt1
- fix script

* Tue May 26 2020 Pavel Moseev <mars@altlinux.org>  1.0.4-alt1
- split package to frontend and backend

* Mon May 25 2020 Pavel Moseev <mars@altlinux.org>  1.0.3-alt1
- add config-file and uninstall mechanism

* Wed May 13 2020 Pavel Moseev <mars@altlinux.org>  1.0.2-alt1
- rewrite the program using bash script

* Fri Apr 17 2020 Pavel Moseev <mars@altlinux.org>  1.0.1-alt1
- initial build
