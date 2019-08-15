Name: xfce4-power-manager
Version: 1.6.5
Release: alt1
Summary: Power management for the Xfce desktop environment
Summary (ru_RU.UTF8): Утилита расширенного управления питанием для Xfce

Group: Graphical desktop/XFce
License: %gpl2plus
Url: https://goodies.xfce.org/projects/applications/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/xfce4-power-manager
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfconf-devel libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel
BuildRequires: libXext-devel
BuildRequires: libXrandr-devel
BuildRequires: libnotify-devel >= 0.4.1
BuildRequires: libglade-devel > 2.0.0
BuildRequires: libupower-devel
BuildRequires: gettext intltool desktop-file-utils
BuildPreReq: exo-csource

Requires: polkit
Requires: upower

%define _unpackaged_files_terminate_build 1

%description
xfce4-power-manager is a tool for the Xfce desktop environment for
managing profiles of policies which affect power consumption, such as
the display brightness level, display sleep times, or CPU frequency
scaling.

%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfpm_version_tag configure.ac.in
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-polkit \
	--enable-dpms \
	--enable-network-manager \
	--with-backend=linux \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%_bindir/*
%_sbindir/xfpm-power-backlight-helper
%_sbindir/xfce4-pm-helper
%_libdir/xfce4/panel/plugins/*.so
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.*
%_datadir/xfce4/panel/plugins/*.desktop
%_datadir/polkit-1/actions/*.policy
%_mandir/man?/*
%_datadir/metainfo/*.xml

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 1.6.5-alt1
- Updated to 1.6.5.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 1.6.4-alt1
- Updated to 1.6.4.

* Mon Jul 01 2019 Mikhail Efremov <sem@altlinux.org> 1.6.3-alt1
- Updated to 1.6.3.

* Fri May 17 2019 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1
- Updated to 1.6.2.

* Tue Aug 14 2018 Mikhail Efremov <sem@altlinux.org> 1.6.1-alt1
- Don't requre xfce4-panel.
- Updated url.
- Updated to 1.6.1.

* Mon May 30 2016 Mikhail Efremov <sem@altlinux.org> 1.4.4-alt2
- Enable debug (minimum level).
- Patch from upstream:
  + Look up the schema for light-locker's settings recursively

* Mon Mar 23 2015 Mikhail Efremov <sem@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 1.4.3-alt1
- Updated to 1.4.3.

* Tue Feb 17 2015 Mikhail Efremov <sem@altlinux.org> 1.4.2-alt1
- Updated to 1.4.2.
- Drop obsoleted patches.

* Mon Jun 02 2014 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Fri Mar 28 2014 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt7.git20140319
- logind support: treat "challenge" responses as true.
- Port to upower-0.99 D-Bus interface.
- Drop obsoleted patch.
- Fix Xfce name (XFCE -> Xfce).
- Upstream git snapshot (master branch).

* Thu Aug 29 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt6
- Use xfsm-shutdown-helper for suspend/hibernate.

* Fri May 31 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt5
- Fix xrandr brightness control for 64 bit builds.
- Enable xrandr brightness control for eDP displays
     (from xfce4-dev@ by Marcus Overhagen).

* Tue Apr 09 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt4
- Add systemd support for suspend/hibernate (closes: #28763).

* Thu Feb 21 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt3
- Don't allow systemd to handle suspend/hibernate events.

* Thu Aug 30 2012 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt2
- Don't control disk's spin speed.
- Don't try to use internel documentation.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Tue Apr 10 2012 Mikhail Efremov <sem@altlinux.org> 1.0.11-alt1
- Fix crash when all outputs don't support the backlight property.
- Fix crash when xfpm tries to refresh the status icon of a removed
  battery.
- Let the brightness keys work even when numlock is on.
- Drop AC_PROG_LIBTOOL and AC_DISABLE_STATIC for LT_PREREQ and
  LT_INIT.
- Drop obsoleted patches.
- Updated to 1.0.11.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt6
- Rebuild with xfce4-panel-4.9.

* Wed Nov 30 2011 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt5
- Run xfce4-fixkeyboard script after suspend/hibernate.

* Tue May 31 2011 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt4
- Don't attach to the status icon if libnotify >= 0.7
    (patch from upstream).
- Add patch for NM-0.9 support.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt3
- Update Russian translation (by Andrey Cherepanov).
- Add more strings for translation.

* Tue Mar 29 2011 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt2
- Added upower and udisks to requires.

* Tue Feb 22 2011 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Updated to 1.0.10.

* Wed Jan 26 2011 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1
- tar.bz2 -> tar.
- Updated to 1.0.3.

* Tue Jan 19 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.8.4.2-alt1
- Version update.

* Fri Oct 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.8.4-alt1
- Version update.

* Thu Jul 09 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.8.1.1-alt1
- Version update.

* Wed May 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.8.1-alt1
- Update to 0.8.0RC2. Version updated to 0.8.1 for resolve conflicts with 0.8.0beta2

* Fri Apr 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.8.0beta2-alt1
First build for Sisyphus
