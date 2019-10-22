%define _unpackaged_files_terminate_build 1

Name: veyon
Version: 4.2.5
Release: alt1
Group: Education
License: GPLv2
Url: https://veyon.io/
# https://github.com/veyon/veyon/

Summary: Open source computer monitoring and classroom management
Summary(ru.UTF-8): Программа с открытым кодом для контроля компьютеров и организации учебного процесса

Source: %name-%version.tar
Source1: ultravnc.tar
Source2: libvncserver.tar
Source3: x11vnc.tar

Patch1: Unbundle-some-libraries-and-fix-build-alt.patch

BuildRequires: rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++ make cmake
BuildRequires: kde5-kldap-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: libjpeg-devel
BuildRequires: zlib-devel
BuildRequires: liblzo2-devel
BuildRequires: libssl-devel
BuildRequires: libldap-devel
BuildRequires: libpam0-devel
BuildRequires: libprocps-devel
BuildRequires: libsasl2-devel
BuildRequires: libqca2-devel
BuildRequires: libqca-qt5-devel
BuildRequires: libXdamage-devel
BuildRequires: libXtst-devel

%description
Veyon is a free and open source software 
for computer monitoring and classroom management supporting Windows and Linux.
It enables teachers to view and control computer labs and interact with students.
Veyon is available in different languages and provides lots of useful features:

* see what's going on in computer labs in overview mode and take screenshots
* remote control computers to support and help users
* broadcast teacher's screen to students in realtime by using demo mode 
(either in fullscreen or in a window)
* lock workstations for attracting attention to teacher
* send text messages to students
* powering on/off and rebooting computers remote
* remote logoff and remote execution of arbitrary commands/scripts
* home schooling - Veyon's network technology is not restricted to a subnet 
and therefore students at home can join lessons via VPN connections 
just by installing the Veyon service.

%description -l ru_RU.UTF-8
Veyon - это бесплатное программное обеспечение с открытым исходным кодом
для контроля компьютеров и организации учебного процесса, поддерживающее Windows и Linux.
Оно позволяет учителям просматривать и контролировать компьютерные классы
и взаимодействовать со студентами.
Veyon доступен на разных языках и предоставляет множество полезных функций:

* просмотр происходящего в компьютерных классах в режиме обзора и создание скриншотов
* удаленное управление компьютерами для поддержки и помощи пользователям
* трансляция экрана учителя ученикам в режиме реального времени,
используя демонстрационный режим (либо в полноэкранном режиме, либо в окне)
* блокировка рабочих мест для привлечения внимания к учителю
* отправка текстовых сообщений студентам
* удалённое включение / выключение и перезагрузка компьютеров
* удаленный выход из системы и удаленное выполнение произвольных команд / скриптов
* домашнее обучение - сетевые технологии Veyon не ограничиваются подсетью,
поэтому студенты могут присоединиться к урокам через VPN-подключения,
просто установив Veyon у себя на домашнем ПК.

%prep
%setup -a1 -a2 -a3
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc COPYING README.md
%_unitdir/veyon.service
%_libdir/%name
%_libdir/*.so
%_bindir/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*
%_datadir/polkit-1/actions/*
%_datadir/pixmaps/*
%_datadir/%name

%changelog
* Tue Oct 22 2019 Pavel Moseev <mars@altlinux.org> 4.2.5-alt1
- Initial release for ALT Linux
