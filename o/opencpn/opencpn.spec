%define _unpackaged_files_terminate_build 1

Name: opencpn
Version: 5.0.0
Release: alt2
Summary: A free and open source software for marine navigation

Group: Other
License: %gpl2only
Url: http://opencpn.org
Source0: OpenCPN-%version.tar.gz
Source1: %name.desktop

ExcludeArch: ppc64le

Patch1: opencpn-4.4.0-fix_library_path.patch

Requires: %name-data

#Errara
#Patch100:

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Mon Mar 25 2013
# optimized out: cmake-modules fontconfig fontconfig-devel glib2-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
BuildRequires: bzlib-devel cmake gcc-c++ libGLU-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel zlib-devel

BuildRequires: compat-libwxGTK3.1-gtk2-devel libgtk+2-devel
Requires: libgtk2-engine-adwaita

BuildRequires: tinyxml-devel libgps-devel libportaudio2-devel libcurl-devel libexpat-devel
BuildRequires: liblz4-devel liblzma-devel libsndfile-devel libarchive-devel libelf-devel
BuildRequires: libexif-devel libwxsvg-devel libsqlite3-devel

# use bundled wxcurl: none in Sisyphus 20190327
# use bundled unarr : none in Sisyphus 20190327

%description
OpenCPN is a free software (GPLv2) project to create a concise chart plotter
and navigation software, for use underway or as a planning tool. OpenCPN is
developed by a team of active sailors using real world conditions for program
testing and refinement.

%package data
Summary: Architecture independent files for OpenCPN
Group: Other
BuildArch: noarch

%description data
Architecture independent files for OpenCPN.

%prep
%setup -n OpenCPN-%version
#patch1 -p2

#patch100 -p1

#rm -f src/tinyxml*.cpp include/tinyxml.h
#rm -rf plugins/grib_pi/src/zlib-1.2.3
#rm -rf plugins/grib_pi/src/bzip2

# https://lists.altlinux.org/pipermail/devel/2019-March/207515.html
sed -i 's/\(SET .LIB_INSTALL_DIR "lib64".\)/# \1/' CMakeLists.txt

%build
%add_optflags %(pkg-config --cflags pango)
%cmake -DBUNDLE_DOCS=1 -DBUNDLE_TCDATA=1 -DBUNDLE_GSHHS=1
cd BUILD
make

%install
cd BUILD
make install DESTDIR=%buildroot
cp -f %SOURCE1 %buildroot%_datadir/applications

# It is copied from %%_builddir by %%doc macro, so removed from %%buildroot
# /usr/share/doc/opencpn/changelog
# /usr/share/doc/opencpn/copyright
rm -rf %buildroot/%_datadir/doc

%find_lang %name
%find_lang --append --output=%name.lang %name-dashboard_pi
%find_lang --append --output=%name.lang %name-grib_pi
%find_lang --append --output=%name.lang %name-wmm_pi
%find_lang --append --output=%name.lang %name-chartdldr_pi

%files
%doc data/license.txt
%doc data/copyright
%doc data/changelog

%_bindir/opencpn

# https://lists.altlinux.org/pipermail/devel/2019-March/207515.html
%dir %_usr/lib/%name
%_usr/lib/opencpn/*_pi.so

%files data -f BUILD/%name.lang
%doc data/doc/*
%_man1dir/opencpn.*

%_datadir/appdata/opencpn.appdata.xml

%dir %_datadir/%name
%dir %_datadir/%name/sounds
#dir %_datadir/%name/gshhs
#dir %_datadir/%name/tcdata
%dir %_datadir/%name/s57data
%dir %_datadir/%name/uidata
%dir %_datadir/%name/plugins

%_datadir/%name/sounds/*
#{_datadir}/%name/gshhs/*
#{_datadir}/%name/tcdata/*
%_datadir/%name/s57data/*
%_datadir/%name/uidata/*
%_datadir/%name/plugins/*

%dir %_datadir/%name/doc
%_datadir/%name/doc/help_web.html

%_datadir/%name/opencpn.png

%_iconsdir/hicolor/64x64/apps/*
%_iconsdir/hicolor/48x48/apps/*
%_iconsdir/hicolor/scalable/apps/*
%_datadir/applications/%name.desktop

%_datadir/%name/COPYING.gplv2
%_datadir/%name/COPYING.gplv3
%_datadir/%name/COPYING.lgplv2
%_datadir/%name/COPYING.lgplv3
%_datadir/%name/CoC-909_2013-InlandECDIS_20170308s.pdf
%_datadir/%name/LICENSING
%_datadir/%name/LINUX_DEVICES.md
%_datadir/%name/authors.html
%_datadir/%name/license.html

%changelog
* Tue Aug 20 2019 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt2
- add_optflags (pkg-config --cflags pango) (Fix FTBFS)
- ExcludeArch: ppc64le

* Thu Mar 28 2019 Sergey Y. Afonin <asy@altlinux.ru> 5.0.0-alt1
- New version (thanx to TEAM)
- Built with wxGTK3.1
- Added some system libraries for building (ALT #36402)
- Disabled opencpn-4.4.0-fix_library_path.patch

* Wed Aug 22 2018 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt2
- Fix library path.
- Little cleanup spec.
- Fix bogus date in changelog.

* Thu Dec 01 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.4.0-alt1
- New version

* Sun Feb 16 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.2.2-alt1
- New version
- Moved architecture-independent data to noarch subpackage %name-data

* Wed Apr 03 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.2.0-alt1
- Initial build for ALT Linux

* Sat Sep 22 2012 Eric 'Sparks' Christensen <sparks@fedoraproject.org> - 3.0.2-1
- Initial package.
