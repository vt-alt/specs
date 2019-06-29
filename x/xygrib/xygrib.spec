%define binname XyGrib

Name: xygrib
Version: 1.2.4
Release: alt1

Summary: Visualisation of meteo data from files in GRIB formats

License: %gpl3only
Group: Networking/Other
Url: https://opengribs.org
Source0: %binname-%version.tar.gz
Source1: %binname.desktop

Requires: fonts-ttf-liberation
Requires: %name-data = %version-%release

BuildRequires(pre): rpm-build-licenses

BuildRequires: cmake qt5-base-devel qt5-tools-devel libpng-devel libopenjpeg2.0-devel libnova-devel libproj-devel zlib-devel bzlib-devel

%description
Visualization of meteo data from files in GRIB formats v1 and v2.
GRIB data are used to display weather data in detailed format for
a certain area of sea or land. XyGrib is a fork of zyGrib 8.0.1.

%package data
Summary: Architecture independent files for XyGrib.
Group: Networking/Other
BuildArch: noarch

%description data
Architecture independent files for XyGrib.

Included low resolution maps for XyGrib (25 km, 5 km and 1 km)
and cities with population from 3000 to 10000 and more 10000.

data/gis/* have another license: %ccby30
home page: http://www.geonames.org/

%prep

%setup -q -n %binname-%version

%build
# -DNO_UPDATE=1 deactivates XyGrib internal SW update
%cmake \
    -DCMAKE_INSTALL_PREFIX=%_datadir/openGribs \
    -DCMAKE_CXX_FLAGS="%optflags -DNO_UPDATE=1"

cd BUILD
make

%install
cd BUILD
make install DESTDIR=%buildroot

mkdir %buildroot/%_bindir
mv %buildroot/%_datadir/openGribs/XyGrib/%binname %buildroot/%_bindir/%binname

mkdir -p -m 755 %buildroot/%_datadir/pixmaps
cp %buildroot/%_datadir/openGribs/XyGrib/data/img/xyGrib_32.xpm %buildroot/%_datadir/pixmaps
mkdir -p -m 755 %buildroot/%_datadir/applications
install -m 644 %SOURCE1 %buildroot/%_datadir/applications

%files
%doc README.md LICENSE
%_bindir/%binname
%_datadir/pixmaps/*
%_datadir/applications/%binname.desktop

%files data
%_datadir/openGribs

%changelog
* Fri Jun 28 2019 Sergey Y. Afonin <asy@altlinux.ru> 1.2.4-alt1
- Initial build for AltLinux
