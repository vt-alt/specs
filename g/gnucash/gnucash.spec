%set_verify_elf_method unresolved=relaxed

# TODO:fix build Python bindings
%def_enable python
%def_with aqbanking

Name: 	 gnucash
Version: 3.903
Release: alt1

Summary: GnuCash is an application to keep track of your finances
Summary(ru_RU.UTF8): Программа учёта финансов GnuCash

License: GPL-2.0+
Group:   Office
Url: 	 http://www.gnucash.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %name-%version.tar
Source1: gtest.tar
Source2: %name.1
Source3: gnc-vcs-info.h
Source4: ChangeLog
Source5: %name-README.RU
Source7: conv_gnucash2.sh
Source8: gnucash.appdata.xml.in
Source9: gnucash.desktop.in

Patch2: %name-alt-fix-rpath.patch

AutoReq: yes, noperl

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libgtk+3-devel
BuildRequires: doxygen graphviz guile-devel intltool libglade-devel
BuildRequires: libgwenhywfar-devel libgwenhywfar-gtk3
BuildRequires: libofx-devel libreadline-devel slib-guile
BuildRequires: libdconf-devel
BuildRequires: libdbi-devel
BuildRequires: libdbi-drivers-devel
BuildRequires: libdbi-drivers-dbd-sqlite3
BuildRequires: libdbi-drivers-dbd-mysql
BuildRequires: libdbi-drivers-dbd-pgsql
BuildRequires: swig
BuildRequires: libexpat-devel
BuildRequires: libffi-devel
BuildRequires: libpcre-devel
BuildRequires: libpixman-devel
BuildRequires: libdrm-devel
BuildRequires: libsecret-devel
BuildRequires: xsltproc
BuildRequires: zlib-devel
BuildRequires: libxslt-devel
BuildRequires: boost-locale-devel boost-filesystem-devel boost-program_options-devel
%if_with aqbanking
BuildRequires: aqbanking-devel
%endif
BuildRequires: libgmock-devel libgtest-devel
BuildRequires: libwebkit2gtk-devel
%if_enabled python
BuildRequires: python3-devel
%endif
BuildRequires: perl-podlators
BuildRequires: perl-Date-Manip
BuildRequires: /proc

Requires: %{name}-program = %EVR
Requires: %{name}-quotes = %EVR
Requires: %{name}-docs
Requires: slib-guile
Requires: dconf

%description
GnuCash is a personal finance manager. A check-book like
register GUI allows you to enter and track bank accounts,
stocks, income and even currency trades. The interface is
designed to be simple and easy to use, but is backed with
double-entry accounting principles to ensure balanced books.

%description -l ru_RU.UTF8
GnuCash -- это личный финансовый менеджер. Книга учёта
в виде журнала на экране позволит вам вводить и отслеживать
состояние банковских счетов, ценных бумаг, приход денег и
даже курсы валют. Интерфейс программы разработан простым и
лёгким в использовании, но в то же время применяется
принцип двойной записи для обеспечения сведения баланса.

%package program
Summary: Program of GnuCash
Summary(ru_RU.UTF8): GnuCash (программа)
Group: Office
Requires: lib%name = %EVR

%description program
Executable files of GnuCash without documentation.

%description program -l ru_RU.UTF8
Исполняемые файлы GnuCash без документации.

%package -n lib%name-devel
Group: Development/C
Summary: Libraries needed to develop for gnucash
Summary(ru_RU.UTF8): Библиотеки, требуемые для разработки с gnucash
Requires: lib%name = %version
Obsoletes: %name-devel

%description -n lib%name-devel
Libraries needed to develop for gnucash.
%description -n lib%name-devel -l ru_RU.UTF8
Библиотеки, требуемые для разработки с gnucash.

%package -n lib%name
Summary: Libraries for gnucash (sql backends too).
Group: System/Libraries

%add_findprov_lib_path %_libdir/%name

%description -n lib%name
This package provides libraries to use gnucash.

%description -n lib%name -l ru_RU.UTF8
Пакет предоставляет библиотеки, используемые gnucash.

%package quotes
Summary: Allow GnuCash to fetch quotes
Group: Office
Requires: %name
Requires: perl-Date-Manip perl-Finance-Quote

%description quotes
Virtual package that install needed perl modules for quote's online
fetch and update.

%prep
%setup
%patch2 -p1
tar xf %SOURCE1
cp %SOURCE2 doc
cp %SOURCE3 libgnucash/core-utils
cp %SOURCE4 .
cp %SOURCE8 gnucash/gnome
cp %SOURCE9 gnucash/gnome

%build
%cmake -GNinja \
%if_without aqbanking
       -DWITH_AQBANKING=OFF \
%endif
       -DCMAKE_C_FLAGS="-DGLIB_DISABLE_DEPRECATION_WARNINGS" \
       -DCMAKE_CXX_FLAGS="-DGLIB_DISABLE_DEPRECATION_WARNINGS" \
       -DCMAKE_SKIP_RPATH=OFF \
       -DCMAKE_SKIP_INSTALL_RPATH=OFF \
       -DCMAKE_INSTALL_RPATH:DIR=%_libdir/%name \
       -DGENERATE_SWIG_WRAPPERS=ON \
       -DGMOCK_ROOT=%_builddir/%name-%version/gtest \
       -DGTEST_ROOT=%_builddir/%name-%version/gtest
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

mv %buildroot%_libdir/lib* %buildroot%_libdir/gnucash/

rm -rf %buildroot%_bindir/gnucash-valgrind \
       %buildroot%_libexecdir/%name/src/

%find_lang %name --with-gnome

install -m755 %SOURCE7 %buildroot%_bindir/conv_gnucash2.sh

tar cfJ ChangeLog.tar.xz ChangeLog{,.????}

rm -f %buildroot%_datadir/gnucash/gnome \
      %buildroot%_bindir/gnc-test-env \
      %buildroot%_bindir/gnc-fq-update \
      %buildroot%_datadir/glib-2.0/schemas/gschemas.compiled

rm -rf %buildroot%_datadir/guile/site/*/tests \
       %buildroot%_libdir/guile/*/site-ccache/tests

%files

%files -n lib%name-devel
%_includedir/%name/

%files -n lib%name
%dir %_libdir/%name/
%_libdir/%name/lib*.so

# hbci отдельно
#%exclude %_libdir/%name/libgncmod-hbci*

%files program -f %name.lang
%doc AUTHORS ChangeLog.tar.xz HACKING NEWS README*
%doc doc/README.* doc/examples
%doc %_defaultdocdir/%name/
%_bindir/*
%config %_sysconfdir/%name
%_datadir/guile/site/*/%name
%_libdir/guile/*/site-ccache/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%doc %_man1dir/*
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/metainfo/%name.appdata.xml
%_datadir/glib-2.0/schemas/org.%name.*.xml

#hbci отдельно
#%exclude %_datadir/%name/glade/hbci*

%files quotes

%changelog
* Tue Jun 02 2020 Andrey Cherepanov <cas@altlinux.org> 3.903-alt1
- New version.
- Build with python bindings.
- Package examples.

* Sun May 24 2020 Andrey Cherepanov <cas@altlinux.org> 3.902-alt3
- Use rpm-build-ninja for build.

* Sat May 23 2020 Andrey Cherepanov <cas@altlinux.org> 3.902-alt2
- Use rpm-macros-ninja-build instead of monolite ninja-build.

* Wed May 20 2020 Andrey Cherepanov <cas@altlinux.org> 3.902-alt1
- New version.
- Build using ninja.

* Sun Apr 12 2020 Andrey Cherepanov <cas@altlinux.org> 3.10-alt1
- New version.
- Fix License tag according to SPDX.

* Mon Apr 06 2020 Andrey Cherepanov <cas@altlinux.org> 3.9-alt1
- New version.

* Thu Mar 05 2020 Andrey Cherepanov <cas@altlinux.org> 3.8-alt1
- New version.
- Build directly from upstream tag.

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 3.7-alt2
- NMU: use buildreq libdbi-drivers-dbd-sqlite3 for sqlite
- disable python bindings

* Mon Oct 14 2019 Andrey Cherepanov <cas@altlinux.org> 3.7-alt1
- New version.

* Mon Jul 01 2019 Andrey Cherepanov <cas@altlinux.org> 3.6-alt1
- New version.

* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 3.5-alt1
- New version.

* Thu Jan 03 2019 Andrey Cherepanov <cas@altlinux.org> 3.4-alt1
- New version.

* Mon Oct 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.3-alt1
- New version.

* Mon Jul 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2-alt2
- NMU: rebuilt with boost-1.67.0

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- New version

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1-alt1.1
- NMU: rebuilt with boost-1.67.0

* Mon May 21 2018 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- New version.
- Make subpackage gnucash for program files without documentation. gnucash
  is now the metapackage and it requires gnucash-docs (ALT #21478).

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.0-alt1
- New version.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 2.6.20-alt1
- New version.

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.6.19-alt3
- Rebuild with libgwenhywfar-4.20.0.

* Tue Feb 20 2018 Andrey Cherepanov <cas@altlinux.org> 2.6.19-alt2
- Rebuild with libgwenhywfar 4.19.0.

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.19-alt1
- New version.

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.18-alt2
- Rebuilt with libdbi-0.9.0.

* Mon Oct 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.18-alt1
- New version

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.17-alt1
- New version

* Sun Mar 26 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.16-alt1
- New version

* Wed Dec 21 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.15-alt1
- New version

* Thu Nov 10 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.14-alt1
- New version

* Tue Jul 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.13-alt1
- New version

* Mon May 02 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.12-alt2
- Rebuild with new aqbanking

* Tue Apr 19 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.12-alt1
- New version

* Sun Jan 17 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.11-alt1
- New version

* Sat Jan 02 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.10-alt1
- New version

* Mon Oct 12 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.9-alt1
- New version

* Wed Sep 30 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.8-alt1
- New version

* Fri Jul 03 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.7-alt1
- New version

* Thu Apr 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.6-alt1
- New version

* Mon Jan 12 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version
- Fix License

* Sat Oct 04 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- New version

* Fri Apr 11 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.3-alt1
- New version

* Mon Mar 24 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.2-alt1
- New version
- Fix check for build python bindings

* Thu Jan 30 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version
- Replace GConf2 bt dconf

* Thu Jan 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version
- Use aqbanking
- Remove redundant binaries and registration of GConf schemas

* Sun Nov 24 2013 Andrey Cherepanov <cas@altlinux.org> 2.4.13-alt1
- New version
- Build with libofx-0.9.9

* Sun Apr 08 2012 Alexey Morsov <swi@altlinux.ru> 2.4.10-alt1
- new version

* Fri Jan 13 2012 Andrey Cherepanov <cas@altlinux.org> 2.4.8-alt2
- Remove libgsf-gnome support (no more gnome-vfs/bonobo support in libgsf)

* Mon Nov 07 2011 Alexey Morsov <swi@altlinux.ru> 2.4.8-alt1
- new version
- fix postgresql9 devel package name

* Mon Sep 12 2011 Alexey Morsov <swi@altlinux.ru> 2.4.7-alt1
- new version

* Sun Mar 20 2011 Alexey Morsov <swi@altlinux.ru> 2.4.4-alt1
- new version
- add zlib-devel

* Sat Mar 12 2011 Alexey Morsov <swi@altlinux.ru> 2.4.3-alt1
- new version

* Fri Feb 11 2011 Alexey Morsov <swi@altlinux.ru> 2.4.2-alt1
- new version

* Tue Jan 11 2011 Alexey Morsov <swi@altlinux.ru> 2.4.0-alt2.1
- clean spec
- build with sql backends

* Tue Jan 11 2011 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt2
- add virtual package for quotes fetching
- fix perl module name (thanks Alexey Morsov)

* Fri Jan 07 2011 Alexey Morsov <swi@altlinux.ru> 2.4.0-alt1
- new version
- spec clean up
- remove unneeded patches

* Thu Apr 22 2010 Andrey Cherepanov <cas@altlinux.org> 2.2.9-alt4
- fix requirements for build in Sisyphus

* Sun Sep 20 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2.9-alt3
- restore post/postun for gconf (fix bug #21627)

* Sun Sep 20 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2.9-alt2
- build with guile18
- fix build with goffice

* Thu May 21 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2.9-alt1
- new version 2.2.9 (with rpmrb script)

* Thu Dec 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.7-alt2
- rebuild with new libofx 0.9.0
- remove post/postun sections
- fix files listed twice

* Sat Oct 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.7-alt1
- new version 2.2.7 (with rpmrb script)
- update buildreqs

* Tue Sep 09 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.6-alt1
- new version 2.2.6 (with rpmrb script)

* Thu Jul 31 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.5-alt2
- rebuild with libgnomeoffice 0.7
- add install/uninstall_info

* Thu May 15 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.5-alt1
- new version 2.2.5 (with rpmrb script)

* Thu Apr 03 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt2
- really fix filenames handling (bug #14694)

* Sat Mar 08 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt1
- new version 2.2.4 (with rpmrb script)
- fix gconf schemas installing (thanks to Yury Aliaev)

* Thu Feb 28 2008 Yury Aliaev <mutabor@altlinux.ru> 2.2.3-alt2
- fixed filenames handling in non-utf8 locales

* Tue Jan 22 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- new version 2.2.3 (with rpmrb script)
- use new icons from tarball

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt1
- build release 2.2.2
- rebuild with libgnomeoffice 0.6

* Tue Dec 11 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt0.1svn
- build from svn r16633
- rebuild with libgnomeoffice 0.5
- cleanup spec

* Fri Sep 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version 2.2.1 (with rpmrb script)

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Sat Jun 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version 2.1.3 (with rpmrb script)
- rebuild with new libgnomeoffice 0.4

* Sun Apr 29 2007 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)
- bzip Changelogs

* Thu Apr 19 2007 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- new version 2.1 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version 2.0.5 (with rpmrb script)

* Fri Dec 29 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt0.2
- build with external qof

* Sat Dec 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt0.1
- new version 2.0.3 (with rpmrb script)

* Sat Dec 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1.1
- rebuild with internal libgnomeoffice

* Wed Oct 18 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- update buildreq

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt0.1
- new version 2.0.2 (with rpmrb script)

* Sun Jul 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new stable release 2.0.0 (fix bug #9823))
- add missed libdir/gnucash

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1svn20060521
- new build from SVN (r14146)

* Fri May 12 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1svn20060512
- new build from SVN (r14029)

* Fri Apr 14 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1svn20060414
- new build from SVN (r13773)
- double make for build error workaround

* Mon Jan 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1svn20060123
- new build from SVN (r12926), russian translation updated
- NOTE: convert your old gnucash files with conv_gnucash2.sh script

* Wed Dec 01 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1cvs20041201
- first build with GNOME2 (for developing purposes ONLY)
- use a macro for ldconfig

* Sun May 23 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.9-alt2
- build with rebuilt gnome1 libraries
- remove python requiring

* Wed Apr 28 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.9-alt1
- new version
- applied full diff patch from debian unstable (due dlopen problem)

* Wed Jan 14 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt3
- update ru.po
- move .so files from -devel to libgnucash for dynamic linking purposes
- change require python to universal way (without version)
- remove COPYING from doc

* Sat Jan 03 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt2
- build without *.la files
- build with gcc3.3
- disable guppi support

* Thu Dec 04 2003 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt1
- new version
- build with Guppi
- add autostart gconfd-1 before gnucash in start script

* Mon Oct 06 2003 Vitaly Lipatov <lav@altlinux.ru> 1.8.7-alt1
- new version
- disable autoreq for perl and set it manually

* Sun Jun 22 2003 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- new version

* Mon Mar 24 2003 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- new version
- postgres backend enabled
- update russian translation

* Sun Jan 26 2003 Vitaly Lipatov <lav@altlinux.ru> 1.7.8-alt1
- new version

* Mon Jan 06 2003 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- new version
- Warning: Be careful with RUB currency (use RUR instead) in your file.
- update russian translation
- postgres disabled via build problems
- add needed binaries in file section
- add README_koi8-r.txt
- cleanup spec

* Sat Dec 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- gnucash-devel rename to libgnucash-devel
- spec cleanup
- add Postgres support package (untested)
- new version
- update ru.po

* Mon Nov 04 2002 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt2
- remove dependences on libtermcap
- update russian translation

* Fri Nov 01 2002 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version
- spec updated

* Mon Feb 18 2002 AEN <aen@logic.ru> 1.6.5-alt3
- ru.po updates from Vitaly Lipatov

* Tue Jan 22 2002 AEN <aen@logic.ru> 1.6.5-alt2
- rebuilt with new Guppi

* Mon Jan 14 2002 AEN <aen@logic.ru> 1.6.5-alt1
- new version

* Wed Dec 05 2001 AEN <aen@logic.ru> 1.6.4-alt5
- rebuilt with gtkhtml-1.0.0

* Wed Nov 21 2001 AEN <aen@logic.ru> 1.6.4-alt4
- rebuild with libguppi-0.40.2

* Fri Nov 09 2001 AEN <aen@logicru> 1.6.4-alt3
- rebuilt with new gal

* Thu Nov 1 2001 AEN <aen@logic.ru> 1.6.4-alt2
- rebuild in new environment

* Fri Oct 12 2001 AEN <aen@logic.ru> 1.6.4-alt1
- new version

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation

* Tue Oct 24 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.8-1mdk
- new version 1.4.8
- added buildconflicts with libxml2-devel

* Mon Oct  9 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.7-2mdk
- added /usr/lib/gnucash/perl/* library files
- added la files in devel
- added man pages
- added requirement in devel
- gnucash.so is needed in the *normal* package because of swig
- moved libgncengine.so from devel to normal, just in case...

* Mon Oct  2 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.7-1mdk
- new version

* Tue Sep 12 2000  <rchaillat@bi.mandrakesoft.com> 1.4.6-1mdk
- new version

* Thu Aug 31 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.5-2mdk
- added comment about g-wrap
- added menu file

* Wed Aug 30 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.4.5-1mdk
- went back to stable releases
- macroszification
- corrected icons
- added some more BuildRequires (xpm, guile-devel)
- specfile clean-up
- split application and devel packages

* Fri Jul 21 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.5.0-1mdk
- Updated version

* Tue Jul 11 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.4.2-3mdk
- Repaired missing libs

* Mon Jul 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.4.2-1mdk
- Updated version / release 2 hours ago.

* Sat Jul 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.4.1-1mdk
- Updated version

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.1-5mdk
- Give full path when using convert.
- BuildPrereq: /usr/bin/convert.
- Regenerate libtoolize everywhere there is a configure.
- BuildRequires: eperl swig.

* Mon Apr 10 2000 Francis Galiegue <fg@mandrakesoft.com> 1.3.1-4mdk

- Patched to compile with perl 5.6.0

* Wed Mar 22 2000 Francis Galiegue <fg@mandrakesoft.com> 1.3.1-3mdk

- Icon for menu entry
- Rebuilt on kenobi

* Mon Mar 13 2000 Francis Galiegue <francis@mandrakesoft.com> 1.3.1-2mdk

- Menu'ized, changed group to Office (was: Applications/Finance)

* Mon Mar 13 2000 Francis Galiegue <francis@mandrakesoft.com>

- First RPM for Mandrake

* Tue Feb 29 2000 Christian Schaller <Uraues@linuxrising.org>
- Updated for use with TurboLinux and some minor SPEC changes
