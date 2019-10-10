%define privuser  dyndns
%define privgroup dyndns
%define privpath  /var/empty

Summary: A client to update host entries on DynDNS like services
Summary(ru_RU.UTF8): Клиент для обновления записей служб динамического DNS, подобных DynDNS
Name: ddclient
Version: 3.9.0
Release: alt1
License: GPLv2
Group: System/Configuration/Networking
Url: http://ddclient.sourceforge.net/
Source0: %name-%version.tar.xz
Source1: ddclientd
Source2: README_SSL.ALT.txt
Patch0: %name-3.7.1-piddir.diff
Patch1: %name-3.9.0.fix_ssl_warning_altspecifics.diff
Patch2: %name-3.8.1-ipv6.patch
BuildArch: noarch

Requires: perl-Digest-SHA1

BuildRequires: perl-Data-Validate-IP

%description
DDclient is a small full featured client requiring only Perl and no
additional modules. It runs under most UNIX OSes and has been tested
under Linux and FreeBSD. Supported features include: operating as a
daemon, manual and automatic updates, static and dynamic updates,
optimized updates for multiple addresses, MX, wildcards, abuse
avoidance, retrying failed updates, and sending update status to
syslog and through e-mail. This release may now obtain your IP address
from any interface, web based IP detection, Watchguard's SOHO router,
Netopia's R910 router, SMC's Barricade broadband router, Netgear's
RT3xx router, Linksys' broadband routers, MaxGate's UGATE-3x00
routers, ELSA's LANCOM DSL/10 routers, Cisco's 2610, 3com 3c886a 56k
Lan Modem, SOHOWare BroadGuard NBG800, almost every other router with
user configurable FW definitions (see the sample-etc_ddclient.conf)
and now provides Full support for DynDNS.org's NIC2 protocol. Support
is also included for other dynamic DNS services. Comes with sample
scripts for use with DHCP, PPP, and cron. See the README for more
information.

%description -l ru_RU.UTF8
DDclient - маленький, но полнофункциональный клиент для службы динамического DNS,
требующий для работы только наличия Perl без каких-либо дополнительных модулей.
DDclient работает под большинством UNIX-подобных операционных систем и был
протестирован в Linux и FreeBSD. Среди поддерживаемых функций: работа в качестве
демона (сервиса), ручное и автоматическое обновление, статическое и динамическое
обновление, оптимизированное обновление для нескольких адресов, управление MX-записью,
использование масок (шаблонов) адресов, предотвращение неправильного использования,
повтор попыток обновления в случае неудачи, отправка состояния обновления службе
syslog или посредством e-mail. В настоящей версии DDclient возможно получение
IP адреса вашего компьютера с любого интерфейса, со служб обнаружения IP адресов,
расположенных в сети интернет, с роутеров Watchguard SOHO, Netopia R910,
широкополосных SMC Barricade, Netgear RT3xx, широкополосных Linksys, MaxGate UGATE-3x00,
ELSA LANCOM DSL/10, Cisco 2610, сетевого модема 3com 3c886a 56k, SOHOWare BroadGuard NBG800,
и практически любого другого роутера с конфигурируемыми пользователем настройками
встроенного сетевого экрана (firewall, см. пример конфигурации etc_ddclient.conf).
Также, настоящая версия DDclient предоставляет полную поддержку протокола NIC2 от DynDNS.org.
Поддержка других служб динамического DNS тоже включена и организуется с помощью
скриптов для совместного использования с DHCP, PPP, и cron; примеры скриптов включены
в пакет. Более детальные сведения находятся в файле README.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
# #%patch2 -p0
install -m 0644 %SOURCE2 ./README_SSL.ALT.txt

%build
%install
mkdir -p %buildroot{%_sbindir,%_sysconfdir/%name,%_initdir}
mkdir -p %buildroot/var/cache/ddclient
mkdir -p %buildroot/var/run/ddclient

install -p ddclient %buildroot%_sbindir
install -p sample-etc_ddclient.conf %buildroot%_sysconfdir/%name/ddclient.conf
touch %buildroot%_sysconfdir/%name/ddclient.cache
install -p -m 0755 %SOURCE1 %buildroot%_initdir/ddclientd

mkdir -p %buildroot/lib/tmpfiles.d
cat <<EOF >%buildroot/lib/tmpfiles.d/ddclient.conf
d /var/run/ddclient 2770 root dyndns -
EOF

%pre
/usr/sbin/groupadd -r -f %privgroup
/usr/sbin/useradd -r -s /dev/null -g %privgroup -d %privpath >/dev/null -c 'DynDNS daemon' %privuser >/dev/null 2>&1 ||:

%post
%post_service ddclientd

%files
%doc sample* README* COPY* Change*
%_sbindir/ddclient
%dir %attr(750,root,dyndns) %_sysconfdir/%name
%attr(600,dyndns,dyndns) %config(noreplace) %_sysconfdir/%name/ddclient.conf
%config(noreplace) %ghost %_sysconfdir/%name/ddclient.cache
%_initdir/ddclientd
/lib/tmpfiles.d/ddclient.conf
%dir %attr(2770,root,dyndns) /var/cache/ddclient
%dir %attr(2770,root,dyndns) /var/run/ddclient

%changelog
* Thu Oct 03 2019 Motsyo Gennadi <drool@altlinux.ru> 3.9.0-alt1
- 3.9.0 (#34396)

* Sun May 18 2014 Motsyo Gennadi <drool@altlinux.ru> 3.8.1-alt2.1
- build for Sisyphus

* Thu May 08 2014 Denis G. Samsonenko <ogion@altlinux.org> 3.8.1-alt2
- IPv6 support patch
- /lib/tmpfiles.d/ddclient.conf
- /etc/rc.d/init.d/ddclientd corrected

* Mon Nov 04 2013 Motsyo Gennadi <drool@altlinux.ru> 3.8.1-alt1
- 3.8.1

* Sun Nov 22 2009 Motsyo Gennadi <drool@altlinux.ru> 3.8.0-alt1.2
- fixed russian locale for Summary

* Wed Oct 28 2009 Motsyo Gennadi <drool@altlinux.ru> 3.8.0-alt1.1
- added russian description and summary (fixed #22091). Thanks to Phantom.

* Sun Apr 26 2009 Motsyo Gennadi <drool@altlinux.ru> 3.8.0-alt1
- 3.8.0
- change SSL warning for ALT cpecifics, add README_SSL.ALT.txt (#19256)

* Sun Apr 13 2008 Motsyo Gennadi <drool@altlinux.ru> 3.7.3-alt3
- fix repocop warning (init-condrestart)
- remove preun script (close #14745)
- fix permissions for config file
- fix license

* Sun Mar 02 2008 Motsyo Gennadi <drool@altlinux.ru> 3.7.3-alt2
- add condrestart to initscript

* Sun Aug 12 2007 Motsyo Gennadi <drool@altlinux.ru> 3.7.3-alt1
- 3.7.3

* Thu Jul 12 2007 Motsyo Gennadi <drool@altlinux.ru> 3.7.2-alt1
- 3.7.2

* Tue Apr 24 2007 Motsyo Gennadi <drool@altlinux.ru> 3.7.1-alt1
- initial build for Sisyphus

* Tue Apr 24 2007 Motsyo Gennadi <drool@altlinux.ru> 3.7.1-alt0.M24.4
- fix daemon for correctly status report (thanks to uka for hints again)

* Sun Apr 22 2007 Motsyo Gennadi <drool@altlinux.ru> 3.7.1-alt0.M24.3
- fix permissions (thanks to uka for hints)
- fixed & modify daemon

* Sun Apr 22 2007 Motsyo Gennadi <drool@altlinux.ru> 3.7.1-alt0.M24.2
- change owner for process to special pseudouser (thanks to wrar & uka for hints)
- fix permissions for pseudouser

* Sat Apr 21 2007 Motsyo Gennadi <drool@altlinux.ru> 3.7.1-alt0.M24.1
- initial build for ALT Linux (ALM-2.4)

* Tue Mar 20 2007 Lenny Cartier <lenny@mandriva.com> 3.7.1-2mdv2007.1
+ Revision: 146924
- Add /var/cache/ddclient directory

* Tue Feb 13 2007 Lenny Cartier <lenny@mandriva.com> 3.7.1-1mdv2007.1
+ Revision: 120449
- Update to 3.7.1
- Import ddclient

* Thu Jun 15 2006 Lenny Cartier <lenny@mandriva.com> 3.7.0-1mdv2007.0
- 3.7.0

* Sun Dec 18 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 3.6.7-1mdk
- New release 3.6.7

* Fri May 27 2005 Nicolas L�cureuil <neoclust@mandriva.org> 3.6.6-1mdk
- New release 3.6.6

* Wed Feb 09 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 3.6.5-3mdk
- remove patch to fix initscript

* Wed Jan 05 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.6.5-2mdk
- fix initscript (from Luis Alves)

* Tue Jan 04 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.6.5-1mdk
- 3.6.5

* Mon Nov 08 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.6.4-2mdk
- move config files to /etc/ddclient

* Thu Nov 04 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.6.4-1mdk
- 3.6.4

* Tue Dec 16 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.6.3-1mdk
- from Laurent Grawet <laurent.grawet@ibelgique.com> :
	- Initial Mandrake build.

* Sun Jul  6 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Initial build.
