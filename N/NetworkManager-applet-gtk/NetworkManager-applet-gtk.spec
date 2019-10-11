%define nm_version 1.4.1-alt1.git20160914
#define git_date .git20180106
%define git_date %nil

%define _unpackaged_files_terminate_build 1

%def_without appindicator
%def_with team
%def_without selinux
%def_with gcr
%def_without libnm_gtk

%ifarch %e2k
%define more_warnings no
%else
%define more_warnings error
%endif

Name: NetworkManager-applet-gtk
Version: 1.8.24
Release: alt1%git_date
License: %gpl2plus
Group: Graphical desktop/GNOME
Summary: Panel applet for use with NetworkManager
Url: http://www.gnome.org/projects/NetworkManager/
# Upstream: git://git.gnome.org/network-manager-applet
Source: nm-applet-%version.tar
Patch: nm-applet-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: libdbus-devel libdbus-glib libgtk+3-devel libtool libpolkit1-devel

BuildRequires: libwireless-devel
BuildRequires: libnotify-devel
%if_with libnm_gtk
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: libnm-util-devel >= %nm_version
BuildRequires: libnm-glib-devel >= %nm_version
BuildRequires: libnm-glib-vpn-devel >= %nm_version
BuildRequires: NetworkManager-glib-gir-devel >= %nm_version
%endif
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnm-gir-devel >= %nm_version
BuildRequires: iso-codes-devel
BuildRequires: gnome-common
BuildRequires: libgudev-devel
BuildRequires: libmm-glib-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libsecret-devel
BuildRequires: mobile-broadband-provider-info
BuildRequires: gtk-doc
%{?_with_appindicator:BuildRequires: libappindicator-gtk3-devel}
%{?_with_team:BuildRequires: libjansson-devel}
%{?_with_selinux:BuildRequires: libselinux-devel}
%{?_with_gcr:BuildRequires: gcr-libs-devel}

Requires: NetworkManager-daemon >= %nm_version
Requires: dbus-tools-gui
Requires: mobile-broadband-provider-info
#Requires: polkit-gnome
Requires: iso-codes

Obsoletes: NetworkManager-gnome < 0.9.8.4
Provides: NetworkManager-gnome = %version-%release

%description
This package contains GNOME utilities and applications for use with
NetworkManager, including a panel applet for wireless networks.

%if_with libnm_gtk
%package -n libnm-gtk
License: %gpl2plus
Group: Graphical desktop/GNOME
Summary: Private libraries for NetworkManager GUI support (libnm-glib version)

%description -n libnm-gtk
This package contains private libraries to be used only by nm-applet and
the GNOME Control Center.

This library will be obsolete by libnma in the future.

%package -n libnm-gtk-devel
License: %gpl2plus
Group: Development/GNOME and GTK+
Summary: Private header files for NetworkManager GUI support (libnm-glib version)
Requires: libnm-gtk = %version-%release
Requires: libnm-util-devel >= %nm_version
Requires: libnm-glib-devel >= %nm_version
Requires: libnm-glib-vpn-devel >= %nm_version
Requires: libgtk+3-devel

%description -n libnm-gtk-devel
This package contains private header and pkg-config files to be used
only by nm-applet and the GNOME control center.

This library will be obsolete by libnma in the future.

%package -n libnm-gtk-gir
License: %gpl2plus
Group: System/Libraries
Summary: GObject introspection data for the libnm-gtk
Requires: libnm-gtk = %version-%release

%description -n libnm-gtk-gir
GObject introspection data for the libnm-gtk.

%package -n libnm-gtk-gir-devel
License: %gpl2plus
Group: System/Libraries
Summary: GObject introspection devel data for the libnm-gtk
BuildArch: noarch
Requires: libnm-gtk-gir = %version-%release
Requires: libnm-gtk-devel = %version-%release

%description -n libnm-gtk-gir-devel
GObject introspection devel data for the libnm-gtk.
%endif

%package -n libnma
License: %gpl2plus
Group: Graphical desktop/GNOME
Summary: Private libraries for NetworkManager GUI support (libnm version)

%description -n libnma
This package contains private libraries to be used only by nm-applet and
the GNOME Control Center.

%package -n libnma-devel
License: %gpl2plus
Group: Development/GNOME and GTK+
Summary: Private header files for NetworkManager GUI support (libnm version)
Requires: libnma = %version-%release
Requires: libnm-devel >= %nm_version
Requires: libgtk+3-devel

%description -n libnma-devel
This package contains private header and pkg-config files to be used
only by nm-applet and the GNOME control center.

%package -n libnma-gir
License: %gpl2plus
Group: System/Libraries
Summary: GObject introspection data for the libnma
Requires: libnma = %version-%release

%description -n libnma-gir
GObject introspection data for the libnma.

%package -n libnma-gir-devel
License: %gpl2plus
Group: System/Libraries
Summary: GObject introspection devel data for the libnma
BuildArch: noarch
Requires: libnma-gir = %version-%release
Requires: libnma-devel = %version-%release

%description -n libnma-gir-devel
GObject introspection devel data for the libnma.

%package -n libnma-devel-doc
Summary: Development documentation for libnma-devel-doc
Group: Development/Documentation
BuildArch: noarch

%description -n libnma-devel-doc
This package contains development documentation for libnma-devel-doc.

%prep
%setup -n nm-applet-%version
%patch -p1
%build

%autoreconf
# Use GETTEXT_PACKAGE as PACKAGE:
# these variables are not the same and gettext doesn't use GETTEXT_PACKAGE at all.
sed -i 's/^PACKAGE = @PACKAGE@/PACKAGE = @GETTEXT_PACKAGE@/' po/Makefile.in.in
%configure \
	--disable-static \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
	%{subst_with selinux} \
	%{subst_with gcr} \
	--with-wwan \
	%{subst_with appindicator} \
	%{subst_with team} \
	--enable-introspection \
%if_with libnm_gtk
	--with-libnm-gtk \
%else
	--without-libnm-gtk \
%endif
	--without-libnma-gtk4 \
	--enable-mobile-broadband-provider-info \
	--enable-gtk-doc \
	--disable-silent-rules \
	--enable-more-warnings=%more_warnings

%make_build

%install
%makeinstall_std
%find_lang nm-applet

# For VPN plugins
mkdir -p %buildroot/%_datadir/gnome-vpn-properties

%check
make check

%files -f nm-applet.lang
%_bindir/*
%_iconsdir/hicolor/*/apps/*
%_sysconfdir/xdg/autostart/nm-applet.desktop
%_datadir/GConf/gsettings/nm-applet.convert
%_datadir/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
%doc %_man1dir/*.*

%_datadir/applications/*.desktop
%_datadir/metainfo/*.xml
%dir %_datadir/gnome-vpn-properties

%if_with libnm_gtk
%files -n libnm-gtk
%_libdir/libnm-gtk.so.*

%files -n libnm-gtk-devel
%_includedir/libnm-gtk/
%_libdir/libnm-gtk.so
%_pkgconfigdir/libnm-gtk.pc

%files -n libnm-gtk-gir
%_libdir/girepository-1.0/NMGtk-1.0.typelib

%files -n libnm-gtk-gir-devel
%_datadir/gir-1.0/NMGtk-1.0.gir
%endif

%files -n libnma
%_libdir/libnma.so.*

%files -n libnma-devel
%_includedir/libnma/
%_libdir/libnma.so
%_pkgconfigdir/libnma.pc

%files -n libnma-gir
%_libdir/girepository-1.0/NMA-1.0.typelib

%files -n libnma-gir-devel
%_datadir/gir-1.0/NMA-1.0.gir

%files -n libnma-devel-doc
%doc %_datadir/gtk-doc/html/libnma

%changelog
* Thu Oct 10 2019 Mikhail Efremov <sem@altlinux.org> 1.8.24-alt1
- Updated to 1.8.24.

* Wed Sep 04 2019 Mikhail Efremov <sem@altlinux.org> 1.8.22-alt2
- Patches from upstream:
  + editor: register to the connection-removed signal only once.
  + editor: avoid crash when checking for visible children.
- Update Russian translation (by Olesya Gerasimenko).

* Wed May 29 2019 Mikhail Efremov <sem@altlinux.org> 1.8.22-alt1
- Fix gettext domain.
- Drop intltool from BR.
- Updated to 1.8.22.

* Wed Feb 20 2019 Mikhail Efremov <sem@altlinux.org> 1.8.20-alt2
- Disable silent rules.
- Patch from upstream:
  + wifi-dialog: fix wrong free.

* Mon Feb 11 2019 Mikhail Efremov <sem@altlinux.org> 1.8.20-alt1
- Updated to 1.8.20.

* Fri Dec 14 2018 Mikhail Efremov <sem@altlinux.org> 1.8.18-alt2
- Disable libnm-gtk build.

* Mon Sep 10 2018 Mikhail Efremov <sem@altlinux.org> 1.8.18-alt1
- Updated to 1.8.18.

* Wed Aug 08 2018 Mikhail Efremov <sem@altlinux.org> 1.8.16-alt1
- Add mobile-broadband-provider-info to BR.
- Updated to 1.8.16.

* Mon Jul 16 2018 Mikhail Efremov <sem@altlinux.org> 1.8.14-alt1
- Drop "Don't allow to create new connection for missing device plugins"
  patch (closes: #35139).
- Patches from upstream:
  + connection-editor: don't defer creation of vpn connection to idle
  + c-e: fix leak in update_relabel_list_filename() (clear_name_if_present())
- Updated to 1.8.14.

* Mon Jun 04 2018 Mikhail Efremov <sem@altlinux.org> 1.8.12-alt2
- Patch from upstream:
    + Don't double-free priv->dupes (closes: #34980).

* Mon May 28 2018 Mikhail Efremov <sem@altlinux.org> 1.8.12-alt1
- Updated to 1.8.12.
- Use %%e2k macro.

* Thu Jan 11 2018 Mikhail Efremov <sem@altlinux.org> 1.8.11-alt1.git20180106
- Upstream git snapshot.

* Wed Nov 15 2017 Mikhail Efremov <sem@altlinux.org> 1.8.6-alt1
- Updated to 1.8.6.
- Enable teamd support.
- Fix build on e2k.

* Wed Sep 20 2017 Mikhail Efremov <sem@altlinux.org> 1.8.4-alt1
- Updated to 1.8.4.

* Tue Jul 04 2017 Mikhail Efremov <sem@altlinux.org> 1.8.3-alt1.git20170703
- Upstream git snapshot.

* Tue Apr 11 2017 Mikhail Efremov <sem@altlinux.org> 1.7.1-alt1.git20170410
- Upstream git snapshot.

* Mon Feb 06 2017 Mikhail Efremov <sem@altlinux.org> 1.4.5-alt1.git20170205
- Upstream git snapshot.

* Mon Oct 03 2016 Mikhail Efremov <sem@altlinux.org> 1.4.2-alt1
- Updated to 1.4.2.

* Fri Sep 16 2016 Mikhail Efremov <sem@altlinux.org> 1.4.1-alt1.git20160914
- Upstream git snapshot (nm-1-4 branch).

* Thu Aug 25 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Fix handling of wired 802-1x security setting.
- Updated to 1.4.0.

* Tue Aug 23 2016 Mikhail Efremov <sem@altlinux.org> 1.3.91-alt1
- Updated to 1.3.91 (1.4-rc1).

* Thu Aug 04 2016 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1
- Updated to 1.2.4.

* Fri May 27 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt2
- Fix libnma-devel requires.
- Fix work without gnome-keyring (closes: #32123).
- Fix wired 802-1x secrets saving.

* Wed May 11 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Fri Apr 22 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Don't require polkit-gnome.
- Updated to 1.2.0.

* Wed Apr 06 2016 Mikhail Efremov <sem@altlinux.org> 1.1.93-alt1
- Updated to 1.1.93 (1.2-rc1).

* Tue Mar 29 2016 Mikhail Efremov <sem@altlinux.org> 1.1.92-alt1
- Updated to 1.1.92 (1.2-beta3).

* Tue Mar 01 2016 Mikhail Efremov <sem@altlinux.org> 1.1.91-alt1
- Use nm-dbus-compat.h instead of dbus/dbus.h.
- Fix adsl connections hiding.
- Updated to 1.1.91 (1.2-beta2).

* Tue Jan 19 2016 Mikhail Efremov <sem@altlinux.org> 1.1.90-alt1
- Updated BR.
- Updated gnome-keyring patch.
- Updated to 1.1.90.

* Thu Dec 24 2015 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt1
- Updated to 1.0.10.

* Mon Nov 30 2015 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt1
- Updated to 1.0.8.

* Mon Nov 02 2015 Mikhail Efremov <sem@altlinux.org> 1.0.7-alt1.git20151102
- Upstream git snapshot (nma-1-0 branch).

* Mon Aug 31 2015 Mikhail Efremov <sem@altlinux.org> 1.0.6-alt1
- Package appdata file.
- configure: Fix macro name.
- Updated to 1.0.6.

* Wed Jul 15 2015 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1
- Don't allow to create new connection for missing device plugins.
- Updated to 1.0.4.

* Fri May 08 2015 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Minor spec cleanup.
- Updated to 1.0.2.

* Thu Feb 12 2015 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Fix 'no icon on start' bug again.
- Updated to 1.0.0.

* Fri Dec 05 2014 Mikhail Efremov <sem@altlinux.org> 0.9.10.1-alt1.git20141205
- Treat warrnings as errors again.
- Upstream git snapshot (nma-0-9-10 branch).

* Wed Oct 29 2014 Mikhail Efremov <sem@altlinux.org> 0.9.10.1-alt1.git20141029
- Upstream git snapshot (nma-0-9-10 branch).

* Tue Jul 29 2014 Mikhail Efremov <sem@altlinux.org> 0.9.10.0-alt1
- Updated to 0.9.10.0.

* Mon Jun 23 2014 Mikhail Efremov <sem@altlinux.org> 0.9.9.98-alt1
- Updated to 0.9.9.98 (0.9.10-rc1).

* Tue Apr 22 2014 Mikhail Efremov <sem@altlinux.org> 0.9.9.0-alt2.git20140422
- Upstream git snapshot (master branch).

* Fri Mar 28 2014 Mikhail Efremov <sem@altlinux.org> 0.9.9.0-alt2.git20140327
- Disable gnome-bluetooth support.
- Temporary don't treat warrnings as errors again.
- Upstream git snapshot (master branch)

* Fri Feb 07 2014 Mikhail Efremov <sem@altlinux.org> 0.9.9.0-alt1.git20140205
- Drop --with-gtkver configure option.
- Upstream git snapshot (master branch)

* Thu Nov 14 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.8-alt1
- Updated to 0.9.8.8.

* Wed Oct 30 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt4
- Use libnm-* devel packages.

* Thu Sep 26 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt3
- Updated from upstream git:
  + Updtated translations.
  + nma-bt-device: fix creation of BT settings when creating connection.

* Tue Sep 17 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt2
- Rebuild with libgnome-bluetooth-3.9.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt1
- Don't reload DBUS configuration during install.
- Rename to NetworkManager-applet-gtk.
- Updated to 0.9.8.4.

* Fri Jul 12 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.2-alt2
- Fix interaction with gnome-keyring.

* Fri Jun 14 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.2-alt1
- Updated to 0.9.8.2.

* Tue Jun 04 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt4
- Require iso-codes.

* Tue Apr 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt3
- Enable new ModemManager1 interface support (closes: #28788).
- Updated Russian translation (from upstream git).

* Tue Mar 12 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt2
- Autostart nm-applet in the KDE too (closes: #28666).

* Thu Feb 21 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt1
- Updated to 0.9.8.0.

* Thu Feb 14 2013 Mikhail Efremov <sem@altlinux.org> 0.9.7.997-alt1
- Treat warrnings as errors.
- Updated to 0.9.7.997 (0.9.8-beta2).

* Tue Sep 25 2012 Mikhail Efremov <sem@altlinux.org> 0.9.6.2-alt2
- Temporary don't treat warrnings as errors again.
- Rebuild against libgnome-bluetooth.so.11.

* Tue Aug 14 2012 Mikhail Efremov <sem@altlinux.org> 0.9.6.2-alt1
- Updated to 0.9.6.2.

* Wed Aug 08 2012 Mikhail Efremov <sem@altlinux.org> 0.9.6.0-alt1
- Fix some leaks (patch from upstream git).
- Updated to 0.9.6.0.

* Tue Jul 03 2012 Mikhail Efremov <sem@altlinux.org> 0.9.5.95-alt1
- Treat warrnings as errors again.
- Updated from upstream git (7e1c118eee).
- Updated to 0.9.5.95.

* Fri Apr 27 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.1-alt3
- Updated translations from upstream git.
- Add gcr to requires.

* Tue Apr 10 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.1-alt2
- Fix %%_datadir/libnm-gtk packaging.

* Mon Apr 02 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.1-alt1
- Updated from upstream git (e4e5146f1e).
- 0.9.4.1.

* Thu Mar 15 2012 Mikhail Efremov <sem@altlinux.org> 0.9.3.995-alt1.git20120315
- upstream git snapshot (master branch)

* Wed Feb 29 2012 Mikhail Efremov <sem@altlinux.org> 0.9.3.990-alt2.git20120228
- Temporary don't treat warrnings as errors.

* Tue Feb 28 2012 Mikhail Efremov <sem@altlinux.org> 0.9.3.990-alt1.git20120228
- upstream git snapshot (master branch)

* Fri Nov 11 2011 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Rename src.rpm package again.
- 0.9.2 release.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.95-alt1
- 0.9.1.95 (0.9.2-rc1).

* Wed Sep 21 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.90-alt2.git20110920
- Fix typo in requires.

* Tue Sep 20 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.90-alt1.git20110920
- Add iso-codes to BR.
- upstream git snapshot (master branch)

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- Don't package empty files.
- 0.9.0 release.

* Tue Jun 07 2011 Mikhail Efremov <sem@altlinux.org> 0.8.9997-alt1.git20110607
- upstream git snapshot (master branch)

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt2.git20110510
- Build with GTK+3.
- Rename src.rpm package.

* Tue May 10 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt1.git20110510
- Build with libnotify-0.7.
- Own %%_datadir/gnome-vpn-properties.
- Enable tests.
- upstream git snapshot (master branch)

* Wed Mar 23 2011 Mikhail Efremov <sem@altlinux.org> 0.8.997-alt1.git20110323
- Changed libexecdir to %%_libexecdir/NetworkManager.
- Don't create auto wired connection.
- Drop Packager from spec.
- upstream git snapshot (master branch)

* Thu Nov 11 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20101106
- Fix source tarball and general patch packaging.

* Sun Nov 07 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1.git20101106
- upstream git snapshot
    (almost corresponds with 0.8.2 release, but builded from master branch).

* Tue Oct 19 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt3.git20100914
- rebuild with libgnome-bluetooth.so.8

* Tue Sep 14 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100914
- upstream git snapshot (master branch)

* Thu Jul 22 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100722
- spec cleanup
- upstream git snapshot
    (almost corresponds with 0.8.1 release, but builded from master branch).

* Wed Jun 30 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100628
- drop nm-applet.desktop.

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1.git20100628
- upstream git snapshot (master branch)

* Thu May 27 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt2.git20100525
- build gnome-bluetooth plugin

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100525
- upstream git snapshot
- Updated Russian translation (by Andrey Cherepanov).

* Thu Apr 29 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20100427
- upstream git snapshot

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- 0.8.0 release

* Thu Feb 04 2010 Mikhail Efremov <sem@altlinux.org> 0.7.999-alt1.git20100204
- Don't package ChangeLog.
- upstream git snapshot

* Sat Jan 09 2010 Mikhail Efremov <sem@altlinux.org> 0.7.998-alt1
- 0.7.998 (0.8-rc2)

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 0.7.997-alt1.git20091209
- upstream git snapshot

* Fri Nov 27 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt2.git20091124
- add polkit-gnome require (closes #22371).

* Tue Nov 24 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091124
- upstream git snapshot

* Wed Oct 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091026
- 0.7.996 (upstream git snapshot).

* Wed Oct 21 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1.997-alt1
- 0.7.1.997 (0.7.2-rc3)

* Mon Oct 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.git20091005
- Russian translation by Andrey Cherepanov.
- new upstream git snapshot (NETWORKMANAGER_APPLET_0_7 branch)

* Tue Jul 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.git20090728
- new upstream git snapshot (NETWORKMANAGER_APPLET_0_7 branch)

* Thu Jul 16 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.git20090716
- upstream git snapshot (NETWORKMANAGER_APPLET_0_7 branch)
- removed libmbca support.

* Wed Apr 15 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Release 0.7.1

* Mon Apr 06 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt1
- 0.7.0.100 (0.7.1-rc4)

* Thu Mar 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt1
- 0.7.0.99 (0.7.1-rc3)

* Thu Feb 26 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.98-alt1
- 0.7.0.98 (0.7.1-rc2)
- pack source as tar instead tar.gz

* Thu Feb 19 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.97-alt1
- 0.7.0.97 (0.7.1-rc1)

* Thu Jan 22 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt9
- applied Ubuntu patch for libmbca support.

* Fri Dec 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt8
- enable 'Available for all users' checkbutton

* Thu Dec 11 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt7
- fix 'no icon' bug again 

* Wed Dec 03 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt6
- Release NetworkManager 0.7

* Tue Dec 02 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt5.svn.r1043
- create auto wired connection if needed

* Tue Nov 25 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt4.svn.r1043
- BuildRequires fixed

* Mon Nov 24 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn.r1043
- new svn snapshot
- nm-applet-no-icon-fix.patch removed (obsolete)

* Fri Nov 21 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn.r986
- update_menus removed (obsolete)
- Requires fixed
- disable 'Available for all users' checkbutton (it does not work yet)

* Wed Nov 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn.r986
- Requires and BuildRequires updated

* Tue Oct 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1.svn.r986
- new svn ref

* Fri Oct 10 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1.svn.r838.M41.4
- fix 'no icon' bug  

* Thu Sep 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1.svn.r838.M41.3
- autostarting in KDE 

* Mon Sep 08 2008 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1.svn.r838.M41.2
- don't call gtk-update-icon-cache in %%post{,un}

* Fri Sep 05 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt1.svn.r838.M41.1
- port to M41 

* Wed Aug 13 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn.r838
- new svn snapshot
- spec updated

* Tue Jul 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080722
- new svn snapshot (797)
- .desktop file is added (applet can start from the menu now)

* Wed May 28 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080527
- new svn snapshot (730)
- spec post/postun sections fixed

* Tue Apr 29 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080428
- new svn snapshot (705)
- spec cleanup

* Tue Apr 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080419
- initial build
