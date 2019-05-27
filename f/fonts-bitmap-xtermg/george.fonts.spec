%define cname xtermg

Name: fonts-bitmap-%cname
Version: 3.1
Release: alt1
Summary: XTermG fonts - a fixed width English/Cyrillic fonts with some additional characters
License: Free
Group: System/Fonts/X11 bitmap
BuildArch: noarch

Source0: %name-%version.tar.gz

BuildPreReq: rpm-build-fonts

# Automatically added by buildreq on Wed Apr 04 2018
BuildRequires: bdftopcf python3-dev python3-module-tpg

%description
XTermG fonts is an English/Cyrillic (ISO10646-1 and KOI7/8)
fixed size font familly with some commonly useful characters added.
Sizes: 12x20 12x20 8x14 8x16 8x16 8x8

# TODO package -n fonts-console-%cname

%prep
%setup -n george.fonts

%build
%make pcf

%install
%bitmap_fonts_install %cname

%files -f %cname.files
%doc TODO

%changelog
* Sat May 25 2019 Fr. Br. George <george@altlinux.ru> 3.1-alt1
- Linedraw endings

* Wed Apr 04 2018 Fr. Br. George <george@altlinux.ru> 3.0-alt1
- ALT build at least


