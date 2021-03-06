Name: ras1c
Version: 1.2
Release: alt1

Summary: 1C:Enterprise 8 Remote Administration Server init script
Summary(ru_RU.UTF-8): Скрипт запуска сервера удалённого администрирования 1С:Предприятие 8

Group: System/Configuration/Boot and Init
License: CC-BY-4.0
Url: https://packages.altlinux.org

Source: %name-%version.tar

BuildArch: noarch
Packager: Pavel Isopenko <pauli@altlinux.org>
%description
1C:Enterprise 8 Remote Administration Server (RAS) initialization script. Start, stop, restart, status. 1C_Enterprise83-server required
%description -l ru_RU.UTF-8
Сценарий инициализации сервера удалённого администрирования (RAS) платформы 1С:Предприятие 8. Запуск, остановка, перезапуск и запрос состояния. Требуется 1C_Enterprise83-server - сервер 1С:Предприятие 8.3 для Linux

%prep
%setup

%install
%__install -Dp -m0755 ras1c %buildroot%_initdir/ras1c

%files
%_initdir/%name

%post
%post_service %name
service %name start

%preun
service %name stop

%changelog
* Mon Jul 13 2020 Pavel Isopenko <pauli@altlinux.org> 1.2-alt1
- add init info

* Mon Jul 13 2020 Pavel Isopenko <pauli@altlinux.org> 1.1-alt1
- add condstop condrestart targets

* Fri Jul 10 2020 Pavel Isopenko <pauli@altlinux.org> 1.0-alt1
- initial build for Sisyphus





