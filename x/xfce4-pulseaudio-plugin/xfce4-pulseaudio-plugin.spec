Name: xfce4-pulseaudio-plugin
Version: 0.4.2
Release: alt1

Summary: A pulseaudio plugin for the Xfce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

# git://git.xfce.org/panel-plugins/xfce4-pulseaudio-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%def_disable wnck

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: libxfconf-devel
BuildRequires: libpulseaudio-devel libnotify-devel
BuildRequires: libkeybinder3-devel libdbus-glib-devel
%{?_enable_wnck:BuildRequires: libwnck3-devel}

Requires: xfce4-panel >= 4.11

%define _unpackaged_files_terminate_build 1

%description
A panel plugin for controlling PulseAudio mixer.

%prep
%setup
%patch -p1
# Don't use git tag in version.
%xfce4_drop_gitvtag pulseaudio_version_tag configure.ac.in

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-keybinder \
	%{subst_enable wnck} \
	--disable-silent-rules \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/*/*.*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- Updated to 0.4.2.

* Thu Aug 16 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt2
- Update url.
- Use dbus-glib CFLAGS.
- Add libdbus-glib-devel to BR.
- Rebuild with libxfconf-0.so.3.
- Fix debug level.

* Thu Apr 12 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Updated to 0.4.1.

* Tue Mar 20 2018 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Tue Feb 27 2018 Mikhail Efremov <sem@altlinux.org> 0.3.5-alt1
- Add knob for libwnck3 support.
- Updated to 0.3.5.

* Mon Nov 27 2017 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Mon Oct 30 2017 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.
- Disable silent rules.

* Fri Sep 29 2017 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Wed Sep 06 2017 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Mon Apr 24 2017 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Thu Apr 06 2017 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt3
- Enable keybinder support.

* Wed Mar 15 2017 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt2
- Fix menu translation.
- Use _unpackaged_files_terminate_build.
- Added translations from upstream git.

* Tue Oct 27 2015 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Thu May 14 2015 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Add libnotify-devel to BR.
- Updated to 0.2.3.

* Fri Mar 27 2015 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Thu Mar 19 2015 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Patches from upstream git:
  + Remove grab-broken.
  + Disconnect events and cleanup.
  + Removed grab_notify to avoid crashes.
- Initial build (closes: #30822).

