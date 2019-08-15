%define base thunar-volman
Name: %base-plugin
Version: 0.9.5
Release: alt1

Summary: Thunar volume manager plugin
Summary (ru): Дополнение Thunar для управления подключенными устройствами
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/thunar-plugins/thunar-volman
Packager: XFCE Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/thunar-volman
Source: %base-%version.tar
Patch: %base-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfconf-devel libexo-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: libgtk+3-devel intltool libgudev-devel libnotify-devel

Requires: gvfs

%define _unpackaged_files_terminate_build 1

%description
thunar-volman is an extension for the Thunar File Manager, which enables
automatic management of removable drives and media. For example, if
thunar-volman is installed and configured properly, and you plug in your
digitcal camera, it will automatically spawn your preferred photo
application and import the new pictures from your camera.

It was designed to look and behave similar to gnome-volume-manager to
get consistent removable drive and media management in Xfce and GNOME.
This is to help GNOME refugees and people using both Xfce and GNOME
(i.e. having to use GNOME at the office).

%description -l ru
Данный пакет содержит в себе дополнение для файлового менеджера Thunar
позволяющее управлять подключенными к системе съемными устройствами.
Например, если данное дополнение установлено и настроено и вы подключите
цифровую камеру, автоматически запустится указанное вами приложение для
получения фотографий с камеры и работы с ними.

Данное дополнение специально разработано похожим на
gnome-volume-manager - менеджер управления томами для GNOME. Это
позволит людям использовавшим ранее GNOME легко ориентироваться в нем.

%prep
%setup -n %base-%version
%patch -p1

%build
%xfce4reconf
%configure \
    --enable-notifications \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %base

%files -f %base.lang
%doc README AUTHORS
%_bindir/*
%_iconsdir/hicolor/*/*/*
%_desktopdir/*.desktop

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 0.9.5-alt1
- Updated to 0.9.5.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1
- Updated to 0.9.4.

* Sun Jun 30 2019 Mikhail Efremov <sem@altlinux.org> 0.9.3-alt1
- Updated to 0.9.3.

* Tue May 21 2019 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Updated to 0.9.2.

* Tue Nov 27 2018 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1
- Updated to 0.9.1.

* Thu Aug 09 2018 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- Enable debug (minimum level).
- Update url.
- Use _unpackaged_files_terminate_build.
- Updated to 0.9.0.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
= Drop obsoleted patch.
- Updated to 0.8.1.

* Tue May 21 2013 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt2
- Use xfce_dialog_show_help ().

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Updated to 0.7.1.

* Mon Apr 09 2012 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Wed Nov 30 2011 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt4
- Run xfce4-fixkeyboard script when USB keyboard is plugged.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt3
- Add gvfs to requires (closes: #26190).

* Mon Jul 18 2011 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt2
- Fix ThunarHelp path.

* Wed Jan 26 2011 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Spec cleanup, tar.bz2 -> tar.
- Updated to 0.6.0.

* Tue May 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.3.80+svn7321-alt1
- Added russian translation

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.80-alt1
- new version

* Tue Jan 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.1.2-alt1
- First build

