%define realname nrpe
%define nagios_confdir   %_sysconfdir/nagios
%define contacts_cfgdir  %_sysconfdir/nagios/contacts
%define plugins_cmddir   %_sysconfdir/nagios/commands
%define templates_cfgdir %_sysconfdir/nagios/templates
%define nagios_plugdir   %_libexecdir/nagios/plugins
%define nagios_evhdir    %_libexecdir/nagios/eventhandlers
%define plugin_docdir    %_docdir/%name-%version
%define nagios_usr nagios
%define nagios_grp nagiosnew

Name: nagios-%realname
Version: 3.2.1
Release: alt5

Summary: NRPE -- Nagios(R) Remote Plug-ins Execution daemon.
Summary(ru_RU.UTF-8): NRPE -- Сервер выполнения команд Nagios(R) на удаленном хосте.
License: GPLv2
Group: Monitoring
URL: http://www.nagios.org

###########################################
# Relations with Nagios daemon or other nagios-plugins executors pkgs (like NRPE)

# Provide the abstract service names (which are virtual pkg names),
# specify their origin (our pkg name as the epoch + version-release):
Provides: nagios-daemon = %EVR

# Conflict with all other real pkgs which provide the same services
# (they should specify the origin the same way, so the epoch-version-release
# of the virtual pkgs will always differ from that of ours if they are provided
# by a different real pkg):
Conflicts: nagios-daemon < %EVR
Conflicts: nagios-daemon > %EVR
# End of the statements to describe relations with Nagios daemon or NRPE pkgs
########################################

Requires: nagios-plugins
Requires(pre): nagios-common
Conflicts: nagios < 3.0.6-alt12

Source0: %name-%version.tar
Source1: %realname-init
Source2: nagios-addons-nrpe.cfg

# fix default NRPE configuration
Patch0: %realname-3.2.1-alt-config.patch
Patch1: %realname-2.12-alt-defpath.patch

# Automatically added by buildreq on Sat Jul 01 2006
BuildRequires: libssl-devel openssl

%package -n nagios-addons-%realname
Summary: Nagios(R) plug-in for NRPE.
Summary(ru_RU.UTF-8): Модуль для Nagios(R), взаимодействующий с сервером NRPE.
License: GPLv2
Group: Monitoring
PreReq: nagios-plugins
Provides: nagios-plugins-nrpe = %version
Obsoletes: nagios-plugins-nrpe

%description
The %name packages contains the Nagios(R) Remote Plug-ins Executor
-- daemon which can execute predefined commands on the remote host.
Execution request is send via check_nrpe Nagios(R) plug-in. Allowed
monitoring commands are described in the daemon configuration file.

Install the %name package if you want accept and procedd requests
from check_nrpe on this hosts.

%description -l ru_RU.UTF-8
NRPE -- сервер выполнения комманд системы мониторинга Nagios(R) на удаленном
хосте. Система мониторинга Nagios(R) отправляет запросы серверу NRPE с помощью
подключаемого модуля check_nrpe. Команды мониторинга описываются в файле
конфигурации демона.

Установите этот пакет, если вы желаете принимать запросы на выполнение команд
мониторинга от сервера Nagios(R).

%description -n nagios-addons-%realname
Plug-in for Nagios(R) monitoring system. With this plug-in you can send check
request to remote host, with installed NRPE, and process result of execution
as host or service state.

%description -l ru_RU.UTF-8 -n nagios-addons-%realname
Подключаемый модуль для системы мониторинга Nagios(R). Позволяет отправлять
запросы на выполнение команд мониторинга к удаленному хосту с установленным
демоном NRPE.

%prep
%setup
%patch0 -p1
#patch1 -p1

%build
%configure \
    --with-nrpe-user=%nagios_usr \
    --with-nrpe-group=%nagios_grp \
    --with-nrpe-port=65534 \
    --enable-ssl \
    --disable-command-args \
    --with-pluginsdir="%_libexecdir/nagios/plugins"

%make_build all
#pushd contrib
#	gcc -o nrpe_check_control nrpe_check_control.c
#popd

%install
mkdir -p %buildroot%plugin_docdir

# install binaries
install -pDm0711 src/nrpe %buildroot%_sbindir/nrpe
install -pDm0711 src/check_nrpe %buildroot%nagios_plugdir/check_nrpe
#install -pDm0711 contrib/nrpe_check_control %buildroot%nagios_evhdir/nrpe_check_control

# install config
install -pDm0644 sample-config/nrpe.cfg %buildroot%nagios_confdir/nrpe.cfg
install -pDm0644 %SOURCE2 %buildroot%plugins_cmddir/nagios-addons-nrpe.cfg

#install init-script
install -pDm0755 %SOURCE1 %buildroot%_initdir/nrpe

# install docs
for d in CHANGELOG.md LEGAL README* SECURITY.md; do
    install -m 0644 $d %buildroot%plugin_docdir/
done
#install -m 0644 contrib/README.nrpe_check_control %buildroot%plugin_docdir/

mkdir -p %buildroot%nagios_confdir/nrpe-commands

%post
%post_service %realname

%preun
%preun_service %realname

%files
%dir %nagios_confdir
%dir %nagios_confdir/nrpe-commands
%config(noreplace) %nagios_confdir/nrpe.cfg
%_initdir/nrpe
%_sbindir/nrpe
%doc %plugin_docdir/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way.
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/nagios-nrpe-%version

%files -n nagios-addons-%realname
%config(noreplace) %plugins_cmddir/nagios-addons-nrpe.cfg
%nagios_plugdir/check_nrpe
#%nagios_evhdir/nrpe_check_control
%doc %plugin_docdir/*

%changelog
* Thu May 07 2020 Paul Wolneykien <manowar@altlinux.org> 3.2.1-alt5
- Remove check_timed_logs.pl: use package nagios-plugins-timed-logs
  instead.
- Set to use "nagiosnew" group in all configs.

* Fri Feb 07 2020 Paul Wolneykien <manowar@altlinux.org> 3.2.1-alt4
- Merged-in changes from v3.2.1-alt2.M80C.3.

* Fri Feb 07 2020 Paul Wolneykien <manowar@altlinux.org> 3.2.1-alt2.M80C.3
- Enable inclusion of /etc/nagios/nrpe-commands by default.

* Wed Jan 22 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 3.2.1-alt3
- merge c8.1 changes into sisyphus

* Mon Aug 05 2019 Ivan Zakharyaschev <imz@altlinux.org> 3.2.1-alt2.M80C.2
- temporarily disabled build of check_control (thx nbr@)

* Mon Aug 05 2019 Ivan Zakharyaschev <imz@altlinux.org> 3.2.1-alt2.M80C.1
- do not allow arguments (to harden more against CVE-2014-2913, BDU:2019-01845):
  + set dont_blame_nrpe=0
  + --disable-command-args
- package check_timed_logs.pl

* Fri Jan 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.2.1-alt2
- Real build of new version since 2.12. (Fixes CVE-2014-2913, BDU:2019-01845)
- Update patches.
- Massive cleanup spec.
- Change build scheme.

* Tue Nov 06 2018 Grigory Ustinov <grenka@altlinux.org> 3.2.1-alt1
- Build new version (Closes: #35576).

* Wed Oct 10 2018 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt2
- Rebuild without libwrap.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jun 07 2017 Denis Medvedev <nbr@altlinux.org> 3.1.1-alt1
- upgraded to upstream  version 3.1.1

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.12-alt3.qa2
- NMU: rebuilt for debuginfo.

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.12-alt3.qa1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.12-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for nagios-nrpe
  * postclean-05-filetriggers for spec file

* Mon Jan 12 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 2.12-alt3
- fixes according to repocop repotrts:
  + add LSB headers to init-script
  + add 'Packager' tag to spec-file

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.12-alt2.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Thu May 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.12-alt2
- start NRPE daemon via init-script (#15435). By default:
  + bind to 127.0.0.1 only;
  + allow connections only from 127.0.0.1;
- fix pre-requires for nrpe package  (#15436);
- fix path to plugins directory (#15440);
- add nrpe_check_control event handler to NRPE plugins package,
  see README.nrpe_check_control for usage details
- rename package nagios-plugins-nrpe to nagios-addons-nrpe
  + add default commands definition file for Nagios plugin and event handler

* Sat Mar 29 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.12-alt1
- 2.12

* Thu Mar 13 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.11-alt1
- 2.11
- fix for ALT bug id 12611

* Sun May 06 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.8-alt1b1
- 2.8b1

* Sat Jan 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.6-alt1
- 2.6

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.5.2-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Jul 01 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.5.2-alt1
- 2.5.2
- add --enable-command-args (ALT bug id 9503)
- add SSL support

* Fri Feb 24 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.4-alt1
- 2.4
- misc fixes based on info from nagios-devel@

* Mon Feb 13 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3-alt1
- 2.3

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.0-alt1.1
- Rebuilt with openssl-0.9.7d.

* Sun Dec 21 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0-alt1
- v.2.0

* Sun Mar 30 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.8-alt1
- inital package for ALT Linux
