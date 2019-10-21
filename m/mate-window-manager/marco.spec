%define rname marco

Name: mate-window-manager
Version: 1.22.3
Release: alt1
Epoch: 1
Summary: MATE Desktop window manager
License: LGPLv2+ and GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %rname-%version.tar
Patch: %rname-%version-%release.patch

BuildRequires: mate-common libSM-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXinerama-devel libXpresent-devel
BuildRequires: libXrandr-devel libcanberra-gtk3-devel libgtop-devel libstartup-notification-devel zenity yelp-tools

%description
MATE Desktop window manager

%package -n libmarco-private
Group: System/Libraries
Summary: Libraries for marco
License: LGPLv2+

%description -n libmarco-private
This package provides Libraries for marco.

%package devel
Group: Development/C
Summary: Development files for marco

%description devel
Development files for marco

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %rname --with-gnome --all-name

%files
%doc AUTHORS COPYING README ChangeLog
%_bindir/%rname
%_bindir/%rname-message
%_bindir/%rname-theme-viewer
%dir %_datadir/%rname/icons
%_datadir/themes/*
%_datadir/mate-control-center/keybindings/50-marco*.xml
%_datadir/mate/wm-properties
%_desktopdir/%rname.desktop
%_man1dir/%rname.1*
%_man1dir/%rname-message.1*
%_man1dir/%rname-theme-viewer.1*

%files -n libmarco-private -f %rname.lang
%_libdir/libmarco-private.so.*
%_datadir/glib-2.0/schemas/org.mate.marco.gschema.xml

%files devel
%_includedir/marco-1
%_bindir/marco-window-demo
%_libdir/libmarco-private.so
%_pkgconfigdir/*.pc
%_datadir/%rname/icons/marco-window-demo.png
%_man1dir/marco-window-demo.1*

%changelog
* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.3-alt1
- 1.22.3

* Wed Jul 10 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Thu Apr 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Feb 12 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Mon Mar 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Wed Feb 21 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
