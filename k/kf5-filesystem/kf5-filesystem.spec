%define lng_list af ar as ast be be@latin bg bn bn_IN br bs ca ca@valencia crh cs csb cy da de el en en_GB en_US eo es et eu fa fi fr fy ga gd gl gu ha he hi hne hr hsb hu hy ia id is it ja ka kk km kn ko ku lb lt lv mai mk ml mr ms nb nds ne nl nn oc or pa pl ps pt pt_BR ro ru se si sk sl sq sr sr@ijekavian sr@ijekavianlatin sr@latin sv ta te tg th tr tt ug uk uz uz@cyrillic vi wa xh zh_CN zh_HK zh_TW

%define major 5
%define minor 19
%define bugfix 2

Name: kf5-filesystem
Version: %major.%minor.%bugfix
Release: alt1
%K5init altplace

Summary: The basic directory layout for KF5
License: Public Domain
Group: System/Base

Requires: filesystem qt5-base-common
Obsoletes: kf5-i18n-ru kf5-i18n-uk

Source1: kde5
Source2: dbus-session-dir.conf
Source3: dbus-system-dir.conf

BuildRequires(pre): rpm-build-kf5

%description
The %name package is one of the basic KF5 packages that is installed on
a %distribution system; %name contains the basic directory layout
for the KDE 5, including the correct permissions for the directories.

%install
mkdir -p %buildroot/%_libdir

mkdir -p %buildroot/%_kf5_bin
mkdir -p %buildroot/%_kf5_sbin

mkdir -p %buildroot/%_kf5_icon/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128,scalable}/{actions,apps,devices,emblems,emotes,mimetypes,places,resources,status}
mkdir -p %buildroot/%_K5mod
mkdir -p %buildroot/%_K5exec
mkdir -p %buildroot/%_K5start
mkdir -p %buildroot/%_K5app
mkdir -p %buildroot/%_K5emo
mkdir -p %buildroot/%_K5snd
mkdir -p %buildroot/%_K5tmpl
mkdir -p %buildroot/%_K5wall
mkdir -p %buildroot/%_K5conf
mkdir -p %buildroot/%_K5cfg
mkdir -p %buildroot/%_K5cf_upd
mkdir -p %buildroot/%_K5data/{color-schemes,solid/{actions,devices},widgets/pics,plasma/{packages,shells,updates,layout-templates}}
mkdir -p %buildroot/%_K5data/dbus-1/{interfaces,services,system-services}
mkdir -p %buildroot/%_K5dbus_iface
mkdir -p %buildroot/%_K5dbus_srv
mkdir -p %buildroot/%_K5dbus_sys_srv
#
mkdir -p %buildroot/%_K5notif
mkdir -p %buildroot/%_K5srv/ServiceMenus
mkdir -p %buildroot/%_K5srvtyp
mkdir -p %buildroot/%_K5xmlgui

mkdir -p %buildroot/%_kf5_xdgapp
mkdir -p %buildroot/%_desktopdir/kf5
mkdir -p %buildroot/%_K5xdgdir
mkdir -p %buildroot/%_K5xdgmenu

mkdir -p %buildroot/%_K5inc
mkdir -p %buildroot/%_K5link
mkdir -p %buildroot/%_K5plug/kf5/{kio_dnd,parts}
mkdir -p %buildroot/%_K5cf_bin

mkdir -p %buildroot/%_K5xdgconf/{autostart,colors,menus,ui}

mkdir -p %buildroot/%_K5data/{katepart5,knotifications5,kservices5/ServiceMenus,kservicetypes5,kxmlgui5,knsrcfiles}

mkdir -p %buildroot/%_K5i18n/
for l in %lng_list
do
    mkdir -p %buildroot/%_K5i18n/$l/{LC_MESSAGES,LC_SCRIPTS}
done

mkdir -p %buildroot/%_K5doc
for l in %lng_list
do
    mkdir -p %buildroot/%_K5doc/$l
done


ln -s `relative %_kf5_bin %_K5data/bin` %buildroot/%_K5data/bin
ln -s `relative %_libdir %_K5data/lib` %buildroot/%_K5data/lib

mkdir -p %buildroot/%_bindir/
install -m 0755 %SOURCE1 %buildroot/%_bindir/kde5

# install dbus dirs
mkdir -p %buildroot/{%_K5conf_dbus_sessd,%_K5conf_dbus_sysd}
install -m 0644 %SOURCE2 %buildroot/%_K5conf_dbus_sessd/kf5.conf
#install -m 0644 %SOURCE3 %buildroot/%_K5conf_dbus_sysd/kf5.conf

%files
%config %_K5conf_dbus_sessd/kf5.conf
#%config %_K5conf_dbus_sysd/kf5.conf
%_bindir/kde5
%_datadir/k*5/
%_K5plug/kf5
%_sysconfdir/kf5
%dir %_kf5_bin
%dir %_kf5_sbin
%dir %_K5cf_bin
%dir %_K5exec
%dir %_K5inc
%dir %_K5link
%dir %_desktopdir/kf5

%changelog
* Wed Jun 19 2019 Sergey V Turchin <zerg@altlinux.org> 5.19.2-alt1
- add knsrcfiles dir

* Mon Jun 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.19.1-alt1
- obsolete kf5-i18n-*

* Thu Dec 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.19.0-alt2
- Fixed processing arguments containing spaces.
- Added %%ubt tag to release.

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- use kde own dbus services dir

* Tue Sep 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- fix error message when execute kde5 script with arguments

* Mon Jul 13 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- change data dirs order in helper script

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- update dirs

* Fri Apr 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- add helper script

* Wed Apr 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- update dirs

* Sat Mar 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.2
- update dirs

* Thu Feb 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.1
- initial build
