Name: spatialite-gui
Version: 1.7.1
Release: alt4
Summary: GUI to manage Spatialite databases

Group: Databases
License: GPLv3+
Url: https://www.gaia-gis.it/fossil/spatialite_gui
Source0: http://www.gaia-gis.it/gaia-sins/spatialite_gui-%version.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>

Patch1: %name-alt-link-with-sqlite3.patch

BuildRequires: desktop-file-utils
BuildRequires: freexl-devel
BuildRequires: libspatialite-devel
BuildRequires: libgaiagraphics-devel
BuildRequires: libwxGTK-devel
BuildRequires: libsqlite3-devel
BuildRequires: libgeos-devel
BuildRequires: libproj-devel gcc-c++ gcc
BuildRequires: libxml2-devel

%description
GUI to manage Spatialite databases.

%prep
%setup -n spatialite_gui-%version
%patch1 -p2

# Delete shebang from desktop file
#TODO: Clarify
sed -i '1d' gnome_resource/%name.desktop

# Remove existing Makefiles
rm -f Makefile-static*

%build
%autoreconf
%configure  \
        --disable-static
%make_build

%install
%makeinstall_std

# Install icon and desktop file
# Mailed the author
mkdir -p %buildroot%_datadir/pixmaps
install -pm 0644 gnome_resource/%name.png %buildroot%_datadir/pixmaps

desktop-file-install                               \
    --dir=%buildroot%_datadir/applications         \
    gnome_resource/%name.desktop

%files
%doc COPYING AUTHORS
%_bindir/*
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png

%changelog
* Fri Mar 06 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.7.1-alt4
- NMU: Fixed BuildRequires (sqlite-devel -> libsqlite3-devel).

* Sun Oct 06 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.7.1-alt3
- Rebuild with libproj 6.2.0 (use ACCEPT_USE_OF_DEPRECATED_PROJ_API_H)
- Fix possible overfull in sprintf

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.7.1-alt2
- Rebuild with libproj 5.2.0

* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- New version.

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt3
- Rebuild with geos 3.6.2

* Fri Feb 05 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt2
- Rebuild with new geos

* Sat Feb 02 2013 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt1
- Build for Sisyphus

* Sun Jan  6 2013 Volker Frohlich <volker27@gmx.at> 1.6.0-1
- New upstream release
- Patch missing linking instruction

* Sun Dec  2 2012 Bruno Wolff III <bruno@wolff.to> 1.5.0-5
- Rebuild for libspatialite soname bump

* Fri Jul  6 2012 Volker Frohlich <volker27@gmx.at> 1.5.0-2
- Add forgotten BR freexl-devel

* Wed Jan 11 2012 Volker Frohlich <volker27@gmx.at> 1.5.0-1
- Update for new release
- Update URL and source URL
- Correct license to GPLv3+
- Drop patch for wxwidget (solved)
- Use upstreams desktop file and icon
- Don't modify linker flags anymore (solved)

* Mon Jan  9 2012 Volker Frohlich <volker27@gmx.at> 1.4.0-3
- Exclude ppc64 architecture

* Sun Jan  8 2012 Volker Frohlich <volker27@gmx.at> 1.4.0-2
- Remove post and postun sections with useless ldconfig

* Sun Dec  4 2011 Volker Frohlich <volker27@gmx.at> 1.4.0-1
- Initial packaging
