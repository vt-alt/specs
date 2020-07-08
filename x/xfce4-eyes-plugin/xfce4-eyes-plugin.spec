Name: xfce4-eyes-plugin
Version: 4.5.1
Release: alt1

Summary: Eyes plugin for Xfce Desktop
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-eyes-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-eyes-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: intltool libxml2-devel

Requires: xfce4-panel >= 4.8

%define _unpackaged_files_terminate_build 1

%description
Eyes is a xfce4 panel plugin that adds eyes which watch your every step.
Scary!

%prep
%setup
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag eyes_version_tag configure.ac.in

%build
%xfce4reconf
%configure \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/eyes/
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*.png

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Fri Jul 03 2020 Mikhail Efremov <sem@altlinux.org> 4.5.1-alt1
- Added Vcs tag.
- Updated url.
- Don't use rpm-build-licenses.
- Updated to 4.5.1.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 4.5.0-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 4.5.0.

* Wed Apr 27 2016 Mikhail Efremov <sem@altlinux.org> 4.4.5-alt1
- Updated to 4.4.5.

* Mon Mar 16 2015 Mikhail Efremov <sem@altlinux.org> 4.4.4-alt1
- Updated to 4.4.4.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 4.4.3-alt2
- Rebuild with libxfce4util-4.12.

* Mon Dec 29 2014 Mikhail Efremov <sem@altlinux.org> 4.4.3-alt1
- Fix build: create m4/ directory.
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 4.4.3.

* Mon Mar 04 2013 Mikhail Efremov <sem@altlinux.org> 4.4.2-alt1
- Fix build: use LT_PREREQ.
- Updated translations from upstream git.
- Updated to 4.4.2.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 4.4.1-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 4.4.1-alt2
- Rebuild with xfce4-panel-4.9.

* Sat Feb 05 2011 Mikhail Efremov <sem@altlinux.org> 4.4.1-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.
- Updated to 4.4.1

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt1
- new version
- add watch file

* Mon Dec 18 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- new version

* Thu Aug 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.3.0-alt1
- First build for Sisyphus.

