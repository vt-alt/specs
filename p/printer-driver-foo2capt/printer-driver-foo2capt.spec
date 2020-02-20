Name: printer-driver-foo2capt
Version: 0.1.0
Release: alt1.git94b2bf2

Source: %name-%version.tar

Summary: Driver for Canon CAPT printers
URL: https://github.com/agalakhov/captdriver
License: GPL-3.0-or-later
Group: System/Configuration/Printing

BuildRequires: libcups-devel

%description
This is a driver for Canon CAPT-based printers (LBP-***)
based on several reverse engineering attempts. This is
currently in an early alpha stage. Use at your own risk.

Compatible printers:
Canon LBP-2900
Canon LBP-2900B
Canon LBP-3000

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
install -d %buildroot%_libexecdir/cups/filter
install -d %buildroot%_datadir/ppd/foo2capt

install -m0755 src/rastertocapt %buildroot%_libexecdir/cups/filter/
install -m644 Canon-LBP-2900.ppd %buildroot%_datadir/ppd/foo2capt/

%files
%_datadir/ppd/foo2capt/Canon-LBP-2900.ppd
%_libexecdir/cups/filter/rastertocapt

%changelog
* Fri Nov 1 2019 Grigory Maksimov <zacat@altlinux.org> 0.1.0-alt1.git94b2bf2
- Initial build for ALT
