%def_disable snapshot
# since 3.13.6
# see https://git.gnome.org/browse/evolution-data-server/commit/?id=a2790163af4d3f375a778055d0e2699207dfd050
%set_verify_elf_method unresolved=relaxed
%set_verify_elf_method rpath=relaxed

%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %_prefix/libexec

%define ver_major 3.32
%define ver_base 3.32
%define ver_lib 1.2

%def_disable debug
%def_disable static
%def_with libdb
%def_with openldap
%def_without static_ldap
%def_with krb5
%def_enable goa
%def_enable google
%def_enable canberra
# Ubuntu online accounts support
%def_disable uoa
%{?_enable_snapshot:%def_enable gtk_doc}
%def_disable gtk_doc
%def_enable introspection
%def_enable vala
%def_enable installed_tests

Name: evolution-data-server
Version: %ver_major.4
Release: alt1

Summary: Evolution Data Server
License: %lgpl2plus
Group: Graphical desktop/GNOME
URL: https://wiki.gnome.org/Apps/Evolution

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%endif
Patch1: %name-1.4.2.1-debug-lock.patch

%add_findprov_lib_path %_libdir/%name

%define glib_ver 2.40.0
%define gtk3_ver 3.10.0
%define libsoup_ver 2.42
%define gcr_ver 3.4
%define secret_ver 0.5
%define sqlite_ver 3.7.17
%define gweather_ver 3.10.0
%define ical_ver 0.43
%define gdata_ver 0.15.1
%define goa_ver 3.8.0
%define vala_ver 0.13.1
%define webkit_ver 2.13.0

Requires: dconf

BuildRequires(pre): cmake rpm-build-gnome rpm-build-licenses rpm-build-xdg rpm-build-gir
BuildRequires: gcc-c++ intltool
BuildRequires: gtk-doc >= 1.0
BuildRequires: gnome-common
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk3_ver
BuildRequires: libxml2-devel
BuildRequires: libsoup-devel >= %libsoup_ver
BuildRequires: libsqlite3-devel >= %sqlite_ver
BuildRequires: libgweather-devel >= %gweather_ver
BuildRequires: libical-devel >= %ical_ver
BuildRequires: libgdata-devel >= %gdata_ver
BuildRequires: libsecret-devel >= %secret_ver
BuildRequires: gcr-libs-devel >= %gcr_ver
BuildRequires: gperf docbook-utils flex bison libcom_err-devel libnss-devel libnspr-devel zlib-devel libicu-devel
%{?_enable_goa:BuildRequires: libgnome-online-accounts-devel >= %goa_ver liboauth-devel libgdata-devel >= %gdata_ver}
%{?_enable_google:BuildRequires: libwebkit2gtk-devel >= %webkit_ver libjson-glib-devel}
%{?_enable_uoa:BuildRequires: libaccounts-glib-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libsoup-gir-devel libgtk+3-gir-devel}
%{?_with_libdb:BuildRequires: libdb4-devel}
%{?_with_krb5:BuildRequires: libkrb5-devel}
%{?_enable_vala:BuildRequires: vala >= %vala_ver vala-tools >= %vala_ver}
%{?_enable_canberra:BuildRequires: libcanberra-gtk3-devel}

# /usr/libexec/evolution-data-server/csv2vcard uses perl(diagnostics.pm)
BuildRequires: perl-devel

%if_with openldap
BuildRequires: libldap-devel
%if_with static_ldap
BuildRequires: libldap-devel-static libssl-devel libsasl2-devel
%endif
%endif

%description
Evolution Data Server provides a central location for
addressbook and calendar in the GNOME Desktop.

%package devel
Summary: Development files for Evolution Data Server
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides development files for Evolution Data Server

%package devel-doc
Summary: Development documentation for Evolution Data Server
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
Evolution Data Server provides a central location for
addressbook and calendar in the GNOME Desktop.

This package contains development documentation for Evolution Data Server.

%package gir
Summary: GObject introspection data for the EDS
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Evolution Data Server libraries

%package gir-devel
Summary: GObject introspection devel data for the EDS
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Evolution Data Server libraries

%package vala
Summary: Vala language bindings for the EDS libraries
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description vala
This package provides Vala language bindings for the EDS libraries

%package tests
Summary: Tests for the EDS
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed EDS libraries.


%prep
%setup
%if_enabled debug
%patch1 -p1
%endif

%build
%add_optflags -D_FILE_OFFSET_BITS=64
# reenable RPATH* to link against private libraries
%cmake \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=ON \
	-DCAMEL_LOCK_HELPER_GROUP:STRING=mail \
	-DSENDMAIL_PATH:STRING=%_sbindir/sendmail \
	-DENABLE_FILE_LOCKING:STRING=fcntl \
	-DENABLE_DOT_LOCKING:BOOL=OFF \
	-DENABLE_SCHEMAS_COMPILE:BOOL=OFF \
	-DENABLE_SMIME:BOOL=ON \
	%{?_with_libdb:-DWITH_LIBDB:BOOL=ON} \
	%{?_with_openldap:-DWITH_OPENLDAP:BOOL=ON} \
	%{?_with_static_ldap:-DWITH_STATIC_LDAP:BOOL=ON} \
	%{?_with_krb5:-DWITH_KRB5:BOOL=ON} \
	%{?_enable_goa:-DENABLE_GOA:BOOL=ON} \
	%{?_disable_google:-DENABLE_GOOGLE_AUTH:BOOL=OFF} \
	%{?_disable_canberra:-DENABLE_CANBERRA:BOOL=OFF} \
	%{?_disable_uoa:-DENABLE_UOA:BOOL=OFF} \
	%{?_enable_introspection:-DENABLE_INTROSPECTION:BOOL=ON} \
	%{?_enable_gtk_doc:-DENABLE_GTK_DOC:BOOL=ON} \
	%{?_enable_vala:-DENABLE_VALA_BINDINGS:BOOL=ON} \
	%{?_enable_installed_tests:-DENABLE_INSTALLED_TESTS:BOOL=ON}
%cmake_build

%install
%cmakeinstall_std
# if unstable
ln -s camel-lock-helper-1.2 %buildroot%_libexecdir/camel-lock-helper

%find_lang --with-gnome --output=%name.lang %name %name-%ver_base

%files -f %name.lang
%_xdgconfigdir/autostart/org.gnome.Evolution-alarm-notify.desktop
%_desktopdir/org.gnome.Evolution-alarm-notify.desktop
%_libexecdir/*
%{?_enable_installed_tests:%exclude %_libexecdir/%name/installed-tests/}
%dir %_libdir/%name/addressbook-backends
%dir %_libdir/%name/calendar-backends
%dir %_libdir/%name/camel-providers
%_libdir/%name/*/*.so
%_libdir/%name/*/*.urls
%_libdir/*.so.*
%_libdir/%name/libedbus-private.so
%_datadir/%name/
%_datadir/dbus-1/services/*
%_prefix/lib/systemd/user/evolution-addressbook-factory.service
%_prefix/lib/systemd/user/evolution-calendar-factory.service
%_prefix/lib/systemd/user/evolution-source-registry.service
%_prefix/lib/systemd/user/evolution-user-prompter.service

%_datadir/pixmaps/*
%_datadir/GConf/gsettings/evolution-data-server.convert
%_datadir/glib-2.0/schemas/org.gnome.evolution-data-server.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.Evolution.DefaultSources.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution-data-server.addressbook.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution-data-server.calendar.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.eds-shell.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.shell.network-config.gschema.xml
%doc AUTHORS NEWS README MAINTAINERS

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled gtk_doc
%files devel-doc
%_gtk_docdir/*
%endif

%if_enabled introspection
%files gir
#%_typelibdir/ECalendar-%ver_lib.typelib
%_typelibdir/Camel-%ver_lib.typelib
%_typelibdir/EBookContacts-%ver_lib.typelib
%_typelibdir/EDataServer-%ver_lib.typelib
%_typelibdir/EDataServerUI-%ver_lib.typelib
%_typelibdir/EBook-%ver_lib.typelib

%files gir-devel
#%_girdir/ECalendar-%ver_lib.gir
%_girdir/Camel-%ver_lib.gir
%_girdir/EBookContacts-%ver_lib.gir
%_girdir/EDataServer-%ver_lib.gir
%_girdir/EDataServerUI-%ver_lib.gir
%_girdir/EBook-%ver_lib.gir
%endif

%if_enabled vala
%files vala
%_datadir/vala/vapi/*.deps
%_datadir/vala/vapi/*.vapi
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/%name/installed-tests/
%_datadir/installed-tests/%name/
%endif

%changelog
* Mon Jul 15 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.4-alt1
- 3.32.4

* Mon Jun 17 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.3-alt1
- 3.32.3

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Feb 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.5-alt1
- 3.30.5

* Mon Jan 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.4-alt1
- 3.30.4

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Jul 30 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.5-alt1
- 3.28.5

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.4-alt2
- rebuilt against libicu*.so.62

* Mon Jul 16 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.4-alt1
- 3.28.4

* Mon Jun 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Thu Apr 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt2
- updated to 3.28.1-3-ga96acb5 (fixed BGO ##791475, 795108)

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Mar 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.6-alt1
- 3.26.6

* Mon Feb 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.5-alt1
- 3.26.5

* Mon Jan 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.4-alt1
- 3.26.4

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt2
- rebuilt against libical.so.3/libicu*.so.60

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2.1-alt1
- 3.26.2.1

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Thu Sep 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.6-alt1
- 3.24.6

* Mon Aug 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.5-alt1
- 3.24.5

* Mon Jul 17 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.4-alt1
- 3.24.4

* Mon Jun 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.7-alt1
- 3.22.7

* Mon Mar 13 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.6-alt1
- 3.22.6

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt1
- 3.22.5

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt1
- 3.22.4

* Mon Dec 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Sep 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.92-alt1
- 3.21.92

* Mon Aug 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.91-alt1
- 3.21.91

* Tue Aug 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.90-alt1
- 3.21.90

* Mon Aug 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.5-alt1
- 3.20.5

* Mon Jul 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Mon Jun 06 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Wed Apr 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt0.1
- updated to 3.20.1-8-g0a20e2c (fixed BGO ##235681, 728496 RHBZ #1328330)

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Feb 15 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.5-alt1
- 3.18.5

* Mon Feb 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt3
- updated to 3.18.4-10-g144e6d7
- build against libicu*.so.56

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt2
- rebuilt against libical.so.2

* Mon Jan 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt1
- 3.18.4

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Aug 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.5-alt1
- 3.16.5

* Sun Aug 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt2
- rebuilt against libgdata.so.22

* Mon Jul 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt1
- 3.16.4 release

* Sun Jun 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt0.1
- 3.16.4 snapshot

* Mon Jun 08 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Feb 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.11-alt1
- 3.12.11

* Mon Jan 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.10-alt1
- 3.12.10

* Mon Dec 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.9-alt1
- 3.12.9

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.8-alt1
- 3.12.8

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.7-alt1
- 3.12.7 release

* Wed Oct 01 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.7-alt0.1
- updated to 3.12.7_e3b9159b

* Sat Sep 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.6-alt2
- rebuilt for GNOME-3.14

* Mon Sep 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.6-alt1
- 3.12.6

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.5-alt1
- 3.12.5

* Mon Jul 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.4-alt1
- 3.12.4 release

* Thu Jul 03 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.4-alt0.1
- 3.12.4_4581a32

* Mon Jun 09 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Sun Apr 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1 release

* Thu Apr 03 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt0.1
- 3.12.1 snapshot (8476b8abe)

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Sun Mar 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.92-alt1
- 3.11.92

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.4-alt1
- 3.10.4

* Mon Dec 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt3
- rebuilt against libical.so.1

* Tue Nov 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt2
- rebuilt with libical-1.0

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Sun Oct 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Sat Sep 21 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Jul 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Sun May 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Sun Apr 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1 release

* Tue Apr 02 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt0.1
- 3.8.1 snapshot (1738716)

* Sun Mar 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Mar 07 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.4-alt1
- 3.6.4

* Tue Jan 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Sun Nov 11 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Sun Oct 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Sat Sep 22 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.4-alt1
- 3.4.4

* Mon Jun 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Jan 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sun Sep 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Sep 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.92-alt1
- 3.1.92

* Sun Sep 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.90-alt1
- 3.1.90
- new vala subpackage

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2.1-alt1
- 3.0.2.1

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Sat Mar 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt2
- updated buildreqs
- fixed build with newer GTK

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Thu Aug 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2.1-alt1
- 2.30.2.1

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Sat Mar 20 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0
- removed upstreamed patches
- removed upstreamed patch and other hacks for build with --as-needed

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92
- updated as_needed patch
- updated buildreqs

* Tue Mar 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.3.1-alt1
- 2.28.3.1

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Sun Oct 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90
- updated patches

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3
- fixed krb5 detection

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Fri May 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1.1-alt2
- fixed build with new libtool_2.2

* Wed Apr 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1.1-alt1
- 2.26.1.1

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- drop upstreamed patches

* Wed Mar 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- updated buildreqs

* Mon Jan 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3
- fixed build from SVN (thanks shaba@)

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete *ldconfig from %%post{,un}

* Fri Nov 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1.1-alt1
- 2.24.1.1
- don't rebuild documentation

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0

* Mon Jun 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- 2.22.3

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Fri May 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1.1-alt1
- 2.22.1.1

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1
- changed libexec dir to %_prefix/libexec/%name

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22

* Mon Feb 04 2008 Alexey Shabalin <shaba@altlinux.ru> 1.12.3-alt1
- 1.12.3
- Removed patch for GNOME bug #363695 (causes issues)
- Add patch for RH bug #215702 / GNOME bug #487988 (fix ldap query)
- Run gtkdocize to avoid requiring gtk-doc 1.9

* Thu Nov 29 2007 Alexey Shabalin <shaba@altlinux.ru> 1.12.2-alt1
- 1.12.2

* Wed Nov 21 2007 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt2
- fix link with libedataserverui (evolution-data-server-1.11.3-as-needed.patch)
- remove set_verify_elf_method unresolved=relaxed

* Thu Oct 25 2007 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt1
- 1.12.1
- Disable patch for GNOME bug #376991 for now.  It may be contributing
  to password prompting problems as described in RH bug #296671.
- Remove patch for GNOME bug #420167 (fixed upstream)

* Fri Oct 12 2007 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt1
- 1.12.0
- Add support build with static ldap (default disable-> %%def_disable ldap_static)
- Add Requires: glib2 >= 2.14.0, since it's in the buildroot now, and
  forcibly introduces deps on symbols that don't exist in 2.13.  If
  only we had working symbol versioning.
- Add Requires: libbonobo >= 2.20.0, libgnome >= 2.20.0
- Add patch for GNOME bug #420167 (fix e-d-s leaks)
- Revise patches:
  + mandriva patch for fix empty error dialog in non utf8 locale
  + GNOME bug #417999 to fix GNOME bug #447591 
    (Automatic Contacts combo boxes don't work).
  + evolution-data-server-1.8.0-no-gnome-common.patch 
    so that we no longer have to run autoconf before building.
  + GNOME bug #363695 evolution-data-server-1.9.1-kill-ememory.patch
    (deprecate EMemPool, EStrv, EPoolv).
  + GNOME bug #376991.
- Remove patches:
  + RH bug #203058 (fixed upstream)
  + RH bug #210142 (fixed upstream)
  + GNOME bug #360240 (fixed upstream)
  + GNOME bug #360619 (fixed upstream)
  + GNOME bug #373117 (fixed upstream)
  + GNOME bug #415891 (fixed upstream)
  + GNOME bug #415922 (fixed upstream)
  + RH bug #215634 (fixed upstream)
  + GNOME bug #466987 (fixed upstream)

* Fri Aug 17 2007 Alexey Shabalin <shaba@altlinux.ru> 1.10.3.1-alt1
- Updated to 1.10.3.1
- change packager
- add/remove patches from fc7

* Sun Mar 25 2007 Ilya Mashkin <oddity@altlinux.ru> 1.8.3-alt2
- add some patches
- add URL

* Sat Feb 24 2007 Ilya Mashkin <oddity@altlinux.ru> 1.8.3-alt1
- Updated to 1.8.3

* Mon Jan 01 2007 Ilya Mashkin <oddity@altlinux.ru> 1.8.2-alt1
- New release 1.8.2

* Mon Oct 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.8.1-alt1
- Release 1.8.1

* Tue Sep 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.8.0-alt1
- Release 1.8.0
- Patch0 has gone upstream
- Enabled gnome-keyring
- Buildreq

* Fri Sep 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.3-alt1
- Release 1.6.3

* Thu Jun 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.2-alt1
- Release 1.6.2

* Sat Apr 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.1-alt1
- Release 1.6.1

* Wed Mar 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.0-alt1
- Release 1.6.0

* Thu Mar 09 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.92-alt2
- Patch0: Adopted the dynamic libdb patch from Ross Burton (GNOME bug 319393)
- Enabled sys_db4 by default after a discussion on evolution-hackers
- Patch2: proper use of variables affecting the krb5 library test
- Relaxed the unresolved symbol check (proper fix blocked by GNOME bug 334169)

* Sun Mar 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.92-alt1
- 1.5.92

* Thu Feb 16 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.91-alt1
- Updated to 1.5.91

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.2.1-alt2.1
- Rebuilt for new pkg-config dependencies.

* Sat Jan 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2.1-alt2
- Explicit dependency on libnss and libnspr

* Wed Dec 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2.1-alt1
- 1.4.2.1

* Wed Nov 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt2
- Disable system libdb patch by default in hope to stop
  index corruption
- Compile with separately installed libnspr and libnss

* Tue Nov 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt1
- 1.4.2
- Run intltoolize

* Sat Nov 19 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1.1-alt2.1
- Spec cosmetics
- Drop explicit nspr/nss configure flags, relying on mozilla .pc files instead

* Sat Oct 22 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1.1-alt2
- Version required for libsoup bumped to 2.2.6

* Wed Oct 19 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1.1-alt1
- 1.4.1.1

* Tue Oct 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt1
- 1.4.1
- Patch1 is obsolete
- Specify mozilla library directories

* Tue Sep 06 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.0-alt1
- 1.4.0
- Updated Patch1

* Sun Sep 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.8-alt2
- --with-e2k-debug for the debug build
- --enable-nntp
- Correct name for lock helper (GNOME bug #305633) [Patch1]

* Fri Aug 26 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.8-alt1
- 1.3.8
- Updated Patch0

* Mon Aug 08 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.7-alt0.1
- 1.3.7

* Thu Aug 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.6.1-alt0.1
- 1.3.6.1

* Fri Jul 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.6-alt0.1
- 1.3.6

* Fri Jul 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.5-alt0.1
- 1.3.5
- Updated Patch0

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Tue Apr 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Thu Mar 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Fri Feb 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Sat Dec 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3
- development documentation moved to devel-doc subpackage.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Sep 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sun Sep 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.99-alt1
- 0.0.99

* Wed Aug 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.97-alt1
- 0.0.97

* Tue Jul 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.96-alt1
- 0.0.96

* Tue Jul 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.95-alt1
- 0.0.95

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.94.1-alt1
- 0.0.94.1

* Sat Jun 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.94-alt1
- 0.0.94

* Fri May 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.93-alt1
- 0.0.93

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.92-alt1
- 0.0.92

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.91-alt2
- rebuild against new gnutls (1.0.10)

* Tue Apr 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.91-alt1
- 0.0.91

* Sat Mar 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.90-alt1
- 0.0.90

* Thu Feb 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.7-alt2
- rebuild against libdb4.2

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.7-alt1
- 0.0.7

* Tue Jan 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.6-alt1
- First build for Sisyphus.
