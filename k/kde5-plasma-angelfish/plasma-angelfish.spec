%define rname plasma-angelfish

%define sover 3
%define libfalkonprivate libfalkonprivate%sover

Name: kde5-plasma-angelfish
Version: 1.4.0
Release: alt3
%K5init altplace

Summary: A very fast open source browser based on WebKit core
License: GPLv3+
Group: Networking/WWW
Url: https://anongit.kde.org/plasma-angelfish.git

Requires(post,preun): alternatives >= 0.2
Provides: webclient

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Feb 25 2020 (-bi)
# optimized out: alternatives cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libgdk-pixbuf libglvnd-devel libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-core libqt5-gui libqt5-network libqt5-positioning libqt5-qml libqt5-quick libqt5-quickcontrols2 libqt5-svg libqt5-test libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-widgets libsasl2-3 libstdc++-devel libx265-176 python-modules python2-base python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 sh4
#BuildRequires: appstream extra-cmake-modules git-core kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-purpose-devel libssl-devel python3-dev qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires: extra-cmake-modules kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-purpose-devel
BuildRequires: desktop-file-utils

%description
Falkon is a new and very fast World Wide Web Browser
which uses Qt Framework and its QtWebKit rendering core.
It is a lightweight browser with some advanced functions
like integrated AdBlock, Search Engines Manager, Theming
support, Speed Dial and SSL Certificate manager.


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

#install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/xbrowser       %_K5bin/angelfish      5
%_bindir/x-www-browser       %_K5bin/angelfish      5
__EOF__

# add mime types categories
desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
    --add-mime-type=x-scheme-handler/http \
    --add-mime-type=x-scheme-handler/https \
    %buildroot/%_K5xdgapp/org.kde.mobile.angelfish.desktop

%find_lang --all-name --with-qt %name

%files -f %name.lang
%config /%_sysconfdir/alternatives/packages.d/%name
%_K5bin/angelfish
%_K5xdgapp/*angelfish*.desktop
%_K5icon/*/*/apps/*angelfish*.*

%changelog
* Tue Feb 25 2020 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt3
- fix provides and requires

* Tue Feb 25 2020 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt2
- add x-scheme-handler/http to desktop-file

* Tue Feb 25 2020 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt1
- initial build
