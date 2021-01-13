%define full_ver %(pkg-config --modversion libpq)
%define pg_ver %(c=%{full_ver}; echo ${c%%.*})

Name: timescaledb
Version: 2.0.0
Release: alt1
Summary: Open-source time-series database powered by PostgreSQL
Group: Databases
License: Apache-2.0
Url: http://www.timescale.com
Source0: %name-%version.tar

BuildRequires: cmake
BuildRequires: libssl-devel
BuildRequires: postgresql-devel

%description
TimescaleDB is an open-source database designed to make SQL scalable for
time-series data.  It is engineered up from PostgreSQL, providing automatic
partitioning across time and space (partitioning key), as well as full SQL
support.

%package -n postgresql%pg_ver-%name
Summary: Open-source time-series database powered by PostgreSQL
Group: Databases
Requires: postgresql%pg_ver-server

%description -n postgresql%pg_ver-%name
TimescaleDB is an open-source database designed to make SQL scalable for
time-series data.  It is engineered up from PostgreSQL, providing automatic
partitioning across time and space (partitioning key), as well as full SQL
support.

%prep
%setup
# Remove tsl directory containing sources licensed under Timescale license
rm -rf tsl
echo %major_ver

%build
%cmake \
    -DUSE_OPENSSL=ON \
    -DSEND_TELEMETRY_DEFAULT=OFF \
    -DREGRESS_CHECKS=OFF \
    -DAPACHE_ONLY=ON \
    -DPG_CONFIG=%_bindir/pg_config

%cmake_build

%install
%cmakeinstall_std

%files -n postgresql%pg_ver-%name
%doc README.md LICENSE-APACHE
%_libdir/pgsql/*
%_datadir/pgsql/extension/*

%changelog
* Fri Jan 08 2021 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Fri Oct 02 2020 Alexey Shabalin <shaba@altlinux.org> 1.7.4-alt1
- Initial build.

