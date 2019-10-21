%define _libexecdir %_prefix/libexec

Name: mate-utils
Version: 1.22.2
Release: alt1
Epoch: 1
Summary: MATE utility programs
License: GPLv3+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: mate-dictionary = %epoch:%version-%release
Requires: mate-screenshot = %epoch:%version-%release
Requires: mate-search-tool = %epoch:%version-%release
Requires: mate-system-log = %epoch:%version-%release
Requires: mate-disk-usage-analyzer = %epoch:%version-%release
Obsoletes: mate-utils-libs

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common gcc-c++ gtk-doc inkscape libSM-devel libcanberra-gtk3-devel libgtop-devel mate-panel-devel librsvg-utils yelp-tools

%description
The mate-utils package contains a set of small "desk accessory" utility
applications for MATE, such as a dictionary, a disk usage analyzer,
a screen-shot tool and others.

%package common
Group: Graphical desktop/MATE
Summary: Common files for %name
BuildArch: noarch

%description common
%summary

%package devel
Group: Development/C
Summary: Development files for mate-utils
Obsoletes: mate-dictionary-devel
Requires:  mate-dictionary = %epoch:%version-%release

%description devel
The mate-utils-devel package contains header files and other resources
needed to develop programs using the libraries contained in mate-utils

%package -n mate-system-log
Group: Graphical desktop/MATE
Summary: A log file viewer for the MATE desktop
Requires: %name-common = %epoch:%version-%release

%description -n mate-system-log
An application that lets you view various system log files

%package -n mate-screenshot
Group: Graphical desktop/MATE
Summary: A utility to take a screen-shot of the desktop
Requires: %name-common = %epoch:%version-%release

%description -n mate-screenshot
An application that let you take a screen-shot of your desktop

%package -n mate-dictionary
Group: Graphical desktop/MATE
Summary: A dictionary for MATE Desktop
Requires: %name-common = %epoch:%version-%release

%description -n mate-dictionary
The mate-dictionary package contains a dictionary application for MATE Desktop

%package -n mate-search-tool
Group: Graphical desktop/MATE
Summary: A file searching tool for MATE Desktop
Requires: %name-common = %epoch:%version-%release

%description -n mate-search-tool
An application to search for files on your computer

%package -n mate-disk-usage-analyzer
Group: Graphical desktop/MATE
Summary: A disk usage analyzing tool for MATE Desktop
Requires: %name-common = %epoch:%version-%release

%description -n mate-disk-usage-analyzer
An application to help analyze disk usage

%prep
%setup -q
%patch -p1

rm -fr gsearchtool/help/pt

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile \
	--enable-gdict-applet \
	--enable-gtk-doc \
	--enable-gtk-doc-html \
	--enable-ipv6

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome
%find_lang mate-disk-usage-analyzer --with-gnome
%find_lang mate-dictionary --with-gnome
%find_lang mate-search-tool --with-gnome
%find_lang mate-system-log --with-gnome

%files

%files common -f %name.lang
%doc COPYING COPYING.libs NEWS README

%files devel
%_includedir/mate-dict
%_libdir/libmatedict.so
%_pkgconfigdir/mate-dict.pc
%_datadir/gtk-doc/html/mate-dict

%files -n mate-system-log -f mate-system-log.lang
%_bindir/mate-system-log
%_datadir/%name
%_datadir/glib-2.0/schemas/org.mate.system-log.gschema.xml
%_desktopdir/mate-system-log.desktop
%_iconsdir/hicolor/*/apps/mate-system-log*
%_man1dir/mate-system-log.1*

%files -n mate-screenshot
%_bindir/mate-screenshot
%_bindir/mate-panel-screenshot
%_datadir/metainfo/mate-screenshot.appdata.xml
%_desktopdir/mate-screenshot.desktop
%_datadir/mate-screenshot
%_datadir/glib-2.0/schemas/org.mate.screenshot.gschema.xml
%_man1dir/mate-screenshot.1*
%_man1dir/mate-panel-screenshot.1*

%files -n mate-dictionary -f mate-dictionary.lang
%doc mate-dictionary/AUTHORS mate-dictionary/README
%_bindir/mate-dictionary
%_datadir/metainfo/mate-dictionary.appdata.xml
%_desktopdir/mate-dictionary.desktop
%_datadir/mate-dict
%_datadir/mate-dictionary
%_libexecdir/mate-dictionary-applet
%_libdir/libmatedict.so.*
%_datadir/glib-2.0/schemas/org.mate.dictionary.gschema.xml
%_datadir/mate-panel/applets/org.mate.DictionaryApplet.mate-panel-applet
%_datadir/dbus-1/services/org.mate.panel.applet.DictionaryAppletFactory.service
%_man1dir/mate-dictionary.1*

%files -n mate-search-tool -f mate-search-tool.lang
%_bindir/mate-search-tool
%_datadir/metainfo/mate-search-tool.appdata.xml
%_desktopdir/mate-search-tool.desktop
%_datadir/glib-2.0/schemas/org.mate.search-tool.gschema.xml
%_datadir/pixmaps/mate-search-tool
%_man1dir/mate-search-tool.1*

%files -n mate-disk-usage-analyzer -f mate-disk-usage-analyzer.lang
%doc baobab/AUTHORS baobab/README
%_bindir/mate-disk-usage-analyzer
%_datadir/metainfo/mate-disk-usage-analyzer.appdata.xml
%_desktopdir/mate-disk-usage-analyzer.desktop
%_datadir/mate-disk-usage-analyzer
%_datadir/glib-2.0/schemas/org.mate.disk-usage-analyzer.gschema.xml
%_iconsdir/hicolor/*/apps/mate-disk-usage-analyzer.*
%_man1dir/mate-disk-usage-analyzer.1*

%changelog
* Wed Oct 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Thu Mar 07 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Feb 12 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20.0-alt1.qa1
- NMU: applied repocop patch

* Wed Mar 21 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
