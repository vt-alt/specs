%define rname kcm-grub2

%def_disable packagekit

%define liquidshell_sover 5
%define libliquidshell liquidshell%liquidshell_sover

Name: kde5-kcm-grub2
Version: 0.6.4
Release: alt3
%K5init altplace

Group: Graphical desktop/KDE
Summary:  Configuring the GRUB2
Url: https://cgit.kde.org/kcm-grub2.git
License: GPLv3

Source: %rname-%version.tar
Source1: po.tar
Patch1: alt-no-details-btn.patch
Patch2: alt-wallpaper.patch

BuildRequires(pre): rpm-build-kf5

# Automatically added by buildreq on Mon Oct 28 2019 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libGL-devel libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms pkg-config python-base python-modules python-modules-compiler python3 python3-base python3-dev qt5-base-devel rpm-build-python3 sh4
#BuildRequires: ImageMagick-tools appstream ccmake extra-cmake-modules kf5-kcmutils-devel kf5-ki18n-devel kf5-kio-devel libImageMagick-devel libssl-devel packagekit-qt-devel python3-module-mpl_toolkits qt5-wayland-devel
BuildRequires: extra-cmake-modules
BuildRequires: libImageMagick-devel
BuildRequires: kf5-kcmutils-devel kf5-ki18n-devel kf5-kio-devel
#packagekit-qt-devel libssl-devel

%description
A KDE Control Module for configuring the GRUB2 bootloader.


%prep
%setup -n %rname-%version -a1
%patch1 -p1
%patch2 -p1

%build
%K5build \
    -DGRUB_INSTALL_EXE=/usr/sbin/grub-install \
    -DGRUB_MKCONFIG_EXE=/usr/sbin/grub-mkconfig \
    -DGRUB_PROBE_EXE=/usr/sbin/grub-probe \
    -DGRUB_SET_DEFAULT_EXE=/usr/sbin/grub-set-default \
    -DGRUB_MENU=/boot/grub/grub.cfg \
    -DGRUB_CONFIG=/etc/sysconfig/grub2 \
    -DGRUB_ENV=/boot/grub/grubenv \
    -DGRUB_MEMTEST=/etc/grub.d/39_memtest \
    #

%install
%K5install

#K5install_move data doc

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README
%_K5plug/kcm_grub2.so
%_K5libexecdir/kauth/kcmgrub2helper
%_K5srv/kcm_grub2.desktop
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmgrub2.policy
%_K5dbus_sys_srv/org.kde.kcontrol.kcmgrub2.service
%_K5dbus/system.d/org.kde.kcontrol.kcmgrub2.conf


%changelog
* Thu Nov 21 2019 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt3
- add GRUB_WALLPAPER support

* Thu Nov 14 2019 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt2
- remove Details button from info dialogs

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt1
- initial build
