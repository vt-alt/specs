%define msxver 0.3.1
%define sfxver 0.2.3
Name: openttd-3rd-party
Version: 0.6.0
Release: alt1

Summary: 3rd Party data files for openttd
License: GPLv2
Group: Games/Strategy
URL: http://www.openttd.com/
Requires: openttd-data >= 1.5.0
Packager: Anton Farygin <rider@altlinux.com>
Buildarch: noarch

Source: opengfx-%version.tar
Source1: openmsx-%msxver-all.zip
Source2: opensfx-%sfxver-all.zip

BuildRequires: unzip


%description
3rd Party data files for openttd

%prep
%setup -q -n opengfx-%version

%build
unzip %SOURCE1
unzip %SOURCE2

%install
mkdir -p %buildroot%_prefix/games
mkdir -p %buildroot%_datadir/games/openttd/gm
mkdir -p %buildroot%_datadir/games/openttd/data
cp *.grf *.obg opensfx-%sfxver/opensfx.* %buildroot%_datadir/games/openttd/data/
cp openmsx-%msxver/*.{mid,obm} %buildroot%_datadir/games/openttd/gm

%files
%_datadir/games/openttd/data/*
%_datadir/games/openttd/gm/*


%changelog
* Mon Apr 06 2020 Anton Farygin <rider@altlinux.ru> 0.6.0-alt1
- new version 

* Wed Apr 03 2019 Anton Farygin <rider@altlinux.ru> 0.5.5-alt1
- new version

* Fri May 05 2017 Anton Farygin <rider@altlinux.ru> 0.5.4-alt1
- new version

* Tue Apr 07 2015 Anton Farygin <rider@altlinux.ru> 0.5.2-alt1
- updated to RC1 release for new version of openttd

* Tue Jun 24 2014 Anton Farygin <rider@altlinux.ru> 0.5.1-alt1
- new version

* Thu Apr 10 2014 Anton Farygin <rider@altlinux.ru> 0.5.0-alt1
- new version

* Tue Jun 25 2013 Anton Farygin <rider@altlinux.ru> 0.4.7-alt1
- new version

* Fri Jul 20 2012 Anton Farygin <rider@altlinux.ru> 0.4.4-alt1
- new version

* Tue Aug 31 2010 Anton Farygin <rider@altlinux.ru> 0.2.4-alt2
- updated openmsx to 0.3.1

* Thu Jun 17 2010 Anton Farygin <rider@altlinux.ru> 0.2.4-alt1
- first build for Sisyphus
