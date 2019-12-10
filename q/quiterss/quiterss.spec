%ifnarch %e2k
%def_with qt5
%endif

Name: quiterss
Version: 0.19.2
Release: alt1

Summary: RSS/Atom aggregator
Summary(ru_RU.UTF-8): QuiteRSS - быстрая и удобная программа для чтения новостных лент RSS/Atom
License: GPLv3
Group: Networking/WWW

Url: http://code.google.com/p/quite-rss/
Source0: http://quite-rss.googlecode.com/files/QuiteRSS-%{version}-src.tar.gz
Source44: import.info
Source45: quiterss.watch
BuildRequires: desktop-file-utils
%if_with qt5
BuildRequires: qt5-base-devel qt5-tools
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: libqtsingleapplication-qt5-devel
Requires: qt5-sql-sqlite
%else
BuildRequires: gcc-c++ qt4-devel
BuildRequires: pkgconfig(QtGui) pkgconfig(QtNetwork) pkgconfig(QtWebKit) pkgconfig(QtXml) pkgconfig(QtSql)
BuildRequires: libqtsingleapplication-devel pkgconfig(phonon)
Requires: libqt4-sql-sqlite
%endif
BuildRequires: pkgconfig(sqlite3)
BuildRequires: dos2unix

%description
Qt-based RSS/Atom aggregator.

%description -l ru_RU.UTF-8
Быстрая и удобная программа для чтения новостных лент RSS/Atom,
написанная на Qt.

%prep
#setup -n QuiteRSS-%version-src
%setup -c
sed -i 's,qtsingleapplication.h,QtSolutions/&,' src/application/mainapplication.h
sed -i 's,phonon/audiooutput.h,kde4/&,' src/application/mainwindow.h
sed -i 's,phonon/mediaobject.h,kde4/&,' src/application/mainwindow.h
# 0.19.1 introduced CRLF EOLs here, reported upstream
dos2unix %name.desktop

%build
%if_with qt5
qmake-qt5 PREFIX=%prefix SYSTEMQTSA=True
%else
qmake-qt4 PREFIX=%prefix SYSTEMQTSA=True
%endif
%make_build release

%install
make install INSTALL_ROOT=%buildroot
desktop-file-validate %buildroot%_desktopdir/%name.desktop
%find_lang %name --with-qt --without-mo

%files -f %name.lang
%doc AUTHORS CHANGELOG COPYING README.md
%_bindir/%name
%dir %_datadir/%name/
%_datadir/%name/sound/
%_datadir/%name/style/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/apps/%name.png
%dir %_datadir/%name/lang

%changelog
* Wed Nov 27 2019 Michael Shigorin <mike@altlinux.org> 0.19.2-alt1
- new version (watch file uupdate)

* Wed Nov 20 2019 Michael Shigorin <mike@altlinux.org> 0.19.1-alt2
- replace BR: qt5-sql-sqlite3 with qt5-sql-sqlite (closes: #37515)

* Mon Nov 18 2019 Michael Shigorin <mike@altlinux.org> 0.19.1-alt1
- new version (watch file uupdate)
- desktop file fixup

* Sat Nov 16 2019 Anton Midyukov <antohami@altlinux.org> 0.19.0-alt1
- new version

* Sun Nov 10 2019 Anton Midyukov <antohami@altlinux.org> 0.18.12-alt2
- rebuild with qt5 except e2k

* Mon Jul 02 2018 Michael Shigorin <mike@altlinux.org> 0.18.12-alt1
- new version (watch file uupdate)

* Fri Jun 01 2018 Michael Shigorin <mike@altlinux.org> 0.18.11-alt1
- new version (watch file uupdate)

* Wed Apr 18 2018 Michael Shigorin <mike@altlinux.org> 0.18.10-alt1
- new version (watch file uupdate)

* Mon Dec 04 2017 Michael Shigorin <mike@altlinux.org> 0.18.9-alt1
- new version (watch file uupdate)

* Fri Aug 25 2017 Michael Shigorin <mike@altlinux.org> 0.18.8-alt1
- new version (watch file uupdate)

* Thu Aug 24 2017 Michael Shigorin <mike@altlinux.org> 0.18.7-alt1
- new version (watch file uupdate)

* Mon Jun 26 2017 Michael Shigorin <mike@altlinux.org> 0.18.6-alt1
- new version (watch file uupdate)

* Fri Jun 16 2017 Michael Shigorin <mike@altlinux.org> 0.18.5-alt1
- new version (watch file uupdate)

* Wed Mar 09 2016 Michael Shigorin <mike@altlinux.org> 0.18.4-alt1
- new version (watch file uupdate)

* Thu Jan 28 2016 Michael Shigorin <mike@altlinux.org> 0.18.3-alt1
- new version (watch file uupdate)

* Wed Jul 15 2015 Michael Shigorin <mike@altlinux.org> 0.18.2-alt1
- new version (watch file uupdate)

* Mon Jul 13 2015 Michael Shigorin <mike@altlinux.org> 0.18.1-alt1
- new version (watch file uupdate)

* Mon Apr 20 2015 Michael Shigorin <mike@altlinux.org> 0.17.7-alt1
- new version (watch file uupdate)

* Thu Feb 12 2015 Michael Shigorin <mike@altlinux.org> 0.17.6-alt1
- new version (watch file uupdate)

* Mon Jan 19 2015 Michael Shigorin <mike@altlinux.org> 0.17.5-alt1
- new version (watch file uupdate)

* Sat Jan 10 2015 Michael Shigorin <mike@altlinux.org> 0.17.4-alt1
- new version (watch file uupdate)

* Mon Jan 05 2015 Michael Shigorin <mike@altlinux.org> 0.17.3-alt1
- new version (watch file uupdate)

* Tue Dec 30 2014 Michael Shigorin <mike@altlinux.org> 0.17.2-alt1
- new version (watch file uupdate)

* Tue Nov 18 2014 Michael Shigorin <mike@altlinux.org> 0.17.1-alt1
- new version (watch file uupdate)

* Thu Oct 30 2014 Michael Shigorin <mike@altlinux.org> 0.17.0-alt2
- no need to fcimport it anymore

* Tue Sep 09 2014 Michael Shigorin <mike@altlinux.org> 0.17.0-alt1
- new version (watch file uupdate)

* Thu Aug 21 2014 Michael Shigorin <mike@altlinux.org> 0.16.2-alt1
- new version (watch file uupdate)

* Fri Jul 11 2014 Michael Shigorin <mike@altlinux.org> 0.16.1-alt1
- new version (watch file uupdate)

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_1
- update to new release by fcimport

* Tue May 27 2014 Michael Shigorin <mike@altlinux.org> 0.16.0-alt1
- new version (watch file uupdate)

* Tue May 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.15.4-alt1_1
- by mike@ request

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.5-alt1_1
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.4-alt1_1
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt1_1
- update to new release by fcimport

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1
- update to new release by fcimport

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_1
- new release

