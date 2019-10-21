%define rname mozo

Name: mate-menu-editor
Version: 1.22.2
Release: alt1
Epoch: 1
Summary: MATE Desktop menu editor
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %rname-%version.tar
Patch: %rname-%version-%release.patch

BuildArch: noarch
BuildRequires: mate-common glib2-devel gtk-update-icon-cache python3-devel
BuildRequires: pkgconfig(libmate-menu) pkgconfig(pygobject-3.0)

%description
MATE Desktop menu editor

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %rname --with-gnome --all-name

%files -f %rname.lang
%doc AUTHORS COPYING README
%_bindir/%rname
%_iconsdir/hicolor/*/apps/%rname.png
%_datadir/%rname
%_desktopdir/%rname.desktop
%python3_sitelibdir_noarch/Mozo
%_man1dir/%rname.1.*

%changelog
* Thu Oct 17 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Wed Apr 24 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Feb 12 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Wed Mar 21 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
