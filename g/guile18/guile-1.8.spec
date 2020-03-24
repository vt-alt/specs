%define iname guile
%define sversion 1.8

%set_automake_version 1.11

Name: %{iname}18
Version: %sversion.7
Release: alt8
Epoch: 1

Summary: A GNU implementation of Scheme for application extensibility
License: LGPL-2.1-or-later
Group: Development/Scheme
Url: http://www.gnu.org/software/guile/

Source: ftp://alpha.gnu.org/gnu/%iname/%iname-%version.tar

Patch0: guile18-snarf-check-and-output-texi.scm.patch
Patch2: guile-1.8.7-testsuite.patch
Patch3: guile-1.8.7-testsuite2.patch
Patch4: guile-1.8.7-mkdir-umask.patch
Patch5: guile-1.8.7-overflow.patch
Patch6: guile-2.0.2-fix-read-beyond-end-of-hashtable-size-array-in-hasht.patch

BuildRequires: libgmp-devel libltdl-devel libncurses-devel libreadline-devel
BuildRequires: /proc /dev/pts

%add_findreq_skiplist %_datadir/%iname/%sversion/scripts/*

%description
GUILE (GNU's Ubiquitous Intelligent Language for Extension) is a library
implementation of the Scheme programming language, written in C.  GUILE
provides a machine-independent execution platform that can be linked in
as a library during the building of extensible programs.

%package devel
Summary: A GNU implementation of Scheme for application extensibility
Group: Development/Scheme
Requires: %name = %EVR
Requires: libgmp-devel
Conflicts: guile14-devel guile16-devel

%description devel
GUILE (GNU's Ubiquitous Intelligent Language for Extension) is a library
implementation of the Scheme programming language, written in C.  GUILE
provides a machine-independent execution platform that can be linked in
as a library during the building of extensible programs.

Install this package if you are going to develop extendable programs.

%prep
%setup -n %iname-%version
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%__subst -p 's/^libguile_la_LDFLAGS = .*/& $(GUILE_CFLAGS)/' libguile/Makefile*

%build
%add_optflags -fwrapv
%autoreconf

%configure --with-threads --enable-error-on-warning=no --disable-static
#NO SMP
%make

%install
#export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%_libdir
#make install DESTDIR=$RPM_BUILD_ROOT LDFLAGS=-L$RPM_BUILD_ROOT%_libdir
%makeinstall
#alternatives stuff
mv %buildroot%_bindir/%iname %buildroot%_bindir/%name
mv %buildroot%_man1dir/%iname.1 %buildroot%_man1dir/%name.1
sed -i '/^#!/ s,guile[[:blank:]],%name ,' %buildroot%_bindir/guile-config

%check
make check

%files
%_bindir/%name
%dir %_datadir/%iname
%dir %_datadir/%iname/%sversion
%_libdir/lib*.so.*
%_libdir/lib%iname?*.so
%_datadir/%iname/%sversion/*
%_mandir/man1/%name.1.*

%files devel
%_bindir/%iname-snarf
%_bindir/%iname-config
%_bindir/%iname-tools
%_libdir/lib%iname.so
%_includedir/*
%_datadir/aclocal/*
%_datadir/info/*.info*
%_libdir/pkgconfig/%iname-%sversion.pc

%changelog
* Tue Mar 17 2020 Ivan Zakharyaschev <imz@altlinux.org>  1:1.8.7-alt8
- Fixes:
  + OVE-20200317-0001 excessive/unoptimal memory allocation for hashtables due to read-beyond-end

    (Thanks svace & coverity static analysis,
    https://lists.gnu.org/archive/html/guile-devel/2011-07/msg00069.html,
    backported from 2.0.3.)

* Fri Dec 14 2018 Dmitry V. Levin <ldv@altlinux.org> 1:1.8.7-alt7
- Fixed build (see rhbz#1307394).

* Thu Aug 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.8.7-alt6
- get rid of alternatives

* Mon Jul 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.8.7-alt5
- stop providing guile-devel
- drop devel-static subpackage
- fix incorrect behavior (due to integer overflow) when compiled with gcc >= 6
  (https://lists.gnu.org/archive/html/guile-devel/2016-02/msg00045.html)

* Tue Oct 11 2016 Mikhail Efremov <sem@altlinux.org> 1:1.8.7-alt4
- Remove 'umask' calls from 'mkdir'.

* Thu Apr 07 2016 Mikhail Efremov <sem@altlinux.org> 1:1.8.7-alt3
- Don't specify extension for manpages.
- tests: Update srfi-14.test.

* Mon Dec 02 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.8.7-alt2.5
- Fix BFS (use old automake 1.11).

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.8.7-alt2.4
- Rebuilt with gmp 5.0.5

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.8.7-alt2.3
- Rebuilt for debuginfo

* Thu Nov 04 2010 Sergey Y. Afonin <asy@altlinux.ru> 1:1.8.7-alt2.2
- NMU
- changed fix for build with newest cpp (closes: ALT#24310)
- removed unnecessary call of autoreconf
- added %check section with testsuite's patches from fedoraproject's guile

* Sat Aug 14 2010 Alex Karpov <karpov@altlinux.ru> 1:1.8.7-alt2.1
- removed packages-i18-common requirement (fixed rebuild)

* Tue Nov 24 2009 Stanislav Ievlev <inger@altlinux.org> 1:1.8.7-alt2
- fix build with newest cpp

* Wed Sep 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:1.8.7-alt1.1
- BuildRequres: gcc-fortran removed

* Mon Jul 20 2009 Stanislav Ievlev <inger@altlinux.org> 1:1.8.7-alt1
- 1.8.7

* Wed Apr 22 2009 Stanislav Ievlev <inger@altlinux.org> 1:1.8.6-alt2
- build for Sisyphus

* Mon Dec 15 2008 Alex Karpov <karpov@altlinux.ru> 1:1.8.6-alt1
- 1.8.6

* Tue Dec 09 2008 Alex Karpov <karpov@altlinux.ru> 1:1.8.5-alt1.1
- wrong options for x86_64 build excluded

* Sun Nov 30 2008 Alex Karpov <karpov@altlinux.ru> 1:1.8.5-alt1
- 1.8.5

* Tue Mar 18 2008 Alex Karpov <karpov@altlinux.ru> 1:1.8.4-alt1
- 1.8.4

* Wed Oct 17 2007 Alex Karpov <karpov@altlinux.ru> 1:1.8.3-alt1
- 1.8.3

* Mon Aug 27 2007 Alex Karpov <karpov@altlinux.ru> 1:1.8.2-alt1
- new version

* Mon Feb 12 2007 Alex Karpov <karpov@altlinux.ru> 1:1.8.1-alt1
- "Url:" added, bug 9466 fixed

* Wed Feb 07 2007 Alex Karpov <karpov@altlinux.ru> 1:1.8.1-alt0.1
- picked from orphaned, new version

* Tue Mar 07 2006 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.91-alt0.4
- Fixed build with --as-needed.

* Fri Feb 17 2006 Stanislav Ievlev <inger@altlinux.org> 1:1.7.91-alt0.3
- build with optlevel 0 on amd64 (guile are too unstable with such optimization)

* Fri Feb 17 2006 Stanislav Ievlev <inger@altlinux.org> 1:1.7.91-alt0.2.1
- cvs snapshot

* Thu Feb 16 2006 Stanislav Ievlev <inger@altlinux.org> 1:1.7.91-alt0.2
- increase alternatives weight

* Wed Feb 15 2006 Stanislav Ievlev <inger@altlinux.org> 1:1.7.91-alt0.1
- 1.8 rc1

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:1.6.7-alt2.1.1
- Rebuilt with libreadline.so.5.

* Mon Jul 11 2005 Anton D. Kachalov <mouse@altlinux.org> 1:1.6.7-alt2.1
- x86_64 support

* Wed Mar 23 2005 Alexey Voinov <voins@altlinux.ru> 1:1.6.7-alt2
- .unsigned patch added [fixes #6298]

* Wed Dec 22 2004 Alexey Voinov <voins@altlinux.ru> 1:1.6.7-alt1
- new version (1.6.7)

* Tue Dec 14 2004 Alexey Voinov <voins@altlinux.ru> 1:1.6.6-alt1
- new version (1.6.6)

* Thu Oct 19 2004 Alexey Voinov <voins@altlinux.ru> 1:1.6.5-alt1
- new version (1.6.5)
- removed deps on libtool-1.4
- removed build dep on self
- buildreq updated
- alternatives entry updated

* Tue Dec 02 2003 Alexey Voinov <voins@altlinux.ru> 1:1.6.4-alt4
- rebuilt without *.la

* Wed Oct 01 2003 Alexey Voinov <voins@altlinux.ru> 1:1.6.4-alt3
- now requires libtool_1.4
- fix buildreq
- guile-readline files included in devel subpackage

* Sun Jun 01 2003 Alexey Voinov <voins@voins.program.ru> 1:1.6.4-alt2
- threads support enabled.

* Thu May 08 2003 Alexey Voinov <voins@voins.program.ru> 1:1.6.4-alt1
- spec derived from guile-1.4
- new version
- support for alternatives.
- devel-static created.

* Mon Oct 21 2002 AEN <aen@altlinux.ru> 1:1.4-alt1
- Serial : 1

* Thu May 31 2001 AEN <aen@logic.ru> 1.4-ipl9mdk
- rebuild with new umb-schene package
- requires on new umb-scheme

* Fri Jan 05 2001 AEN <aen@logic.ru>
- adopted for RE

* Wed Nov 15 2000 Egil Moeller <redhog@mandrakesoft.com> 1.4-7mdk
- Bugworkaround around the flawed Makefile.

* Mon Sep 11 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4-6mdk
- ooops wrong info file name.

* Mon Sep 11 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4-5mdk
- finalized BM (Thanks Stefan).

* Fri Sep  8 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4-4mdk
- removed menu entry.
- added a depency for guile-devel on guile with the same release.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4-3mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Pixel <pixel@mandrakesoft.com> 1.4-2mdk
- add provides libguile.so.6

* Tue Jul 11 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4-1mdk
- 1.4

* Thu Mar 30 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.3.4-3mdk
- fix group

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- provides libguile.so.[15].

* Fri Nov 05 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- SMP build/check
- 1.3.4

* Tue Aug 31 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added macro %%{guilever} as apckage version is 1.3.2a but
  for paths, etc. it remains 1.2.3
- corrected %files section (some libs weren't included)

* Thu Aug 26 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- -1.3.2a

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Wed Mar 17 1999 Michael Johnson <johnsonm@redhat.com>
- added .ansi patch to fix #endif

* Wed Feb 10 1999 Cristian Gafton <gafton@redhat.com>
- add patch for the scm stuff

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- integrate changes from rhcn version (#640)

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- call libtoolize first to get it to compile on the arm

* Sat Jan  9 1999 Todd Larason <jtl@molehill.org>
- Added "Requires: guile" at suggestion of Manu Rouat <emmanuel.rouat@wanadoo.fr>

* Fri Jan  1 1999 Todd Larason <jtl@molehill.org>
- guile-devel does depend on guile
- remove devel dependancy on m4
- move guile-snarf from guile to guile-devel
- Converted to rhcn

* Wed Oct 21 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.3.
- don't strip libguile.so.*.0.0. (but set the execute bits).

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- spec file fixups

* Wed Sep  2 1998 Michael Fulbright <msf@redhat.com>
- Updated for RH 5.2

* Mon Jan 26 1998 Marc Ewing <marc@redhat.com>
- Started with spec from Tomasz Koczko <kloczek@idk.com.pl>
- added slib link

* Thu Sep 18 1997 Tomasz Koczko <kloczek@idk.com.pl>          (1.2-3)
- added %%attr(-, root, root) for %%doc,
- in %%post, %%postun ldconfig runed as parameter "-p",
- removed /bin/sh from requires,
- added %%description,
- changes in %%files.

* Fri Jul 11 1997 Tomasz Koczko <kloczek@rudy.mif.pg.gda.pl>  (1.2-2)
- all rewrited for using Buildroot,
- added %%postun,
- removed making buid logs,
- removed "--inclededir", added "--enable-dynamic-linking" to configure
  parameters,
- added striping shared libs and /usr/bin/guile,
- added "Requires: /bin/sh" (for guile-snarf) in guile package and
  "Requires: m4" for guile-devel,
- added macro %%{PACKAGE_VERSION} in "Source:" and %%files,
- added %%attr macros in %%files.
