%def_without p7_backport
%def_without xtdesktop
%def_without desklaunch
%def_without kde3kdesktop
%def_without ivman
Name: icewm-startup
Version: 0.20
Release: alt3

Summary: simple pluggable IceWM autostart manager

Summary(ru_RU.UTF-8): менеджер автозапуска программ IceWM
License: GPL
Group: Graphical desktop/Icewm
Url: http://git.altlinux.org

Packager: Dmitriy Khanzhin <jinn@altlinux.org>
#Source: %name-%version.tar.bz2
Source1: XXkb.conf

BuildArch: noarch
AutoReq: no

%define icewmconfdir %_sysconfdir/X11/icewm
#due to new icewmconfdir in /etc/X11
Requires: icewm >= 1.2.25

%description
Simple pluggable icewm autostart manager is a generic IceWM startup script
which allows one to configure IceWM default autostart via installing corresponding rpm plug-ins.

%description -l ru_RU.UTF-8
менеджер автозапуска программ IceWM
позволяет путем установки rpm расширений просто настраивать 
рабочий стол IceWM по умолчанию сразу для всех пользователей, 
сохраняя за пользователями полную свободу персональной настройки
автозапуска.

Имеющиеся модули позволяют при старте icewm обновлять локальное меню пользователя
(если у него оно есть), запускать ivman, gkrellm, xxkb, mount-tray, WiFi manager,
запускать рабочий стол (idesk, kdesktop) и т. д.

%package apt-indicator
Group: Graphical desktop/Icewm
Summary: apt-indicator autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск apt-indicator при старте IceWM
Requires: %name apt-indicator
AutoReq: no

%description apt-indicator
apt-indicator plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 apt-indicator
запуск apt-indicator при старте IceWM
(Требует менеджер автозапуска программ IceWM).

%package delay
Group: Graphical desktop/Icewm
Summary: delay before starting programs
Summary(ru_RU.UTF-8): задержка запуска программ
Requires: %name
AutoReq: no

%description delay
delay before starting programs, to eliminate possible artifacts,
typically used to have time to start icewmtray.
%description -l ru_RU.UTF-8 delay
задержка перед запуском программ, чтобы устранить возможные артефакты,
обычно используется, чтобы успел стартовать icewmtray.

%package gkrellm
Group: Graphical desktop/Icewm
Summary: gkrellm autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск gkrellm при старте IceWM
# xtoolwait is required because icewm is not launched yet
Requires: %name gkrellm xtoolwait
AutoReq: no

%description gkrellm
gkrellm plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 gkrellm
запуск gkrellm при старте IceWM
(Требует менеджер автозапуска программ IceWM).

%package idesk
Group: Graphical desktop/Icewm
Summary: idesk autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск idesk при старте IceWM
Requires: %name idesk
Conflicts: %name-kdesktop
AutoReq: no

%description idesk
idesk plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 idesk
idesk plug-in для менеджера автозапуска программ при старте IceWM.

%if_with kde3kdesktop
%package kdesktop
Group: Graphical desktop/Icewm
Summary: kdesktop autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск kdesktop при старте IceWM
Requires: %name kdebase-wm
Conflicts: %name-idesk
AutoReq: no

%description kdesktop
kdesktop plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 kdesktop
kdesktop plug-in для менеджера автозапуска программ при старте IceWM.
%endif

%package mount-tray
Group: Graphical desktop/Icewm
Summary: mount-tray autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск mount-tray при старте IceWM
Requires: %name mount-tray
AutoReq: no

%description mount-tray
mount-tray is a small Qt-based tray application for mount and unmount
removable devices like USB storage or CD and DVD-ROM. It used udisks
for mount and unmount operations, udev for device detection and DBus
for take information about external mounting and unmounting.

This package provides mount-tray plug-in for IceWM autostart manager.

%description -l ru_RU.UTF-8 mount-tray
mount-tray - это небольшой аплет для монтирования и размонтирования
извлекаемых устройств наподобие USB флешки, CD или DVD-ROM.

Установите этот пакет, если вы хотите запускать mount-tray при старте IceWM.

%package notification-daemon
Group: Graphical desktop/Icewm
Summary: notification-daemon autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск notification-daemon при старте IceWM
Requires: %name
Requires: /usr/bin/nm-applet
Requires: /usr/libexec/polkit-1/polkit-gnome-authentication-agent-1
AutoReq: no

%description notification-daemon
notification-daemon provides a notification server according to Desktop Notifications Specification.
This package provides notification-daemon plug-in for IceWM autostart manager.

%description -l ru_RU.UTF-8 notification-daemon
notification-daemon используется для отображения уведомлений от других программ.
Установите этот пакет, если вы хотите запускать notification-daemon при старте IceWM.

%package xxkb
Group: Graphical desktop/Icewm
Summary: xxkb autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск xxkb при старте IceWM
Requires: %name xxkb
AutoReq: no
Conflicts: %name-xxkb-tray

%description xxkb
xxkb plug-in for simple pluggable IceWM autostart manager.
~/.xxkbrc or /etc/X11/app-defaults/XXkb is required.
%description -l ru_RU.UTF-8 xxkb
xxkb plug-in для менеджера автозапуска программ при старте IceWM.
Плагин запускает xxkb только при наличии ~/.xxkbrc или 
/etc/X11/app-defaults/XXkb.

%package xxkb-tray
Group: Graphical desktop/Icewm
Summary: xxkb autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск xxkb при старте IceWM
Requires: %name xxkb
AutoReq: no
Conflicts: %name-xxkb

%description xxkb-tray
xxkb plug-in for simple pluggable IceWM autostart manager.
~/.xxkbrc or /etc/X11/app-defaults/XXkb is required.
When you install package the file /etc/X11/app-defaults/XXkb
will be overwritten, and after removing returned to the old file.
%description -l ru_RU.UTF-8 xxkb-tray
xxkb plug-in для менеджера автозапуска программ при старте IceWM.
Плагин запускает xxkb только при наличии ~/.xxkbrc или 
/etc/X11/app-defaults/XXkb.
При установке пакета файл /etc/X11/app-defaults/XXkb будет
перезаписан, а после удаления возвращен старый файл.

%if_with desklaunch
%package desklaunch
Group: Graphical desktop/Icewm
Summary: desklaunch autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск desklaunch при старте IceWM
Requires: %name desklaunch
AutoReq: no
%endif #desklaunch

%if_with desklaunch
%description desklaunch
desklaunch plug-in for simple pluggable IceWM autostart manager.
desklaunch is only launched for users that have ~/.desklaunchrc.
%description -l ru_RU.UTF-8 desklaunch
desklaunch plug-in для менеджера автозапуска программ IceWM.
Плагин запускает desklaunch только при наличии ~/.desklaunchrc.
%endif #desklaunch

%if_with xtdesktop
%package xtdesktop
Group: Graphical desktop/Icewm
Summary: xtdesktop autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск xtdesktop при старте IceWM
Requires: %name xtdesktop
AutoReq: no
%endif #xtdesktop

%if_with xtdesktop
%description xtdesktop
xtdesktop plug-in for simple pluggable IceWM autostart manager.
xtdesktop is only launched for users that have ~/.xtdeskrc.
%description -l ru_RU.UTF-8 xtdesktop
xtdesktop plug-in для менеджера автозапуска программ IceWM.
Плагин запускает xtdesktop только при наличии ~/.xtdeskrc.
%endif #xtdesktop

%if_with ivman
%package ivman
Group: Graphical desktop/Icewm
Summary: ivman autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск ivman при старте IceWM
Requires: %name ivman
AutoReq: no

%description ivman
ivman plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 ivman
ivman plug-in для менеджера автозапуска программ IceWM.
%endif

%package spacefm
Group: Graphical desktop/Icewm
Summary: spacefm autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск spacefm при старте IceWM
Requires: %name spacefm
AutoReq: no

%description spacefm
spacefm plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 spacefm
spacefm plug-in для менеджера автозапуска программ IceWM.

%package update-menus
Group: Graphical desktop/Icewm
Summary: autoupdate of user menu at IceWM startup
Summary(ru_RU.UTF-8): автообновление меню пользователя при старте IceWM (при необходимости)
Requires: %name menu
AutoReq: no

%description update-menus
update-menus plug-in for simple pluggable IceWM autostart manager.
Does autoupdate of user menu at IceWM startup. (~/.icewm/menu).

%description -l ru_RU.UTF-8 update-menus
update-menus plug-in для менеджера автозапуска программ IceWM.
автообновление меню пользователя при старте IceWM. 
Автообновление запускается только если пользователь 
не пользуется общесистемным меню, а предпочитает 
локальное меню из ~/.icewm/menu.

%package networkmanager
Group: Graphical desktop/Icewm
Summary: start gnome networkmanager applet
%if_with p7_backport
Requires: %name NetworkManager-gnome polkit-gnome
%else
Requires: %name ModemManager NetworkManager-applet-gtk
Requires: NetworkManager-wifi usb-modeswitch
%endif
AutoReq: no

%description networkmanager
networkmanager plug-in for simple network configuration.
Start gnome networkmanager applet into tray.

%package tray_mixer_plus
Group: Graphical desktop/Icewm
Summary: start simple tray sound volume control
Requires: %name tray_mixer_plus
AutoReq: no

%description tray_mixer_plus
tray_mixer_plus plug-in for simple sound volume control.

%package pnmixer
Group: Graphical desktop/Icewm
Summary: pnmixer autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск pnmixer при старте IceWM
Requires: %name pnmixer
AutoReq: no

%description pnmixer
pnmixer plug-in for simple sound volume control.

%package grun
Group: Graphical desktop/Icewm
Summary: setup Run dialog
Requires: %name grun
AutoReq: no

%description grun
grun plug-in for setup dialog of launching applications in console mode.

%package simple-sound
Group: Graphical desktop/Icewm
Summary: Startup and shutdown simple sound for IceWM
Summary(ru_RU.UTF-8): Простейшие звуки при старте и выключении IceWM
Requires: %name aplay
AutoReq: no

%description simple-sound
Startup and shutdown simple sound for IceWM.
%description -l ru_RU.UTF-8 simple-sound
Простейшие звуки при старте и выключении IceWM.

%prep
%setup -q -c -T

%build

cat > README.ru_RU.UTF-8 <<EOF



~/.icewm/startup.d

# starting all system-wide icewm autostart programs
for file in %icewmconfdir/startup.d/*; do
  userfile=~/.icewm/startup.d/`echo $file | sed -e 's,%icewmconfdir/startup.d/,,'`
  # root can disable autostart removing 'execute' bits
  if [ -x $file ]; then 
    # User-supplied programs disable system-wide programs.
    # So user can disable system-wide program 
    # by touching file in ~/.icewm/startup.d/ with the same name
    # or even replace it with his own script.

    # skip system-wide program if user-supplied file exists.
    [ -e $userfile ] || . $file
  fi
done

# starting user-supplied icewm autostart programs
for file in ~/.icewm/startup.d/*; do
  # running user files 
  # user can disable autostart removing 'execute' bits
  [ -x $file ] && . $file
done


EOF



%install

# Startup

%__mkdir_p %buildroot/%icewmconfdir/startup.d
cat <<'EOF' > %buildroot/%icewmconfdir/startup
#!/bin/sh

# starting all system-wide icewm autostart programs
for file in %icewmconfdir/startup.d/*; do
  userfile=~/.icewm/startup.d/`echo $file | sed -e 's,%icewmconfdir/startup.d/,,'`
  # root can disable autostart removing 'execute' bits
  if [ -x $file ]; then 
    # User-supplied programs disable system-wide programs.
    # So user can disable system-wide program 
    # by touching file in ~/.icewm/startup.d/ with the same name
    # or even replace it with his own script.

    # skip system-wide program if user-supplied file exists.
    [ -e $userfile ] || . $file
  fi
done

# starting user-supplied icewm autostart programs
for file in ~/.icewm/startup.d/*; do
  # running user files 
  # user can disable autostart removing 'execute' bits
  [ -x $file ] && . $file
done
EOF

# Shutdown

%__mkdir_p %buildroot/%icewmconfdir/shutdown.d
cat <<'EOF' > %buildroot/%icewmconfdir/shutdown
#!/bin/sh

# starting all system-wide icewm autostart programs in shutdown time
for file in %icewmconfdir/shutdown.d/*; do
  userfile=~/.icewm/shutdown.d/`echo $file | sed -e 's,%icewmconfdir/shutdown.d/,,'`
  # root can disable autostart removing 'execute' bits
  if [ -x $file ]; then 
    # User-supplied programs disable system-wide programs.
    # So user can disable system-wide program 
    # by touching file in ~/.icewm/shutdown.d/ with the same name
    # or even replace it with his own script.

    # skip system-wide program if user-supplied file exists.
    [ -e $userfile ] || . $file
  fi
done

# starting user-supplied icewm autostart programs in shutdown time
for file in ~/.icewm/shutdown.d/*; do
  # running user files 
  # user can disable autostart removing 'execute' bits
  [ -x $file ] && . $file
done
EOF

cat <<'EOF' > %buildroot/%icewmconfdir/startup.d/010-delay
#!/bin/sh

# delay before starting programs, to eliminate possible artifacts
# name index 010- to save ability to run programs before this
tmem=`free -m | awk '/Mem/{print $2}'`
    if [ $tmem -le 512 ]
	then delay=7
    elif [ $tmem -gt 1024 ]
	then delay=3
    else delay=5
    fi
sleep $delay
EOF

echo 'xtoolwait gkrellm'> %buildroot/%icewmconfdir/startup.d/gkrellm
echo 'mount-tray&'> %buildroot/%icewmconfdir/startup.d/mount-tray
%if_with ivman
echo 'ivman&'> %buildroot/%icewmconfdir/startup.d/ivman
%endif
echo 'apt-indicator&'> %buildroot/%icewmconfdir/startup.d/apt-indicator
echo "/usr/libexec/notification-daemon&" > %buildroot/%icewmconfdir/startup.d/notification-daemon
echo "spacefm --desktop&" > %buildroot/%icewmconfdir/startup.d/spacefm
echo "pnmixer&" > %buildroot/%icewmconfdir/startup.d/pnmixer
%if_with kde3kdesktop
echo 'kdesktop&'> %buildroot/%icewmconfdir/startup.d/kdesktop
%endif

cat <<EOF > %buildroot/%icewmconfdir/startup.d/020-idesk
#!/bin/sh
if [ -e ~/.ideskrc ]; then 
  idesk &
else # first run
  startidesk &
fi
EOF

install -pD -m 644 %SOURCE1 %buildroot/%icewmconfdir/XXkb.conf
cat <<EOF > %buildroot/%icewmconfdir/startup.d/060-xxkb
#!/bin/sh
# it is not wise to run non-configured xxkb, so we look 
# whether it is configured.
# if [ -e ~/.xxkbrc ] then user has configured xxkb properly
# if [ -e /etc/X11/app-defaults/XXkb ]
# then sysadmin has configured xxkb properly.

if [ -e ~/.xxkbrc ] || [ -e /etc/X11/app-defaults/XXkb ]; then
  xxkb&
fi
EOF

cp %buildroot/%icewmconfdir/startup.d/060-xxkb %buildroot/%icewmconfdir/startup.d/060-xxkb-tray

%if_with desklaunch
cat <<EOF > %buildroot/%icewmconfdir/startup.d/desklaunch
#!/bin/sh
# it is not wise to run non-configured desklaunch, so we look 
# whether it is configured.
# if [ -e ~/.desklaunchrc ] then user has configured desklaunch properly
if [ -e ~/.desklaunchrc ]; then
  desklaunch&
fi
EOF
%endif #desklaunch

%if_with xtdesktop
cat <<EOF > %buildroot/%icewmconfdir/startup.d/xtdesktop
#!/bin/sh
# it is not wise to run non-configured xtdesktop, so we look 
# whether it is configured.
# if [ -e ~/.xtdeskrc ] then user has configured xtdesktop properly
if [ -e ~/.xtdeskrc ]; then
  xtdesktop&
fi
EOF
%endif #xtdesktop

cat <<EOF > %buildroot/%icewmconfdir/startup.d/001-update-menus
#!/bin/sh
# if user has no local menu we will not create it either.
# otherwise it is worth updating it.
if [ -e ~/.icewm/menu ]; then
  update-menus&
fi
EOF

cat <<EOF > %buildroot/%icewmconfdir/startup.d/080-networkmanager
#!/bin/sh
/usr/libexec/polkit-1/polkit-gnome-authentication-agent-1&
/usr/bin/nm-applet&
EOF

echo "tray_mixer_plus&" > %buildroot/%icewmconfdir/startup.d/070-tray_mixer_plus

cat <<EOF > %buildroot/%icewmconfdir/startup.d/000-simple-sound
#!/bin/sh

if [ -e ~/.icewm/sounds/startup.wav ]; then
    aplay ~/.icewm/sounds/startup.wav 2&> /dev/null&
else
    if [ -e /usr/share/X11/icewm/sounds/startup.wav ]; then
    aplay /usr/share/X11/icewm/sounds/startup.wav 2&> /dev/null&
    fi
fi
EOF

cat <<EOF > %buildroot/%icewmconfdir/shutdown.d/000-simple-sound
#!/bin/sh

if [ -e ~/.icewm/sounds/shutdown.wav ]; then
    aplay ~/.icewm/sounds/shutdown.wav 2&> /dev/null&
else
    if [ -e /usr/share/X11/icewm/sounds/shutdown.wav ]; then
    aplay /usr/share/X11/icewm/sounds/shutdown.wav 2&> /dev/null&
    fi
fi
EOF

chmod 755 %buildroot/%icewmconfdir/startup.d/*
chmod 755 %buildroot/%icewmconfdir/startup
chmod 755 %buildroot/%icewmconfdir/shutdown.d/*
chmod 755 %buildroot/%icewmconfdir/shutdown

%post xxkb-tray
if [ $1 -eq 1 ]; then
if [ -e /etc/X11/app-defaults/XXkb ]; then
cp -fp /etc/X11/app-defaults/XXkb %icewmconfdir/XXkb~
cp -fp %icewmconfdir/XXkb.conf /etc/X11/app-defaults/XXkb
fi
fi

%post grun
if [ $1 -eq 1 ]; then
echo "RunCommand=\"grun\"" >> %icewmconfdir/prefoverride
fi

%preun xxkb-tray
if [ $1 -eq 0 ]; then
if [ -e %icewmconfdir/XXkb~ ]; then
mv -f %icewmconfdir/XXkb~ /etc/X11/app-defaults/XXkb
else
rm -f /etc/X11/app-defaults/XXkb
fi
fi

%preun grun
if [ $1 -eq 0 ]; then
sed -i '/RunCommand=\"grun\"/d' %icewmconfdir/prefoverride
if [ "`wc -w %icewmconfdir/prefoverride | cut -d" " -f1`" == "0" ]; then
rm -f %icewmconfdir/prefoverride
fi
fi

%files
#%doc README
%dir %icewmconfdir/startup.d
%config %icewmconfdir/startup
%dir %icewmconfdir/shutdown.d
%config %icewmconfdir/shutdown
#%_man1dir/*

%files apt-indicator
%config %icewmconfdir/startup.d/apt-indicator

%files delay
%config %icewmconfdir/startup.d/010-delay

%if_with desklaunch
%files desklaunch
%config %icewmconfdir/startup.d/desklaunch
%endif #desklaunch

%files gkrellm
%config %icewmconfdir/startup.d/gkrellm

%files idesk
%config %icewmconfdir/startup.d/020-idesk

%if_with ivman
%files ivman
%config %icewmconfdir/startup.d/ivman
%endif

%files spacefm
%config %icewmconfdir/startup.d/spacefm

%files pnmixer
%config %icewmconfdir/startup.d/pnmixer

%if_with kde3kdesktop
%files kdesktop
%config %icewmconfdir/startup.d/kdesktop
%endif

%files mount-tray
%config %icewmconfdir/startup.d/mount-tray

%files notification-daemon
%config %icewmconfdir/startup.d/notification-daemon

%files update-menus
%config %icewmconfdir/startup.d/001-update-menus

%if_with xtdesktop
%files xtdesktop
%config %icewmconfdir/startup.d/xtdesktop
%endif #xtdesktop

%files xxkb
%config %icewmconfdir/startup.d/060-xxkb

%files xxkb-tray
%config %icewmconfdir/startup.d/060-xxkb-tray
%icewmconfdir/XXkb.conf

%files networkmanager
%config %icewmconfdir/startup.d/080-networkmanager

%files tray_mixer_plus
%config %icewmconfdir/startup.d/070-tray_mixer_plus

%files grun

%files simple-sound
%config %icewmconfdir/startup.d/000-simple-sound
%config %icewmconfdir/shutdown.d/000-simple-sound

%changelog
* Tue Oct 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.20-alt3
- fixed requires for notification-daemon

* Sat Apr 27 2019 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt2
- build without ivman subpackage

* Sat Mar 30 2019 Anton Midyukov <antohami@altlinux.org> 0.20-alt1
- added pnmixer

* Sat Jun 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2
- fixed unpackaged files

* Wed Apr 11 2018 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- added spacefm (closes: 34794)

* Thu Sep 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- removed kdesktop

* Tue Nov 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- added notification-daemon

* Tue Oct 11 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt4
- added apt-indicator

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt3
- updated description

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt0.M70T.1
- backport for t7

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- conditional def_with networkmanager (t7 support)

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- added mount-tray subpackage

* Sat Sep 26 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.15-alt2
- updated requires for networkmanager subpackage

* Sun May 31 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.15-alt1
- added "shutdown" script, thx to YYY at forum
- added simple-sound subpackage, thx to YYY and Leo-sp150 at forum
- delay moved to separate subpackage
- cosmetic fix of xxkb conf file
- some programs are assigned numeric indexes
- changed Url: and Packager:

* Mon Feb 09 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.14-alt3
- fixed typo in networkmanager subpackage

* Tue May 14 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.14-alt2
- delay before starting programs made customizable

* Wed Apr 10 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.14-alt1
- added grun subpackage

* Sat Mar 30 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.13-alt1
- added xxkb-tray subpackage
- added tray_mixer_plus subpackage
- spec converted to utf-8

* Thu Feb 28 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.12-alt1
- added delay before starting programs, to eliminate possible artifacts
- added networkmanager

* Wed Mar 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt3
- removed artsd support (obsolete)

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1
- disabled unmet subpackages using nmu script

* Fri Sep 21 2007 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- fixed requires in update-menus

* Thu Sep 20 2007 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added arts, update-menus
- TODO: README

* Sat Sep 08 2007 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- added ivman, desklaunch and xtdesktop support

* Mon Apr 17 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt2
- added kdesktop support

* Wed Mar 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt1
- build for Sisyphus

* Wed Mar 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt0.M30.1
- backport for M30

* Wed Mar 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt0
- initial build
