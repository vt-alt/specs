Name: xfdashboard
Version: 0.8.0
Release: alt1

Summary: A Gnome shell like dashboard for Xfce
License: GPL-2.0+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/apps/xfdashboard/start

Vcs: https://gitlab.xfce.org/apps/xfdashboard.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-xdg

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfconf-devel libgarcon-devel libxfce4util-devel libxfce4ui-gtk3-devel
BuildRequires: libgtk+3-devel libwnck3-devel libclutter-devel libdbus-glib-devel
BuildRequires: libXinerama-devel

%define _unpackaged_files_terminate_build 1

%description
xfdashboard provides a GNOME shell dashboard like interface for use with
Xfce desktop. It can be configured to run to any keyboard shortcut and
when executed provides an overview of applications currently open
enabling the user to switch between different applications. The search
feature works like Xfce's app finder which makes it convenient to search
for and start applications.

%package -n lib%name
Summary: Shared libraries for %name
Group: Graphical desktop/XFce

%description -n lib%name
This package contains libraries for %name.

%package -n lib%name-devel
Summary: Devel files for %name
Group: Graphical desktop/XFce
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains development files required to build
%name-based software.

%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfdashboard_version_tag configure.ac.in
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--disable-silent-rules \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%{name}*
%_libdir/%name/
%exclude %_libdir/%name/plugins/*.la
%_xdgconfigdir/autostart/*.desktop
%_datadir/appdata/*.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.*
%_datadir/themes/%{name}*/
%_datadir/%name/

# Don't package example-search-provider plugin:
# it is just a skeleton for creating new search provider plugins.
%exclude %_libdir/%name/plugins/example-search-provider.so

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_pkgconfigdir/*.pc
%_includedir/%name/
%_libdir/*.so

%changelog
* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Tue Nov 17 2020 Mikhail Efremov <sem@altlinux.org> 0.7.90-alt1
- Updated to 0.7.90.

* Wed Sep 23 2020 Mikhail Efremov <sem@altlinux.org> 0.7.8-alt1
- Don't package example-search-provider plugin.
- Don't package plugins *.la files.
- Added Vcs tag.
- Updated Url tag.
- Updated to 0.7.8.

* Tue Dec 03 2019 Mikhail Efremov <sem@altlinux.org> 0.7.7-alt1
- Don't use rpm-build-licenses
- Updated to 0.7.7.

* Mon Aug 20 2018 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt1
- Updated to 0.7.5.

* Tue Aug 14 2018 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt1
- Add libXinerama-devel to BR.
- Package plugins.
- Package libxfdashboard.
- Disable silent rules.
- Enable debug (minimum level).
- Update url.
- Use _unpackaged_files_terminate_build.
- Updated to 0.7.4.

* Fri Jun 19 2015 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- Updated to 0.4.2.

* Mon Mar 30 2015 Mikhail Efremov <sem@altlinux.org> 0.3.91-alt1
- Updated url.
- Updated to 0.3.91.

* Fri Mar 20 2015 Mikhail Efremov <sem@altlinux.org> 0.3.90-alt1
- Updated to 0.3.90.

* Mon Mar 16 2015 Mikhail Efremov <sem@altlinux.org> 0.3.9-alt1
- Updated to 0.3.9.

* Mon Oct 20 2014 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Mon Sep 08 2014 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Wed Aug 27 2014 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Wed Jul 23 2014 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Tue Jul 01 2014 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Thu May 29 2014 Mikhail Efremov <sem@altlinux.org> 0.1.92-alt1
- Updated to 0.1.92.

* Mon May 26 2014 Mikhail Efremov <sem@altlinux.org> 0.1.91-alt1
- Updated to 0.1.91.

* Mon Mar 31 2014 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt2
- Rebuild with libcogl-1.18.0.

* Thu Mar 20 2014 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1
- Updated to 0.1.6.

* Wed Mar 12 2014 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- Updated url and description.
- Updated to 0.1.5.

* Tue Feb 25 2014 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1
- Updated to 0.1.4.

* Wed Feb 12 2014 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- Updated to 0.1.3.

* Mon Jan 27 2014 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.

* Mon Jan 13 2014 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Updated to 0.1.1.

* Thu Nov 28 2013 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20131125
- Initial build.

