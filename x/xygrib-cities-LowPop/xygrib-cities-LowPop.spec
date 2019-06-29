Name: xygrib-cities-LowPop
Version: 0.1
Release: alt1

Summary: Additional cities lists for XyGrib (with low population).

License: %ccby30
Group: Networking/Other
Url: https://www.opengribs.org/en/downloads
Source0: cities_0-300.txt.gz
Source1: cities_300-1k.txt.gz
Source2: cities_1k-3k.txt.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: xygrib-data

%description
This package contain additional cities lists with population < 3000
cities_1k-3k.txt.gz  1000 <= population < 3000 32394 cities
cities_300-1k.txt.gz  300 <= population < 1000 35458 cities
cities_0-300.txt.gz          population < 300  37729 cities

Warning: loading a lot of cities can slow the program start.

Data extracted from the database GeoNames: http://www.geonames.org/

%prep

%build

%install

%__mkdir_p %buildroot/%_datadir/openGribs/XyGrib/data/gis
cp %SOURCE0 %buildroot/%_datadir/openGribs/XyGrib/data/gis
cp %SOURCE1 %buildroot/%_datadir/openGribs/XyGrib/data/gis
cp %SOURCE2 %buildroot/%_datadir/openGribs/XyGrib/data/gis

%files
%_datadir/openGribs/XyGrib/data/gis/*

%changelog
* Fri Jun 28 2019 Sergey Y. Afonin <asy@altlinux.ru> 0.1-alt1
- Initial build for AltLinux
