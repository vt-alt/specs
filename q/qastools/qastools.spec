Name: qastools
Version: 0.23.0
Release: alt1

Summary: Collection of desktop applications for ALSA
License: GPLv3
Group: Sound

Url: http://xwmw.org/qastools
Source: %name-%version.tar
Patch: disabled-tray-icon-at-startup.patch
Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: qt5-base-devel qt5-svg-devel qt5-tools-devel
# BuildRequires: qt5-linguist
BuildRequires: pkgconfig(alsa)
# For libudev.h
BuildRequires: libudev-devel

Requires: qasconfig = %version-%release
Requires: qashctl = %version-%release
Requires: qasmixer = %version-%release

%description
QasTools is a collection of desktop applications for the ALSA sound system.

%package -n qascommon
Summary: Common part of QasTools
Group: Sound
BuildArch: noarch

%description -n qascommon
Common part of QasTools.

%package -n qasconfig
Summary: ALSA configuration browser
Group: Sound
Requires: qascommon = %version-%release
Requires: icon-theme-hicolor

%description -n qasconfig
Browser for the ALSA configuration tree.

%package -n qashctl
Summary: ALSA complex mixer
Group: Sound
Requires: qascommon = %version-%release
Requires: icon-theme-hicolor

%description -n qashctl
Mixer for ALSA's more complex "High level Control Interface".

%package -n qasmixer
Summary: ALSA simple mixer
Group: Sound
Requires: qascommon = %version-%release
Requires: icon-theme-hicolor

%description -n qasmixer
Desktop mixer for ALSA's "Simple Mixer Interface" (alsamixer).

%prep
%setup
%patch -p1

%build
%cmake -DSKIP_LICENSE_INSTALL:BOOL=ON
%cmake_build

%install
%cmakeinstall_std
for file in %buildroot/%_desktopdir/*.desktop; do
    desktop-file-validate $file
done

%files
# meta package

%files -n qascommon
%doc COPYING CHANGELOG README.md TODO
%_datadir/%name

%files -n qasconfig
%_bindir/qasconfig
%_desktopdir/qasconfig.desktop
%_iconsdir/hicolor/*/apps/qasconfig.*
%_man1dir/qasconfig.1.*
%_datadir/metainfo/qasconfig.appdata.xml

%files -n qashctl
%_bindir/qashctl
%_desktopdir/qashctl.desktop
%_iconsdir/hicolor/*/apps/qashctl.*
%_man1dir/qashctl.1.*
%_datadir/metainfo/qashctl.appdata.xml

%files -n qasmixer
%_bindir/qasmixer
%_desktopdir/qasmixer.desktop
%_iconsdir/hicolor/*/apps/qasmixer.*
%_man1dir/qasmixer.1.*
%_datadir/metainfo/qasmixer.appdata.xml

%changelog
* Fri Aug 07 2020 Anton Midyukov <antohami@altlinux.org> 0.23.0-alt1
- new version 0.23.0

* Tue Nov 19 2019 Anton Midyukov <antohami@altlinux.org> 0.22.0-alt1
- new version 0.22.0

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.21.0-alt5
- NMU: remove rpm-build-ubt from BR:

* Fri May 31 2019 Michael Shigorin <mike@altlinux.org> 0.21.0-alt4
- Dropped %%ubt
- Minor spec cleanup

* Sat Jun 16 2018 Anton Midyukov <antohami@altlinux.org> 0.21.0-alt3%ubt
- Rebuilt for aarch64

* Sun Jan 14 2018 Anton Midyukov <antohami@altlinux.org> 0.21.0-alt2%ubt
- Disabled tray icon at startup

* Thu Dec 21 2017 Anton Midyukov <antohami@altlinux.org> 0.21.0-alt1%ubt
- Initial build for ALT Sisyphus.
