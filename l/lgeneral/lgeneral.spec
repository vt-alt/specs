#define unpack tar
Name: lgeneral
Summary: Turn-based strategy inspired by Panzer General
Version: 1.4.3
Release: alt1
License: GPL-2.0-or-later
Group: Games/Strategy
Url: http://lgames.sf.net

Source: %name-%version.tar.gz
Source2: %name.NOTES.ALT
Source3: scenarios.tar.bz2
Source4: nicolas.zip
Source5: newcampaign.zip
Source6: APP-6A.zip
Patch0: lgeneral-1.4.3-alt-gettext.patch
Patch1: lgeneral-1.4.3-alt-link.patch

Obsoletes: pg-data

BuildRequires: libSDL-devel libSDL_mixer-devel unzip

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer General.
Original data files can be downloaed from http://lgames.sourceforge.net/index.php?project=LGeneral

%prep
%setup
%patch0 -p2
%patch1 -p2

touch config.rpath

%build
%autoreconf
%configure \
	--disable-rpath \
	--with-libintl-prefix=%prefix

%make_build

%install
mkdir -p %buildroot%_datadir/%name/pg-data
%make_install install DESTDIR="%buildroot"
tar xvfj %SOURCE3
mv scenarios/* %buildroot%_datadir/%name/scenarios/
unzip %SOURCE4
cp -pr nicolas/* %buildroot%_datadir/%name/
unzip %SOURCE5
cp -pr  NewCampaign/* %buildroot%_datadir/%name/
unzip %SOURCE6 -d APP
cp -pr APP/* %buildroot%_datadir/%name/

cp %SOURCE2 %buildroot%_datadir/%name/NOTES.ALT

%find_lang %name pg --output=%name.lang

%files -f %name.lang
%_bindir/*
%_datadir/%name/*
%_iconsdir/hicolor/*/*/*
%_desktopdir/*
%_man1dir/lgc-pg.*
%_man6dir/lgeneral.*

%changelog
* Tue May 05 2020 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt1
- New version 1.4.3
- Cleanup spec

* Tue Jul 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt5.2
- Fix build with new toolchain

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt5.1
- Built with external gettext

* Wed Dec 10 2008 Mikhail Pokidko <pma@altlinux.org> 1.2-alt5
- fixed build for x86_64

* Wed Dec 10 2008 Mikhail Pokidko <pma@altlinux.org> 1.2-alt4
- fixed NATO mod path

* Wed Dec 10 2008 Mikhail Pokidko <pma@altlinux.org> 1.2-alt3
- beta13 version. 
 + Added NATO mod.

* Tue Aug 28 2007 Pokidko Mikhail <pma@altlinux.org> 1.2-alt2
- Additional scenarios and 2 campains packed.
  Original data files can be downloaed from http://lgames.sourceforge.net/index.php?project=LGeneral

* Tue Mar 13 2007 Mikhail Pokidko <pma@altlinux.ru> 1.2-alt1
- initial ALT build

