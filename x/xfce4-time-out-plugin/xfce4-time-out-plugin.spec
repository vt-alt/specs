Name: xfce4-time-out-plugin
Version: 1.0.3
Release: alt1

Summary: Timeout plugin for Xfce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

# git://git.xfce.org/panel-plugins/xfce4-time-out-plugin
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4util-devel libxfce4ui-devel libxfce4panel-devel
BuildRequires: libSM-devel perl-XML-Parser xorg-cf-files

Requires: xfce4-panel >= 4.9

%define _unpackaged_files_terminate_build 1

%description
xfce4-time-out-plugin is a plugin for the Xfce panel. It's a
comfortable tool for taking a break from computer work every now
and then. You can define a working interval and whenever time
of this interval has passed your screen is locked for a configurable
amount of time - which gives you enough time to grab a cup of
coffee, smoke a cigarette or even do something healthy like eating,
exercising, cleaning up or whatever.

%prep
%setup

%build
%xfce4reconf
%configure \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_liconsdir/*.png
%_iconsdir/hicolor/scalable/apps/*.svg

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Tue Aug 13 2019 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Update url.
- Updated to 1.0.3.

* Tue Mar 10 2015 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt3
- Rebuild with libxfce4util-4.12.
- Fix Summary.
- Fix Xfce name (XFCE -> Xfce).

* Fri May 04 2012 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt2
- Don't package *.la file.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Updated to 1.0.1.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Rebuild with xfce4-panel-4.9.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.
- Updated to 1.0.0.

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1.1-alt1
- First build
