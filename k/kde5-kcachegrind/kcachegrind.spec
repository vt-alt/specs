%add_findreq_skiplist %_K5bin/hotshot2calltree

%define rname kcachegrind

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Summary: GUI to profilers such as Valgrind
License: %gpl2only
Group: Development/Tools
Url: https://www.kde.org/applications/development/kcachegrind

%ifarch %ix86
Requires: valgrind
%endif

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5 rpm-build-licenses rpm-build-python3
BuildRequires: qt5-tools-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-karchive-devel kf5-kdoctools-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kio-devel kf5-kdbusaddons-devel

%description
%rname is a profile data visualization tool, used to determine the most time
consuming execution parts of program.

%prep
%setup -n %rname-%version
#exclude examples from build
sed -i -e '/add_subdirectory([[:space:]]*cgview[[:space:]]*)\|add_subdirectory([[:space:]]*qcachegrind[[:space:]]*)/d' CMakeLists.txt
# fix shebang
sed -i \
  -e "s|^#![[:space:]]*/usr/bin/env python$|#!%{__python3}|g" \
  converters/hotshot2calltree.cmake

%build
%K5build

%install
%K5install
%K5install_move data %rname

%find_lang %name --with-kde --all-name
%K5find_qtlang %name --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/dprof2calltree
%_K5bin/hotshot2calltree
%_K5bin/kcachegrind
%_K5bin/memprof2calltree
%_K5bin/op2calltree
%_K5bin/pprof2calltree
%_K5xdgapp/org.kde.%{rname}.desktop
%_K5icon/hicolor/*/*/%{rname}*.*
#%_K5xmlgui/%rname/
%_K5data/%rname/

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Mon Jan 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt2
- build with python3

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Mon Feb 25 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Fri Nov 17 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Mon Aug 28 2017 Stanislav Levin <slev@altlinux.org> 17.08.0-alt1
- Initial build

