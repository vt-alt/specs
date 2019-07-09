Name:           kdesvn
Version:        2.1.0
Release:        alt1
Summary:        A subversion client for KF5 with KIO integration

Group:          Development/Tools
License:        GPLv2+
URL:            https://projects.kde.org/projects/extragear/sdk/kdesvn
# git clone git://anongit.kde.org/kdesvn
Source0:        %name-%{version}.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: gcc-c++
BuildRequires: subversion-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-ktextwidgets-devel

%description
kdesvn is yet another client for subversion. But it uses native
KDE API instead of a extra lib like GAMBAS and it is using the
native subversion delevelopment API instead of just parsing the
output of the commandline tool like most other clients do. It tries
to setup a look and feel like the standard filemanager of KDE and is
integrated into it via KPart.

The base C++ interface to subversion I took from the (real great) tool
Rapidsvn (see http://rapidsvn.tigris.org/) with some modifcations andi
fixes.

%prep
%setup -q

%build
%K5init no_altplace
%K5build

%install
%K5install
%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING GPL.txt TODO
%_K5bin/kdesvn*
%_qt5_plugindir/*.so
%_qt5_plugindir/kf5/kded/*.so
%_K5srv/*
%_datadir/kconf_update/*
%_K5cfg/*.kcfg
%_K5dbus_iface/*
%_K5dbus_srv/*
%_K5icon/hicolor/*/*/*.png
%_K5icon/hicolor/*/*/*.svgz
%_K5xdgapp/*.desktop
%_K5xmlgui/%name
%_datadir/%name
%_datadir/metainfo/*.appdata.xml

%changelog
* Mon Jul 08 2019 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Tue Oct 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt3
- NMU: fixed build with Qt-5.11.

* Sun Jan 22 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt2
- Fix summary and description

* Fri Jan 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version for KF5

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- New version

* Tue Oct 06 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt2
- Fix localization build

* Wed Mar 19 2014 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- First build KDE4 version for ALT Linux (ALT #29251)
