# NB: fails with e.g. --disable bat due to manpage
%define _unpackaged_files_terminate_build 1

%set_verify_elf_method relaxed

%def_enable bat
%def_enable readline
%def_enable webgui
%def_disable debug

%if_enabled webgui
%global php_version php7
%endif

%define bacula_major 11

Name: bacula%{bacula_major}
Version: %{bacula_major}.0.0
Release: alt1

License: AGPL-3.0
Summary: Network based backup program
Group: Archiving/Backup

Url: https://www.bacula.org/
# http://git.bacula.org/bacula.git
Source: %name-%version.tar
Source1: bacula-dir.init
Source2: bacula-fd.init
Source3: bacula-sd.init
Source4: bacula-fd.sysconfig
Source5: bacula-fd.limit
Source8: %name-configs-default-%version.tar
Source9: %name-icons-%version.tar
Source10: bacula.sysconfig
Source11: tmpfiles.conf
Source12: bacula-fd.service
Source13: bacula-sd.service
Source14: bacula-dir.service
Source15: %name-gui-%version.tar
Source16: baculum-apache2.logrotate
# Image taken from Fedora's bacula package
Source17: generic.xpm
Patch1: %name-alt.patch
Patch2: %name-gui-alt.patch
Patch3: bacula-9.4.0-fedora-seg-fault.patch
Patch4: %name-upstream-Fix-MySQL-update-procedure.patch
Patch5: %name-upstream-Fix-update_sqlite3_tables.patch

BuildRequires: gcc-c++
BuildRequires: libMySQL-devel postgresql-devel
BuildRequires: libssl-devel libncurses-devel libsqlite3-devel libacl-devel libcap-devel zlib-devel
BuildRequires: liblz4-devel
BuildRequires: dvd+rw-tools groff-base iputils bc

%if_enabled bat
BuildRequires: qt5-base-devel
BuildRequires: /usr/bin/convert
%endif

%filter_from_requires /libbaccats-%version\.so/d

%if_enabled readline
BuildRequires: libreadline-devel
%endif
%if_enabled bat
BuildRequires: imake libICE-devel libX11-devel xorg-cf-files
%endif

Requires: %name-common = %EVR
Requires: %name-client = %EVR
Requires: %name-storage = %EVR
Requires: %name-console = %EVR
Requires: %name-dir = %EVR

Conflicts: bacula9

%package client
Summary: Network based backup program (client only)
Group: Archiving/Backup
Provides: %name-fd = %EVR
Conflicts: bacula-client
Conflicts: bacula7-client
Conflicts: bacula9-client
Requires: %name-common = %EVR

%package storage
Summary: Network based backup program (storage only)
Group: Archiving/Backup
Conflicts: bacula-storage
Conflicts: bacula7-storage
Conflicts: bacula9-storage
Requires: %name-common = %EVR

%package console
Summary: Network based backup program (console only)
Group: Archiving/Backup
Conflicts: bacula-console
Conflicts: bacula7-console
Conflicts: bacula9-console
Requires: %name-common = %EVR

%package bat
Summary: Network based backup program (Qt5 Bacula Administration Tool)
Group: Archiving/Backup
Conflicts: bacula-bat
Conflicts: bacula7-bat
Conflicts: bacula9-bat

%package traymonitor
Summary: Bacula system tray monitor
Group: Archiving/Backup
Conflicts: bacula9-traymonitor

%package director-common
Summary: Network based backup program (director common)
Group: Archiving/Backup
Requires: %name-common = %EVR
Conflicts: bacula-director-common
Conflicts: bacula7-director-common
Conflicts: bacula9-director-common

%package director-mysql
Summary: Network based backup program (MySQL director only)
Group: Archiving/Backup
Requires(pre): %name-director-common = %EVR
Provides: %name-director = %EVR
Obsoletes: %name-director < %EVR
Provides: %name-dir = %EVR
Conflicts: bacula-director-mysql
Conflicts: bacula7-director-mysql
Conflicts: bacula9-director-mysql

%package director-sqlite3
Summary: Network based backup program (SQLITE3 director only)
Group: Archiving/Backup
Requires(pre): sqlite3
Requires(pre): %name-director-common = %EVR
Provides: %name-dir = %EVR
Conflicts: bacula-director-sqlite3
Conflicts: bacula7-director-sqlite3
Conflicts: bacula9-director-sqlite3

%package director-postgresql
Summary: Network based backup program (PostgreSQL director only)
Group: Archiving/Backup
Requires(pre): %name-director-common = %EVR
Requires: postgresql
Provides: %name-dir = %EVR
Conflicts: bacula-director-postgresql
Conflicts: bacula7-director-postgresql
Conflicts: bacula9-director-postgresql

%package common
Summary: Network based backup program (common files)
Group: Archiving/Backup
Requires(pre): passwdqc-utils
Conflicts: bacula-common
Conflicts: bacula7-common
Conflicts: bacula9-common

%package debug
Summary: Network based backup program (debug files)
Group: Archiving/Backup
Requires: %name-common = %EVR
BuildArch: noarch
Conflicts: bacula-debug
Conflicts: bacula7-debug
Conflicts: bacula9-debug

%package nagios
Summary: The check_bacula plugin for nagios
Group: Archiving/Backup
Conflicts: bacula-nagios
Conflicts: bacula7-nagios
Conflicts: bacula9-nagios

%package -n baculum%{bacula_major}-common
Summary: The baculum web interface for bacula.
Group: Archiving/Backup
BuildArch: noarch
Requires: %name = %EVR
Requires: %name-console = %EVR
Requires: baculum%{bacula_major}-tools = %EVR
Requires: %{php_version}
Requires: %{php_version}-dom
Requires: %{php_version}-curl
Requires: %{php_version}-ldap
Requires: %{php_version}-mbstring
Conflicts: baculum9-common

%package -n baculum%{bacula_major}-tools
Summary: Bacula tools required for baculum web interface.
Group: Archiving/Backup
Requires: %name = %EVR
Requires: %name-console = %EVR
Conflicts: baculum9-tools

%package -n baculum%{bacula_major}-mysql
Summary: The baculum web interface for bacula.
Group: Archiving/Backup
BuildArch: noarch
Provides: baculum%{bacula_major} = %EVR
Requires: baculum%{bacula_major}-common = %EVR
Requires: %name-director-mysql = %EVR
Requires: %{php_version}-pdo_mysql
Requires: %{php_version}-mysqlnd
Conflicts: baculum9-mysql

%package -n baculum%{bacula_major}-sqlite3
Summary: The baculum web interface for bacula.
Group: Archiving/Backup
BuildArch: noarch
Provides: baculum%{bacula_major} = %EVR
Requires: baculum%{bacula_major}-common = %EVR
Requires: %name-director-sqlite3 = %EVR
Requires: %{php_version}-pdo_sqlite
Conflicts: baculum9-sqlite3

%package -n baculum%{bacula_major}-postgresql
Summary: The baculum web interface for bacula.
Group: Archiving/Backup
BuildArch: noarch
Provides: baculum%{bacula_major} = %EVR
Requires: baculum%{bacula_major}-common = %EVR
Requires: %name-director-postgresql = %EVR
Requires: %{php_version}-pdo_pgsql
Conflicts: baculum9-postgresql

%package -n baculum%{bacula_major}-apache2
Summary: The baculum web interface for bacula.
Group: Archiving/Backup
BuildArch: noarch
Requires: baculum%{bacula_major} = %EVR
Requires: apache2-mod_%{php_version}
Conflicts: baculum9-apache2

%description
Bacula is a set of computer programs that permits the system
administrator to manage backup, recovery, and verification of computer
data across a network of computers of different kinds.
Bacula can also run entirely upon a single computer and can backup to
various types of media, including tape and disk. In technical terms, it
is a network Client/Server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage
management features that make it easy to find and recover lost or
damaged files. Due to its modular design, Bacula is scalable from small
single computer systems to systems consisting of hundreds of computers
located over a large network.

%description client
Bacula File services (or Client program) is the software program that is
installed on the machine to be backed up. It is specific to the
operating system on which it runs and is responsible for providing the
file attributes and data when requested by the Director. The File
services are also responsible for the file system dependent part of
restoring the file attributes and data during a recovery operation.
This program runs as a daemon on the machine to be backed up, and in
some of the documentation, the File daemon is referred to as the Client
(for example in Bacula configuration file)

%description storage
Bacula Storage services consist of the software programs that perform
the storage and recovery of the file attributes and data to the physical
backup media or volumes. In other words, the Storage daemon is
responsible for reading and writing your tapes (or other storage media,
e.g. files).
The Storage services runs as a daemon on the machine that has the backup
device (usually a tape drive).

%description director-common
Director common package for bacula.

%description director-mysql
Bacula Director is the program that supervises all the backup, restore,
verify and archive operations. The system administrator uses the Bacula
Director to schedule backups and to recover files.
Catalog services are comprised of the software programs responsible for
maintaining the file indexes and volume databases for all files backed up.
The Catalog services permit the System Administrator or user to quickly
locate and restore any desired file, since it maintains a record of all
Volumes used, all Jobs run, and all Files saved.
This package contains Director built for MySQL backend.

%description director-sqlite3
Bacula Director is the program that supervises all the backup, restore,
verify and archive operations. The system administrator uses the Bacula
Director to schedule backups and to recover files.
Catalog services are comprised of the software programs responsible for
maintaining the file indexes and volume databases for all files backed up.
The Catalog services permit the System Administrator or user to quickly
locate and restore any desired file, since it maintains a record of all
Volumes used, all Jobs run, and all Files saved.
This package contains Director built for SQLite3 backend.

%description director-postgresql
Bacula Director is the program that supervises all the backup, restore,
verify and archive operations. The system administrator uses the Bacula
Director to schedule backups and to recover files.
Catalog services are comprised of the software programs responsible for
maintaining the file indexes and volume databases for all files backed up.
The Catalog services permit the System Administrator or user to quickly
locate and restore any desired file, since it maintains a record of all
Volumes used, all Jobs run, and all Files saved.
This package contains Director built for PostgreSQL backend.

%description console
Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director.
This package contains text based management console.

%description bat
Bacula Administration Tool package.

%description traymonitor
Tray monitor for your bacula server.

%description common
Common files for bacula parts.

%description debug
Debug files for bacula.

%description nagios
The check_bacula plugin for nagios.

%description -n baculum%{bacula_major}-common
Baculum is Bacula web based interface. It enables Bacula administration
functions such as:

- Running Bacula jobs (backup, restore, verify...).
- Two services: Baculum API and Baculum Web
- Configuring Bacula on local and remote hosts
- Monitoring Bacula service status.
- Bacula console available via a Web window.
- Multi-user interface.
- Support for customized and restricted consoles (Console ACL function).
- Volume management.
- User friendly graphs and metrics.
- Basic storage daemon operations (mount, umount, release, ...).
- Easy to use configuration and restore wizards.
- Multiple Director support.
- Live AJAX based statuses.

%description -n baculum%{bacula_major}-tools
Baculum is Bacula web based interface. It enables Bacula administration
functions such as:

- Running Bacula jobs (backup, restore, verify...).
- Two services: Baculum API and Baculum Web
- Configuring Bacula on local and remote hosts
- Monitoring Bacula service status.
- Bacula console available via a Web window.
- Multi-user interface.
- Support for customized and restricted consoles (Console ACL function).
- Volume management.
- User friendly graphs and metrics.
- Basic storage daemon operations (mount, umount, release, ...).
- Easy to use configuration and restore wizards.
- Multiple Director support.
- Live AJAX based statuses.

%description -n baculum%{bacula_major}-mysql
Baculum is Bacula web based interface. It enables Bacula administration
functions such as:

- Running Bacula jobs (backup, restore, verify...).
- Two services: Baculum API and Baculum Web
- Configuring Bacula on local and remote hosts
- Monitoring Bacula service status.
- Bacula console available via a Web window.
- Multi-user interface.
- Support for customized and restricted consoles (Console ACL function).
- Volume management.
- User friendly graphs and metrics.
- Basic storage daemon operations (mount, umount, release, ...).
- Easy to use configuration and restore wizards.
- Multiple Director support.
- Live AJAX based statuses.

%description -n baculum%{bacula_major}-sqlite3
Baculum is Bacula web based interface. It enables Bacula administration
functions such as:

- Running Bacula jobs (backup, restore, verify...).
- Two services: Baculum API and Baculum Web
- Configuring Bacula on local and remote hosts
- Monitoring Bacula service status.
- Bacula console available via a Web window.
- Multi-user interface.
- Support for customized and restricted consoles (Console ACL function).
- Volume management.
- User friendly graphs and metrics.
- Basic storage daemon operations (mount, umount, release, ...).
- Easy to use configuration and restore wizards.
- Multiple Director support.
- Live AJAX based statuses.

%description -n baculum%{bacula_major}-postgresql
Baculum is Bacula web based interface. It enables Bacula administration
functions such as:

- Running Bacula jobs (backup, restore, verify...).
- Two services: Baculum API and Baculum Web
- Configuring Bacula on local and remote hosts
- Monitoring Bacula service status.
- Bacula console available via a Web window.
- Multi-user interface.
- Support for customized and restricted consoles (Console ACL function).
- Volume management.
- User friendly graphs and metrics.
- Basic storage daemon operations (mount, umount, release, ...).
- Easy to use configuration and restore wizards.
- Multiple Director support.
- Live AJAX based statuses.

%description -n baculum%{bacula_major}-apache2
Baculum is Bacula web based interface. It enables Bacula administration
functions such as:

- Running Bacula jobs (backup, restore, verify...).
- Two services: Baculum API and Baculum Web
- Configuring Bacula on local and remote hosts
- Monitoring Bacula service status.
- Bacula console available via a Web window.
- Multi-user interface.
- Support for customized and restricted consoles (Console ACL function).
- Volume management.
- User friendly graphs and metrics.
- Basic storage daemon operations (mount, umount, release, ...).
- Easy to use configuration and restore wizards.
- Multiple Director support.
- Live AJAX based statuses.

%prep
%setup -b 8 -b 9
%if_enabled webgui
%setup -T -D -b 15
%endif

%patch1 -p2

%if_enabled webgui
pushd ../%name-gui-%version/baculum
%patch2 -p3
popd
%endif

%patch3 -p1
%patch4 -p2
%patch5 -p2

mv ../%name-icons-%version icons

# remove bundled copy of lz4
rm -f src/lib/lz4.{c,h}

%build
export MTX=%_sbindir/mtx
autoheader -B autoconf autoconf/configure.in >autoconf/config.h.in
autoconf -B autoconf autoconf/configure.in >configure

%configure \
	--with-openssl \
	--mandir=%_mandir \
	--with-working-dir=%_localstatedir/bacula \
	--with-scriptdir=%_datadir/bacula/scripts \
	--with-pid-dir=%_var/run/bacula \
	--sysconfdir=%_sysconfdir/bacula \
	--enable-batch-insert \
%if_enabled readline
	--with-readline \
	--disable-conio \
%endif
	--with-dir-user=bacula \
	--with-dir-group=bacula \
	--with-sd-user=bacula \
	--with-sd-group=bacula \
	--with-postgresql \
	--with-sqlite3 \
	%{subst_enable bat } \
	--with-mysql \
	--with-logdir=%_logdir \
	#
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

# make the nagios plugin
pushd examples/nagios/check_bacula
%make LIBS="-lpthread -ldl -lssl -lcrypto"
popd

%install
%makeinstall_std

mkdir -p %buildroot%_initdir %buildroot%_unitdir
install -p -m755 %SOURCE1 %buildroot%_initdir/bacula-dir
install -p -m644 %SOURCE14 %buildroot%_unitdir/bacula-dir.service
install -p -m755 %SOURCE2 %buildroot%_initdir/bacula-fd
install -p -m644 %SOURCE12 %buildroot%_unitdir/bacula-fd.service
install -p -m755 %SOURCE3 %buildroot%_initdir/bacula-sd
install -p -m644 %SOURCE13 %buildroot%_unitdir/bacula-sd.service

mkdir -p %buildroot%_tmpfilesdir/
install -p -m644 %SOURCE11 %buildroot%_tmpfilesdir/bacula.conf

install -pD -m644 %_sourcedir/bacula.sysconfig \
	%buildroot%_sysconfdir/sysconfig/bacula
install -pD -m644 %_sourcedir/bacula-fd.sysconfig \
	%buildroot%_sysconfdir/sysconfig/bacula-fd

install -pD -m644 scripts/logrotate %buildroot%_sysconfdir/logrotate.d/bacula

install -pD -m644 %_sourcedir/bacula-fd.limit \
	%buildroot%_sysconfdir/sysconfig/limits.d/bacula-fd

mkdir -p %buildroot/var/run/bacula

mkdir -p %buildroot%_datadir/{applications,sample-configs}
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_niconsdir
mkdir -p %buildroot%_datadir/bacula/sample-configs
mkdir -p %buildroot%_sysconfdir/{security/console.apps,pam.d}
install -d -m755 %buildroot%_bindir
mv %buildroot%_sbindir/bconsole %buildroot%_bindir/
chmod 755 %buildroot%_bindir/bconsole
mv %buildroot%_sysconfdir/bacula/bconsole.conf %buildroot%_datadir/bacula/sample-configs/

%if_enabled bat
rm -f %buildroot%_sbindir/bat
install -m755 src/qt-console/.libs/bat %buildroot%_sbindir/bat
install -pD -m644 icons/bat16x16.png %buildroot%_miconsdir/bat.png
install -pD -m644 icons/bat32x32.png %buildroot%_niconsdir/bat.png
install -pD -m644 icons/bat48x48.png %buildroot%_liconsdir/bat.png
install -pD -m644 scripts/bat.desktop %buildroot%_desktopdir/bat.desktop
mv %buildroot%_sysconfdir/bacula/bat.conf %buildroot%_datadir/bacula/sample-configs/
install -d %buildroot%_defaultdocdir/bacula/html
mv %buildroot%_defaultdocdir/bacula/*.{html,png} %buildroot%_defaultdocdir/bacula/html/

# QT Tray monitor
convert %SOURCE17 bacula-tray-monitor.png
rm -f %buildroot%_sbindir/bacula-tray-monitor
install -m755 src/qt-console/tray-monitor/.libs/bacula-tray-monitor %buildroot%_sbindir/bacula-tray-monitor
install -pD -m644 manpages/bacula-tray-monitor.1 %buildroot%_man1dir/bacula-tray-monitor.1
install -pD -m644 bacula-tray-monitor.png %buildroot%_pixmapsdir/bacula-tray-monitor.png
install -pD -m644 scripts/bacula-tray-monitor.desktop %buildroot%_desktopdir/bacula-tray-monitor.desktop
rm -f %buildroot%_datadir/bacula/scripts/bacula-tray-monitor.desktop
%endif

cp -ar ../%name-configs-default-%version/* %buildroot%_sysconfdir/bacula/

install -pD -m755 %buildroot%_datadir/bacula/scripts/mtx-changer %buildroot%_sbindir
install -pD -m644 %buildroot%_datadir/bacula/scripts/mtx-changer.conf %buildroot%_sysconfdir/bacula/
sed -i "s|%_datadir/bacula/scripts|%_sysconfdir/bacula|g" %buildroot%_sbindir/mtx-changer
install -pD -m755 %buildroot%_datadir/bacula/scripts/disk-changer %buildroot%_sbindir
chmod 755 %buildroot%_sbindir/*

rm -f %buildroot%_datadir/bacula/scripts/mtx-changer
rm -f %buildroot%_datadir/bacula/scripts/mtx-changer.conf
rm -f %buildroot%_datadir/bacula/scripts/disk-changer

# install the nagios plugin
install -d %buildroot%_sysconfdir/nagios/commands
install -d %buildroot%_libdir/nagios/plugins

install -m755 examples/nagios/check_bacula/check_bacula %buildroot%_libdir/nagios/plugins/

cat > %buildroot%_sysconfdir/nagios/commands/check_bacula.cfg << EOF
# 'check_bacula' command definition
define command{
    command_name    check_bacula
    command_line    %_libdir/nagios/plugins/check_bacula -H \$HOSTADDRESS$ -D \$ARG1\$ -M \$ARG2\$ -K \$ARG3\$ -P \$ARG4\$
}
EOF

mkdir -p %buildroot/%_altdir
echo "%_libdir/libbaccats-%version.so %_libdir/libbaccats-sqlite3-%version.so        10" > %buildroot/%_altdir/bacula-dir.sqlite3
echo "%_libdir/libbaccats-%version.so %_libdir/libbaccats-mysql-%version.so          20" > %buildroot/%_altdir/bacula-dir.mysql
echo "%_libdir/libbaccats-%version.so %_libdir/libbaccats-postgresql-%version.so     30" > %buildroot/%_altdir/bacula-dir.pgsql

mkdir -p %buildroot/%_logdir/bacula/

%if_enabled webgui
pushd ../%name-gui-%version/baculum
%make DESTDIR=%buildroot HTTPDNAME=httpd2 HTTPDSITECONF=conf/sites-available
popd

# Remove links to missing translations
rm -f %buildroot/usr/share/baculum/htdocs/protected/API/Lang/pt/messages.mo
rm -f %buildroot/usr/share/baculum/htdocs/protected/API/Lang/ja/messages.mo

# Link cache to specific directory
mkdir -p %buildroot/%_cachedir/baculum/assets
mkdir -p %buildroot/%_cachedir/baculum/runtime
rmdir %buildroot%_datadir/baculum/htdocs/assets
rmdir %buildroot%_datadir/baculum/htdocs/protected/runtime
ln -sr %buildroot%_cachedir/baculum/assets %buildroot%_datadir/baculum/htdocs/assets
ln -sr %buildroot%_cachedir/baculum/runtime %buildroot%_datadir/baculum/htdocs/protected/runtime

# initial user config support for apache2
mkdir -p %buildroot%_cachedir/baculum/API-Config
mkdir -p %buildroot%_cachedir/baculum/Web-Config
rmdir %buildroot%_datadir/baculum/htdocs/protected/API/Config
rmdir %buildroot%_datadir/baculum/htdocs/protected/Web/Config
ln -sr %buildroot%_cachedir/baculum/API-Config %buildroot%_datadir/baculum/htdocs/protected/API/Config
ln -sr %buildroot%_cachedir/baculum/Web-Config %buildroot%_datadir/baculum/htdocs/protected/Web/Config
mv %buildroot%_sysconfdir/baculum/Config-api-apache %buildroot%_sysconfdir/baculum/Config-api-apache2
mv %buildroot%_sysconfdir/baculum/Config-web-apache %buildroot%_sysconfdir/baculum/Config-web-apache2
# Not using relative sylinks here since final location of symlink file is both at /usr/share/baculum/htdocs/... and at /var/cache/baculum/... at the same time.
ln -s %_sysconfdir/baculum/Config-api-apache2/baculum.users %buildroot%_datadir/baculum/htdocs/protected/API/Config/baculum.users
ln -s %_sysconfdir/baculum/Config-web-apache2/baculum.users %buildroot%_datadir/baculum/htdocs/protected/Web/Config/baculum.users

# Logs support
mkdir -p %buildroot%_logdir/httpd2/baculum-api
mkdir -p %buildroot%_logdir/httpd2/baculum-web
rmdir %buildroot%_datadir/baculum/htdocs/protected/API/Logs
rmdir %buildroot%_datadir/baculum/htdocs/protected/Web/Logs
ln -sr %buildroot%_logdir/httpd2/baculum-api %buildroot%_datadir/baculum/htdocs/protected/API/Logs
ln -sr %buildroot%_logdir/httpd2/baculum-web %buildroot%_datadir/baculum/htdocs/protected/Web/Logs

mkdir -p %buildroot%_sysconfdir/logrotate.d
install -p -m644 %SOURCE16 %buildroot%_sysconfdir/logrotate.d/baculum-apache2

%find_lang baculum-api baculum-web --output baculum.lang
%endif

# remove unpackaged files
rm -f %buildroot%_libdir/libbaccats.so
rm -f %buildroot%_libdir/libbaccats-%version.so
rm -fr %buildroot%_sysconfdir/baculum/Config-api-lighttpd
rm -fr %buildroot%_sysconfdir/baculum/Config-web-lighttpd
rm -f %buildroot%_sysconfdir/baculum/baculum-api-lighttpd.conf
rm -f %buildroot%_sysconfdir/baculum/baculum-web-lighttpd.conf
rm -f %buildroot%_sbindir/bacula
rm -f %buildroot%_datadir/bacula/scripts/{bacula,bacula-ctl-*,startmysql,stopmysql,bconsole}
rm -f %buildroot%_prefix%_unitdir/baculum-api-lighttpd.service
rm -f %buildroot%_prefix%_unitdir/baculum-web-lighttpd.service

%pre common
%_sbindir/groupadd -r -f bacula
%_sbindir/useradd -r -n -g bacula -d /var/empty -s /bin/false -c "Bacula pseudo user" bacula >/dev/null 2>&1 ||:
%_sbindir/usermod -d /var/empty -s /bin/false bacula >/dev/null 2>&1

%post common
for i in %_sysconfdir/bacula/bacula-*-password.conf; do
 [ ! -s "$i" ] || continue
 printf 'Password = "%%s"\n' "$(pwqgen|sed -e 's/[\"$\`\\]/\\&/g')" > "$i";
done

%post client
%post_service bacula-fd

%pre storage
%_sbindir/groupadd -r -f tape
gpasswd -a bacula tape >/dev/null 2>&1

%post storage
%post_service bacula-sd

%post director-sqlite3
%post_service bacula-dir
if [ ! -s %_localstatedir/bacula/bacula.db ]; then
    %_datadir/bacula/scripts/make_sqlite3_tables
    chown bacula.bacula %_localstatedir/bacula/bacula.db
fi

%post director-mysql
%post_service bacula-dir

%post director-postgresql
%post_service bacula-dir

%preun director-sqlite3
%preun_service bacula-dir

%preun director-mysql
%preun_service bacula-dir

%preun director-postgresql
%preun_service bacula-dir

%preun client
%preun_service bacula-fd

%preun storage
%preun_service bacula-sd

%files common
%attr (1770,root,bacula) %_localstatedir/bacula
%attr (0775,root,bacula) %dir %_var/run/bacula
%attr (0750,root,bacula) %dir %_sysconfdir/bacula
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/bacula-*-password.conf
%dir %_datadir/bacula
%dir %_datadir/bacula/scripts
%_datadir/bacula/scripts/bacula_config
%_datadir/bacula/scripts/btraceback.mdb
%dir %_docdir/bacula
%_docdir/bacula/ReleaseNotes
%_docdir/bacula/LICENSE
%_docdir/bacula/ChangeLog
%_docdir/bacula/INSTALL
%_docdir/bacula/LICENSE-FAQ
%_docdir/bacula/LICENSE-FOSS
%_docdir/bacula/README
%_docdir/bacula/VERIFYING

%_tmpfilesdir/*
%_man8dir/bacula.8*
%_sbindir/bsmtp
%_man1dir/bsmtp.1*
%_libdir/libbac-%version.so
%_libdir/libbaccfg-%version.so
%_libdir/libbacfind-%version.so
%_libdir/libbac.so
%_libdir/libbaccfg.so
%_libdir/libbacfind.so
%_libdir/libbacsd-%version.so
%_libdir/libbacsd.so

%files console
%attr (0644,root,root) %_datadir/bacula/sample-configs/bconsole.conf
%config(noreplace) %attr (0600,root,root) %_sysconfdir/bacula/bconsole.conf
%_bindir/bconsole
%_man8dir/bconsole.8*

%if_enabled bat
%files bat
%attr (0644,root,root) %_datadir/bacula/sample-configs/bat.conf
%doc %_defaultdocdir/bacula/html
%attr (0755,root,root) %_sbindir/bat
%_man1dir/bat.1*
%_miconsdir/bat.png
%_liconsdir/bat.png
%_niconsdir/bat.png
%_desktopdir/bat.desktop

%files traymonitor
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/bacula/bacula-tray-monitor.conf
%_desktopdir/bacula-tray-monitor.desktop
%_pixmapsdir/bacula-tray-monitor.png
%_man1dir/bacula-tray-monitor.1*
%_sbindir/bacula-tray-monitor
%endif

%files client
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/sysconfig/bacula-fd
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/sysconfig/limits.d/bacula-fd
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/bacula-fd.conf
%_sbindir/bacula-fd
%config %_initdir/bacula-fd
%_unitdir/bacula-fd.service
%_libdir/bpipe-fd.so
%_man8dir/bacula-fd.8*

%files storage
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/bacula-sd.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/mtx-changer.conf
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/device.d
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/device.d/*.conf
%config %_initdir/bacula-sd
%_unitdir/bacula-sd.service
%_sbindir/bacula-sd
%_sbindir/bextract
%_sbindir/bls
%_sbindir/btape
%_sbindir/mtx-changer
%_sbindir/disk-changer
%_datadir/bacula/scripts/isworm
%_datadir/bacula/scripts/tapealert
%_man8dir/bacula-sd.8*
%_man8dir/bextract.8*
%_man8dir/bls.8*
%_man8dir/btape.8*

%files debug
%_sbindir/btraceback
%_datadir/bacula/scripts/btraceback.dbx
%_datadir/bacula/scripts/btraceback.gdb
%_man8dir/btraceback.8*

%files director-common
%doc COPYING ChangeLog ReleaseNotes VERIFYING updatedb
%dir %attr (0770,root,bacula) %_sysconfdir/bacula/client.d
%dir %attr (0770,root,bacula) %_sysconfdir/bacula/fileset.d
%dir %attr (0770,root,bacula) %_sysconfdir/bacula/job.d
%dir %attr (0770,root,bacula) %_sysconfdir/bacula/messages.d
%dir %attr (0770,root,bacula) %_sysconfdir/bacula/pool.d
%dir %attr (0770,root,bacula) %_sysconfdir/bacula/schedule.d
%dir %attr (0770,root,bacula) %_sysconfdir/bacula/storage.d
%dir %attr (1770,root,bacula) %_logdir/bacula/
%config(noreplace) %attr (0660,root,bacula) %_sysconfdir/bacula/bacula-dir.conf
%config(noreplace) %attr (0660,root,bacula) %_sysconfdir/bacula/client.d/*.conf
%config(noreplace) %attr (0660,root,bacula) %_sysconfdir/bacula/fileset.d/*.conf
%config(noreplace) %attr (0660,root,bacula) %_sysconfdir/bacula/job.d/*.conf
%config(noreplace) %attr (0660,root,bacula) %_sysconfdir/bacula/messages.d/*.conf
%config(noreplace) %attr (0660,root,bacula) %_sysconfdir/bacula/pool.d/*.conf
%config(noreplace) %attr (0660,root,bacula) %_sysconfdir/bacula/schedule.d/*.conf
%config(noreplace) %attr (0660,root,bacula) %_sysconfdir/bacula/storage.d/*.conf
%config(noreplace) %_sysconfdir/sysconfig/bacula
%_initdir/bacula-dir
%_sbindir/bregex
%_sbindir/bwild
%_man8dir/bacula-dir.8*
%_man8dir/dbcheck.8*
%_man8dir/bscan.8*
%_man8dir/bcopy.8*
%_man8dir/bregex.8*
%_man8dir/bwild.8*
%_sysconfdir/logrotate.d/bacula
%_unitdir/bacula-dir.service
%_sbindir/bacula-dir
%_sbindir/bcopy
%_sbindir/bscan
%_sbindir/dbcheck
%_libdir/libbacsql-%version.so
%_libdir/libbacsql.so
%_datadir/bacula/scripts/baculabackupreport
%_datadir/bacula/scripts/create_bacula_database
%_datadir/bacula/scripts/delete_catalog_backup
%_datadir/bacula/scripts/drop_bacula_database
%_datadir/bacula/scripts/drop_bacula_tables
%_datadir/bacula/scripts/grant_bacula_privileges
%_datadir/bacula/scripts/make_bacula_tables
%_datadir/bacula/scripts/make_catalog_backup
%_datadir/bacula/scripts/make_catalog_backup.pl
%_datadir/bacula/scripts/update_bacula_tables
%_datadir/bacula/scripts/query.sql

%files director-mysql
%_altdir/bacula-dir.mysql
%_libdir/libbaccats-mysql*.so
%_datadir/bacula/scripts/create_mysql_database
%_datadir/bacula/scripts/drop_mysql_database
%_datadir/bacula/scripts/drop_mysql_tables
%_datadir/bacula/scripts/grant_mysql_privileges
%_datadir/bacula/scripts/make_mysql_tables
%_datadir/bacula/scripts/update_mysql_tables

%files director-postgresql
%_altdir/bacula-dir.pgsql
%_libdir/libbaccats-postgresql*.so
%_datadir/bacula/scripts/create_postgresql_database
%_datadir/bacula/scripts/drop_postgresql_database
%_datadir/bacula/scripts/drop_postgresql_tables
%_datadir/bacula/scripts/grant_postgresql_privileges
%_datadir/bacula/scripts/make_postgresql_tables
%_datadir/bacula/scripts/update_postgresql_tables

%files director-sqlite3
%_altdir/bacula-dir.sqlite3
%_libdir/libbaccats-sqlite3*.so
%_datadir/bacula/scripts/create_sqlite3_database
%_datadir/bacula/scripts/drop_sqlite3_database
%_datadir/bacula/scripts/drop_sqlite3_tables
%_datadir/bacula/scripts/grant_sqlite3_privileges
%_datadir/bacula/scripts/make_sqlite3_tables
%_datadir/bacula/scripts/update_sqlite3_tables

%files nagios
%_sysconfdir/nagios/commands/check_bacula.cfg
%_libdir/nagios/plugins/check_bacula

%files

%if_enabled webgui
%files -n baculum%{bacula_major}-common -f baculum.lang
%dir %_sysconfdir/baculum
%_datadir/baculum
%exclude %_datadir/baculum/htdocs/assets
%exclude %_datadir/baculum/htdocs/protected/runtime
%exclude %_datadir/baculum/htdocs/protected/API/Logs
%exclude %_datadir/baculum/htdocs/protected/Web/Logs
%exclude %_datadir/baculum/htdocs/protected/API/Config
%exclude %_datadir/baculum/htdocs/protected/Web/Config

%files -n baculum%{bacula_major}-tools
%_sbindir/bbconsjson
%_sbindir/bdirjson
%_sbindir/bfdjson
%_sbindir/bsdjson

%files -n baculum%{bacula_major}-mysql

%files -n baculum%{bacula_major}-sqlite3

%files -n baculum%{bacula_major}-postgresql

%files -n baculum%{bacula_major}-apache2
%config(noreplace) %_sysconfdir/logrotate.d/baculum-apache2
%config(noreplace) %attr(0600,apache2,apache2) %_sysconfdir/baculum/Config-api-apache2/baculum.users
%config(noreplace) %attr(0600,apache2,apache2) %_sysconfdir/baculum/Config-web-apache2/baculum.users
%config(noreplace) %_sysconfdir/httpd2/conf/sites-available/*
%_datadir/baculum/htdocs/assets
%_datadir/baculum/htdocs/protected/runtime
%_datadir/baculum/htdocs/protected/API/Logs
%_datadir/baculum/htdocs/protected/Web/Logs
%_datadir/baculum/htdocs/protected/API/Config
%_datadir/baculum/htdocs/protected/Web/Config
%attr(755,apache2,apache2) %_cachedir/baculum/
%attr(755,apache2,apache2) %_cachedir/baculum/assets
%attr(755,apache2,apache2) %_cachedir/baculum/runtime
%dir %attr(755,apache2,apache2) %_cachedir/baculum/API-Config
%dir %attr(755,apache2,apache2) %_cachedir/baculum/Web-Config
%config(noreplace) %_cachedir/baculum/API-Config/baculum.users
%config(noreplace) %_cachedir/baculum/Web-Config/baculum.users
%attr(755,apache2,apache2) %_logdir/httpd2/baculum-api
%attr(755,apache2,apache2) %_logdir/httpd2/baculum-web
%endif

%changelog
* Thu Feb 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 11.0.0-alt1
- Updated to upstream version 11.0.0.

* Mon Jan 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.6.7-alt1
- Updated to upstream version 9.6.7.

* Mon Oct 19 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 9.6.6-alt1
- Updated to upstream version 9.6.6.

* Thu Aug 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 9.6.5-alt1
- Updated to upstream version 9.6.5.

* Fri Apr 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 9.6.3-alt1
- Updated to upstream version 9.6.3.

* Thu Feb 13 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 9.4.4-alt3
- Restored make_catalog_backup script (Closes: #38083).

* Wed Jul 24 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 9.4.4-alt2
- Updated permissions for baculum.
- Increased priority of postgresql backend.

* Thu Jul 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 9.4.4-alt1
- Updated to upstream version 9.4.4.

* Sun Apr 21 2019 Michael Shigorin <mike@altlinux.org> 9.4.2-alt4
- minor spec cleanup

* Tue Mar 26 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 9.4.2-alt3
- Use system lz4 library (Closes: #36398)

* Mon Mar 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 9.4.2-alt2
- Updated runtime dependencies.

* Thu Mar 07 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 9.4.2-alt1
- Updated to upstream version 9.4.2 (Closes: #36244).
- Replaced Qt4 by Qt5.

* Thu Feb 07 2019 Nikolai Kostrigin <nickel@altlinux.org> 9.0.6-alt4
- fix FTBFS against libmysqlclient21

* Thu Jan 10 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.6-alt3
- Updated build dependencies and cleaned up spec.

* Tue Sep 04 2018 Alexei Takaseev <taf@altlinux.org> 9.0.6-alt2
- Rebuilt with openssl 1.1.
- Add requires postgresql10 to bacula9-director-postgresql subpackage

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.6-alt1
- Updated to upstream version 9.0.6.
- Reverted case change of VersionId for web-interface.
- Added symlink to default baculum.users configurations.

* Fri Nov 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.3-alt5
- Added conflicts to bacula7 packages.

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.3-alt4
- Updated tmpfiles permissions.

* Thu Nov 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.3-alt3
- Fixed sql scripts to use VersionId with correct case (closes: #34118).

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.3-alt2
- Fixed cache dir location.

* Mon Sep 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.3-alt1
- Updated to upstream version 9.0.3.
- Packaged web-interface baculum.

* Thu May 18 2017 Boris Gulay <boresexpress@altlinux.org> 7.4.7-alt2
- Use readline instead of conio.
- Update initscripts to use common style and check config before load.
* Wed Apr 19 2017 Boris Gulay <boresexpress@altlinux.org> 7.4.7-alt1
- Initial build of branch 7.X (spec based on v5).
- Change folder names for config files.
- Change way config files are included.
