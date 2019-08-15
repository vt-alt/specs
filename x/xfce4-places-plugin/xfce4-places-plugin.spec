Name: xfce4-places-plugin
Version: 1.8.1
Release: alt1

Summary: This plugin is a menu with quick access to folders, documents, and removable media
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

# git://git.xfce.org/panel-plugins/xfce4-places-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel libexo-gtk3-devel
BuildRequires: libxfconf-devel
BuildPreReq: libgio-devel libnotify-devel
BuildRequires: libxml2-devel intltool

Requires: xfce4-panel >= 4.8

%define _unpackaged_files_terminate_build 1

%description
This xfce4-places-plugin brings much of the functionality of GNOME's
Places menu to Xfce.
The plugin looks a lot like a launcher with multiple items in a menu.
The main "launcher" button opens up Thunar at the user's home directory.
The arrow button opens up a menu with two sections: system-defined
locations and user-defined locations.
The system-defined locations are consistent with Thunar (including their
icons).
For user-defined bookmarks, the plugin reads the ~/.gtk-bookmarks file
so that it shares bookmarks with Thunar, Nautilus, the GNOME Panel, etc.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-gio-unix \
	--enable-notifications \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_bindir/xfce4-popup-places
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/panel/plugins/*.desktop

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1
- Updated to 1.8.1.

* Mon May 13 2019 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1
- Updated to 1.8.0.

* Thu Aug 16 2018 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt2
- Patch from upstream:
  + Bug 11939:  xfce4-places-plugin 1.7.0 crashes with undefined
    symbol
- Rebuild with libxfconf-0.so.3.
- Add libxfconf-devel to BR.
- Update url.
- Use _unpackaged_files_terminate_build.
- Enable debug (minimum level).

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt1
- Updated to 1.7.0.

* Tue Nov 26 2013 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 1.6.0.

* Fri Sep 28 2012 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.

* Tue Aug 28 2012 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Fri Apr 13 2012 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt4.git20110107
- Rebuild with xfce4-panel-4.9.

* Thu Sep 01 2011 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt3.git20110107
- Rebuild for libnotify 0.7.

* Mon Mar 21 2011 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt2.git20110107
- Don't to package Changelog.
- Really fix implicit DSO linking.
- Port to gio (patch from Xfce bug #6663).
- Port to libxfce4ui (patch from Xfce bug #7317).
- Updated from upstream's git.

* Tue Feb 08 2011 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Add patches from Fedora.
- Spec updated, tar.bz2 -> tar.
- Updated to 1.2.0.

* Fri May 08 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.0-alt2
- rebuild, update requires

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.0.0-alt1
- new version
- add watch file

* Thu May 03 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.0-alt1
- first build

