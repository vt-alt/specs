Name: apt-indicator
Version: 0.3.12
Release: alt5

Summary: Applet for indication that newer packages are available
License: GPL
Group: System/Configuration/Packaging
Url: http://apt-indicator.sourceforge.net/
Packager: Sergey V Turchin <zerg@altlinux.org>

Source: %name-%version.tar

Provides: egg = %version-%release, alt-update = %version-%release
Obsoletes: egg < %version-%release, alt-update < %version-%release
Requires: qt5-svg
Requires: /usr/bin/xdg-su /usr/sbin/synaptic

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ libstdc++-devel qt5-base-devel qt5-tools
BuildRequires: docbook-dtds docbook-style-xsl help2man libapt-devel
BuildRequires: xml-common xsltproc
#BuildRequires: libdb4.4-devel

%description
This package contains simple applet both for Gnome and KDE which
made notifications for users that newer packages are available.


%prep
%setup -q -n %name-%version
%qmake_qt5 "CONFIG += release debug_info"

%build
%make
%make -C doc
lrelease-qt5 checker/checker.pro
lrelease-qt5 agent/agent.pro
help2man --output=apt-indicator.1 --no-info apt-indicator ||:

%install
%make INSTALL_ROOT=%buildroot install

# icons
install -Dm 0644 pixmaps/package-available.png %buildroot/%_iconsdir/hicolor/22x22/apps/apt-indicator.png
install -Dm 0644 pixmaps/light/package-available.svg %buildroot/%_iconsdir/hicolor/scalable/apps/apt-indicator.svg

mkdir -p %buildroot/%_datadir/%name/translations/
install -m644 translations/apt_indicator_*.qm %buildroot/%_datadir/%name/translations/
mkdir -p %buildroot/%_man1dir/
[ -f %{name}.1 ] \
    && install -m644 %{name}.1 %buildroot/%_man1dir/
mkdir -p %buildroot/%_datadir/applications/
install -m644 %name.desktop %buildroot/%_datadir/applications/%name.desktop

for d in %_sysconfdir/xdg/autostart
do
mkdir -p %buildroot/$d/
install -m644 %name.desktop %buildroot/$d/%name.desktop
sed -i 's|\(^Exec=.*\)|\1 --autostarted|' %buildroot/$d/%name.desktop
done

# docs
ln -sf %_docdir/%name-%version/html %buildroot/%_datadir/%name/doc
mkdir -p %buildroot/%_datadir/%name/pixmaps


%files
%doc doc/html doc/images NEWS TODO README
%_bindir/*
#%_man1dir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_sysconfdir/xdg/autostart/apt-indicator.desktop
%_iconsdir/hicolor/*/apps/apt-indicator.*

%changelog
* Wed Sep 04 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.3.12-alt5
- really adapt c flags for C++14 (used in the last source changes
  here & in APT in 0.3.12-alt4), so that they really have effect on e2k

* Thu Jun 13 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.12-alt4
- Rebuilt with new apt

* Wed Feb 20 2019 Ivan A. Melnikov <iv@altlinux.org> 0.3.12-alt3
- build with debuginfo

* Thu Jan 24 2019 Sergey V Turchin <zerg at altlinux dot org> 0.3.12-alt2
- fix requires

* Mon Jan 21 2019 Sergey V Turchin <zerg at altlinux dot org> 0.3.12-alt1
- use only internal icons
- don't show dialog at exit

* Wed Jun 27 2018 Sergey V Turchin <zerg at altlinux dot org> 0.3.11-alt1%ubt
- wait after startup only if autostarted

* Tue Jun 26 2018 Sergey V Turchin <zerg at altlinux dot org> 0.3.10-alt1%ubt
- fix raise info window

* Thu Jun 21 2018 Sergey V Turchin <zerg at altlinux dot org> 0.3.9-alt1%ubt
- raise info window on second app startup if tray is already visible

* Fri Dec 15 2017 Sergey V Turchin <zerg at altlinux dot org> 0.3.8-alt1%ubt
- remove "Run program" button from info window

* Fri Dec 15 2017 Sergey V Turchin <zerg at altlinux dot org> 0.3.7-alt1%ubt
- fix retrive update checker info

* Tue Nov 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.6-alt1.qa1
- Rebuilt with libapt-pkg-libc6.9-6.so.6.

* Tue Aug 02 2016 Sergey V Turchin <zerg at altlinux dot org> 0.3.6-alt1
- don't package pixmaps
- extend hide timer when app in use

* Tue Jul 19 2016 Sergey V Turchin <zerg at altlinux dot org> 0.3.5-alt1
- use help text images from from current icon theme

* Fri Jul 15 2016 Sergey V Turchin <zerg at altlinux dot org> 0.3.4-alt1
- decrease default interval between checkings

* Thu Jul 14 2016 Sergey V Turchin <zerg at altlinux dot org> 0.3.3-alt1
- load help browser control button icons from current theme
- set window icon

* Tue Jul 12 2016 Sergey V Turchin <zerg at altlinux dot org> 0.3.2-alt1
- activate info window
- don't show dialog when system tray not available

* Fri Jul 08 2016 Sergey V Turchin <zerg at altlinux dot org> 0.3.1-alt1
- prefer icons from current icon theme
- update internal icons from Breeze icon theme

* Wed Jul 06 2016 Sergey V Turchin <zerg at altlinux dot org> 0.3.0-alt1
- port to Qt5

* Tue Oct 13 2015 Sergey V Turchin <zerg at altlinux dot org> 0.2.11-alt1
- fix system tray icon pixmap

* Thu May 28 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.10-alt1.1.1.1
- Rebuilt for:
 + libapt-pkg-libc6.9-6.so.5.
 + gcc5 C++11 ABI.

* Wed Sep 10 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.10-alt1.1.1
- Rebuilt with libapt-pkg-libc6.9-6.so.4.

* Tue Mar 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1.1
- NMU: rebuild with libapt

* Wed Oct 09 2013 Sergey V Turchin <zerg at altlinux dot org> 0.2.10-alt0.M70P.1
- built for M70P

* Wed Oct 09 2013 Sergey V Turchin <zerg at altlinux dot org> 0.2.10-alt1
- minimize checker process priority

* Mon Apr 15 2013 Sergey V Turchin <zerg at altlinux dot org> 0.2.9-alt1
- ionice checking process

* Mon Jan 14 2013 Sergey V Turchin <zerg at altlinux dot org> 0.2.8-alt2
- built with _FILE_OFFSET_BITS=64

* Tue Oct 09 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.8-alt1
- fix to build with gcc 4.7

* Mon Mar 26 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.7-alt0.M60P.1
- built for M60P

* Mon Mar 26 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.7-alt1
- warn correctly if assume a user's identity utility not found

* Fri Mar 23 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.6-alt0.M60P.1
- built for M60P

* Fri Mar 23 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.6-alt1
- fix execution error dialog text

* Wed Mar 21 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.5-alt0.M60P.1
- built for M60P

* Thu Mar 15 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.5-alt1
- show replaced packages separately

* Wed Mar 14 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.4-alt2.M60P.1
- built for M60P

* Wed Mar 14 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.4-alt3
- fix russian translation

* Wed Mar 14 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.4-alt1.M60P.1
- built for M60P

* Wed Mar 14 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.4-alt2
- update russian translation

* Wed Mar 14 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.4-alt0.M60P.1
- built for M60P

* Wed Mar 14 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.4-alt1
- fix warning message

* Tue Mar 13 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.3-alt0.M60P.1
- built for M60P

* Tue Mar 13 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.3-alt1
- show executed command line when error

* Wed Mar 07 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt0.M60P.1
- built for M60P

* Wed Mar 07 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt1
- simplify checker code to avoid crash

* Wed Feb 29 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt0.M60P.1
- built for M60P

* Wed Feb 29 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- execute programs via xdg-su

* Mon Feb 06 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt0.M60P.1
- built for M60P

* Mon Jan 23 2012 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1
- fix double startup
- fix update systray status

* Thu Jun 02 2011 Sergey V Turchin <zerg at altlinux dot org> 0.1.19-alt1
- rename apt-indicator-agent process to avoid double startup (ALT#25692)

* Wed Apr 20 2011 Sergey V Turchin <zerg at altlinux dot org> 0.1.18-alt2
- fix build requires

* Fri Oct 01 2010 Sergey V Turchin <zerg at altlinux dot org> 0.1.18-alt1
- update "working" pixmap

* Thu Sep 30 2010 Sergey V Turchin <zerg at altlinux dot org> 0.1.17-alt1
- update pixmaps

* Fri Sep 10 2010 Sergey V Turchin <zerg at altlinux dot org> 0.1.16-alt1
- increase initial check timeout to 60 sec

* Tue Apr 27 2010 Sergey V Turchin <zerg at altlinux dot org> 0.1.15-alt1
- save information window geometry when hide
- fix small bug in configurator

* Mon Dec 21 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1.14-alt1.1
- NMU:
  + rebuilt with apt 0.5.15lorg2-alt31.1

* Wed Dec 16 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.14-alt0.M51.1
- built for M51

* Wed Dec 16 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.14-alt1
- allow to start upgrade program separately (ALT#22078)

* Tue Dec 15 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.13-alt1
- fix popup information window when closed
- fix reset to default settings

* Tue Nov 24 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.12-alt1
- allow restore default settings

* Mon Sep 14 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.11-alt2
- remove /usr/share/autostart entry

* Mon Aug 10 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.11-alt1
- fix detect running copy

* Mon Jun 22 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.10-alt1
- show tray icon when agent already started and icon hidden

* Tue Jun 09 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.9-alt1
- hide system tray icon when do nothing

* Fri May 08 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.8-alt1
- move agent to separate process to facilitate autostart

* Fri Apr 24 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.7-alt1
- allow to start repositories configurator
- minor usability improvements

* Tue Apr 14 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.6-alt0.M50.1
- built for M50

* Mon Apr 13 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.6-alt1
- ask for autostart at exit

* Mon Apr 13 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.5-alt1
- ignore fetch cdrom errors

* Fri Apr 10 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.4-alt0.M50.1
- built for M50

* Fri Apr 10 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.4-alt1
- allow to switch off popup messages
- fix to don't change state when sources.list-s not configured
- fix help browser behavior
- update Russian translation

* Wed Apr 08 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.3-alt0.M50.1
- built for M50

* Wed Apr 08 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.3-alt1
- update icons
- show popup message when updates available

* Wed Apr 08 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.2-alt1
- improve updating program configuration

* Tue Apr 07 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt0.M50.1
- built for M50

* Mon Apr 06 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt1
- fix menu translations
- update info window if shown
- close info window on upgrade program exit
- add xdg autostart entry

* Fri Dec 12 2008 Dmitry V. Levin <ldv@altlinux.org> 0.1.0-alt1.1
- Removed obsolete %%update_menus/%%clean_menus calls.
- Built with libapt-pkg-libc6.9-6.so.2.

* Mon Nov 10 2008 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1
- port to Qt4

* Wed Apr 28 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.4-alt1
- 0.0.4 rc1

* Wed Mar 10 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.3-alt2
- update russian translation

* Tue Mar 09 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.3-alt1
- 0.0.3

* Thu Jan 15 2004 Dmitry V. Levin <ldv@altlinux.org> 0.0.2-alt5.1
- Rebuilt with apt-0.5.15cnc5.

* Tue Sep 23 2003 Sergey V Turchin <zerg at altlinux dot org> 0.0.2-alt5
- add requires to synaptic-usermode

* Tue Sep 02 2003 Sergey V Turchin <zerg at altlinux dot org> 0.0.2-alt4
- update code from cvs

* Fri Jun 20 2003 Sergey V Turchin <zerg at altlinux dot org> 0.0.2-alt3
- update from cvs

* Thu Jun 05 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.0.2-alt2
- fix Cancel button in YesNoDialog

* Wed Jun 04 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.0.2-alt1
- new version

* Thu May 29 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.1-alt2
- added documentation

* Tue May 27 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.0.1-alt1
- update from cvs
- new version
- fix BuildRequires
- first build for Sisyphus

* Tue May 27 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.0.0-alt6
- update from cvs (fixed autostart.desktop)

* Tue May 27 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.0.0-alt5
- update from cvs
- add to %_datadir/autostart/*.desktop to %%files

* Mon May 26 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.0.0-alt4
- update from cvs
- add to %_datadir/autostart for KDE

* Mon May 26 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.0.0-alt3

* Mon May 26 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.0.0-alt2
- update from cvs
- add menu

* Mon May 26 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.0-alt1
- Initial release for Daedalus
