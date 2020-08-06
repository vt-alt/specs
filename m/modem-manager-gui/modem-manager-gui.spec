Name:          modem-manager-gui
Summary:       Graphical interface for ModemManager
Summary(de):   Grafische Oberfläche für ModemManager
Summary(ru):   Графический интерфейс для ModemManager
Version:       0.0.20
Release:       alt1

Group:	       System/Configuration/Networking	
License:       GPLv3
URL:           http://linuxonly.ru/cms/page.php?7

Packager:      Andrey Cherepanov <cas@altlinux.org>

# The original download link is a PHP script which points to this file:
Source0:       http://download.tuxfamily.org/gsf/source/%{name}-%{version}.tar.gz
Source1:       %name.watch

BuildRequires: meson
BuildRequires: pkgconfig
BuildRequires: desktop-file-utils
BuildRequires: gdbm-devel
BuildRequires: glib2-devel
BuildRequires: libappindicator-gtk3-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgtkspell3-devel
BuildRequires: libnotify-devel
BuildRequires: gettext-tools
BuildRequires: po4a
BuildRequires: itstool
# TODO: need to package ofono
#BuildRequires: ofono-devel

Requires: ModemManager
Requires: NetworkManager

%description
This program is a simple graphical interface for Modem Manager
daemon dbus interface.
Current features:
- View device information: Operator name, Mode, IMEI, IMSI,
  Signal level.
- Send and receive SMS messages with long massages
  concatenation and store messages in database.
- Send USSD requests and read answers in GSM7 and UCS2 formats
  converted to system UTF8 charset.
- Scan available mobile networks.

%description -l de
Dieses Programm ist eine einfache grafische Oberfläche für
die DBus-Schnittstelle des ModemManager-Daemons.
Funktionen:
- Geräteinformationen anzeigen: Name des Netzanbieters, Modus,
  IMEI, IMSI, Signalstärke.
- SMS senden und empfangen, Verkettung langer Nachrichten,
  Speichern der Nachrichten in der Datenbank.
- USSD-Befehle in den Formaten GSM7 und UCS2 senden und
  Antworten empfangen, Umwandlung in den UTF-8-Zeichensatz.
- Nach verfügbaren Mobilnetzwerken suchen.

%description -l ru
Данная программа является простым графическим интерфейсом для
демона Modem Manager, использующим интерфейс dbus.
Текущие возможности:
- Просмотр информации об устройстве: имени оператора, режима работы,
  IMEI, IMSI и уровня сигнала.
- Прием и отправка сообщений SMS с объединением длинных сообщений
  и сохранением сообщений в базе данных.
- Отправка запросов USSD и прием ответов в кодировках GSM7 и UCS2
  с последующей конвертацией в системную кодировку UTF8.
- Сканирование доступных мобильных сетей.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

# Move appdata to its directory
mkdir -p %buildroot%_datadir/appdata
mv %buildroot%_datadir/metainfo/%name.appdata.xml %buildroot%_datadir/appdata

%find_lang --with-man --with-gnome %name

%files -f %name.lang
%doc LICENSE AUTHORS Changelog
%_bindir/%name
%_libdir/%name/
%_sysconfdir/NetworkManager/dispatcher.d/95-mmgui-timestamp-notifier
%_datadir/polkit-1/actions/ru.linuxonly.%name.policy
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%{name}*
%doc %_datadir/help/uz@Latn
%_datadir/locale/uz@*/LC_MESSAGES/%name.mo
%doc %_mandir/uz@*/man1/%name.1*
%doc %_man1dir/%name.1.*
%_datadir/appdata/%name.appdata.xml

%changelog
* Mon Aug 03 2020 Andrey Cherepanov <cas@altlinux.org> 0.0.20-alt1
- New version.

* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 0.0.19.1-alt2
- Fix help pages format errors by upstream commit 68fb09c (ALT #36473).

* Mon Apr 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.19.1-alt1
- New version.

* Mon Mar 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.19-alt1
- New version.

* Tue Oct 13 2015 Andrey Cherepanov <cas@altlinux.org> 0.0.18-alt1
- New version

* Tue Sep 09 2014 Andrey Cherepanov <cas@altlinux.org> 0.0.17.1-alt1
- New version
- Drop obsoleted patches and localization
- Fix charset of Russian man page
- Add watch file

* Thu Jul 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.0.16-alt1
- Build for Sisyphus (thanks Fedora for spec) (ALT #29225)

