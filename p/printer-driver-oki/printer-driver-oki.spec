Name:     printer-driver-oki
Version:  1.0.1
Release:  alt1

Summary:  OKI Data printer drivers for Linux
License:  GPL-2.0
Group:    Other
Url:      https://github.com/rbalint/printer-driver-oki
BuildArch: noarch

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

#BuildRequires:

%description
Oki Data printer drivers for Linux, downloaded from ftp://ftp2.okidata.com/pub/drivers/linux/

Supported Models:

* OKI 24 Pin
* OKI 9 Pin
* OKI B2200 / B2400 PCL
* OKI B4000 / B400 / MB400 PCL
* OKI B4000 / B400 / MB400 PS
* OKI B6250 / B6500
* OKI B6300
* OKI B710 / B720 / B730
* OKI B930
* OKI C330 / C530
* OKI C3600
* OKI C5550 MFP / MC560 MFP / CX2032 MFP / CX2033 MFP
* OKI C6050 / C6150
* OKI C610 / C710 / C711
* OKI C830 / MC860 MFP / CX2633 MFP
* OKI C910 / C9600 / C9650
* OKI MB471 MFP / MB491 MFP
* OKI MC361 MFP / MC561 MFP / CX2731 MFP

%prep
%setup

%build
%make_build

%install
install -d %buildroot%_libexecdir/cups/filter
%makeinstall_std PREFIX=%_prefix

%files
%doc README
%_libexecdir/cups/filter/*
%_datadir/ppd/okidata

%changelog
* Tue Oct 20 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
