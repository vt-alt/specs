%def_disable snapshot
%set_verify_elf_method unresolved=relaxed
# Some plugins/extensions link with others, resulting in multiple rpath entries
%set_verify_elf_method rpath=relaxed

%define xdg_name org.gnome.Evolution
%define _libexecdir %_prefix/libexec
%define ver_major 3.32
%define ver_base 3.32
%define gst_api_ver 1.0

%def_disable gtk_doc
%def_with openldap
%def_disable static_ldap
%def_enable map
%def_enable autoar
%def_enable ytnef
%def_enable installed_tests

# %define plugins experimental
%define plugins all

Name: evolution
Version: %ver_major.3
Release: alt1

Summary: Integrated GNOME mail client, calendar and address book
License: GPLv2+
Group: Office
Url: https://wiki.gnome.org/Apps/Evolution

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%endif

%define evo_plugin_dir %_libdir/evolution/plugins
%define evo_module_dir %_libdir/evolution/modules
%add_findprov_lib_path %_libdir/%name/%ver_base

Provides: camel

# from configure.ac
%define glib_ver 2.40.0
%define gtk_ver 3.10
%define clutter_gtk_ver 0.91.8
%define eds_ver 3.32.3
%define gnome_icon_ver 3.0.0
%define gnome_desktop_ver 2.91.6
%define libsoup_ver 2.42.0
%define libnotify_ver 0.7.0
%define gweather_ver 3.5.0
%define ical_ver 1.0.1
%define gdata_ver 0.10.0
%define champlain_ver 0.12
%define pst_ver 0.6.54
%define webkit_ver 2.13.90
%define geocode_ver 3.10.0
%define gcr_ver 3.4
%define autoar_ver 0.1.1

Requires: %name-data = %version-%release
Requires: evolution-data-server >= %eds_ver
Requires: gnome-icon-theme
Requires: gnome-settings-daemon
Requires: highlight

BuildRequires: cmake gcc-c++ flex  gnome-common
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgail3-devel >= %gtk_ver
BuildRequires: gnome-icon-theme >= %gnome_icon_ver
BuildRequires: evolution-data-server-devel >= %eds_ver
BuildRequires: libgnome-desktop3-devel >= %gnome_desktop_ver
BuildRequires: libsoup-gnome-devel >= %libsoup_ver
BuildRequires: libnotify-devel >= %libnotify_ver
BuildRequires: libgweather-devel >= %gweather_ver
BuildRequires: libical-devel >= %ical_ver libicu-devel
BuildRequires: libgdata-devel >= %gdata_ver
BuildRequires: libpst-devel >= %pst_ver
BuildRequires: libwebkit2gtk-devel >= %webkit_ver
BuildRequires: libclutter-gtk3-devel >= %clutter_gtk_ver
BuildRequires: gcr-libs-devel >= %gcr_ver libcryptui-devel
BuildRequires: libkrb5-devel
%{?_enable_map:BuildRequires: libchamplain-gtk3-devel >= %champlain_ver libgeocode-glib-devel >= %geocode_ver}
%{?_enable_ytnef:BuildRequires: libytnef-devel}
%{?_enable_autoar:BuildRequires: libgnome-autoar-devel >= %autoar_ver}
%{?_with_openldap:BuildRequires: libldap-devel %{?_enable_static_ldap:libldap-devel-static libssl-devel libsasl2-devel}}

BuildRequires: docbook-utils intltool yelp-tools itstool gtk-doc
BuildRequires: libSM-devel libcom_err-devel gstreamer%gst_api_ver-devel
BuildRequires: python-modules-compiler python-modules-encodings libnspr-devel libnss-devel libX11-devel libcanberra-gtk3-devel
BuildRequires: zlib-devel libxml2-devel libgtkspell3-devel

%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool.

%package data
Summary: Evolution data files
Group: Office
BuildArch: noarch

%description data
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool.

This package contains common noarch files needed for  Evolution.

%package bogofilter
Group: Networking/Mail
Summary: Bogofilter plugin for Evolution
Requires: %name = %version-%release
Requires: bogofilter

%description bogofilter
This package contains the plugin to filter junk mail using Bogofilter.

%package spamassassin
Group: Networking/Mail
Summary: SpamAssassin plugin for Evolution
Requires: %name = %version-%release
Requires: spamassassin

%description spamassassin
This package contains the plugin to filter junk mail using SpamAssassin.

%package devel
Summary: Evolution development files
Group: Development/C
Requires: %name = %version-%release
Requires: evolution-data-server-devel >= %eds_ver

%description devel
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool.

This package contains files needed to develop Evolution plugins.

%package devel-doc
Summary: Evolution development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool.

This package contains documentation needed to develop Evolution plugins.

%package tests
Summary: Tests for the Evolution
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Evolution.


%prep
%setup

%build
# reenable RPATH* to link against private libraries
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
	-DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=ON \
	-DKILL_PROCESS_COMMAND:STRING=%_bindir/killall \
	-DENABLE_SCHEMAS_COMPILE:BOOL=OFF \
	-DENABLE_SMIME:BOOL=ON \
	%{?_enable_autoar:-DENABLE_AUTOAR:BOOL=ON} \
	%{?_enable_ytnef:-DENABLE_YTNEF:BOOL=ON} \
	%{?_enable_map:-DENABLE_CONTACT_MAPS:BOOL=ON} \
	%{?_with_openldap:-DWITH_OPENLDAP:BOOL=ON} \
	%{?_with_static_ldap:-DWITH_STATIC_LDAP:BOOL=ON} \
	%{?_enable_gtk_doc:-DENABLE_GTK_DOC:BOOL=ON} \
	%{?_enable_installed_tests:-DENABLE_INSTALLED_TESTS:BOOL=ON} \
	-DVERSION_SUBSTRING:STRING=-%release
%cmake_build

%install
%cmakeinstall_std

# evolution command name
mv %buildroot%_bindir/evolution %buildroot%_bindir/evolution-%ver_major
ln -s %name-%ver_major %buildroot%_bindir/%name

# remove non-packaged files
find %buildroot -type f -name "*.la" -print0 | xargs -r0 rm --

%find_lang --with-gnome --output=%name.lang %name %name-%ver_base

%files
%_bindir/*
%_libdir/%name/
%_libdir/evolution-data-server/ui-modules/module-evolution-alarm-notify.so
%_libexecdir/%name/evolution-backup
%_libexecdir/%name/killev
%doc AUTHORS ChangeLog NEWS README

%exclude %evo_module_dir/module-bogofilter.so
%exclude %evo_module_dir/module-spamassassin.so

%files data -f %name.lang
%_desktopdir/*
%_datadir/%name/
%_datadir/glib-2.0/schemas/org.gnome.evolution.addressbook.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.calendar.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.importer.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.mail.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.attachment-reminder.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.autocontacts.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.email-custom-header.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.external-editor.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.face-picture.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.itip.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.mail-notification.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.prefer-plain.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.publish-calendar.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.templates.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.shell.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.text-highlight.gschema.xml
%_datadir/GConf/gsettings/evolution.convert
%_iconsdir/hicolor/*/*/*
%_man1dir/%name.1.*
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/metainfo/%xdg_name-pst.metainfo.xml

%files devel
%_includedir/*
%_pkgconfigdir/*

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%files bogofilter
%evo_module_dir/module-bogofilter.so
%_datadir/glib-2.0/schemas/org.gnome.evolution.bogofilter.gschema.xml
%_datadir/metainfo/%xdg_name-bogofilter.metainfo.xml

%files spamassassin
%evo_module_dir/module-spamassassin.so
%_datadir/glib-2.0/schemas/org.gnome.evolution.spamassassin.gschema.xml
%_datadir/metainfo/%xdg_name-spamassassin.metainfo.xml

%if_enabled installed_tests
%files tests
%_libexecdir/%name/installed-tests/
%_datadir/installed-tests/%name/
%endif


%changelog
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

* Mon Jul 16 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.4-alt1
- 3.28.4

* Mon Jun 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Thu Apr 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt2
- updated to 3.28.1-9-gd59f43c (fixed BGO #1560312/ALT #34800)

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
- rebuilt against libical.so.3

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

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

* Mon Aug 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.5-alt1
- 3.20.5

* Mon Jul 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Mon Jun 06 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Feb 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.5.1-alt1
- 3.18.5.1

* Mon Feb 15 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.5-alt1
- 3.18.5

* Thu Feb 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt3
- updated to 3.18.4-18-g34b9382

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

* Mon Jul 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt1
- 3.16.4 release

* Sun Jun 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt0.1
- 3.16.4 snapshot

* Mon Jun 08 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2.1-alt1
- 3.16.2.1

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Feb 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.11-alt1
- 3.12.11

* Mon Jan 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.10-alt1
- 3.12.10
- enabled TNEF attachments support via libytnef library

* Mon Dec 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.9-alt1
- 3.12.9

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.8-alt1
- 3.12.8

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.7-alt1
- 3.12.7 release

* Wed Oct 01 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.7-alt0.1
- updated to 3.12.7_c8335691

* Sat Sep 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.6-alt2
- rebuilt for GNOME-3.14

* Mon Sep 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.6-alt1
- 3.12.6

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.5-alt1
- 3.12.5

* Mon Jul 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.4-alt1
- 3.12.4 release

* Thu Jul 03 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.4-alt0.1
- 3.12.4_7d48fad0

* Mon Jun 09 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Sun Apr 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1 release

* Tue Apr 01 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt0.1
- 3.12.1 snapshot (455a11216)

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Sun Mar 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.92-alt1
- 3.11.92

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.4-alt1
- 3.10.4

* Mon Dec 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt3
- rebuilt against libical*.so.1

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
- 3.8.1 snapshot (b00e0e1)

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

* Tue Feb 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt2
- fixed pst-import plugin for libpst-0.6.54

* Mon Jan 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Oct 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- temporarily disabled maps in contacts preview via libchamplain

* Sun Sep 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Sep 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.92-alt1
- 3.1.92

* Sun Sep 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.90-alt1
- 3.1.90

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt2
- 3.0.3 ftp release

* Wed Jun 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3 snapshot

* Wed Jun 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- fixed schemas list

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sat Apr 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt2
- added x-scheme-handler/mailto mimetype to evolution.desktop
- updated translations

* Fri Apr 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Sat Mar 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt2
- updated buildreqs
- fixed build with newer GTK+

* Mon Feb 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- redefine %%_libexecdir to make evolution work on x86_64

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Thu Aug 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3
- remove pregenerated .desktop files (closes #23665)

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1.2-alt2
- removed obsolete depenedece on gnome-spell

* Wed Apr 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1.2-alt1
- 2.30.1.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Sat Mar 20 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Mon Mar 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90
- new -data noarch subpackage
- libpst support enabled

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6
- new devel-doc subpackage
- updated buildreqs

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Sun Oct 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0
- radically relaxed %%strict_build_settings

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Wed Aug 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Fri May 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1.1-alt2
- fixed build with new libtool_2.2

* Wed Apr 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1.1-alt1
- 2.26.1.1

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt2
- NetworkManager support enabled

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Mar 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Mon Jan 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- updated buildreqs

* Mon Jan 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post{,un} scripts

* Fri Nov 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1.1-alt1
- 2.24.1.1
- add COPYING to %%doc (see NEWS)
- attempt to properly link exchange plugin -- patch2 (shaba@)

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Sep 27 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- drop patches for bugs that fixed in upstream

* Mon Jun 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- 2.22.3
- remove patches CVE-2008-1108 and CVE-2008-1109 (fixed upstream)

* Thu Jun 05 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt2
- Add patches for fix CVE-2008-1108 and CVE-2008-1109 (buffer overflow vulnerabilities)
- Remove the welcome email from Novell

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Fri May 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1.1-alt1
- 2.22.1.1
- drop patch18 for check line status (fixed upstream)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for evolution

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Thu Mar 13 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Mon Feb 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.12.3-alt1
- 2.12.3
- Removed patches:
  + RH bug #215467 / GNOME bug #380644 (fixed upstream)
  + GNOME bug #363695 (causes issues)
- Add patch for GNOME bug #454465 (fix Save button in task dialog)
- Revise patch for GNOME bug #417999

* Thu Nov 29 2007 Alexey Shabalin <shaba@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Thu Oct 25 2007 Alexey Shabalin <shaba@altlinux.ru> 2.12.1-alt1
- 2.12.1
- Disable patch for GNOME bug #376991 for now. It may be contributing
  to password prompting problems as described in RH bug #296671.
- Revise patch for GNOME bug #362638 to fix GNOME bug #357175
  (Evolution fails to close after IMAP alert has been displayed).
- remove require perl-devel (ALT #13168)

* Fri Oct 12 2007 Alexey Shabalin <shaba@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Evolution no longer requires libgnomeprint[ui].
- require libgtkhtml3 >= 3.16.0
- Revised patch for linking with krb5
- removed patches:
  + evolution-2.6.0-prototypes.patch (obsolete)
  + RH bug #157400 / GNOME bug #303877 (fixed upstream)
  + RH bug #157505 / GNOME bug #303878 (fixed upstream)
  + RH bug #190359 (fixed upstream)
  + RH bug #161885 / GNOME bug #309166 (fixed upstream)
  + RH bug #202751 / GNOME bug #355766 (fixed upstream)
  + RH bug #182247 (fixed upstream)
  + GNOME bug #373837 (fixed upstream)
  + RH bug #218801 (fixed upstream)
  + GNOME bug #373116 (fixed upstream)
  + RH bug #218898 / GNOME bug #385414 (fixed upstream)
  + GNOME bug #419469 (fixed upstream)
  + GNOME bug #419524 (fixed upstream)
  + GNOME bug #418971 (fixed upstream)
  + RH bug #234315 (fixed upstream)
  + RH bug #236399 (fixed upstream)
  + RH bug #236860 (fixed upstream)
  + RH bug #238155 (fixed upstream)
  + RH bug #240147 (fixed upstream)
- Add patches:
  + GNOME bug #476040 (fix attachment icon)
  + GNOME bug #477045 (use standard icon names)

* Mon Sep 10 2007 Alexey Rusakov <ktirf@altlinux.org> 2.10.3-alt2
- added Requires: gnome-settings-daemon (ALT Bug #12225)

* Fri Aug 17 2007 Alexey Shabalin <shaba@altlinux.ru> 2.10.3-alt1
- Update to 2.10.3
- change packager
- add/remove patches from fc7
- mini fix spec
- fix build with krb5 (patch1)

* Wed May 02 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.3-alt3
- CVE-2007-1002 (Shared memo categories format string vulnerability)
- fixed #11672 (crash during startup) 
 
* Sun Mar 11 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.3-alt2
- add some patches from Fedora updates

* Sat Feb 24 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.3-alt1
- new version 2.8.3

* Thu Jan 04 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.2.1-alt1
- new version 2.8.2.1

* Fri Dec 29 2006 Ilya Mashkin <oddity@altlinux.ru> 2.8.1.1-alt2
- rebuild with new dbus

* Fri Oct 20 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.1.1-alt1
- new version 2.8.1.1 (with rpmrb script)

* Tue Sep 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.0-alt1
- Release 2.8.0
- Updated Patch0
- Patch1 has gone upstream

* Fri Sep 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.3-alt1
- Release 2.6.3

* Sun Jul 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt2
- Rebuilt without GStreamer 0.8; no inline audio as of yet

* Thu Jun 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt1
- Release 2.6.2

* Sat May 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.1-alt1
- Release 2.6.1

* Wed Apr 19 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.6.0-alt2.1
- Rebuild with dbus-0.61-alt1 .

* Sat Mar 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt2
- x86_64 fix: make sure that %%_libexecdir and %%_libdir are the same

* Wed Mar 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt1
- Release 2.6.0

* Sat Mar 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.92-alt2
- Added gnome-icon-theme to the build dependencies
- Patch1: resolve undefined symbols

* Sun Mar 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.92-alt1
- 2.5.92
- Patch1 has gone upstream

* Sat Feb 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.91-alt1
- Updated to 2.5.91
- Removed Debian-style menu
- Patch1: fix a crash on opening a new message composer (GNOME bug 331680)
- Buildreq

* Wed Dec 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.2.1-alt1
- 2.4.2.1
- Gnome Spell GConf key patch from Vital Khilko

* Wed Nov 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.2-alt1
- 2.4.2
- Compile with separately installed libnspr and libnss

* Wed Nov 23 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt2.1
- Spec cosmetics
- Drop explicit nspr/nss configure flags, relying on mozilla .pc files instead

* Sat Oct 22 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt2
- Version required for libsoup bumped to 2.2.6
- Dropped gal dependencies
- Buildreq

* Tue Oct 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Thu Sep 22 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.0-alt2
- Added /usr/bin/evolution symlink (bug 7918)

* Tue Sep 06 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Fri Aug 26 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.3.8-alt1
- 2.3.8

* Mon Aug 08 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.3.7-alt0.1
- 2.3.7

* Fri Jul 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.3.6.1-alt0.1
- Updated to 2.3.6.1

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Tue Apr 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Thu Mar 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Thu Mar 10 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1.1
- put symlinks to libeshell & libeutil in %%_libdir
  so connector can find thease libararies. (reported by Alex Gorbachenko).

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Fri Feb 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Mon Jan 24 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt2
- remove 'use diagnostics' from addressbook/tools/csv2vcard.
- don't use setgid for camel-lock-helper.
- fixed CAN-2005-0102.
- requres mozilla, mozilla-psm (#5444).

* Sat Dec 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt1
- 2.0.3
- fixed #5452 (thanks mhz@).

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt0.5
- 2.0.2

* Thu Sep 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt0.5
- 2.0.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt0.5
- 2.0.0

* Sun Sep 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.94.1-alt0.5
- new version.

* Wed Aug 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.92.1-alt0.5
- 1.5.92.1

* Wed Aug 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.92-alt0.5
- 1.5.92

* Tue Jul 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.91-alt0.5
1.5.91

* Tue Jul 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.90-alt0.5
- 1.5.90

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.9.2-alt0.5
- 1.5.9.2

* Sat Jun 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.9.1-alt0.5
- 1.5.9.1

* Fri May 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.8-alt0.5
- 1.5.8

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.7-alt0.5
- 1.5.7

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.6.2-alt0.5
- 1.5.6.2

* Tue Apr 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.6-alt0.5
- 1.5.6

* Sat Mar 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.5-alt0.5
- 1.5.5
- devel subpackage.

* Thu Feb 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.4-alt0.6
- fix build for new krb5 libs location.
- fix buildreqs.

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.4-alt0.5
- 1.5.4

* Sat Jan 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.3-alt0.5
- 1.5.3

* Wed Aug 06 2003 AEN <aen@altlinux.ru> 1.4.4-alt1
- new version

* Mon Jul 14 2003 AEN <aen@altlinux.ru> 1.4.3-alt2
- PreReq and BuildRequires on liborbi2 & libbonobo2 added (thnks to Vyt)

* Fri Jul 11 2003 AEN <aen@altlinux.ru> 1.4.3-alt1
- release

* Tue Jul 08 2003 AEN <aen@altlinux.ru> 1.4.1-alt0.2
- libexecdir fixed

* Thu Jul 03 2003 AEN <aen@altlinux.ru> 1.4.1-alt0.1
- new version from cvs

* Wed Jul 02 2003 AEN <aen@altlinux.ru> 1.4.0-alt2
- wombat patch from mdk

* Mon Mar 31 2003 AEN <aen@altlinux.ru> 1.2.3-alt1
- new version

* Tue Mar 18 2003 AEN <aen@altlinux.ru> 1.2.2-alt2
- security patch

* Sat Feb 15 2003 AEN <aen@altlinux.ru> 1.2.2-alt1
- new version

* Wed Feb 05 2003 AEN <aen@altlinux.ru> 1.2.1-alt3
- new ru.po from CVS added

* Wed Jan 15 2003 AEN <aen@altlinux.ru> 1.2.1-alt2
- requires fixed

* Mon Dec 23 2002 AEN <aen@altlinux.ru> 1.2.1-alt1
- new version

* Mon Dec 02 2002 AEN <aen@altlinux.ru> 1.2.0-alt3
- added Requires on gnome-vfs >= 1.0.5

* Tue Nov 19 2002 AEN <aen@altlinux.ru> 1.2.0-alt2
- fixed permissions

* Mon Nov 18 2002 AEN <aen@altlinux.ru> 1.2.0-alt1
- new version

* Thu Oct 24 2002 AEN <aen@altlinux.ru> 1.0.8-alt3
- scrollkeeper patch from MDK
- build with pilot

* Tue Oct 22 2002 AEN <aen@altlinux.ru> 1.0.8-alt2
- rebuilt with mozilla-1.2a
- pilot temporary disabled

* Mon Jul 01 2002 AEN <aen@logic.ru> 1.0.8-alt1
- new version

* Mon Jun 17 2002 AEN <aen@logic.ru> 1.0.7-alt1
- new version
- patch2 removed

* Wed Jun 05 2002 AEN <aen@logic.ru> 1.0.5-alt3
- rebuild with mozilla-1.0
- patch2 from CVS

* Wed May 15 2002 AEN <aen@logic.ru> 1.0.5-alt2
- enable-file-locking=fcntl

* Mon May 13 2002 AEN <aen@logic.ru> 1.0.5-alt1
- new version

* Tue Mar 26 2002 AEN <aen@logic.ru> 1.0.3-alt1
- new version
- build with external nss

* Wed Mar 13 2002 AEN <aen@logic.ru> 1.0.2-alt3
- *.desktop converted

* Sun Mar 10 2002 AEN <aen@logic.ru> 1.0.2-alt2
- rebuild with static nss-1.1.3

* Mon Feb 04 2002 AEN <aen@logc.ru> 1.0.2-alt1
- new version

* Fri Jan 25 2002 AEN <aen@logic.ru> 1.0.1-alt5
- BuildRequires generated

* Fri Jan 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.1-alt4
- Updated buildrequires.

* Thu Jan 17 2002 AEN <aen@logic.ru> 1.0.1-alt3
- requires: gtkhtml added

* Tue Jan 15 2002 AEN <aen@logic.ru> 1.0.1-alt2
- updates russian translation

* Mon Jan 14 2002 AEN <aen@logic.ru> 1.0.1-alt1
- new version
- patches 0-1 removed, patch2 refreshed

* Wed Dec 05 2001 AEN <aen@logic.ru> 1.0-alt1
- release

* Wed Nov 21 2001 AEN <aen@logic.ru> 0.99.2-alt2
- official RC2
- rebuild with new gnome-pilot

* Mon Nov 19 2001 AEN <aen@logic.ru> 0.99.2-alt1
- snapshot

* Fri Nov 09 2001 AEN <aen@logic.ru> 0.99-alt2
- w/o font patch

* Fri Nov 09 2001 AEN <aen@logic.ru> 0.99-alt1
- new version

* Mon Oct 29 2001 AEN <aen@logic.ru> 0.16-alt0.1
- build snapshot

* Tue Oct 09 2001 AEN <aen@logic.ru> 0.15-alt2
- fonts patch

* Tue Oct 09 2001 AEN <aen@logic.ru> 0.15-alt1
- new version

* Wed Sep 12 2001 AEN <aen@logic.ru> 0.13-alt3
- requires bonobo-conf
* Mon Sep 10 2001 AEN <aen@logic.ru> 0.13-alt2
- i18n patch from MDK

* Fri Sep 07 2001 AEN <aen@logic.ru> 0.13-alt1
- release 0.13

* Wed Sep 05 2001 AEN <aen@logic.ru> 0.13-alt0.1
- snapshot

* Wed Sep 05 2001 AEN <aen@logic.ru> 0.12-alt3
- rebuild with new libgal/gtkhtml
- oaf-slay added to %post

* Thu Aug 23 2001 AEN <aen@logic.ru> 0.12-alt2
- rebuild with new libtool/autoconf

* Thu Aug 09 2001 AEN <aen@logic.ru> 0.12-alt1
- new version

* Tue Jul 24 2001 AEN <aen@logic.ru> 0.11-alt1
- new version
- w/o movemail

* Tue Jul 17 2001 AEN <aen@logic.ru> 0.10.99-alt3
- new snapshot with  gtkhtml-0.10.0

* Thu Jul 12 2001 AEN <aen@logic.ru> 0.10.99-alt2
- new snapshot

* Mon Jul 9 2001 AEN <aen@logic.ru> 0.10.99-alt1
- new version with db-3.1.17

* Thu May 24 2001 AEN <aen@logic.ru> 0.10-alt5
- built cvs version with libgal-0.8 and gtkhtml-0.9.3+
- built w/o pilot, ssl, nspr

* Thu May 17 2001 AEN <aen@logic.ru> 0.10-alt4
- build with pilot support

* Wed May 16 2001 AEN <aen@logic.ru> 0.10-alt3
- charset patch
- ru.po fixed

* Tue May 15 2001 AEN <aen@logic.ru> 0.10-alt2
- %files fixed

* Tue May 15 2001 AEN <aen@logic.ru> 0.10-alt1
- 0.10
* Mon Apr 9 2001 AEN <aen@logic.ru> 0.9-ipl3mdk
- sync with MDK
- rebuild in Gnome-1.4 environment

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9-ipl2mdk
- Moved static libraries to devel-static subpackage.

* Wed Mar 14 2001 AEN <aen@logic.ru> 0.9-ipl1mdk
- 0.9

* Thu Feb 22 2001 AEN <aen@logic.ru> 0.8-ipl3mdk
- build ximean snapsot 2001/02/16

* Thu Feb 22 2001 AEN <aen@logic.ru> 0.8-ipl2mdk
- rebuild with new libraries
- gal-0.5 patch

* Sat Dec 16 2000 AEN <aen@logic.ru>
- 0.8
- adopted for RE
* Thu Nov 16 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6-3mdk
- Really remove dependency on old libstdc++

* Sat Nov  4 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6-2mdk
- simple rebuild (new libstdc++)

* Fri Oct 27 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6-1mdk
- Release 0.6
- Disable LDAP (OpenLDAP 2.0 not supported yet)

* Mon Sep 18 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5.1-1mdk
- Release 0.5.1

* Fri Sep 15 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5-2mdk
- add missing icons

* Thu Sep 14 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5-1mdk
- Release 0.5 (+ merge from Helix 0mdk_helix_1)

* Mon Aug 28 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.4.1-1mdk
- Release 0.4.1 (merge from Helix 0_helix_1)
- no longer conflict with gnome-pim

* Fri Aug 11 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.3.1-2mdk
- add dependency on gnome-vfs
- add menu entry

* Thu Aug  3 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.3.1-1mdk
- Release 0.3.1
- first mandrake package : BM + macroszification
- Build without GConf

* Sun May 21 2000 Ross Golder <rossigee@bigfoot.com>
- created spec file
