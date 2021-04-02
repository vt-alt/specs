%define ver_major 3.8

Name: vino-mate
Version: %ver_major.1
Release: alt5

Summary: A remote desktop system for MATE
License: GPL
URL: https://wiki.gnome.org/Projects/Vino
Group: Networking/Remote access
Packager: Korneechev Evgeniy <ekorneechev@altlinux.org>

Source: %name-%version.tar.xz
Patch0: vino-3.8.1-fc-allocation.patch
Patch1: vino-3.8.1-alt-fixed_MATE.patch
Patch2: vino-handle-close-notification.patch

BuildRequires: intltool gnome-common desktop-file-utils libnm-devel
BuildRequires: libgio-devel libgtk+3-devel libsoup-devel libdbus-devel
BuildRequires: libXdamage-devel libXtst-devel libSM-devel xorg-cf-files xorg-inputproto-devel
BuildRequires: libavahi-glib-devel libgcrypt-devel libgnutls-devel libsecret-devel
BuildRequires: libjpeg-devel libnotify-devel >= 0.7 zlib-devel
BuildRequires: libtelepathy-glib-devel >= 0.11.6

Conflicts: vino
Provides: mate-vino = %version-%release

%description
Vino is a VNC server for MATE. It allows remote users to
connect to a running MATE session using VNC.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export LDFLAGS="$LDFLAGS -lgcrypt"
%configure \
	--disable-http-server \
	--disable-schemas-compile
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang vino

%files -f vino.lang
%_bindir/*
%_libexecdir/vino-server
%dir %_datadir/vino
%_datadir/vino/*.ui
%_datadir/vino/webservices
%_datadir/applications/*.desktop
%_sysconfdir/xdg/autostart/vino-server.desktop
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Vino.service
%_datadir/telepathy/clients/Vino.client
%config %_datadir/glib-2.0/schemas/*.xml
%_datadir/GConf/gsettings/org.gnome.Vino.convert
%doc AUTHORS NEWS README docs/TODO docs/remote-desktop.txt docs/debugging.txt

%changelog
* Mon Mar 29 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt5
- Handle close notification.

* Mon Dec 17 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 3.8.1-alt4
- updated buildreqs

* Tue Oct 17 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 3.8.1-alt3
- renamed to vino-mate
 + fixed url and description
 + fixed start on MATE (alt patch)

* Tue Jun 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt2
- fixed crash (fc patch)

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Fri Sep 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.90-alt1
- 3.5.90

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Nov 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Sep 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Mon Jul 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Sep 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.91-alt1
- 2.31.91

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Mon Oct 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91
- updated buildreqs

* Thu Jun 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt2
- fix build with new gnutls.

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Thu Mar 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- drop upstreamed patch
- updated buildreqs

* Sat Feb 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- added libglade-devel to buildreqs

* Fri Dec 05 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- updated buildreqs

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 2.22.2-alt2
- fix desktop file

* Sat Jul 05 2008 Igor Zubkov <icesik@altlinux.org> 2.22.2-alt1
- 2.22.1 -> 2.22.2

* Mon May 05 2008 Igor Zubkov <icesik@altlinux.org> 2.22.1-alt2
- build with --enable-gnome-keyring

* Tue Apr 15 2008 Igor Zubkov <icesik@altlinux.org> 2.22.1-alt1
- 2.18.1 -> 2.22.1
- buildreq

* Mon Apr 14 2008 Igor Zubkov <icesik@altlinux.org> 2.18.1-alt1
- build for Sisyphus

* Sat Apr 28 2007 Daisuke SUZUKI <daisuke@linux.or.jp> 2.18.1-0vl1
- new upstream release

* Sat Apr 01 2006 Daisuke SUZUKI <daisuke@linux.or.jp> 2.13.5-0vl3
- run gtk-update-icon-cache in %%post script.

* Mon Mar 13 2006 Daisuke SUZUKI <daisuke@linux.or.jp> 2.13.5-0vl2
- enable avahi, add BuildRequires: avahi-devel

* Wed Mar 08 2006 Daisuke SUZUKI <daisuke@linux.or.jp> 2.13.5-0vl1
- new upstream release

* Mon Sep 19 2005 Daisuke SUZUKI <daisuke@linux.or.jp> 2.12.0-0vl1
- new upstream release

* Tue Mar 22 2005 Daisuke SUZUKI <daisuke@linux.or.jp> 2.10.0-0vl1
- new upstream version

* Tue Nov 30 2004 Daisuke SUZUKI <daisuke@linux.or.jp> 2.8.1-0vl1
- initial build for Vine Linux
- add japanese summary and description.

* Tue Oct 12 2004 Mark McLoughlin <markmc@redhat.com> 2.8.1-1
- Update to 2.8.1
- Remove backported fixes

* Thu Oct  7 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0.1-1.1
- Don't hang with metacity's "reduced resources" mode (#134240) 
- Improve the key repeat rate situation a good deal (#134451)

* Wed Sep 29 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0.1-1
- Update to 2.8.0.1

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-1
- Update to 2.8.0
- Remove upstreamed work-without-gnutls patch

* Tue Sep  7 2004 Matthias Clasen <mclasen@redhat.com> 2.7.92-3
- Disable help button until there is help (#131632)
 
* Wed Sep  1 2004 Mark McLoughlin <markmc@redhat.com> 2.7.92-2
- Add patch to fix hang without GNU TLS (bug #131354)

* Mon Aug 30 2004 Mark McLoughlin <markmc@redhat.com> 2.7.92-1
- Update to 2.7.92

* Tue Aug 17 2004 Mark McLoughlin <markmc@redhat.com> 2.7.91-1
- Update to 2.7.91

* Mon Aug 16 2004 Mark McLoughlin <markmc@redhat.com> 2.7.90-2
- Define libgcrypt_version

* Thu Aug 12 2004 Mark McLoughlin <markmc@redhat.com> 2.7.90-1
- Update to 2.7.90

* Wed Aug  4 2004 Mark McLoughlin <markmc@redhat.com> 2.7.4-1
- Update to 2.7.4

* Tue Jul 13 2004 Mark McLoughlin <markmc@redhat.com> 2.7.3.1-1
- Initial build.
