Name: xfce4-stopwatch-plugin
Version: 0.3.1
Release: alt1

Summary: Stopwatch plugin for the Xfce panel
License: %bsd
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: vala libxfce4panel-gtk3-vala libxfce4util-vala

Requires: xfce4-panel >= 4.8

%define _unpackaged_files_terminate_build 1

%description
The xfce-stopwatch-plugin is a panel plugin to keep track of elapsed time.
There are no ways to configure the plugin at this time, just add it to the
panel. The time elapsed will be saved when your panel quits and restored next
time it's running. If time was ticking, it will not start ticking again
automatically.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*
%exclude %_libdir/xfce4/panel/plugins/*.la
%_iconsdir/hicolor/*/apps/*.*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Fri Jun 14 2019 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Initial build.
