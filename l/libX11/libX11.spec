Name: libX11
Version: 1.6.7
Release: alt2
Epoch: 3
Summary: X11 Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: filesystem > 2.3.1-alt1
Requires: %name-locales = %version-%release
Provides: %name-ccache = %version-%release
Obsoletes: %name-ccache < %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libxcb-devel perl-Pod-Parser xorg-proto-devel xorg-util-macros xmlto xorg-sgml-doctools xorg-xtrans-devel

%description
X11 Library

%package devel
Summary: X11 Libraries and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%package locales
Summary: Xorg locales
Group: System/Internationalization
BuildArch: noarch
Conflicts: %name <= 1.1.1-alt2

%description locales
This package contains set of Xorg locales

%def_enable	ipv6
%def_disable	loadable_i18n
%def_disable	xlocaledir

%prep
%setup -q

%patch -p1

%build
%autoreconf
%configure \
	%{subst_enable ipv6} \
	%{subst_enable loadable_i18n} \
	%{subst_enable xlocaledir} \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_docdir -name \*.xml -delete
find %buildroot%_docdir -name \*.db -delete

%if_enabled loadable_i18n
rm -f %buildroot%_libdir/X11/locale/common/*.la
%endif

%files
%doc AUTHORS COPYING NEWS README
%_libdir/*.so.*
%if_enabled loadable_i18n
%_libdir/X11/locale
%endif
%dir %_datadir/X11
%_datadir/X11/X*
%_man5dir/*.5*

%files devel
%_docdir/%name
%_includedir/X11/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*.3*

%files locales
%_datadir/X11/locale

%changelog
* Thu Sep 17 2020 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.7-alt2
- fixes: CVE-2020-14363

* Wed Oct 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.7-alt1
- 1.6.7

* Mon May 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.5-alt1
- 1.6.5

* Tue Nov 29 2016 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.4-alt1
- 1.6.4

* Mon May 18 2015 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.3-alt1
- 1.6.3

* Mon Sep 09 2013 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.2-alt1
- 1.6.2

* Tue Jul 30 2013 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.1-alt1
- 1.6.1

* Tue Jun 04 2013 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.0-alt1
- 1.6.0

* Fri May 24 2013 Valery Inozemtsev <shrek@altlinux.ru> 3:1.5.99.902-alt1
- 1.6.0 RC2

* Sun Mar 10 2013 Valery Inozemtsev <shrek@altlinux.ru> 3:1.5.99.901-alt1
- 1.6.0 RC1

* Sat Jun 02 2012 Valery Inozemtsev <shrek@altlinux.ru> 3:1.5.0-alt1
- 1.5.0

* Sun May 27 2012 Valery Inozemtsev <shrek@altlinux.ru> 3:1.4.99.902-alt1
- 1.5.0 RC2

* Fri Mar 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 3:1.4.99.901-alt1
- 1.5.0 RC1

* Wed Mar 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 3:1.4.99.1-alt1
- 1.4.99.1

* Fri Jul 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:1.4.4-alt1
- 1.4.4

* Thu Jun 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:1.4.3-alt2
- enabled ipv6

* Wed Apr 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:1.4.3-alt1
- 1.4.3

* Fri Mar 18 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:1.4.2-alt1
- 1.4.2

* Mon Feb 07 2011 Alexey Tourbin <at@altlinux.ru> 3:1.4.1-alt2
- rebuilt for debuginfo

* Wed Jan 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:1.4.1-alt1
- 1.4.1

* Mon Nov 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:1.4.0-alt1
- 1.4.0

* Fri Nov 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:1.3.99.903-alt1
- 1.4 RC3

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:1.3.6-alt2
- rebuild

* Wed Sep 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:1.3.6-alt1
- 1.3.6

* Thu Aug 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:1.3.5-alt1
- 1.3.5

* Fri Jun 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:1.3.4-alt1
- 1.3.4
- drop %name-ccache subpackage

* Sun Jan 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:1.3.3-alt1
- 1.3.3

* Sat Oct 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:1.3.2-alt1
- 1.3.2

* Sun Oct 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:1.3.1-alt1
- 1.3.1

* Fri Oct 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:1.3-alt1
- 1.3

* Fri Jul 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:1.2.2-alt1
- 1.2.2

* Wed Apr 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:1.2.1-alt1
- 1.2.1

* Wed Apr 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:1.2-alt2
- fixed strange font mixups, when fontsets are still used

* Tue Feb 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:1.2-alt1
- 1.2

* Tue Nov 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.5-alt5
- reverted previous change

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.5-alt4
- fixed strange font mixups, when fontsets are still used

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.5-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.5-alt2
- added XF86Battery, XF86Bluetooth, XF86WLAN, XF86UWB to keysymdb

* Fri Sep 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.5-alt1
- 1.1.5

* Tue Jul 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.4-alt6
- fixed unbalanced parenthesis in XKBlib.h

* Mon Jun 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.4-alt5
- libX11-1.1-branch 2008-06-13
- fixed memory leak in XOpenDisplay

* Sat May 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.4-alt4
- new subpackage libX11-ccache

* Sat Mar 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.4-alt3
- disabled loadable-i18n (close #14896, #14918)

* Mon Mar 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.4-alt2
- enabled loadable-i18n
- drop compatibility directory /usr/X11R6/lib from ld.so.conf

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.4-alt1
- 1.1.4

* Mon Feb 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.3-alt8
- GIT snapshot 2008-02-24 (1a1a42a3ca1dfaf42f1094936b71c140fc030fcb):
  + XIM: Fix a hand when switching input context
  + XErrorDB updates for Render 0.9 & XFixes 4.0

* Tue Dec 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.3-alt7
- GIT snapshot 2007-12-10 (e8d4cefa0837afa149a10e981528b368485a9e38)
  + additions to the Compose file for UTF-8
  + fix the <U\x+> keysyms in the en_US.UTF-8 Compose file

* Mon Nov 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.3-alt6
- GIT snapshot 2007-10-29 (2af660c2fcd15c86c66459bfc074c190ea1462e6)
  + Two threads can request sequence sync and XID fetch simultaneously.

* Mon Oct 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.3-alt5
- GIT snapshot 2007-08-31 (11ea09745efa8de7dc82fe30ebd2393f08390957)
  + Add XF86 keyboard/monitor brightness keysyms to the keysymbdb.

* Sun Oct 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.3-alt4
- build with xcb

* Tue Aug 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.3-alt3
- GIT snapshot 2007-08-20 (21ca953337fb221b85345bf35ce1a98a0dcb2bf2)
  + Fix typo. The code <U1000000D> was used where <U10000DC> was obviously intended.

* Sun Aug 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.3-alt2
- GIT snapshot 2007-08-18 (eff33ae525337ce2026be135a26464c7b1237113):
  + Fix a mutex reference-counting bug
  + Fix SMP Compose targets
  + Add some compose sequences
  + Compose fix for Latin-1 (from Debian)
  + Add additional Euro signs to compose
  + Patch for Catalan locales

* Thu Aug 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.3-alt1
- 1.1.3

* Tue Jun 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.2-alt3
- added libX11-1.1.2-git-XGetWindowAttributes.patch: fix locking in _XimGetWindowEventmask.

* Mon Jun 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.2-alt2
- added libX11-1.1.2-git-XGetMotionEvents-arg-order.patch

* Thu Jun 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.1.1-alt7
- rollback to 1.1.1
- added libX11-1.1.1-git-el_GR.UTF-8.patch

* Mon Jun 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.2-alt1
- 1.1.2

* Tue May 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt6
- build without xcb

* Wed May 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt5
- build with xcb
- added libX11-1.1.1-git-memleak-xcb.patch

* Wed Apr 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt4
- fixed CVE-2007-1667
- added libX11-1.1.1-git-XSetSizeHintset-bug7703.patch: Fixed XSetSizeHints()
  et al wrt use of uninitialized data.

* Tue Apr 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt3
- move locales to subpackage %name-locales

* Sun Mar 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt2
- added libX11-1.1.1-git-file-descriptor-leak.patch

* Fri Dec 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt1
- 1.1.1

* Fri Nov 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1-alt1
- 1.1

* Sat Nov 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.99.2-alt1
- 1.0.99.2

* Sun Oct 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.3-alt5
- added libX11-1.0.3-git-fix_leaks_in_GetKeyboardByName.patch,
	libX11-1.0.3-git-bug2286.patch

* Wed Oct 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.3-alt4
- added libX11-1.0.3-git-double-open.patch:
	+ fix double open of compose file.

* Tue Oct 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.3-alt3
- added libX11-1.0.3-git-LockUnlockDisplay.patch

* Wed Oct 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.3-alt2
- rebuild with glibc-2.5

* Wed Sep 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.3-alt1
- 1.0.3

* Mon Sep 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.1-alt1
- 1.0.1
- disabled XLOCALEDIR environment variable support

* Sun Sep 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.3-alt2
- enabled XLOCALEDIR environment variable support

* Sun Sep 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.3-alt1
- 1.0.3

* Tue May 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt6
- added patches:
	libX11-1.0.0-NULLdereferences.patch
	libX11-1.0.0-memoryleak.patch
	libX11-1.0.0-coverity.patch

* Wed Feb 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt5
- fixed compatibility directory

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt4
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt3
- fixed requires for %name-devel

* Sun Jan 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt2
- added PreReq filesystem > 2.3.1-alt1

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.4-alt1
- Xorg-7.0RC3

* Sun Nov 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.3-alt0.1
- initial build

