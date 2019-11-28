# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: chrome-gnome-shell
Version: 10.1
Release: alt1
Summary: Support for managing GNOME Shell Extensions through web browsers

License: GPLv3+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome

Source: %name-%version.tar
#Source-url: https://download.gnome.org/sources/%name/%version/%name-%version.tar.xz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: python3-devel
#BuildRequires: %_bindir/base64
#BuildRequires: %_bindir/head
BuildRequires: %_bindir/jq
#BuildRequires: %_bindir/sha256sum
#BuildRequires: %_bindir/tr

%description
Browser extension for Google Chrome/Chromium, Firefox, Vivaldi, Opera (and
other Browser Extension, Chrome Extension or WebExtensions capable browsers)
and native host messaging connector that provides integration with GNOME Shell
and the corresponding extensions repository https://extensions.gnome.org.

%prep
%setup

%build
%cmake   -DBUILD_EXTENSION=OFF \
         -DCMAKE_INSTALL_LIBDIR=%_lib \
         -DPython_ADDITIONAL_VERSIONS=3
%cmake_build

%install
%cmakeinstall_std

# fix FHS
mkdir -p %buildroot%python3_sitelibdir
[ %_lib = lib64 ] &&
  mv %buildroot%python3_sitelibdir_noarch/chrome_gnome_shell-*.egg-info \
  %buildroot%python3_sitelibdir/

%check
desktop-file-validate %buildroot%_desktopdir/org.gnome.ChromeGnomeShell.desktop

%files
%doc LICENSE
%_sysconfdir/chromium/
%_sysconfdir/opt/chrome/
%_bindir/chrome-gnome-shell
%_libdir/mozilla/native-messaging-hosts/
%python3_sitelibdir/chrome_gnome_shell-*.egg-info
%_desktopdir/org.gnome.ChromeGnomeShell.desktop
%_datadir/dbus-1/services/org.gnome.ChromeGnomeShell.service
%_iconsdir/gnome/*/apps/org.gnome.ChromeGnomeShell.png

%changelog
* Tue Oct 29 2019 Anton Midyukov <antohami@altlinux.org> 10.1-alt1
- initial build for ALT Sisyphus
