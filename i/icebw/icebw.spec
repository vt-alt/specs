# For build on x86_64 fix (via macros?)
#gpointer knop=gtk_object_get_user_data(GTK_OBJECT(widget));
#switch ((gint)knop)

%define build_lang uk_UA.KOI8-U

%define oname iceBw
%define oversion 14_14

Name:    icebw
Version: 14.14
Release: alt1
Summary: Free financial accounting system with GTK interface

Group:   Office
License: GPL-2.0
Url:     http://www.iceb.net.ua

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %url/download/%name-%oversion.tar.bz2
Source1: %name.watch
Patch1:	 %name-fix-pathes.patch
Patch2:  %name-alt-fix-missing-global-variables.patch
Patch3:  %name-bindir.patch
Patch4:  %name-fix-mariadb-link-library.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libmariadb-devel
BuildRequires: libgtk+3-devel
BuildRequires: libpcre-devel

%description
Free financial accounting system.

%prep
%setup -q -c
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
subst "s|/usr/share/locale/ru/|%buildroot%_datadir/locale/uk/|g" locale/uk_ru

%build
%cmake_insource -GNinja
%ninja_build

%install
%ninja_install
#mkdir -p %buildroot%_bindir
#find buhg_g -perm 0755 -a -name i_\* -a ! -name \*.dir -exec cp -v '{}' %buildroot%_bindir ';'
mkdir -p %buildroot%_datadir/locale/uk/LC_MESSAGES
pushd locale
./uk_ru
popd
mkdir -p %buildroot%_desktopdir
cp -v desktop/applications/*.desktop %buildroot%_desktopdir
mkdir -p %buildroot%_pixmapsdir
cp -v desktop/pixmaps/*.png %buildroot%_pixmapsdir

%files
%_bindir/*
%_desktopdir/*.desktop
%_pixmapsdir/*.png
%_datadir/locale/uk/LC_MESSAGES/%oname.mo

%changelog
* Wed Jul 01 2020 Andrey Cherepanov <cas@altlinux.org> 14.14-alt1
- new version 14.14
- build using ninja
- fix License tag according to SPDX

* Fri May 01 2020 Cronbuild Service <cronbuild@altlinux.org> 14.13-alt1
- new version 14.13

* Mon Mar 09 2020 Cronbuild Service <cronbuild@altlinux.org> 14.12-alt1
- new version 14.12

* Wed Jan 29 2020 Cronbuild Service <cronbuild@altlinux.org> 14.11-alt1
- new version 14.11

* Tue Dec 24 2019 Cronbuild Service <cronbuild@altlinux.org> 14.10-alt1
- new version 14.10

* Tue Oct 29 2019 Andrey Cherepanov <cas@altlinux.org> 14.9-alt1
- new version 14.9

* Mon Sep 16 2019 Andrey Cherepanov <cas@altlinux.org> 14.8-alt1
- new version 14.8

* Tue Aug 13 2019 Andrey Cherepanov <cas@altlinux.org> 14.7-alt1
- new version 14.7
- fix path of MariaDB includes and its library name
- add development requires (libmariadb-devel and libpcre-devel)

* Sat Jun 22 2019 Cronbuild Service <cronbuild@altlinux.org> 14.6-alt1
- new version 14.6

* Thu Jun 06 2019 Cronbuild Service <cronbuild@altlinux.org> 14.5-alt1
- new version 14.5

* Sun Feb 03 2019 Cronbuild Service <cronbuild@altlinux.org> 14.4-alt1
- new version 14.4

* Sat Dec 08 2018 Cronbuild Service <cronbuild@altlinux.org> 14.3-alt1
- new version 14.3

* Sun Oct 21 2018 Cronbuild Service <cronbuild@altlinux.org> 14.2-alt1
- new version 14.2

* Tue Sep 18 2018 Cronbuild Service <cronbuild@altlinux.org> 14.1-alt1
- new version 14.1

* Thu Sep 06 2018 Cronbuild Service <cronbuild@altlinux.org> 14.0-alt1
- new version 14.0

* Wed Aug 01 2018 Cronbuild Service <cronbuild@altlinux.org> 13.8-alt1
- new version 13.8

* Wed Jun 20 2018 Cronbuild Service <cronbuild@altlinux.org> 13.7-alt1
- new version 13.7

* Fri Jun 08 2018 Cronbuild Service <cronbuild@altlinux.org> 13.6-alt1
- new version 13.6

* Thu May 03 2018 Cronbuild Service <cronbuild@altlinux.org> 13.5-alt1
- new version 13.5

* Tue Apr 03 2018 Cronbuild Service <cronbuild@altlinux.org> 13.4-alt1
- new version 13.4

* Sun Mar 04 2018 Cronbuild Service <cronbuild@altlinux.org> 13.3-alt1
- new version 13.3

* Thu Feb 01 2018 Cronbuild Service <cronbuild@altlinux.org> 13.2-alt1
- new version 13.2

* Tue Jan 02 2018 Cronbuild Service <cronbuild@altlinux.org> 13.1-alt1
- new version 13.1

* Thu Nov 30 2017 Cronbuild Service <cronbuild@altlinux.org> 13.0-alt1
- new version 13.0

* Sat Nov 04 2017 Andrey Cherepanov <cas@altlinux.org> 12.14-alt1
- new version 12.14

* Mon Feb 06 2017 Andrey Cherepanov <cas@altlinux.org> 12.6-alt2
- Prepare for cronbuild

* Tue Jan 03 2017 Andrey Cherepanov <cas@altlinux.org> 12.6-alt1
- new version 12.6

* Mon Dec 12 2016 Andrey Cherepanov <cas@altlinux.org> 12.5-alt1
- new version 12.5

* Fri Dec 02 2016 Andrey Cherepanov <cas@altlinux.org> 12.4-alt1
- new version 12.4

* Tue Nov 01 2016 Andrey Cherepanov <cas@altlinux.org> 12.3-alt1
- new version 12.3

* Sat Oct 01 2016 Andrey Cherepanov <cas@altlinux.org> 12.2-alt1
- new version 12.2

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 12.1-alt1
- new version 12.1

* Thu Sep 01 2016 Andrey Cherepanov <cas@altlinux.org> 12.0-alt1
- new version 12.0

* Tue Aug 02 2016 Andrey Cherepanov <cas@altlinux.org> 11.18-alt1
- new version 11.18

* Sat Jul 16 2016 Andrey Cherepanov <cas@altlinux.org> 11.17-alt1
- new version 11.17

* Thu Jul 14 2016 Andrey Cherepanov <cas@altlinux.org> 11.16-alt1
- new version 11.16

* Fri Jun 10 2016 Andrey Cherepanov <cas@altlinux.org> 11.15-alt1
- new version 11.15

* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 11.14-alt1
- new version 11.14

* Tue May 03 2016 Andrey Cherepanov <cas@altlinux.org> 11.13-alt1
- new version 11.13

* Tue Apr 19 2016 Andrey Cherepanov <cas@altlinux.org> 11.12-alt1
- new version 11.12

* Fri Apr 08 2016 Andrey Cherepanov <cas@altlinux.org> 11.10-alt1
- new version 11.10

* Sat Apr 02 2016 Andrey Cherepanov <cas@altlinux.org> 11.9-alt1
- new version 11.9

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 11.7-alt1
- new version 11.7

* Tue Feb 02 2016 Andrey Cherepanov <cas@altlinux.org> 11.5-alt1
- new version 11.5
- fix missing global variables as `organ`

* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 11.4-alt1
- new version 11.4

* Wed Dec 02 2015 Andrey Cherepanov <cas@altlinux.org> 11.3-alt1
- new version 11.3

* Thu Oct 08 2015 Andrey Cherepanov <cas@altlinux.org> 11.2-alt1
- new version 11.2

* Fri Oct 02 2015 Andrey Cherepanov <cas@altlinux.org> 11.1-alt1
- new version 11.1

* Tue Sep 01 2015 Andrey Cherepanov <cas@altlinux.org> 11.0-alt1
- new version 11.0

* Mon Aug 03 2015 Andrey Cherepanov <cas@altlinux.org> 10.17-alt1
- new version 10.17

* Sat Jul 25 2015 Andrey Cherepanov <cas@altlinux.org> 10.16-alt1
- new version 10.16

* Thu Jul 09 2015 Andrey Cherepanov <cas@altlinux.org> 10.15-alt1
- new version 10.15

* Fri Jul 03 2015 Andrey Cherepanov <cas@altlinux.org> 10.14-alt1
- new version 10.14

* Tue Jun 16 2015 Andrey Cherepanov <cas@altlinux.org> 10.13-alt1
- new version 10.13

* Fri Jun 12 2015 Andrey Cherepanov <cas@altlinux.org> 10.12-alt1
- new version 10.12

* Fri Jun 05 2015 Andrey Cherepanov <cas@altlinux.org> 10.11-alt1
- new version 10.11

* Sat May 02 2015 Andrey Cherepanov <cas@altlinux.org> 10.10-alt1
- new version 10.10

* Wed Apr 01 2015 Andrey Cherepanov <cas@altlinux.org> 10.9-alt1
- new version 10.9

* Fri Mar 13 2015 Andrey Cherepanov <cas@altlinux.org> 10.8-alt1
- new version 10.8
- fix path to database template in i_admin

* Wed Mar 04 2015 Andrey Cherepanov <cas@altlinux.org> 10.7-alt1
- new version 10.7

* Fri Feb 20 2015 Andrey Cherepanov <cas@altlinux.org> 10.6-alt1
- new version 10.6

* Wed Jan 21 2015 Andrey Cherepanov <cas@altlinux.org> 10.5-alt1
- new version 10.5

* Tue Jan 06 2015 Andrey Cherepanov <cas@altlinux.org> 10.3-alt1
- new version 10.3

* Tue Dec 02 2014 Andrey Cherepanov <cas@altlinux.org> 10.2-alt1
- new version 10.2

* Fri Nov 14 2014 Andrey Cherepanov <cas@altlinux.org> 10.1-alt1
- new version 10.1

* Tue Sep 02 2014 Andrey Cherepanov <cas@altlinux.org> 10.0-alt1
- New version

* Mon Jun 02 2014 Andrey Cherepanov <cas@altlinux.org> 9.15-alt1
- New version

* Thu Feb 27 2014 Andrey Cherepanov <cas@altlinux.org> 9.11-alt1
- New version
- Fix project URL

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 7.0-alt1.qa1
- NMU: rebuilt with libmysqlclient.so.18.

* Wed Aug 31 2011 Andrey Cherepanov <cas@altlinux.org> 7.0-alt1
- New version 7.0

* Tue Apr 19 2011 Andrey Cherepanov <cas@altlinux.org> 6.11-alt1
- New version 6.11

* Wed Dec 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 6.1-alt1
- 6_1

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 4.0-alt1
- initial build for ALT Linux Sisyphus

