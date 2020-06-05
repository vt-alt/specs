%define soname 4
%define gtkver 2

%def_disable bootstrap

Name: libfm
Version: 1.3.1
Release: alt3

Summary: Core library of PCManFM file manager
License: GPL
Group: System/Libraries

Url: https://lxde.org
Source: %name-%version.tar
Patch0: 0001-SF-1087-Fix-all-allfiles-parse-conditions.patch
Patch1: 0002-SF-1082-Fix-SelectionCount-condition-parsing-if-was-.patch

%{?_disable_bootstrap:BuildPreReq: rpm-build-xdg}
BuildRequires: intltool %{?_disable_bootstrap:libmenu-cache-devel}
BuildRequires: libdbus-glib-devel libudisks2-devel
BuildRequires: glib2-devel libgtk+%gtkver-devel
BuildRequires: gtk-doc
BuildRequires: vala >= 0.13.0
BuildRequires: libexif-devel
BuildRequires: libxslt-devel

BuildRequires: gcc-c++ cmake rpm-macros-cmake

%description
LibFM is a core library of PCManFM file manager.

%package -n %name%soname
Summary: %summary
Group: System/Libraries
Requires: gvfs wm-common-freedesktop
Conflicts: libfm2

%description -n %name%soname
LibFM is a core library of PCManFM file manager.

It is developed as the core of next generation PCManFM and takes care
of all file-related operations such as copy & paste, drag & drop, file
associations or thumbnail support. By utilizing glib/gio and gvfs
libfm can access remote filesystems supported by gvfs.

%package devel
Summary: Development files for %name
Group: Development/Other
Conflicts: libfm2-devel

%description devel
This package contains files needed to build applications using LibFM.

%if_disabled bootstrap
%package -n lxde-lxshortcut
Summary: Application shortcuts editor
Group: Graphical desktop/Other

%description -n lxde-lxshortcut
LXShortcut is a small program used to edit application shortcuts
created with freedesktop.org Desktop Entry spec.
%endif

%prep
%setup
%patch0 -p1
%patch1 -p1
sed -ri '/AM_INIT_AUTOMAKE/s,-Werror,\0 -Wno-portability,' configure.ac

%build
%autoreconf
%configure \
    --disable-static \
    --disable-silent-rules \
%if_disabled bootstrap
    --with-gtk=%gtkver \
%else
    --with-extra-only \
    --with-gtk=no \
%endif
    --disable-gtk-doc \
    --enable-largefile \
    --enable-udisks \
    --sysconfdir=%_sysconfdir

%make_build

# FIXME: tilda versions don't work with RPM in general
sed -i 's,\~[a-z0-9]*,,g' libfm*.pc

%install
%makeinstall_std
%find_lang libfm

# Remove unnecessary files
rm -f %buildroot%_libdir/%name/modules/*.la
%if %gtkver==3
    rm -f %buildroot%_pkgconfigdir/libfm-gtk.pc
%endif
%if %gtkver==2
    rm -f %buildroot%_pkgconfigdir/libfm-gtk3.pc
%endif

%files -n %name%soname -f libfm.lang
%_libdir/*.so.*
%if_disabled bootstrap
%_xdgconfigdir/*
%dir %_libdir/%name
%dir %_libdir/%name/modules
%_libdir/%name/modules/*.so
%_xdgmimedir/packages/*
%_datadir/%name/
%_desktopdir/libfm-pref-apps.desktop
%_bindir/libfm-pref-apps
%_man1dir/libfm-pref-apps.1*
%endif

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
#%%doc %_datadir/gtk-doc/html/%name

%if_disabled bootstrap
%files -n lxde-lxshortcut
%_bindir/lxshortcut
%_desktopdir/lxshortcut.desktop
%_man1dir/lxshortcut.1*
%endif

%changelog
* Fri May 22 2020 Anton Midyukov <antohami@altlinux.org> 1.3.1-alt3
- Added upstream patchs

* Fri Sep 13 2019 Nikita Ermakov <arei@altlinux.org> 1.3.1-alt2
- Add bootstrap flag.

* Fri Jan 04 2019 Anton Midyukov <antohami@altlinux.org> 1.3.1-alt1
- new version 1.3.1

* Tue Jun 12 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0.2-alt2
- disable gtk-doc (fix FTBFS)
- fix URL

* Tue May 01 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0.2-alt1
- new version 1.3.0.2

* Tue Apr 24 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Tue Dec 13 2016 Anton Midyukov <antohami@altlinux.org> 1.2.5-alt1
- new version 1.2.5

* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4

* Mon Mar 02 2015 Michael Shigorin <mike@altlinux.org> 1.2.3-alt3
- added missing Requires: wm-common-freedesktop to %name%soname
  as per http://www.altlinux.org/Window_Manager_Policy
  (MIME type handling should work now)

* Mon Dec 08 2014 Michael Shigorin <mike@altlinux.org> 1.2.3-alt2
- added Requires: gvfs (closes: #30514)

* Tue Oct 14 2014 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 1.2.2.1-alt1
- 1.2.2.1

* Thu May 22 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt5
- moved lxshortcut desktop file and manpage to appropriate subpackage

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt4
- separate lxde-lxshortcut for proper dist-upgrade

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt3
- merged 1.1.2-alt0.2.1 changelog record to please the buildsystem

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt2
- re-enabled gtk support (reverted to gtk2 though) for pcmanfm

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- 1.2.0
- disabled gtk support (upstream chose Qt instead of GTK3)
  + thus dropped libfm-pref-apps, lxshortcut
- renamed main subpackage according to shared libs policy

* Fri Mar 07 2014 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt0.rc1.1
- Build libfm 1.2.0 as separate package

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt0.2.1
- Fixed build
