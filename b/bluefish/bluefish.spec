Name: bluefish
Version: 2.2.11
Release: alt1

Summary: A GTK3 web development application for experienced users

Serial: 2

Url: http://bluefish.openoffice.nl
License: GPL-3.0-or-later
Group: Editors

Source: %name-%version.tar.bz2

# Fedora patchs
# Avoid potential aliasing issues in zencoding plugin
Patch0: bluefish-2.2.10-strict-aliasing.patch

# Avoid use of /usr/bin/env in shipped scripts
# Also change /usr/bin/python → /usr/bin/python2 (for now)
Patch1: bluefish-2.2.11-shellbang.patch

# Strip all python content if we don't have Python
Patch2: bluefish-2.2.11-no-python.patch

Requires: bluefish-common = %serial:%version-%release

BuildRequires: intltool
BuildRequires: libgtk+3-devel
BuildRequires: libgucharmap-devel
BuildRequires: libxml2-devel
BuildRequires: libenchant-devel
BuildRequires: libappstream-glib

%description
Bluefish is a powerful editor for experienced web designers and programmers.
Bluefish supports many programming and markup languages, but it focuses on
editing dynamic and interactive websites

%package common
Summary: Common files for Bluefish
Group: Editors
BuildArch: noarch
Serial: 2

%description common
Bluefish is a powerful editor for experienced web designers and programmers.
These are common files.

%prep
%setup
#for N in src/plugin_*/po; do ln -s /usr/share/intltool/Makefile.in.in $N/;done
#for N in src/plugin_*/po; do test -r $N/Makefile.in.in && echo $N || ln -s /usr/share/intltool/Makefile.in.in $N/;done
find data -type f -name \*.py -exec sed -i 's/\r//' {} \;

%patch0
%patch1
%patch2

%build
#autoreconf
%configure --disable-update-databases --disable-xml-catalog-update
%make_build

%install
# No makeinstall macros here, because of hardcoded DESTDIR-only
make install DESTDIR=%buildroot

# Unpackaged files
rm %buildroot%_libdir/%name/*.la

%find_lang %name
for c in `echo src/plugin_*`; do
  %find_lang %{name}_`basename $c`
done
cat %{name}_plugin_*.lang >> %name.lang

%files
%_bindir/*
%_libdir/%name

%files common -f %name.lang
%exclude %_defaultdocdir/%name
%doc data/bflang/sample.bflang2 AUTHORS COPYING ChangeLog README TODO
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/pixmaps/*
%_datadir/applications/*
%_datadir/appdata/%name.appdata.xml
%_datadir/mime/packages/*
%_iconsdir/hicolor/*/*/*.??g
%_man1dir/*
%dir %_datadir/xml/%name
%_datadir/xml/%name/*

%changelog
* Sat May 23 2020 Anton Midyukov <antohami@altlinux.org> 2:2.2.11-alt1
- New version 2.2.11
- build with gtk3
- disable python support

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 2:2.2.9-alt1
- Autobuild version bump to 2.2.9

* Wed Feb 11 2015 Fr. Br. George <george@altlinux.ru> 2:2.2.7-alt1
- Autobuild version bump to 2.2.7

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 2:2.2.6-alt1
- Autobuild version bump to 2.2.6

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 2:2.2.5-alt1
- Autobuild version bump to 2.2.5

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 2:2.2.4-alt1
- Autobuild version bump to 2.2.4
- Fix DOS LFs

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 2:2.2.3-alt1
- Autobuild version bump to 2.2.3

* Wed Mar 21 2012 Fr. Br. George <george@altlinux.ru> 2:2.2.2-alt1
- Autobuild version bump to 2.2.2

* Tue Dec 27 2011 Fr. Br. George <george@altlinux.ru> 2:2.2.1-alt2
- Translation fixed

* Tue Dec 27 2011 Fr. Br. George <george@altlinux.ru> 2:2.2.1-alt1
- Autobuild version bump to 2.2.1

* Fri Sep 23 2011 Fr. Br. George <george@altlinux.ru> 2:2.0.3-alt3
- Rebuild with libgucharmap req

* Mon Jun 20 2011 Fr. Br. George <george@altlinux.ru> 2:2.0.3-alt2
- Rebulid with manual gtk+2 buildreq

* Thu Mar 31 2011 Fr. Br. George <george@altlinux.ru> 2:2.0.3-alt1
- Versiob up
- Upgrade serial due to ALT package versioning policy violation

* Wed Jan 13 2011 Alex Negulescu <alecs@altlinux.org> 1:2.0.3rc1-alt2
- marked language specific files (http://www.altlinux.org/FindLangPolicy)

* Wed Jan 12 2011 Alex Negulescu <alecs@altlinux.org> 1:2.0.3rc1-alt1
- version up
- moved architecture-independent data to bluefish-common & other minor spec changes

* Mon Sep 20 2010 Fr. Br. George <george@altlinux.ru> 1:2.0.2-alt1
- Version up

* Mon Jul 19 2010 Fr. Br. George <george@altlinux.ru> 1:2.0.1.6001-alt1
- Update to svn r6001

* Sat Jul 17 2010 Fr. Br. George <george@altlinux.ru> 1:2.0.1-alt2
- Version up
- Synchronized with upstream FC spec

* Fri Dec 11 2009 Fr. Br. George <george@altlinux.ru> 1:1.0.7-alt2
- Remove WYSIWYG from description (closes #22254)
- Manpage found

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1:1.0.7-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for bluefish
  * postclean-05-filetriggers for spec file

* Sat Apr 12 2008 Fr. Br. George <george@altlinux.ru> 1:1.0.7-alt1
- Version up

* Sat Apr 12 2008 Fr. Br. George <george@altlinux.ru> 1:1.0.5-alt1.2
- Adopted from orphaned

* Wed Mar 01 2006 Stanislav Ievlev <inger@altlinux.org> 1:1.0.5-alt1.1
- remove qt4 from buildreqs (was buildreq bug)

* Mon Feb 27 2006 Stanislav Ievlev <inger@altlinux.org> 1:1.0.5-alt1
- 1.0.5 , fixed icons path

* Tue Jan 25 2005 Stanislav Ievlev <inger@altlinux.org> 1:1.0-alt1
- 1.0

* Mon Apr 12 2004 Stanislav Ievlev <inger@altlinux.org> 1:0.13-alt1
- 0.13
  TODO: add provides to aspell-dictionary when aspell will be fixed

* Tue Dec 02 2003 Stanislav Ievlev <inger@altlinux.org> 1:0.12-alt1
- 0.12

* Fri Aug 29 2003 Stanislav Ievlev <inger@altlinux.ru> 1:0.11-alt1
- 0.11

* Thu Mar 06 2003 Stanislav Ievlev <inger@altlinux.ru> 1:0.9-alt1
- 0.9

* Thu Jan 16 2003 Stanislav Ievlev <inger@altlinux.ru> 1:0.8-alt2
- changed in menu location

* Thu Jan 09 2003 Stanislav Ievlev <inger@altlinux.ru> 1:0.8-alt1
- move from CVS to stable version. 0.8

* Tue Oct 15 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.7-alt0.4.gtk2port.20020926
- fixed paths

* Wed Oct 09 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.7-alt0.3.gtk2port.20020926
- rebuild with gtk2.1

* Thu Sep 26 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.7-alt0.2.gtk2port.20020926
- move to gtk2 port
- snapshot at 20020926

* Fri Nov 16 2001 AEN <aen@logic.ru> 0.7-alt0.1
- new code from CVS

* Thu Oct 11 2001 AEN <aen@logic.ru> 0.6-alt1
- rebuilt with libpng.so.3
- Serial -> 1

* Fri Apr 6 2001 AEN <aen@logic.ru> 0.6-ipl2mdk
- ru.po fixed
* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE adaptations

* Sun Dec 24 2000  Daouda Lo <daouda@mandrakesoft.com> 0.6-1mdk
- release
- patch should be applied with -p1
- more translations (br, hu, pl)
- many bug fixes

* Mon Nov 27 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.5-8mdk
- gtk+-devel ! gtk+ for buildrequires (isuck).

* Mon Nov 27 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.5-7mdk
- add gtk+ as buildrequires as asked by Dadou.

* Sat Oct 07 2000 Daouda Lo <daouda@mandrakesoft.com> 0.5-6mdk
- fix icons

* Sun Oct 01 2000 David BAUDENS <baudens@mandrakesoft.com> 0.5-5mdk
- Use optimizations
- Fix Summary and Description
- Fix group and menu entry

* Tue Sep 26 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.5-4mdk
- shrink the icon.

* Fri Aug 25 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5-3mdk
- fix menu entry (reported by Guillaume Rousse)
- update menu entry version

- uses find_lang for locale files
- moved configure call to build section
- fixed english locale file

* Thu Aug 24 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.5-1mdk
- _menudir.
- update menus and clean menus macro.
- a very new and shiny version.

* Tue Aug 22 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.4-2mdk
- BM
- macros

* Tue May 16 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.4-1mdk
- fix install of pixmaps
- used srpm provided by Geoffrey Lee <snailtalk@linux-mandrake.com>

* Fri Apr 28 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 0.3.6-2mdk
- minor change to description, the best html editor is cat and ^D ;-)
- URL for it
- add url for source
- change location of file, stuff shouldn't go in /usr/local

* Wed Apr 26 2000 Daouda Lo <daouda@mandrakesoft.com> 0.3.6-1mdk
- release.
- SMP build check.
- package should be relocatable
- add menu entry with icon.

* Tue Apr 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.2-2mdk
- fix group

* Tue Sep  7 1999 Daouda LO <daouda@mandrakesoft.com> 0.3.2-1mdk
- First spec file for Mandrake distribution.
-Mandrake Adaptations
