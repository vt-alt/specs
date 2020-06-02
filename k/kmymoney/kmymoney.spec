Name:    kmymoney
Version: 5.0.8
Release: alt1

Summary: A Personal Finance Manager for KDE4
Summary(ru_RU.UTF-8): Учёт финансов под KDE4
License: GPLv2 or GPLv3
Group:   Office
URL:     http://kmymoney2.sourceforge.net

Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar
Source2: %name.watch

AutoReq: yes, noperl

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-webengine-devel
BuildRequires: kf5-kauth-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-purpose-devel
BuildRequires: kf5-solid-devel
BuildRequires: libkf5quickaddons
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kde5-kholidays-devel
BuildRequires: kde5-kcontacts-devel
BuildRequires: kde5-akonadi-devel
BuildRequires: kde5-kidentitymanagement-devel
BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-kross-devel
BuildRequires: kde5-kpimtextedit-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kdiagram-devel
BuildRequires: kf5-kdewebkit-devel

BuildRequires: boost-devel
BuildRequires: glib2-devel
BuildRequires: libassuan-devel
BuildRequires: ktoblzcheck-devel
BuildRequires: libOpenSP-devel
BuildRequires: libalkimia-devel >= 7.0.0
BuildRequires: libaqbanking-devel >= 5.0.0
BuildRequires: libgamin-devel
BuildRequires: libglibmm-devel
BuildRequires: libgmp_cxx-devel
BuildRequires: libgpgme-devel
BuildRequires: libgwenhywfar-devel >= 4.0.0
BuildRequires: libical-devel
BuildRequires: libical-glib
BuildRequires: libicu-devel
BuildRequires: libofx-devel >= 0.9.4
BuildRequires: libspeex-devel
BuildRequires: libxml++2-devel 
BuildRequires: libxml2-devel
BuildRequires: libsqlcipher-devel
BuildRequires: python-devel
BuildRequires: python-module-weboob

Requires: %name-i18n

Obsoletes: kde4-kmymoney

%description
KMyMoney strives to be the best personal finance manager.
The ultimate objectives of KMyMoney are...
* Accuracy.  Using time tested double entry accounting principles
  helps ensure that your finances are kept in correct order.
* Ease of use.  Strives to be the easiest open source personal
  finance manager to use, especially for the non-technical user.
* Familiar Features.  Intends to provide all important features
  found in the commercially-available, personal finance managers.


%package devel
Summary: Include files and libraries mandatory for KMyMoney development
Group: Development/KDE and QT
Requires: %name = %version
Obsoletes: kde4-kmymoney-devel

%description devel
Include files and libraries mandatory for development with package
kmymoney (KDE4).

%package kbanking
Summary: Online Banking plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release
Requires: aqbanking libgwenhywfar
Obsoletes: kde4-kmymoney-kbanking

%description kbanking
KBanking is the glue code needed to get the online banking features
provided by AqBanking into KMyMoney.

%package ofximport
Summary: OFX importing plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release
Requires: libofx
Obsoletes: kde4-kmymoney-ofximport

%description ofximport
OFX importing plugin for KMyMoney.

%package icalexport
Summary: ICalendar plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release
Obsoletes: kde4-kmymoney-icalexport

%description icalexport
KMyMoney iCalendar allows you to export information about scheduled
transactions to an iCalendar formatted file which can be read by most
calendar applications. This way, you can see your due payments in your
calendar application.

%package printcheck
Summary: Print cheques plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release
Obsoletes: kde4-kmymoney-printcheck

%description printcheck
This plugin gives you the ability to print transaction data onto a
preformatted paper check.

%package reconciliationreport
Summary: Reconciliation report plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release
Obsoletes: kde4-kmymoney-reconciliationreport

%description reconciliationreport
The reconciliation report plugin gives you a detailed report about the
status of a reconciliation. Once present, it will be automatically
invoked by KMyMoney after each reconciliation.

%package csv
Summary: CSV importing and exporting plugin for KMyMoney
Group:   Office
Provides: %name-csvexport = %EVR
Obsoletes: %name-csvexport < %EVR
Provides: %name-csvimport = %EVR
Obsoletes: %name-csvimport < %EVR
Requires: %name = %version-%release

%description csv
CSV importing and exporting plugin for KMyMoney.

%package qif
Summary: QIF importing and exporting plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release

%description qif 
QIF importing and exporting plugin for KMyMoney.

%package gncimport
Summary: GNC importing plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release

%description gncimport
GNC importing plugin for KMyMoney.

%package payeeidentifier
Summary: Payee identifier plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release

%description payeeidentifier
Payee identifier plugin for KMyMoney.

%package onlinetasks
Summary: National orders plugin for online banking in KMyMoney
Group:   Office
Requires: %name = %version-%release

%description onlinetasks
Plugin with national orders for online banking in KMyMoney.

%package weboob
Summary: Weboob plugin for KMyMoney
Group:   Office
Requires: %name = %version-%release

%description weboob
Plugin for import transactions from Weboob to KMyMoney.

%package plugins
Summary: All KMyMoney plugins
Group:   Office
Requires: %name = %version-%release
Requires: %name-csv
Requires: %name-qif
Requires: %name-csvimport
Requires: %name-gncimport
Requires: %name-icalexport 
Requires: %name-kbanking 
Requires: %name-ofximport 
Requires: %name-onlinetasks
Requires: %name-payeeidentifier
Requires: %name-printcheck
Requires: %name-reconciliationreport
Requires: %name-weboob
Obsoletes: kde4-kmymoney-plugins

%description plugins
All KmyMoney plugins: kbanking, ofximport, icalexport, printcheck,
reconciliationreport, csvimport, csvexport, onlinetasks, payeeidentifier
and weboob.

%package i18n
Summary: Internationalization and documentation for KMyMoney
Group: System/Internationalization 
Requires: %name = %version-%release
Obsoletes: kde4-kmymoney-i18n
BuildArch: noarch

%description i18n
Internationalization and documentation for KMyMoney

%prep
%setup -q -n %name-%version

%build
# Need to build in one thread, see https://bugs.kde.org/show_bug.cgi?id=364387 for details
#export NPROCS=1
%K5init no_altplace
%K5build -DCMAKE_SKIP_RPATH=1 \
         -DKDE_INSTALL_METAINFODIR=%_datadir/appdata \
         -DENABLE_WEBENGINE=OFF \
         -DENABLE_SQLCIPHER=OFF

%install
%K5install
%find_lang %name --all

%files
%doc AUTHORS COPYING README* TODO
%_K5bin/%name
%_K5lib/libkmm_icons.so.*
%_K5lib/libkmm_menus.so.*
%_K5lib/libkmm_models.so.*
%_K5lib/libkmm_mymoney.so.*
%_K5lib/libkmm_plugin.so.*
%_K5lib/libkmm_settings.so.*
%_K5lib/libkmm_widgets.so.*
%_K5lib/libkmm_printer.so.*
%_desktopdir/kf5/*%name.desktop
%doc %_K5doc/en/*
%_K5cfg/*.kcfg
%_K5srvtyp/*.desktop
%_K5srv/kcm_forecastview.desktop
%_K5srv/kcm_reportsview.desktop
%_K5srv/kcm_xmlstorage.desktop
%_datadir/%name/*
%exclude %_datadir/%name/templates/*
%_datadir/mime/packages/*
%_K5icon/hicolor/*/apps/%name.png
%_K5icon/hicolor/*/mimetypes/application-x-kmymoney.png
%_datadir/kconf_update/%name.upd
%_datadir/appdata/org.*.appdata.xml
%_K5xmlgui/sqlstorage/sqlstorage.rc
%_qt5_plugindir/kmymoney/budgetview.so
%_qt5_plugindir/kmymoney/forecastview.so
%_qt5_plugindir/kmymoney/kcm_forecastview.so
%_qt5_plugindir/kmymoney/kcm_reportsview.so
%_qt5_plugindir/kmymoney/kcm_xmlstorage.so
%_qt5_plugindir/kmymoney/onlinejoboutboxview.so
%_qt5_plugindir/kmymoney/reportsview.so
%_qt5_plugindir/kmymoney/sqlstorage.so
%_qt5_plugindir/kmymoney/xmlstorage.so

%files devel
%dir %_includedir/%name
%_includedir/%name/*
%_K5link/lib*.so

%files kbanking
%_qt5_plugindir/kmymoney/kbanking.so
%_K5xmlgui/kbanking
%_datadir/kbanking

%files ofximport
%_qt5_plugindir/kmymoney/ofximporter.so
%_K5xmlgui/ofximporter

%files icalexport
%_qt5_plugindir/kmymoney/icalendarexporter.so
%_qt5_plugindir/kmymoney/kcm_icalendarexporter.so
%_K5xmlgui/icalendarexporter
%_K5srv/kcm_icalendarexporter.desktop

%files printcheck
%_qt5_plugindir/kmymoney/checkprinting.so
%_qt5_plugindir/kmymoney/kcm_checkprinting.so
%_K5xmlgui/checkprinting
%_datadir/checkprinting
%_K5srv/kcm_checkprinting.desktop

%files reconciliationreport
%_qt5_plugindir/kmymoney/reconciliationreport.so

%files csv
%_libdir/libkmm_csvimportercore.so*
%_qt5_plugindir/kmymoney/csvimporter.so
%_qt5_plugindir/kmymoney/kcm_csvimporter.so
%_qt5_plugindir/kmymoney/csvexporter.so
%_K5xmlgui/csvimporter
%_K5xmlgui/csvexporter
%_K5srv/kcm_csvimporter.desktop

%files qif
%_qt5_plugindir/kmymoney/qifimporter.so
%_qt5_plugindir/kmymoney/qifexporter.so
%_qt5_plugindir/kmymoney/kcm_qif.so
%_K5xmlgui/qifimporter
%_K5xmlgui/qifexporter
%_K5srv/kcm_qifimporter.desktop
%_K5srv/kcm_qifexporter.desktop

%files gncimport
%_qt5_plugindir/kmymoney/gncimporter.so

%files payeeidentifier
%_libdir/libkmm_payeeidentifier.so.*

%files onlinetasks
%_qt5_plugindir/kmymoney/konlinetasks_sepa.so

%files weboob
%_qt5_plugindir/kmymoney/weboob.so
%_K5xmlgui/weboob

%files plugins

%files i18n -f %name.lang
%_datadir/%name/templates/*
%_K5doc/*/kmymoney/
%exclude %_K5doc/en

%changelog
* Mon Feb 03 2020 Andrey Cherepanov <cas@altlinux.org> 5.0.8-alt1
- New version.

* Thu Oct 10 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.7-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.6-alt1
- New version.

* Fri Jul 12 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.5-alt1
- New version.

* Tue Apr 23 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.4-alt1
- New version.

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.3-alt1
- New version.

* Tue Nov 06 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1
- New version.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt2.qa1
- NMU: applied repocop patch

* Sat Sep 29 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt2
- Fix build with Qt 5.11.
- Package appdata file.

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version.
- Do not build API documentation.

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt2
- Rebuild with libgwenhywfar-4.20.0.

* Thu Feb 15 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version for KDE 5.

* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.1.1-alt1
- New version.

* Sun Oct 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.8.1-alt1
- New version

* Mon Apr 10 2017 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt2
- Use documentation and localization from released tarball

* Wed Jun 29 2016 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt1
- new version 4.8.0
- New plugins: payeeidentifier, onlinetasks, weboob
- i18n package is required for main package

* Mon May 02 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.2-alt4
- Rebuild with new aqbanking
- Build without Nepomuk support

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.2-alt3
- Rebuild with new libalkimia

* Mon Jan 25 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.2-alt2
- Fix build

* Tue Apr 28 2015 Andrey Cherepanov <cas@altlinux.org> 4.7.2-alt1
- New version

* Sat Apr 04 2015 Andrey Cherepanov <cas@altlinux.org> 4.7.1-alt1
- New version

* Fri Apr 03 2015 Andrey Cherepanov <cas@altlinux.org> 4.6.4-alt4
- Rebuild with new version of libgwenhywfar

* Wed Aug 27 2014 Andrey Cherepanov <cas@altlinux.org> 4.6.4-alt3
- Fix source tarball name in watch file

* Sun Nov 24 2013 Andrey Cherepanov <cas@altlinux.org> 4.6.4-alt2
- Rebuild with libofx-0.9.9

* Thu Nov 21 2013 Andrey Cherepanov <cas@altlinux.org> 4.6.4-alt1
- New version

* Wed Apr 10 2013 Andrey Cherepanov <cas@altlinux.org> 4.6.3-alt3
- Fix build with GMP 5.1.0
- Support Nepomuk
- Generate HTML documentation

* Wed Mar 06 2013 Andrey Cherepanov <cas@altlinux.org> 4.6.3-alt2
- Fix build in Sisyphus

* Fri Nov 30 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.3-alt1
- New version 4.6.3

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.2-alt5.2
- Rebuilt

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.2-alt5.1
- Rebuilt with gmp 5.0.5

* Tue Jun 05 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt5
- Fix obsoletes to prevent "trigger effect"

* Tue Jun 05 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt4
- Replace kde4-kmymoney package

* Wed May 30 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt3
- Add missing translations to kmymoney-i18n
- Pack CVS import plugin

* Fri Feb 10 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt2
- Remove pt_BR documentation

* Thu Feb 09 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt1
- New version 4.6.2

* Mon Jan 16 2012 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt1
- New version 4.6.1
- Remove standard library path from RPATH
- Add watch file

* Tue Sep 13 2011 Andrey Cherepanov <cas@altlinux.org> 4.6.0-alt3
- Remove unnecessary dependencies

* Fri Sep 09 2011 Andrey Cherepanov <cas@altlinux.org> 4.6.0-alt2
- Fix obsoletes to prevent downgrade

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 4.6.0-alt1
- New version 4.6.0
- Rename to kmymoney
- Set standard placement

* Wed Mar 02 2011 Andrey Cherepanov <cas@altlinux.org> 4.5.3-alt1
- New version 4.5.3

* Tue Feb 01 2011 Andrey Cherepanov <cas@altlinux.org> 4.5.2-alt1
- New version 4.5.2

* Mon Nov 22 2010 Andrey Cherepanov <cas@altlinux.org> 4.5.1-alt1
- new version 4.5.1

* Thu Oct 07 2010 Andrey Cherepanov <cas@altlinux.org> 4.5.0-alt1
- stable version 4.5.0
- rename package to kde4-kmymoney

* Mon May 17 2010 Andrey Cherepanov <cas@altlinux.org> 3.97.2-alt1
- Version 3.97.2 (beta)

* Thu Apr 15 2010 Andrey Cherepanov <cas@altlinux.org> 3.97.0-alt1
- Version 3.97.0 (beta)
