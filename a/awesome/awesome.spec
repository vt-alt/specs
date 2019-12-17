Name: awesome
Version: 4.3
Release: alt3
Group: Graphical desktop/Other
License: GPL2+

Url: https://awesomewm.org/
Packager: Evgenii Terechkov <evg@altlinux.org>
Source: %name-%version.tar
Source1: %name.wmsession
Source2: %name.menu-method
Patch0:%name-%version-alt.patch

Summary: A window manager initialy based on a dwm code rewriting

BuildRequires: ImageMagick-tools asciidoctor cmake gcc-c++ gperf
BuildRequires: imlib2-devel libdbus-devel libev-devel liblua5.3-devel
BuildRequires: libncurses-devel libpango-devel libreadline-devel xmlto
BuildRequires: libxdg-basedir-devel libstartup-notification-devel
BuildRequires: libXdmcp-devel libgdk-pixbuf-devel lgi
BuildRequires: lua5.3 libpango-gir libgdk-pixbuf-gir libcairo-gobject
BuildRequires: libpcre-devel libxkbcommon-devel libxkbcommon-x11-devel libxcbutil-xrm-devel

BuildPreReq: libxcbutil-devel >= 0.3.8 libxcbutil-keysyms-devel >= 0.3.8
BuildPreReq: libxcbutil-icccm-devel >= 0.3.8 libxcbutil-cursor-devel

Requires: libstartup-notification >= 0.10-alt1
Requires: lgi >= 0.9.1
Requires: libpango-gir
Requires: libcairo-gobject
Requires: libgdk-pixbuf-gir

%description
awesome is a window manager initialy based on a dwm code rewriting. It's
extremely fast, small, dynamic and awesome.

%prep
%setup -n %name-%version
%patch0 -p1

%build
echo -n "v%version" >| .version_stamp
mkdir -p build
pushd build
CFLAGS="%optflags" \
CXXFLAGS="%optflags" \
cmake \
  -Wno-dev \
  -DPREFIX=%prefix \
  -DAWESOME_DOC_PATH=%_docdir/%name-%version \
  -DCMAKE_INSTALL_PREFIX=%prefix \
  -DSYSCONF_INSTALL_DIR=%_sysconfdir \
  -DSYSCONFDIR=%_sysconfdir \
  -DCOMPRESS_MANPAGES=OFF \
%if %_lib == lib64
  -DLIB_SUFFIX=64 \
%endif
  ..

%make_build
popd

%install
pushd build
# Fix manpages:
for i in `find manpages -type f -iname '*.[0-9]'`; do
    sed -i '1i.\\" -*- mode: troff; coding: utf-8 -*-' $i
# "
done

%makeinstall DESTDIR=%buildroot install
popd
install -D -m 644 %name.desktop %buildroot/%_desktopdir/%name.desktop
touch %buildroot%_sysconfdir/xdg/%name/menu.lua
install -D -m 644 %SOURCE1 %buildroot%_sysconfdir/X11/wmsession.d/05%name
install -D -m 755 %SOURCE2 %buildroot%_sysconfdir/menu-methods/%name

%find_lang %name

%files -f %name.lang
%_bindir/*
%_sysconfdir/menu-methods/%name
%_sysconfdir/xdg/%name
%ghost %_sysconfdir/xdg/%name/menu.lua
%_sysconfdir/X11/wmsession.d/*
%_man1dir/aw*
%_man5dir/aw*
%_mandir/*/man1/aw*
%_mandir/*/man5/aw*
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/xsessions/%name.desktop
%doc LICENSE build/docs/*.md

%changelog
* Sat Jun  1 2019 Terechkov Evgenii <evg@altlinux.org> 4.3-alt3
- Add /usr/share/xsessions/awesome.desktop (ALT#36830)

* Thu Apr  4 2019 Terechkov Evgenii <evg@altlinux.org> 4.3-alt2
- Add libgdk-pixbuf-gir to Requires (ALT#36499)

* Fri Feb 22 2019 Terechkov Evgenii <evg@altlinux.org> 4.3-alt1
- 4.3 (Too Long)

* Thu Aug 24 2017 Terechkov Evgenii <evg@altlinux.org> 4.2-alt1
- 4.2 (Human after all)

* Mon Mar 20 2017 Terechkov Evgenii <evg@altlinux.org> 4.1-alt1
- 4.1 (Technologic)

* Fri Feb 24 2017 Terechkov Evgenii <evg@altlinux.org> 4.0-alt1
- 4.0 (Harder, Better, Faster, Stronger)

* Sat Jan 28 2017 Terechkov Evgenii <evg@altlinux.org> 3.5.9-alt3
- Fix build

* Mon Oct 17 2016 Terechkov Evgenii <evg@altlinux.org> 3.5.9-alt2
- Rebuild with lua5.3

* Mon Mar 21 2016 Terechkov Evgenii <evg@altlinux.org> 3.5.9-alt1
- 3.5.9 (Mighty Ravendark)

* Sun Jan 31 2016 Terechkov Evgenii <evg@altlinux.org> 3.5.8-alt1
- 3.5.8 (Major Tom)

* Mon Jan 18 2016 Terechkov Evgenii <evg@altlinux.org> 3.5.7-alt1
- 3.5.7 (Space Oddity)

* Mon Jan 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.5.6-alt1
- 3.5.6 (For Those About To Rock)

* Tue Apr 22 2014 Terechkov Evgenii <evg@altlinux.org> 3.5.5-alt1
- 3.5.5 (Kansas City Shuffle)

* Fri Apr  4 2014 Terechkov Evgenii <evg@altlinux.org> 3.5.4-alt1
- 3.5.4

* Sun Mar 30 2014 Terechkov Evgenii <evg@altlinux.org> 3.5.3-alt1
- 3.5.3 (Crazy)

* Fri Nov 15 2013 Terechkov Evgenii <evg@altlinux.org> 3.5.2-alt1
- 3.5.2 (The Fox)

* Wed Apr 10 2013 Terechkov Evgenii <evg@altlinux.org> 3.5.1-alt1
- 3.5.1 (Ruby Tuesday)

* Mon Jan 21 2013 Terechkov Evgenii <evg@altlinux.org> 3.5-alt4
- We need libcairo-gobject

* Mon Dec 24 2012 Terechkov Evgenii <evg@altlinux.org> 3.5-alt3
- Oops. Adding missing requires

* Sat Dec 22 2012 Terechkov Evgenii <evg@altlinux.org> 3.5-alt2
- 3.5 (Last Christmas)

* Tue Dec 18 2012 Terechkov Evgenii <evg@altlinux.org> 3.5-alt1.rc2
- 3.5-rc2 (I'll Kill Her)

* Tue Dec  4 2012 Terechkov Evgenii <evg@altlinux.org> 3.5-alt1.rc1
- 3.5-rc1 (Dirty Magic)

* Wed Oct  3 2012 Terechkov Evgenii <evg@altlinux.org> 3.4.13-alt2
- Set default background according to WM Policy 1.1

* Sun Sep  9 2012 Terechkov Evgenii <evg@altlinux.org> 3.4.13-alt1
- 3.4.13 (Octopus)

* Sun Sep  2 2012 Terechkov Evgenii <evg@altlinux.org> 3.4.12-alt1
- 3.4.12 (Starlight)

* Fri Apr  6 2012 Terechkov Evgenii <evg@altlinux.org> 3.4.10-alt2
- Fix FTBFS with new glib

* Wed May 25 2011 Terechkov Evgenii <evg@altlinux.org> 3.4.10-alt1
- 3.4.10 (Exploder)

* Sat May 14 2011 Terechkov Evgenii <evg@altlinux.org> 3.4.9-alt3
- Manpages fixed in spec (thanks to legion@)
- git-20110508

* Sat Apr  9 2011 Terechkov Evgenii <evg@altlinux.org> 3.4.9-alt2
- Fix build with new cmake (Dirty hack)

* Thu Jan 20 2011 Terechkov Evgenii <evg@altlinux.org> 3.4.9-alt1
- 3.49 (Smack)

* Thu Dec  2 2010 Terechkov Evgenii <evg@altlinux.org> 3.4.8-alt1
- 3.4.8 (Never Know)

* Thu Sep 16 2010 Terechkov Evgenii <evg@altlinux.org> 3.4.7-alt1
- 3.4.7 (Left Of Center)

* Mon Jul 19 2010 Terechkov Evgenii <evg@altlinux.ru> 3.4.6-alt1
- 3.4.6 (Hooch)

* Wed May 19 2010 Terechkov Evgenii <evg@altlinux.ru> 3.4.5-alt1
- 3.4.5 (Close To You)

* Wed Mar 10 2010 Terechkov Evgenii <evg@altlinux.ru> 3.4.4-alt1
- 3.4.4 (Jet Sex)

* Tue Feb 23 2010 Terechkov Evgenii <evg@altlinux.ru> 3.4.3-alt2
- Lets conform to ALT Linux IconPathPolicy: http://www.altlinux.org/IconPathsPolicy

* Wed Jan  6 2010 Terechkov Evgenii <evg@altlinux.ru> 3.4.3-alt1
- 3.4.3 (Engines)

* Sun Dec 27 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4.2-alt1
- 3.4.2 (For The Restless)

* Wed Oct 21 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt4
- 3.4 (Closing In)

* Mon Oct 19 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt3.rc3
- Set minimal required libstartup-notification (ALT#21983, thanks to wrar@, barabashka@)

* Sat Oct 10 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt2.rc3
- 3.4-rc3 (Black Star)

* Mon Sep 28 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt2.rc2
- 3.4-rc2 (Piku)

* Sun Sep 27 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt2.rc1
- Default config fixed

* Sat Sep 26 2009 Terechkov Evgenii <evg@altlinux.ru> 3.4-alt1.rc1
- 3.4-rc1 (Uprising)

* Sat Sep 19 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.4-alt2
- Sources cleanup (thanks to kas@)

* Wed Sep  9 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.4-alt1
- 3.3.4 (Mercury)

* Sun Aug 30 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.3-alt1
- 3.3.3 (Firelight)

* Wed Aug  5 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.2-alt1
- 3.3.2 (Half Moon)

* Fri Jul 17 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.1-alt2
- Generic X error format message fixed

* Thu Jul 16 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3.1-alt1
- 3.3.1

* Tue Jun 16 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3-alt2
- Ignore size hints by default, @kas
- git-20090616

* Thu Jun  4 2009 Terechkov Evgenii <evg@altlinux.ru> 3.3-alt1
- 3.3

* Fri May 29 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2.1-alt4
- Rebuild with libxcb-1.3

* Sun Apr 26 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2.1-alt3
- ALT-specific patch extracted
- Buildrequires updated
- git-20090426 from upstream (to work with libxcbutil-0.3.4)
- Version stamp now updated correctly
- Dependency to gxmessage suppressed

* Sat Apr 25 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2.1-alt2
- Rebuild with libxcbutil-0.3.4

* Tue Apr 21 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Sat Mar 14 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2-alt2
- 3.2

* Mon Feb 23 2009 Terechkov Evgenii <evg@altlinux.ru> 3.2-alt1.rc3
- 3.2-rc3

* Thu Jan 22 2009 Terechkov Evgenii <evg@altlinux.ru> 3.1.1-alt3
- srpm->git migration (thanks, kas@)
- Substitute "+" to "_" in section name (kas@, c78693654a5639759decb3c606a3adb98311ed57)

* Fri Jan 16 2009 Terechkov Evgenii <evg@altlinux.ru> 3.1.1-alt2
- Patch0 added to set default background image loader to xsetroot (see #18514)

* Tue Jan 13 2009 Terechkov Evgenii <evg@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Sun Dec 21 2008 Terechkov Evgenii <evg@altlinux.ru> 3.1-alt2
- Debian-menu generation added

* Tue Dec 16 2008 Terechkov Evgenii <evg@altlinux.ru> 3.1-alt1
- 3.1

* Sun Nov 16 2008 Terechkov Evgenii <evg@altlinux.ru> 3.0-alt2
- Update spec to new filetriggers system

* Sun Oct 12 2008 Terechkov Evgenii <evg@altlinux.ru> 3.0-alt1
- Initial build for ALT Linux Sisyphus (Thanks OpenSuSE for spec)
