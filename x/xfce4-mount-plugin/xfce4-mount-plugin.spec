Name: xfce4-mount-plugin
Version: 1.1.5
Release: alt1

Summary: Mount plugin for Xfce Desktop
License: GPLv2+
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>

Url: https://docs.xfce.org/panel-plugins/xfce4-mount-plugin
Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-mount-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
%name this little plugin behaves like the "kwikdisk - removable media
utility" shipped Press it and it will display a list of items
representing your various devices. The plugin displays various
information on each device.

%prep
%setup
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag mount_version_tag configure.ac.in

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
%_iconsdir/hicolor/*/apps/*
%_datadir/xfce4/panel/plugins/*.desktop

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Dec 28 2020 Mikhail Efremov <sem@altlinux.org> 1.1.5-alt1
- Updated to 1.1.5.

* Mon Dec 21 2020 Mikhail Efremov <sem@altlinux.org> 1.1.4-alt1
- Updated to 1.1.4.

* Mon Sep 14 2020 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt2.ge162062
- Fixed BR.
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.
- Upstream git snapshot.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 1.1.3.

* Mon Apr 04 2016 Mikhail Efremov <sem@altlinux.org> 0.6.7-alt3
- Patch from upstream:
  + Fixed autoconf and intltools bug 12470.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.6.7-alt2
- Rebuild with libxfce4util-4.12.

* Mon May 26 2014 Mikhail Efremov <sem@altlinux.org> 0.6.7-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 0.6.7.

* Wed Jun 05 2013 Mikhail Efremov <sem@altlinux.org> 0.6.4-alt1.git20130427
- Upstream git snapshot.
- Updated to 0.6.4.

* Fri May 04 2012 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt2
- Don't package *.la file.

* Fri Apr 27 2012 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt1
- Require xfce4-panel.
- Updated to 0.6.3.

* Mon Apr 23 2012 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Updated to 0.6.2.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Drop obsoleted patch.
- Updated to 0.6.0.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt4
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt3
- Rebuild with xfce4-panel-4.9.

* Thu Jan 27 2011 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt2
- Fix desktop file path for xfce4-panel >= 4.8.
- Add translations patch from FC.
- Spec update.

* Mon May 19 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.5-alt1
- new fersion

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.4-alt1
- new version
- add watch file

* Thu May 03 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.4.7-alt1
- 0.4.7

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.5-alt1
- 0.4.5 for xfce 4.4rc1

* Sun Sep 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3.1-alt1
- new version
- add russian and ukrainian translation

* Thu Aug 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3-alt1
- First build for Sisyphus.

