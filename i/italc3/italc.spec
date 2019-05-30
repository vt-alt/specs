# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

# %%docdir set
%define docdir %_defaultdocdir/%name-%version
%define confdir %_sysconfdir/italc
%define keysdir %confdir/keys
%define xinitdir %_sysconfdir/X11/xinit.d

%define program_name %(echo '%name'|sed -r 's/^(.*[^0-9]+)[0-9]+$/\\1/')
%define master_group %{program_name}master

# set %%{program_name}-* groups
%define admin_group %{program_name}-admins
%define supporter_group %{program_name}-supporters
%define teacher_group %{program_name}-teachers
%define other_group %{program_name}-others

# for filetriggers use
%if "%{?branch_switch}" == "" || "%{?branch_switch}" == "M50"
%define filetriggers yes
%define rpm_min_ver 4.0.4-alt96.11
%define menu_min_ver 2.1.41-alt4
%else
%if "%{?branch_switch}" == "M41"
%define filetriggers yes
%define rpm_min_ver 4.0.4-alt95.M41.7
%define menu_min_ver 2.1.41-alt3.M41.1
%else
%undefine filetriggers
%endif
%endif

Name: italc3
Version: 3.0.3
Release: alt2

Summary: Didactical software for teachers etc
Summary(de_DE.UTF-8): Didaktische Software fuer Lehrer usw
Summary(ru_RU.UTF-8): Управление компьютерным классом
License: %gpl2plus
Group: Networking/Remote access

Url: http://italc.sourceforge.net/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar
Source1: po-%version.tar
Source10: iTALC.conf
Source20: ica-launcher.sh
Source30: italc-client-autostart.desktop
Source33: italc-master.desktop

Patch12: italc3-additional-de-support.patch
Patch13: italc3-fix-library-path.patch

Conflicts: %program_name < 3.0.0
Conflicts: italc2 < 3.0.0

BuildRequires(pre): rpm-macros-branch rpm-build-licenses rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: GraphicsMagick-ImageMagick-compat
BuildRequires: icoutils

BuildRequires: cmake gcc-c++ java-devel libXdamage-devel libjpeg-devel libpam-devel phonon-devel libpng-devel
BuildRequires: qt5-base-devel qt5-tools-devel

%description
iTALC is a use- and powerful didactical tool for teachers. It lets you view
and control other computers in your network in several ways. It supports Linux
and Windows 2000/XP/Vista.

Features:

* see what's going on in computer-labs by using overview mode and
  make snapshots
* remote-control computers to support and help other people
* show a demo (either in fullscreen or in a window) - the teacher's screen
  is shown on all student's computers in realtime
* lock workstations for moving undivided attention to teacher
* send text-messages to students
* powering on/off and rebooting computers per remote
* remote logon and logoff and remote execution of arbitrary commands/scripts
* home-schooling - iTALC's network-technology is not restricted to a subnet
  and therefore students at home can join lessons via VPN-connections just
  by installing iTALC client

Furthermore iTALC is optimized for usage on multi-core systems (by making
heavy use of threads). No matter how many cores you have, iTALC can make use
of all of them.

%description -l de_DE.UTF-8
iTALC ist ein nuetzliches und leistungsfaehiges didaktisches Werkzeug für
Lehrer, mit dem man andere Computer im Netzwerk auf verschiedene Art und Weise
beobachten und fernsteuern kann.

iTALC unterstuetzt derzeit Linux und Windows 2000/XP/Vista.

Funktionen:

* sehen, was in Computerkabinetten los ist (Uebersichtsmodus) und
  Schnapsschuesse erstellen
* Computern fernsteuern, um anderen Leuten zu unterstuetzen
* eine Demo zeigen (entweder als Vollbild oder in einem Fenster) -
  der Lehrer-Bildschirm wird auf alle Schuelercomputer in Echtzeit uebertragen
* Schuelercomputer sperren um Aufmerksamkeit zu erlangen
* Textnachrichten an Schueler senden
* Computer uebers Netzwerk an- und ausschalten sowie neustarten
* Remote-Anmeldung sowie Ausfuehrung beliebiger Befehle/Skripte
* Anbindung zu Hause sitzender Schueler ueber VPN moeglich

Weiterhin ist iTALC optimiert auf die Nutzung auf Mehrkern-Systemen 
(indem es in grossen Umfang Threads benutzt). Egal wie viele Kerne sie haben,
iTALC kann von allen Gebrauch machen.

%description -l ru_RU.UTF-8
iTALC - мощная программа для учителей работающих в компьютеризированных
классах. Она позволяет различными способами контролировать компьютеры
учащихся входящих в состав сети. iTALC поддерживает Linux
и Windows 2000/XP/Vista а также может использоваться в смешанных сетях.

Возможности:

* просмотр и запись происходящего на компьютерах учеников
* удаленный контроль компьютеров входящих в сеть, для поддержки и помощи
  учащимся
* показ учебных материалов (в режиме полного экрана или в отдельном окне)
  на всех компьютерах сети
* блокировка рабочих станций для привлечения большего внимания к изложению
  материала
* пересылка текстовых сообщений учащимся
* включение и выключение всех компьютеров сети
* удаленный вход и выход и запуск команд и скриптов
* обучение на расстоянии. iTALC может работать не только в локальных сетях -
  с помощью соединений VPN можно организовать преподавание и в домашних
  условиях

Следует отметить что iTALC оптимизирован для работы с многоядерными системами.
Не важно сколько ядер вы имеете - iTALC может использовать все.

%package client
Summary: Software for iTALC-clients
Summary(de_DE.UTF-8): Software fuer iTALC-Clients
Summary(ru_RU.UTF-8): iTALC-клиент
Group: Networking/Remote access
Requires: %name = %version-%release
Conflicts: %program_name-client < 3.0.0


%description client
This package contains the software, needed by iTALC-clients.

See /usr/share/italc/doc/INSTALL for details on how to install and setup iTALC
in your network.

%description client -l de_DE.UTF-8
Dieses Paket beinhaltet die Software, die auf iTALC-Clients benoetigt wird.

Weitere Details ueber die Installation und Einrichtung von iTALC in Ihrem
Netzwerk finden Sie in /usr/share/italc/doc/INSTALL.

%description client -l ru_RU.UTF-8
Этот пакет содержит программное обеспечение, необходимое для организации
iTALC-клиента.

Более подробную информацию о установке и настройке iTALC в вашей сети
см. в /usr/share/italc/doc/INSTALL.

%package master
Summary: iTALC master software
Summary(de_DE.UTF-8): iTALC-Master-Software
Summary(ru_RU.UTF-8): iTALC-мастер
Group: Networking/Remote access
Requires: %name-client = %version-%release
# for filetriggers use
%ifdef rpm_min_ver
Requires: rpm >= %rpm_min_ver
%endif
%ifdef menu_min_ver
Requires: menu >= %menu_min_ver
%endif
Conflicts: %program_name-master < 3.0.0

%description master
This package contains the actual master-software for accessing clients.

See /usr/share/italc/doc/INSTALL for details on how to install and setup iTALC
in your network.

%description master -l de_DE.UTF-8
Dieses Paket beinhaltet die eigentliche Master-Software, um auf Clients
zuzugreifen.

Weitere Details ueber die Installation und Einrichtung von iTALC in Ihrem
Netzwerk finden Sie in /usr/share/italc/doc/INSTALL.

%description master -l ru_RU.UTF-8
Этот пакет содержит программное обеспечение, необходимое для организации
мастер-доступа к iTALC-клиентам.

Более подробную информацию о установке и настройке iTALC в вашей сети
см. в /usr/share/italc/doc/INSTALL.

%prep
%setup
tar xf %SOURCE1
%patch12 -p1
%patch13 -p1

%build
%cmake -DCMAKE_INSTALL_DOCDIR:PATCH='%docdir'
%cmake_build update-locales VERBOSE=1
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

# Install iTALC.conf
install -m 644 -pD %SOURCE10 "%buildroot%_sysconfdir/xdg/iTALC Solutions/iTALC.conf"
ln -snf "$(relative "%buildroot%_sysconfdir/xdg/iTALC Solutions" %buildroot%_sysconfdir/xdg/iTALC)" %buildroot%_sysconfdir/xdg/iTALC

# Create key dirs
mkdir -p %buildroot%keysdir/private/teacher
mkdir -p %buildroot%keysdir/private/admin
mkdir -p %buildroot%keysdir/private/supporter
mkdir -p %buildroot%keysdir/private/other
mkdir -p %buildroot%keysdir/public/teacher
mkdir -p %buildroot%keysdir/public/admin
mkdir -p %buildroot%keysdir/public/supporter
mkdir -p %buildroot%keysdir/public/other

# mkdir -p %buildroot%xinitdir
# ln -snf $(relative %buildroot%_bindir/ica-launcher %buildroot%xinitdir/ica-launcher) %buildroot%xinitdir/ica-launcher
# For autostart ica only
install -m 755 -pD %SOURCE20 %buildroot%_bindir/ica-launcher
install -d %buildroot%xinitdir/
ln -snf $(relative %buildroot%_bindir/ica-launcher %buildroot%xinitdir/ica-launcher) %buildroot%xinitdir/ica-launcher

find %buildroot%keysdir -mindepth 2 -maxdepth 2 -type d -print0 \
	| xargs -r0 -i touch "{}/key"

# Move ica to %_libdir/italc
mkdir -p %buildroot/%_libdir/italc
mv %buildroot%_bindir/ica %buildroot/%_libdir/italc
ln -s ../%_lib/italc/ica %buildroot%_bindir/ica

# Move JavaViewer to %%docdir
mkdir -p %buildroot%docdir
mv %buildroot%_datadir/italc/JavaViewer %buildroot%docdir/

# Install desktop file
install -Dm644 %SOURCE30 %buildroot%_sysconfdir/xdg/autostart/italc-client-autostart.desktop
install -Dm644 %SOURCE33 %buildroot%_desktopdir/italc.desktop

# Install icons
for size in 16 22 32 64 128; do
    install -Dm644 lib/resources/icon${size}.png %buildroot%_iconsdir/hicolor/${size}x${size}/apps/italc.png
done

# Install man pages
mkdir -p %buildroot%_man1dir
cp imc/imc.1 ica/ica.1 ima/italc.1 %buildroot%_man1dir

%find_lang %name

%pre client
%_sbindir/groupadd -r -f %master_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %admin_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %supporter_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %teacher_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %other_group 2>/dev/null ||:

%ifndef filetriggers
%post master
%update_menus

%postun master
%clean_menus
%endif

%files -f %name.lang
%doc %docdir

%files client
%_bindir/ica
%_libdir/italc/ica
%attr(4711,root,root) %_bindir/italc_auth_helper
%_bindir/imc
%_man1dir/imc.1.*
%_libdir/*.so
%_man1dir/ica.1.*
%_bindir/ica-launcher
%xinitdir/ica-launcher
%_sysconfdir/xdg/autostart/italc-client-autostart.desktop
%dir %confdir
%dir %keysdir
%attr(0770,root,%master_group) %dir %keysdir/private
%attr(0775,root,%master_group) %dir %keysdir/public
%attr(2770,root,%teacher_group) %dir %keysdir/private/teacher
%attr(2770,root,%admin_group) %dir %keysdir/private/admin
%attr(2770,root,%supporter_group) %dir %keysdir/private/supporter
%attr(2770,root,%other_group) %dir %keysdir/private/other
%attr(2775,root,%teacher_group) %dir %keysdir/public/teacher
%attr(2775,root,%admin_group) %dir %keysdir/public/admin
%attr(2775,root,%supporter_group) %dir %keysdir/public/supporter
%attr(2775,root,%other_group) %dir %keysdir/public/other
%ghost %attr(0660,root,%teacher_group) %config(noreplace) %keysdir/private/teacher/key
%ghost %attr(0660,root,%admin_group) %config(noreplace) %keysdir/private/admin/key
%ghost %attr(0660,root,%supporter_group) %config(noreplace) %keysdir/private/supporter/key
%ghost %attr(0660,root,%other_group) %config(noreplace) %keysdir/private/other/key
%ghost %attr(0664,root,%teacher_group) %config(noreplace) %keysdir/public/teacher/key
%ghost %attr(0664,root,%admin_group) %config(noreplace) %keysdir/public/admin/key
%ghost %attr(0664,root,%supporter_group) %config(noreplace) %keysdir/public/supporter/key
%ghost %attr(0664,root,%other_group) %config(noreplace) %keysdir/public/other/key
%dir %config(noreplace) "%_sysconfdir/xdg/iTALC Solutions"
%config(noreplace) %attr(0664,root,%master_group)  "%_sysconfdir/xdg/iTALC Solutions/iTALC.conf"
%_sysconfdir/xdg/iTALC

%files master
%_bindir/italc
%_man1dir/italc.1.*
%_desktopdir/italc.desktop
%_iconsdir/hicolor/*x*/apps/italc.png

%changelog
* Mon May 27 2019 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt2
- Complete Russian localization of desktop files.
- Fix Russian package descriptions.
- Remove deprecated desktop files.
- Fix autostart desktop file.

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt1
- Initial build in Sisyphus (based on italc2 spec file).
