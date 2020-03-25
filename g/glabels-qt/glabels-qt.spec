Name: glabels-qt
Version: 3.99
Release: alt1master558

Summary: gLabels Label Designer (Qt/C++)

License: GPL
Group: Graphics
Url: http://glabels.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/jimevins/glabels-qt/archive/glabels-3.99-master558.tar.gz
Source: %name-%version.tar

Conflicts: glabels

BuildRequires: gcc-c++ cmake
BuildRequires: zlib-devel
BuildRequires: qt5-base-devel qt5-svg-devel qt5-tools-devel
BuildRequires: libqt5-test

BuildRequires: libqrencode4-devel
# libbarcode-static-devel
# zint (obsoleted)

%description
gLabels-qt is the development version of the next major version of gLabels (a.k.a. glabels-4).

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

#find_lang --with-qt

%files
%doc README.md CREDITS.md
%_bindir/glabels-qt
%_bindir/glabels-batch-qt
%_datadir/appdata/*
%_desktopdir/*
%_datadir/%name/
%_man1dir/*
%_iconsdir/hicolor/*/*/*
%_datadir/mime/packages/*

%changelog
* Thu Feb 06 2020 Vitaly Lipatov <lav@altlinux.ru> 3.99-alt1master558
- initial build for ALT Sisyphus
