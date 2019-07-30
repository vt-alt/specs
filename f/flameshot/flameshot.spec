Name: flameshot
Version: 0.6.0.0.53.git7ee9a3f
Release: alt1

Summary: Powerful yet simple to use screenshot software

License: GPLv3
Group: Graphics
Url: https://github.com/lupoDharkael/flameshot

Source: %name-%version.tar
Patch: flameshot-0.6.0-fix-autostart-icon.patch

Packager: Anton Shevtsov <x09@altlinux.org>

BuildRequires: qt5-base-devel qt5-tools qt5-svg-devel

%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

%prep
%setup
%patch -p1
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%qmake_qt5 PREFIX=%_prefix
%make_build

%install
%install_qt5

%check
%make_build check

%files
%doc LICENSE README.md
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/bash-completion/completions/%name
%_datadir/dbus-1/interfaces/org.dharkael.Flameshot.xml
%_datadir/dbus-1/services/org.dharkael.Flameshot.service
%_datadir/%name
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/%name.appdata.xml

%changelog
* Mon Jun 03 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.0.0.53.git7ee9a3f-alt1
- Build from new commit.
- Fix problem with disabled tray icon (Closes: #36299).
  + (https://github.com/lupoDharkael/flameshot/pull/495)
- New try of fixing icon in autostarted program (Closes: #36134).
- E2K: strip UTF-8 BOM for lcc < 1.24 (thx to mike@).
- Minor spec cleanup (thx to mike@).

* Mon Mar 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.0.0.46.git4261915-alt1
- Fixed translation of system buttons in dialogs.
  + (https://github.com/lupoDharkael/flameshot/pull/474)
- Added russian translation of desktop file.
  + (https://github.com/lupoDharkael/flameshot/pull/475)
- Fixed errors in russian translation.
  + (https://github.com/lupoDharkael/flameshot/pull/476)
- Fixed export of startup option in configuration file (Closes: #36149).
  + (https://github.com/lupoDharkael/flameshot/pull/477)
- Fixed icon in autostarted program for i586 arch (Closes: #36134).

* Tue Feb 19 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.0.0.25.git94daa4f-alt1
- Fix icon in autostarted program (Closes: #36134).
- Update russian translation.

* Fri Nov 16 2018 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt2
- Corrected the previous build according good sense.

* Mon Sep 03 2018 Anton Shevtsov <x09@altlinux.org> 0.6.0-alt1
- Initial build for ALT
