%define rname kmag

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Summary: %rname is a small utility to magnify a part of the screen
License: %gpl2only
Group: Graphical desktop/KDE
Url: https://www.kde.org/applications/utilities/kmag
Source0: %rname-%version.tar
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt rpm-build-licenses 
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kdoctools-devel kf5-ki18n-devel
BuildRequires: kf5-kio-devel kf5-kauth-devel
BuildRequires: libqaccessibilityclient-qt5-devel

%description
%summary. %rname is very useful for people with visual disabilities and for
those working in the fields of image analysis, web development etc.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data %rname
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/%rname
%_K5xdgapp/org.kde.%{rname}.desktop
%_K5icon/hicolor/*/*/%{rname}*.*
#%_K5xmlgui/%rname/
%_K5data/%rname/

%changelog
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

* Wed Nov 21 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2
- build without qaccessibilityclient

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Fri Nov 17 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Aug 25 2017 Stanislav Levin <slev@altlinux.org> 17.08.0-alt2%ubt
- Fix BuildRequires to compile against Qt5 version qaccessibility library

* Thu Aug 24 2017 Stanislav Levin <slev@altlinux.org> 17.08.0-alt1%ubt
- Initial build

