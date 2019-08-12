%def_disable snapshot

%define ver_major 4.1
%define _name files
%define xdg_name org.pantheon.%_name
%define rdn_name io.elementary.%_name

Name: pantheon-files
Version: %ver_major.9
Release: alt1

Summary: The file manager of the Pantheon desktop
License: GPLv3
Group: File tools
Url: https://github.com/elementary/%_name

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
#VCS: https://github.com/elementary/files.git
Source: %_name-%version.tar
%endif

Provides: %rdn_name = %version-%release

#Depends: tumbler
#Recommends: contractor
#Suggests: tumbler-plugins-extra
Requires: polkit zeitgeist tumbler elementary-icon-theme

BuildRequires(pre): meson
BuildRequires: intltool libappstream-glib-devel
BuildRequires: vala-tools libsqlite3-devel libgtk+3-devel
BuildRequires: libgee0.8-devel libgranite-devel
BuildRequires: libgail3-devel libdbus-glib-devel libnotify-devel
BuildRequires: libxkbcommon-devel libgranite-vala
BuildRequires: libzeitgeist2.0-devel libplank-devel libplank-vala
BuildRequires: libpolkit-devel
BuildRequires: libcanberra-devel libcanberra-vala

%description
The simple, powerful, and sexy file manager from elementary.

%package devel
Summary: Development files for pantheon-files
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for pantheon-files.

%package vala
Summary: Vala language bindings for the pantheon-files
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for the pantheon-files.

%prep
%setup -n %_name-%version

%build
%meson -Dwith-unity=false
%meson_build

%install
%meson_install
%find_lang %rdn_name

%files -f %rdn_name.lang
%doc AUTHORS README*
%_bindir/*
%_libdir/*.so.*
%_libdir/gtk-3.0/modules/libpantheon-filechooser-module.so
%_libdir/%rdn_name/
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/dbus-1/services/%rdn_name.Filemanager1.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/polkit-1/actions/%rdn_name.policy
%_datadir/%rdn_name/
%dir %_pixmapsdir/%rdn_name
%_pixmapsdir/%rdn_name/*.png
%_datadir/metainfo/%rdn_name.appdata.xml

%files devel
%_includedir/%name-widgets.h
%_includedir/%name-core/
%_libdir/*.so
%_pkgconfigdir/%name-core.pc
%_pkgconfigdir/%name-widgets.pc

%if 0
%files vala
%_vapidir/%name-core.vapi
%_vapidir/%name-widgets.vapi
%endif

%changelog
* Fri Aug 09 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.9-alt1
- 4.1.9

* Sun May 12 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.8-alt1
- 4.1.8

* Thu Apr 25 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.7-alt1
- updated to 4.1.7-7-g732d80c3

* Wed Apr 03 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.6-alt1
- updated to 4.1.6-11-g7629b75d

* Fri Feb 15 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.5-alt1
- 4.1.5

* Fri Jan 25 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.3-alt1
- updated to 4.1.3-30-gedee9887

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.2-alt1
- updated to 4.1.2-4-g08e2084f

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt3
- updated to d5c2444 (no tags in git)
- built against libgranite.so.5

* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt2
- rebuilt against libgranite.so.4

* Sun Jun 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Tue Apr 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Sat Mar 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.1.1-alt1
- 0.3.1.1

* Sat Jan 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Sun Jan 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.0.5-alt1
- 0.3.0.5

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.0.3.1-alt1
- 0.3.0.3.1

* Thu Sep 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.0.2-alt1
- 0.3.0.2

* Wed Mar 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5.1-alt1
- 0.1.5.1

* Mon Nov 11 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5-alt2
- Make build more verbose

* Sat Oct 12 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5-alt1
- 0.1.4 -> 0.1.5

* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt2
- Fix pkgconfig file

* Mon Sep 09 2013 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt1
- 0.1.3 -> 0.1.4

* Sat Aug 24 2013 Igor Zubkov <icesik@altlinux.org> 0.1.3-alt1
- build for Sisyphus

