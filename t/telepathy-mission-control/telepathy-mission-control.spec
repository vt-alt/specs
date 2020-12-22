%define _libexecdir %_prefix/libexec
%define api_ver 5.5
%define plugin_abi_ver 0

#monitor device suspending and resuming
%def_disable upower
# NetworkManager support
%def_enable nm
%def_disable check

Name: telepathy-mission-control
Version: 5.16.6
Release: alt1

Summary: Telepathy mission control plugin library
License: LGPL-2.1
Group: System/Libraries
Url: http://mission-control.sourceforge.net/

Source: http://telepathy.freedesktop.org/releases/%name/%name-%version.tar.gz

Requires: dconf

BuildRequires(pre): rpm-build-python3
BuildRequires: gtk-doc libgio-devel >= 2.46.0 libdbus-glib-devel libtelepathy-glib-devel >= 0.22.0
%{?_enable_upower:BuildRequires: libupower-devel < 0.99}
%{?_enable_nm:BuildRequires: libnm-devel}

%if_enabled check
BuildRequires: /proc python3-module-twisted-words python3-module-twisted-core
BuildRequires: python3-module-dbus telepathy-logger dbus-tools-gui
%endif

%description
Mission Control, or MC, is a Telepathy component providing a way for
"end-user" applications to abstract some of the details of connection
managers, to provide a simple way to manipulate a bunch of connection
managers at once, and to remove the need to have in each program the
account definitions and credentials.

%package -n lib%name
Summary: Telepathy mission control plugin library
Group: System/Libraries
Obsoletes: %name
Provides: %name = %version-%release

%description -n lib%name
Mission Control, or MC, is a Telepathy component providing a way for
"end-user" applications to abstract some of the details of connection
managers, to provide a simple way to manipulate a bunch of connection
managers at once, and to remove the need to have in each program the
account definitions and credentials.

%package -n lib%name-devel
Summary: Development libraries and header files for %name
Group: Development/C
Requires: lib%name = %version-%release
Obsoletes: %name-devel
Provides: %name-devel = %version-%release

%description -n lib%name-devel
Development libraries and header files for %name.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
export CFLAGS="$CFLAGS `pkg-config --cflags glib-2.0` `pkg-config --cflags dbus-glib-1`"
%configure \
	--disable-static \
	--disable-schemas-compile \
	PYTHON=%__python3

%make_build

%install
%makeinstall_std
# plugin dir
mkdir %buildroot%_libdir/mission-control-plugins.%plugin_abi_ver

%check
%make check

%files -n lib%name
%_bindir/*
%_libdir/libmission-control-plugins.so.*
%_libexecdir/mission-control-5
%dir %_libdir/mission-control-plugins.%plugin_abi_ver
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/im.telepathy.MissionControl.FromEmpathy.gschema.xml
%_man1dir/*
%_man8dir/*
%doc AUTHORS ChangeLog

%files -n lib%name-devel
%_libdir/libmission-control-plugins.so
%_includedir/mission-control-%api_ver/
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/*

%changelog
* Fri Aug 28 2020 Yuri N. Sedunov <aris@altlinux.org> 5.16.6-alt1
- 5.16.6

* Sun Oct 27 2019 Yuri N. Sedunov <aris@altlinux.org> 5.16.5-alt1
- 5.16.5

* Sun Jul 01 2018 Yuri N. Sedunov <aris@altlinux.org> 5.16.4-alt2
- updated buildreqs
- disabled %%check

* Sat Sep 03 2016 Yuri N. Sedunov <aris@altlinux.org> 5.16.4-alt1
- 5.16.4

* Tue Feb 16 2016 Yuri N. Sedunov <aris@altlinux.org> 5.16.3-alt1.1
- packaged %%_libdir/mission-control-plugins.0 (ALT #31378)

* Tue Aug 26 2014 Yuri N. Sedunov <aris@altlinux.org> 5.16.3-alt1
- 5.16.3

* Mon Jun 16 2014 Yuri N. Sedunov <aris@altlinux.org> 5.16.2-alt1
- 5.16.2

* Tue Feb 18 2014 Yuri N. Sedunov <aris@altlinux.org> 5.16.1-alt2
- rebuilt for GNOME-3.12 (temporarily disabled upower support)

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 5.16.1-alt1
- 5.16.1

* Thu Oct 03 2013 Yuri N. Sedunov <aris@altlinux.org> 5.16.0-alt1
- 5.16.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 5.15.1-alt1
- 5.15.1

* Tue May 07 2013 Yuri N. Sedunov <aris@altlinux.org> 5.14.1-alt1
- 5.14.1

* Sat Oct 06 2012 Yuri N. Sedunov <aris@altlinux.org> 5.14.0-alt1
- 5.14.0

* Thu Sep 27 2012 Yuri N. Sedunov <aris@altlinux.org> 5.13.2-alt1
- 5.13.2

* Wed Jul 25 2012 Yuri N. Sedunov <aris@altlinux.org> 5.12.1-alt1
- 5.12.1

* Tue Apr 03 2012 Yuri N. Sedunov <aris@altlinux.org> 5.12.0-alt1
- 5.12.0

* Mon Feb 27 2012 Yuri N. Sedunov <aris@altlinux.org> 5.11.0-alt1
- 5.11.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 5.10.1-alt2
- used %%autoreconf to fix RPATH problem

* Sun Nov 13 2011 Yuri N. Sedunov <aris@altlinux.org> 5.10.1-alt1
- 5.10.1

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 5.8.1-alt1
- 5.8.1

* Wed Aug 10 2011 Yuri N. Sedunov <aris@altlinux.org> 5.8.0-alt1
- 5.8.0

* Sun Apr 03 2011 Yuri N. Sedunov <aris@altlinux.org> 5.7.7-alt1
- 5.7.7

* Tue Mar 08 2011 Yuri N. Sedunov <aris@altlinux.org> 5.7.6-alt1
- 5.7.6

* Mon Dec 13 2010 Yuri N. Sedunov <aris@altlinux.org> 5.6.1-alt1
- 5.6.1

* Fri Sep 03 2010 Yuri N. Sedunov <aris@altlinux.org> 5.5.3-alt1
- 5.5.3

* Wed Jun 16 2010 Yuri N. Sedunov <aris@altlinux.org> 5.4.3-alt1
- 5.4.3

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 5.4.2-alt1
- 5.4.2

* Wed Apr 21 2010 Yuri N. Sedunov <aris@altlinux.org> 5.4.0-alt1
- 5.4.0

* Wed Nov 25 2009 Yuri N. Sedunov <aris@altlinux.org> 5.3.2-alt2
- updated buildreqs
- %%check section

* Thu Nov 19 2009 Yuri N. Sedunov <aris@altlinux.org> 5.3.2-alt1
- 5.3.2
- gnome-keyring support

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 5.2.3-alt1
- 5.2.3

* Sun Jul 20 2008 Igor Zubkov <icesik@altlinux.org> 4.67-alt1
- 4.66 -> 4.67

* Sat Jun 28 2008 Igor Zubkov <icesik@altlinux.org> 4.66-alt1
- 4.65 -> 4.66

* Wed Apr 30 2008 Igor Zubkov <icesik@altlinux.org> 4.65-alt1
- 4.60 -> 4.65
- buildreq

* Sat Feb 23 2008 Igor Zubkov <icesik@altlinux.org> 4.60-alt1
- 4.57 -> 4.60

* Fri Jan 25 2008 Igor Zubkov <icesik@altlinux.org> 4.57-alt2
- rename telepathy-mission-control to libtelepathy-mission-control
- rename telepathy-mission-control-devel to libtelepathy-mission-control-devel

* Fri Jan 25 2008 Igor Zubkov <icesik@altlinux.org> 4.57-alt1
- 4.55 -> 4.57

* Tue Jan 15 2008 Igor Zubkov <icesik@altlinux.org> 4.55-alt1
- 4.54 -> 4.55

* Tue Jan 15 2008 Igor Zubkov <icesik@altlinux.org> 4.54-alt1
- 4.53 -> 4.54

* Tue Jan 15 2008 Igor Zubkov <icesik@altlinux.org> 4.53-alt1
- 4.51 -> 4.53

* Tue Dec 11 2007 Igor Zubkov <icesik@altlinux.org> 4.51-alt1
- 4.49 -> 4.51
- buildreq

* Thu Oct 25 2007 Igor Zubkov <icesik@altlinux.org> 4.49-alt1
- 4.45 -> 4.49

* Thu Oct 04 2007 Igor Zubkov <icesik@altlinux.org> 4.45-alt1
- 4.42 -> 4.45

* Mon Sep 24 2007 Igor Zubkov <icesik@altlinux.org> 4.42-alt1
- 4.41 -> 4.42

* Thu Sep 20 2007 Igor Zubkov <icesik@altlinux.org> 4.41-alt1
- 4.39 -> 4.41

* Mon Sep 17 2007 Igor Zubkov <icesik@altlinux.org> 4.39-alt1
- 4.37 -> 4.39

* Thu Sep 06 2007 Igor Zubkov <icesik@altlinux.org> 4.37-alt1
- 4.34 -> 4.37

* Tue Aug 14 2007 Igor Zubkov <icesik@altlinux.org> 4.34-alt1
- 4.33 -> 4.34

* Thu Aug 09 2007 Igor Zubkov <icesik@altlinux.org> 4.33-alt1
- 4.31 -> 4.33

* Thu Aug 02 2007 Igor Zubkov <icesik@altlinux.org> 4.31-alt1
- 4.30 -> 4.31

* Tue Jul 17 2007 Igor Zubkov <icesik@altlinux.org> 4.30-alt1
- 4.26 -> 4.30

* Fri Jun 22 2007 Igor Zubkov <icesik@altlinux.org> 4.26-alt1
- build for Sisyphus


