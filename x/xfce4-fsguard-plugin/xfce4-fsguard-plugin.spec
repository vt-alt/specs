Name: xfce4-fsguard-plugin
Version: 1.1.1
Release: alt1

Summary: Plugin checks the chosen mountpoint for free disk space
License: %bsdstyle
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>

Url: https://goodies.xfce.org/projects/panel-plugins/%name
# git://git.xfce.org/panel-plugins/xfce4-fsguard-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: libSM-devel perl-XML-Parser xorg-cf-files intltool

Requires: xfce4-panel >= 4.8

%define _unpackaged_files_terminate_build 1

%description
A little Xfce plugin, which checks the free space on the chosen
mountpoint frequently. It displays 4 different icons and a message box,
depending on the free space. The amount of free disk space is visible in
a tooltip. If you left-click on its icon, it opens the mountpoint
directory in the file manager.

%prep
%setup
%patch -p1

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
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/*/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Wed Aug 14 2019 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1
- Updated to 1.1.1.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 1.1.0.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 1.0.2.

* Wed Jun 05 2013 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt2
- Updated translations from upstream git.
- Don't package *.la files.

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Updated to 1.0.1.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Rebuild with xfce4-panel-4.9.

* Sat Feb 05 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Fix desktop file path.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.
- Updated to 1.0.0.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.2-alt1
- new version

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.1-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- new version
- return from orphaned
- add watch file

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.3.0-alt1
- First build for Sisyphus.

