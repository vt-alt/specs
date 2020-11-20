Name: aspell
Version: 0.60.8
Release: alt1

Summary: An Open Source interactive spelling checker program
License: LGPL-2.1
Group: Text tools
Url: http://%name.net/

Source: http://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source101: %name-ispell.alternatives

BuildRequires(pre): rpm-macros-alternatives
BuildRequires: gcc-c++ libncursesw-devel
Requires: lib%name = %version-%release

%def_disable static
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
GNU Aspell is a spell checker designed to eventually replace Ispell.
It can either be used as a library or as an independent spell checker.
Its main feature is that it does a much better job of coming up with
possible suggestions than just about any other spell checker out there
for the English language, including Ispell and Microsoft Word. It
also has many other technical enhancements over Ispell such as using
shared memory for dictionaries and intelligently handling personal
dictionaries when more than one Aspell process is open at once.

%package -n %name-ispell
Summary: Spell and Ispell compatibility scripts for Aspell
Group: Text tools
BuildArch: noarch
Requires(post,preun): alternatives >= 0.2
Requires: %name = %version-%release
Provides: ispell
Provides: /usr/bin/spell
Obsoletes: pspell-ispell

%description -n %name-ispell
Two simple scripts: Spell and Ispell compatibility scripts for Aspell.

%package -n lib%name
Summary: Shared libraries required for %name-based software
Group: System/Libraries
Provides: libpspell
Obsoletes: libpspell

%description -n lib%name
Shared libraries required for %name-based software.

%package -n lib%name-devel
Summary: Development files needed to build applications with %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files needed to build applications with %name.

%package -n lib%name-devel-static
Summary: Static library needed to build static applications with %name
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static library needed to build statically linked applications with %name.

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static} \
	--enable-pkgdatadir=%_datadir/%name \
	--enable-pkglibdir=%_libdir/%name \
	--enable-wide-curses
%make_build


%install
%make_install DESTDIR=%buildroot install
ln -sf cp1251.cset %buildroot%_datadir/%name/windows-1251.cset
mv %buildroot%_datadir/%name/ispell %buildroot%_bindir/%name-ispell
mv %buildroot%_datadir/%name/spell %buildroot%_bindir/%name-spell
install -d %buildroot%_altdir
install -p -m 644 %SOURCE101 %buildroot%_altdir/%name-ispell

cp modules/filter/*.info %buildroot%_libdir/%name/
rm -rf %buildroot%_libdir/%name/*.la

%find_lang %name

%files -n lib%name
%_datadir/%name
%dir %_libdir/%name
%_libdir/*.so.*
%_libdir/%name/*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_infodir/aspell-dev.*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n %name-ispell
%_altdir/%name-ispell
%_bindir/%name-ispell
%_bindir/%name-spell

%files -f %name.lang
%doc README TODO
%_bindir/aspell
%_bindir/aspell-import
%_bindir/pspell-config
%_bindir/pre*
%_bindir/run-with-aspell
%_bindir/word-list-compress
%_infodir/aspell.info.*
%_man1dir/*.1.*

%changelog
* Mon Nov 16 2020 Alexei Takaseev <taf@altlinux.org> 0.60.8-alt1
- 0.60.8 (ALT #39290)
- Fix License
- Drop unneeded patch aspell-0.60.6.1-gcc7-fixes.patch (fix in upstream)

* Sat Aug 11 2018 Alexei Takaseev <taf@altlinux.org> 0.60.6.1-alt3
- Add BR: rpm-macros-alternatives

* Sat Jun 09 2018 Alexei Takaseev <taf@altlinux.org> 0.60.6.1-alt2
- Fix build with gcc7 (patch from Fedora)

* Tue Dec 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.60.6.1-alt1.1
- NMU: added BR: texinfo

* Tue Dec 20 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.60.6.1-alt1
- Updated to 0.60.6.1
- Make interpackage dependencies strict

* Mon Oct 25 2010 Damir Shayhutdinov <damir@altlinux.ru> 0.60.6-alt3
- Rebuilt for new symbol provides

* Mon Nov 09 2009 Damir Shayhutdinov <damir@altlinux.ru> 0.60.6-alt2
- Removed obsolete info macros from post/preun

* Sat Nov 15 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.60.6-alt1
- Updated to 0.60.6
- Removed obsolete ldconfig

* Fri Jul 11 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.60.5-alt3
- Some fixes from php-coder@
  + Build with libncursesw to fix charset problems in UTF8 locale (#16302).
  + Fixed crash in UTF8 locale with empty input file (#15747).
  + spec cleanup

* Thu Feb 01 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.60.5-alt2
- Fixed info file deregestration (#10748)

* Thu Dec 28 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.60.5-alt1
- New upstream version

* Sun Nov 26 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.60.4-alt5
- Fix aspell-ispell alternative bug (empty line at end of file).

* Fri Nov 17 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.60.4-alt4
- Ressurected from orphaned
- Applied patch by zerg@
- Fix build with gcc4 by zerg@
- Fix ispell alternatives by zerg@

* Mon Jan 30 2006 Vital Khilko <vk@altlinux.ru> 0.60.4-alt3
- fixed stupid mistake in rpm scripts

* Tue Jan 24 2006 Vital Khilko <vk@altlinux.ru> 0.60.4-alt2
- some fixes

* Wed Dec 07 2005 Vital Khilko <vk@altlinux.ru> 0.60.4-alt1
- 0.60.4
- #8221

* Tue Aug 09 2005 Vital Khilko <vk@altlinux.ru> 0.60.3-alt1
- 0.60.3

* Tue Jun 21 2005 Vital Khilko <vk@altlinux.ru> 0.60.2-alt4
- #6446

* Thu Mar 17 2005 Vital Khilko <vk@altlinux.ru> 0.60.2-alt3
- fixed filters location

* Sat Jan 22 2005 Dmitry V. Levin <ldv@altlinux.org> 0.60.2-alt2
- Fixed heavily broken build dependencies.
- Disabled build of static libraries by default.

* Thu Jan 20 2005 Vital Khilko <vk@altlinux.ru> 0.60.2-alt1
- 0.60.2
- #5727
- #5057

* Wed Sep 01 2004 Vital Khilko <vk@altlinux.ru> 0.60.0-alt1
- official release.

* Fri Aug 20 2004 Vital Khilko <vk@altlinux.ru> 0.60.0-alt0.7
- new pre-release snapshot

* Wed Aug 11 2004 Vital Khilko <vk@altlinux.ru> 0.60.0-alt0.6
- new pre-release snapshot
- added symlink to windows-1251.cset from cp1251.cset for
  sylpheed-claws support

* Mon Jul 19 2004 Vital Khilko <vk@altlinux.ru> 0.60.0-alt0.5
- new pre-release snapshot

* Thu Jun 24 2004 Vital Khilko <vk@altlinux.ru> 0.60.0-alt0.4
- new pre-release snapshot

* Wed Jun 09 2004 Vital Khilko <vk@altlinux.ru> 0.60.0-alt0.3
- new pre-release snapshot
- patched buffer overflow in word-list-compress tool

* Fri Jun 04 2004 Vital Khilko <vk@altlinux.ru> 0.60.0-alt0.2
- new pre-release snapshot

* Mon May 17 2004 Vital Khilko <vk@altlinux.ru> 0.60.0-alt0.1
- new version

* Mon Jan 05 2004 Vital Khilko <vk@altlinux.ru> 0.51.0-alt1
- new version
- added gettext suppport & added belarusian translation
- added modules support
- added more encodings support

* Mon Nov 24 2003 Vital Khilko <vk@altlinux.ru> 0.50.4-alt3
- rebuild without *-devel-static and .la files
- fix provides

* Mon Nov 10 2003 Vital Khilko <vk@altlinux.ru> 0.50.4-alt2
- add alternatives to aspell-ispell package

* Mon Oct 20 2003 Vital Khilko <vk@altlinux.ru> 0.50.4-alt1
- new version
- fixed part one of bug #613714 and a hack to sort of fix part two
- added cp1251 support
- fix provides

* Mon Sep 15 2003 Vital Khilko <vk@altlinux.ru> 0.50.3-alt1
- new version
- pspell merged with aspell
- move en, en_CA, en_GB dictionaries to separate package

* Wed Sep 18 2002 AEN <aen@altlinux.ru> 0.33.7.1-alt1
- rebuild with fixed pspell

* Fri Aug 17 2001 AEN <aen@logic.ru> 0.33.7-alt1
- new version
* Wed Jun 13 2001 AEN <aen@logic.ru> 0.33.6.3-alt1
- rebuilt with libpspell-.12.2

* Mon May 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.32.5-ipl5mdk
- Libification.
- Built with pspell-0.11.2-ipl8mdk

* Fri Jan 12 2001 AEN <aen@logic.ru>
- RE adaptations

* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 0.32.5-3mdk
- Fix Requires and BuildRequires

* Wed Sep 20 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.32.5-2mdk
- Provides pwli files (Thanks Michael Reinsch)

* Fri Aug 25 2000 Troels Liebe Bentsen 0.32.5-1mdk
- Updated to new version.
- Added packages en, en_CA, en_GB

* Thu Aug 24 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.32.1-1mdk
- release 0.32.1 (merge from helix 0_helix_1)
- BM + macroszification

* Thu Jan 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 28.3-1mdk
- v28.3

* Fri Aug 27 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- initial spec
