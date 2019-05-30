Name: xfce4-cpugraph-plugin
Version: 1.0.90
Release: alt1

Summary: CPU monitor for the Xfce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/panel-plugins/xfce4-cpugraph-plugin
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel
BuildRequires: intltool libxml2-devel

Requires: xfce4-panel >= 4.11

%define _unpackaged_files_terminate_build 1

%description
A CPU monitor plugin for the Xfce panel. It offers multiple display
modes (LED, gradient, fire, etc...) to show the current CPU load of
the system. The colors and the size of the plugin are customizable.

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
%doc README AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_datadir/icons/hicolor/*/*/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Wed May 29 2019 Mikhail Efremov <sem@altlinux.org> 1.0.90-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 1.0.90.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt2
- Rebuild with libxfce4util-4.12.
- Fix Xfce name (XFCE -> Xfce).

* Wed Jul 04 2012 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1
- Updated to 1.0.5.

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1
- Updated to 1.0.4.

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1
- Updated to 1.0.3.

* Fri May 04 2012 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt2
- Don't package *.la files.

* Mon Apr 30 2012 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt2
- Rebuild with xfce4-panel-4.9.

* Sat Feb 05 2011 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.gz -> tar.
- Drop watch file.
- Updated to 1.0.1.

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- return from orphaned
- new version 0.4.0
- add watch file

* Mon Dec 18 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.3.0-alt1
- new version

* Sat Jan 01 2005 Andrey Astafiev <andrei@altlinux.ru> 0.2.2-alt2
- Rebuilt with new xfce4-panel.

* Sat Aug 14 2004 Andrey Astafiev <andrei@altlinux.ru> 0.2.2-alt1
- First version of RPM package for Sisyphus.
