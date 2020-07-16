%define _unpackaged_files_terminate_build 1

Name: xosview
Version: 1.22
Release: alt1
Summary: An X Window System utility for monitoring system resources
License: GPL-2.0 and BSD-4-Clause-UC
Group: Monitoring
Url: http://xosview.sourceforge.net/

# https://github.com/hills/xosview.git
Source: %name-%version.tar
Source1: xosview16.png
Source2: xosview32.png
Source3: xosview48.png

Patch: xosview-1.21-alt-e2k.patch

BuildRequires: gcc-c++ libXpm-devel libX11-devel desktop-file-utils

%description
The %name utility displays a set of bar graphs which show the current
system state, including memory usage, CPU usage, system load, etc.
Xosview runs under the X Window System.

%prep
%setup
%patch -p1

%build
%make_build OPTFLAGS="${CFLAGS:-%optflags}"

cat > %{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%name
GenericName=OS Resource Viewer
Comment=
Exec=xosview
Icon=xosview
Categories=Utility;System;Monitor;
Terminal=false
EOF

%install
mkdir -p %buildroot{%_bindir,%_man1dir,%_x11appconfdir}
%make_install install PREFIX=%buildroot%prefix

install -pD -m644 Xdefaults %buildroot%_x11appconfdir/XOsview
install -pD -m644 %SOURCE1  %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE2  %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE3  %buildroot%_liconsdir/%name.png

desktop-file-install --dir %buildroot%_datadir/applications %{name}.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	%buildroot%_desktopdir/xosview.desktop

%files
%doc COPYING*
%doc CHANGES README.linux TODO
%config %_x11appconfdir/*
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%_liconsdir/*.png
%_niconsdir/*.png
%_miconsdir/*.png

%changelog
* Fri Jul 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.22-alt1
- Updated to upstream version 1.22.

* Wed Nov 06 2019 Michael Shigorin <mike@altlinux.org> 1.21-alt2
- E2K: fix ftbfs (patch sent upstream)
- NB: there's xosview2 2.3.1 out there too!

* Wed Nov 06 2019 Michael Shigorin <mike@altlinux.org> 1.21-alt1
- 1.21

* Fri Oct 06 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.19-alt1
- Updated to upstream version 1.19.

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.8.3-alt4.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for xosview

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt4.1
- NMU: converted debian menu to freedesktop

* Sun Aug 02 2009 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt4
- Fixed build with fresh toolchain.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt3
- Fixed build with fresh gcc.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt2
- Removed obsolete %%update_menus/%%clean_menus calls.

* Tue Mar 21 2006 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt1
- Updated to 1.8.3.
- Fixed build with X11 in /usr.
- Updated build dependencies.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.2-alt1.1
- Rebuilt with libstdc++.so.6.

* Thu Sep 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.8.2-alt1
- Updated to 1.8.2.

* Fri Jan 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.8.0-alt5
- Fix build with gcc3.3.

* Thu Sep 11 2003 Dmitry V. Levin <ldv@altlinux.org> 1.8.0-alt4
- Updated build dependencies.

* Wed Nov 27 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8.0-alt3
- Fixed menu entry (#0001626).
- Additional convention enforcement on patch file names.

* Thu Oct 24 2002 Stanislav Ievlev <inger@altlinux.ru> 1.8.0-alt2
- rebuild with gcc3

* Wed Jun 05 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8.0-alt1
- 1.8.0
- Updated urls.

* Tue Mar 12 2002 Stanislav Ievlev <inger@altlinux.ru> 1.7.3-ipl9mdk
- Rebuilt
- Added rpath patch from RH/MDK

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.7.3-ipl8mdk
- RE adaptions.

* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 1.7.3-8mdk
- Rebuild with gcc-2.96 & glibc-2.2

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.7.3-7mdk
- automatically added BuildRequires

* Mon Jul 10 2000 dam's <damien@mandrakesoft.com> 1.7.3-6mdk
- minor specfile correction.

* Mon Jul 03 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.7.3-5mdk
- chmouelization
- build against new libstdc++

* Wed May 03 2000 dam's <damien@mandrakesoft.com> 1.7.3-4mdk
- Corrected icons.

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 1.7.3-3mdk
- Convert gif icon to xpm.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 1.7.3-2mdk
- Added menu entry.

* Fri Mar 31 2000 dam's <damien@mandrakesoft.com> 1.7.3-1mdk
- upgrade to 1.7.3

* Fri Jan 21 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.7.2-4mdk

- fixed build on sparc.

* Wed Jan 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.7.2-3mdk
- libtoolize --force.
- use egcs on alpha.

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Enable SMP build/check

* Sat Jul 17 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 1.7.2

* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Mon Mar  8 1999 Jeff Johnson <jbj@redhat.com>
- updated to 1.7.1.

* Wed Mar  3 1999 Matt Wilson <msw@redhat.com>
- updated to 1.7.0

* Fri Feb  5 1999 Bill Nottingham <notting@redhat.com>
- build against new libstdc++, build on arm

* Tue Dec 22 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.6.2.a.

* Tue Jun 16 1998 Jeff Johnson <jbj@redhat.com>
- add sparc/alpha functionality.
- add %clean

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Mon Jun 01 1998 Erik Troan <ewt@redhat.com>
- how the hell did this get setuid root?

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5.1 (so that it compiles with egcs)
- buildroot

* Tue Nov  4 1997 Erik Troan <ewt@redhat.com>
- commented out line causing core dumps when exiting

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
