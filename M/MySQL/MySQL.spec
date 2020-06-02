%define _unpackaged_files_terminate_build 1
%def_without debug
%def_with libs
%def_with devel
#do not build mysql_router until MySQL-Shell arrival
%def_without mysql_router
%def_disable static
%define mysqld_user mysql
%define mysqlrouter_user mysqlrouter
%define _libexecdir %_sbindir
%define ROOT %_localstatedir/mysql
%define ROUTER_ROOT %_localstatedir/mysqlrouter

Name: MySQL
Version: 8.0.20
Release: alt2

Summary: A very fast and reliable SQL database engine
Summary(ru_RU.UTF-8): Очень быстрый и надежный SQL-сервер
Group: Databases
License: GPL / LGPL
Url: http://www.mysql.com/
Packager: MySQL Development Team <mysql@packages.altlinux.org>

Source: %name-%version.tar
Source99: boost.tar
Source1: mysqld.init
Source2: mysql.logrotate
Source3: safe_mysqld
Source4: mysqld_wrapper
Source5: my.cnf
Source6: mysql.chroot.lib
Source7: mysql.chroot.conf
Source8: mysql.chroot.all
Source9: mysql_migrate
Source10: mysqld.sysconfig
Source14: README.ALT-ru_RU.UTF-8
Source15: alt-mysql_install_db.sh
Source16: mysql.control
Source17: mysqld-chroot.control

Source20: mysql.tmpfiles.d
Source21: mysqld.service
Source22: mysqld.service.d-user

Source25: client.cnf
Source26: server.cnf
Source27: mysql-clients.cnf
Source28: chroot.cnf
Source29: no-chroot.cnf
Source30: mysqlrouter.conf 

Patch0: mysql-%version.patch

# ALTLinux
Patch1: mysql-8.0.20-alt-chroot.patch
Patch2: mysql-5.0.20-alt-libdir.patch
Patch4: mysql-8.0.20-alt-client.patch
Patch5: mysql-8.0.12-alt-load_defaults.patch
Patch6: mysql-5.1.50-alt-fPIC-innodb.patch
Patch7: mysql-8.0.12-alt-mysql_config-libs.patch
Patch9: mysql-8.0.18-alt-disable-run-libmysql_api_test.patch

# Patches taken from boost 1.59
Patch115: boost-1.58.0-pool.patch
Patch125: boost-1.57.0-mpl-print.patch

Patch200: mysql-8.0.20-oracle-fix-charset-nullptr.patch

# Automatically added by buildreq on Tue Nov 20 2018 (-bi)
# optimized out: cmake cmake-modules control elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libsasl2-3 libstdc++-devel libtinfo-devel perl pkg-config python-base sh3 xz
BuildRequires: ccmake
BuildRequires: chrooted
BuildRequires: gcc-c++
BuildRequires: libaio-devel
BuildRequires: libedit-devel
BuildRequires: libevent-devel
BuildRequires: liblz4-devel
BuildRequires: libncurses-devel
BuildRequires: libssl-devel
BuildRequires: zlib-devel
BuildRequires: libsystemd-devel
BuildRequires: protobuf-compiler
BuildRequires: libprotobuf-lite-devel

%define soname 21

%package -n libmysqlclient%soname
Summary: Shared libraries for MySQL
Summary(ru_RU.UTF-8): Динамические библиотеки для MySQL
License: LGPL
Group: System/Libraries
Provides: libMySQL = %EVR
Obsoletes: libMySQL < %EVR

%package -n libmysqlclient%soname-devel
Summary: Development header files and libraries for MySQL
Summary(ru_RU.UTF-8): Интерфейс прикладного уровня для разработки программ с MySQL
License: LGPL
Group: Development/C
Requires: libmysqlclient%soname = %EVR
Provides: MySQL-devel = %EVR mysql-devel = %EVR
Obsoletes: MySQL-devel < %EVR mysql-devel < %EVR
Provides: libMySQL-devel = %EVR
Obsoletes: libMySQL-devel < %EVR
Conflicts: libmariadb-devel
Provides: libmysqlclient-devel = %EVR

%package -n libmysqlclient%soname-devel-static
Summary: Development static libraries for MySQL
Summary(ru_RU.UTF-8): Интерфейс прикладного уровня для разработки программ с MySQL
License: LGPL
Group: Development/C
Requires: libmysqlclient%soname-devel = %EVR
Provides: libMySQL-devel-static = %EVR
Obsoletes: libMySQL-devel-static < %EVR
Conflicts: libmariadb-devel-static

%package client
Summary: MySQL Client
Summary(ru_RU.UTF-8): Клиент MySQL
License: GPL
Group: Databases
Provides: mysql-client = %EVR
Obsoletes: mysql-client < %EVR
Conflicts: mariadb-client

%package server
Summary: A very fast and reliable SQL database engine
Summary(ru_RU.UTF-8): Очень быстрый и надежный SQL-сервер
License: GPL
Group: Databases
Requires(pre): MySQL-client = %EVR
Requires(pre): shadow-utils, coreutils, glibc-locales
Requires(post,preun): chkconfig, chrooted, coreutils, findutils, grep, sed
Provides: mysql-server = %EVR MySQL = %EVR mysql = %EVR community-mysql = %EVR
Obsoletes: mysql-server < %EVR MySQL < %EVR mysql < %EVR
Conflicts: mariadb-server-control mariadb-common

%package server-perl
Summary: Perl utils for MySQL-server
Summary(ru_RU.UTF-8): Perl-утилиты для MySQL-server
License: GPL
Group: Databases
Requires: MySQL-server = %EVR, perl-DBD-mysql
BuildArch: noarch

%if_with mysql_router
%package router
Summary: MySQL Router
Summary(ru_RU.UTF-8): MySQL Router
License: GPL
Group: Databases
Provides: mysql-router = %EVR
Obsoletes: mysql-router < %EVR
%endif

%define see_base For a description of MySQL see the base MySQL RPM or %url
%define see_base_ru Подробное описание смотрите в пакете MySQL или на %url

%description
MySQL is a true multi-user, multi-threaded SQL (Structured Query
Language) database server. MySQL is a client/server implementation
that consists of a server daemon (mysqld) and many different client
programs/libraries.

The main goals of MySQL are speed, robustness and ease of use.  MySQL
was originally developed because we needed a SQL server that could
handle very big databases with magnitude higher speed than what any
database vendor could offer to us. And since we did not need all the
features that made their server slow we made our own. We have now been
using MySQL since 1996 in a environment with more than 40 databases,
10,000 tables, of which more than 500 have more than 7 million
rows. This is about 200G of data.

The base upon which MySQL is built is a set of routines that have been
used in a highly demanding production environment for many
years. While MySQL is still in development, it already offers a rich
and highly useful function set.

This version allows to use transactions with BDB tables and extended
character set support. See the documentation for more information

%description -l ru_RU.UTF-8
MySQL - это многопользовательский, многопоточный SQL-сервер (SQL -
структурированный язык запросов) баз данных. MySQL построен по технологии
клиент/сервер и включает в себя сервер mysqld и набор различных клиентских
программ и библиотек разработчиков.

Козыри MySQL - скорость, надежность и простота использования. Разработка
MySQL ведется на основе программного кода, который используется в
критических промышленных приложениях уже в течение многих лет. Несмотря на
то, что MySQL только разрабатывается, он уже предоставляет богатый и очень
полезный набор функций.

Данная версия MySQL собрана с поддержкой транзакций и расширенной поддержкой
различных текстовых кодировок. См. документацию для более подробной информации.

%description server
MySQL is a true multi-user, multi-threaded SQL (Structured Query
Language) database server. MySQL is a client/server implementation
that consists of a server daemon (mysqld) and many different client
programs/libraries.

The main goals of MySQL are speed, robustness and ease of use.  MySQL
was originally developed because we needed a SQL server that could
handle very big databases with magnitude higher speed than what any
database vendor could offer to us. And since we did not need all the
features that made their server slow we made our own. We have now been
using MySQL since 1996 in a environment with more than 40 databases,
10,000 tables, of which more than 500 have more than 7 million
rows. This is about 200G of data.

The base upon which MySQL is built is a set of routines that have been
used in a highly demanding production environment for many
years. While MySQL is still in development, it already offers a rich
and highly useful function set.

This version allows to use transactions with BDB tables and extended
character set support. See the documentation for more information.

By default, MySQL server runs in safe chrooted environment with own uid and gid.

%description server-perl
MySQL is a true multi-user, multi-threaded SQL (Structured Query
Language) database server. MySQL is a client/server implementation
that consists of a server daemon (mysqld) and many different client
programs/libraries.
This package contents perl utils for MySQL-server.

%description server -l ru_RU.UTF-8
MySQL - это многопользовательский, многопоточный SQL-сервер (SQL -
структурированный язык запросов) баз данных. MySQL построен по технологии
клиент/сервер и включает в себя сервер mysqld и набор различных клиентских
программ и библиотек разработчиков.

Козыри MySQL - скорость, надежность и простота использования. Разработка
MySQL ведется на основе программного кода, который используется в
критических промышленных приложениях уже в течение многих лет. Несмотря на
то, что MySQL только разрабатывается, он уже предоставляет богатый и очень
полезный набор функций.

Данная версия MySQL собрана с поддержкой транзакций и расширенной поддержкой
различных текстовых кодировок. См. документацию для более подробной информации.

%description -n libmysqlclient%soname
This package contains the shared libraries (*.so*) which certain
languages and applications need to dynamically load and use MySQL.

%description -n libmysqlclient%soname -l ru_RU.UTF-8
Этот пакет содержит динамически загружаемые библиотеки (файлы *.so*),
требуемые для работы большинства клиентских приложений, взаимодействующих
с СУБД MySQL.

%description -n libmysqlclient%soname-devel
This package contains the development header files and libraries
necessary to develop MySQL client applications.

%see_base

%description -n libmysqlclient%soname-devel -l ru_RU.UTF-8
Этот пакет содержит файлы заголовков и библиотеки интерфейса
прикладного уровня, необходимые для разработки клиентских
приложений, взаимодействующих с SQL-сервером MySQL.

%see_base_ru

%description -n libmysqlclient%soname-devel-static
This package contains the development libraries for static linking
necessary to develop MySQL client applications.

%see_base

%description -n libmysqlclient%soname-devel-static -l ru_RU.UTF-8
Этот пакет содержит статические библиотеки интерфейса прикладного уровня,
необходимые для разработки клиентских приложений,
взаимодействующих с SQL-сервером MySQL.

%see_base_ru

%description client
This package contains the standard MySQL clients.

%see_base

%description client -l ru_RU.UTF-8
Этот пакет содержит стандартные клиентские программы для SQL-сервера MySQL

%see_base_ru

%if_with mysql_router
%description router 
This package contains MySQL Router utility.

 MySQL Router is a building block for high availability (HA) solutions. It
simplifies application development by intelligently routing connections to
MySQL servers for increased performance and reliability.

 MySQL Router 8 fully supports MySQL 5.7 and MySQL 8, and it replaces the
MySQL Router 2.x series. If you currently use Router 2.0 or 2.1 then we
recommend upgrading your installation to MySQL Router 8.

%see_base

%description router -l ru_RU.UTF-8
Этот пакет содержит утилиту MySQL Router.

 MySQL Router является составной частью для построения отказоустойчивых решений
высокой доступности. Он упрощает разработку приложений осуществляя
перенаправление подключений к MySQL серверам для обеспечения большего
быстродействия и надежности.

 MySQL Router 8 полностью поддерживает MySQL 5.7 и MySQL 8, заменяя собой
линейку MySQL Router 2.x. Если Вы в настоящий момент используете Router 2.0 или
2.1, то рекомендуется переход на MySQL Router 8.

%see_base_ru
%endif

%prep
%setup -a99
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch9 -p1

# Patch Boost
pushd boost/boost_1_70_0
%patch115 -p0
%patch125 -p1
popd

%patch200 -p1

# with patch4
# Prepare commands list for completion in mysql client.
sed -n 's/^\([[:space:]]*{[[:space:]]*SYM.*(\)\("[&<=>|!A-Z][^"]*"\).*/{\2,0, 0, 0, ""},/p' <sql/lex.h >client/mysql_symbols.inc

%if_without mysql_router
sed -i 's/ADD_SUBDIRECTORY(router)/# ADD_SUBDIRECTORY(router)/' CMakeLists.txt
%endif

%build

%cmake \
	-DBUILD_CONFIG=mysql_release \
	-DFEATURE_SET="community" \
	-DINSTALL_LAYOUT=RPM \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
	-DCMAKE_C_FLAGS:STRING="$CFLAGS" \
	-DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS" \
	-DCMAKE_INSTALL_PREFIX="%_prefix" \
	-DSYSCONFDIR="%_sysconfdir" \
	-DSYSCONF2DIR="%_sysconfdir/my.cnf.d" \
	-DINSTALL_INCLUDEDIR=include/mysql \
	-DINSTALL_INFODIR=share/info \
	-DINSTALL_LIBDIR="%_lib" \
	-DINSTALL_MANDIR=share/man \
	-DINSTALL_MYSQLSHAREDIR=share/mysql \
	-DINSTALL_MYSQLTESTDIR=share/mysql-test \
	-DINSTALL_PLUGINDIR="%_lib/mysql/plugin" \
	-DINSTALL_SBINDIR=sbin \
	-DINSTALL_SCRIPTDIR=sbin \
	-DINSTALL_SUPPORTFILESDIR=share/mysql \
	-DINSTALL_MYSQLDATADIR="%ROOT" \
	-DINSTALL_MYSQLKEYRINGDIR="/var/lib/mysql-keyring" \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DMYSQL_UNIX_ADDR="%ROOT/mysql.sock" \
	-DMYSQL_DATADIR="%ROOT" \
	-DMYSQL_USER=mysql \
	-DWITH_SSL=system \
	-DWITH_ZLIB=system \
	-DWITH_LZ4=system \
	-DWITH_LIBEVENT=system \
	-DWITH_EDITLINE=system \
	-DWITH_PROTOBUF=system \
	-DWITH_PIC=ON \
	-DWITH_EXTRA_CHARSETS=all \
	-DWITH_ARCHIVE_STORAGE_ENGINE=ON \
	-DWITH_BLACKHOLE_STORAGE_ENGINE=ON \
	-DWITH_INNOBASE_STORAGE_ENGINE=ON \
	-DWITH_PARTITION_STORAGE_ENGINE=ON \
	-DWITH_FEDERATED_STORAGE_ENGINE=ON \
	-DWITHOUT_EXAMPLE_STORAGE_ENGINE=ON \
	-DENABLED_LOCAL_INFILE=ON \
	-DWITH_READLINE=OFF \
	-DWITH_SYSTEMD=ON \
	-DCMAKE_C_FLAGS="%optflags" \
	-DCMAKE_CXX_FLAGS="%optflags" \
	-DWITH_BOOST=../boost/boost_1_70_0 \
	-DCOMPILATION_COMMENT="(%distribution)" \
%if_with debug
	-DWITH_DEBUG=1 \
%endif
	-DMYSQL_SERVER_SUFFIX="-%release"

%cmake_build

%install
mkdir -p %buildroot{%_bindir,%_sbindir,%_includedir,%_mandir,%_datadir,/var/log/mysql}
mkdir -p %buildroot%ROOT/{etc,/%_lib,%_libdir,%_libdir/mysql/plugin/,dev,log,tmp,/var/{nis,yp/binding},db/mysql,usr/share/mysql/charsets}
touch %buildroot%ROOT{%_sysconfdir/{hosts,services,{host,nsswitch,resolv}.conf},/dev/urandom,/var/nis/NIS_COLD_START}
%if_with mysql_router
mkdir -p %buildroot%ROUTER_ROOT/{log,data/{,keyring},run}
%endif

%cmakeinstall_std


# Install various helper scripts.
install -pD -m755 %SOURCE1 %buildroot%_initdir/mysqld
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/mysql
install -pD -m755 %SOURCE3 %buildroot%_sbindir/safe_mysqld
install -pD -m755 %SOURCE4 %buildroot%_sbindir/mysqld_wrapper
install -pD -m750 %SOURCE6 %buildroot%_sysconfdir/chroot.d/mysql.lib
%if "%_libdir" == "/usr/lib64"
sed -i s,usr/lib,usr/lib64,g %buildroot%_sysconfdir/chroot.d/mysql.lib
%endif
install -pD -m750 %SOURCE7 %buildroot%_sysconfdir/chroot.d/mysql.conf
install -pD -m750 %SOURCE8 %buildroot%_sysconfdir/chroot.d/mysql.all
install -pD -m750 %SOURCE9 %buildroot%_sbindir/mysql_migrate
install -pD -m644 %SOURCE10 %buildroot%_sysconfdir/sysconfig/mysqld
install -pD -m755 %SOURCE16 %buildroot%_controldir/mysqld
install -pD -m755 %SOURCE17 %buildroot%_controldir/mysqld-chroot

# Backwards compatibility symlinks (ALT #14863)
ln -snf ../sbin/safe_mysqld %buildroot%_bindir/mysqld_safe

%if_with debug
ln -snf ../sbin/mysqld-debug %buildroot%_sbindir/mysqld
%endif

# delete deprecated
rm -f %buildroot%_bindir/mysql_install_db

# Install configuration files.
install -pD -m644 %SOURCE5 %buildroot%_sysconfdir/my.cnf
install -pD -m644 %SOURCE25 %buildroot%_sysconfdir/my.cnf.d/client.cnf
install -pD -m644 %SOURCE26 %buildroot%_sysconfdir/my.cnf.d/server.cnf
install -pD -m644 %SOURCE27 %buildroot%_sysconfdir/my.cnf.d/mysql-clients.cnf
install -pD -m644 %SOURCE28 %buildroot%_sysconfdir/my.cnf.server/chroot.cnf
install -pD -m644 %SOURCE29 %buildroot%_sysconfdir/my.cnf.server/no-chroot.cnf

install -pD -m644 %SOURCE20 %buildroot%_tmpfilesdir/mysql.conf
install -pD -m644 %SOURCE21 %buildroot%_unitdir/mysqld.service
install -pD -m644 %SOURCE22 %buildroot%_sysconfdir/systemd/system/mysqld.service.d/user.conf
%if_with mysql_router
install -pD -m644 %SOURCE30 %buildroot%_sysconfdir/mysqlrouter/mysqlrouter.conf
%endif

# Fix libmysqlclient_r symlinks
(
	cd %buildroot%_libdir
	N="libmysqlclient_r.so"
	for l in $N.*; do
		if [ -h $l ]; then
			t=${l#$N}
			ln -sf libmysqlclient.so$t $N$t
		fi
	done
)

# Populate chroot with data to some extent.
install -pD -m644 %buildroot%_datadir/mysql/charsets/* \
		     %buildroot%ROOT%_datadir/mysql/charsets

(
	cd %buildroot%_datadir/mysql
	for i in */errmsg.sys; do
		install -pD -m644 $i  %buildroot%ROOT%_datadir/mysql/$i
	done
)


mkdir -p %buildroot%_docdir/MySQL-%version
install -p -m644 README %SOURCE14 %buildroot%_docdir/MySQL-%version

rm -f %buildroot%_bindir/safe_mysqld
rm -f %buildroot%_datadir/mysql/mysql{-*.spec,-log-rotate,.server}

touch %buildroot%ROOT/log/queries
touch %buildroot%_logdir/mysql/info

install -p -m 0750 -d %buildroot%_localstatedir/mysql-files
install -p -m 0700 -d %buildroot%_localstatedir/mysql-keyring

# not needed in rpm package
rm -rf %buildroot%_datadir/mysql-test
rm -f %buildroot%_libdir/mysql/plugin/*.la
rmdir %buildroot%_libdir/mysql/plugin/debug
rm -f %buildroot%_bindir/mysql_embedded
rm -f %buildroot%_libdir/mysql/*.a
rm -f %buildroot%_datadir/mysql/magic
rm -f %buildroot%_datadir/mysql/mysqld_multi.server
rm -f %buildroot%_bindir/mysqld_pre_systemd
rm -f %buildroot%_libdir/libmysqlservices.a
rm -f %buildroot%_unitdir/mysqld@.service
rm -f %buildroot%_bindir/comp_err
%if_disabled static
rm -f %buildroot%_libdir/libmysqlclient*.a
%endif

# broken manpages referencing missing paths
rm -f %buildroot%_man1dir/mysql{_client_,}test_embedded.1
rm -fr %buildroot/usr/share/info

%define get_datadir \
DATADIR=`/usr/bin/my_print_defaults mysqld |sed -ne 's/^--datadir=\\(.*\\)/\\1/pg' |tail -1` \
[ -n "$DATADIR" ] || { echo "Failed to read configuration"; exit 1; }

%if_with mysql_router 
%pre router
/usr/sbin/groupadd -r -f %mysqlrouter_user
/usr/sbin/useradd -r -g %mysqlrouter_user -d %ROUTER_ROOT -s /dev/null -c "MySQL router" -n %mysqlrouter_user >/dev/null 2>&1 ||:
if [ -e /etc/mysqlrouter/mysqlrouter.conf -a ! -e /etc/mysqlrouter/mysqlrouter.conf.rename ]; then
        mv -v /etc/mysqlrouter/mysqlrouter.conf /etc/mysqlrouter/mysqlrouter.conf.rename &&
        chown 0:0 /etc/mysqlrouter/mysqlrouter.conf.rename &&
        chmod 600 /etc/mysqlrouter/mysqlrouter.conf.rename ||
        { echo "Error moving mysqlrouter.conf" >&2; exit 1; }
fi

%post router
if [ -f /etc/mysqlrouter/mysqlrouter.conf.rename -a ! -L /etc/mysqlrouter/mysqlrouter.conf.rename -a ! -e /etc/mysqlrouter/mysqlrouter.conf ]; then
        mv -fv /etc/mysqlrouter/mysqlrouter.conf /etc/mysqlrouter/mysqlrouter.conf.rpmnew &&
        mv -v /etc/mysqlrouter/mysqlrouter.conf.rename /etc/mysqlrouter/mysqlrouter.conf &&
        chown 0:0 /etc/mysqlrouter/mysqlrouter.conf &&
        chmod 600 /etc/mysqlrouter/mysqlrouter.conf ||
        { echo "Error moving mysqlrouter/mysqlrouter.conf" >&2; mv -v /etc/mysqlrouter/mysqlrouter.conf.rename /etc/mysqlrouter/mysqlrouter.conf; }
fi
%endif

%postun server
if [ $1 = 0 ]; then
	rm -f %ROOT/lib/* %ROOT/var/yp/binding/*
fi

%preun server
%preun_service mysqld

%pre server
/usr/sbin/groupadd -r -f %mysqld_user
/usr/sbin/useradd -r -g %mysqld_user -d %ROOT -s /dev/null -c "MySQL server" -n %mysqld_user >/dev/null 2>&1 ||:

if [ ! -e %ROOT/my.cnf -a -f /etc/my.cnf -a ! -L /etc/my.cnf -a ! -e /etc/my.cnf.rename ]; then
	mv -v /etc/my.cnf /etc/my.cnf.rename &&
	chown 0:0 /etc/my.cnf.rename &&
	chmod 600 /etc/my.cnf.rename ||
	{ echo "Error moving my.cnf" >&2; exit 1; }
fi

%pre_control mysqld
%pre_control mysqld-chroot

echo "########################################################################"
echo "#              Attention! MySQL upgrade to %version                      #"
echo "########################################################################"
echo "#  Please beware: database format upgrade function has been moved      #"
echo "# from mysql_upgrade utility to mysqld server daemon since 8.0.16      #"
echo "#  DB upgrade attempt will be performed automatically after server     #"
echo "# package update. This can take the time, so wait patiently, please... #"
echo "#  If failure occures please refer to following manuals to recover:    #"
echo "# https://mysqlserverteam.com/mysql-8-0-16-mysql_upgrade-is-going-away #"
echo "# https://dev.mysql.com/doc/refman/8.0/en/upgrading.html               #"
echo "# https://dev.mysql.com/doc/refman/8.0/en/rebuilding-tables.html       #"
echo "########################################################################"

%post server
if [ -f /etc/my.cnf.rename -a ! -L /etc/my.cnf.rename -a ! -e /etc/my.cnf ]; then
	mv -fv %ROOT/my.cnf %ROOT/my.cnf.rpmnew &&
	mv -v /etc/my.cnf.rename %ROOT/my.cnf &&
	chown 0:0 %ROOT/my.cnf &&
	chmod 600 %ROOT/my.cnf ||
	{ echo "Error moving my.cnf" >&2; mv -v /etc/my.cnf.rename /etc/my.cnf; }
fi

if grep "^[[:space:]]*skip-bdb[[:space:]]*$" /var/lib/mysql/my.cnf > /dev/null 2>&1; then
	sed -i "s/^[[:space:]]*skip-bdb[[:space:]]*$/#skip-bdb/" /var/lib/mysql/my.cnf;
fi

if grep "^[[:space:]]*bdb-logdir=" /var/lib/mysql/my.cnf > /dev/null 2>&1; then
	sed -i "s/^[[:space:]]*bdb-logdir=/#bdb-logdir=/" /var/lib/mysql/my.cnf;
fi


if grep "^[[:space:]]*skip-locking[[:space:]]*$" /var/lib/mysql/my.cnf > /dev/null 2>&1; then
	sed -i "s/^[[:space:]]*skip-locking[[:space:]]*$/skip-external-locking/" /var/lib/mysql/my.cnf;
fi

rm -rf %ROOT/dev
%_sysconfdir/chroot.d/mysql.all force

%post_control -s local mysqld
%post_control -s enabled mysqld-chroot


# see also http://dev.mysql.com/doc/refman/5.5/en/upgrading.html
%get_datadir
if [ "$DATADIR" = / ]; then
	# Have to update configuration manually.
	sed -i 's,^datadir=/$,datadir=/db,g' /etc/my.cnf &&
		DATADIR=`/usr/bin/my_print_defaults mysqld |sed -ne 's/^--datadir=\(.*\)/\1/pg' |tail -1` ||
		{ echo "Failed to update configuration"; exit 1; }
fi

NEED_RESTART=
if [ -f "%ROOT/mysql/db.frm" -a ! -f "%ROOT$DATADIR/mysql/db.frm" ]; then
	%_initdir/mysqld status &>/dev/null && %_initdir/mysqld stop && NEED_RESTART=1 ||:
	(cd %ROOT
	install -d -m750 -o %mysqld_user -g adm ".$DATADIR"
	for d in `find -mindepth 1 -maxdepth 1 -type d |grep -Ev '\./(dev|etc|lib|log|tmp|db)$'`; do
		mv -i "$d" ".$DATADIR/$d"
	done)
	echo "Database root have been moved to $DATADIR"
fi

# refer to https://bugs.mysql.com/bug.php?id=95165
if [ -f "%ROOT$DATADIR/mysql_upgrade_info" ]; then
        echo "MySQL-server: %ROOT$DATADIR/mysql_upgrade_info present - changing owner to %mysqld_user:%mysqld_user"
        chown %mysqld_user:%mysqld_user %ROOT$DATADIR/mysql_upgrade_info
fi

if [ -n "$NEED_RESTART" ]; then
	%_initdir/mysqld start ||:
else
	%post_service mysqld
fi

%triggerin server -- MySQL-server < 5.7.21-alt1
#if pre 5.7.21 installation of server have never been run, we should
#remove empty /var/lib/mysql/db/mysql dir to enable --initialize sequence
%get_datadir
# look for empty dir 
if [ "$(ls -A %ROOT$DATADIR/mysql)" ]; then
#     echo "Database dir is not Empty"
     echo "%ROOT$DATADIR/mysql"
else
#    echo "Database dir is Empty, removing"
    rmdir %ROOT$DATADIR/mysql ||:
fi

echo "####################################################################"
echo "#              Attention! MySQL upgrade 5.5.xx -> %version           #"
echo "####################################################################"
echo "#  Please backup your data before you start conversion!            #"
echo "#  You may need database format conversion for correct operation:  #"
echo "# 1. run server: /usr/sbin/mysqld -C utf8 --skip-grant-tables &    #"
echo "# 2. run converter:  /usr/bin/mysql_upgrade                        #"
echo "#  To ensure the conversion succeeded:                             #"
echo "# 3. cat %ROOT$DATADIR/mysql_upgrade_info                      #"
echo "# MySQL version should be displayed as: \"%version\"                   #"
echo "####################################################################"

%triggerpostun server -- MySQL-server < 5.5.28-alt1
%get_datadir
# they've moved innodb to plugins in later 5.1 just to move it back in 5.5, sigh
if [ -f /var/lib/mysql/my.cnf -a -f "%ROOT$DATADIR/ibdata1" ]; then
	if grep "^plugin-load=innodb=ha_innodb_plugin\.so" /var/lib/mysql/my.cnf; then
		echo "  WARNING: if InnoDB is used, please examine /var/lib/mysql/my.cnf*"
		echo "  and ensure that the *builtin* innodb is in use again"
	fi
fi

%if_with libs
%files -n libmysqlclient%soname
%_libdir/libmysqlclient*.so.*
%endif

%if_with devel
%files -n libmysqlclient%soname-devel
%_bindir/mysql_config
%_libdir/libmysqlclient*.so
%_includedir/*
%_man1dir/mysql_config.1*
%_aclocaldir/mysql.m4
%_pkgconfigdir/*.pc
%endif

%if_enabled static
%files -n libmysqlclient%soname-devel-static
%_libdir/libmysqlclient*.a
%_libdir/mysql
%_pkgconfigdir/*.pc
%endif

%files client
%dir %_sysconfdir/my.cnf.d
%config(noreplace) %_sysconfdir/my.cnf.d/client.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/mysql-clients.cnf
%_bindir/innochecksum
%_bindir/my_print_defaults
%_bindir/mysql
%_bindir/mysql_client_test
%_bindir/mysqladmin
%_bindir/mysqlbinlog
%_bindir/mysqlcheck
%_bindir/mysqldump
%_bindir/mysqlimport
%_bindir/mysqlpump
%_bindir/mysqlshow
%_bindir/mysqltest
%_bindir/mysqltest_safe_process
%_bindir/mysqlxtest
%_bindir/mysqlslap
%_bindir/mysql_config_editor
%_bindir/ibd2sdi
%_bindir/perror
%_bindir/zlib_decompress
%_mandir/man?/*
%exclude %_man1dir/mysql_config.1*

%if_with mysql_router
%files router
%config(noreplace) %_sysconfdir/mysqlrouter/mysqlrouter.conf
%dir %_libdir/mysqlrouter
%_libdir/mysqlrouter/*
%_libdir/libmysqlrouter.so*
%_libdir/libmysqlharness.so*
%_bindir/mysqlrouter
%_bindir/mysqlrouter_plugin_info
%attr(3771,root,mysqlrouter) %dir %ROUTER_ROOT
%attr(3770,root,mysqlrouter) %dir %ROUTER_ROOT/data
%attr(750,mysqlrouter,mysqlrouter) %ROUTER_ROOT/data/keyring
%attr(3770,root,mysqlrouter) %dir %ROUTER_ROOT/run
%attr(3770,root,mysqlrouter) %dir %ROUTER_ROOT/log
%endif

%files server-perl
%_bindir/mysqldumpslow

%files server
%_initdir/*
%config(noreplace) %_sysconfdir/sysconfig/*
%config(noreplace) %_sysconfdir/logrotate.d/*
%config(noreplace) %_sysconfdir/control.d/facilities/*
%config %_sysconfdir/chroot.d/*
%config(noreplace) %_sysconfdir/my.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/server.cnf
%_sysconfdir/my.cnf.server
%config(noreplace) %_sysconfdir/my.cnf.server/*.cnf
%_tmpfilesdir/mysql.conf
%_unitdir/mysqld.service
%config(noreplace) %_sysconfdir/systemd/system/mysqld.service.d/user.conf

%_bindir/*isam*
%_bindir/mysql_secure_installation
%_bindir/mysql_ssl_rsa_setup
%_bindir/mysql_tzinfo_to_sql
%_bindir/mysql_upgrade
%_bindir/mysqld_safe
%_sbindir/*
%_libdir/mysql/plugin
%_datadir/mysql
%attr(750,root,adm) %dir /var/log/mysql
%ghost %verify(not md5 mtime size) /var/log/mysql/*
%attr(0770,root,mysql) %dir %_localstatedir/mysql-files
%attr(0700,mysql,mysql) %dir %_localstatedir/mysql-keyring
%dir %_docdir/MySQL-%version
%_docdir/MySQL-%version/README*
%attr(3771,root,mysql) %dir %ROOT
%attr(710,root,mysql) %dir %ROOT/%_lib
%attr(710,root,mysql) %dir %ROOT/%_libdir
%attr(710,root,mysql) %dir %ROOT/%_libdir/mysql
%attr(710,root,mysql) %dir %ROOT/%_libdir/mysql/plugin
%attr(710,root,mysql) %dir %ROOT%_sysconfdir
%ghost %ROOT%_sysconfdir/hosts
%ghost %ROOT%_sysconfdir/services
%ghost %ROOT%_sysconfdir/*.conf
%dir %ROOT/dev
%ghost %ROOT/dev/urandom
%attr(710,root,mysql) %dir %ROOT/var
%dir %ROOT/var/nis
%ghost %ROOT/var/nis/NIS_COLD_START
%dir %ROOT/var/yp
%dir %ROOT/var/yp/binding
%dir %ROOT/usr
%dir %ROOT%_datadir
%ROOT%_datadir/mysql
%attr(3770,root,mysql) %dir %ROOT/db
%attr(750,mysql,mysql) %ghost %ROOT/db/*
%attr(3770,root,mysql) %dir %ROOT/log
%attr(660,mysql,mysql) %ghost %verify(not md5 mtime size) %ROOT/log/*
%attr(3770,root,mysql) %dir %ROOT/tmp

%changelog
* Tue May 26 2020 Nikolai Kostrigin <nickel@altlinux.org> 8.0.20-alt2
- add add oracle-fix-charset-nullptr patch
  + refer to https://bugs.launchpad.net/ubuntu/+source/mysql-8.0/+bug/1877504

* Tue Apr 28 2020 Nikolai Kostrigin <nickel@altlinux.org> 8.0.20-alt1
- new version
  + (fixes: CVE-2019-15601, CVE-2020-2780, CVE-2020-2804, CVE-2020-2760)
  + (fixes: CVE-2020-2893, CVE-2020-2895, CVE-2020-2898, CVE-2020-2903)
  + (fixes: CVE-2020-2896, CVE-2020-2765, CVE-2020-2892, CVE-2020-2897)
  + (fixes: CVE-2020-2923, CVE-2020-2924, CVE-2020-2901, CVE-2020-2928)
  + (fixes: CVE-2020-2904, CVE-2020-2925, CVE-2020-2759, CVE-2020-2763)
  + (fixes: CVE-2020-2812, CVE-2020-2926, CVE-2020-2921, CVE-2020-2930)
- spec: fix bogus dates and trailing space in changelog
- update alt-chroot patch
- update alt-client patch
- solve unpackaged files warnings

* Fri Apr 17 2020 Nikolai Kostrigin <nickel@altlinux.org> 8.0.19-alt2
- spec: add explicit conflicts between MySQL and mariadb subpackages
  to fix MySQL-server biarch package installation failure with mariadb
  preinstalled

* Sun Jan 26 2020 Nikolai Kostrigin <nickel@altlinux.org> 8.0.19-alt1
- new version
- spec: switch to strict dependencies
- update alt-client patch

* Fri Dec 06 2019 Nikolai Kostrigin <nickel@altlinux.org> 8.0.18-alt1
- new version
- update patches: chroot, alt-disable-run-libmysql_api_test
- remove obsolete alt-aarch64-lib64 patch
- spec: switch to system libprotobuf-lite; add respective BR's

* Thu Aug 08 2019 Nikolai Kostrigin <nickel@altlinux.org> 8.0.17-alt1
- new version
- update patches: chroot, load_defaults

* Thu Jun 13 2019 Nikolai Kostrigin <nickel@altlinux.org> 8.0.16-alt1
- new version (DB upgrade function was moved from client program to server)
- chroot patch updated
- spec: update warning message on new DB upgrade behaviour
  + change owner of mysql_upgrade_info file to mysqld user
    to enable flawless upgrade

* Wed May 29 2019 Nikolai Kostrigin <nickel@altlinux.org> 8.0.15-alt2
- fix chrooted daemonization in SysVinit systems (closes: #36856)
- move mysql_config manual to devel package

* Tue Feb 05 2019 Nikolai Kostrigin <nickel@altlinux.org> 8.0.15-alt1
- new version
- replace PreReq with Requires(pre)

* Thu Nov 15 2018 Nikolai Kostrigin <nickel@altlinux.org> 8.0.13-alt1
- new version
- update patches: chroot, client, load_defaults, mysql_config-libs

* Mon Oct 15 2018 Nikolai Kostrigin <nickel@altlinux.org> 5.7.23-alt3
- remove ubt
- fix build by removing libwrap dependency

* Thu Sep 13 2018 Nikolai Kostrigin <nickel@altlinux.org> 5.7.23-alt2
- fix mysqld init script charset initialization sequence (closes: #35298)
- move tmpfiles to /run/mysqld (rider@)

* Mon Sep 03 2018 Anton Farygin <rider@altlinux.ru> 5.7.23-alt1
- 5.7.23
- removed old and unused trigger with execution of the mysql_upgrade

* Mon Jul 09 2018 Nikolai Kostrigin <nickel@altlinux.org> 5.7.22-alt1
- 5.7.22
- new version (some bug fixes)

* Fri Jun 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.7.21-alt8
- NMU: updated provides (Closes: #35004).

* Wed May 30 2018 Nikolai Kostrigin <nickel@altlinux.org> 5.7.21-alt7
- fix chrooted mysqld operation under SysVinit

* Tue May 29 2018 Nikolai Kostrigin <nickel@altlinux.org> 5.7.21-alt6
- modify chroot control facility (combine server and client setup)
- fix unowned dir /etc/my.cnf.server (closes: #32229)

* Thu May 24 2018 Nikolai Kostrigin <nickel@altlinux.org> 5.7.21-alt5
- fix installation with preinstalled maria-db (conflict mariadb-server-control)
- add database upgrade warning message to post install scripts
- fixed typo in initscript (thanks to rider@)

* Thu May 10 2018 Nikolai Kostrigin <nickel@altlinux.org> 5.7.21-alt4
- enable backport to p8 (merge commit history)

* Wed May 09 2018 Nikolai Kostrigin <nickel@altlinux.org> 5.7.21-alt3
- rebuild with ubt

* Fri Mar 23 2018 Nikolai Kostrigin <nickel@altlinux.org> 5.7.21-alt2
- 5.7.21
- update chroot patch

* Thu Feb 15 2018 Alexey Shabalin <shaba@altlinux.ru> 5.7.21-alt1
- 5.7.21
- sync patches, configs, scripts with mariadb

* Mon Jul 24 2017 Denis Medvedev <nbr@altlinux.org> 5.5.57-alt1
- 5.5.57 (Fixes: CVE-2017-3653, CVE-2017-3651, CVE-2017-3652, CVE-2017-3648, CVE-2017-3641, CVE-2017-3636, CVE-2017-3635)
- Fixes various memory and pointer mishandlings.

* Mon Apr 03 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 5.5.54-alt1
- 5.5.54 (Fixes: CVE-2017-3318, CVE-2017-3317, CVE-2017-3313, CVE-2017-3312, CVE-2017-3291, CVE-2017-3265, CVE-2017-3258, CVE-2017-3244, CVE-2017-3243, CVE-2017-3238)

* Thu Nov 17 2016 Anton Farygin <rider@altlinux.ru> 5.5.53-alt2
- disabled secure_file_priv in default cofiguration because still used
  chrooted environment (/var/lib/mysql) (closes: #32758)

* Wed Nov 02 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 5.5.53-alt1
- 5.5.53
- dh-1024 patch removed (2048 is upstream value now)

* Sat Sep 12 2015 Michael Shigorin <mike@altlinux.org> 5.5.43-alt2
- added aarch64 support (glebfm@)

* Tue Apr 07 2015 Michael Shigorin <mike@altlinux.org> 5.5.43-alt1
- 5.5.43

* Tue Feb 03 2015 Michael Shigorin <mike@altlinux.org> 5.5.42-alt1
- 5.5.42
  + dropped texinfo pages (missing now)

* Sat Jun 08 2013 Michael Shigorin <mike@altlinux.org> 5.5.32-alt1
- 5.5.32

* Mon Apr 01 2013 Michael Shigorin <mike@altlinux.org> 5.5.30-alt3
- made subpackages with client libraries and devel headers optional,
  turned these off by default since mariadb provides them and looks
  more maintainable based on current consensus (closes: #28676)
- dropped explicit library requirements (set-versions should suffice)

* Mon Mar 04 2013 Michael Shigorin <mike@altlinux.org> 5.5.30-alt2
- fixed chrooted configuration (closes: #28630)

* Tue Feb 05 2013 Michael Shigorin <mike@altlinux.org> 5.5.30-alt1
- 5.5.30

* Sun Dec 23 2012 Michael Shigorin <mike@altlinux.org> 5.5.29-alt1
- 5.5.29
- added is_prefix, scramble symbols to libmysqlclient18
  for better compatibility with the one from mariadb
  (also needed by DBD::mysql and hydra, correspondingly)
- increased DH key length from 512 to 1024 bits (thanks, fedora)

* Tue Oct 23 2012 Michael Shigorin <mike@altlinux.org> 5.5.28-alt6
- applied several more fedora patches

* Tue Oct 23 2012 Michael Shigorin <mike@altlinux.org> 5.5.28-alt5
- added forgotten complimentary libmysqlclient patch from fedora
- libmysqlclient18 -> libmysqlclient-devel dependency expunged

* Thu Oct 18 2012 Michael Shigorin <mike@altlinux.org> 5.5.28-alt4
- added library versioning from fedora (thx ldv@ and rpmsodiff)

* Sun Oct 14 2012 Michael Shigorin <mike@altlinux.org> 5.5.28-alt3
- added Conficts: libmariadb*

* Thu Oct 11 2012 Michael Shigorin <mike@altlinux.org> 5.5.28-alt2
- fixed one-byte postun trigger thinko (included current version)

* Thu Oct 11 2012 Michael Shigorin <mike@altlinux.org> 5.5.28-alt1
- 5.5.28 (closes: #27016)
  + NB: innodb is builtin *again*, please pay attention to my.cnf
- use innodb_file_per_table (closes: #27072)
- fixed charset handling in initscript (closes: #26817)
- implemented extendedstatus in initscript (closes: #7719)
- implemented basic control facility (lnkvisitor@)

* Mon Jun 18 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 5.5.25-alt1
- Test build Mysql 5.5.25

* Mon May 07 2012 Michael Shigorin <mike@altlinux.org> 5.1.63-alt1
- 5.1.63

* Fri Mar 23 2012 Michael Shigorin <mike@altlinux.org> 5.1.62-alt1
- 5.1.62
- /dev/urandom tweaks
- spec cleanup

* Wed Mar 21 2012 Michael Shigorin <mike@altlinux.org> 5.1.61-alt2
- create /dev/urandom in chroot so SSL support actually works;
  thanks naf@ (closes: #27100)

* Thu Jan 12 2012 Michael Shigorin <mike@altlinux.org> 5.1.61-alt1
- 5.1.61

* Fri Dec 30 2011 Michael Shigorin <mike@altlinux.org> 5.1.60-alt2
- please note that 5.1.50-alt1 introduced modular InnoDB support
  thus the plugin must be loaded if it's supposed to be used

* Wed Nov 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.60-alt1
- 5.1.60

* Tue Sep 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.59-alt1
- 5.1.59

* Wed Jul 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.58-alt1
- 5.1.58

* Tue May 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.57-alt1
- 5.1.57

* Fri Mar 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.56-alt4
- make mysqld plugins usable (ALT #25248)

* Thu Mar 17 2011 Alexey Tourbin <at@altlinux.ru> 5.1.56-alt3
- hack around __cxa_pure_virtual issue

* Thu Mar 17 2011 Alexey Tourbin <at@altlinux.ru> 5.1.56-alt2
- built with OpenSSL instead of bunled yaSSL
- mysql_config: disabled dependency on libssl-devel

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.56-alt1
- 5.1.56

* Wed Feb 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.55-alt1
- 5.1.55

* Tue Nov 02 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.52-alt1
- 5.1.52

* Tue Sep 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.51-alt1
- 5.1.51

* Mon Sep 27 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.50-alt6
- upgrade old my.cnf more gracefully (closes #24165)

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.1.50-alt5
- added my_compiler.h for build with my_global.h

* Thu Sep 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.50-alt4
- remove unsupported --skip-bdb from /usr/sbin/mysql_migrate

* Wed Sep 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.50-alt3
- remove unsupported options from /usr/sbin/mysql_install_db

* Wed Sep 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.50-alt2
- Provide/Oblosete libMySQL5.1{-devel,-devel-static} (closes #24134)

* Fri Sep 17 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.50-alt1
- 5.1.50

* Mon Jan 25 2010 Anton Farygin <rider@altlinux.ru> 5.0.89-alt1
- new version (closes #18943)
- fixed CVE-2009-2446 from upstream (closes #20724)
- setup utf8 encoding instead of latin1 by default (closes #12390)
- include C99 aliasing violation patch from mythtv (closes #22452)
- removed username-length patch
- wait for mysqld shutdown (closes #22234)
- don't run initial setup mysql database if mysql.user table already exists

* Mon Jun 29 2009 L.A. Kostis <lakostis@altlinux.ru> 5.0.83-alt2
- Security fixes:
  + CVE-2008-4456: potential XSS in HTML output (closes #19843).
- Remove obsoleted macros.

* Thu Jun 25 2009 L.A. Kostis <lakostis@altlinux.ru> 5.0.83-alt1
- 5.0.83.
- Remove obsoleted macros.
- Disabled patch20,patch22, updated htmlhelp to revision 15415.

* Wed May 13 2009 L.A. Kostis <lakostis@altlinux.ru> 5.0.81-alt1
- 5.0.81.
- Update htmlhelp to revision 14892.

* Sun May 03 2009 L.A. Kostis <lakostis@altlinux.ru> 5.0.77-alt1
- 5.0.77.
- Update htmlhelp to revision 14789.
- Remove obsoleted patches.

* Sun Jan 18 2009 L.A. Kostis <lakostis@altlinux.ru> 5.0.75-alt1
- 5.0.75.
- Package some packages as noarch.
- Change htmlhelp package group to Documentation.
- Update htmlhelp to revision 13252.

* Fri Nov 21 2008 L.A. Kostis <lakostis@altlinux.ru> 5.0.67-alt2
- Bugfix build.
- Remove deprecated %%post_ldconfig/%%postun_ldconfig.
- Added patches:
  + mysql-5.0.68-BUG#37027: expire_logs_days and missing
    binlogs cause a crash !

* Tue Nov 11 2008 L.A. Kostis <lakostis@altlinux.ru> 5.0.67-alt1
- 5.0.67.
- rediffed patches.
- Applied patches from Debian unstable/Ubuntu intrepid:
  + mysqlhotcopy-invalid-dbtable.patch: fix broken security fix.
  + upstream_bug_23921: Fixes random build failures.
  + scripts__mysql_config__libs: Removes unnecessary library dependencies.
- Applied patch from Gentoo:
  + ltmain.patch: fix build with recent automake.

* Sun Sep 14 2008 Dmitry V. Levin <ldv@altlinux.org> 5.0.51-alt3.a
- Build for Sisyphus.

* Wed Sep 10 2008 Dmitry V. Levin <ldv@altlinux.org> 5.0.51-alt2.a.M40.2
- mysql_install_db: Fixed typo (closes: #15924).
- Reduced rpm macros abuse in specfile.
- Updated reference manual.

* Sat May 31 2008 Dmitry V. Levin <ldv@altlinux.org> 5.0.51-alt2.a.M40.1
- Fixed build for 4.0 branch.

* Sun Mar 16 2008 L.A. Kostis <lakostis@altlinux.ru> 5.0.51-alt2.a
- 5.0.51a.
- Security fixes:
  + CVE-2008-0226, CVE-2008-0227 (Three vulnerabilities in yaSSL versions 1.7.5
    that could lead to a server crash or execution of unauthorized code.)
  + ALTER VIEW retained the original DEFINER value, even when altered by
    another user, which could allow that user to gain the access rights of the
    view (MySQL #29908).
- Add glibc-locales to -server deps (ALT #13909 #14731).
- Make links to mysqld_safe for backwards compatibility (ALT #14863).
- Update html documentation to 10265 revsion.

* Tue Jan 01 2008 L.A. Kostis <lakostis@altlinux.ru> 5.0.51-alt1
- 5.0.51.
- Security fixes:
  + CVE-2007-5969 (RENAME TABLE System Table Overwrite Vulnerability)
  + CVE-2007-6303 CVE-2007-6304
    (Server Privilege Escalation And Denial Of Service Vulnerabilities)
- Update html documentation to 9232 revision.

* Thu Aug 09 2007 L.A. Kostis <lakostis@altlinux.ru> 5.0.46-alt2
- fix a typo in alt-mysql_install_db.patch.

* Mon Aug 06 2007 L.A. Kostis <lakostis@altlinux.ru> 5.0.46-alt1
- 5.0.46.
- Update -alt-install-db.patch.
- Update -alt-username-length patch.
- Update documentation to 7319 revision.

* Wed Jun 20 2007 L.A. Kostis <lakostis@altlinux.ru> 5.0.42-alt1
- 5.0.42.

* Mon May 28 2007 L.A. Kostis <lakostis@altlinux.ru> 5.0.41-alt1
- 5.0.41 release.
- Fix CVE-2007-2583 DoS (Failure to Handle Exceptional Conditions).
- Added patches from BK:
  + BUG#28337 (NOT EXISTS with GROUP BY behaves different in 5.0.40).
- Update ALTLinux patches:
  + install-db patch.
  + username-length patch.
- Updated html help (to 6552 revision).
- Allow custom nice setting for mysqld (fix ALT #10941).
- Added mysqld-multi (fix ALT #5715).
- Added several files for -server and client.

* Sun Feb 11 2007 L.A. Kostis <lakostis@altlinux.ru> 5.0.34-alt1
- 5.0.34 release.
- update html help (to 4891 revision).
- Fix db_install in hasher (closes #10788).
- Fix charset detection routes in init.d script.
- Update install-db patch.
- Remove obsoleted patches.

* Sat Dec 30 2006 L.A. Kostis <lakostis@altlinux.ru> 5.0.30-alt0.1
- Unofficial 5.0.30 release (use Debian sources).
- Use Docs from previous 5.0.27-GA release.
- Fix SSL docs install.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 5.0.27-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Nov 02 2006 L.A. Kostis <lakostis@altlinux.ru> 5.0.27-alt1
- 5.0.27 release;
- Added patches:
  + db-4.1.24-disable-pthreadsmutexes.patch: fix NPTL issues
    (found in Mandriva package);
  + mysql-5.0.15-disable-pthreadsmutexes.patch: fix NPTL issues
    (found in Mandriva package);
  + mysql-5.0.27-alt-username-length.patch: add custom username-length
    (5.0 backport of BUG#16553) and README.ALT-ru_RU.UTF-8 about incompatible
    changes introduced by this patch;
- Add html documentation from http://dev.mysql.com/docs.

* Sat Aug 26 2006 LAKostis <lakostis at altlinux.org> 5.0.24-alt2
- fix libmysqlclient ABI breakage introduced in 5.0.24 (see
  http://bugs.mysql.com/bug.php?id=21543 for details).

* Wed Aug 09 2006 LAKostis <lakostis at altlinux.org> 5.0.24-alt1
- 5.0.24 release.

* Thu Jun 01 2006 LAKostis <lakostis at altlinux.ru> 5.0.22-alt1
- 5.0.22.
- Security fix of SQL-injection multibyte encoding processing.

* Wed May 10 2006 LAKostis <lakostis at altlinux.ru> 5.0.21-alt1
- 5.0.21.
- Remove bk patches (merged to upstream).
- Update install_db patch.
- Update -no-atomic patch.
- Remove tinfo patch (http://bugs.mysql.com/bug.php?id=18912).
- Security fixes:
  + CVE-2006-1516;
  + CVE-2006-1517;
  + CVE-2006-1518.

* Fri Apr 14 2006 LAKostis <lakostis at altlinux.ru> 5.0.20-alt1
- 5.0.20.
- Add mysql_upgrade trigger/script for proper 4.x -> 5.0 upgrade.
- Added some fixing patches from upcoming 5.0.21:
  + BUG#16281 (Multi-table update failing to change matched rows).
  + BUG#18830 (incompatibility new libraries with old server).
- Removed obsoleted patches.

* Sun Apr 09 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt2
- Added patches:
  + BUG#15719 fix (see #9348 for details);
  + BUG#17667 (aka CVE-2006-0903) fix;

* Thu Feb 23 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt1.4
- fix #9135;
- fix debug switch.
- fix non-static build switch.

* Sun Feb 12 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt1.3
- fix bogus vars in init.d script.
- add skip-bdb only for x86_64.

* Tue Feb 07 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt1.2
- fix alt-chroot patch.
- fix init.d script and add /etc/sysconfig/mysqld entry.

* Sun Feb 05 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt1.1
- remove chroot patch. Need to rework!
- disable ssl support.
- fix ssl switch.

* Wed Feb 01 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt1
- release for Sisyphus;
- cleanup patches.

* Thu Jan 26 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt0.1
- jump to 5.0.18.
- update patches from Fedora.
- update create_db patch.
- update defaults patch, add DATADIR to config_search path.
- add old_passwords=1 for compatibility with old clients.
- disable log queries by default.
- disable bdb support (for AMD64/x86 see comment in my.cnf).
- disable -static builds by default.

* Tue Jan 17 2006 LAKostis <lakostis at altlinux.ru> 4.1.16-alt0.1
- 4.1.16.

* Sun Dec 25 2005 LAKostis <lakostis at altlinux.ru> 4.1.14-alt0.5
- remove chroot build switch.

* Sun Nov 20 2005 LAKostis <lakostis at altlinux.ru> 4.1.14-alt0.4
- fix chroot config handling.

* Sat Sep 17 2005 LAKostis <lakostis at altlinux.ru> 4.1.14-alt0.3
- 4.1.14;
- FIXME - need rework chroot patch for proper charset handling;
- add isam support for old db installs.
- add x86_64 patches from RH and Annvix;
- add non-chroot build switch;
- remove doc package.

* Thu Mar 24 2005 Kachalov Anton <mouse@altlinux.ru> 4.0.24-alt1
- 4.0.24

* Wed Oct 20 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.21-alt1
- 4.0.21
- don't kill other mysqld processes on service stop (#5371)

* Mon Jun 07 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.20-alt1
- new version 4.0.20
- Added script mysqlhotcopy (#3365)
- Merge -utils package with -server-perl
- fixed mysqld.init script (3rd time :)

* Wed Apr 28 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.18-alt4
- Move mysqlaccess and mysqldumpslow scripts to new MySQL-utils package (#3964)

* Wed Mar 17 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.18-alt3
- Added requires for MySQL-client for perl-CGI (#2359)

* Fri Feb 27 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.18-alt2
- MySQL server crashes while running on systems with LDAP (#3729)

* Wed Feb 18 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.18-alt1
- new version 4.0.18
- fixed mysqld.init script (Dmitry Vukolov <dav@altlinux.org>)

* Thu Dec 18 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.17-alt1
- new version 4.0.17

* Fri Nov 28 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.16-alt2
- fixed setting of default charset
- removed depreciated buildreqs

* Tue Nov 25 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.16-alt1
- new version 4.0.16
- fixed Requires(post,preun) (#3155)
- Do not package .la files.

* Tue Sep 30 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.15-alt2
- added mysql_migrate script for migration from 3.x to 4.0 version of MySQL
- mysql_install_db script fix (based on old ldv's script)

* Wed Sep 17 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.15-alt1
- new version 4.0.15
- enabled charset conversion for more charsets

* Thu Jul 10 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.13-alt1
- new version 4.0.13

* Fri Mar 21 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.56-alt3
- Fixed my.cnf migration support.

* Tue Mar 18 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.56-alt2
- Fixed build in environment without /proc.
- Fixed build without libncurses-devel.
- Updated buildrequires.
- server: handle default my.cnf migration.

* Tue Mar 18 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.56-alt1
- Updated to 3.23.56, redone few patches.

* Tue Mar 11 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.55-alt3
- load_defaults: do not process untrusted files if executed by root.

* Mon Mar 10 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.55-alt2
- Packaged %%ROOT/my.cnf, owned by root and available to root only,
  to avoid mysql->root possible privilege escalation described by
  Gufino in his Bugtraq posting:
  http://www.securityfocus.com/archive/1/314391
- Changed /etc/my.cnf permissions from 0600 to 0644.
  Check your /etc/my.cnf file and move all sensitive data out there.
- Updated comment in logrotate script, thanks to discussion in
  Sisyphus mailing list:
  http://www.altlinux.ru/pipermail/sisyphus/2003-February/039434.html

* Tue Jan 28 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.55-alt1
- Updated to 3.23.55.
- Applied docs build fixes from Lenz Grimmer.

* Fri Dec 13 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.54-alt2
- mysqlbug: fixed contact email address.

* Thu Dec 12 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.54-alt1
- Updated to 3.23.54.
- Updated chroot patch to new version.
- Added reservedwords.texi (lost in new version).
- Updated interpackage dependencies.
- Adjusted perl dependencies.

* Tue Dec 03 2002 Stanislav Ievlev <inger@altlinux.ru> 3.23.53-alt2
- added server-perl subpackage, to reduce deps on perl of server

* Tue Oct 15 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.53-alt1
- 3.23.53
- Better debugging support.

* Mon Sep 16 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.52-alt1
- 3.23.52
- Ensure tzset(3) is called before chroot(2).
- Removed %%_sysconfdir/localtime from %%ROOT chroot.
- Use subst instead of perl for text substitution.
- Linked with readline-4.3.
- Built with gcc-3.2.

* Wed Jul 03 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.51-alt2
- Patched to link with libtinfo.

* Fri Jun 14 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.51-alt1
- 3.23.51
- Fixed typo in safe_mysqld.
- Removed aggressive optimization.

* Sat Apr 27 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.50-alt1
- 3.23.50

* Wed Apr 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.49-alt5
- Fixed recent fix.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.49-alt4
- Updated chroot (fixed permissions, added NIS/NIS+ support).

* Mon Apr 08 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.49-alt3
- Added my_dir.h to libMySQL-devel (#0000701).

* Thu Feb 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.49-alt2
- Added %%ROOT/dev removal from existing configurations.
- Dropped mysql.chroot.log script (unneeded anymore).

* Wed Feb 20 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.49-alt1
- 3.23.49.
- Removed /dev from %ROOT.
- Fixed server %%post/%%preun scripts (#0000324).

* Fri Jan 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.47-alt1
- 3.23.47.

* Thu Dec 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.23.46-alt2
- Made gif2png conversion configurable.
- Automatically regenerated buildrequires.

* Mon Dec 03 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.23.46-alt1
- 3.23.46

* Mon Nov 26 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.23.45-alt1
- 3.23.45
- Fixed relocation of libmysqlclient* libraries (#0000145).
- Split html documentation (#0000179).
- Added png pictures to html documentation subpackage.

* Sun Nov 04 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.23.44-alt1
- 3.23.44

* Wed Oct 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.43-alt1
- 3.23.43
- Patched scripts in MySQL-bench to make them functional (mdk).

* Fri Sep 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.42-alt1
- 3.23.42
- Updated interpackage dependencies.
- Built with internal db-3.2.9a.

* Fri Apr 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.33-ipl8mdk
- Fixed mysqld_wrapper to handle server shutdown correctly.
- Relocated mysql_install_db from %%_bindir to %%_sbindir/
- Updated mysql_install_db to work with chrooted environments.

* Thu Apr 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.33-ipl7mdk
- Fixed (finally?) server %%postin script to handle recent database move.

* Wed Apr 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.33-ipl6mdk
- Fixed (again) server %%postin script to handle recent database move.
- Updated PreReqs for server subpackage.

* Tue Apr 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.33-ipl5mdk
- Updated %%postin script to handle recent database move.

* Sat Apr 21 2001 Alexander Bokovoy <ab@avilink.net> 3.23.33-ipl4mdk
- Fixed bug in datadir handling for chrooted environments.
- MySQL databases moved to $chrootdir/db/
- libMySQL-devel has been transformed to libMySQL-devel and libMySQL-devel-static
- mysql_config has been changed to reflect libMySQL-devel splitting:
    + it returns $libs set to shared ones only when libMySQL-devel-static not installed

* Tue Feb 27 2001 Dmitry V. Levin <ldv@fandra.org> 3.23.33-ipl3mdk
- Fixed dependencies for server subpackage (added PreReqs).
- Moved %%_bindir/my_print_defaults utility back to client subpackage.
- Moved texinfo documentation back to client subpackage.
- Fixed %%post/%%preun scripts for proper texinfo documentation (un)installation.

* Sat Feb 24 2001 Alexander Bokovoy <ab@avilink.net> 3.23.33-ipl2mdk
- Proper distribution of utilites along packages
- Fixed texinfo documentation
- Fixed dependencies

* Thu Feb 15 2001 Dmitry V. Levin <ldv@fandra.org> 3.23.33-ipl1mdk
- 3.23.33
- Rewritten startup scripts.
- Ported to new chrooted scheme.
- Changed address for bug reports to devel@alt-linux.org.

* Fri Feb 09 2001 Dmitry V. Levin <ldv@fandra.org> 3.23.32-ipl6mdk
- Libification.
- Fixed texinfo documentation.
- Client: added readline expansion for all symbols.

* Thu Feb 01 2001 Alexander Bokovoy <ab@avilink.net> 3.23.32-ipl5mdk
- New version with correct db3

* Sat Dec 30 2000 Alexander Bokovoy <ab@avilink.net> 3.23.29-ipl4mdk
- MySQL-devel depends on MySQL-shared, not MySQL-client
- Syntax error in mysql_install_db fixed

* Sun Dec 24 2000 Alexander Bokovoy <ab@avilink.net> 3.23.29-ipl3mdk
- Update to 3.23.29
- Rebuild with db3-3.2.3e

* Sun Dec 17 2000 Alexander Bokovoy <ab@avilink.net> 3.23.28-ipl2mdk
- Duplication of files in MySQL/MySQL-Client fixed
- mysql_config moved to MySQL-shared
- Various programs from MySQL package require DBI and DBD::mysql perl modules,
  dependencies fixed
- mysqlbug redirects bug reports to devel@linux.iplabs.ru mailing list
- MyISAM RAID type enabled by default

* Sat Dec 16 2000 Alexander Bokovoy <ab@avilink.net> 3.23.28-ipl1mdk
- Updated to 3.23.28
- SPEC file cleaned and uses now IPL rules
- Russian translations added
- Transactions support with BDB tables
- Bench package now requires perl-DBD-mysql instead of perl-Mysql
- Init script has new status command which displays pids of mysqld processes
- Various C++ fixes against g++ 2.96

* Thu Nov 16 2000 Mikhail Zabaluev <mookid@sigent.ru> 3.23.27-1mdk_mhz
- Updated to 3.23.27
- --with-extra-charsets=all, because we need Cyrillic
- made sure that readline is external
- macroized install-info
- mandrakized init script
- custom logrotate config to rotate *.err logs

* Sat Sep 02 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.23.23-1mdk
- Updated to 3.23.23 to correct php segfaults
- Added separate libmysql_r directory; now both a threaded
  and non-threaded library is shipped.

* Wed Aug 09 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.23.22-2mdk
- Put libmysqlclient.so in devel package

* Mon Aug 07 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.23.22-1mdk
- Updated to 3.23.22
  (this is a beta version, but starting from 3.23.19, the license is
   GPL, so we prefer the beta to the non-GPL stable tree)
- Macroize
- Merged with the spec from David Axmark <davida@mysql.com>
  :Added the support-files/my-example.cnf to the docs directory.
  :Removed devel dependency on base since it is about client
   development.
  :The --enable-assembler switch is now automatically disables on
   platforms there assembler code is unavailable. This should allow
   building this RPM on non i386 systems.

* Tue May 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.22.32-6mdk
- Recompile with egcs on alpha.

* Tue Apr 18 2000 Pixel <pixel@mandrakesoft.com> 3.22.32-5mdk
- disable starting of mysql while in install

* Thu Apr 06 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.22.32-4mdk
- fix bench perms

* Thu Apr 06 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.22.32-3mdk
- cleaned spec file

* Mon Apr 03 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.22.32-2mdk
- new group

* Sun Feb 27 2000 Jean-Michel Dault <jmdault@netrevolution.com> 3.22.32-1mdk
- updated to 3.22.32 - security updates

* Wed Jan 19 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 3.22.30

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

* Mon Jan 3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 3.22.29

* Fri Dec 31 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- rebuilt for Mandrake 7.0

* Sun Dec 12 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 3.22.27

* Wed Sep 1 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- put the shared libs in separate package
- fixed dependancies

* Thu Aug 19 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- added fr locale
- Mandrake adaptations
- Solaris adaptations

* Mon Feb 22 1999 David Axmark <david@detron.se>
- Removed unportable cc switches from the spec file. The defaults can
  now be overridden with environment variables. This feature is used
  to compile the official RPM with optimal (but compiler version
  specific) switches.
- Removed the repetitive description parts for the sub rpms. Maybe add
  again if RPM gets a multiline macro capability.
- Added support for a pt_BR translation. Translation contributed by
  Jorge Godoy <jorge@bestway.com.br>.

* Wed Nov 4 1998 David Axmark <david@detron.se>
- A lot of changes in all the rpm and install scripts. This may even
  be a working RPM :-)

* Sun Aug 16 1998 David Axmark <david@detron.se>
- A developers changelog for MySQL is available in the source RPM. And
  there is a history of major user visible changed in the Reference
  Manual.  Only RPM specific changes will be documented here.
