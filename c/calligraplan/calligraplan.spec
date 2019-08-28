# obsileted koffice version
%define koffice_ver 4:2.3.70
%define oname calligra-plan

%define sover 16
%define libkplatokernel libkplatokernel%sover
%define libkplatomodels libkplatomodels%sover
%define libkplatoui libkplatoui%sover
%define libplankundo2 libplankundo2%sover
%define libplanmain libplanmain%sover
%define libplanodf libplanodf%sover
%define libplanplugin libplanplugin%sover
%define libplanprivate libplanprivate%sover
%define libplanstore libplanstore%sover
%define libplanwidgets libplanwidgets%sover
%define libplanwidgetutils libplanwidgetutils%sover
%define libplanworkfactory libplanworkfactory%sover

Name: calligraplan
Version: 3.1.0
Release: alt7
Epoch: 0
%K5init

Group: Office
Summary: A project planner
License: GPLv2+ / LGPLv2+
Url: https://www.calligra.org/plan/
Provides: koffice-kplato = %koffice_ver
Obsoletes: koffice-kplato < %koffice_ver
Requires: %oname-common = %EVR
Requires: kf5-kreport

Source: http://download.kde.org/stable/calligra/%version/calligraplan-%version.tar
# Upstream patches
Patch1: 0001-Fix-build-with-Qt-5.11-missing-headers.patch
Patch2: 0002-Fix-compile-on-CI.patch
Patch3: 0003-Port-to-KCalCore-API-changes.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: kf5-karchive-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kcmutils-devel
BuildRequires: kf5-kio-devel kf5-knotifications-devel kf5-kparts-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-kactivities-devel kf5-khtml-devel kde5-kholidays-devel kf5-kdiagram-devel
BuildRequires: kf5-kjs-devel kf5-kitemmodels-devel
BuildRequires: kde5-kcalcore-devel kde5-kcontacts-devel kde5-akonadi-devel kde5-akonadi-contacts-devel
BuildRequires: qt5-base-devel qt5-svg-devel qt5-x11extras-devel
BuildRequires: zlib-devel

%description
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package -n %oname
Group: Office
Summary: A project planner
License: GPLv2+ / LGPLv2+
Provides: koffice-kplato = %koffice_ver
Obsoletes: koffice-kplato < %koffice_ver
Requires: %oname-common = %EVR
Requires: kf5-kreport
%description -n %oname
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package -n %oname-common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description -n %oname-common
%name common package

%package -n %oname-devel
Group: Development/KDE and QT
Summary: Header files and libraries needed for %name development
Conflicts: libflake-devel
%description -n %oname-devel
Header files and libraries needed for %name development

%package -n %libkplatokernel
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libkplatokernel
%name library

%package -n %libkplatomodels
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libkplatomodels
%name library

%package -n %libkplatoui
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libkplatoui
%name library

%package -n %libplankundo2
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libplankundo2
%name library

%package -n %libplanmain
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libplanmain
%name library

%package -n %libplanodf
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libplanodf
%name library

%package -n %libplanplugin
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libplanplugin
%name library

%package -n %libplanprivate
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libplanprivate
%name library

%package -n %libplanstore
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libplanstore
%name library

%package -n %libplanwidgets
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libplanwidgets
%name library

%package -n %libplanwidgetutils
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libplanwidgetutils
%name library

%package -n %libplanworkfactory
Summary: %name library
Group: System/Libraries
Requires: %oname-common = %EVR
%description -n %libplanworkfactory
%name library

%prep
%setup
%patch1 -p2
%patch2 -p1
%patch3 -p1

%build
%K5build \
    -DPACKAGERS_BUILD=OFF \
    -DBUILD_TESTING=OFF \
    -DTEMPLATES_INSTALL_DIR:PATH=%_K5tmpl \
    #

%install
%K5install

## unpackaged files
rm -frv %buildroot/%_datadir/locale/x-test/

%find_lang --with-kde --all-name %name

%files -n %oname-common -f %name.lang
%_K5icon/*/*/*/*

%files -n %oname-devel
%_K5link/lib*.so

%files -n %oname
%dir %_K5plug/calligraplan/
%dir %_K5plug/calligraplan/parts/
%dir %_K5plug/calligraplan/formatfilters/
%dir %_K5plug/calligraplan/schedulers/
%config(noreplace) %_K5xdgconf/calligraplan*rc
%_K5bin/calligraplan
%_K5bin/calligraplanwork
%_K5lib/libkdeinit5_calligraplan.so
%_K5lib/libkdeinit5_calligraplanwork.so
%_K5plug/calligraplan/parts/calligraplanpart.so
%_K5plug/calligraplan/formatfilters/planicalexport.so
%_K5plug/calligraplan/formatfilters/plankplatoimport.so
%_K5plug/calligraplan/schedulers/libplantjscheduler.so
%_K5plug/calligraplanworkpart.so
%_datadir/calligraplan/
%_datadir/calligraplanwork/
%_K5xmlgui/calligraplan/
%_K5xmlgui/calligraplanwork/
%_K5cfg/calligraplansettings.kcfg
%_K5cfg/calligraplanworksettings.kcfg
%_K5xdgapp/org.kde.calligraplan.desktop
%_K5xdgapp/org.kde.calligraplanwork.desktop
%_datadir/metainfo/org.kde.calligraplan.appdata.xml

%files -n %libkplatokernel
%_K5lib/libkplatokernel.so.%sover
%_K5lib/libkplatokernel.so.*

%files -n %libkplatomodels
%_K5lib/libkplatomodels.so.%sover
%_K5lib/libkplatomodels.so.*

%files -n %libkplatoui
%_K5lib/libkplatoui.so.%sover
%_K5lib/libkplatoui.so.*

%files -n %libplankundo2
%_K5lib/libplankundo2.so.%sover
%_K5lib/libplankundo2.so.*

%files -n %libplanmain
%_K5lib/libplanmain.so.%sover
%_K5lib/libplanmain.so.*

%files -n %libplanodf
%_K5lib/libplanodf.so.%sover
%_K5lib/libplanodf.so.*

%files -n %libplanplugin
%_K5lib/libplanplugin.so.%sover
%_K5lib/libplanplugin.so.*

%files -n %libplanprivate
%_K5lib/libplanprivate.so.%sover
%_K5lib/libplanprivate.so.*

%files -n %libplanstore
%_K5lib/libplanstore.so.%sover
%_K5lib/libplanstore.so.*

%files -n %libplanwidgets
%_K5lib/libplanwidgets.so.%sover
%_K5lib/libplanwidgets.so.*

%files -n %libplanwidgetutils
%_K5lib/libplanwidgetutils.so.%sover
%_K5lib/libplanwidgetutils.so.*

%files -n %libplanworkfactory
%_K5lib/libplanworkfactory.so.%sover
%_K5lib/libplanworkfactory.so.*

%changelog
* Fri Aug 23 2019 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt7
- fix build with new kcalcore

* Thu Aug 15 2019 Oleg Solovyov <mcpain@altlinux.org> 0:3.1.0-alt6
- Fixed build

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt5.qa1
- NMU: remove rpm-build-ubt from BR:

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt4.qa1
- NMU: applied repocop patch

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0:3.1.0-alt4
- Fixed build with new Qt.

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt3
- NMU: added url

* Tue Mar 20 2018 Oleg Solovyov <mcpain@altlinux.org> 0:3.1.0-alt2%ubt
- split libs
- rename packages

* Tue Mar 13 2018 Oleg Solovyov <mcpain@altlinux.org> 0:3.1.0-alt1%ubt
- initial build for ALT
