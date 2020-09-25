Name:		currencyconverter

Summary:	Currency converter
Summary(ru_RU.UTF8): Конвертер валют
Summary(uk_UA.UTF8): Конвертор валют

Version:	1.0.0
Release:	alt1
License:	GPLv3+
Group:		Office
Url:		https://bitbucket.org/admsasha/currencyconverter

Source0:	%name-%version.tar.xz
Source1:	currencyconverter_uk_UA.ts

BuildRequires: libssl-devel qt5-tools-devel

%description
Converter currency exchange rates

%description -l ru_RU.UTF8
Конвертер курсов валют

%description -l uk_UA.UTF8
Конвертор курсів валют

%prep
%setup
subst 's|Office;Finance|Qt;Office;Finance|g' ./pkg/%name.desktop

%build
cp -a %SOURCE1 ./langs/currencyconverter_uk_UA.ts
lrelease-qt5 ./CurrencyConverter.pro
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" CurrencyConverter.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%doc README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Thu Sep 10 2020 Motsyo Gennadi <drool@altlinux.ru> 1.0.0-alt1
- initial build
