%define rname	r_kiosk
%define rver	0.9.0
%define cid 	\{4D498D0A-05AD-4fdb-97B5-8A0AABC1FC5B\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name: firefox-r-kiosk
Version: 0.9.0.1
Release: alt2

Summary: Real Kiosk extension for Mozilla Firefox

License: Public Domain
Group: Networking/WWW
Url: https://addons.mozilla.org/en/firefox/addon/r-kiosk/
Source: https://addons.mozilla.org/firefox/downloads/file/132044/%rname-%rver-fx.xpi
Packager: Michael Shigorin <mike@altlinux.org>

ExcludeArch: ppc64le armh

BuildRequires(pre): rpm-build-firefox
BuildRequires: unzip
Requires: %firefox_name >= 2.0

%description
Real Kiosk is a Firefox extension that defaults to full screen,
disables all menus, toolbars, key commands and right button menus.
Alt+Home still takes you home.

You can enable Navigation toolbar by adding the following to user.js:
user_pref("rkiosk.navbar", true);

You might want to remove the print dialog by adding following lines
to your user.js:

user_pref("print.always_print_silent",true);
user_pref("print.show_print_progress",false);

Notice that the user can still close Firefox with for example Alt-F4
and get access to your computer. You might want to prevent this with
a suitable setup of your operating system's graphical environment.

Caution! R-kiosk extension can be removed only in Firefox Safe Mode.
Howto: http://kb.mozillazine.org/Safe_Mode_(Firefox)
(of course, a packaged version is removed with package manager)

%prep
%setup -c

%install
mkdir -p %buildroot/%ciddir
cp -pr * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then [ ! -d "%ciddir" ] || rm -rf "%ciddir"; fi

%files
%ciddir

%changelog
* Mon Nov 30 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.0.1-alt2
- ExcludeArch: ppc64le armh

* Mon Sep 07 2015 Michael Shigorin <mike@altlinux.org> 0.9.0.1-alt1
- built for ALT Linux (compatible with Firefox 38)

