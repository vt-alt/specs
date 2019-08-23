# lsb.spec.in -- an rpm spec file templete for LSB package
# Epson Inkjet Printer Driver (ESC/P-R) for Linux
# Copyright (C) Seiko Epson Corporation 2014.
#  This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110, USA.

%define pkg     epson-inkjet-printer-escpr2
%define ver     1.1.1
%define rel     1

# used in RPM macro set for the LSB Driver Development Kit
%define drivername      epson-inkjet-printer-escpr2
%define driverstr       epson-inkjet-printer-escpr2
%define distribution    LSB
%define manufacturer    EPSON
%define supplier        %{drivername}
%define lsbver          3.2

%define extraversion    -%{rel}lsb%{lsbver}
%define supplierstr     Seiko Epson Corporation

AutoReqProv: no

Name: %{pkg}
Version: %{ver}
Release: alt1
License: LGPL and SEIKO EPSON CORPORATION SOFTWARE LICENSE AGREEMENT
URL: http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX
# Open http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX&productName=WF-M5799
Group: System/Configuration/Hardware
Summary: Epson Inkjet Printer Driver 2 (ESC/P-R) for Linux

Source0: %name-%version.tar

BuildRequires: libcups-devel

ExclusiveArch: %ix86 x86_64 aarch64

%description
This software is a filter program used with Common UNIX Printing
System (CUPS) from the Linux. This can supply the high quality print
with Seiko Epson Color Ink Jet Printers.

This product supports only EPSON ESC/P-R printers. This package can be
used for all EPSON ESC/P-R printers.

For detail list of supported printer, please refer to below site:
http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

%prep
%setup -q

%build
%undefine _configure_gettext
%configure \
        --disable-static \
        --with-cupsfilterdir=%_libexecdir/cups/filter \
        --with-cupsppddir=%_datadir/cups/model
make pkgdatadir=%_datadir

%install
make install-strip DESTDIR=%buildroot pkgdatadir=%_datadir
# Compress all ppds
gzip -n9 %buildroot%_datadir/cups/model/%name/*.ppd

%files
%doc README README.ja COPYING AUTHORS NEWS
%_libdir/libescpr2.so*
%_libexecdir/cups/filter/epson-escpr*
%_datadir/cups/model/%name

%changelog
* Fri Aug 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.
- Supported new models:
  + Epson EP-882A Series
  + Epson EP-982A3 Series
  + Epson XP-8600 Series
  + Epson XP-970 Series
- Build only for i586, x86_64 and aarch64.

* Thu May 30 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.34-alt1
- New version.
- Supported new models:
  + Epson ST-M1000 Series
  + Epson ST-M3000 Series

* Tue May 14 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.33-alt1
- New version.
- Supported new models:
  + Epson PX-M270FT Series
  + Epson PX-M270T Series
  + Epson PX-M885F
  + Epson PX-S270T Series
  + Epson PX-S885

* Mon Apr 15 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.32-alt1
- New version.
- Supported new models:
  + ET-3710 Series
  + ET-3760 Series
  + ET-4760 Series
  + ET-M1170 Series
  + ET-M2170 Series
  + M1170 Series
  + M2170 Series

* Mon Mar 04 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.30-alt1
- Initial build for Sisyphus.
