
%add_findreq_skiplist %_K5xdgapp/*/scripts/*/*.py
%add_findreq_skiplist %_K5xdgapp/*/scripts/*/*.rb

# obsileted koffice version
%define koffice_ver 4:2.3.70
%def_disable plan

Name: calligra
Version: 3.1.0
Release: alt9
Epoch: 0
%K5init no_altplace
%define libname lib%name

Group: Office
Summary: An integrated office suite
Url: http://www.calligra-suite.org/
License: GPLv2+ / LGPLv2+

Provides: koffice = %koffice_ver
Obsoletes: koffice < %koffice_ver

#Requires: %name-gemini
Requires: %name-words
Requires: %name-sheets
Requires: %name-stage
Requires: %name-karbon
%if_enabled plan
Requires: %name-plan
%endif
Requires: %name-okular-generators

Source: http://download.kde.org/stable/calligra/%version/calligra-%version.tar
# Upstream patches
Patch1: 0001-Fix-build-with-Qt-5.11-missing-headers.patch
Patch2: 0001-Missing-include-for-QFrame.patch
Patch3: 0001-Fix-compilation-with-Qt-5.13.patch
#
Patch10: 0010-poppler071.patch
Patch11: 0011-poppler071.patch
Patch12: 0012-poppler071.patch
Patch13: 0013-poppler071.patch
Patch14: 0014-poppler071.patch
Patch15: 0015-poppler071.patch
Patch16: 0016-poppler074.patch
Patch17: 0017-poppler074.patch
# ALT
Patch103: alt-disable-products.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: kf5-attica-devel boost-devel eigen3 gcc-c++ glib2-devel rpm-build-python rpm-build-ruby
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel qt5-svg-devel qt5-declarative-devel qt5-script-devel qt5-x11extras-devel
#BuildRequires: qt5-quick1-devel
#BuildRequires: qt5-webkit-devel
BuildRequires: kf5-attica-devel kde5-kholidays-devel
BuildRequires: kf5-kactivities-devel kf5-karchive-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdoctools-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-kjs-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kcmutils-devel kf5-kdelibs4support-devel
BuildRequires: kf5-kio-devel kf5-kross-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-sonnet-devel
BuildRequires: kf5-ktextwidgets-devel kf5-threadweaver-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
#BuildRequires: kde5-marble-devel
BuildRequires: kde5-kcalcore-devel kde5-kcontacts-devel kde5-akonadi-devel kde5-akonadi-contacts-devel
BuildRequires: kde5-okular-devel
BuildRequires: kf5-kdiagram-devel kf5-kreport-devel kf5-kproperty-devel
BuildRequires: qt5-phonon-devel libqca-qt5-devel libpoppler-qt5-devel
BuildRequires: libexiv2-devel libfftw3-devel libfreetds-devel libGLEW-devel libgsl-devel libicu-devel libjpeg-devel libopenjpeg2.0-devel libtiff-devel pstoedit
BuildRequires: liblcms2-devel libmysqlclient-devel
BuildRequires: libsqlite3-devel sqlite3 libxbase-devel openexr-devel postgresql-devel
BuildRequires: libvisio-devel libwpg-devel libwpd10-devel libwps-devel libodfgen-devel libetonyek-devel libxml2-devel
BuildRequires: libdrm-devel libpng-devel libexpat-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package core
Group: System/Libraries
Summary: Core support files for %name
Provides: koffice-core = %koffice_ver
Obsoletes: koffice-core < %koffice_ver
Provides:  koffice-kchart = %koffice_ver
Obsoletes: koffice-kchart < %koffice_ver
Provides:  koffice-kformula = %koffice_ver
Obsoletes: koffice-kformula < %koffice_ver
Requires: fonts-ttf-latex-xft
%description core
%summary.

%package devel
Group: Development/KDE and QT
Summary: Header files and libraries needed for %name development
Conflicts: libflake-devel
%description devel
Header files and libraries needed for %name development

%package words
Group: Office
Summary: An intuitive word processor application with desktop publishing features
Provides: kword = %version-%release
Provides: koffice-kword = %koffice_ver
Obsoletes: koffice-kword < %koffice_ver
Requires: %name-core
%description words
KWord is an intuitive word processor and desktop publisher application.
With it, you can create informative and attractive documents with
pleasure and ease.

%package sheets
Group: Office
Summary: A fully-featured spreadsheet application
Provides: %name-tables = %EVR
Requires: %name-core
%description sheets
Tables is a fully-featured calculation and spreadsheet tool.  Use it to
quickly create and calculate various business-related spreadsheets, such
as income and expenditure, employee working hours...

%package stage
Group: Office
Summary: A full-featured presentation program
Provides: koffice-kpresenter = %koffice_ver
Obsoletes: koffice-kpresenter < %koffice_ver
Requires: %name-core
%description stage
Stage is a powerful and easy to use presentation application. You
can dazzle your audience with stunning slides containing images, videos,
animation and more.

%package karbon
Group: Graphics
Summary: A vector drawing application
Provides: karbon = %version-%release
Provides: koffice-karbon = %koffice_ver
Obsoletes: koffice-karbon < %koffice_ver
Requires: %name-core
Requires: pstoedit
%description karbon
Karbon is a vector drawing application with an user interface that is
easy to use, highly customizable and extensible. That makes Karbon a
great application for users starting to explore the world of vector
graphics as well as for artists wanting to create breathtaking vector
art.

Whether you want to create clipart, logos, illustrations or photorealistic
vector images - look no further, Karbon is the tool for you!

%if_enabled plan
%package plan
Group: Office
Summary: A project planner
Provides: koffice-kplato = %koffice_ver
Obsoletes: koffice-kplato < %koffice_ver
Requires: %name-core
Requires: kf5-kreport
%description plan
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.
%endif

%package gemini
Group: Office
Summary: Office Suite
Requires: %name-core
%description gemini
The KDE Office suite for 2-in-1 devices.

%package  okular-generators
Group: Office
Summary:  OpenDocument text and presenter support for okular
Requires: %name-stage
Requires: kde5-okular-core
Provides: calligra-okular-odp = %EVR
Obsoletes: calligra-okular-odp < %EVR
Provides: calligra-okular-odf = %EVR
Obsoletes: calligra-okular-odf < %EVR
%description okular-generators
%summary.

%package -n %libname
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libname
%name libraries

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch103 -p1

%build
%K5build \
    -DCALLIGRA_SHOULD_BUILD_PRODUCTS=ALL \
    -DPACKAGERS_BUILD=OFF \
    -DBUILD_TESTING=OFF \
    -DTEMPLATES_INSTALL_DIR:PATH=%_K5tmpl \
    #

%install
%K5install

## unpackaged files
rm -fv %buildroot%_datadir/mime/packages/{krita_ora,x-iwork-keynote-sffkey}.xml
rm -frv %buildroot/%_datadir/locale/x-test/

# remove InitialPreference
for f in %buildroot/%_K5xdgapp/*.desktop ; do
    sed -i '/^InitialPreference=/d' $f
done

%find_lang --with-kde --all-name %name

%files
%files common -f %name.lang
%dir %_K5srv/ServiceMenus/calligra/
%doc AUTHORS README

%files devel
%_K5bin/cstester
%_K5bin/cstrunner
%_K5bin/visualimagecompare
%_K5link/lib*.so

%files core
%dir %_K5plug/calligra/
%dir %_K5plug/calligra/colorspaces/
%dir %_K5plug/calligra/dockers/
%dir %_K5plug/calligra/formatfilters/
%dir %_K5plug/calligra/pageapptools/
%dir %_K5plug/calligra/shapefiltereffects/
%dir %_K5plug/calligra/shapes/
%dir %_K5plug/calligra/textediting/
%dir %_K5plug/calligra/textinlineobjects/
%dir %_K5plug/calligra/tools/
%config(noreplace) %_K5xdgconf/calligra_stencils.knsrc
%_K5bin/calligra
%_K5bin/calligraconverter
%_K5qml/
%_datadir/calligra
%_datadir/calligra_shape_music/fonts/Emmentaler-14.ttf
%_datadir/color/icc/calligra/
%_K5plug/calligra/textediting/calligra_textediting_autocorrect.so
%_K5plug/calligra/tools/calligra_tool_basicflakes.so
%_K5plug/calligra/textediting/calligra_textediting_changecase.so
%_K5plug/calligra/tools/calligra_tool_defaults.so
%_K5plug/calligra/dockers/calligra_docker_defaults.so
%_K5plug/calligra/dockers/calligra_docker_stencils.so
%_K5plug/calligrathumbnail.so
%_K5plug/calligradocinfopropspage.so
%_K5plug/calligra/pageapptools/kopabackgroundtool.so
%_K5plug/calligra/colorspaces/kolcmsengine.so
%_K5plug/calligra/formatfilters/calligra_filter_eps2svgai.so
%_K5plug/calligra/formatfilters/calligra_filter_pdf2svg.so
%_K5plug/calligra/formatfilters/calligra_filter_kpr2odp.so
%_K5plug/calligra/formatfilters/calligra_filter_vsdx2odg.so
%_K5plug/calligra/textediting/calligra_textediting_spellcheck.so
%_K5plug/calligra/textinlineobjects/calligra_textinlineobject_variables.so
%_K5plug/calligra/textediting/calligra_textediting_thesaurus.so
%_K5plug/calligra/shapes/calligra_shape_artistictext.so
%_K5plug/calligra/shapes/calligra_shape_chart.so
%_K5plug/calligra/shapes/calligra_shape_formula.so
%_K5plug/calligra/shapes/calligra_shape_music.so
%_K5plug/calligra/shapes/calligra_shape_picture.so
%_K5plug/calligra/shapes/calligra_shape_plugin.so
%_K5plug/calligra/shapes/calligra_shape_spreadsheet.so
%_K5plug/calligra/shapes/calligra_shape_text.so
%_K5plug/calligra/shapes/calligra_shape_vector.so
%_K5plug/calligra/shapes/calligra_shape_video.so
%_K5plug/calligra/shapefiltereffects/calligra_filtereffects.so
%_K5plug/calligraimagethumbnail.so
%_K5xdgmime/msooxml-all.xml
%_K5xdgmime/calligra_svm.xml
%_K5icon/*/*/*/*
%_K5srv/calligra_odg_thumbnail.desktop
%_K5srv/calligradocinfopropspage.desktop
%_K5srv/flow_vsdx_thumbnail.desktop
%_K5srv/flow_wpg_thumbnail.desktop
%_K5plug/calligra/shapes/calligra_shape_paths.so

%files gemini
%_K5bin/calligragemini
%_K5bin/calligrageminithumbnailhelper
%_K5xdgapp/org.kde.calligragemini.desktop
%_datadir/calligragemini/
%_datadir/metainfo/org.kde.calligragemini.appdata.xml

%files sheets
%config(noreplace) %_K5xdgconf/calligrasheetsrc
%_K5bin/calligrasheets
%_K5lib/libkdeinit5_calligrasheets.so
%_K5plug/calligra/*/calligrasheets*.so
%_K5plug/calligrasheets/*/kspread*module.so
%_K5plug/calligra/formatfilters/calligra_filter_*sheets*.so
%_K5plug/calligra/formatfilters/calligra_filter_*kspread*.so
%_K5plug/calligra/formatfilters/calligra_filter_xls*.so
%_K5plug/calligrasheets/extensions/sheetssolver.so
%_K5plug/calligra/deferred/calligra_shape_spreadsheet-deferred.so
%_datadir/calligrasheets/
%_K5xmlgui/calligrasheets/
%_K5srv/sheets_*_thumbnail.desktop
%_K5srv/ServiceMenus/calligra/sheets_print.desktop
%_K5cfg/calligrasheets.kcfg
%_K5tmpl/SpreadSheet.*
%_K5tmpl/.source/SpreadSheet.*
%_K5xdgapp/org.kde.calligrasheets.desktop
%_datadir/metainfo/org.kde.calligrasheets.appdata.xml

%files stage
%config(noreplace) %_K5xdgconf/calligrastagerc
%doc stage/AUTHORS stage/CHANGES
%_K5plug/calligra/*/*stage*.*
%_K5plug/calligra/textinlineobjects/kprvariables.so
%_K5plug/calligrastage/pageeffects/kpr_pageeffect_*.so
%_K5plug/calligrastage/shapeanimations/kpr_shapeanimation_*.so
%_K5plug/calligra/formatfilters/calligra_filter_ppt2odp.so
%_K5plug/calligra/formatfilters/calligra_filter_pptx2odp.so
%_K5plug/calligra/formatfilters/calligra_filter_key2odp.so
%_K5plug/calligrastage/tools/calligrastagetoolanimation.so
%_datadir/calligrastage/
%_K5xmlgui/calligrastage/
%_K5tmpl/Presentation.*
%_K5tmpl/.source/Presentation.*
%_K5srv/stage_*_thumbnail.desktop

%files karbon
%config(noreplace) %_K5xdgconf/karbonrc
%_K5bin/karbon
%_K5lib/libkdeinit5_karbon.so
%_K5plug/karbon/extensions/*karbon*.*
%_K5plug/calligra/formatfilters/calligra_filter_wmf2svg.so
%_K5plug/calligra/formatfilters/calligra_filter_xfig2odg.so
%_K5plug/calligra/formatfilters/calligra_filter_karbon1x2karbon.so
%_K5plug/calligra/formatfilters/calligra_filter_karbon2image.so
%_K5plug/calligra/formatfilters/calligra_filter_karbon2svg.so
%_K5plug/calligra/formatfilters/calligra_filter_karbon2wmf.so
%_K5plug/calligra/formatfilters/calligra_filter_svg2karbon.so
%_K5plug/calligra/parts/karbonpart.so
%_K5plug/calligra/tools/karbon_tools.so
%_datadir/karbon/
%_K5xmlgui/karbon/
%_K5srv/karbon_*_thumbnail.desktop
%_K5tmpl/Illustration.*
%_K5tmpl/.source/Illustration.*
%_K5xdgapp/org.kde.karbon.desktop
%_K5srv/ServiceMenus/calligra/karbon_print.desktop
%_datadir/metainfo/org.kde.karbon.appdata.xml

%if_enabled plan
%files plan
%doc plan/CHANGELOG plan/TODO
%config(noreplace) %_K5xdgconf/calligraplan*rc
%_K5bin/calligraplan
%_K5bin/calligraplanwork
%_K5lib/libkdeinit5_calligraplan.so
%_K5lib/libkdeinit5_calligraplanwork.so
%_K5plug/calligra/parts/calligraplanpart.so
%_K5plug/calligra/formatfilters/planicalexport.so
%_K5plug/calligra/formatfilters/plankplatoimport.so
%_K5plug/calligraplan/schedulers/libplantjscheduler.so
%_K5plug/calligraplanworkpart.so
%_K5plug/kreport/planreport_textplugin.so
%_datadir/calligraplan/
%_datadir/calligraplanwork/
%_K5xmlgui/calligraplan/
%_K5xmlgui/calligraplanwork/
%_K5cfg/calligraplansettings.kcfg
%_K5cfg/calligraplanworksettings.kcfg
%_K5xdgapp/org.kde.calligraplan.desktop
%_K5xdgapp/org.kde.calligraplanwork.desktop
%endif

%files words
%config(noreplace) %_K5xdgconf/calligrawordsrc
%_K5bin/calligrawords
%_K5lib/libkdeinit5_calligrawords.so
%_K5plug/calligra/parts/calligrawordspart.so
%_datadir/calligrawords/
%_K5xmlgui/calligrawords/
%_K5tmpl/TextDocument.*
%_K5tmpl/.source/TextDocument.*
%_K5xdgapp/org.kde.calligrawords.desktop
%_K5xdgapp/org.kde.calligrawords_ascii.desktop
%_K5plug/calligra/formatfilters/calligra_filter_applixword2odt.so
%_K5plug/calligra/formatfilters/calligra_filter_ascii2words.so
%_K5plug/calligra/formatfilters/calligra_filter_doc2odt.so
%_K5plug/calligra/formatfilters/calligra_filter_docx2odt.so
%_K5plug/calligra/formatfilters/calligra_filter_html2ods.so
%_K5plug/calligra/formatfilters/calligra_filter_odt2ascii.so
%_K5plug/calligra/formatfilters/calligra_filter_odt2epub2.so
%_K5plug/calligra/formatfilters/calligra_filter_odt2html.so
%_K5plug/calligra/formatfilters/calligra_filter_odt2mobi.so
%_K5plug/calligra/formatfilters/calligra_filter_rtf2odt.so
%_K5plug/calligra/formatfilters/calligra_filter_wpd2odt.so
%_K5plug/calligra/formatfilters/calligra_filter_wpg2svg.so
%_K5plug/calligra/formatfilters/calligra_filter_wpg2odg.so
%_K5plug/calligra/formatfilters/calligra_filter_wps2odt.so
%_K5plug/calligra/formatfilters/calligra_filter_odt2docx.so
%_K5plug/calligra/formatfilters/calligra_filter_odt2wiki.so
#%_K5xdgapp/calligra_filter_odt2docx.desktop
%_K5srv/words_*_thumbnail.desktop
%_K5srv/ServiceMenus/calligra/words_print.desktop
%_K5xdgmime/wiki-format.xml
%_datadir/metainfo/org.kde.calligrawords.appdata.xml

%files okular-generators
%_K5lib/libkookularGenerator_odp.so*
%_K5lib/libkookularGenerator_odt.so*
%_K5plug/okular/generators/okularGenerator_*_calligra.so
%_K5xdgapp/okularApplication_*_calligra.desktop
%_K5srv/okular*_calligra.desktop

%files -n %libname
%_K5lib/lib*.so.*
%exclude %_K5lib/libkookularGenerator_odp.so*
%exclude %_K5lib/libkookularGenerator_odt.so*

%changelog
* Wed Sep 18 2019 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt9
- fix compile with new Qt

* Thu Jul 04 2019 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt8
- set additional provides (ALT#16944)
- build without qtwebkit

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt7
- NMU: remove rpm-build-ubt from BR:

* Mon Feb 18 2019 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt6
- fix build with poppler-0.72

* Thu Nov 08 2018 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt5
- fix build with poppler-0.71

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0:3.1.0-alt4
- Fixed build with new Qt.

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt3
- rebuild with new okular

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt2
- rebuild with new okular

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt1
- new version

* Tue Oct 31 2017 Sergey V Turchin <zerg@altlinux.org> 0:3.0.1-alt2
- move binaries to /usr/bin

* Wed Aug 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0:3.0.1-alt1
- Updated to upstream version 3.0.1.

* Fri Apr 08 2016 Sergey V Turchin <zerg@altlinux.org> 0:2.9.11-alt2
- rebuild with new poppler

* Thu Feb 11 2016 Sergey V Turchin <zerg@altlinux.org> 0:2.9.11-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 0:2.9.10-alt3
- remove InitialPreference from desktop-files

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 0:2.9.10-alt2
- rebuild with new okular

* Mon Jan 18 2016 Sergey V Turchin <zerg@altlinux.org> 0:2.9.10-alt1
- new version

* Mon Nov 09 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.9-alt1
- new version

* Fri Sep 04 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.7-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.5-alt2
- rebuild with new exiv2

* Fri Jun 19 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.5-alt1
- new version

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0:2.9.2-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Apr 23 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.2-alt2
- rebuild with new marble

* Wed Apr 15 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.2-alt1
- new version

* Thu Mar 26 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.1-alt1
- new version

* Wed Mar 04 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.0-alt1
- new version

* Wed Jan 28 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.8.7-alt3
- rebuild with new okular

* Thu Dec 25 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.7-alt2
- split Calligra Active to separate package
- rebuilt with new poppler

* Tue Dec 09 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.7-alt1
- new version

* Thu Nov 27 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.6-alt1
- new version

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.5-alt3
- rebuild

* Fri Aug 15 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.5-alt2
- rebuilt with new KDE

* Mon Jul 07 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.5-alt1
- new version

* Fri Jun 06 2014 Alexey Shabalin <shaba@altlinux.ru> 0:2.8.3-alt2
- switch to librevenge-based import libs

* Thu May 22 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.3-alt0.M70P.1
- built for M70P

* Thu May 22 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.3-alt1
- new version

* Thu Apr 24 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.2-alt0.M70P.1
- built for M70P

* Wed Apr 23 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.2-alt1
- new version

* Thu Apr 03 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.1-alt0.M70P.1
- built for M70P

* Wed Apr 02 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.1-alt1
- new version

* Wed Apr 02 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.0-alt0.M70P.1
- built for M70P

* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.0-alt1
- new version

* Tue Feb 04 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.7.5-alt4
- rebuilt

* Fri Dec 20 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.5-alt3
- require stage for okular odp

* Thu Dec 19 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.5-alt2
- move ppt import modules into core subpackage

* Mon Dec 09 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.5-alt1
- new version

* Fri Nov 01 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.4-alt1
- new version

* Mon Sep 16 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.3-alt1
- new version

* Wed Sep 11 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.2-alt1
- new version

* Thu Aug 01 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.1-alt1
- new version

* Tue Jul 30 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.4-alt1.M70P.1
- built for M70P

* Tue Jul 30 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.4-alt2
- fix build requires

* Mon Jul 29 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.4-alt1
- new version

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.3-alt1
- new version

* Wed Apr 24 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.1-alt4
- rebuild with new poppler

* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.1-alt3
- rebuild with new poppler
- fix requires

* Thu Feb 28 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.1-alt2
- built with opengtl

* Fri Feb 22 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.1-alt1
- new version

* Thu Feb 07 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.0-alt1
- new version

* Sun Jan 27 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.5.5-alt2
- don't split libs
- fix requires

* Thu Jan 24 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.5.5-alt1
- new version

* Tue Dec 18 2012 Sergey V Turchin <zerg@altlinux.org> 0:2.5.4-alt3
- rebuilt with new marble

* Sun Dec 16 2012 Sergey V Turchin <zerg@altlinux.org> 0:2.5.4-alt1.M60P.1
- built for M60P

* Sun Dec 16 2012 Sergey V Turchin <zerg@altlinux.org> 0:2.5.4-alt2
- don't obsolete kivio by flow

* Thu Dec 13 2012 Sergey V Turchin <zerg@altlinux.org> 0:2.5.4-alt1
- new version

* Fri Nov 02 2012 Sergey V Turchin <zerg@altlinux.org> 0:2.5.3-alt1
- new version

* Wed Oct 31 2012 Sergey V Turchin <zerg@altlinux.org> 4:2.5.2-alt1
- new version

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4:2.4.1-alt1
- initial build
