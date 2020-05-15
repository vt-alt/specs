%def_without dbus
%define origver 2020.1

Name: FlightGear
Version: %origver
Release: alt1

Summary: open-source flight simulator
License: GPLv2+
Group: Games/Arcade

Url: http://www.flightgear.org
# Source0-url: https://sourceforge.net/projects/flightgear/files/release-%origver/flightgear-%version.tar.bz2
Source0: %name-%version.tar
Source2: FlightGear.menu
Source3: FlightGear-22x22.xpm
Source4: FlightGear-32x32.xpm
Source5: FlightGear-48x48.xpm
Source10: fg-16.png
Source11: fg-32.png
Source12: fg-48.png
Source13: fg-64.png
Source14: fg-128.png
Source15: FlightGear.desktop
Patch1: 0001-check-to-be-sure-that-n-is-not-being-set-as-format-t.patch
Patch2: 0002-make-ShivaVG-and-FGAdminUI-static-libraries.patch
Patch5: 0005-explicitely-link-with-libX11.patch
Patch6: 0006-make-fglauncher-a-static-library.patch

Requires: FlightGear-data = %version
#Requires: fgrun >= 1.6.1

BuildRequires: libsimgear-devel = %version
BuildRequires: libOpenSceneGraph-devel >= 3.4.0
BuildRequires: boost-devel >= 1.44
BuildRequires: plib-devel >= 1.8.5

# TODO: fltk??
BuildRequires: rpm-macros-cmake cmake gcc-c++ imake libalut-devel libfltk-devel libfreeglut-devel libjpeg-devel libpng-devel

BuildRequires: libpng-devel libfltk-devel libudev-devel
BuildPreReq: libXres-devel libXi-devel libXmu-devel
BuildPreReq: libXtst-devel libXcomposite-devel libXcursor-devel
BuildPreReq: libXdamage-devel libXdmcp-devel libXfixes-devel
BuildPreReq: libXft-devel libXinerama-devel libxkbfile-devel
BuildPreReq: libXpm-devel libXrandr-devel libXrender-devel
BuildPreReq: libXScrnSaver-devel libXv-devel libXxf86misc-devel
BuildPreReq: libXxf86vm-devel libXxf86vm-devel libapr1-devel

%if_with dbus
# disables screensaver; requires running messagebus service
BuildRequires: libdbus-devel
Requires: dbus
%endif

%description
FlightGear is a free, open-source, multi-platform, and sophisticated
flight simulator framework for the development and pursuit
of interesting flight simulator ideas.

This package contains the engine; see also fgrun or fgo to start
FlightGear conveniently.

You will also need some experience and probably a tutorial:
http://ericbrasseur.org/flight_simulator_tutorial.html

%prep
%setup
%patch1 -p1
#patch2 -p1
#patch5 -p1
%patch6 -p1

sed -i 's/\r//' docs-mini/AptNavFAQ.FlightGear.html
for ext in Cygwin IRIX Joystick Linux MSVC MSVC8 MacOS SimGear Unix \
	Win32-X autoconf mingw plib src xmlsyntax; do
	rm -f docs-mini/README.$ext
done
for f in docs-mini/README.xmlparticles Thanks; do
	iconv -f iso-8859-1 -t utf-8 -o ${f}.utf8 ${f}
	mv -f ${f}.utf8 ${f}
done

# argh
sed -i 's,/lib/FlightGear,/share/flightgear,' CMakeLists.txt

# TODO: link with external sqlite3?
%ifarch %e2k
# unsupported as of lcc-1.23.21
sed -i 's,-fno-fast-math,,' 3rdparty/sqlite3/CMakeLists.txt
%endif

%build
# FIXME: tests got linking problems with lcc 1.23.20, cf. mcst#3675?
%cmake \
%ifarch %e2k
	-DENABLE_TESTS:BOOL=OFF \
%endif
	%nil
%cmake_build

%install
%cmakeinstall_std

rm -rf %buildroot%_datadir/locale
rm -rf %buildroot%_datadir/bash-completion/ %buildroot%_datadir/zsh/

%files
%_bindir/*
%_mandir/*/*
%_iconsdir/*/*/*/flightgear.*
%_desktopdir/org.flightgear.FlightGear.desktop

%changelog
* Tue May 12 2020 Michael Shigorin <mike@altlinux.org> 2020.1-alt1
- 2020.1

* Sat Oct 12 2019 Michael Shigorin <mike@altlinux.org> 2018.2.2-alt2
- fix build on e2kv4+ with lcc 1.23.20 too

* Thu Jun 21 2018 Vitaly Lipatov <lav@altlinux.ru> 2018.2.2-alt1
- new version (2018.2.2)
- rebuild against OpenSceneGraph 3.4.1

* Thu Sep 07 2017 Michael Shigorin <mike@altlinux.org> 2017.2.1-alt1
- 2017.2.1
  + dropped patch2 along with fgadmin
  + disabled patch5
- E2K: avoid lcc-unsupported option

* Sat Feb 20 2016 Michael Shigorin <mike@altlinux.org> 2016.1.1-alt1
- 2016.1

* Wed Sep 30 2015 Michael Shigorin <mike@altlinux.org> 3.6.0-alt0.1
- 3.6.0-RC
- dropped obsolete patches
- replaced gentoo patches with fedora ones

* Wed Sep 30 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt3
- rebuilt against OpenSceneGraph 3.2.3

* Tue Sep 29 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt2
- rebuilt against current OpenSceneGraph (incl. gcc5 C++11 ABI change)
- added gentoo patches

* Thu Feb 19 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Feb 10 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt0.2
- 3.4.0-RC2

* Wed Oct 22 2014 Michael Shigorin <mike@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Jul 29 2014 Michael Shigorin <mike@altlinux.org> 3.0.0-alt1.2
- rebuilt with OpenSceneGraph 3.2.1

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.1
- Rebuilt with new libfltk

* Sat Feb 22 2014 Michael Shigorin <mike@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Feb 06 2014 Michael Shigorin <mike@altlinux.org> 3.0.0-alt0.3
- 3.0.0-rc3

* Tue Nov 26 2013 Michael Shigorin <mike@altlinux.org> 2.12.1-alt1
- 2.12.1

* Thu Sep 26 2013 Michael Shigorin <mike@altlinux.org> 2.12.0-alt1
- 2.12.0
- patch3 partially applied upstream
- patch4 applied upstream

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10.0-alt2.1
- Rebuilt with new libfltk

* Tue Feb 19 2013 Michael Shigorin <mike@altlinux.org> 2.10.0-alt2
- dropped stale version.h stating it's 2.8.0 still
  (so fgroot data version was being mistreated)
- clarified data version dependency to be strict

* Mon Feb 18 2013 Michael Shigorin <mike@altlinux.org> 2.10.0-alt1
- 2.10.0

* Wed Nov 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.2
- Fixed build

* Thu Sep 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.1
- Rebuilt with libpng15

* Sat Aug 18 2012 Michael Shigorin <mike@altlinux.org> 2.8.0-alt1
- 2.8.0

* Mon Jun 25 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt4
- applied fedora patches for CVE-2012-2090 and CVE-2012-2091

* Sat Mar 31 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt3
- added nice tutorial link

* Wed Mar 28 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt2
- fixed desktop file (stale data prefix, ouch)

* Sat Feb 18 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt1
- 2.6.0
  + cmake build
- disabled fgrun dependency until it's fixed again
  (1.6.1 package is ready but malfunctions)

* Mon Sep 26 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt2
- rebuilt against SimGear built with libOpenSceneGraph-3.0.1
- fixed minimal -data version required
- require fgrun again
- minor spec cleanup

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt1.1
- merged andyc@'s 2.4.0-alt1 and omitted (technical rebuild related,
  nothing special) 2.0.0-alt3

* Sun Sep 11 2011 Andrew Clark <andyc@altlinux.org> 2.4.0-alt1
- version update to 2.4.0-alt1

* Thu Mar 10 2011 Michael Shigorin <mike@altlinux.org> 2.0.0-alt3
- rebuilt with current OpenSceneGraph

* Fri Mar 12 2010 Andrew Clark <andyc@altlinux.org> 2.0.0-alt2
- fgrun removed from requires

* Tue Mar 2 2010 Andrew Clark <andyc@altlinux.org> 2.0.0-alt1
- update to version 2.0.0-alt1

* Fri Feb 5 2010 Andrew Clark <andyc@altlinux.org> 1.9.1-alt3.cvs050210
- update to version 1.9.1-alt3.cvs050210
- fgrun removed

* Mon Nov 02 2009 Michael Shigorin <mike@altlinux.org> 1.9.1-alt3
- applied desktop file patch by icesik@

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 1.9.1-alt2
- fixed FTBFS with gcc-4.4 (a patch needed an addition)
- added gentoo patches (sdl, parallel) just in case

* Tue Mar 24 2009 Michael Shigorin <mike@altlinux.org> 1.9.1-alt1
- 1.9.1
  + no more build in %%install
  + imported icons from fedora (GPL; previously available at
    http://jrbabcock.home.comcast.net/flightgear/icons/)
  + disabled fgrun in desktop file (currently broken,
    tries to execve "")
- disabled patch1 (fixed upstream)
- updated patch6 to fgrun-1.5.1
- added fedora gcc44 patch (future-proof)
- replaced debian menufile with fd.o one based on fedora's
- spec cleanup
- buildreq

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.0.0-alt1.3.1
- fix build
- don't run update menu after install and uninstall

* Tue Jul 08 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1.3
- Fixed fgrun startup from menu

* Tue Jan 29 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1.2
- Fixed #14231 (fgrun game mode must turn on fullscreen)

* Wed Jan 09 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1.1
- Fixed buildrequies (autoconf/automake dependecies)

* Tue Jan 08 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1
- 1.0.0
- Now uses system libexpat (#8251)

* Tue May 01 2007 Albert R. Valiev <darkstar@altlinux.ru> 0.9.10-alt1.1
- Rebuild with libalut
- Update fgrun to 0.4.8

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 0.9.10-alt1
- 0.9.10

* Thu Mar 02 2006 Albert R. Valiev <darkstar@altlinux.ru> 0.9.9-alt1.1
- Updated build requirements.

* Sat Dec 03 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.9.9-alt1
- New version

* Tue Mar 01 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.9.8-alt2
- Parallel build turned of (cause it fails to build with it...)

* Fri Jan 21 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.9.8-alt1
- Update to 0.9.8 version
- Changed FlightGear Launcher from fgkicker to fgrun.
- Rebuild with g++3.4 compiler

* Tue Sep 14 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.9.6-alt2.pre1
- Fixed airports.dat file installation
- Moved airports.dat from FlightGear-data package into main package

* Tue Sep 14 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.9.6-alt1.pre1
- New version build
- Added FlightGear launcher
- Removed old menu entries

* Sat Jun 14 2003 Albert R. Valiev <darkstar@altlinux.ru> 0.9.2-alt1
- Initial build to sisyphus
- Created menu entries for majority of flyable aircrafts
