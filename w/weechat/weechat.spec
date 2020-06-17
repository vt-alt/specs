Name: weechat
Version: 2.6
Release: alt1

Summary: fast, light & extensible IRC client
License: GPL-3.0
Group: Networking/IRC

URL: http://www.weechat.org/
Source: %name-%version.tar
Patch0: weechat-alt-python.patch

Packager: Alexey Gladkov <legion@altlinux.ru>

# Automatically added by buildreq on Thu Oct 20 2011
BuildRequires: asciidoc asciidoc-a2x
BuildRequires: libaspell-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgnutls-devel
BuildRequires: lua-devel
BuildRequires: libcurl-devel
BuildRequires: zlib-devel
BuildRequires: libncursesw-devel
BuildRequires: ruby
BuildRequires: libruby-devel
BuildRequires: perl-devel
BuildRequires: python3-devel
BuildRequires: source-highlight
BuildRequires: tcl-devel

%description
WeeChat is a fast, light and extensible chat client. It runs on many
platforms (including Linux, BSD and Mac OS).
WeeChat is:
- modular: a lightweight core with plugins around
- multi-protocols: IRC and Jabber (other soon)
- extensible: C plugins and scripts (Perl, Python, Ruby, Lua and Tcl)
- free software: released under GPLv3 license
- fully documented: user's guide, API, FAQ,.. translated in many languages
Development is very active, and bug fixes are very fast!

%package plugin-aspell
Summary: Aspell plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-aspell
This package contains aspell plugin for weechat.

%package plugin-lua
Summary: Lua plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-lua
This package contains lua plugin for weechat.

%package plugin-perl
Summary: Perl plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-perl
This package contains perl plugin for weechat.

%package plugin-python
Summary: Python plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-python
This package contains python plugin for weechat.

%package plugin-ruby
Summary: Ruby plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-ruby
This package contains ruby plugin for weechat.

%package plugin-tcl
Summary: Tcl plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-tcl
This package contains ruby plugin for weechat.

%prep
%setup
#patch0 -p2

# build plugins as plugins, not libs
find ./src/plugins -name "Makefile*" -print0 | xargs -r0 subst 's,\(\-module\),\1 -avoid-version,' --

%build
./autogen.sh

%configure \
	--enable-threads \
	--enable-exec \
	--enable-buflist \
	--enable-perl \
	--enable-ruby \
	--enable-lua \
	--enable-python \
	--disable-python2 \
	--enable-gnutls \
	--enable-aspell \
	--enable-man \
	--enable-doc

%make_build

%install
%make_install DESTDIR=%buildroot install

rm -rf -- \
	%buildroot/%_includedir \
	%buildroot/%_pkgconfigdir \
#

find %buildroot -name '*.la' -delete
find %buildroot -name '*.a' -delete

%find_lang %name

%files -f %name.lang
%_bindir/*
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_niconsdir/%name.png
%_libdir/%name/plugins/alias.so
%_libdir/%name/plugins/buflist.so
%_libdir/%name/plugins/charset.so
%_libdir/%name/plugins/fifo.so
%_libdir/%name/plugins/fset.so
%_libdir/%name/plugins/exec.so
%_libdir/%name/plugins/script.so
%_libdir/%name/plugins/irc.so
%_libdir/%name/plugins/logger.so
%_libdir/%name/plugins/relay.so
%_libdir/%name/plugins/xfer.so
%_libdir/%name/plugins/trigger.so
#_mandir/man*/*
#_defaultdocdir/%name

%files plugin-aspell
%_libdir/%name/plugins/spell.so

%files plugin-lua
%_libdir/%name/plugins/lua.so

%files plugin-perl
%_libdir/%name/plugins/perl.so

%files plugin-python
%_libdir/%name/plugins/python.so

%files plugin-ruby
%_libdir/%name/plugins/ruby.so

%files plugin-tcl
%_libdir/%name/plugins/tcl.so

%changelog
* Mon Nov 18 2019 Alexey Gladkov <legion@altlinux.ru> 2.6-alt1
- New version (2.6)

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1.1
- rebuild with new perl 5.28.1

* Thu Aug 16 2018 Alexey Gladkov <legion@altlinux.ru> 2.2-alt1
- New version (2.2)

* Wed Apr 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.1-alt2
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1.1
- Rebuild with Ruby 2.5.0

* Tue Dec 26 2017 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt1
- New version (2.0.1)

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt2.1
- rebuild with new perl 5.26.1

* Sat Nov 25 2017 Alexey Gladkov <legion@altlinux.ru> 1.9.1-alt2
- Add buflist and exec plugins.

* Mon Nov 20 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.9.1-alt1
- NMU: New security version (1.9.1) (Fixes: CVE-2017-14727)

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.9-alt1.1
- Rebuild with Ruby 2.4.1

* Sun Jun 25 2017 Alexey Gladkov <legion@altlinux.ru> 1.9-alt1
- New version (1.9)

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4-alt1.4
- NMU: rebuild against Tcl/Tk 8.6

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1.3
- (NMU) rebuild with perl 5.24.1

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1.2.1
- rebuild with new lua 5.3

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1.2
- (NMU) rebuild with Ruby 2.3.1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Jan 26 2016 Alexey Gladkov <legion@altlinux.ru> 1.4-alt1
- New version (1.4)

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.3.5-alt4
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.3.5-alt3
- rebuilt for perl-5.16

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.5-alt2.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 0.3.5-alt2
- Rebuilt for perl-5.14.

* Thu Sep 01 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.5-alt1
- 0.3.5.

* Thu Jan 27 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.4-alt1
- 0.3.4.
- Introduce -plugin-tcl subpackage.
- Update Summary and Descriptions, made some spec cleanups.

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt2.1
- Rebuilt with python 2.6

* Sat Jul 04 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.6-alt2
- Rebuilt with Ruby 1.9
- Fixed build with new gnutls
- Removed obsolete %%update_menus/%%clean_menus calls

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.6-alt1
- 0.2.6.
- License: GPLv3.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.5-alt1
- 0.2.5.

* Fri Apr 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.4-alt1
- 0.2.4.

* Thu Oct 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.2.1-alt2
- 0.2.1.

* Wed May 31 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.7-alt2.1
- Rebuild with libgnutls.so.13 .

* Tue Mar 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1.7-alt2
- fix build with new ruby.

* Sat Jan 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1.7-alt1
- 0.1.7 release.

* Thu Oct 06 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.5-alt1
- 0.1.5 release.
- fixed absolute link.
- added ruby plugins support.

* Tue Jul 05 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.3-alt1
- 0.1.3 release

* Sat Jun 11 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.2.1-alt1
- 0.1.2.1 release.
- python interface added.

* Fri Apr 08 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.1-alt2
- 0.1.1 release.

* Fri Mar 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.1-alt1
- 0.1.1 CVS from 04032005.

* Mon Nov 22 2004 Pavlov Konstantin <thresh@altlinux.ru> 0.0.9-alt0.1pre2
- 0.0.9pre1 development version.
- initial build for sisyphus
