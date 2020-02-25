
%global qt_module qtdeclarative
%def_enable bootstrap

Name: qt5-declarative
Version: 5.12.7
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtDeclarative component
Url: http://qt.io/
License:  LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Source: %qt_module-everywhere-src-%version.tar
Source10: rpm-build-qml.tar
Source1: qml
Source2: qml.env
Source3: find-provides.sh
Source4: find-requires.sh

%include %SOURCE1
%qml_req_skipall 0
%qml_add_req_nover Qt.test.qtestroot
%define __find_provides %SOURCE3
%define __find_requires %SOURCE4

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-qt5
BuildRequires: rpm-build-python3
BuildRequires: gcc-c++ glibc-devel qt5-base-devel
%if_disabled bootstrap
BuildRequires: qt5-tools
%endif

%description
%summary


%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel rpm-build-qml
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-qml
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
Obsoletes: libqt5-v8 < %version-%release
#Conflicts: qt5-quickcontrols < 5.7
Provides: qt5-qtdeclarative = %version-%release
%description -n libqt5-qml
%summary

%package -n libqt5-quick
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
Provides: libQtQuick5 = %version-release
%description -n libqt5-quick
%summary

%package -n libqt5-quickparticles
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-quickparticles
%summary

%package -n libqt5-quicktest
Group: System/Libraries
Summary: Qt5 - library
Provides: qml(Qt.test.qtestroot)
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-quicktest
%summary

%package -n libqt5-quickwidgets
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-quickwidgets
%summary

%package -n libqt5-quickshapes
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-quickshapes
%summary

%package -n rpm-build-qml
Group: Development/Other
Summary: RPM helper macros to rebuild QML packages
%description -n rpm-build-qml
These helper macros provide possibility to rebuild
QML modules by some Alt Linux Team Policy compatible way.

%prep
%include %SOURCE2
%setup -n %qt_module-everywhere-src-%version -a10
mv rpm-build-qml src/
mkdir bin_add
ln -s %__python3 bin_add/python

%build
export PATH=$PWD/bin_add:$PATH
%qmake_qt5
%make_build
%if_disabled bootstrap
%make docs
%endif

#build rpm-build-qml
export BUILDFLAGS="-I../../include/QtQml/%version -I../../include/QtQml/%version/QtQml -I../../include/QtQml"
pushd src/rpm-build-qml
%qmake_qt5 rpmbqml-qmlinfo.pro
%make_build
popd

%install
%install_qt5
%if_disabled bootstrap
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

#install rpm-build-qml
pushd src/rpm-build-qml
install -pD -m755 rpmbqml-qmlinfo %buildroot%_bindir/rpmbqml-qmlinfo
install -pD -m755 rpmbqml-prov-enum.pl %buildroot%_bindir/rpmbqml-prov-enum.pl
install -pD -m755 qml.prov %buildroot%_rpmlibdir/qml.prov
install -pD -m755 qml.prov.files %buildroot%_rpmlibdir/qml.prov.files
install -pD -m755 qml.req %buildroot%_rpmlibdir/qml.req
install -pD -m755 qml.req.files %buildroot%_rpmlibdir/qml.req.files
popd

mkdir -p %buildroot%_rpmmacrosdir/
cat %SOURCE1 | sed 's|define[[:space:]][[:space:]]*||' >> %buildroot%_rpmmacrosdir/qml
cat %SOURCE2 >> %buildroot%_rpmmacrosdir/qml.env

%files common
%doc LICENSE.*EXCEPT*
%doc dist/changes*
%dir %_qt5_qmldir/
%dir %_qt5_qmldir/Qt/
%dir %_qt5_qmldir/Qt/labs/
%dir %_qt5_qmldir/QtQml/
%dir %_qt5_qmldir/QtQuick/
%dir %_qt5_plugindir/qmltooling/

%files doc
%if_disabled bootstrap
%_qt5_docdir/*
%endif
%_qt5_examplesdir/*

%files -n libqt5-qml
%_qt5_libdir/libQt5Qml.so.*
%_qt5_qmldir/builtins.qmltypes
%_qt5_qmldir/Qt/labs/folderlistmodel/
%_qt5_qmldir/Qt/labs/qmlmodels/
%_qt5_qmldir/Qt/labs/settings/
%_qt5_qmldir/Qt/labs/sharedimage/
%_qt5_qmldir/Qt/labs/wavefrontmesh/
%_qt5_qmldir/QtQml/*
%_qt5_qmldir/QtQuick/LocalStorage/
%_qt5_qmldir/QtQuick/Layouts/
%_qt5_qmldir/QtQuick/Shapes/

%files -n libqt5-quick
%_qt5_libdir/libQt5Quick.so.*
#%_qt5_plugindir/accessible/libqtaccessiblequick.so
%_qt5_qmldir/QtQuick.2/
#%_qt5_qmldir/QtQuick/Dialogs/
#%_qt5_qmldir/QtQuick/PrivateWidgets/
%_qt5_qmldir/QtQuick/Window.2/

%files -n libqt5-quickparticles
%_qt5_libdir/libQt5QuickParticles.so.*
%_qt5_qmldir/QtQuick/Particles.2/

%files -n libqt5-quicktest
%_qt5_libdir/libQt5QuickTest.so.*
%_qt5_qmldir/QtTest/

%files -n libqt5-quickwidgets
%_qt5_libdir/libQt5QuickWidgets.so.*

%files -n libqt5-quickshapes
%_qt5_libdir/libQt5QuickShapes.so.*


%files devel
%_bindir/qml*
%_qt5_plugindir/qmltooling/*
%_qt5_bindir/qml*
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_headerdir/Qt*/
%_qt5_archdatadir/mkspecs/modules/*.pr*
%_qt5_archdatadir/mkspecs/features/*.pr*
%_libdir/cmake/Qt*/
%_pkgconfigdir/Qt?Qml.pc
%_pkgconfigdir/Qt?Quick*.pc
#%_pkgconfigdir/Qt?QmlDevTools.pc

%files devel-static
%_qt5_libdir/libQt?QmlDevTools.a
%_qt5_libdatadir/libQt?QmlDevTools.a
%_qt5_libdir/libQt?PacketProtocol.a
%_qt5_libdatadir/libQt?PacketProtocol.a
%_qt5_libdir/libQt?QmlDebug.a
%_qt5_libdatadir/libQt?QmlDebug.a

%files -n rpm-build-qml
%doc src/rpm-build-qml/LICENSE
%_rpmmacrosdir/qml
%_rpmmacrosdir/qml.env
%_rpmlibdir/qml.req
%_rpmlibdir/qml.req.files
%_rpmlibdir/qml.prov
%_rpmlibdir/qml.prov.files
%_bindir/rpmbqml-prov-enum.pl
%_bindir/rpmbqml-qmlinfo

%changelog
* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Fri Dec 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt3
- build with python3

* Fri Oct 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt2
- build docs

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Thu Jun 27 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt2
- provide qt5-qtdeclarative and libQtQuick5

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Thu Aug 16 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt2%ubt
- build docs

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1%ubt
- new version

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1%ubt
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Wed Mar 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt.2
- build docs

* Mon Feb 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt.1
- don't build docs

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Wed Oct 25 2017 Oleg Solovyov <mcpain@altlinux.org> 5.9.2-alt3%ubt
- add rpm-build-qml package

* Mon Oct 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt2%ubt
- build docs

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1%ubt
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt2
- build docs

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Oct 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- force SSE2 compile flags for ix86

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Mon Jul 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Fri Jun 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Tue Feb 24 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Fri Dec 12 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Tue Sep 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Wed Jun 04 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt2
- build docs

* Mon Jun 02 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Wed Feb 12 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1.M70P.2
- build docs

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1.M70P.1
- built for M70P

* Thu Oct 24 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- build docs

* Thu Sep 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
