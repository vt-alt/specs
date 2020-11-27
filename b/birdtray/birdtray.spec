%define _unpackaged_files_terminate_build 1

Name: birdtray
Version: 1.9.0
Release: alt1
Summary: Birdtray is a free system tray notification for new mail for Thunderbird
License: GPLv3 
Group: Networking/Mail
Url: https://github.com/gyunaev/birdtray
Source: %name-%version.tar
Patch1: alt-qt5.15.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt5-base-devel
BuildRequires: libsqlite3-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-svg-devel

%description
System tray notifications for Thunderbird
Birdtray provides systray notifications for Thunderbird.  It displays the
count of unread mail, hides the Thunderbird window when not in use, and
restores it on clicking the tray icon.  It also provides a context menu
with commands such as starting composing a new mail.

It is a nasty hack -- an external process looking at Thunderbird's
insides, it suffers from problems like noticing new mails only after a
delay, having to restart Thunderbird just to hide its window, etc --
you'd want to use an extension like firetray instead -- but, it is
likely that support for Thunderbird XUL extensions will be dropped soon,
possibly by the time you read these words.

%prep
%setup
%patch1 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%buildroot/%prefix
%cmake_build

%install
mkdir %buildroot
cd BUILD
cmake --build . --target install
sed -i '/Exec=birdtray/i\Comment=Birdtray' %buildroot%_desktopdir/com.ulduzsoft.Birdtray.desktop

%files
%doc README.md
%_bindir/%name
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*
%_datadir/ulduzsoft/
%_datadir/ulduzsoft/%name/translations/*.qm
%_desktopdir/com.ulduzsoft.Birdtray.desktop

%changelog
* Thu Nov 12 2020 Mikhail Chernonog <snowmix@altlinux.org> 1.9.0-alt1
- 1.8.1 -> 1.9.0

* Tue Sep 29 2020 Sergey V Turchin <zerg@altlinux.org> 1.8.1-alt2
- Fix to build with Qt-5.15

* Fri Jul 24 2020 Mikhail Chernonog <snowmix@altlinux.org> 1.8.1-alt1
- 1.7.0 -> 1.8.1

* Wed Feb 19 2020 Mikhail Chernonog <snowmix@altlinux.org> 1.7.0-alt1
- 1.5 -> 1.7.0
- Update desktop file
- Update spec file for build using cmake

* Wed May 15 2019 Mikhail Chernonog <snowmix@altlinux.org> 1.5-alt1
- Initial build for Sisyphus
