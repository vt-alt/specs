Name: FlightGear-data
Version: 2020.1
Release: alt1

Summary: Data pack for FlightGear open-source flight simulator

License: GPL
Group: Games/Arcade
Url: http://www.flightgear.org

Packager: Michael Shigorin <mike@altlinux.org>

# Source-url: https://sourceforge.net/projects/flightgear/files/release-2018.2/FlightGear-%version-data.tar.bz2
Source: %name-%version.tar

BuildArch: noarch

AutoReqProv: no

Provides: fgfs-data = %version-%release
# to avoid data lurking w/o binaries
# NB: release intentionally left out
Requires: FlightGear = %version


# it's more than two gigs of data
%brp_strip_none
%set_fixup_method skip
#set_strip_method none
%set_cleanup_method skip
%set_compress_method none
%set_verify_elf_method skip

%description
FlightGear is a free, open-source, multi-platform, and sophisticated
flight simulator framework for the development and pursuit of
interesting flight simulator ideas.

This package contains base FlightGear data files; feel free to
visit %url for more scenery and aircraft.

%package -n FlightGear-doc
Summary: Documentation for FlightGear open-source flight simulator
Group: Books/Computer books

%description -n FlightGear-doc
FlightGear is a free, open-source, multi-platform, and sophisticated
flight simulator framework for the development and pursuit of
interesting flight simulator ideas.

This package contains FlightGear documentation.

See also this nice and eagerly read tutorial:
http://ericbrasseur.org/flight_simulator_tutorial.html

%prep
%setup

%install
mkdir -p %buildroot{%_datadir/flightgear,%_docdir}
mv Docs %buildroot%_docdir/FlightGear-%version
mv AUTHORS ChangeLog NEWS README %buildroot%_docdir/FlightGear-%version/
mv * %buildroot%_datadir/flightgear/

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find %buildroot -name 'Thumbs.db*' -print -delete

%files
%_datadir/flightgear/

%files -n FlightGear-doc
%_docdir/FlightGear-%version

%changelog
* Wed May 13 2020 Michael Shigorin <mike@altlinux.org> 2020.1-alt1
- 2020.1

* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 2018.2.2-alt1
- 2018.2.2

* Thu Sep 07 2017 Michael Shigorin <mike@altlinux.org> 2017.2.1-alt1
- 2017.2.1

* Sat Feb 20 2016 Michael Shigorin <mike@altlinux.org> 2016.1.1-alt1
- 2016.1

* Wed Sep 30 2015 Michael Shigorin <mike@altlinux.org> 3.6.0-alt0.1
- 3.6.0-RC

* Thu Feb 19 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Feb 10 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt0.2
- 3.4.0-RC2

* Wed Oct 22 2014 Michael Shigorin <mike@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sat Feb 22 2014 Michael Shigorin <mike@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Feb 12 2014 Michael Shigorin <mike@altlinux.org> 3.0.0-alt0.4
- 3.0.0-rc4

* Thu Feb 06 2014 Michael Shigorin <mike@altlinux.org> 3.0.0-alt0.3
- 3.0.0-rc3

* Tue Nov 26 2013 Michael Shigorin <mike@altlinux.org> 2.12.1-alt1
- 2.12.1

* Thu Sep 26 2013 Michael Shigorin <mike@altlinux.org> 2.12.0-alt1
- 2.12.0

* Tue Feb 19 2013 Michael Shigorin <mike@altlinux.org> 2.10.0-alt2
- avoid double compression

* Tue Feb 19 2013 Michael Shigorin <mike@altlinux.org> 2.10.0-alt1
- 2.10.0

* Sun Sep 09 2012 Michael Shigorin <mike@altlinux.org> 2.8.0-alt2
- added non-strict dependency on the main package to avoid lurking data

* Sat Aug 18 2012 Michael Shigorin <mike@altlinux.org> 2.8.0-alt1
- 2.8.0

* Sat Mar 03 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt1
- 2.6.0

* Sat Nov 12 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt2
- move to the current strip regulations, argh
- minor spec tweaks

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt1.1
- disable autoreq (we don't need no svginstr)
- FG-2.4 data expected in %_datadir/flightgear (no camelcase)

* Thu Sep 15 2011 Andrew Clark <andyc@altlinux.org> 2.4.0-alt1
- version update to 2.4.0-alt1

* Tue Mar 2 2010 Andrew Clark <andyc@altlinux.org> 2.0.0-alt1
- update to version 2.0.0-alt1

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.9.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * windows-thumbnail-database-in-package for FlightGear-data
  * postclean-05-filetriggers for spec file

* Tue Mar 24 2009 Michael Shigorin <mike@altlinux.org> 1.9.0-alt1
- 1.9.0
- spec cleanup

* Tue Jan 08 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 0.9.10-alt1
- 0.9.10
- fixes #8683
- noarch
- optimized packaging
  + danced with set_*_method macro parameters
- removed COPYING (standard GPLv2, see License: tag)

* Sat Dec 03 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.9.9-alt1
- Update to 0.9.9 version

* Fri Jan 21 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.9.8-alt1
- Update to 0.9.8 version

* Tue Sep 14 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.9.6-alt2.pre1
- Airports data file moved into main FlightGear package

* Tue Sep 14 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.9.6-alt1.pre1
- New version build
- Added FlightGear launcher
- Removed old menu entries

* Sat Jun 14 2003 Albert R. Valiev <darkstar@altlinux.ru> 0.9.2-alt1
- Initial build to sisyphus
- Created menu entries for majority of flyable aircrafts
