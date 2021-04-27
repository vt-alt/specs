Name: onboard
Version: 1.4.1
Release: alt3

Summary: Simple on-screen Keyboard
License: GPL-3.0+
Group: Graphical desktop/GNOME 
URL: https://launchpad.net/onboard/

Source0: http://launchpad.net/%name/0.96/%version/+download/%name-%version.tar.gz
Source1: ru.po 

BuildRequires(pre): etersoft-build-utils rpm-build-gnome python3-devel
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: libXi-devel
BuildRequires: libXtst-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libcanberra-devel
BuildRequires: libdconf-devel
BuildRequires: libgtk+3-devel 
BuildRequires: libhunspell-devel
BuildRequires: libxkbfile-devel
BuildRequires: python3-module-distutils-extra >= 2.12
BuildRequires: libappindicator-gtk3-gir-devel
BuildRequires: libudev-devel

Requires: python3-module-dbus
# see ALT bug #35174
Requires: iso-codes

%filter_from_requires /^python3(pypredict.lm)/d

%description
An on-screen keyboard useful on tablet PCs or for mobility impaired
users.

%package gnome
Group:    Graphical desktop/GNOME
Summary:  GNOME Shell support for onboard
Requires: onboard = %version-%release
Requires: gnome-shell

%description gnome
GNOME Shell support for onboard.

%prep
%setup -q
install -Dpm0644 %SOURCE1 po/ru.po

%build
%python3_build

%install
%python3_install

desktop-file-install --dir %buildroot%_desktopdir       \
    --remove-category="Accessibility"        \
    build/share/applications/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir       \
    --remove-category="Accessibility"        \
    build/share/applications/%name-settings.desktop

mkdir -p %buildroot%_datadir/locale
cp -a build/mo/* %buildroot%_datadir/locale

# remove themed icons
rm -rf %buildroot%_iconsdir/ubuntu-mono-*

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING* NEWS README HACKING
%_bindir/%name
%_bindir/%name-settings
%_datadir/%name/
%_datadir/glib-2.0/schemas/*.gschema.xml
#_xdgconfigdir/autostart/%name-autostart.desktop
%_desktopdir/%name.desktop
%_desktopdir/%name-settings.desktop
%_man1dir/%{name}*.1*
%_iconsdir/HighContrast/scalable/apps/onboard.svg
%_iconsdir/hicolor/scalable/apps/onboard.svg
%_iconsdir/hicolor/*x*/apps/onboard.png
%_datadir/sounds/freedesktop/stereo/onboard-key-feedback.oga
%_datadir/dbus-1/services/*
%python3_sitelibdir/Onboard/
%python3_sitelibdir/%{name}*.egg-info

%files gnome
%_datadir/gnome-shell/extensions/Onboard_Indicator@onboard.org

%changelog
* Mon Apr 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt3
- Complete Russian translation (thanks Olesya Gerasimenko).
- Remove Accessability category from desktop files.
- Fix License tag according to SPDX.

* Fri Aug 03 2018 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt2
- Added requires to iso-codes (ALT#35174)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 23 2017 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- New version

* Sun Sep 18 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version

* Thu Jul 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version (use Python3)

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.96.2-alt2.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Jan 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.96.2-alt2
- hack around startup crash

* Wed Jan 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.96.2-alt1
- updated to 0.96.2
- now it is arch-dependent

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.95.1-alt1.1
- Rebuild with Python-2.7

* Sat Oct 01 2011 Andrey Cherepanov <cas@altlinux.org> 0.95.1-alt1
- Initial build in Sisyphus (closes: #26220)
