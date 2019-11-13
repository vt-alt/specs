Name: easypaint
Epoch: 1
Version: 0.1.1
Release: alt1
Summary: Easy graphic editing program
License: MIT
Group: Graphics
URL: https://github.com/Gr1N/EasyPaint

Source: %name-%version.tar
Source1: %name.desktop

BuildRequires: gcc-c++ qt5-base-devel qt5-tools
BuildRequires: ImageMagick-tools

%description
%summary

%prep
%setup

%build
pushd sources
lrelease-qt5 easypaint.pro
%qmake_qt5
%make_build
popd

%install
install -Dp -m0755 sources/bin/easypaint %buildroot%_bindir/%name
install -Dp -m0644 sources/media/logo/easypaint_64.png %buildroot%_pixmapsdir/%name.png
install -Dp -m0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%_datadir/%name/translations
cp sources/translations/*.qm %buildroot%_datadir/%name/translations/

for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
        convert %buildroot%_pixmapsdir/%name.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/%name.png
done

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/*.png
%_liconsdir/*
%_niconsdir/*
%_miconsdir/*

%changelog
* Wed Nov 06 2019 Anton Midyukov <antohami@altlinux.org> 1:0.1.1-alt1
- New snapshot from commit 81d7a87d
- switch to new upstream
- build with qt5
- build translations (Closes: 32788)
- update license

* Fri Apr 15 2011 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build in Sisyphus

* Fri Apr 15 2011 TI_Eugene <ti.eugene@gmail.com>
- 0.6.0, initial OBS release
