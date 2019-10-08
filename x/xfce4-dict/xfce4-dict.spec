Name: xfce4-dict
Version: 0.8.3
Release: alt1

Summary: Xfce4 Dictionary - A client program to query different dictionaries
License: %gpl2plus
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>
Url: https://goodies.xfce.org/projects/panel-plugins/%name
# git://git.xfce.org/apps/xfce4-dict
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Obsoletes: xfce4-dict-plugin < 0.5.2
Provides: xfce4-dict-plugin

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: libgio-devel
BuildRequires: intltool

Requires: enchant xdg-utils

%define _unpackaged_files_terminate_build 1

%description
This program allows you to search different kinds of dictionary services
for words or phrases and shows you the result.
Currently you can query a "Dict" server(RFC 2229), any online dictionary
service by opening a web browser or search for words using a spell check
program like aspell, ispell or enchant.

xfce4-dict contains a stand-alone application called "xfce4-dict" and a
panel plugin for the Xfce panel.

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
%_bindir/xfce4-dict
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_desktopdir/*.desktop
%_man1dir/*
%_iconsdir/*/*/*/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Oct 07 2019 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1
- Updated to 0.8.3.

* Wed Nov 28 2018 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1
- Updated to 0.8.2.

* Tue Oct 09 2018 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2
- Fix parallel build.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 0.8.1.

* Wed Apr 27 2016 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- Updated to 0.7.2.

* Mon Mar 16 2015 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Updated to 0.7.1.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2
- Rebuild with libxfce4util-4.12.
- Fix Xfce name (XFCE -> Xfce).

* Mon May 20 2013 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt2
- Rebuild with xfce4-panel-4.9.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Updated to 0.6.0.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.2-alt1
- new version

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.0-alt1
- new version

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.1-alt1
- new version

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.2.0-alt1
- First build for Sisyphus.

