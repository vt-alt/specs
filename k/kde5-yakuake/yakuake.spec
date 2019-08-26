%define oname yakuake

Name:    kde5-%oname
Version: 19.08.0
Release: alt1

Summary: Very powerful Quake style Konsole for KF5
License: GPLv2, GPLv3 or any later version accepted by the membership of KDE e.V.
Group: Terminals
Url: http://extragear.kde.org/apps/yakuake/

# Download from https://download.kde.org/stable/yakuake/
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt5-declarative-devel
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
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-sonnet-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-svg-devel

Requires:  kde5-konsole
Requires:  kf5-kglobalaccel
Provides:  %oname = %version-release
Obsoletes: %oname < %version-release 

%description
A KDE konsole which looks like those found in Quake.

This version is built with KF5.

%prep
%setup -n %oname-%version

%build
%K5build

%install
%K5install
%find_lang --with-kde %oname

%files -f %oname.lang
%doc AUTHORS COPYING COPYING.DOC ChangeLog NEWS README TODO
%_K5bin/*
%_K5xdgconf/%oname.knsrc
%_K5xdgapp/*.desktop
%_K5icon/*/*/apps/*
%_datadir/%oname
%_K5notif/%oname.notifyrc
%_K5dbus_srv/*.service
%_datadir/metainfo/*.appdata.xml

%changelog
* Sun Aug 25 2019 Andrey Cherepanov <cas@altlinux.org> 19.08.0-alt1
- New version.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.5-alt1
- New version.

* Sun Dec 10 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- New version.

* Thu Jun 30 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt2
- Rename package to kde5-yakuake (ALT #32098)

* Mon Jun 20 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version on KF5
- Place in standard directories
- Requires kde-konsole

* Thu Apr 04 2013 Andrey Cherepanov <cas@altlinux.org> 2.9.9-alt1
- New version 2.9.9

* Sat Jul 17 2010 Andrey Rahmatullin <wrar@altlinux.org> 2.9.7-alt1
- 2.9.7

* Tue Jun 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.6-alt2
- rename back to yakuake

* Fri May 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.6-alt1
- 2.9.6

* Tue May 12 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.5-alt1
- 2.9.5

* Mon Nov 17 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.4-alt3
- remove update_*/clean_* invocations

* Wed Oct 29 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.4-alt2
- Sisyphus build
- rename to kde4-yakuake, enable __kde4_alternate_placement

* Sat Sep 06 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.4-alt1
- 2.9.4

* Sat Aug 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.3-alt2
- rebuild

* Mon Jun 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.3-alt1
- 2.9.3

* Sat May 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.2-alt1
- 2.9.2
- use %%K4find_lang

* Sun Mar 30 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.1-alt1
- 2.9.1

* Mon Mar 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9-alt1
- 2.9 (KDE4 version)
- Daedalus build

* Sun Feb 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Nov 20 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.8-alt2
- spec cleanup
- enable _unpackaged_files_terminate_build
- fix packaging of icons (#10173, php-coder@)

* Sat Oct 13 2007 Nick S. Grechukh <gns@altlinux.org> 2.8-alt1
- new version (wrar@ reminded ;)

* Thu May 04 2006 Nick S. Grechukh <gns@altlinux.org> 2.7.5-alt1
- new version. fixed Url and Source. i18n removed (fixed in upstream)

* Mon Feb 13 2006 Nick S. Grechukh <gns@altlinux.org> 2.7.3-alt5
- removed kdedesktop2mdkmenu

* Sun Nov 13 2005 Nick S. Grechukh <gns@altlinux.ru> 2.7.3-alt4
- new version with i18n patch from Albert Valiev

* Mon Oct 24 2005 Nick S. Grechukh <gns@altlinux.org> 2.7.2-alt1
- new version

* Thu Oct 13 2005 Nick S. Grechukh <gns@altlinux.org> 2.6-alt1
- initial build 
