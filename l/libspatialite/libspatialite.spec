%global _geocallback "--disable-geocallbacks"

Name: libspatialite
Version: 4.3.0a
Release: alt3
Summary: Enables SQLite to support spatial data
Group: System/Libraries
License: MPLv1.1 or GPLv2+ or LGPLv2+
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: https://www.gaia-gis.it/fossil/libspatialite
Source0: http://www.gaia-gis.it/gaia-sins/%name-sources/%name-%version.tar.gz

BuildRequires: libproj-devel
BuildRequires: freexl-devel
BuildRequires: libsqlite3-devel
BuildRequires: libgeos-devel
BuildRequires: libxml2-devel
BuildRequires: zlib-devel

%description
SpatiaLite is a a library extending the basic SQLite core
in order to get a full fledged Spatial DBMS, really simple
and lightweight, but mostly OGC-SFS compliant.

%package devel
Summary: Development libraries and headers for SpatiaLite
Group: System/Libraries
Requires: %name%{?_isa} = %version-%release
Requires: pkgconfig

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%add_optflags -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H=1
%configure \
    --disable-static \
    %{?_geocallback}

%make_build

%install
%makeinstall_std

# Delete undesired libtool archives
rm -f %buildroot%_libdir/*.la


%files
%doc COPYING AUTHORS
%_libdir/%name.so.*
%_libdir/mod_spatialite.so.*

%files devel
%doc examples/*.c
%_includedir/spatialite.h
%_includedir/spatialite
%_libdir/%name.so
%_libdir/mod_spatialite.so
%_libdir/pkgconfig/spatialite.pc

%changelog
* Fri Oct 04 2019 Vladislav Zavjalov <slazav@altlinux.org> 4.3.0a-alt3
- Rebuild with libproj 6.2.0 (use DACCEPT_USE_OF_DEPRECATED_PROJ_API_H)

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 4.3.0a-alt2
- Rebuild with libproj 5.2.0

* Wed Feb 28 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0a-alt1
- New version. (ALT #34590)

* Thu Feb 04 2016 Andrey Cherepanov <cas@altlinux.org> 4.1.1-alt1.1
- Rebuild with new geos

* Thu Feb 27 2014 Ilya Mashkin <oddity@altlinux.ru> 4.1.1-alt1
- 4.1.1

* Tue Jan 29 2013 Ilya Mashkin <oddity@altlinux.ru> 4.0.0-alt1
- Build for Sisyphus

* Sun Dec  1 2012 Volker Frohlich <volker27@gmx.at> - 4.0.0-1
- New upstream release
- Remove arch restrictions, solving BZ 663938 and 846301
- Update conditional for geosadvanced

* Sat Aug 18 2012 Volker Frohlich <volker27@gmx.at> - 3.1.0-0.3.RC2
- Add ppc to excluded archs (BZ #846301)
- Don't build with profiling

* Fri Jan 27 2012 Volker Frohlich <volker27@gmx.at> - 3.1.0-0.1.RC2
- Add pkconfig as Requirement to the devel sub-package
- Drop freexl patch (solved), build with Freexl
- Update descriptions and summaries
- Re-design conditionals for build flags
- Don't run checks if built without advancedgeos
- Include examples as documentation

* Wed Jan 14 2012 Volker Frohlich <volker27@gmx.at> - 3.0.1-1
- New upstream release
- Drop defattr
- Run tests
- Own spatialite include-dir
- Add GPLv2+ and LGPLv2+ as alternative licenses
- Update URL and source URL
- Reduce build conditions to EPEL or not
- Use isa macro in base package Requires

* Tue Dec 7 2010 Volker Frohlich <volker27@gmx.at> 2.4.0-0.5.RC4
- Corrected wrong Fedora version number in if-statement

* Sun Dec 5 2010 Volker Frohlich <volker27@gmx.at> 2.4.0-0.4.RC4
- Refined configure condition to support RHEL

* Fri Dec 3 2010 Volker Frohlich <volker27@gmx.at> 2.4.0-0.3.RC4
- Added buildroot
- Added doc files

* Wed Dec 1 2010 Volker Frohlich <volker27@gmx.at> 2.4.0-0.2.RC4
- Added description of devel package
- Switched to disable-static flag

* Sun Nov 28 2010 Volker Frohlich <volker27@gmx.at> 2.4.0-0.1.RC4
- Initial packaging for Fedora
