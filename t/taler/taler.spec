Name:		taler
Version:	0.15.0.1
Release:	alt5
Summary:	Taler - first Belarus cryptocurrency
Url:		https://taler.site/
Group:		Office
License:	MIT
Source0:	%name.tar.xz

Source1:	%name.png
Source2:	%name.desktop

Patch1: taler-0.15.0.1-alt-boost-compat.patch
Patch2: taler-0.15.0.1-alt-boost-compat-2.patch
Patch3: taler-0.15.0.1-alt-boost-1.73.0-compat.patch
Patch4: taler-0.15.0.1-alt-qt-5.15-compat.patch

BuildRequires: boost-devel-static boost-interprocess-devel git-core libdb4.8_cxx-devel
BuildRequires: libevent-devel libminiupnpc-devel libprotobuf-devel libqrencode-devel
BuildRequires: libssl-devel libstdc++-devel-static libzeromq-devel protobuf-compiler
BuildRequires: qt5-base-devel qt5-tools

BuildRequires: /usr/bin/convert

%description
Taler is an experimental digital currency that enables instant payments to anyone,
anywhere in the world. Taler uses peer-to-peer technology to operate with no central
authority: managing transactions and issuing money are carried out collectively by
the network. Taler Core is the name of open source software which enables the use of
this currency.

For more information, as well as an immediately useable, binary version of the Taler
Core software, see https://taler.site.

%prep
%setup -n %name
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2

%build
%add_optflags -std=c++11
NOCONFIGURE=1 ./autogen.sh
autoreconf -fisv
%configure --libdir=%_libdir/%name --with-gui=qt5 --enable-static=no
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
%_man1dir/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.0.1-alt5
- Rebuilt with boost-1.74.0.

* Thu Jun 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.0.1-alt4
- Rebuilt with boost-1.73.0.

* Fri Apr 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.0.1-alt3
- Rebuilt with boost-1.72.0.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.15.0.1-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.0.1-alt2
- NMU: rebuilt with boost-1.67.0.

* Wed Feb 07 2018 Motsyo Gennadi <drool@altlinux.ru> 0.15.0.1-alt1
- initial build for ALT Linux
