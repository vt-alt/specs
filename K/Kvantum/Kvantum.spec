Name: Kvantum
Version: 0.16.0
Release: alt1

Summary: SVG-based theme engine for Qt5, KDE and LXQt
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://github.com/tsujan/Kvantum
# Source-url: https://github.com/tsujan/Kvantum/archive/V%version.tar.gz
Source: %name-%version.tar.gz
Packager: Leontiy Volodin <lvol@altlinux.org>

BuildRequires: gcc-c++ cmake libX11-devel libXext-devel libqt4-devel qt5-base-devel qt5-tools-devel qt5-svg-devel qt5-x11extras-devel kf5-kwindowsystem-devel desktop-file-utils icon-theme-hicolor
Requires: %name-data

%description
Kvantum is an SVG-based theme engine for Qt5, KDE and LXQt, with an emphasis
on elegance, usability and practicality.

Kvantum has a default dark theme, which is inspired by the default theme of
Enlightenment. Creation of realistic themes like that for KDE was the first
reason to make Kvantum but it goes far beyond its default theme: you could
make themes with very different looks and feels for it, whether they be
photorealistic or cartoonish, 3D or flat, embellished or minimalistic, or
something in between, and Kvantum will let you control almost every aspect of
Qt widgets.

Kvantum also comes with extra themes that are installed as root with Qt5
installation and can be selected and activated by using Kvantum Manager.

%package data
Summary: SVG-based theme engine for Qt5, KDE and LXQt
Group: Graphical desktop/Other
BuildArch: noarch

%description data
Kvantum is an SVG-based theme engine for Qt5, KDE and LXQt, with an emphasis
on elegance, usability and practicality.

This package contains the data needed for Kvantum.

%prep
%setup

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif
%cmake_insource
%make_build

%install
%makeinstall_std

# desktop-file-validate doesn't recognize LXQt
sed -i "s|LXQt|X-LXQt|" %buildroot%_desktopdir/kvantummanager.desktop
desktop-file-validate %buildroot%_desktopdir/kvantummanager.desktop

%find_lang %name --all-name --with-qt

%files
%doc COPYING
%doc ChangeLog NEWS README.md
%_bindir/kvantummanager
%_bindir/kvantumpreview
%_qt5_plugindir/styles/libkvantum.so

%files data -f %name.lang
%_datadir/Kvantum
%_desktopdir/kvantummanager.desktop
%dir %_datadir/color-schemes
%_datadir/color-schemes/Kv*
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/apps
%_iconsdir/hicolor/scalable/apps/kvantum.svg
%dir %_datadir/themes
%dir %_datadir/themes/Kv*
%_datadir/themes/Kv*/*

%changelog
* Thu Jun 25 2020 Leontiy Volodin <lvol@altlinux.org> 0.16.0-alt1
- 0.16.0
- fully translated in russian (thanks Dmitry Astankov)

* Wed May 06 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.3-alt1
- 0.15.3

* Mon Apr 13 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.2-alt1
- 0.15.2

* Wed Mar 18 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.1-alt1
- 0.15.1

* Thu Mar 12 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.0-alt1
- 0.15.0

* Thu Jan 09 2020 Leontiy Volodin <lvol@altlinux.org> 0.14.1-alt1
- 0.14.1

* Mon Dec 30 2019 Leontiy Volodin <lvol@altlinux.org> 0.14.0-alt1
- 0.14.0

* Mon Dec 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.13.0-alt1
- 0.13.0

* Mon Oct 14 2019 Leontiy Volodin <lvol@altlinux.org> 0.12.1-alt1
- 0.12.1

* Wed Oct 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.12.0-alt1
- 0.12.0

* Tue Jul 30 2019 Leontiy Volodin <lvol@altlinux.org> 0.11.2-alt1
- 0.11.2

* Tue Jul 02 2019 Michael Shigorin <mike@altlinux.org> 0.11.1-alt2
- E2K: explicit -std=c++11
- minor spec cleanup

* Mon May 13 2019 Leontiy Volodin <lvol@altlinux.org> 0.11.1-alt1
- 0.11.1

* Mon Mar 25 2019 Leontiy Volodin <lvol@altlinux.org> 0.11.0-alt1
- New release 0.11.0

* Wed Feb 06 2019 Leontiy Volodin <lvol@altlinux.org> 0.10.9-alt3
- 0.10.9 (final release)

* Fri Jan 11 2019 Leontiy Volodin <lvol@altlinux.org> 0.10.9-alt2.gitefca972
- Update from git (commit: efca972)
- Fixed post-install files

* Thu Nov 08 2018 Leontiy Volodin <lvol@altlinux.org> 0.10.9-alt1
- New release 0.10.9
- Changed spec for update from git

* Wed Nov 07 2018 Leontiy Volodin <lvol@altlinux.org> 0.10.8-alt1
- Initial release for Sisyphus

