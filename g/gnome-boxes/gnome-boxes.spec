# since 3.29.x depends on modules in %_libdir/%name
%set_verify_elf_method unresolved=relaxed

%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define ver_major 3.32
%define xdg_name org.gnome.Boxes
%def_disable ovirt
%def_disable installed_tests

Name: gnome-boxes
Version: %ver_major.2
Release: alt1

Summary: A simple GNOME 3 application to access remote or virtual systems
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
Group: Emulators
License: LGPLv3+
Url: https://wiki.gnome.org/Apps/Boxes

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define govirt_ver 0.3.4
%define glib_ver 2.50.0
%define gtk_ver 3.22.20
%define gtk_vnc_ver 0.4.4
%define libvirt_glib_ver 2.0.0
%define libxml2_ver 2.7.8
%define libusb_ver 1.0.9
%define spice_gtk_ver 0.32
%define gudev_ver 165
%define osinfo_ver 0.2.12
%define tracker_ver 0.13.1
%define uuid_ver 1.41.3
%define libsoup_ver 2.38
%define libarchive_ver 3.0.0

Requires: gnome-keyring

BuildRequires(pre): meson
BuildRequires: yelp-tools
BuildRequires: gobject-introspection-devel >= 0.9.6
BuildRequires: libvala-devel >= 0.28.0.16
BuildRequires: vala-tools
BuildRequires: glib2-devel >= %glib_ver libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver libgtk+3-gir-devel
BuildRequires: libgtk3vnc-devel >= %gtk_vnc_ver
BuildRequires: libsecret-devel libsecret-gir-devel
BuildRequires: libvirt-gobject-devel >= %libvirt_glib_ver
BuildRequires: libvirt-gconfig-devel >= %libvirt_glib_ver
BuildRequires: libxml2-devel >= %libxml2_ver
BuildRequires: libusb-devel >= %libusb_ver
BuildRequires: libspice-gtk3-devel >= %spice_gtk_ver
BuildRequires: libgudev-devel >= %gudev_ver
BuildRequires: libosinfo-devel >= %osinfo_ver
BuildRequires: tracker-devel >= %tracker_ver
BuildRequires: libuuid-devel >= %uuid_ver
BuildRequires: libsoup-devel >= %libsoup_ver
BuildRequires: libarchive-devel >= %libarchive_ver
%{?_enable_ovirt:BuildRequires: pkgconfig(govirt-1.0) >= %govirt_ver}
BuildRequires: libwebkit2gtk-devel
BuildRequires: libfreerdp-devel
BuildRequires: libvte3-devel

# Need libvirtd and an hypervisor to do anything useful
Requires: libvirt-daemon
Requires: qemu-kvm

# Needed for unattended installations
Requires: fuseiso
Requires: mtools

# gnome-boxes uses a dark theme
Requires: gnome-icon-theme

%description
gnome-boxes lets you easily create, setup, access, and use:
  * remote machines
  * remote virtual machines
  * local virtual machines
  * When technology permits, set up access for applications on
    local virtual machines

%package tests
Summary: Tests for the Boxes
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the Boxes.


%prep
%setup

%build
%meson \
	%{?_disable_ovirt:-Dovirt=false} \
	%{?_enable_installed_tests:-Dinstalled_tests=true}
%meson_build

%install
%meson_install
%find_lang %name --with-gnome

%files -f %name.lang
%doc AUTHORS README* NEWS TODO
%_bindir/%name
%_libdir/%name/
%_datadir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*
%_libexecdir/gnome-boxes-search-provider
%_datadir/dbus-1/services/*.service
%_datadir/gnome-shell/search-providers/gnome-boxes-search-provider.ini
%_datadir/metainfo/*.xml

%if_enabled installed_tests
%files tests
%_libexecdir/%name/installed-tests/
%_datadir/installed-tests/%name/
%endif

%exclude %_includedir/%name/

%changelog
* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Thu May 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Fri Mar 29 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0.2-alt1
- 3.32.0.2

* Mon Mar 18 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0.1-alt1
- 3.32.0.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Thu Nov 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Wed Oct 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Thu Sep 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Fri Jun 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.5-alt1
- updated to v3.28.5-5-ge8b9d5c

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Sat Apr 07 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- updated to v3.28.0-10-ga1f74a0

* Sun Mar 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.92-alt1
- 3.27.92

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Sun Sep 17 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Mar 21 2017 Alexey Shabalin <shaba@altlinux.ru> 3.24.0-alt1
- 3.24.0

* Fri Mar 03 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.4-alt1
- 3.22.4

* Mon Dec 26 2016 Alexey Shabalin <shaba@altlinux.ru> 3.22.3-alt1
- 3.22.3

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.22.1-alt1
- 3.22.1

* Mon Jun 27 2016 Alexey Shabalin <shaba@altlinux.ru> 3.20.2-alt2
- rebuild with spice-gtk-0.32-alt1

* Tue May 10 2016 Alexey Shabalin <shaba@altlinux.ru> 3.20.2-alt1
- 3.20.2

* Mon Apr 25 2016 Alexey Shabalin <shaba@altlinux.ru> 3.20.1-alt1
- 3.20.1

* Fri Apr 01 2016 Alexey Shabalin <shaba@altlinux.ru> 3.20.0-alt1
- 3.20.0

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 3.18.1-alt1
- 3.18.1

* Wed Apr 15 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.1-alt1
- 3.16.1

* Mon Mar 30 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.0-alt1
- 3.16.0

* Wed Nov 12 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.2-alt1
- 3.14.2

* Tue Sep 30 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.2-alt1
- 3.12.2

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.0-alt1
- 3.12.0

* Mon Feb 24 2014 Alexey Shabalin <shaba@altlinux.ru> 3.11.90.1-alt1.git.58bb18
- upstream snapshot 58bb18a328c2f3db3c3b656edcc8bd93630a2084

* Wed Oct 30 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1
- 3.10.0
- disable govirt support

* Thu Sep 19 2013 Alexey Shabalin <shaba@altlinux.ru> 3.9.92-alt1
- 3.9.92

* Tue Sep 03 2013 Alexey Shabalin <shaba@altlinux.ru> 3.9.91-alt1
- 3.9.91

* Tue Jul 30 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.4-alt1
- 3.8.4

* Tue May 14 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.2-alt1
- 3.8.2

* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.1.2-alt2
- update to upstream/gnome-3-8 branch
- build with oVirt support

* Fri Apr 19 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.1.2-alt1
- 3.8.1.2

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Fri Mar 22 2013 Alexey Shabalin <shaba@altlinux.ru> 3.7.92-alt1
- 3.7.92

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 3.7.90-alt1
- 3.7.90

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 3.6.3-alt1
- 3.6.3

* Tue Nov 13 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.2-alt1
- 3.6.2

* Mon Oct 15 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Tue Sep 11 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.3-alt1.1
- rebuild with new libspice-client-glib-2.0.so.1, libspice-client-gtk-3.0.so.1

* Thu Jun 14 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.3-alt1
- 3.4.3

* Wed May 16 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.2-alt1
- 3.4.2

* Tue Apr 24 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Wed Apr 04 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.0.1-alt1
- Initial build.

