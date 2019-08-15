Name: qlipper
Version: 5.1.2
Release: alt1

Summary: Lightweight clipboard history
License: GPLv3+
Group: Graphical desktop/Other

Url: https://github.com/pvanek/qlipper
Packager: Anton Midyukov <antohami@altlinux.org>

Source0: %name-%version.tar
Source1: qlipper_ru.ts
Source2: qlipper-startup.desktop
Patch0: qlipper-5.1.1-cmake-ru.patch
Patch1: qlipper-5.1.1-desktop-ru.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: qt5-tools-devel

%description
Lightweight clipboard history applet.

%prep
%setup
%patch0 -p1
%patch1 -p1
cp -a %SOURCE1 ts
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.h' |
	xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%cmake -DCMAKE_BUILD_TYPE=release -DUSE_SYSTEM_QXT=OFF -DUSE_SYSTEM_QTSA=ON ..
%cmake_build

%install
%cmakeinstall_std
desktop-file-validate %buildroot/%_desktopdir/%name.desktop

mkdir -p %buildroot%_sysconfdir/xdg/autostart
install -pm644 %SOURCE2 %buildroot%_sysconfdir/xdg/autostart/

%find_lang %name --with-qt --without-mo

%files -f %name.lang
%doc COPYING
%doc README
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/128x128/apps/qlipper.png
%_sysconfdir/xdg/autostart/qlipper-startup.desktop

%changelog
* Tue Aug 13 2019 Anton Midyukov <antohami@altlinux.org> 5.1.2-alt1
- new version 5.1.2

* Fri Jun 21 2019 Michael Shigorin <mike@altlinux.org> 5.1.1-alt5
- E2K: strip UTF-8 BOM for lcc < 1.24
- Drop remainders of %%ubt use
- Minor spec cleanup

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt4
- NMU: remove %%ubt from release

* Sat Jun 16 2018 Anton Midyukov <antohami@altlinux.org> 5.1.1-alt3
- Rebuilt for aarch64

* Thu Mar 22 2018 Anton Midyukov <antohami@altlinux.org> 5.1.1-alt2
- Added autostart

* Tue Mar 06 2018 Anton Midyukov <antohami@altlinux.org> 5.1.1-alt1
- Initial build for ALT (thanks Rosa Team for russian translation)
