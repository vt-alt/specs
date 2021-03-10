%define full_ver %(pkg-config --modversion libpq)
%define pg_ver %(c=%{full_ver}; echo ${c%%.*})

Name: repmgr
Version: 5.2.1
Release: alt2
Summary: Replication Manager for PostgreSQL Clusters
Group: Databases
License: GPL-3.0
Url: http://www.repmgr.org/
Source0: %name-%version.tar
Source1: repmgr.init
Source2: repmgr.sudoers
Source3: repmgr.service
Source4: repmgr.tmpfiles
Source5: repmgr.sysconfig

Patch: %name-%version.patch

Requires: postgresql-common

BuildRequires: flex
BuildRequires: libssl-devel
BuildRequires: postgresql-devel postgresql-devel-static
# for build doc
BuildRequires: docbook-dtds docbook-style-xsl
BuildRequires: /usr/bin/xmllint /usr/bin/xsltproc


%description
Repmgr is an open-source tool suite for managing replication and failover in a
cluster of PostgreSQL servers. It enhances PostgreSQL's built-in hot-standby
capabilities with tools to set up standby servers, monitor replication, and
perform administrative tasks such as failover or manual switchover operations.

%package -n postgresql%pg_ver-%name
Summary: Replication Manager for PostgreSQL Clusters
Group: Databases
Requires: postgresql%pg_ver-server

%description -n postgresql%pg_ver-%name
Repmgr is an open-source tool suite for managing replication and failover in a
cluster of PostgreSQL servers. It enhances PostgreSQL's built-in hot-standby
capabilities with tools to set up standby servers, monitor replication, and
perform administrative tasks such as failover or manual switchover operations.

%package doc
Summary:  Documentation for the Replication Manager for PostgreSQL Clusters
Group: Documentation
BuildArch: noarch

%description doc
The package contains documentation for the Replication Manager for PostgreSQL Clusters.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
USE_PGXS=1 %make_build
%make doc
%make doc-repmgr.html

%install
USE_PGXS=1 %makeinstall_std

mkdir -p %buildroot/{%_initdir,%_unitdir,%_tmpfilesdir,%_sysconfdir/{sysconfig,sudoers.d,%name},%_logdir/%name}
install -p -m755 %SOURCE1 %buildroot%_initdir/%name
install -p -m644 %SOURCE2 %buildroot%_sysconfdir/sudoers.d/%name
install -p -m644 %SOURCE3 %buildroot%_unitdir/%name.service
install -p -m644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf
install -p -m644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name
install -p -m644 repmgr.conf.sample %buildroot%_sysconfdir/%name/%name.conf

%post -n postgresql%pg_ver-%name
echo "Execute the following psql command inside any database that you want to update:"
echo "ALTER EXTENSION repmgr UPDATE;                                                 "

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE
%_bindir/repmgr
%_bindir/repmgrd
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/sudoers.d/%name
%dir %attr(750,root,postgres) %_sysconfdir/%name
%config(noreplace) %attr(640,root,postgres) %_sysconfdir/%name/%name.conf
%_initdir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%attr(1775,root,postgres) %dir %_logdir/%name

%files -n postgresql%pg_ver-%name
%_libdir/pgsql/*
%_datadir/pgsql/extension/*

%files doc
%doc doc/html

%changelog
* Wed Feb 24 2021 Alexey Shabalin <shaba@altlinux.org> 5.2.1-alt2
- Execute service as postgres system user.

* Wed Feb 10 2021 Alexey Shabalin <shaba@altlinux.org> 5.2.1-alt1
- Initial build.
