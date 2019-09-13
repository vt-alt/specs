%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 2.60
%define api_ver 2.0
%define pcre_ver 8.31
%define gio_module_dir %_libdir/gio/modules

%set_verify_elf_method strict
%add_verify_elf_skiplist %_libexecdir/installed-tests/glib/*

%def_with sys_pcre
%def_enable selinux
%def_disable fam
%def_disable systemtap
%def_enable installed_tests
%def_enable gtk_doc
%def_enable man
%def_enable libmount
%def_disable debug
%def_disable check

Name: glib2
Version: %ver_major.7
Release: alt1

Summary: A library of handy utility functions
License: %lgpl2plus
Group: System/Libraries
Url: ftp://ftp.gnome.org

%if_enabled snapshot
Source: glib-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/glib/%ver_major/glib-%version.tar.xz
%endif

Source1: glib-compat.map
Source2: glib-compat.lds
Source3: gobject-compat.map
Source4: gobject-compat.lds
Source5: gio-compat.map
Source6: gio-compat-2.57.lds

Source10: glib2.sh
Source11: glib2.csh

Patch: glib-2.59.3-alt-compat-version-script.patch
# stop spam about deprecated paths in schemas
Patch1: glib-2.53.5-alt-deprecated_paths-nowarning.patch
Patch2: glib-2.53.7-alt-add-xvt.patch
Patch3: glib-2.38.2-alt-lfs.patch
Patch4: glib-2.50.1-alt-dbus_socket_path.patch

# mike@: fix build with lcc 1.23 (lacks some gcc5 builtins)
Patch10: glib-2.60.1-alt-e2k-lcc.patch

%def_with locales
%if_with locales
Requires: %name-locales = %version
%endif

Provides: lib%name = %version
Obsoletes: lib%name < %version

Provides: %name-core = %version
Obsoletes: %name-core < %version

# use python3
#AutoReqProv: nopython
#%define __python %nil
%add_python3_path %_datadir/glib-2.0/codegen
%allow_python3_import_path %_datadir/glib-2.0/codegen

%if_with sys_pcre
BuildRequires: libpcre-devel >= %pcre_ver
Requires: pcre-config(utf8) pcre-config(unicode-properties)
BuildPreReq: pcre-config(utf8) pcre-config(unicode-properties)
%endif

BuildRequires(pre): meson rpm-build-licenses rpm-build-python3
BuildRequires: gcc-c++ gtk-doc indent
BuildRequires: glibc-kernheaders libdbus-devel libpcre-devel
BuildRequires: libffi-devel zlib-devel libelf-devel
%{?_enable_libmount:BuildRequires: libmount-devel}
%{?_enable_selinux:BuildRequires: libselinux-devel}
%{?_enable_fam:BuildRequires: libgamin-devel}
%{?_enable_systemtap:BuildRequires: libsystemtap-sdt-devel}

# for check  & tests
BuildRequires: /proc dbus-tools-gui desktop-file-utils chrpath

%description
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality as
an event loop, threads, dynamic loading, and an object system.

%package locales
Summary: Glib internationalization
Group: System/Internationalization
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description locales
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality as
an event loop, threads, dynamic loading, and an object system.

This package provides internationalization support for Glib.

%package devel
Summary: Development files and tools for GLib
Group: Development/C
Requires: %name = %version-%release
Requires: rpm-build-gir >= 0.5
Provides: lib%name-devel = %version
Obsoletes: lib%name-devel < %version

%description devel
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality as
an event loop, threads, dynamic loading, and an object system.

This package provides header files and development tools for GLIB.

%package devel-static
Summary: Static version of GLib libraries
Group: Development/C
Requires: %name-devel = %version-%release
Provides: lib%name-devel-static = %version
Obsoletes: lib%name-devel-static < %version

%description devel-static
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality as
an event loop, threads, dynamic loading, and an object system.

This package provides GLIB static libraries.

%package doc
Summary: Documentation for GLib
Group: Development/Documentation
Provides: %name-devel-doc = %version
Obsoletes: %name-devel-doc < %version
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description doc
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality as
an event loop, threads, dynamic loading, and an object system.

This package contains documentation for GLib.

%package -n libgio
Summary: GIO input/output framework
Group: System/Libraries
Provides: gvfs-utils = %version-%release %_bindir/gio
Requires: %name = %version-%release
Requires: gsettings-desktop-schemas
Requires: shared-mime-info >= 0.80

%description -n libgio
GIO is a VFS API, designed to replace GnomeVFS. This GIO implementation is
a part of Glib project; it has support for local filesystems, and
a separate GVFS project contains various backend implementations (CIFS,
FTP, SFTP etc.).

%package -n libgio-devel
Summary: GIO input/output framework
Group: Development/C
Requires: libgio = %version-%release
Requires: %name-devel = %version-%release

%description -n libgio-devel
GIO is a VFS API, designed to replace GnomeVFS. This GIO implementation is
a part of Glib project; it has support for local filesystems, and
a separate GVFS project contains various backend implementations (CIFS,
FTP, SFTP etc.).

This package contains files necessary for development with GIO.

%package -n libgio-doc
Summary: GIO documentation
Group: Development/Documentation
# due to HTML links
Requires: %name-doc = %version-%release
BuildArch: noarch

%description -n libgio-doc
GIO is a VFS API, designed to replace GnomeVFS. This GIO implementation is
a part of Glib project; it has support for local filesystems, and
a separate GVFS project contains various backend implementations (CIFS,
FTP, SFTP etc.).

This package contains documentation for GIO.

%package tests
Summary: Tests for the glib2/libgio packages
Group: Development/Other
Requires: libgio = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed glib2/libgio packages.

%if 0
%package gdb
%description gdb
%endif

%prep
%setup -n glib-%version
%patch -p1 -b .compat_map
%patch1
%patch2 -p1
%patch3 -p1
%patch4

%if_with sys_pcre
rm glib/pcre/*.[ch]
%endif

install -p -m644 %_sourcedir/glib-compat.map glib/compat.map
install -p -m644 %_sourcedir/glib-compat.lds glib/compat.lds
install -p -m644 %_sourcedir/gobject-compat.map gobject/compat.map
install -p -m644 %_sourcedir/gobject-compat.lds gobject/compat.lds
install -p -m644 %_sourcedir/gio-compat.map gio/compat.map
install -p -m644 %_sourcedir/gio-compat-2.57.lds gio/compat.lds

# abicheck always ok
subst '/exit 1/d' check-abis.sh

%ifarch %e2k
subst "/subdir('fuzzing')/d" meson.build
%patch10 -p1
%endif

%build
%meson \
    --default-library=both \
    -Dgio_module_dir='%gio_module_dir' \
    %{?_disable_selinux:-Dselinux=false} \
    %{?_disable_xattr:-Dxattr=false} \
    %{?_disable_libmount:-Dlibmount=false} \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_enable_man:-Dman=true} \
    %{?_without_sys_pcre:-Dinternal_pcre=true} \
    %{?_enable_fam:-Dfam=true} \
    %{?_enable_systemtap:-Dsystemtap=true} \
    %{?_enable_installed_tests:-Dinstalled_tests=true} \
    -Diconv='libc'
%meson_build

%install
%meson_install

# Relocate libgilb-2.0.so.0 to /%_lib.
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/libglib-%api_ver.so.0* %buildroot/%_lib
rm %buildroot%_libdir/libglib-%api_ver.so
ln -s ../../%_lib/libglib-%api_ver.so.0 %buildroot%_libdir/libglib-%api_ver.so

install -pD -m755 %_sourcedir/glib2.sh %buildroot%_sysconfdir/profile.d/glib2.sh
install -pD -m755 %_sourcedir/glib2.csh %buildroot%_sysconfdir/profile.d/glib2.csh

chmod +x %buildroot%_bindir/gtester-report

# GIO modules cache
mkdir -p %buildroot%gio_module_dir
touch %buildroot%gio_module_dir/giomodule.cache
# filetrigger that updates GIO modules cache
cat <<EOF > filetrigger
#!/bin/sh -e

dir=%_libdir/gio/modules/
grep -qs '^'\$dir'' && /usr/bin/gio-querymodules \$dir ||:
EOF

install -pD -m 755 filetrigger %buildroot%_rpmlibdir/gio.filetrigger

# filetrigger that compiles all the GSettings XML schema files under %_datadir/glib-2.0/schemas
cat <<EOF > filetrigger
#!/bin/sh -e

dir=%_datadir/glib-%api_ver/schemas
grep -qs '^'\$dir'' && /usr/bin/glib-compile-schemas --allow-any-name \$dir ||:
EOF

install -pD -m 755 filetrigger %buildroot%_rpmlibdir/gsettings.filetrigger

%find_lang glib20

%check
# g_mapped_file_new fails on /dev/null in hasher
# GLib:ERROR:mappedfile.c:52:test_device: assertion failed (error == (g-file-error-quark, 17)): Failed to map /dev/null' /dev/null': mmap() failed: No such device (g-file-error-quark, 7)
%meson_test

%files
/%_lib/libglib-%api_ver.so.0*
%_libdir/libgobject-%api_ver.so.0*
%_libdir/libgmodule-%api_ver.so.0*
%_libdir/libgthread-%api_ver.so.0*
%config(noreplace) %_sysconfdir/profile.d/*
%doc AUTHORS NEWS README

%files locales -f glib20.lang

%files devel
%_bindir/glib-genmarshal
%_bindir/glib-gettextize
%_bindir/glib-mkenums
%_bindir/gobject*
%_bindir/gtester*
%dir %_includedir/glib-%api_ver
%_includedir/glib-%api_ver/glib*
%_includedir/glib-%api_ver/gobject*
%_includedir/glib-%api_ver/gmodule*
%dir %_libdir/glib-%api_ver
%dir %_libdir/glib-%api_ver/include
%_libdir/glib-%api_ver/include/*.h
%_libdir/libglib-%api_ver.so
%_libdir/libgmodule-%api_ver.so
%_libdir/libgobject-%api_ver.so
%_libdir/libgthread-%api_ver.so
%_pkgconfigdir/glib-%api_ver.pc
%_pkgconfigdir/gmodule*-%api_ver.pc
%_pkgconfigdir/gobject-%api_ver.pc
%_pkgconfigdir/gthread-%api_ver.pc
%_datadir/aclocal/glib*.m4
%_datadir/aclocal/gsettings.m4
%dir %_datadir/glib-%api_ver
%_datadir/glib-%api_ver/gettext/
%_datadir/gettext/its/gschema.its
%_datadir/gettext/its/gschema.loc
%_datadir/glib-%api_ver/codegen/

%if_enabled man
%_man1dir/glib-genmarshal.*
%_man1dir/glib-gettextize.*
%_man1dir/glib-mkenums.*
%_man1dir/gobject*
%_man1dir/gtester*
%endif

%files devel-static
%_libdir/libglib-%api_ver.a
%_libdir/libgobject-%api_ver.a
%_libdir/libgthread-%api_ver.a
# gmodule and gio use dynamic loading
%exclude %_libdir/libgmodule-%api_ver.a
%exclude %_libdir/libgio-%api_ver.a
%if_enabled fam
%exclude %_libdir/gio/modules/libgiofam.a
%exclude %_libdir/gio/modules/libgiofam.la
%endif

%files doc
%doc %_datadir/gtk-doc/html/glib
%doc %_datadir/gtk-doc/html/gobject

%files -n libgio
%_bindir/gapplication
%_bindir/gio
%_bindir/gio-launch-desktop
%_bindir/gio-querymodules
%_bindir/gsettings
%_bindir/glib-compile-schemas
%_bindir/gresource
%_bindir/glib-compile-resources
%_bindir/gdbus
%_libdir/libgio-%api_ver.so.*
%dir %_libdir/gio
%dir %_libdir/gio/modules
%{?_enable_fam:%_libdir/gio/modules/libgiofam.so}
%_libdir/gio/modules/giomodule.cache
%_rpmlibdir/gio.filetrigger
%_rpmlibdir/gsettings.filetrigger
%_datadir/glib-%api_ver/schemas/

%if_enabled man
%_man1dir/gapplication.1.*
%_man1dir/gsettings.*
%_man1dir/glib-compile-schemas.*
%_man1dir/gresource.*
%_man1dir/glib-compile-resources.1*
%_man1dir/gdbus.*
%_man1dir/gio.1.*
%_man1dir/gio-querymodules.*
%endif

%_datadir/bash-completion/completions/gapplication
%_datadir/bash-completion/completions/gio
%_datadir/bash-completion/completions/gresource
%_datadir/bash-completion/completions/gdbus
%_datadir/bash-completion/completions/gsettings

%files -n libgio-devel
%_bindir/gdbus-codegen
%dir %_includedir/glib-%api_ver
%dir %_includedir/glib-%api_ver/gio
%_includedir/glib-%api_ver/gio/*.h
%dir %_includedir/gio-unix-%api_ver
%dir %_includedir/gio-unix-%api_ver/gio
%_includedir/gio-unix-%api_ver/gio/*.h
%_libdir/libgio-%api_ver.so
%_pkgconfigdir/gio-%api_ver.pc
%_pkgconfigdir/gio-unix-%api_ver.pc
%{?_enable_man:%_man1dir/gdbus-codegen.*}

%files -n libgio-doc
%doc %_datadir/gtk-doc/html/gio

%exclude %_datadir/gdb/auto-load/%_libdir/libglib-%api_ver.so.0.*-gdb.py
%exclude %_datadir/gdb/auto-load/%_libdir/libgobject-%api_ver.so.0.*-gdb.py
%exclude %_datadir/glib-%api_ver/gdb/
%exclude %_datadir/glib-%api_ver/valgrind/

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/glib/
# exclude empty
%exclude %_libexecdir/installed-tests/glib/x-content/unix-software/autorun.sh
%_datadir/installed-tests/glib/
%endif

%changelog
* Tue Sep 03 2019 Yuri N. Sedunov <aris@altlinux.org> 2.60.7-alt1
- 2.60.7

* Wed Jul 24 2019 Yuri N. Sedunov <aris@altlinux.org> 2.60.6-alt1
- 2.60.6

* Tue Jul 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.60.5-alt1
- 2.60.5

* Mon Jun 10 2019 Yuri N. Sedunov <aris@altlinux.org> 2.60.4-alt1
- 2.60.4 (fixed CVE-2019-12450)

* Thu May 23 2019 Yuri N. Sedunov <aris@altlinux.org> 2.60.3-alt1
- 2.60.3

* Fri May 03 2019 Yuri N. Sedunov <aris@altlinux.org> 2.60.2-alt1
- 2.60.2

* Sat Apr 20 2019 Yuri N. Sedunov <aris@altlinux.org> 2.60.1-alt2
- fixed build on %%e2k

* Mon Apr 15 2019 Yuri N. Sedunov <aris@altlinux.org> 2.60.1-alt1
- 2.60.1

* Mon Mar 04 2019 Yuri N. Sedunov <aris@altlinux.org> 2.60.0-alt1
- 2.60.0

* Mon Jan 21 2019 Yuri N. Sedunov <aris@altlinux.org> 2.58.3-alt1
- 2.58.3

* Tue Dec 18 2018 Yuri N. Sedunov <aris@altlinux.org> 2.58.2-alt1
- 2.58.2

* Thu Nov 01 2018 Yuri N. Sedunov <aris@altlinux.org> 2.58.1-alt4
- updated to 2.58.1-81-g2daebb93f

* Wed Oct 03 2018 Yuri N. Sedunov <aris@altlinux.org> 2.58.1-alt3
- back to autotools to avoid problems with static linking

* Tue Oct 02 2018 Yuri N. Sedunov <aris@altlinux.org> 2.58.1-alt2
- fixed glib-2.0.pc for static link

* Fri Sep 21 2018 Yuri N. Sedunov <aris@altlinux.org> 2.58.1-alt1
- 2.58.1 (ported to meson build system)

* Thu Aug 30 2018 Yuri N. Sedunov <aris@altlinux.org> 2.58.0-alt1
- 2.58.0

* Fri Aug 17 2018 Yuri N. Sedunov <aris@altlinux.org> 2.56.2-alt1
- 2.56.2

* Sat Apr 07 2018 Yuri N. Sedunov <aris@altlinux.org> 2.56.1-alt1
- 2.56.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 2.56.0-alt1
- 2.56.0

* Tue Jan 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.54.3-alt1
- 2.54.3

* Sat Oct 28 2017 Yuri N. Sedunov <aris@altlinux.org> 2.54.2-alt1
- 2.54.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.54.1-alt1
- 2.54.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.54.0-alt1
- 2.54.0

* Thu Jun 22 2017 Yuri N. Sedunov <aris@altlinux.org> 2.52.3-alt1
- 2.52.3

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.52.2-alt1
- 2.52.2

* Sat Apr 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.52.1-alt1
- 2.52.1

* Sun Mar 19 2017 Yuri N. Sedunov <aris@altlinux.org> 2.52.0-alt1
- 2.52.0

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.50.3-alt1
- 2.50.3

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 2.50.2-alt1
- 2.50.2

* Sat Oct 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.50.1-alt2
- gio/gdbusaddress.c: s|var/run/dbus|/run/dbus| (ALT #32444, #32642)

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 2.50.1-alt1
- 2.50.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 2.50.0-alt1
- 2.50.0

* Thu Aug 18 2016 Yuri N. Sedunov <aris@altlinux.org> 2.48.2-alt1
- 2.48.2

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 2.48.1-alt1
- 2.48.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 2.48.0-alt1
- 2.48.0

* Sat Nov 07 2015 Yuri N. Sedunov <aris@altlinux.org> 2.46.2-alt1
- 2.46.2

* Sat Oct 24 2015 Yuri N. Sedunov <aris@altlinux.org> 2.46.1-alt2
- 2.46.1_24366e15 (fixed BGO ##755609, 754994, 754983...)

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 2.46.1-alt1
- 2.46.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.46.0-alt1
- 2.46.0

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 2.44.1-alt1
- 2.44.1

* Mon Apr 06 2015 Yuri N. Sedunov <aris@altlinux.org> 2.44.0-alt1.1
- updated to 2-44_12dd1cc9f3

* Tue Mar 24 2015 Yuri N. Sedunov <aris@altlinux.org> 2.44.0-alt1
- 2.44.0

* Thu Feb 26 2015 Yuri N. Sedunov <aris@altlinux.org> 2.42.2-alt1
- 2.42.2

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 2.42.1-alt1
- 2.42.1

* Thu Oct 02 2014 Yuri N. Sedunov <aris@altlinux.org> 2.42.0-alt2
- updated to 2-42_677fd20 (fixed BGO #728256, 736806, 737143..)

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 2.42.0-alt1
- 2.42.0

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 2.40.2-alt1
- 2.40.2

* Sat Sep 20 2014 Yuri N. Sedunov <aris@altlinux.org> 2.40.1-alt1
- 2.40.1 release

* Tue May 20 2014 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1.2
- updated to 321b827d6
- removed upstreamed glib-2.38-bgo-707298.patch

* Wed Apr 02 2014 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1.1
- updated to c7a661988e

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1
- 2.40.0

* Wed Jan 22 2014 Yuri N. Sedunov <aris@altlinux.org> 2.38.2-alt3
- applied patch for BGO #707298

* Thu Dec 12 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38.2-alt2
- added glibc-kernheaders to buildreqs
- installed tests

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38.2-alt1
- 2.38.2

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38.1-alt1
- 2.38.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt1
- 2.38.0
- optional systemtap support
- new optional -test subpackage

* Sun Jul 14 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.3-alt2
- fixed BGO 701560 from upstream

* Mon Jun 10 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.3-alt1
- 2.36.3

* Fri May 31 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.2-alt2
- fixed list of terminal in gio/gdesktopappinfo.c (ALT #29011)

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.2-alt1
- 2.36.2

* Mon Apr 29 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt3
- disabled patch11

* Sat Apr 27 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt2
- suppressed warnings about deprecated paths in schemas
- applied upstream patches related to BGO ##698716, 698081
  and ALT #28903

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt1
- 2.36.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 2.35.9-alt1
- 2.35.9

* Sat Jan 12 2013 Yuri N. Sedunov <aris@altlinux.org> 2.34.3-alt2
- fixed gtester (ldv@)

* Tue Nov 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.34.3-alt1
- 2.34.3

* Sat Nov 10 2012 Yuri N. Sedunov <aris@altlinux.org> 2.34.2-alt1
- 2.34.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.34.1-alt1
- 2.34.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Mon Jul 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.4-alt1
- 2.32.4

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3
- built with intenrnal PCRE as recommended
- disabled optional fam monitor support

* Mon May 07 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Sat Mar 24 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.31.22-alt1
- 2.31.22
- removed g_unix_resolver_get_type from gio-compat.lds

* Mon Mar 12 2012 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Sat Nov 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.30.1-alt2.1
- Rebuild with Python-2.7
- bootstrap without python-module-pygobject python-module-dbus

* Wed Oct 19 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt2
- fixed https://bugzilla.gnome.org/show_bug.cgi?id=661896

* Sat Oct 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Jun 06 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.8-alt1
- 2.28.8

* Sat May 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.7-alt1
- 2.28.7

* Thu Apr 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.6-alt1
- 2.28.6

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.5-alt2
- glib2-devel requires rpm-build-gir >= 0.5

* Fri Apr 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.5-alt1
- 2.28.5
- %%check section

* Mon Mar 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt1
- 2.28.4

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Mon Mar 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Fri Feb 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Feb 09 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 2.26.2-alt3
- added ld scripts to mitigate symbol versioning issues

* Mon Feb 07 2011 Alexey Tourbin <at@altlinux.ru> 2.26.2-alt2
- rebuilt for debuginfo
- disabled symbol versioning

* Mon Dec 20 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2 current snapshot

* Sun Nov 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Sat Oct 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt3
- %%_datadir/glib-2.0/schemas/ moved to the libgio subpackage
- gsettings-desktop-schemas rqs moved to libgio

* Thu Oct 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- %%_datadir/glib-2.0/schemas/ moved to the main glib2 subpackage
- gsettings-desktop-schemas added to rqs

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Sun Sep 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.25.17-alt1
- 2.25.17

* Sun Aug 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2

* Sat Jul 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.25.12-alt1
- 2.25.12

* Thu Jun 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.25.10-alt1
- 2.25.10
- updated version scripts for GLIB_2.25.10 and GIO_2.25.10

* Mon May 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Mar 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Mar 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.6-alt1
- 2.23.6
- updated version scripts for GLIB_2.23.6

* Tue Mar 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.5-alt1
- 2.22.5

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.5-alt1
- 2.23.5
- updated version scripts for GLIB_2.23.5

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.4-alt1
- 2.23.4
- updated version scripts for GLIB_2.23.4 and GIO_2.23.4

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.3-alt1
- 2.23.3

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.2-alt1
- 2.23.2

* Thu Dec 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.23.1-alt1
- 2.23.1

* Tue Dec 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.22.3-alt1
- 2.22.3

* Thu Oct 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.22.2-alt1
- 2.22.2

* Wed Sep 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.22.1-alt1
- 2.22.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.21.6-alt1
- 2.21.6

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.21.5-alt1
- 2.21.5 
- updated version scripts for GIO_2.21.5

* Mon Aug 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.21.4-alt1
- 2.21.4
- updated version scripts for GLIB_2.21.4 and GIO_2.21.4

* Sat Jun 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.4-alt1
- 2.20.4

* Sat May 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.3-alt1
- 2.20.3

* Sun May 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.2-alt1
- 2.20.2

* Fri Apr 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.1-alt1
- 2.20.1

* Fri Mar 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Mon Mar 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.10-alt1
- 2.19.10

* Wed Feb 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.8-alt1
- 2.19.8

* Tue Feb 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.6-alt1
- 2.19.6
- updated version script for GIO_2.19.6

* Tue Jan 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.5-alt1
- 2.19.5
- drop upstreamed patches
- updated version scripts for GLIB_2.19.5, GIO_2.19.5

* Sat Jan 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.18.4-alt1
- 2.18.4

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.18.3-alt1
- 2.18.3
- drop upstreamed patches
- remove obsolete ldconfig from %%post{,un}

* Sun Nov 09 2008 Yuri N. Sedunov <aris@altlinux.org> 2.18.2-alt2
- fix gnome bugs ##528670, 528320

* Fri Oct 17 2008 Yuri N. Sedunov <aris@altlinux.org> 2.18.2-alt1
- 2.18.2

* Thu Sep 18 2008 Alexey Tourbin <at@altlinux.ru> 2.18.1-alt1
- 2.16.6 -> 2.18.1
- updated version scripts for shared libraries (GLIB_2.18, GIO_2.18)
- only libglib-2.0.so.0 must be relocated from /usr/lib to /lib
- renamed /etc/profile.d/libglib2.sh back to glib2.sh (in setup-2.2.8-alt1,
  lang.sh was renamed to 0lang.sh, so now it goes before glib2.sh)
- glib2: split glib2-locales subpackage (noarch)
- glib2-devel-doc: renamed to glib2-doc, split libgio-doc (noarch)
- glib2-devel-static: packaged only libglib-2.0.a, libgobject-2.0.a,
  and libgthread-2.0.a (libgmodule-2.0 and libgio-2.0 use dynamic loading,
  and should not be used for static linking)

* Sat Sep 13 2008 Yuri N. Sedunov <aris@altlinux.org> 2.16.6-alt1
- new bugfix release
- build with system pcre, always enable regex (at@)

* Sun Jul 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.16.5-alt1
- new version
- temporarily disabled gtk-doc due to gnome bug #543855

* Wed Jul 02 2008 Yuri N. Sedunov <aris@altlinux.org> 2.16.4-alt1
- new version
- libgio reqiures %%name = %%version-%%release
- small fix in gtester-report

* Wed Apr 09 2008 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version (2.16.3)

* Tue Mar 11 2008 Alexey Rusakov <ktirf@altlinux.org> 2.16.1-alt1
- New version (2.16.1).

* Sat Mar 01 2008 Alexey Rusakov <ktirf@altlinux.org> 2.15.6-alt1
- New version (2.15.6).
- Updated dependencies and version scripts.
- New subpackages, libgio and libgio-devel.

* Thu Jan 10 2008 Alexey Rusakov <ktirf@altlinux.org> 2.14.5-alt1
- New version (2.14.5).

* Sat Dec 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.4-alt1
- new version (2.14.4)

* Thu Nov 08 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.3-alt1
- New version (2.14.3).
- Added -Denable-regex=true switch.
- Enforce usage of the system supplied printf (just to make sure).

* Tue Oct 02 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.1-alt4
- fixed files in -devel moved accidentally to /lib, too.

* Mon Oct 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.1-alt3
- made the splitting optional, disabled by default (since it brings some
  troubles if glib2 is being installed as a dependency).

* Sat Sep 29 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.1-alt2
- split out glib2-core from glib2 and moved its contents to /lib, since
  system programs depend on glib2 (ALT Bug #12936).

* Mon Sep 17 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.1-alt1
- new version (2.14.1)

* Mon Aug 27 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.0-alt1
- new version
- updated symver scripts
- removed %%__ macros
- use macros from rpm-build-gnome and rpm-build-licenses

* Fri Jul 27 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.13-alt1
- new version 2.12.13 (with rpmrb script)

* Sun May 20 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.12-alt1
- new version (2.12.12)

* Sun Jan 21 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.9-alt1
- new version 2.12.9 (with rpmrb script)

* Fri Jan 05 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.7-alt1
- new version 2.12.7 (with rpmrb script)

* Tue Oct 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.4-alt2
- enabled building static libraries.
- fixed typos in comments.

* Tue Oct 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.4-alt1
- new version 2.12.4 (with rpmrb script)

* Thu Aug 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.2-alt1
- new version 2.12.2 (with rpmrb script)

* Tue Jul 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version 2.12.1 (with rpmrb script)

* Mon Jul 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- new version (2.12.0)

* Sun May 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.3-alt1
- new version 2.10.3 (with rpmrb script)

* Sat Apr 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.2-alt1
- new version (2.10.2)

* Thu Mar 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.1-alt1
- new version (2.10.1)

* Sun Feb 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.9.6-alt1
- new version
- fixed bug #9005

* Sun Jan 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.9.5-alt1
- new version

* Thu Jan 26 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.9.4-alt1
- new version

* Sat Jan 21 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.6-alt1
- new version

* Sat Jan 21 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.5-alt2
- replaced pkgconfig with pkg-config.

* Wed Jan 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.5-alt1
- new version

* Wed Nov 16 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.4-alt1
- new version

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.3-alt1
- new version

* Tue Sep 27 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 2.8.1-alt2
- NMU: introduced GLIB_2.8 ABI interface for new functions in
  libglib-2.0.so.0 and libgobject-2.0.so.0

* Sun Aug 28 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.1-alt1
- 2.8.1
- Renamed scripts for profile.d so that they go after lang.* scripts
  (thanks to Vitaly Lipatov).

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Wed Apr 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Mon Feb 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3
- set G_FILENAME_ENCODING using natspec.

* Fri Feb 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sat Jan 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Thu Dec 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Fri Dec 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.7-alt1
- 2.5.7
- documentation moved to devel-doc subpackage.

* Tue Nov 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt2
- fix #5567 (thanks lav@).

* Sat Nov 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt1
- 2.5.6

* Thu Nov 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Mon Sep 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Mon Aug 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.6-alt1
- 2.4.6

* Sat Jul 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.5-alt1
- 2.4.5
- #4873 fixed in upstream.

* Mon Jul 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4-alt1.1
- fix g_unescape_uri_string. Thanks lav@ (close #4873).

* Sun Jul 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Sat Jun 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Fri Apr 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Mar 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Tue Mar 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Fri Jan 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Wed Dec 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt2
- do not package .la files.
- devel-static subpackage is optional now.

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Mon Jun 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Mon Feb 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Sat Dec 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Thu Dec 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Wed Nov 27 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-alt2
- remove deps on csh by fixing headers of /etc/profile.d files

* Tue Nov 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Sun Sep 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt2
- glib2.{sh,csh) added (RH).

* Sat Sep 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt1
- 2.0.6
- fixed-ltmain.sh removed, not needed more.
- post/postun scripts improved.
- gcc-3.2 used.

* Fri Jun 14 2002 Igor Androsov <blake@altlinux.ru> 2.0.4-alt1
- New release

* Wed May 29 2002 Igor Androsov <blake@altlinux.ru> 2.0.3-alt2
- Return removed in 2.0.1-alt2 fixed-ltmain.sh - fixed not installing
  gobject, module, gthread if host where building not have installed
  glib2-devel

* Tue May 28 2002 Igor Androsov <blake@altlinux.ru> 2.0.3-alt1
- New release

* Thu May 23 2002 Igor Androsov <blake@altlinux.ru> 2.0.1-alt2
- clean spec
- added /usr/share/glib-2.0/*

* Sun Mar 31 2002 AEN <aen@logic.ru> 2.0.1-alt1
- new verson

* Wed Mar 27 2002 AEN <aen@logic.ru> 2.0.0-alt1
- release

* Tue Feb 05 2002 AEN <aen@logic.ru> 1.3.12.90-alt2
- .so links moved to devel

* Wed Jan 09 2002 AEN <aen@logic.ru> 1.3.12.90 -alt1
- sources from Rawide

* Wed Oct 17 2001 AEN <aen@logic.ru> 1.3.9-alt1
- new version

* Tue Sep 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3.7-alt1
- Renamed to glib2.

* Fri Sep 21 2001 Stanislav Ievlev <inger@altlinux.ru> 1.3.7-alt1
- 1.3.7

* Fri Jun 15 2001 AEN <aen@logic.ru> 1.3.6-alt1
- new version
- BuildReq added
- Make patch
* Thu May 31 2001 Stanislav Ievlev <inger@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Fri Apr 20 2001 Stanislav Ievlev <inger@altlinux.ru> 1.3.4-alt1
- Up to 1.3.4. Cleanup spec, librification, statification

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation

* Mon Nov 20 2000 DindinX <odin@mandrakesoft.com> 1.3.2-3mdk
- redo my patch to best fit glib-1.3.2
- move %%doc to -devel

* Mon Nov 20 2000 Daouda Lo <daouda@mandrakesoft.com> 1.3.2-2mdk
- regenerate Dindinx's patch.

* Sat Nov 18 2000 Daouda Lo <daouda@mandrakesoft.com> 1.3.2-1mdk
- release

* Wed Nov 15 2000 DindinX <odin@mandrakesoft.com> 1.3.1-1mdk
- version 1.3.1 (first pre2)

