%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

Name: mate-system-monitor
Version: 1.22.2
Release: alt1
Epoch: 1
Summary: Process and resource monitor
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common gcc-c++ libgtkmm3-devel libgtop-devel librsvg-devel libsystemd-devel libwnck3-devel libxml2-devel yelp-tools

%description
mate-system-monitor allows to graphically view and manipulate the running
processes on your system. It also provides an overview of available resources
such as CPU and memory.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile \
	--enable-systemd

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS NEWS COPYING README
%_bindir/%name
%_libexecdir/%name
%_datadir/polkit-1/actions/org.mate.mate-system-monitor.policy
%_datadir/metainfo/%name.appdata.xml
%_desktopdir/%name.desktop
%_datadir/pixmaps/%name
%_datadir/glib-2.0/schemas/org.mate.system-monitor.*.xml
%_man1dir/*.1*

%changelog
* Wed Oct 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Thu Apr 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Wed Dec 26 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
