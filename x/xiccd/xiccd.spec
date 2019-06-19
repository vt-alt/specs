Name: xiccd
Version: 0.3.0
Release: alt1

Summary: X color profile daemon
License: %gpl3plus
Group: Graphics

URL: https://github.com/agalakhov/xiccd
# https://github.com/agalakhov/xiccd.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libX11-devel libXrandr-devel glib2-devel libcolord-devel

Requires: colord

%define _unpackaged_files_terminate_build 1

%description
xiccd is a simple bridge between colord and X.
It does the following tasks:
 * Enumerates displays and register them in colord;
 * Creates default ICC profiles based on EDID data;
 * Applies ICC profiles provided by colord;
 * Maintains user's private ICC storage directory.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%config(noreplace) %_sysconfdir/xdg/autostart/*.desktop
%_bindir/%name
%_man8dir/*

%changelog
* Tue Jun 18 2019 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Mon Jun 19 2017 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Use upstream's desktop file.
- Updated to 0.2.4.

* Mon Jun 09 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt2
- rebuilt against libcolord.so.2

* Thu Nov 28 2013 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Initial build.

