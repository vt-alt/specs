%define rname kig
%add_python3_path %_K5bin
%add_findreq_skiplist %_K5bin/pykig.py
%define add_python3_requires() %(echo -n "Requires: "; for p in %*; do echo -n "python3($p) "; done; echo)

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Education
Summary: Interactive Geometry
Url: http://www.kde.org
License: GPLv2+ or LGPLv2+

%add_python3_requires traceback os math getopt xml.sax.saxutils

Source: %rname-%version.tar
# upstream
Patch1: 0001-explicitly-use-QLibrary-to-load-libpython-like-pykde.patch

# Automatically added by buildreq on Tue Mar 22 2016 (-bi)
# optimized out: boost-python-headers cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libqt5-xmlpatterns libstdc++-devel libxcbutil-keysyms pkg-config python-base python-devel python-modules python3 qt5-base-devel rpm-build-gir rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: boost-devel-headers boost-python-devel extra-cmake-modules kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel python-module-google python3-base qt5-svg-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-python3
BuildRequires: extra-cmake-modules qt5-base-devel qt5-svg-devel qt5-xmlpatterns-devel
BuildRequires: boost-devel-headers boost-python3-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel kf5-kcrash-devel

%description
Kig is a program for exploring geometric constructions.


%prep
%setup -n %rname-%version
%patch1 -p1
sed -i '1d' pykig/pykig.py
sed -i '1i#!%__python3' pykig/pykig.py
#sed -i -E '/[[:space:]]except[[:space:]]+.*,.*/s/(^.*except[[:space:]]+)([[:alpha:]].*):$/\1(\2):/' pykig/pykig.py

%build
PY3_VER_WO_DOTS=`echo "%_python3_abi_version"| sed 's|\.||g'`
%K5build \
    -DPYTHON_EXECUTABLE:PATH=%__python3 \
    -DPYTHON_INCLUDE_DIR=%__python3_includedir \
    -DPYTHON_LIBRARY=%__libpython3 \
    -DBoostPython_INCLUDE_DIRS="%__python3_includedir;%_includedir/boost" \
    -DBoostPython_LIBRARIES="%__libpython3;%_libdir/libboost_python${PY3_VER_WO_DOTS}.so" \
    #

%install
%K5install
%K5install_move data kig katepart
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/kig
%_K5bin/pykig.py
%_K5plug/kigpart.so
%_K5data/kig/
%_datadir/katepart5/syntax/*-kig.xml
%_K5icon/*/*/apps/kig.*
%_K5icon/*/*/mimetypes/application-x-kig.*
%_K5xmlgui/kig/
%_K5xdgapp/org.kde.kig.desktop
%_K5srv/kig_part.desktop

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Mon Dec 02 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt2
- build with python3
- remove ubt tag

* Wed Nov 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Fri Jul 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Wed Jun 06 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2
- rebuild with new boost

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1
- new version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
