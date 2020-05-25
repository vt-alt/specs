# -*- mode: rpm-spec; coding: utf-8 -*-
%def_without devel

# Use ICU
%def_with icu

%define prog_name            postgresql
%define postgresql_major     11
%define postgresql_minor     5
%define postgresql_altrel    5

# Look at: src/interfaces/libpq/Makefile
%define libpq_major          5

# Look at: src/interfaces/ecpg/ecpglib/Makefile
%define libecpg_major        6

%define libpq_name    libpq%libpq_major
%define libecpg_name  libecpg%libecpg_major

Name: %prog_name%postgresql_major-1C
Version: %postgresql_major.%postgresql_minor
Release: alt%postgresql_altrel

Summary: PostgreSQL client programs and libraries (edition for 1C 8.3.13 and later)
License: PostgreSQL
Group: Databases
URL: http://www.postgresql.org/

Packager: PostgreSQL Maintainers Team <pgsql@packages.altlinux.org>

%define PGSQL pgsql
%define docdir %_docdir/%prog_name-%version

Source0: %name-%version.tar
Source1: README.ALT-ru_RU.UTF-8
Source2: README.rpm-dist
Source3: postgresql-check-db-dir
Source4: postgresql.init.in
Source5: postgresql.service

Patch2: 0002-Fix-search-for-setproctitle.patch
Patch3: 0003-Use-terminfo-not-termcap.patch
Patch4: 0004-Fix-includedirs.patch
Patch6: 0006-Workaround-for-will-always-overflow-destination-buff.patch
Patch8: 0001-Add-postgresql-startup-method-through-service-1-to-i.patch

# 1C
Patch101: 00001-1C-FULL.patch

Provides: %prog_name = %EVR
Conflicts: %prog_name < %EVR
Conflicts: %prog_name > %EVR

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
Summary: The shared libraries required for any PostgreSQL clients (edition for 1C 8.3.13 and later)
Group: Databases

%description -n %libpq_name
C and C++ libraries to enable user programs to communicate with the
PostgreSQL database backend. The backend can be on another machine and
accessed through TCP/IP.

%package -n %libecpg_name
Summary: Shared library %libecpg_name for PostgreSQL (edition for 1C 8.3.13 and later)
Group: Databases
Requires: %libpq_name = %EVR

%description -n %libecpg_name
%libecpg_name is used by programs built with ecpg (Embedded PostgreSQL for C)
Use postgresql-dev to develop such programs.

%package -n postgresql-devel
Summary: PostgreSQL development header files (edition for 1C 8.3.13 and later)
Group: Development/Databases
Requires: %libpq_name = %EVR
Requires: %libecpg_name = %EVR

%description -n postgresql-devel
The postgresql-devel package contains the header files needed to compile applications
which will directly interact with a PostgreSQL database management server.
You need to install this package if you want to develop applications which will interact
with a PostgreSQL server.

%package -n postgresql-devel-static
Summary:  Development static library for postgresql-devel (edition for 1C 8.3.13 and later)
Group: Development/Databases
Requires: postgresql-devel = %EVR

%description -n postgresql-devel-static
Development static library for postgresql-devel
%endif

%package docs
Summary: Extra documentation for PostgreSQL (edition for 1C 8.3.13 and later)
Group: Databases
BuildArch: noarch

%description docs
The postgresql-docs package includes the SGML source for the documentation
as well as the documentation in other formats, and some extra documentation.
Install this package if you want to help with the PostgreSQL documentation
project, or if you want to generate printed documentation.

%package contrib
Summary: Contributed source and binaries distributed with PostgreSQL (edition for 1C 8.3.13 and later)
Group: Databases
Requires: %name-server = %EVR
Provides: %prog_name-contrib = %EVR

%description contrib
The postgresql-contrib package includes the contrib tree distributed with (edition for 1C 8.3.13 and later)
the PostgreSQL tarball.  Selected contrib modules are prebuilt.

%package server
Summary: The programs needed to create and run a PostgreSQL server (edition for 1C 8.3.13 and later)
Group: Databases
Requires(pre): shadow-utils, syslogd-daemon, grep, sed
Requires(pre): postgresql-common > 1.0-alt3
Requires: %name = %EVR
Requires: glibc-locales
Provides: %prog_name-server = %EVR

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
Summary: The PL/Tcl procedural language for PostgreSQL (edition for 1C 8.3.13 and later)
Group: Databases
Requires: %name-server = %EVR
Provides: postgresql-tcl

%description tcl
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-tcl package contains the PL/Tcl procedural language
for the backend.

%package perl
Summary: The PL/Perl procedural language for PostgreSQL (edition for 1C 8.3.13 and later)
Group: Databases
Requires: %name-server = %EVR
Provides: postgresql-perl = %EVR

%description perl
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-perl package contains the PL/Perl procedural
language for the backend.

%package python
Summary: Development module for Python code to access a PostgreSQL DB (edition for 1C 8.3.13 and later)
Group: Databases
Requires: %name-server = %EVR
Provides: postgresql-python = %EVR

%description python
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-python package includes a module for
developers to use when writing Python code for accessing a PostgreSQL
database.

%prep
%setup -q

%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch6 -p2
%patch8 -p1

# 1C
%patch101 -p1

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

# The initscripts....
install -p -m755 -D %SOURCE4 %buildroot%_initdir/%prog_name

# README.ALT
install -p -m 644 -D %SOURCE1 %buildroot%docdir/README.ALT-ru_RU.UTF-8
install -p -m 644 -D %SOURCE2 %buildroot%docdir/README.rpm-dist

install -p -m 644 -D %SOURCE5 %buildroot%_unitdir/postgresql.service

##### end ALT-stuff

sed -e 's|^PGVERSION=.*$|PGVERSION=%version|' \
        -e 's|^PGDOCDIR=.*$|PGDOCDIR=%docdir|' \
        < %SOURCE3 >postgresql-check-db-dir
touch -r postgresql-check-db-dir postgresql-check-db-dir
install -m 755 postgresql-check-db-dir %buildroot%_bindir/postgresql-check-db-dir

# Fix initscript versions

sed -i 's,@VERSION@,%postgresql_major,' %buildroot%_initdir/%prog_name
sed -i 's,@FULLVERSION@,%version,' %buildroot%_initdir/%prog_name

# PGDATA needs removal of group and world permissions due to pg_pwd hole.
install -d -m700 %buildroot%_localstatedir/%PGSQL/data

# backups of data go here...
install -d -m700 %buildroot%_localstatedir/%PGSQL/backups

# Fix a dangling symlink
mkdir -p %buildroot%_includedir/%PGSQL/port
cp src/include/port/linux.h %buildroot%_includedir/%PGSQL/port/
ln -s port/linux.h %buildroot%_includedir/%PGSQL/os.h
ln -s %_includedir/%PGSQL %buildroot%_includedir/postgresql

install -dm700 %buildroot%_localstatedir/%PGSQL

pushd contrib
%make_build install DESTDIR=%buildroot pkglibdir=%_libdir/%PGSQL docdir=%docdir
popd

cp -a COPYRIGHT README \
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
%docdir/bug.template

%files docs
%dir %docdir
%dir %docdir/html
%docdir/html/*.html
%docdir/html/*.css
%dir %docdir/tutorial
%docdir/tutorial/*
%docdir/contrib
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
%_libdir/pgsql/fasttrun.so
%_datadir/%PGSQL/extension/fasttrun-*.sql
%_datadir/%PGSQL/extension/fasttrun.control
%_libdir/pgsql/file_fdw.so
%_datadir/%PGSQL/extension/file_fdw-*.sql
%_datadir/%PGSQL/extension/file_fdw.control
%_libdir/pgsql/fulleq.so
%_datadir/%PGSQL/extension/fulleq-*.sql
%_datadir/%PGSQL/extension/fulleq.control
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
%_libdir/pgsql/mchar.so
%_datadir/%PGSQL/extension/mchar-*.sql
%_datadir/%PGSQL/extension/mchar.control
%_libdir/pgsql/moddatetime.so
%_datadir/%PGSQL/extension/moddatetime-*.sql
%_datadir/%PGSQL/extension/moddatetime.control
%_libdir/pgsql/online_analyze.so
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
%_libdir/pgsql/plantuner.so
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
* Fri May 22 2020 Alexei Takaseev <taf@altlinux.org> 11.5-alt5
- Replace all 1C patches by 00001-1C-FULL.patch

* Wed Feb 12 2020 Alexei Takaseev <taf@altlinux.org> 11.5-alt4
- Fix priv checks for ALTER <object> DEPENDS ON EXTENSION (Fixes CVE-2020-1720)

* Tue Feb 04 2020 Alexei Takaseev <taf@altlinux.org> 11.5-alt3
- Add patch from 1C:
    * 00016-empty_materialize.patch
    * 00017-eqjoinsel_hist.patch
    * 00018-explain_tuple_count.patch
    * 00019-aggfix.patch

* Tue Dec 10 2019 Alexei Takaseev <taf@altlinux.org> 11.5-alt2
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00010-joinsel.patch
    * 00015-lessmem.patch

* Tue Oct 29 2019 Alexei Takaseev <taf@altlinux.org> 11.5-alt1
- 11.5
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00004-postgresql-1c-10.patch
    * 00005-coalesce_cost.patch
    * 00006-pg_receivewal.patch
    * 00007-remove_selfjoin.patch
    * 00008-planner_timing.patch
    * 00009-opt_group_by_and_cost_sort.patch
    * 00010-joinsel.patch
    * 00011-max_files_per_process.patch
    * 00012-index_getattr_optimization.patch
    * 00013-notransvalue.patch
    * 00014-optimizer_utils.patch
    * 00015-lessmem.patch

* Fri Oct 25 2019 Alexei Takaseev <taf@altlinux.org> 10.10-alt2
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00004-postgresql-1c-10.patch
    * 00007-remove_selfjoin.patch
    * 00008-planner_timing.patch
    * 00010-joinsel.patch
    * 00015-lessmem.patch

* Wed Aug 07 2019 Alexei Takaseev <taf@altlinux.org> 10.10-alt1
- 10.10 (Fixes CVE-2019-10208)

* Fri Aug 02 2019 Alexei Takaseev <taf@altlinux.org> 10.9-alt2
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00002-online_analyze.patch
    * 00003-plantuner.patch
    * 00004-postgresql-1c-10.patch
    * 00005-coalesce_cost.patch
    * 00007-remove_selfjoin.patch
    * 00009-opt_group_by_and_cost_sort.patch
    * 00010-joinsel.patch
    * 00011-max_files_per_process.patch
    * 00012-index_getattr_optimization.patch
- Add patch from 1C:
    * 00013-notransvalue.patch
    * 00014-optimizer_utils.patch
    * 00015-lessmem.patch

* Thu Jun 20 2019 Alexei Takaseev <taf@altlinux.org> 10.9-alt1
- 10.9 (Fixes CVE-2019-10164)

* Mon May 13 2019 Alexei Takaseev <taf@altlinux.org> 10.8-alt1
- 10.8
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00004-postgresql-1c-10.patch

* Fri Apr 05 2019 Alexei Takaseev <taf@altlinux.org> 10.7-alt3
- Re-applay patches from 1C:
    * 00003-plantuner.patch
    * 00004-postgresql-1c-10.patch
    * 00006-pg_receivewal.patch
    * 00007-remove_selfjoin.patch
    * 00009-opt_group_by_and_cost_sort.patch
    * 00010-joinsel.patch
- Add patch from 1C:
    * 00012-index_getattr_optimization.patch

* Thu Apr 04 2019 Alexei Takaseev <taf@altlinux.org> 10.7-alt2
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

* Thu Feb 14 2019 Alexei Takaseev <taf@altlinux.org> 10.7-alt1
- 10.7

* Mon Feb 04 2019 Alexei Takaseev <taf@altlinux.org> 10.6-alt3
- Re-applay patches from 1C:
    * 00007-remove_selfjoin.patch
    * 00010-joinsel.patch
- Cleanup spec: remove "%%def_without ver_old"

* Wed Jan 30 2019 Alexei Takaseev <taf@altlinux.org> 10.6-alt2
- Build with ICU
- Re-applay patches from 1C:
    * 00002-online_analyze.patch
    * 00004-postgresql-1c-10.patch
- Add patches from 1C:
    * 0009-postgresql-10-logging.patch
    * 00007-remove_selfjoin.patch
    * 00008-planner_timing.patch
    * 00009-opt_group_by~nd_cost_sort.patch
    * 00010-joinsel.patch
    * 00011-max_files_per_process.patch

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 10.6-alt1.1
- rebuild with new perl 5.28.1

* Thu Nov 08 2018 Alexei Takaseev <taf@altlinux.org> 10.6-alt1
- 10.6
- (Fixes CVE-2018-16850)

* Fri Oct 19 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt3
- Disable package libs for --without devel. This will provide
  one set of libraries for all versions of the PG.

* Tue Sep 04 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt2
- Add BR: libkrb5-devel
- Rebuild with OpenSSL 1.1.x

* Sat Aug 11 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt1
- 10.5
- (Fixes CVE-2018-10915, CVE-2018-10925)

* Mon Jul 16 2018 Alexei Takaseev <taf@altlinux.org> 10.4-alt1
- 10.4
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00004-postgresql-1c-10.patch
    * 00005-coalesce_cost.patch
- Remove patches:
    * 00005-exists_opt-2.patch
    * 00006-coalesce_cost-1.patch
    * 00007-drop-orphan-tt.patch
    * 00008-receivexlog-umask.patch
- Add patch:
    * 00006-pg_receivewal.patch

* Wed May 09 2018 Alexei Takaseev <taf@altlinux.org> 9.6.9-alt1
- 9.6.9
- (Fixes CVE-2018-1115)

* Wed Feb 28 2018 Alexei Takaseev <taf@altlinux.org> 9.6.8-alt1
- 9.6.8
- Re-applay patches from 1C:
    * 00001-1c_FULL_96.patch
    * 00004-postgresql-1c-9.6.patch
    * 00005-exists_opt-2.patch
- Remove path 00001-1c_create_append_path.patch (fixed in 00001-1c_FULL_96.patch)
- (Fixes CVE-2018-1058)

* Wed Feb 07 2018 Alexei Takaseev <taf@altlinux.org> 9.6.7-alt1
- 9.6.7
- Add patches:
    * 00001-1c_create_append_path.patch
    * 00005-exists_opt-2.patch
    * 00006-coalesce_cost-1.patch
    * 00007-drop-orphan-tt.patch
    * 00008-receivexlog-umask.patch
- Re-applay patch 00002-online_analyze.patch from 1C
- Remove patch 00003-applock.patch

* Fri Feb 02 2018 Alexei Takaseev <taf@altlinux.org> 9.6.6-alt2
- Rename pg_rewind's copy_file_range() to avoid conflict with new linux syscall

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 9.6.6-alt1.1
- rebuild with new perl 5.26.1

* Thu Nov 09 2017 Alexei Takaseev <taf@altlinux.org> 9.6.6-alt1
- 9.6.6
- Remove conflicts to PG 9.1, 9.2

* Thu Oct 05 2017 Alexei Takaseev <taf@altlinux.org> 9.6.5-alt2
- Add conflicts to PG 10

* Wed Aug 30 2017 Alexei Takaseev <taf@altlinux.org> 9.6.5-alt1
- 9.6.5

* Wed Aug 09 2017 Alexei Takaseev <taf@altlinux.org> 9.6.4-alt1
- 9.6.4
- (Fixes CVE-2017-7547)

* Thu May 11 2017 Alexei Takaseev <taf@altlinux.org> 9.6.3-alt1
- Initial build for ALT Linux Sisyphus
