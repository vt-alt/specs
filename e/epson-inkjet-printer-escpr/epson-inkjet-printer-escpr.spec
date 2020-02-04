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

%define pkg     epson-inkjet-printer-escpr
%define ver     1.7.7
%define rel     1

# used in RPM macro set for the LSB Driver Development Kit
%define drivername      epson-inkjet-printer-escpr
%define driverstr       epson-inkjet-printer-escpr
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
License: GPL-2.0+
URL: http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX
# Open URL http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX&productName=ET-2750 and push button with magnifier
Group: System/Configuration/Hardware
Summary: Epson Inkjet Printer Driver (ESC/P-R) for Linux

Source0: %{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM bug_x86_64.patch -- fix a segfault on x64_64 (probably manifested with GCC7 use)
# https://aur.archlinux.org/cgit/aur.git/plain/bug_x86_64.patch?h=epson-inkjet-printer-escpr
Patch0:  bug_x86_64.patch

BuildRequires: libcups-devel

%description
This software is a filter program used with Common UNIX Printing
System (CUPS) from the Linux. This can supply the high quality print
with Seiko Epson Color Ink Jet Printers.

This product supports only EPSON ESC/P-R printers. This package can be
used for all EPSON ESC/P-R printers.

For detail list of supported printer, please refer to below site:
http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

# Packaging settings
%prep
%setup -q
%patch0 -p1

%build
%undefine _configure_gettext
%autoreconf
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
%_libdir/libescpr.so*
%_libexecdir/cups/filter/epson-escpr*
%_datadir/cups/model/%name

%changelog
* Wed Jan 29 2020 Andrey Cherepanov <cas@altlinux.org> 1.7.7-alt1
- New version.
- Supported new models:
 + Epson ET-M2120 Series

* Tue Dec 03 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.6-alt1
- New version.
- Supported new models:
  + Epson EC-C110 Series

* Wed Nov 06 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1
- New version.
- Supported new models:
  + Epson M2110 Series
  + Epson M2120 Series

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt1
- New version.
- Supported new models:
  + Epson EP-M552T Series

* Wed Sep 04 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.3-alt1
- New version.
- Supported new models:
  + Epson WF-2810 Series

* Fri Aug 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.2-alt1
- New version.
- Supported new models:
  + Epson EP-712A Series
  + Epson EP-812A Series
  + Epson EW-052A Series
  + Epson WF-110 Series
  + Epson XP-3100 Series

* Tue May 14 2019 Andrey Cherepanov <cas@altlinux.org> 1.6.41-alt1
- New version.
- Supported new models:
  + Epson PX-S06 Series
  + Epson WF-2830 Series
  + Epson WF-2850 Series

* Thu Apr 25 2019 Andrey Cherepanov <cas@altlinux.org> 1.6.40-alt1
- New version.
- Supported new models:
  + XP-2100 Series

* Mon Apr 22 2019 Andrey Cherepanov <cas@altlinux.org> 1.6.39-alt1
- New version.
- Supported new models:
  + XP-4100 Series

* Mon Apr 15 2019 Andrey Cherepanov <cas@altlinux.org> 1.6.38-alt1
- New version.
- Supported new models:
  + ET-2760 Series

* Tue Apr 02 2019 Andrey Cherepanov <cas@altlinux.org> 1.6.37-alt1
- New version.
- Supported new models:
  + ET-2720 Series
  + L3160 Series

* Fri Feb 15 2019 Andrey Cherepanov <cas@altlinux.org> 1.6.35-alt1
- New version.
- Supported new models:
  + ST-2000 Series

* Wed Jan 30 2019 Andrey Cherepanov <cas@altlinux.org> 1.6.34-alt1
- New version.
  - Supported new models:
    + ET-1110 Series

* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.33-alt1
- New version.
  - Supported new models:
    + ET-4700 Series
    + L1110 Series

* Mon Oct 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.32-alt1
- New version.
  * Supported new models:
    + L5190 Series
    + L7180 Series
    + PX-S170T Series
    + PX-S170UT Series

* Fri Sep 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.29-alt1
- New version.
  * Supported new models:
    + EP-711A_Series
    + EP-811A_Series
    + ET-2710_Series
    + ET-M1100_Series
    + ET-M1120_Series
    + EW-M770T_Series
    + L3100_Series
    + L3110_Series
    + L3150_Series
    + L7160_Series
    + M1100_Series
    + M1120_Series
    + XP-7100_Series
- Fix a segfault on x64_64.
- Compress all ppds.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.20-alt2
- Increate release number to fix conflict with autoimports.

* Thu Jun 07 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.20-alt1
- Initial build in Sisyphus (imported from epson-inkjet-printer-escpr-1.6.20-1lsb3.2.src.rpm)
