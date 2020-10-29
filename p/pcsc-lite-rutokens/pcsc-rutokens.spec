%define realname rutokens-driver

%define libpcsclite_usbdropdir %(pkg-config libpcsclite --variable=usbdropdir)

Name: pcsc-lite-rutokens
Version: 1.0.6
Release: alt1
License: LGPL-2.1+
Group: System/Configuration/Hardware
Url: http://www.rutoken.ru/support/download/drivers-for-nix/
Summary: USB IFD Handler for RutokenS

BuildRequires: pkgconfig(libpcsclite) >= 1.3.3
BuildRequires: pkgconfig(libusb)

Provides: %realname ifd-rutokens
Requires: pcsc-lite

# https://github.com/AktivCo/rutokens-driver
Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
./reconf

%configure \
	--disable-static \
	--enable-usbdropdir=%libpcsclite_usbdropdir \
	--enable-udevrules \
	#
LDFLAGS=
%make_build

%install
%makeinstall DESTDIR=%buildroot

%files
%doc AUTHORS COPYING NEWS README
#%%config(noreplace) /etc/udev/rules.d/95-rutokens.rules
%libpcsclite_usbdropdir/ifd-rutokens.bundle

%changelog
* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- New version.

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version.

* Thu Sep 15 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version

* Wed Apr 02 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.3-alt1
- Initial build.
