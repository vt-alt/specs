# SPEC file for QtPass
#

%define real_name    QtPass

Name:     qtpass
Version:  1.2.3
Release:  alt1.1

Summary: a multi-platform GUI for pass, the standard unix password manager
Summary(ru_RU.UTF-8): кросс-платформенный интерфейс к менеджеру паролей pass

Group:    Text tools
License:  %gpl3plus
URL:      https://qtpass.org/
# URL: https://github.com/IJHack/qtpass

Packager: Nikolay Fetisov <naf@altlinux.org>

Source0: %real_name-%version.tar
Patch0:  %real_name-%version-%release.patch

Patch1:  %name-1.1.6-alt-desktop.patch
Patch2:  %name-1.2.0-alt-tests.patch
Patch3: alt-qt5.15.patch

Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png

BuildRequires(pre): rpm-build-licenses desktop-file-utils


# Automatically added by buildreq on Sat May 12 2018
# optimized out: gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libqt5-core libqt5-gui libqt5-network libqt5-test libqt5-widgets libqt5-xml libstdc++-devel python-base python-modules python3 python3-base python3-module-zope qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel ruby
BuildRequires: kf5-kwallet-devel python3-dev python3-module-mpl_toolkits qt5-multimedia-devel qt5-script-devel qt5-svg-devel qt5-tools-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel ruby-stdlibs

Requires: gnupg gnupg2 git-core pwgen

%description
QtPass is a multi-platform GUI for pass, the standard unix
password manager, with the following features:

* Reading pass password stores
* Displaying the password and related info
* Editing and adding of passwords and information
* Per-folder user selection for multi-user password stores
* Updating to and from a git repository
* Copying password to clipboard
* Using pass or git and gpg2 directly
* And other

%description -l ru_RU.UTF-8
QtPass -  кроссплатформенный графический интерфейс к менеджеру
паролей pass, с поддержкой:

* чтение хранилищ паролей pass,
* отображение паролей и сопутствующей информации
* редактирование и добавление паролей в хранилище
* поддержка выбора пользоваталей для многопользовательских хранилищ
* поддержка размещения хранилища паролей в репозитории git,
* копирование паролей в буфер обмена,
* работа с использованием pass или напрямую через git и gpg2
* и прочее.


%prep
%setup  -n %real_name-%version
%patch0 -p1

%patch1
#%%patch2
%patch3 -p1


mv -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/LICENSE) LICENSE

%build
%qmake_qt5  PREFIX=%buildroot%prefix
%make

%install
%makeinstall

install -D -m0644 -- qtpass.desktop %buildroot%_desktopdir/%name.desktop

install -D -m0644 -- artwork/icon.svg   %buildroot%_iconsdir/hicolor/scalable/apps/qtpass-icon.svg
install -D -m0644 -- %SOURCE1 %buildroot%_miconsdir/%name.png
install -D -m0644 -- %SOURCE2 %buildroot%_niconsdir/%name.png
install -D -m0644 -- %SOURCE3 %buildroot%_liconsdir/%name.png

install -D -m0644 -- qtpass.appdata.xml %buildroot%_datadir/appdata/%name.appdata.xml

%files
%doc README.md CHANGELOG.md FAQ.md
%doc --no-dereference LICENSE

%_bindir/%name

%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/appdata/%name.appdata.xml

%changelog
* Fri Sep 11 2020 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1.1
- Fix compile with Qt-5.15

* Mon Jun 11 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.2.3-alt1
- New version

* Sat May 12 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.2.2-alt1
- New version

* Mon Jan 08 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.2.1-alt1
- New version
  - Insecure password generation fixed

* Sat Dec 09 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.2.0-alt1
- New version

* Thu Jan 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.1.6-alt1
- Initial build for ALT Linux Sisyphus

