Name: xfce4-session
Version: 4.14.1
Release: alt1

Summary: Session manager for Xfce desktop environment
Summary (ru): Менеджер сессий для окружения рабочего стола Xfce
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://www.xfce.org/
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: git://git.xfce.org/xfce/xfce4-session
Source: %name-%version.tar
Source1: xfce.wmsession

Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfconf-devel libxfce4ui-gtk3-devel
# gdk-pixbuf-csource needed in maintainer mode
BuildRequires: libgdk-pixbuf-devel
BuildRequires: exo-csource
BuildRequires: libpolkit-devel
BuildRequires: libdbus-glib-devel
BuildRequires: iceauth intltool libSM-devel libglade-devel libwnck3-devel xorg-cf-files

Requires: wm-common-freedesktop
Requires: xfce4-about

Obsoletes: xfce-utils < %version
Obsoletes: libxfsm < %version-%release

%define _unpackaged_files_terminate_build 1

%description
%name is the session manager for the Xfce desktop environment.

%description -l ru
Данный пакет содержит в себе менеджер сессий, используемый в окружении
рабочего стола Xfce.

%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfsm_version_tag configure.ac.in
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--with-backend=linux \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
install -Dm0644 %SOURCE1 %buildroot%_x11sysconfdir/wmsession.d/10Xfce4
%find_lang %name

%files -f %name.lang
%doc README NEWS AUTHORS
%doc doc/FAQ doc/README.Kiosk
%_x11sysconfdir/wmsession.d/*
%config(noreplace) %_sysconfdir/xdg/xfce4/*
%config(noreplace) %_sysconfdir/xdg/autostart/*.desktop
%_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml
%_bindir/*
%dir %_libdir/xfce4/session
%_libdir/xfce4/session/xfsm-*
%_desktopdir/*
%_iconsdir/hicolor/*/*/*
%_mandir/man?/*
%_datadir/xsessions/*.desktop
%_datadir/polkit-1/actions/*.policy

%changelog
* Mon Jan 13 2020 Mikhail Efremov <sem@altlinux.org> 4.14.1-alt1
- Use Vcs rpm tag.
- Don't use rpm-build-licenses.
- Updated to 4.14.1.

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt1
- Avoid dependency on systemd-utils.
- Updated to 4.14.0.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 4.13.4-alt1
- Drop libxfsm subpackage.
- Updated to 4.13.4.

* Mon Jul 01 2019 Mikhail Efremov <sem@altlinux.org> 4.13.3-alt1
- Updated to 4.13.3.

* Tue May 21 2019 Mikhail Efremov <sem@altlinux.org> 4.13.2-alt1
- Don't use deprecated PreReq.
- Drop devel subpackage.
- Drop engines subpackage.
- Drop gnome-authentication-agent autostart desktop-file
  (closes: #36604).
- Updated to 4.13.2.

* Wed Jan 30 2019 Mikhail Efremov <sem@altlinux.org> 4.13.1-alt2.git99294d961d5b3
- Upstream git snapshot (master branch).

* Mon Aug 06 2018 Mikhail Efremov <sem@altlinux.org> 4.13.1-alt1
- Updated url.
- Updated to 4.13.1.

* Thu Aug 02 2018 Mikhail Efremov <sem@altlinux.org> 4.13.0-alt1
- Require libxfce4ui-2 instead of libxfce4ui-1 in pc.in file.
- Add libdbus-glib-devel to BR.
- Use dbus-glib CFLAGS.
- Enable debug (minimum level).
- Updated to 4.13.0.

* Wed Nov 30 2016 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt4
- Use absolute path in the xsessions/xfce.desktop (closes: #32828).

* Mon May 23 2016 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt3
- Use Exec to start gnome authentication agent again.

* Tue Apr 12 2016 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt2
- xflock4: Add light-locker support.
- Use TryExec to start gnome authentication agent.
- Improve "Fix shutdown action in the fallback mode" patch.

* Mon Mar 16 2015 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt1
- Updated to 4.12.1.

* Fri Mar 13 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt2
- Fix shutdown action in the fallback mode.
- Require xfce4-about.
- Patch from upstream:
  + Drop check for sessions file before it's written.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Wed Feb 18 2015 Mikhail Efremov <sem@altlinux.org> 4.11.1-alt1
- Drop obsoleted patches.
- Updated to 4.11.1.

* Mon Feb 24 2014 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- xflock4: Add mate-screensaver support.
- Updated to 4.11.0.

* Wed Sep 25 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt8.git20130719
- Ensure that logind can shutdown/reboot/sleep method (closes: #29224).

* Tue Jul 23 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt7.git20130719
- Avoid automatic dependence on ConsoleKit.
- Improve gpg and ssh agents handling code.
- Update translations from upstream git.

* Wed Jun 26 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt6.git20130610
- Don't try to launch ssh-agent by default.
- Handle gpg and ssh agents separately (closes: #29108).
- Updated translations from upstream git.

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt5.git20130426
- Added gnome-authentication-agent autostart desktop-file (closes: #28920).

* Mon Apr 29 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt4.git20130426
- xinitrc: Migrate old Xkb settings to the new scheme.

* Sun Apr 28 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt3.git20130426
- Upstream git snapshot (closes: #28903).

* Thu Apr 18 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt3.git20130327
- Lock screen when sleep in case of systemd too.

* Wed Apr 10 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt2.git20130327
- Use sudo for suspend/hibernate as fallback.
- Add systemd-logind support for suspend/hibernate.
- Enable systemd-logind support (drop ConsoleKit).
- Upstream git snapshot.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 24 2012 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- Stop ssh-agent started from /etc/X11/profile.d/ssh-agent.sh.
- Fix gpg-agent shutdown.
- Replace mkdirhier with mkdir (closes: #27265).
- Updated from upstream git (e5f6df86fe):
    + Translations.
    + Skip gpg/ssh-agent if GNOME compat is enabled and gnome-keyring
      found.
    + Remove remaining code to shutdown gconf.
- Updated to 4.9.2.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Fri Apr 13 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Rewritten patch: Restore XKB settings after suspend/hibernate.
- Obsolete xfce-utils.
- Add xfce.wmsession from xfce-utils.
- Drop old patches.
- Updated to 4.9.0.

* Mon Feb 13 2012 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt1
- Updated to 4.8.3.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt5
- Rebuild with xfce4-panel-4.9.

* Tue Dec 20 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt4
- Updated Debian's force-xfsettingsd-start.patch.

* Thu Dec 01 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt3
- Restore XKB settings after suspend/hibernate.

* Thu Oct 13 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt2
- Added patches from Debian.
- Lock screen on suspend/hibernate in favor power manager's settings.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt1
- Drop obsoleted patches.
- Updated to 4.8.2.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt5
- Only perform hostname checks when TCP connections are enabled.
- Updated Russian documentation.
- Updated Russian translation.

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt4
- Updated Russian translation (by Artem Zolochevskiy).

* Wed Jul 20 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt3
- Fix documentation generation.

* Tue Jul 19 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt2
- Update Russian translation (by Artem Zolochevskiy).
- Patches from upstream:
    + Fix GDM_LANG usage to be compatible with GDM3.
    + Fix crash if save timeout for a client is triggered.

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Updated to 4.8.1.

* Mon Jan 24 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Spec cleanup, tar.bz2 -> tar.
- Fix shadows in 'simple' splash engine (patch from Ubuntu).
- Drop old Ubuntu's icons.
- Remove old patches.
- Fix license.
- Updated to 4.8.0.

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Mon Oct 15 2007 Igor Zubkov <icesik@altlinux.org> 4.4.1-alt1.1
- NMU
  + fix build with new intltool

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release
- add patches from Ubuntu 7.04
- add images from Ubuntu 7.04

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Wed Oct 25 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt2
- fix x86_64

* Wed Sep 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- new version 4.4rc1

* Tue Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

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
