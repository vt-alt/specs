Name: xfce4-datetime-plugin
Version: 0.8.0
Release: alt1

Summary: Datetime plugin for the Xfce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

#git://git.xfce.org/panel-plugins/xfce4-datetime-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util
BuildRequires: perl-XML-Parser intltool

Requires: xfce4-panel >= 4.8

%define _unpackaged_files_terminate_build 1

%description
%name is the datetime plugin for the Xfce panel.

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
%doc README ChangeLog AUTHORS
%_libdir/xfce4/panel/plugins/*.so
%exclude %_libdir/xfce4/panel/plugins/*.la
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Tue Apr 30 2019 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Updated to 0.7.1.

* Mon Aug 20 2018 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 0.7.0.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt2
- Rebuild with libxfce4util-4.12.
- Fix Xfce name (XFCE,XFce -> Xfce).

* Fri Feb 15 2013 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Drop remained USE_GTK_TOOLTIP_API.
- Drop obsoleted patches.
- Updated to 0.6.2.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt4
- Fix build: Replace BM_DEBUG_SUPPOR with XDT_FEATURE_DEBUG.
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt3
- Rebuild with xfce4-panel-4.9.

* Mon Jan 31 2011 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt2
- Fix plugindir path for xfce4-panel >= 4.8.
- Fix desktop file path for xfce4-panel >= 4.8.
- Remove watch file.
- Port to libxfce4ui.
- Spec updated, tar.bz2 -> tar.
- Add patches from Fedora.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.6.1-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.0-alt1
- new version
- add watch file

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.4.1-alt1
- new version

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sat Jan 01 2005 Andrey Astafiev <andrei@altlinux.ru> 0.3.1-alt2
- Rebuilt with new xfce4-panel.

* Sat Dec 25 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Thu Feb 05 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.0-alt2
- Fixed BuildRequires.

* Mon Feb 02 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Mon Nov 03 2003 Andrey Astafiev <andrei@altlinux.ru> 0.2-alt1
- 0.2

* Tue Oct 07 2003 Andrey Astafiev <andrei@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
