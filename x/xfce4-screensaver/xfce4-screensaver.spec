Name: xfce4-screensaver
Version: 0.1.11
Release: alt1

Summary: Screen saver and locker for Xfce
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/XFce
Url: https://git.xfce.org/apps/xfce4-screensaver/about/

Vcs: https://gitlab.xfce.org/apps/xfce4-screensaver.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-xdg

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfconf-devel libgarcon-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: glib2-devel libgtk+3-devel libgio-devel
BuildRequires: libdbus-glib-devel libdbus-devel
BuildRequires: libXScrnSaver-devel libxklavier-devel libXrandr-devel libGL-devel
BuildRequires: libsystemd-devel libpam0-devel libwnck3-devel
BuildRequires: xmlto

Requires: xfce4-common

%define _unpackaged_files_terminate_build 1

%description
%name is a screen saver and locker that aims to have simple, sane,
secure defaults and be well integrated with the desktop.

This project is a port of MATE Screensaver, itself a port of GNOME Screensaver.
It has been tightly integrated with the Xfce desktop, utilizing Xfce libraries
and the Xfconf configuration backend.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--disable-static \
	--disable-silent-rules \
	--enable-maintainer-mode \
	--with-mit-ext \
	--enable-pam \
	--with-pam-auth-type=system \
	--with-systemd \
	--enable-locking \
	--enable-docbook-docs \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README.md
%attr(640,root,chkpwd) %config(noreplace) %_sysconfdir/pam.d/%name
%_xdgconfigdir/autostart/%name.desktop
%_xdgmenusdir/*.menu
%_bindir/%{name}*
%_libexecdir/%{name}*
%attr(2711,root,chkpwd) %_libexecdir/%name-dialog
%_desktopdir/screensavers/*.desktop
%_desktopdir/*.desktop
%_datadir/dbus-1/services/*.service
%_datadir/desktop-directories/*.directory
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_pixmapsdir/*.svg

%changelog
* Mon Nov 09 2020 Mikhail Efremov <sem@altlinux.org> 0.1.11-alt1
- Update Vcs tag.
- Drop exo-csource from BR.
- 0.1.10 -> 0.1.11.

* Mon Mar 30 2020 Mikhail Efremov <sem@altlinux.org> 0.1.10-alt1
- 0.1.9 -> 0.1.10.

* Mon Mar 23 2020 Mikhail Efremov <sem@altlinux.org> 0.1.9-alt1
- Use Vcs tag.
- Don't use rpm-build-licenses.
- 0.1.8 -> 0.1.9.

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 0.1.8-alt1
- 0.1.7 -> 0.1.8.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 0.1.7-alt1
- 0.1.6 -> 0.1.7.

* Sun Jun 30 2019 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1
- 0.1.5 -> 0.1.6.

* Thu Jun 13 2019 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- 0.1.4 -> 0.1.5.

* Fri Mar 22 2019 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1
- 0.1.3 -> 0.1.4.

* Wed Jan 30 2019 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- Add pam_deny.so to PAM stack.
- It's OK if pam_gnome_keyring.so is absent.
- Install dialog as sgid program.
- Workaround for sgid GTK dialog.
- 0.1.2 -> 0.1.3.

* Mon Nov 19 2018 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- 0.1.0 -> 0.1.2.

* Mon Oct 15 2018 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.
