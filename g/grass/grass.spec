%define shortver 78
%define libver 7.8

Name:    grass
Version: 7.8.5
Release: alt1

%def_with mysql
%def_with postgres
%def_with sqlite
%def_with python3
# liblas-config
%def_without liblas
# Missing
%def_without opendwg
# Old version
%def_without opencl
# pdal-config
%def_without pdal

Summary: Geographic Resources Analysis Support System
License: %gpl2plus
Group:   Sciences/Geosciences
URL:     https://grass.osgeo.org
#VCS: https://github.com/OSGeo/grass

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

Patch0: %name-pkgconf.patch
Patch1: %name-use-simplejson.patch
Patch2: %name-soname.patch
Patch3: %name-alt-build-with-external-lz4.patch
Patch4: %name-alt-build-with-gdal.patch

%define grassdir grass%shortver
#define grassdir grass-%version
%define grassdatadir /var/lib/grass%shortver/data

BuildRequires(pre): rpm-build-licenses

BuildRequires: flex gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-six
BuildRequires: python3-module-simplejson
%else
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-six
BuildRequires: python-module-simplejson
%endif
BuildRequires: libfftw3-devel libjpeg-devel libpng-devel libtiff-devel zlib-devel
BuildRequires: libncurses-devel libtinfo-devel
BuildRequires: postgresql-devel libmariadb-devel libsqlite3-devel
BuildRequires: libqt4-core libXmu-devel swig libfreetype-devel readline-devel libGLU-devel
BuildRequires: proj-devel libgdal-devel libproj-nad proj
BuildRequires: tcl-devel tk-devel
BuildRequires: libICE-devel, libSM-devel, libX11-devel, libXau-devel, libXaw-devel
BuildRequires: libXrandr-devel, libXdmcp-devel, libXext-devel, libXfixes-devel
BuildRequires: libXfont-devel, libXft-devel, libXi-devel, libXmu-devel, libXpm-devel
BuildRequires: libXrender-devel, libXres-devel, libXScrnSaver-devel, libXinerama-devel
BuildRequires: libXt-devel, libXtst-devel, libXxf86dga-devel, libXcomposite-devel
BuildRequires: libXxf86vm-devel, libdmx-devel, libfontenc-devel, libGLU-devel
BuildRequires: libXdamage-devel, libxkbfile-devel, xcursorgen, xorg-font-utils
BuildRequires: libXvMC-devel, libXcursor-devel, libXevie-devel, libXv-devel
BuildRequires: xorg-xtrans-devel, xorg-util-macros, xorg-sgml-doctools
BuildRequires: gccmakedep, imake, lndir, makedepend, rman, xorg-cf-files
BuildRequires: libcairo-devel
BuildRequires: libblas-devel
BuildRequires: libgeos-devel
BuildRequires: liblapack-devel
BuildRequires: lesstif-devel
BuildRequires: libGLw-devel
BuildRequires: libunixODBC-devel
BuildRequires: libwxGTK-devel
BuildRequires: libmariadbd-devel
BuildRequires: python-module-simplejson
BuildRequires: xorg-glproto-devel
BuildRequires: desktop-file-utils
BuildRequires: bzlib-devel
BuildRequires: libzstd-devel
BuildRequires: libnetcdf-devel
BuildRequires: opencl-headers
BuildRequires: libgomp-devel
BuildRequires: liblz4-devel
BuildRequires: python-modules-distutils

# internal modules
%if_with python3
%add_python3_req_skip srs wms_base wms_cap_parsers
%add_python3_lib_path %_libdir/%grassdir
%else
%add_python_req_skip srs wms_base wms_cap_parsers
%endif
%add_findreq_skiplist %_libdir/%grassdir/etc/*

%description
GRASS (Geographic Resources Analysis Support System) is an
open source, Free Software Geographical Information System (GIS)
with raster, topological vector, image processing, and graphics
production functionality that operates on various platforms
through a graphical user interface and shell in X-Window.

%package -n lib%name
Summary: GRASS (Geographic Resources Analysis Support System) runtime libraries
Group: Sciences/Geosciences
Provides: %name-docs = %version-%release
Obsoletes: %name-docs < %version-%release

%description -n lib%name
GRASS (Geographic Resources Analysis Support System) runtime libraries.

%package devel
Summary: Development files for GRASS
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development headers for GRASS.

%prep
%setup
# Remove bundled lz4
rm lib/gis/lz4{.h,.c}
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
subst 's/\t/        /g' \
      scripts/v.db.dropcolumn/v.db.dropcolumn.py \
      scripts/v.db.addtable/v.db.addtable.py

%build
export LDCONFIG=-llz4
%configure \
	--prefix=%_libdir \
	--with-nls \
	--with-cxx \
	--enable-largefile \
	--enable-shared \
	--with-blas \
	--with-bzlib \
	--with-cairo \
	--with-cxx \
        %{subst_with opendwg} \
	--with-fftw \
	--with-freetype-includes=%{_includedir}/freetype2 \
	--with-freetype=yes \
	--with-gdal \
	--with-geos \
	--with-glw \
	--with-gomp \
	--with-lapack \
        %{subst_with liblas} \
	--with-motif \
	%{subst_with mysql} \
	--with-mysql-includes=%{_includedir}/mysql \
        --with-netcdf=%_libdir/hdf5-seq/bin/nc-config \
	--with-nls \
	--with-odbc \
        %{subst_with opencl} \
	--with-opengl \
	--with-openmp \
	%{subst_with pdal} \
	%{subst_with postgres} \
	--with-postgres-includes=/usr/include/pgsql \
	--with-proj \
	--with-proj-share=%{_datadir}/proj \
        --with-pthread \
	--with-python \
	--with-readline \
	%{subst_with sqlite} \
	--with-wxwidgets=wx-config \
	--with-x \
        --with-zstd

%make

%install
%makeinstall UNIX_BIN=%buildroot%_bindir PREFIX=%buildroot%_prefix install

# Change GISBASE in startup script
sed -i -e 's|%buildroot%_prefix|%_libdir|g' \
        %buildroot%_bindir/%name%shortver

#TODO: Quotes and linebreaks in sed calls
# Replace GISBASE environment variable with paths that match our locale file layout
sed -i -e 's|os.path.join(os.getenv("GISBASE"), '\''locale'\''|os.path.join('\''%_datadir'\'', '\''locale'\''|' -e 's|os.path.join(os.getenv("GISBASE"), "etc"|os.path.join(\"%_libdir/%grassdir\", "etc"|' -e 's|self.gisbase  = os.getenv("GISBASE")|self.gisbase = "%_docdir/%grassdir"|' %buildroot%_prefix/%grassdir/etc/python/grass/script/*.py

# Make grass headers and libraries available on the system
mv %buildroot%_prefix/%grassdir/lib/ %buildroot%_libdir
mv %buildroot%_prefix/%grassdir/include %buildroot%_prefix/
rm -rf %buildroot%_includedir/Make

# Make man pages available on system, convert to utf8 and avoid name conflict with "parallel" manpage
mkdir -p %buildroot%_man1dir
for manpage in `find  %buildroot%_prefix/%grassdir/docs/man/man1 -type f` ; do
   iconv -f iso8859-1 -t utf8 \
        $manpage > %buildroot%_man1dir/`basename $manpage`"grass"
done
sed -i -e 's/^.TH \(.*\) 1/.TH \1 1grass/' %buildroot%_man1dir/*
rm -rf %buildroot%_prefix/%grassdir/man

# Make locales available on system
mkdir -p %buildroot%_datadir/locale/
mv %buildroot%_prefix/%grassdir/locale %buildroot%_datadir/

# Create versionless symlinks for binary and libdir
# The libdir symlink is handy for QGIS. QGIS asks the user for gisbase
# and then stores it. See Fedora BZ 711860
# Ubuntu does it the same way
#
# The binary symlink may keeps us from creating the desktop file
# And we will can just pack it
ln -s %_bindir/%name%shortver %buildroot%_bindir/%name
ln -s %_libdir/%grassdir %buildroot%_libdir/%name

mkdir -p %buildroot%_libdir/pkgconfig
install -p -m 644 %name.pc %buildroot%_libdir/pkgconfig/

for res in 48x48 64x64; do
  mkdir -p %buildroot%_datadir/icons/hicolor/$res/apps
  install -p -m 644 gui/icons/%name-$res.png %buildroot%_datadir/icons/hicolor/$res/apps/%name.png
done

# "Encoding" should be removed; Gone for releases after 6.4.3
# http://trac.osgeo.org/grass/changeset/57941/grass
install -Dm 0644 \
	gui/icons/%name.desktop \
        %buildroot%_desktopdir/%name.desktop

# Install AppData file
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 gui/icons/%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# Move icon folder in GISBASE and set its path to be FHS compliant
mv %buildroot%_prefix/%grassdir/docs/html/icons %buildroot%_prefix/%grassdir/

# Switch to the system wide docs, to be FHS compliant
rm -rf %buildroot%_prefix/%grassdir/docs

# Hide GISBASE into system's %_libdir instead, to be FHS compliant
mv %buildroot%_prefix/%grassdir %buildroot%_libdir/

# Correct font path
sed -i -e 's|%buildroot%_prefix/%grassdir|%_libdir/%grassdir|' \
%buildroot%_libdir/%grassdir/etc/fontcap

# Remove service scripts
rm -rf %buildroot%_libdir/%grassdir/tools

# Move python to %%python_sitelibdir
%if_with python3
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%_libdir/%grassdir/etc/python/grass %buildroot%python3_sitelibdir
%else
mkdir -p %buildroot%python_sitelibdir
mv %buildroot%_libdir/%grassdir/etc/python/grass %buildroot%python_sitelibdir
%endif

# Cleanup %%grassdir
rm -rf %buildroot%_libdir/%grassdir/share %buildroot%_libdir/*.a

# Prepare python files for Python 3
%if_with python3
find %buildroot -type f | xargs -l1 subst 's,^#!/usr/bin/env python.*$,#!%__python3,'
#%ifarch %ix86
#subst 's/\<\([0-9]\+\)L\>/\1/' %buildroot%python3_sitelibdir/grass/lib/ogsf.py \
#                               %buildroot%python3_sitelibdir/grass/lib/raster.py
#%endif
%endif

# Mark localization files
%find_lang --output %name.lang %{name}mods %{name}libs %{name}wxpy

%post
[ ! -L %_lockdir/grass62/locks ] || rm -f %_lockdir/grass62/locks
[ $1 -ne 1 ] || ln -s %_lockdir/grass%shortver %_libdir/%grassdir/locks

%preun
rm -f %_libdir/%grassdir/locks

%files -f %name.lang
%doc AUTHORS CHANGES translators.csv contributors.csv contributors_extra.csv doc
%_bindir/*
%dir %_libdir/%grassdir
%dir %_libdir/grass
%_libdir/%grassdir/*
%exclude %_libdir/%grassdir/driver/db/*
%_libdir/%grassdir/driver/db/*
%if_with python3
%python3_sitelibdir/%name
%else
%python_sitelibdir/%name
%endif
%_desktopdir/*.desktop
%_datadir/appdata/%name.appdata.xml
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/*.1grass*

%files -n lib%name
%_libdir/lib%{name}_*.%libver.so

%files devel
%_pkgconfigdir/%name.pc
%_includedir/%name
%exclude %_libdir/lib%{name}_*.%libver.so
%_libdir/lib%{name}_*.so

%changelog
* Mon Apr 19 2021 Andrey Cherepanov <cas@altlinux.org> 7.8.5-alt1
- New version.
- Build with Python3.

* Thu Mar 28 2019 Andrey Cherepanov <cas@altlinux.org> 7.6.1-alt1
- New version.
- Remove bundled copy of liblz4 (ALT #36396).
- Spec cleanup.

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 7.4.4-alt2
- Rebuild with libproj 5.2.0

* Mon Jan 07 2019 Andrey Cherepanov <cas@altlinux.org> 7.4.4-alt1
- New version.

* Mon Dec 17 2018 Andrey Cherepanov <cas@altlinux.org> 7.4.3-alt1
- New version.

* Tue Oct 16 2018 Andrey Cherepanov <cas@altlinux.org> 7.4.1-alt1
- New version.
- Use mariadb instead of MySQL.

* Wed Sep 26 2018 Grigory Ustinov <grenka@altlinux.org> 7.4.0-alt2
- Fixed FTBFS.

* Sat Feb 24 2018 Andrey Cherepanov <cas@altlinux.org> 7.4.0-alt1
- New version.
- Make switch for build witih python3 (disabled by default).

* Sun Dec 10 2017 Dmitry V. Levin <ldv@altlinux.org> 7.2.2-alt2
- Build with fftw3.

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 7.2.2-alt1
- New version

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 7.2.1-alt2
- Rebuild with geos 3.6.2

* Tue Jul 25 2017 Andrey Cherepanov <cas@altlinux.org> 7.2.1-alt1
- New version

* Fri Jan 27 2017 Andrey Cherepanov <cas@altlinux.org> 7.2.0-alt1
- New version

* Fri Oct 28 2016 Andrey Cherepanov <cas@altlinux.org> 7.0.5-alt1
- New version

* Fri Sep 02 2016 Andrey Cherepanov <cas@altlinux.org> 7.0.4-alt1
- New version
- Fix gisbase path in startup script (ALT #31954)

* Thu Feb 04 2016 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt2
- Rebuild with new libproj

* Fri Dec 11 2015 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt1
- New version (https://grass.osgeo.org/news/50/15/GRASS-GIS-7-0-2-released/)

* Wed Oct 07 2015 Andrey Cherepanov <cas@altlinux.org> 7.0.1-alt1
- New version

* Thu Mar 05 2015 Andrey Cherepanov <cas@altlinux.org> 7.0.0-alt1
- New version

* Tue Jan 28 2014 Andrey Cherepanov <cas@altlinux.org> 6.4.3-alt1
- New version
- Add support of useful bindings
- Move libraries to libgrass (ALT #15725)

* Fri Jun 07 2013 Ivan Ovcherenko <asdus@altlinux.org> 6.4.2-alt1.2
- Create versionless symlinks

* Thu Mar 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.2-alt1.1
- build fixed

* Fri Feb 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.2-alt1
- 6.4.2
- build fixed

* Fri Apr 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.0-alt2.3
- build fixed

* Fri Nov 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.0-alt2.2
- build fixed
- BuildRequires structured

* Mon Sep 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.0-alt2.1
- rebuild with MySQL 5.1

* Tue Sep 14 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.0-alt2
- 6.4.0 release
- docs moved to /usr/share (may cause problems) for fixing build

* Fri Sep 03 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 6.4.0-alt1.rc6
- new version: 6.4.0 RC6
- enabled install section of spec with corresponding checks
- built with mysql,sqlite
- fixed lockdir symlinking
- doc subpackage
- devel subpackage

* Thu Dec 04 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.2.3-alt2
- build fixed 

* Mon Apr 07 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.2.3-alt1
- new upstream version: advanced vectors, new GUI

* Thu Aug 23 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.2.2-alt1
- first try by me

* Wed Feb 14 2007 Dmitri Kuzishchin <dim@altlinux.ru> 6.2.1-alt1
- Initial package.
