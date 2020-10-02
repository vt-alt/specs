Name:		sibcoin
Version:	0.16.2.0
Release:	alt3
Summary:	Siberian Chervonets Wallet
Url:		http://sibcoin.org/en/
Group:		Office
License:	MIT
ExclusiveArch: %ix86 x86_64
Source0:	%name.tar.xz

Source1:	%name.png
Source2:	%name.desktop

Patch1: %name-%version-alt-boost-1.73.0-compat.patch
Patch2: %name-%version-alt-qt-5.15-compat.patch

BuildRequires: boost-devel-static boost-interprocess-devel libdb4.8_cxx-devel protobuf-compiler
BuildRequires: libevent-devel libprotobuf-devel libqrencode-devel libssl-devel libzeromq-devel
BuildRequires: qt5-base-devel qt5-tools

BuildRequires: /usr/bin/convert

%description
"Siberian Chervonets" (SIB) is a decentralized payment system, free of useles
intermediaries, control function which performs a public mathematical algorithm.
All calculations are directly from user to user. And users, in turn, form a
distributed network in which information is stored for each transaction, constantly
updating and receiving an acknowledgment from the other participants.

%prep
%setup -n %name
%patch1 -p2
%patch2 -p2

%build
%add_optflags -std=c++11
NOCONFIGURE=1 ./autogen.sh
autoreconf -fisv
%configure --libdir=%_libdir/%name --with-gui=qt5
%make_build

%install
make DESTDIR=%buildroot install
install -Dp -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %SOURCE1 %buildroot%_liconsdir/%name.png
convert -resize 32x32 %SOURCE1 %buildroot%_niconsdir/%name.png
convert -resize 16x16 %SOURCE1 %buildroot%_miconsdir/%name.png

%files
%doc CONTRIBUTING.md COPYING README.md
%dir %_libdir/%name
%_bindir/*
%_libdir/%name/libbitcoinconsensus.so*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.2.0-alt3
- Rebuilt with boost-1.74.0.

* Thu Jun 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.2.0-alt2
- Rebuilt with boost-1.73.0.

* Sun Oct 28 2018 Motsyo Gennadi <drool@altlinux.ru> 0.16.2.0-alt1
- 0.16.2.0

* Thu Sep 27 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.16.1.2-alt2.qa1
- Added ExclusiveArch: %ix86 x86_64.

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.1.2-alt2
- NMU: rebuilt with boost-1.67.0.

* Thu Sep 21 2017 Motsyo Gennadi <drool@altlinux.ru> 0.16.1.2-alt1
- 0.16.1.2

* Thu Aug 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.1.1-alt2
- Rebuilt with updated libdb4.8.

* Fri Jul 07 2017 Motsyo Gennadi <drool@altlinux.ru> 0.16.1.1-alt1
- initial build for ALT Linux
