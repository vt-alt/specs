Name: mate-icon-theme
Version: 1.22.2
Release: alt1
Epoch: 1
Summary: Icon theme for MATE Desktop
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: mate-common icon-naming-utils

%description
Icon theme for MATE Desktop

%prep
%setup -q
%patch -p1

rm -f mate/scalable/animations/*.svg

%build
%autoreconf
%configure \
	--enable-icon-mapping

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING README
%_iconsdir/mate
%_iconsdir/menta

%changelog
* Wed Oct 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Mon Apr 22 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Tue Nov 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Tue Mar 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
