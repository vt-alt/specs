Name:           xfce4-notifyd
Version:        0.6.1
Release:        alt1
Summary:        Simple notification daemon for Xfce
Summary(ru_RU.UTF-8): Менеджер уведомлений для Xfce

Group:          Graphical desktop/XFce
License:        GPL-2.0-only
URL:            https://docs.xfce.org/apps/notifyd/start
Vcs:            https://gitlab.xfce.org/apps/xfce4-notifyd.git
Source0:        %name-%version.tar
Patch:          %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4ui-gtk3-devel libxfconf-devel libxfce4util-devel
BuildRequires: libxfce4panel-gtk3-devel
BuildRequires: libgio-devel libICE-devel libX11-devel libSM-devel
BuildRequires: desktop-file-utils libnotify-devel

# Automatically added by buildreq on Mon Sep 21 2009
BuildRequires: intltool libglade-devel

Requires:       xfce4-common
Requires:       dbus icon-theme-hicolor
Requires:       notify-send
Obsoletes:      notification-daemon-xfce <= 0.3.7

Provides: desktop-notification-daemon

%define _unpackaged_files_terminate_build 1

%description
Xfce4-notifyd is a simple, visually-appealing notification daemon for
Xfce that implements the freedesktop.org desktop notifications
specification.
Features:
* Themable using the GTK+ theming mechanism
* Visually appealing: rounded corners, shaped windows
* Supports transparency and fade effects

%description -l ru_RU.UTF-8
Простой менеджер уведомлений для Xfce работающий по спецификациям
freedesktop.org.
Возможности:
* Наличие встроенного механизма тем
* Поддержка скруглений для углов окон
* Поддержка прозрачности и эффекта скрытия

%package -n xfce4-notification-plugin
Summary: Notification plugin for the Xfce panel
Group: Graphical desktop/XFce
Requires: %name

%description -n xfce4-notification-plugin
Notification plugin for the Xfce panel.

%prep
%setup
%patch -p1
# Don't use git tag in version.
%xfce4_drop_gitvtag %{name}_version_tag configure.ac.in

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-dbus-start-daemon \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README TODO
%_bindir/xfce4-notifyd-config
%_libdir/xfce4/notifyd/
%_desktopdir/*.desktop
%_datadir/dbus-1/services/*
%_usr/lib/systemd/user/xfce4-notifyd.service
%_iconsdir/hicolor/*/*/*.*
%_datadir/themes/Default/xfce-notify-4.0/
%_datadir/themes/Bright/
%_datadir/themes/Retro/
%_datadir/themes/Smoke/
%_datadir/themes/ZOMG-PONIES!/
%_man1dir/*

%files -n xfce4-notification-plugin
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/panel/plugins/*.desktop

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Wed May 06 2020 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1
- Dropped exo-csource from BR.
- Updated Vcs tag.
- Updated to 0.6.1.

* Wed Apr 08 2020 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Added Vcs tag.
- Don't use rpm-build-licenses.
- Updated to 0.6.0.

* Tue Apr 30 2019 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1
- Updated to 0.4.4.

* Mon Oct 29 2018 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1
- Updated to 0.4.3.

* Thu Oct 25 2018 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt2
- Fix systemd userdir location (closes: #35520).

* Thu Aug 16 2018 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- Package panel plugin as separate subpackage.
- Fix systemd userdir.
- Don't require dbus-binding-tool.
- Enable debug (minimum level).
- Fix url.
- Use _unpackaged_files_terminate_build.
- Updated BR.
- Updated to 0.4.2.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt2
- Rebuild with libxfce4util-4.12.
- Fix Xfce name (XFCE -> Xfce).
- Provide desktop-notification-daemon.

* Wed May 08 2013 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Add xfce4-common requires.
- Updated to 0.2.4.

* Wed May 08 2013 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Fix tests build with --as-needed.
- Updated from upstream git:
  + Translations.
  + Fix border drawing when compositing is disabled.
- Updated to 0.2.3.

* Tue May 22 2012 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt3.git20120521
- Updated translations from upstream git.
- Fix BR.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt2.git20120413
- Upstream git snapshot.

* Tue Aug 16 2011 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Drop obsoleted patches.
- Updated to 0.2.2.

* Wed Jun 22 2011 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt3
- Add notify-send requires.
- Update Russian translation (by Artem Zolochevskiy).

* Thu Mar 24 2011 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt2
- Add libxfce4util-devel to BR.
- Renew dbus-service-name.patch.

* Thu Feb 10 2011 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Own %%{_libdir}/xfce4/notifyd/
- Updated to 0.2.1.

* Wed Jan 26 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Spec cleanup, tar.bz2 -> tar.
- Update dbus-service-name.patch from FC.
- Drop xfce4-notifyd-0.1.0-send-second-arg-notification-closed.patch
    (fixed in upstream).
- Updated to 0.2.0.

* Wed Nov 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.1.0-alt2
- First build for Sisyphus.


