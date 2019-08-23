Name: QtBitcoinTrader
Version: 1.40.42
Release: alt1
Summary: Bitcoin Secure Trading Client for most popular Bitcoin exchanges
Url: http://sourceforge.net/projects/bitcointrader/
Group: Office
License: GPLv3
Source0: BitcoinTraderQtSRC_v%{version}.zip

# Automatically added by buildreq on Wed Sep 16 2015 (-bi)
# optimized out: elfutils fontconfig libGL-devel libcom_err-devel libkrb5-devel libqt5-core libqt5-gui libqt5-multimedia libqt5-network libqt5-script libqt5-widgets libstdc++-devel python-base python3 python3-base qt5-base-devel qt5-declarative-devel
BuildRequires: ImageMagick-tools gcc-c++ libssl-devel qt5-multimedia-devel qt5-script-devel qt5-svg-devel unzip zlib-devel

%description
Qt Bitcoin Trader
Secure Trading Client for most popular Bitcoin exchanges.
This software helps you open and cancel orders very fast.
Real time data monitoring.

%prep
%setup -n BitcoinTraderQtSRC_v%{version}

%build
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" QtBitcoinTrader_Desktop.pro
%make_build

%install
install -Dp -m 0755 %name %buildroot%_bindir/%name
install -Dp -m 0644 %name.desktop %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
install -m 0644 %name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 %name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 %name.png %buildroot%_miconsdir/%name.png

%files
%doc README.md
%_bindir/*
%_desktopdir/*
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

%changelog
* Fri Aug 23 2019 Motsyo Gennadi <drool@altlinux.ru> 1.40.42-alt1
- 1.40.42

* Sun Apr 14 2019 Motsyo Gennadi <drool@altlinux.ru> 1.40.41-alt1
- 1.40.41

* Sat Jan 26 2019 Motsyo Gennadi <drool@altlinux.ru> 1.40.40-alt1
- 1.40.40

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.40.13-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Apr 13 2018 Motsyo Gennadi <drool@altlinux.ru> 1.40.13-alt1
- 1.40.13

* Fri Sep 22 2017 Motsyo Gennadi <drool@altlinux.ru> 1.40.09-alt1
- 1.40.09

* Sun Sep 17 2017 Motsyo Gennadi <drool@altlinux.ru> 1.40.08-alt1
- 1.40.08

* Sun Sep 10 2017 Motsyo Gennadi <drool@altlinux.ru> 1.40.07-alt1
- 1.40.07

* Mon Jul 17 2017 Motsyo Gennadi <drool@altlinux.ru> 1.40.03-alt1
- 1.40.03

* Wed Sep 16 2015 Motsyo Gennadi <drool@altlinux.ru> 1.10.01-alt1
- 1.10.01

* Sat Apr 26 2014 Motsyo Gennadi <drool@altlinux.ru> 1.07.98-alt1
- v1.07.98 Beta

* Tue Dec 31 2013 Motsyo Gennadi <drool@altlinux.ru> 1.07.96.4-alt1
- v1.07.96.4 Beta

* Tue Sep 10 2013 Motsyo Gennadi <drool@altlinux.ru> 1.07.74-alt1
- v1.07.74 Beta testing
- BTC-e FTC and History FIX

* Tue Jul 02 2013 Motsyo Gennadi <drool@altlinux.ru> 1.06-alt1
- 1.06

* Mon Jun 24 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Jun 17 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Thu Jun 06 2013 Motsyo Gennadi <drool@altlinux.ru> 0.99-alt1
- 0.99

* Mon Jun 03 2013 Motsyo Gennadi <drool@altlinux.ru> 0.98-alt1
- 0.98

* Tue May 28 2013 Motsyo Gennadi <drool@altlinux.ru> 0.96-alt1
- 0.96

* Fri May 24 2013 Motsyo Gennadi <drool@altlinux.ru> 0.94-alt1
- 0.94

* Sat May 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.93-alt2
- fixed rules

* Sat May 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.93-alt1
- 0.93

* Fri May 17 2013 Motsyo Gennadi <drool@altlinux.ru> 0.90-alt1
- 0.90

* Tue May 14 2013 Motsyo Gennadi <drool@altlinux.ru> 0.87-alt1
- initial build for ALT Linux
