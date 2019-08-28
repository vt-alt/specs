%define rname kate

%define sover 5
%define libkateinterfaces libkateinterfaces%sover

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Group: Editors
Summary: Advanced text editor
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: %name-common = %version-%release
#Requires: %name-core = %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Aug 21 2015 (-bi)
# optimized out: cmake cmake-modules desktop-file-utils docbook-dtds docbook-style-xsl elfutils kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms pkg-config python-base python3 python3-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kactivities-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel kf5-threadweaver-devel libgit2-devel python-module-google qt5-script-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-script-devel
BuildRequires: libgit2-devel
BuildRequires: kf5-kactivities-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel
BuildRequires: kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-threadweaver-devel

%description
A fast and advanced text editor with nice plugins

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package core
Summary: Core files needed for %rname
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files needed for %rname

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n kde5-kwrite
Group: Editors
Summary: Text editor for KDE
Requires: %name-common = %version-%release
#Requires: %name-core = %version-%release
%description -n kde5-kwrite
Text editor for KDE

%package -n %libkateinterfaces
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkateinterfaces
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kateproject katexmltools
%find_lang %name --with-kde --all-name

kde5_add_text_mimes() {
desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
	--add-mime-type=text/css \
	--add-mime-type=text/csv \
	--add-mime-type=text/english \
	--add-mime-type=text/plain \
	--add-mime-type=text/x-adasrc \
	--add-mime-type=text/x-bibtex \
	--add-mime-type=text/x-c++ \
	--add-mime-type=text/x-chdr \
	--add-mime-type=text/x-c++hdr \
	--add-mime-type=text/x-csharp \
	--add-mime-type=text/x-csrc \
	--add-mime-type=text/x-c++src \
	--add-mime-type=text/x-dsrc \
	--add-mime-type=text/x-fortran \
	--add-mime-type=text/x-gle \
	--add-mime-type=text/x-java \
	--add-mime-type=text/x-javascript \
	--add-mime-type=text/x-log \
	--add-mime-type=text/x-makefile \
	--add-mime-type=text/x-objcsrc \
	--add-mime-type=text/x-pascal \
	--add-mime-type=text/x-patch \
	--add-mime-type=text/x-perl \
	--add-mime-type=text/x-php \
	--add-mime-type=text/x-python \
	--add-mime-type=text/x-sh \
	--add-mime-type=text/x-sql \
	--add-mime-type=text/x-tcl \
	--add-mime-type=text/x-tex \
	--add-mime-type=text/x-rpm-spec \
	$1
}

kde5_add_text_mimes %buildroot/%_K5xdgapp/org.kde.kate.desktop
kde5_add_text_mimes %buildroot/%_K5xdgapp/org.kde.kwrite.desktop

%files common -f %name.lang
%doc COPYING*
%_K5icon/hicolor/*/apps/kate.*
#%_K5icon/hicolor/*/actions/*.*

#%files core

%files
#%config(noreplace) %_K5xdgconf/katerc
#%config(noreplace) %_K5xdgconf/ktexteditor*
%_K5bin/kate
#%_K5lib/libkdeinit5_kate.so
%_K5plug/ktexteditor/
%_K5plug/plasma/dataengine/*_kate*.so
%_K5xdgapp/org.kde.kate.desktop
%_K5data/plasma/plasmoids/org.kde.plasma.katesessions/
%_K5data/plasma/services/org.kde.plasma.katesessions.*
%_K5srv/plasma-*katesessions.desktop
#%_K5srv/kate*.desktop
%_K5data/kateproject/
%_K5data/katexmltools/
#%_K5xmlgui/*
#%_K5doc/en/kate/

%files -n kde5-kwrite
%_K5bin/kwrite
#%_K5lib/libkdeinit5_kwrite.so
%_K5xdgapp/org.kde.kwrite.desktop
%_K5icon/hicolor/*/apps/kwrite.*
#%_K5data/kwrite/
#%_K5doc/en/kwrite/

#%files -n libkateinterfaces5
#%_K5lib/libkateinterfaces5.so.*
#%files -n libkatepartinterfaces5
#%_K5lib/libkatepartinterfaces5.so.*

#%files devel
#%_K5inc/kate/
#%_K5inc/kate_*.h
#%_K5link/lib*.so

%changelog
* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Mon May 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Tue Oct 10 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt2%ubt
- rebuild with new libgit

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Fri Mar 24 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2%ubt
- rebuild with new libgit

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Nov 24 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Tue Sep 06 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Fri Jul 01 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Wed Mar 23 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt2
- rebuild with new libgit2

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Thu Sep 24 2015 Yuri N. Sedunov <aris@altlinux.org> 15.08.1-alt1.1
- rebuilt against libgit2.so.23

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Tue Jul 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt1
- initial build
