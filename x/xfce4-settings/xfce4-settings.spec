Name: xfce4-settings
Version: 4.14.2
Release: alt1
Summary: Settings Manager for Xfce
Summary (ru_RU.UTF-8): Менеджер настроек Xfce

License: GPLv2+
Url: https://www.xfce.org/
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/xfce4-settings
Source: %name-%version.tar
Source1: xfce4-fixkeyboard
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools > 4.5
BuildRequires: libxfce4ui-gtk3-devel libexo-gtk3-devel libxfconf-devel libgarcon-devel >= 0.1.10
BuildRequires: intltool libICE-devel libXcursor-devel libXi-devel libXrandr-devel libglade-devel libnotify-devel libxklavier-devel libupower-devel >= 0.99.4-alt2
BuildRequires: libcolord-devel
BuildRequires: xorg-drv-libinput-devel

Requires: libgarcon-settings-manager-menu

Obsoletes: xfce4-mcs-manager xfce4-mcs-plugins

%define _unpackaged_files_terminate_build 1

%description
This package provides the settings manager applications
for the Xfce desktop.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе менеджер настроек для окружения рабочего
стола Xfce.

%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfce4_settings_version_tag configure.ac.in
%xfce4reconf
%configure  \
	--enable-debug=minimum \
	--enable-maintainer-mode \
	--disable-silent-rules \
	--enable-libnotify \
	--enable-xcursor \
	--enable-xorg-libinput \
	--enable-libxklavier \
	--enable-sound-settings \
	--enable-pluggable-dialogs \
	--enable-colord
%make

%install
%makeinstall_std
%find_lang %name
install -pDm0755 %SOURCE1 %buildroot%_bindir/xfce4-fixkeyboard

%files -f %name.lang
%doc README TODO NEWS INSTALL COPYING AUTHORS
%_bindir/*
%_libdir/xfce4/*
%config(noreplace) %_sysconfdir/xdg/autostart/*
%config(noreplace) %_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%_sysconfdir/xdg/menus/xfce-settings-manager.menu
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.*

%changelog
* Mon Jan 13 2020 Mikhail Efremov <sem@altlinux.org> 4.14.2-alt1
- Don't use rpm-build-licenses.
- Updated to 4.14.2.

* Thu Aug 22 2019 Mikhail Efremov <sem@altlinux.org> 4.14.1-alt1
- Updated to 4.14.1.

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt1
- Updated to 4.14.0.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 4.13.8-alt1
- Updated to 4.13.8.

* Mon Jul 01 2019 Mikhail Efremov <sem@altlinux.org> 4.13.7-alt1
- Updated to 4.13.7.

* Sat May 18 2019 Mikhail Efremov <sem@altlinux.org> 4.13.6-alt1
- Enabled colord support.
- Updated to 4.13.6.

* Wed Oct 03 2018 Mikhail Efremov <sem@altlinux.org> 4.13.5-alt1
- Updated to 4.13.5.

* Thu Aug 02 2018 Mikhail Efremov <sem@altlinux.org> 4.13.4-alt1
- Updated url.
- Updated to 4.13.4.

* Fri Jun 22 2018 Mikhail Efremov <sem@altlinux.org> 4.12.4-alt1
- Disabled silent rules.
- Enabled debug (minimum level).
- Updated to 4.12.4.

* Mon Mar 19 2018 Mikhail Efremov <sem@altlinux.org> 4.12.3-alt1
- Updated to 4.12.3.

* Thu Mar 01 2018 Mikhail Efremov <sem@altlinux.org> 4.12.2-alt1
- Updated to 4.12.2.

* Thu Feb 02 2017 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt2
- Enable libinput support.

* Thu Sep 15 2016 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt1
- Updated to 4.12.1.

* Mon Aug 01 2016 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt2
- Fix segfault when upowerd is not running (closes: #32331).
- Patch from upstream:
  + Make sure icon == NULL if no icon is found.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Wed Feb 18 2015 Mikhail Efremov <sem@altlinux.org> 4.11.4-alt1
- Updated to 4.11.4.

* Fri Oct 31 2014 Mikhail Efremov <sem@altlinux.org> 4.11.3-alt3.git20141027
- Upstream git snapshot, including:
  + Fix for --display being fatal (closes: #30348).

* Wed Oct 15 2014 Mikhail Efremov <sem@altlinux.org> 4.11.3-alt2
- Rebuild with upower-0.99.1.

* Mon Aug 25 2014 Mikhail Efremov <sem@altlinux.org> 4.11.3-alt1
- Updated to 4.11.3.

* Fri Mar 28 2014 Mikhail Efremov <sem@altlinux.org> 4.11.2-alt2
- Rebuild with upower-0.99.

* Mon Feb 24 2014 Mikhail Efremov <sem@altlinux.org> 4.11.2-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 4.11.2.

* Tue Sep 24 2013 Mikhail Efremov <sem@altlinux.org> 4.11.1-alt1
- Updated to 4.11.1.

* Tue May 07 2013 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1.git20130506
- Drop patch for old libxfce4ui.
- Upsatream git snapshot.

* Mon Apr 29 2013 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1.git20130423
- xfce4-fixkeyboard: Update for new xfce4-settings.
- Upsatream git snapshot.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.5-alt1
- Updated to 4.9.5.

* Mon Apr 02 2012 Mikhail Efremov <sem@altlinux.org> 4.9.4-alt1
- Require libgarcon-settings-manager-menu.
- Updated to 4.9.4.

* Mon Feb 13 2012 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- Updated to 4.9.2.

* Mon Jan 23 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Mon Dec 12 2011 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt4
- Some fixes from upstream.
- Updated transations.

* Mon Dec 12 2011 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt3
- Updated Russian translation.

* Wed Nov 30 2011 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt2
- Add xfce4-fixkeyboard script.

* Fri Nov 25 2011 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Updated to 4.9.0.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt1
- Drop obsoleted patches.
- Updated to 4.8.3.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt3
- Updated Russian translation.

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt2
- Updated Russian translation (by Artem Zolochevskiy).

* Thu Jun 23 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt1
- Don't use freed memory (patch from upstream).
- Updated to 4.8.2.

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Updated to 4.8.1.

* Thu Jan 20 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Update summary and description.
- Fix license.
- Drop debian-libxklavier-5.0-API.patch (fixed in upstream).
- Spec cleanup.
- Updated to 4.8.0.
- remove xkl-config-registry-load.patch.

* Wed Jul 14 2010 Mikhail Efremov <sem@altlinux.org> 4.6.4-alt2
- fix build: add debian-libxklavier-5.0-API.patch.

* Tue Jan 26 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.4-alt1
- Version update.

* Wed Nov 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt4
- Added xkl-config-registry-load.patch.

* Fri Oct 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Russian translation update.

* Wed Aug 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Added Obsoletes for xfce4-mcs-manager and xfce4-mcs-plugins
- Updated Russian translation

* Sun Apr 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1
- First build for ALTLinux
