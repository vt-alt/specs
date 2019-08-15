Name: xfce4-battery-plugin
Version: 1.1.3
Release: alt1

Summary: Battery monitor plugin for the Xfce panel
License: %gpl2plus, %lgpl2plus
Group: Graphical desktop/XFce
Url:  https://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/panel-plugins/xfce4-battery-plugin
Source: %name-%version.tar

Requires: xfce4-panel >= 4.9

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4util-devel libxfce4ui-gtk3-devel libxfce4panel-gtk3-devel

BuildRequires: perl-XML-Parser intltool

%define _unpackaged_files_terminate_build 1

%description
%name is the battery monitor plugin for the Xfce panel.

%prep
%setup

%build
%xfce4reconf
%configure \
    --disable-static \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/*/*/*/*

%exclude %_libdir/xfce4/panel/plugins/*.la
# Seems glibc doesn't support uz@Latn
%exclude %_datadir/locale/uz@Latn/LC_MESSAGES/xfce4-battery-plugin.mo

%changelog
* Tue Aug 13 2019 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt1
- Updated to 1.1.3.

* Mon Jan 14 2019 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt1
- Updated to 1.1.2.

* Mon Sep 24 2018 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1
- Update to 1.1.1.

* Mon Aug 20 2018 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Don't package uz@Latn translation.
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Update to 1.1.0.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt2
- Rebuild with libxfce4util-4.12.
- Fix Xfce name (XFce,XFCE -> Xfce).

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1
- Updated to 1.0.5.

* Mon May 14 2012 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1
- Updated to 1.0.4.

* Mon Apr 30 2012 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Wed Apr 18 2012 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Drop obsoleted patch.
- Updated to 1.0.1.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Rebuild with xfce4-panel-4.9.

* Mon Jan 31 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Fix desktop file path.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.
- Drop xfce4-battery-plugin-build.patch (fixed in upstream).
- Updated to 1.0.0.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.1-alt1
- new version

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.0-alt2
- fix build

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.0-alt1
- new version

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.90.3-alt1
- 0.4.90.3

* Thu Aug 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3.0-alt1
- New version

* Mon Dec 27 2004 Andrey Astafiev <andrei@altlinux.ru> 0.2.0-alt2
- Rebuilt with libxfcegui4.so.3

* Tue Sep 16 2003 Andrey Astafiev <andrei@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 0.1.2-alt0.9
- First version of RPM package for Sisyphus.
