Name:		beebeep
Summary:	Secure Network Chat
Version:	5.8.2
Release:	alt0.1.p9
Group:		Networking/Chat

Url:		http://sourceforge.net/projects/beebeep/
Source0:	%name-code-%version.tar.bz2
Source1:	%name.desktop
License:	GPLv3+

BuildRequires: /usr/bin/convert qt5-multimedia-devel qt5-tools-devel qt5-webkit-devel qt5-webview-devel qt5-x11extras-devel

%description
BeeBEEP is a secure network chat. You can talk and send files with all your
friends inside a local area network such of an office, home or internet cafe
without a server.

%prep
%setup -n %name-code-r1352

%build
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" -recursive -o Makefile beebeep-desktop.pro
%make_build

%install
mkdir -p %buildroot%_bindir
mv test/%name %buildroot%_bindir/%name
mkdir -p %buildroot%_libdir
cp -a test/* %buildroot%_libdir
mkdir -p %buildroot%_datadir/%name
cp -a ./locale/*.qm %buildroot%_datadir/%name
cp -a ./misc/*.wav %buildroot%_datadir/%name
install -Dp -m 0644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop

# Icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 src/images/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 src/images/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 src/images/%name.png %buildroot%_miconsdir/%name.png

%files
%doc *.txt
%dir %_datadir/%name
%_bindir/%name
%_libdir/lib*
%_datadir/%name/*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Fri Nov 27 2020 Motsyo Gennadi <drool@altlinux.ru> 5.8.2-alt0.1.p9
- build for p9

* Thu Nov 26 2020 Motsyo Gennadi <drool@altlinux.ru> 5.8.2-alt1
- initial build for ALT Linux
