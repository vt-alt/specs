Name: parole
Version: 1.0.4
Release: alt1

%def_enable clutter

Summary: Media player for the Xfce desktop
License: %gpl2plus
Group: Video

URL: https://goodies.xfce.org/projects/applications/parole
# git://git.xfce.org/apps/parole
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4ui-gtk3-devel libxfce4util-devel libxfconf-devel
BuildRequires: libgtk+3-devel libnotify-devel libtag-devel
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel
BuildRequires: libdbus-glib-devel libdbus-devel
%{?_enable_clutter:BuildRequires: libclutter-devel libclutter-gtk3-devel}
BuildRequires: intltool gtk-doc

Requires: gstreamer1.0
Requires: gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-bad1.0 gst-plugins-ugly1.0 gst-libav

%define _unpackaged_files_terminate_build 1

%description
Parole is a modern simple media player based on the GStreamer framework
and written to fit well in the Xfce desktop. Parole features playback of
local media files, DVD/CD and live streams. Parole is extensible via
plugins.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: libgtk+3-devel
BuildArch: noarch

%description devel
This package contains header files and documentation
for developing plugins for %name.

%prep
%setup
%patch -p1
mkdir m4

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-taglib \
	%{subst_enable clutter} \
	--enable-gtk-doc \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS README THANKS
%_bindir/%name
%_libdir/%name-*/
%exclude %_libdir/%name-*/*.la
%_desktopdir/*.desktop
%_datadir/metainfo/%name.appdata.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/%name/

%files devel
%_includedir/*
%doc %_datadir/gtk-doc/html/*

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1
- Updated to 1.0.4.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1
- Updated to 1.0.3.

* Thu Apr 04 2019 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Fri Aug 17 2018 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt2
- Update url.
- Fix debug level.
- Rebuild with libxfconf-0.so.3.

* Thu Apr 12 2018 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Updated to 1.0.1.

* Fri Mar 02 2018 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Updated to 1.0.0.

* Mon Jun 05 2017 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Drop gtreamer-0.10 build support.
- Updated to 0.9.2.

* Mon Feb 27 2017 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1
- Updated to 0.9.1.

* Mon Feb 13 2017 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- Enabled debug (minimal).
- devel: Fixed requires.
- Updated to 0.9.0.

* Mon Feb 08 2016 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2
- Add more GStreamer media plugins to requires (closes: #31681).

* Mon Oct 26 2015 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- Updated to 0.8.1.

* Fri Mar 13 2015 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Enable clutter support.
- Updated to 0.8.0.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt2
- Rebuild with libxfce4util-4.12.

* Thu Dec 05 2013 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 0.5.4.

* Wed Oct 16 2013 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt1
- Updated to 0.5.3.

* Thu Jul 25 2013 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Require gst-plugins-base and gst-plugins-good.
- Require gstreamer.
- Enable patch for no gstreamer codec-installer for ALT too.
- Updated to 0.5.2.

* Tue Jun 11 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.1-alt2
- Build with gstreamer0.10 on %%arm

* Tue Jun 04 2013 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Updated to 0.5.1.

* Fri Mar 08 2013 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- Build with gstreamer1.0.
- Updated to 0.5.0.

* Tue Jan 08 2013 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Mon May 21 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0.6-alt3
- Fix DSO linking.
- Updated translations from upstream git.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0.6-alt2
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).
- Updated translations from upstream git.

* Tue Jun 07 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0.6-alt1
- Updated to 0.2.0.6.

* Mon Feb 21 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0.2-alt2
- Package parole-devel as noarch.

* Sun Feb 20 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0.2-alt1
- Fix documentation bulding.
- Initial build (slightly based on FC spec).
