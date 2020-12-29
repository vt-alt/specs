Name: xfce4-smartbookmark-plugin
Version: 0.5.2
Release: alt1

Summary: Smart bookmarks for the Xfce panel
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-smartbookmark-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-smartbookmark-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel

BuildRequires: libXt-devel libgtk+3-devel xorg-cf-files

Requires: xfce4-panel >= 4.11

%define _unpackaged_files_terminate_build 1

%description
A plugin which allows you to do a search directly on Internet on sites
like Google or ALT Linux Bugzilla. It allows you to send requests
directly to your browser and perform custom searches.

%prep
%setup
%patch -p1

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
%doc README.md NEWS AUTHORS
%_libdir/xfce4/panel/plugins/*.so
%exclude %_libdir/xfce4/panel/plugins/*.la
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Thu Dec 24 2020 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Mon Sep 14 2020 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt2.g3fc7592
- Fixed BR.
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.
- Upstream git snapshot.

* Tue Aug 13 2019 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Updated to 0.5.1.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 0.5.0.

* Wed Mar 25 2015 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1
- Updated to 0.4.6.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.4.5-alt2
- Rebuild with libxfce4util-4.12.
- Fix Xfce name (XFCE -> Xfce).

* Mon Jan 21 2013 Mikhail Efremov <sem@altlinux.org> 0.4.5-alt1
- Updated to 0.4.5.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt2
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Mon Feb 06 2012 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1
- Use ALT bugzilla link instead of Debian's.
- Fix location of the desktop file.
- Updated to 0.4.4.

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.2-alt1
- First build for Sisyphus.

