Name:		transgui
Version:	5.18.0
Release:	alt3

Summary:	An App to remotely control a Transmission Bit-Torrent client
Summary(ru_RU.UTF8): Приложение для удаленного управления Бит-торрент-клиентом Transmission
Summary(uk_UA.UTF8): Додаток для віддаленого керування Біт-торрент-клієнтом Transmission
Group:		Networking/File transfer
License:	GPLv2

Url:		https://github.com/transmission-remote-gui/transgui

# https://github.com/transmission-remote-gui/transgui.git
Source:	%name-%version.tar
Source1:	%name.desktop
Source2:	%name.1

Patch0:		%name-5.18.0_Duplicate_object_member_status.diff

BuildRequires(pre): rpm-build-ubt
BuildRequires: /usr/bin/convert lazarus

ExclusiveArch: %ix86 x86_64

%add_findreq_skiplist %_datadir/%name/lang/%name.pl

%description
Transmission Remote GUI is a feature rich cross platform front-end to remotely control
a Transmission Bit-Torrent client daemon via its RPC protocol. Transmission Remote GUI
is faster and has more functionality than the built-in Transmission web interface.

%description -l ru_RU.UTF8
Transmission Remote GUI является многофункциональным кроссплатформенныйм интерфейсом для
дистанционного управления демоном Бит-торрент-клиента Transmission через его RPC-протокол.
Transmission Remote GUI быстрее и имеет больше возможностей, чем встроенный веб-интерфейс
Transmission.

%description -l uk_UA.UTF8
Transmission Remote GUI є багатофункціональним багатоплатформовим інтерфейсом для дистанційного
керування демоном Біт-торрент-клієнта Transmission через його RPC-протокол. Transmission Remote
GUI швидше і має більше можливостей, ніж вбудований веб-інтерфейс Transmission.

%prep
%setup
%patch0 -p1

%build
lazbuild -B transgui.lpi
%make_build \
	UNIXHier=1 \
	PREFIX=%_prefix

%install
%make install \
	UNIXHier=1 \
	PREFIX=%_prefix \
	INSTALL_PREFIX=%buildroot%_prefix

install -Dp -m 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -Dp -m 644 %SOURCE2 %buildroot%_man1dir/%name.1

# Icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 %name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 %name.png %buildroot%_miconsdir/%name.png

# Lang
mkdir -p %buildroot%_datadir/%name
cp -a lang %buildroot%_datadir/%name/
rm -f %buildroot%_datadir/%name/lang/transgui.template

%files
%dir %_datadir/%name
%doc README.md LICENSE rpc-spec.txt VERSION.txt
%_bindir/*
%_desktopdir/%name.desktop
%_man1dir/%name.*
%_iconsdir/hicolor/*/apps/*
%_datadir/%name/lang

%changelog
* Mon Mar 08 2021 Motsyo Gennadi <drool@altlinux.ru> 5.18.0-alt3
- fix error 'Duplicate object member: "status"'
  https://github.com/transmission-remote-gui/transgui/issues/1325

* Tue May 05 2020 Motsyo Gennadi <drool@altlinux.ru> 5.18.0-alt2
- ExclusiveArch %ix86 x86_64 only (lazarus)

* Tue May 05 2020 Motsyo Gennadi <drool@altlinux.ru> 5.18.0-alt1
- 5.18.0

* Sat Apr 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.15.4-alt1.S1
- Updated to upstream version 5.15.4.

* Sun Jan 12 2014 Motsyo Gennadi <drool@altlinux.ru> 5.0.1-alt3
- fix interception of links
- cleanup spec-file

* Sun Jan 05 2014 Motsyo Gennadi <drool@altlinux.ru> 5.0.1-alt2
- add mime-types support
- remove sh-script for old version

* Sun Jan 05 2014 Motsyo Gennadi <drool@altlinux.ru> 5.0.1-alt1
- 5.0.1

* Wed Nov 14 2012 Motsyo Gennadi <drool@altlinux.ru> 4.1-alt1
- 4.1

* Mon Oct 15 2012 Motsyo Gennadi <drool@altlinux.ru> 4.0.3-alt1
- initial build for ALT Linux
