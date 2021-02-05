%def_enable qt5

Name: mount-tray
Version: 1.2.5
Release: alt7

Summary: udisks based removable device mounter
License: GPLv2
Group: System/Kernel and hardware
Url: https://github.com/h4tr3d/mount-tray
Packager: Evgenii Terechkov <evg@altlinux.org>

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: gcc-c++ libudev-devel
%if_enabled qt5
BuildRequires: qt5-base-devel
%else
BuildRequires: libqt4-devel
%endif
Requires: udisks2

%description
Small Qt-based tray application for mount and unmount removable
devices like USB storage or CD and DVD-ROM. It used udisks for mount
and unmount operations, udev for device detection and DBus for take
information about external mounting and unmounting (for ex from
pcmanfm).

%prep
%setup
%patch0 -p1

%build
%if_enabled qt5
%qmake_qt5
%else
%qmake_qt4
%endif
%make_build STRIP=touch

%install
install -pDm 755 %name %buildroot%_bindir/%name
install -pDm 644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -pDm 644 images/%name.png %buildroot%_pixmapsdir/%name.png

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%doc COPY

%changelog
* Wed Jan 27 2021 Dmitriy Khanzhin <jinn@altlinux.org> 1.2.5-alt7
- Use tray icon in png format (ALT #39566)
- Restore patch
- Remove [Build]Requires no longer needed

* Thu Jan 07 2021 Dmitriy Khanzhin <jinn@altlinux.org> 1.2.5-alt6
- Add application icon
- Add Requires: udisks2
- Remove patch
- Cleanup spec

* Wed Nov 13 2019 Nikita Ermakov <arei@altlinux.org> 1.2.5-alt5
- Enable Qt5 by default and make Qt4 optional.

* Sun Mar 26 2017 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt4
- Change Url: (ALT#33264)

* Tue Nov 17 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt3
- Add requires to libqt[45]-svg (ALT#31502)

* Fri Jul  3 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt2
- Build with qt4 (qt5 is now optional)

* Fri Jul  3 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt1
- 1.2.5-4-g8bb9e94
