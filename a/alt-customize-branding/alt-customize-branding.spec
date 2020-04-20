%define rname alt-customize-branding

Name: %rname
Version: 1.0.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Customize branding tool
License: GPL-3.0-or-later
Source: %rname-%version.tar 

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

%description
The ALT tool for KDE to customize branding

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

%find_lang --with-qt --all-name %rname

%files -f %rname.lang
%doc COPYING
%_K5bin/*
%_K5libexecdir/kauth/altcusbranding_helper
%_K5xdgapp/%rname.desktop
%_datadir/polkit-1/actions/org.kde.altcusbranding.policy
%_K5dbus_sys_srv/org.kde.altcusbranding.service
%_K5dbus/system.d/org.kde.altcusbranding.conf
#%%_qt5_translationdir/*
#%%doc README

%changelog
* Fri Apr 17 2020 Pavel Moseev <mars@altlinux.org>  1.0.1-alt1
- initial build
