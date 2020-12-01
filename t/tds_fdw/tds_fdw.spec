Summary: TDS Foreign data wrapper
Name: tds_fdw
Version: 2.0.2
Release: alt2
License: PostgreSQL
Group: Development/Databases
Url: https://github.com/tds-fdw/tds_fdw
Packager: Pavel Vasenkov <pav@altlinux.org>
Source: %name-%version.tar.gz

BuildRequires: libfreetds-devel
BuildRequires: postgresql-devel

Requires: postgresql-%name = %EVR

%description
This is a PostgreSQL foreign data wrapper that can connect to databases that use the Tabular Data Stream (TDS) protocol, such as Sybase databases and Microsoft SQL server.

%package -n postgresql-%name
Summary: PostgreSQL foreign data wrapper extension for PostgreSQL
Group: Databases

%description -n postgresql-%name
This is a PostgreSQL foreign data wrapper that can connect to databases that use the Tabular Data Stream (TDS) protocol, such as Sybase databases and Microsoft SQL server.

%prep
%setup

%build

%make USE_PGXS=1
%make_build

%makeinstall_std

%files -n postgresql-%name
%_defaultdocdir/postgresql/extension/README.%name.md
%_libdir/pgsql/%name.so
%_datadir/pgsql/extension/*

%changelog
* Fri Nov 27 2020 Pavel Vasenkov <pav@altlinux.org> 2.0.2-alt2
- Set package name and descriptions

* Fri Nov 13 2020 Pavel Vasenkov <pav@altlinux.org> 2.0.2-alt1
- Initial build in Sisyphus 
