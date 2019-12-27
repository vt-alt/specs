# vir: set ft=spec: -*- rpm-spec -*-
%define mmn 20120211
%define apache_configs_branch 2
%define apache_configs_dirs_name %apache2_name-configs-dirs%apache_configs_branch
%define apache_configs_dirs_version %apache_configs_branch.2.0
%define apache_configs_name %apache2_name-configs%apache_configs_branch
%define apache_configs_version %apache_configs_branch.3.2
%define apache_config_tool_branch 0
%define apache_config_tool_name %apache2_name-config-tools
%define apache_config_tool_version %apache_config_tool_branch.1.2
%define docdir %apache2_docdir_prefix-%version
%define macrosname %name-build

Name:    apache2
Version: 2.4.41
Release: alt1
Epoch: 1

License: %asl
Group: System/Servers
Url: http://httpd.apache.org/

Summary: The most widely used Web server on the Internet
Summary(ru_RU.UTF-8): Самый популярный веб-сервер Internet
Summary(uk_UA.UTF-8): Найбільш популярний веб-сервер Internet

Source0: httpd-%version.tar
Source1: apache2.watch

Source11: apache2-alt-configs-3.0.tar
Source12: README.ALT.ru_RU.KOI8-R
Source13: apache2-alt-alternatives-0.3.0.tar
Source14: README.ALT.ru_RU.UTF8
Source15: tmpfiles.conf
Source16: httpd.env.conf
Source17: htcacheclean.conf
Source18: htcacheclean-daemon-start.sh
Source19: htcacheclean.cron.daily

Source35: httpd2.init.Sisyphus
Source36: htcacheclean.init
Source37: httpd.service
Source38: htcacheclean.service

# scripts for control
Source40: cgi-bin_test-cgi.control.sh
Source41: cgi-bin_printenv.control.sh
Source42: htcacheclean-run.control.sh
Source43: htcacheclean-mode.control.sh

# RPM FileTrigger
Source50: 00-apache2-common.filetrigger
Source51: zz80-apache2-base.filetrigger
Source52: 90-apache2-base-a2chkconfig.filetrigger
Source53: 90-apache2-base-httpd.filetrigger
Source54: 90-apache2-htcacheclean.filetrigger
Source55: zz90-apache2-htcacheclean.filetrigger
Source56: zzzz-apache2-common.filetrigger

# scripts for condstopstart-web
Source60: server-condstop.sh
Source62: server-condstart.sh
Source63: server-condstart-rpm.sh

# scripts for SSL cert
Source70: apache2-cert-sh-functions.sh
Source71: apache2-cert-sh.sh

# ALT patches:
Patch1: apache2-2.4.28-alt-all-0.3.patch
Patch2: apache2-2.4.25-alt-apachectl.patch
Patch3: apache2-2.4.27-alt-httpd.conf.patch
Patch4: apache2-2.4.35-tlv1.2-default.patch

BuildRequires(pre): rpm-macros-apache2 >= 3.12
BuildRequires(pre): libssl-devel
BuildRequires(pre): rpm-macros-condstopstart
BuildRequires(pre): libaprutil1-devel 
BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-macros-webserver-cgi-bin-control
BuildPreReq: rpm >= 4.0.4-alt100.62
# For use -z sed option
BuildPreReq: sed >= 1:4.2.2-alt1

Requires: %name-base = %EVR
Requires: %_bindir/ab2
Requires: %_bindir/htpasswd2
Requires: webserver-cgi-bin
Requires: webserver-html
Requires: webserver-icons

# Modules by default
Requires: %name-mod_cache_disk >= %EVR

BuildPreReq: webserver-common

# Automatically added by buildreq on Fri Mar 31 2006
BuildRequires: zlib-devel

BuildPreReq: rpm-macros-alternatives
BuildPreReq: pkg-config
BuildPreReq: libgdbm-devel
BuildPreReq: libexpat-devel
BuildPreReq: libpcre-devel
BuildPreReq: openldap libldap-devel
BuildPreReq: libsasl2-devel libsasl2-plugin-gssapi
BuildPreReq: openssl
#following is required by dbmmanage
BuildPreReq: perl-DBM perl-Digest-SHA1 zlib-devel

#Fix libtool use
BuildPreReq: libtool >= 3:2.2.6

%description
Apache is a powerful, full-featured, efficient and freely-available
Web server.

%description -l ru_RU.UTF-8
Apache - мощный, функциональный, высокопроизводительный и
свободно распространяемый веб-сервер.

%package base
Summary: The most widely used Web server on the Internet (base)
Summary(ru_RU.UTF-8): Самый популярный веб-сервер Internet (база)
Summary(uk_UA.UTF-8): Найбільш популярний веб-сервер Internet (база)
Group: System/Servers

Provides: webserver
Provides: httpd
Provides: %name-common = %EVR
Provides: %apache_configs_name = %apache_configs_version
Provides: %apache_configs_dirs_name = %apache_configs_dirs_version
Provides: %apache_config_tool_name = %apache_config_tool_version

Provides: %apache2_addonconfdir
Provides: %apache2_serverdatadir
Provides: %apache2_errordir
Provides: %apache2_errordir/include
Provides: %_var/lib/dav
Provides: %apache2_proxycachedir
Provides: %apache2_spooldir
Provides: %apache2_spooldir/tmp
Provides: %apache2_spooldir/sessions
Provides: %apache2_spooldir/uploads
Provides: %apache2_basedir
Provides: %apache2_moduledir
Provides: %apache2_modulelink
Provides: %apache2_confdir
Provides: %apache2_confdir_inc
Provides: %apache2_extra_available
Provides: %apache2_extra_enabled
Provides: %apache2_extra_start
Provides: %apache2_mods_available
Provides: %apache2_mods_enabled
Provides: %apache2_mods_start
Provides: %apache2_ports_available
Provides: %apache2_ports_enabled
Provides: %apache2_ports_start
Provides: %apache2_sites_available
Provides: %apache2_sites_enabled
Provides: %apache2_sites_start
Provides: %apache2_libdir
Provides: %apache2_logfiledir
Provides: %apache2_runtimedir
Provides: %apache2_lockdir
Provides: %docdir

Conflicts: apache-common <= 1.3.42rusPL30.24-alt9
Conflicts: apache <= 1.3.42rusPL30.24-alt9
Conflicts: apache-mod_perl < 1.3.42rusPL30.24-alt9
Conflicts: apache2-htcacheclean <= 2.2.22-alt11

Obsoletes: %name-init
Obsoletes: %name-common < %EVR
PreReq: webserver-common
Requires: %name-mods >= %version-%release
Requires: %apache_configs_dirs_name >= %apache_configs_branch
Requires: %apache_config_tool_name >= %apache_config_tool_branch
Requires: %_sbindir/%apache2_dname
Requires: %condstopstart_webdir
Requires: %condstopstart_webrundir

%description base
Apache is a powerful, full-featured, efficient and freely-available
Web server.

This package does not require a webserver-cgi-bin, webserver-html and
webserver-icons.

%description -l ru_RU.UTF-8 base
Apache - мощный, функциональный, высокопроизводительный и
свободно распространяемый веб-сервер.

Данный пакет не требует наличия webserver-cgi-bin, webserver-html и
webserver-icons.

%package full
Summary: The most widely used Web server on the Internet (full)
Summary(ru_RU.UTF-8): Самый популярный веб-сервер Internet (full)
Summary(uk_UA.UTF-8): Найбільш популярний веб-сервер Internet (full)
Group: System/Servers
BuildArch: noarch

Requires: %name = %EVR
Requires: %name-cgi-bin >= %EVR
Requires: %name-html >= %EVR
Requires: %name-icons >= %EVR

%description full
Apache is a powerful, full-featured, efficient and freely-available
Web server.

This package requires a %name-cgi-bin, %name-html and %name-icons.

%description -l ru_RU.UTF-8 full
Apache - мощный, функциональный, высокопроизводительный и
свободно распространяемый веб-сервер.

Данный пакет требует наличия %name-cgi-bin, %name-html и %name-icons.

%package mods
Summary: Modules for %name installations
Summary(ru_RU.UTF-8): Модули для инсталляции %name
Group: System/Servers
Conflicts: apache2 < 2.2.4-alt17
Conflicts: apache2-base <= 2.2.22-alt15
PreReq: %name-base = %EVR
Requires: %name-mmn = %mmn
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr
Requires: %apache2_libapr_name >= %apache2_libapr_evr
Requires: %apache2_moduledir
Obsoletes: apache2-mod_macro

%description mods
This package contains modules for %name.

%description -l ru_RU.UTF-8 mods
В этом пакете находятся модули для %name.

%package configs-A1PROXIED
Summary: This is a hack to run proxified Apache2 in case Apache1 is running
Summary(ru_RU.UTF-8): Хак для поддержки проксирования Apache2 через Apache1, при его запуске
Group: System/Servers
BuildArch: noarch
Requires: %apache_configs_dirs_name >= %apache_configs_branch
Requires: %apache_config_tool_name >= %apache_config_tool_branch
Requires: %name-base = %EVR

%description configs-A1PROXIED
This is a hack to run proxified Apache2 in case Apache1 is running.

%description -l ru_RU.UTF-8 configs-A1PROXIED
Хак для поддержки проксирования Apache2 через Apache1, при его запуске.

%package httpd-worker
Summary: High speed threaded model for Apache HTTPD 2.1
Summary(ru_RU.UTF-8): Высокоскоростная нитевая модель для Apache HTTPD 2.1
Group: System/Servers
PreReq: %name-base = %EVR
PreReq: alternatives >= 0.4
Provides: %name-mmn = %mmn
Provides: %_sbindir/%apache2_dname
Provides: %name-httpd = %EVR

%description httpd-worker
The worker MPM provides a threaded implementation for Apache HTTPD 2.1. It is
considerably faster than the traditional model, and is the recommended MPM.

Worker generally is a good choice for high-traffic servers because it
has a smaller memory footprint than the prefork MPM.

%package httpd-prefork
Summary: Traditional model for Apache HTTPD 2.1
Summary(ru_RU.UTF-8): Традиционная модель для Apache HTTPD 2.1
Group: System/Servers
PreReq: %name-base = %EVR
PreReq: alternatives >= 0.4
Provides: %name-mmn = %mmn
Provides: %_sbindir/%apache2_dname
Provides: %name-httpd = %EVR
Provides: %name-httpd-prefork-like = %EVR

%description httpd-prefork
This Multi-Processing Module (MPM) implements a non-threaded,
pre-forking web server that handles requests in a manner similar to
Apache 1.3. It is appropriate for sites that need to avoid threading for
compatibility with non-thread-safe libraries. It is also the best MPM
for isolating each request, so that a problem with a single request will
not affect any other.

It is not as fast, but is considered to be more stable.

%package httpd-event
Summary: Event driven model for Apache HTTPD 2.1
Summary(ru_RU.UTF-8): Событийная модель для Apache HTTPD 2.1
Group: System/Servers
PreReq: %name-base = %EVR
PreReq: alternatives >= 0.4
Provides: %name-mmn = %mmn
Provides: %_sbindir/%apache2_dname
Provides: %name-httpd = %EVR

%description httpd-event
The event Multi-Processing Module (MPM) is designed to allow more
requests to be served simultaneously by passing off some processing
work to supporting threads, freeing up the main threads to work on
new requests.

This MPM is especially suitable for sites that see extensive KeepAlive traffic


%package -n rpm-build-%name
Summary: RPM helper to rebuild Web servers and apps packages
Summary(ru_RU.UTF-8): Набор утилит для автоматической Web серверов и приложений
Group: Development/Other

Requires: rpm-macros-apache2 >= %get_SVR rpm-macros-apache2

%description -n rpm-build-%name
These helper provide possibility to rebuild Web servers and applications
packages by some ALT Linux Web Packaging Policy.

%description -n rpm-build-%name -l ru_RU.UTF-8
Набор утилит для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.

%package devel
Summary: Module development tools for the Apache web server
Summary(ru_RU.UTF-8): Средства разработки модулей для веб-сервера Apache
Group: Development/C
Obsoletes: secureweb-devel
PreReq: %name-base = %EVR
Requires: %name-httpd = %EVR

Provides: %apache2_includedir
Provides: %apache2_installbuilddir

Obsoletes: %apache2_name-libapr %apache2_name-libapr-devel %apache2_name-libapr-devel %apache2_name-libaprutil %apache2_name-libaprutil-devel %apache2_name-libaprutil-devel
Requires: %apache2_libaprutil_name-devel >= %apache2_libaprutil_evr
Requires: %apache2_libapr_name-devel >= %apache2_libapr_evr
Requires: rpm-build-%name = %EVR

%description devel
The apache-devel package contains the source code for the Apache
Web server you'll need to build Dynamic
Shared Objects (DSOs) for Apache.

If you are installing the Apache Web server and
you want to be able to compile or develop additional modules
for Apache, you'll need to install this package.

%description -l ru_RU.UTF-8 devel
Пакет содержит заголовочные файлы из исходных текстов веб-сервера Apache,
необходимые для сборки динамически подключаемых модулей (DSO).

Если Вы устанавливаете веб-сервер Apache и собираетесь компилировать или
разрабатывать для него дополнительные модули, Вам нужно установить этот пакет.

%package docs
Summary: Apache Manual
Summary(ru_RU.UTF-8): Документация по Apache
Group: Books/Other
AutoReq: no
BuildArch: noarch
Requires: %docdir

Provides: %docdir/manual

%description docs
This package contains the Apache server documentation in HTML format.

%description -l ru_RU.UTF-8 docs
Этот пакет содержит документацию к веб-серверу Apache в формате HTML.

%package manual
Summary: Apache Manual for www
Summary(ru_RU.UTF-8): Документация по Apache для www
Group: Books/Other
PreReq: %name-base = %EVR
Requires: %docdir/manual
Requires: %apache_configs_dirs_name >= %apache_configs_branch
Requires: %apache_config_tool_name >= %apache_config_tool_branch
AutoReq: no
BuildArch: noarch

%description manual
This package contains the Apache server documentation in HTML format,
for www server using.

%description -l ru_RU.UTF-8 manual
Этот пакет содержит документацию к веб-серверу Apache в формате HTML,
для применения на www сервере.

%package manual-addons
Summary: manual-addons dir
Summary(ru_RU.UTF-8): Каталог manual-addons
Group: Books/Other
BuildArch: noarch
PreReq: webserver-common

%description manual-addons
This package contains the manual-addons dir for Apache server.

%description -l ru_RU.UTF-8 manual-addons
Этот пакет содержит каталог manual-addons для веб-сервера Apache.

%package datadirs
Summary: data dirs for Apache
Summary(ru_RU.UTF-8): каталоги данных для Apache
Group: System/Servers
BuildArch: noarch

Provides: %_datadir/%name
Provides: %_datadir/%name/cgi-bin

%description datadirs
This package contains the Apache server data dirs.

%description -l ru_RU.UTF-8 datadirs
Этот пакет содержит каталоги данных к веб-серверу Apache.

%package cgi-bin-test-cgi
Summary: cgi-bin/test-cgi for Apache
Summary(ru_RU.UTF-8): cgi-bin/test-cgi для Apache
Group: System/Servers
BuildArch: noarch
PreReq: webserver-common
PreReq: %_sysconfdir/control.d/webserver-cgi-bin-functions
Provides: webserver-cgi-bin-test-cgi
Conflicts: apache-cgi-bin-test-cgi
Conflicts: apache2-cgi-bin < 2.2.9-alt10
Conflicts: apache-common < 1.3.37rusPL30.23-alt1.1

Requires: %_datadir/%name/cgi-bin

%description cgi-bin-test-cgi
This package contains the Apache server test-cgi scripts.

%description -l ru_RU.UTF-8 cgi-bin-test-cgi
Этот пакет содержит test-cgi скрипт для веб-сервера Apache.

%package cgi-bin-printenv
Summary: cgi-bin/printenv for Apache
Summary(ru_RU.UTF-8): cgi-bin/printenv для Apac`he
Group: System/Servers
BuildArch: noarch
PreReq: webserver-common
PreReq: %_sysconfdir/control.d/webserver-cgi-bin-functions
Provides: webserver-cgi-bin-printenv
Conflicts: apache-cgi-bin-printenv
Conflicts: apache2-cgi-bin < 2.2.9-alt10
Conflicts: apache-common < 1.3.37rusPL30.23-alt1.1

Requires: %_datadir/%name/cgi-bin

%description cgi-bin-printenv
This package contains the Apache server printenv scripts.

%description -l ru_RU.UTF-8 cgi-bin-printenv
Этот пакет содержит printenv скрипт для веб-сервера Apache.

%package cgi-bin
Summary: cgi-bin for Apache
Summary(ru_RU.UTF-8): cgi-bin для Apache
Group: System/Servers
BuildArch: noarch
Provides: webserver-cgi-bin
Requires: %name-cgi-bin-test-cgi = %EVR
Requires: %name-cgi-bin-printenv = %EVR
Conflicts: apache-common <= 1.3.42rusPL30.24-alt9
Conflicts: apache-cgi-bin

%description cgi-bin
This package contains the Apache server cgi-bin dir and cgi scripts.

%description -l ru_RU.UTF-8 cgi-bin
Этот пакет содержит каталог cgi-bin с типовыми скриптами к веб-серверу Apache.

%package html
Summary: html for Apache
Summary(ru_RU.UTF-8): html для Apache
Group: System/Servers
BuildArch: noarch
PreReq: webserver-common
Provides: webserver-html
Conflicts: apache-common <= 1.3.42rusPL30.24-alt9
Conflicts: apache-html

%description html
This package contains the Apache server html dir.

%description -l ru_RU.UTF-8 html
Этот пакет содержит каталог html для веб-сервера Apache.

%package icons
Summary: icons for Apache
Summary(ru_RU.UTF-8): icons для Apache
Group: System/Servers
BuildArch: noarch
PreReq: webserver-common
Provides: webserver-icons
Conflicts: apache-common <= 1.3.42rusPL30.24-alt9
Conflicts: apache-icons

%description icons
This package contains the Apache server icons dir.

%package mod_ssl
Group: System/Servers
Summary: SSL/TLS module for the Apache HTTP server
PreReq: %name-base = %EVR
Requires: %name-mmn = %mmn
Requires: %apache_configs_dirs_name >= %apache_configs_branch
Requires: %apache_config_tool_name >= %apache_config_tool_branch
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr
Requires: %apache2_libapr_name >= %apache2_libapr_evr

Conflicts: apache2-mod_ssl-compat <= 2.2.22-alt14

Provides: %apache2_proxycachedir/mod_ssl

%description mod_ssl
The mod_ssl module provides strong cryptography for the Apache Web
server via the Secure Sockets Layer (SSL) and Transport Layer
Security (TLS) protocols.

%package mod_ldap
Group: System/Servers
Summary: Modules LDAP support for the Apache HTTP server
PreReq: %name-base = %EVR
Requires: %name-mmn = %mmn
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr
Requires: %apache2_libapr_name >= %apache2_libapr_evr
Provides: %name-mod_authnz_ldap = %EVR

%description mod_ldap
This package contains the modules:
mod_ldap -- LDAP connection pooling and result caching services for use by
    other LDAP modules.
mod_authnz_ldap -- Allows an LDAP directory to be used to store the database
    for HTTP Basic authentication.

%package mod_cache_disk
Group: System/Servers
Summary: Module supported content cache storage for the Apache HTTP server
PreReq: %name-base = %EVR
Requires: %name-mmn = %mmn
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr
Requires: %apache2_libapr_name >= %apache2_libapr_evr
Requires: %_sbindir/%apache2_htcacheclean_dname
Provides: %apache2_htcacheclean_cachepath

Conflicts: apache2-common < 2.2.19-alt1.1
Obsoletes: apache2-mod_disk_cache


%description mod_cache_disk
This package contains the module mod_cache_disk (ex.mod_disk_cache)

%package htcacheclean-control
Summary: Control rules for htcacheclean
Group: System/Servers
BuildArch: noarch

%description htcacheclean-control
This package contains control rules for the htcacheclean.
See control(8) for details.

%package htcacheclean
Summary: Clean up the cache disk for Apache
Group: System/Servers
Requires: %apache2_htcacheclean_cachepath
Requires: %name-base = %EVR
Requires: %_controldir/htcacheclean-run
Requires: %_controldir/htcacheclean-mode

%description htcacheclean
Htcacheclean is used to keep the size of mod_cache_disk's storage within
a certain limit. This tool can run either manually or in daemon mode.

%package ab
Summary: Apache HTTP server benchmarking tool
Group: System/Servers
Conflicts: apache2-base < 2.2.22-alt9
Conflicts: apache-common <= 1.3.42rusPL30.24-alt9

%description ab
Ab is a tool for benchmarking your Apache Hypertext Transfer Protocol
(HTTP) server. It is designed to give you an impression of how your
current Apache installation performs. This especially shows you how many
requests per second your Apache installation is capable of serving.

%package htpasswd
Summary: Manage user files for basic authentication
Group: System/Servers
Conflicts: apache2-base < 2.2.22-alt9
Conflicts: apache-common <= 1.3.42rusPL30.24-alt9

%description htpasswd
Htpasswd is used to create and update the flat-files used to store
usernames and password for basic authentication of HTTP users.
If htpasswd cannot access a file, such as not being able to write to
the output file or not being able to read the file in order to update
it, it returns an error status and makes no changes.

%package suexec
Summary: Suexec binary for Apache
Summary(ru_RU.UTF-8): Программа suexec для Apache
Summary(uk_UA.UTF-8): Програма suexec для Apache
Group: System/Servers
PreReq: %name-base = %EVR
Requires: %name-mmn = %mmn
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr
Requires: %apache2_libapr_name >= %apache2_libapr_evr
Requires: %apache_configs_dirs_name >= %apache_configs_branch
Requires: %apache_config_tool_name >= %apache_config_tool_branch

%description suexec
This package adds suexec to Apache. Suexec provides Apache users the ability
to run CGI and SSI programs under user IDs different from the user ID of the
calling web-server. Normally, when a CGI or SSI program executes, it runs as
the same user who is running the web server.

%description -l ru_RU.UTF-8 suexec
Этот пакет добавляет к Apache suexec. Эта программа позволяет запускать CGI-
и SSI-программы под идентификаторами пользователя, отличными от UID
веб-сервера.

%description -l uk_UA.UTF-8 suexec
Цей пакунок додає до Apache suexec. Ця програма дозволяє запускати CGI-
та SSI-програми під ідентифікаторами користувача, що відрізняються від
UID веб-серверу.

%package compat
Summary: Set DocumentRoot in %apache2_serverdatadir
Summary(ru_RU.UTF-8): Установка DocumentRoot в %apache2_serverdatadir
Group: System/Servers
BuildArch: noarch
Requires: %name-base = %EVR
Requires: %apache_configs_dirs_name >= %apache_configs_branch
Requires: %apache_config_tool_name >= 0.1.2

Provides: %apache2_compat_htdocsdir
Provides: %apache2_compat_cgibindir
Provides: %apache2_compat_iconsdir
Provides: %apache2_compat_iconssmalldir

%description compat
Set DocumentRoot in %apache2_serverdatadir to support the old configurations.

%description -l ru_RU.UTF-8 compat
Установка DocumentRoot в %apache2_serverdatadir для поддержки старых конфигураций.

%package mod_ssl-compat
Summary: Set DocumentRoot in %apache2_serverdatadir (for https)
Summary(ru_RU.UTF-8): Установка DocumentRoot в %apache2_serverdatadir (для https)
Group: System/Servers
BuildArch: noarch
Requires: %name-compat = %EVR
Requires: %name-mod_ssl = %EVR
Requires: %apache_configs_dirs_name >= %apache_configs_branch
Requires: %apache_config_tool_name >= %apache_config_tool_branch

%description mod_ssl-compat
Set DocumentRoot in %apache2_serverdatadir (for https) to support the old configurations.

%description -l ru_RU.UTF-8 mod_ssl-compat
Установка DocumentRoot в %apache2_serverdatadir для поддержки старых конфигураций (https).


%add_findprov_lib_path %apache2_libdir

%prep
%setup -q -n httpd-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .orig
%patch4 -p2

# generate ALTLinux Apache layout
echo "
# ALT layout
<Layout ALTLinux>
    prefix:		%apache2_basedir
    exec_prefix:	%prefix
    bindir:		%_bindir
    sbindir:		%_sbindir
    libdir:		%apache2_libdir
    libexecdir:		%apache2_moduledir
    mandir:		%_mandir
    sysconfdir:		%apache2_confdir
    datadir:		%apache2_datadir
    iconsdir:		%apache2_iconsdir
    htdocsdir:		%apache2_htdocsdir
    manualdir:		%apache2_manualdir
    cgidir:		%apache2_cgibindir
    includedir:		%apache2_includedir
    localstatedir:	%_var
    runtimedir:		%apache2_runtimedir
    logfiledir:		%apache2_logfiledir
    proxycachedir:	%apache2_proxycachedir
    infodir:		%_infodir
    installbuilddir:	%apache2_installbuilddir
    errordir:		%apache2_errordir
</Layout>
" >> config.layout

# Safety check: prevent build if defined MMN does not equal upstream MMN.
vmmn=`echo MODULE_MAGIC_NUMBER_MAJOR | cpp -include $PWD/include/ap_mmn.h | grep -e '^[0-9]'`
if [ "$vmmn" != "%mmn" ]; then
   : Error: Upstream MMN is now ${vmmn}, packaged MMN is %mmn.
   : Update the mmn macro and rebuild.
   exit 1
fi

%build
function mpmbuild()
{
mpm=$1; shift
mkdir $mpm; pushd $mpm
cat > config.cache <<EOF
ac_cv_func_pthread_mutexattr_setpshared=no
ac_cv_func_sem_open=no
EOF
../configure -C \
	--enable-layout=ALTLinux \
	--with-pcre=%_usr/bin/pcre-config \
	--with-perl=/usr/bin/perl \
	--with-apr=%apache2_apr_config \
	--with-apr-util=%apache2_apu_config \
	--enable-suexec --with-suexec \
	--with-suexec-caller=%apache2_user \
	--with-suexec-docroot=%apache2_suexec_docroot \
	--with-suexec-logfile=%apache2_logfiledir/suexec.log \
	--with-suexec-bin=%_sbindir/suexec%apache2_branch \
	--with-suexec-uidmin=500 --with-suexec-gidmin=500 \
	--with-suexec-userdir=public_html \
	--enable-so \
	--with-mpm=$mpm \
        --with-devrandom \
        --with-ldap --enable-ldap --enable-auth-ldap --enable-authnz-ldap \
        --enable-cache --enable-disk-cache --enable-mem-cache \
	--enable-ssl --with-ssl \
	--enable-deflate --enable-cgid \
	--enable-proxy --enable-proxy-connect \
	--enable-proxy-http --enable-proxy-ftp \
	--enable-charset_lite=shared \
	--enable-unixd --enable-mods-static='unixd' \
	$*

%make_build
popd
}

ln -snf %_datadir/apr-1/build/PrintPath build/PrintPath
libtoolize --install
autoheader
autoconf -I %_datadir/apr-1

# Only bother enabling optional modules for main build.
mpmbuild prefork --enable-mods-shared=all --with-program-name=%apache2_dname

# To prevent most modules being built statically into httpd.worker,
# easiest way seems to be enable them shared.
mpmbuild worker --enable-mods-shared=all  --with-program-name=%apache2_dname

mpmbuild event --enable-mods-shared=all  --with-program-name=%apache2_dname

# Verify that the same modules were built into the two httpd binaries
./prefork/%apache2_dname -l | grep -v prefork > prefork.mods
./worker/%apache2_dname -l | grep -v worker > worker.mods
./event/%apache2_dname -l | grep -v event > event.mods
if ( ! diff -u prefork.mods worker.mods ) \
	|| ( ! diff -u prefork.mods event.mods ) \
#	|| ( ! diff -u prefork.mods itk.mods ) \
#	|| ( ! diff -u prefork.mods peruser.mods ) \
then
  : Different modules built into httpd binaries, will not proceed
  exit 1
fi

%install
# Install README.ALT
install -m 644 %SOURCE12 ./
install -m 644 %SOURCE14 ./

# Generate sed script for substitute the real paths in configs
echo '
s|@@Port@@|80|g
s|@@SSLPort@@|443|g
s|@@SSLCertificateFile@@|%apache2_sslcertificatefile|g
s|@@SSLCertificateFile-dsa@@|%apache2_sslcertsdir/%apache2_sslcertname-dsa.%apache2_sslcertext|g
s|@@SSLCertificateKeyFile@@|%apache2_sslcertificatekeyfile|g
s|@@SSLCertificateKeyFile-dsa@@|%apache2_sslkeysdir/%apache2_sslcertname-dsa.key|g
s|@@SSLCertificateChainFile@@|%apache2_sslcertsdir/ca-root.pem|g
s|@@SSLCACertificatePath@@|%apache2_sslcertsdir|g
s|@@SSLCACertificateFile@@|%apache2_sslcertsdir/ca-root.pem|g
s|@@SSLCARevocationPath@@|%apache2_sslcertsdir|g
s|@@SSLCARevocationFile@@|%apache2_sslcertsdir/ca-bundle.crl|g
s|@vhosts_dir@|%apache2_vhostdir|g
s|@htcacheclean_cachepath@|%apache2_htcacheclean_cachepath|g
s|@SERVER@|%apache2_dname|g
s|@LOCKFILE@|%apache2_httpdlockfile|g
s|@RPMTRIGGERDIR@|%apache2_rpmfiletriggerdir|g
s|@RPMTRIGGERSTARTFILE@|%apache2_rpmhttpdstartfile|g
s|@RUNDIR@|%condstopstart_webrundir|g
s|%%apache2_branch|%apache2_branch|g
s|%%apache2_sslcertshfunctions|%apache2_sslcertshfunctions|g
s|%%apache2_sslcertsh|%apache2_sslcertsh|g
' >> SetMacros.sed


pushd prefork
make DESTDIR=%buildroot install
popd
mv %buildroot%_sbindir/%apache2_dname %buildroot%_sbindir/%apache2_dname.prefork

# install worker binary
WDIR=worker
install -m 755 $WDIR/%apache2_dname %buildroot%_sbindir/%apache2_dname.worker

# install event binary
WDIR=event
install -m 755 $WDIR/%apache2_dname %buildroot%_sbindir/%apache2_dname.event

#-----------------------------------------------------------------------------------
# Tune up executibles to co-exist with apache-ru
#
pushd %buildroot%_sbindir
#fix attributes of suexec for rpm build
chmod 755 suexec
%if "%apache2_branch" != ""
#rename suexec binary to be named that apache is expect it to be
ln -s suexec suexec%apache2_branch
#
# compatability symlinks for tools in /usr/sbin
# Maybe it's better to push ru-apache-devel before installing devel package
rm envvars-std
for tool in apachectl checkgid envvars rotatelogs fcgistarter htcacheclean; do
    ln -s ${tool} ${tool}%apache2_branch
done
# compatability symlinks for tools in /usr/bin 
pushd %buildroot%_bindir
TOOLS="ab htdbm logresolve htpasswd apxs dbmmanage httxt2dbm htdigest check_forensic"
for tool in $TOOLS; do
    ln -s ${tool} %buildroot%_bindir/${tool}%apache2_branch
done
popd
%endif
popd
#
#-----------------------------------------------------------------------------------

pushd %buildroot%apache2_confdir
tar xvSf %SOURCE11
popd

mkdir -p %buildroot%_altdir
pushd %buildroot%_altdir
tar xvSf %SOURCE13
popd

# mod_ssl bits
for suffix in crl crt csr key prm; do
   mkdir %buildroot%apache2_confdir/ssl.${suffix}
done
# create a prototype server.{crt,key}
touch %buildroot%apache2_confdir/ssl.crt/server.crt
touch %buildroot%apache2_confdir/ssl.key/server.key

# for holding mod_dav lock database
mkdir -p %buildroot%_var/lib/dav

# create a prototype session cache
mkdir -p %buildroot%apache2_proxycachedir/mod_ssl
touch %buildroot%apache2_proxycachedir/mod_ssl/scache.{dir,pag,sem}

# create spools
install -d %buildroot%apache2_spooldir/{,tmp,sessions,uploads}

# create lock dir
install -d %buildroot%apache2_lockdir

# create dir for mod_cache_disk
install -d %buildroot%apache2_htcacheclean_cachepath

# Make the MMN accessible to module packages
echo %mmn > %buildroot%apache2_includedir/.mmn

# symlinks for /etc/httpd2
ln -snf $(relative %buildroot%apache2_logfiledir %buildroot%apache2_loglink) %buildroot%apache2_loglink
ln -snf $(relative %buildroot%apache2_runtimedir %buildroot%apache2_runtimelink) %buildroot%apache2_runtimelink
ln -snf $(relative %buildroot%apache2_moduledir %buildroot%apache2_modulelink) %buildroot%apache2_modulelink
ln -snf $(relative %buildroot%apache2_installbuilddir %buildroot%apache2_basedir/build) %buildroot%apache2_basedir/build
ln -snf $(relative %buildroot%apache2_spooldir/uploads %buildroot%apache2_uploadslink) %buildroot%apache2_uploadslink
ln -snf $(relative %buildroot%apache2_lockdir %buildroot%apache2_locklink) %buildroot%apache2_locklink

# create config dirs for additional modules and Virtual hosts
mkdir %buildroot%apache2_addonconfdir

#------------------------------------------------------------------------------------
# tune up configuration files

# Install conf/*-start.d/*.conf
for d in mods ports sites extra; do
	find docs/conf/$d-start.d/ -maxdepth 1 -name '*.conf' -type f -print0 | \
		xargs -r0 install -D -t %buildroot%apache2_confdir/$d-start.d/
done

pushd %buildroot%apache2_confdir

find -type f -print0 | \
	xargs -r0 sed -i -e 's/^\([[:space:]]*User\)[[:space:]]\+.*/\1 %apache2_user/
s/^\([[:space:]]*Group\)[[:space:]]\+.*/\1 %apache2_group/
s/^\([[:space:]]*ServerAdmin\)[[:space:]]\+you/\1 %apache2_webmaster/
' httpd*.conf

# create conf/*-enabled/* for %%ghost
for d in mods ports sites extra; do
	pushd $d-available/
	find -maxdepth 1 \( -name '*.conf' -o -name '*.load' \) -type f -print0 | \
		(cd ../$d-enabled/ && xargs -r0 touch)
	popd
done
pushd sites-available/
find -maxdepth 1 \( -name 'default*.conf' -o -name 'default*.load' \) -type f -print0 | \
	sed -zr 's@^(.*/)?default@\1000-default@' | \
	(cd ../sites-enabled/ && xargs -r0 touch)
popd
popd

#------------------------------------------------------------------------------------

#install ALT misc documentation and logos

# Move .../conf/original to %%docdir/original
install -d %buildroot%docdir/
mv %buildroot%apache2_confdir/original %buildroot%docdir/original
ln -snf $(relative %buildroot%docdir/original %buildroot%apache2_confdir/original) %buildroot%apache2_confdir/original

# docroot
# Move %%apache2_manualdir to %%docdir/manual
mv %buildroot%apache2_manualdir %buildroot%docdir/manual
ln -snf $(relative %buildroot%docdir/manual %buildroot%apache2_manualdir) %buildroot%apache2_manualdir

# install docs to %%docdir/
cp -r ABOUT_APACHE README CHANGES LICENSE README.ALT* %buildroot%docdir/

# install the daemon start script
install -pD -m755 %SOURCE18 \
	%buildroot%_sbindir/%apache2_htcacheclean_dname-daemon-start

# install the init scripts
install -pD -m755 %SOURCE35 \
	%buildroot%_initdir/%apache2_dname
install -pD -m755 %SOURCE36 \
	%buildroot%_initdir/%apache2_htcacheclean_dname
install -pD -m644 %SOURCE37 \
	%buildroot%_unitdir/%apache2_dname.service
install -pD -m644 %SOURCE38 \
	%buildroot%_unitdir/%apache2_htcacheclean_dname.service

# install sysconfig settings file
install -pD -m 600 %SOURCE16 %buildroot%apache2_envconf
install -pD -m 644 %SOURCE17 %buildroot%_sysconfdir/sysconfig/%apache2_htcacheclean_dname

# install the cron script
install -pD -m 755 %SOURCE19 \
	%buildroot%_sysconfdir/cron.daily/%apache2_htcacheclean_dname

# Generate logrotate file
mkdir -p %buildroot%_sysconfdir/logrotate.d
echo '%apache2_logfiledir/*log {
	missingok
	notifempty
	sharedscripts
	create 0644 root %apache2_group
	delaycompress
	postrotate
	/sbin/service %apache2_dname condreload >/dev/null
	endscript
}
'>%buildroot%_sysconfdir/logrotate.d/%apache2_name

# install addon documentation old root
mkdir -p %buildroot%apache2_compat_manualaddonsdir/

###
## now remove installed files we ain't gonna use
#
rm -f %buildroot%apache2_installbuilddir/config.nice \
	%buildroot%apache2_moduledir/httpd.exp \
	%buildroot%apache2_installbuilddir/mkdir.sh \
	%buildroot%apache2_errordir/README

# create old apache2 dirs
mkdir -p %buildroot%apache2_compat_htdocsdir/
mkdir -p %buildroot%apache2_compat_cgibindir/
mkdir -p %buildroot%apache2_compat_iconsdir/
mkdir -p %buildroot%apache2_compat_iconssmalldir/

# Install scripts for control
install -pD %SOURCE40 %buildroot%_controldir/cgi-bin_test-cgi
install -pD %SOURCE41 %buildroot%_controldir/cgi-bin_printenv
install -pD %SOURCE42 %buildroot%_controldir/htcacheclean-run
install -pD %SOURCE43 %buildroot%_controldir/htcacheclean-mode

# Create datadirs
install -d %buildroot%_datadir/%name/cgi-bin/

# Move cgi scripts to data dirs
mv %buildroot%apache2_cgibindir/* %buildroot%_datadir/%name/cgi-bin/

# Install RPM FileTrigger
install -pD %SOURCE50 %buildroot%_rpmlibdir/00-%apache2_name.filetrigger
install -pD %SOURCE51 %buildroot%_rpmlibdir/zz80-%apache2_name-base.filetrigger
install -pD %SOURCE52 %buildroot%_rpmlibdir/90-%apache2_name-base-a2chkconfig.filetrigger
install -pD %SOURCE53 %buildroot%_rpmlibdir/90-%apache2_name-base-httpd.filetrigger
install -pD %SOURCE54 %buildroot%_rpmlibdir/90-%apache2_name-htcacheclean.filetrigger
install -pD %SOURCE55 %buildroot%_rpmlibdir/zz90-%apache2_name-htcacheclean.filetrigger
install -pD %SOURCE56 %buildroot%_rpmlibdir/zzzz-%apache2_name.filetrigger

# Install scripts for condstopstart-web
install -pD %SOURCE60 %buildroot%condstopstart_webdir/%apache2_dname-condstop
ln -s %apache2_dname-condstop %buildroot%condstopstart_webdir/%apache2_dname-condstop-rpm
install -pD %SOURCE62 %buildroot%condstopstart_webdir/%apache2_dname-condstart
install -pD %SOURCE63 %buildroot%condstopstart_webdir/%apache2_dname-condstart-rpm

# Install config for tempfiles
install -pD -m 644 %SOURCE15 %buildroot%_tmpfilesdir/%name.conf

# Install scripts for SSL cert
install -pD -m 644 %SOURCE70 %buildroot%apache2_sslcertshfunctions
install -pD -m 755 %SOURCE71 %buildroot%apache2_sslcertsh

# Substitute the real paths in configs
find %buildroot%_sysconfdir original %buildroot%_rpmlibdir %buildroot%condstopstart_webdir %buildroot%_sbindir/apachectl* \
		%buildroot%_unitdir %buildroot%_sbindir/%apache2_htcacheclean_dname-daemon-start \
		%buildroot%{apache2_sslcertsh}* \
		-type f -print0 \
	| xargs -r0 sed -i -f SetMacros.sed

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%name-files.req.list
# %name dirlist for %_rpmlibdir/files.req
%apache2_addonconfdir/	%name-base
%apache2_serverdatadir/	%name-base
%apache2_errordir/	%name-base
%apache2_errordir/include/	%name-base
%_var/lib/dav	%name-base
%apache2_proxycachedir/	%name-base
%apache2_spooldir/	%name-base
%apache2_spooldir/tmp/	%name-base
%apache2_spooldir/sessions/	%name-base
%apache2_spooldir/uploads/	%name-base
%apache2_lockdir/	%name-base
%apache2_basedir/	%name-base
%apache2_confdir/	%name-base
%apache2_confdir_inc/	%name-base
%apache2_extra_available/	%name-base
%apache2_extra_enabled/	%name-base
%apache2_extra_start/	%name-base
%apache2_mods_available/	%name-base
%apache2_mods_enabled/	%name-base
%apache2_mods_start/	%name-base
%apache2_ports_available/	%name-base
%apache2_ports_enabled/	%name-base
%apache2_ports_start/	%name-base
%apache2_sites_available/	%name-base
%apache2_sites_enabled/	%name-base
%apache2_sites_start/	%name-base
%apache2_libdir/	%name-base
%apache2_moduledir/	%name-base
%apache2_modulelink/	%name-base
%apache2_logfiledir/	%name-base
%apache2_runtimedir/	%name-base
%_datadir/%name/	%name-datadirs
%_datadir/%name/cgi-bin/	%name-datadirs
%apache2_proxycachedir/mod_ssl/	%name-mod_ssl
%apache2_htcacheclean_cachepath/	%name-mod_cache_disk
%apache2_includedir/	%name-devel
%apache2_installbuilddir/	%name-devel
%apache2_compat_htdocsdir/	%name-compat
%apache2_compat_cgibindir/	%name-compat
%apache2_compat_iconsdir/	%name-compat
%apache2_compat_iconssmalldir/	%name-compat
EOF

mkdir -p %buildroot%_rpmmacrosdir
cat <<\EOF >%buildroot%_rpmmacrosdir/%macrosname
# Macros for build %name-mod_*
%%%{name}_mmn	%mmn
EOF

#============ S C R I P T S ==================================================
#
#
%pre base
# Create user and groups
%_sbindir/groupadd -r -f %apache2_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %apache2_webmaster 2>/dev/null ||:
%_sbindir/useradd -g %apache2_group -c 'Apache2 WWW server' -d %apache2_datadir -s '/dev/null' \
	-G %webserver_group -r %apache2_user 2>/dev/null || :
if LANG=C %_bindir/id %apache2_user 2>/dev/null | \
		grep -qv "groups=[^[:space:]]*(%webserver_group)"; then
	echo 'Warning: User %apache2_user was not included in the group %webserver_group!'
	%_bindir/gpasswd -a %apache2_user %webserver_group
	echo '     Added user %apache2_user to group %webserver_group.'
fi
if [ $1 -eq 2 ]; then
	if [ -e %apache2_conf ] && \
			! (grep -qs -m1 '^[[:space:]]*[Ii][Nn][Cc][Ll][Uu][Dd][Ee][[:space:]]\+conf/ports-enabled' %apache2_conf && \
			grep -qs -m1 '^[[:space:]]*[Ii][Nn][Cc][Ll][Uu][Dd][Ee][[:space:]]\+conf/mods-enabled' %apache2_conf && \
			grep -qs -m1 '^[[:space:]]*[Ii][Nn][Cc][Ll][Uu][Dd][Ee][[:space:]]\+conf/sites-enabled' %apache2_conf && \
			grep -qs -m1 '^[[:space:]]*[Ii][Nn][Cc][Ll][Uu][Dd][Ee][[:space:]]\+conf/extra-enabled' %apache2_conf) ; then
		echo 'Warning: configuration files %apache2_conf is old!'
		echo '    Renamed old file %apache2_conf'
		echo '    to %apache2_conf.rpmsave'
		mv %apache2_conf %apache2_conf.rpmsave
	fi
	if [ -e %apache2_confdir/%apache2_dname.worker.conf ] && \
			[ ! -L %apache2_confdir/%apache2_dname.worker.conf ]; then
		echo 'Warning: original configuration files %apache2_confdir/%apache2_dname.worker.conf'
		echo '    saved as %apache2_confdir/%apache2_dname.worker.conf.rpmold'
		mv %apache2_confdir/%apache2_dname.worker.conf %apache2_confdir/%apache2_dname.worker.conf.rpmold
	fi
fi
exit 0

%preun base
if [ $1 -eq 0 ]; then
    %preun_service %apache2_dname
fi
exit 0

%post base
if [ ! -e %apache2_conf ] && \
		[ -e %apache2_conf.rpmnew ]; then
	mv %apache2_conf.rpmnew %apache2_conf
fi
if [ $1 -eq 1 ]; then
	%post_service %apache2_dname
fi
exit 0



%pre manual
if [ $1 -eq 2 ] && \
		[ -e %apache2_manualdir ] && \
		[ ! -L %apache2_manualdir ] ; then
	echo 'Warning: original %apache2_manualdir not symlink!'
	echo '    Saved as %apache2_manualdir.rpmold'
	mv %apache2_manualdir %apache2_manualdir.rpmold
fi
exit 0

%pre htcacheclean
%pre_control htcacheclean-run
%pre_control htcacheclean-mode
exit 0

%preun htcacheclean
if [ $1 -eq 0 ]; then
    %preun_service %apache2_htcacheclean_dname
fi
exit 0

%post htcacheclean
%post_apache2_rpmrenamevarinconfig %_sysconfdir/sysconfig/%apache2_htcacheclean_dname CACHEPATH HTCACHECLEAN_PATH
%post_apache2_rpmrenamevarinconfig %_sysconfdir/sysconfig/%apache2_htcacheclean_dname INTERVAL HTCACHECLEAN_DAEMON_INTERVAL
%post_apache2_rpmrenamevarinconfig %_sysconfdir/sysconfig/%apache2_htcacheclean_dname LIMIT HTCACHECLEAN_SIZE
%post_apache2_rpmrenamevarinconfig %_sysconfdir/sysconfig/%apache2_htcacheclean_dname OPTIONS HTCACHECLEAN_OPTIONS
%post_control -s auto htcacheclean-run
%post_control -s daemon htcacheclean-mode
if [ $1 -eq 1 ]; then
	%post_service %apache2_htcacheclean_dname
fi
exit 0

%pre cgi-bin-test-cgi
%pre_webserver_cgi_bin_control cgi-bin_test-cgi

%post cgi-bin-test-cgi
%post_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_test-cgi

%preun cgi-bin-test-cgi
%preun_webserver_cgi_bin_control cgi-bin_test-cgi

%postun cgi-bin-test-cgi
%postun_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_test-cgi

%triggerpostun cgi-bin-test-cgi -- apache-common < 1.3.37rusPL30.23-alt1.1, apache-cgi-bin < 1.3.41rusPL30.23-alt4.7.3, apache2-cgi-bin < 2.2.9-alt10, apache2-cgi-bin-test-cgi
%triggerpostun_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_test-cgi

%pre cgi-bin-printenv
%pre_webserver_cgi_bin_control cgi-bin_printenv

%post cgi-bin-printenv
%post_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_printenv

%preun cgi-bin-printenv
%preun_webserver_cgi_bin_control cgi-bin_printenv

%postun cgi-bin-printenv
%postun_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_printenv

%triggerpostun cgi-bin-printenv -- apache-common < 1.3.37rusPL30.23-alt1.1, apache-cgi-bin < 1.3.41rusPL30.23-alt4.7.3, apache2-cgi-bin < 2.2.9-alt10, apache2-cgi-bin-printenv
%triggerpostun_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_printenv


%files mods
%config(noreplace) %apache2_mods_available/*.load
%config(noreplace) %apache2_mods_available/*.conf
%ghost %apache2_mods_enabled/*.load
%ghost %apache2_mods_enabled/*.conf
%exclude %apache2_mods_available/ssl.load
%exclude %apache2_mods_available/ssl.conf
%exclude %apache2_mods_available/*ldap.load
%exclude %apache2_mods_available/cache_disk.*
%exclude %apache2_mods_enabled/ssl.load
%exclude %apache2_mods_enabled/ssl.conf

%doc %docdir/original/mods-available/*.load
%doc %docdir/original/mods-available/*.conf
%exclude %docdir/original/mods-available/ssl.load
%exclude %docdir/original/mods-available/ssl.conf
%exclude %docdir/original/mods-available/cache_disk.*

# everything but mod_ssl.so:
%apache2_moduledir/mod_*.so
%exclude %apache2_moduledir/mod_ssl.so
%exclude %apache2_moduledir/mod_*ldap.so
%exclude %apache2_moduledir/mod_suexec.so
%exclude %apache2_moduledir/mod_cache_disk.so

%files httpd-worker
%_sbindir/%apache2_dname.worker
%_altdir/%name-httpd-worker

%files httpd-prefork
%_sbindir/%apache2_dname.prefork
%_altdir/%name-httpd-prefork

%files httpd-event
%_sbindir/%apache2_dname.event
%_altdir/%name-httpd-event

%files

%files base
%doc %dir %docdir/
%doc %docdir/original
%exclude %docdir/original/mods-available/*
%doc %docdir/ABOUT_APACHE
%doc %docdir/README*
%doc %docdir/CHANGES
%doc %docdir/LICENSE

%config %_tmpfilesdir/*

%attr(2770,root,%apache2_group) %dir %apache2_proxycachedir/
%attr(750,root,%apache2_group) %dir %apache2_spooldir/
%attr(2770,root,%apache2_group) %dir %apache2_spooldir/tmp/
%attr(2770,root,%apache2_group) %dir %apache2_spooldir/sessions/
%attr(2770,root,%apache2_group) %dir %apache2_spooldir/uploads/
%attr(2770,root,%apache2_group) %dir %apache2_lockdir
%attr(0750,root,%apache2_group) %dir %apache2_logfiledir/
%attr(0750,root,%apache2_group) %dir %apache2_runtimedir/
%dir %apache2_libdir/
%dir %apache2_moduledir/

%dir %apache2_basedir/
%apache2_loglink
%apache2_runtimelink
%apache2_modulelink
%apache2_uploadslink
%apache2_locklink

%dir %apache2_confdir/
%dir %apache2_confdir_inc/
%dir %apache2_extra_available/
%dir %apache2_extra_enabled/
%dir %apache2_extra_start/
%dir %apache2_mods_available/
%dir %apache2_mods_enabled/
%dir %apache2_mods_start/
%dir %apache2_ports_available/
%dir %apache2_ports_enabled/
%dir %apache2_ports_start/
%dir %apache2_sites_available/
%dir %apache2_sites_enabled/
%dir %apache2_sites_start/

%apache2_confdir/original
%config(noreplace) %apache2_confdir/magic
%config(noreplace) %apache2_confdir/mime.types
%config(noreplace) %apache2_confdir_inc/*.conf

%config(noreplace) %apache2_conf
%config(noreplace) %apache2_mods_start/*.conf
%exclude %apache2_mods_start/*-manual*.conf
%config(noreplace) %apache2_ports_available/*.conf
%ghost %apache2_ports_enabled/*.conf
%config(noreplace) %apache2_ports_start/*.conf
%exclude %apache2_ports_available/http-A1PROXIED.conf
%exclude %apache2_ports_enabled/http-A1PROXIED.conf
%exclude %apache2_ports_start/020-A1PROXIED.conf
%config(noreplace) %apache2_sites_available/*.conf
%config(noreplace) %apache2_sites_start/*.conf
%exclude %apache2_sites_available/default-compat.conf
%exclude %apache2_sites_available/default_https-compat.conf
%exclude %apache2_sites_enabled/default_https.conf
%exclude %apache2_sites_enabled/000-default_https.conf
%exclude %apache2_sites_enabled/vhosts-A1PROXIED.conf
%exclude %apache2_sites_enabled/default-compat.conf
%exclude %apache2_sites_enabled/000-default-compat.conf
%exclude %apache2_sites_enabled/default_https-compat.conf
%exclude %apache2_sites_enabled/000-default_https-compat.conf
%exclude %apache2_sites_start/020-A1PROXIED.conf
%exclude %apache2_sites_start/*-default-compat.conf
%config(noreplace) %apache2_extra_available/*.conf
%ghost %apache2_extra_enabled/*.conf
%exclude %apache2_extra_available/httpd-manual*.conf
%exclude %apache2_extra_enabled/httpd-manual*.conf
%exclude %apache2_extra_enabled/httpd-*-compat.conf
%config(noreplace) %apache2_extra_start/*.conf
%exclude %apache2_extra_start/*-manual*.conf
%exclude %apache2_extra_start/*-default-compat.conf
%dir %apache2_addonconfdir/
%attr(0755,root,root) %apache2_sslcertsh
%config %_initdir/%apache2_dname
%_sbindir/a2*
%_sbindir/apachectl*
%attr(0600,root,root) %config(noreplace) %apache2_envconf
%_unitdir/%apache2_dname.service



%attr(0644,root,root) %config(noreplace) %_sysconfdir/logrotate.d/%apache2_name

%_bindir/ht*
%exclude %apache2_sslcertshfunctions
%exclude %_bindir/htpasswd*
%_bindir/logresolve*
%_sbindir/rotatelogs*
%exclude %_sbindir/htcacheclean*

%_sbindir/checkgid*
%_bindir/check_forensic*
%_bindir/dbmmanage*
%_sbindir/fcgistarter*

%_bindir/httxt2dbm*

%_rpmlibdir/*-%apache2_name.filetrigger
%_rpmlibdir/*-%apache2_name-base.filetrigger
%_rpmlibdir/*-%apache2_name-base-*.filetrigger

%condstopstart_webdir/%apache2_dname-cond*

%dir %apache2_serverdatadir/
%dir %apache2_errordir/
%dir %apache2_errordir/include/

%config(noreplace) %apache2_errordir/*.var
%config(noreplace) %apache2_errordir/include/*.html

%attr(0700,%apache2_user,%apache2_group) %dir %_var/lib/dav

%_mandir/man1/*
%exclude %_mandir/man1/htpasswd*
%exclude %_mandir/man1/ab*
%exclude %_mandir/man1/apxs*

%_mandir/man8/*
%exclude %_mandir/man8/htcacheclean*
%exclude %_mandir/man8/suexec*

%files full

%files configs-A1PROXIED
%config(noreplace) %apache2_ports_available/http-A1PROXIED.conf
%ghost %apache2_ports_enabled/http-A1PROXIED.conf
%config(noreplace) %apache2_ports_start/020-A1PROXIED.conf
%ghost %apache2_sites_enabled/vhosts-A1PROXIED.conf
%config(noreplace) %apache2_sites_start/020-A1PROXIED.conf

%files docs
%docdir/manual

%files manual
%apache2_manualdir
%config(noreplace) %apache2_mods_start/*-manual.conf
%config(noreplace) %apache2_extra_available/httpd-manual.conf
%ghost %apache2_extra_enabled/httpd-manual.conf
%config(noreplace) %apache2_extra_start/*-manual.conf

%files manual-addons
%config(noreplace) %apache2_mods_start/*-manual-addons.conf
%config(noreplace) %apache2_extra_available/httpd-manual-addons.conf
%ghost %apache2_extra_enabled/httpd-manual-addons.conf
%config(noreplace) %apache2_extra_start/*-manual-addons.conf

%files datadirs
%dir %_datadir/%name/
%dir %_datadir/%name/cgi-bin/

%files cgi-bin-test-cgi
%_controldir/cgi-bin_test-cgi
%attr(644,root,root) %_datadir/%name/cgi-bin/test-cgi

%files cgi-bin-printenv
%_controldir/cgi-bin_printenv
%attr(644,root,root) %_datadir/%name/cgi-bin/printenv

%files cgi-bin

%files html
%apache2_htdocsdir/*.html

%files icons
%defattr(644,root,%apache2_webmaster,2775)
%apache2_iconsdir/README
%apache2_iconsdir/README.html
%apache2_iconsdir/*.gif
%apache2_iconsdir/*.png
%apache2_iconsdir/*.svg
%apache2_iconsdir/small/*.gif
%apache2_iconsdir/small/*.png

%files mod_ssl
%attr(0644,root,root) %apache2_sslcertshfunctions
%apache2_moduledir/mod_ssl.so
%attr(0600,root,root) %config(noreplace) %apache2_mods_available/ssl.load
%ghost %apache2_sites_enabled/default_https.conf
%ghost %apache2_sites_enabled/000-default_https.conf
%ghost %apache2_confdir/ssl.crt/server.crt
%ghost %apache2_confdir/ssl.key/server.key
%attr(2770,root,%apache2_group) %dir %apache2_proxycachedir/mod_ssl/
%attr(0600,%apache2_user,%apache2_group) %ghost %apache2_proxycachedir/mod_ssl/scache.dir
%attr(0600,%apache2_user,%apache2_group) %ghost %apache2_proxycachedir/mod_ssl/scache.pag
%attr(0600,%apache2_user,%apache2_group) %ghost %apache2_proxycachedir/mod_ssl/scache.sem
%doc %docdir/original/mods-available/ssl.load

%files mod_ldap
%apache2_moduledir/mod_*ldap.so

%files mod_cache_disk
%apache2_moduledir/mod_cache_disk.so
%config(noreplace) %apache2_mods_available/cache_disk.*
%attr(2770,root,%apache2_group) %dir %apache2_htcacheclean_cachepath/
%doc %docdir/original/mods-available/cache_disk.*

%files htcacheclean-control
%_controldir/htcacheclean-*

%files htcacheclean
%_sbindir/htcacheclean*
%_mandir/man8/htcacheclean*
%attr(0644,root,root) %config(noreplace) %_sysconfdir/sysconfig/%apache2_htcacheclean_dname
%_unitdir/%apache2_htcacheclean_dname.service
%config %_initdir/%apache2_htcacheclean_dname
%config %_sysconfdir/cron.daily/%apache2_htcacheclean_dname

%_rpmlibdir/*-%apache2_name-htcacheclean.filetrigger

%files ab
%_bindir/ab*

%files htpasswd
%_bindir/htpasswd*
%_mandir/man1/htpasswd*

%files -n rpm-build-%name
%_rpmlibdir/%name-files.req.list
%_rpmmacrosdir/%macrosname

%files devel
%apache2_basedir/build
%dir %apache2_includedir/
%apache2_includedir/.mmn
%apache2_includedir/ap_*
%apache2_includedir/[hmoprsu]*
%apache2_includedir/apache_noprobes.h
%apache2_includedir/cache_common.h

%_bindir/apxs*
%dir %apache2_installbuilddir/
%apache2_installbuilddir/[clprs]*.mk
%apache2_installbuilddir/instdso.sh

%_sbindir/envvars*

%files suexec
%apache2_moduledir/mod_suexec.so
%attr(4510,root,%apache2_group) %_sbindir/suexec*
%_mandir/man8/suexec*

%files compat
%config(noreplace) %apache2_sites_available/default-compat.conf
%ghost %apache2_sites_enabled/default-compat.conf
%ghost %apache2_sites_enabled/000-default-compat.conf
%config(noreplace) %apache2_sites_start/*-default-compat.conf
%ghost %apache2_extra_enabled/httpd-*-compat.conf
%config(noreplace) %apache2_extra_start/*-default-compat.conf
%dir %apache2_compat_htdocsdir/
%dir %apache2_compat_cgibindir/
%dir %apache2_compat_iconssmalldir/
%dir %apache2_compat_manualaddonsdir/

%files mod_ssl-compat
%ghost %apache2_sites_enabled/default_https-compat.conf
%ghost %apache2_sites_enabled/000-default_https-compat.conf

%changelog
* Wed Aug 14 2019 Anton Farygin <rider@altlinux.ru> 1:2.4.41-alt1
- 2.4.41 

* Tue Apr 02 2019 Anton Farygin <rider@altlinux.ru> 1:2.4.39-alt1
- 2.4.39
- fixes:
   * Apache HTTP Server privilege escalation from modules scripts. CVE-2019-0211
   * mod_auth_digest access control bypass. CVE-2019-0217
   * mod_ssl access control bypass. CVE-2019-0215
   * Apache httpd URL normalization inconsistincy. CVE-2019-0220

* Fri Jan 25 2019 Anton Farygin <rider@altlinux.ru> 1:2.4.38-alt1
- 2.4.38
- fixes:
   * important: mod_ssl 2.4.37 remote DoS when used with OpenSSL 1.1.1. CVE-2019-0190
   * low: mod_session_cookie does not respect expiry time. CVE-2018-17199
   * low: DoS for HTTP/2 connections via slow request bodies. CVE-2018-17189 

* Wed Oct 24 2018 Anton Farygin <rider@altlinux.ru> 1:2.4.37-alt1
- 2.4.37
- removed TimeoutStartSec in httpd.service (closes: #27925)
- save to log remoteip instead of remote hostname for fix of work with
  mod_remoteip module (closes: #34974)


* Mon Oct 15 2018 Anton Farygin <rider@altlinux.ru> 1:2.4.35-alt2
- removed ubt tag
- changed rundir location to /run in tmpfiles
- disabled TLSv1 and TLSv1.1 protocols by default (closes: #34717)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.4.35-alt1.qa1
- NMU: applied repocop patch

* Tue Sep 25 2018 Anton Farygin <rider@altlinux.ru> 1:2.4.35-alt1
- 2.4.35

* Mon Sep 03 2018 Anton Farygin <rider@altlinux.ru> 1:2.4.34-alt2
- rebuilt with openssl-1.1 (Sisyphus)

* Tue Jul 31 2018 Anton Farygin <rider@altlinux.ru> 1:2.4.34-alt1
- 2.4.34
- fixes:
	* CVE-2018-1333 DoS for HTTP/2 connections by crafted requests
	* CVE-2018-8011 mod_md, DoS via Coredumps on specially crafted requests

* Sat Mar 31 2018 Anton Farygin <rider@altlinux.ru> 1:2.4.33-alt1
- 2.4.33
- fixes:
	* CVE-2018-1303 low: Possible out of bound read in mod_cache_socache
	* CVE-2018-1302 low: Possible write of after free on HTTP/2 stream shutdown
	* CVE-2018-1301 low: Possible out of bound access after failure in reading the HTTP request 
	* CVE-2018-1312 low: Weak Digest auth nonce generation in mod_auth_digest
	* CVE-2017-15715 low: <FilesMatch> bypass with a trailing newline in the file name
	* CVE-2017-15710 low: Out of bound write in mod_authnz_ldap when using too small Accept-Language values
	* CVE-2018-1283 medium: Tampering of mod_session data for CGI applications

* Thu Feb 15 2018 Stanislav Levin <slev@altlinux.org> 1:2.4.29-alt2
- Change the default access control directives according to apache 2.4 standard.
  Mixing old and new directives leads to unexpected results.

* Fri Oct 27 2017 Anton Farygin <rider@altlinux.ru> 1:2.4.29-alt1
- new version 2.4.29

* Tue Oct 10 2017 Anton Farygin <rider@altlinux.ru> 1:2.4.28-alt1
- new version 2.4.28
- disabled NameVirtualHost directive in ports_all.conf (closes: #32269)
- increased timeout for restarting httpd on SysVinit sytems (closes: #31062)
- increased LOOPSSTART and TimeoutStartSec (closes: #33978)
- fixes:
	* CVE-2017-9798 Corrupted or freed memory access

* Fri Jul 14 2017 Anton Farygin <rider@altlinux.ru> 1:2.4.27-alt1
- 2.4.27
- removed use of rpm-eval.sh from spec
- removed use of some apache2_*dir macroses from spec
- dropped apache branch suffix from utils and created compatability symlinks

* Sat Jun 24 2017 Anton Farygin <rider@altlinux.ru> 1:2.4.26-alt1
- 2.4.26

* Mon May 29 2017 Anton Farygin <rider@altlinux.ru> 1:2.4.25-alt2
- added ubt tag
- deep cleaning of the specfile (remove oldest trigger* macros, commented code, 
	garbage defined macros and etc..)

* Thu May 18 2017 Anton Farygin <rider@altlinux.ru> 1:2.4.25-alt1
- updated to 2.4.25 witch security fixes:
    + CVE-2016-8740 mod_http2: Mitigate DoS memory exhaustion via endless CONTINUATION frames.
    + CVE-2016-5387 core: Mitigate [f]cgi "httpoxy" issues
    + CVE-2016-2161 mod_auth_digest: Prevent segfaults during client entry allocation when the shared memory space is exhausted.
    + CVE-2016-0736 mod_session_crypto: Authenticate the session data/cookie with a MAC (SipHash) to prevent deciphering or tampering with a padding oracle attack.
- increased service startup time (closes: #33491)
- cleanup spec and patches

* Tue Aug 23 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.4.23-alt1
- updated to 2.4.23

* Thu May 26 2016 Sergey Alembekov <rt@altlinux.ru> 2.4.18-alt3
- there is no reason to not compile unixd module statically

* Wed Apr 27 2016 Sergey Alembekov <rt@altlinux.ru> 2.4.18-alt2
- obsoletes mod_macro
- fixes in mod_ssl defaults

* Sun Mar 06 2016 Sergey Alembekov <rt@altlinux.ru> 2.4.18-alt1
- new version 2.4.18
- peruser patch no longer supported
- itk patch became a module
- mod_disk_cache became mod_cache_disk

* Tue Oct 06 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.2.31-alt1
- updated to 2.2.31
- imported srpms as new git

* Wed May 29 2013 Aleksey Avdeev <solo@altlinux.ru> 2.2.24-alt3
- In a2enmod added a mandatory dependency checking for inclusion
  (Closes: #28992)

* Sun Apr 14 2013 Aleksey Avdeev <solo@altlinux.ru> 2.2.24-alt1
- 2.2.24
- Security fixes (CVE-2012-3499, CVE-2012-4558, CVE-2012-0883,
  CVE-2012-2687)

* Tue Feb 12 2013 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt17
- Fix %%name-base: Add Requires %%name-mods

* Wed Feb 06 2013 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt16
- Remove subpackage %%name-common (create virtual package for %%name-base)
- Create subpackage %%name-mods
- Remove %%name-%%apache2_libssl_name provides
- Use docdir %%apache2_docdir_prefix-%%version
- Add setting %%EVR for all provides: %%name-httpd-prefork-like
- Add new macros %%apache2_mmn to rpm-build-%%name subpackage

* Sat Jan 26 2013 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt15
- Subpackages %%name-mod_ssl{-compat,} converted to use the default
  certificate with a name %%apache2_sslcertname, located in the system
  certificate store
- SSL certificate is the default created when you run the daemon if it
  is not previously created
- Add %%ghost for %%apache2_sites_enabled/000-default*.conf

* Fri Jan 11 2013 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt14
- Added auto adjust the variable names in your %%_sysconfdir/sysconfig/%%apache2_htcacheclean_dname:
  + CACHEPATH in HTCACHECLEAN_PATH
  + INTERVAL in HTCACHECLEAN_DAEMON_INTERVAL
  + LIMIT in HTCACHECLEAN_SIZE
  + OPTIONS in HTCACHECLEAN_OPTIONS

* Fri Jan 11 2013 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt13
- Add to %%name-htcacheclean-control subpackage

* Sun Dec 23 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt12
- Fix start for systemd: Use TimeoutStartSec=10s (Closes: #27925)
- Add to %%name-htcacheclean subpackage:
  + %%_sysconfdir/sysconfig/%%apache2_htcacheclean_dname
  + systemd unit file for %%apache2_htcacheclean_dname (Closes: #28025)
  + cron daily script for runing %%apache2_htcacheclean_dname
- Update attr ang owner for %%apache2_runtimedir/
- Unuse vars (in %%_sysconfdir/sysconfig/%%apache2_htcacheclean_dname):
  + CACHEPATH (use HTCACHECLEAN_PATH)
  + INTERVAL (use HTCACHECLEAN_DAEMON_INTERVAL)
  + LIMIT (use HTCACHECLEAN_SIZE)
  + LOCKFILE
  + OPTIONS (use HTCACHECLEAN_OPTIONS)

* Sat Oct 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt11
- %%apache2_apachectl and %%_initdir/%%apache2_dname use variables
  (WAITSTOP, WAITGRACEFULSTOP, USLEEPSTART and LOOPSSTART), if they are
  defined in the file %%apache2_envconf

* Thu Oct 18 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt10
- Fix %%apache2_sbindir/apachectl%%apache2_branch start: use briefstatus
  loop in poststart (Closes: #27856)
- Move requires %%name-ab and %%name-htpasswd to %%name subpackage
- Fix conflicts for %%name-ab and %%name-htpasswd subpackage

* Wed Oct 17 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt9
- Move %%_bindir/ab2 to %%name-ab subpackage (Closes: #27860)
- Move %%_bindir/htpasswd2 to %%name-htpasswd subpackage

* Fri Aug 24 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt8
- Applied repocop fixes:
  * postclean-03-private-rpm-macros for the spec file
- Fix service httpd2 restart for systemd: Posted expectation actually
  completing the demon (300 seconds maximum)

* Wed Aug 22 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt7
- Convert Summary(ru_RU.KOI8-R) for subpackage %%name-cgi-bin to ru_RU.UTF-8

* Tue Aug 21 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt6
- Add %%_unitdir/%%apache2_dname.service to %%name-base subpackage
- Rename %%_sysconfdir/tmpfiles.d/%%name to
  %%_sysconfdir/tmpfiles.d/%%name.conf and fix permissions

* Fri Aug 17 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt5
- Fix %%_initdir/%%apache2_dname return status

* Fri Aug 10 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt4
- %%apache2_sbindir/apachectl%%apache2_branch replaced by the "official"
  apachectl (patched) (Closes: #27086)
- The function stop() in %%_initdir/%%apache2_dname now waiting
  (maximum 300 seconds) of the actual completion of the demon
  (Closes: #11531, #27091)

* Tue Aug 07 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt3
- Add %%_sysconfdir/tmpfiles.d/%%name (Closes: #27604)

* Tue Feb 14 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt2
- Add scripts for condstopstart-web

* Thu Feb 02 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.22-alt1
- 2.2.22
- Security fixes (CVE-2011-3368, CVE-2011-3607, CVE-2011-4317, CVE-2012-0021,
  CVE-2012-0031, CVE-2012-0053)

* Sat Nov 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.2.21-alt2
- Security fixes (CVE-2011-3368)

* Tue Sep 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.2.21-alt1
- 2.2.21
- Security fixes (CVE-2011-3348)

* Wed Aug 31 2011 Aleksey Avdeev <solo@altlinux.ru> 2.2.20-alt1
- 2.2.20
- Security fixes (CVE-2011-3192)
- Update patchset itk for apache2.2-mpm-itk-2.2.17-01

* Tue Aug 02 2011 Aleksey Avdeev <solo@altlinux.ru> 2.2.19-alt3
- %%_initdir/%%apache2_htcacheclean_dname: Fix missing condstop target

* Fri Jul 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.2.19-alt2
- Use %%apache2_htcacheclean_cachepath for set CacheRoot
- Move mod_disk_cache module to %%name-mod_disk_cache subpackage
- Move htcacheclean (binary and init script) to %%name-htcacheclean
  subpackage

* Mon Jun 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.2.19-alt1
- 2.2.19

* Mon Jun 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.2.17-alt5
- Fix zz-apache2-base.filetrigger
  (thanks to Sergei Epiphanov <serpiph nikiet.ru>)

* Sun Jun 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.2.17-alt4
- Fix httpd2 restart the upgrade.

* Tue May 31 2011 Aleksey Avdeev <solo@altlinux.ru> 2.2.17-alt3
- Trigger handle movement configuration file in to %%apache2_confdir_inc
  (Closes: #24960)
- Condrestart and a2chkconfig script completely removed, obsoleted
  by rpm file triggers
- Add lsb header to init

* Mon Dec 27 2010 Aleksey Avdeev <solo@altlinux.ru> 2.2.17-alt2
- Fix build gcc4.5 use

* Wed Oct 20 2010 Aleksey Avdeev <solo@altlinux.ru> 2.2.17-alt1
- 2.2.17

* Wed Oct 20 2010 Aleksey Avdeev <solo@altlinux.ru> 2.2.16-alt3
- Fix <modname>.conf loaded with upgrade (Closes: #24101)
- Fix location for DavLock database (Closes: #24336)

* Fri Sep 17 2010 Aleksey Avdeev <solo@altlinux.ru> 2.2.16-alt2
- Use gpasswd -a in %%pre %%name-common (Closes: #23240)

* Thu Sep 16 2010 Aleksey Avdeev <solo@altlinux.ru> 2.2.16-alt1
- 2.2.16 (Closes: #23933)
- Security fixes (CVE-2009-3555, CVE-2010-0408, CVE-2010-0425,
  CVE-2010-043, CVE-2010-1452, CVE-2010-2068)
- Updated messages a2{en,dis}*: added an indication of the file
  (Closes: #20932)
- Move %%apache2_extra_available/Directory_*_default.conf.in to
  %%apache2_confdir/include/ dir

* Fri Oct 09 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.14-alt4
- Fix installation %%name-base (Closes: #21865)

* Wed Oct 07 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.14-alt2
- Move %%apache2_extra_available/userdir_default.conf to
  %%apache2_mods_available/userdir.conf (Closes: #21160)
- Add %%ghost for %%apache2_*_enabled/* (Closes: #11275)

* Tue Oct 06 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.14-alt1
- 2.2.14
- Security fixes (CVE-2009-2412, CVE-2009-2699, CVE-2009-3094, CVE-2009-3095)
- Update patchsets:
  + itk for apache2.2-mpm-itk-2.2.11-02 (Closes: #21486)
  + peruser for httpd-2.2.3-peruser-0.3.0-dc3

* Mon Sep 07 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.12-alt2
- Rebuild with libldap2.4
- Update README.ALT.ru_RU.* (Closes: #21084)
  (thanks to Kharitonov A. Dmitry <kharpost rambler.ru>)

* Thu Jul 30 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.12-alt1
- 2.2.12
- Security fixes (CVE-2008-2939, CVE-2009-0023, CVE-2009-1191, CVE-2009-1195,
  CVE-2009-1890, CVE-2009-1891, CVE-2009-1955 and CVE-2009-1956)
  (Closes: #20218, #20674 and #20760)
- Add support new MIME types (Closes: #11460)

* Fri May 29 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt18
- Add experimental MPM: %%name-httpd-itk and %%name-httpd-peruser subpackage
  (Closes: #16460 and #16766)

* Sun May 24 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt17
- Fix Requires for LDAP support (Closes: #20122)
- Move mod_ldap and mod_authnz_ldap modules to %%name-mod_ldap subpackage
- Fix build libtool 2.x use (thanks to Boris Savelev <boris altlinux.org>)

* Wed Apr 29 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt16
- Fix libtool 2.2.6 use
- Fix Requires

* Tue Apr 14 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt15
- Fix %%apache2_sbindir/a2chkconfig_list (Closes: #19625)
- Update message in %%pre common (#19602)
  (thanks to Sergey Vlasov <vsu altlinux org>)

* Fri Feb 06 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt14
- Fix Provides/Requires (Closes: #11643)

* Wed Nov 12 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt13
- Remove libdb application switch using and %%name-%%apache2_libdb_name
  provides

* Tue Oct 28 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt12
- Fix symlink for cgi-bin scripts created

* Tue Oct 28 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt11
- Fix permission for README.ALT.ru_RU.KOI8-R (Closes: #17377)
- Fix config files (Closes: #16914)
- Fix a2ensite (Closes: #17287)
- Add provides %%name-httpd-prefork-like for %%name-httpd-prefork
  (Closes: #17285)
- Add build subpackages:
  + %%name-datadirs -- data dirs
  + %%name-cgi-bin-test-cgi and %%name-cgi-bin-printenv -- cgi-bin scripts
    (use control for facility)

* Fri Aug 22 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt10
- Add build subpackages (#16353):
  + %%name-base (not requires a webserver-cgi-bin, webserver-html
    and webserver-icons)
  + %%name-fill (requires a %%name-cgi-bin, %%name-html and %%name-icons)
- Add auto adding user %%apache2_user to group %%webserver_group
- Add httpd provides in %%name-base subpackage (#13665)

* Fri Aug 15 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt9
- Remove libdb and distr application switch from this package
- Add use libdb and distr application switch from the package
  rpm-macros-apache2
- Add and use %%name-%%apache2_libssl_name provides

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.9-alt8.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Aug 08 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt8
- Fix crash rpm --eval in rpm-eval.sh (Closes: #16623)

* Wed Aug 06 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt7
- Fix autoconf version to 2.50

* Tue Aug 05 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt6
- Fix permissions sets (Closes: #16568)

* Mon Aug 04 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt5
- Fix conflict with the package directories webserver-common (Closes: #16546)

* Sat Aug 02 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt4
- Add use apache_ru_compat application switch from the package
  rpm-macros-apache2 (enabled by default)
- Unuse rpm-macros-apache2-compat package for build
- Obsolete all macros %%a_* and %%apache_* (use rpm-macros-apache2-compat
  package)

* Fri Aug 01 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt3
- Removed version of the webserver-{cgi-bin,html,icons}
- Use rpm-macros-apache2 and rpm-macros-apache2-compat
- Add build subpackage for ALT Linux RPM Packaging Policy:
  + rpm-build-%%name
- Use apache_ru_compat only

* Fri Jul 11 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt2
- Fix set SSL port in files (Closes: #16337)

* Tue Jul 08 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.9-alt1
- 2.2.9
- Security fixes (CVE-2008-2364, CVE-2007-6420)

* Mon Jul 07 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.8-alt7
- Fix #16290: update %%apache_moduledir sets

* Sun Jul 06 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.8-alt6
- Unset BuildArch %%_target_cpu

* Fri Jul 04 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.8-alt5
- Fix #16253

* Thu Jun 26 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.8-alt4
- Fix #16165:
  + unuse vhosts-filesystem package
  + remove provide favour description file for apachkconfig
- Fix conflicts
- Set BuildArch to noarch for subpackages

* Tue Jun 17 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.8-alt3
- Add config file for icons dir
- Create subpackages for set DocumentRoot in %%a2_datadir:
  + %%name-compat
  + %%name-mod_ssl-compat
- Fix rpm group for %%name-configs-A1PROXIED subpackage
- Fix sets priority for sites-available/default*.conf files
- Fix substitute the real paths in configs

* Tue Jun 10 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.8-alt2.1
- Add using webserver-common package:
  + removing Provides dirs
    %%apache_datadir/{,cgi-bin/,html/{,addon-modules/},icons/{,small/}}
  + adding %%apache_user to %%webserver_group
- Adding conflicts to apache{,-*} < 1.3.41rusPL30.23-alt4.1
- Create subpackages:
  + %%name-docs
  + %%name-cgi-bin
  + %%name-manual-addons
  + %%name-html
  + %%name-icons
- Update subpackage %%name-manual for %%name-docs using

* Thu Apr 03 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.8-alt2
- Rebuild

* Fri Feb 29 2008 Aleksey Avdeev <solo@altlinux.ru> 2.2.8-alt1
- 2.2.8: security fixes (CVE-2007-6421, CVE-2007-6421, CVE-2007-6422,
  CVE-2007-6388, CVE-2007-5000, CVE-2008-0005)
- Fix #14601: less-than-optimal examples in conf/sites-available.
  (Thanks Mikhail Gusarov <dottedmag altlinux org>)

* Wed Oct 17 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.6-alt5
- Fix #12898: modify packaged config files to disable directory autoindexing
  by default (/home/*/public_html stay indexed though); you might want
  to reconsider that in case the configuration wasn't touched at all
  (thus will be replaced during package upgrade) but directory indexes
  are needed. (Thanks Timur Batyrshin <batyrshin ieml ru> for
  proposal/discussion/patch):
  + Update apache2-2.2.6-alt-configs-*.patch to
    apache2-2.2.6-alt-configs-0.3.patch
- Fix #13125: perl path to /usr/bin/perl sets in
  /var/www/apache2/cgi-bin/printenv. (Thanks PeterVF <petervf front ru>)
  + Adding apache2-2.2.6-alt-cgi-0.1.patch

* Fri Sep 28 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.6-alt4
- Update apache2-2.2.6-alt-debian.conf-*.patch to
  apache2-2.2.6-alt-debian.conf-0.3.patch:
  + fix #12933 bug
- Move Provides: %%apache_configs_name = %%apache_configs_version
  from %%name-common to %%name subpackage
- Add Provides: %%apache_configs_dirs_name = %%apache_configs_dirs_version
  to %%name-common subpackage
- Add Requires: %%apache_configs_dirs_name >= %%apache_configs_branch
  and remove Requires: %%apache_configs_name in subpackage
  + %%name
  + %%name-configs-A1PROXIED
  + %%name-manual
  + %%name-mod_ssl
  + %%name-suexec
- Add macros in %%_sysconfdir/rpm/macros.d/%%name
  + %%apache_configs_dirs_name
  + %%apache_configs_dirs_version

* Wed Sep 19 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.6-alt3
- Adding %%ghost %%a_sysconfdir/ssl.{crt,key}/server.{crt,key} (#12059)
- Adding Provides and Summary in any config in
  {extra,ports,sites}-available/*.conf files
  + Update apache2-2.2.6-alt-configs-*.patch to
    apache2-2.2.6-alt-configs-0.2.patch
  + Update apache2-alt-configs-*.tar to apache2-alt-configs-0.9.tar
- Update Provides: %%apache_configs_name to 2.2.0

* Sun Sep 16 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.6-alt2
- Update apache2-2.2.6-alt-debian.conf-*.patch to
  apache2-2.2.6-alt-debian.conf-0.2.patch:
  + remove auto selecting for cgi/cgid module in /usr/sbin/a2enmod

* Fri Sep 14 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.6-alt1
- 2.2.6
- Adding SECURITY to upstream:
  + CVE-2007-4465 (cve.mitre.org)
- Updating patchs for 2.2.6:
  + apache2-2.2.5-alt-debian.conf-0.1.patch to
    apache2-2.2.6-alt-debian.conf-0.1.patch
  + apache2-2.2.5-alt-configs-0.1.patch to
    apache2-2.2.6-alt-configs-0.1.patch
  + apache2-2.2.5-alt-default_https.conf.in-0.1.patch to
    apache2-2.2.6-alt-default_https.conf.in-0.1.patch
- Set Requires libapr1-devel >= 1.2.8-alt1.1
- Add %%name-configs-A1PROXIED subpackage
- Add Provides in %%name-common subpackage
  + %%apache_configs_name = %%apache_configs_version
  + %%apache_config_tool_name = %%apache_config_tool_version
- Add Requires: %%apache_configs_name >= %%apache_configs_branch
  and %%apache_config_tool_name >= %%apache_config_tool_branch in subpackage
  + %%name
  + %%name-configs-A1PROXIED
  + %%name-manual
  + %%name-mod_ssl
  + %%name-suexec
- Add macros in %%_sysconfdir/rpm/macros.d/%%name
  + %%apache_configs_name
  + %%apache_configs_branch
  + %%apache_configs_version
  + %%apache_config_tool_name
  + %%apache_config_tool_branch
  + %%apache_config_tool_version
  + %%apache_mmn
  + %%apache_libdb
- Add file Provides: %%a_sbindir/%%a_dname in subpackage
  + %%name-httpd-worker
  + %%name-httpd-prefork
  + %%name-httpd-event

* Sat Aug 18 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.5-alt1
- 2.2.5
- Adding SECURITY to upstream (old patchs removing):
  + CVE-2007-3847
  + CVE-2007-1863 (remove apache2-2.2.3-fedora-fix-CVE-2007-1863.patch)
  + CVE-2007-3304 (remove apache2-2.2.4-alt-fix-CVE-2007-3304.0.1.patch)
  + CVE-2006-5752 (remove apache2-2.2.3-fedora-fix-CVE-2006-5752.patch)
  + CVE-2007-1862 (remove apache2-2.2.4-asc-fix-CVE-2007-1862-0.1.patch)
- Updating patchs for 2.2.5:
  + apache2-2.2.4-alt-debian.conf-0.18.patch to
    apache2-2.2.5-alt-debian.conf-0.1.patch
  + apache2-2.2.4-alt-configs.0.2.patch to apache2-2.2.5-alt-configs-0.1.patch
  + apache2-2.2.4-alt-default_https.conf.in.0.1.patch to
    apache2-2.2.5-alt-default_https.conf.in-0.1.patch

* Tue Jul 24 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt33
- Create and using docs/conf/extra-available/Directory_*_default.conf.in
  + Update apache2-2.2.4-alt-configs.*.patch to apache2-2.2.4-alt-configs.0.2.patch
  + Update apache2-alt-configs-*.tar to apache2-alt-configs-0.9.tar
- Update apache2-2.2.4-alt-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.18.patch
  remove bad Options in <Directory "@exp_cgidir@">

* Sat Jul 07 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt32
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.17.patch
  + %%a_sbindir/a2chkconfig.in: fix find using

* Thu Jul 05 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt31
- Using Fedora Project patchs for security fixes:
  + CVE-2006-5752 apache2-2.2.3-fedora-fix-CVE-2006-5752.patch
  + CVE-2007-1863 apache2-2.2.3-fedora-fix-CVE-2007-1863.patch
  + CVE-2007-3304 apache2-2.2.4-alt-fix-CVE-2007-3304.0.1.patch
    (apache2-2.2.3-fedora-fix-CVE-2007-3304.patch -- removing)
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.16.patch
  + adding deleteing all broken symbolic links in %%a_sysconfdir/*-enabled
    in a2chkconfig
- Add apache2-2.2.4-alt-configs.0.1.patch
  + moving NameVirtualHost to %%a_sysconfdir/sites-available/ports_all.conf
- Update *-alt-configs-* to apache2-alt-configs-0.8
  + enabled %%a_sysconfdir/sites-available/ports_all.conf by default

* Wed Jul 04 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt30
- Add Fedora Project patchs for security fixes:
  + CVE-2006-5752 apache2-2.2.3-fedora-fix-CVE-2006-5752.patch
  + CVE-2007-1863 apache2-2.2.3-fedora-fix-CVE-2007-1863.patch
  + CVE-2007-3304 apache2-2.2.3-fedora-fix-CVE-2007-3304.patch

* Sun Jun 17 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt29
- Fix moving debuging messages from a2chkconfig (in rpm scripts) to /dev/null
- Renamed files *defoult* to *default*
  + update apache2-2.2.4-alt-debian.conf-*.patch to
    apache2-2.2.4-alt-debian.conf-0.15.patch
  + update apache2-alt-configs-*.tar to apache2-alt-configs-0.7.tar

* Sun Jun 17 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt28
- Fix a2chkconfig: ignore error in a2{en,dis}* adding
  + update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.14.patch
- Moving debuging messages from a2chkconfig (in rpm scripts) to /dev/null

* Sun Jun 17 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt27
- Fix find extra-available/*.conf to package
  + update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.13.patch

* Thu Jun 14 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt26
- Fix CVE-2007-1862
  (see <http://issues.apache.org/bugzilla/show_bug.cgi?id=41551>)
  + use apache2-2.2.4-asc-fix-CVE-2007-1862-0.1.patch
  + add Requires libapr1-devel >= 1.2.8-alt1.2

* Thu Jun 07 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt25
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.12.patch
  + add a2chkconfig_list (for alterator-apache2 use)
  + moving mods-available/*.conf to extra-available/*.conf, and rename
  + using SSI by defoult
- Update *-alt-configs-* to apache2-alt-configs-0.6
  + add sets dir_defoult and log_config_defoult to yes

* Wed May 02 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt24
- Building mod_authnz_ldap: --enable-authnz-ldap using
- Creating apache2-httpd-event subpackage
- Update apache2-alt-alternatives-*.tar to apache2-alt-alternatives-0.2.tar:
  add alternative for /usr/sbin/httpd2.event

* Sat Apr 28 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt23
- Using --with-program-name=%%a_dname for all server build:
  + only defoult program name (is %%a_dname) for all %%a_dname.*
  + only defoult config name (is %%a_dname.conf) for all %%a_dname.*
- Removing %%a_dname.*.conf link
- Remove Requires %%name-httpd-prefork and %%name-httpd-worker in
  %%name-devel subpackage

* Wed Apr 25 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt22
- Removing debug message in %%pre %%name
- Fix %%register_alternatives for %%name-httpd-worker
- Fix #11531: adding sleep 1 to init scripts

* Mon Apr 09 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt20
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.10.patch
  + fix support/a2chkconfig.in (#11395): read all string
    in conf/*-start.d/*.conf
  + fix #11333: adding man to a2chkconfig (thanks to Avramenko Andrew)
- Update *-alt-configs-* to apache2-alt-configs-0.4. Adding to conf/:
  + mods-start.d/010-manual.conf
  + mods-start.d/020-manual-addons.conf
  + extra-start.d/020-httpd-manual.conf (#11410)
  + extra-start.d/030-httpd-manual-addons.conf
- Man to suexec moving to %%name-suexec subpackage

* Fri Apr 06 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt19
- Add Requires %%name-httpd-prefork and %%name-httpd-worker to
  %%name-devel subpackage
- Remove %%name-init subpackage
- Fix packages updating

* Thu Apr 05 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt18
- Add Provides to %%name-common subpackage:
  + %%name-mmn
  + %%name-libdb
- Remove Provides:
  + %%name-common-mmn
  + %%name-common-libdb
- Updating %%a_sbindir/%%a_dname:
  + renamed %%a_sbindir/%%a_dname to %%a_sbindir/%%a_dname.prefork
  + use alternatives for create symlinc %%a_sbindir/%%a_dname to
    %%a_sbindir/%%a_dname.prefork or %%a_sbindir/%%a_dname.worker
- Adding symlink for %%a_sysconfdir/%%a_dname.conf:
  + %%a_sysconfdir/%%a_dname.prefork.conf
- Adding trigger scripts to %%a_dname for update/remove
  apache2-{init,httpd-{prefork,worker}}

* Tue Apr 03 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt17
- Creating subpackage:
  + apache2-common
  + apache2-httpd-{worker,prefork}
  + apache2-init
- Update *-alt-configs-* to apache2-alt-configs-0.3
  + adding httpd-manual-addons.conf, for using @apache_addondocdir@

* Sun Apr 01 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt16
- Disable httpd2 service startup by default (#11280):
  that might lead to undesired consequences in case of
  "accidentally" installed packages and/or forgetting
  about them while configuring services; see also [ru]:
  http://lists.altlinux.org/pipermail/devel/2006-December/039909.html
- Fix creating the %%a_sysconfdir/%%a_dname.conf when updating
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.9.patch
  + fix widely reported in the a2chkconfig (#11274)
  + fix messages from a2{en,dis}{mod,site,port,extra} (#11247)


* Thu Mar 29 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt15
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.8.patch
  + Fix #11247
- Update *-alt-configs-* to apache2-alt-configs-0.2
  + Fix #11245
  + Fix #11246
- Adding README.ALT.ru_RU.KOI8-R

* Mon Mar 26 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt14
- Removing apache2-2.2.4-alt-conf.in-A1PROXIED.patch (is old)
- default-0.1.a2chkconfig.tar updated to apache2-alt-configs-0.1.tar
  + add defoult configs for virtual hosts template, A1PROXIED using and
    for using old @rel_sysconfdir@/addon.d
- Fix User, Group and ServerAdmin sets to configs
- Unused SSL option
- Removing dirs (unused, is old):
  + %%apache_vhosttempldir
  + %%apache_vhostconfdir
  + %%apache_addonvhostconfdir
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.7.patch
  + fix: remove using /etc/httpd2/conf/extra/httpd-manual.conf

* Mon Mar 26 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt13
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.6.patch
  + fix support/a2chkconfig.in
- Add apache2-2.2.4-alt-default_https.conf.in.0.1.patch
  + fix SSL keys patchs
- Renamed macros:
  + %%ad_name to %%a_dname
  + %%apache_apxs to %%a_apxs
  + %%apache_addondocdir to %%a_addondocdir
- Removing macros in spec:
  + %%apache_basedir (use %%a_prefix)
  + %%apache_confdir (use %%a_sysconfdir)
  + %%apache_datadir (use %%a_datadir)
  + %%apache_htdocsdir (use %%a_docsdir)
  + %%apache_cgibindir (use %%a_cgidir)
  + %%apache_logdir (use %%a_logfiledir)
  + %%apache_moduledir (use %%a_libexecdir)
- Use sed script for substitute the real paths in all configs
- Fix scripts

* Sun Mar 25 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt12
- Not using old configs
  + renamed old %%a_sysconfdir/%%ad_name{,.worker}.conf to
    %%a_sysconfdir/%%ad_name{,.worker}.conf.rpmold
  + create new %%a_sysconfdir/%%ad_name{,.worker}.conf
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.5.patch
  + fix adding %%a_sbindir/a2{en,dis}{port,extra}
  + adding create %%a_sbindir/{extra,ports,sites,mods}-start.d
  + add %%a_sbindir/a2chkconfig
- Adding %%a_sysconfdir/*-start.d/*.conf (configs files for a2chkconfig)
- Fix missed $OPTIONS variable in conftest() function in the init script
  (bug#11156): use patch from Nikolay A. Fetisov <naf@altlinux.org>
- Renamed old %%a_manualdir to %%a_manualdir.rpmold, for create symlink to
  %%_docdir/%%a_name-manual-%%apache_version/manual
- Moveing %%a_manualdir to %%_docdir/%%a_name-manual-%%apache_version/manual
  and create symlink from %%a_manualdir
- Using TMPDIR=/var/spool/apache2/tmp in init script
- Add triggerpostun fo deleting old symlink
  %%_docdir/apache2-manual-2.2.4/manual

* Sun Mar 18 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt11
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.4.patch
  + add %%a_sbindir/a2{en,dis}{port,extra}
  + fix Makefile.in (for configs create)

* Sun Mar 18 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt10
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.3.patch
  + fix %%a_sbindir/a2{en,dis}site
  + using <IfModule authz_host_module> in *.conf files

* Fri Mar 16 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt9
- Remove old patchs:
  + httpd-2.0.55-alt-build.patch
- Add utils:
  + %%a_sbindir/a2{en,dis}{mod,site}
  + %%a_sbindir/check_forensic
- Add mans:
  + a2{en,dis}mod.8
  + checkgid.8
  + check_forensic.8
- Update *-debian.conf-*.patch to apache2-2.2.4-alt-debian.conf-0.2.patch

* Thu Mar 15 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt8
- Add apache2-2.2.4-alt-debian.conf-0.1.patch, for using Debian`like
  cofigs dirs:
  + %%a_sysconfdir/extra-available/
  + %%a_sysconfdir/extra-enabled/
  + %%a_sysconfdir/mods-available/
  + %%a_sysconfdir/mods-enabled/
  + %%a_sysconfdir/ports-available/
  + %%a_sysconfdir/ports-enabled/
  + %%a_sysconfdir/sites-available/
  + %%a_sysconfdir/sites-enabled/
- Remove old patchs:
  + apache2-2.2.4-alt-conf.in-include-0.1.patch
  + apache2-2.2.4-alt-Makefile.in-SSL.patch
  + apache2-2.2.4-alt-Makefile.in-LoadModule.patch

* Wed Mar 07 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt7
- Add dir provides:
  + %%a_proxycachedir/
  + %%_spooldir/apache%%apache_branch/{,tmp,sessions,uploads}

* Wed Feb 28 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt6
- Link with system PCRE library!
- Update warning message from %%pre

* Mon Feb 26 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt5
- set requires for %%name-mod_ssl
  + %%name = %%apache_version-%%apache_release
  + %%name-libdb = %%n_dbver
- modufy auto update in %%pre:
  + update %%a_sysconfdir/httpd2{,.worker}.conf only


* Tue Feb 20 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt4
- use apache2-2.2.4-alt-conf.in-0.2.patch:
  + corected module name for using in <IfModule ...>
- no modify defoult root page (use original upstrem page)
- remove use`nt files:
  + altlinux.html
  + altlinux.png
- no corected path to perl
- moved to apache2-suexec:
  + %%a_sysconfdir/modules.d/A.[0-9][0-9][0-9]_suexec.conf
  + %%a_libexecdir/mod_suexec.so

* Fri Feb 16 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt3
- auto update %%a_sysconfdir/httpd2*.conf including in %%pre:
  + added "Include /etc/httpd2/conf/modules.d/A.*.conf"
  + commented all LoadModule directives
- use %%post_service httpd%%apache_branch in mod_ssl pakage

* Tue Feb 13 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt2
- adding %%a_sysconfdir/extra/httpd-ssl.conf to apache2-mod_ssl
- update apache2-2.2.4-alt-conf.in.patch to 0.1:
  + update patchs for SSL keys
- update apache2-2.2.4-alt-conf.in-include-0.1.patch:
  + activate httpd-ssl.conf including
- adding apache2-2.2.4-alt-Makefile.in-LoadModule.patch:
  + create %%a_sysconfdir/modules.d/A.*.conf for LoadModule using

* Sun Feb 11 2007 Aleksey Avdeev <solo@altlinux.ru> 2.2.4-alt1
- 2.2.4
- use PrintPath
- add htcacheclean
- add patchs:
  + apache2-2.2.4-alt-conf.in.patch
  + apache2-2.2.4-alt-conf.in-include.patch
  + apache2-2.2.4-alt-conf.in-A1PROXIED.patch
  + apache2-2.2.4-alt-Makefile.in-SSL.patch
- apache_native_apr switch delete:
  + no build native libapr
  + use external libapr1 onli
- prevent build if upstream MMN differs from mmn macro
- merge 2.0.59-alt0.M24.1:
  + set pkgconfig in BuildPreReq

* Wed Nov 01 2006 Aleksey Avdeev <solo@altlinux.ru> 2.0.59-alt3
- fix build: add patch from Sviatoslav Sviridov <svd@altlinux.ru>
  for spec

* Tue Oct 31 2006 Aleksey Avdeev <solo@altlinux.ru> 2.0.59-alt2
- build libdb4.4 to defoult
- add new provides: %%name-libdb = %%n_dbver
- turn back conditional libdb4.4-devel, libdb4.3-devel (for Compact 3.0)
  or libdb4.2-devel (for Master 2.4) build

* Sun Oct 22 2006 Sviatoslav Sviridov <svd@altlinux.ru> 2.0.59-alt1.1.libdb4.4
- Rebuild with libdb4.4

* Mon Jul 31 2006 Aleksey Avdeev <solo@altlinux.ru> 2.0.59-alt1
- 2.0.59

* Wed Jul 12 2006 Aleksey Avdeev <solo@altlinux.ru> 2.0.55-alt9
- rebuilt for update libldap (use libldap-2.3)

* Sat Apr 01 2006 Aleksey Avdeev <solo@altlinux.ru> 2.0.55-alt8
- link with no system PCRE library (old!)

* Wed Mar 29 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0.55-alt7.2
- Fixed build with ld --as-needed.
- Link with system PCRE library!

* Wed Mar 29 2006 Aleksey Avdeev <solo@altlinux.ru> 2.0.55-alt7
- hack for --as-needed fix

* Sun Mar 19 2006 Aleksey Avdeev <solo@altlinux.ru> 2.0.55-alt5
- update spec for backports in 3.0

* Thu Mar 09 2006 Aleksey Avdeev <solo@altlinux.ru> 2.0.55-alt4
- merge 2.0.55-alt0.M24.1 (Grigory Batalov <bga@altlinux.ru>):
  + check for libapr >= 0.9.7
  + turn back conditional static build
  + delaycompress in logrotate config
  + change /usr/sbin/service to /sbin/service in logrotate config
  + change service to reload to httpd2 in logrotate config
  + log dir owned by apache2 group
  + htdocs dir owned by webmaster group
- update conditional static build
- turn back conditional libdb4.3-devel or libdb4.2-devel
  (for Master 2.4) build

* Mon Jan 23 2006 Anton Farygin <rider@altlinux.ru> 2.0.55-alt3.1
- NMU:
    - requires fixed (libdb4.2-devel-static changed to libdb4.3-devel)
    - tested build for x86_64

* Wed Nov 23 2005 Yury Konovalov <yurix@altlinux.ru> 2.0.55-alt3
- Require newer apr bug #8517

* Mon Nov 21 2005 Yury Konovalov <yurix@altlinux.ru> 2.0.55-alt2
- fix bug #7490

* Sat Oct 15 2005 Yury Konovalov <yurix@altlinux.ru> 2.0.55-alt1
- 2.0.55
- adopt to new ALT common macroses behaivour

* Mon Aug 15 2005 Yury Konovalov <yurix@altlinux.ru> 2.0.54-alt2
- remove unexpanded macros apache2-suexec Bug#:7490

* Tue Apr 19 2005 Yury Konovalov <yurix@altlinux.ru> 2.0.54-alt1
- 2.0.54
- fix initscript hostname handling (bug#6291)

* Mon Dec 27 2004 Sviatoslav Sviridov <svd@altlinux.ru> 2.0.52-alt3
- updated alt-configure patch to check for available libldap
  and link with libldap
- applied patches:
  + httpd-2.0.52-sslauth.patch
  + httpd-2.0.52-SSLCipherSuite-bypass-CAN-2004-0885.diff
  + httpd-2.0.52-memory-consumption-DoS-CAN-2004-0942.diff
  + util_ldap_cache_mgr.c.patch

* Sun Nov 14 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.52-alt2
- Fixed build with system libapr/libaprutil,
  patch from Sviatoslav Sviridov.
- Built with system libapr/libaprutil and openldap-2.2.18-alt3.

* Wed Oct 20 2004 Yury Konovalov <yurix@altlinux.ru> 2.0.52-alt1
- 2.0.52
- build with native apr

* Thu Sep 16 2004 Yury Konovalov <yurix@altlinux.ru> 2.0.51-alt1
- 2.0.51

* Sun Aug 29 2004 Yury Konovalov <yurix@altlinux.ru> 2.0.50-alt4
- fix build failed with APR

* Mon Jul 12 2004 Yury Konovalov <yurix@altlinux.ru> 2.0.50-alt3
- rpm trigger script removed

* Mon Jul 05 2004 Yury Konovalov <yurix@altlinux.ru> 2.0.50-alt2
- rebuild

* Tue Jun 29 2004 Yury Konovalov <yurix@altlinux.ru> 2.0.50-alt1
- 2.0.50
- provide favour description file for apachkconfig

* Mon Jun 07 2004 Yury Konovalov <yurix@altlinux.ru> 2.0.49-alt2
- added vhost.d-addon directory and apache_addonvhostconfdir RPM macros
- apache now use apache2 user/group account by default
- Include only A.*.conf files from addon.d vhosts.d vhosts.d-addon dirs
  to make configs been disabled by default.
- Add AliasMatch to manual-addons directory. Also link is included in main
  manual page

* Tue May 18 2004 Yury Konovalov <yurix@altlinux.ru> 2.0.49-alt1
- rebuild for current Sisyphus
- use vhosts-filesystem macroses for default docroot and vhosts directory.
- provide vhosts config template to be used by upcoming vhosts management scripts.
- 2.0.49

* Sat Nov 15 2003 Yury Konovalov <yurix@altlinux.ru> 2.0.48-uc4
- provide apache2-liapr* packages in case build with internal apr
  otherwise make apache2-devel provide fake apache2-liapr* packages
- provide conf.d and vhost.d configuration directories.
  (Thank you, Sviataslau Svirydau for the ideas)

* Wed Nov 12 2003 Yury Konovalov <yurix@altlinux.ru> 2.0.48-uc3
- use %%make_build instead of make %%{?_smp_mflags}.
- smp patch for makefile applied.
  (Thanks for the above changes goes to Sviataslau Svirydau)

* Tue Nov 11 2003 Yury Konovalov <yurix@altlinux.ru> 2.0.48-uc2
- build charset_lite module
- apache_native_apr switch added to enable build with external
  apr.
- fix buildreq
  (Thanks to Sviataslau Svirydau for pointing this)

* Sat Nov 01 2003 Yury Konovalov <yurix@altlinux.ru> 2.0.48-uc1
- Remove Alt layout file. Autogenerate it from spec instead
- Provide option to build packages that could be installed on
  the same host with ru-apache
- Make spec to look like those for russian apache
    - move suexec into suexec package
    - update macroses to be ru-apache compatible
    - provide rpm macros in devel package
    - steal distrib detection method from ru-apache package
- 2.0.48

* Tue Sep 09 2003 Yury Konovalov <yurix@altlinux.ru> 2.0.46-uc2
- Fix prefix to be apache_root.

* Wed Aug 27 2003 Yury Konovalov <yurix@altlinux.ru> 2.0.46-uc1
- First build for ALTLinux.

* Sat Apr 5 2003 Graham Leggett <minfrin@apache.org> 2.0.46-dev
- Moved mime.types back to the default location.
- Added mod_ldap and friends, mod_cache and friends.
- Added openldap dependancy.

* Sun Mar 30 2003 Graham Leggett <minfrin@apache.org> 2.0.45-1
- Created generic Apache rpm spec file from that donated by Redhat.
- Removed Redhat specific patches and boilerplate files.
- Removed SSL related Makefiles.

* Mon Feb 24 2003 Joe Orton <jorton@redhat.com> 2.0.40-21
- add security fix for CAN-2003-0020; replace non-printable characters
  with '!' when printing to error log.
- disable debuginfo on IA64.

* Tue Feb 11 2003 Joe Orton <jorton@redhat.com> 2.0.40-20
- disable POSIX semaphores to support 2.4.18 kernel (#83324)

* Wed Jan 29 2003 Joe Orton <jorton@redhat.com> 2.0.40-19
- require xmlto 0.0.11 or later
- fix apr_strerror on glibc2.3

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 2.0.40-18
- rebuilt

* Thu Jan 16 2003 Joe Orton <jorton@redhat.com> 2.0.40-17
- add mod_cgid and httpd binary built with worker MPM (#75496)
- allow choice of httpd binary in init script
- pick appropriate CGI module based on loaded MPM in httpd.conf
- source /etc/sysconfig/httpd in apachectl to get httpd choice
- make "apachectl status" fail gracefully when links isn't found (#78159)

* Mon Jan 13 2003 Joe Orton <jorton@redhat.com> 2.0.40-16
- rebuild for OpenSSL 0.9.7

* Fri Jan  3 2003 Joe Orton <jorton@redhat.com> 2.0.40-15
- fix possible infinite recursion in config dir processing (#77206)
- fix memory leaks in request body processing (#79282)

* Thu Dec 12 2002 Joe Orton <jorton@redhat.com> 2.0.40-14
- remove unstable shmht session cache from mod_ssl
- get SSL libs from pkg-config if available (Nalin Dahyabhai)
- stop "apxs -a -i" from inserting AddModule into httpd.conf (#78676)

* Wed Nov  6 2002 Joe Orton <jorton@redhat.com> 2.0.40-13
- fix location of installbuilddir in apxs when libdir!=/usr/lib

* Wed Nov  6 2002 Joe Orton <jorton@redhat.com> 2.0.40-12
- pass libdir to configure; clean up config_vars.mk
- package instdso.sh, fixing apxs -i (#73428)
- prevent build if upstream MMN differs from mmn macro
- remove installed but unpackaged files

* Wed Oct  9 2002 Joe Orton <jorton@redhat.com> 2.0.40-11
- correct SERVER_NAME encoding in i18n error pages (thanks to Andre Malo)

* Wed Oct  9 2002 Joe Orton <jorton@redhat.com> 2.0.40-10
- fix patch for CAN-2002-0840 to also cover i18n error pages

* Wed Oct  2 2002 Joe Orton <jorton@redhat.com> 2.0.40-9
- security fixes for CAN-2002-0840 and CAN-2002-0843
- fix for possible mod_dav segfault for certain requests

* Tue Sep 24 2002 Gary Benson <gbenson@redhat.com>
- updates to the migration guide

* Wed Sep  4 2002 Nalin Dahyabhai <nalin@redhat.com> 2.0.40-8
- link httpd with libssl to avoid library loading/unloading weirdness

* Tue Sep  3 2002 Joe Orton <jorton@redhat.com> 2.0.40-7
- add LoadModule lines for proxy modules in httpd.conf (#73349)
- fix permissions of conf/ssl.*/ directories; add Makefiles for
  certificate management (#73352)

* Mon Sep  2 2002 Joe Orton <jorton@redhat.com> 2.0.40-6
- provide "httpd-mmn" to manage module ABI compatibility

* Sun Sep  1 2002 Joe Orton <jorton@redhat.com> 2.0.40-5
- fix SSL session cache (#69699)
- revert addition of LDAP support to apr-util

* Mon Aug 26 2002 Joe Orton <jorton@redhat.com> 2.0.40-4
- set SIGXFSZ disposition to "ignored" (#69520)
- make dummy connections to the first listener in config (#72692)

* Mon Aug 26 2002 Joe Orton <jorton@redhat.com> 2.0.40-3
- allow "apachectl configtest" on a 1.3 httpd.conf
- add mod_deflate
- enable LDAP support in apr-util
- don't package everything in /var/www/error as config(noreplace)

* Wed Aug 21 2002 Bill Nottingham <notting@redhat.com> 2.0.40-2
- add trigger (#68657)

* Mon Aug 12 2002 Joe Orton <jorton@redhat.com> 2.0.40-1
- update to 2.0.40

* Wed Jul 24 2002 Joe Orton <jorton@redhat.com> 2.0.36-8
- improve comment on use of UserDir in default config (#66886)

* Wed Jul 10 2002 Joe Orton <jorton@redhat.com> 2.0.36-7
- use /sbin/nologin as shell for apache user (#68371)
- add patch from CVS to fix possible infinite loop when processing
  internal redirects

* Wed Jun 26 2002 Gary Benson <gbenson@redhat.com> 2.0.36-6
- modify init script to detect 1.3.x httpd.conf's and direct users
  to the migration guide

* Tue Jun 25 2002 Gary Benson <gbenson@redhat.com> 2.0.36-5
- patch apachectl to detect 1.3.x httpd.conf's and direct users
  to the migration guide
- ship the migration guide

* Fri Jun 21 2002 Joe Orton <jorton@redhat.com>
- move /etc/httpd2 back to /etc/httpd
- add noindex.html page and poweredby logo; tweak default config
  to load noindex.html if no default "/" page is present.
- add patch to prevent mutex errors on graceful restart

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 2.0.36-4
- automated rebuild

* Wed Jun 12 2002 Joe Orton <jorton@redhat.com> 2.0.36-3
- add patch to fix SSL mutex handling

* Wed Jun 12 2002 Joe Orton <jorton@redhat.com> 2.0.36-2
- improved config directory patch

* Mon May 20 2002 Joe Orton <jorton@redhat.com>
- initial build; based heavily on apache.spec and mod_ssl.spec
- fixes: #65214, #58490, #57376, #61265, #65518, #58177, #57245
