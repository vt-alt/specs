%define pg_ver 12

Name: postgis
Version: 3.1.1
Release: alt0.p9.1

Summary: Geographic Information Systems Extensions to PostgreSQL
Summary(ru_RU.UTF-8): Геоинформационные расширения для PostgreSQL
License: GPL-2.0
Group: Databases
Url: http://postgis.refractions.net

Source: %name-%version.tar
Source1: create_template_postgis
Source2: postgis.watch

BuildRequires: gcc-c++
BuildRequires: ImageMagick-tools
BuildRequires: docbook-dtds
BuildRequires: docbook-style-xsl
BuildRequires: flex
BuildRequires: libgdal-devel
BuildRequires: libgeos-devel
BuildRequires: libgtk+2-devel
BuildRequires: libproj-devel
BuildRequires: libxml2-devel
BuildRequires: postgresql-devel
BuildRequires: libjson-c-devel
BuildRequires: libprotobuf-c-devel
BuildRequires: protobuf-c-compiler
BuildRequires: libpcre-devel
BuildRequires: xsltproc

Requires: postgresql%pg_ver-%name = %EVR

%description
PostGIS adds support for geographic objects to the PostgreSQL
object-relational database. In effect, PostGIS "spatially enables" the
PostgreSQL server, allowing it to be used as a backend spatial
database for geographic information systems (GIS).

%description -l ru_RU.UTF-8
PostGIS добавляет поддержку географических объектов в PostgreSQL. В
сущности PostGIS является расширением PostgreSQL сервера,
позволяющим использовать его для хранения и обработки геоданных в
геоинформационных системах (ГИС).

%package -n postgresql%pg_ver-%name
Summary: The PostGIS extension for PostgreSQL
Group: Databases
Requires: postgresql%pg_ver-server

%description -n postgresql%pg_ver-%name
This package contains shared library for PostgreSQL server

%description -n postgresql%pg_ver-%name -l ru_RU.UTF-8
Подгружаемая postgis библиотека для PostgreSQL сервера

%prep
%setup
subst "s|PGSQL_DOCDIR|DOCDIR|g" doc/Makefile.in

%build
export PCRE_CPPFLAGS=-I/usr/include/pcre
./autogen.sh
%configure \
	--disable-static \
	--with-gui \
	--with-raster \
	--with-xsldir=%_datadir/xml/docbook/xsl-stylesheets
%make all docs comments

%install
install -pD -m0755 %SOURCE1 %buildroot%_bindir/create_template_postgis
install -d %buildroot%_libdir/pgsql/
install -d %buildroot%_includedir
%makeinstall_std
%makeinstall_std -C doc docs-install comments-install man-install DOCDIR=%_docdir/%name-%version

rm -rf %buildroot%_libdir/liblwgeom.a

%files
%doc %_docdir/%name-%version
%_bindir/pgsql2shp
%_bindir/shp2pgsql*
%_bindir/raster2pgsql
%_man1dir/*
%_datadir/pgsql/applications/shp2pgsql-gui.desktop
%_datadir/pgsql/icons/hicolor/*/apps/shp2pgsql-gui.png

%files -n postgresql%pg_ver-%name
%_bindir/create_template_postgis
%_libdir/pgsql/%{name}*.so
%_libdir/pgsql/address_standardizer*.so
%_datadir/pgsql/contrib/postgis-*/*.sql
%_datadir/pgsql/contrib/postgis-*/*.pl
%_datadir/pgsql/extension
%doc %_datadir/doc/postgresql/extension/README.address_standardizer

%changelog
* Wed Apr 21 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt0.p9.1
- Backport new version to p9 branch for PostgreSQL 12.

* Mon Feb 01 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- New version.

* Mon Dec 28 2020 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Sun Nov 22 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt1
- New version (build with PosgreSQL 13).

* Sat Aug 22 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version.

* Thu May 28 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version.

* Thu Dec 12 2019 Andrey Cherepanov <cas@altlinux.org> 2.5.3-alt2
- Rebuild with PostgreSQL 12.

* Tue Aug 13 2019 Andrey Cherepanov <cas@altlinux.org> 2.5.3-alt1
- New version.

* Tue Mar 19 2019 Andrey Cherepanov <cas@altlinux.org> 2.5.2-alt1
- New version.
- Require postgresql11 (ALT #36240).

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 2.5.1-alt2
- Rebuild with libproj 5.2.0

* Wed Nov 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt1
- New version.

* Tue Oct 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- New version.
- Add watch file to src.rpm.

* Mon Apr 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.4-alt1
- New version.

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1
- New version.
- Build from upstream tarball.
- Add support for json-c, protobuf-c and pcre.
- Fix build with postgresql10 (thanks taf@).

* Mon Oct 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- New version

* Tue Aug 29 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.3-alt2
- Return postgresql-postgis for Postgis extension

* Sat Aug 26 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.3-alt1
- 2.3.3
- Merge postgis and postgresql-postgis, exclude postgis-devel

* Tue Nov 27 2012 Alexey Shabalin <shaba@altlinux.ru> 1.5.8-alt1
- 1.5.8

* Mon Jul 30 2012 Alexey Shabalin <shaba@altlinux.ru> 1.5.5-alt1
- 1.5.5

* Thu Apr 19 2012 Alexey Shabalin <shaba@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Sat May 22 2010 Denis Klimov <zver@altlinux.org> 1.5.1-alt5
- change proj-devel to libproj-devel in BuildRequires

* Mon Mar 29 2010 Denis Klimov <zver@altlinux.org> 1.5.1-alt4
- add subpackage with postgresql shared lib
- remove wildchars from create_template_postgis
- add patch for install dirs
- Closes #23248

* Sun Mar 28 2010 Denis Klimov <zver@altlinux.org> 1.5.1-alt3
- fix install create_template_postgis

* Sun Mar 28 2010 Denis Klimov <zver@altlinux.org> 1.5.1-alt2
- add create_template_postgis script

* Wed Mar 17 2010 Denis Klimov <zver@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux

