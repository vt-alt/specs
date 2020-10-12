Name: elinks
Version: 0.12
Release: alt0.12.6

Summary: Lynx-like text WWW browser with many features
License: GPLv2
Group: Networking/WWW

URL: http://elinks.cz
Source: elinks-0.12pre5.tar
Patch: %name-%version-%release.patch

# alternatives
%set_compress_method gzip
%define weight 30
PreReq: alternatives >= 0.2.0
BuildPreReq: alternatives >= 0.2.0

Provides: webclient, links
Provides: %_bindir/links
Obsoletes: links

# Automatically added by buildreq on Wed Sep 30 2009
BuildRequires: bzlib-devel docbook-utils libexpat-devel libgpm-devel lua-devel libssl-devel python-modules-encodings xmlto zlib-devel

%description
ELinks is advanced text-mode web browser with wide scale of additional
features and extensibility by possibility to plug in own scripts in Lua
language. This project aims to provide feature-rich version of Links,
with more open patches/features inclusion policy.

%prep
%setup -n elinks-0.12pre5
%patch -p1

# fix shebang
sed -i 's,/usr/bin/env python,%_bindir/python2,' doc/tools/asciidoc/asciidoc.py

%build
cat config/m4/*.m4 >acinclude.m4
%autoreconf
export ac_cv_prog_HAVE_SMBCLIENT=no
%configure %{subst_enable debug} \
	--sysconfdir=/etc/elinks \
	--without-x \
	--enable-utf-8 \
	--enable-256-colors \
	--enable-cgi \
	--enable-finger \
	--enable-gopher \
	--enable-nntp \
	--disable-smb \
	--disable-leds \
	--without-spidermonkey \
	--without-idn \
	--without-lzma \
	#
touch src/intl/gettext/plural.y
make -C src/intl/gettext V=1 plural.c

%add_optflags -fno-strict-aliasing -Wno-pointer-sign -Werror
%ifarch %e2k
# elinks-0.12/src/util/error.h:189 (#define if_assert_failed) => ftbfs on e2k
%add_optflags  -Wno-error=assign-where-compare-meant
# textarea.c:46 (int split_prev:1) => error #108: signed bit field of length 1
%add_optflags -Wno-error=signed-one-bit-field
%endif

make -C src V=1 CFLAGS="%optflags"
make -C doc V=1 features.txt manual.html

%install
%makeinstall_std V=1

mkdir -p %buildroot%_altdir
cat <<__EOF__ >%buildroot%_altdir/elinks
%_bindir/links		%_bindir/elinks		%weight
%_man1dir/links.1.gz	%_man1dir/elinks.1.gz	%_bindir/elinks
__EOF__

install -pD -m644 elinks.conf %buildroot/etc/elinks/elinks.conf

%find_lang elinks

%files -f elinks.lang
%_bindir/elinks
%dir /etc/elinks
%config(noreplace) /etc/elinks/elinks.conf
%_man1dir/elinks.*
%_man5dir/elinks*
%_altdir/elinks
%doc AUTHORS COPYING NEWS README THANKS
%doc doc/manual.html

%changelog
* Sat Oct 03 2020 Michael Shigorin <mike@altlinux.org> 0.12-alt0.12.6
- workaround ftbfs with lcc

* Sun May 31 2020 Anton Midyukov <antohami@altlinux.org> 0.12-alt0.12.5
- Fix FTBFS

* Tue Sep 17 2019 Ivan A. Melnikov <iv@altlinux.org> 0.12-alt0.12.4
- fix double dereference (closes: #36113)

* Wed Sep 11 2019 Denis Medvedev <nbr@altlinux.org> 0.12-alt0.12.3
- (Fixes: CVE-2012-4545)

* Tue Feb 05 2019 Fr. Br. George <george@altlinux.ru> 0.12-alt0.12.2
- rebuild with OpenSSL 1.1

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt0.12.1
- rebuild with new lua 5.3

* Tue May 24 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.12-alt0.12
- Fixed build with bison-3.0.

* Tue Jul 24 2012 Dmitry V. Levin <ldv@altlinux.org> 0.12-alt0.11
- Fixed build with gcc 4.6.

* Mon Nov 08 2010 Dmitry V. Levin <ldv@altlinux.org> 0.12-alt0.10
- Fixed build with gcc 4.5.

* Thu Sep 30 2010 Dmitry V. Levin <ldv@altlinux.org> 0.12-alt0.9.1
- Rebuilt with libssl.so.10.

* Wed Sep 30 2009 Alexey Tourbin <at@altlinux.ru> 0.12-alt0.9
- fixed configure test for lua-5.1
- removed menu and icons

* Tue Jul 14 2009 Alexey Tourbin <at@altlinux.ru> 0.12-alt0.8
- elinks-0.12pre3-7-g3bcca8e -> elinks-0.12pre5

* Sun Apr 12 2009 Alexey Tourbin <at@altlinux.ru> 0.12-alt0.7
- 0.12pre2-85-g8ad3280 -> elinks-0.12pre3-7-g3bcca8e (20090405)

* Sat Mar 07 2009 Alexey Tourbin <at@altlinux.ru> 0.12-alt0.6
- elinks-0.12pre2 -> 0.12pre2-85-g8ad3280 (20090301)

* Mon Dec 15 2008 Alexey Tourbin <at@altlinux.ru> 0.12-alt0.5
- fixed gcc-4.3 warnings
- removed menus/alternatives scriptlets

* Mon Sep 22 2008 Alexey Tourbin <at@altlinux.ru> 0.12-alt0.4
- elinks-0.12pre1 -> elinks-0.12pre2

* Sat Jul 05 2008 Alexey Tourbin <at@altlinux.ru> 0.12-alt0.3
- updated to elinks-0.12pre1

* Sun Jun 15 2008 Alexey Tourbin <at@altlinux.ru> 0.12-alt0.2
- updated to elinks-0.12-a833d6d0 (20080609)

* Sun Jun 17 2007 Alexey Tourbin <at@altlinux.ru> 0.12-alt0.1
- rebased to elinks-0.12 branch

* Mon Apr 16 2007 Alexey Tourbin <at@altlinux.ru> 0.11.3-alt1
- 0.11.2 -> 0.11.3

* Tue Nov 21 2006 Alexey Tourbin <at@altlinux.ru> 0.11.2-alt1
- 0.11.1 -> 0.11.2 (SMB protocol disabled, CVE-2006-5925)

* Sun Oct 15 2006 Alexey Tourbin <at@altlinux.ru> 0.11.1-alt3
- fixed more gcc warnings (check asprintf return value)
- restored -rdynamic for use with backtrace

* Sat Oct 14 2006 Alexey Tourbin <at@altlinux.ru> 0.11.1-alt2
- cloned git tree from elinks.cz, applied my changes and built with gear
- fixed a handful of warnings emitted by new gcc compiler
- fixed lua alert message on startup (when hooks.lua fails)
- removed -rdynamic from LDFLAGS
- changed doc packaging; only asciidoc-generated manual.html is now
  packaged, which really has most of the stuff inside it

* Wed May 17 2006 Alexey Tourbin <at@altlinux.ru> 0.11.1-alt1
- 0.10.6 -> 0.11.1
- patched for lua-5.1

* Thu Sep 15 2005 Alexey Tourbin <at@altlinux.ru> 0.10.6-alt1
- 0.10.5 -> 0.10.6

* Thu May 05 2005 Alexey Tourbin <at@altlinux.ru> 0.10.5-alt1
- 0.10.4 -> 0.10.5

* Wed Apr 06 2005 Alexey Tourbin <at@altlinux.ru> 0.10.4-alt1
- 0.10.3 -> 0.10.4

* Thu Mar 03 2005 Alexey Tourbin <at@altlinux.ru> 0.10.3-alt1
- 0.10.2 -> 0.10.3

* Thu Feb 03 2005 Alexey Tourbin <at@altlinux.ru> 0.10.2-alt1
- 0.10.1 -> 0.10.2
- added smart prefixes (altbug and altbugno) for ALT bugzilla to elinks.conf

* Thu Jan 06 2005 Alexey Tourbin <at@altlinux.ru> 0.10.1-alt1
- 0.10pre3 -> 0.10.1
- build without JavaScript by default
- build without libidn
- %_docdir/elinks-%version/contrib not packaged

* Mon Nov 08 2004 Alexey Tourbin <at@altlinux.ru> 0.10-alt0.2
- 0.10pre2 -> 0.10pre3

* Thu Oct 07 2004 Alexey Tourbin <at@altlinux.ru> 0.10-alt0.1
- 0.9.1 -> 0.10pre2
- enabled JavaScript, Finger, Gopher, NNTP, international domain names
- updated patches
- upgraded to new alternatives format
- rebuilt with lua5:
  + /etc/elinks/hooks.lua not packaged
  + smart prefixes available under `Options Manager/Protocol/URI Rewrite'
  + old hooks.lua for lua4 available in %_docdir/elinks-%version/contrib/lua

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.1-alt4.1
- Rebuilt with openssl-0.9.7d.

* Fri Mar 19 2004 Alexey Tourbin <at@altlinux.ru> 0.9.1-alt4
- cvs-listbox-segfault.patch: fixes elinks bug #391 (oh my)
- cvs-menu-segfault.patch: fixes elinks bug #394

* Sat Feb 07 2004 Alexey Tourbin <at@altlinux.ru> 0.9.1-alt3
- Owl patches updated:
  * Fri Feb 06 2004 Michail Litvak <mci@owl.openwall.com> 0.9.1-owl4
  - Fix yet another bug in -owl-tmp patch (Thanks to Maxim Timofeyev).

* Mon Feb 02 2004 Alexey Tourbin <at@altlinux.ru> 0.9.1-alt2
- Owl patches updated:
  * Sun Feb 01 2004 Solar Designer <solar@owl.openwall.com> 0.9.1-owl3
  - Don't leak kernel version information (uname -srm) via User-Agent by
  default.
  * Sun Feb 01 2004 Michail Litvak <mci@owl.openwall.com> 0.9.1-owl2
  - Fix bug in -owl-tmp patch (Thanks to Alexey Tourbin for report).

* Fri Jan 30 2004 Alexey Tourbin <at@altlinux.ru> 0.9.1-alt1
- 0.9.1, many new features compared to 0.4.3, see NEWS
- features revision:
  + enabled: 256 colors, SMB protocol, local CGI support
  + built-in URI rewriting kept enabled (hooks.lua prefixes still work)
- Owl patches merged in:
  * Sun Jan 25 2004 Solar Designer <solar@owl.openwall.com> 0.9.0-owl2
  - Use vitmp in textarea_edit().
  - Minor corrections to the temporary file handling patch.
  - Do not set xterm window title (it wasn't getting reset when Elinks is
  exited, the URL wasn't sanitized before being used as a part of a terminal
  escape sequence, and some xterm's and window managers are known to have
  vulnerabilities exploitable via the window title string).
  - Don't define external programs for tn3270, gopher, news, and irc URLs by
  default.
  - When invoking external programs, treat '-' as an unsafe character unless
  it is preceded by a safe non-whitespace one.
  - man page corrections and updates of the "see also" lists for Owl.
  * Wed Jan 21 2004 Michail Litvak <mci@owl.openwall.com> 0.9.0-owl1
  - Switch from Links to ELinks.
- install icons from contrib
- more docs packaged; ChangeLog not packaged (NEWS is enough)
- alt-default-lang-charset.patch disabled: system language detection
  re-implemented upstream, system charset is in progress

* Thu Nov 27 2003 Alexey Tourbin <at@altlinux.ru> 0.4.3-alt7
- 0.4.3 finally released

* Tue Sep 16 2003 Alexey Tourbin <at@altlinux.ru> 0.4.3-alt6rc2
- alt-owl-tmp.patch disabled again since it breaks things down

* Wed Sep 10 2003 Alexey Tourbin <at@altlinux.ru> 0.4.3-alt4rc2
- alt-owl-tmp.patch resurrected (the use of tempnam(3) eliminated)
- gcc -Werror enabled

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 0.4.3-alt3rc2
- 0.4.3rc2
- cpan (=search.cpan.org) added to hooks.lua

* Fri Jun 20 2003 Alexey Tourbin <at@altlinux.ru> 0.4.3-alt2rc1
- rebuild to fit to new lua4-devel package

* Tue Jun 10 2003 Alexey Tourbin <at@altlinux.ru> 0.4.3-alt1rc1
- 0.4.3rc1

* Tue May 27 2003 Alexey Tourbin <at@altlinux.ru> 0.4.2-alt8
- cvs fixes (20030526); patches reordered
- increase height for big dialogs (alt-dialog-height.patch)
- use colors and frames for all terminals by default

* Thu May 08 2003 Alexey Tourbin <at@altlinux.ru> 0.4.2-alt7
- cvs fixes (REL_0_4 20030507)
- added alt (=search.altlinux.ru) and atmsk (=atmks.ru) hooks

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt6
- new alternatives config format

* Fri Mar 14 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt5
- PreReq fixes

* Wed Mar 12 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt4
- update buildreqs

* Tue Mar 11 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt3
- move to new alternatives scheme
  warning to mantainter: alternatives removing must be in preun
- added packager tag

* Fri Mar 07 2003 Alexey Tourbin <at@altlinux.ru> 0.4.2-alt2
- alt-default-lang-charset (according to locale settings) patch

* Sun Jan 26 2003 Alexey Tourbin <at@altlinux.ru> 0.4.2-alt1
- 0.4.2 (a few fixes)
- alt-owl-tmp patch disabled; this requires extra study

* Tue Jan 21 2003 Alexey Tourbin <at@altlinux.ru> 0.4.1-alt1cvs
- 0.4.1 (bugfix release) + current-stable fixes (cvs-20030120 patch;
  my env-http_proxy patch accepted)
- fixed %%postun code
- lua-scripts-fixes patch integrated (PLD Team)
- yandex search added to hooks.lua (alt-hooks patch)
- COPYING points to /usr/share/license/GPL-2

* Tue Dec 24 2002 Alexey Tourbin <at@altlinux.ru> 0.4.0-alt1
- initial build (based on links1-0.98-alt3)
