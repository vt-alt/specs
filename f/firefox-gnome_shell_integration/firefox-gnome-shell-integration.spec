# SPEC file for FlashBlock extension

%define rname	gnome_shell_integration
%define cid 	chrome-gnome-shell@gnome.org
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name: %firefox_name-%rname
Version: 10.1
Release: alt1

Summary: GNOME Shell integration extension for Firefox
Summary(ru_RU.UTF-8): расширение GNOME Shell integration для Firefox

License: %gpl3plus
Group: Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/gnome-shell-integration/
BuildArch: noarch

Source0: %rname-%version.xpi

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires: unzip

Requires: chrome-gnome-shell = %version

%description
GNOME Shell integration - extension provides integration with
GNOME Shell and the corresponding extensions repository
https://extensions.gnome.org

%description -l ru_RU.UTF-8
GNOME Shell integration - расширение для браузеров семейства
Mozilla-Firefox, предназначенное для интеграции с GNOME Shell
и установки расширений для него из репозитория
https://extensions.gnome.org

%prep
%setup -c

%install
mkdir -p -- %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Tue Oct 29 2019 Anton Midyukov <antohami@altlinux.org> 10.1-alt1
- Initial build
