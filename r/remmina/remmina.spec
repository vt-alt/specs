%def_without telepathy

%define _unpackaged_files_terminate_build 1

Name: remmina
Version: 1.3.7
Release: alt1
Summary: Remote Desktop Client

Group: Networking/Remote access
License: GPLv2+ and MIT
Url: http://remmina.sourceforge.net
Source: %name-%version.tar
#Source1: ru.po
Patch1: fix_plugins_search_v1.2.32.1.patch

Requires: icon-theme-hicolor

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: gettext pkgconfig(libpcre)
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: libgcrypt-devel libssl-devel
BuildRequires: libjpeg-devel libtasn1-devel libpng-devel libpixman-devel zlib-devel
BuildRequires: pkgconfig(glib-2.0) >= 2.30 pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(avahi-ui-gtk3) >= 0.6.30 pkgconfig(avahi-client) >= 0.6.30
BuildRequires: pkgconfig(freerdp2) >= 2.0.0 libcups-devel
BuildRequires: pkgconfig(winpr2)
BuildRequires: pkgconfig(gtk+-3.0) pkgconfig(gdk-pixbuf-2.0) pkgconfig(pango) pkgconfig(cairo) pkgconfig(atk) libwayland-client-devel
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libssh) >= 0.6
BuildRequires: pkgconfig(libvncserver)
%{?_with_telepathy:BuildRequires: pkgconfig(telepathy-glib) pkgconfig(dbus-glib-1)}
BuildRequires: pkgconfig(vte-2.91)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(spice-client-gtk-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libsodium)

%add_findreq_skiplist %_datadir/%name/external_tools/*

%description
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

Remmina supports multiple network protocols in an integrated and consistent
user interface. Currently RDP, VNC, XDMCP and SSH are supported

%package devel
Summary: remmina development headers
Group: Development/Other

%description devel
Files required to build plugins for remmina

%package plugins
Summary: A set of plugins for remmina
Group: Networking/Remote access
BuildArch: noarch

Requires: %name
Requires: %name-plugins-exec
Requires: %name-plugins-secret
Requires: %name-plugins-nx
Requires: %name-plugins-rdp
Requires: %name-plugins-st
Requires: %name-plugins-vnc
Requires: %name-plugins-xdmcp
Requires: %name-plugins-spice

%description plugins
A set of plugins for %name remote desktop client

%package plugins-exec
Summary: External execution plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-exec
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin to execute external processes (commands or
applications) from the Remmina window.

%package plugins-secret
Summary: Keyring integration for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR
Provides: %name-plugins-gnome = %EVR
Obsoletes: %name-plugins-gnome < %EVR

%description plugins-secret
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin with keyring support for the Remmina remote
desktop client.

%package plugins-nx
Summary: NX plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR
Requires: nxproxy

%description plugins-nx
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the NX plugin for the Remmina remote desktop client.

%package plugins-rdp
Summary: RDP plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR
Requires: freerdp-plugins-standard

%description plugins-rdp
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the Remote Desktop Protocol (RDP) plugin for the Remmina
remote desktop client.

%package plugins-st
Summary: Simple Terminal plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-st
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the Simple Terminal plugin for the Remmina remote desktop
client.

%package plugins-vnc
Summary: VNC plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-vnc
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the VNC plugin for the Remmina remote desktop
client.

%package plugins-xdmcp
Summary: XDMCP plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR
Requires: xorg-xephyr

%description plugins-xdmcp
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the XDMCP plugin for the Remmina remote desktop
client.

%package plugins-spice
Summary: SPICE plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-spice
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the SPICE plugin for the Remmina remote desktop
client.

%package gnome-session
Summary: Gnome Shell session for Remmina kiosk mode
Group: Networking/Remote access
Requires: %name = %EVR
Requires: gnome-session

%description gnome-session
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains Remmina kiosk mode, including a Gnome Shell session
that shows up under the display manager session menu.

%prep
%setup
%patch1 -p1

#cp -f %SOURCE1 po/

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DWITH_APPINDICATOR=OFF \
    -DWITH_AVAHI=ON \
    -DWITH_FREERDP=ON \
    -DWITH_GCRYPT=ON \
    -DWITH_GETTEXT=ON \
    -DWITH_LIBSSH=ON \
     %{?_without_telepathy:-DWITH_TELEPATHY=OFF} \
    -DWITH_VTE=ON \
    -DREMMINA_PLUGINDIR=%_libdir/remmina/plugins

%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_pkgconfigdir
install -p -m 644 data/%name.pc.in %buildroot%_pkgconfigdir/%name.pc

subst "s|@prefix@|%prefix|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@exec_prefix@|%_exec_prefix|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@libdir@|%_libdir|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@includedir@|%_includedir|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@VERSION@|%version|g" %buildroot%_pkgconfigdir/%name.pc

%find_lang %name

%files -f %name.lang
%doc AUTHORS CHANGELOG.md README.md
%_bindir/%name
%_bindir/remmina-file-wrapper
%_datadir/metainfo/*.appdata.xml
%_datadir/mime/*/*.xml
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*/actions/*.*
%_iconsdir/hicolor/*/apps/*.*
%_iconsdir/hicolor/*/emblems/remmina-sftp-symbolic.svg
%_iconsdir/hicolor/*/emblems/remmina-ssh-symbolic.svg
%_datadir/%name
%_man1dir/remmina.1.*
%_man1dir/remmina-file-wrapper.1.*
%dir %_libdir/remmina
%dir %_libdir/remmina/plugins

%files plugins
%files plugins-exec
%_libdir/remmina/plugins/remmina-plugin-exec.so

%files plugins-secret
%_libdir/remmina/plugins/remmina-plugin-secret.so

%files plugins-nx
%_libdir/remmina/plugins/remmina-plugin-nx.so
%_iconsdir/hicolor/*/emblems/remmina-nx-symbolic.svg

%files plugins-rdp
%_libdir/remmina/plugins/remmina-plugin-rdp.so
%_iconsdir/hicolor/*/emblems/remmina-rdp-ssh-symbolic.svg
%_iconsdir/hicolor/*/emblems/remmina-rdp-symbolic.svg

%files plugins-st
%_libdir/remmina/plugins/remmina-plugin-st.so
%_iconsdir/hicolor/*/emblems/remmina-tool-symbolic.svg

%files plugins-vnc
%_libdir/remmina/plugins/remmina-plugin-vnc.so
%_iconsdir/hicolor/*/emblems/remmina-vnc-ssh-symbolic.svg
%_iconsdir/hicolor/*/emblems/remmina-vnc-symbolic.svg

%files plugins-xdmcp
%_libdir/remmina/plugins/remmina-plugin-xdmcp.so
%_iconsdir/hicolor/*/emblems/remmina-xdmcp-ssh-symbolic.svg
%_iconsdir/hicolor/*/emblems/remmina-xdmcp-symbolic.svg

%files plugins-spice
%_libdir/remmina/plugins/remmina-plugin-spice.so
%_iconsdir/hicolor/*/emblems/remmina-spice-ssh-symbolic.svg
%_iconsdir/hicolor/*/emblems/remmina-spice-symbolic.svg

%files gnome-session
%_bindir/gnome-session-remmina
%_bindir/remmina-gnome
%_datadir/gnome-session/sessions/remmina-gnome.session
%_datadir/xsessions/remmina-gnome.desktop
%_man1dir/gnome-session-remmina.1.*
%_man1dir/remmina-gnome.1.*

%files devel
%_includedir/%name
%_pkgconfigdir/*

%changelog
* Mon Dec 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.7-alt1
- 1.3.7
- drop local localization ru.po

* Thu Nov 21 2019 Ivan A. Melnikov <iv@altlinux.org> 1.3.6-alt2
- package remmina-file-wrapper.sh (closes: #37514)

* Tue Sep 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.6-alt1
- 1.3.6

* Tue Apr 30 2019 Pavel Moseev <mars@altlinux.org> 1.3.4-alt2
- update translation

* Mon Mar 25 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.4-alt1
- 1.3.4

* Fri Feb 01 2019 Ivan A. Melnikov <iv@altlinux.org> 1.3.2-alt1
- 1.3.2 (closes: #35993)

* Fri Jan 25 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- 1.3.0

* Wed Jan 16 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.32.1-alt1
- 1.2.32.1
- split plugins package
- add gnome-session package for kiosk mode

* Wed Aug 29 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt5.rc21%ubt
- fix to build with new libssh

* Wed Jun 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt4.rc21%ubt
- fix plugins search in version 1.2.0-rc21

* Tue Jun 26 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt3.rc21%ubt
- increase release number for allow backport to p8

* Wed Jun 13 2018 Oleg Gadelshin <olegeg@altlinux.ru> 1.2.0-alt2.rc20%ubt
- increase release number to alt2
- add remmina-1.2.0-rdp-passwordispin_option.patch for use of smartcard pin as password

* Tue Sep 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1.rc20%ubt
- 1.2.0-rcgit.20
- increase release number for allow backport to p8

* Wed Jul 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc19
- 1.2.0-rcgit.19

* Tue Jan 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc17
- 1.2.0-rcgit.17

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc11.1
- add skip requires for external tools

* Thu Apr 07 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc11
- 1.2.0.rcgit.11

* Tue Aug 04 2015 Michael Shigorin <mike@altlinux.org> 1.1.2-alt2
- fixed plugins path on non-x86_64
- fixed build (closes: #31184)
- added missing R: %name (closes: #27266)

* Sat Mar 21 2015 Mikhail Kolchin <mvk@altlinux.org> 1.1.2-alt1
- new version

* Thu Mar 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt3.1
- Fixed build

* Wed Sep 18 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt3
- Revert "FreeRDP moved from kbd to locale" (see https://github.com/FreeRDP/Remmina/pull/31)

* Thu Mar 22 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt2
- build from git ffba771dcd70e37635e9c8ff3a905273c933294a (ALT #27099)

* Fri Feb 10 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- new version

* Tue Jan 17 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.99.1-alt1.git
- new version
- union of package remmina and reminna-plugins
- fix (ALT #26205)

* Tue Feb 01 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.3-alt1
- new version

* Sun Jan 30 2011 Denis Baranov <baraka@altlinux.ru> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)

* Thu Oct 28 2010 Mykola Grechukh <gns@altlinux.ru> 0.8.3-alt1
- new version

* Thu Aug 12 2010 Mykola Grechukh <gns@altlinux.ru> 0.8.1-alt1
- new version

* Tue Jul 20 2010 Mykola Grechukh <gns@altlinux.ru> 0.8.0-alt1
- first build for ALT Linux

* Wed May 05 2010 Damien Durand <splinux@fedoraproject.org> - 0.7.5-1
- Upstream release, 0.7.5
- Remove the old "DSO" patch

* Tue Mar 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.4-2
- Add patch to fix DSO issue

* Sat Feb 27 2010 Damien Durand <splinux@fedoraproject.org> 0.7.4-1
- Update to 0.7.4
- Fix License tag

* Sun Feb 14 2010 Damien Durand <splinux@fedoraproject.org> 0.7.3-1
- Upstream release
- Add rdesktop, xorg-x11-server-Xephyr in Requires
- Add grdc in Provides/Obsoletes
- Add --enable-vnc=dl in %%configure
- Remove unneeded README.LibVNCServer
- Fix "icons/hicolor" path

* Thu Jan 07 2010 Damien Durand <splinux@fedoraproject.org> 0.7.2-2
- Fix Summary
- Split BuildRequires

* Thu Jan 07 2010 Damien Durand <splinux@fedoraproject.org> 0.7.2-1
- Initial release
