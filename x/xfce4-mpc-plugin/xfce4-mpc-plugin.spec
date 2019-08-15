Name: xfce4-mpc-plugin
Version: 0.5.2
Release: alt1

Summary: MPD Client Plugin
License: %bsdstyle
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExcludeArch: aarch64

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: libmpd-devel

Requires: xfce4-panel >= 4.8

%define _unpackaged_files_terminate_build 1

%description
This is a simple Musicpd (https://www.musicpd.org) client plugin for the
Xfce panel.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Tue Aug 13 2019 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Mon Dec 10 2018 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Updated to 0.5.1.

* Tue Sep 04 2018 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt2
- Don't build the package on aarch64.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Fix Xfce name (XFCE -> Xfce).
- Updated to 0.5.0.

* Fri Feb 17 2012 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Updated translations from upstream git.
- Initial build.
