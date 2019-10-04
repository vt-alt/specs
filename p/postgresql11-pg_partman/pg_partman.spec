%define pg_ver 11

Name: postgresql%pg_ver-pg_partman
Version: 4.2.0
Release: alt1

Summary: pg_partman is an extension to create and manage both time-based and serial-based table partition sets.
License: PostgreSQL
Group: Databases
Url: https://badge.fury.io/pg/pg_partman

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Sat May 18 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 python-base sh4
BuildRequires: postgresql-devel

BuildRequires: postgresql-devel

Requires: postgresql%pg_ver-server

%description
pg_partman is an extension to create and manage both time-based and serial-based
table partition sets. Native partitioning in PostgreSQL 10 is supported as of
pg_partman v3.0.1 and much more extensively as of 4.0.0 along with
PostgreSQL 11. Note that all the features of trigger-based partitioning
are not yet supported in native, but performance in both reads & writes is
significantly better.

%prep
%setup
%patch0 -p1

%build
%make

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/pgsql/pg_partman_bgw.so
%_datadir/pgsql/extension/*
%doc %_datadir/doc/postgresql/extension/*

%changelog
* Wed Oct 02 2019 Alexei Takaseev <taf@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sat May 18 2019 Alexei Takaseev <taf@altlinux.org> 4.1.0-alt1
- Initial build for ALT Linux
