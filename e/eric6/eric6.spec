Name: eric6
Summary: Python IDE
Version: 19.04
Release: alt2

License: GPLv3+
Group: Development/Python3
Url: http://eric-ide.python-projects.org
Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch

Source: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-%version.tar.gz
Source1: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-de-%version.tar.gz
Source2: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-en-%version.tar.gz
Source3: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-es-%version.tar.gz
Source4: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-ru-%version.tar.gz

Source30: eric-16.png
Source31: eric-32.png
Source32: eric-48.png
Source33: eric-64.png

# sane defaults: disable version check, qt4/qt5 configuration
Patch1: eric6-18.06-defaults.patch
Patch2: eric6-desktop.patch
BuildRequires(pre): rpm-build-python3
BuildRequires: desktop-file-utils
BuildRequires: python3-devel
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-qscintilla2-qt5
BuildRequires: libappstream-glib
%py3_requires PyQt5.Qsci
%py_requires json

# ???
%add_python3_req_skip __builtin__ mod_python

%description
eric6 is a full featured Python IDE.

%prep
%setup -a 1 -a 2 -a 3 -a 4 -n eric6-%version

%patch1 -p1
%patch2 -p2

%build
# Empty build

%install
python3 install.py \
  -i %buildroot/ \
  -b %_bindir \
  -d %python3_sitelibdir

# icons
install -m644 -p -D %SOURCE30 %buildroot%_iconsdir/hicolor/16x16/apps/eric.png
install -m644 -p -D %SOURCE31 %buildroot%_iconsdir/hicolor/32x32/apps/eric.png
install -m644 -p -D %SOURCE32 %buildroot%_iconsdir/hicolor/48x48/apps/eric.png
install -m644 -p -D %SOURCE33 %buildroot%_iconsdir/hicolor/64x64/apps/eric.png

%find_lang %name --with-qt --all-name

# use legacy appdata dir instead of metainfo
if [ -d %buildroot%_datadir/metainfo ]; then
mkdir -p %buildroot%_datadir/appdata/
mv %buildroot%_datadir/metainfo/*.xml \
%buildroot%_datadir/appdata/
fi

## unpackaged files
# deprecated icons
rm -rfv %buildroot%_pixmapsdir/eric*
rm -fv  %buildroot%python3_sitelibdir/eric6/LICENSE.GPL3

# not needed
rm -fv %buildroot%_desktopdir/eric6_*.desktop

%check
appstream-util validate-relax --nonet %buildroot%_datadir/appdata/eric6.appdata.xml
desktop-file-validate %buildroot%_desktopdir/eric6.desktop

%files -f %name.lang
%doc eric/README* THANKS LICENSE.GPL3
%_bindir/eric6*
%python3_sitelibdir/eric6config.py*
%python3_sitelibdir/__pycache__/*
%dir %python3_sitelibdir/eric6/
%python3_sitelibdir/eric6/*.py*
%python3_sitelibdir/eric6/__pycache__/
%python3_sitelibdir/eric6/icons/
%python3_sitelibdir/eric6/pixmaps/
%python3_sitelibdir/eric6/[A-Z]*/
%python3_sitelibdir/eric6/*.e4k
%dir %python3_sitelibdir/eric6/i18n/
%python3_sitelibdir/eric6plugins/
%_datadir/appdata/eric6.appdata.xml
%_desktopdir/eric6.desktop
%_iconsdir/hicolor/*/apps/eric.*
%_datadir/qt5/qsci/api/python/*
%_datadir/qt5/qsci/api/qss/*
%_datadir/qt5/qsci/api/ruby/*

%changelog
* Mon Jun 03 2019 Anton Midyukov <antohami@altlinux.org> 19.04-alt2
- add russian translate for desktop file
- clean not needed desktop files
- add icon 16x16

* Mon Apr 22 2019 Anton Midyukov <antohami@altlinux.org> 19.04-alt1
- New version 19.04

* Wed Jan 24 2018 Anton Midyukov <antohami@altlinux.org> 18.01-alt1.S1
- New version 18.01
- Added missing requires python(json)

* Mon Jan 15 2018 Anton Midyukov <antohami@altlinux.org> 17.11-alt2.S1
- Added missing requires python3(PyQt5.Qsci)

* Mon Nov 13 2017 Anton Midyukov <antohami@altlinux.org> 17.11-alt1.S1
- Initial build for ALT Sisyphus (Closes: 33933).
