%define xfce_ver 4.13
%def_enable introspection
%def_enable vala

Name: xfce4-panel
Version: 4.14.0
Release: alt2

Summary: Panel for Xfce
Summary(ru_RU.UTF-8): Панель для окружения рабочего стола Xfce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://www.xfce.org/

# Upstream: git://git.xfce.org/xfce/xfce4-panel
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfce4ui-gtk3-devel >= %xfce_ver libexo-gtk3-devel >= 0.6.0 libgarcon-gtk3-devel
BuildRequires: gtk-doc libwnck3-devel libICE-devel libXext-devel libSM-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgtk+2-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libxfce4util-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools}

Requires: libxfce4panel = %version-%release
Requires: xfce4-common

Obsoletes: xfce4-showdesktop-plugin, xfce4-windowlist-plugin

%define libxfce4panel_name_gtk2 libxfce4panel-1.0
%define libxfce4panel_name_gtk3 libxfce4panel-2.0
%define wrapper_name_gtk3 wrapper-2.0

%define _unpackaged_files_terminate_build 1

%description
%name is the panel for the Xfce desktop environment.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе панель для окружения рабочего стола Xfce.

%package -n libxfce4panel
Summary: Library for Xfce panel (GTK+2)
License: %lgpl2plus
Group: Development/C

%description -n libxfce4panel
This package contains library for Xfce panel plugins
(GTK+2 variant).

%package -n libxfce4panel-devel
Summary: Development files to build Xfce panel plugins (GTK+2)
License: %lgpl2plus
Group: Development/C
Requires: libxfce4panel = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < 4.8.0

%description -n libxfce4panel-devel
This package contains files to develop plugins for Xfce panel
(GTK+2 variant).

%package -n libxfce4panel-devel-doc
Summary: Documentation files to build Xfce panel plugins
Group: Development/Documentation
Requires: libxfce4panel-devel = %version-%release
Provides: %name-devel-doc = %version-%release
Obsoletes: %name-devel-doc < 4.8.0
BuildArch: noarch

%description -n libxfce4panel-devel-doc
This package contains files to develop plugins for Xfce panel.

%package -n libxfce4panel-gtk3
Summary: Library for Xfce panel (GTK+3)
License: %lgpl2plus
Group: Development/C

%description -n libxfce4panel-gtk3
This package contains library for Xfce panel plugins
(GTK+3 variant).

%package -n libxfce4panel-gtk3-devel
Summary: Development files to build Xfce panel plugins (GTK+3)
License: %lgpl2plus
Group: Development/C
Requires: libxfce4panel-gtk3 = %version-%release

%description -n libxfce4panel-gtk3-devel
This package contains files to develop plugins for Xfce panel
(GTK+3 variant).

%if_enabled introspection
%package -n libxfce4panel-gtk3-gir
Summary: GObject introspection data for libxfce4panel-gtk3
Group: System/Libraries
Requires: libxfce4panel-gtk3 = %EVR

%description -n libxfce4panel-gtk3-gir
GObject introspection data for libxfce4panel-gtk3.

%package -n libxfce4panel-gtk3-gir-devel
Summary: GObject introspection devel data for libxfce4panel-gtk3
Group: System/Libraries
BuildArch: noarch
Requires: libxfce4panel-gtk3-gir = %EVR
Requires: libxfce4panel-gtk3-devel = %EVR

%description -n libxfce4panel-gtk3-gir-devel
GObject introspection devel data for libxfce4panel-gtk3.
%endif

%if_enabled vala
%package -n libxfce4panel-gtk3-vala
Summary: Vala bindings for libxfce4panel-gtk3
Group: System/Libraries
Requires: libxfce4panel-gtk3-devel = %EVR
BuildArch: noarch

%description -n libxfce4panel-gtk3-vala
Vala bindings for libxfce4panel-gtk3.
%endif


%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfce4_panel_version_tag configure.ac.in
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	%{subst_enable introspection} \
	%{subst_enable vala} \
	--enable-gtk-doc \
	--enable-gtk2 \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README
%config(noreplace) %_sysconfdir/xdg/xfce4/*
%_bindir/*
%_libdir/xfce4/panel/
%exclude %_libdir/xfce4/panel/%wrapper_name_gtk3
%_iconsdir/hicolor/*/*/*
%_datadir/xfce4/panel/
%_desktopdir/*.desktop
%exclude %_libdir/xfce4/panel/plugins/*.la

%files -n libxfce4panel
%_libdir/%libxfce4panel_name_gtk2.so.*

%files -n libxfce4panel-devel
%_libdir/pkgconfig/%libxfce4panel_name_gtk2.pc
%_libdir/%libxfce4panel_name_gtk2.so
%_includedir/xfce4/%libxfce4panel_name_gtk2/

%files -n libxfce4panel-devel-doc
%doc %_datadir/gtk-doc/html/libxfce4panel-*/

%files -n libxfce4panel-gtk3
%_libdir/%libxfce4panel_name_gtk3.so.*
%_libdir/xfce4/panel/%wrapper_name_gtk3

%files -n libxfce4panel-gtk3-devel
%_libdir/pkgconfig/%libxfce4panel_name_gtk3.pc
%_libdir/%libxfce4panel_name_gtk3.so
%_includedir/xfce4/%libxfce4panel_name_gtk3/

%if_enabled introspection
%files -n libxfce4panel-gtk3-gir
%_libdir/girepository-1.0/*.typelib

%files -n libxfce4panel-gtk3-gir-devel
%_datadir/gir-1.0/*.gir
%endif

%if_enabled vala
%files -n libxfce4panel-gtk3-vala
%_datadir/vala/vapi/libxfce4panel-*
%endif

%changelog
* Mon Sep 23 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt2
- Fix systray icons drawing w/o compositing (by Ivan A. Melnikov).

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt1
- Updated to 4.14.0.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 4.13.7-alt1
- Updated to 4.13.7.

* Fri Jul 05 2019 Mikhail Efremov <sem@altlinux.org> 4.13.6-alt2
- Enable vala support.
- Enable GObject introspection support.
- Fix changelog entry.

* Mon Jul 01 2019 Mikhail Efremov <sem@altlinux.org> 4.13.6-alt1
- Don't use deprecated PreReq.
- Updated to 4.13.6.

* Fri May 17 2019 Mikhail Efremov <sem@altlinux.org> 4.13.5-alt1
- Updated to 4.13.5.
- Drop no longer used directories.

* Wed Jan 02 2019 Mikhail Efremov <sem@altlinux.org> 4.13.4-alt1
- Updated to 4.13.4.

* Tue Aug 07 2018 Mikhail Efremov <sem@altlinux.org> 4.13.3-alt1
- Update url.
- Enable debug (minimum level).
- Updated to 4.13.3.

* Thu Dec 14 2017 Mikhail Efremov <sem@altlinux.org> 4.12.2-alt1
- Updated to 4.12.2.

* Wed Oct 26 2016 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt1
- Updated to 4.12.1.

* Fri Feb 12 2016 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt3
- Don't try to use panel-desktop-handler in the KDE (closes: #31542).

* Thu Mar 12 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt2
- Package GTK+3 variant of the library.

* Thu Mar 05 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Mon Jan 12 2015 Mikhail Efremov <sem@altlinux.org> 4.11.2-alt1
- Updated to 4.11.2.

* Wed Jun 25 2014 Mikhail Efremov <sem@altlinux.org> 4.11.1-alt1
- Updated to 4.11.1.

* Mon Feb 17 2014 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 4.11.0.

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 4.10.1-alt1.git20130506
- Bump version (this snapshot is newer then %name-4.10.1 release).
- Upstream git snapshot.

* Mon Dec 03 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt3
- applicationsmenu plugin: Skip empty GenericName.
- Require xfce4-common.
- Own %%_libexecdir/xfce4.

* Tue May 22 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt2
- Fix BR.
- Drop %%_datadir/xfce4/panel-plugins directory.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- Updated to 4.9.2.

* Mon Apr 09 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Sat Dec 31 2011 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Drop old Russan manual translation.
- Updated to 4.9.0.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.6-alt1
- Drop obsoleted patches.
- Updated to 4.8.6.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 4.8.5-alt3
- Updated Russian translation.

* Tue Aug 16 2011 Mikhail Efremov <sem@altlinux.org> 4.8.5-alt2
- Add Russian documentation (by Artem Zolochevskiy).
- Updated Russian translation (by Artem Zolochevskiy).

* Thu Jun 23 2011 Mikhail Efremov <sem@altlinux.org> 4.8.5-alt1
- Updated to 4.8.5.

* Mon May 30 2011 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt2
- Add patches from upstream git:
   + Sleep on startup until a window manager is detected.
   + Fix menu positioning for moved external plugins.

* Mon Apr 11 2011 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt1
- Drop obsoleted patches.
- Updated to 4.8.3.

* Mon Mar 21 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt3
- Fix build requires.

* Tue Mar 01 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt2
- Patch from upstream:
    Fix work with grouped windows (closes: #25174).

* Sun Feb 27 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt1
- Drop obsoleted patch.
- Updated to 4.8.2.

* Mon Feb 21 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt3
- Fix Russian translation.

* Fri Feb 18 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt2
- Patch from upstream: Initialize viewport if screen is connected.
- Fix Russian translation (closes: #25107).

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Updated to 4.8.1.

* Fri Jan 21 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Move libxfce4panel to separate subpackage.
- Spec cleanup, tar.bz2 -> tar.
- Remove exo-0.5.1.patch.
- Updated to 4.8.0.

* Tue Jan 26 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.3-alt1
- New version.

* Tue Jan 26 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.3-alt0.M51.1
- Backport to branch 5.1.

* Mon Jan 04 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt4
- Fix build with gtkdocize.

* Sun Oct 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Russian translation updated.

* Tue May 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt0.M50.2
- Backport to Desktop 5.0

* Sat May 09 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Updated russian translation

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
- Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Sun Jun 17 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt2
- fix 12007

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  4.3.99.1-alt2
- Fix buildreq and cleanup spec

* Tue Sep 12 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- new version 4.4rc1

* Tue Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Wed Mar 23 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt2
- Fixed panel settings saving.

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.99.3-alt1
- 4.1.99.3

* Mon Nov 01 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.91-alt1
- 4.1.91

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Mon Dec 22 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Tue Nov 18 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Sep 26 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- 3.99.2

* Mon Jul 14 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.1-alt0.9
- 3.99.1

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 3.90.0-alt0.9
- First version of RPM package for Sisyphus.
- Spec derived from original version.
