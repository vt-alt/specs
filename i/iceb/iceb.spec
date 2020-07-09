%define oname iceB

Name:    iceb
Version: 19.14
Release: alt1

Summary: Free financial accounting system (console)

Packager: Andrey Cherepanov <cas@altlinux.org>

Group:   Office
License: GPL-2.0
Url:     http://iceb.net.ua

Source:  %name-%version.tar
Source1: %name.watch
Patch2:  %name-fix-mariadb-link-library.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: libmariadb-devel
BuildRequires: libncursesw-devel
BuildRequires: libpcre-devel

%description
Free financial accounting system.

%prep
%setup -q -c
%patch2 -p2

%build
%cmake -GNinja
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

install -d %buildroot%_bindir
find BUILD/buhg -perm 0755 -a -type f -exec cp '{}' %buildroot%_bindir ';'
#find BUILD/additionally/other -perm 0755 -a -type f -exec cp '{}' %buildroot%_bindir ';'

install -d %buildroot%_desktopdir
cp -a desktop/applications/*.desktop %buildroot%_desktopdir
install -d %buildroot%_pixmapsdir
cp -a desktop/pixmaps/*.png %buildroot%_pixmapsdir

# Remove terminfo
rm -rf %buildroot/lib/terminfo

%files
%doc CHANGES COPYING READMI.TXT
%_bindir/*
%_datadir/%oname
%_desktopdir/*.desktop
%_pixmapsdir/*.png
%_sysconfdir/cups/iceb.*
%_libexecdir/cups/filter/iceb_ps

%changelog
* Wed Jul 01 2020 Andrey Cherepanov <cas@altlinux.org> 19.14-alt1
- new version 19.14
- build using ninja
- package cups filter
- fix License tag according to SPDX

* Fri May 01 2020 Cronbuild Service <cronbuild@altlinux.org> 19.13-alt1
- new version 19.13

* Mon Mar 09 2020 Cronbuild Service <cronbuild@altlinux.org> 19.12-alt1
- new version 19.12

* Wed Jan 29 2020 Cronbuild Service <cronbuild@altlinux.org> 19.11-alt1
- new version 19.11

* Tue Dec 24 2019 Cronbuild Service <cronbuild@altlinux.org> 19.10-alt1
- new version 19.10

* Tue Oct 29 2019 Andrey Cherepanov <cas@altlinux.org> 19.9-alt1
- new version 19.9

* Sat Sep 07 2019 Andrey Cherepanov <cas@altlinux.org> 19.8-alt1
- new version 19.8

* Tue Aug 13 2019 Andrey Cherepanov <cas@altlinux.org> 19.7-alt1
- new version 19.7
- fix path of MariaDB includes and its library name
- add development requires (libmariadb-devel and libpcre-devel)

* Sat Jun 22 2019 Cronbuild Service <cronbuild@altlinux.org> 19.6-alt1
- new version 19.6

* Thu Jun 06 2019 Cronbuild Service <cronbuild@altlinux.org> 19.5-alt1
- new version 19.5

* Sun Feb 03 2019 Cronbuild Service <cronbuild@altlinux.org> 19.4-alt1
- new version 19.4

* Sat Dec 08 2018 Cronbuild Service <cronbuild@altlinux.org> 19.3-alt1
- new version 19.3

* Sun Oct 21 2018 Cronbuild Service <cronbuild@altlinux.org> 19.2-alt1
- new version 19.2

* Tue Sep 18 2018 Cronbuild Service <cronbuild@altlinux.org> 19.1-alt1
- new version 19.1

* Mon Sep 10 2018 Andrey Cherepanov <cas@altlinux.org> 19.0-alt1
- new version 19.0

* Wed Aug 01 2018 Cronbuild Service <cronbuild@altlinux.org> 18.8-alt1
- new version 18.8

* Wed Jun 20 2018 Cronbuild Service <cronbuild@altlinux.org> 18.7-alt1
- new version 18.7

* Fri Jun 08 2018 Cronbuild Service <cronbuild@altlinux.org> 18.6-alt1
- new version 18.6

* Thu May 03 2018 Andrey Cherepanov <cas@altlinux.org> 18.5-alt1
- new version 18.5

* Tue Apr 03 2018 Cronbuild Service <cronbuild@altlinux.org> 18.4-alt1
- new version 18.4

* Sun Mar 04 2018 Cronbuild Service <cronbuild@altlinux.org> 18.3-alt1
- new version 18.3

* Thu Feb 01 2018 Cronbuild Service <cronbuild@altlinux.org> 18.2-alt1
- new version 18.2

* Tue Jan 02 2018 Cronbuild Service <cronbuild@altlinux.org> 18.1-alt1
- new version 18.1

* Thu Nov 30 2017 Cronbuild Service <cronbuild@altlinux.org> 18.0-alt1
- new version 18.0

* Tue Aug 01 2017 Cronbuild Service <cronbuild@altlinux.org> 17.14-alt1
- new version 17.14

* Sun Jul 02 2017 Cronbuild Service <cronbuild@altlinux.org> 17.13-alt1
- new version 17.13

* Fri Jun 02 2017 Cronbuild Service <cronbuild@altlinux.org> 17.12-alt1
- new version 17.12

* Wed May 03 2017 Cronbuild Service <cronbuild@altlinux.org> 17.11-alt1
- new version 17.11

* Mon Apr 03 2017 Cronbuild Service <cronbuild@altlinux.org> 17.10-alt1
- new version 17.10

* Sat Mar 04 2017 Cronbuild Service <cronbuild@altlinux.org> 17.9-alt1
- new version 17.9

* Sun Feb 19 2017 Andrey Cherepanov <cas@altlinux.org> 17.6-alt2
- Prepare for cronbuild
- Use cmake for build
- Simplify spec and package rules

* Tue Jan 03 2017 Andrey Cherepanov <cas@altlinux.org> 17.6-alt1
- new version 17.6

* Sun Dec 11 2016 Andrey Cherepanov <cas@altlinux.org> 17.5-alt1
- new version 17.5

* Fri Dec 02 2016 Andrey Cherepanov <cas@altlinux.org> 17.4-alt1
- new version 17.4

* Tue Nov 01 2016 Andrey Cherepanov <cas@altlinux.org> 17.3-alt1
- new version 17.3

* Sat Oct 01 2016 Andrey Cherepanov <cas@altlinux.org> 17.2-alt1
- new version 17.2

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 17.1-alt1
- new version 17.1

* Thu Sep 01 2016 Andrey Cherepanov <cas@altlinux.org> 17.0-alt1
- new version 17.0

* Tue Aug 02 2016 Andrey Cherepanov <cas@altlinux.org> 16.18-alt1
- new version 16.18

* Sat Jul 16 2016 Andrey Cherepanov <cas@altlinux.org> 16.17-alt1
- new version 16.17

* Thu Jul 14 2016 Andrey Cherepanov <cas@altlinux.org> 16.16-alt1
- new version 16.16

* Fri Jun 10 2016 Andrey Cherepanov <cas@altlinux.org> 16.15-alt1
- new version 16.15

* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 16.14-alt1
- new version 16.14

* Tue May 03 2016 Andrey Cherepanov <cas@altlinux.org> 16.13-alt1
- new version 16.13

* Tue Apr 19 2016 Andrey Cherepanov <cas@altlinux.org> 16.12-alt1
- new version 16.12

* Fri Apr 08 2016 Andrey Cherepanov <cas@altlinux.org> 16.10-alt1
- new version 16.10

* Sat Apr 02 2016 Andrey Cherepanov <cas@altlinux.org> 16.9-alt1
- new version 16.9

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 16.7-alt1
- new version 16.7

* Tue Feb 02 2016 Andrey Cherepanov <cas@altlinux.org> 16.5-alt1
- new version 16.5

* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 16.4-alt1
- new version 16.4

* Wed Dec 02 2015 Andrey Cherepanov <cas@altlinux.org> 16.3-alt1
- new version 16.3

* Thu Oct 08 2015 Andrey Cherepanov <cas@altlinux.org> 16.2-alt1
- new version 16.2

* Fri Oct 02 2015 Andrey Cherepanov <cas@altlinux.org> 16.1-alt1
- new version 16.1

* Tue Sep 01 2015 Andrey Cherepanov <cas@altlinux.org> 16.0-alt1
- new version 16.0

* Sun Aug 02 2015 Andrey Cherepanov <cas@altlinux.org> 15.17-alt1
- new version 15.17

* Sat Jul 25 2015 Andrey Cherepanov <cas@altlinux.org> 15.16-alt1
- new version 15.16

* Thu Jul 09 2015 Andrey Cherepanov <cas@altlinux.org> 15.15-alt1
- new version 15.15

* Fri Jul 03 2015 Andrey Cherepanov <cas@altlinux.org> 15.14-alt1
- new version 15.14

* Tue Jun 16 2015 Andrey Cherepanov <cas@altlinux.org> 15.13-alt1
- new version 15.13

* Fri Jun 12 2015 Andrey Cherepanov <cas@altlinux.org> 15.12-alt1
- new version 15.12

* Fri Jun 05 2015 Andrey Cherepanov <cas@altlinux.org> 15.11-alt1
- new version 15.11

* Sat May 02 2015 Andrey Cherepanov <cas@altlinux.org> 15.10-alt1
- new version 15.10

* Wed Apr 01 2015 Andrey Cherepanov <cas@altlinux.org> 15.9-alt1
- new version 15.9

* Fri Mar 13 2015 Andrey Cherepanov <cas@altlinux.org> 15.8-alt1
- new version 15.8
- move data files to /usr/share/iceB (as hardcoded)

* Wed Mar 04 2015 Andrey Cherepanov <cas@altlinux.org> 15.7-alt1
- new version 15.7

* Fri Feb 20 2015 Andrey Cherepanov <cas@altlinux.org> 15.6-alt1
- new version 15.6

* Wed Jan 21 2015 Andrey Cherepanov <cas@altlinux.org> 15.5-alt1
- new version 15.5

* Fri Jan 02 2015 Andrey Cherepanov <cas@altlinux.org> 15.3-alt1
- new version 15.3

* Tue Dec 02 2014 Andrey Cherepanov <cas@altlinux.org> 15.2-alt1
- New version

* Fri Nov 14 2014 Andrey Cherepanov <cas@altlinux.org> 15.1-alt1
- new version 15.1

* Mon Sep 01 2014 Andrey Cherepanov <cas@altlinux.org> 15.0-alt1
- Nee version

* Mon Jun 02 2014 Andrey Cherepanov <cas@altlinux.org> 14.15-alt1
- New version

* Thu Feb 27 2014 Andrey Cherepanov <cas@altlinux.org> 14.11-alt1
- New version
- Fix project URL

* Sun Apr 07 2013 Andrey Cherepanov <cas@altlinux.org> 12.0-alt3
- Rebuild with new libmysqlclient

* Wed Sep 19 2012 Andrey Cherepanov <cas@altlinux.org> 12.0-alt2
- Fix build

* Thu Sep 01 2011 Andrey Cherepanov <cas@altlinux.org> 12.0-alt1
- New version 12.0

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 9.0-alt1
- build new version, update spec
- disable build html doc

* Fri Jun 18 2004 Sergey V Turchin <zerg at altlinux dot org> 5.60-alt2
- fix menu section

* Tue Feb 03 2004 Sergey V Turchin <zerg at altlinux dot org> 5.60-alt1
- new version

* Tue Sep 30 2003 Sergey V Turchin <zerg at altlinux dot org> 5.35-alt2
- fix build requires

* Fri Sep 13 2002 Sergey V Turchin <zerg@altlinux.ru> 5.35-alt1
- new version
- byuld with gcc3.2

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 5.24-alt2
- add -doc-html package

* Fri Apr 05 2002 Sergey V Turchin <zerg@altlinux.ru> 5.24-alt1
- initial spec
