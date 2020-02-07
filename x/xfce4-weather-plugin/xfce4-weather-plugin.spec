Name: xfce4-weather-plugin
Version: 0.10.0
Release: alt4.g1510e45

Summary: Weather plugin for the Xfce panel
License: GPL-2.0+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>
Vcs: git://git.xfce.org/panel-plugins/xfce4-weather-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4util-devel libxfce4ui-gtk3-devel libxfce4panel-gtk3-devel

BuildRequires: intltool libxml2-devel libsoup-devel libupower-devel
BuildRequires: exo-csource

Requires: xfce4-panel >= 4.12.0-alt2

%define _unpackaged_files_terminate_build 1

%description
%name is the plugin for the Xfce panel, that display weather information
using forecast data provided by met.no.

%prep
%setup
%patch -p1
mkdir m4
# Don't use git tag in version.
%xfce4_drop_gitvtag weather_version_tag configure.ac.in

%build
%xfce4reconf
%configure \
    --disable-static \
	--enable-maintainer-mode \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/weather
%_datadir/xfce4/panel/plugins/*.desktop
%_liconsdir/*.png

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Wed Feb 05 2020 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt4.g1510e45
- Updated Url.
- Added Vcs tag.
- Updated description.
- Upstream git snapshot.

* Wed Nov 27 2019 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt3
- Don't use rpm-build-licenses.
- Fix reading astrodata from cache.

* Fri Nov 22 2019 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt2
- Fix day/night calculation (closes: #37528).

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1
- Updated to 0.10.0.

* Sat Mar 23 2019 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1
- Updated to 0.9.1.

* Mon Sep 24 2018 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- Fix 'may be used uninitialized' warning.
- Enable debug (minimum level).
- Update url.
- Updated to 0.9.0.

* Thu Oct 12 2017 Mikhail Efremov <sem@altlinux.org> 0.8.10-alt1
- Updated to 0.8.10.

* Fri Feb 17 2017 Mikhail Efremov <sem@altlinux.org> 0.8.9-alt1
- Updated to 0.8.9.

* Thu Sep 01 2016 Mikhail Efremov <sem@altlinux.org> 0.8.8-alt1
- Updated to 0.8.8.

* Tue Apr 26 2016 Mikhail Efremov <sem@altlinux.org> 0.8.7-alt1
- Updated to 0.8.7.

* Wed Jun 24 2015 Mikhail Efremov <sem@altlinux.org> 0.8.6-alt1
- Updated to 0.8.6.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.8.5-alt2
- Rebuild with libxfce4util-4.12.

* Mon Dec 29 2014 Mikhail Efremov <sem@altlinux.org> 0.8.5-alt1
- Updated to 0.8.5.

* Wed Nov 05 2014 Mikhail Efremov <sem@altlinux.org> 0.8.4-alt1
- Updated to 0.8.4.

* Wed Oct 15 2014 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt5
- Rebuild with upower-0.99.1

* Mon Oct 13 2014 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt4
- Patches from upstream git:
  + Support upower-0.99 (Xfce bug #10922)..
  + Switch to met.no locationforecastLTS-1.2 API (Xfce bug #10916).
  + Make plugin ready for met.no locationforecast-1.2 API
    (Xfce bug #10916).

* Fri Mar 28 2014 Paul Wolneykien <manowar@altlinux.org> 0.8.3-alt3
- Rebuild with upower v0.99.0

* Wed Jun 05 2013 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt2
- Don't package *.la files.

* Tue Feb 19 2013 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1
- Updated to 0.8.3.

* Wed Sep 12 2012 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1
- Updated to 0.8.2.

* Wed Aug 08 2012 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- Updated from upstream git (e803ccad50).
- Updated to 0.8.1.

* Tue Jul 24 2012 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Drop obsoleted patch.
- Updated to 0.8.0.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt4
- Change the license key for the one from CTW (patch from Debian).
- Port xfce4-weather-plugin to libxfce4ui (Xfce bug #7956).
- Don't use git snapshot, build 0.7.4 version again.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt3.git20111123
- Rebuild with xfce4-panel-4.9.

* Wed Nov 23 2011 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt2.git20111123
- Changed descpription.
- Upstream git snapshot.

* Thu Feb 10 2011 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Updated to 0.7.4.

* Fri Jun 18 2010 Paul Wolneykien <manowar@altlinux.ru> 0.7.2-alt1
- New upstream version 0.7.2 (closes: 23634)

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux> 0.6.2-alt1
- new version
- add watch file

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.5.99.1-alt1
- 0.5.99.1

* Sun Mar 13 2005 Andrey Astafiev <andrei@altlinux.ru> 0.4.9-alt1
- 0.4.9

* Sat Jan 29 2005 Andrey Astafiev <andrei@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Tue Jan 18 2005 Andrey Astafiev <andrei@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sat Jan 01 2005 Andrey Astafiev <andrei@altlinux.ru> 0.3.0-alt2
- Rebuilt with new xfce4-panel.

* Mon May 17 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.0-alt1
- First version of RPM package for Sisyphus.
