Name: xfce4-timer-plugin
Version: 1.7.1
Release: alt1

Summary: Timer plugin for Xfce
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-timer-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-timer-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4util-devel libxfce4ui-gtk3-devel libxfce4panel-gtk3-devel
BuildRequires: perl-XML-Parser intltool

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
Nothing to describe really. Use the options menu to add timers. You can
choose them to be countdown periods or alarms at certain times. Only one
of them can be run at a time.

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
%doc README ChangeLog AUTHORS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*.*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Fri Jul 24 2020 Mikhail Efremov <sem@altlinux.org> 1.7.1-alt1
- Added Vcs tag.
- Don't use rpm-build-licenses.
- Updatde url,
- Updated to 1.7.1.

* Thu Aug 23 2018 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt1
- Update url.
- Explicitly set debug level minimum.
- Updated to 1.7.0.

* Wed Jun 08 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1
- Updated translations from upstream git.
- Updated to 1.6.0.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt2
- Rebuild with libxfce4util-4.12.
- Fix Summary.
- Fix Xfce name (XFCE -> Xfce).
- Require xfce4-panel.

* Wed Jun 05 2013 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1
- Updated translations from upstream git.
- Updated to 1.5.0.

* Tue Apr 23 2013 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Updated from upstream git.
- Updated to 1.0.2.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt2
- Rebuild with xfce4-panel-4.9.

* Wed Jun 22 2011 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Drop obsoleted patch.
- Updated to 0.6.2.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt2
- Fix segfault when creating plugin in 4.8 panel.
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.6.1-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.6-alt1
- new version
- add watch file

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.5.1-alt1
- First build
