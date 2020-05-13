# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qterminal
Version: 0.15.0
Release: alt1

Summary: Qt-based multitab terminal emulator
License: GPL
Group: Terminals

Url: http://github.com/qterminal/qterminal
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake lxqt-build-tools
BuildRequires: qt5-base-devel qt5-tools-devel qt5-x11extras-devel
BuildRequires: libqtermwidget-devel >= %version

%description
Qt-based multitab terminal emulator based on QTermWidget.

Initially this project was started as an attempt to create relatively
light and stable terminal emulator application like Konsole or
gnome-terminal but without any dependency from such monsters as KDE or
Gnome. I was looking for such kind of application for a long time but
haven't found anything worth while. That's why when I met QTermWidget
and tried it I was really happy! :) That was exactly what I need.
Actually I didn't pay much effort for its improvement, I've just put it
into tab widget, add basic config and some useful actions. Seems that's
pretty much enough for now.

0.4.0+ is a friendly fork, the original project is still available
at http://qterminal.sourceforge.net/

%prep
%setup

%build
%ifarch e2k
%add_optflags -std=c++11
%endif
%cmake \
    -DUSE_QT5=true \
    -DQTERMWIDGET_PATH_SHARE=%_datadir/qtermwidget5
%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS LICENSE CHANGELOG README*
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*
%_datadir/appdata/*
%_datadir/%name

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Tue May 22 2018 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- 0.9.0

* Tue Oct 24 2017 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Fri Aug 25 2017 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- build against qt5/qtermwidget-qt5
- E2K: add -std=c++11 explicitly

* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Nov 14 2014 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- 0.6.0 (closes: #30468)
- updated Url:
- use bundled libqxt

* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- moved to gitorius 0.4.0 fork
- spec cleanup

* Mon Jan 24 2011 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1
- Initial build in Sisyphus

* Sat Jan 08 2011 TI_Eugene <ti.eugene@gmail.com> 0.2.0
- Next version

* Fri Feb 03 2009 TI_Eugene <ti.eugene@gmail.com> 0.1.4
- Initital build in OBS
