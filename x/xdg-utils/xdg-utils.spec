Name: xdg-utils
Version: 1.1.3
Release: alt7

Summary: A set of command line tools that assist applications with a variety of desktop integration tasks

License: MIT
Group: System/Base
Url: https://www.freedesktop.org/wiki/Software/xdg-utils/

# Source-url: https://portland.freedesktop.org/download/xdg-utils-%version.tar.gz
Source: %name-%version.tar

Patch0: added-xdg-su-1.1.0rc1-alt.patch
Patch1: xdg-open-opera.patch
Patch2: xdg-su-added-lxde-and-gksu-and-beesu-support-1.1.2.patch
Patch5: xdg-open-generic-mimeapps.patch
Patch6: xdg-su-use-gnomesu-for-xfce-if-available.patch
Patch7: xdg-open-fix-ifs-use.patch
Patch8: xdg-open-kde5.patch
Patch9: xdg-su-kde5.patch
Patch10: xdg-common-detect-de-generic.patch
Patch11: xdg-open-added_open_lxqt.patch
Patch12: xdg-open-fix-open-url-in-lxde.patch
Patch13: xdg-desktop-menu-dummy.patch
Patch14: xdg-email-detect-thunderbird-kde5.patch
Patch15: xdg-email-detect-thunderbird-mate.patch
Patch16: xdg-su-xvt.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 25 2007
BuildRequires: xmlto w3m

AutoReq: no
Requires: coreutils, file, gawk, grep, procps, sed, sh, which, xprop, xset

%description
Xdg-utils is a set of command line tools that assist applications with
a variety of desktop integration tasks. About half of the tools focus on
tasks commonly required during the installation of a desktop application
and the other half focuses on integration with the desktop environment
while the application is running. Even if the desktop components of your
application are limited to an installer, configuration or management tool,
Xdg-utils provides you with an easy way to enhance the usage experience
of your customers by improving the integration of these components in
the user's environment.

The following scripts are provided at this time:
* xdg-desktop-menu      Install desktop menu items
* xdg-desktop-icon      Install icons to the desktop
* xdg-icon-resource     Install icon resources
* xdg-mime              Query information about file type handling and
                        install descriptions for new file types
* xdg-open              Open a file or URL in the user's preferred application
* xdg-email             Send mail using the user's preferred e-mail composer
* xdg-screensaver       Control the screensaver
* xdg-su                Run as root

Testsuite for xdg-utils is available from
http://portland.freedesktop.org/wiki/TestSuite

%prep
%setup
pushd scripts
# we should _never_ patch generated files
ls *.in | sed -e 's,\(.*\)\.in$,\1,' | xargs rm -f
popd
%patch0 -p2
#patch1 -p1
%patch2 -p2
%patch5 -p1
%patch6 -p2
#patch7 -p2
#patch8 -p1
%patch9 -p1
%patch10 -p2
%patch11 -p2
%patch12 -p2
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
%autoreconf
%configure
%make_build
%make_build -C scripts scripts

%install
%makeinstall_std

%files
%_bindir/xdg-desktop-icon
%_bindir/xdg-desktop-menu
%_bindir/xdg-email
%_bindir/xdg-icon-resource
%_bindir/xdg-mime
%_bindir/xdg-open
%_bindir/xdg-screensaver
%_bindir/xdg-settings
%_bindir/xdg-su
%_man1dir/*
%doc ChangeLog README LICENSE RELEASE_NOTES TODO

%changelog
* Wed Oct 07 2020 Sergey V Turchin <zerg@altlinux.org> 1.1.3-alt7
- xdg-su: add fallback to xvt if no xterm found

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt6
- NMU: remove rpm-build-ubt from BR:

* Tue Nov 06 2018 Sergey V Turchin <zerg@altlinux.org> 1.1.3-alt5
- fix detect thunderbird for MATE

* Tue Nov 06 2018 Sergey V Turchin <zerg@altlinux.org> 1.1.3-alt4
- fix detect thunderbird for KDE

* Wed Jul 18 2018 Sergey V Turchin <zerg@altlinux.org> 1.1.3-alt3
- fix wrong xdg-desktop-menu-dummy.menu

* Fri Jul 06 2018 Anton Midyukov <antohami@altlinux.org> 1.1.3-alt2
- fix xdg-open url in LXDE (regression of the new version)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- new version 1.1.3 (with rpmrb script)

* Tue Mar 06 2018 Anton Midyukov <antohami@altlinux.org> 1.1.2-alt4
- fix xdg-open support lxqt (Closes: 34614)

* Sun Feb 11 2018 Anton Midyukov <antohami@altlinux.org> 1.1.2-alt3
- Fix detected unknown DE (e.g. wmaker or IceWM)
- use beesu for generic

* Mon Jul 03 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.2-alt2
- restore KDE5 support for xdg-su (ALT#33581)

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- new version 1.1.2 (with rpmrb script) (ALT bug 33159)

* Tue Aug 04 2015 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt12
- add KDE5 support to xdg-su and xdg-open (ALT#31161)

* Thu Feb 26 2015 Michael Shigorin <mike@altlinux.org> 1.1.0-alt11
- xdg-su: added MATE support (closes: #30458)

* Sat May 24 2014 Michael Shigorin <mike@altlinux.org> 1.1.0-alt10
- xdg-open: fix totally broken IFS use (closes: #28728)
  + thanks Maxim Suhanov for analysis

* Mon Mar 17 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0-alt9
- Drop patches for obsolete version of xdg-su.
- xdg-su: use gnomesu or su_generic for xfce.

* Wed Aug 28 2013 Fr. Br. George <george@altlinux.ru> 1.1.0-alt8
- Add support for "first wins" mimeapps.list query

* Fri Nov 30 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1.0-alt7
- Explicitly rebuild the scripts target.
- Build with w3m: need for proper *.in -> * conversion.
- Detect and control the mate-screensaver via D-Bus (patch,
  closes: 28139).
- Add MATE to the DE detector (patch).

* Tue Sep 11 2012 Mykola Grechukh <gns@altlinux.ru> 1.1.0-alt6
- use generic for LXDE if beesu not found; fixes problem of -c.

* Wed Mar 07 2012 Radik Usupov <radik@altlinux.org> 1.1.0-alt5
- Added lxde support to xdg-su

* Wed Mar 07 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt4
- add gksu support to xdg-su

* Fri Feb 17 2012 Radik Usupov <radik@altlinux.org> 1.1.0-alt3
- New upstreame snapshot (b961235b197647d)

* Sun Nov 13 2011 Michael Shigorin <mike@altlinux.org> 1.1.0-alt2
- added a patch adding opera to xdg-open browser list
  (after chromium-browser for being proprietary,
  before google-chrome for being redistributable)

* Sun Apr 24 2011 Radik Usupov <radik@altlinux.org> 1.1.0-alt1
- New release (1.1.0-rc1)

* Mon Sep 27 2010 Radik Usupov <radik@altlinux.org> 1.0.2-alt7
- Added browsers Midori and Arora

* Fri Aug 06 2010 Alexey I. Froloff <raorn@altlinux.org> 1:1.0.2-alt6
- Synced with 1.0.2+cvs20100307-1 debian package

* Wed Aug 19 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt5
- remove full path to kde binaries (drop patches 14, 30) (fix ALT #20906 again)

* Fri Jul 31 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt4
- fix path to kde4 programs (fix ALT #20906)

* Sat Jan 03 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- fix path to kfmclient (fix bug #18412)

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- fix command injection (CVE-2008-0386)
- apply patches from Fedora, Mandriva
- add xdg-su from SUSE

* Fri Sep 21 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)
- disable autoreq, add manual requires (fix bug #12863)

* Wed Apr 25 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- first build for ALT Linux Sisyphus

