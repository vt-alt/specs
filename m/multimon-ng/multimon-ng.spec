Name:     multimon-ng
Version:  1.1.7
Release:  alt2

Summary:  A fork of multimon that decodes multiple digital transmission modes
License:  GPL-2.0
Group:    Engineering
Url:      https://github.com/EliasOenal/multimon-ng

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(x11)

Requires: sox

%description
MultimonNG a fork of multimon. It decodes the following digital transmission modes:
* POCSAG512 POCSAG1200 POCSAG2400
* EAS
* UFSK1200 CLIPFSK AFSK1200 AFSK2400 AFSK2400_2 AFSK2400_3
* HAPN4800
* FSK9600
* DTMF
* ZVEI1 ZVEI2 ZVEI3 DZVEI PZVEI
* EEA EIA CCIR
* MORSE CW
* FLEX

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc COPYING README.md
%_bindir/*

%changelog
* Fri May 17 2019 Anton Midyukov <antohami@altlinux.org> 1.1.7-alt2
- Requires: sox

* Tue May 14 2019 Anton Midyukov <antohami@altlinux.org> 1.1.7-alt1
- Initial build for Sisyphus
