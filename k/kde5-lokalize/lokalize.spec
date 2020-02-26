%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%_K5if_ver_gteq %ubt_id M90
%def_enable obsolete_kde4
%add_findreq_skiplist %_datadir/lokalize/scripts/*.py
%else
%def_disable obsolete_kde4
%add_findreq_skiplist %_K5data/lokalize/scripts/*.py
%endif


%define rname lokalize
Name: kde5-%rname
Version: 19.12.2
Release: alt1
%K5init %{?_enable_obsolete_kde4:no_altplace}

Group: Development/Tools
Summary: Computer-aided translation system
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

%if_enabled obsolete_kde4
Provides: kde4sdk-lokalize = %version-%release
Obsoletes: kde4sdk-lokalize < %version-%release
%endif
Requires: kde5-kross-python python3-module-PyQt5

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Oct 01 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel rpm-build-gir xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kross-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libhunspell-devel python-module-google qt5-script-devel rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-script-devel
BuildRequires: libhunspell-devel desktop-file-utils
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel
BuildRequires: kf5-kparts-devel kf5-kross-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel kf5-kcrash-devel

%description
Lokalize is the localization tool for KDE and other open source software.


%prep
%setup -n %rname-%version
sed -i 's|\(.*FIND_LIBRARY.*HUNSPELL_LIBRARIES.*NAMES\)|\1 hunspell|' cmake/FindHUNSPELL.cmake

%build
%K5build

%install
%K5install
%if_enabled obsolete_kde4
%else
%K5install_move data lokalize
%endif
%find_lang %name --with-kde --all-name

# fix menu file
desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
    --remove-category=Office \
    %buildroot/%_K5xdgapp/org.kde.lokalize.desktop

%files -f %name.lang
%doc COPYING*
%_K5bin/lokalize
%if_enabled obsolete_kde4
%_datadir/lokalize/
%_datadir/metainfo/*lokalize*.xml
%else
%_K5data/lokalize/
%endif
%_K5xdgapp/org.kde.lokalize.desktop
%_K5cfg/lokalize*
%_K5icon/*/*/apps/lokalize.*
%_K5xmlgui/lokalize/
%_K5notif/lokalize*
%_datadir/qlogging-categories5/*.*categories

%changelog
* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Wed Feb 05 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt2
- obsolete kde4sdk-lokalize
- package appdata

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Mon Mar 18 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Wed Feb 13 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Fri Feb 01 2019 Pavel Moseev <mars@altlinux.org> 18.12.1-alt2
- add language-team settings to Lokalize

* Thu Jan 31 2019 Pavel Moseev <mars@altlinux.org> 18.08.1-alt2
- add language-team settings to Lokalize  

* Thu Jan 10 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.1-alt1
- new version

* Wed Oct 10 2018 Sergey V Turchin <zerg@altlinux.org> 18.08.1-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Fri Jun 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Thu May 04 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1
- new version

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Mon Dec 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Tue Oct 11 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt2
- fix menu item

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

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

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- initial build
