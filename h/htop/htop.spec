%def_enable openvz
%def_enable unicode
%def_enable taskstats

Name: htop
Version: 3.0.5
Release: alt1

Summary: Interactive ncurses-based process viewer for Linux
License: GPL
Group: Monitoring

Url: http://hisham.hm/htop/
Source0: %name-%version.tar
Source1: %name.ru.1
Patch: htop-3.0.5-alt-colorscheme.patch

BuildRequires: libncursesw-devel
BuildRequires: python3
BuildRequires: /proc
%{?!_with_bootstrap:BuildRequires: ImageMagick-tools}

%define rman1dir %_mandir/ru/man1

Summary(ru_RU.UTF-8): Интерактивный просмотр списка запущенных процессов

%description
%name is similar to top, but allows to scroll the list vertically
and horizontally to see all processes and their full command lines.

Tasks related to processes (killing,  renicing)
can be done without entering their PIDs.

%description -l ru_RU.UTF-8
%name служит для просмотра списка запущенных процессов.
По сравнению с классическим top он усовершенствован следующим образом:

  * если список процессов не влезает в экран по высоте,
    его можно пролистывать вверх/вниз,
  * если информация о процессе не влезает в экран по ширине,
    её можно прокручивать вправо/влево,
  * действия над процессами (смена приоритета, удаление)
    не требуют вручную вводить идентификатор процесса (PID),
  * возможны действия над группами процессов.

htop использует для работы с экраном библиотеку ncurses.

%prep
%setup
%patch -p1

# fix shebang
#sed -i 's|#!/usr/bin/env python|#!/usr/bin/python2|' scripts/MakeHeader.py

%build
%autoreconf
%configure -C \
	%{subst_enable openvz} \
	%{subst_enable unicode} \
	%{subst_enable taskstats}
%make_build

%install
%makeinstall_std
install -pDm644 %SOURCE1 %buildroot%rman1dir/%name.1
install -pDm644 %name.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

%if_with bootstrap
%else
mkdir -p %buildroot%_niconsdir
convert %name.png -resize 32x32 %buildroot%_niconsdir/%name.png
rm -r %buildroot%_pixmapsdir/
%endif

%files
%_bindir/%name
%_man1dir/%name.1*
%rman1dir/%name.1*
%doc AUTHORS README ChangeLog
%_desktopdir/%name.*
%{?!_with_bootstrap:%_niconsdir/%name.*}
%_iconsdir/hicolor/128x128/apps/%name.png

%changelog
* Sat Jan 30 2021 Anton Midyukov <antohami@altlinux.org> 3.0.5-alt1
- new version 3.0.5

* Wed Sep 02 2020 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- New version

* Sat May 02 2020 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt2
- fix shebang to /usr/bin/python2

* Sun Dec 30 2018 Michael Shigorin <mike@altlinux.org> 2.2.0-alt1
- new version (watch file uupdate)
- buildreq

* Fri Dec 28 2018 Ivan A. Melnikov <iv@altlinux.org> 2.1.0-alt2
- set default color scheme to Broken Gray (closes: #35252)

* Mon Feb 05 2018 Michael Shigorin <mike@altlinux.org> 2.1.0-alt1
- new version (watch file uupdate)

* Sat Dec 24 2016 Michael Shigorin <mike@altlinux.org> 2.0.2-alt2
- BOOTSTRAP: minimal build can cope without IM indeed

* Tue Jul 26 2016 Michael Shigorin <mike@altlinux.org> 2.0.2-alt1
- new version (watch file uupdate)

* Wed Mar 09 2016 Michael Shigorin <mike@altlinux.org> 2.0.1-alt1
- new version (watch file uupdate)

* Thu Feb 11 2016 Michael Shigorin <mike@altlinux.org> 2.0.0-alt1
- new version (watch file uupdate)

* Sun Aug 16 2015 Michael Shigorin <mike@altlinux.org> 1.0.3-alt2
- fixed 128px icon path, added proper 32px icon path
  (thanks shadowsbrother@ for spotting this)

* Thu Aug 28 2014 Michael Shigorin <mike@altlinux.org> 1.0.3-alt1
- new version (watch file uupdate)
- enabled OOM score support (closes: #30245)
- converted spec to UTF-8

* Wed Feb 20 2013 Michael Shigorin <mike@altlinux.org> 1.0.2-alt1
- new version (watch file uupdate)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 1.0.1-alt2
- added watch file

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Nov 23 2011 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- 1.0 (thx led@ for a hint)

* Sat Jun 25 2011 Michael Shigorin <mike@altlinux.org> 0.9-alt1
- 0.9

* Sat Aug 01 2009 Michael Shigorin <mike@altlinux.org> 0.8.3-alt4
- IconPathsPolicy alignment (repocop)

* Wed Jul 29 2009 Michael Shigorin <mike@altlinux.org> 0.8.3-alt3
- applied repocop patch
- added missing Additional Category to desktop file
- added Packager:

* Tue Jun 30 2009 Michael Shigorin <mike@altlinux.org> 0.8.3-alt2
- 0.8.3 (closes: #20594)
  + 0.8.2: integration with lsof to list files opened by a process
  + NB: "VEID" column got renamed to "CTID"
- spec cleanup and macro optimization
- replaced autohack with proper BR: /proc
- alt2: merged 0.8.3-alt1 by Ilya (see also #20594)

* Tue Jun 30 2009 Ilya Evseev <evseev@altlinux.ru> 0.8.3-alt1
- updated to new version 0.8.3

* Sat Sep 27 2008 Ilya Evseev <evseev@altlinux.ru> 0.8.1-alt1
- updated to new version 0.8.1

* Sat May 31 2008 Ilya Evseev <evseev@altlinux.ru> 0.8-alt2
- support for unicode and taskstats: enable by default

* Sat May 31 2008 Ilya Evseev <evseev@altlinux.ru> 0.8-alt1
- updated to new version 0.8

* Thu Jan 10 2008 Ilya Evseev <evseev@altlinux.ru> 0.7-alt1
- updated to new version 0.7
- apply specfile patch by mike@ from bugzilla #13519: see below...
- NMU:
  + CPU affinity configuration
  + improved process organization in tree view
  + OpenVZ support
  + bugfixes
- spec macro abuse cleanup
- replace Debian menufile with freedesktop.org desktop file

* Mon Jun 25 2007 Ilya G. Evseev <evseev@altlinux.ru> 0.6.6-alt1
- updated to version 0.6.6

* Mon Jan 22 2007 Ilya G. Evseev <evseev@altlinux.ru> 0.6.5-alt1
- updated to version 0.6.5

* Sat Oct 07 2006 Ilya G. Evseev <evseev@altlinux.ru> 0.6.4-alt1
- updated to version 0.6.4

* Fri Aug 25 2006 Ilya G. Evseev <evseev@altlinux.ru> 0.6.3-alt1
- updated to version 0.6.3

* Wed May 24 2006 Ilya G. Evseev <evseev@altlinux.ru> 0.6.2-alt1
- updated to version 0.6.2

* Fri May 12 2006 Ilya G. Evseev <evseev@altlinux.ru> 0.6.1-alt1
- updated to version 0.6.1
- closed bug #8830 (fixed in upstream)
- specfile changes:
   + docfiles list (missed TODO)
   + GUI icon

* Thu Dec 29 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.6-alt1
- updated to version 0.6

* Tue Nov  1 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.5.4-alt1
- updated to version 0.5.4

* Fri Sep 23 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.5.3-alt2
- bugfix: prevent /proc things at confugure stage because hasher
  (ALTLinux build environment) does not provide /proc filesystem

* Wed Sep 21 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.5.3-alt1
- updated to version 0.5.3

* Wed May 18 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.5.2-alt1
- updated to version 0.5.2

* Sun Apr 10 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.5.1-alt1
- updated to version 0.5.1

* Fri Dec  3 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.5-alt1
- version 0.5
- russian manual page updated to actual state

* Wed Aug 25 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.4-alt1
- upgrade to 0.4

* Thu Jul  1 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.3.3-alt3
- multiple specfile fixes for compatibility with ALTLinux SpecFile conventions:
- fixed build numbering
- russian texts in UTF-8 are moved beyound first 256-bytes block
- more small things...

* Wed Jun 30 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.3.3-2alt
- fixed invalid BuildPreReq
- manage menu entry

* Mon Jun 28 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.3.3-1alt
- Upgrade to 0.3.3
- Added russian manpage

* Fri Jun  4 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.3.1-1alt
- Initial build

## EOF ##
