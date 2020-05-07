Name:		QCheckers
Summary:	Qt checkers game
Summary(ru_RU.UTF8): Игра в шашки на Qt
Summary(uk_UA.UTF8): Гра в шашки на Qt
Version:	0.9.0
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
License:	GPLv2
Group:		Games/Boards
Url:		https://github.com/portnov/qcheckers
Source0:	%name-%version.tar.gz
Source1:	%name.desktop
Source2:	qcheckers_uk.ts
Source3:	%name.png

BuildRequires: /usr/bin/convert qt5-charts-devel qt5-declarative-devel qt5-multimedia-devel qt5-svg-devel qt5-tools-devel

%description
QCheckers (formely known as KCheckers) is a Qt-based checkers
board game. It can play english draughts and russian draughts.

There is some additional information in the FAQ file.

%prep
%setup -q -n %name
subst 's|0.8.1|0.9.0|g' ./src/common.h

%build
cp %SOURCE2 ./lang/
lrelease-qt5 ./lang/*.ts
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" "PREFIX=/usr"
%make_build VERBOSE=1

%install
make INSTALL_ROOT=%buildroot install
install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
rm -f %buildroot%_datadir/qcheckers/lang/*.ts

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %SOURCE3 %buildroot%_liconsdir/%name.png
convert -resize 32x32 %SOURCE3 %buildroot%_niconsdir/%name.png
convert -resize 16x16 %SOURCE3 %buildroot%_miconsdir/%name.png

%files
%dir %_datadir/qcheckers
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/qcheckers
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Thu May 07 2020 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Thu Nov 08 2012 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial build for ALT Linux
