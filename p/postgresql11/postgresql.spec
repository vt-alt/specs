# -*- mode: rpm-spec; coding: utf-8 -*-
%def_without devel

# Use ICU
%def_with icu

%define prog_name            postgresql
%define postgresql_major     11
%define postgresql_minor     7
%define postgresql_altrel    1

# Look at: src/interfaces/libpq/Makefile
%define libpq_major          5

# Look at: src/interfaces/ecpg/ecpglib/Makefile
%define libecpg_major        6

%define libpq_name    libpq%libpq_major
%define libecpg_name  libecpg%libecpg_major

Name: %prog_name%postgresql_major
Version: %postgresql_major.%postgresql_minor
Release: alt%postgresql_altrel

Summary: PostgreSQL client programs and libraries
License: PostgreSQL
Group: Databases
URL: http://www.postgresql.org/

Packager: PostgreSQL Maintainers Team <pgsql@packages.altlinux.org>

%define PGSQL pgsql
%define docdir %_docdir/%prog_name-%version

Source0: %name-%version.tar

Patch2: 0002-Fix-search-for-setproctitle.patch
Patch3: 0003-Use-terminfo-not-termcap.patch
Patch4: 0004-Fix-includedirs.patch
Patch6: 0006-Workaround-for-will-always-overflow-destination-buff.patch
Patch8: 0001-Add-postgresql-startup-method-through-service-1-to-i.patch

Provides: %prog_name = %EVR
Conflicts: %prog_name < %EVR
Conflicts: %prog_name > %EVR
# 1C
Conflicts: %{prog_name}10-1C

BuildRequires: OpenSP docbook-style-dsssl docbook-style-dsssl-utils docbook-style-xsl flex libldap-devel libossp-uuid-devel libpam-devel libreadline-devel libssl-devel libxslt-devel openjade perl-DBI perl-devel postgresql-common python-devel setproctitle-devel tcl-devel xsltproc zlib-devel
BuildRequires: libselinux-devel libkrb5-devel
%if_without devel
BuildRequires: postgresql-devel
%endif
%if_with icu
BuildRequires: libicu-devel
%endif

%description
PostgreSQL is an advanced Object-Relational database management system
(DBMS) that supports almost all SQL constructs (including
transactions, subselects and user-defined types and functions). The
postgresql package includes the client programs and libraries that
you'll need to access a PostgreSQL DBMS server.  These PostgreSQL
client programs are programs that directly manipulate the internal
structure of PostgreSQL databases on a PostgreSQL server. These client
programs can be located on the same machine with the PostgreSQL
server, or may be on a remote machine which accesses a PostgreSQL
server over a network connection. This package contains the docs
in HTML for the whole package, as well as command-line utilities for
managing PostgreSQL databases on a PostgreSQL server.

If you want to manipulate a PostgreSQL database on a remote PostgreSQL
server, you need this package. You also need to install this package
if you're installing the postgresql-server package.

%if_with devel
%package -n %libpq_name
Summary: The shared libraries required for any PostgreSQL clients
Group: Databases
# TODO remove
Provides: libpq5.11 = %EVR
Obsoletes: libpq5.11 < %EVR
#

%description -n %libpq_name
C and C++ libraries to enable user programs to communicate with the
PostgreSQL database backend. The backend can be on another machine and
accessed through TCP/IP.

%package -n %libecpg_name
Summary: Shared library %libecpg_name for PostgreSQL
Group: Databases
Requires: %libpq_name = %EVR
# TODO remove
Provides: libecpg6.11 = %EVR
Obsoletes: libecpg6.11 < %EVR
#

%description -n %libecpg_name
%libecpg_name is used by programs built with ecpg (Embedded PostgreSQL for C)
Use postgresql-dev to develop such programs.

%package -n postgresql-devel
Summary: PostgreSQL development header files
Group: Development/Databases
Requires: %libpq_name = %EVR
Requires: %libecpg_name = %EVR
# TODO remove
Provides: libpq-devel, libecpg-devel, libpq5-devel, libecpg6-devel, libpq5.11-devel, libecpg6.11-devel, postgresql11-devel
Obsoletes: libpq-devel, libecpg-devel, libpq5-devel, libecpg6-devel, libpq5.11-devel, libecpg6.11-devel, postgresql11-devel
#

%description -n postgresql-devel
The postgresql-devel package contains the header files needed to compile applications
which will directly interact with a PostgreSQL database management server.
You need to install this package if you want to develop applications which will interact
with a PostgreSQL server.

%package -n postgresql-devel-static
Summary:  Development static library for postgresql-devel
Group: Development/Databases
Requires: postgresql-devel = %EVR
# TODO remove
Provides: libpq-devel-static, libecpg-devel-static, libpq5-devel-static, libecpg6-devel-static, libpq5.11-devel-static, libecpg6.11-devel-static, postgresql11-devel-static
Obsoletes: libpq-devel-static, libecpg-devel-static, libpq5-devel-static, libecpg6-devel-static, libpq5.11-devel-static, libecpg6.11-devel-static, postgresql11-devel-static
#

%description -n postgresql-devel-static
Development static library for postgresql-devel
%endif

%package docs
Summary: Extra documentation for PostgreSQL
Group: Databases
BuildArch: noarch
# 1C
Conflicts: %{prog_name}10-1C-docs

%description docs
The postgresql-docs package includes the SGML source for the documentation
as well as the documentation in other formats, and some extra documentation.
Install this package if you want to help with the PostgreSQL documentation
project, or if you want to generate printed documentation.

%package contrib
Summary: Contributed source and binaries distributed with PostgreSQL
Group: Databases
Requires: %name-server = %EVR
Provides: %prog_name-contrib = %EVR
# 1C
Conflicts: %{prog_name}10-1C-contrib

%description contrib
The postgresql-contrib package includes the contrib tree distributed with
the PostgreSQL tarball.  Selected contrib modules are prebuilt.

%package server
Summary: The programs needed to create and run a PostgreSQL server
Group: Databases
Requires(pre): shadow-utils, syslogd-daemon, grep, sed
Requires(pre): postgresql-common > 1.0-alt3
Requires: %name = %EVR
Requires: glibc-locales
Provides: %prog_name-server = %EVR
# 1C
Conflicts: %{prog_name}10-1C-server

%description server
The postgresql-server package includes the programs needed to create
and run a PostgreSQL server, which will in turn allow you to create
and maintain PostgreSQL databases.  PostgreSQL is an advanced
Object-Relational database management system (DBMS) that supports
almost all SQL constructs (including transactions, subselects and
user-defined types and functions). You should install
postgresql-server if you want to create and maintain your own
PostgreSQL databases and/or your own PostgreSQL server. You also need
to install the postgresql package.


%package tcl
Summary: The PL/Tcl procedural language for PostgreSQL
Group: Databases
Requires: %name-server = %EVR
Provides: postgresql-tcl
# 1C
Conflicts: %{prog_name}10-1C-tcl

%description tcl
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-tcl package contains the PL/Tcl procedural language
for the backend.

%package perl
Summary: The PL/Perl procedural language for PostgreSQL
Group: Databases
Requires: %name-server = %EVR
Provides: postgresql-perl = %EVR
# 1C
Conflicts: %{prog_name}10-1C-perl

%description perl
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-perl package contains the PL/Perl procedural
language for the backend.

%package python
Summary: Development module for Python code to access a PostgreSQL DB
Group: Databases
Requires: %name-server = %EVR
Provides: postgresql-python = %EVR
# 1C
Conflicts: %{prog_name}10-1C-python

%description python
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-python package includes a module for
developers to use when writing Python code for accessing a PostgreSQL
database.

%prep
%setup

%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch6 -p2
%patch8 -p1

%build
%autoreconf

%configure --includedir=%_includedir/%PGSQL \
--sysconfdir=%_sysconfdir/%PGSQL \
    --datadir=%_datadir/%PGSQL \
    --disable-rpath \
    --enable-nls \
    --enable-thread-safety \
%if_with icu
    --with-icu \
%endif
    --with-docdir=%docdir \
    --with-includes=%_includedir/krb5 \
    --with-pam \
    --with-openssl \
    --with-perl \
    --with-gssapi \
    --with-krb5 \
    --with-ldap \
    --with-tcl --with-tclconfig=%_libdir \
    --with-readline \
    --with-python \
    --with-libxml \
    --with-selinux \
    --with-libxslt \
    --with-gnu-ld \
    --with-ossp-uuid

%make_build pkglibdir=%_libdir/%PGSQL

pushd contrib
%make_build all libdir=%_libdir/%PGSQL/contrib
popd

# adjust dockbook styles
find doc/src/sgml/ -type f -name "stylesheet.*" -print0 | xargs -0 sed -i \
	-e "s,http://docbook.sourceforge.net/release/xsl/current,/usr/share/xml/docbook/xsl-stylesheets,g" --
%make_build -C doc all

%install
%make_build install DESTDIR=%buildroot pkglibdir=%_libdir/%PGSQL
ln -s /usr/include/pgsql %buildroot%_libdir/%PGSQL/pgxs/src/include

%make_build -C doc install DESTDIR=%buildroot docdir=%docdir

##### ALT-stuff
pushd altlinux

# The initscripts....
install -p -m 755 -D %prog_name.init.in %buildroot%_initdir/%prog_name
install -p -m 644 -D %prog_name.service %buildroot%_unitdir/%prog_name.service

# README.ALT
install -p -m 644 -D README.ALT-ru_RU.UTF-8 %buildroot%docdir/README.ALT-ru_RU.UTF-8
install -p -m 644 -D README.rpm-dist %buildroot%docdir/README.rpm-dist

popd
##### end ALT-stuff

sed -e 's|^PGVERSION=.*$|PGVERSION=%version|' \
        -e 's|^PGDOCDIR=.*$|PGDOCDIR=%docdir|' \
        < altlinux/postgresql-check-db-dir >postgresql-check-db-dir
touch -r postgresql-check-db-dir postgresql-check-db-dir
install -m 755 postgresql-check-db-dir %buildroot%_bindir/postgresql-check-db-dir

# Fix initscript versions
sed -i 's,@VERSION@,%postgresql_major,' %buildroot%_initdir/%prog_name
sed -i 's,@FULLVERSION@,%version,' %buildroot%_initdir/%prog_name

# PGDATA needs removal of group and world permissions due to pg_pwd hole.
install -d -m 700 %buildroot%_localstatedir/%PGSQL/data

# backups of data go here...
install -d -m 700 %buildroot%_localstatedir/%PGSQL/backups

# Fix a dangling symlink
mkdir -p %buildroot%_includedir/%PGSQL/port
cp src/include/port/linux.h %buildroot%_includedir/%PGSQL/port/
ln -s port/linux.h %buildroot%_includedir/%PGSQL/os.h
ln -s %_includedir/%PGSQL %buildroot%_includedir/postgresql

pushd contrib
%make_build install DESTDIR=%buildroot pkglibdir=%_libdir/%PGSQL docdir=%docdir
popd

cp -a COPYRIGHT README README.git \
    doc/{KNOWN_BUGS,MISSING_FEATURES,TODO,bug.template} \
    src/tutorial %buildroot%docdir/

%find_lang ecpglib%libecpg_major-%postgresql_major
%find_lang ecpg-%postgresql_major
%find_lang initdb-%postgresql_major
%find_lang libpq%libpq_major-%postgresql_major
%find_lang pg_archivecleanup-%postgresql_major
%find_lang pg_basebackup-%postgresql_major
%find_lang pg_config-%postgresql_major
%find_lang pg_controldata-%postgresql_major
%find_lang pg_ctl-%postgresql_major
%find_lang pg_dump-%postgresql_major
%find_lang pg_resetwal-%postgresql_major
%find_lang pg_rewind-%postgresql_major
%find_lang pg_test_fsync-%postgresql_major
%find_lang pg_test_timing-%postgresql_major
%find_lang pg_upgrade-%postgresql_major
%find_lang pg_verify_checksums-%postgresql_major
%find_lang pg_waldump-%postgresql_major
%find_lang pgscripts-%postgresql_major
%find_lang plperl-%postgresql_major
%find_lang plpgsql-%postgresql_major
%find_lang plpython-%postgresql_major
%find_lang pltcl-%postgresql_major
%find_lang postgres-%postgresql_major
%find_lang psql-%postgresql_major

cat psql-%postgresql_major.lang \
    pg_dump-%postgresql_major.lang \
    pgscripts-%postgresql_major.lang \
    pg_basebackup-%postgresql_major.lang \
    pg_test_fsync-%postgresql_major.lang \
    pg_test_timing-%postgresql_major.lang \
    pg_verify_checksums-%postgresql_major.lang > main.lang

cat postgres-%postgresql_major.lang \
    pg_controldata-%postgresql_major.lang \
    initdb-%postgresql_major.lang \
    pg_ctl-%postgresql_major.lang \
    plpgsql-%postgresql_major.lang \
    pg_rewind-%postgresql_major.lang \
    pg_upgrade-%postgresql_major.lang \
    pg_resetwal-%postgresql_major.lang \
    pg_waldump-%postgresql_major.lang > server.lang

cat pg_config-%postgresql_major.lang > devel.lang

cat ecpg-%postgresql_major.lang \
    ecpglib%libecpg_major-%postgresql_major.lang > ecpg.lang

cat pg_archivecleanup-%postgresql_major.lang > contrib.lang

%pre
# Need to make backups of some executables if an upgrade
# They will be needed to do a dump of the old version's database.
# All output redirected to /dev/null.
exec &>/dev/null
if [ $1 -gt 1 -a -d %_libdir/%PGSQL ]
then
    if [ ! -d %_libdir/%PGSQL/backup ]; then
        mkdir -p %_libdir/%PGSQL/backup
    fi
    cd %_bindir
    cp -fp pg_dump pg_dumpall psql %_libdir/%PGSQL/backup || :
fi

%pre server
exec &>/dev/null

if [ $1 -gt 1 ]
then
   if [ ! -d %_libdir/%PGSQL/backup ]; then
       mkdir -p %_libdir/%PGSQL/backup
   fi
   cd %_bindir
   cp -fp postmaster postgres %_libdir/%PGSQL/backup
fi

%post server
echo PGLIB=%_datadir/%PGSQL >> ~postgres/.bash_profile
echo PGDATA=%_localstatedir/%PGSQL/data >> ~postgres/.bash_profile
echo export PGLIB PGDATA >> ~postgres/.bash_profile
chown postgres:postgres ~postgres/.bash_profile

%post_service %prog_name

%preun server
%preun_service %prog_name

# $2, holds the number of instances of the target package that will remain
# after the operation if $2 is 0, the target package will be removed
%triggerpostun -- %{prog_name}9.3-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}9.4-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}9.5-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}9.6-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}10-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}10-1C-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}11-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%files -f main.lang
%_bindir/clusterdb
%_bindir/createdb
%_bindir/createuser
%_bindir/dropdb
%_bindir/dropuser
%_bindir/pg_dump
%_bindir/pg_dumpall
%_bindir/pg_restore
%_bindir/psql
%_bindir/reindexdb
%_bindir/vacuumdb
%_bindir/pg_basebackup
%_bindir/pg_test_fsync
%_bindir/pg_test_timing
%_bindir/pg_verify_checksums
%_bindir/pg_isready
%_bindir/pg_recvlogical
%_man1dir/clusterdb.1*
%_man1dir/createdb.1*
%_man1dir/createuser.1*
%_man1dir/dropdb.1*
%_man1dir/dropuser.1*
%_man1dir/pg_dump.1*
%_man1dir/pg_restore.1*
%_man1dir/pg_dumpall.1*
%_man1dir/pg_test_fsync.1*
%_man1dir/pg_test_timing.1*
%_man1dir/psql.1*
%_man1dir/reindexdb.1*
%_man1dir/vacuumdb.1*
%_man1dir/pg_basebackup.1*
%_man1dir/pg_isready.1*
%_man1dir/pg_recvlogical.1*
%_man1dir/pg_verify_checksums.1*
%_man7dir/*
%dir %docdir
%docdir/KNOWN_BUGS
%docdir/MISSING_FEATURES
%docdir/TODO
%docdir/COPYRIGHT
%docdir/README
%docdir/README.git
%docdir/bug.template

%files docs
%dir %docdir
%dir %docdir/html
%docdir/html/*.html
%docdir/html/*.css
%dir %docdir/tutorial
%docdir/tutorial/*
%docdir/extension

%files -f contrib.lang contrib
%_bindir/oid2name
%_bindir/pg_standby
%_bindir/pgbench
%_bindir/vacuumlo
%_bindir/pg_archivecleanup

%_man1dir/oid2name.1*
%_man1dir/pg_archivecleanup.1*
%_man1dir/pg_standby.1*
%_man1dir/pgbench.1*
%_man1dir/vacuumlo.1*

%dir %_datadir/%PGSQL/contrib
%dir %_libdir/pgsql

%_libdir/pgsql/_int.so
%_datadir/%PGSQL/extension/intarray-*.sql
%_datadir/%PGSQL/extension/intarray.control
%_libdir/pgsql/adminpack.so
%_datadir/%PGSQL/extension/adminpack-*.sql
%_datadir/%PGSQL/extension/adminpack.control
%_libdir/pgsql/amcheck.so
%_datadir/%PGSQL/extension/amcheck-*.sql
%_datadir/%PGSQL/extension/amcheck.control
%_libdir/pgsql/auth_delay.so
%_libdir/pgsql/auto_explain.so
%_libdir/pgsql/autoinc.so
%_datadir/%PGSQL/extension/autoinc-*.sql
%_datadir/%PGSQL/extension/autoinc.control
%_libdir/pgsql/bloom.so
%_datadir/%PGSQL/extension/bloom-*.sql
%_datadir/%PGSQL/extension/bloom.control
%_libdir/pgsql/btree_gin.so
%_datadir/%PGSQL/extension/btree_gin-*.sql
%_datadir/%PGSQL/extension/btree_gin.control
%_libdir/pgsql/btree_gist.so
%_datadir/%PGSQL/extension/btree_gist-*.sql
%_datadir/%PGSQL/extension/btree_gist.control
%_libdir/pgsql/citext.so
%_datadir/%PGSQL/extension/citext-*.sql
%_datadir/%PGSQL/extension/citext.control
%_libdir/pgsql/cube.so
%_datadir/%PGSQL/extension/cube-*.sql
%_datadir/%PGSQL/extension/cube.control
%_libdir/pgsql/dblink.so
%_datadir/%PGSQL/extension/dblink-*.sql
%_datadir/%PGSQL/extension/dblink.control
%_libdir/pgsql/dict_int.so
%_datadir/%PGSQL/extension/dict_int-*.sql
%_datadir/%PGSQL/extension/dict_int.control
%_libdir/pgsql/dict_xsyn.so
%_datadir/%PGSQL/extension/dict_xsyn-*.sql
%_datadir/%PGSQL/extension/dict_xsyn.control
%_libdir/pgsql/earthdistance.so
%_datadir/%PGSQL/extension/earthdistance-*.sql
%_datadir/%PGSQL/extension/earthdistance.control
%_libdir/pgsql/file_fdw.so
%_datadir/%PGSQL/extension/file_fdw-*.sql
%_datadir/%PGSQL/extension/file_fdw.control
%_libdir/pgsql/fuzzystrmatch.so
%_datadir/%PGSQL/extension/fuzzystrmatch-*.sql
%_datadir/%PGSQL/extension/fuzzystrmatch.control
%_libdir/pgsql/hstore.so
%_datadir/%PGSQL/extension/hstore-*.sql
%_datadir/%PGSQL/extension/hstore.control
%_libdir/pgsql/hstore_plperl.so
%_datadir/%PGSQL/extension/hstore_plperl*.sql
%_datadir/%PGSQL/extension/hstore_plperl*.control
%_libdir/pgsql/hstore_plpython2.so
%_datadir/%PGSQL/extension/hstore_plpython2u-*.sql
%_datadir/%PGSQL/extension/hstore_plpythonu-*.sql
%_datadir/%PGSQL/extension/hstore_plpython2u.control
%_datadir/%PGSQL/extension/hstore_plpythonu.control
%_libdir/pgsql/insert_username.so
%_datadir/%PGSQL/extension/insert_username-*.sql
%_datadir/%PGSQL/extension/insert_username.control
%_datadir/%PGSQL/extension/intagg-*.sql
%_datadir/%PGSQL/extension/intagg.control
%_libdir/pgsql/isn.so
%_datadir/%PGSQL/extension/isn-*.sql
%_datadir/%PGSQL/extension/isn.control
%_libdir/pgsql/jsonb_plperl.so
%_datadir/%PGSQL/extension/jsonb_plperl-*.sql
%_datadir/%PGSQL/extension/jsonb_plperl.control
%_datadir/%PGSQL/extension/jsonb_plperlu-*.sql
%_datadir/%PGSQL/extension/jsonb_plperlu.control
%_libdir/pgsql/jsonb_plpython2.so
%_datadir/%PGSQL/extension/jsonb_plpython2u-*.sql
%_datadir/%PGSQL/extension/jsonb_plpython2u.control
%_datadir/%PGSQL/extension/jsonb_plpythonu-*.sql
%_datadir/%PGSQL/extension/jsonb_plpythonu.control
%_libdir/pgsql/lo.so
%_datadir/%PGSQL/extension/lo-*.sql
%_datadir/%PGSQL/extension/lo.control
%_libdir/pgsql/ltree.so
%_datadir/%PGSQL/extension/ltree-*.sql
%_datadir/%PGSQL/extension/ltree.control
%_libdir/pgsql/ltree_plpython2.so
%_datadir/%PGSQL/extension/ltree_plpython2u-*.sql
%_datadir/%PGSQL/extension/ltree_plpython2u.control
%_datadir/%PGSQL/extension/ltree_plpythonu-*.sql
%_datadir/%PGSQL/extension/ltree_plpythonu.control
%_libdir/pgsql/moddatetime.so
%_datadir/%PGSQL/extension/moddatetime-*.sql
%_datadir/%PGSQL/extension/moddatetime.control
%_libdir/pgsql/pageinspect.so
%_datadir/%PGSQL/extension/pageinspect-*.sql
%_datadir/%PGSQL/extension/pageinspect.control
%_libdir/pgsql/passwordcheck.so
%_libdir/pgsql/pg_buffercache.so
%_datadir/%PGSQL/extension/pg_buffercache-*.sql
%_datadir/%PGSQL/extension/pg_buffercache.control
%_libdir/pgsql/pg_freespacemap.so
%_datadir/%PGSQL/extension/pg_freespacemap-*.sql
%_datadir/%PGSQL/extension/pg_freespacemap.control
%_libdir/pgsql/pg_prewarm.so
%_datadir/%PGSQL/extension/pg_prewarm-*.sql
%_datadir/%PGSQL/extension/pg_prewarm.control
%_libdir/pgsql/pg_stat_statements.so
%_datadir/%PGSQL/extension/pg_stat_statements-*.sql
%_datadir/%PGSQL/extension/pg_stat_statements.control
%_libdir/pgsql/pg_trgm.so
%_datadir/%PGSQL/extension/pg_trgm-*.sql
%_datadir/%PGSQL/extension/pg_trgm.control
%_libdir/pgsql/pg_visibility.so
%_datadir/%PGSQL/extension/pg_visibility-*.sql
%_datadir/%PGSQL/extension/pg_visibility.control
%_libdir/pgsql/pgcrypto.so
%_datadir/%PGSQL/extension/pgcrypto-*.sql
%_datadir/%PGSQL/extension/pgcrypto.control
%_libdir/pgsql/pgoutput.so
%_libdir/pgsql/pgrowlocks.so
%_datadir/%PGSQL/extension/pgrowlocks-*.sql
%_datadir/%PGSQL/extension/pgrowlocks.control
%_libdir/pgsql/pgstattuple.so
%_datadir/%PGSQL/extension/pgstattuple-*.sql
%_datadir/%PGSQL/extension/pgstattuple.control
%_libdir/pgsql/pgxml.so
%_datadir/%PGSQL/extension/xml2-*.sql
%_datadir/%PGSQL/extension/xml2.control
%_libdir/pgsql/postgres_fdw.so
%_datadir/%PGSQL/extension/postgres_fdw-*.sql
%_datadir/%PGSQL/extension/postgres_fdw.control
%_libdir/pgsql/refint.so
%_datadir/%PGSQL/extension/refint-*.sql
%_datadir/%PGSQL/extension/refint.control
%_libdir/pgsql/seg.so
%_datadir/%PGSQL/extension/seg-*.sql
%_datadir/%PGSQL/extension/seg.control
%_libdir/pgsql/sepgsql.so
%_datadir/%PGSQL/contrib/sepgsql.sql
%_libdir/pgsql/sslinfo.so
%_datadir/%PGSQL/extension/sslinfo-*.sql
%_datadir/%PGSQL/extension/sslinfo.control
%_libdir/pgsql/tablefunc.so
%_datadir/%PGSQL/extension/tablefunc-*.sql
%_datadir/%PGSQL/extension/tablefunc.control
%_libdir/pgsql/tcn.so
%_datadir/%PGSQL/extension/tcn-*.sql
%_datadir/%PGSQL/extension/tcn.control
%_libdir/pgsql/test_decoding.so
%_libdir/pgsql/timetravel.so
%_datadir/%PGSQL/extension/timetravel-*.sql
%_datadir/%PGSQL/extension/timetravel.control
%_libdir/pgsql/tsm_system_rows.so
%_datadir/%PGSQL/extension/tsm_system_rows-*.sql
%_datadir/%PGSQL/extension/tsm_system_rows.control
%_libdir/pgsql/tsm_system_time.so
%_datadir/%PGSQL/extension/tsm_system_time-*.sql
%_datadir/%PGSQL/extension/tsm_system_time.control
%_libdir/pgsql/unaccent.so
%_datadir/%PGSQL/extension/unaccent-*.sql
%_datadir/%PGSQL/extension/unaccent.control
%_libdir/pgsql/uuid-ossp.so
%_datadir/%PGSQL/extension/uuid-ossp-*.sql
%_datadir/%PGSQL/extension/uuid-ossp.control

%files -f server.lang server
%config %_initdir/%prog_name
%_bindir/initdb
%_bindir/postgresql-check-db-dir
%_bindir/pg_controldata
%_bindir/pg_ctl
%_bindir/postgres
%_bindir/postmaster
%_bindir/pg_upgrade
%_bindir/pg_rewind
%_bindir/pg_receivewal
%_bindir/pg_resetwal
%_bindir/pg_waldump

%_man1dir/initdb.1*
%_man1dir/pg_controldata.1*
%_man1dir/pg_ctl.1*
%_man1dir/pg_upgrade.1*
%_man1dir/postgres.1*
%_man1dir/postmaster.1*
%_man1dir/pg_rewind.1*
%_man1dir/pg_receivewal.1*
%_man1dir/pg_resetwal.1*
%_man1dir/pg_waldump.1*

%dir %_libdir/%PGSQL
%dir %_datadir/%PGSQL/extension
%_libdir/%PGSQL/plpgsql.so
%_datadir/%PGSQL/extension/plpgsql-*.sql
%_datadir/%PGSQL/extension/plpgsql.control
%_libdir/%PGSQL/dict_snowball.so
%_libdir/%PGSQL/*_and_*.so
%_libdir/%PGSQL/euc2004_sjis2004.so
%_libdir/%PGSQL/libpqwalreceiver.so
%dir %_datadir/%PGSQL
%_datadir/%PGSQL/errcodes.txt
%dir %_datadir/%PGSQL/timezone
%_datadir/%PGSQL/timezone/*
%dir %_datadir/%PGSQL/timezonesets
%_datadir/%PGSQL/timezonesets/*
%dir %_datadir/%PGSQL/tsearch_data
%_datadir/%PGSQL/tsearch_data/*
%_datadir/%PGSQL/postgres.bki
%_datadir/%PGSQL/postgres.description
%_datadir/%PGSQL/postgres.shdescription
%_datadir/%PGSQL/*.sample
%_datadir/%PGSQL/conversion_create.sql
%_datadir/%PGSQL/information_schema.sql
%_datadir/%PGSQL/sql_features.txt
%_datadir/%PGSQL/system_views.sql
%_datadir/%PGSQL/snowball_create.sql
%_localstatedir/%PGSQL
%docdir/README.ALT-ru_RU.UTF-8
%docdir/README.rpm-dist
%attr(700,postgres,postgres)  %dir %_localstatedir/%PGSQL
%attr(700,postgres,postgres)  %dir %_localstatedir/%PGSQL/backups
%attr(700,postgres,postgres)  %dir %_localstatedir/%PGSQL/data
%_unitdir/*

%files -f pltcl-%postgresql_major.lang tcl
%dir %_libdir/%PGSQL
%_libdir/%PGSQL/pltcl.so
%_datadir/%PGSQL/extension/pltcl-*.sql
%_datadir/%PGSQL/extension/pltcl.control
%_datadir/%PGSQL/extension/pltclu-*.sql
%_datadir/%PGSQL/extension/pltclu.control

%files -f plperl-%postgresql_major.lang perl
%dir %_libdir/%PGSQL
%_libdir/%PGSQL/plperl.so
%_datadir/%PGSQL/extension/plperl-*.sql
%_datadir/%PGSQL/extension/plperl.control
%_datadir/%PGSQL/extension/plperlu-*.sql
%_datadir/%PGSQL/extension/plperlu.control

%files -f plpython-%postgresql_major.lang python
%dir %docdir
%dir %_libdir/%PGSQL
%_libdir/%PGSQL/plpython2.so
%_datadir/%PGSQL/extension/plpython2u-*.sql
%_datadir/%PGSQL/extension/plpython2u.control
%_datadir/%PGSQL/extension/plpythonu-*.sql
%_datadir/%PGSQL/extension/plpythonu.control

%if_with devel
%files -f libpq%libpq_major-%postgresql_major.lang -n %libpq_name
%_libdir/libpq.so.%libpq_major
%_libdir/libpq.so.%libpq_major.*

%files -f ecpg.lang -n %libecpg_name
%_libdir/libecpg.so.%libecpg_major
%_libdir/libecpg.so.%libecpg_major.*
%_libdir/libecpg_compat.so.*
%_libdir/libpgtypes.so.*

%files -f devel.lang -n postgresql-devel
%_bindir/ecpg
%_bindir/pg_config
%_includedir/%PGSQL
%_includedir/postgresql
%dir %_libdir/%PGSQL
%dir %_libdir/%PGSQL/pgxs/
%_libdir/libecpg*.so
%_libdir/libpq*.so
%_libdir/libpgtypes.so
%_libdir/%PGSQL/pgxs/*
%_libdir/pkgconfig/libecpg.pc
%_libdir/pkgconfig/libecpg_compat.pc
%_libdir/pkgconfig/libpq.pc
%_libdir/pkgconfig/libpgtypes.pc
%_man1dir/ecpg.*
%_man1dir/pg_config.*
%_man3dir/*

%files -n postgresql-devel-static
%_libdir/libecpg*.a
%_libdir/libpgcommon.a
%_libdir/libpgfeutils.a
%_libdir/libpgtypes.a
%_libdir/libpgport.a
%_libdir/libpq*.a
%endif

%changelog
* Wed Feb 12 2020 Alexei Takaseev <taf@altlinux.org> 11.7-alt1
- 11.7 (Fixes CVE-2020-1720)

* Wed Nov 13 2019 Alexei Takaseev <taf@altlinux.org> 11.6-alt1
- 11.6

* Wed Oct 02 2019 Alexei Takaseev <taf@altlinux.org> 11.5-alt2
- Disable -devel

* Wed Aug 07 2019 Alexei Takaseev <taf@altlinux.org> 11.5-alt1
- 11.5 (Fixes CVE-2019-10208, CVE-2019-10209)

* Thu Jun 20 2019 Alexei Takaseev <taf@altlinux.org> 11.4-alt1
- 11.4 (Fixes CVE-2019-10164)

* Wed May 08 2019 Alexei Takaseev <taf@altlinux.org> 11.3-alt1
- 11.3
- (Fixes CVE-2019-10129, CVE-2019-10130)

* Fri Apr 05 2019 Alexei Takaseev <taf@altlinux.org> 11.2-alt3
- Add temporary provides libpq-devel and libecpg-devel to
  postgresql-devel

* Fri Mar 29 2019 Alexei Takaseev <taf@altlinux.org> 11.2-alt2
- Move *.control and *.sql files from -server to -contrib subpackage
  (Fixes ALT#36271)
- Removed unnecessary minor version in package name libpq and libecpg
- Join subpackages libpq-devel, libecpg-devel and postgresql-devel to
  one postgresql-devel subpackage
- Remove unneeded Conflicts like postgresqlX.Y
- Remove unneeded Conflicts < and > for all subpackages
- Rename postgresqlX-devel to postgresql-devel
- Add Requires to -server for -contrib, -perl, -python and -tcl and subpackages
- Remove unneeded Requires tcl >= 8.4.0-alt1 for -tcl subpackages

* Thu Feb 14 2019 Alexei Takaseev <taf@altlinux.org> 11.2-alt1
- 11.2
- Build with ICU

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 11.1-alt1.1
- rebuild with new perl 5.28.1

* Thu Nov 08 2018 Alexei Takaseev <taf@altlinux.org> 11.1-alt1
- 11.1
- (Fixes CVE-2018-16850)

* Fri Oct 19 2018 Alexei Takaseev <taf@altlinux.org> 11.0-alt2
- Disable package libs for --without devel. This will provide
  one set of libraries for all versions of the PG.

* Thu Oct 18 2018 Alexei Takaseev <taf@altlinux.org> 11.0-alt1
- 11.0

* Thu Sep 27 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt7
- Drop online_analyze and plantuner contribs - performance
  degradation

* Mon Sep 10 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt6
- Another fix conflicts with libpq5.10-1C

* Fri Sep 07 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt5
- Add Obsolete to libpq-1C

* Wed Sep 05 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt4
- Add online_analyze and plantuner contribs

* Tue Sep 04 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt3
- Add BR: libkrb5-devel
- Rebuild with OpenSSL 1.1.x

* Tue Aug 14 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt2
- Change conflict 1C 9.6 -> 1C 10

* Sat Aug 11 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt1
- 10.5
- (Fixes CVE-2018-10915, CVE-2018-10925)

* Wed May 09 2018 Alexei Takaseev <taf@altlinux.org> 10.4-alt1
- 10.4
- (Fixes CVE-2018-1115)

* Fri Mar 02 2018 Alexei Takaseev <taf@altlinux.org> 10.3-alt1
- 10.3
- (Fixes CVE-2018-1058)

* Wed Feb 07 2018 Alexei Takaseev <taf@altlinux.org> 10.2-alt1
- 10.2

* Fri Feb 02 2018 Alexei Takaseev <taf@altlinux.org> 10.1-alt2
- Rename pg_rewind's copy_file_range() to avoid conflict with new linux syscall

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 10.1-alt1.1
- rebuild with new perl 5.26.1

* Thu Nov 09 2017 Alexei Takaseev <taf@altlinux.org> 10.1-alt1
- 10.1
- Remove conflicts to PG 9.1, 9.2
- Cleanup spec
- Remove chroot dead code

* Thu Oct 05 2017 Alexei Takaseev <taf@altlinux.org> 10.0-alt1
- 10.0
- Enable -devel

* Wed Sep 20 2017 Alexei Takaseev <taf@altlinux.org> 10.0-alt0.rc1
- 10.0 rc1

* Wed Aug 30 2017 Alexei Takaseev <taf@altlinux.org> 10.0-alt0.b4
- 10.0 beta4

* Wed Aug 30 2017 Alexei Takaseev <taf@altlinux.org> 9.6.5-alt1
- 9.6.5

* Wed Aug 09 2017 Alexei Takaseev <taf@altlinux.org> 9.6.4-alt1
- 9.6.4
- (Fix CVE-2017-7547)

* Thu May 11 2017 Alexei Takaseev <taf@altlinux.org> 9.6.3-alt2
- Add conflict with postgresql for 1C

* Wed May 10 2017 Alexei Takaseev <taf@altlinux.org> 9.6.3-alt1
- 9.6.3

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 9.6.2-alt1.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Sun Feb 12 2017 Alexei Takaseev <taf@altlinux.org> 9.6.2-alt1
- 9.6.2

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 9.6.1-alt1.1
- rebuild with new perl 5.24.1

* Thu Oct 27 2016 Alexei Takaseev <taf@altlinux.org> 9.6.1-alt1
- 9.6.1

* Thu Sep 29 2016 Alexei Takaseev <taf@altlinux.org> 9.6.0-alt1
- 9.6.0

* Wed Aug 10 2016 Alexei Takaseev <taf@altlinux.org> 9.5.4-alt1
- 9.5.4

* Fri May 13 2016 Alexei Takaseev <taf@altlinux.org> 9.5.3-alt1
- 9.5.3

* Thu Mar 31 2016 Alexei Takaseev <taf@altlinux.org> 9.5.2-alt1
- 9.5.2

* Wed Feb 10 2016 Alexei Takaseev <taf@altlinux.org> 9.5.1-alt1
- 9.5.1

* Thu Jan 14 2016 Alexei Takaseev <taf@altlinux.org> 9.5.0-alt1
- 9.5.0

* Mon Jan 11 2016 Alexei Takaseev <taf@altlinux.org> 9.4.5-alt2
- Fix loss man pages
- Fix build with flex 2.6.0

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 9.4.5-alt1.1
- rebuild with new perl 5.22.0

* Wed Oct 07 2015 Alexei Takaseev <taf@altlinux.org> 9.4.5-alt1
- 9.4.5
- Add symlink /usr/include/postgresql->pgsql (ALT:#28249)

* Sun Jun 14 2015 Alexei Takaseev <taf@altlinux.org> 9.4.4-alt1
- 9.4.4

* Wed Jun 03 2015 Alexei Takaseev <taf@altlinux.org> 9.4.3-alt1
- 9.4.3

* Tue May 26 2015 Alexei Takaseev <taf@altlinux.org> 9.4.2-alt2
- rebuild with rpm-build-4.0.4-alt100.84

* Thu May 21 2015 Alexei Takaseev <taf@altlinux.org> 9.4.2-alt1
- 9.4.2

* Wed Feb 04 2015 Alexei Takaseev <taf@altlinux.org> 9.4.1-alt1
- 9.4.1

* Wed Dec 17 2014 Alexei Takaseev <taf@altlinux.org> 9.4.0-alt1
- 9.4.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 9.3.5-alt1.1
- rebuild with new perl 5.20.1

* Mon Jul 28 2014 Alexei Takaseev <taf@altlinux.org> 9.3.5-alt1
- 9.3.5
- Fix ALT#30197

* Wed Apr 16 2014 Alexei Takaseev <taf@altlinux.org> 9.3.4-alt5
- Add postgresql-devel-static subpackage

* Fri Apr 04 2014 Andriy Stepanov <stanv@altlinux.ru> 9.3.4-alt4
- Remove chroot logic from sysvinit scrtipt

* Thu Apr 03 2014 Alexei Takaseev <taf@altlinux.org> 9.3.4-alt3
- Add postgresql.service
- Add postgresql-check-db-dir for correct start under systemd
- Fix ALT#28562

* Tue Apr 01 2014 Alexei Takaseev <taf@altlinux.org> 9.3.4-alt2
- Fix name libecpg6.3 to libecpg6.5

* Fri Mar 28 2014 Andriy Stepanov <stanv@altlinux.ru> 9.3.4-alt1
- Jump to 9.3.x

* Sat Jan 12 2013 Alexei Takaseev <taf@altlinux.org> 9.2.2-alt1
- 9.2.2

* Sat Dec 29 2012 Alexei Takaseev <taf@altlinux.org> 9.1.7-alt1
- 9.1.7
- Removed unnecessary require to be able to older versions of the
  utilities on the new libraries.Removed unnecessary dependency to
  be able to older versions of the utilities on the new libraries.

* Wed Sep 26 2012 Alexei Takaseev <taf@altlinux.org> 9.1.6-alt1
- 9.1.6

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 9.1.3-alt2
- rebuilt for perl-5.16

* Sat Mar 31 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 9.1.3-alt1
- 9.1.3.
- Package /var/lib/pgsql as a directory.

* Wed Dec 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.1.2-alt1
- 9.1.2.

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.1.1-alt1.1
- Rebuild with Python-2.7.

* Tue Nov 01 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.1.1-alt1
- 9.1.1.
- Enable devel.
- Rediff chroot patch.
- Fix symlink adjustment when chroot mode enabled.

* Tue Oct 11 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.5-alt1
- 9.0.5 (Fixes CVE-2011-2483).
- Disable devel subpackage.

* Wed Apr 27 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.4-alt1
- 9.0.4.
- Write initdb progress messages to stdout instead of syslog.

* Mon Mar 28 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.3-alt2
- Add build dependency on zlib-devel for fix building.

* Wed Feb 09 2011 Alexey Tourbin <at@altlinux.ru> 9.0.3-alt1.1
- rebuilt for debuginfo provides

* Wed Feb 02 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.3-alt1
- 9.0.3 (Fixes CVE-2010-4015).
- Chroot scripts: exit silently when PG_CHROOT_DIR is not set.
- Initscript: remove LOCKFILE when stopping the service.

* Mon Dec 20 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.2-alt1
- 9.0.2.

* Fri Nov 12 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.1-alt4
- Initscript:
  + Introduce "service postgresql initdb" and don't run initdb
    automatically.
  + Use SourceIfNotEmpty for sysconf-file sourcing.
  + Start postgres directly (without wrapping around "start_daemon
    --make-pidfile") and with output redirection to separate
    pgstartup.log (Closes: #19337).
  + When chroot mode enabled, adjust symlink /var/lib/pgsql at every
    startup.
- Unhardcode PG_CHROOT_DIR, let users redefine it (Closes: #22287).
- Return back pg_upgrade.

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 9.0.1-alt3.1
- Rebuilt with perl 5.12.

* Wed Nov 03 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.1-alt3
- Enable -devel subpackage.
- postgresql.init: fix checking of executable path in
  delete_wrong_pidfile(). Before this condstop() has no chance to stop
  running daemon when doing package upgrade.
- Fix locales copying to chroot dir according to change of localedir
  introduced in glibc-locales-2.11.2-alt3.
- postgresql.init: disable autostart on system startup by default.
- Add rpm trigger for properly restoring chkconfig state after upgrading
  postgresql version.
- Don't package pg_upgrade and postgresql-dump.

* Wed Oct 27 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.1-alt2
- Rebuild for Sisyphus (without devel part).
- Run chroot script only when upgrading package (tnx ldv@ for hit).
- Avoid leaving unowned directories after package uninstall.
- Use only local dockbook xsl-stylesheets when building.

* Thu Oct 07 2010 Konstantin Pavlov <thresh@altlinux.org> 9.0.1-alt1
- 9.0.1 release.

* Mon Sep 06 2010 Konstantin Pavlov <thresh@altlinux.org> 9.0.0-alt1.rc1
- 9.0 release candidate 1.

* Wed Aug 11 2010 Konstantin Pavlov <thresh@altlinux.org> 9.0.0-alt1.beta4
- 9.0 beta 4.

* Mon Aug 09 2010 Konstantin Pavlov <thresh@altlinux.org> 8.4.4-alt2
- Copy all locale files in chroot (fixes #23821).

* Wed May 19 2010 Konstantin Pavlov <thresh@altlinux.org> 8.4.4-alt1
- 8.4.4 release.

* Fri Mar 19 2010 Konstantin Pavlov <thresh@altlinux.org> 8.4.3-alt1
- 8.4.3 release.

* Fri Mar 19 2010 Konstantin Pavlov <thresh@altlinux.org> 8.4.2-alt2
- Build contrib with libossp-uuid.

* Thu Mar 04 2010 Konstantin Pavlov <thresh@altlinux.org> 8.4.2-alt1
- 8.4.2 release.
- Use patches by Alexey Novikov (http://gitorious.org/shader-alt/postgresql/).

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.3.8-alt1.1
- Rebuilt with python 2.6

* Sat Nov 07 2009 Michael Bochkaryov <misha@altlinux.ru> 8.3.8-alt1
- 8.3.8

* Sat Sep 05 2009 Michael Bochkaryov <misha@altlinux.ru> 8.3.7-alt4
- Apply buffer overflow patch by Ivan Fedorov

* Sat Aug 01 2009 Michael Bochkaryov <misha@altlinux.ru> 8.3.7-alt3
- fix buffer overflow (import from postgresql-8.3eter)

* Thu Mar 19 2009 Ivan Fedorov <ns@altlinux.org> 8.3.7-alt2
- fix building

* Thu Mar 19 2009 Ivan Fedorov <ns@altlinux.org> 8.3.7-alt1
- 8.3.7

* Thu Nov 06 2008 Ivan Fedorov <ns@altlinux.org> 8.3.5-alt1
- 8.3.5
  + Fix GiST index corruption

* Fri Oct 17 2008 Ivan Fedorov <ns@altlinux.org> 8.3.4-alt2
- fixed #10861, #14576.
- spec cleanup.
- rework contrib subsytem.
- rename libpq subpackages to real names.

* Mon Oct 13 2008 Pavlov Konstantin <thresh@altlinux.ru> 8.3.4-alt1
- updated to 8.3.4 version (fixes #17534).
- added support to use non-chrooted postgresql server, see control postgresql.
- fixed #16683.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 8.3.3-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun Jun 15 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.3-alt1
- updated to 8.3.3 version

* Tue Jun 03 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.1-alt5
- Built with GSSAPI, thanks to Dmitry M. Maslennikov (fix #15877)
- Built with LDAP support

* Tue May 13 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.1-alt4
- fixed tsearch_data directory packaging bug

* Thu Apr 10 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.1-alt3
- LSB compatible init header added
- init script fix (#15269)
- full text search data added
- explicit build with libxml2 and libxslt support

* Sat Mar 29 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.1-alt2
- fix libpq name to avoid unmets

* Fri Mar 28 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.1-alt1
- rebuild for ALT Linux Sisyphus

* Thu Mar 27 2008 Serge A. Ribalchenko <fisher@netstyle.com.ua> 8.3.1-nets1
- chroot patch from postgresql-8.2.4 merged;
- libpgport.a exclude discarded
