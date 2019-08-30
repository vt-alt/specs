%define rname krename

Name: kde5-%rname
Version: 5.0.0
Release: alt6
%K5init

Summary: A powerful batch renamer for KDE5
Group: File tools
License: GPL
Url: https://userbase.kde.org/KRename

Source: %rname-%version.tar
Patch1: alt-startupinfo-labels-color.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: kf5-kcompletion-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-kjs-devel kf5-kio-devel kf5-kservice-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: libexiv2-devel libfreetype-devel libpodofo-devel libtag-devel
BuildRequires: qt5-base-devel

%description
Krename is a very powerful batch file renamer for KDE5 which can rename a list
of files based on a set of expressions. It can copy/move the files to another
directory or simply rename the input files. Krename supports many conversion
operations, including conversion of a filename to lowercase or to uppercase,
conversion of the first letter of every word to uppercase, adding numbers to
filenames, finding and replacing parts of the filename, and many more.
It can also change access and modification dates, permissions, and file ownership.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data locale
%find_lang --with-kde %rname

%files -f %rname.lang
%_K5bin/%rname
%_K5xdgapp/*.desktop
%_K5icon/*/*/apps/*.*
%_K5srv/ServiceMenus/*.desktop

%changelog
* Fri Jun 14 2019 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt6
- dont use ubt macro

* Tue Sep 04 2018 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt5
- NMU: rebuild with podofo 0.9.6

* Wed Apr 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt4
- fix conflict with kde4-krename

* Tue Apr 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt3
- add fix against KDEBUG-391291
- fix startup info page labels color

* Wed Apr 18 2018 Oleg Solovyov <mcpain@altlinux.org> 5.0.0-alt2
- add %%ubt tag for backporting

* Mon Apr 16 2018 Oleg Solovyov <mcpain@altlinux.org> 5.0.0-alt1
- initial build for ALT

