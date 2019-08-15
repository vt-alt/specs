%def_enable introspection
%def_enable vala

Name: libxfce4ui
Version: 4.14.1
Release: alt1

Summary: Various GTK+2 widgets for Xfce
Summary (ru_RU.UTF-8): Набор виджетов GTK+2 для Xfce
License: %lgpl2plus
Group: Graphical desktop/XFce
Url: https://www.xfce.org/

Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/libxfce4ui
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: gtk-doc intltool libSM-devel libgladeui-devel libstartup-notification-devel libxfce4util-devel libxfconf-devel xorg-cf-files
BuildRequires: libgtk+3-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libxfce4util-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools}

Requires: %name-common = %version-%release

%define libxfce4kbd_name_gtk2 libxfce4kbd-private-2
%define libxfce4ui_name_gtk2 %name-1
%define libxfce4kbd_name_gtk3 libxfce4kbd-private-3
%define libxfce4ui_name_gtk3 %name-2

%define _unpackaged_files_terminate_build 1

%description
Various GTK+2 widgets for Xfce.

%description -l ru_RU.UTF-8
Набор виджетов GTK+2 для Xfce.

%package devel
Summary: Development files for %name (GTK+2)
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for the %name library (GTK+2 variant).

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-doc
This package contains development documentation for %name.

%package common
Summary: Common files for both variants of %name
Group: Graphical desktop/XFce
BuildArch: noarch

%description common
This package contains the common files for both variants of %name.

%package gtk3
Summary: Various GTK+3 widgets for Xfce
Group: Graphical desktop/XFce
Requires: %name-common = %version-%release

%description gtk3
Various GTK+3 widgets for Xfce.

%package gtk3-devel
Summary: Development files for %name (GTK+3)
Group: Development/C
Requires: %name-gtk3 = %version-%release

%description gtk3-devel
Development files for the %name library (GTK+3 variant).

%if_enabled introspection
%package gtk3-gir
Summary: GObject introspection data for %name-gtk3
Group: System/Libraries
Requires: %name = %EVR

%description gtk3-gir
GObject introspection data for %name-gtk3.

%package gtk3-gir-devel
Summary: GObject introspection devel data for %name-gtk3
Group: System/Libraries
BuildArch: noarch
Requires: %name-gtk3-gir = %EVR
Requires: %name-gtk3-devel = %EVR

%description gtk3-gir-devel
GObject introspection devel data for %name-gtk3.
%endif

%if_enabled vala
%package gtk3-vala
Summary: Vala bindings for %name-gtk3
Group: System/Libraries
Requires: %name-gtk3-devel = %EVR
BuildArch: noarch

%description gtk3-vala
Vala bindings for %name-gtk3.
%endif

%package -n xfce4-about
Summary: Xfce4 'About' dialog
Group: Graphical desktop/XFce
# Due to xfce4-about
Conflicts: xfce-utils < 4.8.3-alt3

%description -n xfce4-about
This package contains the 'About Xfce' dialog.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-gtk-doc \
	--enable-startup-notification \
	--enable-gladeui \
	%{subst_enable introspection} \
	%{subst_enable vala} \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files
%_libdir/%libxfce4kbd_name_gtk2.so.*
%_libdir/%libxfce4ui_name_gtk2.so.*

%files devel
%_includedir/xfce4/%libxfce4kbd_name_gtk2
%_includedir/xfce4/%libxfce4ui_name_gtk2
%_pkgconfigdir/%libxfce4kbd_name_gtk2.pc
%_pkgconfigdir/%libxfce4ui_name_gtk2.pc
%_libdir/%libxfce4kbd_name_gtk2.so
%_libdir/%libxfce4ui_name_gtk2.so
%_datadir/glade3/catalogs/*.xml
%_datadir/glade3/pixmaps/*/*/*/*
%_libdir/glade3/modules/*.so
%exclude %_libdir/glade3/modules/*.la

%files devel-doc
%doc %_datadir/gtk-doc/html/%name

%files common -f %name.lang
%doc README NEWS AUTHORS
%_liconsdir/*
%config(noreplace) %_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml/*.xml

%files gtk3
%_libdir/%libxfce4kbd_name_gtk3.so.*
%_libdir/%libxfce4ui_name_gtk3.so.*

%files gtk3-devel
%_includedir/xfce4/%libxfce4kbd_name_gtk3
%_includedir/xfce4/%libxfce4ui_name_gtk3
%_pkgconfigdir/%libxfce4kbd_name_gtk3.pc
%_pkgconfigdir/%libxfce4ui_name_gtk3.pc
%_libdir/%libxfce4kbd_name_gtk3.so
%_libdir/%libxfce4ui_name_gtk3.so

%if_enabled introspection
%files gtk3-gir
%_libdir/girepository-1.0/*.typelib

%files gtk3-gir-devel
%_datadir/gir-1.0/*.gir
%endif

%if_enabled vala
%files gtk3-vala
%_datadir/vala/vapi/%name-*
%endif

%files -n xfce4-about
%_bindir/xfce4-about
%_desktopdir/xfce4-about.desktop

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14.1-alt1
- Updated to 4.14.1.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 4.13.7-alt1
- Updated to 4.13.7.

* Fri Jul 05 2019 Mikhail Efremov <sem@altlinux.org> 4.13.6-alt2
- Enable vala support.
- Enable GObject introspection support.

* Mon Jul 01 2019 Mikhail Efremov <sem@altlinux.org> 4.13.6-alt1
- Updated to 4.13.6.

* Sat May 18 2019 Mikhail Efremov <sem@altlinux.org> 4.13.5-alt1
- Updated to 4.13.5.

* Mon Aug 06 2018 Mikhail Efremov <sem@altlinux.org> 4.13.4-alt1
- Make devel-doc subpackage noarch.
- Use _unpackaged_files_terminate_build.
- Updated url.
- Enabled debug (minimum level).
- Updated to 4.13.4.

* Mon Mar 16 2015 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt1
- Updated to 4.12.1.

* Thu Mar 12 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt2
- Package GTK+3 variant of the libraries.
- Move libgladeui stuff to the libxfce4ui-devel subpackage.
- Move xfce4-about to the separate subpackage.

* Thu Mar 05 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Thu Feb 19 2015 Mikhail Efremov <sem@altlinux.org> 4.11.2-alt1
- Updated to 4.11.2.

* Mon Feb 24 2014 Mikhail Efremov <sem@altlinux.org> 4.11.1-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 4.11.1.

* Mon Sep 23 2013 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Updated to 4.11.0.

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt3.git20130505
- Upstream git snapshot.

* Tue Dec 04 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt2
- Rebuild against libgladeui-1.so.11.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- Updated to 4.9.2.

* Fri Apr 06 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Tue Jan 10 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt2
- Add conflict with xfce-utils < 4.8.3-alt3.

* Tue Jan 10 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Updated to 4.9.0.

* Thu Dec 29 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Don't build static libraries.
- Use maintainer mode.
- Updated to 4.8.1.

* Tue Nov 08 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt4
- Replace <Primary> shortcut with <Control>.

* Mon Aug 29 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt3
- Updated Russian translation.

* Wed Jan 19 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt2
- Own xfce4-keyboard-shortcuts.xml file.
- Fix group.
- Fix license.
- Added keyboard-shortcuts patch from FC.

* Mon Jan 17 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Updated to 4.8.0.
- Spec cleanup.

* Sun May 16 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.7.2-alt1
- First build for sisyphus. Spec based on libxfcegui4 spec file.

