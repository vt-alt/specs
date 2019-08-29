# vim: set ft=spec: -*- rpm-spec -*-

Name: aptitude
Version: 0.4.5
Release: alt12

Summary: Terminal-based apt frontend
Group: System/Configuration/Packaging
License: GPL
Url: http://people.debian.org/~dburrows/aptitude
Packager: Sir Raorn <raorn@altlinux.ru>

# git://git.altlinux.org/gears/a/aptitude.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libapt-devel >= 0.5.15lorg2-alt42

# Automatically added by buildreq on Sat Oct 07 2006
BuildRequires: cppunit-devel docbook-dtds docbook-style-xsl gcc-c++ html2text libapt-devel libncursesw-devel libsigc++2.0-devel xsltproc

%description
aptitude is a terminal-based apt frontend.  This is a heavily
emasculated version of Debian software, besause some features
can't be ported to apt-rpm.

%package doc
Summary: English manual for aptitude, a terminal-based apt frontend
Group: Books/Computer books
# Can't use noarch:
#--- aptitude-doc-0.4.5-alt5.noarch.rpm.i586     2009-12-21 18:23:35 +0300
#+++ aptitude-doc-0.4.5-alt5.noarch.rpm.x86_64   2009-12-21 18:23:35 +0300
#@@ -77,35 +77,35 @@
# /usr/share/doc/aptitude-doc-0.4.5/index.html
#-/usr/share/doc/aptitude-doc-0.4.5/ld-id2608397.html
#+/usr/share/doc/aptitude-doc-0.4.5/ld-id3016206.html
#...
#BuildArch: noarch
Conflicts: %name < %version-%release
Conflicts: %name > %version-%release

%description doc
aptitude is a terminal-based apt frontend.  This package contains
the English version of the aptitude user's manual in HTML format.

%prep
%setup
%patch -p1
find -type f -name '*.cc' -print0 |
	xargs -r0 sed -i '1,1 s/^/#include "config.h"\n/' --

%build
%add_optflags -std=c++14
%add_optflags -fno-strict-aliasing
# gettext uses mkinstalldirs...
touch mkinstalldirs
# STFU, automake!
touch ChangeLog
%autoreconf

%configure \
  --disable-werror \
  --disable-docs
%make_build
%make_build -C doc/en

%install
mkdir -p %buildroot%_localstatedir/%name
%makeinstall_std
rm -rf %buildroot%_mandir

%make_install DESTDIR=%buildroot -C doc/en install-man
install -p -m644 doc/en/README.en %buildroot%_datadir/%name/README
rm -f %buildroot%_datadir/%name/function_*

%find_lang %name

%files -f %name.lang
%doc AUTHORS FAQ NEWS
%_bindir/*
%_datadir/%name
%_man8dir/%name.8*
%_localstatedir/*

%files doc
%doc doc/en/output-html/*

%changelog
* Thu Jun 13 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.5-alt12
- Rebuilt with new Apt

* Fri Apr 26 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.4.5-alt11
- (no user visible changes) Removed "interesting" dead code (related
  to Recommends, not present in ALT rpm), which didn't compile after
  we changed apt's API recently.

* Thu Nov 29 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.5-alt10
- NMU: fixed build with new libapt.

* Mon Oct 23 2017 Andrew Savchenko <bircoph@altlinux.org> 0.4.5-alt9
- Fix build with lcc.

* Tue Apr 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.5-alt8
- Fixed build with gcc6.
- Fixed crash in internal minesweeper game.

* Wed Nov 23 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.5-alt7.qa1
- Rebuilt with libapt-pkg-libc6.9-6.so.6.
- Fixed build with sigc++.

* Thu May 28 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.5-alt6.1.1.1
- Rebuilt for:
 + libapt-pkg-libc6.9-6.so.5.
 + gcc5 C++11 ABI.

* Wed Sep 10 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.5-alt6.1.1
- Rebuilt with libapt-pkg-libc6.9-6.so.4.

* Tue Mar 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt6.1
- NMU: rebuild with libapt

* Wed Jan 30 2013 Dmitry V. Levin <ldv@altlinux.org> 0.4.5-alt6
- Fixed and enabled LFS support (see #28214).

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt5.qa3
- Fixed build with glibc 2.16

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt5.qa2
- Fixed build

* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.5-alt5.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for aptitude
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])

* Sun Nov 22 2009 Alexey I. Froloff <raorn@altlinux.org> 0.4.5-alt5
- Packaged User's Manual, dropped useless data and developer README's
- Resurrected changelog viewer

* Sun May 31 2009 Alexey I. Froloff <raorn@altlinux.org> 0.4.5-alt4
- Fixed build with g++ 4.4.x
- Disabled strict aliasing optimization

* Sun Apr 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.4.5-alt3
- Fixed segfault when Aptitude::UI::Minibuf-Prompts set to true
- Fixed "reinstall" action, disabled UI reinstall (closes: #17164)

* Fri Dec 12 2008 Dmitry V. Levin <ldv@altlinux.org> 0.4.5-alt2.1
- Fixed build with g++ 4.3.x.

* Wed Aug 13 2008 Sir Raorn <raorn@altlinux.ru> 0.4.5-alt2
- New option "Aptitude::UI::Disable-Mouse" - ignore mouse
  events (for use with b0rken terminals)
- Support for command-line package file installation
- Better "autoinstalled" status assignment for packages that
  obsolete other packages

* Sat May 17 2008 Sir Raorn <raorn@altlinux.ru> 0.4.5-alt1
- [0.4.5]
- Fix CLI "update" and disable UI "UpdatePackageList" (closes: #10204)
- Use libapt-pkg when calculating dist-upgrade instead of dburrows-invented
  square-wheeled bicycle (this means you can use aptitude dist-upgrade and
  get sane results)

* Thu Dec 14 2006 Sir Raorn <raorn@altlinux.ru> 0.4.4-alt1
- [0.4.4]

* Sat Oct 14 2006 Sir Raorn <raorn@altlinux.ru> 0.4.1-alt1.1
- Rebuilt with new apt

* Sat Oct 07 2006 Sir Raorn <raorn@altlinux.ru> 0.4.1-alt1
- [0.4.1]
- Updated build requires
- All pathes merged into GIT repository
- Removed some of aptitude functionality:
 + changelog viewer (unusable outside Debian)
 + "Tasks" support (unusable outside Debian)
 + "Tags" support (unusable outside Debian)
 + hierarchy support (unusable outside Debian)
 + "Audit recommendations" support (not applicable for RPM)
 + "Become root" functionality (closes: #7332)
 + trust checks (not available in apt < 0.6)
 + "purge" support (not applicable for RPM)
 + "Problem Resolver" because it only generates problems
- Changed some defaults:
 + default group policy is "status,section(none)"
 + "section" group method set to "groups" concept, not
   "sections" (not applicable for RPM)
 + "Security updates" are coming from "updates" component,
   not "securyty.debian.org" site
- Closes: #7333 (fixed in upstream)

* Fri Apr 14 2006 Sir Raorn <raorn@altlinux.ru> 0.3.1deb3-alt2
- Rebuilt with new apt
- Fixed --as-needed link

* Sun Jan 30 2005 Sir Raorn <raorn@altlinux.ru> 0.3.1deb3-alt1
- [0.3.1-3]
- Match Description parsing with apt-rpm's LongDesc format
- Put packages coming from updates.altlinux.org into "Security updates" section
- Enabled documentation (manpage and user's manual)
- Merge package descriptions from debian/control
- Updated build requires

* Sat Jan 29 2005 Sir Raorn <raorn@altlinux.ru> 0.2.15.8deb1-alt2.1
- Rebuilt with new libapt-pkg

* Thu Jan 20 2005 Dmitry V. Levin <ldv@altlinux.org> 0.2.15.8deb1-alt2
- Fixed compilation issues detected by g++-3.4.3.

* Fri Oct 08 2004 Sir Raorn <raorn@altlinux.ru> 0.2.15.8deb1-alt1
- [0.2.15.8-1]
- Do not hide Maintainer and Source package from package wiew.

* Mon Sep 20 2004 Sir Raorn <raorn@altlinux.ru> 0.2.15.7deb1-alt1
- [0.2.15.7-1]
- cnc-rpm patch updated from conectiva (thanx, boiko)
- Documentation removed (totally b0rken)

* Thu Jul 15 2004 Sir Raorn <raorn@altlinux.ru> 0.2.15.2deb1-alt1
- [0.2.15.2-1]

* Thu May 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.13-alt2.1
- Rebuilt with libapt-0.5.15cnc6-alt1.

* Fri Jan 16 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.13-alt2
- Updated rpm-apt patch.
- Fixed build.
- Rebuilt with apt-0.5.15cnc5.

* Sat Oct 11 2003 Sir Raorn <raorn@altlinux.ru> 0.2.13-alt1
- New maintainer
- [0.2.13]
- Removed patches:
  + alt-gcc3
- Updated patches:
  + alt-cnc-apt-rpm (was: cnc-rpm)
- Default package grouping policy set to
  "filter(missing),status,section(none,nopassthrough)"
- Updated buildreqs

* Wed Dec 04 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.11.1-alt1
- Updated to aptitude-0.2.11.1-2cl.

* Wed Sep 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.8-alt3
- rebuld with gcc3

* Wed Mar 27 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2.8-alt2
- Added librpm-4.0.4 build support.
- Built with librpm-4.0.4, updated buildrequires.

* Fri Mar 22 2002 Rider <rider@altlinux.ru> 0.2.8-alt1
- 0.2.8 with Conectiva patches.

* Tue Nov 06 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.0.7.13-ipl11mdk
- Initial build with rpm4.

* Thu Aug 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.0.7.13-ipl10mdk
- Corrected requires and buildrequires lists.
- Reworked compilation options again: we add only '-fno-exceptions' now.

* Wed Aug 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.0.7.13-ipl9mdk
- Added %%optflags_nocpp to compilation options.
- Rebuilt with apt-0.3.19cnc52-alt2, corrected apt requires.

* Thu Jul 26 2001 Alexander Bokovoy <ab@altlinux.ru> 0.0.7.13-ipl8mdk
- rebuild against apt-get cnc51

* Sun Apr 14 2001 Alexander Bokovoy <ab@avilink.net> 0.0.7.13-ipl7mdk
- rebuild against apt-get cnc38

* Tue Feb 20 2001 Alexander Bokovoy <ab@avilink.net> 0.0.7.13-ipl6mdk
- Wrong group fixed

* Mon Feb 19 2001 Alexander Bokovoy <ab@avilink.net> 0.0.7.13-ipl5mdk
- rebuild against apt-get cnc36

* Tue Jan 24 2001 Alexander Bokovoy <ab@avilink.net> 0.0.7.13-ipl4mdk
- Incompabilities between libapt-pkg and aptitude sources fixed

* Tue Jan 22 2001 Alexander Bokovoy <ab@avilink.net> 0.0.7.13-ipl3mdk
- New upstream version
- rebuild with new apt

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 0.0.7.6-ipl2mdk
- Specfile cleanup.

* Sun Dec 02 2000 Alexander Bokovoy <ab@avilink.net>
- MDK RE-fication
- Patch for incorrect class cast under gcc 2.96

* Mon Oct 16 2000 Claudio Matsuoka <claudio@conectiva.com>
- new upstream release: 0.0.7.6

* Fri Oct 13 2000 Claudio Matsuoka <claudio@conectiva.com>
- new upstream release: 0.0.7.4
- minor RPM cleanups
- specfile fixes

* Thu Oct 12 2000 Claudio Matsuoka <claudio@conectiva.com>
- added missing help file, manpage
- changed /var/state/aptitude to FHS-compliant /var/lib/aptitude

* Tue Oct 10 2000 Claudio Matsuoka <claudio@conectiva.com>
- upgraded to 0.0.7.3
- some RPM cleanup
- package quality: 50-60%%

* Mon Oct  2 2000 Claudio Matsuoka <claudio@conectiva.com>
- package created
