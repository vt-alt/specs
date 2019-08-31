%def_enable gtk_doc

Name: muffin
Version: 4.2.2
Release: alt2

Summary: Window and compositing manager based on Clutter
License: GPLv2+
Group: Graphical desktop/GNOME

Url: https://github.com/linuxmint/muffin
# To generate tarball
# wget https://github.com/linuxmint/muffin/tarball/1.0.2 -O muffin-1.0.2.tar.gz
Source: %name-%version.tar
Source1: pkg.m4
Patch: %name-%version-%release.patch

# since 4.0 muffin forks Cogl and Clutter libraries into own private libraries
%filter_from_provides /typelib[(]Cally[)]/d
%filter_from_provides /typelib[(]Clutter[)]/d
%filter_from_provides /typelib[(]ClutterX11[)]/d
%filter_from_provides /typelib[(]Cogl[)]/d
%filter_from_provides /typelib[(]CoglPango[)]/d
%filter_from_requires /typelib[(]Cally[)]/d
%filter_from_requires /typelib[(]Clutter[)]/d
%filter_from_requires /typelib[(]ClutterX11[)]/d
%filter_from_requires /typelib[(]Cogl[)]/d
%filter_from_requires /typelib[(]CoglPango[)]/d

%filter_from_provides /gir[(]Cally[)]/d
%filter_from_provides /gir[(]Clutter[)]/d
%filter_from_provides /gir[(]ClutterX11[)]/d
%filter_from_provides /gir[(]Cogl[)]/d
%filter_from_provides /gir[(]CoglPango[)]/d
%filter_from_requires /gir[(]Cally[)]/d
%filter_from_requires /gir[(]Clutter[)]/d
%filter_from_requires /gir[(]ClutterX11[)]/d
%filter_from_requires /gir[(]Cogl[)]/d
%filter_from_requires /gir[(]CoglPango[)]/d

# There is already registered upstream issue https://github.com/linuxmint/muffin/issues/199
# But untill it will be fixed by Cinnamon devs we handle it manually.
%filter_from_provides /typelib(Meta)/d
%filter_from_provides /gir(Meta)/d

Requires: lib%name = %version-%release
Requires: zenity

BuildPreReq: rpm-build-gir >= 0.7.1-alt6
BuildPreReq: libgtk+3-devel >= 3.3.3
BuildRequires: libcanberra-gtk3-devel libstartup-notification-devel
BuildRequires: libXrandr-devel libXcursor-devel libXcomposite-devel
BuildRequires: libXinerama-devel libXext-devel libSM-devel
BuildRequires: gtk-doc gnome-common intltool gnome-doc-utils
BuildRequires: zenity
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libcinnamon-desktop-devel libcinnamon-desktop-gir-devel
BuildRequires: libxkbcommon-x11-devel libxkbfile-devel xkeyboard-config-devel
BuildRequires: libXi-devel libXdamage-devel
BuildRequires: libjson-glib-devel libjson-glib-gir-devel
BuildRequires: libgbm-devel
BuildRequires: libwayland-server-devel libwayland-egl-devel
BuildRequires: libdrm-devel libGL-devel
BuildRequires: libxcb-devel libXtst-devel
BuildRequires: libgudev-devel libinput-devel

%description
Muffin is a window and compositing manager that displays and manages
your desktop via OpenGL. Muffin combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

While Muffin can be used stand-alone, it is primarily intended to be
used as the display core of a larger system such as Cinnamon.
For this reason, Muffin is very extensible via plugins, which
are used both to add fancy visual effects and to rework the window
management behaviors to meet the needs of the environment.
%package utils

Summary: Additional utilities for %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description utils
Utilities for testing Metacity/Muffin themes.

%package -n lib%name
Summary: Shared libraries for %name
Group: System/Libraries
# manual dependencies
Requires: typelib(Gtk) = 3.0

%description -n lib%name
Shared libraries for Muffin and its plugins.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C
Requires: lib%name = %version-%release
# manual dependencies
Requires: gir(Gtk) = 3.0

%description -n lib%name-devel
Header files and libraries for developing Muffin plugins.

%package -n lib%name-devel-doc
Summary: Development doc package for %name
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Development docs package for Muffin.

%package -n lib%name-gir
Summary: GObject introspection data for the Muffin library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Muffin library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Muffin library
Group: System/Libraries
Requires: lib%name-devel = %version-%release lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Muffin library

%set_typelibdir %_libdir/%name
%set_girdir %_libdir/%name

%prep
%setup -n %name-%version
%patch0 -p1
[ ! -d m4 ] && mkdir m4
cp %SOURCE1 m4/

%ifarch %e2k
sed -i 's,-Werror=pointer-arith,,' */configure.ac
%endif

%build
%autoreconf
%configure --disable-static \
	   --disable-schemas-compile \
	   %{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_man1dir/muffin.1*
%_man1dir/muffin-message.1*
%_bindir/muffin
%_bindir/muffin-message
%_libexecdir/muffin-restart-helper
%_desktopdir/*.desktop
%_datadir/muffin
%_datadir/glib-2.0/schemas/org.cinnamon.muffin.gschema.xml
%doc README AUTHORS NEWS HACKING doc/theme-format.txt

%files utils
%_bindir/muffin-theme-viewer
%_bindir/muffin-window-demo
%_man1dir/muffin-theme-viewer.1*
%_man1dir/muffin-window-demo.1*

%files -n lib%name
%_libdir/lib*.so.*
%dir %_libdir/%name
%exclude %_libdir/%name/*.la
%_libdir/%name/*.so

%dir %_libdir/%name/plugins
%_libdir/%name/plugins/default.so

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
%endif

%files -n lib%name-gir
%_libdir/%name/*.typelib

%files -n lib%name-gir-devel
%_libdir/%name/*.gir


%changelog
* Mon Aug 19 2019 Anton Midyukov <antohami@altlinux.org> 4.2.2-alt2
- Not requires GConf

* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 4.2.2-alt1
- 4.2.2-1-g3c9fdcf

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 4.2.1-alt1
- 4.2.1

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sat Jun 15 2019 Michael Shigorin <mike@altlinux.org> 4.0.7-alt1.1
- E2K: ftbfs workaround until lcc 1.23.19+ (mcst#4023)

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.org> 4.0.7-alt1
- 4.0.7

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 4.0.5-alt1
- 4.0.5

* Fri Dec 07 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.3-alt2
- add libGL-devel BR, do not rely on indirect deps

* Tue Dec 4 2018 Vladimir Didenko <cow@altlinux.org> 4.0.3-alt1
- 4.0.3-3-gc3ffb54

* Fri Nov 23 2018 Vladimir Didenko <cow@altlinux.org> 4.0.2-alt1.1
- fix requires and provides

* Wed Nov 21 2018 Vladimir Didenko <cow@altlinux.org> 4.0.2-alt1
- 4.0.2

* Fri Sep 14 2018 Vladimir Didenko <cow@altlinux.org> 3.8.3-alt1
- 3.8.3

* Mon Jul 23 2018 Vladimir Didenko <cow@altlinux.org> 3.8.2-alt2
- 3.8.2-5-g3732b82

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon May 7 2018 Vladimir Didenko <cow@altlinux.org> 3.8.1-alt1
- 3.8.1-1-g8188c39

* Thu May 3 2018 Vladimir Didenko <cow@altlinux.org> 3.8.0-alt1
- 3.8.0

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Aug 23 2017 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- 3.4.1

* Fri May 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0-1-g3e72a6a

* Tue Jan 31 2017 Vladimir Didenko <cow@altlinux.org> 3.2.2-alt1
- 3.2.2

* Fri Nov 25 2016 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt1
- 3.2.1

* Fri Nov 11 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Oct 4 2016 Vladimir Didenko <cow@altlinux.org> 3.0.5-alt3
- Fix requires

* Mon Oct 3 2016 Vladimir Didenko <cow@altlinux.org> 3.0.5-alt2
- Fix build requires

* Fri Jun 24 2016 Vladimir Didenko <cow@altlinux.org> 3.0.5-alt1
- 3.0.5

* Fri May 20 2016 Vladimir Didenko <cow@altlinux.org> 3.0.4-alt1
- 3.0.4

* Thu May 12 2016 Vladimir Didenko <cow@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Apr 20 2016 Vladimir Didenko <cow@altlinux.org> 2.8.5-alt3
- Better fix for wrong context menu position.

* Mon Apr 18 2016 Vladimir Didenko <cow@altlinux.org> 2.8.5-alt2
- Fix wrong context menu position.

* Mon Dec 14 2015 Vladimir Didenko <cow@altlinux.org> 2.8.4-alt1
- 2.8.4-2-gffb688b

* Mon Nov 16 2015 Vladimir Didenko <cow@altlinux.org> 2.8.3-alt1
- 2.8.3-1-g0315e39

* Mon Nov 2 2015 Vladimir Didenko <cow@altlinux.org> 2.8.1-alt2
- 2.8.1-2-g72dacf5

* Wed Oct 21 2015 Vladimir Didenko <cow@altlinux.org> 2.8.1-alt1
- 2.8.1

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0-2-g8c976c9

* Mon Jul 27 2015 Vladimir Didenko <cow@altlinux.org> 2.6.1-alt2
- don't provide Meta typelib (closes: #31171)

* Tue Jun 2 2015 Vladimir Didenko <cow@altlinux.org> 2.6.1-alt1
- 2.6.1

* Wed May 20 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt1
- 2.5.0

* Fri Feb 6 2015 Vladimir Didenko <cow@altlinux.org> 2.4.4-alt1
- 2.4.4

* Fri Jan 16 2015 Vladimir Didenko <cow@altlinux.org> 2.4.3-alt1
- 2.4.3

* Tue Nov 25 2014 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt1
- 2.4.2

* Mon Nov 10 2014 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Oct 14 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- git20141002

* Tue Jul 22 2014 Vladimir Didenko <cow@altlinux.org> 2.2.6-alt1
- 2.2.6

* Thu Jun 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.5-alt1
- 2.2.5

* Wed May 21 2014 Vladimir Didenko <cow@altlinux.org> 2.2.4-alt1
- 2.2.4

* Mon May 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Apr 30 2014 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt2
- 2.2.1-9-g570843c

* Fri Apr 18 2014 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Apr 7 2014 Vladimir Didenko <cow@altlinux.org> 2.0.5-alt3
- git20140404

* Tue Mar 5 2014 Vladimir Didenko <cow@altlinux.org> 2.0.5-alt2
- build with gnome-3.12

* Mon Nov 25 2013 Vladimir Didenko <cow@altlinux.org> 2.0.5-alt1
- 2.0.5-4-g6f67cf3

* Tue Nov 12 2013 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- 2.0.2

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt4
- rebuild for GNOME-3.10

* Thu Aug 29 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt3
- v1.8.2-58-gc13a698

* Mon Aug 5 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt2
- 1.8.2-51-gd05c4c6

* Tue May 21 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt1
- 1.8.2

* Fri May 17 2013 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon May 6 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0

* Wed Apr 24 2013 Vladimir Didenko <cow@altlinux.org> 1.7.3-alt2
- 1.7.3-16-ge0ad43f
- created gir and gir-devel subpackages
- use set_typelibdir and set_girdir macroses.

* Tue Apr 16 2013 Vladimir Didenko <cow@altlinux.org> 1.7.3-alt1
- 1.7.3

* Tue Mar 12 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt2
- add support for gtk-3.7 enum values

* Fri Feb 22 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt1
- 1.7.1-3-g2f496ac

* Fri Nov 16 2012 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt2
- rebuilt for Sisyphus

* Wed Oct 31 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.1.2-alt1
- 1.1.2

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Wed May 30 2012 Michael Shigorin <mike@altlinux.org> 1.0.3-alt2
- rebuilt for Sisyphus

* Wed May 23 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.0.3-alt1
- update to 1.0.3

* Thu Apr 12 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- removed obsolete configure option
- added lost %%post, %%preun scripts
- simplified buildreqs, fixed reqs
- more cleanups

* Wed Apr 11 2012 Michael Shigorin <mike@altlinux.org> 1.0.2-alt1
- rebuilt for Sisyphus
- libification
- spec cleanup

* Mon Apr 09 2012 Vyacheslav Dikonov <slava@altlinux.ru> 1.0.2-slava1
- ALTLinux build
- linuxmint-muffin-a5935f8
- muffin-XKeycodeToKeySum-fix.patch

* Tue Mar 13 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-1
- update to 1.0.2

* Thu Feb 17 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0.1-1
- update version to 1.0.1

* Thu Feb 02 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-2
- make review changes

* Wed Jan 04 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-1
- initial package based on fedora mutter srpm
