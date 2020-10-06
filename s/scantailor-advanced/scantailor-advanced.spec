Name: scantailor-advanced
Version: 1.0.17
Release: alt0.git3d1e74e

Summary: Scan processing software
License: GPL
Group: Graphics
Url: https://github.com/4lex4/scantailor-advanced/

#Source-url: https://github.com/4lex4/scantailor-advanced/archive/v%version.tar.gz
# Source-url: https://github.com/4lex4/scantailor-advanced/archive/master.zip
Source: %name-%version.tar
Source1: %name.desktop

# Automatically added by buildreq on Fri Apr 10 2009
BuildRequires: boost-devel-headers boost-intrusive-devel cmake gcc-c++
BuildRequires: zlib-devel libXft-devel libXmu-devel libXpm-devel libjpeg-devel libtiff-devel libpng-devel
BuildRequires: qt5-base-devel qt5-tools-devel qt5-svg-devel libqt5-core libqt5-network libqt5-gui qt5-imageformats

%description
scantailor-advanced is a book scan processing software.
ScanTailor Advanced is the version that merges the features
of the ScanTailor Featured and ScanTailor Enhanced versions,
brings new ones and fixes.
It splits scanned pages, aligns, and converts to b/w from
grayscale. It has GUI interface. Analogs of this
program are ScanKromsator (written by kamerade bolega,
currently discontinued), BookRestorer.

%description -l ru_RU.UTF-8
scantailor-advanced - программа для обработки отсканированных
книг. Эта программа может разделять развороты, выравнивать
страницы и переводить в ч/б из градаций серого. Имеет
GUI интерфейс. Наиболее известными аналогами
программы является ScanKromsator (написан камрадом bolega,
сейчас не развивается) и BookRestorer.

%prep
%setup

%build
#cp resources/appicon.svg %name.svg
%cmake
%cmake_build

%install
%cmakeinstall_std
mv %buildroot%_bindir/scantailor %buildroot%_bindir/%name
mv %buildroot%_iconsdir/hicolor/scalable/apps/ScanTailor.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
#mkdir -p %buildroot%_bindir
#mkdir -p %buildroot%_datadir/%name/translations
#install -pm755 scantailor-advanced %buildroot/%_bindir/
#install -pm644 *.qm %buildroot%_datadir/%name/translations
#install -pm644 -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
rm -f %buildroot%_desktopdir/scantailor.desktop
install -pm644 -D %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/scantailor-advanced
%dir %_datadir/%name/
%_datadir/%name/translations/
%_desktopdir/%name.desktop
/usr/share/mime/packages/scantailor-project.xml
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Sat Sep 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.17-alt0.git3d1e74e
- build git 3d1e74e

* Fri Apr 05 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.16-alt1
- initial build for ALT Sisyphus

