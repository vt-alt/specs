Name: timeline
Version: 2.2.0
Release: alt1
Group: Office
Summary: Displaying and navigating events on a timeline
License: GPL-3.0 and CC-BY-SA-3.0
Url: http://thetimelineproj.sourceforge.net/

Source: %name-%version.zip
Source1: %name.1
Patch: timeline-fix-paths.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: unzip

%description
Timeline is a cross-platform application for displaying and navigating
events on a timeline.

Features:
- Organize events in hierarchical categories
- Move and resize events with the mouse
- Duplicate events
- Search events
- Go to a specific date
- Scroll and zoom with mouse wheel
- Different representation depending on zoom level
- Export to image
- Available in multiple languages

%package -n python3-module-timelinelib
Group: Development/Python3
Summary: Python module for %name, %summary

%description -n python3-module-timelinelib
Python module for %name, %summary

%prep
%setup
%patch -p0

cat > %name.desktop <<@@@
[Desktop Entry]
Icon=%name
Name=Timeline
Comment=Display and navigate information on a timeline
Comment[ru]=Редактор данных на временной шкале
Exec=%name
Terminal=false
Type=Application
Categories=Office;Calendar;
StartupNotify=false
@@@

%build
python3 ./tools/generate-mo-files.py

%install
install -Dpm0755 source/timeline.py %buildroot%_bindir/timeline

mkdir -p %buildroot%_datadir/timeline
cp -pr icons %buildroot%_datadir/timeline/
 
mkdir -p %buildroot%python3_sitelibdir/timelinelib
cp -pr source/timelinelib/* %buildroot%python3_sitelibdir/timelinelib/
 
install -Dpm0644 icons/48.png %buildroot%_datadir/icons/hicolor/48x48/apps/timeline.png
 
install -Dm0644 %name.desktop %buildroot%_desktopdir/%name.desktop
 
mkdir -p %buildroot%_datadir/locale
cp -a translations/*/ %buildroot%_datadir/locale/
 
install -Dm0644 %SOURCE1 %buildroot%_man1dir/%name.1

# Drop bundled python dependencies.
rm -rf %buildroot%_datadir/timeline/dependencies

%find_lang %name

%files -f %name.lang
%doc AUTHORS README
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/%name.desktop
%_man1dir/*

%files -n python3-module-timelinelib
%python3_sitelibdir/timelinelib*

%changelog
* Fri May 22 2020 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version (ALT #38517).
- Fix License tag according to SPDX.

* Wed Feb 11 2015 Fr. Br. George <george@altlinux.ru> 1.5.0-alt1
- Autobuild version bump to 1.5.0

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 1.4.1-alt1
- Autobuild version bump to 1.4.1

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Autobuild version bump to 1.3.0

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 1.2.4-alt1
- Autobuild version bump to 1.2.4

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 0.21.1-alt1
- Autobuild version bump to 0.21.1

* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 0.20.0-alt1
- Autobuild version bump to 0.20.0

* Wed Jan 16 2013 Fr. Br. George <george@altlinux.ru> 0.19.0-alt1
- Autobuild version bump to 0.19.0
- Fix patch

* Wed Oct 24 2012 Fr. Br. George <george@altlinux.ru> 0.18.0-alt2
- Add library dependence

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 0.18.0-alt1
- Autobuild version bump to 0.18.0

* Mon Jun 25 2012 Fr. Br. George <george@altlinux.ru> 0.17.0-alt1
- Autobuild version bump to 0.17.0
- Fix patch

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13.0-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Fr. Br. George <george@altlinux.ru> 0.13.0-alt1
- Autobuild version bump to 0.13.0

