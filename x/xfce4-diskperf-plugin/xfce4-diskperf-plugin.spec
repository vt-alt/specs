Name: xfce4-diskperf-plugin
Version: 2.6.2
Release: alt1

Summary: Disk performance plugin for the Xfce panel
License: %bsdstyle
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>
Url: https://goodies.xfce.org/projects/panel-plugins/%name

# Upstream: git://git.xfce.org/panel-plugins/xfce4-diskperf-plugin
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel
BuildRequires: intltool perl-XML-Parser

Requires: xfce4-panel >= 4.9

%define _unpackaged_files_terminate_build 1

%description
%name is the disk performance plugin for the Xfce panel.

%prep
%setup
#patch -p1

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

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Tue Aug 13 2019 Mikhail Efremov <sem@altlinux.org> 2.6.2-alt1
- Updated for 2.6.2.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 2.6.1-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated for 2.6.1.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 2.5.5-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated for 2.5.5.

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 2.5.4-alt1
- Updated for 2.5.4.

* Mon May 14 2012 Mikhail Efremov <sem@altlinux.org> 2.5.3-alt1
- Updated for 2.5.3.

* Fri May 04 2012 Mikhail Efremov <sem@altlinux.org> 2.5.2-alt2
- Don't package *.la file.

* Mon Apr 30 2012 Mikhail Efremov <sem@altlinux.org> 2.5.2-alt1
- Updated for 2.5.2.

* Fri Apr 13 2012 Mikhail Efremov <sem@altlinux.org> 2.5.1-alt1
- Updated for 2.5.1.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 2.3.0-alt2
- Rebuild with xfce4-panel-4.9.

* Thu Feb 10 2011 Mikhail Efremov <sem@altlinux.org> 2.3.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Drop xfce4-diskperf-plugin-2.1.0-alt-fix.patch (fixed in upstream).
- Remove xfce4-diskperf-plugin-asneeded.patchi (obsolete).
- Spec updated, tar.bz2 -> tar.
- Updated to 2.3.0.

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 2.2.0-alt1
- new version

* Mon Oct 15 2007 Igor Zubkov <icesik@altlinux.org> 2.1.0-alt1.1
- NMU
  + fix build with new intltool

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.1.0-alt1
- new version

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.0-alt1
- 2.0

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Wed Nov 19 2003 Andrey Astafiev <andrei@altlinux.ru> 1.4-alt1
- 1.4

* Mon Nov 03 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2-alt1
- 1.2

* Mon Oct 20 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0-alt1
- First version of RPM package for Sisyphus.
