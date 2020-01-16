Name: xfdesktop
Version: 4.14.2
Release: alt1

Summary: Desktop manager for the Xfce Desktop Environment
Summary (ru_RU.UTF-8): Менеджер рабочего стола Xfce
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://www.xfce.org/
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: git://git.xfce.org/xfce/xfdesktop
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libthunar-devel libgarcon-devel libgarcon-gtk3-devel libxfce4panel-gtk3-devel libxfconf-devel libexo-gtk3-devel libxfce4ui-gtk3-devel
BuildRequires: intltool libSM-devel libwnck3-devel time xorg-cf-files
BuildRequires: libICE-devel libnotify-devel

Requires: exo-utils

%define _unpackaged_files_terminate_build 1

%description
%name contains a desktop manager for the Xfce Desktop Environment.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе менеджер рабочего стола для окружения Xfce.

%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfdesktop_version_tag configure.ac.in
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-gio-unix \
	--enable-notifications \
	--enable-thunarx \
	--enable-desktop-icons \
	--enable-file-icons \
	--enable-debug=minimum

%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README NEWS AUTHORS doc/README.*
%_bindir/*
%_desktopdir/*
%_liconsdir/*
%_niconsdir/*
%_iconsdir/hicolor/scalable/apps/*
%_pixmapsdir/*
%_mandir/man?/*
%_datadir/backgrounds/xfce

%changelog
* Mon Jan 13 2020 Mikhail Efremov <sem@altlinux.org> 4.14.2-alt1
- Use Vcs rpm tag.
- Don't use rpm-build-licenses.
- Updated to 4.14.0.

* Mon Sep 30 2019 Mikhail Efremov <sem@altlinux.org> 4.14.1-alt2
- Fixed package version.
- Patches from upstream:
    + Show file names in tooltips (Bug #15899).
    + fallback style: Highlight selected icons (Bug #15866).

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt1
- Updated to 4.14.0.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 4.13.6-alt1
- Updated to 4.13.6.

* Sun Jun 30 2019 Mikhail Efremov <sem@altlinux.org> 4.13.5-alt1
- Updated to 4.13.5.

* Sat May 18 2019 Mikhail Efremov <sem@altlinux.org> 4.13.4-alt1
- Updated to 4.13.4.

* Mon Mar 11 2019 Mikhail Efremov <sem@altlinux.org> 4.13.3-alt1
- Drop libglade-devel from BR.
- Updated to 4.13.3.

* Tue Aug 07 2018 Mikhail Efremov <sem@altlinux.org> 4.13.2-alt1
- Update url.
- Require exo-utils.
- Updated to 4.13.2.

* Mon Jun 26 2017 Mikhail Efremov <sem@altlinux.org> 4.12.4-alt1
- Enabled debug (minimum level).
- Updated to 4.12.4.

* Mon Jul 20 2015 Mikhail Efremov <sem@altlinux.org> 4.12.3-alt1
- Updated to 4.12.3.

* Mon May 18 2015 Mikhail Efremov <sem@altlinux.org> 4.12.2-alt1
- Updated to 4.12.2.

* Mon Mar 23 2015 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt1
- Updated to 4.12.1.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Mon Sep 15 2014 Mikhail Efremov <sem@altlinux.org> 4.11.8-alt1
- Updated to 4.11.8.

* Mon Aug 11 2014 Mikhail Efremov <sem@altlinux.org> 4.11.7-alt1
- Updated to 4.11.7.

* Mon Apr 07 2014 Mikhail Efremov <sem@altlinux.org> 4.11.6-alt1
- Updated to 4.11.6.

* Mon Mar 31 2014 Mikhail Efremov <sem@altlinux.org> 4.11.5-alt1
- Updated to 4.11.5.

* Tue Mar 18 2014 Mikhail Efremov <sem@altlinux.org> 4.11.4-alt1
- Updated to 4.11.4.

* Thu Feb 20 2014 Mikhail Efremov <sem@altlinux.org> 4.11.3-alt1
- Updated to 4.11.3.

* Tue Dec 24 2013 Mikhail Efremov <sem@altlinux.org> 4.11.2-alt1
- Package README.kiosk and README.xfconf.
- Updated to 4.11.2.

* Fri Nov 22 2013 Mikhail Efremov <sem@altlinux.org> 4.11.1-alt1.git20131119
- Fix Xfce name (XFce,XFCE -> Xfce).
- Upstream git snapshot.

* Tue Nov 05 2013 Mikhail Efremov <sem@altlinux.org> 4.11.1-alt1.git20131105
- Upstream git snapshot.

* Thu Oct 17 2013 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt2.git20131014
- Upstream git snapshot.

* Mon Sep 30 2013 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Drop obsoleted patches.
- Updated to 4.11.0.

* Mon Mar 11 2013 Mikhail Efremov <sem@altlinux.org> 4.10.2-alt1
- Updated to 4.10.2.

* Wed Feb 06 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt5
- Set default backdrop if current one is not valid.
- Updated "Fix backgrounds search path" patch from upstream.

* Thu Jul 05 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt4
- fix use-after-free in xfdesktop_regular_file_icon_peek_tooltip
  (by Stefan Seyfried, patch from Xfce bug #9059).

* Tue Jun 26 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt3
- Really fix backgrounds search path.

* Mon Jun 25 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt2
- Fix backgrounds search path.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.3-alt1
- Updated to 4.9.3.

* Fri Apr 13 2012 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- Updated to 4.9.2.

* Wed Mar 07 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Updated to 4.9.0.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt1
- Drop obsoleted patches.
- Updated to 4.8.3.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt3
- Updated Russian documentation.
- Updated Russian translation.

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt2
- Fix moving files to the desktop with shift & drag (from upstream).
- Updated Russian translation (by Artem Zolochevskiy).

* Sun Apr 24 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt1
- Remove old unused xfce4-menumethod file.
- Drop obsoleted patches.
- Updated to 4.8.2.

* Sat Feb 26 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt2
- Patch from upstream:
    + Fix crash on focus in when items are selected.
- Fix crash on verifying file validness (closes: #25161).

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Updated to 4.8.1.
- Drop old patches.

* Wed Jan 26 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Patches from upstream git:
    + Use Name field as display name of desktop files.
    + Handle volume changes in a timeout.
    + Support absolute icon paths in desktop files.
- Drop xfce-education-directory-icon.patch (obsolete).
- Remove old Ubuntu's patches.
- Spec cleanup, tar.bz2 -> tar.
- Updated to 4.8.0.

* Tue Sep 01 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Added education category icon and patch.

* Tue May 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Russian translation updated

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Wed Dec 12 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt2
- fix menu "Eject" for ejectable devices

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release
- add patches from Ubuntu 7.04

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sat Dec 30 2006 ALT QA Team Robot <qa-robot@altlinux.org> 4.3.99.2-alt1.1
- Rebuilt due to libdbus-1.so.2 -> libdbus-1.so.3 soname change.

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  4.3.99.1-alt2
- Fix buildreq and cleanup spec

* Sat Sep 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- 4.4rc1

* Tue Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Feb 19 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt2
- Fixed bug #6141.

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.99.3-alt1
- 4.1.99.3

* Mon Nov 01 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.91-alt1
- 4.1.91

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.6-alt1
- 4.0.6
- Fixed menu (thanks to zerg@).

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Thu Jan 22 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3-alt2
- Changed menu title to "ALT Linux"

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Tue Dec 23 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Tue Nov 18 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Sep 26 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Mon Sep 22 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt2
- Added rough system menu support (works only for russian).
  Thanks to Eugene A. Suchkov.

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- 3.99.2

* Mon Jul 14 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.1-alt0.9
- 3.99.1

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 3.90.0-alt0.9
- First version of RPM package for Sisyphus.
- Spec derived from original version.
